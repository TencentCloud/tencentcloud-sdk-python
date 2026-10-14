# -*- coding: utf-8 -*-
#
# Copyright 2017-2026 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
"""
Domain-level failover switching module.

When SDK-initiated requests hit DNS/TCP/TLS class failures (see `tests/dns_failure_test/
DNS_FAILURE_SDK_EXCEPTION_ANALYSIS.md` for details), this module retries sequentially
in the order "primary domain → .com.cn → .cn" and maintains an independent CircuitBreaker
for each candidate domain.

Rules:
  - *.tencentcloudapi.com             ->  *.tencentcloudapi.com.cn  ->  *.tencentcloudapi.cn
  - *.{region}.tencentcloudapi.com    ->  *.{region}.tencentcloudapi.com.cn  ->  *.{region}.tencentcloudapi.cn
  - *.internal.tencentcloudapi.com    ->  Follow general rules for switching
  - *.intl.tencentcloudapi.com        ->  No switching (international site)
"""
import json
import logging
import socket
import threading

try:
    import ssl as _ssl
except ImportError:  # pragma: no cover
    _ssl = None

from tencentcloud.common.circuit_breaker import CircuitBreaker
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException

logger = logging.getLogger("tencentcloud_sdk_common")

# Primary domain root → backup candidate roots (in priority order)
_FAILOVER_SUFFIX_RULES = [
    ("tencentcloudapi.com", ["tencentcloudapi.com.cn", "tencentcloudapi.cn"]),
]

# International site domain suffix: strict match, no switching
_INTL_SUFFIX = ".intl.tencentcloudapi.com"


class _InternalBreakerSetting(object):
    """Circuit breaker thresholds for domain failover (completely internal constants, not exposed to users).

    Field names are consistent with RegionBreakerProfile to reuse existing CircuitBreaker implementation.
    Each candidate domain's CircuitBreaker holds an independent setting instance to avoid mutual interference.
    """

    def __init__(self):
        self.max_fail_num = 5
        self.max_fail_percent = 0.75
        self.window_interval = 60 * 5   # Accumulated window within 5 minutes
        self.timeout = 60               # Enter HALF_OPEN after 60s in OPEN state
        self.max_requests = 5           # Return to CLOSED after accumulating 5 successes in HALF_OPEN


def _classify_exception(exc):
    """Identify the original exception type along the __cause__ / __context__ chain, return the kind that can trigger domain switching.

    Return values:
      - "DNS_NXDOMAIN" / "DNS_TIMEOUT"      -> Class A DNS failure
      - "TCP_CONN_REFUSED"                  -> Class B connection refused
      - "TCP_READ_TIMEOUT"                  -> Class B read timeout
      - "TLS_ERROR"                         -> Class C certificate error
      - "JSON_DECODE_ERROR"                 -> Class C JSON parsing failure (no switching)
      - None                                -> Non-network class exception (no switching)
    """
    # JSONDecodeError wrapper at business method level
    if isinstance(exc, TencentCloudSDKException) and exc.get_code() == "JSONDecodeError":
        return "JSON_DECODE_ERROR"

    # Find the original exception along the exception chain
    raw = None
    if isinstance(exc, TencentCloudSDKException):
        raw = exc.__cause__ or exc.__context__
    else:
        raw = exc
    if raw is None:
        return None

    # Walk to the end of the chain
    root = raw
    seen = set()
    while True:
        nxt = getattr(root, "__cause__", None) or getattr(root, "__context__", None)
        if nxt is None or id(nxt) in seen:
            break
        seen.add(id(root))
        root = nxt

    # Lazy import requests to avoid affecting call paths not using http
    try:
        import requests
        req_conn_err = requests.exceptions.ConnectionError
        req_read_timeout = requests.exceptions.ReadTimeout
        req_connect_timeout = requests.exceptions.ConnectTimeout
        req_ssl_error = requests.exceptions.SSLError
    except ImportError:  # pragma: no cover
        req_conn_err = req_read_timeout = req_connect_timeout = req_ssl_error = ()

    # TLS error
    if req_ssl_error and isinstance(raw, req_ssl_error):
        return "TLS_ERROR"
    if _ssl is not None and isinstance(root, _ssl.SSLError):
        return "TLS_ERROR"

    # Read timeout
    if req_read_timeout and isinstance(raw, req_read_timeout):
        return "TCP_READ_TIMEOUT"
    if isinstance(root, socket.timeout):
        return "TCP_READ_TIMEOUT"

    # Connection timeout
    if req_connect_timeout and isinstance(raw, req_connect_timeout):
        return "TCP_READ_TIMEOUT"

    # Connection refused (including DNS returning 0.0.0.0 / hijacked to non-service IP)
    if isinstance(root, ConnectionRefusedError):
        return "TCP_CONN_REFUSED"

    # DNS resolution failure
    if isinstance(root, socket.gaierror):
        errno = getattr(root, "errno", None)
        # EAI_AGAIN = -3 on glibc, 11002 on Windows → mostly DNS timeout
        if errno in (socket.EAI_AGAIN, -3, 11002):
            return "DNS_TIMEOUT"
        return "DNS_NXDOMAIN"

    # Other ConnectionError (fallback also triggers switching to avoid missed judgments)
    if req_conn_err and isinstance(raw, req_conn_err):
        return "DNS_NXDOMAIN"

    return None


