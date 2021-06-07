# -*- coding: utf-8 -*-
# 发音评估初始化（https://cloud.tencent.com/document/product/884/19319）
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.soe.v20180724 import soe_client, models
import uuid

try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("secretId", "secretKey")

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)
    httpProfile.keepAlive = True  # 保持活动状态

    # 实例化一个client选项，可选的，没有特殊需求可以跳过。
    clientProfile = ClientProfile()  # 客户端配置文件
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True  # 未签署的有效负载
    clientProfile.httpProfile = httpProfile  # http选项
    client = soe_client.SoeClient(cred, "", clientProfile)  # 连接soe的连接

    # 请求参数赋值
    req = models.InitOralProcessRequest()  # 连接soe的评测初始化模块
    req.SessionId = str(uuid.uuid1())  # 语音段唯一标识，一段语音一个SessionId
    req.RefText = "red"  # 评测文本
    req.WorkMode = 1  # 语音输入模式，0：流式分片，1：非流式一次性评估
    req.EvalMode = 1  # 评估模式，0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息。4: 英文单词音素诊断评测模式，针对一个单词音素诊断评测。
    req.ScoreCoeff = 1  # 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段
    # req.SoeAppId = "123456"  # 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。
    # req.IsLongLifeSession = 0  # 长效session标识，当该参数为1时，session的持续时间为300s，但会一定程度上影响第一个数据包的返回速度，且TransmitOralProcess必须同时为1才可生效。
    req.StorageMode = 0  # 音频存储模式，0：不存储，1：存储到公共对象存储，输出结果为该会话最后一个分片TransmitOralProcess 返回结果 AudioUrl 字段，2：永久存储音频，需要提工单申请，会产生一定存储费用，3：自定义存储，将音频存储到自定义的腾讯云[对象存储](https://cloud.tencent.com/product/cos)中，需要提工单登记存储信息。
    # req.SentenceInfoEnabled = 0  # 输出断句中间结果标识，0：不输出，1：输出，通过设置该参数，可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
    req.ServerType = 0  # 评估语言，0：英文，1：中文。
    req.IsAsync = 0  # 异步模式标识，0：同步模式，1：异步模式，可选值参考[服务模式](https://cloud.tencent.com/document/product/884/33697)。
    req.TextMode = 0  # 输入文本模式，0: 普通文本，1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本。2：音素注册模式（提工单注册需要使用音素的单词）。

    # 请求服务，获取结果
    resp = client.InitOralProcess(req)
    json_resp = resp.to_json_string()

    # 输出json格式的字符串回包
    print(json_resp)


except TencentCloudSDKException as err:
    print(err)

