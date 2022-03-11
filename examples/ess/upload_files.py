# -*- coding: utf-8 -*-
import base64

from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.ess.v20201111 import ess_client, models

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("**************", "**************")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "file.ess.tencent.cn"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = False
    clientProfile.httpProfile = httpProfile

    client = ess_client.EssClient(cred, "ap-guangzhou", clientProfile)
    req = models.UploadFilesRequest()

    caller = models.Caller()
    # Appid 电子签侧应用id,电子签提供
    caller.ApplicationId = "**************"
    # 管理员用户id或者员工用户id
    caller.OperatorId = "**************"
    req.Caller = caller

    req.BusinessType = "FLOW"

    with open("/*****/*****.pdf", "rb") as file:
        encoded = base64.encodebytes(file.read())

    uploadFile = models.UploadFile()
    uploadFile.FileBody = encoded.decode("utf-8")
    uploadFile.FileName = "******.pdf"

    req.FileInfos = [uploadFile]
    req.CoverRect = False

    resp = client.UploadFiles(req)
    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
