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
from tencentcloud.tdai.v20250717 import models
from typing import Dict


class TdaiClient(AbstractClient):
    _apiVersion = '2025-07-17'
    _endpoint = 'tdai.tencentcloudapi.com'
    _service = 'tdai'

    async def ContinueAgentWork(
            self,
            request: models.ContinueAgentWorkRequest,
            opts: Dict = None,
    ) -> models.ContinueAgentWorkResponse:
        """
        本接口（ContinueAgentWork）用于重启智能体实例的值守任务，通常在用户需要重启时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "ContinueAgentWork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ContinueAgentWorkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAgentInstance(
            self,
            request: models.CreateAgentInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateAgentInstanceResponse:
        """
        本接口（CreateAgentInstance）用于创建一个智能体实例，通常在用户购买一个智能体实例时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAgentInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAgentInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateChatCompletion(
            self,
            request: models.CreateChatCompletionRequest,
            opts: Dict = None,
    ) -> models.CreateChatCompletionResponse:
        """
        用于创建一次会话的SSE接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateChatCompletion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateChatCompletionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDutyTaskDetail(
            self,
            request: models.DescribeAgentDutyTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDutyTaskDetailResponse:
        """
        查询智能体值守任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDutyTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDutyTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentDutyTasks(
            self,
            request: models.DescribeAgentDutyTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentDutyTasksResponse:
        """
        查询智能体值守任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentDutyTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentDutyTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstance(
            self,
            request: models.DescribeAgentInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstanceResponse:
        """
        本接口（DescribeAgentInstance）用于查询智能体实例详情，通常在用户查询所购买的所有智能体实例详情时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgentInstances(
            self,
            request: models.DescribeAgentInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentInstancesResponse:
        """
        本接口（DescribeAgentInstances）用于查询智能体实例列表，通常在用户查询所购买的所有智能体列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgentInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAgents(
            self,
            request: models.DescribeAgentsRequest,
            opts: Dict = None,
    ) -> models.DescribeAgentsResponse:
        """
        本接口（DescribeAgents）用于查询智能体列表，通常在用户查询所购买的所有智能体列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChatDetail(
            self,
            request: models.DescribeChatDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeChatDetailResponse:
        """
        本接口（DescribeChatDetail）用于查询对话详情，通常在用户查询会话的历史记录时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChatDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChatDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeChats(
            self,
            request: models.DescribeChatsRequest,
            opts: Dict = None,
    ) -> models.DescribeChatsResponse:
        """
        本接口（DescribeChats）用于查询对话列表，通常在用户查询会话列表时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeChats"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeChatsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportUrl(
            self,
            request: models.DescribeReportUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeReportUrlResponse:
        """
        智能体报告地址生成并下载
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateAgentInstance(
            self,
            request: models.IsolateAgentInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateAgentInstanceResponse:
        """
        本接口（IsolateAgentInstance）用于隔离智能体实例，通常在用户需要隔离智能体实例时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateAgentInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateAgentInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAgentInstanceParameters(
            self,
            request: models.ModifyAgentInstanceParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyAgentInstanceParametersResponse:
        """
        本接口（ModifyAgentInstanceParameters）用于修改智能体实例的参数列表，通常在用户需要配置智能体实例时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAgentInstanceParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAgentInstanceParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyChatTitle(
            self,
            request: models.ModifyChatTitleRequest,
            opts: Dict = None,
    ) -> models.ModifyChatTitleResponse:
        """
        本接口（ModifyChatTitle）用于修改会话标题，通常在用户修改会话标题时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyChatTitle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyChatTitleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseAgentWork(
            self,
            request: models.PauseAgentWorkRequest,
            opts: Dict = None,
    ) -> models.PauseAgentWorkResponse:
        """
        本接口（PauseAgentWork）用于暂停智能体实例的值守任务，通常在用户需要暂停时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "PauseAgentWork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseAgentWorkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverAgentInstance(
            self,
            request: models.RecoverAgentInstanceRequest,
            opts: Dict = None,
    ) -> models.RecoverAgentInstanceResponse:
        """
        本接口（RecoverAgentInstance）用于解隔离智能体实例，通常在用户需要解隔离智能体实例时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverAgentInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverAgentInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveChat(
            self,
            request: models.RemoveChatRequest,
            opts: Dict = None,
    ) -> models.RemoveChatResponse:
        """
        本接口（RemoveChat）用于删除会话，通常在用户删除会话时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveChat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveChatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartAgentTask(
            self,
            request: models.StartAgentTaskRequest,
            opts: Dict = None,
    ) -> models.StartAgentTaskResponse:
        """
        该接口用于启动一个智能体的任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartAgentTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartAgentTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateAgentInstance(
            self,
            request: models.TerminateAgentInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateAgentInstanceResponse:
        """
        本接口（TerminateAgentInstance）用于下线智能体实例，通常在用户需要下线智能体实例时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateAgentInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateAgentInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)