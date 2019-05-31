# -*- coding: utf-8 -*-
import os
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.v20181106 import hcm_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("secretId"),
        os.environ.get("secretKey"))

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "hcm.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = hcm_client.HcmClient(cred, "", clientProfile)
    req = models.EvaluationRequest
    req.SessionId = "stress_test_956938"
    req.Image = "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"
    # 可选，不填默认为default
    req.HcmAppid = ""
    # 可选，与Image参数二者填一即可
    req.Url = ""

    resp = client.Evaluation(req)

    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
