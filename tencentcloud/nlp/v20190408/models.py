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


class AutoSummarizationRequest(AbstractModel):
    """AutoSummarization请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）\n        :type Text: str\n        :param Length: 指定摘要的长度上限（默认值为200）
注：为保证摘要的可读性，最终生成的摘要长度会低于指定的长度上限。\n        :type Length: int\n        """
        self.Text = None
        self.Length = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSummarizationResponse(AbstractModel):
    """AutoSummarization返回参数结构体

    """

    def __init__(self):
        """
        :param Summary: 文本摘要结果\n        :type Summary: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Summary = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Summary = params.get("Summary")
        self.RequestId = params.get("RequestId")


class CCIToken(AbstractModel):
    """文本纠错结果

    """

    def __init__(self):
        """
        :param Word: 错别字内容\n        :type Word: str\n        :param BeginOffset: 错别字的起始位置，从0开始\n        :type BeginOffset: int\n        :param CorrectWord: 错别字纠错结果\n        :type CorrectWord: str\n        """
        self.Word = None
        self.BeginOffset = None
        self.CorrectWord = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.BeginOffset = params.get("BeginOffset")
        self.CorrectWord = params.get("CorrectWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatBotRequest(AbstractModel):
    """ChatBot请求参数结构体

    """

    def __init__(self):
        """
        :param Query: 用户请求的query\n        :type Query: str\n        :param OpenId: 服务的id,  主要用于儿童闲聊接口，比如手Q的openid\n        :type OpenId: str\n        :param Flag: 0: 通用闲聊, 1:儿童闲聊, 默认是通用闲聊\n        :type Flag: int\n        """
        self.Query = None
        self.OpenId = None
        self.Flag = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.OpenId = params.get("OpenId")
        self.Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatBotResponse(AbstractModel):
    """ChatBot返回参数结构体

    """

    def __init__(self):
        """
        :param Reply: 闲聊回复\n        :type Reply: str\n        :param Confidence: 对于当前输出回复的自信度\n        :type Confidence: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Reply = None
        self.Confidence = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Reply = params.get("Reply")
        self.Confidence = params.get("Confidence")
        self.RequestId = params.get("RequestId")


