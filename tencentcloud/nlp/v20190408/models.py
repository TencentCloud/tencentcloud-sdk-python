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


class AnalyzeSentimentRequest(AbstractModel):
    """AnalyzeSentiment请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）。
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeSentimentResponse(AbstractModel):
    """AnalyzeSentiment返回参数结构体

    """

    def __init__(self):
        r"""
        :param Positive: 正面情感概率。
        :type Positive: float
        :param Neutral: 中性情感概率。
        :type Neutral: float
        :param Negative: 负面情感概率。
        :type Negative: float
        :param Sentiment: 情感分类结果：
positive：正面情感
negative：负面情感
neutral：中性、无情感
        :type Sentiment: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class AutoSummarizationRequest(AbstractModel):
    """AutoSummarization请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
        :type Text: str
        :param Length: 指定摘要的长度上限（默认值为200）
注：为保证摘要的可读性，最终生成的摘要长度会低于指定的长度上限。
        :type Length: int
        """
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
        r"""
        :param Summary: 文本摘要结果
        :type Summary: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Summary = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Summary = params.get("Summary")
        self.RequestId = params.get("RequestId")


class BasicParticiple(AbstractModel):
    """基础粒度分词和词性标注的结果

    """

    def __init__(self):
        r"""
        :param Word: 基础词。
        :type Word: str
        :param BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param Length: 基础词的长度。
        :type Length: int
        :param Pos: 词性。
        :type Pos: str
        """
        self.Word = None
        self.BeginOffset = None
        self.Length = None
        self.Pos = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCIToken(AbstractModel):
    """文本纠错结果

    """

    def __init__(self):
        r"""
        :param Word: 错别字内容
        :type Word: str
        :param BeginOffset: 错别字的起始位置，从0开始
        :type BeginOffset: int
        :param CorrectWord: 错别字纠错结果
        :type CorrectWord: str
        """
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
        


class Category(AbstractModel):
    """分类详细信息

    """

    def __init__(self):
        r"""
        :param Id: 分类id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param Label: 分类英文名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param Name: 分类中文名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Score: 分类置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self.Id = None
        self.Label = None
        self.Name = None
        self.Score = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Label = params.get("Label")
        self.Name = params.get("Name")
        self.Score = params.get("Score")
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
        r"""
        :param Query: 用户请求的query
        :type Query: str
        :param OpenId: 服务的id,  主要用于儿童闲聊接口，比如手Q的openid
        :type OpenId: str
        :param Flag: 0: 通用闲聊, 1:儿童闲聊, 默认是通用闲聊
        :type Flag: int
        """
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
        r"""
        :param Reply: 闲聊回复
        :type Reply: str
        :param Confidence: 对于当前输出回复的自信度
        :type Confidence: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param FirstClassName: 一级分类名称
        :type FirstClassName: str
        :param SecondClassName: 二级分类名称
        :type SecondClassName: str
        :param FirstClassProbability: 一级分类概率
        :type FirstClassProbability: float
        :param SecondClassProbability: 二级分类概率
        :type SecondClassProbability: float
        :param ThirdClassName: 三级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type ThirdClassName: str
        :param ThirdClassProbability: 三级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type ThirdClassProbability: float
        :param FourthClassName: 四级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FourthClassName: str
        :param FourthClassProbability: 四级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FourthClassProbability: float
        :param FifthClassName: 五级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FifthClassName: str
        :param FifthClassProbability: 五级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FifthClassProbability: float
        """
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
        


