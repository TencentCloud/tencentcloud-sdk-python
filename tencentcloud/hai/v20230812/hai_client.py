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


    def DescribeApplications(self, request):
        """查询应用

        :param request: Request instance for DescribeApplications.
        :type request: :class:`tencentcloud.hai.v20230812.models.DescribeApplicationsRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.DescribeApplicationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeApplications", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeApplicationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNetworkStatus(self, request):
        """查询实例的网络配置及消耗情况

        :param request: Request instance for DescribeInstanceNetworkStatus.
        :type request: :class:`tencentcloud.hai.v20230812.models.DescribeInstanceNetworkStatusRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.DescribeInstanceNetworkStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNetworkStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNetworkStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstances(self, request):
        """查询实例

        :param request: Request instance for DescribeInstances.
        :type request: :class:`tencentcloud.hai.v20230812.models.DescribeInstancesRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.DescribeInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """查询地域列表

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.hai.v20230812.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScenes(self, request):
        """查询场景

        :param request: Request instance for DescribeScenes.
        :type request: :class:`tencentcloud.hai.v20230812.models.DescribeScenesRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.DescribeScenesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScenes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScenesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceLoginSettings(self, request):
        """查询服务登录配置

        :param request: Request instance for DescribeServiceLoginSettings.
        :type request: :class:`tencentcloud.hai.v20230812.models.DescribeServiceLoginSettingsRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.DescribeServiceLoginSettingsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceLoginSettings", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceLoginSettingsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceRunInstances(self, request):
        """本接口 (InquirePriceRunInstances) 用于实例询价。

        :param request: Request instance for InquirePriceRunInstances.
        :type request: :class:`tencentcloud.hai.v20230812.models.InquirePriceRunInstancesRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.InquirePriceRunInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceRunInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceRunInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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


    def StartInstance(self, request):
        """本接口 (StartInstance) 用于主动启动实例。

        :param request: Request instance for StartInstance.
        :type request: :class:`tencentcloud.hai.v20230812.models.StartInstanceRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.StartInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInstance(self, request):
        """本接口 (StopInstance) 用于主动关闭实例。

        :param request: Request instance for StopInstance.
        :type request: :class:`tencentcloud.hai.v20230812.models.StopInstanceRequest`
        :rtype: :class:`tencentcloud.hai.v20230812.models.StopInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInstance", params, headers=headers)
            response = json.loads(body)
            model = models.StopInstanceResponse()
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