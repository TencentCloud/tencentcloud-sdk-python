#!/usr/bin/python
# -*- coding: utf-8 -*-
import httpx

__all__ = ["ApiRequest", "ApiResponse", "RequestPrettyFormatter", "ResponsePrettyFormatter"]

ApiRequest = httpx.Request
ApiResponse = httpx.Response


class RequestPrettyFormatter(object):
    def __init__(self, req: ApiRequest, format_body=True, delimiter="\n"):
        self._req = req
        self._format_body = format_body
        self._delimiter = delimiter

    def __str__(self):
        lines = ["%s %s" % (self._req.method, self._req.url)]
        for k, v in self._req.headers.items():
            lines.append("%s: %s" % (k, v))
        lines.append("")
        if self._format_body:
            try:
                lines.append(self._req.content.decode("utf-8"))
            except UnicodeDecodeError:
                # binary body
                import base64
                lines.append("base64_body:" + base64.standard_b64encode(self._req.content).decode())
        return self._delimiter.join(lines)


class ResponsePrettyFormatter(object):
    def __init__(self, resp: ApiResponse, format_body=True, delimiter="\n"):
        self._resp = resp
        self._format_body = format_body
        self._delimiter = delimiter

    def __str__(self):
        lines = ['%s %d %s' % (self.str_ver(self._resp.http_version), self._resp.status_code, self._resp.reason_phrase)]
        for k, v in self._resp.headers.items():
            lines.append('%s: %s' % (k, v))
        return self._delimiter.join(lines)

    async def astr(self):
        lines = ['%s %d %s' % (self.str_ver(self._resp.http_version), self._resp.status_code, self._resp.reason_phrase)]
        for k, v in self._resp.headers.items():
            lines.append('%s: %s' % (k, v))
        if self._format_body:
            lines.append('')
            lines.append((await self._resp.aread()).decode("utf-8"))
        return self._delimiter.join(lines)

    @staticmethod
    def str_ver(ver):
        if ver == 10:
            return "HTTP/1.0"
        elif ver == 11:
            return "HTTP/1.1"
        elif ver == 20:
            return "HTTP/2.0"
        else:
            return str(ver)
