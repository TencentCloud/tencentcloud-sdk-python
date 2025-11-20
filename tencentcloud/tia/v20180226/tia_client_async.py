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
from tencentcloud.tia.v20180226 import models
from typing import Dict


class TiaClient(AbstractClient):
    _apiVersion = '2018-02-26'
    _endpoint = 'tia.tencentcloudapi.com'
    _service = 'tia'

    async def CreateJob(
            self,
            request: models.CreateJobRequest,
            opts: Dict = None,
    ) -> models.CreateJobResponse:
        """
        创建训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModel(
            self,
            request: models.CreateModelRequest,
            opts: Dict = None,
    ) -> models.CreateModelResponse:
        """
        部署模型，用以对外提供服务。有两种部署模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJob(
            self,
            request: models.DeleteJobRequest,
            opts: Dict = None,
    ) -> models.DeleteJobResponse:
        """
        删除训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModel(
            self,
            request: models.DeleteModelRequest,
            opts: Dict = None,
    ) -> models.DeleteModelResponse:
        """
        删除指定的部署模型。模型有两种部署模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJob(
            self,
            request: models.DescribeJobRequest,
            opts: Dict = None,
    ) -> models.DescribeJobResponse:
        """
        获取训练任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModel(
            self,
            request: models.DescribeModelRequest,
            opts: Dict = None,
    ) -> models.DescribeModelResponse:
        """
        描述已经部署的某个模型。而模型部署有两种模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InstallAgent(
            self,
            request: models.InstallAgentRequest,
            opts: Dict = None,
    ) -> models.InstallAgentResponse:
        """
        安装agent
        """
        
        kwargs = {}
        kwargs["action"] = "InstallAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InstallAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListJobs(
            self,
            request: models.ListJobsRequest,
            opts: Dict = None,
    ) -> models.ListJobsResponse:
        """
        列举训练任务
        """
        
        kwargs = {}
        kwargs["action"] = "ListJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListModels(
            self,
            request: models.ListModelsRequest,
            opts: Dict = None,
    ) -> models.ListModelsResponse:
        """
        用以列举已经部署的模型。而部署有两种模式：`无服务器模式` 和 `集群模式`。`无服务器模式` 下，模型文件被部署到无服务器云函数，即 [SCF](https://cloud.tencent.com/product/scf)，用户可以在其控制台上进一步操作。`集群模式` 下，模型文件被部署到 TI-A 的计算集群中。不同部署模式下的模型分开列出。
        """
        
        kwargs = {}
        kwargs["action"] = "ListModels"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListModelsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryLogs(
            self,
            request: models.QueryLogsRequest,
            opts: Dict = None,
    ) -> models.QueryLogsResponse:
        """
        查询 TI-A 训练任务的日志
        """
        
        kwargs = {}
        kwargs["action"] = "QueryLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)