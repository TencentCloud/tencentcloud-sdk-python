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
from tencentcloud.cloudmate.v20251030 import models
from typing import Dict


class CloudmateClient(AbstractClient):
    _apiVersion = '2025-10-30'
    _endpoint = 'cloudmate.tencentcloudapi.com'
    _service = 'cloudmate'

    async def CloudMateAgent(
            self,
            request: models.CloudMateAgentRequest,
            opts: Dict = None,
    ) -> models.CloudMateAgentResponse:
        """
        发起智能诊断对话
        注意：使用该API时，请务必设置请求域名（Endpoint）为 cloudmate.ai.tencentcloudapi.com
        """
        
        kwargs = {}
        kwargs["action"] = "CloudMateAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloudMateAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)