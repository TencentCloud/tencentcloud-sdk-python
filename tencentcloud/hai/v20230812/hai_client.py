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
from tencentcloud.hai.v20230812 import models


class HaiClient(AbstractClient):
    _apiVersion = '2023-08-12'
    _endpoint = 'hai.tencentcloudapi.com'
    _service = 'hai'


    def RunInstances(self, request):
        """本接口 (RunInstances) 用于创建一个或多个指定配置的实例。

        :param request: Request instance for RunInstances.
        :type request: :class:`tencentcloud.hai.v20230812.models.RunInstancesRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.RunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateInstances(self, request):
        """本接口 (TerminateInstances) 用于主动退还实例。

        :param request: Request instance for TerminateInstances.
        :type request: :class:`tencentcloud.hai.v20230812.models.TerminateInstancesRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.TerminateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))