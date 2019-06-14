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
        :param Length: 指定摘要的长度（默认值为200）
注：为保证摘要的可读性，最终生成的摘要长度并不会严格遵循这个值，会有略微的浮动
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


class ContentApprovalRequest(AbstractModel):
    """ContentApproval请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待审核的文本（仅支持UTF-8格式，不超过2000字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class ContentApprovalResponse(AbstractModel):
    """ContentApproval返回参数结构体

    """

    def __init__(self):
        """
        :param EvilFlag: 文本是否恶意：
0、正常；
1、恶意；
2、可疑送审
        :type EvilFlag: int
        :param EvilKeywords: 恶意关键词组
        :type EvilKeywords: list of str
        :param EvilType: 文本恶意类型：
0、正常；
1、政治；
2、色情；
3、辱骂/低俗；
4、暴恐/毒品；
5、广告/灌水；
6、迷信/邪教；
7、其他违法（如跨站追杀/恶意竞争等）；
8、综合
        :type EvilType: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.EvilFlag = None
        self.EvilKeywords = None
        self.EvilType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EvilFlag = params.get("EvilFlag")
        self.EvilKeywords = params.get("EvilKeywords")
        self.EvilType = params.get("EvilType")
        self.RequestId = params.get("RequestId")


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
        :param DpTokens: 句法依存分析结果
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
        :param Text: 待处理的文本（仅支持UTF-8格式，不超过2000字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


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
        :param Flag: 词法分析模式（默认取1值）：
1、高精度；
2、高性能；
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
        :param NerTokens: 命名实体识别结果
        :type NerTokens: list of NerToken
        :param PosTokens: 分词&词性标注结果
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


class SensitiveWordsRecognitionRequest(AbstractModel):
    """SensitiveWordsRecognition请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待识别的文本（仅支持UTF-8格式，不超过2000字）
        :type Text: str
        """
        self.Text = None


    def _deserialize(self, params):
        self.Text = params.get("Text")


class SensitiveWordsRecognitionResponse(AbstractModel):
    """SensitiveWordsRecognition返回参数结构体

    """

    def __init__(self):
        """
        :param SensitiveWords: 敏感词数组
        :type SensitiveWords: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SensitiveWords = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SensitiveWords = params.get("SensitiveWords")
        self.RequestId = params.get("RequestId")


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
        :param Flag: 文本所属类型（默认取4值）：
1、电商
2、APP
3、美食
4、酒店和其他
        :type Flag: int
        """
        self.Text = None
        self.Flag = None


    def _deserialize(self, params):
        self.Text = params.get("Text")
        self.Flag = params.get("Flag")


class SentimentAnalysisResponse(AbstractModel):
    """SentimentAnalysis返回参数结构体

    """

    def __init__(self):
        """
        :param Negative: 负面情感概率
        :type Negative: float
        :param Positive: 正面情感概率
        :type Positive: float
        :param Sentiment: 情感属性
        :type Sentiment: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Negative = None
        self.Positive = None
        self.Sentiment = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Negative = params.get("Negative")
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


class TextClassificationRequest(AbstractModel):
    """TextClassification请求参数结构体

    """

    def __init__(self):
        """
        :param Text: 待分类的文本（仅支持UTF-8格式，不超过2000字）
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
        :param Classes: 文本分类结果
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
        :param Text: 待纠错的文本（仅支持UTF-8格式，不超过200字）
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