def is_failover_triggered(kind):
    """Whether the kind triggers domain switching. JSON_DECODE_ERROR and None do not trigger."""
    return kind in ("DNS_NXDOMAIN", "DNS_TIMEOUT",
                    "TCP_CONN_REFUSED", "TCP_READ_TIMEOUT", "TLS_ERROR")


def _split_host_suffix(host):
    """Split host by known suffixes like "tencentcloudapi.com" into (prefix, matched_suffix).
    Returns (None, None) if no supported suffix is matched.
    """
    if not host:
        return None, None
    for suffix, _ in _FAILOVER_SUFFIX_RULES:
        if host == suffix or host.endswith("." + suffix):
            prefix = host[: -len(suffix)]  # including the trailing '.' (or empty string)
            return prefix, suffix
    return None, None


def build_candidates(host):
    """Construct candidate domain sequence based on original host, with the host itself always as the first item.

    If host matches `*.intl.tencentcloudapi.com`, returns `[host]` (no switching).
    If host doesn't match any supported suffix (e.g., user-defined endpoint / ip), also returns `[host]`.
    """
    if not host:
        return [host]

    # International sites do not switch
    if host == _INTL_SUFFIX.lstrip(".") or host.endswith(_INTL_SUFFIX):
        return [host]

    prefix, suffix = _split_host_suffix(host)
    if suffix is None:
        return [host]

    candidates = [host]
    for alt in dict(_FAILOVER_SUFFIX_RULES)[suffix]:
        candidates.append(prefix + alt)
    return candidates


class DomainFailoverManager(object):
    """Container for maintaining circuit breakers by candidate domain dimension.

    Lifecycle: AbstractClient holds one instance; CircuitBreaker is dynamically created
    when each candidate domain first appears. Not shared between different client instances
    (consistent with the scope of existing region_breaker).

    This manager is an internal SDK component, completely transparent to users: no switches exposed,
    no thresholds exposed, always active. Only when host doesn't match `*.tencentcloudapi.com` family
    (e.g., intl domains, custom endpoints, IPs) is equivalent to "no switching", with behavior
    completely consistent with before the modification.
    """

    def __init__(self):
        self._breakers = {}
        self._lock = threading.Lock()

    def get_breaker(self, host):
        with self._lock:
            br = self._breakers.get(host)
            if br is None:
                br = CircuitBreaker(_InternalBreakerSetting())
                self._breakers[host] = br
            return br

    def iter_available_candidates(self, host):
        """Return (candidate_host, breaker, generation) in order.

        - If circuit breaker is OPEN, skip that candidate; if all are OPEN, downgrade to "still try primary domain"
          to avoid all traffic being rejected (consistent with existing region_breaker behavior).
        - Caller is responsible for calling breaker.after_requests(generation, success) to write back results.
        """
        candidates = build_candidates(host)
        usable = []
        for c in candidates:
            br = self.get_breaker(c)
            generation, need_skip = br.before_requests()
            if need_skip:
                logger.debug("domain_failover: skip %s (breaker open)", c)
                continue
            usable.append((c, br, generation))

        if not usable:
        # All circuit breakers are OPEN, give one more chance in this case, choose primary domain
            br = self.get_breaker(candidates[0])
            generation, _ = br.before_requests()
            usable.append((candidates[0], br, generation))
        return usable
