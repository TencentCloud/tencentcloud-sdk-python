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
        :param BotName: 机器人名称
        :type BotName: str
        :param BotCnName: 机器人中文名称
        :type BotCnName: str
        """
        self.BotName = None
        self.BotCnName = None


    def _deserialize(self, params):
        self.BotName = params.get("BotName")
        self.BotCnName = params.get("BotCnName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBotResponse(AbstractModel):
    """CreateBot返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskRequestId: 任务ID
        :type TaskRequestId: str
        :param Msg: 任务信息
        :type Msg: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskRequestId = None
        self.Msg = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskRequestId = params.get("TaskRequestId")
        self.Msg = params.get("Msg")
        self.RequestId = params.get("RequestId")


class Group(AbstractModel):
    """Group是消息组的具体定义，当前包含ContentType、Url、Content三个字段。其中，具体的ContentType字段定义，参考互联网MIME类型标准。

    """

    def __init__(self):
        r"""
        :param ContentType: 消息类型参考互联网MIME类型标准，当前仅支持"text/plain"。	
        :type ContentType: str
        :param Url: 返回内容以链接形式提供。	
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param Content: 普通文本。	
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self.ContentType = None
        self.Url = None
        self.Content = None


    def _deserialize(self, params):
        self.ContentType = params.get("ContentType")
        self.Url = params.get("Url")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRequest(AbstractModel):
    """Reset请求参数结构体

    """

    def __init__(self):
        r"""
        :param BotId: 机器人标识
        :type BotId: str
        :param UserId: 子账户id，每个终端对应一个
        :type UserId: str
        :param BotVersion: 机器人版本号。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotVersion: str
        :param BotEnv: 机器人环境{dev:测试;release:线上}。BotVersion/BotEnv二选一：二者均填，仅BotVersion有效；二者均不填，默认BotEnv=dev
        :type BotEnv: str
        """
        self.BotId = None
        self.UserId = None
        self.BotVersion = None
        self.BotEnv = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.UserId = params.get("UserId")
        self.BotVersion = params.get("BotVersion")
        self.BotEnv = params.get("BotEnv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetResponse(AbstractModel):
    """Reset返回参数结构体

    """

    def __init__(self):
        r"""
        :param DialogStatus: 当前会话状态。取值:"start"/"continue"/"complete"
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 匹配到的机器人名称
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 匹配到的意图名称
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param ResponseText: 机器人回答
        :type ResponseText: str
        :param SlotInfoList: 语义解析的槽位结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param SessionAttributes: 透传字段
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param Question: 用户说法。该说法是用户原生说法或ASR识别结果，未经过语义优化
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param WaveUrl: tts合成pcm音频存储链接。仅当请求参数NeedTts=true时返回
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveUrl: str
        :param WaveData: tts合成的pcm音频。二进制数组经过base64编码(暂时不返回)
注意：此字段可能返回 null，表示取不到有效值。
        :type WaveData: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.ResponseText = None
        self.SlotInfoList = None
        self.SessionAttributes = None
        self.Question = None
        self.WaveUrl = None
        self.WaveData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        self.ResponseText = params.get("ResponseText")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.SessionAttributes = params.get("SessionAttributes")
        self.Question = params.get("Question")
        self.WaveUrl = params.get("WaveUrl")
        self.WaveData = params.get("WaveData")
        self.RequestId = params.get("RequestId")