class ClassifyContentRequest(AbstractModel):
    """ClassifyContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param Title: 待分类的文章的标题（仅支持UTF-8格式，不超过100字符）。
        :type Title: str
        :param Content: 待分类文章的内容, 每个元素对应一个段落。（仅支持UTF-8格式，文章内容长度总和不超过2000字符）
        :type Content: list of str
        """
        self.Title = None
        self.Content = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyContentResponse(AbstractModel):
    """ClassifyContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param FirstClassification: 一级分类。分类详情见附录-三级分类体系表。
        :type FirstClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param SecondClassification: 二级分类。分类详情见附录-三级分类体系表。
        :type SecondClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param ThirdClassification: 三级分类。分类详情见附录-三级分类体系表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.FirstClassification = None
        self.SecondClassification = None
        self.ThirdClassification = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FirstClassification") is not None:
            self.FirstClassification = Category()
            self.FirstClassification._deserialize(params.get("FirstClassification"))
        if params.get("SecondClassification") is not None:
            self.SecondClassification = Category()
            self.SecondClassification._deserialize(params.get("SecondClassification"))
        if params.get("ThirdClassification") is not None:
            self.ThirdClassification = Category()
            self.ThirdClassification._deserialize(params.get("ThirdClassification"))
        self.RequestId = params.get("RequestId")


class ComposeCoupletRequest(AbstractModel):
    """ComposeCouplet请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 生成对联的关键词。长度需>=2，当长度>2时，自动截取前两个字作为关键字。内容需为常用汉字（不含有数字、英文、韩语、日语、符号等等其他）。
        :type Text: str
        :param TargetType: 返回的文本结果为繁体还是简体。0：简体；1：繁体。默认为0。
        :type TargetType: int
        """
        self.Text = None
        self.TargetType = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeCoupletResponse(AbstractModel):
    """ComposeCouplet返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopScroll: 横批。
        :type TopScroll: str
        :param Content: 上联与下联。
        :type Content: list of str
        :param RandomCause: 当对联随机生成时，展示随机生成原因。
        :type RandomCause: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopScroll = None
        self.Content = None
        self.RandomCause = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopScroll = params.get("TopScroll")
        self.Content = params.get("Content")
        self.RandomCause = params.get("RandomCause")
        self.RequestId = params.get("RequestId")


