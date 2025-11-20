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
from tencentcloud.securitylake.v20240117 import models
from typing import Dict


class SecuritylakeClient(AbstractClient):
    _apiVersion = '2024-01-17'
    _endpoint = 'securitylake.tencentcloudapi.com'
    _service = 'securitylake'

    async def DescribeSecurityAlarmTableList(
            self,
            request: models.DescribeSecurityAlarmTableListRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityAlarmTableListResponse:
        """
        查询告警列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityAlarmTableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityAlarmTableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)