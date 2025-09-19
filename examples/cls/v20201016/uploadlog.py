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
    ##安装lz4: pip install lz4==0.8.2
    import lz4

    if not hasattr(lz4, 'loads') or not hasattr(lz4, 'dumps'):
        lz4 = None
    else:
        def lz_compresss(data):
            return lz4.dumps(data)[4:]

except ImportError:
    lz4 = None

try:
    compressType = "xxx"  # 压缩方式, 目前只支持lz4, 客户根据需要填写(空字符串意味不压缩)
    region = "xxxx"  # 需要根据客户的实际地域自行填写
    topicId = "xxxxxx-xxxxxx-xxxxxx-xxxxxx"  # 这里需要使用客户实际的topicId，不能输入topicname
    hashKey = ""  # 可选参数，具体参考官方文档：https://cloud.tencent.com/document/product/614/59470
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
    clientProfile.httpProfile = httpProfile

    client = common_client.CommonClient("cls", '2020-10-16', cred, region, clientProfile)
    body = pb.pb_gen(1, 1)
    if compressType == "lz4":
        if lz4 is None or body == "":
            print("lz4 exception")
            exit(1)
        else:
            body = lz_compresss(body)

    headers = {
        "X-CLS-TopicId": topicId,
        "X-CLS-HashKey": hashKey,
        "X-CLS-CompressType": compressType,
    }

    resp = client.call_octet_stream("UploadLog", headers, body)

    # 输出json格式的字符串回包
    print("%s" % resp)

except TencentCloudSDKException as err:
    print("%s" % err)
