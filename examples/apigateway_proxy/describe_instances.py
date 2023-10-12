# -*- coding: utf-8 -*-
import os

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 导入对应产品模块的client models。
from tencentcloud.cvm.v20170312 import cvm_client, models
# 导入可选配置类
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    http_profile = HttpProfile()

    # 此处域名必须和APIGateway中后端配置-后端地址保持一致
    http_profile.endpoint = "cvm.tencentcloudapi.com"
    # 此处必须为纯域名格式，不能有http(s)前缀，也不能有URL Path
    http_profile.apigw_endpoint = "service-1q2w3e4r-12345678.gz.apigw.tencentcs.com"

    client_profile = ClientProfile()
    client_profile.httpProfile = http_profile

    # 配置结束，以下为普通的调用过程

    client = cvm_client.CvmClient(cred, "ap-shanghai", client_profile)

    # 实例化一个cvm实例信息查询请求对象,每个接口都会对应一个request对象。
    req = models.DescribeInstancesRequest()

    # 填充请求参数,这里request对象的成员变量即对应接口的入参。
    # 你可以通过官网接口文档或跳转到request对象的定义处查看请求参数的定义。
    # 创建Filter对象, 以zone的维度来查询cvm实例。
    filter = models.Filter()
    filter.Name = "zone"
    filter.Values = ["ap-shanghai-1", "ap-shanghai-2"]
    req.Filters = [filter]

    # 通过client对象调用DescribeInstances方法发起请求。注意请求方法名与请求对象是对应的。
    # 返回的resp是一个DescribeInstancesResponse类的实例，与请求对象对应。
    resp = client.DescribeInstances(req)

    # 输出json格式的字符串回包
    print(resp.to_json_string(indent=2))

    # 也可以取出单个值。
    # 你可以通过官网接口文档或跳转到response对象的定义处查看返回字段的定义。
    print(resp.TotalCount)
except TencentCloudSDKException as err:
    print(err)
