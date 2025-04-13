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
from tencentcloud.hunyuan.v20230901 import models


class HunyuanClient(AbstractClient):
    _apiVersion = '2023-09-01'
    _endpoint = 'hunyuan.tencentcloudapi.com'
    _service = 'hunyuan'


    def ActivateService(self, request):
        """开通服务

        :param request: Request instance for ActivateService.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.ActivateServiceRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ActivateServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateService", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatCompletions(self, request):
        """如需使用OpenAI兼容接口， 请参考文档：[OpenAI 兼容接口](https://cloud.tencent.com/document/product/1729/111007)

        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for ChatCompletions.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.ChatCompletionsRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ChatCompletionsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatCompletions", params, models.ChatCompletionsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatTranslations(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for ChatTranslations.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.ChatTranslationsRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ChatTranslationsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("ChatTranslations", params, models.ChatTranslationsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateThread(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for CreateThread.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.CreateThreadRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.CreateThreadResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("CreateThread", params, models.CreateThreadResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FilesDeletions(self, request):
        """删除文件。

        :param request: Request instance for FilesDeletions.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.FilesDeletionsRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.FilesDeletionsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("FilesDeletions", params, models.FilesDeletionsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FilesList(self, request):
        """文件列表。

        :param request: Request instance for FilesList.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.FilesListRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.FilesListResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("FilesList", params, models.FilesListResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def FilesUploads(self, request):
        """上传用于不同用途的文件。
        当前用途仅支持 hunyuan 等模型的文档理解。

        :param request: Request instance for FilesUploads.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.FilesUploadsRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.FilesUploadsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("FilesUploads", params, models.FilesUploadsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetEmbedding(self, request):
        """腾讯混元 Embedding 接口，可以将文本转化为高质量的向量数据。向量维度为1024维。

        :param request: Request instance for GetEmbedding.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.GetEmbeddingRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GetEmbeddingResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetEmbedding", params, headers=headers)
            response = json.loads(body)
            model = models.GetEmbeddingResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetThread(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for GetThread.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.GetThreadRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GetThreadResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetThread", params, models.GetThreadResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetThreadMessage(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for GetThreadMessage.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.GetThreadMessageRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GetThreadMessageResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetThreadMessage", params, models.GetThreadMessageResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetThreadMessageList(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for GetThreadMessageList.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.GetThreadMessageListRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GetThreadMessageListResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GetThreadMessageList", params, models.GetThreadMessageListResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetTokenCount(self, request):
        """该接口用于计算文本对应Token数、字符数。

        :param request: Request instance for GetTokenCount.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.GetTokenCountRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GetTokenCountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetTokenCount", params, headers=headers)
            response = json.loads(body)
            model = models.GetTokenCountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GroupChatCompletions(self, request):
        """如需使用OpenAI兼容接口， 请参考文档：[OpenAI 兼容接口](https://cloud.tencent.com/document/product/1729/111007)

        腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for GroupChatCompletions.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.GroupChatCompletionsRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.GroupChatCompletionsResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("GroupChatCompletions", params, models.GroupChatCompletionsResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanImageChatJob(self, request):
        """混元生图（多轮对话）接口基于混元大模型，将根据输入的文本描述生成图像，支持通过多轮对话的方式不断调整图像内容。分为提交任务和查询任务2个接口。
        提交任务：输入文本和前置对话 ID 等，提交一个混元生图多轮对话异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得在上一轮对话基础上继续生成的图像结果。
        混元生图（多轮对话）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for QueryHunyuanImageChatJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanImageChatJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanImageChatJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanImageChatJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanImageChatJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanImageJob(self, request):
        """混元生图接口基于混元大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个混元生图异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。混元生图默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for QueryHunyuanImageJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanImageJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanImageJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanImageJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanImageJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanTo3DJob(self, request):
        """查询混元生3D任务

        :param request: Request instance for QueryHunyuanTo3DJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanTo3DJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.QueryHunyuanTo3DJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunThread(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认该接口下单账号限制并发数为  5 路，如您有提高并发限制的需求请 [购买](https://buy.cloud.tencent.com/hunyuan) 。
         3. 请使用 SDK 调用本接口，每种开发语言的 SDK Git 仓库 examples/hunyuan/v20230901/ 目录下有提供示例供参考。SDK 链接在文档下方 “**开发者资源 - SDK**” 部分提供。
         4. 我们推荐您使用 API Explorer，方便快速地在线调试接口和下载各语言的示例代码，[点击打开](https://console.cloud.tencent.com/api/explorer?Product=hunyuan&Version=2023-09-01&Action=ChatCompletions)。

        :param request: Request instance for RunThread.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.RunThreadRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.RunThreadResponse`

        """
        try:
            params = request._serialize()
            return self._call_and_deserialize("RunThread", params, models.RunThreadResponse, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetPayMode(self, request):
        """设置付费模式

        :param request: Request instance for SetPayMode.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SetPayModeRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SetPayModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPayMode", params, headers=headers)
            response = json.loads(body)
            model = models.SetPayModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanImageChatJob(self, request):
        """混元生图（多轮对话）接口基于混元大模型，将根据输入的文本描述生成图像，支持通过多轮对话的方式不断调整图像内容。分为提交任务和查询任务2个接口。
        提交任务：输入文本和前置对话 ID 等，提交一个混元生图多轮对话异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得在上一轮对话基础上继续生成的图像结果。
        混元生图（多轮对话）默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanImageChatJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanImageChatJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanImageChatJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanImageChatJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanImageChatJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanImageJob(self, request):
        """混元生图接口基于混元大模型，将根据输入的文本描述，智能生成与之相关的结果图。分为提交任务和查询任务2个接口。
        提交任务：输入文本等，提交一个混元生图异步任务，获得任务 ID。
        查询任务：根据任务 ID 查询任务的处理状态、处理结果，任务处理完成后可获得生成图像结果。
        并发任务数（并发）说明：并发任务数指能同时处理的任务数量。混元生图默认提供1个并发任务数，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanImageJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanImageJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanImageJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanImageJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanImageJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DJob(self, request):
        """提交混元生3D任务

        :param request: Request instance for SubmitHunyuanTo3DJob.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanTo3DJobRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.SubmitHunyuanTo3DJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TextToImageLite(self, request):
        """文生图轻量版接口根据输入的文本描述，智能生成与之相关的结果图。
        文生图轻量版默认提供3个并发任务数，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后才能开始处理下一个任务。

        :param request: Request instance for TextToImageLite.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.TextToImageLiteRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.TextToImageLiteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TextToImageLite", params, headers=headers)
            response = json.loads(body)
            model = models.TextToImageLiteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))