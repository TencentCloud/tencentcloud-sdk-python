# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AutoSummarizationRequest(AbstractModel):
    """AutoSummarization请求参数结构体

    """

    def __init__(self):
        """
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


class AutoSummarizationResponse(AbstractModel):
    """AutoSummarization返回参数结构体

    """

    def __init__(self):
        """
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


class CCIToken(AbstractModel):
    """文本纠错结果

    """

    def __init__(self):
        """
        :param BeginOffset: 错别字的起始位置，从0开始
        :type BeginOffset: int
        :param CorrectWord: 错别字纠错结果
        :type CorrectWord: str
        :param Word: 错别字内容
        :type Word: str
        """
        self.BeginOffset = None
        self.CorrectWord = None
        self.Word = None


    def _deserialize(self, params):
        self.BeginOffset = params.get("BeginOffset")
        self.CorrectWord = params.get("CorrectWord")
        self.Word = params.get("Word")


class ChatBotRequest(AbstractModel):
    """ChatBot请求参数结构体

    """

    def __init__(self):
        """
        :param Query: 用户请求的query
        :type Query: str
        :param Flag: 0: 通用闲聊, 1:儿童闲聊, 默认是通用闲聊
        :type Flag: int
        :param OpenId: 服务的id,  主要用于儿童闲聊接口，比如手Q的openid
        :type OpenId: str
        """
        self.Query = None
        self.Flag = None
        self.OpenId = None


    def _deserialize(self, params):
        self.Query = params.get("Query")
        self.Flag = params.get("Flag")
        self.OpenId = params.get("OpenId")


class ChatBotResponse(AbstractModel):
    """ChatBot返回参数结构体

    """

    def __init__(self):
        """
        :param Confidence: 对于当前输出回复的自信度
        :type Confidence: float
        :param Reply: 闲聊回复
        :type Reply: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Confidence = None
        self.Reply = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Confidence = params.get("Confidence")
        self.Reply = params.get("Reply")
        self.RequestId = params.get("RequestId")


class ClassificationResult(AbstractModel):
    """文本分类结果

    """

    def __init__(self):
        """
        :param FirstClassName: 一级分类名称
        :type FirstClassName: str
        :param FirstClassProbability: 一级分类概率
        :type FirstClassProbability: float
        :param SecondClassName: 二级分类名称
        :type SecondClassName: str
        :param SecondClassProbability: 二级分类概率
        :type SecondClassProbability: float
        """
        self.FirstClassName = None
        self.FirstClassProbability = None
        self.SecondClassName = None
        self.SecondClassProbability = None


    def _deserialize(self, params):
        self.FirstClassName = params.get("FirstClassName")
        self.FirstClassProbability = params.get("FirstClassProbability")
        self.SecondClassName = params.get("SecondClassName")
        self.SecondClassProbability = params.get("SecondClassProbability")


class DependencyParsingRequest(AbstractModel):
    """DependencyParsing请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过200字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


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


class DescribeEntityRequest(AbstractModel):
    """DescribeEntity请求参数结构体

    """

    def __init__(self):
        """
        :param EntityName: 实体名称
        :type EntityName: str
        """
        self.EntityName = None


    def _deserialize(self, params):
        self.EntityName = params.get("EntityName")


class DescribeEntityResponse(AbstractModel):
    """DescribeEntity返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体相关信息
        :type Content: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param LeftEntityName: 输入第一个实体
        :type LeftEntityName: str
        :param RightEntityName: 输入第二个实体
        :type RightEntityName: str
        """
        self.LeftEntityName = None
        self.RightEntityName = None


    def _deserialize(self, params):
        self.LeftEntityName = params.get("LeftEntityName")
        self.RightEntityName = params.get("RightEntityName")


class DescribeRelationResponse(AbstractModel):
    """DescribeRelation返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回查询实体间的关系
        :type Content: list of EntityRelationContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param TripleCondition: 三元组查询条件
        :type TripleCondition: str
        """
        self.TripleCondition = None


    def _deserialize(self, params):
        self.TripleCondition = params.get("TripleCondition")


