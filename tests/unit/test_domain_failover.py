# -*- coding: utf-8 -*-
"""
域名切换容灾（Domain Failover）功能的测试脚本。

本功能为 SDK 内部机制，对用户完全透明。本脚本通过白盒 + 集成两种方式验证：
  1. 候选域名生成（build_candidates）是否符合规则。
  2. 异常识别（_classify_exception）对 6 类故障的分类是否准确。
  3. 主域名故障时是否能按 [主 → .com.cn → .cn] 顺序切换。
  4. `.intl.` 域名是否严格不切换。
  5. 自定义 endpoint / IP 是否不受影响。
  6. 断路器是否在连续失败后跳过坏候选。

运行方式：
    python tests/dns_failure_test/test_domain_failover.py
"""
from __future__ import print_function

import os
import socket
import sys
import time
import traceback

# 强制使用工程根目录下的 SDK，而非系统全局安装的旧版本
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.domain_failover import (
    build_candidates, _classify_exception, is_failover_triggered,
)
from tencentcloud.cvm.v20170312 import cvm_client, models


# --------------------------------------------------------------------------- #
# 1) 白盒：候选域名生成
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
# 2) 白盒：_classify_exception
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
        """构造 outer(inner) 的链（outer 捕获 inner 再抛自己），模拟 requests 对
        底层异常的包装。"""
        try:
            try:
                raise inner
            except Exception:
                raise outer_cls(str(inner))
        except outer_cls as e:
            return e

    cases = [
        (_wrap(_chain(socket.gaierror(-2, "Name or service not known"),
                      requests.exceptions.ConnectionError)), "DNS_NXDOMAIN"),
        (_wrap(_chain(socket.gaierror(-3, "Temporary failure in name resolution"),
                      requests.exceptions.ConnectionError)), "DNS_TIMEOUT"),
        (_wrap(_chain(ConnectionRefusedError(111, "Connection refused"),
                      requests.exceptions.ConnectionError)), "TCP_CONN_REFUSED"),
        (_wrap(_chain(socket.timeout("timed out"),
                      requests.exceptions.ReadTimeout)), "TCP_READ_TIMEOUT"),
        (_wrap(_chain(Exception("cert mismatch"),
                      requests.exceptions.SSLError)), "TLS_ERROR"),
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
# 3) 集成：触发不同 host 的容灾路径
#    注：按新的"用户无感知"设计，ClientProfile 不再暴露 domain_failover 配置。
# --------------------------------------------------------------------------- #

def make_client(endpoint, req_timeout=3):
    cred = credential.Credential("AKIDFakeIdForDomainFailoverTest",
                                 "FakeKeyForDomainFailoverTest")
    http_profile = HttpProfile()
    http_profile.reqTimeout = req_timeout
    http_profile.endpoint = endpoint
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client_profile.disable_region_breaker = True   # 避免 region_breaker 干扰
    return cvm_client.CvmClient(cred, "ap-guangzhou", client_profile)


class _GaiPatcher(object):
    """Patch socket.getaddrinfo：
    - 落在 resolvable_hosts 中的 host 返回 fake_ip。
    - 其他 tencentcloudapi host 返回 NXDOMAIN。
    - 其他 host 走真实解析。
    """

    def __init__(self, resolvable_hosts=None, fake_ip=None):
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


def case_all_dns_fail():
    """所有 3 个候选都 DNS 失败：期望按序尝试 [com, com.cn, cn]。"""
    client = make_client("cvm.tencentcloudapi.com")
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
            print("!!! 未抛异常，不符合预期")
        except TencentCloudSDKException:
            pass
        print("resolved hosts sequence:")
        for h in p.resolved_log:
            print("  - %s" % h)
        expected = ["cvm.tencentcloudapi.com",
                    "cvm.tencentcloudapi.com.cn",
                    "cvm.tencentcloudapi.cn"]
        uniq = []
        for h in p.resolved_log:
            if h not in uniq:
                uniq.append(h)
        ok = (uniq == expected)
        print("顺序校验: " + ("OK" if ok else "FAIL, got=%s" % uniq))


def case_primary_fail_backup_tried():
    """主域名 DNS 失败，第二候选被"解析成功"但连接到 127.0.0.1:443（无服务）→
    连接被拒 → 切到第三候选 → 再 DNS 失败。
    目的是验证切换确实发生，而不是一遇到主域名失败就返回。"""
    client = make_client("cvm.tencentcloudapi.com")
    with _GaiPatcher(resolvable_hosts={"cvm.tencentcloudapi.com.cn"},
                     fake_ip="127.0.0.1") as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
        except TencentCloudSDKException:
            pass
        print("resolved hosts sequence:")
        for h in p.resolved_log:
            print("  - %s" % h)
        tried = set(p.resolved_log)
        ok_primary = "cvm.tencentcloudapi.com" in tried
        ok_backup = "cvm.tencentcloudapi.com.cn" in tried
        print("主域名被尝试:   %s" % ok_primary)
        print("第二候选被尝试: %s" % ok_backup)


def case_intl_no_failover():
    """intl 域名必须不做切换。"""
    client = make_client("cvm.intl.tencentcloudapi.com")
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
        except TencentCloudSDKException:
            pass
        uniq_tried = list(dict.fromkeys(p.resolved_log))
        print("resolved hosts: %s" % uniq_tried)
        ok = (uniq_tried == ["cvm.intl.tencentcloudapi.com"])
        print("仅尝试主域名（intl 不切换）: " + ("OK" if ok else "FAIL"))


def case_custom_endpoint_no_failover():
    """非 tencentcloudapi 后缀的 endpoint 不切换。"""
    client = make_client("custom.example.invalid")
    try:
        client.DescribeRegions(models.DescribeRegionsRequest())
    except TencentCloudSDKException:
        pass
    breakers = client.domain_failover._breakers
    print("注册的候选数: %d" % len(breakers))
    print("候选列表: %s" % list(breakers.keys()))
    ok = (list(breakers.keys()) == ["custom.example.invalid"])
    print("仅保留单一候选（自定义 endpoint 不切换）: " + ("OK" if ok else "FAIL"))


def case_breaker_skips_bad_candidate():
    """多次失败后，主域名断路器进入 OPEN 状态。"""
    from tencentcloud.common.circuit_breaker import STATE_OPEN
    client = make_client("cvm.tencentcloudapi.com")
    # 直接修改内部常量的副本阈值，方便快速触发（仅影响当前 client 的断路器）
    for br_name in ("cvm.tencentcloudapi.com", "cvm.tencentcloudapi.com.cn", "cvm.tencentcloudapi.cn"):
        br = client.domain_failover.get_breaker(br_name)
        br.breaker_setting.max_fail_num = 2
        br.breaker_setting.max_fail_percent = 0.1

    with _GaiPatcher():
        for _ in range(3):
            try:
                client.DescribeRegions(models.DescribeRegionsRequest())
            except TencentCloudSDKException:
                pass
    primary_breaker = client.domain_failover._breakers.get("cvm.tencentcloudapi.com")
    print("primary breaker state: %s (OPEN=%d)" % (primary_breaker.state, STATE_OPEN))
    ok = primary_breaker.state == STATE_OPEN
    print("主域名断路器 OPEN: " + ("OK" if ok else "FAIL"))


def case_no_profile_exposed():
    """回归：ClientProfile 不再暴露 domain_failover 相关字段/参数。"""
    cp = ClientProfile()
    assert not hasattr(cp, "domain_failover_profile"), \
        "ClientProfile should NOT expose domain_failover_profile"
    # 确保 DomainFailoverProfile 类也不从 client_profile 导出
    try:
        from tencentcloud.common.profile import client_profile as cp_mod
        assert not hasattr(cp_mod, "DomainFailoverProfile"), \
            "DomainFailoverProfile should NOT exist in client_profile module"
    except Exception as e:
        print("!!! %s" % e)
        raise
    print("ClientProfile 未暴露 domain_failover_profile: OK")
    print("client_profile 模块未导出 DomainFailoverProfile: OK")


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main():
    test_build_candidates()
    test_classify_exception()

    run_case("A 全部候选 DNS 失败，观察切换顺序", case_all_dns_fail)
    run_case("B 主域名失败切到第二候选", case_primary_fail_backup_tried)
    run_case("C intl 严格不切换", case_intl_no_failover)
    run_case("D 自定义 endpoint 不切换", case_custom_endpoint_no_failover)
    run_case("E 断路器会跳过坏候选", case_breaker_skips_bad_candidate)
    run_case("F Profile 未暴露容灾开关（用户无感知）", case_no_profile_exposed)


if __name__ == "__main__":
    main()
