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
from tencentcloud.es.v20250101 import models


class EsClient(AbstractClient):
    _apiVersion = '2025-01-01'
    _endpoint = 'es.tencentcloudapi.com'
    _service = 'es'


    def ChatCompletions(self, request):
        """本服务支持一系列高性能的大语言模型，包括DeepSeek以及腾讯自主研发的混元大模型，结合混合搜索等先进搜索技术，快速高效实现RAG，有效解决幻觉和知识更新问题。
        本接口有单账号调用上限控制，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。

        :param request: Request instance for ChatCompletions.
        :type request: :class:`tencentcloud.es.v20250101.models.ChatCompletionsRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ChatCompletionsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatCompletions", params, models.ChatCompletionsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChunkDocument(self, request):
        """实时文档切片

        :param request: Request instance for ChunkDocument.
        :type request: :class:`tencentcloud.es.v20250101.models.ChunkDocumentRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocumentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChunkDocument", params, headers=headers)
            response = json.loads(body)
            model = models.ChunkDocumentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChunkDocumentAsync(self, request):
        """文本切片是将长文本分割为短片段的技术，用于适配模型输入、提升处理效率或信息检索，平衡片段长度与语义连贯性，适用于NLP、数据分析等场景。
        本接口为异步接口，有单账号调用上限控制，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service) 。

        :param request: Request instance for ChunkDocumentAsync.
        :type request: :class:`tencentcloud.es.v20250101.models.ChunkDocumentAsyncRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ChunkDocumentAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ChunkDocumentAsync", params, headers=headers)
            response = json.loads(body)
            model = models.ChunkDocumentAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDocumentChunkResult(self, request):
        """获取文档切片结果

        :param request: Request instance for GetDocumentChunkResult.
        :type request: :class:`tencentcloud.es.v20250101.models.GetDocumentChunkResultRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetDocumentChunkResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDocumentChunkResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetDocumentChunkResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetDocumentParseResult(self, request):
        """本接口用于获取文档解析异步处理结果。

        :param request: Request instance for GetDocumentParseResult.
        :type request: :class:`tencentcloud.es.v20250101.models.GetDocumentParseResultRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetDocumentParseResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetDocumentParseResult", params, headers=headers)
            response = json.loads(body)
            model = models.GetDocumentParseResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTextEmbedding(self, request):
        """Embedding是一种将高维数据映射到低维空间的技术，通常用于将非结构化数据，如文本、图像或音频转化为向量表示，使其更容易输入机器模型进行处理，并且向量之间的距离可以反映对象之间的相似性。
        本接口有单账号调用上限控制，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。

        :param request: Request instance for GetTextEmbedding.
        :type request: :class:`tencentcloud.es.v20250101.models.GetTextEmbeddingRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.GetTextEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTextEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.GetTextEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseDocument(self, request):
        """本服务可将各类格式文档精准转换为标准格式，满足企业知识库建设、技术文档迁移、内容平台结构化存储等需求。
        本接口有单账号调用上限控制，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)。

        :param request: Request instance for ParseDocument.
        :type request: :class:`tencentcloud.es.v20250101.models.ParseDocumentRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocumentResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ParseDocument", params, models.ParseDocumentResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ParseDocumentAsync(self, request):
        """本服务可将各类格式文档精准转换为标准格式，满足企业知识库建设、技术文档迁移、内容平台结构化存储等需求。
        本接口为异步接口，有单账号调用上限控制，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。

        :param request: Request instance for ParseDocumentAsync.
        :type request: :class:`tencentcloud.es.v20250101.models.ParseDocumentAsyncRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.ParseDocumentAsyncResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ParseDocumentAsync", params, headers=headers)
            response = json.loads(body)
            model = models.ParseDocumentAsyncResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunRerank(self, request):
        """重排序

        :param request: Request instance for RunRerank.
        :type request: :class:`tencentcloud.es.v20250101.models.RunRerankRequest`
        :rtype: :class:`tencentcloud.es.v20250101.models.RunRerankResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunRerank", params, headers=headers)
            response = json.loads(body)
            model = models.RunRerankResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))