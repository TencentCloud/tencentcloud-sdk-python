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
        :param _Text: 待分析的文本（仅支持UTF-8格式，不超过200字）。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalyzeSentimentResponse(AbstractModel):
    """AnalyzeSentiment返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Positive: 正面情感概率。
        :type Positive: float
        :param _Neutral: 中性情感概率。
        :type Neutral: float
        :param _Negative: 负面情感概率。
        :type Negative: float
        :param _Sentiment: 情感分类结果：
positive：正面情感
negative：负面情感
neutral：中性、无情感
        :type Sentiment: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Positive = None
        self._Neutral = None
        self._Negative = None
        self._Sentiment = None
        self._RequestId = None

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Neutral(self):
        return self._Neutral

    @Neutral.setter
    def Neutral(self, Neutral):
        self._Neutral = Neutral

    @property
    def Negative(self):
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative

    @property
    def Sentiment(self):
        return self._Sentiment

    @Sentiment.setter
    def Sentiment(self, Sentiment):
        self._Sentiment = Sentiment

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Positive = params.get("Positive")
        self._Neutral = params.get("Neutral")
        self._Negative = params.get("Negative")
        self._Sentiment = params.get("Sentiment")
        self._RequestId = params.get("RequestId")


class AutoSummarizationRequest(AbstractModel):
    """AutoSummarization请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
        :type Text: str
        :param _Length: 指定摘要的长度上限（默认值为200）
注：为保证摘要的可读性，最终生成的摘要长度会低于指定的长度上限。
        :type Length: int
        """
        self._Text = None
        self._Length = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Length = params.get("Length")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AutoSummarizationResponse(AbstractModel):
    """AutoSummarization返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Summary: 文本摘要结果
        :type Summary: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Summary = None
        self._RequestId = None

    @property
    def Summary(self):
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Summary = params.get("Summary")
        self._RequestId = params.get("RequestId")


