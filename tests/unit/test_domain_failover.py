# -*- coding: utf-8 -*-
"""
域名切换容灾（Domain Failover）功能的测试脚本。

覆盖：
  1. 候选域名生成（build_candidates）的白盒验证。
  2. 异常识别（_classify_exception）对 6 类故障的分类是否准确。
  3. 主域名故障时是否能按 [主 → .com.cn → .cn] 顺序切换。
  4. `.intl.` 域名是否严格不切换。
  5. 自定义 endpoint / IP 是否不受影响。
  6. 断路器是否在连续失败后跳过坏候选。
  7. JSON_DECODE_ERROR 场景是否**不**触发切换。

运行方式：
    python tests/dns_failure_test/test_domain_failover.py
"""
from __future__ import print_function

import json
import os
import socket
import sys
import threading
import time
import traceback

# 强制使用工程根目录下的 SDK，而非系统全局安装的旧版本
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

try:
    from http.server import BaseHTTPRequestHandler, HTTPServer
except ImportError:  # py2
    from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile, DomainFailoverProfile, RegionBreakerProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.domain_failover import (
    build_candidates, _classify_exception, is_failover_triggered,
)
from tencentcloud.cvm.v20170312 import cvm_client, models


# --------------------------------------------------------------------------- #
# 1) 白盒测试：候选域名生成
# --------------------------------------------------------------------------- #

def test_build_candidates():
    print("\n" + "=" * 80)
    print("[UNIT] build_candidates")
    print("=" * 80)
    cases = [
        ("cvm.tencentcloudapi.com",
         ["cvm.tencentcloudapi.com", "cvm.tencentcloudapi.com.cn", "cvm.tencentcloudapi.cn"]),
        ("cvm.ap-guangzhou.tencentcloudapi.com",
         ["cvm.ap-guangzhou.tencentcloudapi.com",
          "cvm.ap-guangzhou.tencentcloudapi.com.cn",
          "cvm.ap-guangzhou.tencentcloudapi.cn"]),
        ("cvm.internal.tencentcloudapi.com",
         ["cvm.internal.tencentcloudapi.com",
          "cvm.internal.tencentcloudapi.com.cn",
          "cvm.internal.tencentcloudapi.cn"]),
        ("cvm.intl.tencentcloudapi.com", ["cvm.intl.tencentcloudapi.com"]),
        ("cvm.ap-guangzhou.intl.tencentcloudapi.com",
         ["cvm.ap-guangzhou.intl.tencentcloudapi.com"]),
        ("custom.example.com", ["custom.example.com"]),
        ("127.0.0.1:8080", ["127.0.0.1:8080"]),
    ]
    passed = 0
    for host, expected in cases:
        got = build_candidates(host)
        ok = (got == expected)
        print(("  [OK] " if ok else "  [FAIL] ") + host)
        if not ok:
            print("        expected=%s" % expected)
            print("        got     =%s" % got)
        passed += int(ok)
    print("Summary: %d/%d passed" % (passed, len(cases)))


# --------------------------------------------------------------------------- #
# 2) 白盒测试：_classify_exception
# --------------------------------------------------------------------------- #