class ComposePoetryRequest(AbstractModel):
    """ComposePoetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 生成诗词的关键词。
        :type Text: str
        :param PoetryType: 生成诗词的类型。0：藏头或藏身；1：藏头；2：藏身。默认为0。
        :type PoetryType: int
        :param Genre: 诗的体裁。0：五言律诗或七言律诗；5：五言律诗；7：七言律诗。默认为0。
        :type Genre: int
        """
        self.Text = None
        self.PoetryType = None
        self.Genre = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.PoetryType = params.get("PoetryType")
        self.Genre = params.get("Genre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposePoetryResponse(AbstractModel):
    """ComposePoetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param Title: 诗题，即输入的生成诗词的关键词。
        :type Title: str
        :param Content: 诗的内容。
        :type Content: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Title = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Content = params.get("Content")
        self.RequestId = params.get("RequestId")


class CompoundParticiple(AbstractModel):
    """复合粒度分词和词性标注的结果。

    """

    def __init__(self):
        r"""
        :param Word: 基础词。
        :type Word: str
        :param BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param Length: 基础词的长度。
        :type Length: int
        :param Pos: 词性。
        :type Pos: str
        """
        self.Word = None
        self.BeginOffset = None
        self.Length = None
        self.Pos = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorrectionItem(AbstractModel):
    """纠错结果列表

    """

    def __init__(self):
        r"""
        :param Order: 纠错句子的序号。
        :type Order: int
        :param BeginOffset: 错误的起始位置，从0开始。
        :type BeginOffset: int
        :param Len: 错误内容长度。
        :type Len: int
        :param Word: 错误内容。
        :type Word: str
        :param CorrectWord: 纠错结果，当为删除类错误时，结果为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectWord: list of str
        :param CorrectionType: 纠错类型。0：替换；1：插入；2：删除。
        :type CorrectionType: int
        :param Confidence: 纠错信息置信度。0：error；1：warning；error的置信度更高。（仅供参考）
        :type Confidence: int
        :param DescriptionZh: 纠错信息中文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionZh: str
        :param DescriptionEn: 纠错信息英文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionEn: str
        """
        self.Order = None
        self.BeginOffset = None
        self.Len = None
        self.Word = None
        self.CorrectWord = None
        self.CorrectionType = None
        self.Confidence = None
        self.DescriptionZh = None
        self.DescriptionEn = None


    def _deserialize(self, params):
        self.Order = params.get("Order")
        self.BeginOffset = params.get("BeginOffset")
        self.Len = params.get("Len")
        self.Word = params.get("Word")
        self.CorrectWord = params.get("CorrectWord")
        self.CorrectionType = params.get("CorrectionType")
        self.Confidence = params.get("Confidence")
        self.DescriptionZh = params.get("DescriptionZh")
        self.DescriptionEn = params.get("DescriptionEn")
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
        r"""
        :param Name: 自定义词库名称，不超过20字。
        :type Name: str
        :param Description: 自定义词库描述，不超过100字。
        :type Description: str
        """
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
        r"""
        :param DictId: 创建的自定义词库ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DictId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DictId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DictId = params.get("DictId")
        self.RequestId = params.get("RequestId")


class CreateWordItemsRequest(AbstractModel):
    """CreateWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param DictId: 自定义词库ID。
        :type DictId: str
        :param WordItems: 待添加的词条集合。
        :type WordItems: list of WordItem
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDictRequest(AbstractModel):
    """DeleteDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param DictId: 要删除的自定义词库ID。
        :type DictId: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWordItemsRequest(AbstractModel):
    """DeleteWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param DictId: 自定义词库ID。
        :type DictId: str
        :param WordItems: 待删除的词条集合。
        :type WordItems: list of WordItem
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DependencyParsingRequest(AbstractModel):
    """DependencyParsing请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
        :type Text: str
        """
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
        r"""
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
<li>核心关系，eg: 整个句子的核心
        :type DpTokens: list of DpToken
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param DictId: 自定义词库ID。
        :type DictId: str
        :param Name: 自定义词库名称，模糊搜索。
        :type Name: str
        """
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
        r"""
        :param Dicts: 查询到的词库信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Dicts: list of DictInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Limit: 每页数据量，范围为1~100，默认为10。
        :type Limit: int
        :param Offset: 分页偏移量，从0开始，默认为0。
        :type Offset: int
        """
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
        r"""
        :param TotalCount: 记录总条数。
        :type TotalCount: int
        :param Dicts: 自定义词库信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Dicts: list of DictInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeWordItemsRequest(AbstractModel):
    """DescribeWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param DictId: 自定义词库ID。
        :type DictId: str
        :param Offset: 分页偏移量，从0开始，默认为0。
        :type Offset: int
        :param Limit: 每页数据量，范围为1~100，默认为10。
        :type Limit: int
        :param Text: 待检索的词条文本，支持模糊匹配。
        :type Text: str
        """
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
        r"""
        :param TotalCount: 词条记录总条数。
        :type TotalCount: int
        :param WordItems: 词条信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type WordItems: list of WordItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Name: 自定义词库名称。
        :type Name: str
        :param Id: 自定义词库ID。
        :type Id: str
        :param Description: 自定义词库描述信息。
        :type Description: str
        :param UpdateTime: 自定义词库修改时间，形式为:yyyy-mm-dd hh:mm:ss。
        :type UpdateTime: str
        :param CreateTime: 自定义词库创建时间，形式为:yyyy-mm-dd hh:mm:ss。
        :type CreateTime: str
        """
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
        r"""
        :param Relation: 句法依存关系的类型
        :type Relation: str
        :param HeadId: 当前词父节点的序号
        :type HeadId: int
        :param Word: 基础词
        :type Word: str
        :param Id: 基础词的序号
        :type Id: int
        """
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
        


class Embellish(AbstractModel):
    """文本润色结果

    """

    def __init__(self):
        r"""
        :param Text: 润色后的文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param EmbellishType: 润色类型。类型如下：
expansion：扩写
rewriting：改写
translation_m2a：从现代文改写为古文
translation_a2m：从古文改写为现代文


注意：此字段可能返回 null，表示取不到有效值。
        :type EmbellishType: str
        """
        self.Text = None
        self.EmbellishType = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.EmbellishType = params.get("EmbellishType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Entity(AbstractModel):
    """实体识别结果。

    """

    def __init__(self):
        r"""
        :param Word: 基础词。
        :type Word: str
        :param BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param Length: 基础词的长度。
        :type Length: int
        :param Type: 实体类型的标准名字。
        :type Type: str
        :param Name: 类型名字的自然语言表达。（中文或英文）
        :type Name: str
        """
        self.Word = None
        self.BeginOffset = None
        self.Length = None
        self.Type = None
        self.Name = None


    def _deserialize(self, params):
        self.Word = params.get("Word")
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Type = params.get("Type")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateSentenceSimilarityRequest(AbstractModel):
    """EvaluateSentenceSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param SentencePairList: 待分析的句子对数组。句子对应不超过5对，支持中英文文本，原句子与目标句子均应不超过500字符。
        :type SentencePairList: list of SentencePair
        """
        self.SentencePairList = None


    def _deserialize(self, params):
        if params.get("SentencePairList") is not None:
            self.SentencePairList = []
            for item in params.get("SentencePairList"):
                obj = SentencePair()
                obj._deserialize(item)
                self.SentencePairList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateSentenceSimilarityResponse(AbstractModel):
    """EvaluateSentenceSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param ScoreList: 每个句子对的相似度分值。
        :type ScoreList: list of float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ScoreList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ScoreList = params.get("ScoreList")
        self.RequestId = params.get("RequestId")


class EvaluateWordSimilarityRequest(AbstractModel):
    """EvaluateWordSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param SourceWord: 计算相似度的源词。（仅支持UTF-8格式，不超过10字符）

        :type SourceWord: str
        :param TargetWord: 计算相似度的目标词。（仅支持UTF-8格式，不超过10字符）

        :type TargetWord: str
        """
        self.SourceWord = None
        self.TargetWord = None


    def _deserialize(self, params):
        self.SourceWord = params.get("SourceWord")
        self.TargetWord = params.get("TargetWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateWordSimilarityResponse(AbstractModel):
    """EvaluateWordSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param Similarity: 词相似度分值。
        :type Similarity: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.RequestId = params.get("RequestId")


class GenerateCoupletRequest(AbstractModel):
    """GenerateCouplet请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 生成对联的关键词。长度需>=2，当长度>2时，自动截取前两个字作为关键字。内容需为常用汉字（不含有数字、英文、韩语、日语、符号等等其他）。
        :type Text: str
        :param TargetType: 返回的文本结果为繁体还是简体。0：简体；1：繁体。默认为0。
        :type TargetType: int
        """
        self.Text = None
        self.TargetType = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCoupletResponse(AbstractModel):
    """GenerateCouplet返回参数结构体

    """

    def __init__(self):
        r"""
        :param TopScroll: 横批。
        :type TopScroll: str
        :param Content: 上联与下联。
        :type Content: list of str
        :param RandomCause: 当对联随机生成时，展示随机生成原因。
        :type RandomCause: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopScroll = None
        self.Content = None
        self.RandomCause = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopScroll = params.get("TopScroll")
        self.Content = params.get("Content")
        self.RandomCause = params.get("RandomCause")
        self.RequestId = params.get("RequestId")


class GenerateKeywordSentenceRequest(AbstractModel):
    """GenerateKeywordSentence请求参数结构体

    """

    def __init__(self):
        r"""
        :param WordList: 生成句子的关键词，关键词个数需不超过4个，中文关键词长度应不超过10字符，英文关键词长度不超过3个单词。关键词中不可包含标点符号。
        :type WordList: list of str
        :param Number: 返回生成句子的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param Domain: 指定生成句子的领域，支持领域如下：
general：通用领域，支持中英文
academic：学术领域，仅支持英文
默认为general（通用领域）。
        :type Domain: str
        """
        self.WordList = None
        self.Number = None
        self.Domain = None


    def _deserialize(self, params):
        self.WordList = params.get("WordList")
        self.Number = params.get("Number")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateKeywordSentenceResponse(AbstractModel):
    """GenerateKeywordSentence返回参数结构体

    """

    def __init__(self):
        r"""
        :param KeywordSentenceList: 生成的句子列表。
        :type KeywordSentenceList: list of KeywordSentence
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.KeywordSentenceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("KeywordSentenceList") is not None:
            self.KeywordSentenceList = []
            for item in params.get("KeywordSentenceList"):
                obj = KeywordSentence()
                obj._deserialize(item)
                self.KeywordSentenceList.append(obj)
        self.RequestId = params.get("RequestId")


class GeneratePoetryRequest(AbstractModel):
    """GeneratePoetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 生成诗词的关键词。
        :type Text: str
        :param PoetryType: 生成诗词的类型。0：藏头或藏身；1：藏头；2：藏身。默认为0。
        :type PoetryType: int
        :param Genre: 诗的体裁。0：五言律诗或七言律诗；5：五言律诗；7：七言律诗。默认为0。
        :type Genre: int
        """
        self.Text = None
        self.PoetryType = None
        self.Genre = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.PoetryType = params.get("PoetryType")
        self.Genre = params.get("Genre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneratePoetryResponse(AbstractModel):
    """GeneratePoetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param Title: 诗题，即输入的生成诗词的关键词。
        :type Title: str
        :param Content: 诗的内容。
        :type Content: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Title = None
        self.Content = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Title = params.get("Title")
        self.Content = params.get("Content")
        self.RequestId = params.get("RequestId")


class Keyword(AbstractModel):
    """关键词提取结果

    """

    def __init__(self):
        r"""
        :param Score: 权重
        :type Score: float
        :param Word: 关键词
        :type Word: str
        """
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
        


class KeywordSentence(AbstractModel):
    """通过关键词生成的句子信息

    """

    def __init__(self):
        r"""
        :param TargetText: 通过关键词生成的句子。
        :type TargetText: str
        """
        self.TargetText = None


    def _deserialize(self, params):
        self.TargetText = params.get("TargetText")
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
        r"""
        :param Text: 待处理的文本（仅支持UTF-8格式，不超过10000字符）
        :type Text: str
        :param Num: 指定关键词个数上限（默认值为5）
        :type Num: int
        """
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
        r"""
        :param Keywords: 关键词提取结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of Keyword
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过500字）
        :type Text: str
        :param DictId: 指定要加载的自定义词库ID。
        :type DictId: str
        :param Flag: 词法分析模式（默认取2值）：
1、高精度（混合粒度分词能力）；
2、高性能（单粒度分词能力）；
        :type Flag: int
        """
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
        r"""
        :param NerTokens: 命名实体识别结果。取值范围：
<li>PER：表示人名，如刘德华、贝克汉姆</li>
<li>LOC：表示地名，如北京、华山</li>
<li>ORG：表示机构团体名，如腾讯、最高人民法院、人大附中</li>
<li>PRODUCTION：表示产品名，如QQ、微信、iPhone</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NerTokens: list of NerToken
        :param PosTokens: 分词&词性标注结果（词性表请参见附录）
        :type PosTokens: list of PosToken
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Word: 基础词
        :type Word: str
        :param Length: 长度
        :type Length: int
        :param BeginOffset: 起始位置
        :type BeginOffset: int
        :param Type: 命名实体类型
        :type Type: str
        """
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
        


class ParseWordsRequest(AbstractModel):
    """ParseWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待分析的文本（支持中英文文本，不超过500字符）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseWordsResponse(AbstractModel):
    """ParseWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param NormalText: 输入文本正则化的结果。（包括对英文文本中的开头和实体进行大写等）
        :type NormalText: str
        :param BasicParticiples: 基础粒度分词和词性标注的结果。（词性表请参见附录）

        :type BasicParticiples: list of BasicParticiple
        :param CompoundParticiples: 复合粒度分词和词性标注的结果。（词性表请参见附录）
        :type CompoundParticiples: list of CompoundParticiple
        :param Entities: 实体识别结果。（实体类型数据请参见附录）

        :type Entities: list of Entity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NormalText = None
        self.BasicParticiples = None
        self.CompoundParticiples = None
        self.Entities = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NormalText = params.get("NormalText")
        if params.get("BasicParticiples") is not None:
            self.BasicParticiples = []
            for item in params.get("BasicParticiples"):
                obj = BasicParticiple()
                obj._deserialize(item)
                self.BasicParticiples.append(obj)
        if params.get("CompoundParticiples") is not None:
            self.CompoundParticiples = []
            for item in params.get("CompoundParticiples"):
                obj = CompoundParticiple()
                obj._deserialize(item)
                self.CompoundParticiples.append(obj)
        if params.get("Entities") is not None:
            self.Entities = []
            for item in params.get("Entities"):
                obj = Entity()
                obj._deserialize(item)
                self.Entities.append(obj)
        self.RequestId = params.get("RequestId")


class PosToken(AbstractModel):
    """分词&词性标注结果

    """

    def __init__(self):
        r"""
        :param Word: 基础词
        :type Word: str
        :param Length: 长度
        :type Length: int
        :param BeginOffset: 起始位置
        :type BeginOffset: int
        :param Pos: 词性
        :type Pos: str
        """
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
        


class RetrieveSimilarWordsRequest(AbstractModel):
    """RetrieveSimilarWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 输入的词语。（仅支持UTF-8格式，不超过10字符）
        :type Text: str
        :param Number: 召回的相似词个数，取值范围为1-20。
        :type Number: int
        """
        self.Text = None
        self.Number = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveSimilarWordsResponse(AbstractModel):
    """RetrieveSimilarWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param WordList: 召回的相似词数组。
        :type WordList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.WordList = params.get("WordList")
        self.RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """词条搜索的结果，主要描述该词条是否存在以及相关的词性。

    """

    def __init__(self):
        r"""
        :param Text: 被搜索的词条文本。
        :type Text: str
        :param IsExist: 0表示词条不存在，1表示存在。
        :type IsExist: int
        :param MatchText: 匹配到的词条文本。
        :type MatchText: str
        :param Pos: 词条的词性。
        :type Pos: str
        """
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
        r"""
        :param DictId: 自定义词库ID。
        :type DictId: str
        :param WordItems: 待检索的词条集合。
        :type WordItems: list of WordItem
        """
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
        r"""
        :param Results: 词条检索结果集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of SearchResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class SentenceCorrectionRequest(AbstractModel):
    """SentenceCorrection请求参数结构体

    """

    def __init__(self):
        r"""
        :param TextList: 待纠错的句子列表。可以以数组方式在一次请求中填写多个待纠错的句子。文本统一使用utf-8格式编码，每个中文句子的长度不超过150字符，每个英文句子的长度不超过100个单词，且数组长度需小于150，即句子总数需少于150句。
        :type TextList: list of str
        """
        self.TextList = None


    def _deserialize(self, params):
        self.TextList = params.get("TextList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceCorrectionResponse(AbstractModel):
    """SentenceCorrection返回参数结构体

    """

    def __init__(self):
        r"""
        :param CorrectionList: 纠错结果列表。
（注意仅展示错误句子的纠错结果，若句子无错则不展示，若全部待纠错句子都被认为无错，则可能返回数组为空）
        :type CorrectionList: list of CorrectionItem
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CorrectionList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CorrectionList") is not None:
            self.CorrectionList = []
            for item in params.get("CorrectionList"):
                obj = CorrectionItem()
                obj._deserialize(item)
                self.CorrectionList.append(obj)
        self.RequestId = params.get("RequestId")


class SentenceEmbeddingRequest(AbstractModel):
    """SentenceEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 输入的文本（仅支持UTF-8格式，不超过500字）
        :type Text: str
        """
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
        r"""
        :param Vector: 句向量数组
        :type Vector: list of float
        :param Dimension: 句向量的维度
        :type Dimension: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Vector = None
        self.Dimension = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Vector = params.get("Vector")
        self.Dimension = params.get("Dimension")
        self.RequestId = params.get("RequestId")


class SentencePair(AbstractModel):
    """待分析的句子对

    """

    def __init__(self):
        r"""
        :param SourceText: 需要与目标句子计算相似度的源句子。（仅支持UTF-8格式，不超过500字符）
        :type SourceText: str
        :param TargetText: 目标句子。（仅支持UTF-8格式，不超过500字符）

        :type TargetText: str
        """
        self.SourceText = None
        self.TargetText = None


    def _deserialize(self, params):
        self.SourceText = params.get("SourceText")
        self.TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentAnalysisRequest(AbstractModel):
    """SentimentAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
        :type Text: str
        :param Flag: 待分析文本所属的类型，仅当输入参数Mode取值为2class时有效（默认取4值）：
1、商品评论类
2、社交类
3、美食酒店类
4、通用领域类
        :type Flag: int
        :param Mode: 情感分类模式选项，可取2class或3class（默认值为2class）
1、2class：返回正负面二分类情感结果
2、3class：返回正负面及中性三分类情感结果
        :type Mode: str
        """
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
        r"""
        :param Positive: 正面情感概率
        :type Positive: float
        :param Neutral: 中性情感概率，当输入参数Mode取值为3class时有效，否则值为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Neutral: float
        :param Negative: 负面情感概率
        :type Negative: float
        :param Sentiment: 情感分类结果：
1、positive，表示正面情感
2、negative，表示负面情感
3、neutral，表示中性、无情感
        :type Sentiment: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
        :type Text: str
        :param WordNumber: 相似词个数；取值范围：1-200，默认为10；
        :type WordNumber: int
        """
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
        r"""
        :param SimilarWords: 相似词数组
        :type SimilarWords: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SimilarWords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SimilarWords = params.get("SimilarWords")
        self.RequestId = params.get("RequestId")


class Similarity(AbstractModel):
    """文本相似度

    """

    def __init__(self):
        r"""
        :param Text: 目标文本句子
        :type Text: str
        :param Score: 相似度分数
        :type Score: float
        """
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
        r"""
        :param Text: 待分类的文本（仅支持UTF-8格式，不超过10000字）
        :type Text: str
        :param Flag: 领域分类体系（默认取1值）：
1、通用领域，二分类
2、新闻领域，五分类。类别数据不一定全部返回，详情见类目映射表（注意：目前五分类已下线不可用）
        :type Flag: int
        """
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
        r"""
        :param Classes: 文本分类结果（文本分类映射表请参见附录）
        :type Classes: list of ClassificationResult
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class TextCorrectionProRequest(AbstractModel):
    """TextCorrectionPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过128字符）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextCorrectionProResponse(AbstractModel):
    """TextCorrectionPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param CCITokens: 纠错详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CCITokens: list of CCIToken
        :param ResultText: 纠错后的文本
        :type ResultText: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class TextCorrectionRequest(AbstractModel):
    """TextCorrection请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过2000字符）
        :type Text: str
        """
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
        r"""
        :param CCITokens: 纠错详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CCITokens: list of CCIToken
        :param ResultText: 纠错后的文本
        :type ResultText: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class TextEmbellishRequest(AbstractModel):
    """TextEmbellish请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待润色的文本。中文文本长度需<=50字符；英文文本长度需<=30个单词。
        :type Text: str
        :param SourceLang: 待润色文本的语言类型，支持语言如下：
zh：中文
en：英文
        :type SourceLang: str
        :param Number: 返回润色结果的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param Style: 控制润色类型，类型如下：
both：同时返回改写和扩写
expansion：扩写
rewriting：改写
m2a：从现代文改写为古文
a2m：从古文改写为现代文
默认为both。
        :type Style: str
        """
        self.Text = None
        self.SourceLang = None
        self.Number = None
        self.Style = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.SourceLang = params.get("SourceLang")
        self.Number = params.get("Number")
        self.Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextEmbellishResponse(AbstractModel):
    """TextEmbellish返回参数结构体

    """

    def __init__(self):
        r"""
        :param EmbellishList: 润色结果列表。
        :type EmbellishList: list of Embellish
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EmbellishList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EmbellishList") is not None:
            self.EmbellishList = []
            for item in params.get("EmbellishList"):
                obj = Embellish()
                obj._deserialize(item)
                self.EmbellishList.append(obj)
        self.RequestId = params.get("RequestId")


class TextSimilarityProRequest(AbstractModel):
    """TextSimilarityPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param SrcText: 需要与目标句子计算相似度的源句子（仅支持UTF-8格式，不超过128字符）
        :type SrcText: str
        :param TargetText: 目标句子（仅支持UTF-8格式，不超过128字符）
        :type TargetText: list of str
        """
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
        


class TextSimilarityProResponse(AbstractModel):
    """TextSimilarityPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param Similarity: 每个目标句子与源句子的相似度分值，按照分值降序排列
        :type Similarity: list of Similarity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class TextSimilarityRequest(AbstractModel):
    """TextSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param SrcText: 需要与目标句子计算相似度的源句子（仅支持UTF-8格式，不超过500字符）
        :type SrcText: str
        :param TargetText: 目标句子（以句子数量为单位消耗资源包）
        :type TargetText: list of str
        """
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
        r"""
        :param Similarity: 每个目标句子与源句子的相似度分值，按照分值降序排列
        :type Similarity: list of Similarity
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class TextWritingRequest(AbstractModel):
    """TextWriting请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 待续写的句子，文本统一使用utf-8格式编码，长度不超过200字符。
        :type Text: str
        :param SourceLang: 待续写文本的语言类型，支持语言如下：
zh：中文
en：英文
        :type SourceLang: str
        :param Number: 返回续写结果的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param Domain: 指定续写领域，支持领域如下：
general：通用领域，支持中英文补全
academic：学术领域，仅支持英文补全
默认为general（通用领域）。
        :type Domain: str
        :param Style: 指定续写风格，支持风格如下：
science_fiction：科幻
military_history：军事
xuanhuan_wuxia：武侠
urban_officialdom：职场
默认为xuanhuan_wuxia（武侠）。
        :type Style: str
        """
        self.Text = None
        self.SourceLang = None
        self.Number = None
        self.Domain = None
        self.Style = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.SourceLang = params.get("SourceLang")
        self.Number = params.get("Number")
        self.Domain = params.get("Domain")
        self.Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWritingResponse(AbstractModel):
    """TextWriting返回参数结构体

    """

    def __init__(self):
        r"""
        :param WritingList: 续写结果列表。
        :type WritingList: list of Writing
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WritingList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WritingList") is not None:
            self.WritingList = []
            for item in params.get("WritingList"):
                obj = Writing()
                obj._deserialize(item)
                self.WritingList.append(obj)
        self.RequestId = params.get("RequestId")


class UpdateDictRequest(AbstractModel):
    """UpdateDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param DictId: 自定义词库ID。
        :type DictId: str
        :param Description: 词库描述，不超过100字。
        :type Description: str
        :param Name: 词库名称，不超过20字。
        :type Name: str
        """
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
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class WordEmbeddingRequest(AbstractModel):
    """WordEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
        :type Text: str
        """
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
        r"""
        :param Vector: 词向量数组
        :type Vector: list of float
        :param Dimension: 词向量的维度
        :type Dimension: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        r"""
        :param Text: 词条文本内容。
        :type Text: str
        :param CreateTime: 词条创建时间。
        :type CreateTime: str
        :param Pos: 词条的词性。
        :type Pos: str
        """
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
        r"""
        :param SrcWord: 计算相似度的源词（仅支持UTF-8格式，不超过20字）
        :type SrcWord: str
        :param TargetWord: 计算相似度的目标词（仅支持UTF-8格式，不超过20字）
        :type TargetWord: str
        """
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
        r"""
        :param Similarity: 两个词语的相似度
        :type Similarity: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.RequestId = params.get("RequestId")


class Writing(AbstractModel):
    """文本续写结果

    """

    def __init__(self):
        r"""
        :param TargetText: 续写的文本。
        :type TargetText: str
        :param PrefixText: 续写的前缀。
        :type PrefixText: str
        """
        self.TargetText = None
        self.PrefixText = None


    def _deserialize(self, params):
        self.TargetText = params.get("TargetText")
        self.PrefixText = params.get("PrefixText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        