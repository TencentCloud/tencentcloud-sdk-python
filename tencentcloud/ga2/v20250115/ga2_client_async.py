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
from tencentcloud.ga2.v20250115 import models
from typing import Dict


class Ga2Client(AbstractClient):
    _apiVersion = '2025-01-15'
    _endpoint = 'ga2.tencentcloudapi.com'
    _service = 'ga2'

    async def DescribeCrossBorderSettlement(
            self,
            request: models.DescribeCrossBorderSettlementRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderSettlementResponse:
        """
        查询跨境账单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderSettlement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderSettlementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)