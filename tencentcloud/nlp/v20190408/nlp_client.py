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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.nlp.v20190408 import models


class NlpClient(AbstractClient):
    _apiVersion = '2019-04-08'
    _endpoint = 'nlp.tencentcloudapi.com'
    _service = 'nlp'


    def AnalyzeSentiment(self, request):
        """情感分析接口能够对带有情感色彩的主观性文本进行分析、处理、归纳和推理，识别出用户的情感倾向，是积极、中性还是消极，并且提供各自概率。

        :param request: Request instance for AnalyzeSentiment.
        :type request: :class:`tencentcloud.nlp.v20190408.models.AnalyzeSentimentRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.AnalyzeSentimentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AnalyzeSentiment", params, headers=headers)
            response = json.loads(body)
            model = models.AnalyzeSentimentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AutoSummarization(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        利用人工智能算法，自动抽取文本中的关键信息并生成指定长度的文本摘要。可用于新闻标题生成、科技文献摘要生成和商品评论摘要等。

        :param request: Request instance for AutoSummarization.
        :type request: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.AutoSummarizationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AutoSummarization", params, headers=headers)
            response = json.loads(body)
            model = models.AutoSummarizationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatBot(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        闲聊服务基于腾讯领先的NLP引擎能力、数据运算能力和千亿级互联网语料数据的支持，同时集成了广泛的知识问答能力，可实现上百种自定义属性配置，以及儿童语言风格及说话方式，从而让聊天变得更睿智、简单和有趣。


        :param request: Request instance for ChatBot.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ChatBotRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ChatBotResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChatBot", params, headers=headers)
            response = json.loads(body)
            model = models.ChatBotResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClassifyContent(self, request):
        """文本分类接口能够对用户输入的文章进行自动分类，将其映射到具体的类目上，用户只需要提供待分类的文本，而无需关注具体实现。该功能定义了一套较为完备的[三级分类体系](https://cloud.tencent.com/document/product/271/94286)，积累了数百万的语料，经过多轮迭代优化打造了较先进的深度学习模型，以保证效果不断提升。

        :param request: Request instance for ClassifyContent.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ClassifyContentRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ClassifyContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClassifyContent", params, headers=headers)
            response = json.loads(body)
            model = models.ClassifyContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ComposeCouplet(self, request):
        """对联生成接口根据用户输入的命题关键词，智能生成一副完整的春联，包括上联、下联和横批。该接口利用先进的自然语言处理技术，确保生成的春联既符合传统对仗、对韵、对义的要求，又具有新意和创意，为用户提供独特的春节祝福。

        :param request: Request instance for ComposeCouplet.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ComposeCoupletRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ComposeCoupletResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ComposeCouplet", params, headers=headers)
            response = json.loads(body)
            model = models.ComposeCoupletResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ComposePoetry(self, request):
        """诗词生成接口利用现代的自然语言处理和深度学习技术，模仿了古代著名诗人的风格，为用户产生独特的诗词。用户只需输入的命题关键词，接口就能自动生成一首七言律诗或五言律诗。

        :param request: Request instance for ComposePoetry.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ComposePoetryRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ComposePoetryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ComposePoetry", params, headers=headers)
            response = json.loads(body)
            model = models.ComposePoetryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDict(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        根据指定的名称、描述创建自定义词库。

        :param request: Request instance for CreateDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.CreateDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.CreateDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDict", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDictResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWordItems(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        向指定的词库中添加词条。

        :param request: Request instance for CreateWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.CreateWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.CreateWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWordItems", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWordItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDict(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        删除自定义词库，会附带相应删除词库包含的所有词条。

        :param request: Request instance for DeleteDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DeleteDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DeleteDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDict", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDictResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteWordItems(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        用于删除自定义词库中的词条。

        :param request: Request instance for DeleteWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DeleteWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DeleteWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWordItems", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWordItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DependencyParsing(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        句法依存分析接口能够分析出句子中词与词之间的相互依存关系，并揭示其句法结构，包括主谓关系、动宾关系、核心关系等等，可用于提取句子主干、提取句子核心词等，在机器翻译、自动问答、知识抽取等领域都有很好的应用。

        :param request: Request instance for DependencyParsing.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DependencyParsingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DependencyParsing", params, headers=headers)
            response = json.loads(body)
            model = models.DependencyParsingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDict(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        根据id或名称查询自定义词库信息。

        :param request: Request instance for DescribeDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDict", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDictResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDicts(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        返回属于当前用户的所有自定义词库列表。

        :param request: Request instance for DescribeDicts.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeDictsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeDictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDicts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDictsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWordItems(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        依据自定义词库的ID，查询对应的词条信息。

        :param request: Request instance for DescribeWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.DescribeWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.DescribeWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWordItems", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWordItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EvaluateSentenceSimilarity(self, request):
        """通过计算句子间的语义相似性，帮助您快速找到文本中重复或相似的句子，用于文本聚类、相似问题检索等应用场景。

        :param request: Request instance for EvaluateSentenceSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.EvaluateSentenceSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.EvaluateSentenceSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EvaluateSentenceSimilarity", params, headers=headers)
            response = json.loads(body)
            model = models.EvaluateSentenceSimilarityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EvaluateWordSimilarity(self, request):
        """评估两个词语在语义空间的相似程度，为您的场景应用提供有力支持，如关键词过滤、热门话题挖掘等。（目前仅支持中文）

        :param request: Request instance for EvaluateWordSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.EvaluateWordSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.EvaluateWordSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EvaluateWordSimilarity", params, headers=headers)
            response = json.loads(body)
            model = models.EvaluateWordSimilarityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateCouplet(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        根据用户输入的命题关键词自动生成一副春联，包括上联、下联和横批。（如需开通请联系商务）

        :param request: Request instance for GenerateCouplet.
        :type request: :class:`tencentcloud.nlp.v20190408.models.GenerateCoupletRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.GenerateCoupletResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateCouplet", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateCoupletResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateKeywordSentence(self, request):
        """提取文本中的关键信息，生成简洁明了的关键句子，便于用户快速获取核心观点。

        :param request: Request instance for GenerateKeywordSentence.
        :type request: :class:`tencentcloud.nlp.v20190408.models.GenerateKeywordSentenceRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.GenerateKeywordSentenceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateKeywordSentence", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateKeywordSentenceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GeneratePoetry(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        根据用户输入的命题关键词自动生成一首七言律诗或五言律诗。（如需开通请联系商务）

        :param request: Request instance for GeneratePoetry.
        :type request: :class:`tencentcloud.nlp.v20190408.models.GeneratePoetryRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.GeneratePoetryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GeneratePoetry", params, headers=headers)
            response = json.loads(body)
            model = models.GeneratePoetryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KeywordsExtraction(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        基于关键词提取平台，通过对文本内容进行深度分析，提取出文本内容中的关键信息，为用户实现诸如新闻内容关键词自动提取、评论关键词提取等提供基础服务。

        :param request: Request instance for KeywordsExtraction.
        :type request: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.KeywordsExtractionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KeywordsExtraction", params, headers=headers)
            response = json.loads(body)
            model = models.KeywordsExtractionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LexicalAnalysis(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        词法分析接口提供以下三个功能：

        1、智能分词：将连续的自然语言文本，切分成具有语义合理性和完整性的词汇序列；

        2、词性标注：为每一个词附上对应的词性，例如名词、代词、形容词、动词等；

        3、命名实体识别：快速识别文本中的实体，例如人名、地名、机构名等。

        所有的功能均基于千亿级大规模互联网语料进行持续迭代更新，以保证效果不断提升，用户无需担心新词发现、歧义消除、调用性能等问题。目前词法分析已经在泛互联网、金融、政务等不同垂直领域提供业务支持，并取得良好的效果。

        :param request: Request instance for LexicalAnalysis.
        :type request: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.LexicalAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LexicalAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.LexicalAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseWords(self, request):
        """通过精准地对文本进行分词、词性标注、命名实体识别等功能，助您更好地理解文本内容，挖掘出潜在的价值信息。

        :param request: Request instance for ParseWords.
        :type request: :class:`tencentcloud.nlp.v20190408.models.ParseWordsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.ParseWordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseWords", params, headers=headers)
            response = json.loads(body)
            model = models.ParseWordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RetrieveSimilarWords(self, request):
        """基于大数据和深度学习技术，可以快速地找到与给定词语高度相似的其他词语，有助于提高搜索和推荐的准确性。（目前仅支持中文）

        :param request: Request instance for RetrieveSimilarWords.
        :type request: :class:`tencentcloud.nlp.v20190408.models.RetrieveSimilarWordsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.RetrieveSimilarWordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RetrieveSimilarWords", params, headers=headers)
            response = json.loads(body)
            model = models.RetrieveSimilarWordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SearchWordItems(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        查询指定自定义词库中的词条是否存在。

        :param request: Request instance for SearchWordItems.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SearchWordItemsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SearchWordItemsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SearchWordItems", params, headers=headers)
            response = json.loads(body)
            model = models.SearchWordItemsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SentenceCorrection(self, request):
        """智能识别并纠正句子中的语法、拼写、用词等错误，确保文本的准确性和可读性。

        :param request: Request instance for SentenceCorrection.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceCorrectionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceCorrectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SentenceCorrection", params, headers=headers)
            response = json.loads(body)
            model = models.SentenceCorrectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SentenceEmbedding(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        句向量接口能够将输入的句子映射成一个固定维度的向量，用来表示这个句子的语义特征，可用于文本聚类、文本相似度、文本分类等任务，能够显著提高它们的效果。

        该句向量服务由腾讯云自然语言处理团队联合微信智言团队共同打造，基于千亿级大规模互联网语料并采用Bert等领先的深度神经网络模型训练而成，在腾讯内部诸多业务的NLP任务上实测效果显著。

        :param request: Request instance for SentenceEmbedding.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentenceEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SentenceEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.SentenceEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SentimentAnalysis(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        情感分析接口能够对带有情感色彩的主观性文本进行分析、处理、归纳和推理，识别出用户的情感倾向，是积极还是消极，并且提供各自概率。

        该功能基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升。

        :param request: Request instance for SentimentAnalysis.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SentimentAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SentimentAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.SentimentAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SimilarWords(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        相似词接口能够基于同义词库及词向量技术，检索出与输入词语在语义上最相似的若干个词语，可广泛用于检索系统、问答系统、文档归档等场景。

        :param request: Request instance for SimilarWords.
        :type request: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.SimilarWordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SimilarWords", params, headers=headers)
            response = json.loads(body)
            model = models.SimilarWordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextClassification(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        文本分类接口能够对用户输入的文本进行自动分类，将其映射到具体的类目上，用户只需要提供待分类的文本，而无需关注具体实现。

        该功能基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升。

        目前已提供：

        - 通用领域分类体系，二级分类，包括14个分类类目，分别是汽车、科技、健康、体育、旅行、教育、职业、文化、房产、娱乐、女性、奥运、财经以及其他，适用于通用的场景。

        :param request: Request instance for TextClassification.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextClassificationRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextClassificationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextClassification", params, headers=headers)
            response = json.loads(body)
            model = models.TextClassificationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextCorrection(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        提供对中文文本的自动纠错功能，能够识别输入文本中的错误片段，定位错误并给出正确的文本结果；支持长度不超过2000字符（含标点符号）的长文本纠错。

        此功能是基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升，是搜索引擎、语音识别、内容审核等功能更好运行的基础之一。

        :param request: Request instance for TextCorrection.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextCorrection", params, headers=headers)
            response = json.loads(body)
            model = models.TextCorrectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextCorrectionPro(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        提供对中文文本的自动纠错功能，能够识别输入文本中的错误片段，定位错误并给出正确的文本结果；支持长度不超过128字符（含标点符号）的长文本纠错。

        此功能是基于千亿级大规模互联网语料和LSTM、BERT等深度神经网络模型进行训练，并持续迭代更新，以保证效果不断提升，是搜索引擎、语音识别、内容审核等功能更好运行的基础之一。

        :param request: Request instance for TextCorrectionPro.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionProRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextCorrectionProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextCorrectionPro", params, headers=headers)
            response = json.loads(body)
            model = models.TextCorrectionProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextEmbellish(self, request):
        """运用先进的自然语言处理技术，对原始文本进行优化润色，提升文本的通顺性、表达力和语言质量。

        :param request: Request instance for TextEmbellish.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextEmbellishRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextEmbellishResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextEmbellish", params, headers=headers)
            response = json.loads(body)
            model = models.TextEmbellishResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextSimilarity(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        句子相似度接口能够基于深度学习技术来计算一个源句子和多个目标句子的相似度，相似度分值越大的两个句子在语义上越相似。目前仅支持短文本（不超过500字符）的相似度计算，长文本的相似度计算也即将推出。

        鉴于句子相似度是一个应用非常广泛的功能，腾讯云自然语言处理团队在Bert等领先的深度神经网络模型的基础上，专门针对文本相似任务进行了优化，并持续迭代更新。基于句子相似度，可以轻松实现诸如文本去重、相似推荐等功能。

        接口将以句子数量为单位消耗资源包，而不是调用接口次数为单位。

        :param request: Request instance for TextSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextSimilarity", params, headers=headers)
            response = json.loads(body)
            model = models.TextSimilarityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextSimilarityPro(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        句子相似度接口能够基于深度学习技术来计算一个源句子和多个目标句子的相似度，相似度分值越大的两个句子在语义上越相似。目前仅支持短文本（不超过128字符）的相似度计算，长文本的相似度计算也即将推出。

        鉴于句子相似度是一个应用非常广泛的功能，腾讯云自然语言处理团队在Bert等领先的深度神经网络模型的基础上，专门针对文本相似任务进行了优化，并持续迭代更新。基于句子相似度，可以轻松实现诸如文本去重、相似推荐等功能。

        接口将以句子数量为单位消耗资源包，而不是调用接口次数为单位。

        :param request: Request instance for TextSimilarityPro.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityProRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextSimilarityProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextSimilarityPro", params, headers=headers)
            response = json.loads(body)
            model = models.TextSimilarityProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextWriting(self, request):
        """通过自动补全文本片段，帮助用户快速生成高质量、连贯的完整文本，提高创作效率。

        :param request: Request instance for TextWriting.
        :type request: :class:`tencentcloud.nlp.v20190408.models.TextWritingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.TextWritingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextWriting", params, headers=headers)
            response = json.loads(body)
            model = models.TextWritingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDict(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        修改自定义词库元数据信息，包括名称、描述。

        :param request: Request instance for UpdateDict.
        :type request: :class:`tencentcloud.nlp.v20190408.models.UpdateDictRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.UpdateDictResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDict", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDictResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def WordEmbedding(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        词向量接口能够将输入的词语映射成一个固定维度的词向量，用来表示这个词语的语义特征。词向量是很多自然语言处理技术的基础，能够显著提高它们的效果。

        该词向量服务由腾讯知文自然语言处理团队联合腾讯AI Lab共同打造。使用的词向量基于千亿级大规模互联网语料并采用AI Lab自研的DSG算法训练而成，开源的词向量包含800多万中文词汇，在覆盖率、新鲜度及准确性等三方面性能突出。

        :param request: Request instance for WordEmbedding.
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WordEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.WordEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def WordSimilarity(self, request):
        """因业务调整该接口将于北京时间2023年8月1日0点下线，届时该产品功能将无法正常使用，为了避免对您的业务造成影响，请您尽快做好相关业务调整。详见：https://cloud.tencent.com/document/product/271/90711

        词相似度接口能够基于词向量技术来计算两个输入词语的余弦相似度，相似度数值越大的两个词语在语义上越相似。

        :param request: Request instance for WordSimilarity.
        :type request: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityRequest`
        :rtype: :class:`tencentcloud.nlp.v20190408.models.WordSimilarityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WordSimilarity", params, headers=headers)
            response = json.loads(body)
            model = models.WordSimilarityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))