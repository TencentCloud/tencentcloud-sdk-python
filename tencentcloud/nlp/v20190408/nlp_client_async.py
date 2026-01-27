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