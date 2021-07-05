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
from tencentcloud.eis.v20200715 import models


class EisClient(AbstractClient):
    _apiVersion = '2020-07-15'
    _endpoint = 'eis.tencentcloudapi.com'
    _service = 'eis'


    def DescribeEisConnectorConfig(self, request):
        """获取连接器配置参数

        :param request: Request instance for DescribeEisConnectorConfig.
        :type request: :class:`tencentcloud.eis.v20200715.models.DescribeEisConnectorConfigRequest`
        :rtype: :class:`tencentcloud.eis.v20200715.models.DescribeEisConnectorConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeEisConnectorConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeEisConnectorConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListEisConnectorOperations(self, request):
        """获取连接器操作列表

        :param request: Request instance for ListEisConnectorOperations.
        :type request: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorOperationsRequest`
        :rtype: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorOperationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEisConnectorOperations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEisConnectorOperationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListEisConnectors(self, request):
        """连接器列表

        :param request: Request instance for ListEisConnectors.
        :type request: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorsRequest`
        :rtype: :class:`tencentcloud.eis.v20200715.models.ListEisConnectorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ListEisConnectors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ListEisConnectorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)