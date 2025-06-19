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


class AttributeItem(AbstractModel):
    """属性信息

    """

    def __init__(self):
        r"""
        :param _AttributeId: 属性id
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeId: str
        :param _AttributeKey: 属性标识
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeKey: str
        :param _AttributeName: 属性名称
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeName: str
        :param _Labels: 标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Labels: list of AttributeLabelItem
        """
        self._AttributeId = None
        self._AttributeKey = None
        self._AttributeName = None
        self._Labels = None

    @property
    def AttributeId(self):
        """属性id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttributeId

    @AttributeId.setter
    def AttributeId(self, AttributeId):
        self._AttributeId = AttributeId

    @property
    def AttributeKey(self):
        """属性标识
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttributeKey

    @AttributeKey.setter
    def AttributeKey(self, AttributeKey):
        self._AttributeKey = AttributeKey

    @property
    def AttributeName(self):
        """属性名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttributeName

    @AttributeName.setter
    def AttributeName(self, AttributeName):
        self._AttributeName = AttributeName

    @property
    def Labels(self):
        """标签名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttributeLabelItem
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._AttributeId = params.get("AttributeId")
        self._AttributeKey = params.get("AttributeKey")
        self._AttributeName = params.get("AttributeName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabelItem()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeLabelItem(AbstractModel):
    """属性标签信息

    """

    def __init__(self):
        r"""
        :param _LabelId: 标签id
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelId: str
        :param _LabelName: 标签名称，最大80个英文字符
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelName: str
        """
        self._LabelId = None
        self._LabelName = None

    @property
    def LabelId(self):
        """标签id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelId

    @LabelId.setter
    def LabelId(self, LabelId):
        self._LabelId = LabelId

    @property
    def LabelName(self):
        """标签名称，最大80个英文字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LabelName

    @LabelName.setter
    def LabelName(self, LabelName):
        self._LabelName = LabelName


    def _deserialize(self, params):
        self._LabelId = params.get("LabelId")
        self._LabelName = params.get("LabelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttributeLabelReferItem(AbstractModel):
    """属性标签引用

    """

    def __init__(self):
        r"""
        :param _AttributeId: 属性id
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeId: str
        :param _LabelIds: 标签id
注意：此字段可能返回 null，表示取不到有效值。
        :type LabelIds: list of str
        """
        self._AttributeId = None
        self._LabelIds = None

    @property
    def AttributeId(self):
        """属性id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AttributeId

    @AttributeId.setter
    def AttributeId(self, AttributeId):
        self._AttributeId = AttributeId

    @property
    def LabelIds(self):
        """标签id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._LabelIds

    @LabelIds.setter
    def LabelIds(self, LabelIds):
        self._LabelIds = LabelIds


    def _deserialize(self, params):
        self._AttributeId = params.get("AttributeId")
        self._LabelIds = params.get("LabelIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatCompletionsRequest(AbstractModel):
    """ChatCompletions请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 模型名称
        :type Model: str
        :param _Messages: 聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant。
其中，system 角色可选，如存在则必须位于列表的最开始。user 和 assistant 需交替出现，以 user 提问开始，user 提问结束，Content 不能为空。Role 的顺序示例：[system（可选） user assistant user assistant user ...]。

        :type Messages: list of Message
        :param _Stream: 是否流式输出
        :type Stream: bool
        :param _Temperature: 控制生成的随机性，较高的值会产生更多样化的输出。
        :type Temperature: float
        :param _MaxTokens: 最大生成的token数量，默认为4096，最大可设置为16384
        :type MaxTokens: int
        :param _EnableSearch: 是否启用联网搜索
        :type EnableSearch: bool
        """
        self._Model = None
        self._Messages = None
        self._Stream = None
        self._Temperature = None
        self._MaxTokens = None
        self._EnableSearch = None

    @property
    def Model(self):
        """模型名称
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Messages(self):
        """聊天上下文信息。
说明：
1. 长度最多为 40，按对话时间从旧到新在数组中排列。
2. Message.Role 可选值：system、user、assistant。
其中，system 角色可选，如存在则必须位于列表的最开始。user 和 assistant 需交替出现，以 user 提问开始，user 提问结束，Content 不能为空。Role 的顺序示例：[system（可选） user assistant user assistant user ...]。

        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Stream(self):
        """是否流式输出
        :rtype: bool
        """
        return self._Stream

    @Stream.setter
    def Stream(self, Stream):
        self._Stream = Stream

    @property
    def Temperature(self):
        """控制生成的随机性，较高的值会产生更多样化的输出。
        :rtype: float
        """
        return self._Temperature

    @Temperature.setter
    def Temperature(self, Temperature):
        self._Temperature = Temperature

    @property
    def MaxTokens(self):
        """最大生成的token数量，默认为4096，最大可设置为16384
        :rtype: int
        """
        return self._MaxTokens

    @MaxTokens.setter
    def MaxTokens(self, MaxTokens):
        self._MaxTokens = MaxTokens

    @property
    def EnableSearch(self):
        """是否启用联网搜索
        :rtype: bool
        """
        return self._EnableSearch

    @EnableSearch.setter
    def EnableSearch(self, EnableSearch):
        self._EnableSearch = EnableSearch


    def _deserialize(self, params):
        self._Model = params.get("Model")
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Stream = params.get("Stream")
        self._Temperature = params.get("Temperature")
        self._MaxTokens = params.get("MaxTokens")
        self._EnableSearch = params.get("EnableSearch")
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
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.ChatUsage`
        :param _Id: 本次请求的 RequestId。
        :type Id: str
        :param _Choices: 回复内容。
        :type Choices: list of Choice
        :param _Model: 模型名称。
        :type Model: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._Created = None
        self._Usage = None
        self._Id = None
        self._Choices = None
        self._Model = None
        self._RequestId = None

    @property
    def Created(self):
        """Unix 时间戳，单位为秒。
        :rtype: int
        """
        return self._Created

    @Created.setter
    def Created(self, Created):
        self._Created = Created

    @property
    def Usage(self):
        """Token 统计信息。
按照总 Token 数量计费。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ChatUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Id(self):
        """本次请求的 RequestId。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Choices(self):
        """回复内容。
        :rtype: list of Choice
        """
        return self._Choices

    @Choices.setter
    def Choices(self, Choices):
        self._Choices = Choices

    @property
    def Model(self):
        """模型名称。
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Created = params.get("Created")
        if params.get("Usage") is not None:
            self._Usage = ChatUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._Id = params.get("Id")
        if params.get("Choices") is not None:
            self._Choices = []
            for item in params.get("Choices"):
                obj = Choice()
                obj._deserialize(item)
                self._Choices.append(obj)
        self._Model = params.get("Model")
        self._RequestId = params.get("RequestId")


class ChatUsage(AbstractModel):
    """消耗量

    """

    def __init__(self):
        r"""
        :param _PromptTokens: 输入token数
        :type PromptTokens: int
        :param _CompletionTokens: 输出token数
        :type CompletionTokens: int
        :param _TotalTokens: 总token数
        :type TotalTokens: int
        """
        self._PromptTokens = None
        self._CompletionTokens = None
        self._TotalTokens = None

    @property
    def PromptTokens(self):
        """输入token数
        :rtype: int
        """
        return self._PromptTokens

    @PromptTokens.setter
    def PromptTokens(self, PromptTokens):
        self._PromptTokens = PromptTokens

    @property
    def CompletionTokens(self):
        """输出token数
        :rtype: int
        """
        return self._CompletionTokens

    @CompletionTokens.setter
    def CompletionTokens(self, CompletionTokens):
        self._CompletionTokens = CompletionTokens

    @property
    def TotalTokens(self):
        """总token数
        :rtype: int
        """
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
        


class Choice(AbstractModel):
    """返回的回复, 支持多个

    """

    def __init__(self):
        r"""
        :param _FinishReason: 结束标志位，可能为 stop、 content_filter。
stop 表示输出正常结束。
content_filter 只在开启流式输出审核时会出现，表示安全审核未通过。
        :type FinishReason: str
        :param _Delta: 增量返回值，流式调用时使用该字段。
        :type Delta: :class:`tencentcloud.lkeap.v20240522.models.Delta`
        :param _Message: 返回值，非流式调用时使用该字段。
        :type Message: :class:`tencentcloud.lkeap.v20240522.models.Message`
        :param _Index: 索引值，流式调用时使用该字段。
        :type Index: int
        """
        self._FinishReason = None
        self._Delta = None
        self._Message = None
        self._Index = None

    @property
    def FinishReason(self):
        """结束标志位，可能为 stop、 content_filter。
stop 表示输出正常结束。
content_filter 只在开启流式输出审核时会出现，表示安全审核未通过。
        :rtype: str
        """
        return self._FinishReason

    @FinishReason.setter
    def FinishReason(self, FinishReason):
        self._FinishReason = FinishReason

    @property
    def Delta(self):
        """增量返回值，流式调用时使用该字段。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Delta`
        """
        return self._Delta

    @Delta.setter
    def Delta(self, Delta):
        self._Delta = Delta

    @property
    def Message(self):
        """返回值，非流式调用时使用该字段。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Message`
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Index(self):
        """索引值，流式调用时使用该字段。
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index


    def _deserialize(self, params):
        self._FinishReason = params.get("FinishReason")
        if params.get("Delta") is not None:
            self._Delta = Delta()
            self._Delta._deserialize(params.get("Delta"))
        if params.get("Message") is not None:
            self._Message = Message()
            self._Message._deserialize(params.get("Message"))
        self._Index = params.get("Index")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAttributeLabelRequest(AbstractModel):
    """CreateAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _AttributeKey: 属性标识，最大40个英文字符，如style
        :type AttributeKey: str
        :param _AttributeName: 属性名称，最大80个英文字符，如风格
        :type AttributeName: str
        :param _Labels: 属性标签信息
        :type Labels: list of AttributeLabelItem
        """
        self._KnowledgeBaseId = None
        self._AttributeKey = None
        self._AttributeName = None
        self._Labels = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def AttributeKey(self):
        """属性标识，最大40个英文字符，如style
        :rtype: str
        """
        return self._AttributeKey

    @AttributeKey.setter
    def AttributeKey(self, AttributeKey):
        self._AttributeKey = AttributeKey

    @property
    def AttributeName(self):
        """属性名称，最大80个英文字符，如风格
        :rtype: str
        """
        return self._AttributeName

    @AttributeName.setter
    def AttributeName(self, AttributeName):
        self._AttributeName = AttributeName

    @property
    def Labels(self):
        """属性标签信息
        :rtype: list of AttributeLabelItem
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._AttributeKey = params.get("AttributeKey")
        self._AttributeName = params.get("AttributeName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabelItem()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAttributeLabelResponse(AbstractModel):
    """CreateAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class CreateKnowledgeBaseRequest(AbstractModel):
    """CreateKnowledgeBase请求参数结构体

    """


class CreateKnowledgeBaseResponse(AbstractModel):
    """CreateKnowledgeBase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KnowledgeBaseId = None
        self._RequestId = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

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
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._RequestId = params.get("RequestId")


class CreateQARequest(AbstractModel):
    """CreateQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _Question: 问题，最大1000个英文字符
        :type Question: str
        :param _Answer: 答案，最大4000个英文字符
        :type Answer: str
        :param _AttributeLabels: 属性标签
        :type AttributeLabels: list of AttributeLabelReferItem
        """
        self._KnowledgeBaseId = None
        self._Question = None
        self._Answer = None
        self._AttributeLabels = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def Question(self):
        """问题，最大1000个英文字符
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """答案，最大4000个英文字符
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AttributeLabels(self):
        """属性标签
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateQAResponse(AbstractModel):
    """CreateQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _QaId: 问答对ID
        :type QaId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._QaId = None
        self._RequestId = None

    @property
    def QaId(self):
        """问答对ID
        :rtype: str
        """
        return self._QaId

    @QaId.setter
    def QaId(self, QaId):
        self._QaId = QaId

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
        self._QaId = params.get("QaId")
        self._RequestId = params.get("RequestId")


class CreateReconstructDocumentFlowConfig(AbstractModel):
    """创建智能文档解析任务的配置信息

    """

    def __init__(self):
        r"""
        :param _TableResultType: Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为0
        :type TableResultType: str
        :param _ResultType: 智能文档解析返回结果的格式
0：只返回全文MD；
1：只返回每一页的OCR原始Json；
2：只返回每一页的MD，
3：返回全文MD + 每一页的OCR原始Json；
4：返回全文MD + 每一页的MD，
默认值为0
        :type ResultType: str
        """
        self._TableResultType = None
        self._ResultType = None

    @property
    def TableResultType(self):
        """Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为0
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        """智能文档解析返回结果的格式
0：只返回全文MD；
1：只返回每一页的OCR原始Json；
2：只返回每一页的MD，
3：返回全文MD + 每一页的OCR原始Json；
4：返回全文MD + 每一页的MD，
默认值为0
        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        self._ResultType = ResultType


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowRequest(AbstractModel):
    """CreateReconstructDocumentFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。

**支持的文件类型：**
- `PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`、`BMP`、`GIF`、`WEBP`、`HEIC`、`EPS`、`ICNS`、`IM`、`PCX`、`PPM`、`TIFF`、`XBM`、`HEIF`、`JP2`

**支持的文件大小：**
 - `PDF` 最大300M
 - `DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M
 - `TXT`、`MD` 最大10M
 - 其他 最大20M

        :type FileType: str
        :param _FileUrl: 文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _FileBase64: 文件的 Base64 值。
支持的文件类型： PNG、JPG、JPEG、PDF、GIF、BMP、TIFF
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileStartPageNumber: 文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :type FileEndPageNumber: int
        :param _Config: 创建文档解析任务配置信息。
        :type Config: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        """文件类型。

**支持的文件类型：**
- `PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`、`BMP`、`GIF`、`WEBP`、`HEIC`、`EPS`、`ICNS`、`IM`、`PCX`、`PPM`、`TIFF`、`XBM`、`HEIF`、`JP2`

**支持的文件大小：**
 - `PDF` 最大300M
 - `DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M
 - `TXT`、`MD` 最大10M
 - 其他 最大20M

        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileBase64(self):
        """文件的 Base64 值。
支持的文件类型： PNG、JPG、JPEG、PDF、GIF、BMP、TIFF
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        """文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        """文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        """创建文档解析任务配置信息。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateReconstructDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateReconstructDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateReconstructDocumentFlowResponse(AbstractModel):
    """CreateReconstructDocumentFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务唯一id。30天内可以通过GetReconstructDocumentResult接口查询TaskId对应的处理结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务唯一id。30天内可以通过GetReconstructDocumentResult接口查询TaskId对应的处理结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class CreateSplitDocumentFlowConfig(AbstractModel):
    """创建智能文档拆分任务的配置信息

    """

    def __init__(self):
        r"""
        :param _TableResultType: Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为
        :type TableResultType: str
        :param _ResultType: 智能文档解析返回结果的格式
0：只返回全文MD；
1：只返回每一页的OCR原始Json；
2：只返回每一页的MD，
3：返回全文MD + 每一页的OCR原始Json；
4：返回全文MD + 每一页的MD，
默认值为3（返回全文MD + 每一页的OCR原始Json）


        :type ResultType: str
        :param _EnableMllm: 是否开启mllm
        :type EnableMllm: bool
        :param _MaxChunkSize: 最大分片长度
        :type MaxChunkSize: int
        """
        self._TableResultType = None
        self._ResultType = None
        self._EnableMllm = None
        self._MaxChunkSize = None

    @property
    def TableResultType(self):
        warnings.warn("parameter `TableResultType` is deprecated", DeprecationWarning) 

        """Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        warnings.warn("parameter `TableResultType` is deprecated", DeprecationWarning) 

        self._TableResultType = TableResultType

    @property
    def ResultType(self):
        warnings.warn("parameter `ResultType` is deprecated", DeprecationWarning) 

        """智能文档解析返回结果的格式
0：只返回全文MD；
1：只返回每一页的OCR原始Json；
2：只返回每一页的MD，
3：返回全文MD + 每一页的OCR原始Json；
4：返回全文MD + 每一页的MD，
默认值为3（返回全文MD + 每一页的OCR原始Json）


        :rtype: str
        """
        return self._ResultType

    @ResultType.setter
    def ResultType(self, ResultType):
        warnings.warn("parameter `ResultType` is deprecated", DeprecationWarning) 

        self._ResultType = ResultType

    @property
    def EnableMllm(self):
        """是否开启mllm
        :rtype: bool
        """
        return self._EnableMllm

    @EnableMllm.setter
    def EnableMllm(self, EnableMllm):
        self._EnableMllm = EnableMllm

    @property
    def MaxChunkSize(self):
        """最大分片长度
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._ResultType = params.get("ResultType")
        self._EnableMllm = params.get("EnableMllm")
        self._MaxChunkSize = params.get("MaxChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSplitDocumentFlowRequest(AbstractModel):
    """CreateSplitDocumentFlow请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。

**支持的文件类型：**
- `PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`

**支持的文件大小：**
 - `PDF` 最大300M
 - `DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M
 - `TXT`、`MD` 最大10M
 - 其他 最大20M

        :type FileType: str
        :param _FileUrl: 文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _FileName: 文件名，可选。
**需带文件类型后缀**，当文件名无法从传入的`FileUrl`获取时需要通过该字段来明确。
        :type FileName: str
        :param _FileBase64: 文件的 Base64 值。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileStartPageNumber: 文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :type FileEndPageNumber: int
        :param _Config: 文档拆分任务的配置信息。

        :type Config: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileName = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        """文件类型。

**支持的文件类型：**
- `PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`、`HTML`、`EPUB`

**支持的文件大小：**
 - `PDF` 最大300M
 - `DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M
 - `TXT`、`MD` 最大10M
 - 其他 最大20M

        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileName(self):
        """文件名，可选。
**需带文件类型后缀**，当文件名无法从传入的`FileUrl`获取时需要通过该字段来明确。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileBase64(self):
        warnings.warn("parameter `FileBase64` is deprecated", DeprecationWarning) 

        """文件的 Base64 值。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        warnings.warn("parameter `FileBase64` is deprecated", DeprecationWarning) 

        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        """文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        """文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        """文档拆分任务的配置信息。

        :rtype: :class:`tencentcloud.lkeap.v20240522.models.CreateSplitDocumentFlowConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileName = params.get("FileName")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = CreateSplitDocumentFlowConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSplitDocumentFlowResponse(AbstractModel):
    """CreateSplitDocumentFlow返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 拆分任务唯一ID。
30天内可以通过`GetSplitDocumentResult`接口查询TaskId对应的拆分结果。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """拆分任务唯一ID。
30天内可以通过`GetSplitDocumentResult`接口查询TaskId对应的拆分结果。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DeleteAttributeLabelsRequest(AbstractModel):
    """DeleteAttributeLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _AttributeIds: 属性ID
        :type AttributeIds: list of str
        """
        self._KnowledgeBaseId = None
        self._AttributeIds = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def AttributeIds(self):
        """属性ID
        :rtype: list of str
        """
        return self._AttributeIds

    @AttributeIds.setter
    def AttributeIds(self, AttributeIds):
        self._AttributeIds = AttributeIds


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._AttributeIds = params.get("AttributeIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAttributeLabelsResponse(AbstractModel):
    """DeleteAttributeLabels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteDocsRequest(AbstractModel):
    """DeleteDocs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _DocIds: 文档ID列表。支持批量删除，数量不超过100
        :type DocIds: list of str
        """
        self._KnowledgeBaseId = None
        self._DocIds = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def DocIds(self):
        """文档ID列表。支持批量删除，数量不超过100
        :rtype: list of str
        """
        return self._DocIds

    @DocIds.setter
    def DocIds(self, DocIds):
        self._DocIds = DocIds


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._DocIds = params.get("DocIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDocsResponse(AbstractModel):
    """DeleteDocs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteKnowledgeBaseRequest(AbstractModel):
    """DeleteKnowledgeBase请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        """
        self._KnowledgeBaseId = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteKnowledgeBaseResponse(AbstractModel):
    """DeleteKnowledgeBase返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class DeleteQAsRequest(AbstractModel):
    """DeleteQAs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _QaIds: 问答对ID列表。支持批量删除，数量不超过100
        :type QaIds: list of str
        """
        self._KnowledgeBaseId = None
        self._QaIds = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def QaIds(self):
        """问答对ID列表。支持批量删除，数量不超过100
        :rtype: list of str
        """
        return self._QaIds

    @QaIds.setter
    def QaIds(self, QaIds):
        self._QaIds = QaIds


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._QaIds = params.get("QaIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteQAsResponse(AbstractModel):
    """DeleteQAs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class Delta(AbstractModel):
    """返回的内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色名称。
        :type Role: str
        :param _Content: 内容详情。
        :type Content: str
        :param _ReasoningContent: 思维链内容。 ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :type ReasoningContent: str
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None

    @property
    def Role(self):
        """角色名称。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容详情。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        """思维链内容。 ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ReasoningContent = params.get("ReasoningContent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocRequest(AbstractModel):
    """DescribeDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _DocId: 文档ID
        :type DocId: str
        """
        self._KnowledgeBaseId = None
        self._DocId = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def DocId(self):
        """文档ID
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._DocId = params.get("DocId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDocResponse(AbstractModel):
    """DescribeDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocId: 文档ID
        :type DocId: str
        :param _Status: 状态，

- Uploading  上传中  
- Auditing 审核中
- Parsing 解析中  
- ParseFailed 解析失败
- Indexing 创建索引中  
- IndexFailed 创建索引失败
- Success  发布成功
- Failed  失败
        :type Status: str
        :param _FileName: 文件名
        :type FileName: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _AttributeLabels: 属性标签
        :type AttributeLabels: list of AttributeLabelReferItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocId = None
        self._Status = None
        self._FileName = None
        self._UpdateTime = None
        self._AttributeLabels = None
        self._RequestId = None

    @property
    def DocId(self):
        """文档ID
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def Status(self):
        """状态，

- Uploading  上传中  
- Auditing 审核中
- Parsing 解析中  
- ParseFailed 解析失败
- Indexing 创建索引中  
- IndexFailed 创建索引失败
- Success  发布成功
- Failed  失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AttributeLabels(self):
        """属性标签
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels

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
        self._DocId = params.get("DocId")
        self._Status = params.get("Status")
        self._FileName = params.get("FileName")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        self._RequestId = params.get("RequestId")


class DocItem(AbstractModel):
    """离线文档列表回包

    """

    def __init__(self):
        r"""
        :param _DocId: 文档id
注意：此字段可能返回 null，表示取不到有效值。
        :type DocId: str
        :param _Status:  状态，
- Uploading  上传中  
- Auditing 审核中
- Parsing 解析中  
- ParseFailed 解析失败
- Indexing 创建索引中  
- IndexFailed 创建索引失败
- Success  发布成功
- Failed  失败
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _FileName: 文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileName: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _AttributeLabels: 属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeLabels: list of AttributeLabelReferItem
        """
        self._DocId = None
        self._Status = None
        self._FileName = None
        self._UpdateTime = None
        self._AttributeLabels = None

    @property
    def DocId(self):
        """文档id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

    @property
    def Status(self):
        """ 状态，
- Uploading  上传中  
- Auditing 审核中
- Parsing 解析中  
- ParseFailed 解析失败
- Indexing 创建索引中  
- IndexFailed 创建索引失败
- Success  发布成功
- Failed  失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FileName(self):
        """文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def AttributeLabels(self):
        """属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels


    def _deserialize(self, params):
        self._DocId = params.get("DocId")
        self._Status = params.get("Status")
        self._FileName = params.get("FileName")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DocumentUsage(AbstractModel):
    """文档拆分任务的用量

    """

    def __init__(self):
        r"""
        :param _PageNumber: 文档拆分任务的页数
        :type PageNumber: int
        :param _TotalToken: 文档拆分任务消耗的总token数
        :type TotalToken: int
        :param _TotalTokens: 文档拆分任务消耗的总token数
        :type TotalTokens: int
        :param _SplitTokens: 拆分消耗的token数
        :type SplitTokens: int
        :param _MllmTokens: mllm消耗的token数
        :type MllmTokens: int
        """
        self._PageNumber = None
        self._TotalToken = None
        self._TotalTokens = None
        self._SplitTokens = None
        self._MllmTokens = None

    @property
    def PageNumber(self):
        """文档拆分任务的页数
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def TotalToken(self):
        warnings.warn("parameter `TotalToken` is deprecated", DeprecationWarning) 

        """文档拆分任务消耗的总token数
        :rtype: int
        """
        return self._TotalToken

    @TotalToken.setter
    def TotalToken(self, TotalToken):
        warnings.warn("parameter `TotalToken` is deprecated", DeprecationWarning) 

        self._TotalToken = TotalToken

    @property
    def TotalTokens(self):
        """文档拆分任务消耗的总token数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens

    @property
    def SplitTokens(self):
        """拆分消耗的token数
        :rtype: int
        """
        return self._SplitTokens

    @SplitTokens.setter
    def SplitTokens(self, SplitTokens):
        self._SplitTokens = SplitTokens

    @property
    def MllmTokens(self):
        """mllm消耗的token数
        :rtype: int
        """
        return self._MllmTokens

    @MllmTokens.setter
    def MllmTokens(self, MllmTokens):
        self._MllmTokens = MllmTokens


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        self._TotalToken = params.get("TotalToken")
        self._TotalTokens = params.get("TotalTokens")
        self._SplitTokens = params.get("SplitTokens")
        self._MllmTokens = params.get("MllmTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EmbeddingObject(AbstractModel):
    """向量

    """

    def __init__(self):
        r"""
        :param _Embedding: 向量
        :type Embedding: list of float
        """
        self._Embedding = None

    @property
    def Embedding(self):
        """向量
        :rtype: list of float
        """
        return self._Embedding

    @Embedding.setter
    def Embedding(self, Embedding):
        self._Embedding = Embedding


    def _deserialize(self, params):
        self._Embedding = params.get("Embedding")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCharacterUsageRequest(AbstractModel):
    """GetCharacterUsage请求参数结构体

    """


class GetCharacterUsageResponse(AbstractModel):
    """GetCharacterUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Used: 已用字符数
        :type Used: int
        :param _Total: 可用字符数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Used = None
        self._Total = None
        self._RequestId = None

    @property
    def Used(self):
        """已用字符数
        :rtype: int
        """
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Total(self):
        """可用字符数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

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
        self._Used = params.get("Used")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class GetEmbeddingRequest(AbstractModel):
    """GetEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Model: 说明：选择生成向量的模型
备注：仅一个模型可选
        :type Model: str
        :param _Inputs: 说明：需要 embedding 的文本
备注：单条query最多2000个字符，总条数最多7条
        :type Inputs: list of str
        """
        self._Model = None
        self._Inputs = None

    @property
    def Model(self):
        """说明：选择生成向量的模型
备注：仅一个模型可选
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model

    @property
    def Inputs(self):
        """说明：需要 embedding 的文本
备注：单条query最多2000个字符，总条数最多7条
        :rtype: list of str
        """
        return self._Inputs

    @Inputs.setter
    def Inputs(self, Inputs):
        self._Inputs = Inputs


    def _deserialize(self, params):
        self._Model = params.get("Model")
        self._Inputs = params.get("Inputs")
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
        :param _Data: 特征
        :type Data: list of EmbeddingObject
        :param _Usage: 消耗量，返回TotalToken
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Usage = None
        self._RequestId = None

    @property
    def Data(self):
        """特征
        :rtype: list of EmbeddingObject
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Usage(self):
        """消耗量，返回TotalToken
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = EmbeddingObject()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class GetReconstructDocumentResultRequest(AbstractModel):
    """GetReconstructDocumentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 解析任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """解析任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetReconstructDocumentResultResponse(AbstractModel):
    """GetReconstructDocumentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。
- `Success`：执行完成
- `Processing`：执行中
-  `Pause`: 暂停
-  `Failed`：执行失败
-  `WaitExecute`：等待执行
        :type Status: str
        :param _DocumentRecognizeResultUrl: 解析结果的临时下载地址。文件类型为zip压缩包，下载链接有效期30分钟
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档解析失败的页码
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态。
- `Success`：执行完成
- `Processing`：执行中
-  `Pause`: 暂停
-  `Failed`：执行失败
-  `WaitExecute`：等待执行
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        """解析结果的临时下载地址。文件类型为zip压缩包，下载链接有效期30分钟
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        """文档解析失败的页码
        :rtype: list of ReconstructDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

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
        self._Status = params.get("Status")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        self._RequestId = params.get("RequestId")


class GetSplitDocumentResultRequest(AbstractModel):
    """GetSplitDocumentResult请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 拆分任务ID
        :type TaskId: str
        """
        self._TaskId = None

    @property
    def TaskId(self):
        """拆分任务ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetSplitDocumentResultResponse(AbstractModel):
    """GetSplitDocumentResult返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态。

- `Success`：执行完成
- `Processing`：执行中
- `Pause`: 暂停
- `Failed`：执行失败
- `WaitExecute`：等待执行
        :type Status: str
        :param _DocumentRecognizeResultUrl: 拆分结果的临时下载地址。
文件类型为zip压缩包，下载链接有效期30分钟。
压缩包内包含\*.md、\*.jsonl、\*mllm.json以及images文件夹。

> **jsonl** 结构说明：
- `page_content`:
 用于生成嵌入（embedding）库，以便于检索使用。该字段中的图片将使用占位符替换。
- `org_data`:
 表示与 page_content 对应的最小语义完整性块，用于问答模型的处理。
- `big_data`:
 表示与 page_content 对应的最大语义完整性块，也用于问答模型的处理。
        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档拆分失败的页码
        :type FailedPages: list of SplitDocumentFailedPage
        :param _Usage: 文档拆分任务的用量
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._Usage = None
        self._RequestId = None

    @property
    def Status(self):
        """任务状态。

- `Success`：执行完成
- `Processing`：执行中
- `Pause`: 暂停
- `Failed`：执行失败
- `WaitExecute`：等待执行
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DocumentRecognizeResultUrl(self):
        """拆分结果的临时下载地址。
文件类型为zip压缩包，下载链接有效期30分钟。
压缩包内包含\*.md、\*.jsonl、\*mllm.json以及images文件夹。

> **jsonl** 结构说明：
- `page_content`:
 用于生成嵌入（embedding）库，以便于检索使用。该字段中的图片将使用占位符替换。
- `org_data`:
 表示与 page_content 对应的最小语义完整性块，用于问答模型的处理。
- `big_data`:
 表示与 page_content 对应的最大语义完整性块，也用于问答模型的处理。
        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        warnings.warn("parameter `FailedPages` is deprecated", DeprecationWarning) 

        """文档拆分失败的页码
        :rtype: list of SplitDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        warnings.warn("parameter `FailedPages` is deprecated", DeprecationWarning) 

        self._FailedPages = FailedPages

    @property
    def Usage(self):
        """文档拆分任务的用量
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.DocumentUsage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Status = params.get("Status")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = SplitDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        if params.get("Usage") is not None:
            self._Usage = DocumentUsage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class ImportQAsRequest(AbstractModel):
    """ImportQAs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _FileName: 文件名
        :type FileName: str
        :param _FileUrl: 文件的 Url 地址。文件存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 Url 速度和稳定性可能受一定影响。
导入模板：https://cdn.xiaowei.qq.com/lke/assets//static/批量导入问答模板v6.xlsx
        :type FileUrl: str
        :param _FileType: 文件类型，仅支持XLSX格式，请使用模板
        :type FileType: str
        """
        self._KnowledgeBaseId = None
        self._FileName = None
        self._FileUrl = None
        self._FileType = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def FileName(self):
        """文件名
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileUrl(self):
        """文件的 Url 地址。文件存储于腾讯云的 Url 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 Url 速度和稳定性可能受一定影响。
导入模板：https://cdn.xiaowei.qq.com/lke/assets//static/批量导入问答模板v6.xlsx
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileType(self):
        """文件类型，仅支持XLSX格式，请使用模板
        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._FileName = params.get("FileName")
        self._FileUrl = params.get("FileUrl")
        self._FileType = params.get("FileType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportQAsResponse(AbstractModel):
    """ImportQAs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class LabelItem(AbstractModel):
    """属性标签

    """

    def __init__(self):
        r"""
        :param _Name: 属性key
        :type Name: str
        :param _Values: 标签值
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        """属性key
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        """标签值
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttributeLabelsRequest(AbstractModel):
    """ListAttributeLabels请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _PageNumber: 页码，默认1
        :type PageNumber: int
        :param _PageSize: 每页数目，最大50，默认20
        :type PageSize: int
        """
        self._KnowledgeBaseId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def PageNumber(self):
        """页码，默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页数目，最大50，默认20
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListAttributeLabelsResponse(AbstractModel):
    """ListAttributeLabels返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 属性总数
        :type TotalCount: int
        :param _List: 属性标签列表
        :type List: list of AttributeItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """属性总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        """属性标签列表
        :rtype: list of AttributeItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = AttributeItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListDocsRequest(AbstractModel):
    """ListDocs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _PageNumber: 页码，默认1
        :type PageNumber: int
        :param _PageSize: 每页数目，最大50，默认20
        :type PageSize: int
        """
        self._KnowledgeBaseId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def PageNumber(self):
        """页码，默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页数目，最大50，默认20
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDocsResponse(AbstractModel):
    """ListDocs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 文档总数
        :type TotalCount: int
        :param _List: 文档信息
        :type List: list of DocItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """文档总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        """文档信息
        :rtype: list of DocItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = DocItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class ListQAsRequest(AbstractModel):
    """ListQAs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _PageNumber: 页码，默认1
        :type PageNumber: int
        :param _PageSize: 每页数目，最大50，默认20
        :type PageSize: int
        """
        self._KnowledgeBaseId = None
        self._PageNumber = None
        self._PageSize = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def PageNumber(self):
        """页码，默认1
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber

    @property
    def PageSize(self):
        """每页数目，最大50，默认20
        :rtype: int
        """
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._PageNumber = params.get("PageNumber")
        self._PageSize = params.get("PageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListQAsResponse(AbstractModel):
    """ListQAs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 问答对总数量
        :type TotalCount: int
        :param _List: 问答对信息
        :type List: list of QaItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._List = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """问答对总数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def List(self):
        """问答对信息
        :rtype: list of QaItem
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

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
        self._TotalCount = params.get("TotalCount")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = QaItem()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class Message(AbstractModel):
    """会话内容

    """

    def __init__(self):
        r"""
        :param _Role: 角色
        :type Role: str
        :param _Content: 内容
        :type Content: str
        :param _ReasoningContent: 思维链内容。
ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :type ReasoningContent: str
        :param _SearchResults: 搜索结果
        :type SearchResults: list of SearchResult
        """
        self._Role = None
        self._Content = None
        self._ReasoningContent = None
        self._SearchResults = None

    @property
    def Role(self):
        """角色
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def Content(self):
        """内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ReasoningContent(self):
        """思维链内容。
ReasoningConent参数仅支持出参，且只有deepseek-r1模型会返回。
        :rtype: str
        """
        return self._ReasoningContent

    @ReasoningContent.setter
    def ReasoningContent(self, ReasoningContent):
        self._ReasoningContent = ReasoningContent

    @property
    def SearchResults(self):
        """搜索结果
        :rtype: list of SearchResult
        """
        return self._SearchResults

    @SearchResults.setter
    def SearchResults(self, SearchResults):
        self._SearchResults = SearchResults


    def _deserialize(self, params):
        self._Role = params.get("Role")
        self._Content = params.get("Content")
        self._ReasoningContent = params.get("ReasoningContent")
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
        


class ModifyAttributeLabelRequest(AbstractModel):
    """ModifyAttributeLabel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _AttributeId: 属性ID
        :type AttributeId: str
        :param _AttributeKey: 属性标识，最大40个英文字符，如style
        :type AttributeKey: str
        :param _AttributeName: 属性名称，最大80个英文字符，如风格
        :type AttributeName: str
        :param _Labels: 属性标签
        :type Labels: list of AttributeLabelItem
        """
        self._KnowledgeBaseId = None
        self._AttributeId = None
        self._AttributeKey = None
        self._AttributeName = None
        self._Labels = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def AttributeId(self):
        """属性ID
        :rtype: str
        """
        return self._AttributeId

    @AttributeId.setter
    def AttributeId(self, AttributeId):
        self._AttributeId = AttributeId

    @property
    def AttributeKey(self):
        """属性标识，最大40个英文字符，如style
        :rtype: str
        """
        return self._AttributeKey

    @AttributeKey.setter
    def AttributeKey(self, AttributeKey):
        self._AttributeKey = AttributeKey

    @property
    def AttributeName(self):
        """属性名称，最大80个英文字符，如风格
        :rtype: str
        """
        return self._AttributeName

    @AttributeName.setter
    def AttributeName(self, AttributeName):
        self._AttributeName = AttributeName

    @property
    def Labels(self):
        """属性标签
        :rtype: list of AttributeLabelItem
        """
        return self._Labels

    @Labels.setter
    def Labels(self, Labels):
        self._Labels = Labels


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._AttributeId = params.get("AttributeId")
        self._AttributeKey = params.get("AttributeKey")
        self._AttributeName = params.get("AttributeName")
        if params.get("Labels") is not None:
            self._Labels = []
            for item in params.get("Labels"):
                obj = AttributeLabelItem()
                obj._deserialize(item)
                self._Labels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAttributeLabelResponse(AbstractModel):
    """ModifyAttributeLabel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class ModifyQARequest(AbstractModel):
    """ModifyQA请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _QaId: 问答对ID
        :type QaId: str
        :param _Question: 问题，最大1000个英文字符
        :type Question: str
        :param _Answer: 答案，最大4000个英文字符
        :type Answer: str
        :param _AttributeLabels: 属性标签
        :type AttributeLabels: list of AttributeLabelReferItem
        """
        self._KnowledgeBaseId = None
        self._QaId = None
        self._Question = None
        self._Answer = None
        self._AttributeLabels = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def QaId(self):
        """问答对ID
        :rtype: str
        """
        return self._QaId

    @QaId.setter
    def QaId(self, QaId):
        self._QaId = QaId

    @property
    def Question(self):
        """问题，最大1000个英文字符
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """答案，最大4000个英文字符
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AttributeLabels(self):
        """属性标签
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._QaId = params.get("QaId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyQAResponse(AbstractModel):
    """ModifyQA返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

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
        self._RequestId = params.get("RequestId")


class QaItem(AbstractModel):
    """问答对信息

    """

    def __init__(self):
        r"""
        :param _QaId: 问答id
注意：此字段可能返回 null，表示取不到有效值。
        :type QaId: str
        :param _Question: 问题
注意：此字段可能返回 null，表示取不到有效值。
        :type Question: str
        :param _Answer: 答案
注意：此字段可能返回 null，表示取不到有效值。
        :type Answer: str
        :param _AttributeLabels: 属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :type AttributeLabels: list of AttributeLabelReferItem
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._QaId = None
        self._Question = None
        self._Answer = None
        self._AttributeLabels = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def QaId(self):
        """问答id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._QaId

    @QaId.setter
    def QaId(self, QaId):
        self._QaId = QaId

    @property
    def Question(self):
        """问题
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Question

    @Question.setter
    def Question(self, Question):
        self._Question = Question

    @property
    def Answer(self):
        """答案
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Answer

    @Answer.setter
    def Answer(self, Answer):
        self._Answer = Answer

    @property
    def AttributeLabels(self):
        """属性标签
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._QaId = params.get("QaId")
        self._Question = params.get("Question")
        self._Answer = params.get("Answer")
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteRequest(AbstractModel):
    """QueryRewrite请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Messages: 需要改写的多轮历史会话，每轮历史对话需要包含user（问）和assistant（答）成对输入，由于模型字符限制，最多提供4轮对话。针对最后一轮对话进行改写
        :type Messages: list of Message
        :param _Model: 模型名称
        :type Model: str
        """
        self._Messages = None
        self._Model = None

    @property
    def Messages(self):
        """需要改写的多轮历史会话，每轮历史对话需要包含user（问）和assistant（答）成对输入，由于模型字符限制，最多提供4轮对话。针对最后一轮对话进行改写
        :rtype: list of Message
        """
        return self._Messages

    @Messages.setter
    def Messages(self, Messages):
        self._Messages = Messages

    @property
    def Model(self):
        """模型名称
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        if params.get("Messages") is not None:
            self._Messages = []
            for item in params.get("Messages"):
                obj = Message()
                obj._deserialize(item)
                self._Messages.append(obj)
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryRewriteResponse(AbstractModel):
    """QueryRewrite返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: 改写结果
        :type Content: str
        :param _Usage: 消耗量，返回输入token数，输出token数以及总token数
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._Usage = None
        self._RequestId = None

    @property
    def Content(self):
        """改写结果
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Usage(self):
        """消耗量，返回输入token数，输出token数以及总token数
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._Content = params.get("Content")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class ReconstructDocumentFailedPage(AbstractModel):
    """文档解析失败记录

    """

    def __init__(self):
        r"""
        :param _PageNumber: 失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        """失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentSSEConfig(AbstractModel):
    """ReconstructDocumentSSE 功能配置参数

    """

    def __init__(self):
        r"""
        :param _TableResultType: Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为0
        :type TableResultType: str
        :param _MarkdownImageResponseType: Markdown文件中图片返回的形式
0:markdown中图片以链接形式返回
1:markdown中图片只返回图片中提取的文本内容
默认是0
        :type MarkdownImageResponseType: str
        :param _ReturnPageFormat: Markdown文件中是否包含页码信息
        :type ReturnPageFormat: bool
        :param _PageFormat: 自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num>
        :type PageFormat: str
        """
        self._TableResultType = None
        self._MarkdownImageResponseType = None
        self._ReturnPageFormat = None
        self._PageFormat = None

    @property
    def TableResultType(self):
        """Markdown文件中表格返回的形式
0，表格以MD形式返回
1，表格以HTML形式返回
默认为0
        :rtype: str
        """
        return self._TableResultType

    @TableResultType.setter
    def TableResultType(self, TableResultType):
        self._TableResultType = TableResultType

    @property
    def MarkdownImageResponseType(self):
        """Markdown文件中图片返回的形式
0:markdown中图片以链接形式返回
1:markdown中图片只返回图片中提取的文本内容
默认是0
        :rtype: str
        """
        return self._MarkdownImageResponseType

    @MarkdownImageResponseType.setter
    def MarkdownImageResponseType(self, MarkdownImageResponseType):
        self._MarkdownImageResponseType = MarkdownImageResponseType

    @property
    def ReturnPageFormat(self):
        """Markdown文件中是否包含页码信息
        :rtype: bool
        """
        return self._ReturnPageFormat

    @ReturnPageFormat.setter
    def ReturnPageFormat(self, ReturnPageFormat):
        self._ReturnPageFormat = ReturnPageFormat

    @property
    def PageFormat(self):
        """自定义输出页码样式,{{p}}为页码占位符，开启ReturnPageFormat生效。未填默认样式:<page_num>page {{p}}</page_num>
        :rtype: str
        """
        return self._PageFormat

    @PageFormat.setter
    def PageFormat(self, PageFormat):
        self._PageFormat = PageFormat


    def _deserialize(self, params):
        self._TableResultType = params.get("TableResultType")
        self._MarkdownImageResponseType = params.get("MarkdownImageResponseType")
        self._ReturnPageFormat = params.get("ReturnPageFormat")
        self._PageFormat = params.get("PageFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentSSERequest(AbstractModel):
    """ReconstructDocumentSSE请求参数结构体

    """

    def __init__(self):
        r"""
        :param _FileType: 文件类型。
**支持的文件类型**：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2
**支持的文件大小**：
- PDF、DOC、DOCX、PPT、PPTX 支持100M
- MD、TXT、XLS、XLSX、CSV 支持10M
- 其他支持20M

        :type FileType: str
        :param _FileUrl: 文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _FileBase64: 文件的 Base64 值。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :type FileBase64: str
        :param _FileStartPageNumber: 文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :type FileStartPageNumber: int
        :param _FileEndPageNumber: 文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :type FileEndPageNumber: int
        :param _Config: 文档解析配置信息	
        :type Config: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSEConfig`
        """
        self._FileType = None
        self._FileUrl = None
        self._FileBase64 = None
        self._FileStartPageNumber = None
        self._FileEndPageNumber = None
        self._Config = None

    @property
    def FileType(self):
        """文件类型。
**支持的文件类型**：PDF、DOC、DOCX、PPT、PPTX、MD、TXT、XLS、XLSX、CSV、PNG、JPG、JPEG、BMP、GIF、WEBP、HEIC、EPS、ICNS、IM、PCX、PPM、TIFF、XBM、HEIF、JP2
**支持的文件大小**：
- PDF、DOC、DOCX、PPT、PPTX 支持100M
- MD、TXT、XLS、XLSX、CSV 支持10M
- 其他支持20M

        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def FileBase64(self):
        """文件的 Base64 值。
支持的文件大小：所下载文件经Base64编码后不超过 8M。文件下载时间不超过 3 秒。
支持的图片像素：单边介于20-10000px之间。
文件的 FileUrl、FileBase64 必须提供一个，如果都提供，只使用 FileUrl。
        :rtype: str
        """
        return self._FileBase64

    @FileBase64.setter
    def FileBase64(self, FileBase64):
        self._FileBase64 = FileBase64

    @property
    def FileStartPageNumber(self):
        """文档的起始页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的起始页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileStartPageNumber

    @FileStartPageNumber.setter
    def FileStartPageNumber(self, FileStartPageNumber):
        self._FileStartPageNumber = FileStartPageNumber

    @property
    def FileEndPageNumber(self):
        """文档的结束页码。
当传入文件是PDF、PDF、PPT、PPTX、DOC类型时，用来指定识别的结束页码，识别的页码包含当前值。
        :rtype: int
        """
        return self._FileEndPageNumber

    @FileEndPageNumber.setter
    def FileEndPageNumber(self, FileEndPageNumber):
        self._FileEndPageNumber = FileEndPageNumber

    @property
    def Config(self):
        """文档解析配置信息	
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.ReconstructDocumentSSEConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        self._FileBase64 = params.get("FileBase64")
        self._FileStartPageNumber = params.get("FileStartPageNumber")
        self._FileEndPageNumber = params.get("FileEndPageNumber")
        if params.get("Config") is not None:
            self._Config = ReconstructDocumentSSEConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReconstructDocumentSSEResponse(AbstractModel):
    """ReconstructDocumentSSE返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 任务ID。本次请求的唯一标识
        :type TaskId: str
        :param _ResponseType: 响应类型。1：返回进度信息，2：返回解析结果
        :type ResponseType: str
        :param _Progress: 进度。0~100
        :type Progress: str
        :param _ProgressMessage: 进度信息。
        :type ProgressMessage: str
        :param _DocumentRecognizeResultUrl: 文档解析结果的临时下载地址。
文件类型为zip压缩包，下载链接有效期30分钟。
压缩包内包含*.md、*.json以及images文件夹。

        :type DocumentRecognizeResultUrl: str
        :param _FailedPages: 文档解析失败的页码。
        :type FailedPages: list of ReconstructDocumentFailedPage
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :type RequestId: str
        """
        self._TaskId = None
        self._ResponseType = None
        self._Progress = None
        self._ProgressMessage = None
        self._DocumentRecognizeResultUrl = None
        self._FailedPages = None
        self._RequestId = None

    @property
    def TaskId(self):
        """任务ID。本次请求的唯一标识
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def ResponseType(self):
        """响应类型。1：返回进度信息，2：返回解析结果
        :rtype: str
        """
        return self._ResponseType

    @ResponseType.setter
    def ResponseType(self, ResponseType):
        self._ResponseType = ResponseType

    @property
    def Progress(self):
        """进度。0~100
        :rtype: str
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def ProgressMessage(self):
        """进度信息。
        :rtype: str
        """
        return self._ProgressMessage

    @ProgressMessage.setter
    def ProgressMessage(self, ProgressMessage):
        self._ProgressMessage = ProgressMessage

    @property
    def DocumentRecognizeResultUrl(self):
        """文档解析结果的临时下载地址。
文件类型为zip压缩包，下载链接有效期30分钟。
压缩包内包含*.md、*.json以及images文件夹。

        :rtype: str
        """
        return self._DocumentRecognizeResultUrl

    @DocumentRecognizeResultUrl.setter
    def DocumentRecognizeResultUrl(self, DocumentRecognizeResultUrl):
        self._DocumentRecognizeResultUrl = DocumentRecognizeResultUrl

    @property
    def FailedPages(self):
        """文档解析失败的页码。
        :rtype: list of ReconstructDocumentFailedPage
        """
        return self._FailedPages

    @FailedPages.setter
    def FailedPages(self, FailedPages):
        self._FailedPages = FailedPages

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。本接口为流式响应接口，当请求成功时，RequestId 会被放在 HTTP 响应的 Header "X-TC-RequestId" 中。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._ResponseType = params.get("ResponseType")
        self._Progress = params.get("Progress")
        self._ProgressMessage = params.get("ProgressMessage")
        self._DocumentRecognizeResultUrl = params.get("DocumentRecognizeResultUrl")
        if params.get("FailedPages") is not None:
            self._FailedPages = []
            for item in params.get("FailedPages"):
                obj = ReconstructDocumentFailedPage()
                obj._deserialize(item)
                self._FailedPages.append(obj)
        self._RequestId = params.get("RequestId")


class RetrievalRecord(AbstractModel):
    """检索的结果

    """

    def __init__(self):
        r"""
        :param _Metadata: 检索结果的元数据
        :type Metadata: :class:`tencentcloud.lkeap.v20240522.models.RetrievalRecordMetadata`
        :param _Title: 检索到的标题
        :type Title: str
        :param _Content: 检索到的内容
        :type Content: str
        """
        self._Metadata = None
        self._Title = None
        self._Content = None

    @property
    def Metadata(self):
        """检索结果的元数据
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.RetrievalRecordMetadata`
        """
        return self._Metadata

    @Metadata.setter
    def Metadata(self, Metadata):
        self._Metadata = Metadata

    @property
    def Title(self):
        """检索到的标题
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        """检索到的内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        if params.get("Metadata") is not None:
            self._Metadata = RetrievalRecordMetadata()
            self._Metadata._deserialize(params.get("Metadata"))
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrievalRecordMetadata(AbstractModel):
    """检索结果的元数据

    """

    def __init__(self):
        r"""
        :param _Type: 结果的类型。
- `DOC`：文档
- `QA`：问答对
        :type Type: str
        :param _ResultSource: 检索结果的来源。
- `SEMANTIC`：从语义检索中得到的结果
- `FULL_TEXT`：从全文检索中得到的结果
        :type ResultSource: str
        :param _ChunkPageNumbers: 切片在文档中的页码，仅部分文档支持
        :type ChunkPageNumbers: list of int
        """
        self._Type = None
        self._ResultSource = None
        self._ChunkPageNumbers = None

    @property
    def Type(self):
        """结果的类型。
- `DOC`：文档
- `QA`：问答对
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResultSource(self):
        """检索结果的来源。
- `SEMANTIC`：从语义检索中得到的结果
- `FULL_TEXT`：从全文检索中得到的结果
        :rtype: str
        """
        return self._ResultSource

    @ResultSource.setter
    def ResultSource(self, ResultSource):
        self._ResultSource = ResultSource

    @property
    def ChunkPageNumbers(self):
        """切片在文档中的页码，仅部分文档支持
        :rtype: list of int
        """
        return self._ChunkPageNumbers

    @ChunkPageNumbers.setter
    def ChunkPageNumbers(self, ChunkPageNumbers):
        self._ChunkPageNumbers = ChunkPageNumbers


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._ResultSource = params.get("ResultSource")
        self._ChunkPageNumbers = params.get("ChunkPageNumbers")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrievalSetting(AbstractModel):
    """检索参数设置

    """

    def __init__(self):
        r"""
        :param _Type: 检索的类型，不填该参数则检索全部。
- `DOC`：文档
- `QA`：QA

仅RetrieveKnowledge接口支持该参数
        :type Type: str
        :param _TopK: 返回个数
        :type TopK: int
        :param _ScoreThreshold: 分数过滤
        :type ScoreThreshold: float
        """
        self._Type = None
        self._TopK = None
        self._ScoreThreshold = None

    @property
    def Type(self):
        """检索的类型，不填该参数则检索全部。
- `DOC`：文档
- `QA`：QA

仅RetrieveKnowledge接口支持该参数
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def TopK(self):
        """返回个数
        :rtype: int
        """
        return self._TopK

    @TopK.setter
    def TopK(self, TopK):
        self._TopK = TopK

    @property
    def ScoreThreshold(self):
        """分数过滤
        :rtype: float
        """
        return self._ScoreThreshold

    @ScoreThreshold.setter
    def ScoreThreshold(self, ScoreThreshold):
        self._ScoreThreshold = ScoreThreshold


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._TopK = params.get("TopK")
        self._ScoreThreshold = params.get("ScoreThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveKnowledgeRealtimeRequest(AbstractModel):
    """RetrieveKnowledgeRealtime请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID。
        :type KnowledgeBaseId: str
        :param _Query: 用于检索的文本。
        :type Query: str
        :param _DocIds: 实时文件ID列表。
        :type DocIds: list of str
        :param _RetrievalMethod: 检索方法，默认使用`HYBRID`混合检索。
- `SEMANTIC`：语义检索
- `FULL_TEXT`：全文检索
- `HYBRID`：混合检索
        :type RetrievalMethod: str
        :param _RetrievalSetting: 检索设置。
        :type RetrievalSetting: :class:`tencentcloud.lkeap.v20240522.models.RetrievalSetting`
        """
        self._KnowledgeBaseId = None
        self._Query = None
        self._DocIds = None
        self._RetrievalMethod = None
        self._RetrievalSetting = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID。
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def Query(self):
        """用于检索的文本。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def DocIds(self):
        """实时文件ID列表。
        :rtype: list of str
        """
        return self._DocIds

    @DocIds.setter
    def DocIds(self, DocIds):
        self._DocIds = DocIds

    @property
    def RetrievalMethod(self):
        """检索方法，默认使用`HYBRID`混合检索。
- `SEMANTIC`：语义检索
- `FULL_TEXT`：全文检索
- `HYBRID`：混合检索
        :rtype: str
        """
        return self._RetrievalMethod

    @RetrievalMethod.setter
    def RetrievalMethod(self, RetrievalMethod):
        self._RetrievalMethod = RetrievalMethod

    @property
    def RetrievalSetting(self):
        """检索设置。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.RetrievalSetting`
        """
        return self._RetrievalSetting

    @RetrievalSetting.setter
    def RetrievalSetting(self, RetrievalSetting):
        self._RetrievalSetting = RetrievalSetting


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._Query = params.get("Query")
        self._DocIds = params.get("DocIds")
        self._RetrievalMethod = params.get("RetrievalMethod")
        if params.get("RetrievalSetting") is not None:
            self._RetrievalSetting = RetrievalSetting()
            self._RetrievalSetting._deserialize(params.get("RetrievalSetting"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveKnowledgeRealtimeResponse(AbstractModel):
    """RetrieveKnowledgeRealtime返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 检索结果
        :type Records: list of RetrievalRecord
        :param _TotalCount: 检索结果数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Records(self):
        """检索结果
        :rtype: list of RetrievalRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def TotalCount(self):
        """检索结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = RetrievalRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class RetrieveKnowledgeRequest(AbstractModel):
    """RetrieveKnowledge请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID。
        :type KnowledgeBaseId: str
        :param _Query: 用于检索的文本。
        :type Query: str
        :param _RetrievalMethod: 检索方法，默认使用`HYBRID`混合检索。
- `SEMANTIC`：语义检索
- `FULL_TEXT`：全文检索
- `HYBRID`：混合检索
        :type RetrievalMethod: str
        :param _RetrievalSetting: 检索设置。
        :type RetrievalSetting: :class:`tencentcloud.lkeap.v20240522.models.RetrievalSetting`
        :param _AttributeLabels: 标签过滤。
        :type AttributeLabels: list of LabelItem
        """
        self._KnowledgeBaseId = None
        self._Query = None
        self._RetrievalMethod = None
        self._RetrievalSetting = None
        self._AttributeLabels = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID。
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def Query(self):
        """用于检索的文本。
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def RetrievalMethod(self):
        """检索方法，默认使用`HYBRID`混合检索。
- `SEMANTIC`：语义检索
- `FULL_TEXT`：全文检索
- `HYBRID`：混合检索
        :rtype: str
        """
        return self._RetrievalMethod

    @RetrievalMethod.setter
    def RetrievalMethod(self, RetrievalMethod):
        self._RetrievalMethod = RetrievalMethod

    @property
    def RetrievalSetting(self):
        """检索设置。
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.RetrievalSetting`
        """
        return self._RetrievalSetting

    @RetrievalSetting.setter
    def RetrievalSetting(self, RetrievalSetting):
        self._RetrievalSetting = RetrievalSetting

    @property
    def AttributeLabels(self):
        """标签过滤。
        :rtype: list of LabelItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._Query = params.get("Query")
        self._RetrievalMethod = params.get("RetrievalMethod")
        if params.get("RetrievalSetting") is not None:
            self._RetrievalSetting = RetrievalSetting()
            self._RetrievalSetting._deserialize(params.get("RetrievalSetting"))
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = LabelItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveKnowledgeResponse(AbstractModel):
    """RetrieveKnowledge返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Records: 检索结果
        :type Records: list of RetrievalRecord
        :param _TotalCount: 检索结果数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Records = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Records(self):
        """检索结果
        :rtype: list of RetrievalRecord
        """
        return self._Records

    @Records.setter
    def Records(self, Records):
        self._Records = Records

    @property
    def TotalCount(self):
        """检索结果数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

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
        if params.get("Records") is not None:
            self._Records = []
            for item in params.get("Records"):
                obj = RetrievalRecord()
                obj._deserialize(item)
                self._Records.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class RunRerankRequest(AbstractModel):
    """RunRerank请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 查询内容
        :type Query: str
        :param _Docs: 文档列表，最多20个
        :type Docs: list of str
        :param _Model: 模型名称, 默认: lke-reranker-base
        :type Model: str
        """
        self._Query = None
        self._Docs = None
        self._Model = None

    @property
    def Query(self):
        """查询内容
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Docs(self):
        """文档列表，最多20个
        :rtype: list of str
        """
        return self._Docs

    @Docs.setter
    def Docs(self, Docs):
        self._Docs = Docs

    @property
    def Model(self):
        """模型名称, 默认: lke-reranker-base
        :rtype: str
        """
        return self._Model

    @Model.setter
    def Model(self, Model):
        self._Model = Model


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._Docs = params.get("Docs")
        self._Model = params.get("Model")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunRerankResponse(AbstractModel):
    """RunRerank返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreList: 相关性, 数值越大越相关
        :type ScoreList: list of float
        :param _Usage: 消耗量，仅返回TotalToken
        :type Usage: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreList = None
        self._Usage = None
        self._RequestId = None

    @property
    def ScoreList(self):
        """相关性, 数值越大越相关
        :rtype: list of float
        """
        return self._ScoreList

    @ScoreList.setter
    def ScoreList(self, ScoreList):
        self._ScoreList = ScoreList

    @property
    def Usage(self):
        """消耗量，仅返回TotalToken
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.Usage`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

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
        self._ScoreList = params.get("ScoreList")
        if params.get("Usage") is not None:
            self._Usage = Usage()
            self._Usage._deserialize(params.get("Usage"))
        self._RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """搜索结果

    """

    def __init__(self):
        r"""
        :param _Index: 索引
        :type Index: int
        :param _Url: 链接地址
        :type Url: str
        :param _Name: 标题
        :type Name: str
        :param _Snippet: 摘要
        :type Snippet: str
        :param _Icon: 图标
        :type Icon: str
        :param _Site: 站点
        :type Site: str
        :param _PublishedTime: 1740412800
        :type PublishedTime: int
        """
        self._Index = None
        self._Url = None
        self._Name = None
        self._Snippet = None
        self._Icon = None
        self._Site = None
        self._PublishedTime = None

    @property
    def Index(self):
        """索引
        :rtype: int
        """
        return self._Index

    @Index.setter
    def Index(self, Index):
        self._Index = Index

    @property
    def Url(self):
        """链接地址
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        """标题
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Snippet(self):
        """摘要
        :rtype: str
        """
        return self._Snippet

    @Snippet.setter
    def Snippet(self, Snippet):
        self._Snippet = Snippet

    @property
    def Icon(self):
        """图标
        :rtype: str
        """
        return self._Icon

    @Icon.setter
    def Icon(self, Icon):
        self._Icon = Icon

    @property
    def Site(self):
        """站点
        :rtype: str
        """
        return self._Site

    @Site.setter
    def Site(self, Site):
        self._Site = Site

    @property
    def PublishedTime(self):
        """1740412800
        :rtype: int
        """
        return self._PublishedTime

    @PublishedTime.setter
    def PublishedTime(self, PublishedTime):
        self._PublishedTime = PublishedTime


    def _deserialize(self, params):
        self._Index = params.get("Index")
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        self._Snippet = params.get("Snippet")
        self._Icon = params.get("Icon")
        self._Site = params.get("Site")
        self._PublishedTime = params.get("PublishedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SegmentationConfig(AbstractModel):
    """分段配置

    """

    def __init__(self):
        r"""
        :param _MaxChunkSize: 最大分片长度
        :type MaxChunkSize: int
        """
        self._MaxChunkSize = None

    @property
    def MaxChunkSize(self):
        """最大分片长度
        :rtype: int
        """
        return self._MaxChunkSize

    @MaxChunkSize.setter
    def MaxChunkSize(self, MaxChunkSize):
        self._MaxChunkSize = MaxChunkSize


    def _deserialize(self, params):
        self._MaxChunkSize = params.get("MaxChunkSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SplitDocumentFailedPage(AbstractModel):
    """文档解析失败记录

    """

    def __init__(self):
        r"""
        :param _PageNumber: 失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNumber: int
        """
        self._PageNumber = None

    @property
    def PageNumber(self):
        """失败页码	
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PageNumber

    @PageNumber.setter
    def PageNumber(self, PageNumber):
        self._PageNumber = PageNumber


    def _deserialize(self, params):
        self._PageNumber = params.get("PageNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDocRequest(AbstractModel):
    """UploadDoc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KnowledgeBaseId: 知识库ID
        :type KnowledgeBaseId: str
        :param _FileName: 文件名。
**需带文件类型后缀**
        :type FileName: str
        :param _FileType: 文件类型。

**支持的文件类型：**
- `PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`

**支持的文件大小：**
 - `PDF`、`DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M
 - `TXT`、`MD` 最大10M
 - 其他 最大20M

        :type FileType: str
        :param _FileUrl: 文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :type FileUrl: str
        :param _AttributeLabel: 属性标签引用
        :type AttributeLabel: list of AttributeLabelReferItem
        :param _AttributeLabels: 属性标签引用
        :type AttributeLabels: list of AttributeLabelReferItem
        :param _Config: 分段信息
        :type Config: :class:`tencentcloud.lkeap.v20240522.models.SegmentationConfig`
        """
        self._KnowledgeBaseId = None
        self._FileName = None
        self._FileType = None
        self._FileUrl = None
        self._AttributeLabel = None
        self._AttributeLabels = None
        self._Config = None

    @property
    def KnowledgeBaseId(self):
        """知识库ID
        :rtype: str
        """
        return self._KnowledgeBaseId

    @KnowledgeBaseId.setter
    def KnowledgeBaseId(self, KnowledgeBaseId):
        self._KnowledgeBaseId = KnowledgeBaseId

    @property
    def FileName(self):
        """文件名。
**需带文件类型后缀**
        :rtype: str
        """
        return self._FileName

    @FileName.setter
    def FileName(self, FileName):
        self._FileName = FileName

    @property
    def FileType(self):
        """文件类型。

**支持的文件类型：**
- `PDF`、`DOC`、`DOCX`、`XLS`、`XLSX`、`PPT`、`PPTX`、`MD`、`TXT`、`PNG`、`JPG`、`JPEG`、`CSV`

**支持的文件大小：**
 - `PDF`、`DOCX`、`DOC`、`PPT`、`PPTX` 最大 200M
 - `TXT`、`MD` 最大10M
 - 其他 最大20M

        :rtype: str
        """
        return self._FileType

    @FileType.setter
    def FileType(self, FileType):
        self._FileType = FileType

    @property
    def FileUrl(self):
        """文件的 URL 地址。
文件存储于腾讯云的 URL 可保障更高的下载速度和稳定性，建议文件存储于腾讯云。 非腾讯云存储的 URL 速度和稳定性可能受一定影响。
参考：[腾讯云COS文档](https://cloud.tencent.com/document/product/436/7749)
        :rtype: str
        """
        return self._FileUrl

    @FileUrl.setter
    def FileUrl(self, FileUrl):
        self._FileUrl = FileUrl

    @property
    def AttributeLabel(self):
        warnings.warn("parameter `AttributeLabel` is deprecated", DeprecationWarning) 

        """属性标签引用
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabel

    @AttributeLabel.setter
    def AttributeLabel(self, AttributeLabel):
        warnings.warn("parameter `AttributeLabel` is deprecated", DeprecationWarning) 

        self._AttributeLabel = AttributeLabel

    @property
    def AttributeLabels(self):
        """属性标签引用
        :rtype: list of AttributeLabelReferItem
        """
        return self._AttributeLabels

    @AttributeLabels.setter
    def AttributeLabels(self, AttributeLabels):
        self._AttributeLabels = AttributeLabels

    @property
    def Config(self):
        """分段信息
        :rtype: :class:`tencentcloud.lkeap.v20240522.models.SegmentationConfig`
        """
        return self._Config

    @Config.setter
    def Config(self, Config):
        self._Config = Config


    def _deserialize(self, params):
        self._KnowledgeBaseId = params.get("KnowledgeBaseId")
        self._FileName = params.get("FileName")
        self._FileType = params.get("FileType")
        self._FileUrl = params.get("FileUrl")
        if params.get("AttributeLabel") is not None:
            self._AttributeLabel = []
            for item in params.get("AttributeLabel"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabel.append(obj)
        if params.get("AttributeLabels") is not None:
            self._AttributeLabels = []
            for item in params.get("AttributeLabels"):
                obj = AttributeLabelReferItem()
                obj._deserialize(item)
                self._AttributeLabels.append(obj)
        if params.get("Config") is not None:
            self._Config = SegmentationConfig()
            self._Config._deserialize(params.get("Config"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadDocResponse(AbstractModel):
    """UploadDoc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DocId: 文档ID
        :type DocId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DocId = None
        self._RequestId = None

    @property
    def DocId(self):
        """文档ID
        :rtype: str
        """
        return self._DocId

    @DocId.setter
    def DocId(self, DocId):
        self._DocId = DocId

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
        self._DocId = params.get("DocId")
        self._RequestId = params.get("RequestId")


class Usage(AbstractModel):
    """消耗量

    """

    def __init__(self):
        r"""
        :param _TotalPages: 文档页数
        :type TotalPages: int
        :param _InputTokens: 输入token数
        :type InputTokens: int
        :param _OutputTokens: 输出token数
        :type OutputTokens: int
        :param _TotalTokens: 总token数
        :type TotalTokens: int
        """
        self._TotalPages = None
        self._InputTokens = None
        self._OutputTokens = None
        self._TotalTokens = None

    @property
    def TotalPages(self):
        """文档页数
        :rtype: int
        """
        return self._TotalPages

    @TotalPages.setter
    def TotalPages(self, TotalPages):
        self._TotalPages = TotalPages

    @property
    def InputTokens(self):
        """输入token数
        :rtype: int
        """
        return self._InputTokens

    @InputTokens.setter
    def InputTokens(self, InputTokens):
        self._InputTokens = InputTokens

    @property
    def OutputTokens(self):
        """输出token数
        :rtype: int
        """
        return self._OutputTokens

    @OutputTokens.setter
    def OutputTokens(self, OutputTokens):
        self._OutputTokens = OutputTokens

    @property
    def TotalTokens(self):
        """总token数
        :rtype: int
        """
        return self._TotalTokens

    @TotalTokens.setter
    def TotalTokens(self, TotalTokens):
        self._TotalTokens = TotalTokens


    def _deserialize(self, params):
        self._TotalPages = params.get("TotalPages")
        self._InputTokens = params.get("InputTokens")
        self._OutputTokens = params.get("OutputTokens")
        self._TotalTokens = params.get("TotalTokens")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        