# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from tencentcloud.common.abstract_model import AbstractModel


class SendCodeVoiceRequest(AbstractModel):
    """SendCodeVoice请求参数结构体

    """

    def __init__(self):
        """
        :param CodeMessage: 验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是"。
        :type CodeMessage: str
        :param CalledNumber: 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type CalledNumber: str
        :param VoiceSdkAppid: 在[语音控制台](https://console.cloud.tencent.com/vms)添加应用后生成的实际SdkAppid，示例如1400006666。
        :type VoiceSdkAppid: str
        :param PlayTimes: 播放次数，可选，最多3次，默认2次。
        :type PlayTimes: int
        :param SessionContext: 用户的 session 内容，腾讯 server 回包中会原样返回。
        :type SessionContext: str
        """
        self.CodeMessage = None
        self.CalledNumber = None
        self.VoiceSdkAppid = None
        self.PlayTimes = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.CodeMessage = params.get("CodeMessage")
        self.CalledNumber = params.get("CalledNumber")
        self.VoiceSdkAppid = params.get("VoiceSdkAppid")
        self.PlayTimes = params.get("PlayTimes")
        self.SessionContext = params.get("SessionContext")


class SendCodeVoiceResponse(AbstractModel):
    """SendCodeVoice返回参数结构体

    """

    def __init__(self):
        """
        :param SendStatus: 语音验证码发送状态。
        :type SendStatus: :class:`tencentcloud.vms.v20200902.models.SendStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SendStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatus") is not None:
            self.SendStatus = SendStatus()
            self.SendStatus._deserialize(params.get("SendStatus"))
        self.RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """语音验证码发送状态

    """

    def __init__(self):
        """
        :param CallId: 标识本次发送 ID，标识一次下发记录。
        :type CallId: str
        :param SessionContext: 用户的 session 内容，腾讯 server 回包中会原样返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionContext: str
        """
        self.CallId = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.CallId = params.get("CallId")
        self.SessionContext = params.get("SessionContext")


class SendTtsVoiceRequest(AbstractModel):
    """SendTtsVoice请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板 ID，在控制台审核通过的模板 ID。
        :type TemplateId: str
        :param TemplateParamSet: 模板参数，若模板没有参数，请提供为空数组。
        :type TemplateParamSet: list of str
        :param CalledNumber: 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type CalledNumber: str
        :param VoiceSdkAppid: 在[语音控制台](https://console.cloud.tencent.com/vms)添加应用后生成的实际SdkAppid，示例如1400006666。
        :type VoiceSdkAppid: str
        :param PlayTimes: 播放次数，可选，最多3次，默认2次。
        :type PlayTimes: int
        :param SessionContext: 用户的 session 内容，腾讯 server 回包中会原样返回。
        :type SessionContext: str
        """
        self.TemplateId = None
        self.TemplateParamSet = None
        self.CalledNumber = None
        self.VoiceSdkAppid = None
        self.PlayTimes = None
        self.SessionContext = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.TemplateParamSet = params.get("TemplateParamSet")
        self.CalledNumber = params.get("CalledNumber")
        self.VoiceSdkAppid = params.get("VoiceSdkAppid")
        self.PlayTimes = params.get("PlayTimes")
        self.SessionContext = params.get("SessionContext")


class SendTtsVoiceResponse(AbstractModel):
    """SendTtsVoice返回参数结构体

    """

    def __init__(self):
        """
        :param SendStatus: 语音通知发送状态。
        :type SendStatus: :class:`tencentcloud.vms.v20200902.models.SendStatus`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SendStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SendStatus") is not None:
            self.SendStatus = SendStatus()
            self.SendStatus._deserialize(params.get("SendStatus"))
        self.RequestId = params.get("RequestId")