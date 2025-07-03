# -*- coding: utf-8 -*-
import time

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
    req = models.CreateFlowRequest()

    userInfo = models.UserInfo()
    # 发起人用户id，在控制台查询获取
    userInfo.UserId = "**************"
    req.Operator = userInfo

    # 企业方 静默签署ApproverType为3 手动签署ApproverType为0
    enterpriseInfo = models.FlowCreateApprover()
    enterpriseInfo.ApproverType = 3
    enterpriseInfo.OrganizationName = "**************"
    enterpriseInfo.ApproverName = "**************"
    enterpriseInfo.ApproverMobile = "**************"
    enterpriseInfo.Required = True

    # 个人方
    clientInfo = models.FlowCreateApprover()
    clientInfo.ApproverType = 1
    clientInfo.ApproverName = "**************"
    clientInfo.ApproverMobile = "**************"
    clientInfo.Required = True

    req.Approvers = [enterpriseInfo, clientInfo]

    # 请设置合理的过期时间（秒级时间戳），否则容易造成合同过期
    req.DeadLine = int(time.time()) + 7 * 24 * 3600
    req.FlowName = "**************"

    resp = client.CreateFlow(req)
    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
