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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.eis.v20200715 import models
from typing import Dict


class EisClient(AbstractClient):
    _apiVersion = '2020-07-15'
    _endpoint = 'eis.tencentcloudapi.com'
    _service = 'eis'

    async def DescribeEisConnectorConfig(
            self,
            request: models.DescribeEisConnectorConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeEisConnectorConfigResponse:
        """
        获取连接器配置参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEisConnectorConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEisConnectorConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEisConnectorOperations(
            self,
            request: models.ListEisConnectorOperationsRequest,
            opts: Dict = None,
    ) -> models.ListEisConnectorOperationsResponse:
        """
        获取连接器操作列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListEisConnectorOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEisConnectorOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListEisConnectors(
            self,
            request: models.ListEisConnectorsRequest,
            opts: Dict = None,
    ) -> models.ListEisConnectorsResponse:
        """
        连接器列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListEisConnectors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListEisConnectorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)