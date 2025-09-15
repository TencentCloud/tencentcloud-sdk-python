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


class AnalyzeSentimentRequest(AbstractModel):
    r"""AnalyzeSentiment请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（仅支持UTF-8格式，不超过200字）。
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        r"""待分析的文本（仅支持UTF-8格式，不超过200字）。
        :rtype: str
        """
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
    r"""AnalyzeSentiment返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Positive = None
        self._Neutral = None
        self._Negative = None
        self._Sentiment = None
        self._RequestId = None

    @property
    def Positive(self):
        r"""正面情感概率。
        :rtype: float
        """
        return self._Positive

    @Positive.setter
    def Positive(self, Positive):
        self._Positive = Positive

    @property
    def Neutral(self):
        r"""中性情感概率。
        :rtype: float
        """
        return self._Neutral

    @Neutral.setter
    def Neutral(self, Neutral):
        self._Neutral = Neutral

    @property
    def Negative(self):
        r"""负面情感概率。
        :rtype: float
        """
        return self._Negative

    @Negative.setter
    def Negative(self, Negative):
        self._Negative = Negative

    @property
    def Sentiment(self):
        r"""情感分类结果：
positive：正面情感
negative：负面情感
neutral：中性、无情感
        :rtype: str
        """
        return self._Sentiment

    @Sentiment.setter
    def Sentiment(self, Sentiment):
        self._Sentiment = Sentiment

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class BasicParticiple(AbstractModel):
    r"""基础粒度分词和词性标注的结果

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
        r"""基础词。
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        r"""基础词在NormalText中的起始位置。
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        r"""基础词的长度。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Pos(self):
        r"""词性。
        :rtype: str
        """
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
        


