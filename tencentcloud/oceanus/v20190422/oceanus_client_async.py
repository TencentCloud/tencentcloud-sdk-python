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
from tencentcloud.oceanus.v20190422 import models
from typing import Dict


class OceanusClient(AbstractClient):
    _apiVersion = '2019-04-22'
    _endpoint = 'oceanus.tencentcloudapi.com'
    _service = 'oceanus'

    async def CheckConnectorName(
            self,
            request: models.CheckConnectorNameRequest,
            opts: Dict = None,
    ) -> models.CheckConnectorNameResponse:
        """
        查询资源名是否重复
        """
        
        kwargs = {}
        kwargs["action"] = "CheckConnectorName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckConnectorNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckSavepoint(
            self,
            request: models.CheckSavepointRequest,
            opts: Dict = None,
    ) -> models.CheckSavepointResponse:
        """
        检查快照是否可用
        """
        
        kwargs = {}
        kwargs["action"] = "CheckSavepoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckSavepointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CopyJobs(
            self,
            request: models.CopyJobsRequest,
            opts: Dict = None,
    ) -> models.CopyJobsResponse:
        """
        单条和批量复制作业
        """
        
        kwargs = {}
        kwargs["action"] = "CopyJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CopyJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateConnector(
            self,
            request: models.CreateConnectorRequest,
            opts: Dict = None,
    ) -> models.CreateConnectorResponse:
        """
        创建Connector
        """
        
        kwargs = {}
        kwargs["action"] = "CreateConnector"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateConnectorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFolder(
            self,
            request: models.CreateFolderRequest,
            opts: Dict = None,
    ) -> models.CreateFolderResponse:
        """
        作业列表页面新建文件夹请求
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJob(
            self,
            request: models.CreateJobRequest,
            opts: Dict = None,
    ) -> models.CreateJobResponse:
        """
        新建作业接口，一个 AppId 最多允许创建1000个作业
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateJobConfig(
            self,
            request: models.CreateJobConfigRequest,
            opts: Dict = None,
    ) -> models.CreateJobConfigResponse:
        """
        创建作业配置，一个作业最多有100个配置版本
        """
        
        kwargs = {}
        kwargs["action"] = "CreateJobConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateJobConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResource(
            self,
            request: models.CreateResourceRequest,
            opts: Dict = None,
    ) -> models.CreateResourceResponse:
        """
        创建资源接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResourceConfig(
            self,
            request: models.CreateResourceConfigRequest,
            opts: Dict = None,
    ) -> models.CreateResourceConfigResponse:
        """
        创建资源配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResourceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResourceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVariable(
            self,
            request: models.CreateVariableRequest,
            opts: Dict = None,
    ) -> models.CreateVariableResponse:
        """
        创建变量
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVariable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVariableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkSpace(
            self,
            request: models.CreateWorkSpaceRequest,
            opts: Dict = None,
    ) -> models.CreateWorkSpaceResponse:
        """
        创建工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFolders(
            self,
            request: models.DeleteFoldersRequest,
            opts: Dict = None,
    ) -> models.DeleteFoldersResponse:
        """
        作业列表删除文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFolders"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFoldersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJobConfigs(
            self,
            request: models.DeleteJobConfigsRequest,
            opts: Dict = None,
    ) -> models.DeleteJobConfigsResponse:
        """
        删除作业配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJobConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJobs(
            self,
            request: models.DeleteJobsRequest,
            opts: Dict = None,
    ) -> models.DeleteJobsResponse:
        """
        批量删除作业接口，批量操作数量上限20
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResourceConfigs(
            self,
            request: models.DeleteResourceConfigsRequest,
            opts: Dict = None,
    ) -> models.DeleteResourceConfigsResponse:
        """
        删除资源版本
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResourceConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourceConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteResources(
            self,
            request: models.DeleteResourcesRequest,
            opts: Dict = None,
    ) -> models.DeleteResourcesResponse:
        """
        删除资源接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableConfig(
            self,
            request: models.DeleteTableConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteTableConfigResponse:
        """
        删除作业表配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkSpace(
            self,
            request: models.DeleteWorkSpaceRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkSpaceResponse:
        """
        删除工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        查询集群
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFolder(
            self,
            request: models.DescribeFolderRequest,
            opts: Dict = None,
    ) -> models.DescribeFolderResponse:
        """
        查询指定文件夹及其相应的子文件夹信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobConfigs(
            self,
            request: models.DescribeJobConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobConfigsResponse:
        """
        查询作业配置列表，一次最多查询100个
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobEvents(
            self,
            request: models.DescribeJobEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobEventsResponse:
        """
        请求参数不包含 "RunningOrderIds"时，接口获取指定作业的事件，包括作业启动停止、运行失败、快照失败、作业异常等各种事件类型;请求参数不包含 "RunningOrderIds"时，接口为查询作业实例ID接口,获取作业实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobRuntimeInfo(
            self,
            request: models.DescribeJobRuntimeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJobRuntimeInfoResponse:
        """
        获取作业运行时的信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobRuntimeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobRuntimeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobSavepoint(
            self,
            request: models.DescribeJobSavepointRequest,
            opts: Dict = None,
    ) -> models.DescribeJobSavepointResponse:
        """
        查找Savepoint列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobSavepoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobSavepointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobSubmissionLog(
            self,
            request: models.DescribeJobSubmissionLogRequest,
            opts: Dict = None,
    ) -> models.DescribeJobSubmissionLogResponse:
        """
        查询作业实例启动日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobSubmissionLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobSubmissionLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        查询作业
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceConfigs(
            self,
            request: models.DescribeResourceConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceConfigsResponse:
        """
        描述资源配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceRelatedJobs(
            self,
            request: models.DescribeResourceRelatedJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceRelatedJobsResponse:
        """
        获取资源关联作业信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceRelatedJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceRelatedJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResources(
            self,
            request: models.DescribeResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesResponse:
        """
        描述资源接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSystemResources(
            self,
            request: models.DescribeSystemResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeSystemResourcesResponse:
        """
        描述系统资源接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSystemResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSystemResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTreeJobs(
            self,
            request: models.DescribeTreeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeTreeJobsResponse:
        """
        生成树状作业显示结构
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTreeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTreeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTreeResources(
            self,
            request: models.DescribeTreeResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeTreeResourcesResponse:
        """
        查询树状结构资源列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTreeResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTreeResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVariables(
            self,
            request: models.DescribeVariablesRequest,
            opts: Dict = None,
    ) -> models.DescribeVariablesResponse:
        """
        变量列表展示
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVariables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVariablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkSpaces(
            self,
            request: models.DescribeWorkSpacesRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkSpacesResponse:
        """
        授权工作空间列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkSpaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkSpacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FetchSqlGatewayStatementResult(
            self,
            request: models.FetchSqlGatewayStatementResultRequest,
            opts: Dict = None,
    ) -> models.FetchSqlGatewayStatementResultResponse:
        """
        查询Sql Gateway的Statement执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "FetchSqlGatewayStatementResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FetchSqlGatewayStatementResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetMetaTable(
            self,
            request: models.GetMetaTableRequest,
            opts: Dict = None,
    ) -> models.GetMetaTableResponse:
        """
        查询元数据表
        """
        
        kwargs = {}
        kwargs["action"] = "GetMetaTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetMetaTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConnector(
            self,
            request: models.ModifyConnectorRequest,
            opts: Dict = None,
    ) -> models.ModifyConnectorResponse:
        """
        修改Connector
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConnector"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConnectorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFolder(
            self,
            request: models.ModifyFolderRequest,
            opts: Dict = None,
    ) -> models.ModifyFolderResponse:
        """
        自定义树状结构页面拖拽文件夹
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFolder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFolderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyJob(
            self,
            request: models.ModifyJobRequest,
            opts: Dict = None,
    ) -> models.ModifyJobResponse:
        """
        更新作业属性，仅允许以下3种操作，不支持组合操作：
        (1)	更新作业名称
        (2)	更新作业备注
        (3)	更新作业最大并行度
        变更前提：WorkerCuNum<=MaxParallelism
        如果MaxParallelism变小，不重启作业，待下一次重启生效
        如果MaxParallelism变大，则要求入参RestartAllowed必须为True
        假设作业运行状态，则先停止作业，再启动作业，中间状态丢失
        假设作业暂停状态，则将作业更改为停止状态，中间状态丢失
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkSpace(
            self,
            request: models.ModifyWorkSpaceRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkSpaceResponse:
        """
        修改工作空间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkSpace"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkSpaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ParseConnector(
            self,
            request: models.ParseConnectorRequest,
            opts: Dict = None,
    ) -> models.ParseConnectorResponse:
        """
        解析用户上传connector
        """
        
        kwargs = {}
        kwargs["action"] = "ParseConnector"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ParseConnectorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunJobs(
            self,
            request: models.RunJobsRequest,
            opts: Dict = None,
    ) -> models.RunJobsResponse:
        """
        批量启动或者恢复作业，批量操作数量上限20
        """
        
        kwargs = {}
        kwargs["action"] = "RunJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunSqlGatewayStatement(
            self,
            request: models.RunSqlGatewayStatementRequest,
            opts: Dict = None,
    ) -> models.RunSqlGatewayStatementResponse:
        """
        通过Sql gateway执行satement
        """
        
        kwargs = {}
        kwargs["action"] = "RunSqlGatewayStatement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunSqlGatewayStatementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopJobs(
            self,
            request: models.StopJobsRequest,
            opts: Dict = None,
    ) -> models.StopJobsResponse:
        """
        批量停止作业，批量操作数量上限为20
        """
        
        kwargs = {}
        kwargs["action"] = "StopJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TriggerJobSavepoint(
            self,
            request: models.TriggerJobSavepointRequest,
            opts: Dict = None,
    ) -> models.TriggerJobSavepointResponse:
        """
        触发Savepoint
        """
        
        kwargs = {}
        kwargs["action"] = "TriggerJobSavepoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TriggerJobSavepointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)