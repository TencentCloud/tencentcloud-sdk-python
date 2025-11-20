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
from tencentcloud.asw.v20200722 import models
from typing import Dict


class AswClient(AbstractClient):
    _apiVersion = '2020-07-22'
    _endpoint = 'asw.tencentcloudapi.com'
    _service = 'asw'

    async def CreateFlowService(
            self,
            request: models.CreateFlowServiceRequest,
            opts: Dict = None,
    ) -> models.CreateFlowServiceResponse:
        """
        该接口用于生成状态机服务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlowService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlowServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExecution(
            self,
            request: models.DescribeExecutionRequest,
            opts: Dict = None,
    ) -> models.DescribeExecutionResponse:
        """
        查询执行详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExecutionHistory(
            self,
            request: models.DescribeExecutionHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeExecutionHistoryResponse:
        """
        一次执行会有很多步骤，经过很多节点，这个接口描述某一次执行的事件的历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExecutionHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExecutionHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExecutions(
            self,
            request: models.DescribeExecutionsRequest,
            opts: Dict = None,
    ) -> models.DescribeExecutionsResponse:
        """
        对状态机的执行历史进行描述.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowServiceDetail(
            self,
            request: models.DescribeFlowServiceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowServiceDetailResponse:
        """
        查询该用户指定状态机下的详情数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowServiceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowServiceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowServices(
            self,
            request: models.DescribeFlowServicesRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowServicesResponse:
        """
        查询指定用户下所有状态机，以列表形式返回
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowServices"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowServicesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFlowService(
            self,
            request: models.ModifyFlowServiceRequest,
            opts: Dict = None,
    ) -> models.ModifyFlowServiceResponse:
        """
        该接口用于修改状态机
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFlowService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFlowServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartExecution(
            self,
            request: models.StartExecutionRequest,
            opts: Dict = None,
    ) -> models.StartExecutionResponse:
        """
        为指定的状态机启动一次执行
        """
        
        kwargs = {}
        kwargs["action"] = "StartExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopExecution(
            self,
            request: models.StopExecutionRequest,
            opts: Dict = None,
    ) -> models.StopExecutionResponse:
        """
        终止某个状态机
        """
        
        kwargs = {}
        kwargs["action"] = "StopExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)