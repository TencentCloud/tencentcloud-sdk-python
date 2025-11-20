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
from tencentcloud.wedata.v20250806 import models
from typing import Dict


class WedataClient(AbstractClient):
    _apiVersion = '2025-08-06'
    _endpoint = 'wedata.tencentcloudapi.com'
    _service = 'wedata'

    async def AddCalcEnginesToProject(
            self,
            request: models.AddCalcEnginesToProjectRequest,
            opts: Dict = None,
    ) -> models.AddCalcEnginesToProjectResponse:
        """
        关联项目集群
        """
        
        kwargs = {}
        kwargs["action"] = "AddCalcEnginesToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddCalcEnginesToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateResourceGroupToProject(
            self,
            request: models.AssociateResourceGroupToProjectRequest,
            opts: Dict = None,
    ) -> models.AssociateResourceGroupToProjectResponse:
        """
        该接口用于将指定执行资源组绑定到项目
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateResourceGroupToProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateResourceGroupToProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodeFile(
            self,
            request: models.CreateCodeFileRequest,
            opts: Dict = None,
    ) -> models.CreateCodeFileResponse:
        """
        新建代码文件
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCodeFolder(
            self,
            request: models.CreateCodeFolderRequest,
            opts: Dict = None,
    ) -> models.CreateCodeFolderResponse:
        """
        新建代码文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataBackfillPlan(
            self,
            request: models.CreateDataBackfillPlanRequest,
            opts: Dict = None,
    ) -> models.CreateDataBackfillPlanResponse:
        """
        创建数据补录计划
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataBackfillPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataBackfillPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataSource(
            self,
            request: models.CreateDataSourceRequest,
            opts: Dict = None,
    ) -> models.CreateDataSourceResponse:
        """
        该接口用于在指定项目中创建数据源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateOpsAlarmRule(
            self,
            request: models.CreateOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.CreateOpsAlarmRuleResponse:
        """
        设置告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProject(
            self,
            request: models.CreateProjectRequest,
            opts: Dict = None,
    ) -> models.CreateProjectResponse:
        """
        创建项目，创建时包含集群信息
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateProjectMember(
            self,
            request: models.CreateProjectMemberRequest,
            opts: Dict = None,
    ) -> models.CreateProjectMemberResponse:
        """
        添加项目用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "CreateProjectMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateProjectMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceFile(
            self,
            request: models.CreateResourceFileRequest,
            opts: Dict = None,
    ) -> models.CreateResourceFileResponse:
        """
        创建资源文件
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceFolder(
            self,
            request: models.CreateResourceFolderRequest,
            opts: Dict = None,
    ) -> models.CreateResourceFolderResponse:
        """
        创建资源文件文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceGroup(
            self,
            request: models.CreateResourceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateResourceGroupResponse:
        """
        该接口用于购买资源
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSQLFolder(
            self,
            request: models.CreateSQLFolderRequest,
            opts: Dict = None,
    ) -> models.CreateSQLFolderResponse:
        """
        创建数据探索脚本文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSQLScript(
            self,
            request: models.CreateSQLScriptRequest,
            opts: Dict = None,
    ) -> models.CreateSQLScriptResponse:
        """
        新增SQL脚本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        创建任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflow(
            self,
            request: models.CreateWorkflowRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowResponse:
        """
        创建工作流
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkflowFolder(
            self,
            request: models.CreateWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.CreateWorkflowFolderResponse:
        """
        创建文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeFile(
            self,
            request: models.DeleteCodeFileRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeFileResponse:
        """
        删除代码文件
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCodeFolder(
            self,
            request: models.DeleteCodeFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteCodeFolderResponse:
        """
        数据探索删除文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataSource(
            self,
            request: models.DeleteDataSourceRequest,
            opts: Dict = None,
    ) -> models.DeleteDataSourceResponse:
        """
        该接口用于删除数据源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLineage(
            self,
            request: models.DeleteLineageRequest,
            opts: Dict = None,
    ) -> models.DeleteLineageResponse:
        """
        RegisterLineage
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteOpsAlarmRule(
            self,
            request: models.DeleteOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteOpsAlarmRuleResponse:
        """
        删除告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteProjectMember(
            self,
            request: models.DeleteProjectMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteProjectMemberResponse:
        """
        删除项目用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteProjectMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteProjectMemberResponse
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
        
    async def DeleteResourceFolder(
            self,
            request: models.DeleteResourceFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceFolderResponse:
        """
        删除资源文件文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceGroup(
            self,
            request: models.DeleteResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceGroupResponse:
        """
        该接口用于销毁资源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSQLFolder(
            self,
            request: models.DeleteSQLFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteSQLFolderResponse:
        """
        删除SQL文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSQLScript(
            self,
            request: models.DeleteSQLScriptRequest,
            opts: Dict = None,
    ) -> models.DeleteSQLScriptResponse:
        """
        删除探索脚本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTask(
            self,
            request: models.DeleteTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteTaskResponse:
        """
        删除编排空间任务
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflow(
            self,
            request: models.DeleteWorkflowRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowResponse:
        """
        删除工作流
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkflowFolder(
            self,
            request: models.DeleteWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkflowFolderResponse:
        """
        删除数据开发文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkflowFolderResponse
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
        
    async def DissociateResourceGroupFromProject(
            self,
            request: models.DissociateResourceGroupFromProjectRequest,
            opts: Dict = None,
    ) -> models.DissociateResourceGroupFromProjectResponse:
        """
        该接口用于将指定执行资源组解除与项目的绑定
        """
        
        kwargs = {}
        kwargs["action"] = "DissociateResourceGroupFromProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DissociateResourceGroupFromProjectResponse
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
        
    async def GetAlarmMessage(
            self,
            request: models.GetAlarmMessageRequest,
            opts: Dict = None,
    ) -> models.GetAlarmMessageResponse:
        """
        查询告警信息详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetAlarmMessage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetAlarmMessageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCodeFile(
            self,
            request: models.GetCodeFileRequest,
            opts: Dict = None,
    ) -> models.GetCodeFileResponse:
        """
        查看代码文件详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCodeFolder(
            self,
            request: models.GetCodeFolderRequest,
            opts: Dict = None,
    ) -> models.GetCodeFolderResponse:
        """
        获取sql文件夹详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataBackfillPlan(
            self,
            request: models.GetDataBackfillPlanRequest,
            opts: Dict = None,
    ) -> models.GetDataBackfillPlanResponse:
        """
        获取补录计划详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataBackfillPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataBackfillPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataSource(
            self,
            request: models.GetDataSourceRequest,
            opts: Dict = None,
    ) -> models.GetDataSourceResponse:
        """
        该接口用于查看指定数据源的详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetDataSourceRelatedTasks(
            self,
            request: models.GetDataSourceRelatedTasksRequest,
            opts: Dict = None,
    ) -> models.GetDataSourceRelatedTasksResponse:
        """
        数据源关联任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetDataSourceRelatedTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetDataSourceRelatedTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsAlarmRule(
            self,
            request: models.GetOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.GetOpsAlarmRuleResponse:
        """
        根据告警规则id/名称查询单个告警规则信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsAsyncJob(
            self,
            request: models.GetOpsAsyncJobRequest,
            opts: Dict = None,
    ) -> models.GetOpsAsyncJobResponse:
        """
        查询运维中心异步操作详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsAsyncJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsAsyncJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsTask(
            self,
            request: models.GetOpsTaskRequest,
            opts: Dict = None,
    ) -> models.GetOpsTaskResponse:
        """
        获取任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsTaskCode(
            self,
            request: models.GetOpsTaskCodeRequest,
            opts: Dict = None,
    ) -> models.GetOpsTaskCodeResponse:
        """
        获取任务代码
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsTaskCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsTaskCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOpsWorkflow(
            self,
            request: models.GetOpsWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetOpsWorkflowResponse:
        """
        根据工作流id，获取工作流调度详情。
        """
        
        kwargs = {}
        kwargs["action"] = "GetOpsWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOpsWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetProject(
            self,
            request: models.GetProjectRequest,
            opts: Dict = None,
    ) -> models.GetProjectResponse:
        """
        获取项目信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResourceFile(
            self,
            request: models.GetResourceFileRequest,
            opts: Dict = None,
    ) -> models.GetResourceFileResponse:
        """
        获取资源文件详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetResourceGroupMetrics(
            self,
            request: models.GetResourceGroupMetricsRequest,
            opts: Dict = None,
    ) -> models.GetResourceGroupMetricsResponse:
        """
        该接口用于查看指定执行资源组的监控指标
        """
        
        kwargs = {}
        kwargs["action"] = "GetResourceGroupMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetResourceGroupMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSQLFolder(
            self,
            request: models.GetSQLFolderRequest,
            opts: Dict = None,
    ) -> models.GetSQLFolderResponse:
        """
        获取sql文件夹详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetSQLScript(
            self,
            request: models.GetSQLScriptRequest,
            opts: Dict = None,
    ) -> models.GetSQLScriptResponse:
        """
        查询脚本详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTable(
            self,
            request: models.GetTableRequest,
            opts: Dict = None,
    ) -> models.GetTableResponse:
        """
        查询表详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTableColumns(
            self,
            request: models.GetTableColumnsRequest,
            opts: Dict = None,
    ) -> models.GetTableColumnsResponse:
        """
        查询表所有字段列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTableColumns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTableColumnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTask(
            self,
            request: models.GetTaskRequest,
            opts: Dict = None,
    ) -> models.GetTaskResponse:
        """
        获取任务详情接口
        """
        
        kwargs = {}
        kwargs["action"] = "GetTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskCode(
            self,
            request: models.GetTaskCodeRequest,
            opts: Dict = None,
    ) -> models.GetTaskCodeResponse:
        """
        获取任务代码
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskInstance(
            self,
            request: models.GetTaskInstanceRequest,
            opts: Dict = None,
    ) -> models.GetTaskInstanceResponse:
        """
        调度实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskInstanceLog(
            self,
            request: models.GetTaskInstanceLogRequest,
            opts: Dict = None,
    ) -> models.GetTaskInstanceLogResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskInstanceLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskInstanceLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetTaskVersion(
            self,
            request: models.GetTaskVersionRequest,
            opts: Dict = None,
    ) -> models.GetTaskVersionResponse:
        """
        拉取任务版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "GetTaskVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetTaskVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetWorkflow(
            self,
            request: models.GetWorkflowRequest,
            opts: Dict = None,
    ) -> models.GetWorkflowResponse:
        """
        获取工作流信息
        """
        
        kwargs = {}
        kwargs["action"] = "GetWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantMemberProjectRole(
            self,
            request: models.GrantMemberProjectRoleRequest,
            opts: Dict = None,
    ) -> models.GrantMemberProjectRoleResponse:
        """
        修改项目用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "GrantMemberProjectRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantMemberProjectRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def KillTaskInstancesAsync(
            self,
            request: models.KillTaskInstancesAsyncRequest,
            opts: Dict = None,
    ) -> models.KillTaskInstancesAsyncResponse:
        """
        实例批量终止操作-异步操作
        """
        
        kwargs = {}
        kwargs["action"] = "KillTaskInstancesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.KillTaskInstancesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListAlarmMessages(
            self,
            request: models.ListAlarmMessagesRequest,
            opts: Dict = None,
    ) -> models.ListAlarmMessagesResponse:
        """
        获取告警信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListAlarmMessages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListAlarmMessagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCatalog(
            self,
            request: models.ListCatalogRequest,
            opts: Dict = None,
    ) -> models.ListCatalogResponse:
        """
        获取资产目录信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListCatalog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCatalogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListCodeFolderContents(
            self,
            request: models.ListCodeFolderContentsRequest,
            opts: Dict = None,
    ) -> models.ListCodeFolderContentsResponse:
        """
        获取文件夹内容
        """
        
        kwargs = {}
        kwargs["action"] = "ListCodeFolderContents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListCodeFolderContentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListColumnLineage(
            self,
            request: models.ListColumnLineageRequest,
            opts: Dict = None,
    ) -> models.ListColumnLineageResponse:
        """
        获取表字段血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListColumnLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListColumnLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataBackfillInstances(
            self,
            request: models.ListDataBackfillInstancesRequest,
            opts: Dict = None,
    ) -> models.ListDataBackfillInstancesResponse:
        """
        获取单次补录的所有实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataBackfillInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataBackfillInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDataSources(
            self,
            request: models.ListDataSourcesRequest,
            opts: Dict = None,
    ) -> models.ListDataSourcesResponse:
        """
        该接口用于查询指定项目中的数据源列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListDataSources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDataSourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDatabase(
            self,
            request: models.ListDatabaseRequest,
            opts: Dict = None,
    ) -> models.ListDatabaseResponse:
        """
        获取资产数据库信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDownstreamOpsTasks(
            self,
            request: models.ListDownstreamOpsTasksRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamOpsTasksResponse:
        """
        获取任务直接下游详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDownstreamTaskInstances(
            self,
            request: models.ListDownstreamTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamTaskInstancesResponse:
        """
        获取实例直接上游
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListDownstreamTasks(
            self,
            request: models.ListDownstreamTasksRequest,
            opts: Dict = None,
    ) -> models.ListDownstreamTasksResponse:
        """
        获取任务直接下游详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListDownstreamTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListDownstreamTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListLineage(
            self,
            request: models.ListLineageRequest,
            opts: Dict = None,
    ) -> models.ListLineageResponse:
        """
        获取资产血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOpsAlarmRules(
            self,
            request: models.ListOpsAlarmRulesRequest,
            opts: Dict = None,
    ) -> models.ListOpsAlarmRulesResponse:
        """
        查询告警规则列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsAlarmRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsAlarmRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOpsTasks(
            self,
            request: models.ListOpsTasksRequest,
            opts: Dict = None,
    ) -> models.ListOpsTasksResponse:
        """
        根据项目id获取任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListOpsWorkflows(
            self,
            request: models.ListOpsWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListOpsWorkflowsResponse:
        """
        根据项目ID获取项目下工作流
        """
        
        kwargs = {}
        kwargs["action"] = "ListOpsWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListOpsWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProcessLineage(
            self,
            request: models.ListProcessLineageRequest,
            opts: Dict = None,
    ) -> models.ListProcessLineageResponse:
        """
        获取资产血缘信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListProcessLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProcessLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProjectMembers(
            self,
            request: models.ListProjectMembersRequest,
            opts: Dict = None,
    ) -> models.ListProjectMembersResponse:
        """
        获取项目下的用户，分页返回
        """
        
        kwargs = {}
        kwargs["action"] = "ListProjectMembers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProjectMembersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProjectRoles(
            self,
            request: models.ListProjectRolesRequest,
            opts: Dict = None,
    ) -> models.ListProjectRolesResponse:
        """
        获取角色列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListProjectRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProjectRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListProjects(
            self,
            request: models.ListProjectsRequest,
            opts: Dict = None,
    ) -> models.ListProjectsResponse:
        """
        租户全局范围的项目列表，与用户查看范围无关.
        """
        
        kwargs = {}
        kwargs["action"] = "ListProjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListProjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceFiles(
            self,
            request: models.ListResourceFilesRequest,
            opts: Dict = None,
    ) -> models.ListResourceFilesResponse:
        """
        获取资源文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceFolders(
            self,
            request: models.ListResourceFoldersRequest,
            opts: Dict = None,
    ) -> models.ListResourceFoldersResponse:
        """
        查询资源文件文件夹列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceFolders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceFoldersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListResourceGroups(
            self,
            request: models.ListResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.ListResourceGroupsResponse:
        """
        该接口用于查询执行资源组列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListResourceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListResourceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSQLFolderContents(
            self,
            request: models.ListSQLFolderContentsRequest,
            opts: Dict = None,
    ) -> models.ListSQLFolderContentsResponse:
        """
        查询数据探索文件夹树，包括文件夹下的脚本
        """
        
        kwargs = {}
        kwargs["action"] = "ListSQLFolderContents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSQLFolderContentsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSQLScriptRuns(
            self,
            request: models.ListSQLScriptRunsRequest,
            opts: Dict = None,
    ) -> models.ListSQLScriptRunsResponse:
        """
        查询SQL运行记录
        """
        
        kwargs = {}
        kwargs["action"] = "ListSQLScriptRuns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSQLScriptRunsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListSchema(
            self,
            request: models.ListSchemaRequest,
            opts: Dict = None,
    ) -> models.ListSchemaResponse:
        """
        获取资产数据库Schema信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListSchema"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListSchemaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTable(
            self,
            request: models.ListTableRequest,
            opts: Dict = None,
    ) -> models.ListTableResponse:
        """
        获取资产表信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskInstanceExecutions(
            self,
            request: models.ListTaskInstanceExecutionsRequest,
            opts: Dict = None,
    ) -> models.ListTaskInstanceExecutionsResponse:
        """
        调度实例详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskInstanceExecutions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskInstanceExecutionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskInstances(
            self,
            request: models.ListTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.ListTaskInstancesResponse:
        """
        获取实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskVersions(
            self,
            request: models.ListTaskVersionsRequest,
            opts: Dict = None,
    ) -> models.ListTaskVersionsResponse:
        """
        任务保存版本列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTasks(
            self,
            request: models.ListTasksRequest,
            opts: Dict = None,
    ) -> models.ListTasksResponse:
        """
        查询任务分页信息
        """
        
        kwargs = {}
        kwargs["action"] = "ListTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTenantRoles(
            self,
            request: models.ListTenantRolesRequest,
            opts: Dict = None,
    ) -> models.ListTenantRolesResponse:
        """
        获取所有主账号角色列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTenantRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTenantRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUpstreamOpsTasks(
            self,
            request: models.ListUpstreamOpsTasksRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamOpsTasksResponse:
        """
        获取任务直接上游
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUpstreamTaskInstances(
            self,
            request: models.ListUpstreamTaskInstancesRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamTaskInstancesResponse:
        """
        获取实例直接上游
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamTaskInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamTaskInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListUpstreamTasks(
            self,
            request: models.ListUpstreamTasksRequest,
            opts: Dict = None,
    ) -> models.ListUpstreamTasksResponse:
        """
        获取任务直接上游
        """
        
        kwargs = {}
        kwargs["action"] = "ListUpstreamTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListUpstreamTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflowFolders(
            self,
            request: models.ListWorkflowFoldersRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowFoldersResponse:
        """
        查询文件夹列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflowFolders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowFoldersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListWorkflows(
            self,
            request: models.ListWorkflowsRequest,
            opts: Dict = None,
    ) -> models.ListWorkflowsResponse:
        """
        查询工作流列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListWorkflows"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListWorkflowsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseOpsTasksAsync(
            self,
            request: models.PauseOpsTasksAsyncRequest,
            opts: Dict = None,
    ) -> models.PauseOpsTasksAsyncResponse:
        """
        异步批量暂停任务
        """
        
        kwargs = {}
        kwargs["action"] = "PauseOpsTasksAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseOpsTasksAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterLineage(
            self,
            request: models.RegisterLineageRequest,
            opts: Dict = None,
    ) -> models.RegisterLineageResponse:
        """
        RegisterLineage
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterLineage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterLineageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveMemberProjectRole(
            self,
            request: models.RemoveMemberProjectRoleRequest,
            opts: Dict = None,
    ) -> models.RemoveMemberProjectRoleResponse:
        """
        删除项目用户角色
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveMemberProjectRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveMemberProjectRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RerunTaskInstancesAsync(
            self,
            request: models.RerunTaskInstancesAsyncRequest,
            opts: Dict = None,
    ) -> models.RerunTaskInstancesAsyncResponse:
        """
        实例批量重跑-异步
        """
        
        kwargs = {}
        kwargs["action"] = "RerunTaskInstancesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RerunTaskInstancesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunSQLScript(
            self,
            request: models.RunSQLScriptRequest,
            opts: Dict = None,
    ) -> models.RunSQLScriptResponse:
        """
        运行SQL脚本
        """
        
        kwargs = {}
        kwargs["action"] = "RunSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetSuccessTaskInstancesAsync(
            self,
            request: models.SetSuccessTaskInstancesAsyncRequest,
            opts: Dict = None,
    ) -> models.SetSuccessTaskInstancesAsyncResponse:
        """
        实例批量置成功-异步
        """
        
        kwargs = {}
        kwargs["action"] = "SetSuccessTaskInstancesAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetSuccessTaskInstancesAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartOpsTasks(
            self,
            request: models.StartOpsTasksRequest,
            opts: Dict = None,
    ) -> models.StartOpsTasksResponse:
        """
        异步批量启动任务
        """
        
        kwargs = {}
        kwargs["action"] = "StartOpsTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartOpsTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopOpsTasksAsync(
            self,
            request: models.StopOpsTasksAsyncRequest,
            opts: Dict = None,
    ) -> models.StopOpsTasksAsyncResponse:
        """
        异步批量下线任务
        """
        
        kwargs = {}
        kwargs["action"] = "StopOpsTasksAsync"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopOpsTasksAsyncResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopSQLScriptRun(
            self,
            request: models.StopSQLScriptRunRequest,
            opts: Dict = None,
    ) -> models.StopSQLScriptRunResponse:
        """
        停止运行SQL脚本
        """
        
        kwargs = {}
        kwargs["action"] = "StopSQLScriptRun"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopSQLScriptRunResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitTask(
            self,
            request: models.SubmitTaskRequest,
            opts: Dict = None,
    ) -> models.SubmitTaskResponse:
        """
        提交任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCodeFile(
            self,
            request: models.UpdateCodeFileRequest,
            opts: Dict = None,
    ) -> models.UpdateCodeFileResponse:
        """
        更新代码文件
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCodeFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCodeFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCodeFolder(
            self,
            request: models.UpdateCodeFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateCodeFolderResponse:
        """
        重命名代码文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCodeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCodeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataSource(
            self,
            request: models.UpdateDataSourceRequest,
            opts: Dict = None,
    ) -> models.UpdateDataSourceResponse:
        """
        该接口用于更新数据源
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataSource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataSourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOpsAlarmRule(
            self,
            request: models.UpdateOpsAlarmRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateOpsAlarmRuleResponse:
        """
        修改告警规则
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOpsAlarmRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOpsAlarmRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateOpsTasksOwner(
            self,
            request: models.UpdateOpsTasksOwnerRequest,
            opts: Dict = None,
    ) -> models.UpdateOpsTasksOwnerResponse:
        """
        修改任务负责人
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateOpsTasksOwner"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateOpsTasksOwnerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateProject(
            self,
            request: models.UpdateProjectRequest,
            opts: Dict = None,
    ) -> models.UpdateProjectResponse:
        """
        修改项目基础信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceFile(
            self,
            request: models.UpdateResourceFileRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceFileResponse:
        """
        更新资源文件
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceFile"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceFileResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceFolder(
            self,
            request: models.UpdateResourceFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceFolderResponse:
        """
        更新资源文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateResourceGroup(
            self,
            request: models.UpdateResourceGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateResourceGroupResponse:
        """
        该接口用于变配/续费资源
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSQLFolder(
            self,
            request: models.UpdateSQLFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateSQLFolderResponse:
        """
        重命名SQL文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSQLFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSQLFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateSQLScript(
            self,
            request: models.UpdateSQLScriptRequest,
            opts: Dict = None,
    ) -> models.UpdateSQLScriptResponse:
        """
        保存探索脚本内容
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateSQLScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateSQLScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTask(
            self,
            request: models.UpdateTaskRequest,
            opts: Dict = None,
    ) -> models.UpdateTaskResponse:
        """
        更新任务接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflow(
            self,
            request: models.UpdateWorkflowRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowResponse:
        """
        更新工作流（包括工作流基本信息与工作流参数）
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateWorkflowFolder(
            self,
            request: models.UpdateWorkflowFolderRequest,
            opts: Dict = None,
    ) -> models.UpdateWorkflowFolderResponse:
        """
        更新工作流文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateWorkflowFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateWorkflowFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)