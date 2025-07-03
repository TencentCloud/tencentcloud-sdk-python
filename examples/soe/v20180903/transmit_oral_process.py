# -*- coding: utf-8 -*-
# 发音数据传输接口（https://cloud.tencent.com/document/product/884/19318）
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.soe.v20180724 import soe_client, models
import base64


try:
    file = ""  # 音频文件路径地址
    slice_num = 1 * 1024  # 分片大小， 1 * 1024即为1k
    SessionId = ""  # 需要使用请求初始化相同的SessionId

    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential(
        os.environ.get("TENCENTCLOUD_SECRET_ID"),
        os.environ.get("TENCENTCLOUD_SECRET_KEY"))

    # 实例化一个http选项，可选的，没有特殊需求可以跳过。
    httpProfile = HttpProfile()
    httpProfile.reqMethod = "POST"  # post请求(默认为post请求)
    httpProfile.reqTimeout = 30  # 请求超时时间，单位为秒(默认60秒)
    httpProfile.endpoint = "soe.tencentcloudapi.com"  # 指定接入地域域名(默认就近接入)

    # 实例化一个client选项，可选的，没有特殊r需求可以跳过。
    clientProfile = ClientProfile()
    clientProfile.signMethod = "TC3-HMAC-SHA256"  # 指定签名算法(默认为HmacSHA256)
    clientProfile.unsignedPayload = True
    clientProfile.httpProfile = httpProfile
    client = soe_client.SoeClient(cred, "", clientProfile)

    # 读取音频文件
    with open(file, "rb") as f:
        content = f.read()
        content_len = len(content)

    # 分片数量计算
    pkg_num = content_len / slice_num + (content_len % slice_num != 0)
    # 开始分片并传输
    cur_pos = 0
    for j in range(int(pkg_num)):
        if j == int(pkg_num) - 1:
            send_content = content[cur_pos: content_len]
            cur_pos = content_len
            IsEnd = 1
        else:
            send_content = content[cur_pos: cur_pos + slice_num]
            cur_pos += slice_num
            IsEnd = 0
        base64_data = base64.b64encode(send_content).decode()

        # 请求参数赋值
        req = models.TransmitOralProcessRequest()
        req.SeqId = j + 1  # 流式数据包的序号，从1开始，当IsEnd字段为1后后续序号无意义，当IsLongLifeSession不为1且为非流式模式时无意义。
        req.IsEnd = IsEnd  # 是否传输完毕标志，若为0表示未完毕，若为1则传输完毕开始评估，非流式模式下无意义。
        req.VoiceFileType = 3  # 语音文件类型 1: raw, 2: wav, 3: mp3, 4: speex (语言文件格式目前仅支持 16k 采样率 16bit 编码单声道，如有不一致可能导致评估不准确或失败)。
        req.VoiceEncodeType = 1  # 语音编码类型 1:pcm。
        req.UserVoiceData = base64_data  # 当前数据包数据, 流式模式下数据包大小可以按需设置，在网络良好的情况下，建议设置为0.5k，且必须保证分片帧完整（16bit的数据必须保证音频长度为偶数），编码格式要求为BASE64
        req.RefText = "red"  # 评测文本
        req.WorkMode = 0  # 语音输入模式，0：流式分片，1：非流式一次性评估
        req.EvalMode = 1  # 评估模式，0：词模式（中文评测模式下为文字模式），1：句子模式，2：段落模式，3：自由说模式，当为词模式评估时，能够提供每个音节的评估信息，当为句子模式时，能够提供完整度和流利度信息，4：单词纠错模式：能够对单词和句子中的读错读音进行纠正，给出参考正确读音。
        req.ScoreCoeff = 1  # 评价苛刻指数，取值为[1.0 - 4.0]范围内的浮点数，用于平滑不同年龄段的分数，1.0为小年龄段，4.0为最高年龄段
        req.SessionId = SessionId  # 语音段唯一标识，一个完整语音一个SessionId。i
        # req.SoeAppId = ""  # 业务应用ID，与账号应用APPID无关，是用来方便客户管理服务的参数，新的 SoeAppId 可以在[控制台](https://console.cloud.tencent.com/soe)【应用管理】下新建。
        req.StorageMode = 0  # 音频存储模式，0：不存储，1：存储到公共对象存储，输出结果为该会话最后一个分片TransmitOralProcess 返回结果 AudioUrl 字段，2：永久存储音频，需要提工单申请，会产生一定存储费用，3：自定义存储，将音频存储到自定义的腾讯云[对象存储](https://cloud.tencent.com/product/cos)中，需要提工单登记存储信息。
        req.SentenceInfoEnabled = 0  # 输出断句中间结果标识，0：不输出，1：输出，通过设置该参数，可以在评估过程中的分片传输请求中，返回已经评估断句的中间结果，中间结果可用于客户端 UI 更新，输出结果为TransmitOralProcess请求返回结果 SentenceInfoSet 字段。
        req.ServerType = 0  # 评估语言，0：英文，1：中文。
        req.IsAsync = 0  # 异步模式标识，0：同步模式，1：异步模式，可选值参考[服务模式](https://cloud.tencent.com/document/product/884/33697)。
        req.IsQuery = 0  # 查询标识，当该参数为1时，该请求为查询请求，请求返回该 Session 的评估结果。
        req.TextMode = 0  # 输入文本模式，0: 普通文本，1：[音素结构](https://cloud.tencent.com/document/product/884/33698)文本。2：音素注册模式（提工单注册需要使用音素的单词）。

        # 请求服务，获取结果
        resp = client.TransmitOralProcessWithInit(req)
        json_resp = resp.to_json_string()

        # 输出json格式的字符串回包
        print(json_resp)

except TencentCloudSDKException as err:
    print(err)
