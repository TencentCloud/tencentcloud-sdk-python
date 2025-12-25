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
from tencentcloud.dlc.v20210125 import models
from typing import Dict


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.tencentcloudapi.com'
    _service = 'dlc'

    async def AddDMSPartitions(
            self,
            request: models.AddDMSPartitionsRequest,
            opts: Dict = None,
    ) -> models.AddDMSPartitionsResponse:
        """
        DMS元数据新增分区
        """
        
        kwargs = {}
        kwargs["action"] = "AddDMSPartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddDMSPartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddOptimizerEngines(
            self,
            request: models.AddOptimizerEnginesRequest,
            opts: Dict = None,
    ) -> models.AddOptimizerEnginesResponse:
        """
        添加数据优化资源
        """
        
        kwargs = {}
        kwargs["action"] = "AddOptimizerEngines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddOptimizerEnginesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUsersToWorkGroup(
            self,
            request: models.AddUsersToWorkGroupRequest,
            opts: Dict = None,
    ) -> models.AddUsersToWorkGroupResponse:
        """
        添加用户到工作组
        """
        
        kwargs = {}
        kwargs["action"] = "AddUsersToWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUsersToWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AlterDMSDatabase(
            self,
            request: models.AlterDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.AlterDMSDatabaseResponse:
        """
        DMS元数据更新库
        """
        
        kwargs = {}
        kwargs["action"] = "AlterDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AlterDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AlterDMSPartition(
            self,
            request: models.AlterDMSPartitionRequest,
            opts: Dict = None,
    ) -> models.AlterDMSPartitionResponse:
        """
        DMS元数据更新分区
        """
        
        kwargs = {}
        kwargs["action"] = "AlterDMSPartition"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AlterDMSPartitionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AlterDMSTable(
            self,
            request: models.AlterDMSTableRequest,
            opts: Dict = None,
    ) -> models.AlterDMSTableResponse:
        """
        DMS元数据更新表
        """
        
        kwargs = {}
        kwargs["action"] = "AlterDMSTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AlterDMSTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignMangedTableProperties(
            self,
            request: models.AssignMangedTablePropertiesRequest,
            opts: Dict = None,
    ) -> models.AssignMangedTablePropertiesResponse:
        """
        分配原生表表属性
        """
        
        kwargs = {}
        kwargs["action"] = "AssignMangedTableProperties"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignMangedTablePropertiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateDatasourceHouse(
            self,
            request: models.AssociateDatasourceHouseRequest,
            opts: Dict = None,
    ) -> models.AssociateDatasourceHouseResponse:
        """
        绑定数据源和队列
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDatasourceHouse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDatasourceHouseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDataMaskPolicy(
            self,
            request: models.AttachDataMaskPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachDataMaskPolicyResponse:
        """
        绑定数据脱敏策略
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDataMaskPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDataMaskPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachUserPolicy(
            self,
            request: models.AttachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachUserPolicyResponse:
        """
        绑定鉴权策略到用户
        """
        
        kwargs = {}
        kwargs["action"] = "AttachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachWorkGroupPolicy(
            self,
            request: models.AttachWorkGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.AttachWorkGroupPolicyResponse:
        """
        绑定鉴权策略到工作组
        """
        
        kwargs = {}
        kwargs["action"] = "AttachWorkGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachWorkGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindWorkGroupsToUser(
            self,
            request: models.BindWorkGroupsToUserRequest,
            opts: Dict = None,
    ) -> models.BindWorkGroupsToUserResponse:
        """
        绑定工作组到用户
        """
        
        kwargs = {}
        kwargs["action"] = "BindWorkGroupsToUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindWorkGroupsToUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelNotebookSessionStatement(
            self,
            request: models.CancelNotebookSessionStatementRequest,
            opts: Dict = None,
    ) -> models.CancelNotebookSessionStatementResponse:
        """
        本接口（CancelNotebookSessionStatement）用于取消session中执行的任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelNotebookSessionStatement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelNotebookSessionStatementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelNotebookSessionStatementBatch(
            self,
            request: models.CancelNotebookSessionStatementBatchRequest,
            opts: Dict = None,
    ) -> models.CancelNotebookSessionStatementBatchResponse:
        """
        本接口（CancelNotebookSessionStatementBatch）用于批量取消Session 中执行的任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelNotebookSessionStatementBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelNotebookSessionStatementBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelSparkSessionBatchSQL(
            self,
            request: models.CancelSparkSessionBatchSQLRequest,
            opts: Dict = None,
    ) -> models.CancelSparkSessionBatchSQLResponse:
        """
        本接口（CancelSparkSessionBatchSQL）用于取消Spark SQL批任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CancelSparkSessionBatchSQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelSparkSessionBatchSQLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelTask(
            self,
            request: models.CancelTaskRequest,
            opts: Dict = None,
    ) -> models.CancelTaskResponse:
        """
        本接口（CancelTask），用于取消任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelTasks(
            self,
            request: models.CancelTasksRequest,
            opts: Dict = None,
    ) -> models.CancelTasksResponse:
        """
        批量取消任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDataEngineConfigPairsValidity(
            self,
            request: models.CheckDataEngineConfigPairsValidityRequest,
            opts: Dict = None,
    ) -> models.CheckDataEngineConfigPairsValidityResponse:
        """
        本接口（CheckDataEngineConfigPairsValidity）用于检查引擎用户自定义参数的有效性
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDataEngineConfigPairsValidity"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDataEngineConfigPairsValidityResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDataEngineImageCanBeRollback(
            self,
            request: models.CheckDataEngineImageCanBeRollbackRequest,
            opts: Dict = None,
    ) -> models.CheckDataEngineImageCanBeRollbackResponse:
        """
        本接口（CheckDataEngineImageCanBeRollback）用于查看集群是否能回滚。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDataEngineImageCanBeRollback"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDataEngineImageCanBeRollbackResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDataEngineImageCanBeUpgrade(
            self,
            request: models.CheckDataEngineImageCanBeUpgradeRequest,
            opts: Dict = None,
    ) -> models.CheckDataEngineImageCanBeUpgradeResponse:
        """
        本接口（CheckDataEngineImageCanBeUpgrade）用于查看集群镜像是否能够升级。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDataEngineImageCanBeUpgrade"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDataEngineImageCanBeUpgradeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckLockMetaData(
            self,
            request: models.CheckLockMetaDataRequest,
            opts: Dict = None,
    ) -> models.CheckLockMetaDataResponse:
        """
        元数据锁检查
        """
        
        kwargs = {}
        kwargs["action"] = "CheckLockMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckLockMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCHDFSBindingProduct(
            self,
            request: models.CreateCHDFSBindingProductRequest,
            opts: Dict = None,
    ) -> models.CreateCHDFSBindingProductResponse:
        """
        此接口（CreateCHDFSBindingProduct）用于创建元数据加速桶和产品绑定关系
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCHDFSBindingProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCHDFSBindingProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDMSDatabase(
            self,
            request: models.CreateDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDMSDatabaseResponse:
        """
        DMS元数据创建库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDMSTable(
            self,
            request: models.CreateDMSTableRequest,
            opts: Dict = None,
    ) -> models.CreateDMSTableResponse:
        """
        DMS元数据创建表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDMSTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDMSTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataEngine(
            self,
            request: models.CreateDataEngineRequest,
            opts: Dict = None,
    ) -> models.CreateDataEngineResponse:
        """
        为用户创建数据引擎
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataMaskStrategy(
            self,
            request: models.CreateDataMaskStrategyRequest,
            opts: Dict = None,
    ) -> models.CreateDataMaskStrategyResponse:
        """
        创建数据脱敏策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataMaskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataMaskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDatabase(
            self,
            request: models.CreateDatabaseRequest,
            opts: Dict = None,
    ) -> models.CreateDatabaseResponse:
        """
        本接口（CreateDatabase）用于生成建库SQL语句。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateExportTask(
            self,
            request: models.CreateExportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateExportTaskResponse:
        """
        该接口（CreateExportTask）用于创建导出任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateExportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateExportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImportTask(
            self,
            request: models.CreateImportTaskRequest,
            opts: Dict = None,
    ) -> models.CreateImportTaskResponse:
        """
        该接口（CreateImportTask）用于创建导入任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImportTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImportTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInternalTable(
            self,
            request: models.CreateInternalTableRequest,
            opts: Dict = None,
    ) -> models.CreateInternalTableResponse:
        """
        创建托管存储内表（该接口已废弃）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInternalTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInternalTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotebookSession(
            self,
            request: models.CreateNotebookSessionRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookSessionResponse:
        """
        本接口（CreateNotebookSession）用于创建交互式session（notebook）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebookSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotebookSessionStatement(
            self,
            request: models.CreateNotebookSessionStatementRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookSessionStatementResponse:
        """
        本接口（CreateNotebookSessionStatement）用于在session中执行代码片段
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebookSessionStatement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookSessionStatementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNotebookSessionStatementSupportBatchSQL(
            self,
            request: models.CreateNotebookSessionStatementSupportBatchSQLRequest,
            opts: Dict = None,
    ) -> models.CreateNotebookSessionStatementSupportBatchSQLResponse:
        """
        本接口（CreateNotebookSessionStatementSupportBatchSQL）用于创建交互式session并执行SQL任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNotebookSessionStatementSupportBatchSQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNotebookSessionStatementSupportBatchSQLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateResultDownload(
            self,
            request: models.CreateResultDownloadRequest,
            opts: Dict = None,
    ) -> models.CreateResultDownloadResponse:
        """
        创建查询结果下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateResultDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateResultDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateScript(
            self,
            request: models.CreateScriptRequest,
            opts: Dict = None,
    ) -> models.CreateScriptResponse:
        """
        该接口（CreateScript）用于创建sql脚本。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkApp(
            self,
            request: models.CreateSparkAppRequest,
            opts: Dict = None,
    ) -> models.CreateSparkAppResponse:
        """
        创建spark作业
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkAppTask(
            self,
            request: models.CreateSparkAppTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSparkAppTaskResponse:
        """
        启动Spark作业
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkAppTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkAppTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkSessionBatchSQL(
            self,
            request: models.CreateSparkSessionBatchSQLRequest,
            opts: Dict = None,
    ) -> models.CreateSparkSessionBatchSQLResponse:
        """
        本接口（CreateSparkSessionBatchSQL）用于向Spark作业引擎提交Spark SQL批任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkSessionBatchSQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkSessionBatchSQLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSparkSubmitTask(
            self,
            request: models.CreateSparkSubmitTaskRequest,
            opts: Dict = None,
    ) -> models.CreateSparkSubmitTaskResponse:
        """
        本接口（CreateSparkSubmitTask）用于提交SparkSbumit批流任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSparkSubmitTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSparkSubmitTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStandardEngineResourceGroup(
            self,
            request: models.CreateStandardEngineResourceGroupRequest,
            opts: Dict = None,
    ) -> models.CreateStandardEngineResourceGroupResponse:
        """
        创建标准引擎资源组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStandardEngineResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStandardEngineResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateStoreLocation(
            self,
            request: models.CreateStoreLocationRequest,
            opts: Dict = None,
    ) -> models.CreateStoreLocationResponse:
        """
        该接口（CreateStoreLocation）新增或覆盖计算结果存储位置。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTable(
            self,
            request: models.CreateTableRequest,
            opts: Dict = None,
    ) -> models.CreateTableResponse:
        """
        本接口（CreateTable）用于生成建表SQL。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTask(
            self,
            request: models.CreateTaskRequest,
            opts: Dict = None,
    ) -> models.CreateTaskResponse:
        """
        本接口（CreateTask）用于创建并执行SQL任务。（推荐使用CreateTasks接口）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTasks(
            self,
            request: models.CreateTasksRequest,
            opts: Dict = None,
    ) -> models.CreateTasksResponse:
        """
        本接口（CreateTasks），用于批量创建并执行SQL任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTasksInOrder(
            self,
            request: models.CreateTasksInOrderRequest,
            opts: Dict = None,
    ) -> models.CreateTasksInOrderResponse:
        """
        废弃接口，申请下线

        按顺序创建任务（已经废弃，后期不再维护，请使用接口CreateTasks）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTasksInOrder"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTasksInOrderResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTcIcebergTable(
            self,
            request: models.CreateTcIcebergTableRequest,
            opts: Dict = None,
    ) -> models.CreateTcIcebergTableResponse:
        """
        创建TIceberg表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTcIcebergTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTcIcebergTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUser(
            self,
            request: models.CreateUserRequest,
            opts: Dict = None,
    ) -> models.CreateUserResponse:
        """
        创建用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUserVpcConnection(
            self,
            request: models.CreateUserVpcConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateUserVpcConnectionResponse:
        """
        创建用户vpc连接到指定引擎网络
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUserVpcConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUserVpcConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkGroup(
            self,
            request: models.CreateWorkGroupRequest,
            opts: Dict = None,
    ) -> models.CreateWorkGroupResponse:
        """
        创建工作组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCHDFSBindingProduct(
            self,
            request: models.DeleteCHDFSBindingProductRequest,
            opts: Dict = None,
    ) -> models.DeleteCHDFSBindingProductResponse:
        """
        此接口（DeleteCHDFSBindingProduct）用于删除元数据加速桶和产品绑定关系
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCHDFSBindingProduct"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCHDFSBindingProductResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataEngine(
            self,
            request: models.DeleteDataEngineRequest,
            opts: Dict = None,
    ) -> models.DeleteDataEngineResponse:
        """
        删除数据引擎
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataMaskStrategy(
            self,
            request: models.DeleteDataMaskStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteDataMaskStrategyResponse:
        """
        删除数据脱敏策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataMaskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataMaskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNativeSparkSession(
            self,
            request: models.DeleteNativeSparkSessionRequest,
            opts: Dict = None,
    ) -> models.DeleteNativeSparkSessionResponse:
        """
        根据spark session名称销毁eg spark session
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNativeSparkSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNativeSparkSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNotebookSession(
            self,
            request: models.DeleteNotebookSessionRequest,
            opts: Dict = None,
    ) -> models.DeleteNotebookSessionResponse:
        """
        本接口（DeleteNotebookSession）用于删除交互式session（notebook）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNotebookSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNotebookSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteScript(
            self,
            request: models.DeleteScriptRequest,
            opts: Dict = None,
    ) -> models.DeleteScriptResponse:
        """
        该接口（DeleteScript）用于删除sql脚本。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScript"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScriptResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSparkApp(
            self,
            request: models.DeleteSparkAppRequest,
            opts: Dict = None,
    ) -> models.DeleteSparkAppResponse:
        """
        删除spark作业
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSparkApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSparkAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteStandardEngineResourceGroup(
            self,
            request: models.DeleteStandardEngineResourceGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteStandardEngineResourceGroupResponse:
        """
        删除标准引擎资源组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteStandardEngineResourceGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteStandardEngineResourceGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTable(
            self,
            request: models.DeleteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteTableResponse:
        """
        删除表
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteThirdPartyAccessUser(
            self,
            request: models.DeleteThirdPartyAccessUserRequest,
            opts: Dict = None,
    ) -> models.DeleteThirdPartyAccessUserResponse:
        """
        本接口（RegisterThirdPartyAccessUser）用于移除第三方平台访问
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteThirdPartyAccessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteThirdPartyAccessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUser(
            self,
            request: models.DeleteUserRequest,
            opts: Dict = None,
    ) -> models.DeleteUserResponse:
        """
        删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserVpcConnection(
            self,
            request: models.DeleteUserVpcConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteUserVpcConnectionResponse:
        """
        删除用户vpc到引擎网络的连接
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserVpcConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserVpcConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsersFromWorkGroup(
            self,
            request: models.DeleteUsersFromWorkGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersFromWorkGroupResponse:
        """
        从工作组中删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsersFromWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersFromWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkGroup(
            self,
            request: models.DeleteWorkGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkGroupResponse:
        """
        删除工作组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAdvancedStoreLocation(
            self,
            request: models.DescribeAdvancedStoreLocationRequest,
            opts: Dict = None,
    ) -> models.DescribeAdvancedStoreLocationResponse:
        """
        查询sql查询界面高级设置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAdvancedStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAdvancedStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterMonitorInfos(
            self,
            request: models.DescribeClusterMonitorInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterMonitorInfosResponse:
        """
        查询任务监控指标信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterMonitorInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterMonitorInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDLCCatalogAccess(
            self,
            request: models.DescribeDLCCatalogAccessRequest,
            opts: Dict = None,
    ) -> models.DescribeDLCCatalogAccessResponse:
        """
        查询DLC Catalog授权列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDLCCatalogAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDLCCatalogAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDMSDatabase(
            self,
            request: models.DescribeDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.DescribeDMSDatabaseResponse:
        """
        DMS元数据获取库
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDMSPartitions(
            self,
            request: models.DescribeDMSPartitionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDMSPartitionsResponse:
        """
        DMS元数据获取分区
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDMSPartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDMSPartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDMSTable(
            self,
            request: models.DescribeDMSTableRequest,
            opts: Dict = None,
    ) -> models.DescribeDMSTableResponse:
        """
        DMS元数据获取表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDMSTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDMSTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDMSTables(
            self,
            request: models.DescribeDMSTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeDMSTablesResponse:
        """
        DMS元数据获取表列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDMSTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDMSTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngine(
            self,
            request: models.DescribeDataEngineRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEngineResponse:
        """
        本接口根据名称用于获取数据引擎详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngineEvents(
            self,
            request: models.DescribeDataEngineEventsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEngineEventsResponse:
        """
        查询数据引擎事件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngineEvents"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEngineEventsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngineImageVersions(
            self,
            request: models.DescribeDataEngineImageVersionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEngineImageVersionsResponse:
        """
        本接口（DescribeDataEngineImageVersions）用于获取独享集群大版本镜像列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngineImageVersions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEngineImageVersionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEnginePythonSparkImages(
            self,
            request: models.DescribeDataEnginePythonSparkImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEnginePythonSparkImagesResponse:
        """
        本接口（DescribeDataEnginePythonSparkImages）用于获取PYSPARK镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEnginePythonSparkImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEnginePythonSparkImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngineSessionParameters(
            self,
            request: models.DescribeDataEngineSessionParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEngineSessionParametersResponse:
        """
        本接口（DescribeDataEngineSessionParameters）用于获取指定小版本下的Session配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngineSessionParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEngineSessionParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEngines(
            self,
            request: models.DescribeDataEnginesRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEnginesResponse:
        """
        本接口（DescribeDataEngines）用于查询DataEngines信息列表.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEngines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEnginesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataEnginesScaleDetail(
            self,
            request: models.DescribeDataEnginesScaleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDataEnginesScaleDetailResponse:
        """
        查询引擎规格详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataEnginesScaleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataEnginesScaleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataMaskStrategies(
            self,
            request: models.DescribeDataMaskStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeDataMaskStrategiesResponse:
        """
        查询数据脱敏列表接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataMaskStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataMaskStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        本接口（DescribeDatabases）用于查询数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatasourceConnection(
            self,
            request: models.DescribeDatasourceConnectionRequest,
            opts: Dict = None,
    ) -> models.DescribeDatasourceConnectionResponse:
        """
        本接口（DescribeDatasourceConnection）用于查询数据源信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatasourceConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatasourceConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEngineNetworks(
            self,
            request: models.DescribeEngineNetworksRequest,
            opts: Dict = None,
    ) -> models.DescribeEngineNetworksResponse:
        """
        查询引擎网络信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEngineNetworks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEngineNetworksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEngineNodeSpec(
            self,
            request: models.DescribeEngineNodeSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeEngineNodeSpecResponse:
        """
        查询引擎可用的节点规格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEngineNodeSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEngineNodeSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEngineUsageInfo(
            self,
            request: models.DescribeEngineUsageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeEngineUsageInfoResponse:
        """
        本接口根据引擎ID查询数据引擎资源使用情况
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEngineUsageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEngineUsageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeForbiddenTablePro(
            self,
            request: models.DescribeForbiddenTableProRequest,
            opts: Dict = None,
    ) -> models.DescribeForbiddenTableProResponse:
        """
        本接口（DescribeForbiddenTablePro）用于查询被禁用的表属性列表（新）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeForbiddenTablePro"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeForbiddenTableProResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLakeFsDirSummary(
            self,
            request: models.DescribeLakeFsDirSummaryRequest,
            opts: Dict = None,
    ) -> models.DescribeLakeFsDirSummaryResponse:
        """
        查询托管存储指定目录的Summary
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLakeFsDirSummary"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLakeFsDirSummaryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLakeFsInfo(
            self,
            request: models.DescribeLakeFsInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLakeFsInfoResponse:
        """
        查询用户的托管存储信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLakeFsInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLakeFsInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLakeFsTaskResult(
            self,
            request: models.DescribeLakeFsTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeLakeFsTaskResultResponse:
        """
        获取LakeFs上task执行结果访问信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLakeFsTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLakeFsTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNativeSparkSessions(
            self,
            request: models.DescribeNativeSparkSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribeNativeSparkSessionsResponse:
        """
        根据资源组获取spark session列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNativeSparkSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNativeSparkSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkConnections(
            self,
            request: models.DescribeNetworkConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkConnectionsResponse:
        """
        查询网络配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSession(
            self,
            request: models.DescribeNotebookSessionRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSessionResponse:
        """
        本接口（DescribeNotebookSession）用于查询交互式 session详情信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSession"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSessionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSessionLog(
            self,
            request: models.DescribeNotebookSessionLogRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSessionLogResponse:
        """
        本接口（DescribeNotebookSessionLog）用于查询交互式 session日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSessionLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSessionLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSessionStatement(
            self,
            request: models.DescribeNotebookSessionStatementRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSessionStatementResponse:
        """
        本接口（DescribeNotebookSessionStatement）用于查询session 中执行任务的详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSessionStatement"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSessionStatementResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSessionStatementSqlResult(
            self,
            request: models.DescribeNotebookSessionStatementSqlResultRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSessionStatementSqlResultResponse:
        """
        本接口（DescribeNotebookSessionStatementSqlResult）用于获取statement运行结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSessionStatementSqlResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSessionStatementSqlResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSessionStatements(
            self,
            request: models.DescribeNotebookSessionStatementsRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSessionStatementsResponse:
        """
        本接口（DescribeNotebookSessionStatements）用于查询Session中执行的任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSessionStatements"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSessionStatementsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNotebookSessions(
            self,
            request: models.DescribeNotebookSessionsRequest,
            opts: Dict = None,
    ) -> models.DescribeNotebookSessionsResponse:
        """
        本接口（DescribeNotebookSessions）用于查询交互式 session列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNotebookSessions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNotebookSessionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeOtherCHDFSBindingList(
            self,
            request: models.DescribeOtherCHDFSBindingListRequest,
            opts: Dict = None,
    ) -> models.DescribeOtherCHDFSBindingListResponse:
        """
        此接口（DescribeOtherCHDFSBindingList）用于查询其他产品元数据加速桶绑定列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeOtherCHDFSBindingList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeOtherCHDFSBindingListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResultDownload(
            self,
            request: models.DescribeResultDownloadRequest,
            opts: Dict = None,
    ) -> models.DescribeResultDownloadResponse:
        """
        查询结果下载任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResultDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResultDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeScripts(
            self,
            request: models.DescribeScriptsRequest,
            opts: Dict = None,
    ) -> models.DescribeScriptsResponse:
        """
        该接口（DescribeScripts）用于查询SQL脚本列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScripts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScriptsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSessionImageVersion(
            self,
            request: models.DescribeSessionImageVersionRequest,
            opts: Dict = None,
    ) -> models.DescribeSessionImageVersionResponse:
        """
        获取指定大版本下所有小版本的所有内置镜像
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSessionImageVersion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSessionImageVersionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkAppJob(
            self,
            request: models.DescribeSparkAppJobRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkAppJobResponse:
        """
        查询spark作业信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkAppJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkAppJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkAppJobs(
            self,
            request: models.DescribeSparkAppJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkAppJobsResponse:
        """
        查询spark作业列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkAppJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkAppJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkAppTasks(
            self,
            request: models.DescribeSparkAppTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkAppTasksResponse:
        """
        查询Spark作业的运行任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkAppTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkAppTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkSessionBatchSQL(
            self,
            request: models.DescribeSparkSessionBatchSQLRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkSessionBatchSQLResponse:
        """
        本接口（DescribeSparkSessionBatchSQL）用于查询Spark SQL批任务运行状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkSessionBatchSQL"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkSessionBatchSQLResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkSessionBatchSQLCost(
            self,
            request: models.DescribeSparkSessionBatchSQLCostRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkSessionBatchSQLCostResponse:
        """
        本接口（DescribeSparkSessionBatchSQLCost）用于查询Spark SQL批任务消耗
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkSessionBatchSQLCost"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkSessionBatchSQLCostResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkSessionBatchSqlLog(
            self,
            request: models.DescribeSparkSessionBatchSqlLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkSessionBatchSqlLogResponse:
        """
        本接口（DescribeSparkSessionBatchSqlLog）用于查询Spark SQL批任务日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkSessionBatchSqlLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkSessionBatchSqlLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStandardEngineResourceGroupConfigInfo(
            self,
            request: models.DescribeStandardEngineResourceGroupConfigInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeStandardEngineResourceGroupConfigInfoResponse:
        """
        查询标准引擎资源组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStandardEngineResourceGroupConfigInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStandardEngineResourceGroupConfigInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStandardEngineResourceGroups(
            self,
            request: models.DescribeStandardEngineResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeStandardEngineResourceGroupsResponse:
        """
        查询标准引擎资源组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStandardEngineResourceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStandardEngineResourceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStoreLocation(
            self,
            request: models.DescribeStoreLocationRequest,
            opts: Dict = None,
    ) -> models.DescribeStoreLocationResponse:
        """
        查询计算结果存储位置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubUserAccessPolicy(
            self,
            request: models.DescribeSubUserAccessPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeSubUserAccessPolicyResponse:
        """
        本接口（DescribeSubUserAccessPolicy）用于开通了第三方平台访问的用户，查询其子用户的访问策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubUserAccessPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubUserAccessPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTable(
            self,
            request: models.DescribeTableRequest,
            opts: Dict = None,
    ) -> models.DescribeTableResponse:
        """
        本接口（DescribeTable），用于查询单个表的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablePartitions(
            self,
            request: models.DescribeTablePartitionsRequest,
            opts: Dict = None,
    ) -> models.DescribeTablePartitionsResponse:
        """
        本接口（DescribeTablePartitions）用于查询数据表分区信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablePartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablePartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        本接口（DescribeTables）用于查询数据表列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablesName(
            self,
            request: models.DescribeTablesNameRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesNameResponse:
        """
        本接口（DescribeTables）用于查询数据表名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablesName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskList(
            self,
            request: models.DescribeTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskListResponse:
        """
        该接口（DescribleTasks）用于查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskLog(
            self,
            request: models.DescribeTaskLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskLogResponse:
        """
        本接口（DescribeTaskLog）用于获取spark 作业任务日志详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskMonitorInfos(
            self,
            request: models.DescribeTaskMonitorInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskMonitorInfosResponse:
        """
        查询任务监控指标信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskMonitorInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskMonitorInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResourceUsage(
            self,
            request: models.DescribeTaskResourceUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResourceUsageResponse:
        """
        返回任务洞察资源用量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResourceUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResourceUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        查询任务结果，仅支持30天以内的任务查询结果，且返回数据大小超过近50M会进行截断。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        该接口（DescribleTasks）用于查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasksAnalysis(
            self,
            request: models.DescribeTasksAnalysisRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksAnalysisResponse:
        """
        该接口用于洞察分析列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasksAnalysis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksAnalysisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasksCostInfo(
            self,
            request: models.DescribeTasksCostInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksCostInfoResponse:
        """
        该接口（DescribeTasksCostInfo）用于查询任务消耗
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasksCostInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksCostInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasksOverview(
            self,
            request: models.DescribeTasksOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksOverviewResponse:
        """
        查看任务概览页
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasksOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeThirdPartyAccessUser(
            self,
            request: models.DescribeThirdPartyAccessUserRequest,
            opts: Dict = None,
    ) -> models.DescribeThirdPartyAccessUserResponse:
        """
        本接口（RegisterThirdPartyAccessUser）查询开通第三方平台访问的用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeThirdPartyAccessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeThirdPartyAccessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUDFPolicy(
            self,
            request: models.DescribeUDFPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeUDFPolicyResponse:
        """
        获取UDF权限信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUDFPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUDFPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUpdatableDataEngines(
            self,
            request: models.DescribeUpdatableDataEnginesRequest,
            opts: Dict = None,
    ) -> models.DescribeUpdatableDataEnginesResponse:
        """
        查询可更新配置的引擎列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUpdatableDataEngines"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUpdatableDataEnginesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserDataEngineConfig(
            self,
            request: models.DescribeUserDataEngineConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeUserDataEngineConfigResponse:
        """
        查询用户自定义引擎参数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserDataEngineConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserDataEngineConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserInfo(
            self,
            request: models.DescribeUserInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeUserInfoResponse:
        """
        获取用户详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRegisterTime(
            self,
            request: models.DescribeUserRegisterTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRegisterTimeResponse:
        """
        该接口（DescribeUserRegisterTime）用于查询当前用户注册时间，并判断是否是老用户。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRegisterTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRegisterTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserRoles(
            self,
            request: models.DescribeUserRolesRequest,
            opts: Dict = None,
    ) -> models.DescribeUserRolesResponse:
        """
        列举用户角色信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserRoles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserRolesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserType(
            self,
            request: models.DescribeUserTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeUserTypeResponse:
        """
        获取用户类型
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserVpcConnection(
            self,
            request: models.DescribeUserVpcConnectionRequest,
            opts: Dict = None,
    ) -> models.DescribeUserVpcConnectionResponse:
        """
        查询用户vpc到引擎网络的连接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserVpcConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserVpcConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        获取用户列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeViews(
            self,
            request: models.DescribeViewsRequest,
            opts: Dict = None,
    ) -> models.DescribeViewsResponse:
        """
        本接口（DescribeViews）用于查询数据视图列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeViews"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeViewsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkGroupInfo(
            self,
            request: models.DescribeWorkGroupInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkGroupInfoResponse:
        """
        获取工作组详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkGroupInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkGroupInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkGroups(
            self,
            request: models.DescribeWorkGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkGroupsResponse:
        """
        获取工作组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachUserPolicy(
            self,
            request: models.DetachUserPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachUserPolicyResponse:
        """
        解绑用户鉴权策略
        """
        
        kwargs = {}
        kwargs["action"] = "DetachUserPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachUserPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachWorkGroupPolicy(
            self,
            request: models.DetachWorkGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.DetachWorkGroupPolicyResponse:
        """
        解绑工作组鉴权策略
        """
        
        kwargs = {}
        kwargs["action"] = "DetachWorkGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachWorkGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDMSDatabase(
            self,
            request: models.DropDMSDatabaseRequest,
            opts: Dict = None,
    ) -> models.DropDMSDatabaseResponse:
        """
        DMS元数据删除库
        """
        
        kwargs = {}
        kwargs["action"] = "DropDMSDatabase"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDMSDatabaseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDMSPartitions(
            self,
            request: models.DropDMSPartitionsRequest,
            opts: Dict = None,
    ) -> models.DropDMSPartitionsResponse:
        """
        DMS元数据删除分区
        """
        
        kwargs = {}
        kwargs["action"] = "DropDMSPartitions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDMSPartitionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DropDMSTable(
            self,
            request: models.DropDMSTableRequest,
            opts: Dict = None,
    ) -> models.DropDMSTableResponse:
        """
        DMS元数据删除表
        """
        
        kwargs = {}
        kwargs["action"] = "DropDMSTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DropDMSTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateCreateMangedTableSql(
            self,
            request: models.GenerateCreateMangedTableSqlRequest,
            opts: Dict = None,
    ) -> models.GenerateCreateMangedTableSqlResponse:
        """
        生成创建托管表语句
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateCreateMangedTableSql"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateCreateMangedTableSqlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetOptimizerPolicy(
            self,
            request: models.GetOptimizerPolicyRequest,
            opts: Dict = None,
    ) -> models.GetOptimizerPolicyResponse:
        """
        GetOptimizerPolicy
        """
        
        kwargs = {}
        kwargs["action"] = "GetOptimizerPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetOptimizerPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GrantDLCCatalogAccess(
            self,
            request: models.GrantDLCCatalogAccessRequest,
            opts: Dict = None,
    ) -> models.GrantDLCCatalogAccessResponse:
        """
        授权访问DLC Catalog
        """
        
        kwargs = {}
        kwargs["action"] = "GrantDLCCatalogAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GrantDLCCatalogAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LaunchStandardEngineResourceGroups(
            self,
            request: models.LaunchStandardEngineResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.LaunchStandardEngineResourceGroupsResponse:
        """
        启动标准引擎资源组
        """
        
        kwargs = {}
        kwargs["action"] = "LaunchStandardEngineResourceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LaunchStandardEngineResourceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskJobLogDetail(
            self,
            request: models.ListTaskJobLogDetailRequest,
            opts: Dict = None,
    ) -> models.ListTaskJobLogDetailResponse:
        """
        本接口（ListTaskJobLogDetail）用于获取spark 作业任务日志详情
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskJobLogDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskJobLogDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ListTaskJobLogName(
            self,
            request: models.ListTaskJobLogNameRequest,
            opts: Dict = None,
    ) -> models.ListTaskJobLogNameResponse:
        """
        本接口（ListTaskJobLogName）用于获取spark-jar日志名称列表
        """
        
        kwargs = {}
        kwargs["action"] = "ListTaskJobLogName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ListTaskJobLogNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LockMetaData(
            self,
            request: models.LockMetaDataRequest,
            opts: Dict = None,
    ) -> models.LockMetaDataResponse:
        """
        元数据锁
        """
        
        kwargs = {}
        kwargs["action"] = "LockMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LockMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAdvancedStoreLocation(
            self,
            request: models.ModifyAdvancedStoreLocationRequest,
            opts: Dict = None,
    ) -> models.ModifyAdvancedStoreLocationResponse:
        """
        修改sql查询界面高级设置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAdvancedStoreLocation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAdvancedStoreLocationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataEngineDescription(
            self,
            request: models.ModifyDataEngineDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyDataEngineDescriptionResponse:
        """
        修改引擎描述信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataEngineDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataEngineDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGovernEventRule(
            self,
            request: models.ModifyGovernEventRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyGovernEventRuleResponse:
        """
        修改数据治理事件阈值
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGovernEventRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGovernEventRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySparkApp(
            self,
            request: models.ModifySparkAppRequest,
            opts: Dict = None,
    ) -> models.ModifySparkAppResponse:
        """
        更新spark作业
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySparkApp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySparkAppResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySparkAppBatch(
            self,
            request: models.ModifySparkAppBatchRequest,
            opts: Dict = None,
    ) -> models.ModifySparkAppBatchResponse:
        """
        本接口（ModifySparkAppBatch）用于批量修改Spark作业参数配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySparkAppBatch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySparkAppBatchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUser(
            self,
            request: models.ModifyUserRequest,
            opts: Dict = None,
    ) -> models.ModifyUserResponse:
        """
        修改用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserType(
            self,
            request: models.ModifyUserTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyUserTypeResponse:
        """
        修改用户类型。只有管理员用户能够调用该接口进行操作
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkGroup(
            self,
            request: models.ModifyWorkGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkGroupResponse:
        """
        修改工作组信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def PauseStandardEngineResourceGroups(
            self,
            request: models.PauseStandardEngineResourceGroupsRequest,
            opts: Dict = None,
    ) -> models.PauseStandardEngineResourceGroupsResponse:
        """
        暂停标准引擎session
        """
        
        kwargs = {}
        kwargs["action"] = "PauseStandardEngineResourceGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.PauseStandardEngineResourceGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryInternalTableWarehouse(
            self,
            request: models.QueryInternalTableWarehouseRequest,
            opts: Dict = None,
    ) -> models.QueryInternalTableWarehouseResponse:
        """
        本接口（QueryInternalTableWarehouse）用于获取原生表warehouse路径
        """
        
        kwargs = {}
        kwargs["action"] = "QueryInternalTableWarehouse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryInternalTableWarehouseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryResult(
            self,
            request: models.QueryResultRequest,
            opts: Dict = None,
    ) -> models.QueryResultResponse:
        """
        获取任务结果查询
        """
        
        kwargs = {}
        kwargs["action"] = "QueryResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryTaskCostDetail(
            self,
            request: models.QueryTaskCostDetailRequest,
            opts: Dict = None,
    ) -> models.QueryTaskCostDetailResponse:
        """
        该接口（QueryTaskCostDetail）用于查询任务消耗明细
        """
        
        kwargs = {}
        kwargs["action"] = "QueryTaskCostDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryTaskCostDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterThirdPartyAccessUser(
            self,
            request: models.RegisterThirdPartyAccessUserRequest,
            opts: Dict = None,
    ) -> models.RegisterThirdPartyAccessUserResponse:
        """
        本接口（RegisterThirdPartyAccessUser）用于开通第三方平台访问
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterThirdPartyAccessUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterThirdPartyAccessUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDataEngine(
            self,
            request: models.RenewDataEngineRequest,
            opts: Dict = None,
    ) -> models.RenewDataEngineResponse:
        """
        续费数据引擎
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportHeartbeatMetaData(
            self,
            request: models.ReportHeartbeatMetaDataRequest,
            opts: Dict = None,
    ) -> models.ReportHeartbeatMetaDataResponse:
        """
        上报元数据心跳
        """
        
        kwargs = {}
        kwargs["action"] = "ReportHeartbeatMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportHeartbeatMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDataEngine(
            self,
            request: models.RestartDataEngineRequest,
            opts: Dict = None,
    ) -> models.RestartDataEngineResponse:
        """
        重启引擎
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RevokeDLCCatalogAccess(
            self,
            request: models.RevokeDLCCatalogAccessRequest,
            opts: Dict = None,
    ) -> models.RevokeDLCCatalogAccessResponse:
        """
        撤销DLC Catalog访问权限
        """
        
        kwargs = {}
        kwargs["action"] = "RevokeDLCCatalogAccess"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RevokeDLCCatalogAccessResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RollbackDataEngineImage(
            self,
            request: models.RollbackDataEngineImageRequest,
            opts: Dict = None,
    ) -> models.RollbackDataEngineImageResponse:
        """
        回滚引擎镜像版本
        """
        
        kwargs = {}
        kwargs["action"] = "RollbackDataEngineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RollbackDataEngineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetOptimizerPolicy(
            self,
            request: models.SetOptimizerPolicyRequest,
            opts: Dict = None,
    ) -> models.SetOptimizerPolicyResponse:
        """
        设置优化策略的接口
        """
        
        kwargs = {}
        kwargs["action"] = "SetOptimizerPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetOptimizerPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SuspendResumeDataEngine(
            self,
            request: models.SuspendResumeDataEngineRequest,
            opts: Dict = None,
    ) -> models.SuspendResumeDataEngineResponse:
        """
        本接口用于控制挂起或启动数据引擎
        """
        
        kwargs = {}
        kwargs["action"] = "SuspendResumeDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SuspendResumeDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDataEngine(
            self,
            request: models.SwitchDataEngineRequest,
            opts: Dict = None,
    ) -> models.SwitchDataEngineResponse:
        """
        切换主备集群
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SwitchDataEngineImage(
            self,
            request: models.SwitchDataEngineImageRequest,
            opts: Dict = None,
    ) -> models.SwitchDataEngineImageResponse:
        """
        切换引擎镜像版本
        """
        
        kwargs = {}
        kwargs["action"] = "SwitchDataEngineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SwitchDataEngineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindWorkGroupsFromUser(
            self,
            request: models.UnbindWorkGroupsFromUserRequest,
            opts: Dict = None,
    ) -> models.UnbindWorkGroupsFromUserResponse:
        """
        解绑用户上的用户组
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindWorkGroupsFromUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindWorkGroupsFromUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnboundDatasourceHouse(
            self,
            request: models.UnboundDatasourceHouseRequest,
            opts: Dict = None,
    ) -> models.UnboundDatasourceHouseResponse:
        """
        解绑数据源与队列
        """
        
        kwargs = {}
        kwargs["action"] = "UnboundDatasourceHouse"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnboundDatasourceHouseResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlockMetaData(
            self,
            request: models.UnlockMetaDataRequest,
            opts: Dict = None,
    ) -> models.UnlockMetaDataResponse:
        """
        元数据解锁
        """
        
        kwargs = {}
        kwargs["action"] = "UnlockMetaData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlockMetaDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataEngine(
            self,
            request: models.UpdateDataEngineRequest,
            opts: Dict = None,
    ) -> models.UpdateDataEngineResponse:
        """
        本接口用于更新数据引擎配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataEngine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataEngineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataEngineConfig(
            self,
            request: models.UpdateDataEngineConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateDataEngineConfigResponse:
        """
        用户某种操作，触发引擎配置修改
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataEngineConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataEngineConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateDataMaskStrategy(
            self,
            request: models.UpdateDataMaskStrategyRequest,
            opts: Dict = None,
    ) -> models.UpdateDataMaskStrategyResponse:
        """
        更新数据脱敏策略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateDataMaskStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateDataMaskStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateEngineResourceGroupNetworkConfigInfo(
            self,
            request: models.UpdateEngineResourceGroupNetworkConfigInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateEngineResourceGroupNetworkConfigInfoResponse:
        """
        更新标准引擎资源组网络配置信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateEngineResourceGroupNetworkConfigInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateEngineResourceGroupNetworkConfigInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateNetworkConnection(
            self,
            request: models.UpdateNetworkConnectionRequest,
            opts: Dict = None,
    ) -> models.UpdateNetworkConnectionResponse:
        """
        更新网络配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateNetworkConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateNetworkConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateRowFilter(
            self,
            request: models.UpdateRowFilterRequest,
            opts: Dict = None,
    ) -> models.UpdateRowFilterResponse:
        """
        此接口用于更新行过滤规则。注意只能更新过滤规则，不能更新规格对象catalog，database和table。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateRowFilter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateRowFilterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateStandardEngineResourceGroupBaseInfo(
            self,
            request: models.UpdateStandardEngineResourceGroupBaseInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateStandardEngineResourceGroupBaseInfoResponse:
        """
        更新标准引擎资源组基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateStandardEngineResourceGroupBaseInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateStandardEngineResourceGroupBaseInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateStandardEngineResourceGroupConfigInfo(
            self,
            request: models.UpdateStandardEngineResourceGroupConfigInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateStandardEngineResourceGroupConfigInfoResponse:
        """
        更新标准引擎资源组基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateStandardEngineResourceGroupConfigInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateStandardEngineResourceGroupConfigInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateStandardEngineResourceGroupResourceInfo(
            self,
            request: models.UpdateStandardEngineResourceGroupResourceInfoRequest,
            opts: Dict = None,
    ) -> models.UpdateStandardEngineResourceGroupResourceInfoResponse:
        """
        更新标准引擎资源组基础信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateStandardEngineResourceGroupResourceInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateStandardEngineResourceGroupResourceInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUDFPolicy(
            self,
            request: models.UpdateUDFPolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateUDFPolicyResponse:
        """
        UDP权限修改
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUDFPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUDFPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateUserDataEngineConfig(
            self,
            request: models.UpdateUserDataEngineConfigRequest,
            opts: Dict = None,
    ) -> models.UpdateUserDataEngineConfigResponse:
        """
        修改用户引擎自定义配置
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateUserDataEngineConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateUserDataEngineConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDataEngineImage(
            self,
            request: models.UpgradeDataEngineImageRequest,
            opts: Dict = None,
    ) -> models.UpgradeDataEngineImageResponse:
        """
        升级引擎镜像
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDataEngineImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDataEngineImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)