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
from tencentcloud.cis.v20180408 import models


class CisClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'cis.tencentcloudapi.com'
    _service = 'cis'


    def CreateContainerInstance(self, request):
        """此接口（CreateContainerInstance）用于创建容器实例

        :param request: Request instance for CreateContainerInstance.
        :type request: :class:`tencentcloud.cis.v20180408.models.CreateContainerInstanceRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.CreateContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateContainerInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateContainerInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteContainerInstance(self, request):
        """此接口（DeleteContainerInstance）用于删除容器实例

        :param request: Request instance for DeleteContainerInstance.
        :type request: :class:`tencentcloud.cis.v20180408.models.DeleteContainerInstanceRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.DeleteContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteContainerInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteContainerInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerInstance(self, request):
        """此接口（DescribeContainerInstance）用于获取容器实例详情

        :param request: Request instance for DescribeContainerInstance.
        :type request: :class:`tencentcloud.cis.v20180408.models.DescribeContainerInstanceRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.DescribeContainerInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerInstanceEvents(self, request):
        """此接口（DescribeContainerInstanceEvents）用于查询容器实例事件列表

        :param request: Request instance for DescribeContainerInstanceEvents.
        :type request: :class:`tencentcloud.cis.v20180408.models.DescribeContainerInstanceEventsRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.DescribeContainerInstanceEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerInstanceEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerInstanceEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerInstances(self, request):
        """此接口（DescribeContainerInstances）查询容器实例列表

        :param request: Request instance for DescribeContainerInstances.
        :type request: :class:`tencentcloud.cis.v20180408.models.DescribeContainerInstancesRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.DescribeContainerInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeContainerLog(self, request):
        """此接口（DescribeContainerLog）用于获取容器日志信息

        :param request: Request instance for DescribeContainerLog.
        :type request: :class:`tencentcloud.cis.v20180408.models.DescribeContainerLogRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.DescribeContainerLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeContainerLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeContainerLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateCis(self, request):
        """此接口（InquiryPriceCreateCis）用于查询容器实例价格

        :param request: Request instance for InquiryPriceCreateCis.
        :type request: :class:`tencentcloud.cis.v20180408.models.InquiryPriceCreateCisRequest`
        :rtype: :class:`tencentcloud.cis.v20180408.models.InquiryPriceCreateCisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateCis", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateCisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))