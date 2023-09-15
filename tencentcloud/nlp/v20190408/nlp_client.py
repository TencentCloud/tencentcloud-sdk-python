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


    def GenerateKeywordSentence(self, request):
        """根据提供的关键词，生成简洁明了的关键句子，便于用户快速获取核心观点。

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