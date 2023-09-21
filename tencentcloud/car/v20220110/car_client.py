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
from tencentcloud.car.v20220110 import models


class CarClient(AbstractClient):
    _apiVersion = '2022-01-10'
    _endpoint = 'car.tencentcloudapi.com'
    _service = 'car'


    def ApplyConcurrent(self, request):
        """本接口用于申请并发。接口超时时间：20秒。

        :param request: Request instance for ApplyConcurrent.
        :type request: :class:`tencentcloud.car.v20220110.models.ApplyConcurrentRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.ApplyConcurrentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ApplyConcurrent", params, headers=headers)
            response = json.loads(body)
            model = models.ApplyConcurrentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSession(self, request):
        """本接口用于创建会话。接口超时时间：5秒。

        :param request: Request instance for CreateSession.
        :type request: :class:`tencentcloud.car.v20220110.models.CreateSessionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.CreateSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroySession(self, request):
        """销毁会话

        :param request: Request instance for DestroySession.
        :type request: :class:`tencentcloud.car.v20220110.models.DestroySessionRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.DestroySessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroySession", params, headers=headers)
            response = json.loads(body)
            model = models.DestroySessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishStream(self, request):
        """开始云端推流

        :param request: Request instance for StartPublishStream.
        :type request: :class:`tencentcloud.car.v20220110.models.StartPublishStreamRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.StartPublishStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishStream", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartPublishStreamWithURL(self, request):
        """开始云端推流到指定URL

        :param request: Request instance for StartPublishStreamWithURL.
        :type request: :class:`tencentcloud.car.v20220110.models.StartPublishStreamWithURLRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.StartPublishStreamWithURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartPublishStreamWithURL", params, headers=headers)
            response = json.loads(body)
            model = models.StartPublishStreamWithURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopPublishStream(self, request):
        """停止云端推流

        :param request: Request instance for StopPublishStream.
        :type request: :class:`tencentcloud.car.v20220110.models.StopPublishStreamRequest`
        :rtype: :class:`tencentcloud.car.v20220110.models.StopPublishStreamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopPublishStream", params, headers=headers)
            response = json.loads(body)
            model = models.StopPublishStreamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))