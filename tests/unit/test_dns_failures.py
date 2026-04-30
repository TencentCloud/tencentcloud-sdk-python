# -*- coding: utf-8 -*-
"""
DNS 故障场景对 Tencent Cloud Python SDK 异常表现的测试脚本

参考文档：
  https://iwiki.woa.com/p/4019996855 《2.3 SDK 视角：DNS 故障的异常表现》

本脚本针对文档中列出的 A/B/C 三大类、共 11 种 DNS 故障场景，构造等价的本地/网络
模拟条件，通过调用 SDK 的 CVM.DescribeRegions 接口触发异常，并打印：
  1) 最外层 SDK 抛出的 TencentCloudSDKException（code + message）
  2) SDK 捕获到的"原始异常"的真实类型与 repr（通过 PEP 3134 标准异常链
     e.__cause__ 获取；若该层未用 ``raise ... from``，则回退到 e.__context__）
  3) 耗时，以辅助判断故障类型

运行方式（不依赖真实腾讯云账号，SecretId/SecretKey 可任意填，域名错误时请求根本
不会到达签名校验阶段）：
    python tests/dns_failure_test/test_dns_failures.py
"""
from __future__ import print_function

import os
import socket
import sys
import time
import traceback

# 强制使用工程根目录下的 SDK
_PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
if _PROJECT_ROOT not in sys.path:
    sys.path.insert(0, _PROJECT_ROOT)

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models


def make_client(endpoint=None, req_timeout=10, disable_region_breaker=True, scheme=None):
    cred = credential.Credential("AKIDFakeIdForDnsTest", "FakeKeyForDnsTest")
    http_profile = HttpProfile()
    http_profile.reqTimeout = req_timeout
    if scheme:
        http_profile.scheme = scheme
    if endpoint:
        http_profile.endpoint = endpoint
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client_profile.disable_region_breaker = disable_region_breaker
    return cvm_client.CvmClient(cred, "ap-guangzhou", client_profile)


def run_case(title, case_fn):
    print("\n" + "=" * 80)
    print("[CASE] " + title)
    print("=" * 80)
    t0 = time.time()
    try:
        case_fn()
        print("!!! 本次调用没有触发异常，用例不符合预期 !!!")
    except TencentCloudSDKException as e:
        cost = time.time() - t0
        # 通过 Python 标准异常链获取原始异常：优先 __cause__（raise ... from e），
        # 回退 __context__（except 块内裸 raise 时 CPython 自动记录）。
        raw = e.__cause__ or e.__context__
        print("SDK Exception code    : %s" % e.code)
        print("SDK Exception message : %s" % e.message)
        if raw is not None:
            raw_type = "%s.%s" % (type(raw).__module__, type(raw).__name__)
            print("Raw exception type    : %s" % raw_type)
            print("Raw exception repr    : %r" % (raw,))
            # 进一步遍历 __cause__/__context__ 链，展示 requests → urllib3 → socket 的完整传递
            chain = []
            cur = raw
            seen = set()
            while cur is not None and id(cur) not in seen:
                seen.add(id(cur))
                chain.append("%s.%s: %s" % (type(cur).__module__, type(cur).__name__, cur))
                cur = getattr(cur, "__cause__", None) or getattr(cur, "__context__", None)
            if len(chain) > 1:
                print("Raw exception chain   :")
                for i, line in enumerate(chain):
                    print("  [%d] %s" % (i, line))
        else:
            print("Raw exception         : <none> (无 __cause__/__context__)")
        print("耗时                   : %.3fs" % cost)
    except Exception as e:
        cost = time.time() - t0
        print("未被 SDK 包装的异常: %s: %s (%.3fs)" % (type(e).__name__, e, cost))
        traceback.print_exc()


def call_describe_regions(client):
    req = models.DescribeRegionsRequest()
    client.DescribeRegions(req)


# ========== A 类：DNS 解析失败 ==========

def case_a_operator_nxdomain():
    client = make_client(endpoint="cvm.definitely-not-exist-nxdomain.invalid")
    call_describe_regions(client)


def _patch_gai_with(fn):
    import socket as _socket
    real_gai = _socket.getaddrinfo

    def wrapper(host, *args, **kwargs):
        if host and ("tencentcloudapi.com" in host or host.startswith("cvm.")):
            return fn(host, *args, **kwargs)
        return real_gai(host, *args, **kwargs)

    _socket.getaddrinfo = wrapper
    return real_gai


def _restore_gai(real_gai):
    socket.getaddrinfo = real_gai


