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
from tencentcloud.controlcenter.v20230110 import models
from typing import Dict


class ControlcenterClient(AbstractClient):
    _apiVersion = '2023-01-10'
    _endpoint = 'controlcenter.tencentcloudapi.com'
    _service = 'controlcenter'

    async def BatchApplyAccountBaselines(
            self,
            request: models.BatchApplyAccountBaselinesRequest,
            opts: Dict = None,
    ) -> models.BatchApplyAccountBaselinesResponse:
        """
        批量对存量账号应用基线
        """
        
        kwargs = {}
        kwargs["action"] = "BatchApplyAccountBaselines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchApplyAccountBaselinesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAccountFactoryBaseline(
            self,
            request: models.GetAccountFactoryBaselineRequest,
            opts: Dict = None,
    ) -> models.GetAccountFactoryBaselineResponse:
        """
        获取用户基线配置数据
        """
        
        kwargs = {}
        kwargs["action"] = "GetAccountFactoryBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAccountFactoryBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAccountFactoryBaselineItems(
            self,
            request: models.ListAccountFactoryBaselineItemsRequest,
            opts: Dict = None,
    ) -> models.ListAccountFactoryBaselineItemsResponse:
        """
        获取账号工厂系统基线项
        """
        
        kwargs = {}
        kwargs["action"] = "ListAccountFactoryBaselineItems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAccountFactoryBaselineItemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDeployStepTasks(
            self,
            request: models.ListDeployStepTasksRequest,
            opts: Dict = None,
    ) -> models.ListDeployStepTasksResponse:
        """
        获取某个基线项历史应用信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListDeployStepTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDeployStepTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAccountFactoryBaseline(
            self,
            request: models.UpdateAccountFactoryBaselineRequest,
            opts: Dict = None,
    ) -> models.UpdateAccountFactoryBaselineResponse:
        """
        更新用户当前基线项配置，基线配置会覆盖更新为当前配置。新增基线项时需要将新增的基线配置加到现有配置，删除基线项时需要将删除的基线配置从现有配置移除，然后保存最新基线配置。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAccountFactoryBaseline"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAccountFactoryBaselineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)