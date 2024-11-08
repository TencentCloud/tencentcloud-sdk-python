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


class Group(AbstractModel):
    """Group是消息组的具体定义，当前包含ContentType、Url、Content三个字段。其中，具体的ContentType字段定义，参考互联网MIME类型标准。

    """

    def __init__(self):
        r"""
        :param _ContentType: 消息类型参考互联网MIME类型标准，当前仅支持"text/plain"。
        :type ContentType: str
        :param _Url: 返回内容以链接形式提供。
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _Content: 普通文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._ContentType = None
        self._Url = None
        self._Content = None

    @property
    def ContentType(self):
        """消息类型参考互联网MIME类型标准，当前仅支持"text/plain"。
        :rtype: str
        """
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def Url(self):
        """返回内容以链接形式提供。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Content(self):
        """普通文本。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._ContentType = params.get("ContentType")
        self._Url = params.get("Url")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseMessage(AbstractModel):
    """从TBP-RTS服务v1.3版本起，机器人以消息组列表的形式响应，消息组列表GroupList包含多组消息，用户根据需要对部分或全部消息组进行组合使用。

    """

    def __init__(self):
        r"""
        :param _GroupList: 消息组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of Group
        """
        self._GroupList = None

    @property
    def GroupList(self):
        """消息组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Group
        """
        return self._GroupList

    @GroupList.setter
    def GroupList(self, GroupList):
        self._GroupList = GroupList


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self._GroupList = []
            for item in params.get("GroupList"):
                obj = Group()
                obj._deserialize(item)
                self._GroupList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlotInfo(AbstractModel):
    """槽位信息

    """

    def __init__(self):
        r"""
        :param _SlotName: 槽位名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotName: str
        :param _SlotValue: 槽位值
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotValue: str
        """
        self._SlotName = None
        self._SlotValue = None

    @property
    def SlotName(self):
        """槽位名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SlotName

    @SlotName.setter
    def SlotName(self, SlotName):
        self._SlotName = SlotName

    @property
    def SlotValue(self):
        """槽位值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SlotValue

    @SlotValue.setter
    def SlotValue(self, SlotValue):
        self._SlotValue = SlotValue


    def _deserialize(self, params):
        self._SlotName = params.get("SlotName")
        self._SlotValue = params.get("SlotValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextProcessRequest(AbstractModel):
    """TextProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotId: 机器人标识，用于定义抽象机器人。
        :type BotId: str
        :param _BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        :param _TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param _InputText: 请求的文本。
        :type InputText: str
        :param _SessionAttributes: 透传字段，透传给用户自定义的WebService服务。
        :type SessionAttributes: str
        :param _PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
        :type PlatformType: str
        :param _PlatformId: 当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识
        :type PlatformId: str
        """
        self._BotId = None
        self._BotEnv = None
        self._TerminalId = None
        self._InputText = None
        self._SessionAttributes = None
        self._PlatformType = None
        self._PlatformId = None

    @property
    def BotId(self):
        """机器人标识，用于定义抽象机器人。
        :rtype: str
        """
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotEnv(self):
        """机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :rtype: str
        """
        return self._BotEnv

    @BotEnv.setter
    def BotEnv(self, BotEnv):
        self._BotEnv = BotEnv

    @property
    def TerminalId(self):
        """终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :rtype: str
        """
        return self._TerminalId

    @TerminalId.setter
    def TerminalId(self, TerminalId):
        self._TerminalId = TerminalId

    @property
    def InputText(self):
        """请求的文本。
        :rtype: str
        """
        return self._InputText

    @InputText.setter
    def InputText(self, InputText):
        self._InputText = InputText

    @property
    def SessionAttributes(self):
        """透传字段，透传给用户自定义的WebService服务。
        :rtype: str
        """
        return self._SessionAttributes

    @SessionAttributes.setter
    def SessionAttributes(self, SessionAttributes):
        self._SessionAttributes = SessionAttributes

    @property
    def PlatformType(self):
        """平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
        :rtype: str
        """
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def PlatformId(self):
        """当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._BotEnv = params.get("BotEnv")
        self._TerminalId = params.get("TerminalId")
        self._InputText = params.get("InputText")
        self._SessionAttributes = params.get("SessionAttributes")
        self._PlatformType = params.get("PlatformType")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextProcessResponse(AbstractModel):
    """TextProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DialogStatus: 当前会话状态{会话开始: START; 会话中: COUTINUE; 会话结束: COMPLETE}。
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param _BotName: 匹配到的机器人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param _IntentName: 匹配到的意图名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param _SlotInfoList: 槽位信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param _InputText: 原始的用户说法。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputText: str
        :param _ResponseMessage: 机器人应答。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
        :param _SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param _ResultType: 结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param _ResponseText: 机器人对话的应答文本。	
        :type ResponseText: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DialogStatus = None
        self._BotName = None
        self._IntentName = None
        self._SlotInfoList = None
        self._InputText = None
        self._ResponseMessage = None
        self._SessionAttributes = None
        self._ResultType = None
        self._ResponseText = None
        self._RequestId = None

    @property
    def DialogStatus(self):
        """当前会话状态{会话开始: START; 会话中: COUTINUE; 会话结束: COMPLETE}。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DialogStatus

    @DialogStatus.setter
    def DialogStatus(self, DialogStatus):
        self._DialogStatus = DialogStatus

    @property
    def BotName(self):
        """匹配到的机器人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def IntentName(self):
        """匹配到的意图名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IntentName

    @IntentName.setter
    def IntentName(self, IntentName):
        self._IntentName = IntentName

    @property
    def SlotInfoList(self):
        """槽位信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SlotInfo
        """
        return self._SlotInfoList

    @SlotInfoList.setter
    def SlotInfoList(self, SlotInfoList):
        self._SlotInfoList = SlotInfoList

    @property
    def InputText(self):
        """原始的用户说法。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InputText

    @InputText.setter
    def InputText(self, InputText):
        self._InputText = InputText

    @property
    def ResponseMessage(self):
        """机器人应答。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
        """
        return self._ResponseMessage

    @ResponseMessage.setter
    def ResponseMessage(self, ResponseMessage):
        self._ResponseMessage = ResponseMessage

    @property
    def SessionAttributes(self):
        """透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionAttributes

    @SessionAttributes.setter
    def SessionAttributes(self, SessionAttributes):
        self._SessionAttributes = SessionAttributes

    @property
    def ResultType(self):
        """结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def ResponseText(self):
        """机器人对话的应答文本。	
        :rtype: str
        """
        return self._ResponseText

    @ResponseText.setter
    def ResponseText(self, ResponseText):
        self._ResponseText = ResponseText

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
        self._DialogStatus = params.get("DialogStatus")
        self._BotName = params.get("BotName")
        self._IntentName = params.get("IntentName")
        if params.get("SlotInfoList") is not None:
            self._SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self._SlotInfoList.append(obj)
        self._InputText = params.get("InputText")
        if params.get("ResponseMessage") is not None:
            self._ResponseMessage = ResponseMessage()
            self._ResponseMessage._deserialize(params.get("ResponseMessage"))
        self._SessionAttributes = params.get("SessionAttributes")
        self._ResultType = params.get("ResultType")
        self._ResponseText = params.get("ResponseText")
        self._RequestId = params.get("RequestId")


class TextResetRequest(AbstractModel):
    """TextReset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotId: 机器人标识，用于定义抽象机器人。
        :type BotId: str
        :param _BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        :param _TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param _PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
        :type PlatformType: str
        :param _PlatformId: 当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识
        :type PlatformId: str
        """
        self._BotId = None
        self._BotEnv = None
        self._TerminalId = None
        self._PlatformType = None
        self._PlatformId = None

    @property
    def BotId(self):
        """机器人标识，用于定义抽象机器人。
        :rtype: str
        """
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def BotEnv(self):
        """机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :rtype: str
        """
        return self._BotEnv

    @BotEnv.setter
    def BotEnv(self, BotEnv):
        self._BotEnv = BotEnv

    @property
    def TerminalId(self):
        """终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :rtype: str
        """
        return self._TerminalId

    @TerminalId.setter
    def TerminalId(self, TerminalId):
        self._TerminalId = TerminalId

    @property
    def PlatformType(self):
        """平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
        :rtype: str
        """
        return self._PlatformType

    @PlatformType.setter
    def PlatformType(self, PlatformType):
        self._PlatformType = PlatformType

    @property
    def PlatformId(self):
        """当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识
        :rtype: str
        """
        return self._PlatformId

    @PlatformId.setter
    def PlatformId(self, PlatformId):
        self._PlatformId = PlatformId


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._BotEnv = params.get("BotEnv")
        self._TerminalId = params.get("TerminalId")
        self._PlatformType = params.get("PlatformType")
        self._PlatformId = params.get("PlatformId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextResetResponse(AbstractModel):
    """TextReset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DialogStatus: 当前会话状态{会话开始: START; 会话中: COUTINUE; 会话结束: COMPLETE}。
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param _BotName: 匹配到的机器人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param _IntentName: 匹配到的意图名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param _SlotInfoList: 槽位信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param _InputText: 原始的用户说法。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputText: str
        :param _ResponseMessage: 机器人应答。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
        :param _SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param _ResultType: 结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param _ResponseText: 机器人对话的应答文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseText: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DialogStatus = None
        self._BotName = None
        self._IntentName = None
        self._SlotInfoList = None
        self._InputText = None
        self._ResponseMessage = None
        self._SessionAttributes = None
        self._ResultType = None
        self._ResponseText = None
        self._RequestId = None

    @property
    def DialogStatus(self):
        """当前会话状态{会话开始: START; 会话中: COUTINUE; 会话结束: COMPLETE}。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DialogStatus

    @DialogStatus.setter
    def DialogStatus(self, DialogStatus):
        self._DialogStatus = DialogStatus

    @property
    def BotName(self):
        """匹配到的机器人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def IntentName(self):
        """匹配到的意图名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IntentName

    @IntentName.setter
    def IntentName(self, IntentName):
        self._IntentName = IntentName

    @property
    def SlotInfoList(self):
        """槽位信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SlotInfo
        """
        return self._SlotInfoList

    @SlotInfoList.setter
    def SlotInfoList(self, SlotInfoList):
        self._SlotInfoList = SlotInfoList

    @property
    def InputText(self):
        """原始的用户说法。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InputText

    @InputText.setter
    def InputText(self, InputText):
        self._InputText = InputText

    @property
    def ResponseMessage(self):
        """机器人应答。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
        """
        return self._ResponseMessage

    @ResponseMessage.setter
    def ResponseMessage(self, ResponseMessage):
        self._ResponseMessage = ResponseMessage

    @property
    def SessionAttributes(self):
        """透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionAttributes

    @SessionAttributes.setter
    def SessionAttributes(self, SessionAttributes):
        self._SessionAttributes = SessionAttributes

    @property
    def ResultType(self):
        """结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType

    @property
    def ResponseText(self):
        """机器人对话的应答文本。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ResponseText

    @ResponseText.setter
    def ResponseText(self, ResponseText):
        self._ResponseText = ResponseText

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
        self._DialogStatus = params.get("DialogStatus")
        self._BotName = params.get("BotName")
        self._IntentName = params.get("IntentName")
        if params.get("SlotInfoList") is not None:
            self._SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self._SlotInfoList.append(obj)
        self._InputText = params.get("InputText")
        if params.get("ResponseMessage") is not None:
            self._ResponseMessage = ResponseMessage()
            self._ResponseMessage._deserialize(params.get("ResponseMessage"))
        self._SessionAttributes = params.get("SessionAttributes")
        self._ResultType = params.get("ResultType")
        self._ResponseText = params.get("ResponseText")
        self._RequestId = params.get("RequestId")