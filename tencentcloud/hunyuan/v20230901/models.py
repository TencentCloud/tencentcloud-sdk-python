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


class ChatCompletionsRequest(AbstractModel):
    """ChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称，可选值包括 hunyuan-lite、hunyuan-standard、hunyuan-standard-256K、hunyuan-pro、 hunyuan-code、 hunyuan-role、 hunyuan-functioncall、 hunyuan-vision。
各模型介绍请阅读 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 中的说明。

注意：
不同的模型计费不同，请根据 [购买指南](https://cloud.tencent.com/document/product/1729/97731) 按需调用。
        :type Model: str
        :param _Messages: 聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant、 tool。
其中，system 角色可选，如存在则必须位于列表的最开始。user（tool） 和 assistant 需交替出现（一问一答），以 user 提问开始，user（tool）提问结束，且 Content 不能为空。Role 的顺序示例：[system（可选） user assistant user assistant user ...]。
3. Messages 中 Content 总长度不能超过模型输入长度上限（可参考 [产品概述](https://cloud.tencent.com/document/product/1729/104753) 文档），超过则会截断最前面的内容，只保留尾部内容。
        :type Messages: list of Message
        :param _Stream: 流式调用开关。
说明：
1. 未传值时默认为非流式调用（false）。
2. 流式调用时以 SSE 协议增量返回结果（返回值取 Choices[n].Delta 中的值，需要拼接增量数据才能获得完整结果）。
3. 非流式调用时：
调用方式与普通 HTTP 请求无异。
接口响应耗时较长，**如需更低时延建议设置为 true**。
只返回一次最终结果（返回值取 Choices[n].Message 中的值）。

注意：
通过 SDK 调用时，流式和非流式调用需用**不同的方式**获取返回值，具体参考 SDK 中的注释或示例（在各语言 SDK 代码仓库的 examples/hunyuan/v20230901/ 目录中）。
        :type Stream: bool
        :param _StreamModeration: 流式输出审核开关。
说明：
1. 当使用流式输出（Stream 字段值为 true）时，该字段生效。
2. 输出审核有流式和同步两种模式，**流式模式首包响应更快**。未传值时默认为流式模式（true）。
3. 如果值为 true，将对输出内容进行分段审核，审核通过的内容流式输出返回。如果出现审核不过，响应中的 FinishReason 值为 sensitive。
4. 如果值为 false，则不使用流式输出审核，需要审核完所有输出内容后再返回结果。

注意：
当选择流式输出审核时，可能会出现部分内容已输出，但中间某一段响应中的 FinishReason 值为 sensitive，此时说明安全审核未通过。如果业务场景有实时文字上屏的需求，需要自行撤回已上屏的内容，并建议自定义替换为一条提示语，如 “这个问题我不方便回答，不如我们换个话题试试”，以保障终端体验。
        :type StreamModeration: bool
        :param _TopP: 说明：
1. 影响输出文本的多样性，取值越大，生成文本的多样性越强。
2. 取值区间为 [0.0, 1.0]，未传值时使用各模型推荐值。
3. 非必要不建议使用，不合理的取值会影响效果。
        :type TopP: float
        :param _Temperature: 说明：
1. 较高的数值会使输出更加随机，而较低的数值会使其更加集中和确定。
2. 取值区间为 [0.0, 2.0]，未传值时使用各模型推荐值。
3. 非必要不建议使用，不合理的取值会影响效果。
        :type Temperature: float
        :param _EnableEnhancement: 功能增强（如搜索）开关。
说明：
1. hunyuan-lite 无功能增强（如搜索）能力，该参数对 hunyuan-lite 版本不生效。
2. 未传值时默认打开开关。
3. 关闭时将直接由主模型生成回复内容，可以降低响应时延（对于流式输出时的首字时延尤为明显）。但在少数场景里，回复效果可能会下降。
4. 安全审核能力不属于功能增强范围，不受此字段影响。
        :type EnableEnhancement: bool
        :param _Tools: 可调用的工具列表，仅对 hunyuan-functioncall 模型生效。
        :type Tools: list of Tool
        :param _ToolChoice: 工具使用选项，可选值包括 none、auto、custom。
说明：
1. 仅对 hunyuan-functioncall 模型生效。
2. none：不调用工具；auto：模型自行选择生成回复或调用工具；custom：强制模型调用指定的工具。
3. 未设置时，默认值为auto
        :type ToolChoice: str
        :param _CustomTool: 强制模型调用指定的工具，当参数ToolChoice为custom时，此参数为必填
        :type CustomTool: :class:`tencentcloud.hunyuan.v20230901.models.Tool`
        :param _SearchInfo: 默认是false，在值为true且命中搜索时，接口会返回SearchInfo
        :type SearchInfo: bool
        """
        self._Model = None
        self._Messages = None
        self._Stream = None
        self._StreamModeration = None
        self._TopP = None
        self._Temperature = None
        self._EnableEnhancement = None
        self._Tools = None
        self._ToolChoice = None
        self._CustomTool = None
        self._SearchInfo = None

    @property
    def Model(self):
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Messages(self):
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Stream(self):
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def StreamModeration(self):
        return self._StreamModeration

    @StreamModeration.setter
    def StreamModeration(self, StreamModeration):
        self._StreamModeration = StreamModeration

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

    @property
    def EnableEnhancement(self):
        return self._EnableEnhancement

    @EnableEnhancement.setter
    def EnableEnhancement(self, EnableEnhancement):
        self._EnableEnhancement = EnableEnhancement

    @property
    def Tools(self):
        return self._Tools

    @Tools.setter
    def Tools(self, Tools):
        self._Tools = Tools

    @property
    def ToolChoice(self):
        return self._ToolChoice

    @ToolChoice.setter
    def ToolChoice(self, ToolChoice):
        self._ToolChoice = ToolChoice

    @property
    def CustomTool(self):
        return self._CustomTool

    @CustomTool.setter
    def CustomTool(self, CustomTool):
        self._CustomTool = CustomTool

    @property
    def SearchInfo(self):
        return self._SearchInfo

    @SearchInfo.setter
    def SearchInfo(self, SearchInfo):
        self._SearchInfo = SearchInfo


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Stream = params.get("Stream")
        self._StreamModeration = params.get("StreamModeration")
        self._TopP = params.get("TopP")
        self._Temperature = params.get("Temperature")
        self._EnableEnhancement = params.get("EnableEnhancement")
        if params.get("Tools") is not None:
            self._Tools = []
            for item in params.get("Tools"):
                obj = Tool()
                obj._deserialize(item)
                self._Tools.append(obj)
        self._ToolChoice = params.get("ToolChoice")
        if params.get("CustomTool") is not None:
            self._CustomTool = Tool()
            self._CustomTool._deserialize(params.get("CustomTool"))
        self._SearchInfo = params.get("SearchInfo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionsResponse(AbstractModel):
    """ChatCompletions返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Created: Unix 时间戳，单位为秒。
        :type Created: int
        :param _Usage: Token 统计信息。
按照总 Token 数量计费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.Usage`
        :param _Note: 免责声明。
        :type Note: str
        :param _Id: 本轮对话的 ID。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _ErrorMsg: 错误信息。
如果流式返回中服务处理异常，返回该错误信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: :class:`tencentcloud.hunyuan.v20230901.models.ErrorMsg`
        :param _ModerationLevel: 多轮会话风险审核，值为1时，表明存在信息安全风险，建议终止客户多轮会话。
        :type ModerationLevel: str
        :param _SearchInfo: 搜索结果信息
        :type SearchInfo: :class:`tencentcloud.hunyuan.v20230901.models.SearchInfo`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Note = None
        self._Id = None
        self._Choices = None
        self._ErrorMsg = None
        self._ModerationLevel = None
        self._SearchInfo = None
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
    def ModerationLevel(self):
        return self._ModerationLevel

    @ModerationLevel.setter
    def ModerationLevel(self, ModerationLevel):
        self._ModerationLevel = ModerationLevel

    @property
    def SearchInfo(self):
        return self._SearchInfo

    @SearchInfo.setter
    def SearchInfo(self, SearchInfo):
        self._SearchInfo = SearchInfo

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
        self._ModerationLevel = params.get("ModerationLevel")
        if params.get("SearchInfo") is not None:
            self._SearchInfo = SearchInfo()
            self._SearchInfo._deserialize(params.get("SearchInfo"))
        self._RequestId = params.get("RequestId")


class Choice(AbstractModel):
    """返回的回复, 支持多个

    """

    def __init__(self):
        r"""
        :param _FinishReason: 结束标志位，可能为 stop 或 sensitive。
stop 表示输出正常结束，sensitive 只在开启流式输出审核时会出现，表示安全审核未通过。
        :type FinishReason: str
        :param _Delta: 增量返回值，流式调用时使用该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Delta: :class:`tencentcloud.hunyuan.v20230901.models.Delta`
        :param _Message: 返回值，非流式调用时使用该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: :class:`tencentcloud.hunyuan.v20230901.models.Message`
        """
        self._FinishReason = None
        self._Delta = None
        self._Message = None

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

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        if params.get("Delta") is not None:
            self._Delta = Delta()
            self._Delta._deserialize(params.get("Delta"))
        if params.get("Message") is not None:
            self._Message = Message()
            self._Message._deserialize(params.get("Message"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Content(AbstractModel):
    """可以传入多种类型的内容，如图片或文本。当前只支持传入单张图片，传入多张图片时，以第一个图片为准。

    """

    def __init__(self):
        r"""
        :param _Type: 内容类型
注意：
当前只支持传入单张图片，传入多张图片时，以第一个图片为准。
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _Text: 当 Type 为 text 时使用，表示具体的文本内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _ImageUrl: 图片的url，当 Type 为 image_url 时使用，表示具体的图片内容
如"https://example.com/1.png" 或 图片的base64（注意 "data:image/jpeg;base64," 为必要部分）："data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAA......"
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageUrl: :class:`tencentcloud.hunyuan.v20230901.models.ImageUrl`
        """
        self._Type = None
        self._Text = None
        self._ImageUrl = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def ImageUrl(self):
        return self._ImageUrl

    @ImageUrl.setter
    def ImageUrl(self, ImageUrl):
        self._ImageUrl = ImageUrl


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Text = params.get("Text")
        if params.get("ImageUrl") is not None:
            self._ImageUrl = ImageUrl()
            self._ImageUrl._deserialize(params.get("ImageUrl"))
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
        :param _ToolCalls: 模型生成的工具调用，仅 hunyuan-functioncall 模型支持
说明：
对于每一次的输出值应该以Id为标识对Type、Name、Arguments字段进行合并。

注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCalls: list of ToolCall
        """
        self._Role = None
        self._Content = None
        self._ToolCalls = None

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

    @property
    def ToolCalls(self):
        return self._ToolCalls

    @ToolCalls.setter
    def ToolCalls(self, ToolCalls):
        self._ToolCalls = ToolCalls


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        if params.get("ToolCalls") is not None:
            self._ToolCalls = []
            for item in params.get("ToolCalls"):
                obj = ToolCall()
                obj._deserialize(item)
                self._ToolCalls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingData(AbstractModel):
    """Embedding 信息。

    """

    def __init__(self):
        r"""
        :param _Embedding: Embedding 信息，目前为 1024 维浮点数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Embedding: list of float
        :param _Index: 下标，目前不支持批量，因此固定为 0。
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Object: 目前固定为 "embedding"。
注意：此字段可能返回 null，表示取不到有效值。
        :type Object: str
        """
        self._Embedding = None
        self._Index = None
        self._Object = None

    @property
    def Embedding(self):
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Object(self):
        return self._Object

    @Object.setter
    def Object(self, Object):
        self._Object = Object


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        self._Index = params.get("Index")
        self._Object = params.get("Object")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingUsage(AbstractModel):
    """Token 使用计数。

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入 Token 数。
        :type PromptTokens: int
        :param _TotalTokens: 总 Token 数。
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def TotalTokens(self):
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._PromptTokens = params.get("PromptTokens")
        self._TotalTokens = params.get("TotalTokens")
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
        


class GetEmbeddingRequest(AbstractModel):
    """GetEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Input: 输入文本。总长度不超过 1024 个 Token，超过则会截断最后面的内容。
        :type Input: str
        """
        self._Input = None

    @property
    def Input(self):
        return self._Input

    @Input.setter
    def Input(self, Input):
        self._Input = Input


    def _deserialize(self, params):
        self._Input = params.get("Input")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetEmbeddingResponse(AbstractModel):
    """GetEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回的 Embedding 信息。当前不支持批量，所以数组元素数目为 1。
        :type Data: list of EmbeddingData
        :param _Usage: Token 使用计数，按照总 Token 数量收费。
        :type Usage: :class:`tencentcloud.hunyuan.v20230901.models.EmbeddingUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EmbeddingData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = EmbeddingUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class ImageUrl(AbstractModel):
    """具体的图片内容

    """

    def __init__(self):
        r"""
        :param _Url: 图片的 Url（以 http:// 或 https:// 开头）
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._Url = None

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoParam(AbstractModel):
    """logo参数

    """

    def __init__(self):
        r"""
        :param _LogoUrl: 水印url
        :type LogoUrl: str
        :param _LogoImage: 水印base64，url和base64二选一传入
        :type LogoImage: str
        :param _LogoRect: 水印图片位于融合结果图中的坐标，将按照坐标对标识图片进行位置和大小的拉伸匹配
        :type LogoRect: :class:`tencentcloud.hunyuan.v20230901.models.LogoRect`
        """
        self._LogoUrl = None
        self._LogoImage = None
        self._LogoRect = None

    @property
    def LogoUrl(self):
        return self._LogoUrl

    @LogoUrl.setter
    def LogoUrl(self, LogoUrl):
        self._LogoUrl = LogoUrl

    @property
    def LogoImage(self):
        return self._LogoImage

    @LogoImage.setter
    def LogoImage(self, LogoImage):
        self._LogoImage = LogoImage

    @property
    def LogoRect(self):
        return self._LogoRect

    @LogoRect.setter
    def LogoRect(self, LogoRect):
        self._LogoRect = LogoRect


    def _deserialize(self, params):
        self._LogoUrl = params.get("LogoUrl")
        self._LogoImage = params.get("LogoImage")
        if params.get("LogoRect") is not None:
            self._LogoRect = LogoRect()
            self._LogoRect._deserialize(params.get("LogoRect"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LogoRect(AbstractModel):
    """输入框

    """

    def __init__(self):
        r"""
        :param _X: 左上角X坐标
        :type X: int
        :param _Y: 左上角Y坐标
        :type Y: int
        :param _Width: 方框宽度
        :type Width: int
        :param _Height: 方框高度
        :type Height: int
        """
        self._X = None
        self._Y = None
        self._Width = None
        self._Height = None

    @property
    def X(self):
        return self._X

    @X.setter
    def X(self, X):
        self._X = X

    @property
    def Y(self):
        return self._Y

    @Y.setter
    def Y(self, Y):
        self._Y = Y

    @property
    def Width(self):
        return self._Width

    @Width.setter
    def Width(self, Width):
        self._Width = Width

    @property
    def Height(self):
        return self._Height

    @Height.setter
    def Height(self, Height):
        self._Height = Height


    def _deserialize(self, params):
        self._X = params.get("X")
        self._Y = params.get("Y")
        self._Width = params.get("Width")
        self._Height = params.get("Height")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Message(AbstractModel):
    """会话内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色，可选值包括 system、user、assistant、 tool。
        :type Role: str
        :param _Content: 文本内容
        :type Content: str
        :param _Contents: 多种类型内容（目前支持图片和文本），仅 hunyuan-vision 模型支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Contents: list of Content
        :param _ToolCallId: 当role为tool时传入，标识具体的函数调用
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCallId: str
        :param _ToolCalls: 模型生成的工具调用，仅 hunyuan-functioncall 模型支持
注意：此字段可能返回 null，表示取不到有效值。
        :type ToolCalls: list of ToolCall
        """
        self._Role = None
        self._Content = None
        self._Contents = None
        self._ToolCallId = None
        self._ToolCalls = None

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

    @property
    def Contents(self):
        return self._Contents

    @Contents.setter
    def Contents(self, Contents):
        self._Contents = Contents

    @property
    def ToolCallId(self):
        return self._ToolCallId

    @ToolCallId.setter
    def ToolCallId(self, ToolCallId):
        self._ToolCallId = ToolCallId

    @property
    def ToolCalls(self):
        return self._ToolCalls

    @ToolCalls.setter
    def ToolCalls(self, ToolCalls):
        self._ToolCalls = ToolCalls


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        if params.get("Contents") is not None:
            self._Contents = []
            for item in params.get("Contents"):
                obj = Content()
                obj._deserialize(item)
                self._Contents.append(obj)
        self._ToolCallId = params.get("ToolCallId")
        if params.get("ToolCalls") is not None:
            self._ToolCalls = []
            for item in params.get("ToolCalls"):
                obj = ToolCall()
                obj._deserialize(item)
                self._ToolCalls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanImageJobRequest(AbstractModel):
    """QueryHunyuanImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        """
        self._JobId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryHunyuanImageJobResponse(AbstractModel):
    """QueryHunyuanImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobStatusCode: 当前任务状态码：
1：等待中、2：运行中、4：处理失败、5：处理完成。
        :type JobStatusCode: str
        :param _JobStatusMsg: 当前任务状态：排队中、处理中、处理失败或者处理完成。

        :type JobStatusMsg: str
        :param _JobErrorCode: 任务处理失败错误码。

        :type JobErrorCode: str
        :param _JobErrorMsg: 任务处理失败错误信息。

        :type JobErrorMsg: str
        :param _ResultImage: 生成图 URL 列表，有效期1小时，请及时保存。

        :type ResultImage: list of str
        :param _ResultDetails: 结果 detail 数组，Success 代表成功。

        :type ResultDetails: list of str
        :param _RevisedPrompt: 对应 SubmitTextToImageProJob 接口中 Revise 参数。开启扩写时，返回扩写后的 prompt 文本。 如果关闭扩写，将直接返回原始输入的 prompt。
        :type RevisedPrompt: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobStatusCode = None
        self._JobStatusMsg = None
        self._JobErrorCode = None
        self._JobErrorMsg = None
        self._ResultImage = None
        self._ResultDetails = None
        self._RevisedPrompt = None
        self._RequestId = None

    @property
    def JobStatusCode(self):
        return self._JobStatusCode

    @JobStatusCode.setter
    def JobStatusCode(self, JobStatusCode):
        self._JobStatusCode = JobStatusCode

    @property
    def JobStatusMsg(self):
        return self._JobStatusMsg

    @JobStatusMsg.setter
    def JobStatusMsg(self, JobStatusMsg):
        self._JobStatusMsg = JobStatusMsg

    @property
    def JobErrorCode(self):
        return self._JobErrorCode

    @JobErrorCode.setter
    def JobErrorCode(self, JobErrorCode):
        self._JobErrorCode = JobErrorCode

    @property
    def JobErrorMsg(self):
        return self._JobErrorMsg

    @JobErrorMsg.setter
    def JobErrorMsg(self, JobErrorMsg):
        self._JobErrorMsg = JobErrorMsg

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def ResultDetails(self):
        return self._ResultDetails

    @ResultDetails.setter
    def ResultDetails(self, ResultDetails):
        self._ResultDetails = ResultDetails

    @property
    def RevisedPrompt(self):
        return self._RevisedPrompt

    @RevisedPrompt.setter
    def RevisedPrompt(self, RevisedPrompt):
        self._RevisedPrompt = RevisedPrompt

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobStatusCode = params.get("JobStatusCode")
        self._JobStatusMsg = params.get("JobStatusMsg")
        self._JobErrorCode = params.get("JobErrorCode")
        self._JobErrorMsg = params.get("JobErrorMsg")
        self._ResultImage = params.get("ResultImage")
        self._ResultDetails = params.get("ResultDetails")
        self._RevisedPrompt = params.get("RevisedPrompt")
        self._RequestId = params.get("RequestId")


class SearchInfo(AbstractModel):
    """搜索结果信息

    """

    def __init__(self):
        r"""
        :param _SearchResults: 搜索引文信息
注意：此字段可能返回 null，表示取不到有效值。
        :type SearchResults: list of SearchResult
        """
        self._SearchResults = None

    @property
    def SearchResults(self):
        return self._SearchResults

    @SearchResults.setter
    def SearchResults(self, SearchResults):
        self._SearchResults = SearchResults


    def _deserialize(self, params):
        if params.get("SearchResults") is not None:
            self._SearchResults = []
            for item in params.get("SearchResults"):
                obj = SearchResult()
                obj._deserialize(item)
                self._SearchResults.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResult(AbstractModel):
    """搜索引文信息

    """

    def __init__(self):
        r"""
        :param _Index: 搜索引文序号
注意：此字段可能返回 null，表示取不到有效值。
        :type Index: int
        :param _Title: 搜索引文标题
注意：此字段可能返回 null，表示取不到有效值。
        :type Title: str
        :param _Url: 搜索引文链接
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        """
        self._Index = None
        self._Title = None
        self._Url = None

    @property
    def Index(self):
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Title = params.get("Title")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanImageJobRequest(AbstractModel):
    """SubmitHunyuanImageJob请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本描述。 
算法将根据输入的文本智能生成与之相关的图像。 
不能为空，推荐使用中文。最多可传1024个 utf-8 字符。
        :type Prompt: str
        :param _Style: 绘画风格。
请在 [混元生图风格列表](https://cloud.tencent.com/document/product/1729/105846) 中选择期望的风格，传入风格编号。
不传默认不指定风格。
        :type Style: str
        :param _Resolution: 生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3），不传默认使用1024:1024。
        :type Resolution: str
        :param _Num: 图片生成数量。
支持1 ~ 4张，默认生成1张。
        :type Num: int
        :param _Seed: 随机种子，默认随机。
不传：随机种子生成。
正数：固定种子生成。
        :type Seed: int
        :param _Revise: prompt 扩写开关。1为开启，0为关闭，不传默认开启。
开启扩写后，将自动扩写原始输入的 prompt 并使用扩写后的 prompt 生成图片，返回生成图片结果时将一并返回扩写后的 prompt 文本。
如果关闭扩写，将直接使用原始输入的 prompt 生成图片。
建议开启，在多数场景下可提升生成图片效果、丰富生成图片细节。
        :type Revise: int
        :param _LogoAdd: 为生成结果图添加显式水印标识的开关，默认为1。  
1：添加。  
0：不添加。  
其他数值：默认按1处理。  
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        """
        self._Prompt = None
        self._Style = None
        self._Resolution = None
        self._Num = None
        self._Seed = None
        self._Revise = None
        self._LogoAdd = None
        self._LogoParam = None

    @property
    def Prompt(self):
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num

    @property
    def Seed(self):
        return self._Seed

    @Seed.setter
    def Seed(self, Seed):
        self._Seed = Seed

    @property
    def Revise(self):
        return self._Revise

    @Revise.setter
    def Revise(self, Revise):
        self._Revise = Revise

    @property
    def LogoAdd(self):
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._Style = params.get("Style")
        self._Resolution = params.get("Resolution")
        self._Num = params.get("Num")
        self._Seed = params.get("Seed")
        self._Revise = params.get("Revise")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitHunyuanImageJobResponse(AbstractModel):
    """SubmitHunyuanImageJob返回参数结构体

    """

    def __init__(self):
        r"""
        :param _JobId: 任务 ID。
        :type JobId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._JobId = None
        self._RequestId = None

    @property
    def JobId(self):
        return self._JobId

    @JobId.setter
    def JobId(self, JobId):
        self._JobId = JobId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._JobId = params.get("JobId")
        self._RequestId = params.get("RequestId")


class TextToImageLiteRequest(AbstractModel):
    """TextToImageLite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Prompt: 文本描述。
算法将根据输入的文本智能生成与之相关的图像。建议详细描述画面主体、细节、场景等，文本描述越丰富，生成效果越精美。
不能为空，推荐使用中文。最多可传256个 utf-8 字符。
        :type Prompt: str
        :param _NegativePrompt: 反向文本描述。
用于一定程度上从反面引导模型生成的走向，减少生成结果中出现描述内容的可能，但不能完全杜绝。
推荐使用中文。最多可传256个 utf-8 字符。
        :type NegativePrompt: str
        :param _Style: 绘画风格。
请在 [文生图轻量版风格列表](https://cloud.tencent.com/document/product/1729/108992) 中选择期望的风格，传入风格编号。不传默认使用201（日系动漫风格）。
        :type Style: str
        :param _Resolution: 生成图分辨率。
支持生成以下分辨率的图片：768:768（1:1）、768:1024（3:4）、1024:768（4:3）、1024:1024（1:1）、720:1280（9:16）、1280:720（16:9）、768:1280（3:5）、1280:768（5:3）、1080:1920（9:16）、1920:1080（16:9），不传默认使用768:768。
        :type Resolution: str
        :param _LogoAdd: 为生成结果图添加标识的开关，默认为1。
1：添加标识。
0：不添加标识。
其他数值：默认按0处理。
建议您使用显著标识来提示结果图使用了 AI 绘画技术，是 AI 生成的图片。
        :type LogoAdd: int
        :param _LogoParam: 标识内容设置。
默认在生成结果图右下角添加“图片由 AI 生成”字样，您可根据自身需要替换为其他的标识图片。
        :type LogoParam: :class:`tencentcloud.hunyuan.v20230901.models.LogoParam`
        :param _RspImgType: 返回图像方式（base64 或 url) ，二选一，默认为 base64。url 有效期为1小时。
        :type RspImgType: str
        """
        self._Prompt = None
        self._NegativePrompt = None
        self._Style = None
        self._Resolution = None
        self._LogoAdd = None
        self._LogoParam = None
        self._RspImgType = None

    @property
    def Prompt(self):
        return self._Prompt

    @Prompt.setter
    def Prompt(self, Prompt):
        self._Prompt = Prompt

    @property
    def NegativePrompt(self):
        return self._NegativePrompt

    @NegativePrompt.setter
    def NegativePrompt(self, NegativePrompt):
        self._NegativePrompt = NegativePrompt

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style

    @property
    def Resolution(self):
        return self._Resolution

    @Resolution.setter
    def Resolution(self, Resolution):
        self._Resolution = Resolution

    @property
    def LogoAdd(self):
        return self._LogoAdd

    @LogoAdd.setter
    def LogoAdd(self, LogoAdd):
        self._LogoAdd = LogoAdd

    @property
    def LogoParam(self):
        return self._LogoParam

    @LogoParam.setter
    def LogoParam(self, LogoParam):
        self._LogoParam = LogoParam

    @property
    def RspImgType(self):
        return self._RspImgType

    @RspImgType.setter
    def RspImgType(self, RspImgType):
        self._RspImgType = RspImgType


    def _deserialize(self, params):
        self._Prompt = params.get("Prompt")
        self._NegativePrompt = params.get("NegativePrompt")
        self._Style = params.get("Style")
        self._Resolution = params.get("Resolution")
        self._LogoAdd = params.get("LogoAdd")
        if params.get("LogoParam") is not None:
            self._LogoParam = LogoParam()
            self._LogoParam._deserialize(params.get("LogoParam"))
        self._RspImgType = params.get("RspImgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextToImageLiteResponse(AbstractModel):
    """TextToImageLite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ResultImage: 根据入参 RspImgType 填入不同，返回不同的内容。
如果传入 base64 则返回生成图 Base64 编码。
如果传入 url 则返回的生成图 URL , 有效期1小时，请及时保存。
        :type ResultImage: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ResultImage = None
        self._RequestId = None

    @property
    def ResultImage(self):
        return self._ResultImage

    @ResultImage.setter
    def ResultImage(self, ResultImage):
        self._ResultImage = ResultImage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ResultImage = params.get("ResultImage")
        self._RequestId = params.get("RequestId")


class Tool(AbstractModel):
    """用户指定模型使用的工具

    """

    def __init__(self):
        r"""
        :param _Type: 工具类型，当前只支持function
        :type Type: str
        :param _Function: 具体要调用的function
        :type Function: :class:`tencentcloud.hunyuan.v20230901.models.ToolFunction`
        """
        self._Type = None
        self._Function = None

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function


    def _deserialize(self, params):
        self._Type = params.get("Type")
        if params.get("Function") is not None:
            self._Function = ToolFunction()
            self._Function._deserialize(params.get("Function"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolCall(AbstractModel):
    """模型生成的工具调用

    """

    def __init__(self):
        r"""
        :param _Id: 工具调用id
        :type Id: str
        :param _Type: 工具调用类型，当前只支持function
        :type Type: str
        :param _Function: 具体的function调用
        :type Function: :class:`tencentcloud.hunyuan.v20230901.models.ToolCallFunction`
        """
        self._Id = None
        self._Type = None
        self._Function = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Function(self):
        return self._Function

    @Function.setter
    def Function(self, Function):
        self._Function = Function


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        if params.get("Function") is not None:
            self._Function = ToolCallFunction()
            self._Function._deserialize(params.get("Function"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolCallFunction(AbstractModel):
    """具体的function调用

    """

    def __init__(self):
        r"""
        :param _Name: function名称
        :type Name: str
        :param _Arguments: function参数，一般为json字符串
        :type Arguments: str
        """
        self._Name = None
        self._Arguments = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Arguments(self):
        return self._Arguments

    @Arguments.setter
    def Arguments(self, Arguments):
        self._Arguments = Arguments


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Arguments = params.get("Arguments")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ToolFunction(AbstractModel):
    """function定义

    """

    def __init__(self):
        r"""
        :param _Name: function名称，只能包含a-z，A-Z，0-9，\_或-
        :type Name: str
        :param _Parameters: function参数，一般为json字符串
        :type Parameters: str
        :param _Description: function的简单描述
        :type Description: str
        """
        self._Name = None
        self._Parameters = None
        self._Description = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Parameters(self):
        return self._Parameters

    @Parameters.setter
    def Parameters(self, Parameters):
        self._Parameters = Parameters

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Parameters = params.get("Parameters")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Usage(AbstractModel):
    """Token 数量

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入 Token 数量。
        :type PromptTokens: int
        :param _CompletionTokens: 输出 Token 数量。
        :type CompletionTokens: int
        :param _TotalTokens: 总 Token 数量。
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
        