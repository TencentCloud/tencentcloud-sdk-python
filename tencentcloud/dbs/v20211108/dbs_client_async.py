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
from tencentcloud.dbs.v20211108 import models
from typing import Dict


class DbsClient(AbstractClient):
    _apiVersion = '2021-11-08'
    _endpoint = 'dbs.tencentcloudapi.com'
    _service = 'dbs'

    async def ConfigureBackupPlan(
            self,
            request: models.ConfigureBackupPlanRequest,
            opts: Dict = None,
    ) -> models.ConfigureBackupPlanResponse:
        """
        本接口（ConfigureBackupPlan）用于配置备份计划。包括配置备份源实例信息、备份对象以及备份策略等。
        """
        
        kwargs = {}
        kwargs["action"] = "ConfigureBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConfigureBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupPlan(
            self,
            request: models.CreateBackupPlanRequest,
            opts: Dict = None,
    ) -> models.CreateBackupPlanResponse:
        """
        该接口用于创建备份计划。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConnectTestJob(
            self,
            request: models.CreateConnectTestJobRequest,
            opts: Dict = None,
    ) -> models.CreateConnectTestJobResponse:
        """
        该接口用于创建连通性检测任务，请在创建备份计划前，通过该接口来检测你的源端实例是否连通性正常。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConnectTestJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConnectTestJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupCheckJob(
            self,
            request: models.DescribeBackupCheckJobRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupCheckJobResponse:
        """
        本接口（DescribeBackupCheckJob）用于查询备份计划预校验任务的结果。仅对于预校验通过的任务，才能启动备份计划。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupPlans(
            self,
            request: models.DescribeBackupPlansRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupPlansResponse:
        """
        本接口（DescribeBackupPlans）用于查询备份计划列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConnectTestResult(
            self,
            request: models.DescribeConnectTestResultRequest,
            opts: Dict = None,
    ) -> models.DescribeConnectTestResultResponse:
        """
        该接口用于查询连通性检测任务的结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConnectTestResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConnectTestResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBackupCheckJob(
            self,
            request: models.StartBackupCheckJobRequest,
            opts: Dict = None,
    ) -> models.StartBackupCheckJobResponse:
        """
        本接口（StartBackupCheckJob）用于创建备份计划预校验任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StartBackupCheckJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBackupCheckJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartBackupPlan(
            self,
            request: models.StartBackupPlanRequest,
            opts: Dict = None,
    ) -> models.StartBackupPlanResponse:
        """
        本接口（StartBackupPlan）用于启动备份计划。调用此接口前，请务必先使用 StartBackupCheckJob 创建备份计划预校验任务，并通过 DescribeBackupCheckJob 接口查询到任务状态为校验通过时，才能启动备份计划。
        """
        
        kwargs = {}
        kwargs["action"] = "StartBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)