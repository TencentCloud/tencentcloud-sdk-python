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
from tencentcloud.hunyuan.v20230901 import models
from typing import Dict


class HunyuanClient(AbstractClient):
    _apiVersion = '2023-09-01'
    _endpoint = 'hunyuan.tencentcloudapi.com'
    _service = 'hunyuan'

    async def ActivateService(
            self,
            request: models.ActivateServiceRequest,
            opts: Dict = None,
    ) -> models.ActivateServiceResponse:
        """
        开通服务
        """
        
        kwargs = {}
        kwargs["action"] = "ActivateService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActivateServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChatCompletions(
            self,
            request: models.ChatCompletionsRequest,
            opts: Dict = None,
    ) -> models.ChatCompletionsResponse:
        """
        如需使用OpenAI兼容接口， 请参考文档：[OpenAI 兼容接口](https://cloud.tencent.com/document/product/1729/111007)

        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "ChatCompletions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatCompletionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChatTranslations(
            self,
            request: models.ChatTranslationsRequest,
            opts: Dict = None,
    ) -> models.ChatTranslationsResponse:
        """
        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "ChatTranslations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChatTranslationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateThread(
            self,
            request: models.CreateThreadRequest,
            opts: Dict = None,
    ) -> models.CreateThreadResponse:
        """
        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateThread"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateThreadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FilesDeletions(
            self,
            request: models.FilesDeletionsRequest,
            opts: Dict = None,
    ) -> models.FilesDeletionsResponse:
        """
        删除文件。
        """
        
        kwargs = {}
        kwargs["action"] = "FilesDeletions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FilesDeletionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FilesList(
            self,
            request: models.FilesListRequest,
            opts: Dict = None,
    ) -> models.FilesListResponse:
        """
        文件列表。
        """
        
        kwargs = {}
        kwargs["action"] = "FilesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FilesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FilesUploads(
            self,
            request: models.FilesUploadsRequest,
            opts: Dict = None,
    ) -> models.FilesUploadsResponse:
        """
        上传用于不同用途的文件。
        当前用途仅支持 hunyuan 等模型的文档理解。
        """
        
        kwargs = {}
        kwargs["action"] = "FilesUploads"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FilesUploadsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetEmbedding(
            self,
            request: models.GetEmbeddingRequest,
            opts: Dict = None,
    ) -> models.GetEmbeddingResponse:
        """
        腾讯混元 Embedding 接口，可以将文本转化为高质量的向量数据。向量维度为1024维。
        """
        
        kwargs = {}
        kwargs["action"] = "GetEmbedding"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetEmbeddingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetThread(
            self,
            request: models.GetThreadRequest,
            opts: Dict = None,
    ) -> models.GetThreadResponse:
        """
        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "GetThread"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetThreadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetThreadMessage(
            self,
            request: models.GetThreadMessageRequest,
            opts: Dict = None,
    ) -> models.GetThreadMessageResponse:
        """
        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "GetThreadMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetThreadMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetThreadMessageList(
            self,
            request: models.GetThreadMessageListRequest,
            opts: Dict = None,
    ) -> models.GetThreadMessageListResponse:
        """
        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "GetThreadMessageList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetThreadMessageListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTokenCount(
            self,
            request: models.GetTokenCountRequest,
            opts: Dict = None,
    ) -> models.GetTokenCountResponse:
        """
        该接口用于计算文本对应Token数、字符数。
        """
        
        kwargs = {}
        kwargs["action"] = "GetTokenCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTokenCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GroupChatCompletions(
            self,
            request: models.GroupChatCompletionsRequest,
            opts: Dict = None,
    ) -> models.GroupChatCompletionsResponse:
        """
        如需使用OpenAI兼容接口， 请参考文档：[OpenAI 兼容接口](https://cloud.tencent.com/document/product/1729/111007)

        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "GroupChatCompletions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GroupChatCompletionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImageQuestion(
            self,
            request: models.ImageQuestionRequest,
            opts: Dict = None,
    ) -> models.ImageQuestionResponse:
        """
        如需使用OpenAI兼容接口， 请参考文档：[OpenAI 兼容接口](https://cloud.tencent.com/document/product/1729/111007)

        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "ImageQuestion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImageQuestionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryHunyuanImageChatJob(
            self,
            request: models.QueryHunyuanImageChatJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuanImageChatJobResponse:
        """
        混元生图（多轮对话）接口基于混元大模型，将根据输入的文本描述生成图像，支持通过多轮对话的方式不断调整图像内容。分为提交任务和查询任务2个接口。
        提交任务：输入文本和前置对话 ID 等，提交一个混元生图多轮对话异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得在上一轮对话基础上继续生成的图像结果。
        混元生图（多轮对话）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuanImageChatJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuanImageChatJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryHunyuanImageJob(
            self,
            request: models.QueryHunyuanImageJobRequest,
            opts: Dict = None,
    ) -> models.QueryHunyuanImageJobResponse:
        """
        混元生图接口基于混元大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个混元生图异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。混元生图默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "QueryHunyuanImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryHunyuanImageJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunThread(
            self,
            request: models.RunThreadRequest,
            opts: Dict = None,
    ) -> models.RunThreadResponse:
        """
        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。
        """
        
        kwargs = {}
        kwargs["action"] = "RunThread"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunThreadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetPayMode(
            self,
            request: models.SetPayModeRequest,
            opts: Dict = None,
    ) -> models.SetPayModeResponse:
        """
        设置付费模式
        """
        
        kwargs = {}
        kwargs["action"] = "SetPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuanImageChatJob(
            self,
            request: models.SubmitHunyuanImageChatJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanImageChatJobResponse:
        """
        混元生图（多轮对话）接口基于混元大模型，将根据输入的文本描述生成图像，支持通过多轮对话的方式不断调整图像内容。分为提交任务和查询任务2个接口。
        提交任务：输入文本和前置对话 ID 等，提交一个混元生图多轮对话异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得在上一轮对话基础上继续生成的图像结果。
        混元生图（多轮对话）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanImageChatJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanImageChatJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitHunyuanImageJob(
            self,
            request: models.SubmitHunyuanImageJobRequest,
            opts: Dict = None,
    ) -> models.SubmitHunyuanImageJobResponse:
        """
        混元生图接口基于混元大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个混元生图异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。混元生图默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitHunyuanImageJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitHunyuanImageJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TextToImageLite(
            self,
            request: models.TextToImageLiteRequest,
            opts: Dict = None,
    ) -> models.TextToImageLiteResponse:
        """
        文生图轻量版接口根据输入的文本描述，智能生成与之相关的结果图。
        文生图轻量版默认提供3个并发任务数，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。
        """
        
        kwargs = {}
        kwargs["action"] = "TextToImageLite"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TextToImageLiteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)