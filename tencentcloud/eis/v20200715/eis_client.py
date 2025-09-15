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
from tencentcloud.eis.v20200715 import models


class EisClient(AbstractClient):
    _apiVersion = '2020-07-15'
    _endpoint = 'eis.tencentcloudapi.com'
    _service = 'eis'


    def DescribeEisConnectorConfig(self, request):
        r"""获取连接器配置参数

        :param request: Request instance for DescribeEisConnectorConfig.
        :type request: :class:`tencentcloud.eis.v20200715.models.DescribeEisConnectorConfigRequest`
        :rtype: :class:`tencentcloud.eis.v20200715.models.DescribeEisConnectorConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEisConnectorConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEisConnectorConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEisConnectorOperations(self, request):
        r"""获取连接器操作列表

        :param request: Request instance for ListEisConnectorOperations.
        :type request: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorOperationsRequest`
        :rtype: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorOperationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEisConnectorOperations", params, headers=headers)
            response = json.loads(body)
            model = models.ListEisConnectorOperationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListEisConnectors(self, request):
        r"""连接器列表

        :param request: Request instance for ListEisConnectors.
        :type request: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorsRequest`
        :rtype: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListEisConnectors", params, headers=headers)
            response = json.loads(body)
            model = models.ListEisConnectorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))