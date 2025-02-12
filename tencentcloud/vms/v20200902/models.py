# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class SendCodeVoiceRequest(AbstractModel):
    """SendCodeVoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CodeMessage: 验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是"。
        :type CodeMessage: str
        :param _CalledNumber: 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type CalledNumber: str
        :param _VoiceSdkAppid: 在[语音控制台](https://console.cloud.tencent.com/vms)添加应用后生成的实际SdkAppid，示例如1400006666。
        :type VoiceSdkAppid: str
        :param _PlayTimes: 播放次数，可选，最多3次，默认2次。
        :type PlayTimes: int
        :param _SessionContext: 用户的 session 内容，腾讯 server 回包中会原样返回。
        :type SessionContext: str
        """
        self._CodeMessage = None
        self._CalledNumber = None
        self._VoiceSdkAppid = None
        self._PlayTimes = None
        self._SessionContext = None

    @property
    def CodeMessage(self):
        """验证码，仅支持填写数字，实际播报语音时，会自动在数字前补充语音文本"您的验证码是"。
        :rtype: str
        """
        return self._CodeMessage

    @CodeMessage.setter
    def CodeMessage(self, CodeMessage):
        self._CodeMessage = CodeMessage

    @property
    def CalledNumber(self):
        """被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :rtype: str
        """
        return self._CalledNumber

    @CalledNumber.setter
    def CalledNumber(self, CalledNumber):
        self._CalledNumber = CalledNumber

    @property
    def VoiceSdkAppid(self):
        """在[语音控制台](https://console.cloud.tencent.com/vms)添加应用后生成的实际SdkAppid，示例如1400006666。
        :rtype: str
        """
        return self._VoiceSdkAppid

    @VoiceSdkAppid.setter
    def VoiceSdkAppid(self, VoiceSdkAppid):
        self._VoiceSdkAppid = VoiceSdkAppid

    @property
    def PlayTimes(self):
        """播放次数，可选，最多3次，默认2次。
        :rtype: int
        """
        return self._PlayTimes

    @PlayTimes.setter
    def PlayTimes(self, PlayTimes):
        self._PlayTimes = PlayTimes

    @property
    def SessionContext(self):
        """用户的 session 内容，腾讯 server 回包中会原样返回。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext


    def _deserialize(self, params):
        self._CodeMessage = params.get("CodeMessage")
        self._CalledNumber = params.get("CalledNumber")
        self._VoiceSdkAppid = params.get("VoiceSdkAppid")
        self._PlayTimes = params.get("PlayTimes")
        self._SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendCodeVoiceResponse(AbstractModel):
    """SendCodeVoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SendStatus: 语音验证码发送状态。
        :type SendStatus: :class:`tencentcloud.vms.v20200902.models.SendStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SendStatus = None
        self._RequestId = None

    @property
    def SendStatus(self):
        """语音验证码发送状态。
        :rtype: :class:`tencentcloud.vms.v20200902.models.SendStatus`
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SendStatus") is not None:
            self._SendStatus = SendStatus()
            self._SendStatus._deserialize(params.get("SendStatus"))
        self._RequestId = params.get("RequestId")


class SendStatus(AbstractModel):
    """语音验证码发送状态

    """

    def __init__(self):
        r"""
        :param _CallId: 标识本次发送 ID，标识一次下发记录。
        :type CallId: str
        :param _SessionContext: 用户的 session 内容，腾讯 server 回包中会原样返回。
        :type SessionContext: str
        """
        self._CallId = None
        self._SessionContext = None

    @property
    def CallId(self):
        """标识本次发送 ID，标识一次下发记录。
        :rtype: str
        """
        return self._CallId

    @CallId.setter
    def CallId(self, CallId):
        self._CallId = CallId

    @property
    def SessionContext(self):
        """用户的 session 内容，腾讯 server 回包中会原样返回。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext


    def _deserialize(self, params):
        self._CallId = params.get("CallId")
        self._SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTtsVoiceRequest(AbstractModel):
    """SendTtsVoice请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TemplateId: 模板 ID，在控制台审核通过的模板 ID。
        :type TemplateId: str
        :param _CalledNumber: 被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :type CalledNumber: str
        :param _VoiceSdkAppid: 在[语音控制台](https://console.cloud.tencent.com/vms)添加应用后生成的实际SdkAppid，示例如1400006666。
        :type VoiceSdkAppid: str
        :param _TemplateParamSet: 模板参数，若模板没有参数，请提供为空数组。
注：语音消息的内容长度不超过350字。
        :type TemplateParamSet: list of str
        :param _PlayTimes: 播放次数，可选，最多3次，默认2次。
        :type PlayTimes: int
        :param _SessionContext: 用户的 session 内容，腾讯 server 回包中会原样返回。
        :type SessionContext: str
        """
        self._TemplateId = None
        self._CalledNumber = None
        self._VoiceSdkAppid = None
        self._TemplateParamSet = None
        self._PlayTimes = None
        self._SessionContext = None

    @property
    def TemplateId(self):
        """模板 ID，在控制台审核通过的模板 ID。
        :rtype: str
        """
        return self._TemplateId

    @TemplateId.setter
    def TemplateId(self, TemplateId):
        self._TemplateId = TemplateId

    @property
    def CalledNumber(self):
        """被叫手机号码，采用 e.164 标准，格式为+[国家或地区码][用户号码]。
例如：+8613711112222， 其中前面有一个+号 ，86为国家码，13711112222为手机号。
        :rtype: str
        """
        return self._CalledNumber

    @CalledNumber.setter
    def CalledNumber(self, CalledNumber):
        self._CalledNumber = CalledNumber

    @property
    def VoiceSdkAppid(self):
        """在[语音控制台](https://console.cloud.tencent.com/vms)添加应用后生成的实际SdkAppid，示例如1400006666。
        :rtype: str
        """
        return self._VoiceSdkAppid

    @VoiceSdkAppid.setter
    def VoiceSdkAppid(self, VoiceSdkAppid):
        self._VoiceSdkAppid = VoiceSdkAppid

    @property
    def TemplateParamSet(self):
        """模板参数，若模板没有参数，请提供为空数组。
注：语音消息的内容长度不超过350字。
        :rtype: list of str
        """
        return self._TemplateParamSet

    @TemplateParamSet.setter
    def TemplateParamSet(self, TemplateParamSet):
        self._TemplateParamSet = TemplateParamSet

    @property
    def PlayTimes(self):
        """播放次数，可选，最多3次，默认2次。
        :rtype: int
        """
        return self._PlayTimes

    @PlayTimes.setter
    def PlayTimes(self, PlayTimes):
        self._PlayTimes = PlayTimes

    @property
    def SessionContext(self):
        """用户的 session 内容，腾讯 server 回包中会原样返回。
        :rtype: str
        """
        return self._SessionContext

    @SessionContext.setter
    def SessionContext(self, SessionContext):
        self._SessionContext = SessionContext


    def _deserialize(self, params):
        self._TemplateId = params.get("TemplateId")
        self._CalledNumber = params.get("CalledNumber")
        self._VoiceSdkAppid = params.get("VoiceSdkAppid")
        self._TemplateParamSet = params.get("TemplateParamSet")
        self._PlayTimes = params.get("PlayTimes")
        self._SessionContext = params.get("SessionContext")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendTtsVoiceResponse(AbstractModel):
    """SendTtsVoice返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SendStatus: 语音通知发送状态。
        :type SendStatus: :class:`tencentcloud.vms.v20200902.models.SendStatus`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SendStatus = None
        self._RequestId = None

    @property
    def SendStatus(self):
        """语音通知发送状态。
        :rtype: :class:`tencentcloud.vms.v20200902.models.SendStatus`
        """
        return self._SendStatus

    @SendStatus.setter
    def SendStatus(self, SendStatus):
        self._SendStatus = SendStatus

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("SendStatus") is not None:
            self._SendStatus = SendStatus()
            self._SendStatus._deserialize(params.get("SendStatus"))
        self._RequestId = params.get("RequestId")