class DescribeTripleResponse(AbstractModel):
    """DescribeTriple返回参数结构体

    """

    def __init__(self):
        """
        :param Content: 返回三元组信息
        :type Content: list of TripleContent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DpToken(AbstractModel):
    """句法依存分析结果，包括基础词，基础词的序号，当前词父节点的序号，句法依存关系的类型

    """

    def __init__(self):
        """
        :param HeadId: 当前词父节点的序号
        :type HeadId: int
        :param Id: 基础词的序号
        :type Id: int
        :param Relation: 句法依存关系的类型
        :type Relation: str
        :param Word: 基础词
        :type Word: str
        """
        self.HeadId = None
        self.Id = None
        self.Relation = None
        self.Word = None


    def _deserialize(self, params):
        self.HeadId = params.get("HeadId")
        self.Id = params.get("Id")
        self.Relation = params.get("Relation")
        self.Word = params.get("Word")


class EntityRelationContent(AbstractModel):
    """返回的实体关系查询结果详细内容

    """

    def __init__(self):
        """
        :param Object: 实体关系查询返回关系的object
        :type Object: list of EntityRelationObject
        :param Subject: 实体关系查询返回关系的subject
        :type Subject: list of EntityRelationSubject
        :param Relation: 实体关系查询返回的关系名称
        :type Relation: str
        """
        self.Object = None
        self.Subject = None
        self.Relation = None


    def _deserialize(self, params):
        if params.get("Object") is not None:
            self.Object = []
            for item in params.get("Object"):
                obj = EntityRelationObject()
                obj._deserialize(item)
                self.Object.append(obj)
        if params.get("Subject") is not None:
            self.Subject = []
            for item in params.get("Subject"):
                obj = EntityRelationSubject()
                obj._deserialize(item)
                self.Subject.append(obj)
        self.Relation = params.get("Relation")


class EntityRelationObject(AbstractModel):
    """实体关系查询返回的Object类型

    """

    def __init__(self):
        """
        :param Id: object对应id
        :type Id: list of str
        :param Name: object对应name
        :type Name: list of str
        :param Popular: object对应popular值
        :type Popular: list of int
        """
        self.Id = None
        self.Name = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Popular = params.get("Popular")


class EntityRelationSubject(AbstractModel):
    """实体关系查询返回Subject

    """

    def __init__(self):
        """
        :param Id: Subject对应id
        :type Id: list of str
        :param Name: Subject对应name
        :type Name: list of str
        :param Popular: Subject对应popular
        :type Popular: list of int
        """
        self.Id = None
        self.Name = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Popular = params.get("Popular")


class Keyword(AbstractModel):
    """关键词提取结果

    """

    def __init__(self):
        """
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


class KeywordsExtractionRequest(AbstractModel):
    """KeywordsExtraction请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待处理的文本（仅支持UTF-8格式，不超过10000字）
        :type Text: str
        :param Num: 指定关键词个数上限（默认值为5）
        :type Num: int
        """
        self.Text = None
        self.Num = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Num = params.get("Num")


class KeywordsExtractionResponse(AbstractModel):
    """KeywordsExtraction返回参数结构体

    """

    def __init__(self):
        """
        :param Keywords: 关键词提取结果
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
        """
        :param Text: 待分析的文本（仅支持UTF-8格式，不超过500字）
        :type Text: str
        :param Flag: 词法分析模式（默认取2值）：
1、高精度（混合粒度分词能力）；
2、高性能（单粒度分词能力）；
        :type Flag: int
        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")


class LexicalAnalysisResponse(AbstractModel):
    """LexicalAnalysis返回参数结构体

    """

    def __init__(self):
        """
        :param NerTokens: 命名实体识别结果。取值范围：
<li>PER：表示人名</li>
<li>LOC：表示地名</li>
<li>ORG：表示机构团体名</li>
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
        """
        :param BeginOffset: 起始位置
        :type BeginOffset: int
        :param Length: 长度
        :type Length: int
        :param Type: 命名实体类型
        :type Type: str
        :param Word: 基础词
        :type Word: str
        """
        self.BeginOffset = None
        self.Length = None
        self.Type = None
        self.Word = None


    def _deserialize(self, params):
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Type = params.get("Type")
        self.Word = params.get("Word")


class PosToken(AbstractModel):
    """分词&词性标注结果

    """

    def __init__(self):
        """
        :param BeginOffset: 起始位置
        :type BeginOffset: int
        :param Length: 长度
        :type Length: int
        :param Pos: 词性
        :type Pos: str
        :param Word: 基础词
        :type Word: str
        """
        self.BeginOffset = None
        self.Length = None
        self.Pos = None
        self.Word = None


    def _deserialize(self, params):
        self.BeginOffset = params.get("BeginOffset")
        self.Length = params.get("Length")
        self.Pos = params.get("Pos")
        self.Word = params.get("Word")


class SentenceEmbeddingRequest(AbstractModel):
    """SentenceEmbedding请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 输入的文本（仅支持UTF-8格式，不超过500字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class SentenceEmbeddingResponse(AbstractModel):
    """SentenceEmbedding返回参数结构体

    """

    def __init__(self):
        """
        :param Dimension: 句向量的维度
        :type Dimension: int
        :param Vector: 句向量数组
        :type Vector: list of float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Dimension = None
        self.Vector = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dimension = params.get("Dimension")
        self.Vector = params.get("Vector")
        self.RequestId = params.get("RequestId")


class SentenceSimilarityRequest(AbstractModel):
    """SentenceSimilarity请求参数结构体

    """

    def __init__(self):
        """
        :param SrcText: 计算相似度的源句子（仅支持UTF-8格式，不超过500字）
        :type SrcText: str
        :param TargetText: 计算相似度的目标句子（仅支持UTF-8格式，不超过500字）
        :type TargetText: str
        """
        self.SrcText = None
        self.TargetText = None


    def _deserialize(self, params):
        self.SrcText = params.get("SrcText")
        self.TargetText = params.get("TargetText")


class SentenceSimilarityResponse(AbstractModel):
    """SentenceSimilarity返回参数结构体

    """

    def __init__(self):
        """
        :param Similarity: 两个文本的相似度
        :type Similarity: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Similarity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Similarity = params.get("Similarity")
        self.RequestId = params.get("RequestId")


