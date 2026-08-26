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
from tencentcloud.monitor.v20230616 import models
from typing import Dict


class MonitorClient(AbstractClient):
    _apiVersion = '2023-06-16'
    _endpoint = 'monitor.tencentcloudapi.com'
    _service = 'monitor'

    async def CancelAIWorkbenchChat(
            self,
            request: models.CancelAIWorkbenchChatRequest,
            opts: Dict = None,
    ) -> models.CancelAIWorkbenchChatResponse:
        """
        取消对话执行
        """
        
        kwargs = {}
        kwargs["action"] = "CancelAIWorkbenchChat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelAIWorkbenchChatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIWorkbenchAgent(
            self,
            request: models.CreateAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.CreateAIWorkbenchAgentResponse:
        """
        创建 Agent
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAIWorkbenchTask(
            self,
            request: models.CreateAIWorkbenchTaskRequest,
            opts: Dict = None,
    ) -> models.CreateAIWorkbenchTaskResponse:
        """
        创建任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAIWorkbenchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAIWorkbenchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNoticeContentTmpl(
            self,
            request: models.CreateNoticeContentTmplRequest,
            opts: Dict = None,
    ) -> models.CreateNoticeContentTmplResponse:
        """
        创建自定义通知内容模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNoticeContentTmpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNoticeContentTmplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIWorkbenchAgent(
            self,
            request: models.DeleteAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.DeleteAIWorkbenchAgentResponse:
        """
        删除 Agent
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAIWorkbenchTask(
            self,
            request: models.DeleteAIWorkbenchTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteAIWorkbenchTaskResponse:
        """
        删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAIWorkbenchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAIWorkbenchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNoticeContentTmpls(
            self,
            request: models.DeleteNoticeContentTmplsRequest,
            opts: Dict = None,
    ) -> models.DeleteNoticeContentTmplsResponse:
        """
        删除通知内容模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNoticeContentTmpls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNoticeContentTmplsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchAgent(
            self,
            request: models.DescribeAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchAgentResponse:
        """
        查询 Agent 详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchArtifact(
            self,
            request: models.DescribeAIWorkbenchArtifactRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchArtifactResponse:
        """
        查询制品详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchArtifact"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchArtifactResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchExecution(
            self,
            request: models.DescribeAIWorkbenchExecutionRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchExecutionResponse:
        """
        查询执行详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchExecution"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchExecutionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSREDigitalTwinTaskList(
            self,
            request: models.DescribeAIWorkbenchSREDigitalTwinTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSREDigitalTwinTaskListResponse:
        """
        查询AI工作台SRE数字分身任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSREDigitalTwinTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSREDigitalTwinTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSREDigitalTwinWorkLogDetail(
            self,
            request: models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse:
        """
        查询AI工作台SRE数字分身工作日志详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSREDigitalTwinWorkLogDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSREDigitalTwinWorkLogDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSREDigitalTwinWorkLogList(
            self,
            request: models.DescribeAIWorkbenchSREDigitalTwinWorkLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse:
        """
        查询AI工作台SRE数字分身任务工作日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSREDigitalTwinWorkLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSREDigitalTwinWorkLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSession(
            self,
            request: models.DescribeAIWorkbenchSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSessionResponse:
        """
        查询会话详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAIWorkbenchSkill(
            self,
            request: models.DescribeAIWorkbenchSkillRequest,
            opts: Dict = None,
    ) -> models.DescribeAIWorkbenchSkillResponse:
        """
        查询技能详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAIWorkbenchSkill"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAIWorkbenchSkillResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmNotifyHistories(
            self,
            request: models.DescribeAlarmNotifyHistoriesRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmNotifyHistoriesResponse:
        """
        按需查询告警的通知历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmNotifyHistories"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmNotifyHistoriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNoticeContentTmpl(
            self,
            request: models.DescribeNoticeContentTmplRequest,
            opts: Dict = None,
    ) -> models.DescribeNoticeContentTmplResponse:
        """
        根据查询条件获取自定义通知内容模板，若所有查询条件空，则获取账号下所有模板
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNoticeContentTmpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNoticeContentTmplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetAIWorkbenchArtifactDownloadURL(
            self,
            request: models.GetAIWorkbenchArtifactDownloadURLRequest,
            opts: Dict = None,
    ) -> models.GetAIWorkbenchArtifactDownloadURLResponse:
        """
        获取AI工作台制品的下载地址
        """
        
        kwargs = {}
        kwargs["action"] = "GetAIWorkbenchArtifactDownloadURL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAIWorkbenchArtifactDownloadURLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchAgents(
            self,
            request: models.ListAIWorkbenchAgentsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchAgentsResponse:
        """
        查询 Agent 列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchAgents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchAgentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchArtifacts(
            self,
            request: models.ListAIWorkbenchArtifactsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchArtifactsResponse:
        """
        查询产物列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchArtifacts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchArtifactsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchExecutions(
            self,
            request: models.ListAIWorkbenchExecutionsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchExecutionsResponse:
        """
        查询执行列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchMCPs(
            self,
            request: models.ListAIWorkbenchMCPsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchMCPsResponse:
        """
        查询 MCP 列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchMCPs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchMCPsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchMessages(
            self,
            request: models.ListAIWorkbenchMessagesRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchMessagesResponse:
        """
        查询消息列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchResourceInstances(
            self,
            request: models.ListAIWorkbenchResourceInstancesRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchResourceInstancesResponse:
        """
        列出资源实例
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchResourceInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchResourceInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchResourceMaps(
            self,
            request: models.ListAIWorkbenchResourceMapsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchResourceMapsResponse:
        """
        查询资源地图列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchResourceMaps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchResourceMapsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchSessions(
            self,
            request: models.ListAIWorkbenchSessionsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchSessionsResponse:
        """
        查询会话列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchSkills(
            self,
            request: models.ListAIWorkbenchSkillsRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchSkillsResponse:
        """
        查询技能列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchSkills"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchSkillsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAIWorkbenchTasks(
            self,
            request: models.ListAIWorkbenchTasksRequest,
            opts: Dict = None,
    ) -> models.ListAIWorkbenchTasksResponse:
        """
        查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAIWorkbenchTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAIWorkbenchTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNoticeContentTmpl(
            self,
            request: models.ModifyNoticeContentTmplRequest,
            opts: Dict = None,
    ) -> models.ModifyNoticeContentTmplResponse:
        """
        修改通知内容模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNoticeContentTmpl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNoticeContentTmplResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerAIWorkbenchSREDigitalTwinTask(
            self,
            request: models.TriggerAIWorkbenchSREDigitalTwinTaskRequest,
            opts: Dict = None,
    ) -> models.TriggerAIWorkbenchSREDigitalTwinTaskResponse:
        """
        触发数字分身任务请求
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerAIWorkbenchSREDigitalTwinTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerAIWorkbenchSREDigitalTwinTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerAIWorkbenchTask(
            self,
            request: models.TriggerAIWorkbenchTaskRequest,
            opts: Dict = None,
    ) -> models.TriggerAIWorkbenchTaskResponse:
        """
        手动触发任务
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerAIWorkbenchTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerAIWorkbenchTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAIWorkbenchAgent(
            self,
            request: models.UpdateAIWorkbenchAgentRequest,
            opts: Dict = None,
    ) -> models.UpdateAIWorkbenchAgentResponse:
        """
        更新 Agent
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAIWorkbenchAgent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAIWorkbenchAgentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)