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
from tencentcloud.es.v20250101 import models
from typing import Dict


class EsClient(AbstractClient):
    _apiVersion = '2025-01-01'
    _endpoint = 'es.tencentcloudapi.com'
    _service = 'es'

    async def ChatCompletions(
            self,
            request: models.ChatCompletionsRequest,
            opts: Dict = None,
    ) -> models.ChatCompletionsResponse:
        """
        本服务支持一系列高性能的大语言模型，包括DeepSeek以及腾讯自主研发的混元大模型，结合混合搜索等先进搜索技术，快速高效实现RAG，有效解决幻觉和知识更新问题。
        本接口有模型维度调用上限控制，单个模型qps限制5，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。
        """
        
        kwargs = {}
        kwargs["action"] = "ChatCompletions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatCompletionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        kwargs["opts"]["Endpoint"] = "%s://es.ai.tencentcloudapi.com" % self.profile.httpProfile.scheme
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChunkDocument(
            self,
            request: models.ChunkDocumentRequest,
            opts: Dict = None,
    ) -> models.ChunkDocumentResponse:
        """
        文本切片是将长文本分割为短片段的技术，用于适配模型输入、提升处理效率或信息检索，平衡片段长度与语义连贯性，适用于NLP、数据分析等场景。
        本接口为分隔符规则切片接口，有单账号调用上限控制，如您有提高并发限制的需求请 [联系我们](https://cloud.tencent.com/act/event/Online_service)  。
        """
        
        kwargs = {}
        kwargs["action"] = "ChunkDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChunkDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChunkDocumentAsync(
            self,
            request: models.ChunkDocumentAsyncRequest,
            opts: Dict = None,
    ) -> models.ChunkDocumentAsyncResponse:
        """
        文本切片是将长文本分割为短片段的技术，用于适配模型输入、提升处理效率或信息检索，平衡片段长度与语义连贯性，适用于NLP、数据分析等场景。
        本接口为异步接口，有模型维度调用上限控制，单个模型qps限制5，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ChunkDocumentAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChunkDocumentAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDocumentChunkResult(
            self,
            request: models.GetDocumentChunkResultRequest,
            opts: Dict = None,
    ) -> models.GetDocumentChunkResultResponse:
        """
        获取文档切片结果
        """
        
        kwargs = {}
        kwargs["action"] = "GetDocumentChunkResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDocumentChunkResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDocumentParseResult(
            self,
            request: models.GetDocumentParseResultRequest,
            opts: Dict = None,
    ) -> models.GetDocumentParseResultResponse:
        """
        本接口用于获取文档解析异步处理结果。
        """
        
        kwargs = {}
        kwargs["action"] = "GetDocumentParseResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDocumentParseResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMultiModalEmbedding(
            self,
            request: models.GetMultiModalEmbeddingRequest,
            opts: Dict = None,
    ) -> models.GetMultiModalEmbeddingResponse:
        """
        Embedding是一种将高维数据映射到低维空间的技术，通常用于将非结构化数据，如文本、图像或音频转化为向量表示，使其更容易输入机器模型进行处理，并且向量之间的距离可以反映对象之间的相似性。
        本接口有模型维度调用上限控制，单个模型qps限制10，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。
        """
        
        kwargs = {}
        kwargs["action"] = "GetMultiModalEmbedding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMultiModalEmbeddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTextEmbedding(
            self,
            request: models.GetTextEmbeddingRequest,
            opts: Dict = None,
    ) -> models.GetTextEmbeddingResponse:
        """
        Embedding是一种将高维数据映射到低维空间的技术，通常用于将非结构化数据，如文本、图像或音频转化为向量表示，使其更容易输入机器模型进行处理，并且向量之间的距离可以反映对象之间的相似性。
        本接口有模型维度调用上限控制，单个模型qps限制20，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTextEmbedding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTextEmbeddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseDocument(
            self,
            request: models.ParseDocumentRequest,
            opts: Dict = None,
    ) -> models.ParseDocumentResponse:
        """
        本服务可将各类格式文档精准转换为标准格式，满足企业知识库建设、技术文档迁移、内容平台结构化存储等需求。
        本接口有模型维度调用上限控制，单个模型qps限制5，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseDocument"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseDocumentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        kwargs["opts"]["Endpoint"] = "%s://es.ai.tencentcloudapi.com" % self.profile.httpProfile.scheme
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseDocumentAsync(
            self,
            request: models.ParseDocumentAsyncRequest,
            opts: Dict = None,
    ) -> models.ParseDocumentAsyncResponse:
        """
        本服务可将各类格式文档精准转换为标准格式，满足企业知识库建设、技术文档迁移、内容平台结构化存储等需求。
        本接口为异步接口，有模型维度调用上限控制，单个模型qps限制5，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service) 。
        """
        
        kwargs = {}
        kwargs["action"] = "ParseDocumentAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseDocumentAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunRerank(
            self,
            request: models.RunRerankRequest,
            opts: Dict = None,
    ) -> models.RunRerankResponse:
        """
        重排是指在 RAG 过程中，通过评估文档与查询之间的相关性，将最相关的文档放在前面，确保语言模型在生成回答时优先考虑排名靠前的上下文，提高生成结果的准确性和可信度，也可以通过这种方式进行过滤，减少大模型成本。
        本接口有单账号调用上限控制，如您有提高并发限制的需求请[联系我们](https://cloud.tencent.com/act/event/Online_service)  。
        """
        
        kwargs = {}
        kwargs["action"] = "RunRerank"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunRerankResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)