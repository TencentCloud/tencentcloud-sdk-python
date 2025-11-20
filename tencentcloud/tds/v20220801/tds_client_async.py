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
from tencentcloud.tds.v20220801 import models
from typing import Dict


class TdsClient(AbstractClient):
    _apiVersion = '2022-08-01'
    _endpoint = 'tds.tencentcloudapi.com'
    _service = 'tds'

    async def DescribeFinanceFraudUltimate(
            self,
            request: models.DescribeFinanceFraudUltimateRequest,
            opts: Dict = None,
    ) -> models.DescribeFinanceFraudUltimateResponse:
        """
        查询设备标识及风险（金融旗舰版）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFinanceFraudUltimate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFinanceFraudUltimateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFraudBase(
            self,
            request: models.DescribeFraudBaseRequest,
            opts: Dict = None,
    ) -> models.DescribeFraudBaseResponse:
        """
        查询设备风险
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFraudBase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFraudBaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFraudPremium(
            self,
            request: models.DescribeFraudPremiumRequest,
            opts: Dict = None,
    ) -> models.DescribeFraudPremiumResponse:
        """
        查询设备标识及风险
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFraudPremium"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFraudPremiumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFraudUltimate(
            self,
            request: models.DescribeFraudUltimateRequest,
            opts: Dict = None,
    ) -> models.DescribeFraudUltimateResponse:
        """
        查询设备标识及风险（旗舰版）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFraudUltimate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFraudUltimateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrustedID(
            self,
            request: models.DescribeTrustedIDRequest,
            opts: Dict = None,
    ) -> models.DescribeTrustedIDResponse:
        """
        查询设备标识
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrustedID"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrustedIDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)