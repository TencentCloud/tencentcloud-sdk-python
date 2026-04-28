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
from tencentcloud.antiddos.v20250903 import models
from typing import Dict


class AntiddosClient(AbstractClient):
    _apiVersion = '2025-09-03'
    _endpoint = 'antiddos.tencentcloudapi.com'
    _service = 'antiddos'

    async def DescribeDDoSBlockRecords(
            self,
            request: models.DescribeDDoSBlockRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDDoSBlockRecordsResponse:
        """
        查询封堵解封记录和解封配额信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDDoSBlockRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDDoSBlockRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnblockResources(
            self,
            request: models.UnblockResourcesRequest,
            opts: Dict = None,
    ) -> models.UnblockResourcesResponse:
        """
        申请解封资源，可通过 DescribeDDoSBlockRecords 接口获取资源的封堵解封状态。
        """
        
        kwargs = {}
        kwargs["action"] = "UnblockResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnblockResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)