# -*- coding: utf8 -*-
# Copyright (c) 2017-2025 Tencent. All Rights Reserved.
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


class ChatContent(AbstractModel):
    r"""智能诊断结果内容结构

    """

    def __init__(self):
        r"""
        :param _Role: 角色，可选值：
 - user
 - model_thinking
 - model_output
 - knowledge
        :type Role: str
        :param _Parts: 内容分片
注意：此字段可能返回 null，表示取不到有效值。
        :type Parts: list of ChatEventContentPart
        """
        self._Role = None
        self._Parts = None

    @property
    def Role(self):
        r"""角色，可选值：
 - user
 - model_thinking
 - model_output
 - knowledge
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Parts(self):
        r"""内容分片
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ChatEventContentPart
        """
        return self._Parts

    @Parts.setter
    def Parts(self, Parts):
        self._Parts = Parts


    def _deserialize(self, params):
        self._Role = params.get("Role")
        if params.get("Parts") is not None:
            self._Parts = []
            for item in params.get("Parts"):
                obj = ChatEventContentPart()
                obj._deserialize(item)
                self._Parts.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatEventContentPart(AbstractModel):
    r"""智能诊断时间内容分片结构

    """

    def __init__(self):
        r"""
        :param _Text: 文本内容（流式或完整）
        :type Text: str
        :param _FunctionCall: 函数调用信息
        :type FunctionCall: str
        :param _FunctionResponse: 函数返回结果
        :type FunctionResponse: str
        """
        self._Text = None
        self._FunctionCall = None
        self._FunctionResponse = None

    @property
    def Text(self):
        r"""文本内容（流式或完整）
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def FunctionCall(self):
        r"""函数调用信息
        :rtype: str
        """
        return self._FunctionCall

    @FunctionCall.setter
    def FunctionCall(self, FunctionCall):
        self._FunctionCall = FunctionCall

    @property
    def FunctionResponse(self):
        r"""函数返回结果
        :rtype: str
        """
        return self._FunctionResponse

    @FunctionResponse.setter
    def FunctionResponse(self, FunctionResponse):
        self._FunctionResponse = FunctionResponse


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._FunctionCall = params.get("FunctionCall")
        self._FunctionResponse = params.get("FunctionResponse")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudMateAgentRequest(AbstractModel):
    r"""CloudMateAgent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WorkspaceId: 空间 ID
        :type WorkspaceId: str
        :param _Message: 用户提问内容
        :type Message: str
        :param _ScenarioId: 场景 ID
        :type ScenarioId: str
        :param _SessionId: 会话 ID

- 填写上一次接口调用返回的会话 ID（SessionId），可在原有会话基础上继续对话
- 未填写会话 ID 时，创建新会话
        :type SessionId: str
        :param _Streaming: 是否使用流式响应，默认为 false，不启用流式响应
        :type Streaming: bool
        """
        self._WorkspaceId = None
        self._Message = None
        self._ScenarioId = None
        self._SessionId = None
        self._Streaming = None

    @property
    def WorkspaceId(self):
        r"""空间 ID
        :rtype: str
        """
        return self._WorkspaceId

    @WorkspaceId.setter
    def WorkspaceId(self, WorkspaceId):
        self._WorkspaceId = WorkspaceId

    @property
    def Message(self):
        r"""用户提问内容
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def ScenarioId(self):
        r"""场景 ID
        :rtype: str
        """
        return self._ScenarioId

    @ScenarioId.setter
    def ScenarioId(self, ScenarioId):
        self._ScenarioId = ScenarioId

    @property
    def SessionId(self):
        r"""会话 ID

- 填写上一次接口调用返回的会话 ID（SessionId），可在原有会话基础上继续对话
- 未填写会话 ID 时，创建新会话
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Streaming(self):
        r"""是否使用流式响应，默认为 false，不启用流式响应
        :rtype: bool
        """
        return self._Streaming

    @Streaming.setter
    def Streaming(self, Streaming):
        self._Streaming = Streaming


    def _deserialize(self, params):
        self._WorkspaceId = params.get("WorkspaceId")
        self._Message = params.get("Message")
        self._ScenarioId = params.get("ScenarioId")
        self._SessionId = params.get("SessionId")
        self._Streaming = params.get("Streaming")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloudMateAgentResponse(AbstractModel):
    r"""CloudMateAgent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SessionId: 会话ID，用于后续继续对话
        :type SessionId: str
        :param _Timestamp: unix时间戳
        :type Timestamp: int
        :param _Content: 诊断内容
        :type Content: :class:`tencentcloud.cloudmate.v20251030.models.ChatContent`
        :param _Partial: 是否为部分内容（流式场景）
        :type Partial: bool
        :param _TurnComplete: 本轮对话是否完成
        :type TurnComplete: bool
        :param _ErrorCode: 错误代码，无错误时无该字段
        :type ErrorCode: str
        :param _ErrorMessage: 错误详细信息，无错误时无该字段
        :type ErrorMessage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._SessionId = None
        self._Timestamp = None
        self._Content = None
        self._Partial = None
        self._TurnComplete = None
        self._ErrorCode = None
        self._ErrorMessage = None
        self._RequestId = None

    @property
    def SessionId(self):
        r"""会话ID，用于后续继续对话
        :rtype: str
        """
        return self._SessionId

    @SessionId.setter
    def SessionId(self, SessionId):
        self._SessionId = SessionId

    @property
    def Timestamp(self):
        r"""unix时间戳
        :rtype: int
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        r"""诊断内容
        :rtype: :class:`tencentcloud.cloudmate.v20251030.models.ChatContent`
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Partial(self):
        r"""是否为部分内容（流式场景）
        :rtype: bool
        """
        return self._Partial

    @Partial.setter
    def Partial(self, Partial):
        self._Partial = Partial

    @property
    def TurnComplete(self):
        r"""本轮对话是否完成
        :rtype: bool
        """
        return self._TurnComplete

    @TurnComplete.setter
    def TurnComplete(self, TurnComplete):
        self._TurnComplete = TurnComplete

    @property
    def ErrorCode(self):
        r"""错误代码，无错误时无该字段
        :rtype: str
        """
        return self._ErrorCode

    @ErrorCode.setter
    def ErrorCode(self, ErrorCode):
        self._ErrorCode = ErrorCode

    @property
    def ErrorMessage(self):
        r"""错误详细信息，无错误时无该字段
        :rtype: str
        """
        return self._ErrorMessage

    @ErrorMessage.setter
    def ErrorMessage(self, ErrorMessage):
        self._ErrorMessage = ErrorMessage

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SessionId = params.get("SessionId")
        self._Timestamp = params.get("Timestamp")
        if params.get("Content") is not None:
            self._Content = ChatContent()
            self._Content._deserialize(params.get("Content"))
        self._Partial = params.get("Partial")
        self._TurnComplete = params.get("TurnComplete")
        self._ErrorCode = params.get("ErrorCode")
        self._ErrorMessage = params.get("ErrorMessage")
        self._RequestId = params.get("RequestId")