class ClassificationResult(AbstractModel):
    """文本分类结果

    """

    def __init__(self):
        """
        :param FirstClassName: 一级分类名称\n        :type FirstClassName: str\n        :param SecondClassName: 二级分类名称\n        :type SecondClassName: str\n        :param FirstClassProbability: 一级分类概率
注意：此字段可能返回 null，表示取不到有效值。\n        :type FirstClassProbability: float\n        :param SecondClassProbability: 二级分类概率
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecondClassProbability: float\n        :param ThirdClassName: 三级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
注意：此字段可能返回 null，表示取不到有效值。\n        :type ThirdClassName: str\n        :param ThirdClassProbability: 三级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
注意：此字段可能返回 null，表示取不到有效值。\n        :type ThirdClassProbability: float\n        :param FourthClassName: 四级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
注意：此字段可能返回 null，表示取不到有效值。\n        :type FourthClassName: str\n        :param FourthClassProbability: 四级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
注意：此字段可能返回 null，表示取不到有效值。\n        :type FourthClassProbability: float\n        :param FifthClassName: 五级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
注意：此字段可能返回 null，表示取不到有效值。\n        :type FifthClassName: str\n        :param FifthClassProbability: 五级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
注意：此字段可能返回 null，表示取不到有效值。\n        :type FifthClassProbability: float\n        """
        self.FirstClassName = None
        self.SecondClassName = None
        self.FirstClassProbability = None
        self.SecondClassProbability = None
        self.ThirdClassName = None
        self.ThirdClassProbability = None
        self.FourthClassName = None
        self.FourthClassProbability = None
        self.FifthClassName = None
        self.FifthClassProbability = None


    def _deserialize(self, params):
        self.FirstClassName = params.get("FirstClassName")
        self.SecondClassName = params.get("SecondClassName")
        self.FirstClassProbability = params.get("FirstClassProbability")
        self.SecondClassProbability = params.get("SecondClassProbability")
        self.ThirdClassName = params.get("ThirdClassName")
        self.ThirdClassProbability = params.get("ThirdClassProbability")
        self.FourthClassName = params.get("FourthClassName")
        self.FourthClassProbability = params.get("FourthClassProbability")
        self.FifthClassName = params.get("FifthClassName")
        self.FifthClassProbability = params.get("FifthClassProbability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDictRequest(AbstractModel):
    """CreateDict请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 自定义词库名称，不超过20字。\n        :type Name: str\n        :param Description: 自定义词库描述，不超过100字。\n        :type Description: str\n        """
        self.Name = None
        self.Description = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDictResponse(AbstractModel):
    """CreateDict返回参数结构体

    """

    def __init__(self):
        """
        :param DictId: 创建的自定义词库ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DictId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DictId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        self.RequestId = params.get("RequestId")


class CreateWordItemsRequest(AbstractModel):
    """CreateWordItems请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 自定义词库ID。\n        :type DictId: str\n        :param WordItems: 待添加的词条集合。\n        :type WordItems: list of WordItem\n        """
        self.DictId = None
        self.WordItems = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        if params.get("WordItems") is not None:
            self.WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self.WordItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWordItemsResponse(AbstractModel):
    """CreateWordItems返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDictRequest(AbstractModel):
    """DeleteDict请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 要删除的自定义词库ID。\n        :type DictId: str\n        """
        self.DictId = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDictResponse(AbstractModel):
    """DeleteDict返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordItemsRequest(AbstractModel):
    """DeleteWordItems请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 自定义词库ID。\n        :type DictId: str\n        :param WordItems: 待删除的词条集合。\n        :type WordItems: list of WordItem\n        """
        self.DictId = None
        self.WordItems = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        if params.get("WordItems") is not None:
            self.WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self.WordItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWordItemsResponse(AbstractModel):
    """DeleteWordItems返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DependencyParsingRequest(AbstractModel):
    """DependencyParsing请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependencyParsingResponse(AbstractModel):
    """DependencyParsing返回参数结构体

    """

    def __init__(self):
        """
        :param DpTokens: 句法依存分析结果，其中句法依存关系的类型包括：
<li>主谓关系，eg: 我送她一束花 (我 <-- 送)
<li>动宾关系，eg: 我送她一束花 (送 --> 花)
<li>间宾关系，eg: 我送她一束花 (送 --> 她)
<li>前置宾语，eg: 他什么书都读 (书 <-- 读)
<li>兼语，eg: 他请我吃饭 (请 --> 我)
<li>定中关系，eg: 红苹果 (红 <-- 苹果)
<li>状中结构，eg: 非常美丽 (非常 <-- 美丽)
<li>动补结构，eg: 做完了作业 (做 --> 完)
<li>并列关系，eg: 大山和大海 (大山 --> 大海)
<li>介宾关系，eg: 在贸易区内 (在 --> 内)
<li>左附加关系，eg: 大山和大海 (和 <-- 大海)
<li>右附加关系，eg: 孩子们 (孩子 --> 们)
<li>独立结构，eg: 两个单句在结构上彼此独立
<li>标点符号，eg: 。
<li>核心关系，eg: 整个句子的核心\n        :type DpTokens: list of DpToken\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DpTokens = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DpTokens") is not None:
            self.DpTokens = []
            for item in params.get("DpTokens"):
                obj = DpToken()
                obj._deserialize(item)
                self.DpTokens.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDictRequest(AbstractModel):
    """DescribeDict请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 自定义词库ID。\n        :type DictId: str\n        :param Name: 自定义词库名称，模糊搜索。\n        :type Name: str\n        """
        self.DictId = None
        self.Name = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDictResponse(AbstractModel):
    """DescribeDict返回参数结构体

    """

    def __init__(self):
        """
        :param Dicts: 查询到的词库信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Dicts: list of DictInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Dicts = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Dicts") is not None:
            self.Dicts = []
            for item in params.get("Dicts"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Dicts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDictsRequest(AbstractModel):
    """DescribeDicts请求参数结构体

    """

    def __init__(self):
        """
        :param Limit: 每页数据量，范围为1~100，默认为10。\n        :type Limit: int\n        :param Offset: 分页偏移量，从0开始，默认为0。\n        :type Offset: int\n        """
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDictsResponse(AbstractModel):
    """DescribeDicts返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 记录总条数。\n        :type TotalCount: int\n        :param Dicts: 自定义词库信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Dicts: list of DictInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.Dicts = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Dicts") is not None:
            self.Dicts = []
            for item in params.get("Dicts"):
                obj = DictInfo()
                obj._deserialize(item)
                self.Dicts.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeEntityRequest(AbstractModel):
    """DescribeEntity请求参数结构体

    """

    def __init__(self):
        """
        :param EntityName: 实体名称\n        :type EntityName: str\n        """
        self.EntityName = None


    def _deserialize(self, params):
        self.EntityName = params.get("EntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEntityResponse(AbstractModel):
    """DescribeEntity返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体相关信息\n        :type Content: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.RequestId = params.get("RequestId")


class DescribeRelationRequest(AbstractModel):
    """DescribeRelation请求参数结构体

    """

    def __init__(self):
        """
        :param LeftEntityName: 输入第一个实体\n        :type LeftEntityName: str\n        :param RightEntityName: 输入第二个实体\n        :type RightEntityName: str\n        """
        self.LeftEntityName = None
        self.RightEntityName = None


    def _deserialize(self, params):
        self.LeftEntityName = params.get("LeftEntityName")
        self.RightEntityName = params.get("RightEntityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRelationResponse(AbstractModel):
    """DescribeRelation返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体间的关系\n        :type Content: list of EntityRelationContent\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = EntityRelationContent()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTripleRequest(AbstractModel):
    """DescribeTriple请求参数结构体

    """

    def __init__(self):
        """
        :param TripleCondition: 三元组查询条件\n        :type TripleCondition: str\n        """
        self.TripleCondition = None


    def _deserialize(self, params):
        self.TripleCondition = params.get("TripleCondition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTripleResponse(AbstractModel):
    """DescribeTriple返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回三元组信息\n        :type Content: list of TripleContent\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Content") is not None:
            self.Content = []
            for item in params.get("Content"):
                obj = TripleContent()
                obj._deserialize(item)
                self.Content.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeWordItemsRequest(AbstractModel):
    """DescribeWordItems请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 自定义词库ID。\n        :type DictId: str\n        :param Offset: 分页偏移量，从0开始，默认为0。\n        :type Offset: int\n        :param Limit: 每页数据量，范围为1~100，默认为10。\n        :type Limit: int\n        :param Text: 待检索的词条文本，支持模糊匹配。\n        :type Text: str\n        """
        self.DictId = None
        self.Offset = None
        self.Limit = None
        self.Text = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWordItemsResponse(AbstractModel):
    """DescribeWordItems返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 词条记录总条数。\n        :type TotalCount: int\n        :param WordItems: 词条信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type WordItems: list of WordItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.WordItems = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("WordItems") is not None:
            self.WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self.WordItems.append(obj)
        self.RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """自定义词库信息

    """

    def __init__(self):
        """
        :param Name: 自定义词库名称。\n        :type Name: str\n        :param Id: 自定义词库ID。\n        :type Id: str\n        :param Description: 自定义词库描述信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Description: str\n        :param UpdateTime: 自定义词库修改时间，形式为:yyyy-mm-dd hh:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param CreateTime: 自定义词库创建时间，形式为:yyyy-mm-dd hh:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        """
        self.Name = None
        self.Id = None
        self.Description = None
        self.UpdateTime = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Id = params.get("Id")
        self.Description = params.get("Description")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DpToken(AbstractModel):
    """句法依存分析结果，包括基础词，基础词的序号，当前词父节点的序号，句法依存关系的类型

    """

    def __init__(self):
        """
        :param Relation: 句法依存关系的类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type Relation: str\n        :param HeadId: 当前词父节点的序号
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeadId: int\n        :param Word: 基础词
注意：此字段可能返回 null，表示取不到有效值。\n        :type Word: str\n        :param Id: 基础词的序号
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: int\n        """
        self.Relation = None
        self.HeadId = None
        self.Word = None
        self.Id = None


    def _deserialize(self, params):
        self.Relation = params.get("Relation")
        self.HeadId = params.get("HeadId")
        self.Word = params.get("Word")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationContent(AbstractModel):
    """返回的实体关系查询结果详细内容

    """

    def __init__(self):
        """
        :param Object: 实体关系查询返回关系的object
注意：此字段可能返回 null，表示取不到有效值。\n        :type Object: list of EntityRelationObject\n        :param Relation: 实体关系查询返回的关系名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Relation: str\n        :param Subject: 实体关系查询返回关系的subject
注意：此字段可能返回 null，表示取不到有效值。\n        :type Subject: list of EntityRelationSubject\n        """
        self.Object = None
        self.Relation = None
        self.Subject = None


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self.Object = []
            for item in params.get("Object"):
                obj = EntityRelationObject()
                obj._deserialize(item)
                self.Object.append(obj)
        self.Relation = params.get("Relation")
        if params.get("Subject") is not None:
            self.Subject = []
            for item in params.get("Subject"):
                obj = EntityRelationSubject()
                obj._deserialize(item)
                self.Subject.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationObject(AbstractModel):
    """实体关系查询返回的Object类型

    """

    def __init__(self):
        """
        :param Popular: object对应popular值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Popular: list of int\n        :param Id: object对应id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: list of str\n        :param Name: object对应name
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: list of str\n        """
        self.Popular = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Popular = params.get("Popular")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EntityRelationSubject(AbstractModel):
    """实体关系查询返回Subject

    """

    def __init__(self):
        """
        :param Popular: Subject对应popular\n        :type Popular: list of int\n        :param Id: Subject对应id\n        :type Id: list of str\n        :param Name: Subject对应name\n        :type Name: list of str\n        """
        self.Popular = None
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Popular = params.get("Popular")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Keyword(AbstractModel):
    """关键词提取结果

    """

    def __init__(self):
        """
        :param Score: 权重\n        :type Score: float\n        :param Word: 关键词\n        :type Word: str\n        """
        self.Score = None
        self.Word = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Word = params.get("Word")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordsExtractionRequest(AbstractModel):
    """KeywordsExtraction请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待处理的文本（仅支持UTF-8格式，不超过10000字）\n        :type Text: str\n        :param Num: 指定关键词个数上限（默认值为5）\n        :type Num: int\n        """
        self.Text = None
        self.Num = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordsExtractionResponse(AbstractModel):
    """KeywordsExtraction返回参数结构体

    """

    def __init__(self):
        """
        :param Keywords: 关键词提取结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type Keywords: list of Keyword\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Keywords = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Keywords") is not None:
            self.Keywords = []
            for item in params.get("Keywords"):
                obj = Keyword()
                obj._deserialize(item)
                self.Keywords.append(obj)
        self.RequestId = params.get("RequestId")


class LexicalAnalysisRequest(AbstractModel):
    """LexicalAnalysis请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过500字）\n        :type Text: str\n        :param DictId: 指定要加载的自定义词库ID。\n        :type DictId: str\n        :param Flag: 词法分析模式（默认取2值）：
1、高精度（混合粒度分词能力）；
2、高性能（单粒度分词能力）；\n        :type Flag: int\n        """
        self.Text = None
        self.DictId = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.DictId = params.get("DictId")
        self.Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LexicalAnalysisResponse(AbstractModel):
    """LexicalAnalysis返回参数结构体

    """

    def __init__(self):
        """
        :param NerTokens: 命名实体识别结果。取值范围：
<li>PER：表示人名，如刘德华、贝克汉姆</li>
<li>LOC：表示地名，如北京、华山</li>
<li>ORG：表示机构团体名，如腾讯、最高人民法院、人大附中</li>
<li>PRODUCTION：表示产品名，如QQ、微信、iPhone</li>
注意：此字段可能返回 null，表示取不到有效值。\n        :type NerTokens: list of NerToken\n        :param PosTokens: 分词&词性标注结果（词性表请参见附录）\n        :type PosTokens: list of PosToken\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NerTokens = None
        self.PosTokens = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NerTokens") is not None:
            self.NerTokens = []
            for item in params.get("NerTokens"):
                obj = NerToken()
                obj._deserialize(item)
                self.NerTokens.append(obj)
        if params.get("PosTokens") is not None:
            self.PosTokens = []
            for item in params.get("PosTokens"):
                obj = PosToken()
                obj._deserialize(item)
                self.PosTokens.append(obj)
        self.RequestId = params.get("RequestId")


class NerToken(AbstractModel):
    """命名实体识别结果

    """

    def __init__(self):
        """
        :param Word: 基础词\n        :type Word: str\n        :param Length: 长度\n        :type Length: int\n        :param BeginOffset: 起始位置\n        :type BeginOffset: int\n        :param Type: 命名实体类型\n        :type Type: str\n        """
        self.Word = None
        self.Length = None
        self.BeginOffset = None
        self.Type = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.Length = params.get("Length")
        self.BeginOffset = params.get("BeginOffset")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PosToken(AbstractModel):
    """分词&词性标注结果

    """

    def __init__(self):
        """
        :param Word: 基础词\n        :type Word: str\n        :param Length: 长度\n        :type Length: int\n        :param BeginOffset: 起始位置\n        :type BeginOffset: int\n        :param Pos: 词性\n        :type Pos: str\n        """
        self.Word = None
        self.Length = None
        self.BeginOffset = None
        self.Pos = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.Length = params.get("Length")
        self.BeginOffset = params.get("BeginOffset")
        self.Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchResult(AbstractModel):
    """词条搜索的结果，主要描述该词条是否存在以及相关的词性。

    """

    def __init__(self):
        """
        :param Text: 被搜索的词条文本。\n        :type Text: str\n        :param IsExist: 0表示词条不存在，1表示存在。\n        :type IsExist: int\n        :param MatchText: 匹配到的词条文本。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MatchText: str\n        :param Pos: 词条的词性。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pos: str\n        """
        self.Text = None
        self.IsExist = None
        self.MatchText = None
        self.Pos = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.IsExist = params.get("IsExist")
        self.MatchText = params.get("MatchText")
        self.Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchWordItemsRequest(AbstractModel):
    """SearchWordItems请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 自定义词库ID。\n        :type DictId: str\n        :param WordItems: 待检索的词条集合。\n        :type WordItems: list of WordItem\n        """
        self.DictId = None
        self.WordItems = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        if params.get("WordItems") is not None:
            self.WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self.WordItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchWordItemsResponse(AbstractModel):
    """SearchWordItems返回参数结构体

    """

    def __init__(self):
        """
        :param Results: 词条检索结果集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Results: list of SearchResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Results = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = SearchResult()
                obj._deserialize(item)
                self.Results.append(obj)
        self.RequestId = params.get("RequestId")


class SentenceEmbeddingRequest(AbstractModel):
    """SentenceEmbedding请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 输入的文本（仅支持UTF-8格式，不超过500字）\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceEmbeddingResponse(AbstractModel):
    """SentenceEmbedding返回参数结构体

    """

    def __init__(self):
        """
        :param Vector: 句向量数组\n        :type Vector: list of float\n        :param Dimension: 句向量的维度\n        :type Dimension: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Vector = None
        self.Dimension = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vector = params.get("Vector")
        self.Dimension = params.get("Dimension")
        self.RequestId = params.get("RequestId")


class SentimentAnalysisRequest(AbstractModel):
    """SentimentAnalysis请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）\n        :type Text: str\n        :param Flag: 待分析文本所属的类型，仅当输入参数Mode取值为2class时有效（默认取4值）：
1、商品评论类
2、社交类
3、美食酒店类
4、通用领域类\n        :type Flag: int\n        :param Mode: 情感分类模式选项，可取2class或3class（默认值为2class）
1、2class：返回正负面二分类情感结果
2、3class：返回正负面及中性三分类情感结果\n        :type Mode: str\n        """
        self.Text = None
        self.Flag = None
        self.Mode = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")
        self.Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentAnalysisResponse(AbstractModel):
    """SentimentAnalysis返回参数结构体

    """

    def __init__(self):
        """
        :param Positive: 正面情感概率\n        :type Positive: float\n        :param Neutral: 中性情感概率，当输入参数Mode取值为3class时有效，否则值为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type Neutral: float\n        :param Negative: 负面情感概率\n        :type Negative: float\n        :param Sentiment: 情感分类结果：
1、positive，表示正面情感
2、negative，表示负面情感
3、neutral，表示中性、无情感\n        :type Sentiment: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Positive = None
        self.Neutral = None
        self.Negative = None
        self.Sentiment = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Positive = params.get("Positive")
        self.Neutral = params.get("Neutral")
        self.Negative = params.get("Negative")
        self.Sentiment = params.get("Sentiment")
        self.RequestId = params.get("RequestId")


class SimilarWordsRequest(AbstractModel):
    """SimilarWords请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）\n        :type Text: str\n        :param WordNumber: 相似词个数；取值范围：1-200，默认为10；\n        :type WordNumber: int\n        """
        self.Text = None
        self.WordNumber = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.WordNumber = params.get("WordNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarWordsResponse(AbstractModel):
    """SimilarWords返回参数结构体

    """

    def __init__(self):
        """
        :param SimilarWords: 相似词数组\n        :type SimilarWords: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SimilarWords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SimilarWords = params.get("SimilarWords")
        self.RequestId = params.get("RequestId")


class Similarity(AbstractModel):
    """文本相似度

    """

    def __init__(self):
        """
        :param Text: 目标文本句子\n        :type Text: str\n        :param Score: 相似度分数\n        :type Score: float\n        """
        self.Text = None
        self.Score = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextClassificationRequest(AbstractModel):
    """TextClassification请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分类的文本（仅支持UTF-8格式，不超过10000字）\n        :type Text: str\n        :param Flag: 领域分类体系（默认取1值）：
1、通用领域，二分类
2、新闻领域，五分类。类别数据不一定全部返回，详情见类目映射表\n        :type Flag: int\n        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextClassificationResponse(AbstractModel):
    """TextClassification返回参数结构体

    """

    def __init__(self):
        """
        :param Classes: 文本分类结果（文本分类映射表请参见附录）\n        :type Classes: list of ClassificationResult\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Classes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Classes") is not None:
            self.Classes = []
            for item in params.get("Classes"):
                obj = ClassificationResult()
                obj._deserialize(item)
                self.Classes.append(obj)
        self.RequestId = params.get("RequestId")


class TextCorrectionRequest(AbstractModel):
    """TextCorrection请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过2000字符）\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextCorrectionResponse(AbstractModel):
    """TextCorrection返回参数结构体

    """

    def __init__(self):
        """
        :param CCITokens: 纠错详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type CCITokens: list of CCIToken\n        :param ResultText: 纠错后的文本\n        :type ResultText: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CCITokens = None
        self.ResultText = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CCITokens") is not None:
            self.CCITokens = []
            for item in params.get("CCITokens"):
                obj = CCIToken()
                obj._deserialize(item)
                self.CCITokens.append(obj)
        self.ResultText = params.get("ResultText")
        self.RequestId = params.get("RequestId")


class TextSimilarityRequest(AbstractModel):
    """TextSimilarity请求参数结构体

    """

    def __init__(self):
        """
        :param SrcText: 需要与目标句子计算相似度的源句子（仅支持UTF-8格式，不超过500字符）\n        :type SrcText: str\n        :param TargetText: 目标句子\n        :type TargetText: list of str\n        """
        self.SrcText = None
        self.TargetText = None


    def _deserialize(self, params):
        self.SrcText = params.get("SrcText")
        self.TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextSimilarityResponse(AbstractModel):
    """TextSimilarity返回参数结构体

    """

    def __init__(self):
        """
        :param Similarity: 每个目标句子与源句子的相似度分值，按照分值降序排列\n        :type Similarity: list of Similarity\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Similarity") is not None:
            self.Similarity = []
            for item in params.get("Similarity"):
                obj = Similarity()
                obj._deserialize(item)
                self.Similarity.append(obj)
        self.RequestId = params.get("RequestId")


class TripleContent(AbstractModel):
    """三元组查询返回的元记录

    """

    def __init__(self):
        """
        :param Popular: 实体流行度
注意：此字段可能返回 null，表示取不到有效值。\n        :type Popular: int\n        :param Name: 实体名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Order: 实体order
注意：此字段可能返回 null，表示取不到有效值。\n        :type Order: int\n        :param Id: 实体id
注意：此字段可能返回 null，表示取不到有效值。\n        :type Id: str\n        """
        self.Popular = None
        self.Name = None
        self.Order = None
        self.Id = None


    def _deserialize(self, params):
        self.Popular = params.get("Popular")
        self.Name = params.get("Name")
        self.Order = params.get("Order")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictRequest(AbstractModel):
    """UpdateDict请求参数结构体

    """

    def __init__(self):
        """
        :param DictId: 自定义词库ID。\n        :type DictId: str\n        :param Description: 词库描述，不超过100字。\n        :type Description: str\n        :param Name: 词库名称，不超过20字。\n        :type Name: str\n        """
        self.DictId = None
        self.Description = None
        self.Name = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        self.Description = params.get("Description")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictResponse(AbstractModel):
    """UpdateDict返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WordEmbeddingRequest(AbstractModel):
    """WordEmbedding请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）\n        :type Text: str\n        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordEmbeddingResponse(AbstractModel):
    """WordEmbedding返回参数结构体

    """

    def __init__(self):
        """
        :param Vector: 词向量数组\n        :type Vector: list of float\n        :param Dimension: 词向量的维度\n        :type Dimension: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Vector = None
        self.Dimension = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vector = params.get("Vector")
        self.Dimension = params.get("Dimension")
        self.RequestId = params.get("RequestId")


class WordItem(AbstractModel):
    """词条信息。

    """

    def __init__(self):
        """
        :param Text: 词条文本内容。\n        :type Text: str\n        :param CreateTime: 词条创建时间。\n        :type CreateTime: str\n        :param Pos: 词条的词性。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Pos: str\n        """
        self.Text = None
        self.CreateTime = None
        self.Pos = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.CreateTime = params.get("CreateTime")
        self.Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordSimilarityRequest(AbstractModel):
    """WordSimilarity请求参数结构体

    """

    def __init__(self):
        """
        :param SrcWord: 计算相似度的源词（仅支持UTF-8格式，不超过20字）\n        :type SrcWord: str\n        :param TargetWord: 计算相似度的目标词（仅支持UTF-8格式，不超过20字）\n        :type TargetWord: str\n        """
        self.SrcWord = None
        self.TargetWord = None


    def _deserialize(self, params):
        self.SrcWord = params.get("SrcWord")
        self.TargetWord = params.get("TargetWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordSimilarityResponse(AbstractModel):
    """WordSimilarity返回参数结构体

    """

    def __init__(self):
        """
        :param Similarity: 两个词语的相似度\n        :type Similarity: float\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.RequestId = params.get("RequestId")