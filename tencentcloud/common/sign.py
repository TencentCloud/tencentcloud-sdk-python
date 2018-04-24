# -*- coding: utf-8 -*-

import binascii
import hashlib
import hmac
import sys

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


class Sign(object):

    @staticmethod
    def sign(secretKey, signStr, signMethod):
        if sys.version_info[0] > 2:
            signStr = bytes(signStr, 'utf-8')
            secretKey = bytes(secretKey, 'utf-8')

        digestmod = None
        if signMethod == 'HmacSHA256':
            digestmod = hashlib.sha256
        elif signMethod == 'HmacSHA1':
            digestmod = hashlib.sha1
        else:
            raise TencentCloudSDKException("signMethod invalid", "signMethod only support (HmacSHA1, HmacSHA256)")

        hashed = hmac.new(secretKey, signStr, digestmod)
        base64 = binascii.b2a_base64(hashed.digest())[:-1]

        if sys.version_info[0] > 2:
            base64 = base64.decode()

        return base64
