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
        


class ResponseMessage(AbstractModel):
    """从TBP-RTS服务v1.3版本起，机器人以消息组列表的形式响应，消息组列表GroupList包含多组消息，用户根据需要对部分或全部消息组进行组合使用。

    """

    def __init__(self):
        r"""
        :param GroupList: 消息组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupList: list of Group
        """
        self.GroupList = None


    def _deserialize(self, params):
        if params.get("GroupList") is not None:
            self.GroupList = []
            for item in params.get("GroupList"):
                obj = Group()
                obj._deserialize(item)
                self.GroupList.append(obj)
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
        :param BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        :param TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param InputText: 请求的文本。
        :type InputText: str
        :param SessionAttributes: 透传字段，透传给用户自定义的WebService服务。
        :type SessionAttributes: str
        :param PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
        :type PlatformType: str
        :param PlatformId: 当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识
        :type PlatformId: str
        """
        self.BotId = None
        self.BotEnv = None
        self.TerminalId = None
        self.InputText = None
        self.SessionAttributes = None
        self.PlatformType = None
        self.PlatformId = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.BotEnv = params.get("BotEnv")
        self.TerminalId = params.get("TerminalId")
        self.InputText = params.get("InputText")
        self.SessionAttributes = params.get("SessionAttributes")
        self.PlatformType = params.get("PlatformType")
        self.PlatformId = params.get("PlatformId")
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
        :param ResponseMessage: 机器人应答。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
        :param SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
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
        self.ResponseMessage = None
        self.SessionAttributes = None
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
        if params.get("ResponseMessage") is not None:
            self.ResponseMessage = ResponseMessage()
            self.ResponseMessage._deserialize(params.get("ResponseMessage"))
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResultType = params.get("ResultType")
        self.RequestId = params.get("RequestId")


class TextResetRequest(AbstractModel):
    """TextReset请求参数结构体

    """

    def __init__(self):
        r"""
        :param BotId: 机器人标识，用于定义抽象机器人。
        :type BotId: str
        :param BotEnv: 机器人版本，取值"dev"或"release"，{调试版本：dev；线上版本：release}。
        :type BotEnv: str
        :param TerminalId: 终端标识，每个终端(或线程)对应一个，区分并发多用户。
        :type TerminalId: str
        :param PlatformType: 平台类型，{小程序：MiniProgram；小微：XiaoWei；公众号：OfficialAccount；企业微信: WXWork}。
        :type PlatformType: str
        :param PlatformId: 当PlatformType为微信公众号或企业微信时，传递对应微信公众号或企业微信的唯一标识
        :type PlatformId: str
        """
        self.BotId = None
        self.BotEnv = None
        self.TerminalId = None
        self.PlatformType = None
        self.PlatformId = None


    def _deserialize(self, params):
        self.BotId = params.get("BotId")
        self.BotEnv = params.get("BotEnv")
        self.TerminalId = params.get("TerminalId")
        self.PlatformType = params.get("PlatformType")
        self.PlatformId = params.get("PlatformId")
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
        :param ResponseMessage: 机器人应答。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseMessage: :class:`tencentcloud.tbp.v20190627.models.ResponseMessage`
        :param SessionAttributes: 透传字段，由用户自定义的WebService服务返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionAttributes: str
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
        self.ResponseMessage = None
        self.SessionAttributes = None
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
        if params.get("ResponseMessage") is not None:
            self.ResponseMessage = ResponseMessage()
            self.ResponseMessage._deserialize(params.get("ResponseMessage"))
        self.SessionAttributes = params.get("SessionAttributes")
        self.ResultType = params.get("ResultType")
        self.RequestId = params.get("RequestId")