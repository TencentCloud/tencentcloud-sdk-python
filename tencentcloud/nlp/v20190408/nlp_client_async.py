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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.nlp.v20190408 import models
from typing import Dict


class NlpClient(AbstractClient):
    _apiVersion = '2019-04-08'
    _endpoint = 'nlp.tencentcloudapi.com'
    _service = 'nlp'

    async def AnalyzeSentiment(
            self,
            request: models.AnalyzeSentimentRequest,
            opts: Dict = None,
    ) -> models.AnalyzeSentimentResponse:
        """
        情感分析接口能够对带有情感色彩的主观性文本进行分析、处理、归纳和推理，识别出用户的情感倾向，是积极、中性还是消极，并且提供各自概率。
        """
        
        kwargs = {}
        kwargs["action"] = "AnalyzeSentiment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AnalyzeSentimentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClassifyContent(
            self,
            request: models.ClassifyContentRequest,
            opts: Dict = None,
    ) -> models.ClassifyContentResponse:
        """
        NLP技术的句子相似度、相似词召回、文本分类、对联生成、诗词生成、词相似度、文本润色、句子生成和文本补全API接口将于2025年10月31日下线，届时将无法正常调用。为了避免对您的业务造成影响，请您尽快做好相关业务调整。如果您有NLP技术的产品需求，推荐您调用腾讯混元大模型（https://cloud.tencent.com/product/tclm）。

        文本分类接口能够对用户输入的文章进行自动分类，将其映射到具体的类目上，用户只需要提供待分类的文本，而无需关注具体实现。该功能定义了一套较为完备的[三级分类体系](https://cloud.tencent.com/document/product/271/94286)，积累了数百万的语料，经过多轮迭代优化打造了较先进的深度学习模型，以保证效果不断提升。
        """
        
        kwargs = {}
        kwargs["action"] = "ClassifyContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClassifyContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ComposeCouplet(
            self,
            request: models.ComposeCoupletRequest,
            opts: Dict = None,
    ) -> models.ComposeCoupletResponse:
        """
        NLP技术的句子相似度、相似词召回、文本分类、对联生成、诗词生成、词相似度、文本润色、句子生成和文本补全API接口将于2025年10月31日下线，届时将无法正常调用。为了避免对您的业务造成影响，请您尽快做好相关业务调整。如果您有NLP技术的产品需求，推荐您调用腾讯混元大模型（https://cloud.tencent.com/product/tclm）。

        对联生成接口根据用户输入的命题关键词，智能生成一副完整的春联，包括上联、下联和横批。该接口利用先进的自然语言处理技术，确保生成的春联既符合传统对仗、对韵、对义的要求，又具有新意和创意，为用户提供独特的春节祝福。
        """
        
        kwargs = {}
        kwargs["action"] = "ComposeCouplet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ComposeCoupletResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EvaluateSentenceSimilarity(
            self,
            request: models.EvaluateSentenceSimilarityRequest,
            opts: Dict = None,
    ) -> models.EvaluateSentenceSimilarityResponse:
        """
        NLP技术的句子相似度、相似词召回、文本分类、对联生成、诗词生成、词相似度、文本润色、句子生成和文本补全API接口将于2025年10月31日下线，届时将无法正常调用。为了避免对您的业务造成影响，请您尽快做好相关业务调整。如果您有NLP技术的产品需求，推荐您调用腾讯混元大模型（https://cloud.tencent.com/product/tclm）。

        通过计算句子间的语义相似性，帮助您快速找到文本中重复或相似的句子，用于文本聚类、相似问题检索等应用场景。
        """
        
        kwargs = {}
        kwargs["action"] = "EvaluateSentenceSimilarity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EvaluateSentenceSimilarityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseWords(
            self,
            request: models.ParseWordsRequest,
            opts: Dict = None,
    ) -> models.ParseWordsResponse:
        """
        通过精准地对文本进行分词、词性标注、命名实体识别等功能，助您更好地理解文本内容，挖掘出潜在的价值信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseWords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseWordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SentenceCorrection(
            self,
            request: models.SentenceCorrectionRequest,
            opts: Dict = None,
    ) -> models.SentenceCorrectionResponse:
        """
        智能识别并纠正句子中的语法、拼写、用词等错误，确保文本的准确性和可读性。
        """
        
        kwargs = {}
        kwargs["action"] = "SentenceCorrection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SentenceCorrectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)