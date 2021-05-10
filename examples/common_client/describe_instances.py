# -*- coding: utf-8 -*-
import os
import json

from tencentcloud.common.common_client import CommonClient
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    first_cred = credential.STSAssumeRoleCredential(os.environ.get("TENCENTCLOUD_SECRET_ID"), os.environ.get("TENCENTCLOUD_SECRET_KEY"))
    cred = first_cred.get_credential("qcs::cam::uin/11111:roleName/first", "testfirst")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    # 如果需要指定proxy访问接口，可以按照如下方式初始化hp
    # httpProfile = HttpProfile(proxy="http://用户名:密码@代理IP:代理端口")
    httpProfile.reqMethod = "GET"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "api.ap-shanghai.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    # httpProfile.rootDomain = 'ap-shanghai.tencentcloudapi.com'    # 指定根域名, 默认为 tencentcloudapi.com

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化要请求产品(以cvm为例)的client对象，clientProfile是可选的。
    common_client = CommonClient(credential=cred, region="ap-shanghai", version='2020-11-06', service='api', profile=clientProfile)

    print common_client.call_json("DescribeZones", {"Product": "cvm"})


except TencentCloudSDKException as err:
    print(err)
