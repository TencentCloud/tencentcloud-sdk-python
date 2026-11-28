# -*- coding: utf-8 -*-
import os

import pytest
import requests

from tencentcloud.common.http.request import ProxyConnection


@pytest.fixture(autouse=True)
def proxy_environment(monkeypatch):
    # A plain mapping also allows distinct uppercase/lowercase keys on Windows.
    monkeypatch.setattr(os, "environ", {})


def request_proxy(monkeypatch, host, is_http=False, proxy=None):
    sent = {}

    def send(request, **kwargs):
        sent.update(kwargs)
        return requests.Response()

    connection = ProxyConnection(host, is_http=is_http, proxy=proxy)
    monkeypatch.setattr(connection._session, "send", send)
    scheme = "http" if is_http else "https"
    try:
        connection.request("GET", "%s://%s/" % (scheme, host), headers={})
    finally:
        connection._session.close()
    return sent["proxies"].get(scheme)


@pytest.mark.parametrize("is_http", [False, True])
@pytest.mark.parametrize("no_proxy_name", ["no_proxy", "NO_PROXY"])
@pytest.mark.parametrize("host,no_proxy", [
    ("cvm.tencentcloudapi.com", "cvm.tencentcloudapi.com"),
    ("cvm.tencentcloudapi.com", ".tencentcloudapi.com"),
    ("cvm.tencentcloudapi.com", "tencentcloudapi.com"),
    ("cvm.tencentcloudapi.com", "localhost, .tencentcloudapi.com"),
    ("cvm.tencentcloudapi.com", "*"),
    ("192.0.2.5", "192.0.2.0/24"),
    ("cvm.tencentcloudapi.com:8443", "cvm.tencentcloudapi.com"),
])
def test_no_proxy_bypasses_environment_proxy(monkeypatch, is_http, no_proxy_name, host, no_proxy):
    name = "HTTP_PROXY" if is_http else "HTTPS_PROXY"
    monkeypatch.setenv(name, "http://proxy.example:8080")
    monkeypatch.setenv(no_proxy_name, no_proxy)

    assert request_proxy(monkeypatch, host, is_http=is_http) is None


@pytest.mark.parametrize("is_http", [False, True])
@pytest.mark.parametrize("no_proxy", ["localhost", "cvm.tencentcloudapi.com.other.example", "192.0.2.0/24"])
def test_unmatched_host_uses_environment_proxy(monkeypatch, is_http, no_proxy):
    name = "HTTP_PROXY" if is_http else "HTTPS_PROXY"
    proxy = "http://proxy.example:8080"
    monkeypatch.setenv(name, proxy)
    monkeypatch.setenv("NO_PROXY", no_proxy)

    assert request_proxy(monkeypatch, "cvm.tencentcloudapi.com", is_http=is_http) == proxy


@pytest.mark.parametrize("is_http", [False, True])
def test_explicit_proxy_takes_precedence(monkeypatch, is_http):
    name = "HTTP_PROXY" if is_http else "HTTPS_PROXY"
    proxy = "http://explicit.example:8080"
    monkeypatch.setenv(name, "http://environment.example:8080")
    monkeypatch.setenv("NO_PROXY", "*")

    assert request_proxy(monkeypatch, "cvm.tencentcloudapi.com", is_http=is_http, proxy=proxy) == proxy


@pytest.mark.parametrize("lowercase,uppercase,expected", [
    (".tencentcloudapi.com", "localhost", None),
    ("localhost", ".tencentcloudapi.com", "http://proxy.example:8080"),
])
def test_lowercase_no_proxy_takes_precedence(monkeypatch, lowercase, uppercase, expected):
    monkeypatch.setenv("HTTPS_PROXY", "http://proxy.example:8080")
    monkeypatch.setenv("no_proxy", lowercase)
    monkeypatch.setenv("NO_PROXY", uppercase)

    assert request_proxy(monkeypatch, "cvm.tencentcloudapi.com") == expected
