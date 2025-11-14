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
from tencentcloud.ai3d.v20250513 import models


class Ai3dClient(AbstractClient):
    _apiVersion = '2025-05-13'
    _endpoint = 'ai3d.tencentcloudapi.com'
    _service = 'ai3d'


    def QueryHunyuanTo3DProJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for QueryHunyuanTo3DProJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DProJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DProJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryHunyuanTo3DRapidJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for QueryHunyuanTo3DRapidJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DRapidJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.QueryHunyuanTo3DRapidJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryHunyuanTo3DRapidJob", params, headers=headers)
            response = json.loads(body)
            model = models.QueryHunyuanTo3DRapidJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DProJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供3个并发，代表最多能同时处理3个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanTo3DProJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DProJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DProJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DProJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DProJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitHunyuanTo3DRapidJob(self, request):
        r"""混元生3D接口，基于混元大模型，根据输入的文本描述/图片智能生成3D。
        默认提供1个并发，代表最多能同时处理1个已提交的任务，上一个任务处理完毕后，才能开始处理下一个任务。

        :param request: Request instance for SubmitHunyuanTo3DRapidJob.
        :type request: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DRapidJobRequest`
        :rtype: :class:`tencentcloud.ai3d.v20250513.models.SubmitHunyuanTo3DRapidJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitHunyuanTo3DRapidJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitHunyuanTo3DRapidJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))