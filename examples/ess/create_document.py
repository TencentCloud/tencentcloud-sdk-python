# -*- coding: utf-8 -*-

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ess.v20201111 import ess_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "ess.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "HmacSHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = ess_client.EssClient(cred, "", clientProfile)
    req = models.CreateDocumentRequest()

    # 由上一步返回
    req.FlowId = "**************"

    # 传入自定义文件名即可
    req.FileNames = ["**************"]

    userInfo = models.UserInfo()
    # 发起人用户id，在控制台查询获取
    userInfo.UserId = "**************"
    req.Operator = userInfo

    # 控制台配置模板后查询获取
    req.TemplateId = "**************"

    # 发起人填写控件
    formFiled = models.FormField()
    # 控制台配置模板时，于"指定签约区域"步骤，查看控件属性可以获取
    formFiled.ComponentName = "**************"
    formFiled.ComponentValue = "**************"
    req.FormFields = [formFiled]

    resp = client.CreateDocument(req)
    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
