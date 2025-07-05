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
from tencentcloud.ticm.v20181127 import models


class TicmClient(AbstractClient):
    _apiVersion = '2018-11-27'
    _endpoint = 'ticm.tencentcloudapi.com'
    _service = 'ticm'


    def DescribeVideoTask(self, request):
        """提交完视频审核任务后，可以通过本接口来获取当前处理的进度和结果

        :param request: Request instance for DescribeVideoTask.
        :type request: :class:`tencentcloud.ticm.v20181127.models.DescribeVideoTaskRequest`
        :rtype: :class:`tencentcloud.ticm.v20181127.models.DescribeVideoTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImageModeration(self, request):
        """本接口提供多种维度的图像审核能力，支持色情和性感内容识别，政治人物和涉政敏感场景识别，以及暴恐人物、场景、旗帜标识等违禁内容的识别。

        :param request: Request instance for ImageModeration.
        :type request: :class:`tencentcloud.ticm.v20181127.models.ImageModerationRequest`
        :rtype: :class:`tencentcloud.ticm.v20181127.models.ImageModerationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImageModeration", params, headers=headers)
            response = json.loads(body)
            model = models.ImageModerationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def VideoModeration(self, request):
        """本接口提供多种维度的视频审核能力，支持色情和性感内容识别，政治人物和涉政敏感场景识别，以及暴恐人物、场景、旗帜标识等违禁内容的识别。

        :param request: Request instance for VideoModeration.
        :type request: :class:`tencentcloud.ticm.v20181127.models.VideoModerationRequest`
        :rtype: :class:`tencentcloud.ticm.v20181127.models.VideoModerationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("VideoModeration", params, headers=headers)
            response = json.loads(body)
            model = models.VideoModerationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))