def case_a_public_dns_timeout():
    def fake(host, *args, **kwargs):
        time.sleep(2)
        raise socket.gaierror(-3, "Temporary failure in name resolution")
    real = _patch_gai_with(fake)
    try:
        client = make_client(req_timeout=10)
        call_describe_regions(client)
    finally:
        _restore_gai(real)


def case_a_root_server_ddos():
    case_a_public_dns_timeout()


def case_a_tld_ns_tampered():
    case_a_operator_nxdomain()


def case_a_authoritative_dns_ddos():
    def fake(host, *args, **kwargs):
        raise socket.gaierror(-2, "Name or service not known")
    real = _patch_gai_with(fake)
    try:
        client = make_client(req_timeout=10)
        call_describe_regions(client)
    finally:
        _restore_gai(real)


def case_a_gslb_misconfig():
    case_a_authoritative_dns_ddos()


# ========== B 类：连接层异常 ==========

def case_b_operator_return_zero_ip():
    def fake(host, *args, **kwargs):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ("0.0.0.0", 443))]
    real = _patch_gai_with(fake)
    try:
        client = make_client(req_timeout=5)
        call_describe_regions(client)
    finally:
        _restore_gai(real)


def case_b_hijack_port_closed():
    def fake(host, *args, **kwargs):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ("127.0.0.1", 1))]
    real = _patch_gai_with(fake)
    try:
        client = make_client(req_timeout=5)
        call_describe_regions(client)
    finally:
        _restore_gai(real)


def case_b_hijack_no_response():
    def fake(host, *args, **kwargs):
        # 192.0.2.1 是 RFC 5737 TEST-NET-1 保留地址，公网不可路由
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', ("192.0.2.1", 443))]
    real = _patch_gai_with(fake)
    try:
        client = make_client(req_timeout=3)
        call_describe_regions(client)
    finally:
        _restore_gai(real)


# ========== C 类：应用层异常 ==========

def case_c_hijack_tls_mismatch():
    try:
        baidu_ip = socket.gethostbyname("www.baidu.com")
    except Exception:
        print("[SKIP] 无法解析 www.baidu.com，跳过此用例")
        return

    def fake(host, *args, **kwargs):
        return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (baidu_ip, 443))]
    real = _patch_gai_with(fake)
    try:
        client = make_client(req_timeout=10)
        call_describe_regions(client)
    finally:
        _restore_gai(real)


def case_c_hijack_http_unexpected_body():
    import threading
    try:
        from http.server import BaseHTTPRequestHandler, HTTPServer
    except ImportError:
        from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

    class Handler(BaseHTTPRequestHandler):
        def do_POST(self):
            length = int(self.headers.get('Content-Length', 0))
            self.rfile.read(length)
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"hello world (not a tencent cloud api response)")

        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"hello world (not a tencent cloud api response)")

        def log_message(self, fmt, *a):
            return

    srv = HTTPServer(("127.0.0.1", 0), Handler)
    port = srv.server_address[1]
    t = threading.Thread(target=srv.serve_forever)
    t.daemon = True
    t.start()
    try:
        client = make_client(endpoint="127.0.0.1:%d" % port, scheme="http",
                             req_timeout=5)
        call_describe_regions(client)
    finally:
        srv.shutdown()


CASES = [
    ("A-3 operator DNS blocking (NXDOMAIN)",   case_a_operator_nxdomain),
    ("A-3 public DNS down (timeout)",           case_a_public_dns_timeout),
    ("A-4 root server DDoS (timeout)",          case_a_root_server_ddos),
    ("A-5 TLD NS tampered (NXDOMAIN)",          case_a_tld_ns_tampered),
    ("A-6 authoritative DNS DDoS (SERVFAIL)",   case_a_authoritative_dns_ddos),
    ("A-6 GSLB misconfig (NXDOMAIN)",           case_a_gslb_misconfig),

    ("B-3 operator blocking (return 0.0.0.0)",  case_b_operator_return_zero_ip),
    ("B-5 hijack (port closed)",                case_b_hijack_port_closed),
    ("B-5 hijack (no response/timeout)",        case_b_hijack_no_response),

    ("C-5 hijack (HTTPS cert mismatch)",        case_c_hijack_tls_mismatch),
    ("C-5 hijack (HTTP 200 unexpected body)",   case_c_hijack_http_unexpected_body),
]


def main():
    for title, fn in CASES:
        run_case(title, fn)


if __name__ == "__main__":
    main()
