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
from tencentcloud.csxg.v20230303 import models


class CsxgClient(AbstractClient):
    _apiVersion = '2023-03-03'
    _endpoint = 'csxg.tencentcloudapi.com'
    _service = 'csxg'


    def Create5GInstance(self, request):
        """创建5G入云服务接口

        :param request: Request instance for Create5GInstance.
        :type request: :class:`tencentcloud.csxg.v20230303.models.Create5GInstanceRequest`
        :rtype: :class:`tencentcloud.csxg.v20230303.models.Create5GInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Create5GInstance", params, headers=headers)
            response = json.loads(body)
            model = models.Create5GInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Delete5GInstance(self, request):
        """删除5G入云服务

        :param request: Request instance for Delete5GInstance.
        :type request: :class:`tencentcloud.csxg.v20230303.models.Delete5GInstanceRequest`
        :rtype: :class:`tencentcloud.csxg.v20230303.models.Delete5GInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Delete5GInstance", params, headers=headers)
            response = json.loads(body)
            model = models.Delete5GInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Describe5GAPNs(self, request):
        """查询APN信息

        :param request: Request instance for Describe5GAPNs.
        :type request: :class:`tencentcloud.csxg.v20230303.models.Describe5GAPNsRequest`
        :rtype: :class:`tencentcloud.csxg.v20230303.models.Describe5GAPNsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Describe5GAPNs", params, headers=headers)
            response = json.loads(body)
            model = models.Describe5GAPNsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Describe5GInstances(self, request):
        """查询5G入云服务

        :param request: Request instance for Describe5GInstances.
        :type request: :class:`tencentcloud.csxg.v20230303.models.Describe5GInstancesRequest`
        :rtype: :class:`tencentcloud.csxg.v20230303.models.Describe5GInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Describe5GInstances", params, headers=headers)
            response = json.loads(body)
            model = models.Describe5GInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def Modify5GInstanceAttribute(self, request):
        """修改5G入云服务

        :param request: Request instance for Modify5GInstanceAttribute.
        :type request: :class:`tencentcloud.csxg.v20230303.models.Modify5GInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.csxg.v20230303.models.Modify5GInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("Modify5GInstanceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.Modify5GInstanceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))