class BasicParticiple(AbstractModel):
    """基础粒度分词和词性标注的结果

    """

    def __init__(self):
        r"""
        :param _Word: 基础词。
        :type Word: str
        :param _BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param _Length: 基础词的长度。
        :type Length: int
        :param _Pos: 词性。
        :type Pos: str
        """
        self._Word = None
        self._BeginOffset = None
        self._Length = None
        self._Pos = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._Length = params.get("Length")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCIToken(AbstractModel):
    """文本纠错结果

    """

    def __init__(self):
        r"""
        :param _Word: 错别字内容
        :type Word: str
        :param _BeginOffset: 错别字的起始位置，从0开始
        :type BeginOffset: int
        :param _CorrectWord: 错别字纠错结果
        :type CorrectWord: str
        """
        self._Word = None
        self._BeginOffset = None
        self._CorrectWord = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def CorrectWord(self):
        return self._CorrectWord

    @CorrectWord.setter
    def CorrectWord(self, CorrectWord):
        self._CorrectWord = CorrectWord


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._CorrectWord = params.get("CorrectWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Category(AbstractModel):
    """分类详细信息

    """

    def __init__(self):
        r"""
        :param _Id: 分类id。
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Label: 分类英文名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Label: str
        :param _Name: 分类中文名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Score: 分类置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :type Score: float
        """
        self._Id = None
        self._Label = None
        self._Name = None
        self._Score = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Label(self):
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Label = params.get("Label")
        self._Name = params.get("Name")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatBotRequest(AbstractModel):
    """ChatBot请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Query: 用户请求的query
        :type Query: str
        :param _OpenId: 服务的id,  主要用于儿童闲聊接口，比如手Q的openid
        :type OpenId: str
        :param _Flag: 0: 通用闲聊, 1:儿童闲聊, 默认是通用闲聊
        :type Flag: int
        """
        self._Query = None
        self._OpenId = None
        self._Flag = None

    @property
    def Query(self):
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def OpenId(self):
        return self._OpenId

    @OpenId.setter
    def OpenId(self, OpenId):
        self._OpenId = OpenId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._Query = params.get("Query")
        self._OpenId = params.get("OpenId")
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ChatBotResponse(AbstractModel):
    """ChatBot返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Reply: 闲聊回复
        :type Reply: str
        :param _Confidence: 对于当前输出回复的自信度
        :type Confidence: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Reply = None
        self._Confidence = None
        self._RequestId = None

    @property
    def Reply(self):
        return self._Reply

    @Reply.setter
    def Reply(self, Reply):
        self._Reply = Reply

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Reply = params.get("Reply")
        self._Confidence = params.get("Confidence")
        self._RequestId = params.get("RequestId")


class ClassificationResult(AbstractModel):
    """文本分类结果

    """

    def __init__(self):
        r"""
        :param _FirstClassName: 一级分类名称
        :type FirstClassName: str
        :param _SecondClassName: 二级分类名称
        :type SecondClassName: str
        :param _FirstClassProbability: 一级分类概率
        :type FirstClassProbability: float
        :param _SecondClassProbability: 二级分类概率
        :type SecondClassProbability: float
        :param _ThirdClassName: 三级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type ThirdClassName: str
        :param _ThirdClassProbability: 三级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type ThirdClassProbability: float
        :param _FourthClassName: 四级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FourthClassName: str
        :param _FourthClassProbability: 四级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FourthClassProbability: float
        :param _FifthClassName: 五级分类名称，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FifthClassName: str
        :param _FifthClassProbability: 五级分类概率，仅有当新闻领域五分类可能出现，详情见文本分类文档
        :type FifthClassProbability: float
        """
        self._FirstClassName = None
        self._SecondClassName = None
        self._FirstClassProbability = None
        self._SecondClassProbability = None
        self._ThirdClassName = None
        self._ThirdClassProbability = None
        self._FourthClassName = None
        self._FourthClassProbability = None
        self._FifthClassName = None
        self._FifthClassProbability = None

    @property
    def FirstClassName(self):
        return self._FirstClassName

    @FirstClassName.setter
    def FirstClassName(self, FirstClassName):
        self._FirstClassName = FirstClassName

    @property
    def SecondClassName(self):
        return self._SecondClassName

    @SecondClassName.setter
    def SecondClassName(self, SecondClassName):
        self._SecondClassName = SecondClassName

    @property
    def FirstClassProbability(self):
        return self._FirstClassProbability

    @FirstClassProbability.setter
    def FirstClassProbability(self, FirstClassProbability):
        self._FirstClassProbability = FirstClassProbability

    @property
    def SecondClassProbability(self):
        return self._SecondClassProbability

    @SecondClassProbability.setter
    def SecondClassProbability(self, SecondClassProbability):
        self._SecondClassProbability = SecondClassProbability

    @property
    def ThirdClassName(self):
        return self._ThirdClassName

    @ThirdClassName.setter
    def ThirdClassName(self, ThirdClassName):
        self._ThirdClassName = ThirdClassName

    @property
    def ThirdClassProbability(self):
        return self._ThirdClassProbability

    @ThirdClassProbability.setter
    def ThirdClassProbability(self, ThirdClassProbability):
        self._ThirdClassProbability = ThirdClassProbability

    @property
    def FourthClassName(self):
        return self._FourthClassName

    @FourthClassName.setter
    def FourthClassName(self, FourthClassName):
        self._FourthClassName = FourthClassName

    @property
    def FourthClassProbability(self):
        return self._FourthClassProbability

    @FourthClassProbability.setter
    def FourthClassProbability(self, FourthClassProbability):
        self._FourthClassProbability = FourthClassProbability

    @property
    def FifthClassName(self):
        return self._FifthClassName

    @FifthClassName.setter
    def FifthClassName(self, FifthClassName):
        self._FifthClassName = FifthClassName

    @property
    def FifthClassProbability(self):
        return self._FifthClassProbability

    @FifthClassProbability.setter
    def FifthClassProbability(self, FifthClassProbability):
        self._FifthClassProbability = FifthClassProbability


    def _deserialize(self, params):
        self._FirstClassName = params.get("FirstClassName")
        self._SecondClassName = params.get("SecondClassName")
        self._FirstClassProbability = params.get("FirstClassProbability")
        self._SecondClassProbability = params.get("SecondClassProbability")
        self._ThirdClassName = params.get("ThirdClassName")
        self._ThirdClassProbability = params.get("ThirdClassProbability")
        self._FourthClassName = params.get("FourthClassName")
        self._FourthClassProbability = params.get("FourthClassProbability")
        self._FifthClassName = params.get("FifthClassName")
        self._FifthClassProbability = params.get("FifthClassProbability")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyContentRequest(AbstractModel):
    """ClassifyContent请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Title: 待分类的文章的标题（仅支持UTF-8格式，不超过100字符）。
        :type Title: str
        :param _Content: 待分类文章的内容, 每个元素对应一个段落。（仅支持UTF-8格式，文章内容长度总和不超过2000字符）
        :type Content: list of str
        """
        self._Title = None
        self._Content = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassifyContentResponse(AbstractModel):
    """ClassifyContent返回参数结构体

    """

    def __init__(self):
        r"""
        :param _FirstClassification: 一级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
        :type FirstClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param _SecondClassification: 二级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
        :type SecondClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param _ThirdClassification: 三级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
注意：此字段可能返回 null，表示取不到有效值。
        :type ThirdClassification: :class:`tencentcloud.nlp.v20190408.models.Category`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FirstClassification = None
        self._SecondClassification = None
        self._ThirdClassification = None
        self._RequestId = None

    @property
    def FirstClassification(self):
        return self._FirstClassification

    @FirstClassification.setter
    def FirstClassification(self, FirstClassification):
        self._FirstClassification = FirstClassification

    @property
    def SecondClassification(self):
        return self._SecondClassification

    @SecondClassification.setter
    def SecondClassification(self, SecondClassification):
        self._SecondClassification = SecondClassification

    @property
    def ThirdClassification(self):
        return self._ThirdClassification

    @ThirdClassification.setter
    def ThirdClassification(self, ThirdClassification):
        self._ThirdClassification = ThirdClassification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("FirstClassification") is not None:
            self._FirstClassification = Category()
            self._FirstClassification._deserialize(params.get("FirstClassification"))
        if params.get("SecondClassification") is not None:
            self._SecondClassification = Category()
            self._SecondClassification._deserialize(params.get("SecondClassification"))
        if params.get("ThirdClassification") is not None:
            self._ThirdClassification = Category()
            self._ThirdClassification._deserialize(params.get("ThirdClassification"))
        self._RequestId = params.get("RequestId")


class ComposeCoupletRequest(AbstractModel):
    """ComposeCouplet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 生成对联的关键词。长度需>=2，当长度>2时，自动截取前两个字作为关键字。内容需为常用汉字（不含有数字、英文、韩语、日语、符号等等其他）。
        :type Text: str
        :param _TargetType: 返回的文本结果为繁体还是简体。0：简体；1：繁体。默认为0。
        :type TargetType: int
        """
        self._Text = None
        self._TargetType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposeCoupletResponse(AbstractModel):
    """ComposeCouplet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopScroll: 横批。
        :type TopScroll: str
        :param _Content: 上联与下联。
        :type Content: list of str
        :param _RandomCause: 当对联随机生成时，展示随机生成原因。
        :type RandomCause: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopScroll = None
        self._Content = None
        self._RandomCause = None
        self._RequestId = None

    @property
    def TopScroll(self):
        return self._TopScroll

    @TopScroll.setter
    def TopScroll(self, TopScroll):
        self._TopScroll = TopScroll

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RandomCause(self):
        return self._RandomCause

    @RandomCause.setter
    def RandomCause(self, RandomCause):
        self._RandomCause = RandomCause

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopScroll = params.get("TopScroll")
        self._Content = params.get("Content")
        self._RandomCause = params.get("RandomCause")
        self._RequestId = params.get("RequestId")


class ComposePoetryRequest(AbstractModel):
    """ComposePoetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 生成诗词的关键词。
        :type Text: str
        :param _PoetryType: 生成诗词的类型。0：藏头或藏身；1：藏头；2：藏身。默认为0。
        :type PoetryType: int
        :param _Genre: 诗的体裁。0：五言律诗或七言律诗；5：五言律诗；7：七言律诗。默认为0。
        :type Genre: int
        """
        self._Text = None
        self._PoetryType = None
        self._Genre = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def PoetryType(self):
        return self._PoetryType

    @PoetryType.setter
    def PoetryType(self, PoetryType):
        self._PoetryType = PoetryType

    @property
    def Genre(self):
        return self._Genre

    @Genre.setter
    def Genre(self, Genre):
        self._Genre = Genre


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._PoetryType = params.get("PoetryType")
        self._Genre = params.get("Genre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ComposePoetryResponse(AbstractModel):
    """ComposePoetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Title: 诗题，即输入的生成诗词的关键词。
        :type Title: str
        :param _Content: 诗的内容。
        :type Content: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Title = None
        self._Content = None
        self._RequestId = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class CompoundParticiple(AbstractModel):
    """复合粒度分词和词性标注的结果。

    """

    def __init__(self):
        r"""
        :param _Word: 基础词。
        :type Word: str
        :param _BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param _Length: 基础词的长度。
        :type Length: int
        :param _Pos: 词性。
        :type Pos: str
        """
        self._Word = None
        self._BeginOffset = None
        self._Length = None
        self._Pos = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._Length = params.get("Length")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CorrectionItem(AbstractModel):
    """纠错结果列表

    """

    def __init__(self):
        r"""
        :param _Order: 纠错句子的序号。
        :type Order: int
        :param _BeginOffset: 错误的起始位置，从0开始。
        :type BeginOffset: int
        :param _Len: 错误内容长度。
        :type Len: int
        :param _Word: 错误内容。
        :type Word: str
        :param _CorrectWord: 纠错结果，当为删除类错误时，结果为null。
注意：此字段可能返回 null，表示取不到有效值。
        :type CorrectWord: list of str
        :param _CorrectionType: 纠错类型。0：替换；1：插入；2：删除。
        :type CorrectionType: int
        :param _Confidence: 纠错信息置信度。0：error；1：warning；error的置信度更高。（仅供参考）
        :type Confidence: int
        :param _DescriptionZh: 纠错信息中文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionZh: str
        :param _DescriptionEn: 纠错信息英文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type DescriptionEn: str
        """
        self._Order = None
        self._BeginOffset = None
        self._Len = None
        self._Word = None
        self._CorrectWord = None
        self._CorrectionType = None
        self._Confidence = None
        self._DescriptionZh = None
        self._DescriptionEn = None

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Len(self):
        return self._Len

    @Len.setter
    def Len(self, Len):
        self._Len = Len

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def CorrectWord(self):
        return self._CorrectWord

    @CorrectWord.setter
    def CorrectWord(self, CorrectWord):
        self._CorrectWord = CorrectWord

    @property
    def CorrectionType(self):
        return self._CorrectionType

    @CorrectionType.setter
    def CorrectionType(self, CorrectionType):
        self._CorrectionType = CorrectionType

    @property
    def Confidence(self):
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def DescriptionZh(self):
        return self._DescriptionZh

    @DescriptionZh.setter
    def DescriptionZh(self, DescriptionZh):
        self._DescriptionZh = DescriptionZh

    @property
    def DescriptionEn(self):
        return self._DescriptionEn

    @DescriptionEn.setter
    def DescriptionEn(self, DescriptionEn):
        self._DescriptionEn = DescriptionEn


    def _deserialize(self, params):
        self._Order = params.get("Order")
        self._BeginOffset = params.get("BeginOffset")
        self._Len = params.get("Len")
        self._Word = params.get("Word")
        self._CorrectWord = params.get("CorrectWord")
        self._CorrectionType = params.get("CorrectionType")
        self._Confidence = params.get("Confidence")
        self._DescriptionZh = params.get("DescriptionZh")
        self._DescriptionEn = params.get("DescriptionEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDictRequest(AbstractModel):
    """CreateDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 自定义词库名称，不超过20字。
        :type Name: str
        :param _Description: 自定义词库描述，不超过100字。
        :type Description: str
        """
        self._Name = None
        self._Description = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDictResponse(AbstractModel):
    """CreateDict返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 创建的自定义词库ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type DictId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DictId = None
        self._RequestId = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        self._RequestId = params.get("RequestId")


class CreateWordItemsRequest(AbstractModel):
    """CreateWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 自定义词库ID。
        :type DictId: str
        :param _WordItems: 待添加的词条集合。
        :type WordItems: list of WordItem
        """
        self._DictId = None
        self._WordItems = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def WordItems(self):
        return self._WordItems

    @WordItems.setter
    def WordItems(self, WordItems):
        self._WordItems = WordItems


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        if params.get("WordItems") is not None:
            self._WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWordItemsResponse(AbstractModel):
    """CreateWordItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDictRequest(AbstractModel):
    """DeleteDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 要删除的自定义词库ID。
        :type DictId: str
        """
        self._DictId = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDictResponse(AbstractModel):
    """DeleteDict返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWordItemsRequest(AbstractModel):
    """DeleteWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 自定义词库ID。
        :type DictId: str
        :param _WordItems: 待删除的词条集合。
        :type WordItems: list of WordItem
        """
        self._DictId = None
        self._WordItems = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def WordItems(self):
        return self._WordItems

    @WordItems.setter
    def WordItems(self, WordItems):
        self._WordItems = WordItems


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        if params.get("WordItems") is not None:
            self._WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWordItemsResponse(AbstractModel):
    """DeleteWordItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DependencyParsingRequest(AbstractModel):
    """DependencyParsing请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DependencyParsingResponse(AbstractModel):
    """DependencyParsing返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DpTokens: 句法依存分析结果，其中句法依存关系的类型包括：
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
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DpTokens = None
        self._RequestId = None

    @property
    def DpTokens(self):
        return self._DpTokens

    @DpTokens.setter
    def DpTokens(self, DpTokens):
        self._DpTokens = DpTokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DpTokens") is not None:
            self._DpTokens = []
            for item in params.get("DpTokens"):
                obj = DpToken()
                obj._deserialize(item)
                self._DpTokens.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDictRequest(AbstractModel):
    """DescribeDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 自定义词库ID。
        :type DictId: str
        :param _Name: 自定义词库名称，模糊搜索。
        :type Name: str
        """
        self._DictId = None
        self._Name = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDictResponse(AbstractModel):
    """DescribeDict返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Dicts: 查询到的词库信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Dicts: list of DictInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Dicts = None
        self._RequestId = None

    @property
    def Dicts(self):
        return self._Dicts

    @Dicts.setter
    def Dicts(self, Dicts):
        self._Dicts = Dicts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Dicts") is not None:
            self._Dicts = []
            for item in params.get("Dicts"):
                obj = DictInfo()
                obj._deserialize(item)
                self._Dicts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDictsRequest(AbstractModel):
    """DescribeDicts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 每页数据量，范围为1~100，默认为10。
        :type Limit: int
        :param _Offset: 分页偏移量，从0开始，默认为0。
        :type Offset: int
        """
        self._Limit = None
        self._Offset = None

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDictsResponse(AbstractModel):
    """DescribeDicts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 记录总条数。
        :type TotalCount: int
        :param _Dicts: 自定义词库信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Dicts: list of DictInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Dicts = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Dicts(self):
        return self._Dicts

    @Dicts.setter
    def Dicts(self, Dicts):
        self._Dicts = Dicts

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Dicts") is not None:
            self._Dicts = []
            for item in params.get("Dicts"):
                obj = DictInfo()
                obj._deserialize(item)
                self._Dicts.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeWordItemsRequest(AbstractModel):
    """DescribeWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 自定义词库ID。
        :type DictId: str
        :param _Offset: 分页偏移量，从0开始，默认为0。
        :type Offset: int
        :param _Limit: 每页数据量，范围为1~100，默认为10。
        :type Limit: int
        :param _Text: 待检索的词条文本，支持模糊匹配。
        :type Text: str
        """
        self._DictId = None
        self._Offset = None
        self._Limit = None
        self._Text = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWordItemsResponse(AbstractModel):
    """DescribeWordItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 词条记录总条数。
        :type TotalCount: int
        :param _WordItems: 词条信息列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type WordItems: list of WordItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._WordItems = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def WordItems(self):
        return self._WordItems

    @WordItems.setter
    def WordItems(self, WordItems):
        self._WordItems = WordItems

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("WordItems") is not None:
            self._WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordItems.append(obj)
        self._RequestId = params.get("RequestId")


class DictInfo(AbstractModel):
    """自定义词库信息

    """

    def __init__(self):
        r"""
        :param _Name: 自定义词库名称。
        :type Name: str
        :param _Id: 自定义词库ID。
        :type Id: str
        :param _Description: 自定义词库描述信息。
        :type Description: str
        :param _UpdateTime: 自定义词库修改时间，形式为:yyyy-mm-dd hh:mm:ss。
        :type UpdateTime: str
        :param _CreateTime: 自定义词库创建时间，形式为:yyyy-mm-dd hh:mm:ss。
        :type CreateTime: str
        """
        self._Name = None
        self._Id = None
        self._Description = None
        self._UpdateTime = None
        self._CreateTime = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Id = params.get("Id")
        self._Description = params.get("Description")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DpToken(AbstractModel):
    """句法依存分析结果，包括基础词，基础词的序号，当前词父节点的序号，句法依存关系的类型

    """

    def __init__(self):
        r"""
        :param _Relation: 句法依存关系的类型
        :type Relation: str
        :param _HeadId: 当前词父节点的序号
        :type HeadId: int
        :param _Word: 基础词
        :type Word: str
        :param _Id: 基础词的序号
        :type Id: int
        """
        self._Relation = None
        self._HeadId = None
        self._Word = None
        self._Id = None

    @property
    def Relation(self):
        return self._Relation

    @Relation.setter
    def Relation(self, Relation):
        self._Relation = Relation

    @property
    def HeadId(self):
        return self._HeadId

    @HeadId.setter
    def HeadId(self, HeadId):
        self._HeadId = HeadId

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Relation = params.get("Relation")
        self._HeadId = params.get("HeadId")
        self._Word = params.get("Word")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Embellish(AbstractModel):
    """文本润色结果

    """

    def __init__(self):
        r"""
        :param _Text: 润色后的文本。
注意：此字段可能返回 null，表示取不到有效值。
        :type Text: str
        :param _EmbellishType: 润色类型。类型如下：
expansion：扩写
rewriting：改写
translation_m2a：从现代文改写为古文
translation_a2m：从古文改写为现代文


注意：此字段可能返回 null，表示取不到有效值。
        :type EmbellishType: str
        """
        self._Text = None
        self._EmbellishType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def EmbellishType(self):
        return self._EmbellishType

    @EmbellishType.setter
    def EmbellishType(self, EmbellishType):
        self._EmbellishType = EmbellishType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._EmbellishType = params.get("EmbellishType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Entity(AbstractModel):
    """实体识别结果。

    """

    def __init__(self):
        r"""
        :param _Word: 基础词。
        :type Word: str
        :param _BeginOffset: 基础词在NormalText中的起始位置。
        :type BeginOffset: int
        :param _Length: 基础词的长度。
        :type Length: int
        :param _Type: 实体类型的标准名字。
        :type Type: str
        :param _Name: 类型名字的自然语言表达。（中文或英文）
        :type Name: str
        """
        self._Word = None
        self._BeginOffset = None
        self._Length = None
        self._Type = None
        self._Name = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._BeginOffset = params.get("BeginOffset")
        self._Length = params.get("Length")
        self._Type = params.get("Type")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateSentenceSimilarityRequest(AbstractModel):
    """EvaluateSentenceSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SentencePairList: 待分析的句子对数组。句子对应不超过1对，仅支持中文文本，原句子与目标句子均应不超过64字符。
        :type SentencePairList: list of SentencePair
        """
        self._SentencePairList = None

    @property
    def SentencePairList(self):
        return self._SentencePairList

    @SentencePairList.setter
    def SentencePairList(self, SentencePairList):
        self._SentencePairList = SentencePairList


    def _deserialize(self, params):
        if params.get("SentencePairList") is not None:
            self._SentencePairList = []
            for item in params.get("SentencePairList"):
                obj = SentencePair()
                obj._deserialize(item)
                self._SentencePairList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateSentenceSimilarityResponse(AbstractModel):
    """EvaluateSentenceSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreList: 每个句子对的相似度分值。
        :type ScoreList: list of float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreList = None
        self._RequestId = None

    @property
    def ScoreList(self):
        return self._ScoreList

    @ScoreList.setter
    def ScoreList(self, ScoreList):
        self._ScoreList = ScoreList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScoreList = params.get("ScoreList")
        self._RequestId = params.get("RequestId")


class EvaluateWordSimilarityRequest(AbstractModel):
    """EvaluateWordSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SourceWord: 计算相似度的源词。（仅支持UTF-8格式，不超过10字符）

        :type SourceWord: str
        :param _TargetWord: 计算相似度的目标词。（仅支持UTF-8格式，不超过10字符）

        :type TargetWord: str
        """
        self._SourceWord = None
        self._TargetWord = None

    @property
    def SourceWord(self):
        return self._SourceWord

    @SourceWord.setter
    def SourceWord(self, SourceWord):
        self._SourceWord = SourceWord

    @property
    def TargetWord(self):
        return self._TargetWord

    @TargetWord.setter
    def TargetWord(self, TargetWord):
        self._TargetWord = TargetWord


    def _deserialize(self, params):
        self._SourceWord = params.get("SourceWord")
        self._TargetWord = params.get("TargetWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EvaluateWordSimilarityResponse(AbstractModel):
    """EvaluateWordSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Similarity: 词相似度分值。
        :type Similarity: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Similarity = None
        self._RequestId = None

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Similarity = params.get("Similarity")
        self._RequestId = params.get("RequestId")


class GenerateCoupletRequest(AbstractModel):
    """GenerateCouplet请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 生成对联的关键词。长度需>=2，当长度>2时，自动截取前两个字作为关键字。内容需为常用汉字（不含有数字、英文、韩语、日语、符号等等其他）。
        :type Text: str
        :param _TargetType: 返回的文本结果为繁体还是简体。0：简体；1：繁体。默认为0。
        :type TargetType: int
        """
        self._Text = None
        self._TargetType = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TargetType(self):
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._TargetType = params.get("TargetType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateCoupletResponse(AbstractModel):
    """GenerateCouplet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopScroll: 横批。
        :type TopScroll: str
        :param _Content: 上联与下联。
        :type Content: list of str
        :param _RandomCause: 当对联随机生成时，展示随机生成原因。
        :type RandomCause: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopScroll = None
        self._Content = None
        self._RandomCause = None
        self._RequestId = None

    @property
    def TopScroll(self):
        return self._TopScroll

    @TopScroll.setter
    def TopScroll(self, TopScroll):
        self._TopScroll = TopScroll

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RandomCause(self):
        return self._RandomCause

    @RandomCause.setter
    def RandomCause(self, RandomCause):
        self._RandomCause = RandomCause

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopScroll = params.get("TopScroll")
        self._Content = params.get("Content")
        self._RandomCause = params.get("RandomCause")
        self._RequestId = params.get("RequestId")


class GenerateKeywordSentenceRequest(AbstractModel):
    """GenerateKeywordSentence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _WordList: 生成句子的关键词，关键词个数需不超过4个，中文关键词长度应不超过10字符，英文关键词长度不超过3个单词。关键词中不可包含标点符号。
        :type WordList: list of str
        :param _Number: 返回生成句子的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param _Domain: 指定生成句子的领域，支持领域如下：
general：通用领域，支持中英文
academic：学术领域，仅支持英文
默认为general（通用领域）。
        :type Domain: str
        """
        self._WordList = None
        self._Number = None
        self._Domain = None

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._WordList = params.get("WordList")
        self._Number = params.get("Number")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GenerateKeywordSentenceResponse(AbstractModel):
    """GenerateKeywordSentence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _KeywordSentenceList: 生成的句子列表。
        :type KeywordSentenceList: list of KeywordSentence
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._KeywordSentenceList = None
        self._RequestId = None

    @property
    def KeywordSentenceList(self):
        return self._KeywordSentenceList

    @KeywordSentenceList.setter
    def KeywordSentenceList(self, KeywordSentenceList):
        self._KeywordSentenceList = KeywordSentenceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("KeywordSentenceList") is not None:
            self._KeywordSentenceList = []
            for item in params.get("KeywordSentenceList"):
                obj = KeywordSentence()
                obj._deserialize(item)
                self._KeywordSentenceList.append(obj)
        self._RequestId = params.get("RequestId")


class GeneratePoetryRequest(AbstractModel):
    """GeneratePoetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 生成诗词的关键词。
        :type Text: str
        :param _PoetryType: 生成诗词的类型。0：藏头或藏身；1：藏头；2：藏身。默认为0。
        :type PoetryType: int
        :param _Genre: 诗的体裁。0：五言律诗或七言律诗；5：五言律诗；7：七言律诗。默认为0。
        :type Genre: int
        """
        self._Text = None
        self._PoetryType = None
        self._Genre = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def PoetryType(self):
        return self._PoetryType

    @PoetryType.setter
    def PoetryType(self, PoetryType):
        self._PoetryType = PoetryType

    @property
    def Genre(self):
        return self._Genre

    @Genre.setter
    def Genre(self, Genre):
        self._Genre = Genre


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._PoetryType = params.get("PoetryType")
        self._Genre = params.get("Genre")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GeneratePoetryResponse(AbstractModel):
    """GeneratePoetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Title: 诗题，即输入的生成诗词的关键词。
        :type Title: str
        :param _Content: 诗的内容。
        :type Content: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Title = None
        self._Content = None
        self._RequestId = None

    @property
    def Title(self):
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Title = params.get("Title")
        self._Content = params.get("Content")
        self._RequestId = params.get("RequestId")


class Keyword(AbstractModel):
    """关键词提取结果

    """

    def __init__(self):
        r"""
        :param _Score: 权重
        :type Score: float
        :param _Word: 关键词
        :type Word: str
        """
        self._Score = None
        self._Word = None

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word


    def _deserialize(self, params):
        self._Score = params.get("Score")
        self._Word = params.get("Word")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordSentence(AbstractModel):
    """通过关键词生成的句子信息

    """

    def __init__(self):
        r"""
        :param _TargetText: 通过关键词生成的句子。
        :type TargetText: str
        """
        self._TargetText = None

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordsExtractionRequest(AbstractModel):
    """KeywordsExtraction请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待处理的文本（仅支持UTF-8格式，不超过10000字符）
        :type Text: str
        :param _Num: 指定关键词个数上限（默认值为5）
        :type Num: int
        """
        self._Text = None
        self._Num = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Num(self):
        return self._Num

    @Num.setter
    def Num(self, Num):
        self._Num = Num


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Num = params.get("Num")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeywordsExtractionResponse(AbstractModel):
    """KeywordsExtraction返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Keywords: 关键词提取结果
注意：此字段可能返回 null，表示取不到有效值。
        :type Keywords: list of Keyword
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Keywords = None
        self._RequestId = None

    @property
    def Keywords(self):
        return self._Keywords

    @Keywords.setter
    def Keywords(self, Keywords):
        self._Keywords = Keywords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Keywords") is not None:
            self._Keywords = []
            for item in params.get("Keywords"):
                obj = Keyword()
                obj._deserialize(item)
                self._Keywords.append(obj)
        self._RequestId = params.get("RequestId")


class LexicalAnalysisRequest(AbstractModel):
    """LexicalAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（仅支持UTF-8格式，不超过500字）
        :type Text: str
        :param _DictId: 指定要加载的自定义词库ID。
        :type DictId: str
        :param _Flag: 词法分析模式（默认取2值）：
1、高精度（混合粒度分词能力）；
2、高性能（单粒度分词能力）；
        :type Flag: int
        """
        self._Text = None
        self._DictId = None
        self._Flag = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._DictId = params.get("DictId")
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LexicalAnalysisResponse(AbstractModel):
    """LexicalAnalysis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NerTokens: 命名实体识别结果。取值范围：
<li>PER：表示人名，如刘德华、贝克汉姆</li>
<li>LOC：表示地名，如北京、华山</li>
<li>ORG：表示机构团体名，如腾讯、最高人民法院、人大附中</li>
<li>PRODUCTION：表示产品名，如QQ、微信、iPhone</li>
注意：此字段可能返回 null，表示取不到有效值。
        :type NerTokens: list of NerToken
        :param _PosTokens: 分词&词性标注结果（词性表请参见附录）
        :type PosTokens: list of PosToken
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NerTokens = None
        self._PosTokens = None
        self._RequestId = None

    @property
    def NerTokens(self):
        return self._NerTokens

    @NerTokens.setter
    def NerTokens(self, NerTokens):
        self._NerTokens = NerTokens

    @property
    def PosTokens(self):
        return self._PosTokens

    @PosTokens.setter
    def PosTokens(self, PosTokens):
        self._PosTokens = PosTokens

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("NerTokens") is not None:
            self._NerTokens = []
            for item in params.get("NerTokens"):
                obj = NerToken()
                obj._deserialize(item)
                self._NerTokens.append(obj)
        if params.get("PosTokens") is not None:
            self._PosTokens = []
            for item in params.get("PosTokens"):
                obj = PosToken()
                obj._deserialize(item)
                self._PosTokens.append(obj)
        self._RequestId = params.get("RequestId")


class NerToken(AbstractModel):
    """命名实体识别结果

    """

    def __init__(self):
        r"""
        :param _Word: 基础词
        :type Word: str
        :param _Length: 长度
        :type Length: int
        :param _BeginOffset: 起始位置
        :type BeginOffset: int
        :param _Type: 命名实体类型
        :type Type: str
        """
        self._Word = None
        self._Length = None
        self._BeginOffset = None
        self._Type = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._Length = params.get("Length")
        self._BeginOffset = params.get("BeginOffset")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseWordsRequest(AbstractModel):
    """ParseWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（支持中英文文本，不超过500字符）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParseWordsResponse(AbstractModel):
    """ParseWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NormalText: 输入文本正则化的结果。（包括对英文文本中的开头和实体进行大写等）
        :type NormalText: str
        :param _BasicParticiples: 基础粒度分词和词性标注的结果。（请参见附录[词性表](https://cloud.tencent.com/document/product/271/36460)）
        :type BasicParticiples: list of BasicParticiple
        :param _CompoundParticiples: 复合粒度分词和词性标注的结果。（请参见附录[词性表](https://cloud.tencent.com/document/product/271/36460)）
        :type CompoundParticiples: list of CompoundParticiple
        :param _Entities: 实体识别结果。（请参见附录[实体类型数据](https://cloud.tencent.com/document/product/271/90592)）

        :type Entities: list of Entity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NormalText = None
        self._BasicParticiples = None
        self._CompoundParticiples = None
        self._Entities = None
        self._RequestId = None

    @property
    def NormalText(self):
        return self._NormalText

    @NormalText.setter
    def NormalText(self, NormalText):
        self._NormalText = NormalText

    @property
    def BasicParticiples(self):
        return self._BasicParticiples

    @BasicParticiples.setter
    def BasicParticiples(self, BasicParticiples):
        self._BasicParticiples = BasicParticiples

    @property
    def CompoundParticiples(self):
        return self._CompoundParticiples

    @CompoundParticiples.setter
    def CompoundParticiples(self, CompoundParticiples):
        self._CompoundParticiples = CompoundParticiples

    @property
    def Entities(self):
        return self._Entities

    @Entities.setter
    def Entities(self, Entities):
        self._Entities = Entities

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NormalText = params.get("NormalText")
        if params.get("BasicParticiples") is not None:
            self._BasicParticiples = []
            for item in params.get("BasicParticiples"):
                obj = BasicParticiple()
                obj._deserialize(item)
                self._BasicParticiples.append(obj)
        if params.get("CompoundParticiples") is not None:
            self._CompoundParticiples = []
            for item in params.get("CompoundParticiples"):
                obj = CompoundParticiple()
                obj._deserialize(item)
                self._CompoundParticiples.append(obj)
        if params.get("Entities") is not None:
            self._Entities = []
            for item in params.get("Entities"):
                obj = Entity()
                obj._deserialize(item)
                self._Entities.append(obj)
        self._RequestId = params.get("RequestId")


class PosToken(AbstractModel):
    """分词&词性标注结果

    """

    def __init__(self):
        r"""
        :param _Word: 基础词
        :type Word: str
        :param _Length: 长度
        :type Length: int
        :param _BeginOffset: 起始位置
        :type BeginOffset: int
        :param _Pos: 词性
        :type Pos: str
        """
        self._Word = None
        self._Length = None
        self._BeginOffset = None
        self._Pos = None

    @property
    def Word(self):
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def Length(self):
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def BeginOffset(self):
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Word = params.get("Word")
        self._Length = params.get("Length")
        self._BeginOffset = params.get("BeginOffset")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveSimilarWordsRequest(AbstractModel):
    """RetrieveSimilarWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 输入的词语。（仅支持UTF-8格式，不超过10字符）
        :type Text: str
        :param _Number: 召回的相似词个数，取值范围为1-20。
        :type Number: int
        """
        self._Text = None
        self._Number = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Number = params.get("Number")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RetrieveSimilarWordsResponse(AbstractModel):
    """RetrieveSimilarWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WordList: 召回的相似词数组。
        :type WordList: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WordList = None
        self._RequestId = None

    @property
    def WordList(self):
        return self._WordList

    @WordList.setter
    def WordList(self, WordList):
        self._WordList = WordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._WordList = params.get("WordList")
        self._RequestId = params.get("RequestId")


class SearchResult(AbstractModel):
    """词条搜索的结果，主要描述该词条是否存在以及相关的词性。

    """

    def __init__(self):
        r"""
        :param _Text: 被搜索的词条文本。
        :type Text: str
        :param _IsExist: 0表示词条不存在，1表示存在。
        :type IsExist: int
        :param _MatchText: 匹配到的词条文本。
        :type MatchText: str
        :param _Pos: 词条的词性。
        :type Pos: str
        """
        self._Text = None
        self._IsExist = None
        self._MatchText = None
        self._Pos = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def IsExist(self):
        return self._IsExist

    @IsExist.setter
    def IsExist(self, IsExist):
        self._IsExist = IsExist

    @property
    def MatchText(self):
        return self._MatchText

    @MatchText.setter
    def MatchText(self, MatchText):
        self._MatchText = MatchText

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._IsExist = params.get("IsExist")
        self._MatchText = params.get("MatchText")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchWordItemsRequest(AbstractModel):
    """SearchWordItems请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 自定义词库ID。
        :type DictId: str
        :param _WordItems: 待检索的词条集合。
        :type WordItems: list of WordItem
        """
        self._DictId = None
        self._WordItems = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def WordItems(self):
        return self._WordItems

    @WordItems.setter
    def WordItems(self, WordItems):
        self._WordItems = WordItems


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        if params.get("WordItems") is not None:
            self._WordItems = []
            for item in params.get("WordItems"):
                obj = WordItem()
                obj._deserialize(item)
                self._WordItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchWordItemsResponse(AbstractModel):
    """SearchWordItems返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 词条检索结果集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type Results: list of SearchResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = SearchResult()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class SentenceCorrectionRequest(AbstractModel):
    """SentenceCorrection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TextList: 待纠错的句子列表。可以以数组方式在一次请求中填写多个待纠错的句子。文本统一使用utf-8格式编码，每个中文句子的长度不超过150字符，每个英文句子的长度不超过100个单词，且数组长度需小于30，即句子总数需少于30句。
        :type TextList: list of str
        """
        self._TextList = None

    @property
    def TextList(self):
        return self._TextList

    @TextList.setter
    def TextList(self, TextList):
        self._TextList = TextList


    def _deserialize(self, params):
        self._TextList = params.get("TextList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceCorrectionResponse(AbstractModel):
    """SentenceCorrection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorrectionList: 纠错结果列表。
（注意仅展示错误句子的纠错结果，若句子无错则不展示，若全部待纠错句子都被认为无错，则可能返回数组为空）
        :type CorrectionList: list of CorrectionItem
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorrectionList = None
        self._RequestId = None

    @property
    def CorrectionList(self):
        return self._CorrectionList

    @CorrectionList.setter
    def CorrectionList(self, CorrectionList):
        self._CorrectionList = CorrectionList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CorrectionList") is not None:
            self._CorrectionList = []
            for item in params.get("CorrectionList"):
                obj = CorrectionItem()
                obj._deserialize(item)
                self._CorrectionList.append(obj)
        self._RequestId = params.get("RequestId")


class SentenceEmbeddingRequest(AbstractModel):
    """SentenceEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 输入的文本（仅支持UTF-8格式，不超过500字）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentenceEmbeddingResponse(AbstractModel):
    """SentenceEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Vector: 句向量数组
        :type Vector: list of float
        :param _Dimension: 句向量的维度
        :type Dimension: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Vector = None
        self._Dimension = None
        self._RequestId = None

    @property
    def Vector(self):
        return self._Vector

    @Vector.setter
    def Vector(self, Vector):
        self._Vector = Vector

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Vector = params.get("Vector")
        self._Dimension = params.get("Dimension")
        self._RequestId = params.get("RequestId")


class SentencePair(AbstractModel):
    """待分析的句子对

    """

    def __init__(self):
        r"""
        :param _SourceText: 需要与目标句子计算相似度的源句子。（仅支持UTF-8格式，不超过500字符）
        :type SourceText: str
        :param _TargetText: 目标句子。（仅支持UTF-8格式，不超过500字符）

        :type TargetText: str
        """
        self._SourceText = None
        self._TargetText = None

    @property
    def SourceText(self):
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._SourceText = params.get("SourceText")
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentAnalysisRequest(AbstractModel):
    """SentimentAnalysis请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
        :type Text: str
        :param _Flag: 待分析文本所属的类型，仅当输入参数Mode取值为2class时有效（默认取4值）：
1、商品评论类
2、社交类
3、美食酒店类
4、通用领域类
        :type Flag: int
        :param _Mode: 情感分类模式选项，可取2class或3class（默认值为2class）
1、2class：返回正负面二分类情感结果
2、3class：返回正负面及中性三分类情感结果
        :type Mode: str
        """
        self._Text = None
        self._Flag = None
        self._Mode = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag

    @property
    def Mode(self):
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Flag = params.get("Flag")
        self._Mode = params.get("Mode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SentimentAnalysisResponse(AbstractModel):
    """SentimentAnalysis返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Positive: 正面情感概率
        :type Positive: float
        :param _Neutral: 中性情感概率，当输入参数Mode取值为3class时有效，否则值为空
注意：此字段可能返回 null，表示取不到有效值。
        :type Neutral: float
        :param _Negative: 负面情感概率
        :type Negative: float
        :param _Sentiment: 情感分类结果：
1、positive，表示正面情感
2、negative，表示负面情感
3、neutral，表示中性、无情感
        :type Sentiment: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Positive = None
        self._Neutral = None
        self._Negative = None
        self._Sentiment = None
        self._RequestId = None

    @property
    def Positive(self):
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Neutral(self):
        return self._Neutral

    @Neutral.setter
    def Neutral(self, Neutral):
        self._Neutral = Neutral

    @property
    def Negative(self):
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative

    @property
    def Sentiment(self):
        return self._Sentiment

    @Sentiment.setter
    def Sentiment(self, Sentiment):
        self._Sentiment = Sentiment

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Positive = params.get("Positive")
        self._Neutral = params.get("Neutral")
        self._Negative = params.get("Negative")
        self._Sentiment = params.get("Sentiment")
        self._RequestId = params.get("RequestId")


class SimilarWordsRequest(AbstractModel):
    """SimilarWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 输入的词语（仅支持UTF-8格式，不超过20字）
        :type Text: str
        :param _WordNumber: 相似词个数；取值范围：1-200，默认为10；
        :type WordNumber: int
        """
        self._Text = None
        self._WordNumber = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def WordNumber(self):
        return self._WordNumber

    @WordNumber.setter
    def WordNumber(self, WordNumber):
        self._WordNumber = WordNumber


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._WordNumber = params.get("WordNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimilarWordsResponse(AbstractModel):
    """SimilarWords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SimilarWords: 相似词数组
        :type SimilarWords: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SimilarWords = None
        self._RequestId = None

    @property
    def SimilarWords(self):
        return self._SimilarWords

    @SimilarWords.setter
    def SimilarWords(self, SimilarWords):
        self._SimilarWords = SimilarWords

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SimilarWords = params.get("SimilarWords")
        self._RequestId = params.get("RequestId")


class Similarity(AbstractModel):
    """文本相似度

    """

    def __init__(self):
        r"""
        :param _Text: 目标文本句子
        :type Text: str
        :param _Score: 相似度分数
        :type Score: float
        """
        self._Text = None
        self._Score = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Score(self):
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Score = params.get("Score")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextClassificationRequest(AbstractModel):
    """TextClassification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分类的文本（仅支持UTF-8格式，不超过10000字）
        :type Text: str
        :param _Flag: 领域分类体系（默认取1值）：
1、通用领域，二分类
2、新闻领域，五分类。类别数据不一定全部返回，详情见类目映射表（注意：目前五分类已下线不可用）
        :type Flag: int
        """
        self._Text = None
        self._Flag = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def Flag(self):
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextClassificationResponse(AbstractModel):
    """TextClassification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Classes: 文本分类结果（文本分类映射表请参见附录）
        :type Classes: list of ClassificationResult
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Classes = None
        self._RequestId = None

    @property
    def Classes(self):
        return self._Classes

    @Classes.setter
    def Classes(self, Classes):
        self._Classes = Classes

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Classes") is not None:
            self._Classes = []
            for item in params.get("Classes"):
                obj = ClassificationResult()
                obj._deserialize(item)
                self._Classes.append(obj)
        self._RequestId = params.get("RequestId")


class TextCorrectionProRequest(AbstractModel):
    """TextCorrectionPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待纠错的文本（仅支持UTF-8格式，不超过128字符）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextCorrectionProResponse(AbstractModel):
    """TextCorrectionPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CCITokens: 纠错详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CCITokens: list of CCIToken
        :param _ResultText: 纠错后的文本
        :type ResultText: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CCITokens = None
        self._ResultText = None
        self._RequestId = None

    @property
    def CCITokens(self):
        return self._CCITokens

    @CCITokens.setter
    def CCITokens(self, CCITokens):
        self._CCITokens = CCITokens

    @property
    def ResultText(self):
        return self._ResultText

    @ResultText.setter
    def ResultText(self, ResultText):
        self._ResultText = ResultText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CCITokens") is not None:
            self._CCITokens = []
            for item in params.get("CCITokens"):
                obj = CCIToken()
                obj._deserialize(item)
                self._CCITokens.append(obj)
        self._ResultText = params.get("ResultText")
        self._RequestId = params.get("RequestId")


class TextCorrectionRequest(AbstractModel):
    """TextCorrection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待纠错的文本（仅支持UTF-8格式，不超过2000字符）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextCorrectionResponse(AbstractModel):
    """TextCorrection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CCITokens: 纠错详情
注意：此字段可能返回 null，表示取不到有效值。
        :type CCITokens: list of CCIToken
        :param _ResultText: 纠错后的文本
        :type ResultText: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CCITokens = None
        self._ResultText = None
        self._RequestId = None

    @property
    def CCITokens(self):
        return self._CCITokens

    @CCITokens.setter
    def CCITokens(self, CCITokens):
        self._CCITokens = CCITokens

    @property
    def ResultText(self):
        return self._ResultText

    @ResultText.setter
    def ResultText(self, ResultText):
        self._ResultText = ResultText

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CCITokens") is not None:
            self._CCITokens = []
            for item in params.get("CCITokens"):
                obj = CCIToken()
                obj._deserialize(item)
                self._CCITokens.append(obj)
        self._ResultText = params.get("ResultText")
        self._RequestId = params.get("RequestId")


class TextEmbellishRequest(AbstractModel):
    """TextEmbellish请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待润色的文本。中文文本长度需<=50字符；英文文本长度需<=30个单词。
        :type Text: str
        :param _SourceLang: 待润色文本的语言类型，支持语言如下：
zh：中文
en：英文
        :type SourceLang: str
        :param _Number: 返回润色结果的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param _Style: 控制润色类型，类型如下：
both：同时返回改写和扩写
expansion：扩写
rewriting：改写
m2a：从现代文改写为古文
a2m：从古文改写为现代文
默认为both。
        :type Style: str
        """
        self._Text = None
        self._SourceLang = None
        self._Number = None
        self._Style = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SourceLang(self):
        return self._SourceLang

    @SourceLang.setter
    def SourceLang(self, SourceLang):
        self._SourceLang = SourceLang

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SourceLang = params.get("SourceLang")
        self._Number = params.get("Number")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextEmbellishResponse(AbstractModel):
    """TextEmbellish返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EmbellishList: 润色结果列表。
        :type EmbellishList: list of Embellish
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EmbellishList = None
        self._RequestId = None

    @property
    def EmbellishList(self):
        return self._EmbellishList

    @EmbellishList.setter
    def EmbellishList(self, EmbellishList):
        self._EmbellishList = EmbellishList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EmbellishList") is not None:
            self._EmbellishList = []
            for item in params.get("EmbellishList"):
                obj = Embellish()
                obj._deserialize(item)
                self._EmbellishList.append(obj)
        self._RequestId = params.get("RequestId")


class TextSimilarityProRequest(AbstractModel):
    """TextSimilarityPro请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcText: 需要与目标句子计算相似度的源句子（仅支持UTF-8格式，不超过128字符）
        :type SrcText: str
        :param _TargetText: 目标句子（仅支持UTF-8格式，不超过128字符）
        :type TargetText: list of str
        """
        self._SrcText = None
        self._TargetText = None

    @property
    def SrcText(self):
        return self._SrcText

    @SrcText.setter
    def SrcText(self, SrcText):
        self._SrcText = SrcText

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._SrcText = params.get("SrcText")
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextSimilarityProResponse(AbstractModel):
    """TextSimilarityPro返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Similarity: 每个目标句子与源句子的相似度分值，按照分值降序排列
        :type Similarity: list of Similarity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Similarity = None
        self._RequestId = None

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Similarity") is not None:
            self._Similarity = []
            for item in params.get("Similarity"):
                obj = Similarity()
                obj._deserialize(item)
                self._Similarity.append(obj)
        self._RequestId = params.get("RequestId")


class TextSimilarityRequest(AbstractModel):
    """TextSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcText: 需要与目标句子计算相似度的源句子（仅支持UTF-8格式，不超过500字符）
        :type SrcText: str
        :param _TargetText: 目标句子（以句子数量为单位消耗资源包）
        :type TargetText: list of str
        """
        self._SrcText = None
        self._TargetText = None

    @property
    def SrcText(self):
        return self._SrcText

    @SrcText.setter
    def SrcText(self, SrcText):
        self._SrcText = SrcText

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText


    def _deserialize(self, params):
        self._SrcText = params.get("SrcText")
        self._TargetText = params.get("TargetText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextSimilarityResponse(AbstractModel):
    """TextSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Similarity: 每个目标句子与源句子的相似度分值，按照分值降序排列
        :type Similarity: list of Similarity
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Similarity = None
        self._RequestId = None

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Similarity") is not None:
            self._Similarity = []
            for item in params.get("Similarity"):
                obj = Similarity()
                obj._deserialize(item)
                self._Similarity.append(obj)
        self._RequestId = params.get("RequestId")


class TextWritingRequest(AbstractModel):
    """TextWriting请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待续写的句子，文本统一使用utf-8格式编码，长度不超过200字符。
        :type Text: str
        :param _SourceLang: 待续写文本的语言类型，支持语言如下：
zh：中文
en：英文
        :type SourceLang: str
        :param _Number: 返回续写结果的个数。数量需>=1且<=5。
（注意实际结果可能小于指定个数）
        :type Number: int
        :param _Domain: 指定续写领域，支持领域如下：
general：通用领域，支持中英文补全
academic：学术领域，仅支持英文补全
默认为general（通用领域）。
        :type Domain: str
        :param _Style: 指定续写风格，支持风格如下：
science_fiction：科幻
military_history：军事
xuanhuan_wuxia：武侠
urban_officialdom：职场
默认为xuanhuan_wuxia（武侠）。
        :type Style: str
        """
        self._Text = None
        self._SourceLang = None
        self._Number = None
        self._Domain = None
        self._Style = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def SourceLang(self):
        return self._SourceLang

    @SourceLang.setter
    def SourceLang(self, SourceLang):
        self._SourceLang = SourceLang

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Style(self):
        return self._Style

    @Style.setter
    def Style(self, Style):
        self._Style = Style


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._SourceLang = params.get("SourceLang")
        self._Number = params.get("Number")
        self._Domain = params.get("Domain")
        self._Style = params.get("Style")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TextWritingResponse(AbstractModel):
    """TextWriting返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WritingList: 续写结果列表。
        :type WritingList: list of Writing
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WritingList = None
        self._RequestId = None

    @property
    def WritingList(self):
        return self._WritingList

    @WritingList.setter
    def WritingList(self, WritingList):
        self._WritingList = WritingList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WritingList") is not None:
            self._WritingList = []
            for item in params.get("WritingList"):
                obj = Writing()
                obj._deserialize(item)
                self._WritingList.append(obj)
        self._RequestId = params.get("RequestId")


class UpdateDictRequest(AbstractModel):
    """UpdateDict请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DictId: 自定义词库ID。
        :type DictId: str
        :param _Description: 词库描述，不超过100字。
        :type Description: str
        :param _Name: 词库名称，不超过20字。
        :type Name: str
        """
        self._DictId = None
        self._Description = None
        self._Name = None

    @property
    def DictId(self):
        return self._DictId

    @DictId.setter
    def DictId(self, DictId):
        self._DictId = DictId

    @property
    def Description(self):
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._DictId = params.get("DictId")
        self._Description = params.get("Description")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDictResponse(AbstractModel):
    """UpdateDict返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class WordEmbeddingRequest(AbstractModel):
    """WordEmbedding请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 输入的词语（仅支持UTF-8格式，不超过20字）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text


    def _deserialize(self, params):
        self._Text = params.get("Text")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordEmbeddingResponse(AbstractModel):
    """WordEmbedding返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Vector: 词向量数组
        :type Vector: list of float
        :param _Dimension: 词向量的维度
        :type Dimension: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Vector = None
        self._Dimension = None
        self._RequestId = None

    @property
    def Vector(self):
        return self._Vector

    @Vector.setter
    def Vector(self, Vector):
        self._Vector = Vector

    @property
    def Dimension(self):
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Vector = params.get("Vector")
        self._Dimension = params.get("Dimension")
        self._RequestId = params.get("RequestId")


class WordItem(AbstractModel):
    """词条信息。

    """

    def __init__(self):
        r"""
        :param _Text: 词条文本内容。
        :type Text: str
        :param _CreateTime: 词条创建时间。
        :type CreateTime: str
        :param _Pos: 词条的词性。
        :type Pos: str
        """
        self._Text = None
        self._CreateTime = None
        self._Pos = None

    @property
    def Text(self):
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Pos(self):
        return self._Pos

    @Pos.setter
    def Pos(self, Pos):
        self._Pos = Pos


    def _deserialize(self, params):
        self._Text = params.get("Text")
        self._CreateTime = params.get("CreateTime")
        self._Pos = params.get("Pos")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordSimilarityRequest(AbstractModel):
    """WordSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SrcWord: 计算相似度的源词（仅支持UTF-8格式，不超过20字）
        :type SrcWord: str
        :param _TargetWord: 计算相似度的目标词（仅支持UTF-8格式，不超过20字）
        :type TargetWord: str
        """
        self._SrcWord = None
        self._TargetWord = None

    @property
    def SrcWord(self):
        return self._SrcWord

    @SrcWord.setter
    def SrcWord(self, SrcWord):
        self._SrcWord = SrcWord

    @property
    def TargetWord(self):
        return self._TargetWord

    @TargetWord.setter
    def TargetWord(self, TargetWord):
        self._TargetWord = TargetWord


    def _deserialize(self, params):
        self._SrcWord = params.get("SrcWord")
        self._TargetWord = params.get("TargetWord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WordSimilarityResponse(AbstractModel):
    """WordSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Similarity: 两个词语的相似度
        :type Similarity: float
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Similarity = None
        self._RequestId = None

    @property
    def Similarity(self):
        return self._Similarity

    @Similarity.setter
    def Similarity(self, Similarity):
        self._Similarity = Similarity

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Similarity = params.get("Similarity")
        self._RequestId = params.get("RequestId")


class Writing(AbstractModel):
    """文本续写结果

    """

    def __init__(self):
        r"""
        :param _TargetText: 续写的文本。
        :type TargetText: str
        :param _PrefixText: 续写的前缀。
        :type PrefixText: str
        """
        self._TargetText = None
        self._PrefixText = None

    @property
    def TargetText(self):
        return self._TargetText

    @TargetText.setter
    def TargetText(self, TargetText):
        self._TargetText = TargetText

    @property
    def PrefixText(self):
        return self._PrefixText

    @PrefixText.setter
    def PrefixText(self, PrefixText):
        self._PrefixText = PrefixText


    def _deserialize(self, params):
        self._TargetText = params.get("TargetText")
        self._PrefixText = params.get("PrefixText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        