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

    @staticmethod
    def sign_tc3(secret_key, date, service, str2sign):
        def _hmac_sha256(key, msg):
            return hmac.new(key, msg.encode('utf-8'), hashlib.sha256)

        def _get_signature_key(key, date, service):
            k_date = _hmac_sha256(('TC3' + key).encode('utf-8'), date)
            k_service  = _hmac_sha256(k_date.digest(), service)
            k_signing = _hmac_sha256(k_service.digest(), 'tc3_request')
            return k_signing.digest()

        signing_key = _get_signature_key(secret_key, date, service)
        signature = _hmac_sha256(signing_key, str2sign).hexdigest()
        return signature
