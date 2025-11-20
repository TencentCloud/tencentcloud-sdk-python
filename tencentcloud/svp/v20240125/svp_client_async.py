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
from tencentcloud.svp.v20240125 import models
from typing import Dict


class SvpClient(AbstractClient):
    _apiVersion = '2024-01-25'
    _endpoint = 'svp.tencentcloudapi.com'
    _service = 'svp'

    async def CreateSavingPlanOrder(
            self,
            request: models.CreateSavingPlanOrderRequest,
            opts: Dict = None,
    ) -> models.CreateSavingPlanOrderResponse:
        """
        创建节省计划订单
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSavingPlanOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSavingPlanOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSavingPlanCoverage(
            self,
            request: models.DescribeSavingPlanCoverageRequest,
            opts: Dict = None,
    ) -> models.DescribeSavingPlanCoverageResponse:
        """
        查询当前用户节省计划覆盖率明细数据，如无特别说明，金额单位均为元（国内站）或者美元（国际站）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSavingPlanCoverage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSavingPlanCoverageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSavingPlanDeduct(
            self,
            request: models.DescribeSavingPlanDeductRequest,
            opts: Dict = None,
    ) -> models.DescribeSavingPlanDeductResponse:
        """
        查询节省计划抵扣明细
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSavingPlanDeduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSavingPlanDeductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSavingPlanOverview(
            self,
            request: models.DescribeSavingPlanOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeSavingPlanOverviewResponse:
        """
        查用当前用户明细节省计划总览查询时段内的使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSavingPlanOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSavingPlanOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSavingPlanUsage(
            self,
            request: models.DescribeSavingPlanUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeSavingPlanUsageResponse:
        """
        查用当前用户明细节省计划查询时段内的使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSavingPlanUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSavingPlanUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)