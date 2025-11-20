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
from tencentcloud.tchd.v20230306 import models
from typing import Dict


class TchdClient(AbstractClient):
    _apiVersion = '2023-03-06'
    _endpoint = 'tchd.tencentcloudapi.com'
    _service = 'tchd'

    async def DescribeEventStatistics(
            self,
            request: models.DescribeEventStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeEventStatisticsResponse:
        """
        本接口用于查询腾讯云健康看板的实时可用性事件信息，可以通过产品列表、地域进行过滤查询。
        可以参考健康看板历史事件页面来获取查询案例（链接：https://status.cloud.tencent.com/history）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvents(
            self,
            request: models.DescribeEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeEventsResponse:
        """
        本接口用于查询腾讯云健康看板的可用性事件信息，可以通过产品列表、地域列表和事件发生日期进行过滤查询。
        当查询的产品对应时间内无事件时将返回空结果。
        可以参考健康看板历史事件页面来获取查询案例（链接：https://status.cloud.tencent.com/history）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)