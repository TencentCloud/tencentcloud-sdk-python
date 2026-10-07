# -*- coding: utf-8 -*-
"""
Test script for Domain Failover functionality.

This feature is an internal SDK mechanism, completely transparent to users. This script validates through white-box + integration approaches:
  1. Whether candidate domain generation (build_candidates) follows the rules.
  2. Whether exception classification (_classify_exception) accurately categorizes 6 types of failures.
  3. Whether primary domain failures trigger switching in the order [primary → .com.cn → .cn].
  4. Whether `.intl.` domains strictly do not switch.
  5. Whether custom endpoints / IPs are unaffected.
  6. Whether circuit breakers skip bad candidates after consecutive failures.

Run method:
    python tests/dns_failure_test/test_domain_failover.py
"""
from __future__ import print_function

import os
import socket
import sys
import time
import traceback

# Force using SDK from project root directory, not globally installed old version
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
# 1) White-box: Candidate domain generation
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
# 2) White-box: _classify_exception
# --------------------------------------------------------------------------- #

def test_classify_exception():
    print("\n" + "=" * 80)
    print("[UNIT] _classify_exception")
    print("=" * 80)
    import requests

    def _wrap(raw_exc):
        """Simulate network layer wrapping: TencentCloudSDKException('ClientNetworkError', ...) from e"""
        try:
            raise raw_exc
        except Exception as e:
            try:
                raise TencentCloudSDKException("ClientNetworkError", str(e)) from e
            except TencentCloudSDKException as tce:
                return tce

    def _chain(inner, outer_cls):
        """Construct outer(inner) chain (outer catches inner and throws itself), simulating requests'
        wrapping of underlying exceptions."""
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

    # Validate is_failover_triggered semantics
    assert is_failover_triggered("DNS_NXDOMAIN") is True
    assert is_failover_triggered("DNS_TIMEOUT") is True
    assert is_failover_triggered("TCP_CONN_REFUSED") is True
    assert is_failover_triggered("TCP_READ_TIMEOUT") is True
    assert is_failover_triggered("TLS_ERROR") is True
    assert is_failover_triggered("JSON_DECODE_ERROR") is False
    assert is_failover_triggered(None) is False
    print("  [OK] is_failover_triggered semantics")


# --------------------------------------------------------------------------- #
# 3) Integration: Trigger failover paths for different hosts
#    Note: According to the new "user-transparent" design, ClientProfile no longer exposes domain_failover configuration.
# --------------------------------------------------------------------------- #

def make_client(endpoint, req_timeout=3):
    cred = credential.Credential("AKIDFakeIdForDomainFailoverTest",
                                 "FakeKeyForDomainFailoverTest")
    http_profile = HttpProfile()
    http_profile.reqTimeout = req_timeout
    http_profile.endpoint = endpoint
    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile
    client_profile.disable_region_breaker = True   # Avoid region_breaker interference
    return cvm_client.CvmClient(cred, "ap-guangzhou", client_profile)


class _GaiPatcher(object):
    """Patch socket.getaddrinfo:
    - Hosts in resolvable_hosts return fake_ip.
    - Other tencentcloudapi hosts return NXDOMAIN.
    - Other hosts use real resolution.
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
        print("!!! Test case threw uncaught exception: %s: %s" % (type(e).__name__, e))
        traceback.print_exc()
    print("Time taken: %.3fs" % (time.time() - t0))


def case_all_dns_fail():
    """All 3 candidates DNS fail: Expected to try in order [com, com.cn, cn]."""
    client = make_client("cvm.tencentcloudapi.com")
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
            print("!!! No exception thrown, not as expected")
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
        print("Order validation: " + ("OK" if ok else "FAIL, got=%s" % uniq))


def case_primary_fail_backup_tried():
    """Primary domain DNS fails, second candidate "resolves successfully" but connects to 127.0.0.1:443 (no service) →
    Connection refused → switch to third candidate → then DNS fails again.
    Purpose is to verify that switching actually occurs, not returning immediately upon primary domain failure."""
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
        print("Primary domain attempted:   %s" % ok_primary)
        print("Second candidate attempted: %s" % ok_backup)


def case_intl_no_failover():
    """intl domains must not switch."""
    client = make_client("cvm.intl.tencentcloudapi.com")
    with _GaiPatcher() as p:
        try:
            client.DescribeRegions(models.DescribeRegionsRequest())
        except TencentCloudSDKException:
            pass
        uniq_tried = list(dict.fromkeys(p.resolved_log))
        print("resolved hosts: %s" % uniq_tried)
        ok = (uniq_tried == ["cvm.intl.tencentcloudapi.com"])
        print("Only primary domain attempted (intl no switching): " + ("OK" if ok else "FAIL"))


def case_custom_endpoint_no_failover():
    """Endpoints without tencentcloudapi suffix do not switch."""
    client = make_client("custom.example.invalid")
    try:
        client.DescribeRegions(models.DescribeRegionsRequest())
    except TencentCloudSDKException:
        pass
    breakers = client.domain_failover._breakers
    print("Registered candidate count: %d" % len(breakers))
    print("Candidate list: %s" % list(breakers.keys()))
    ok = (list(breakers.keys()) == ["custom.example.invalid"])
    print("Only single candidate retained (custom endpoint no switching): " + ("OK" if ok else "FAIL"))


def case_breaker_skips_bad_candidate():
    """After multiple failures, primary domain circuit breaker enters OPEN state."""
    from tencentcloud.common.circuit_breaker import STATE_OPEN
    client = make_client("cvm.tencentcloudapi.com")
    # Directly modify copy of internal constant thresholds for quick triggering (only affects current client's circuit breakers)
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
    print("Primary domain circuit breaker OPEN: " + ("OK" if ok else "FAIL"))


def case_no_profile_exposed():
    """Regression: ClientProfile no longer exposes domain_failover related fields/parameters."""
    cp = ClientProfile()
    assert not hasattr(cp, "domain_failover_profile"), \
        "ClientProfile should NOT expose domain_failover_profile"
    # Ensure DomainFailoverProfile class is also not exported from client_profile
    try:
        from tencentcloud.common.profile import client_profile as cp_mod
        assert not hasattr(cp_mod, "DomainFailoverProfile"), \
            "DomainFailoverProfile should NOT exist in client_profile module"
    except Exception as e:
        print("!!! %s" % e)
        raise
    print("ClientProfile does not expose domain_failover_profile: OK")
    print("client_profile module does not export DomainFailoverProfile: OK")


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def main():
    test_build_candidates()
    test_classify_exception()

    run_case("A All candidate DNS failures, observe switching order", case_all_dns_fail)
    run_case("B Primary domain failure switches to second candidate", case_primary_fail_backup_tried)
    run_case("C intl strictly no switching", case_intl_no_failover)
    run_case("D Custom endpoint no switching", case_custom_endpoint_no_failover)
    run_case("E Circuit breaker skips bad candidate", case_breaker_skips_bad_candidate)
    run_case("F Profile does not expose failover switch (user transparent)", case_no_profile_exposed)


if __name__ == "__main__":
    main()
