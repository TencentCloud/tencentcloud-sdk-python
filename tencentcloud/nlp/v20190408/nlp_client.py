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