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
from tencentcloud.vtc.v20240223 import models


class VtcClient(AbstractClient):
    _apiVersion = '2024-02-23'
    _endpoint = 'vtc.tencentcloudapi.com'
    _service = 'vtc'


    def ConfirmVideoTranslateJob(self, request):
        """确认视频翻译结果

        :param request: Request instance for ConfirmVideoTranslateJob.
        :type request: :class:`tencentcloud.vtc.v20240223.models.ConfirmVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vtc.v20240223.models.ConfirmVideoTranslateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ConfirmVideoTranslateJob", params, headers=headers)
            response = json.loads(body)
            model = models.ConfirmVideoTranslateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVideoTranslateJob(self, request):
        """查询视频翻译任务

        :param request: Request instance for DescribeVideoTranslateJob.
        :type request: :class:`tencentcloud.vtc.v20240223.models.DescribeVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vtc.v20240223.models.DescribeVideoTranslateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVideoTranslateJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVideoTranslateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitVideoTranslateJob(self, request):
        """提交视频转译任务

        :param request: Request instance for SubmitVideoTranslateJob.
        :type request: :class:`tencentcloud.vtc.v20240223.models.SubmitVideoTranslateJobRequest`
        :rtype: :class:`tencentcloud.vtc.v20240223.models.SubmitVideoTranslateJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitVideoTranslateJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitVideoTranslateJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))