class Category(AbstractModel):
    r"""分类详细信息

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
        r"""分类id。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Label(self):
        r"""分类英文名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Label

    @Label.setter
    def Label(self, Label):
        self._Label = Label

    @property
    def Name(self):
        r"""分类中文名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Score(self):
        r"""分类置信度。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
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
        


class ClassifyContentRequest(AbstractModel):
    r"""ClassifyContent请求参数结构体

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
        r"""待分类的文章的标题（仅支持UTF-8格式，不超过100字符）。
        :rtype: str
        """
        return self._Title

    @Title.setter
    def Title(self, Title):
        self._Title = Title

    @property
    def Content(self):
        r"""待分类文章的内容, 每个元素对应一个段落。（仅支持UTF-8格式，文章内容长度总和不超过2000字符）
        :rtype: list of str
        """
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
    r"""ClassifyContent返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._FirstClassification = None
        self._SecondClassification = None
        self._ThirdClassification = None
        self._RequestId = None

    @property
    def FirstClassification(self):
        r"""一级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
        :rtype: :class:`tencentcloud.nlp.v20190408.models.Category`
        """
        return self._FirstClassification

    @FirstClassification.setter
    def FirstClassification(self, FirstClassification):
        self._FirstClassification = FirstClassification

    @property
    def SecondClassification(self):
        r"""二级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
        :rtype: :class:`tencentcloud.nlp.v20190408.models.Category`
        """
        return self._SecondClassification

    @SecondClassification.setter
    def SecondClassification(self, SecondClassification):
        self._SecondClassification = SecondClassification

    @property
    def ThirdClassification(self):
        r"""三级分类。（请参见附录[三级分类体系表](https://cloud.tencent.com/document/product/271/94286)）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.nlp.v20190408.models.Category`
        """
        return self._ThirdClassification

    @ThirdClassification.setter
    def ThirdClassification(self, ThirdClassification):
        self._ThirdClassification = ThirdClassification

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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
    r"""ComposeCouplet请求参数结构体

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
        r"""生成对联的关键词。长度需>=2，当长度>2时，自动截取前两个字作为关键字。内容需为常用汉字（不含有数字、英文、韩语、日语、符号等等其他）。
        :rtype: str
        """
        return self._Text

    @Text.setter
    def Text(self, Text):
        self._Text = Text

    @property
    def TargetType(self):
        r"""返回的文本结果为繁体还是简体。0：简体；1：繁体。默认为0。
        :rtype: int
        """
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
    r"""ComposeCouplet返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopScroll: 横批。
        :type TopScroll: str
        :param _Content: 上联与下联。
        :type Content: list of str
        :param _RandomCause: 当对联随机生成时，展示随机生成原因。
        :type RandomCause: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopScroll = None
        self._Content = None
        self._RandomCause = None
        self._RequestId = None

    @property
    def TopScroll(self):
        r"""横批。
        :rtype: str
        """
        return self._TopScroll

    @TopScroll.setter
    def TopScroll(self, TopScroll):
        self._TopScroll = TopScroll

    @property
    def Content(self):
        r"""上联与下联。
        :rtype: list of str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def RandomCause(self):
        r"""当对联随机生成时，展示随机生成原因。
        :rtype: str
        """
        return self._RandomCause

    @RandomCause.setter
    def RandomCause(self, RandomCause):
        self._RandomCause = RandomCause

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopScroll = params.get("TopScroll")
        self._Content = params.get("Content")
        self._RandomCause = params.get("RandomCause")
        self._RequestId = params.get("RequestId")


class CompoundParticiple(AbstractModel):
    r"""复合粒度分词和词性标注的结果。

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
        r"""基础词。
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        r"""基础词在NormalText中的起始位置。
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        r"""基础词的长度。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Pos(self):
        r"""词性。
        :rtype: str
        """
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
    r"""纠错结果列表

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
        r"""纠错句子的序号。
        :rtype: int
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def BeginOffset(self):
        r"""错误的起始位置，从0开始。
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Len(self):
        r"""错误内容长度。
        :rtype: int
        """
        return self._Len

    @Len.setter
    def Len(self, Len):
        self._Len = Len

    @property
    def Word(self):
        r"""错误内容。
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def CorrectWord(self):
        r"""纠错结果，当为删除类错误时，结果为null。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CorrectWord

    @CorrectWord.setter
    def CorrectWord(self, CorrectWord):
        self._CorrectWord = CorrectWord

    @property
    def CorrectionType(self):
        r"""纠错类型。0：替换；1：插入；2：删除。
        :rtype: int
        """
        return self._CorrectionType

    @CorrectionType.setter
    def CorrectionType(self, CorrectionType):
        self._CorrectionType = CorrectionType

    @property
    def Confidence(self):
        r"""纠错信息置信度。0：error；1：warning；error的置信度更高。（仅供参考）
        :rtype: int
        """
        return self._Confidence

    @Confidence.setter
    def Confidence(self, Confidence):
        self._Confidence = Confidence

    @property
    def DescriptionZh(self):
        r"""纠错信息中文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DescriptionZh

    @DescriptionZh.setter
    def DescriptionZh(self, DescriptionZh):
        self._DescriptionZh = DescriptionZh

    @property
    def DescriptionEn(self):
        r"""纠错信息英文描述。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class Entity(AbstractModel):
    r"""实体识别结果。

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
        r"""基础词。
        :rtype: str
        """
        return self._Word

    @Word.setter
    def Word(self, Word):
        self._Word = Word

    @property
    def BeginOffset(self):
        r"""基础词在NormalText中的起始位置。
        :rtype: int
        """
        return self._BeginOffset

    @BeginOffset.setter
    def BeginOffset(self, BeginOffset):
        self._BeginOffset = BeginOffset

    @property
    def Length(self):
        r"""基础词的长度。
        :rtype: int
        """
        return self._Length

    @Length.setter
    def Length(self, Length):
        self._Length = Length

    @property
    def Type(self):
        r"""实体类型的标准名字。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Name(self):
        r"""类型名字的自然语言表达。（中文或英文）
        :rtype: str
        """
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
    r"""EvaluateSentenceSimilarity请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SentencePairList: 待分析的句子对数组。句子对应不超过1对，仅支持中文文本，原句子与目标句子均应不超过500字符。
        :type SentencePairList: list of SentencePair
        """
        self._SentencePairList = None

    @property
    def SentencePairList(self):
        r"""待分析的句子对数组。句子对应不超过1对，仅支持中文文本，原句子与目标句子均应不超过500字符。
        :rtype: list of SentencePair
        """
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
    r"""EvaluateSentenceSimilarity返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ScoreList: 每个句子对的相似度分值。
        :type ScoreList: list of float
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ScoreList = None
        self._RequestId = None

    @property
    def ScoreList(self):
        r"""每个句子对的相似度分值。
        :rtype: list of float
        """
        return self._ScoreList

    @ScoreList.setter
    def ScoreList(self, ScoreList):
        self._ScoreList = ScoreList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ScoreList = params.get("ScoreList")
        self._RequestId = params.get("RequestId")


class ParseWordsRequest(AbstractModel):
    r"""ParseWords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Text: 待分析的文本（支持中英文文本，不超过500字符）
        :type Text: str
        """
        self._Text = None

    @property
    def Text(self):
        r"""待分析的文本（支持中英文文本，不超过500字符）
        :rtype: str
        """
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
    r"""ParseWords返回参数结构体

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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NormalText = None
        self._BasicParticiples = None
        self._CompoundParticiples = None
        self._Entities = None
        self._RequestId = None

    @property
    def NormalText(self):
        r"""输入文本正则化的结果。（包括对英文文本中的开头和实体进行大写等）
        :rtype: str
        """
        return self._NormalText

    @NormalText.setter
    def NormalText(self, NormalText):
        self._NormalText = NormalText

    @property
    def BasicParticiples(self):
        r"""基础粒度分词和词性标注的结果。（请参见附录[词性表](https://cloud.tencent.com/document/product/271/36460)）
        :rtype: list of BasicParticiple
        """
        return self._BasicParticiples

    @BasicParticiples.setter
    def BasicParticiples(self, BasicParticiples):
        self._BasicParticiples = BasicParticiples

    @property
    def CompoundParticiples(self):
        r"""复合粒度分词和词性标注的结果。（请参见附录[词性表](https://cloud.tencent.com/document/product/271/36460)）
        :rtype: list of CompoundParticiple
        """
        return self._CompoundParticiples

    @CompoundParticiples.setter
    def CompoundParticiples(self, CompoundParticiples):
        self._CompoundParticiples = CompoundParticiples

    @property
    def Entities(self):
        r"""实体识别结果。（请参见附录[实体类型数据](https://cloud.tencent.com/document/product/271/90592)）

        :rtype: list of Entity
        """
        return self._Entities

    @Entities.setter
    def Entities(self, Entities):
        self._Entities = Entities

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class SentenceCorrectionRequest(AbstractModel):
    r"""SentenceCorrection请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TextList: 待纠错的句子列表。可以以数组方式在一次请求中填写多个待纠错的句子。文本统一使用utf-8格式编码，每个中文句子的长度不超过150字符，每个英文句子的长度不超过100个单词，且数组长度需小于30，即句子总数需少于30句。
        :type TextList: list of str
        """
        self._TextList = None

    @property
    def TextList(self):
        r"""待纠错的句子列表。可以以数组方式在一次请求中填写多个待纠错的句子。文本统一使用utf-8格式编码，每个中文句子的长度不超过150字符，每个英文句子的长度不超过100个单词，且数组长度需小于30，即句子总数需少于30句。
        :rtype: list of str
        """
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
    r"""SentenceCorrection返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CorrectionList: 纠错结果列表。
（注意仅展示错误句子的纠错结果，若句子无错则不展示，若全部待纠错句子都被认为无错，则可能返回数组为空）
        :type CorrectionList: list of CorrectionItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CorrectionList = None
        self._RequestId = None

    @property
    def CorrectionList(self):
        r"""纠错结果列表。
（注意仅展示错误句子的纠错结果，若句子无错则不展示，若全部待纠错句子都被认为无错，则可能返回数组为空）
        :rtype: list of CorrectionItem
        """
        return self._CorrectionList

    @CorrectionList.setter
    def CorrectionList(self, CorrectionList):
        self._CorrectionList = CorrectionList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
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


class SentencePair(AbstractModel):
    r"""待分析的句子对

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
        r"""需要与目标句子计算相似度的源句子。（仅支持UTF-8格式，不超过500字符）
        :rtype: str
        """
        return self._SourceText

    @SourceText.setter
    def SourceText(self, SourceText):
        self._SourceText = SourceText

    @property
    def TargetText(self):
        r"""目标句子。（仅支持UTF-8格式，不超过500字符）

        :rtype: str
        """
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
        