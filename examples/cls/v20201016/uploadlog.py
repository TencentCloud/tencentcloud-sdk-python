# -*- coding: utf-8 -*-
import os
import sys

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

from tencentcloud.common import common_client
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
import pb

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "cls.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = common_client.CommonClient("cls", '2020-10-16', cred, "ap-beijing", clientProfile)
    headers = {
        # 使用对应地域下真实存在的日志主题ID
        "X-CLS-TopicId": "xxxxf2e2-166c-4174-9473-b6a6dfca6f6e",
        # 主题分区，https://cloud.tencent.com/document/product/614/39259
        # 取值00000000000000000000000000000000，ffffffffffffffffffffffffffffffff
        "X-CLS-HashKey": "0fffffffffffffffffffffffffffffff",
        # 压缩类型
        "X-CLS-CompressType": "",
    }
    resp = client.call_octet_stream("UploadLog", headers, pb.pb_gen(1,1))

    # 输出json格式的字符串回包
    print("%s" % resp)

except TencentCloudSDKException as err:
    print("%s" % err)
