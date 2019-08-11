# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

from tencentcloud.tci.v20190318 import tci_client, models
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("", "")
    # cred = credential.Credential(
    #     os.environ.get("TENCENTCLOUD_SECRET_ID"),
    #     os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "tci.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = tci_client.TciClient(cred, "", clientProfile)
    req = models.CreateFaceRequest()
    req.LibraryId = "tci_library_156403897035611372834"
    req.PersonId = "tci_person_1564039695429032573626"
    req.urls=["https://img-blog.csdn.net/20161128171723259"]
    resp = client.CreateFace(req)

    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
