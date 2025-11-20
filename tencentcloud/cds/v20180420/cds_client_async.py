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
from tencentcloud.cds.v20180420 import models
from typing import Dict


class CdsClient(AbstractClient):
    _apiVersion = '2018-04-20'
    _endpoint = 'cds.tencentcloudapi.com'
    _service = 'cds'

    async def DescribeDbauditInstanceType(
            self,
            request: models.DescribeDbauditInstanceTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeDbauditInstanceTypeResponse:
        """
        本接口 (DescribeDbauditInstanceType) 用于查询可售卖的产品规格列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbauditInstanceType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbauditInstanceTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbauditInstances(
            self,
            request: models.DescribeDbauditInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDbauditInstancesResponse:
        """
        本接口 (DescribeDbauditInstances) 用于查询数据安全审计实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbauditInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbauditInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDbauditUsedRegions(
            self,
            request: models.DescribeDbauditUsedRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDbauditUsedRegionsResponse:
        """
        本接口 (DescribeDbauditUsedRegions) 用于查询可售卖地域列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDbauditUsedRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDbauditUsedRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceDbauditInstance(
            self,
            request: models.InquiryPriceDbauditInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceDbauditInstanceResponse:
        """
        用于查询数据安全审计产品实例价格
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceDbauditInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceDbauditInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDbauditInstancesRenewFlag(
            self,
            request: models.ModifyDbauditInstancesRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyDbauditInstancesRenewFlagResponse:
        """
        本接口 (ModifyDbauditInstancesRenewFlag) 用于修改数据安全审计产品实例续费标识
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDbauditInstancesRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDbauditInstancesRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)