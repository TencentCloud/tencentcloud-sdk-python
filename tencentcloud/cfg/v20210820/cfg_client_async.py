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
from tencentcloud.cfg.v20210820 import models
from typing import Dict


class CfgClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'cfg.tencentcloudapi.com'
    _service = 'cfg'

    async def CreateTaskFromAction(
            self,
            request: models.CreateTaskFromActionRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFromActionResponse:
        """
        从动作创建演练
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFromAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFromActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFromMultiAction(
            self,
            request: models.CreateTaskFromMultiActionRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFromMultiActionResponse:
        """
        以多个动作创建演练
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFromMultiAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFromMultiActionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFromTemplate(
            self,
            request: models.CreateTaskFromTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFromTemplateResponse:
        """
        从经验库创建演练
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFromTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFromTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionFieldConfigList(
            self,
            request: models.DescribeActionFieldConfigListRequest,
            opts: Dict = None,
    ) -> models.DescribeActionFieldConfigListResponse:
        """
        根据动作ID获取动作栏位动态配置参数信息，里面包含动作自有和通用两部分参数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionFieldConfigList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionFieldConfigListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeActionLibraryList(
            self,
            request: models.DescribeActionLibraryListRequest,
            opts: Dict = None,
    ) -> models.DescribeActionLibraryListResponse:
        """
        获取混沌演练平台的动作库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeActionLibraryList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeActionLibraryListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeObjectTypeList(
            self,
            request: models.DescribeObjectTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeObjectTypeListResponse:
        """
        查询对象类型列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeObjectTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeObjectTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTask(
            self,
            request: models.DescribeTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResponse:
        """
        查询任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskExecuteLogs(
            self,
            request: models.DescribeTaskExecuteLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskExecuteLogsResponse:
        """
        获取演练过程中的所有日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskExecuteLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskExecuteLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskList(
            self,
            request: models.DescribeTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskListResponse:
        """
        查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskPolicyTriggerLog(
            self,
            request: models.DescribeTaskPolicyTriggerLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskPolicyTriggerLogResponse:
        """
        获取护栏触发日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskPolicyTriggerLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskPolicyTriggerLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplate(
            self,
            request: models.DescribeTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateResponse:
        """
        查询经验库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateList(
            self,
            request: models.DescribeTemplateListRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateListResponse:
        """
        查询经验库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteTask(
            self,
            request: models.ExecuteTaskRequest,
            opts: Dict = None,
    ) -> models.ExecuteTaskResponse:
        """
        执行任务
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ExecuteTaskInstance(
            self,
            request: models.ExecuteTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.ExecuteTaskInstanceResponse:
        """
        触发混沌演练任务的动作，对于实例进行演练操作
        """
        
        kwargs = {}
        kwargs["action"] = "ExecuteTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExecuteTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskRunStatus(
            self,
            request: models.ModifyTaskRunStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskRunStatusResponse:
        """
        修改任务运行状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskRunStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskRunStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerPolicy(
            self,
            request: models.TriggerPolicyRequest,
            opts: Dict = None,
    ) -> models.TriggerPolicyResponse:
        """
        用于触发混沌演练护栏（类型为触发和恢复2种）
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)