class SentimentAnalysisRequest(AbstractModel):
    """SentimentAnalysis请求参数结构体

    """

    def __init__(self):
        """
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


class SentimentAnalysisResponse(AbstractModel):
    """SentimentAnalysis返回参数结构体

    """

    def __init__(self):
        """
        :param Negative: 负面情感概率
        :type Negative: float
        :param Neutral: 中性情感概率，当输入参数Mode取值为3class时有效，否则值为空
        :type Neutral: float
        :param Positive: 正面情感概率
        :type Positive: float
        :param Sentiment: 情感分类结果：
1、positive，表示正面情感
2、negative，表示负面情感
3、neutral，表示中性、无情感
        :type Sentiment: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Negative = None
        self.Neutral = None
        self.Positive = None
        self.Sentiment = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Negative = params.get("Negative")
        self.Neutral = params.get("Neutral")
        self.Positive = params.get("Positive")
        self.Sentiment = params.get("Sentiment")
        self.RequestId = params.get("RequestId")


class SimilarWordsRequest(AbstractModel):
    """SimilarWords请求参数结构体

    """

    def __init__(self):
        """
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


class SimilarWordsResponse(AbstractModel):
    """SimilarWords返回参数结构体

    """

    def __init__(self):
        """
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
        """
        :param Score: 相似度分数
        :type Score: float
        :param Text: 目标文本句子
        :type Text: str
        """
        self.Score = None
        self.Text = None


    def _deserialize(self, params):
        self.Score = params.get("Score")
        self.Text = params.get("Text")


class TextClassificationRequest(AbstractModel):
    """TextClassification请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分类的文本（仅支持UTF-8格式，不超过10000字）
        :type Text: str
        :param Flag: 领域分类体系（默认取1值）：
1、通用领域
2、新闻领域
        :type Flag: int
        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")


class TextClassificationResponse(AbstractModel):
    """TextClassification返回参数结构体

    """

    def __init__(self):
        """
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


class TextCorrectionRequest(AbstractModel):
    """TextCorrection请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过2000字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class TextCorrectionResponse(AbstractModel):
    """TextCorrection返回参数结构体

    """

    def __init__(self):
        """
        :param CCITokens: 纠错详情
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


class TextSimilarityRequest(AbstractModel):
    """TextSimilarity请求参数结构体

    """

    def __init__(self):
        """
        :param SrcText: 需要与目标句子计算相似度的源句子（仅支持UTF-8格式，不超过500字）
        :type SrcText: str
        :param TargetText: 需要与源句子计算相似度的一个或多个目标句子（仅支持UTF-8格式，目标句子的数量不超过100个，每个句子不超过500字）
注意：每成功计算1个目标句子与源句子的相似度算1次调用
        :type TargetText: list of str
        """
        self.SrcText = None
        self.TargetText = None


    def _deserialize(self, params):
        self.SrcText = params.get("SrcText")
        self.TargetText = params.get("TargetText")


class TextSimilarityResponse(AbstractModel):
    """TextSimilarity返回参数结构体

    """

    def __init__(self):
        """
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


class TripleContent(AbstractModel):
    """三元组查询返回的元记录

    """

    def __init__(self):
        """
        :param Id: 实体id
        :type Id: str
        :param Name: 实体名称
        :type Name: str
        :param Order: 实体order
        :type Order: int
        :param Popular: 实体流行度
        :type Popular: int
        """
        self.Id = None
        self.Name = None
        self.Order = None
        self.Popular = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.Order = params.get("Order")
        self.Popular = params.get("Popular")


class WordEmbeddingRequest(AbstractModel):
    """WordEmbedding请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 输入的词语（仅支持UTF-8格式，不超过20字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class WordEmbeddingResponse(AbstractModel):
    """WordEmbedding返回参数结构体

    """

    def __init__(self):
        """
        :param Dimension: 词向量的维度
        :type Dimension: int
        :param Vector: 词向量数组
        :type Vector: list of float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Dimension = None
        self.Vector = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Dimension = params.get("Dimension")
        self.Vector = params.get("Vector")
        self.RequestId = params.get("RequestId")


class WordSimilarityRequest(AbstractModel):
    """WordSimilarity请求参数结构体

    """

    def __init__(self):
        """
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


class WordSimilarityResponse(AbstractModel):
    """WordSimilarity返回参数结构体

    """

    def __init__(self):
        """
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