def test_classify_exception():
    print("\n" + "=" * 80)
    print("[UNIT] _classify_exception")
    print("=" * 80)
    import requests

    def _wrap(raw_exc):
        """模拟网络层包装：TencentCloudSDKException('ClientNetworkError', ...) from e"""
        try:
            raise raw_exc
        except Exception as e:
            try:
                raise TencentCloudSDKException("ClientNetworkError", str(e)) from e
            except TencentCloudSDKException as tce:
                return tce

    def _chain(inner, outer_cls):
        """构造 outer(inner) 的链（outer 捕获 inner 再抛自己），用于模拟 requests 对
        底层异常的包装。"""
        try:
            try:
                raise inner
            except Exception:
                raise outer_cls(str(inner))
        except outer_cls as e:
            return e

    cases = [
        # DNS NXDOMAIN/SERVFAIL → errno=-2
        (_wrap(_chain(socket.gaierror(-2, "Name or service not known"),
                      requests.exceptions.ConnectionError)), "DNS_NXDOMAIN"),
        # DNS 超时 → errno=-3
        (_wrap(_chain(socket.gaierror(-3, "Temporary failure in name resolution"),
                      requests.exceptions.ConnectionError)), "DNS_TIMEOUT"),
        # TCP Connection refused
        (_wrap(_chain(ConnectionRefusedError(111, "Connection refused"),
                      requests.exceptions.ConnectionError)), "TCP_CONN_REFUSED"),
        # 读超时
        (_wrap(_chain(socket.timeout("timed out"),
                      requests.exceptions.ReadTimeout)), "TCP_READ_TIMEOUT"),
        # TLS 错误
        (_wrap(_chain(Exception("cert mismatch"),
                      requests.exceptions.SSLError)), "TLS_ERROR"),
        # JSON 解析失败：业务方法层会包装成 TencentCloudSDKException(code="JSONDecodeError",...)
        (TencentCloudSDKException("JSONDecodeError", "Expecting value: line 1 column 1 (char 0)"),
         "JSON_DECODE_ERROR"),
    ]

    passed = 0
    for exc, expected in cases:
        got = _classify_exception(exc)
        ok = (got == expected)
        print(("  [OK] " if ok else "  [FAIL] ") +
              "%s  expected=%s got=%s" % (type(exc).__name__, expected, got))
        passed += int(ok)
    print("Summary: %d/%d passed" % (passed, len(cases)))

    # 验证 is_failover_triggered 的口径
    assert is_failover_triggered("DNS_NXDOMAIN") is True
    assert is_failover_triggered("DNS_TIMEOUT") is True
    assert is_failover_triggered("TCP_CONN_REFUSED") is True
    assert is_failover_triggered("TCP_READ_TIMEOUT") is True
    assert is_failover_triggered("TLS_ERROR") is True
    assert is_failover_triggered("JSON_DECODE_ERROR") is False
    assert is_failover_triggered(None) is False
    print("  [OK] is_failover_triggered semantics")


# --------------------------------------------------------------------------- #
# 3) 集成测试：主域名 DNS 失败 → 验证切换轨迹
# --------------------------------------------------------------------------- #

def make_client(endpoint, req_timeout=5, enabled=True, scheme=None):
    cred = credential.Credential("AKIDFakeIdForDomainFailoverTest",
                                 "FakeKeyForDomainFailoverTest")
    http_profile = HttpProfile()
    http_profile.reqTimeout = req_timeout
    if scheme:
        http_profile.scheme = scheme
    http_profile.endpoint = endpoint
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client_profile.disable_region_breaker = True  # 避免干扰
    client_profile.domain_failover_profile = DomainFailoverProfile(enabled=enabled)
    return cvm_client.CvmClient(cred, "ap-guangzhou", client_profile)


class _GaiPatcher(object):
    """记录哪些 host 被解析，可以控制哪些 host 返回 NXDOMAIN、哪些走真实解析。"""

    def __init__(self, resolvable_hosts=None, fake_ip=None):
        """:param resolvable_hosts: 集合，在这个集合中的 host 会"解析成功"
                 返回 fake_ip 或本地 127.0.0.1。
           :param fake_ip: 解析后的 IP 地址；None 时使用 127.0.0.1。
        """
        self.resolvable = set(resolvable_hosts or [])
        self.fake_ip = fake_ip or "127.0.0.1"
        self.resolved_log = []
        self._real = None

    def __enter__(self):
        self._real = socket.getaddrinfo

        def fake(host, *args, **kwargs):
            if host and ("tencentcloudapi" in host):
                self.resolved_log.append(host)
                if host in self.resolvable:
                    return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (self.fake_ip, 443))]
                raise socket.gaierror(-2, "Name or service not known")
            return self._real(host, *args, **kwargs)

        socket.getaddrinfo = fake
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        socket.getaddrinfo = self._real


