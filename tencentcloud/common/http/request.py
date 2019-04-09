#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import socket
try:
    from http.client import HTTPConnection, BadStatusLine, HTTPSConnection
    from urllib.parse import urlparse
except ImportError:
    from httplib import HTTPConnection, BadStatusLine, HTTPSConnection
    from urlparse import urlparse

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


class ProxyHTTPSConnection(HTTPSConnection):
    def __init__(self, host, port=None, timeout=60):
        self.has_proxy = False
        self.request_host = host
        https_proxy = (os.environ.get('https_proxy')
                       or os.environ.get('HTTPS_PROXY'))
        if https_proxy:
            url = urlparse(https_proxy)
            if not url.hostname:
                url = urlparse('https://' + https_proxy)
            host = url.hostname
            port = url.port
            self.has_proxy = True
        HTTPSConnection.__init__(self, host, port, timeout=timeout)
        self.request_length = 0

    def send(self, astr):
        HTTPSConnection.send(self, astr)
        self.request_length += len(astr)

    def request(self, method, url, body=None, headers={}):
        self.request_length = 0
        if self.has_proxy:
            self.set_tunnel(self.request_host, 443)
        headers.setdefault("Host", self.request_host)
        HTTPSConnection.request(self, method, url, body, headers)


class ApiRequest(object):
    def __init__(self, host, req_timeout=60, debug=False):
        self.conn = ProxyHTTPSConnection(host, timeout=req_timeout)
        self.req_timeout = req_timeout
        self.keep_alive = False
        self.debug = debug
        self.request_size = 0
        self.response_size = 0

    def set_req_timeout(self, req_timeout):
        self.req_timeout = req_timeout

    def is_keep_alive(self):
        return self.keep_alive

    def set_keep_alive(self, flag=True):
        self.keep_alive = flag

    def set_debug(self, debug):
        self.debug = debug

    def _request(self, req_inter):
        if self.keep_alive:
            req_inter.header["Connection"] = "Keep-Alive"
        if self.debug:
            print("SendRequest %s" % req_inter)
        if req_inter.method == 'GET':
            req_inter_url = '%s?%s' % (req_inter.uri, req_inter.data)
            self.conn.request(req_inter.method, req_inter_url,
                              None, req_inter.header)
        elif req_inter.method == 'POST':
            self.conn.request(req_inter.method, req_inter.uri,
                              req_inter.data, req_inter.header)
        else:
            raise TencentCloudSDKException(
                "ClientParamsError", 'Method only support (GET, POST)')

    def send_request(self, req_inter):
        try:
            self._request(req_inter)
            try:
                http_resp = self.conn.getresponse()
            except BadStatusLine:
                # open another connection when keep-alive timeout
                # httplib will not handle keep-alive timeout,
                # so we must handle it ourself
                if self.debug:
                    print("keep-alive timeout, reopen connection")
                self.conn.close()
                self._request(req_inter)
                http_resp = self.conn.getresponse()
            headers = dict(http_resp.getheaders())
            resp_inter = ResponseInternal(status=http_resp.status,
                                          header=headers,
                                          data=http_resp.read())
            self.request_size = self.conn.request_length
            self.response_size = len(resp_inter.data)
            if not self.is_keep_alive():
                self.conn.close()
            if self.debug:
                print(("GetResponse %s" % resp_inter))
            return resp_inter
        except Exception as e:
            self.conn.close()
            raise TencentCloudSDKException("ClientNetworkError", str(e))


class RequestInternal(object):
    def __init__(self, host="", method="", uri="", header=None, data=""):
        if header is None:
            header = {}
        self.host = host
        self.method = method
        self.uri = uri
        self.header = header
        self.data = data

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("Host: %s\nMethod: %s\nUri: %s\nHeader: %s\nData: %s\n"
                % (self.host, self.method, self.uri, headers, self.data))


class ResponseInternal(object):
    def __init__(self, status=0, header=None, data=""):
        if header is None:
            header = {}
        self.status = status
        self.header = header
        self.data = data

    def __str__(self):
        headers = "\n".join("%s: %s" % (k, v) for k, v in self.header.items())
        return ("Status: %s\nHeader: %s\nData: %s\n"
                % (self.status, headers, self.data))
