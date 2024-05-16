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
from tencentcloud.vcg.v20240404 import models


class VcgClient(AbstractClient):
    _apiVersion = '2024-04-04'
    _endpoint = 'vcg.tencentcloudapi.com'
    _service = 'vcg'


    def DescribeVideoStylizationJob(self, request):
        """用于查询视频风格化任务。视频风格化支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。

        :param request: Request instance for DescribeVideoStylizationJob.
        :type request: :class:`tencentcloud.vcg.v20240404.models.DescribeVideoStylizationJobRequest`
        :rtype: :class:`tencentcloud.vcg.v20240404.models.DescribeVideoStylizationJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoStylizationJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoStylizationJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoStylizationJob(self, request):
        """用于提交视频风格化任务。支持将输入视频生成特定风格的视频。生成后的视频画面风格多样、流畅自然，能够满足社交娱乐、互动营销、视频素材制作等场景的需求。

        :param request: Request instance for SubmitVideoStylizationJob.
        :type request: :class:`tencentcloud.vcg.v20240404.models.SubmitVideoStylizationJobRequest`
        :rtype: :class:`tencentcloud.vcg.v20240404.models.SubmitVideoStylizationJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoStylizationJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoStylizationJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))