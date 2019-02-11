# !/usr/bin/env python
# -*- coding: utf-8 -*-
from base64 import b64decode
from uuid import uuid4
from tencentcloud.common import credential
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.aai.v20180522.models import TextToVoiceRequest
from tencentcloud.aai.v20180522.aai_client import AaiClient
try:
    # 实例化一个认证对象，入参需要传入腾讯云账户secretId，secretKey
    cred = credential.Credential("你的secretID", "你的secretKey")
    # 实例化要进行语音合成请求的client对象
    client = AaiClient(cred, 'ap-shanghai')
    # 实例化一个请求对象
    req = TextToVoiceRequest('先帝创业未半而中道崩殂，今天下三分')
    # 请求对象属性封装
    req.Text = '先帝创业未半而中道崩殂'  # type: str # 要合成语音的文本
    req.SessionId = uuid4()  # type: int # 一次请求对应一个SessionId，会原样返回，建议传入类似于uuid的字符串防止重复
    req.ModelType = 1  # type: int # 模型类型，默认值为1
    req.Volume = 5.0  # type: float # 音量大小，范围：[0，10]，分别对应10个等级的音量，默认为0
    req.Speed = 0.6  # type: float # 语速，范围：[-2，2]，分别对应不同语速：0.6倍，0.8倍，1.0倍，1.2倍，1.5倍，默认为0
    req.ProjectId = 10086  # type: int # 项目id，用户自定义，默认为0
    req.VoiceType = 0  # type: int # 音色0:女声1，亲和风格(默认) 音色1:男声1，成熟风格 音色2:男声2，成熟风格
    req.PrimaryLanguage = 1  # type: int # 主语言类型1:中文，最大100个汉字（标点符号算一个汉字）语言类型2:英文，最大支持400个字母（标点符号算一个字母)
    req.SampleRate = 16000  # type: int # 音频采样率，16000：16k，8000：8k，默认16k
    # 通过client对象调用想要访问的接口，需要传入请求对象
    rep = client.TextToVoice(req)
    # rep为响应对象
    print(rep)
    """
        {
        "Audio": "UklGRlR/AABXQVZFZm10IBAAAAABAAEAgD4AAAB9AAACABAAZGF0YSx9AAD+////AQD//wAAAAAAAAIAAQADAAMABgAEAAYABQAGAAUABwAIAAgACQAAE......AAgACAAEAAgADAAIAAwACAAQAAwACAAIAAgADAAMAAgACAAIAAwABAAAAAAAAAAAAAAD/////AAAAAAAA//8AAP///v/9//7//v///////v8AAP///////wAA/////wAA/////wAAAAAAAAAAAAAAAAAAAAAAAAAA",
        "RequestId": "9a7a1615-3e09-4db2-8032-5c6f497f7e6a",
        "SessionId": "session-1234"
        }
        Audio对应的值为经过base64编码,
        RequestId为返回的唯一请求id,
        SessionId为发送请求时传入的id即uuid4()
    """
    # content为base64解码后的二进制流
    content = b64decode(rep.Audio)
    # I/O操作
    with open('voice.wav', 'wb') as f:
        f.write(content)
except TencentCloudSDKException as e:
    print(e)
