# 简介
欢迎使用腾讯云开发者工具套件（SDK）3.0，SDK3.0是云 API3.0 平台的配套工具。目前已经支持cvm、vpc、cbs等产品，后续所有的云服务产品都会接入进来。新版SDK实现了统一化，具有各个语言版本的SDK使用方法相同，接口调用方式相同，统一的错误码和返回包格式这些优点。
为方便 Python 开发者调试和接入腾讯云产品 API，这里向您介绍适用于 Python 的腾讯云开发工具包，并提供首次使用开发工具包的简单示例。让您快速获取腾讯云 Python SDK 并开始调用。

# 依赖环境

1. 依赖环境：Python 2.7 到 3.6 版本。
2. 从 腾讯云控制台 开通相应产品。
3. 获取 SecretID、SecretKey 以及调用地址（endpoint），endpoint 一般形式为\*.tencentcloudapi.com，如CVM 的调用地址为 cvm.tencentcloudapi.com，具体参考各产品说明。

# 获取安装

安装 Python SDK 前，先获取安全凭证。在第一次使用云 API 之前，用户首先需要在腾讯云控制台上申请安全凭证，安全凭证包括 SecretID 和 SecretKey, SecretID 是用于标识 API 调用者的身份，SecretKey 是用于加密签名字符串和服务器端验证签名字符串的密钥。SecretKey 必须严格保管，避免泄露。

## 通过 Pip 安装(推荐)

您可以通过 pip 安装方式将腾讯云 API Python SDK 安装到您的项目中，如果您的项目环境尚未安装 pip，请详细参见 [pip](https://pip.pypa.io/en/stable/installing/?spm=a3c0i.o32026zh.a3.6.74134958lLSo6o)官网 安装。

通过pip方式安装请在命令行中执行以下命令:

```bash
pip install tencentcloud-sdk-python
```

请注意，如果同时有 python2 和 python3 环境， python3 环境需要使用 pip3 命令安装。

## 通过源码包安装

前往 [Github 代码托管地址](https://github.com/tencentcloud/tencentcloud-sdk-python) 下载最新代码，解压后

    $ cd tencentcloud-sdk-python
    $ python setup.py install

# 示例

以语音合成为例:

```python
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
    req = TextToVoiceRequest()
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
```

注意，如果是有代理的环境下，需要设置系统环境变量 `https_proxy` ，否则可能无法正常调用。

您可以在[github](https://github.com/zepc007/tencentcloud-sdk-python)中examples目录下找到更详细的示例。


