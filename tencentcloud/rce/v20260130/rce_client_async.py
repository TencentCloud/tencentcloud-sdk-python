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
from tencentcloud.rce.v20260130 import models
from typing import Dict


class RceClient(AbstractClient):
    _apiVersion = '2026-01-30'
    _endpoint = 'rce.tencentcloudapi.com'
    _service = 'rce'

    async def AssessEnvironmentRisk(
            self,
            request: models.AssessEnvironmentRiskRequest,
            opts: Dict = None,
    ) -> models.AssessEnvironmentRiskResponse:
        """
        环境风险评估
        """
        
        kwargs = {}
        kwargs["action"] = "AssessEnvironmentRisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssessEnvironmentRiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)