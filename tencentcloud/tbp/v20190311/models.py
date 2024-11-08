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


class CreateBotRequest(AbstractModel):
    """CreateBot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotName: 机器人名称
        :type BotName: str
        :param _BotCnName: 机器人中文名称
        :type BotCnName: str
        """
        self._BotName = None
        self._BotCnName = None

    @property
    def BotName(self):
        """机器人名称
        :rtype: str
        """
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def BotCnName(self):
        """机器人中文名称
        :rtype: str
        """
        return self._BotCnName

    @BotCnName.setter
    def BotCnName(self, BotCnName):
        self._BotCnName = BotCnName


    def _deserialize(self, params):
        self._BotName = params.get("BotName")
        self._BotCnName = params.get("BotCnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBotResponse(AbstractModel):
    """CreateBot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskRequestId: 任务ID
        :type TaskRequestId: str
        :param _Msg: 任务信息
        :type Msg: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskRequestId = None
        self._Msg = None
        self._RequestId = None

    @property
    def TaskRequestId(self):
        """任务ID
        :rtype: str
        """
        return self._TaskRequestId

    @TaskRequestId.setter
    def TaskRequestId(self, TaskRequestId):
        self._TaskRequestId = TaskRequestId

    @property
    def Msg(self):
        """任务信息
        :rtype: str
        """
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

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
        self._TaskRequestId = params.get("TaskRequestId")
        self._Msg = params.get("Msg")
        self._RequestId = params.get("RequestId")


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
        


class ResetRequest(AbstractModel):
    """Reset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotId: 机器人标识
        :type BotId: str
        :param _UserId: 子账户id，每个终端对应一个
        :type UserId: str
        :param _BotVersion: 机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotVersion: str
        :param _BotEnv: 机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotEnv: str
        """
        self._BotId = None
        self._UserId = None
        self._BotVersion = None
        self._BotEnv = None

    @property
    def BotId(self):
        """机器人标识
        :rtype: str
        """
        return self._BotId

    @BotId.setter
    def BotId(self, BotId):
        self._BotId = BotId

    @property
    def UserId(self):
        """子账户id，每个终端对应一个
        :rtype: str
        """
        return self._UserId

    @UserId.setter
    def UserId(self, UserId):
        self._UserId = UserId

    @property
    def BotVersion(self):
        """机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :rtype: str
        """
        return self._BotVersion

    @BotVersion.setter
    def BotVersion(self, BotVersion):
        self._BotVersion = BotVersion

    @property
    def BotEnv(self):
        """机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :rtype: str
        """
        return self._BotEnv

    @BotEnv.setter
    def BotEnv(self, BotEnv):
        self._BotEnv = BotEnv


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._UserId = params.get("UserId")
        self._BotVersion = params.get("BotVersion")
        self._BotEnv = params.get("BotEnv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetResponse(AbstractModel):
    """Reset返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DialogStatus: 当前会话状态。取值:"start"/"continue"/"complete"
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param _BotName: 匹配到的机器人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param _IntentName: 匹配到的意图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param _ResponseText: 机器人回答
        :type ResponseText: str
        :param _SlotInfoList: 语义解析的槽位结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param _SessionAttributes: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param _Question: 用户说法。该说法是用户原生说法或ASR识别结果，未经过语义优化
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _WaveUrl: tts合成pcm音频存储链接。仅当请求参数NeedTts=true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param _WaveData: tts合成的pcm音频。二进制数组经过base64编码(暂时不返回)
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DialogStatus = None
        self._BotName = None
        self._IntentName = None
        self._ResponseText = None
        self._SlotInfoList = None
        self._SessionAttributes = None
        self._Question = None
        self._WaveUrl = None
        self._WaveData = None
        self._RequestId = None

    @property
    def DialogStatus(self):
        """当前会话状态。取值:"start"/"continue"/"complete"
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DialogStatus

    @DialogStatus.setter
    def DialogStatus(self, DialogStatus):
        self._DialogStatus = DialogStatus

    @property
    def BotName(self):
        """匹配到的机器人名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BotName

    @BotName.setter
    def BotName(self, BotName):
        self._BotName = BotName

    @property
    def IntentName(self):
        """匹配到的意图名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IntentName

    @IntentName.setter
    def IntentName(self, IntentName):
        self._IntentName = IntentName

    @property
    def ResponseText(self):
        """机器人回答
        :rtype: str
        """
        return self._ResponseText

    @ResponseText.setter
    def ResponseText(self, ResponseText):
        self._ResponseText = ResponseText

    @property
    def SlotInfoList(self):
        """语义解析的槽位结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SlotInfo
        """
        return self._SlotInfoList

    @SlotInfoList.setter
    def SlotInfoList(self, SlotInfoList):
        self._SlotInfoList = SlotInfoList

    @property
    def SessionAttributes(self):
        """透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SessionAttributes

    @SessionAttributes.setter
    def SessionAttributes(self, SessionAttributes):
        self._SessionAttributes = SessionAttributes

    @property
    def Question(self):
        """用户说法。该说法是用户原生说法或ASR识别结果，未经过语义优化
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def WaveUrl(self):
        """tts合成pcm音频存储链接。仅当请求参数NeedTts=true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaveUrl

    @WaveUrl.setter
    def WaveUrl(self, WaveUrl):
        self._WaveUrl = WaveUrl

    @property
    def WaveData(self):
        """tts合成的pcm音频。二进制数组经过base64编码(暂时不返回)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WaveData

    @WaveData.setter
    def WaveData(self, WaveData):
        self._WaveData = WaveData

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
        self._ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self._SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self._SlotInfoList.append(obj)
        self._SessionAttributes = params.get("SessionAttributes")
        self._Question = params.get("Question")
        self._WaveUrl = params.get("WaveUrl")
        self._WaveData = params.get("WaveData")
        self._RequestId = params.get("RequestId")


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
        :param _TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param _InputText: 请求的文本。
        :type InputText: str
        :param _BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        :param _SessionAttributes: 透传字段，透传给用户自定义的WebService服务。
        :type SessionAttributes: str
        """
        self._BotId = None
        self._TerminalId = None
        self._InputText = None
        self._BotEnv = None
        self._SessionAttributes = None

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
    def BotEnv(self):
        """机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :rtype: str
        """
        return self._BotEnv

    @BotEnv.setter
    def BotEnv(self, BotEnv):
        self._BotEnv = BotEnv

    @property
    def SessionAttributes(self):
        """透传字段，透传给用户自定义的WebService服务。
        :rtype: str
        """
        return self._SessionAttributes

    @SessionAttributes.setter
    def SessionAttributes(self, SessionAttributes):
        self._SessionAttributes = SessionAttributes


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._TerminalId = params.get("TerminalId")
        self._InputText = params.get("InputText")
        self._BotEnv = params.get("BotEnv")
        self._SessionAttributes = params.get("SessionAttributes")
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
        :param _SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param _ResponseText: 机器人对话的应答文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseText: str
        :param _ResultType: 结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。	
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param _ResponseMessage: 机器人应答。	
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`tencentcloud.tbp.v20190311.models.ResponseMessage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DialogStatus = None
        self._BotName = None
        self._IntentName = None
        self._SlotInfoList = None
        self._InputText = None
        self._SessionAttributes = None
        self._ResponseText = None
        self._ResultType = None
        self._ResponseMessage = None
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
    def ResponseMessage(self):
        """机器人应答。	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.tbp.v20190311.models.ResponseMessage`
        """
        return self._ResponseMessage

    @ResponseMessage.setter
    def ResponseMessage(self, ResponseMessage):
        self._ResponseMessage = ResponseMessage

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
        self._SessionAttributes = params.get("SessionAttributes")
        self._ResponseText = params.get("ResponseText")
        self._ResultType = params.get("ResultType")
        if params.get("ResponseMessage") is not None:
            self._ResponseMessage = ResponseMessage()
            self._ResponseMessage._deserialize(params.get("ResponseMessage"))
        self._RequestId = params.get("RequestId")


class TextResetRequest(AbstractModel):
    """TextReset请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotId: 机器人标识，用于定义抽象机器人。
        :type BotId: str
        :param _TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param _BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        """
        self._BotId = None
        self._TerminalId = None
        self._BotEnv = None

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
    def TerminalId(self):
        """终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :rtype: str
        """
        return self._TerminalId

    @TerminalId.setter
    def TerminalId(self, TerminalId):
        self._TerminalId = TerminalId

    @property
    def BotEnv(self):
        """机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :rtype: str
        """
        return self._BotEnv

    @BotEnv.setter
    def BotEnv(self, BotEnv):
        self._BotEnv = BotEnv


    def _deserialize(self, params):
        self._BotId = params.get("BotId")
        self._TerminalId = params.get("TerminalId")
        self._BotEnv = params.get("BotEnv")
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
        :param _DialogStatus: 当前会话状态，取值："START"/"COUTINUE"/"COMPLETE"。
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
        :param _SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
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
        self._SessionAttributes = None
        self._ResponseText = None
        self._RequestId = None

    @property
    def DialogStatus(self):
        """当前会话状态，取值："START"/"COUTINUE"/"COMPLETE"。
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
        self._SessionAttributes = params.get("SessionAttributes")
        self._ResponseText = params.get("ResponseText")
        self._RequestId = params.get("RequestId")