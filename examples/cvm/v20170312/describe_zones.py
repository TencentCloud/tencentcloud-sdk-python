# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.profile import client_profile
from tencentcloud.common.profile import http_profile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    hp = http_profile.HttpProfile()
    # 如果需要指定proxy访问接口，可以按照如下方式初始化hp
    # hp = http_profile.HttpProfile(proxy="http://用户名:密码@代理IP:代理端口")
    hp.reqMethod = "POST"
    cp = client_profile.ClientProfile()
    cp.signMethod = "TC3-HMAC-SHA256"
    cp.httpProfile = hp
    # 实例化要请求产品(以cvm为例)的client对象
    client = cvm_client.CvmClient(cred, "ap-guangzhou", cp)

    # 实例化一个请求对象
    req = models.DescribeZonesRequest()

    # 通过client对象调用想要访问的接口，需要传入请求对象
    resp = client.DescribeZones(req)
    # 输出json格式的字符串回包
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
