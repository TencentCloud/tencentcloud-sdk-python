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
from tencentcloud.tione.v20191022 import models
from typing import Dict


class TioneClient(AbstractClient):
    _apiVersion = '2019-10-22'
    _endpoint = 'tione.tencentcloudapi.com'
    _service = 'tione'

    async def CreateCodeRepository(
            self,
            request: models.CreateCodeRepositoryRequest,
            opts: Dict = None,
    ) -> models.CreateCodeRepositoryResponse:
        """
        创建存储库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotebookInstance(
            self,
            request: models.CreateNotebookInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookInstanceResponse:
        """
        创建Notebook实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebookInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotebookLifecycleScript(
            self,
            request: models.CreateNotebookLifecycleScriptRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookLifecycleScriptResponse:
        """
        创建Notebook生命周期脚本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebookLifecycleScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookLifecycleScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePresignedNotebookInstanceUrl(
            self,
            request: models.CreatePresignedNotebookInstanceUrlRequest,
            opts: Dict = None,
    ) -> models.CreatePresignedNotebookInstanceUrlResponse:
        """
        创建Notebook授权Url
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePresignedNotebookInstanceUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePresignedNotebookInstanceUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrainingJob(
            self,
            request: models.CreateTrainingJobRequest,
            opts: Dict = None,
    ) -> models.CreateTrainingJobResponse:
        """
        创建训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrainingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrainingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeRepository(
            self,
            request: models.DeleteCodeRepositoryRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeRepositoryResponse:
        """
        删除存储库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNotebookInstance(
            self,
            request: models.DeleteNotebookInstanceRequest,
            opts: Dict = None,
    ) -> models.DeleteNotebookInstanceResponse:
        """
        删除notebook实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNotebookInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNotebookInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNotebookLifecycleScript(
            self,
            request: models.DeleteNotebookLifecycleScriptRequest,
            opts: Dict = None,
    ) -> models.DeleteNotebookLifecycleScriptResponse:
        """
        删除Notebook生命周期脚本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNotebookLifecycleScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNotebookLifecycleScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodeRepositories(
            self,
            request: models.DescribeCodeRepositoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeCodeRepositoriesResponse:
        """
        查询存储库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodeRepositories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodeRepositoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodeRepository(
            self,
            request: models.DescribeCodeRepositoryRequest,
            opts: Dict = None,
    ) -> models.DescribeCodeRepositoryResponse:
        """
        查询存储库详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodeRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodeRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookInstance(
            self,
            request: models.DescribeNotebookInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookInstanceResponse:
        """
        查询Notebook实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookInstances(
            self,
            request: models.DescribeNotebookInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookInstancesResponse:
        """
        查询Notebook实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookLifecycleScript(
            self,
            request: models.DescribeNotebookLifecycleScriptRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookLifecycleScriptResponse:
        """
        查看notebook生命周期脚本详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookLifecycleScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookLifecycleScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookLifecycleScripts(
            self,
            request: models.DescribeNotebookLifecycleScriptsRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookLifecycleScriptsResponse:
        """
        查看notebook生命周期脚本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookLifecycleScripts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookLifecycleScriptsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSummary(
            self,
            request: models.DescribeNotebookSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSummaryResponse:
        """
        查询Notebook概览数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingJob(
            self,
            request: models.DescribeTrainingJobRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingJobResponse:
        """
        查询训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrainingJobs(
            self,
            request: models.DescribeTrainingJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeTrainingJobsResponse:
        """
        查询训练任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrainingJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrainingJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartNotebookInstance(
            self,
            request: models.StartNotebookInstanceRequest,
            opts: Dict = None,
    ) -> models.StartNotebookInstanceResponse:
        """
        启动Notebook实例
        """
        
        kwargs = {}
        kwargs["action"] = "StartNotebookInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartNotebookInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopNotebookInstance(
            self,
            request: models.StopNotebookInstanceRequest,
            opts: Dict = None,
    ) -> models.StopNotebookInstanceResponse:
        """
        停止Notebook实例
        """
        
        kwargs = {}
        kwargs["action"] = "StopNotebookInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopNotebookInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopTrainingJob(
            self,
            request: models.StopTrainingJobRequest,
            opts: Dict = None,
    ) -> models.StopTrainingJobResponse:
        """
        停止训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopTrainingJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopTrainingJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCodeRepository(
            self,
            request: models.UpdateCodeRepositoryRequest,
            opts: Dict = None,
    ) -> models.UpdateCodeRepositoryResponse:
        """
        更新存储库
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCodeRepository"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCodeRepositoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNotebookInstance(
            self,
            request: models.UpdateNotebookInstanceRequest,
            opts: Dict = None,
    ) -> models.UpdateNotebookInstanceResponse:
        """
        更新Notebook实例
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNotebookInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNotebookInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)