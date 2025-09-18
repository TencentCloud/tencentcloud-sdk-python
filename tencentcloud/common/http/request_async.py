#!/usr/bin/python
# -*- coding: utf-8 -*-
import httpx

__all__ = ["ApiRequest", "ApiResponse", "ResponsePrettyFormatter"]

ApiRequest = httpx.Request
ApiResponse = httpx.Response


class ResponsePrettyFormatter(object):
    def __init__(self, resp: ApiResponse, format_body=True, delimiter="\n"):
        self._resp = resp
        self._format_body = format_body
        self._delimiter = delimiter

    def __str__(self):
        # todo
        lines = ['%s %d %s' % (self.str_ver(self._resp.raw.version), self._resp.status_code, self._resp.reason)]
        for k, v in self._resp.headers.items():
            lines.append('%s: %s' % (k, v))
        if self._format_body:
            lines.append('')
            lines.append(self._resp.text)
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
