# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac
import sys


class Sign(object):
    def __init__(self, secretId, secretKey):
        self.secretId = secretId
        self.secretKey = secretKey
        if sys.version_info[0] > 2:
            self.Py2 = False
            self.secretKey = bytes(self.secretKey, 'utf-8')
        else:
            self.Py2 = True

    def make(self, requestHost, requestUri, params,
             method='POST', sign_method='HmacSHA1'):
        p = {}
        for k in params:
            if method == 'POST' and str(params[k])[0:1] == '@':
                continue
            p[k.replace('_', '.')] = params[k]
        ps = '&'.join('%s=%s' % (k, p[k]) for k in sorted(p))

        msg = '%s%s%s?%s' % (method.upper(), requestHost, requestUri, ps)
        if not self.Py2:
            msg = bytes(msg, 'utf-8')

        if sign_method == 'HmacSHA256':
            digestmod = hashlib.sha256
        else:
            digestmod = hashlib.sha1

        hashed = hmac.new(self.secretKey, msg, digestmod)
        base64 = binascii.b2a_base64(hashed.digest())[:-1]
        if not self.Py2:
            base64 = base64.decode()

        return base64
