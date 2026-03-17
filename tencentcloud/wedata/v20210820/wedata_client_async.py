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
from tencentcloud.wedata.v20210820 import models
from typing import Dict


class WedataClient(AbstractClient):
    _apiVersion = '2021-08-20'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'

    async def AddProjectUserRole(
            self,
            request: models.AddProjectUserRoleRequest,
            opts: Dict = None,
    ) -> models.AddProjectUserRoleResponse:
        """
        添加项目用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "AddProjectUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddProjectUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateIntegrationTaskAlarms(
            self,
            request: models.BatchCreateIntegrationTaskAlarmsRequest,
            opts: Dict = None,
    ) -> models.BatchCreateIntegrationTaskAlarmsResponse:
        """
        批量创建任务告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateIntegrationTaskAlarms"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateIntegrationTaskAlarmsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchCreateTaskVersionAsync(
            self,
            request: models.BatchCreateTaskVersionAsyncRequest,
            opts: Dict = None,
    ) -> models.BatchCreateTaskVersionAsyncResponse:
        """
        异步批量创建任务版本
        """
        
        kwargs = {}
        kwargs["action"] = "BatchCreateTaskVersionAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchCreateTaskVersionAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteIntegrationTasks(
            self,
            request: models.BatchDeleteIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteIntegrationTasksResponse:
        """
        批量删除集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeleteOpsTasks(
            self,
            request: models.BatchDeleteOpsTasksRequest,
            opts: Dict = None,
    ) -> models.BatchDeleteOpsTasksResponse:
        """
        任务运维-批量删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeleteOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeleteOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchForceSuccessIntegrationTaskInstances(
            self,
            request: models.BatchForceSuccessIntegrationTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.BatchForceSuccessIntegrationTaskInstancesResponse:
        """
        批量置成功集成任务实例
        """
        
        kwargs = {}
        kwargs["action"] = "BatchForceSuccessIntegrationTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchForceSuccessIntegrationTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchKillIntegrationTaskInstances(
            self,
            request: models.BatchKillIntegrationTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.BatchKillIntegrationTaskInstancesResponse:
        """
        批量终止集成任务实例
        """
        
        kwargs = {}
        kwargs["action"] = "BatchKillIntegrationTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchKillIntegrationTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchMakeUpIntegrationTasks(
            self,
            request: models.BatchMakeUpIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchMakeUpIntegrationTasksResponse:
        """
        对集成离线任务执行批量补数据操作
        """
        
        kwargs = {}
        kwargs["action"] = "BatchMakeUpIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchMakeUpIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyOpsOwners(
            self,
            request: models.BatchModifyOpsOwnersRequest,
            opts: Dict = None,
    ) -> models.BatchModifyOpsOwnersResponse:
        """
        批量修改任务责任人
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyOpsOwners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyOpsOwnersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRerunIntegrationTaskInstances(
            self,
            request: models.BatchRerunIntegrationTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.BatchRerunIntegrationTaskInstancesResponse:
        """
        批量重跑集成任务实例
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRerunIntegrationTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRerunIntegrationTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchResumeIntegrationTasks(
            self,
            request: models.BatchResumeIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchResumeIntegrationTasksResponse:
        """
        批量继续执行集成实时任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchResumeIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchResumeIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRunOpsTask(
            self,
            request: models.BatchRunOpsTaskRequest,
            opts: Dict = None,
    ) -> models.BatchRunOpsTaskResponse:
        """
        任务运维-任务列表 批量启动
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRunOpsTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRunOpsTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStartIntegrationTasks(
            self,
            request: models.BatchStartIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchStartIntegrationTasksResponse:
        """
        批量运行集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStartIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStartIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopIntegrationTasks(
            self,
            request: models.BatchStopIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchStopIntegrationTasksResponse:
        """
        批量停止集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopOpsTasks(
            self,
            request: models.BatchStopOpsTasksRequest,
            opts: Dict = None,
    ) -> models.BatchStopOpsTasksResponse:
        """
        仅对任务状态为”调度中“和”已暂停“有效，对所选任务的任务实例进行终止，并停止调度
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchStopWorkflowsByIds(
            self,
            request: models.BatchStopWorkflowsByIdsRequest,
            opts: Dict = None,
    ) -> models.BatchStopWorkflowsByIdsResponse:
        """
        批量停止工作流
        """
        
        kwargs = {}
        kwargs["action"] = "BatchStopWorkflowsByIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchStopWorkflowsByIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchSuspendIntegrationTasks(
            self,
            request: models.BatchSuspendIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchSuspendIntegrationTasksResponse:
        """
        批量暂停集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "BatchSuspendIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchSuspendIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchUpdateIntegrationTasks(
            self,
            request: models.BatchUpdateIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.BatchUpdateIntegrationTasksResponse:
        """
        批量更新集成任务（暂时仅支持批量更新责任人）
        """
        
        kwargs = {}
        kwargs["action"] = "BatchUpdateIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchUpdateIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindProjectExecutorResource(
            self,
            request: models.BindProjectExecutorResourceRequest,
            opts: Dict = None,
    ) -> models.BindProjectExecutorResourceResponse:
        """
        商业化版本：执行资源组-资源包绑定项目
        """
        
        kwargs = {}
        kwargs["action"] = "BindProjectExecutorResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindProjectExecutorResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAlarmRegularNameExist(
            self,
            request: models.CheckAlarmRegularNameExistRequest,
            opts: Dict = None,
    ) -> models.CheckAlarmRegularNameExistResponse:
        """
        判断告警规则重名
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAlarmRegularNameExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAlarmRegularNameExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIntegrationNodeNameExists(
            self,
            request: models.CheckIntegrationNodeNameExistsRequest,
            opts: Dict = None,
    ) -> models.CheckIntegrationNodeNameExistsResponse:
        """
        判断集成节点名称是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIntegrationNodeNameExists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIntegrationNodeNameExistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckIntegrationTaskNameExists(
            self,
            request: models.CheckIntegrationTaskNameExistsRequest,
            opts: Dict = None,
    ) -> models.CheckIntegrationTaskNameExistsResponse:
        """
        判断集成任务名称是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "CheckIntegrationTaskNameExists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckIntegrationTaskNameExistsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckTaskNameExist(
            self,
            request: models.CheckTaskNameExistRequest,
            opts: Dict = None,
    ) -> models.CheckTaskNameExistResponse:
        """
        离线任务重名校验
        """
        
        kwargs = {}
        kwargs["action"] = "CheckTaskNameExist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckTaskNameExistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitIntegrationTask(
            self,
            request: models.CommitIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.CommitIntegrationTaskResponse:
        """
        提交集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "CommitIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CommitRuleGroupTask(
            self,
            request: models.CommitRuleGroupTaskRequest,
            opts: Dict = None,
    ) -> models.CommitRuleGroupTaskResponse:
        """
        提交规则组运行任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "CommitRuleGroupTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CommitRuleGroupTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CountOpsInstanceState(
            self,
            request: models.CountOpsInstanceStateRequest,
            opts: Dict = None,
    ) -> models.CountOpsInstanceStateResponse:
        """
        统计任务实例状态
        """
        
        kwargs = {}
        kwargs["action"] = "CountOpsInstanceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CountOpsInstanceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBaseProject(
            self,
            request: models.CreateBaseProjectRequest,
            opts: Dict = None,
    ) -> models.CreateBaseProjectResponse:
        """
        创建项目 仅项目本身，不包含集群等信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBaseProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBaseProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodeTemplate(
            self,
            request: models.CreateCodeTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateCodeTemplateResponse:
        """
        创建代码模版
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodeTemplateVersion(
            self,
            request: models.CreateCodeTemplateVersionRequest,
            opts: Dict = None,
    ) -> models.CreateCodeTemplateVersionResponse:
        """
        提交代码模版
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeTemplateVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeTemplateVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomFunction(
            self,
            request: models.CreateCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.CreateCustomFunctionResponse:
        """
        创建用户自定义函数
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataModel(
            self,
            request: models.CreateDataModelRequest,
            opts: Dict = None,
    ) -> models.CreateDataModelResponse:
        """
        创建数据建模，提供给云应用使用，实现“Wedata数据建模”的下单发货
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataSource(
            self,
            request: models.CreateDataSourceRequest,
            opts: Dict = None,
    ) -> models.CreateDataSourceResponse:
        """
        创建数据源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDsFolder(
            self,
            request: models.CreateDsFolderRequest,
            opts: Dict = None,
    ) -> models.CreateDsFolderResponse:
        """
        编排空间-创建文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDsFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDsFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHiveTable(
            self,
            request: models.CreateHiveTableRequest,
            opts: Dict = None,
    ) -> models.CreateHiveTableResponse:
        """
        建hive表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHiveTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHiveTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHiveTableByDDL(
            self,
            request: models.CreateHiveTableByDDLRequest,
            opts: Dict = None,
    ) -> models.CreateHiveTableByDDLResponse:
        """
        创建hive表，返回表名称
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHiveTableByDDL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHiveTableByDDLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntegrationNode(
            self,
            request: models.CreateIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.CreateIntegrationNodeResponse:
        """
        创建集成节点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIntegrationTask(
            self,
            request: models.CreateIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateIntegrationTaskResponse:
        """
        创建集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOfflineTask(
            self,
            request: models.CreateOfflineTaskRequest,
            opts: Dict = None,
    ) -> models.CreateOfflineTaskResponse:
        """
        创建离线任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOfflineTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOfflineTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpsMakePlan(
            self,
            request: models.CreateOpsMakePlanRequest,
            opts: Dict = None,
    ) -> models.CreateOpsMakePlanResponse:
        """
        批量补数据（创建补录任务）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpsMakePlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpsMakePlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRule(
            self,
            request: models.CreateRuleRequest,
            opts: Dict = None,
    ) -> models.CreateRuleResponse:
        """
        创建质量规则接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRuleTemplate(
            self,
            request: models.CreateRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateRuleTemplateResponse:
        """
        创建规则模板
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        创建任务。本接口已废弃，请使用接口CreateTaskNew。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskAlarmRegular(
            self,
            request: models.CreateTaskAlarmRegularRequest,
            opts: Dict = None,
    ) -> models.CreateTaskAlarmRegularResponse:
        """
        创建任务告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskAlarmRegular"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskAlarmRegularResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskFolder(
            self,
            request: models.CreateTaskFolderRequest,
            opts: Dict = None,
    ) -> models.CreateTaskFolderResponse:
        """
        编排空间-工作流-创建任务文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskNew(
            self,
            request: models.CreateTaskNewRequest,
            opts: Dict = None,
    ) -> models.CreateTaskNewResponse:
        """
        聚合创建任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTaskVersionDs(
            self,
            request: models.CreateTaskVersionDsRequest,
            opts: Dict = None,
    ) -> models.CreateTaskVersionDsResponse:
        """
        提交任务版本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTaskVersionDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskVersionDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflowDs(
            self,
            request: models.CreateWorkflowDsRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowDsResponse:
        """
        创建工作流
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflowDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DagInstances(
            self,
            request: models.DagInstancesRequest,
            opts: Dict = None,
    ) -> models.DagInstancesResponse:
        """
        拉取dag实例
        """
        
        kwargs = {}
        kwargs["action"] = "DagInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DagInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeTemplate(
            self,
            request: models.DeleteCodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeTemplateResponse:
        """
        删除代码模版
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomFunction(
            self,
            request: models.DeleteCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomFunctionResponse:
        """
        删除用户自定义函数
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataModel(
            self,
            request: models.DeleteDataModelRequest,
            opts: Dict = None,
    ) -> models.DeleteDataModelResponse:
        """
        销毁数据建模，提供给云应用使用，实现“Wedata数据建模”的销毁
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataModel"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataModelResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataSources(
            self,
            request: models.DeleteDataSourcesRequest,
            opts: Dict = None,
    ) -> models.DeleteDataSourcesResponse:
        """
        删除数据源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDsFolder(
            self,
            request: models.DeleteDsFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteDsFolderResponse:
        """
        编排空间-删除文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDsFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDsFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFile(
            self,
            request: models.DeleteFileRequest,
            opts: Dict = None,
    ) -> models.DeleteFileResponse:
        """
        删除文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFilePath(
            self,
            request: models.DeleteFilePathRequest,
            opts: Dict = None,
    ) -> models.DeleteFilePathResponse:
        """
        开发空间-批量删除目录和文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFilePath"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFilePathResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIntegrationNode(
            self,
            request: models.DeleteIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.DeleteIntegrationNodeResponse:
        """
        删除集成节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIntegrationTask(
            self,
            request: models.DeleteIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteIntegrationTaskResponse:
        """
        删除集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLink(
            self,
            request: models.DeleteLinkRequest,
            opts: Dict = None,
    ) -> models.DeleteLinkResponse:
        """
        删除任务连接
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLink"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLinkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOfflineTask(
            self,
            request: models.DeleteOfflineTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteOfflineTaskResponse:
        """
        删除任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOfflineTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOfflineTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectParamDs(
            self,
            request: models.DeleteProjectParamDsRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectParamDsResponse:
        """
        删除项目参数
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectParamDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectParamDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectUsers(
            self,
            request: models.DeleteProjectUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectUsersResponse:
        """
        删除项目用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResource(
            self,
            request: models.DeleteResourceRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceResponse:
        """
        资源管理删除资源。本接口已废弃，请使用接口DeleteResourceFile。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceFile(
            self,
            request: models.DeleteResourceFileRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFileResponse:
        """
        资源管理-删除资源文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceFiles(
            self,
            request: models.DeleteResourceFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFilesResponse:
        """
        资源管理-批量删除资源文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRule(
            self,
            request: models.DeleteRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleResponse:
        """
        删除质量规则接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRuleTemplate(
            self,
            request: models.DeleteRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteRuleTemplateResponse:
        """
        删除规则模板
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskAlarmRegular(
            self,
            request: models.DeleteTaskAlarmRegularRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskAlarmRegularResponse:
        """
        删除任务告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskAlarmRegular"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskAlarmRegularResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskDs(
            self,
            request: models.DeleteTaskDsRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskDsResponse:
        """
        删除编排空间任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTaskLineage(
            self,
            request: models.DeleteTaskLineageRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskLineageResponse:
        """
        删除任务血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTaskLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflowById(
            self,
            request: models.DeleteWorkflowByIdRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowByIdResponse:
        """
        通过工作流Id删除工作流
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflowById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmEvents(
            self,
            request: models.DescribeAlarmEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmEventsResponse:
        """
        告警事件列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAlarmReceiver(
            self,
            request: models.DescribeAlarmReceiverRequest,
            opts: Dict = None,
    ) -> models.DescribeAlarmReceiverResponse:
        """
        告警接收人详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAlarmReceiver"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAlarmReceiverResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAllByFolderNew(
            self,
            request: models.DescribeAllByFolderNewRequest,
            opts: Dict = None,
    ) -> models.DescribeAllByFolderNewResponse:
        """
        查询父目录下所有子文件夹+工作流
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAllByFolderNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAllByFolderNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApproveList(
            self,
            request: models.DescribeApproveListRequest,
            opts: Dict = None,
    ) -> models.DescribeApproveListResponse:
        """
        获取待审批列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApproveList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApproveListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApproveTypeList(
            self,
            request: models.DescribeApproveTypeListRequest,
            opts: Dict = None,
    ) -> models.DescribeApproveTypeListResponse:
        """
        获取审批分类列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApproveTypeList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApproveTypeListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseBizCatalogs(
            self,
            request: models.DescribeBaseBizCatalogsRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseBizCatalogsResponse:
        """
        数据地图-信息配置 数据类目列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseBizCatalogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseBizCatalogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBatchOperateTask(
            self,
            request: models.DescribeBatchOperateTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeBatchOperateTaskResponse:
        """
        批量操作页面获取任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBatchOperateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBatchOperateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCodeTemplateDetail(
            self,
            request: models.DescribeCodeTemplateDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCodeTemplateDetailResponse:
        """
        查询代码模版具体详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCodeTemplateDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCodeTemplateDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeColumnLineage(
            self,
            request: models.DescribeColumnLineageRequest,
            opts: Dict = None,
    ) -> models.DescribeColumnLineageResponse:
        """
        列出字段血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeColumnLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeColumnLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeColumnsMeta(
            self,
            request: models.DescribeColumnsMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeColumnsMetaResponse:
        """
        查询表的所有列元数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeColumnsMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeColumnsMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataAssets(
            self,
            request: models.DescribeDataAssetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataAssetsResponse:
        """
        查询数据资产列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataAssets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataAssetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataCheckStat(
            self,
            request: models.DescribeDataCheckStatRequest,
            opts: Dict = None,
    ) -> models.DescribeDataCheckStatResponse:
        """
        数据质量的概览页面数据监测情况接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataCheckStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataCheckStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataServicePublishedApiDetail(
            self,
            request: models.DescribeDataServicePublishedApiDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDataServicePublishedApiDetailResponse:
        """
        查询数据服务API的发布态信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataServicePublishedApiDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataServicePublishedApiDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataServicePublishedApiList(
            self,
            request: models.DescribeDataServicePublishedApiListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataServicePublishedApiListResponse:
        """
        获取数据服务API的发布态信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataServicePublishedApiList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataServicePublishedApiListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSourceInfoList(
            self,
            request: models.DescribeDataSourceInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceInfoListResponse:
        """
        获取数据源信息-数据源分页列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSourceInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataSourceList(
            self,
            request: models.DescribeDataSourceListRequest,
            opts: Dict = None,
    ) -> models.DescribeDataSourceListResponse:
        """
        数据源详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataSourceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataSourceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseByName(
            self,
            request: models.DescribeDatabaseByNameRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseByNameResponse:
        """
        根据数据库名称和数据源id获取数据库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseByName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseByNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseInfoList(
            self,
            request: models.DescribeDatabaseInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseInfoListResponse:
        """
        获取数据库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseMeta(
            self,
            request: models.DescribeDatabaseMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseMetaResponse:
        """
        根据数据库Id查询数据库元数据，带有数据源和项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseMetas(
            self,
            request: models.DescribeDatabaseMetasRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseMetasResponse:
        """
        查询数据库列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseMetas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseMetasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatasource(
            self,
            request: models.DescribeDatasourceRequest,
            opts: Dict = None,
    ) -> models.DescribeDatasourceResponse:
        """
        数据源详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatasource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatasourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDependOpsTasks(
            self,
            request: models.DescribeDependOpsTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeDependOpsTasksResponse:
        """
        根据层级查找上/下游任务节点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDependOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDependOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDependTaskLists(
            self,
            request: models.DescribeDependTaskListsRequest,
            opts: Dict = None,
    ) -> models.DescribeDependTaskListsResponse:
        """
        通过taskIds查询task详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDependTaskLists"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDependTaskListsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDimensionScore(
            self,
            request: models.DescribeDimensionScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeDimensionScoreResponse:
        """
        质量报告-查询质量评分
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDimensionScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDimensionScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDsFolderTree(
            self,
            request: models.DescribeDsFolderTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeDsFolderTreeResponse:
        """
        查询目录树
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDsFolderTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDsFolderTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDsParentFolderTree(
            self,
            request: models.DescribeDsParentFolderTreeRequest,
            opts: Dict = None,
    ) -> models.DescribeDsParentFolderTreeResponse:
        """
        查询父目录树，用于工作流、任务定位
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDsParentFolderTree"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDsParentFolderTreeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDsTaskVersionInfo(
            self,
            request: models.DescribeDsTaskVersionInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDsTaskVersionInfoResponse:
        """
        查看任务版本详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDsTaskVersionInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDsTaskVersionInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDsTaskVersionList(
            self,
            request: models.DescribeDsTaskVersionListRequest,
            opts: Dict = None,
    ) -> models.DescribeDsTaskVersionListResponse:
        """
        拉取任务版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDsTaskVersionList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDsTaskVersionListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDutyScheduleDetails(
            self,
            request: models.DescribeDutyScheduleDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeDutyScheduleDetailsResponse:
        """
        获取值班日历
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDutyScheduleDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDutyScheduleDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDutyScheduleList(
            self,
            request: models.DescribeDutyScheduleListRequest,
            opts: Dict = None,
    ) -> models.DescribeDutyScheduleListResponse:
        """
        获取值班表列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDutyScheduleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDutyScheduleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEvent(
            self,
            request: models.DescribeEventRequest,
            opts: Dict = None,
    ) -> models.DescribeEventResponse:
        """
        根据项目ID和事件名称查看事件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventCases(
            self,
            request: models.DescribeEventCasesRequest,
            opts: Dict = None,
    ) -> models.DescribeEventCasesResponse:
        """
        根据条件查找事件实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventCases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventCasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEventConsumeTasks(
            self,
            request: models.DescribeEventConsumeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeEventConsumeTasksResponse:
        """
        查看事件实例的消费任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEventConsumeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEventConsumeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExecStrategy(
            self,
            request: models.DescribeExecStrategyRequest,
            opts: Dict = None,
    ) -> models.DescribeExecStrategyResponse:
        """
        查询规则组执行策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExecStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExecStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeExecutorGroupMetric(
            self,
            request: models.DescribeExecutorGroupMetricRequest,
            opts: Dict = None,
    ) -> models.DescribeExecutorGroupMetricResponse:
        """
        商业化版本：根据id查询执行资源组指标
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeExecutorGroupMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeExecutorGroupMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFieldBasicInfo(
            self,
            request: models.DescribeFieldBasicInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeFieldBasicInfoResponse:
        """
        元数据模型-字段基础信息查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFieldBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFieldBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFolderWorkflowList(
            self,
            request: models.DescribeFolderWorkflowListRequest,
            opts: Dict = None,
    ) -> models.DescribeFolderWorkflowListResponse:
        """
        根据项目id 获取项目下所有工作流列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFolderWorkflowList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFolderWorkflowListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFormVersionParam(
            self,
            request: models.DescribeFormVersionParamRequest,
            opts: Dict = None,
    ) -> models.DescribeFormVersionParamResponse:
        """
        查询模版关联的任务和可填充参数，为下一步代码模版提交做准备
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFormVersionParam"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFormVersionParamResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionKinds(
            self,
            request: models.DescribeFunctionKindsRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionKindsResponse:
        """
        查询函数分类
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionKinds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionKindsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFunctionTypes(
            self,
            request: models.DescribeFunctionTypesRequest,
            opts: Dict = None,
    ) -> models.DescribeFunctionTypesResponse:
        """
        查询函数类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFunctionTypes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFunctionTypesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceByCycle(
            self,
            request: models.DescribeInstanceByCycleRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceByCycleResponse:
        """
        根据周期类型查询所有实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceByCycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceByCycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDetailInfo(
            self,
            request: models.DescribeInstanceDetailInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDetailInfoResponse:
        """
        实例详情页，返回某个实例所有生命周期信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDetailInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDetailInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLastLog(
            self,
            request: models.DescribeInstanceLastLogRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLastLogResponse:
        """
        日志获取详情页面
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLastLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLastLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLog(
            self,
            request: models.DescribeInstanceLogRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogResponse:
        """
        获取实例运行日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogDetail(
            self,
            request: models.DescribeInstanceLogDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogDetailResponse:
        """
        获取具体实例相关日志信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogFile(
            self,
            request: models.DescribeInstanceLogFileRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogFileResponse:
        """
        下载日志文件，返回日志下载URL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceLogList(
            self,
            request: models.DescribeInstanceLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceLogListResponse:
        """
        离线任务实例运行日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationNode(
            self,
            request: models.DescribeIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationNodeResponse:
        """
        查询集成节点
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatistics(
            self,
            request: models.DescribeIntegrationStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsResponse:
        """
        数据集成大屏概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsInstanceTrend(
            self,
            request: models.DescribeIntegrationStatisticsInstanceTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsInstanceTrendResponse:
        """
        数据集成大屏实例状态统计趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsInstanceTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsInstanceTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsRecordsTrend(
            self,
            request: models.DescribeIntegrationStatisticsRecordsTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsRecordsTrendResponse:
        """
        数据集成大屏同步条数统计趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsRecordsTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsRecordsTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsTaskStatus(
            self,
            request: models.DescribeIntegrationStatisticsTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsTaskStatusResponse:
        """
        数据集成大屏任务状态分布统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationStatisticsTaskStatusTrend(
            self,
            request: models.DescribeIntegrationStatisticsTaskStatusTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationStatisticsTaskStatusTrendResponse:
        """
        数据集成大屏任务状态统计趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationStatisticsTaskStatusTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationStatisticsTaskStatusTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationTask(
            self,
            request: models.DescribeIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationTaskResponse:
        """
        查询集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationTasks(
            self,
            request: models.DescribeIntegrationTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationTasksResponse:
        """
        查询集成任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIntegrationVersionNodesInfo(
            self,
            request: models.DescribeIntegrationVersionNodesInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeIntegrationVersionNodesInfoResponse:
        """
        查询集成任务版本节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIntegrationVersionNodesInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIntegrationVersionNodesInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLineageColumns(
            self,
            request: models.DescribeLineageColumnsRequest,
            opts: Dict = None,
    ) -> models.DescribeLineageColumnsResponse:
        """
        列出血缘中心字段信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLineageColumns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLineageColumnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLineageInfo(
            self,
            request: models.DescribeLineageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLineageInfoResponse:
        """
        通用血缘查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLineageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLineageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeManualTriggerRecordPage(
            self,
            request: models.DescribeManualTriggerRecordPageRequest,
            opts: Dict = None,
    ) -> models.DescribeManualTriggerRecordPageResponse:
        """
        查询手动任务触发记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeManualTriggerRecordPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeManualTriggerRecordPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOfflineTaskToken(
            self,
            request: models.DescribeOfflineTaskTokenRequest,
            opts: Dict = None,
    ) -> models.DescribeOfflineTaskTokenResponse:
        """
        获取离线任务长连接Token
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOfflineTaskToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOfflineTaskTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOperateOpsTasks(
            self,
            request: models.DescribeOperateOpsTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeOperateOpsTasksResponse:
        """
        任务运维列表组合条件查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOperateOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOperateOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsInstanceLogList(
            self,
            request: models.DescribeOpsInstanceLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsInstanceLogListResponse:
        """
        实例运维-获取实例日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsInstanceLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsInstanceLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsMakePlanInstances(
            self,
            request: models.DescribeOpsMakePlanInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsMakePlanInstancesResponse:
        """
        根据补录计划和补录任务获取补录实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsMakePlanInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsMakePlanInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsMakePlanTasks(
            self,
            request: models.DescribeOpsMakePlanTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsMakePlanTasksResponse:
        """
        查看补录计划任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsMakePlanTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsMakePlanTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsMakePlans(
            self,
            request: models.DescribeOpsMakePlansRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsMakePlansResponse:
        """
        根据条件分页查询补录计划
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsMakePlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsMakePlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOpsWorkflows(
            self,
            request: models.DescribeOpsWorkflowsRequest,
            opts: Dict = None,
    ) -> models.DescribeOpsWorkflowsResponse:
        """
        查询用户生产工作流列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOpsWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOpsWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOrganizationalFunctions(
            self,
            request: models.DescribeOrganizationalFunctionsRequest,
            opts: Dict = None,
    ) -> models.DescribeOrganizationalFunctionsResponse:
        """
        查询全量函数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOrganizationalFunctions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOrganizationalFunctionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeParentTask(
            self,
            request: models.DescribeParentTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeParentTaskResponse:
        """
        查询任务父依赖
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeParentTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeParentTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePendingSubmitTaskList(
            self,
            request: models.DescribePendingSubmitTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribePendingSubmitTaskListResponse:
        """
        获取待提交任务预提交校验信息（注意：工作流编号或者任务编号列表，必须填一项）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePendingSubmitTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePendingSubmitTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProject(
            self,
            request: models.DescribeProjectRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectResponse:
        """
        获取项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectUsers(
            self,
            request: models.DescribeProjectUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectUsersResponse:
        """
        获取项目下的用户，分页返回
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityScore(
            self,
            request: models.DescribeQualityScoreRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityScoreResponse:
        """
        质量报告-质量评分
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityScore"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityScoreResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQualityScoreTrend(
            self,
            request: models.DescribeQualityScoreTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeQualityScoreTrendResponse:
        """
        质量报告-质量分周期趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQualityScoreTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQualityScoreTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealTimeTaskInstanceNodeInfo(
            self,
            request: models.DescribeRealTimeTaskInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeRealTimeTaskInstanceNodeInfoResponse:
        """
        查询实时任务实例节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealTimeTaskInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealTimeTaskInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealTimeTaskMetricOverview(
            self,
            request: models.DescribeRealTimeTaskMetricOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeRealTimeTaskMetricOverviewResponse:
        """
        实时任务运行指标概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealTimeTaskMetricOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealTimeTaskMetricOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealTimeTaskSpeed(
            self,
            request: models.DescribeRealTimeTaskSpeedRequest,
            opts: Dict = None,
    ) -> models.DescribeRealTimeTaskSpeedResponse:
        """
        实时任务同步速度趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealTimeTaskSpeed"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealTimeTaskSpeedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealViewDatabasePage(
            self,
            request: models.DescribeRealViewDatabasePageRequest,
            opts: Dict = None,
    ) -> models.DescribeRealViewDatabasePageResponse:
        """
        离线通过表名称获取表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealViewDatabasePage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealViewDatabasePageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRealViewSchemaPage(
            self,
            request: models.DescribeRealViewSchemaPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRealViewSchemaPageResponse:
        """
        数据集成分页获取数据库SCHEMA信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRealViewSchemaPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRealViewSchemaPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRelatedTasksByTaskId(
            self,
            request: models.DescribeRelatedTasksByTaskIdRequest,
            opts: Dict = None,
    ) -> models.DescribeRelatedTasksByTaskIdResponse:
        """
        根据任务ID分页查询任务绑定监听的事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRelatedTasksByTaskId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRelatedTasksByTaskIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportTaskDetail(
            self,
            request: models.DescribeReportTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeReportTaskDetailResponse:
        """
        查询上报任务详情，注意：任务执行完后，任务详情上报存在10分钟的延迟，使用接口查询任务详情时需等待任务运行完10分钟后查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReportTaskList(
            self,
            request: models.DescribeReportTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeReportTaskListResponse:
        """
        查询上报任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReportTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReportTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceManagePathTrees(
            self,
            request: models.DescribeResourceManagePathTreesRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceManagePathTreesResponse:
        """
        获取资源管理目录树
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceManagePathTrees"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceManagePathTreesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoleList(
            self,
            request: models.DescribeRoleListRequest,
            opts: Dict = None,
    ) -> models.DescribeRoleListResponse:
        """
        获取角色列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoleList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoleListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRule(
            self,
            request: models.DescribeRuleRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleResponse:
        """
        查询规则详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleDimStat(
            self,
            request: models.DescribeRuleDimStatRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleDimStatResponse:
        """
        数据质量概览页面触发维度分布统计接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleDimStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleDimStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecDetail(
            self,
            request: models.DescribeRuleExecDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecDetailResponse:
        """
        查询规则执行结果详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecLog(
            self,
            request: models.DescribeRuleExecLogRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecLogResponse:
        """
        规则执行日志查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecResults(
            self,
            request: models.DescribeRuleExecResultsRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecResultsResponse:
        """
        规则执行结果列表查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecResults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecResultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleExecStat(
            self,
            request: models.DescribeRuleExecStatRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleExecStatResponse:
        """
        数据质量概览页面规则运行情况接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleExecStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleExecStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroup(
            self,
            request: models.DescribeRuleGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupResponse:
        """
        查询规则组详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupExecResultsByPage(
            self,
            request: models.DescribeRuleGroupExecResultsByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupExecResultsByPageResponse:
        """
        规则组执行结果分页查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupExecResultsByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupExecResultsByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupSubscription(
            self,
            request: models.DescribeRuleGroupSubscriptionRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupSubscriptionResponse:
        """
        查询规则组订阅信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupTable(
            self,
            request: models.DescribeRuleGroupTableRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupTableResponse:
        """
        查询表绑定执行规则组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleGroupsByPage(
            self,
            request: models.DescribeRuleGroupsByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleGroupsByPageResponse:
        """
        【过滤条件】
        {表名称TableName,支持模糊匹配}       {表负责人TableOwnerName,支持模糊匹配}      {监控方式MonitorTypes，1.未配置 2.关联生产调度 3.离线周期检测,支持多选}  {订阅人ReceiverUin}
        【必要字段】
        {数据来源DatasourceId}
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleGroupsByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleGroupsByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleTemplate(
            self,
            request: models.DescribeRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleTemplateResponse:
        """
        查询模板详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleTemplates(
            self,
            request: models.DescribeRuleTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleTemplatesResponse:
        """
        查询规则模板列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRuleTemplatesByPage(
            self,
            request: models.DescribeRuleTemplatesByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRuleTemplatesByPageResponse:
        """
        【过滤条件】 {模板名称Name,支持模糊匹配} {模板类型type，1.系统模板 2.自定义模板} {质量检测维度QualityDims, 1.准确性 2.唯一性 3.完整性 4.一致性 5.及时性 6.有效性} 【排序字段】 { 引用数排序类型CitationOrderType，根据引用数量排序 ASC DESC}
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRuleTemplatesByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRuleTemplatesByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRules(
            self,
            request: models.DescribeRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesResponse:
        """
        查询质量规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRulesByPage(
            self,
            request: models.DescribeRulesByPageRequest,
            opts: Dict = None,
    ) -> models.DescribeRulesByPageResponse:
        """
        分页查询质量规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRulesByPage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRulesByPageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScheduleInstances(
            self,
            request: models.DescribeScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduleInstancesResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerInstanceStatus(
            self,
            request: models.DescribeSchedulerInstanceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerInstanceStatusResponse:
        """
        运维大屏-实例状态分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerInstanceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerInstanceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerRunTimeInstanceCntByStatus(
            self,
            request: models.DescribeSchedulerRunTimeInstanceCntByStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerRunTimeInstanceCntByStatusResponse:
        """
        运维大屏-实例运行时长排行
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerRunTimeInstanceCntByStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerRunTimeInstanceCntByStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerTaskCntByStatus(
            self,
            request: models.DescribeSchedulerTaskCntByStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerTaskCntByStatusResponse:
        """
        任务状态统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerTaskCntByStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerTaskCntByStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSchedulerTaskTypeCnt(
            self,
            request: models.DescribeSchedulerTaskTypeCntRequest,
            opts: Dict = None,
    ) -> models.DescribeSchedulerTaskTypeCntResponse:
        """
        运维大屏-任务状态分布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSchedulerTaskTypeCnt"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSchedulerTaskTypeCntResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStatisticInstanceStatusTrendOps(
            self,
            request: models.DescribeStatisticInstanceStatusTrendOpsRequest,
            opts: Dict = None,
    ) -> models.DescribeStatisticInstanceStatusTrendOpsResponse:
        """
        任务状态趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStatisticInstanceStatusTrendOps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStatisticInstanceStatusTrendOpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStreamTaskLogList(
            self,
            request: models.DescribeStreamTaskLogListRequest,
            opts: Dict = None,
    ) -> models.DescribeStreamTaskLogListResponse:
        """
        查询实时任务日志列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStreamTaskLogList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStreamTaskLogListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuccessorOpsTaskInfos(
            self,
            request: models.DescribeSuccessorOpsTaskInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeSuccessorOpsTaskInfosResponse:
        """
        获取下游任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuccessorOpsTaskInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuccessorOpsTaskInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSuccessorTaskInfoList(
            self,
            request: models.DescribeSuccessorTaskInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeSuccessorTaskInfoListResponse:
        """
        获取下游任务信息批量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSuccessorTaskInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSuccessorTaskInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableBasicInfo(
            self,
            request: models.DescribeTableBasicInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTableBasicInfoResponse:
        """
        元数据模型-表基础信息查询接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableBasicInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableBasicInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableContentPreview(
            self,
            request: models.DescribeTableContentPreviewRequest,
            opts: Dict = None,
    ) -> models.DescribeTableContentPreviewResponse:
        """
        查询表的数据预览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableContentPreview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableContentPreviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableDdl(
            self,
            request: models.DescribeTableDdlRequest,
            opts: Dict = None,
    ) -> models.DescribeTableDdlResponse:
        """
        查询表的DDL
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableDdl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableDdlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableInfoList(
            self,
            request: models.DescribeTableInfoListRequest,
            opts: Dict = None,
    ) -> models.DescribeTableInfoListResponse:
        """
        获取数据表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableInfoList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableInfoListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableLineage(
            self,
            request: models.DescribeTableLineageRequest,
            opts: Dict = None,
    ) -> models.DescribeTableLineageResponse:
        """
        列出表血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableLineageInfo(
            self,
            request: models.DescribeTableLineageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTableLineageInfoResponse:
        """
        列出表血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableLineageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableLineageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableMeta(
            self,
            request: models.DescribeTableMetaRequest,
            opts: Dict = None,
    ) -> models.DescribeTableMetaResponse:
        """
        查询表元数据详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableMeta"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableMetaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableMetas(
            self,
            request: models.DescribeTableMetasRequest,
            opts: Dict = None,
    ) -> models.DescribeTableMetasResponse:
        """
        获取表元数据list
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableMetas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableMetasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablePartitions(
            self,
            request: models.DescribeTablePartitionsRequest,
            opts: Dict = None,
    ) -> models.DescribeTablePartitionsResponse:
        """
        查询表的分区详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablePartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablePartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableQualityDetails(
            self,
            request: models.DescribeTableQualityDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableQualityDetailsResponse:
        """
        质量报告-查询表质量详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableQualityDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableQualityDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableSchemaInfo(
            self,
            request: models.DescribeTableSchemaInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTableSchemaInfoResponse:
        """
        获取表schema信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableSchemaInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableSchemaInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableScoreTrend(
            self,
            request: models.DescribeTableScoreTrendRequest,
            opts: Dict = None,
    ) -> models.DescribeTableScoreTrendResponse:
        """
        查询表得分趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableScoreTrend"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableScoreTrendResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableSelect(
            self,
            request: models.DescribeTableSelectRequest,
            opts: Dict = None,
    ) -> models.DescribeTableSelectResponse:
        """
        查询表的select语句
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableSelect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableSelectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskAlarmRegulations(
            self,
            request: models.DescribeTaskAlarmRegulationsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskAlarmRegulationsResponse:
        """
        查询任务告警规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskAlarmRegulations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskAlarmRegulationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskByCycle(
            self,
            request: models.DescribeTaskByCycleRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskByCycleResponse:
        """
        根据周期类型 查询所有任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskByCycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskByCycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskByStatusReport(
            self,
            request: models.DescribeTaskByStatusReportRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskByStatusReportResponse:
        """
        任务状态趋势
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskByStatusReport"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskByStatusReportResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskDetailDs(
            self,
            request: models.DescribeTaskDetailDsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskDetailDsResponse:
        """
        查询任务具体详情【新】
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskDetailDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskDetailDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInstancesStatus(
            self,
            request: models.DescribeTaskInstancesStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInstancesStatusResponse:
        """
        分组获取编排空间调试任务实例状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInstancesStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInstancesStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLineage(
            self,
            request: models.DescribeTaskLineageRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLineageResponse:
        """
        通过任务查询表的血缘关系
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLockStatus(
            self,
            request: models.DescribeTaskLockStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLockStatusResponse:
        """
        查看任务锁状态信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLockStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLockStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskParamDs(
            self,
            request: models.DescribeTaskParamDsRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskParamDsResponse:
        """
        查询任务引用参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskParamDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskParamDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskRunHistory(
            self,
            request: models.DescribeTaskRunHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskRunHistoryResponse:
        """
        分页查询任务运行历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskRunHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskRunHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskScript(
            self,
            request: models.DescribeTaskScriptRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskScriptResponse:
        """
        查询任务脚本。本接口已废弃，请使用接口GetPaginationTaskScript。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskTableMetricOverview(
            self,
            request: models.DescribeTaskTableMetricOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskTableMetricOverviewResponse:
        """
        查询实时任务表粒度指标概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskTableMetricOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskTableMetricOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskTemplates(
            self,
            request: models.DescribeTaskTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskTemplatesResponse:
        """
        查询项目下所有任务列表,包括虚拟任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasksForCodeTemplate(
            self,
            request: models.DescribeTasksForCodeTemplateRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksForCodeTemplateResponse:
        """
        分页查询引用模板的任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasksForCodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksForCodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateDimCount(
            self,
            request: models.DescribeTemplateDimCountRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateDimCountResponse:
        """
        查询规则模板维度分布情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateDimCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateDimCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTenantProjects(
            self,
            request: models.DescribeTenantProjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeTenantProjectsResponse:
        """
        租户全局范围的项目列表，与用户查看范围无关.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTenantProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTenantProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTestRunningRecord(
            self,
            request: models.DescribeTestRunningRecordRequest,
            opts: Dict = None,
    ) -> models.DescribeTestRunningRecordResponse:
        """
        获取编排空间试运行历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTestRunningRecord"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTestRunningRecordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeThirdTaskRunLog(
            self,
            request: models.DescribeThirdTaskRunLogRequest,
            opts: Dict = None,
    ) -> models.DescribeThirdTaskRunLogResponse:
        """
        获取第三方运行日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeThirdTaskRunLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeThirdTaskRunLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTopTableStat(
            self,
            request: models.DescribeTopTableStatRequest,
            opts: Dict = None,
    ) -> models.DescribeTopTableStatResponse:
        """
        数据质量概览页面表排行接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTopTableStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTopTableStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrendStat(
            self,
            request: models.DescribeTrendStatRequest,
            opts: Dict = None,
    ) -> models.DescribeTrendStatResponse:
        """
        数据质量概览页面趋势变化接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrendStat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrendStatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowByFordIds(
            self,
            request: models.DescribeWorkflowByFordIdsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowByFordIdsResponse:
        """
        根据文件夹查询工作流
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowByFordIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowByFordIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowCanvasInfo(
            self,
            request: models.DescribeWorkflowCanvasInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowCanvasInfoResponse:
        """
        查询工作流画布
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowCanvasInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowCanvasInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowExecuteById(
            self,
            request: models.DescribeWorkflowExecuteByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowExecuteByIdResponse:
        """
        查询工作流画布运行起止时间
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowExecuteById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowExecuteByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowInfoById(
            self,
            request: models.DescribeWorkflowInfoByIdRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowInfoByIdResponse:
        """
        通过工作流id，查询工作流详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowInfoById"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowInfoByIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowListByProjectId(
            self,
            request: models.DescribeWorkflowListByProjectIdRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowListByProjectIdResponse:
        """
        根据项目id 获取项目下所有工作流列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowListByProjectId"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowListByProjectIdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowSchedulerInfoDs(
            self,
            request: models.DescribeWorkflowSchedulerInfoDsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowSchedulerInfoDsResponse:
        """
        获取工作流调度信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowSchedulerInfoDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowSchedulerInfoDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkflowTaskCount(
            self,
            request: models.DescribeWorkflowTaskCountRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkflowTaskCountResponse:
        """
        查询工作流任务数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkflowTaskCount"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkflowTaskCountResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DiagnosePro(
            self,
            request: models.DiagnoseProRequest,
            opts: Dict = None,
    ) -> models.DiagnoseProResponse:
        """
        实例诊断，用于诊断 INITIAL、DEPENDENCE、ALLOCATED、LAUNCHED、EVENT_LISTENING、BEFORE_ASPECT、EXPIRED、FAILED状态的实例
        """
        
        kwargs = {}
        kwargs["action"] = "DiagnosePro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DiagnoseProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableProject(
            self,
            request: models.DisableProjectRequest,
            opts: Dict = None,
    ) -> models.DisableProjectResponse:
        """
        禁用项目
        """
        
        kwargs = {}
        kwargs["action"] = "DisableProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadLogByLine(
            self,
            request: models.DownloadLogByLineRequest,
            opts: Dict = None,
    ) -> models.DownloadLogByLineResponse:
        """
        按行下载日志信息
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadLogByLine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadLogByLineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DryRunDIOfflineTask(
            self,
            request: models.DryRunDIOfflineTaskRequest,
            opts: Dict = None,
    ) -> models.DryRunDIOfflineTaskResponse:
        """
        调试运行集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "DryRunDIOfflineTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DryRunDIOfflineTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableProject(
            self,
            request: models.EnableProjectRequest,
            opts: Dict = None,
    ) -> models.EnableProjectResponse:
        """
        启用项目
        """
        
        kwargs = {}
        kwargs["action"] = "EnableProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FindAllFolder(
            self,
            request: models.FindAllFolderRequest,
            opts: Dict = None,
    ) -> models.FindAllFolderResponse:
        """
        编排空间批量操作页面查找全部的文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "FindAllFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FindAllFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreezeOpsTasks(
            self,
            request: models.FreezeOpsTasksRequest,
            opts: Dict = None,
    ) -> models.FreezeOpsTasksResponse:
        """
        任务运维-批量暂停任务
        """
        
        kwargs = {}
        kwargs["action"] = "FreezeOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreezeOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FreezeTasksByWorkflowIds(
            self,
            request: models.FreezeTasksByWorkflowIdsRequest,
            opts: Dict = None,
    ) -> models.FreezeTasksByWorkflowIdsResponse:
        """
        暂停工作流下的所有任务
        """
        
        kwargs = {}
        kwargs["action"] = "FreezeTasksByWorkflowIds"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FreezeTasksByWorkflowIdsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenHiveTableDDLSql(
            self,
            request: models.GenHiveTableDDLSqlRequest,
            opts: Dict = None,
    ) -> models.GenHiveTableDDLSqlResponse:
        """
        生成建hive表的sql
        """
        
        kwargs = {}
        kwargs["action"] = "GenHiveTableDDLSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenHiveTableDDLSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetBatchDetailErrorLog(
            self,
            request: models.GetBatchDetailErrorLogRequest,
            opts: Dict = None,
    ) -> models.GetBatchDetailErrorLogResponse:
        """
        获取批量操作错误日志
        """
        
        kwargs = {}
        kwargs["action"] = "GetBatchDetailErrorLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetBatchDetailErrorLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCosToken(
            self,
            request: models.GetCosTokenRequest,
            opts: Dict = None,
    ) -> models.GetCosTokenResponse:
        """
        获取cos token
        """
        
        kwargs = {}
        kwargs["action"] = "GetCosToken"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCosTokenResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetFileInfo(
            self,
            request: models.GetFileInfoRequest,
            opts: Dict = None,
    ) -> models.GetFileInfoResponse:
        """
        开发空间-获取数据开发脚本信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetFileInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetFileInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetInstanceLog(
            self,
            request: models.GetInstanceLogRequest,
            opts: Dict = None,
    ) -> models.GetInstanceLogResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetIntegrationNodeColumnSchema(
            self,
            request: models.GetIntegrationNodeColumnSchemaRequest,
            opts: Dict = None,
    ) -> models.GetIntegrationNodeColumnSchemaResponse:
        """
        提取数据集成节点字段Schema
        """
        
        kwargs = {}
        kwargs["action"] = "GetIntegrationNodeColumnSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetIntegrationNodeColumnSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetJobStatus(
            self,
            request: models.GetJobStatusRequest,
            opts: Dict = None,
    ) -> models.GetJobStatusResponse:
        """
        获取异步任务执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "GetJobStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetJobStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOfflineDIInstanceList(
            self,
            request: models.GetOfflineDIInstanceListRequest,
            opts: Dict = None,
    ) -> models.GetOfflineDIInstanceListResponse:
        """
        获取离线任务实例列表(新)
        """
        
        kwargs = {}
        kwargs["action"] = "GetOfflineDIInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOfflineDIInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOfflineInstanceList(
            self,
            request: models.GetOfflineInstanceListRequest,
            opts: Dict = None,
    ) -> models.GetOfflineInstanceListResponse:
        """
        获取离线任务实例
        """
        
        kwargs = {}
        kwargs["action"] = "GetOfflineInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOfflineInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetPaginationTaskScript(
            self,
            request: models.GetPaginationTaskScriptRequest,
            opts: Dict = None,
    ) -> models.GetPaginationTaskScriptResponse:
        """
        获取带分页的任务脚本
        """
        
        kwargs = {}
        kwargs["action"] = "GetPaginationTaskScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetPaginationTaskScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskInstance(
            self,
            request: models.GetTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.GetTaskInstanceResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def JudgeResourceFile(
            self,
            request: models.JudgeResourceFileRequest,
            opts: Dict = None,
    ) -> models.JudgeResourceFileResponse:
        """
        资源管理-判断资源文件是否存在
        """
        
        kwargs = {}
        kwargs["action"] = "JudgeResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.JudgeResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillOpsMakePlanInstances(
            self,
            request: models.KillOpsMakePlanInstancesRequest,
            opts: Dict = None,
    ) -> models.KillOpsMakePlanInstancesResponse:
        """
        按补录计划批量终止实例。
        """
        
        kwargs = {}
        kwargs["action"] = "KillOpsMakePlanInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillOpsMakePlanInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillScheduleInstances(
            self,
            request: models.KillScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.KillScheduleInstancesResponse:
        """
        批量终止实例
        """
        
        kwargs = {}
        kwargs["action"] = "KillScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListBatchDetail(
            self,
            request: models.ListBatchDetailRequest,
            opts: Dict = None,
    ) -> models.ListBatchDetailResponse:
        """
        获取批量操作详情列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListBatchDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListBatchDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListInstances(
            self,
            request: models.ListInstancesRequest,
            opts: Dict = None,
    ) -> models.ListInstancesResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LockIntegrationTask(
            self,
            request: models.LockIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.LockIntegrationTaskResponse:
        """
        锁定集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "LockIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LockIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyApproveStatus(
            self,
            request: models.ModifyApproveStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyApproveStatusResponse:
        """
        修改审批单状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyApproveStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyApproveStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataSource(
            self,
            request: models.ModifyDataSourceRequest,
            opts: Dict = None,
    ) -> models.ModifyDataSourceResponse:
        """
        修改数据源
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDimensionWeight(
            self,
            request: models.ModifyDimensionWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyDimensionWeightResponse:
        """
        质量报告-修改维度权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDimensionWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDimensionWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDsFolder(
            self,
            request: models.ModifyDsFolderRequest,
            opts: Dict = None,
    ) -> models.ModifyDsFolderResponse:
        """
        数据开发模块-文件夹更新
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDsFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDsFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyExecStrategy(
            self,
            request: models.ModifyExecStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyExecStrategyResponse:
        """
        更新规则组执行策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyExecStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyExecStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIntegrationNode(
            self,
            request: models.ModifyIntegrationNodeRequest,
            opts: Dict = None,
    ) -> models.ModifyIntegrationNodeResponse:
        """
        更新集成节点
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIntegrationNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIntegrationNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIntegrationTask(
            self,
            request: models.ModifyIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.ModifyIntegrationTaskResponse:
        """
        更新集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMonitorStatus(
            self,
            request: models.ModifyMonitorStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyMonitorStatusResponse:
        """
        更新监控状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMonitorStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMonitorStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProject(
            self,
            request: models.ModifyProjectRequest,
            opts: Dict = None,
    ) -> models.ModifyProjectResponse:
        """
        修改项目基础信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRule(
            self,
            request: models.ModifyRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleResponse:
        """
        更新质量规则接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleGroupSubscription(
            self,
            request: models.ModifyRuleGroupSubscriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleGroupSubscriptionResponse:
        """
        更新规则组订阅信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleGroupSubscription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleGroupSubscriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRuleTemplate(
            self,
            request: models.ModifyRuleTemplateRequest,
            opts: Dict = None,
    ) -> models.ModifyRuleTemplateResponse:
        """
        编辑规则模板
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRuleTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRuleTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskAlarmRegular(
            self,
            request: models.ModifyTaskAlarmRegularRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskAlarmRegularResponse:
        """
        修改任务告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskAlarmRegular"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskAlarmRegularResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskInfo(
            self,
            request: models.ModifyTaskInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskInfoResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        更新任务。本接口已废弃，请使用接口ModifyTaskInfoDs。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskInfoDs(
            self,
            request: models.ModifyTaskInfoDsRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskInfoDsResponse:
        """
        更新任务Ds
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskInfoDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskInfoDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskLinks(
            self,
            request: models.ModifyTaskLinksRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskLinksResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        添加父任务依赖。本接口已废弃，请使用接口ModifyTaskLinksDs。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskLinks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskLinksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskLinksDs(
            self,
            request: models.ModifyTaskLinksDsRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskLinksDsResponse:
        """
        添加父任务依赖
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskLinksDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskLinksDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskName(
            self,
            request: models.ModifyTaskNameRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskNameResponse:
        """
        重命名任务（任务编辑）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTaskScript(
            self,
            request: models.ModifyTaskScriptRequest,
            opts: Dict = None,
    ) -> models.ModifyTaskScriptResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        修改任务脚本。本接口已废弃，请使用接口ModifyTaskInfoDs。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTaskScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTaskScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkflowInfo(
            self,
            request: models.ModifyWorkflowInfoRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkflowInfoResponse:
        """
        更新工作流信息。本接口已废弃，请使用接口UpdateWorkflowInfo。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkflowInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkflowInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkflowSchedule(
            self,
            request: models.ModifyWorkflowScheduleRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkflowScheduleResponse:
        """
        更新工作流调度。本接口已废弃，请使用接口RenewWorkflowSchedulerInfoDs。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkflowSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkflowScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MoveTasksToFolder(
            self,
            request: models.MoveTasksToFolderRequest,
            opts: Dict = None,
    ) -> models.MoveTasksToFolderResponse:
        """
        编排空间-工作流-移动任务到工作流文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "MoveTasksToFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MoveTasksToFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterDsEvent(
            self,
            request: models.RegisterDsEventRequest,
            opts: Dict = None,
    ) -> models.RegisterDsEventResponse:
        """
        注册事件
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterDsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterDsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterDsEventListener(
            self,
            request: models.RegisterDsEventListenerRequest,
            opts: Dict = None,
    ) -> models.RegisterDsEventListenerResponse:
        """
        注册事件监听者
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterDsEventListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterDsEventListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterEvent(
            self,
            request: models.RegisterEventRequest,
            opts: Dict = None,
    ) -> models.RegisterEventResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        注册事件。本接口已废弃，请使用接口RegisterDsEvent。
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterEventListener(
            self,
            request: models.RegisterEventListenerRequest,
            opts: Dict = None,
    ) -> models.RegisterEventListenerResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        注册事件监听器。本接口已废弃，请使用接口RegisterDsEventListener。
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterEventListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterEventListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveDatabase(
            self,
            request: models.RemoveDatabaseRequest,
            opts: Dict = None,
    ) -> models.RemoveDatabaseResponse:
        """
        移除database元数据
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveSchema(
            self,
            request: models.RemoveSchemaRequest,
            opts: Dict = None,
    ) -> models.RemoveSchemaResponse:
        """
        移除schema元数据
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveTable(
            self,
            request: models.RemoveTableRequest,
            opts: Dict = None,
    ) -> models.RemoveTableResponse:
        """
        移除table元数据
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveWorkflowDs(
            self,
            request: models.RemoveWorkflowDsRequest,
            opts: Dict = None,
    ) -> models.RemoveWorkflowDsResponse:
        """
        删除编排空间工作流
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveWorkflowDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveWorkflowDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewWorkflowOwnerDs(
            self,
            request: models.RenewWorkflowOwnerDsRequest,
            opts: Dict = None,
    ) -> models.RenewWorkflowOwnerDsResponse:
        """
        批量更新工作流下任务责任人
        """
        
        kwargs = {}
        kwargs["action"] = "RenewWorkflowOwnerDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewWorkflowOwnerDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewWorkflowSchedulerInfoDs(
            self,
            request: models.RenewWorkflowSchedulerInfoDsRequest,
            opts: Dict = None,
    ) -> models.RenewWorkflowSchedulerInfoDsResponse:
        """
        更新工作流下任务调度信息
        """
        
        kwargs = {}
        kwargs["action"] = "RenewWorkflowSchedulerInfoDs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewWorkflowSchedulerInfoDsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportDatabase(
            self,
            request: models.ReportDatabaseRequest,
            opts: Dict = None,
    ) -> models.ReportDatabaseResponse:
        """
        上报database元数据
        """
        
        kwargs = {}
        kwargs["action"] = "ReportDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportSchema(
            self,
            request: models.ReportSchemaRequest,
            opts: Dict = None,
    ) -> models.ReportSchemaResponse:
        """
        上报schema元数据
        """
        
        kwargs = {}
        kwargs["action"] = "ReportSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportTable(
            self,
            request: models.ReportTableRequest,
            opts: Dict = None,
    ) -> models.ReportTableResponse:
        """
        上报table元数据,当前列数量限制在300
        """
        
        kwargs = {}
        kwargs["action"] = "ReportTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportTaskLineage(
            self,
            request: models.ReportTaskLineageRequest,
            opts: Dict = None,
    ) -> models.ReportTaskLineageResponse:
        """
        血缘上报接口
        """
        
        kwargs = {}
        kwargs["action"] = "ReportTaskLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportTaskLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeIntegrationTask(
            self,
            request: models.ResumeIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.ResumeIntegrationTaskResponse:
        """
        继续集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RobAndLockIntegrationTask(
            self,
            request: models.RobAndLockIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.RobAndLockIntegrationTaskResponse:
        """
        抢占锁定集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "RobAndLockIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RobAndLockIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunForceSucScheduleInstances(
            self,
            request: models.RunForceSucScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.RunForceSucScheduleInstancesResponse:
        """
        实例批量置成功
        """
        
        kwargs = {}
        kwargs["action"] = "RunForceSucScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunForceSucScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunRerunScheduleInstances(
            self,
            request: models.RunRerunScheduleInstancesRequest,
            opts: Dict = None,
    ) -> models.RunRerunScheduleInstancesResponse:
        """
        实例批量重跑
        """
        
        kwargs = {}
        kwargs["action"] = "RunRerunScheduleInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunRerunScheduleInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunTasksByMultiWorkflow(
            self,
            request: models.RunTasksByMultiWorkflowRequest,
            opts: Dict = None,
    ) -> models.RunTasksByMultiWorkflowResponse:
        """
        批量启动工作流
        """
        
        kwargs = {}
        kwargs["action"] = "RunTasksByMultiWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunTasksByMultiWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SaveCustomFunction(
            self,
            request: models.SaveCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.SaveCustomFunctionResponse:
        """
        保存用户自定义函数
        """
        
        kwargs = {}
        kwargs["action"] = "SaveCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SaveCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTaskAlarmNew(
            self,
            request: models.SetTaskAlarmNewRequest,
            opts: Dict = None,
    ) -> models.SetTaskAlarmNewResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        设置任务告警，新建/更新告警信息（最新）
        """
        
        kwargs = {}
        kwargs["action"] = "SetTaskAlarmNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTaskAlarmNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartIntegrationTask(
            self,
            request: models.StartIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.StartIntegrationTaskResponse:
        """
        启动集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopIntegrationTask(
            self,
            request: models.StopIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.StopIntegrationTaskResponse:
        """
        停止集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitCustomFunction(
            self,
            request: models.SubmitCustomFunctionRequest,
            opts: Dict = None,
    ) -> models.SubmitCustomFunctionResponse:
        """
        提交自定义函数
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitCustomFunction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitCustomFunctionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitSqlTask(
            self,
            request: models.SubmitSqlTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitSqlTaskResponse:
        """
        即席分析提交SQL任务
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitSqlTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitSqlTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTask(
            self,
            request: models.SubmitTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitTaskResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        提交任务。本接口已废弃，请使用接口CreateTaskVersionDs。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTaskTestRun(
            self,
            request: models.SubmitTaskTestRunRequest,
            opts: Dict = None,
    ) -> models.SubmitTaskTestRunResponse:
        """
        无
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTaskTestRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTaskTestRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitWorkflow(
            self,
            request: models.SubmitWorkflowRequest,
            opts: Dict = None,
    ) -> models.SubmitWorkflowResponse:
        """
        提交工作流。本接口已废弃，请使用接口BatchCreateTaskVersionAsync。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SuspendIntegrationTask(
            self,
            request: models.SuspendIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.SuspendIntegrationTaskResponse:
        """
        暂停集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "SuspendIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SuspendIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TaskLog(
            self,
            request: models.TaskLogRequest,
            opts: Dict = None,
    ) -> models.TaskLogResponse:
        """
        查询Inlong manager日志
        """
        
        kwargs = {}
        kwargs["action"] = "TaskLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TaskLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerDsEvent(
            self,
            request: models.TriggerDsEventRequest,
            opts: Dict = None,
    ) -> models.TriggerDsEventResponse:
        """
        事件管理-触发事件
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerDsEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerDsEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerEvent(
            self,
            request: models.TriggerEventRequest,
            opts: Dict = None,
    ) -> models.TriggerEventResponse:
        """
        <p style="color:red;">[注意：该版本只满足广州区部分白名单客户使用]</p>
        触发事件。本接口已废弃，请使用接口TriggerDsEvent。
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerEvent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerEventResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerManualTasks(
            self,
            request: models.TriggerManualTasksRequest,
            opts: Dict = None,
    ) -> models.TriggerManualTasksResponse:
        """
        手动任务触发运行
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerManualTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerManualTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnboundProjectExecutorResource(
            self,
            request: models.UnboundProjectExecutorResourceRequest,
            opts: Dict = None,
    ) -> models.UnboundProjectExecutorResourceResponse:
        """
        商业化版本：执行资源组/资源包解除绑定项目
        """
        
        kwargs = {}
        kwargs["action"] = "UnboundProjectExecutorResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnboundProjectExecutorResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlockIntegrationTask(
            self,
            request: models.UnlockIntegrationTaskRequest,
            opts: Dict = None,
    ) -> models.UnlockIntegrationTaskResponse:
        """
        解锁集成任务
        """
        
        kwargs = {}
        kwargs["action"] = "UnlockIntegrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlockIntegrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCodeTemplate(
            self,
            request: models.UpdateCodeTemplateRequest,
            opts: Dict = None,
    ) -> models.UpdateCodeTemplateResponse:
        """
        更新模版
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCodeTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCodeTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataModelRegistryInfo(
            self,
            request: models.UpdateDataModelRegistryInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateDataModelRegistryInfoResponse:
        """
        数语向wedata注册，提供自身cam角色信息，跳转域名、ip、端口信息等
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataModelRegistryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataModelRegistryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProjectUserRole(
            self,
            request: models.UpdateProjectUserRoleRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectUserRoleResponse:
        """
        修改项目用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProjectUserRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectUserRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflowInfo(
            self,
            request: models.UpdateWorkflowInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowInfoResponse:
        """
        <p style="color:red;">[该接口为 ds 中开发]</p>
        更新工作流（包括工作流基本信息与工作流参数）
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflowOwner(
            self,
            request: models.UpdateWorkflowOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowOwnerResponse:
        """
        修改工作流责任人。本接口已废弃，请使用接口RenewWorkflowOwnerDs。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadContent(
            self,
            request: models.UploadContentRequest,
            opts: Dict = None,
    ) -> models.UploadContentResponse:
        """
        保存任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "UploadContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadResource(
            self,
            request: models.UploadResourceRequest,
            opts: Dict = None,
    ) -> models.UploadResourceResponse:
        """
        资源管理-上传资源
        """
        
        kwargs = {}
        kwargs["action"] = "UploadResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)