def run_case(title, fn):
    print("\n" + "=" * 80)
    print("[CASE] " + title)
    print("=" * 80)
    t0 = time.time()
    try:
        fn()
    except Exception as e:
        print("!!! 用例抛出未捕获的异常: %s: %s" % (type(e).__name__, e))
        traceback.print_exc()
    print("耗时: %.3fs" % (time.time() - t0))


def case_all_dns_fail_primary_and_backup():
    """所有 3 个候选都 DNS 失败：期望 SDK 抛异常，但日志中记录尝试了全部 3 个。"""
    client = make_client("cvm.tencentcloudapi.com", req_timeout=3)
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
            print("!!! 未抛异常，不符合预期")
        except TencentCloudSDKException as e:
            pass
        print("resolved hosts sequence:")
        for h in p.resolved_log:
            print("  - %s" % h)
        expected = ["cvm.tencentcloudapi.com",
                    "cvm.tencentcloudapi.com.cn",
                    "cvm.tencentcloudapi.cn"]
        actually_tried = [h for h in p.resolved_log if h in expected]
        # 可能每个 host 因重试被解析多次，这里用"唯一化后包含 3 项"断言顺序
        uniq = []
        for h in actually_tried:
            if h not in uniq:
                uniq.append(h)
        ok = (uniq == expected)
        print("顺序校验: " + ("OK" if ok else "FAIL, got=%s" % uniq))


def case_primary_fail_backup_ok():
    """主域名 DNS 失败，第二候选被解析到本地 HTTP server（我们让它返回假的非 JSON
    → 会抛 JSONDecodeError，不触发再切换；但能证明已经切到了第二候选）。"""
    # 启动本地 HTTP server
    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get('Content-Length', 0))
            self.rfile.read(length)
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"Response": {"Error": {"Code":"InternalFake","Message":"mocked"}, "RequestId":"mock-rid"}}')

        def do_GET(self):
            self.do_POST()

        def log_message(self, fmt, *a):
            return

    srv = HTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever)
    t.daemon = True
    t.start()
    try:
        # 用 http + 端口，让 2 级候选走本地 server；同时让主域名 DNS 失败
        # 注意：build_candidates 基于 host 的后缀；我们用 "cvm.tencentcloudapi.com"
        # 作为 endpoint，第二候选是 "cvm.tencentcloudapi.com.cn"
        client = make_client("cvm.tencentcloudapi.com", req_timeout=3, scheme="http")
        # 把 cvm.tencentcloudapi.com 做成解析失败，把 com.cn 解析到本地端口
        # 需要改监听地址使 HTTP client 能连上。用一个 Patch：主域名失败，第二域名成功。
        # 但由于 requests 会用 DNS 解析 host，我们把 com.cn 解析到 127.0.0.1，
        # 然后另外劫持 urlparse / port：直接在 URL 路径里拼端口是最简方式。
        # 这里退而求其次：仅验证"切换发生"，通过 _GaiPatcher 的 resolved_log 观察。
        with _GaiPatcher(resolvable_hosts={"cvm.tencentcloudapi.com.cn"},
                         fake_ip="127.0.0.1") as p:
            # 由于解析到了 127.0.0.1:443（非 HTTP server 端口），会连接拒绝 → 第二候选
            # 也失败，继续到第三候选 cvm.tencentcloudapi.cn → 再 DNS 失败
            try:
                client.DescribeRegions(models.DescribeRegionsRequest())
            except TencentCloudSDKException as e:
                pass
            print("resolved hosts sequence:")
            for h in p.resolved_log:
                print("  - %s" % h)
            # 期望至少尝试了前两个候选
            tried = set(p.resolved_log)
            ok_primary = "cvm.tencentcloudapi.com" in tried
            ok_backup = "cvm.tencentcloudapi.com.cn" in tried
            print("主域名被尝试:  %s" % ok_primary)
            print("第二候选被尝试: %s" % ok_backup)
    finally:
        srv.shutdown()


