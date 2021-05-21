# -*- coding: utf-8 -*-
import os
import warnings

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models

# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
try:
    warnings.simplefilter('error')
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    # 如果需要指定proxy访问接口，可以按照如下方式初始化hp
    # httpProfile = HttpProfile(proxy="http://用户名:密码@代理IP:代理端口")
    httpProfile.reqMethod = "GET"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30    # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "cvm.ap-shanghai.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    # httpProfile.rootDomain = 'ap-shanghai.tencentcloudapi.com'    # 指定根域名, 默认为 tencentcloudapi.com

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法
    clientProfile.language = "en-US"
    clientProfile.httpProfile = httpProfile

    # 实例化要请求产品(以cvm为例)的client对象，clientProfile是可选的。
    client = cvm_client.CvmClient(cred, "ap-shanghai", clientProfile)

    # 实例化一个cvm实例信息查询请求对象,每个接口都会对应一个request对象。
    req = models.DescribeInstancesRequest()

    # 填充请求参数,这里request对象的成员变量即对应接口的入参。
    # 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义。
    respFilter = models.Filter()  # 创建Filter对象, 以zone的维度来查询cvm实例。
    respFilter.Name = "zone"
    respFilter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
    req.Filters = [respFilter]  # Filters 是成员为Filter对象的列表

    # 这里还支持以标准json格式的string来赋值请求参数的方式。下面的代码跟上面的参数赋值是等效的。
    params = '''{
        "Filters": [
            {
                "Name": "zone",
                "Values": ["ap-shanghai-1", "ap-shanghai-2"],
                "a": "a"

            }
        ]
    }'''
    req.from_json_string(params)

except Exception as err:
    assert "fileds are useless" in str(err)
