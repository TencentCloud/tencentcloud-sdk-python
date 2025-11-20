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
from tencentcloud.monitor.v20230616 import models
from typing import Dict


class MonitorClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'

    async def DescribeAlarmNotifyHistories(
            self,
            request: models.DescribeAlarmNotifyHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNotifyHistoriesResponse:
        """
        按需查询告警的通知历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotifyHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNotifyHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)