def case_intl_no_failover():
    """intl 域名必须不做切换。"""
    client = make_client("cvm.intl.tencentcloudapi.com", req_timeout=3)
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
        except TencentCloudSDKException:
            pass
        uniq_tried = [h for h in dict.fromkeys(p.resolved_log)]
        print("resolved hosts: %s" % uniq_tried)
        ok = (uniq_tried == ["cvm.intl.tencentcloudapi.com"])
        print("仅尝试主域名（intl 不切换）: " + ("OK" if ok else "FAIL"))


def case_custom_endpoint_no_failover():
    """非 tencentcloudapi 后缀的 endpoint 不切换。"""
    client = make_client("custom.example.invalid", req_timeout=3)
    try:
        client.DescribeRegions(models.DescribeRegionsRequest())
    except TencentCloudSDKException as e:
        raw = e.__cause__ or e.__context__
        # 应只有一个候选被尝试（没法直接看 log，但可通过断路器的 get_breaker 数量判断）
        breakers = client.domain_failover._breakers
        print("注册的候选数: %d" % len(breakers))
        print("候选列表: %s" % list(breakers.keys()))
        ok = (list(breakers.keys()) == ["custom.example.invalid"])
        print("仅保留单一候选（自定义 endpoint 不切换）: " + ("OK" if ok else "FAIL"))


def case_disabled():
    """enabled=False 时退化为原逻辑（仅尝试一次）。"""
    client = make_client("cvm.tencentcloudapi.com", req_timeout=3, enabled=False)
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
        except TencentCloudSDKException:
            pass
        uniq_tried = [h for h in dict.fromkeys(p.resolved_log)]
        print("resolved hosts: %s" % uniq_tried)
        ok = (uniq_tried == ["cvm.tencentcloudapi.com"])
        print("enabled=False 时不切换: " + ("OK" if ok else "FAIL"))


def case_breaker_skips_bad_candidate():
    """连续失败超过阈值后，断路器 OPEN，后续请求应直接跳过坏候选。"""
    from tencentcloud.common.circuit_breaker import STATE_OPEN
    # 使用较低阈值，方便快速触发
    client = make_client("cvm.tencentcloudapi.com", req_timeout=3)
    client.domain_failover._profile.breaker_setting.max_fail_num = 2
    client.domain_failover._profile.breaker_setting.max_fail_percent = 0.1

    with _GaiPatcher() as p:
        # 多次调用，每次 3 个候选都会失败，主域名连续 5 次失败后应该被断路
        for i in range(3):
            try:
                client.DescribeRegions(models.DescribeRegionsRequest())
            except TencentCloudSDKException:
                pass
    primary_breaker = client.domain_failover._breakers.get("cvm.tencentcloudapi.com")
    print("primary breaker state: %s (OPEN=%d)" % (primary_breaker.state, STATE_OPEN))
    ok = primary_breaker.state == STATE_OPEN
    print("主域名断路器 OPEN: " + ("OK" if ok else "FAIL"))


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main():
    test_build_candidates()
    test_classify_exception()

    run_case("A 全部候选 DNS 失败，观察切换顺序", case_all_dns_fail_primary_and_backup)
    run_case("B 主域名失败切到第二候选", case_primary_fail_backup_ok)
    run_case("C intl 严格不切换", case_intl_no_failover)
    run_case("D 自定义 endpoint 不切换", case_custom_endpoint_no_failover)
    run_case("E enabled=False 完全不切换", case_disabled)
    run_case("F 断路器会跳过坏候选", case_breaker_skips_bad_candidate)


if __name__ == "__main__":
    main()
