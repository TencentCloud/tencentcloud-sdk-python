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
from tencentcloud.msp.v20180319 import models
from typing import Dict


class MspClient(AbstractClient):
    _apiVersion = '2018-03-19'
    _endpoint = 'msp.tencentcloudapi.com'
    _service = 'msp'

    async def DeregisterMigrationTask(
            self,
            request: models.DeregisterMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeregisterMigrationTaskResponse:
        """
        接口已经废弃不再使用

        取消注册迁移任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationTask(
            self,
            request: models.DescribeMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationTaskResponse:
        """
        获取指定迁移任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListMigrationProject(
            self,
            request: models.ListMigrationProjectRequest,
            opts: Dict = None,
    ) -> models.ListMigrationProjectResponse:
        """
        获取迁移项目名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListMigrationProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListMigrationProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListMigrationTask(
            self,
            request: models.ListMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.ListMigrationTaskResponse:
        """
        获取迁移任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrationTaskBelongToProject(
            self,
            request: models.ModifyMigrationTaskBelongToProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrationTaskBelongToProjectResponse:
        """
        更改迁移任务所属项目
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrationTaskBelongToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrationTaskBelongToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMigrationTaskStatus(
            self,
            request: models.ModifyMigrationTaskStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMigrationTaskStatusResponse:
        """
        更新迁移任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMigrationTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMigrationTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterMigrationTask(
            self,
            request: models.RegisterMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.RegisterMigrationTaskResponse:
        """
        注册迁移任务
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)