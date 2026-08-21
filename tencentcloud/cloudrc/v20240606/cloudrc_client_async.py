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
from tencentcloud.cloudrc.v20240606 import models
from typing import Dict


class CloudrcClient(AbstractClient):
    _apiVersion = '2024-06-06'
    _endpoint = 'cloudrc.tencentcloudapi.com'
    _service = 'cloudrc'

    async def DescribeResource(
            self,
            request: models.DescribeResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceResponse:
        """
        查询资源详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SearchResources(
            self,
            request: models.SearchResourcesRequest,
            opts: Dict = None,
    ) -> models.SearchResourcesResponse:
        """
        搜索资源
        """
        
        kwargs = {}
        kwargs["action"] = "SearchResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SearchResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)