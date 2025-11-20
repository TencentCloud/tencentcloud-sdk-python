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
from tencentcloud.advisor.v20200721 import models
from typing import Dict


class AdvisorClient(AbstractClient):
    _apiVersion = '2020-07-21'
    _endpoint = 'advisor.tencentcloudapi.com'
    _service = 'advisor'

    async def DescribeStrategies(
            self,
            request: models.DescribeStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeStrategiesResponse:
        """
        用于查询评估项的信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStrategyRisks(
            self,
            request: models.DescribeTaskStrategyRisksRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStrategyRisksResponse:
        """
        查询评估项风险实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStrategyRisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStrategyRisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)