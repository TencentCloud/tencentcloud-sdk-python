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
域名级容灾切换模块。

当 SDK 发起的请求命中 DNS/TCP/TLS 类故障（详见 `tests/dns_failure_test/
DNS_FAILURE_SDK_EXCEPTION_ANALYSIS.md`）时，本模块按"主域名 → .com.cn →
.cn"的顺序串行重试，并为每个候选域名维护一个独立的 CircuitBreaker。

规则：
  - *.tencentcloudapi.com             ->  *.tencentcloudapi.com.cn  ->  *.tencentcloudapi.cn
  - *.{region}.tencentcloudapi.com    ->  *.{region}.tencentcloudapi.com.cn  ->  *.{region}.tencentcloudapi.cn
  - *.internal.tencentcloudapi.com    ->  按通用规则切换
  - *.intl.tencentcloudapi.com        ->  不切换（国际站）
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

# 主域名根 → 备份候选根（按优先级排列）
_FAILOVER_SUFFIX_RULES = [
    ("tencentcloudapi.com", ["tencentcloudapi.com.cn", "tencentcloudapi.cn"]),
]

# 国际站域名后缀：严格匹配，不做切换
_INTL_SUFFIX = ".intl.tencentcloudapi.com"


def _classify_exception(exc):
    """沿 __cause__ / __context__ 链识别原始异常类型，返回可触发域名切换的 kind。

    返回值：
      - "DNS_NXDOMAIN" / "DNS_TIMEOUT"      -> A 类 DNS 故障
      - "TCP_CONN_REFUSED"                  -> B 类 连接被拒
      - "TCP_READ_TIMEOUT"                  -> B 类 读超时
      - "TLS_ERROR"                         -> C 类 证书错误
      - "JSON_DECODE_ERROR"                 -> C 类 JSON 解析失败（不切换）
      - None                                -> 非网络类异常（不切换）
    """
    # 业务方法层的 JSONDecodeError 包装
    if isinstance(exc, TencentCloudSDKException) and exc.get_code() == "JSONDecodeError":
        return "JSON_DECODE_ERROR"

    # 沿异常链找到原始异常
    raw = None
    if isinstance(exc, TencentCloudSDKException):
        raw = exc.__cause__ or exc.__context__
    else:
        raw = exc
    if raw is None:
        return None

    # 走到链末端
    root = raw
    seen = set()
    while True:
        nxt = getattr(root, "__cause__", None) or getattr(root, "__context__", None)
        if nxt is None or id(nxt) in seen:
            break
        seen.add(id(root))
        root = nxt

    # 延迟导入 requests，避免影响未使用 http 的调用路径
    try:
        import requests
        req_conn_err = requests.exceptions.ConnectionError
        req_read_timeout = requests.exceptions.ReadTimeout
        req_connect_timeout = requests.exceptions.ConnectTimeout
        req_ssl_error = requests.exceptions.SSLError
    except ImportError:  # pragma: no cover
        req_conn_err = req_read_timeout = req_connect_timeout = req_ssl_error = ()

    # TLS 错误
    if req_ssl_error and isinstance(raw, req_ssl_error):
        return "TLS_ERROR"
    if _ssl is not None and isinstance(root, _ssl.SSLError):
        return "TLS_ERROR"

    # 读超时
    if req_read_timeout and isinstance(raw, req_read_timeout):
        return "TCP_READ_TIMEOUT"
    if isinstance(root, socket.timeout):
        return "TCP_READ_TIMEOUT"

    # 连接超时
    if req_connect_timeout and isinstance(raw, req_connect_timeout):
        return "TCP_READ_TIMEOUT"

    # 连接被拒（包括 DNS 返回 0.0.0.0 / 被劫持到无服务 IP）
    if isinstance(root, ConnectionRefusedError):
        return "TCP_CONN_REFUSED"

    # DNS 解析失败
    if isinstance(root, socket.gaierror):
        errno = getattr(root, "errno", None)
        # EAI_AGAIN = -3 on glibc, 11002 on Windows → 多为 DNS 超时
        if errno in (socket.EAI_AGAIN, -3, 11002):
            return "DNS_TIMEOUT"
        return "DNS_NXDOMAIN"

    # 其他 ConnectionError（兜底也触发切换，避免漏判）
    if req_conn_err and isinstance(raw, req_conn_err):
        return "DNS_NXDOMAIN"

    return None


def is_failover_triggered(kind):
    """kind 是否触发域名切换。JSON_DECODE_ERROR 和 None 均不触发。"""
    return kind in ("DNS_NXDOMAIN", "DNS_TIMEOUT",
                    "TCP_CONN_REFUSED", "TCP_READ_TIMEOUT", "TLS_ERROR")


def _split_host_suffix(host):
    """将 host 按 "tencentcloudapi.com" 等已知后缀拆分为 (prefix, matched_suffix)。
    若未命中任何受支持后缀则返回 (None, None)。
    """
    if not host:
        return None, None
    for suffix, _ in _FAILOVER_SUFFIX_RULES:
        if host == suffix or host.endswith("." + suffix):
            prefix = host[: -len(suffix)]  # 含结尾的 '.'（或空串）
            return prefix, suffix
    return None, None


def build_candidates(host):
    """根据原始 host 构造候选域名序列，首项始终是 host 自身。

    若 host 命中 `*.intl.tencentcloudapi.com`，则返回 `[host]`（不切换）。
    若 host 未命中任何受支持后缀（比如用户自定义 endpoint / ip），也返回 `[host]`。
    """
    if not host:
        return [host]

    # 国际站不切换
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
    """按候选域名维度维护断路器的容器。

    生命周期：AbstractClient 持有一个实例；每个候选域名首次出现时动态
    创建 CircuitBreaker。不同 client 实例间不共享（与现有 region_breaker
    的作用域一致）。
    """

    def __init__(self, profile):
        """:param profile: `DomainFailoverProfile`"""
        self._profile = profile
        self._breakers = {}
        self._lock = threading.Lock()

    @property
    def enabled(self):
        return self._profile is not None and self._profile.enabled

    def get_breaker(self, host):
        with self._lock:
            br = self._breakers.get(host)
            if br is None:
                br = CircuitBreaker(self._profile.breaker_setting)
                self._breakers[host] = br
            return br

    def iter_available_candidates(self, host):
        """按顺序返回 (candidate_host, breaker, generation)。

        - 若断路器为 OPEN，则跳过该候选；若全部 OPEN，则降级为"仍然尝试主域名"
          以避免流量全部被拒（与现有 region_breaker 行为一致）。
        - 调用方负责调用 breaker.after_requests(generation, success) 回写结果。
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
            # 全部断路器都 OPEN，这种情况也要给一次机会，选择主域名
            br = self.get_breaker(candidates[0])
            generation, _ = br.before_requests()
            usable.append((candidates[0], br, generation))
        return usable
