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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.nlp.v20190408 import models


class NlpClient(AbstractClient):
    _apiVersion = '2019-04-08'
    _endpoint = 'nlp.tencentcloudapi.com'
    _service = 'nlp'


    def AnalyzeSentiment(self, request):
        r"""情感分析接口能够对带有情感色彩的主观性文本进行分析、处理、归纳和推理，识别出用户的情感倾向，是积极、中性还是消极，并且提供各自概率。

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
        r"""NLP技术的句子相似度、相似词召回、文本分类、对联生成、诗词生成、词相似度、文本润色、句子生成和文本补全API接口将于2025年10月31日下线，届时将无法正常调用。为了避免对您的业务造成影响，请您尽快做好相关业务调整。如果您有NLP技术的产品需求，推荐您调用腾讯混元大模型（https://cloud.tencent.com/product/tclm）。

        文本分类接口能够对用户输入的文章进行自动分类，将其映射到具体的类目上，用户只需要提供待分类的文本，而无需关注具体实现。该功能定义了一套较为完备的[三级分类体系](https://cloud.tencent.com/document/product/271/94286)，积累了数百万的语料，经过多轮迭代优化打造了较先进的深度学习模型，以保证效果不断提升。

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
        r"""NLP技术的句子相似度、相似词召回、文本分类、对联生成、诗词生成、词相似度、文本润色、句子生成和文本补全API接口将于2025年10月31日下线，届时将无法正常调用。为了避免对您的业务造成影响，请您尽快做好相关业务调整。如果您有NLP技术的产品需求，推荐您调用腾讯混元大模型（https://cloud.tencent.com/product/tclm）。

        对联生成接口根据用户输入的命题关键词，智能生成一副完整的春联，包括上联、下联和横批。该接口利用先进的自然语言处理技术，确保生成的春联既符合传统对仗、对韵、对义的要求，又具有新意和创意，为用户提供独特的春节祝福。

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


    def EvaluateSentenceSimilarity(self, request):
        r"""NLP技术的句子相似度、相似词召回、文本分类、对联生成、诗词生成、词相似度、文本润色、句子生成和文本补全API接口将于2025年10月31日下线，届时将无法正常调用。为了避免对您的业务造成影响，请您尽快做好相关业务调整。如果您有NLP技术的产品需求，推荐您调用腾讯混元大模型（https://cloud.tencent.com/product/tclm）。

        通过计算句子间的语义相似性，帮助您快速找到文本中重复或相似的句子，用于文本聚类、相似问题检索等应用场景。

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


    def ParseWords(self, request):
        r"""通过精准地对文本进行分词、词性标注、命名实体识别等功能，助您更好地理解文本内容，挖掘出潜在的价值信息。

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


    def SentenceCorrection(self, request):
        r"""智能识别并纠正句子中的语法、拼写、用词等错误，确保文本的准确性和可读性。

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