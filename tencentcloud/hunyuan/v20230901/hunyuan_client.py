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


    def ChatPro(self, request):
        """腾讯混元大模型高级版是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口为SSE协议。

        :param request: Request instance for ChatPro.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.ChatProRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ChatProResponse`

        """
        try:
            params = request._serialize()
            return self.call_sse("ChatPro", params, headers=request.headers)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ChatStd(self, request):
        """腾讯混元大模型标准版是由腾讯研发的大语言模型，具备强大的中文创作能力，复杂语境下的逻辑推理能力，以及可靠的任务执行能力。本接口为SSE协议。

        :param request: Request instance for ChatStd.
        :type request: :class:`tencentcloud.hunyuan.v20230901.models.ChatStdRequest`
        :rtype: :class:`tencentcloud.hunyuan.v20230901.models.ChatStdResponse`

        """
        try:
            params = request._serialize()
            return self.call_sse("ChatStd", params, headers=request.headers)
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