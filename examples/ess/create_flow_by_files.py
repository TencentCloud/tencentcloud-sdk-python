# -*- coding: utf-8 -*-

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
    httpProfile.endpoint = "ess.tencentcloudapi.com" # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "HmacSHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile

    client = ess_client.EssClient(cred, "", clientProfile)
    req = models.CreateFlowByFilesRequest()

    userInfo = models.UserInfo()
    # 发起人用户id，在控制台查询获取
    userInfo.UserId = "**************"
    req.Operator = userInfo

    # 签署pdf文件的资源编号列表，目前只支持单文件签署
    req.FileIds = ["**************"]

    # 企业方 静默签署ApproverType为3 手动签署ApproverType为0
    enterpriseInfo = models.ApproverInfo()
    enterpriseInfo.ApproverType = 3
    enterpriseInfo.OrganizationName = "**************"
    enterpriseInfo.ApproverName = "**************"
    enterpriseInfo.ApproverMobile = "**************"

    # 印章控件
    enterpriseComponent = models.Component()
    enterpriseComponent.ComponentValue = "**************"
    enterpriseComponent.ComponentPosY = 497.671875
    enterpriseComponent.ComponentWidth = 74
    enterpriseComponent.FileIndex = 0
    enterpriseComponent.ComponentType = "SIGN_SEAL"
    enterpriseComponent.ComponentPage = 1
    enterpriseComponent.ComponentPosX = 417.15625
    enterpriseComponent.ComponentHeight = 70
    enterpriseInfo.SignComponents = [enterpriseComponent]

    # 个人方
    clientInfo = models.ApproverInfo()
    clientInfo.ApproverType = 1
    clientInfo.ApproverName = "**************"
    clientInfo.ApproverMobile = "**************"

    # 签署控件
    clientComponent = models.Component()
    clientComponent.ComponentPosY = 472.78125
    clientComponent.ComponentWidth = 112
    clientComponent.FileIndex = 0
    clientComponent.ComponentType = "SIGN_SIGNATURE"
    clientComponent.ComponentPage = 1
    clientComponent.ComponentPosX = 146.15625
    clientComponent.ComponentHeight = 40
    clientInfo.SignComponents = [clientComponent]

    req.Approvers = [enterpriseInfo, clientInfo]
    req.FlowName = "**************"
    # 请设置合理的过期时间（秒级时间戳），否则容易造成合同过期
    req.DeadLine = int(time.time()) + 7 * 24 * 3600

    resp = client.CreateFlowByFiles(req)
    # 输出json格式的字符串回包
    print("%s" % resp.to_json_string())

except TencentCloudSDKException as err:
    print("%s" % err)
