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
from tencentcloud.teo.v20220106 import models
from typing import Dict


class TeoClient(AbstractClient):
    _apiVersion = '2022-01-06'
    _endpoint = 'teo.tencentcloudapi.com'
    _service = 'teo'

    async def CreatePrefetchTask(
            self,
            request: models.CreatePrefetchTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePrefetchTaskResponse:
        """
        老版本接口，最近一次调用时23年11月了

        创建预热任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrefetchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrefetchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePurgeTask(
            self,
            request: models.CreatePurgeTaskRequest,
            opts: Dict = None,
    ) -> models.CreatePurgeTaskResponse:
        """
        老版本接口，老版本pod的最近一次调用在23年11月

        创建清除缓存任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePurgeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePurgeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrefetchTasks(
            self,
            request: models.DescribePrefetchTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePrefetchTasksResponse:
        """
        查询预热任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrefetchTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrefetchTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePurgeTasks(
            self,
            request: models.DescribePurgeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribePurgeTasksResponse:
        """
        查询清除缓存历史记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePurgeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePurgeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeZones(
            self,
            request: models.DescribeZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeZonesResponse:
        """
        用户查询用户站点信息列表，支持分页
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)