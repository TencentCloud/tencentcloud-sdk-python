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
from tencentcloud.eis.v20210601 import models
from typing import Dict


class EisClient(AbstractClient):
    _apiVersion = '2021-06-01'
    _endpoint = 'eis.tencentcloudapi.com'
    _service = 'eis'

    async def GetRuntimeMC(
            self,
            request: models.GetRuntimeMCRequest,
            opts: Dict = None,
    ) -> models.GetRuntimeMCResponse:
        """
        获取运行时详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetRuntimeMC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRuntimeMCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetRuntimeResourceMonitorMetricMC(
            self,
            request: models.GetRuntimeResourceMonitorMetricMCRequest,
            opts: Dict = None,
    ) -> models.GetRuntimeResourceMonitorMetricMCResponse:
        """
        获取运行时资源监控详情，cpu，memory，bandwidth
        """
        
        kwargs = {}
        kwargs["action"] = "GetRuntimeResourceMonitorMetricMC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetRuntimeResourceMonitorMetricMCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDeployableRuntimesMC(
            self,
            request: models.ListDeployableRuntimesMCRequest,
            opts: Dict = None,
    ) -> models.ListDeployableRuntimesMCResponse:
        """
        返回用户可用的运行时列表，发布应用时返回的运行时环境，仅shared和private运行时，无sandbox运行时，并且只有running/scaling状态的
        """
        
        kwargs = {}
        kwargs["action"] = "ListDeployableRuntimesMC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDeployableRuntimesMCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRuntimeDeployedInstancesMC(
            self,
            request: models.ListRuntimeDeployedInstancesMCRequest,
            opts: Dict = None,
    ) -> models.ListRuntimeDeployedInstancesMCResponse:
        """
        获取运行时部署的应用实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListRuntimeDeployedInstancesMC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRuntimeDeployedInstancesMCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListRuntimesMC(
            self,
            request: models.ListRuntimesMCRequest,
            opts: Dict = None,
    ) -> models.ListRuntimesMCResponse:
        """
        返回用户的运行时列表，运行时管理主页使用，包含沙箱、共享运行时及独立运行时环境，不包含已经删除的运行时
        """
        
        kwargs = {}
        kwargs["action"] = "ListRuntimesMC"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListRuntimesMCResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)