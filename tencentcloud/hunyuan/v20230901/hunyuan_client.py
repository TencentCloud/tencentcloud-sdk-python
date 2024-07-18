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


    def ChatCompletions(self, request):
        """腾讯混元大模型是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口支持流式或非流式调用，当使用流式调用时为 SSE 协议。

         1. 本接口暂不支持返回图片内容。
         2. 默认每种模型单账号限制并发数为 5 路，如您有提高并发限制的需求请 [联系我们](https://cloud.tencent.com/act/event/Online_service) 。
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