class ResponseMessage(AbstractModel):
    """从TBP-RTS服务v1.3版本起，机器人以消息组列表的形式响应，消息组列表GroupList包含多组消息，用户根据需要对部分或全部消息组进行组合使用。

    """

    def __init__(self):
        r"""
        :param GroupList: 消息组列表。	
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: :class:`tencentcloud.tbp.v20190311.models.Group`
        """
        self.GroupList = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = Group()
            self.GroupList._deserialize(params.get("GroupList"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SlotInfo(AbstractModel):
    """槽位信息

    """

    def __init__(self):
        r"""
        :param SlotName: 槽位名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotName: str
        :param SlotValue: 槽位值
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotValue: str
        """
        self.SlotName = None
        self.SlotValue = None


    def _deserialize(self, params):
        self.SlotName = params.get("SlotName")
        self.SlotValue = params.get("SlotValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextProcessRequest(AbstractModel):
    """TextProcess请求参数结构体

    """

    def __init__(self):
        r"""
        :param BotId: 机器人标识，用于定义抽象机器人。
        :type BotId: str
        :param TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param InputText: 请求的文本。
        :type InputText: str
        :param BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        :param SessionAttributes: 透传字段，透传给用户自定义的WebService服务。
        :type SessionAttributes: str
        """
        self.BotId = None
        self.TerminalId = None
        self.InputText = None
        self.BotEnv = None
        self.SessionAttributes = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.TerminalId = params.get("TerminalId")
        self.InputText = params.get("InputText")
        self.BotEnv = params.get("BotEnv")
        self.SessionAttributes = params.get("SessionAttributes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextProcessResponse(AbstractModel):
    """TextProcess返回参数结构体

    """

    def __init__(self):
        r"""
        :param DialogStatus: 当前会话状态{会话开始: START; 会话中: COUTINUE; 会话结束: COMPLETE}。
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 匹配到的机器人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 匹配到的意图名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param SlotInfoList: 槽位信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param InputText: 原始的用户说法。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputText: str
        :param SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param ResponseText: 机器人对话的应答文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseText: str
        :param ResponseMessage: 机器人应答。	
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`tencentcloud.tbp.v20190311.models.ResponseMessage`
        :param ResultType: 结果类型 {中间逻辑出错:0; 任务型机器人:1; 问答型机器人:2; 闲聊型机器人:3; 未匹配上，返回预设兜底话术:5; 未匹配上，返回相似问题列表:6}。	
注意：此字段可能返回 null，表示取不到有效值。
        :type ResultType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.SlotInfoList = None
        self.InputText = None
        self.SessionAttributes = None
        self.ResponseText = None
        self.ResponseMessage = None
        self.ResultType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.InputText = params.get("InputText")
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResponseText = params.get("ResponseText")
        if params.get("ResponseMessage") is not None:
            self.ResponseMessage = ResponseMessage()
            self.ResponseMessage._deserialize(params.get("ResponseMessage"))
        self.ResultType = params.get("ResultType")
        self.RequestId = params.get("RequestId")


class TextResetRequest(AbstractModel):
    """TextReset请求参数结构体

    """

    def __init__(self):
        r"""
        :param BotId: 机器人标识，用于定义抽象机器人。
        :type BotId: str
        :param TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        """
        self.BotId = None
        self.TerminalId = None
        self.BotEnv = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.TerminalId = params.get("TerminalId")
        self.BotEnv = params.get("BotEnv")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextResetResponse(AbstractModel):
    """TextReset返回参数结构体

    """

    def __init__(self):
        r"""
        :param DialogStatus: 当前会话状态，取值："START"/"COUTINUE"/"COMPLETE"。
注意：此字段可能返回 null，表示取不到有效值。
        :type DialogStatus: str
        :param BotName: 匹配到的机器人名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type BotName: str
        :param IntentName: 匹配到的意图名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IntentName: str
        :param SlotInfoList: 槽位信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SlotInfoList: list of SlotInfo
        :param InputText: 原始的用户说法。
注意：此字段可能返回 null，表示取不到有效值。
        :type InputText: str
        :param SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
        :param ResponseText: 机器人对话的应答文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseText: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DialogStatus = None
        self.BotName = None
        self.IntentName = None
        self.SlotInfoList = None
        self.InputText = None
        self.SessionAttributes = None
        self.ResponseText = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DialogStatus = params.get("DialogStatus")
        self.BotName = params.get("BotName")
        self.IntentName = params.get("IntentName")
        if params.get("SlotInfoList") is not None:
            self.SlotInfoList = []
            for item in params.get("SlotInfoList"):
                obj = SlotInfo()
                obj._deserialize(item)
                self.SlotInfoList.append(obj)
        self.InputText = params.get("InputText")
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResponseText = params.get("ResponseText")
        self.RequestId = params.get("RequestId")