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


class ChatProRequest(AbstractModel):
    """ChatPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 聊天上下文信息。
说明：
1.长度最多为40, 按对话时间从旧到新在数组中排列。
2.Message的Role当前可选值：user、assistant，其中，user和assistant需要交替出现(一问一答)，最后一个为user提问, 且Content不能为空。
3.Messages中Content总长度不超过16000token，超过则会截断最前面的内容，只保留尾部内容。建议不超过4000token。
        :type Messages: list of Message
        :param _TopP: 说明：
1.影响输出文本的多样性，取值越大，生成文本的多样性越强。
2.默认1.0，取值区间为[0.0, 1.0]。
3.非必要不建议使用, 不合理的取值会影响效果。
        :type TopP: float
        :param _Temperature: 说明：
1.较高的数值会使输出更加随机，而较低的数值会使其更加集中和确定。
2.默认1.0，取值区间为[0.0，2.0]。
3.非必要不建议使用,不合理的取值会影响效果。
        :type Temperature: float
        """
        self._Messages = None
        self._TopP = None
        self._Temperature = None

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def TopP(self):
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._TopP = params.get("TopP")
        self._Temperature = params.get("Temperature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatProResponse(AbstractModel):
    """ChatPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Created: unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: token统计信息。
按照总token数量计费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Note: 免责声明。
        :type Note: str
        :param _Id: 本轮对话的id。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _ErrorMsg: 错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Note = None
        self._Id = None
        self._Choices = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Created(self):
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._Note = params.get("Note")
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("ErrorMsg") is not None:
            self._ErrorMsg = ErrorMsg()
            self._ErrorMsg._deserialize(params.get("ErrorMsg"))
        self._RequestId = params.get("RequestId")


class ChatStdRequest(AbstractModel):
    """ChatStd请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 聊天上下文信息。
说明：
1.长度最多为40, 按对话时间从旧到新在数组中排列。
2.Message的Role当前可选值：user、assistant，其中，user和assistant需要交替出现(一问一答)，最后一个为user提问, 且Content不能为空。
3.Messages中Content总长度不超过16000token，超过则会截断最前面的内容，只保留尾部内容。建议不超过4000token。
        :type Messages: list of Message
        :param _TopP: 说明：
1.影响输出文本的多样性，取值越大，生成文本的多样性越强。
2.默认1.0，取值区间为[0.0, 1.0]。
3.非必要不建议使用, 不合理的取值会影响效果。
        :type TopP: float
        :param _Temperature: 说明：
1.较高的数值会使输出更加随机，而较低的数值会使其更加集中和确定。
2.默认1.0，取值区间为[0.0，2.0]。
3.非必要不建议使用,不合理的取值会影响效果。
        :type Temperature: float
        """
        self._Messages = None
        self._TopP = None
        self._Temperature = None

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def TopP(self):
        return self._TopP

    @TopP.setter
    def TopP(self, TopP):
        self._TopP = TopP

    @property
    def Temperature(self):
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._TopP = params.get("TopP")
        self._Temperature = params.get("Temperature")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatStdResponse(AbstractModel):
    """ChatStd返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Created: unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: token统计信息。
按照总token数量计费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Note: 免责声明。
        :type Note: str
        :param _Id: 本轮对话的id。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _ErrorMsg: 错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Note = None
        self._Id = None
        self._Choices = None
        self._ErrorMsg = None
        self._RequestId = None

    @property
    def Created(self):
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Note(self):
        return self._Note

    @Note.setter
    def Note(self, Note):
        self._Note = Note

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._Note = params.get("Note")
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        if params.get("ErrorMsg") is not None:
            self._ErrorMsg = ErrorMsg()
            self._ErrorMsg._deserialize(params.get("ErrorMsg"))
        self._RequestId = params.get("RequestId")


class Choice(AbstractModel):
    """返回的回复, 支持多个

    """

    def __init__(self):
        r"""
        :param _FinishReason: 流式结束标志位，为 stop 则表示尾包。
        :type FinishReason: str
        :param _Delta: 返回值。
        :type Delta: :class:`tencentcloud.hunyuan.v20230901.models.Delta`
        """
        self._FinishReason = None
        self._Delta = None

    @property
    def FinishReason(self):
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Delta(self):
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        if params.get("Delta") is not None:
            self._Delta = Delta()
            self._Delta._deserialize(params.get("Delta"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Delta(AbstractModel):
    """返回的内容（流式返回）

    """

    def __init__(self):
        r"""
        :param _Role: 角色名称。
        :type Role: str
        :param _Content: 内容详情。
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorMsg(AbstractModel):
    """运行时异常信息。

    """

    def __init__(self):
        r"""
        :param _Msg: 错误提示信息。
        :type Msg: str
        :param _Code: 错误码。
4000 服务内部异常。
4001 请求模型超时。

        :type Code: int
        """
        self._Msg = None
        self._Code = None

    @property
    def Msg(self):
        return self._Msg

    @Msg.setter
    def Msg(self, Msg):
        self._Msg = Msg

    @property
    def Code(self):
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Msg = params.get("Msg")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTokenCountRequest(AbstractModel):
    """GetTokenCount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 输入文本
        :type Prompt: str
        """
        self._Prompt = None

    @property
    def Prompt(self):
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetTokenCountResponse(AbstractModel):
    """GetTokenCount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TokenCount: token计数
        :type TokenCount: int
        :param _CharacterCount: 字符计数
        :type CharacterCount: int
        :param _Tokens: 切分后的列表
        :type Tokens: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TokenCount = None
        self._CharacterCount = None
        self._Tokens = None
        self._RequestId = None

    @property
    def TokenCount(self):
        return self._TokenCount

    @TokenCount.setter
    def TokenCount(self, TokenCount):
        self._TokenCount = TokenCount

    @property
    def CharacterCount(self):
        return self._CharacterCount

    @CharacterCount.setter
    def CharacterCount(self, CharacterCount):
        self._CharacterCount = CharacterCount

    @property
    def Tokens(self):
        return self._Tokens

    @Tokens.setter
    def Tokens(self, Tokens):
        self._Tokens = Tokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TokenCount = params.get("TokenCount")
        self._CharacterCount = params.get("CharacterCount")
        self._Tokens = params.get("Tokens")
        self._RequestId = params.get("RequestId")


class Message(AbstractModel):
    """会话内容,  按对话时间序排列，长度最多为40

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _Content: 消息的内容
        :type Content: str
        """
        self._Role = None
        self._Content = None

    @property
    def Role(self):
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    """token 数量

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入 token 数量。
        :type PromptTokens: int
        :param _CompletionTokens: 输出 token 数量。
        :type CompletionTokens: int
        :param _TotalTokens: 总 token 数量。
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._CompletionTokens = params.get("CompletionTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        