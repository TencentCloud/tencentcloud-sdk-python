# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dlc.v20210125 import models


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.tencentcloudapi.com'
    _service = 'dlc'


    def AddDMSPartitions(self, request):
        """DMS元数据新增分区

        :param request: Request instance for AddDMSPartitions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AddDMSPartitionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AddDMSPartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDMSPartitions", params, headers=headers)
            response = json.loads(body)
            model = models.AddDMSPartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddUsersToWorkGroup(self, request):
        """添加用户到工作组

        :param request: Request instance for AddUsersToWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AddUsersToWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AddUsersToWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddUsersToWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddUsersToWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AlterDMSDatabase(self, request):
        """DMS元数据更新库

        :param request: Request instance for AlterDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AlterDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AlterDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AlterDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.AlterDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AlterDMSPartition(self, request):
        """DMS元数据更新分区

        :param request: Request instance for AlterDMSPartition.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AlterDMSPartitionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AlterDMSPartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AlterDMSPartition", params, headers=headers)
            response = json.loads(body)
            model = models.AlterDMSPartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AlterDMSTable(self, request):
        """DMS元数据更新表

        :param request: Request instance for AlterDMSTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AlterDMSTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AlterDMSTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AlterDMSTable", params, headers=headers)
            response = json.loads(body)
            model = models.AlterDMSTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachUserPolicy(self, request):
        """绑定鉴权策略到用户

        :param request: Request instance for AttachUserPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachUserPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachUserPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AttachUserPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachWorkGroupPolicy(self, request):
        """绑定鉴权策略到工作组

        :param request: Request instance for AttachWorkGroupPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachWorkGroupPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachWorkGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachWorkGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AttachWorkGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def BindWorkGroupsToUser(self, request):
        """绑定工作组到用户

        :param request: Request instance for BindWorkGroupsToUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.BindWorkGroupsToUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.BindWorkGroupsToUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindWorkGroupsToUser", params, headers=headers)
            response = json.loads(body)
            model = models.BindWorkGroupsToUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelNotebookSessionStatement(self, request):
        """本接口（CancelNotebookSessionStatement）用于取消session中执行的任务

        :param request: Request instance for CancelNotebookSessionStatement.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelNotebookSessionStatementRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelNotebookSessionStatementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelNotebookSessionStatement", params, headers=headers)
            response = json.loads(body)
            model = models.CancelNotebookSessionStatementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelNotebookSessionStatementBatch(self, request):
        """本接口（CancelNotebookSessionStatementBatch）用于批量取消Session 中执行的任务

        :param request: Request instance for CancelNotebookSessionStatementBatch.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelNotebookSessionStatementBatchRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelNotebookSessionStatementBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelNotebookSessionStatementBatch", params, headers=headers)
            response = json.loads(body)
            model = models.CancelNotebookSessionStatementBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelSparkSessionBatchSQL(self, request):
        """本接口（CancelSparkSessionBatchSQL）用于取消Spark SQL批任务。

        :param request: Request instance for CancelSparkSessionBatchSQL.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelSparkSessionBatchSQLRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelSparkSessionBatchSQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelSparkSessionBatchSQL", params, headers=headers)
            response = json.loads(body)
            model = models.CancelSparkSessionBatchSQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CancelTask(self, request):
        """本接口（CancelTask），用于取消任务

        :param request: Request instance for CancelTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTask", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckLockMetaData(self, request):
        """元数据锁检查

        :param request: Request instance for CheckLockMetaData.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckLockMetaDataRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckLockMetaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckLockMetaData", params, headers=headers)
            response = json.loads(body)
            model = models.CheckLockMetaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDMSDatabase(self, request):
        """DMS元数据创建库

        :param request: Request instance for CreateDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDMSTable(self, request):
        """DMS元数据创建表

        :param request: Request instance for CreateDMSTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDMSTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDMSTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDMSTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDMSTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDataEngine(self, request):
        """为用户创建数据引擎

        :param request: Request instance for CreateDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDatabase(self, request):
        """本接口（CreateDatabase）用于生成建库SQL语句。

        :param request: Request instance for CreateDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateExportTask(self, request):
        """该接口（CreateExportTask）用于创建导出任务

        :param request: Request instance for CreateExportTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateExportTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateExportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateExportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateExportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateImportTask(self, request):
        """该接口（CreateImportTask）用于创建导入任务

        :param request: Request instance for CreateImportTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateImportTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateImportTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateImportTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateImportTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateInternalTable(self, request):
        """创建托管存储内表（该接口已废弃）

        :param request: Request instance for CreateInternalTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateInternalTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateInternalTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInternalTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInternalTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNotebookSession(self, request):
        """本接口（CreateNotebookSession）用于创建交互式session（notebook）

        :param request: Request instance for CreateNotebookSession.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateNotebookSessionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateNotebookSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebookSession", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNotebookSessionStatement(self, request):
        """本接口（CreateNotebookSessionStatement）用于在session中执行代码片段

        :param request: Request instance for CreateNotebookSessionStatement.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateNotebookSessionStatementRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateNotebookSessionStatementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebookSessionStatement", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookSessionStatementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNotebookSessionStatementSupportBatchSQL(self, request):
        """本接口（CreateNotebookSessionStatementSupportBatchSQL）用于创建交互式session并执行SQL任务

        :param request: Request instance for CreateNotebookSessionStatementSupportBatchSQL.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateNotebookSessionStatementSupportBatchSQLRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateNotebookSessionStatementSupportBatchSQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNotebookSessionStatementSupportBatchSQL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNotebookSessionStatementSupportBatchSQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateResultDownload(self, request):
        """创建查询结果下载任务

        :param request: Request instance for CreateResultDownload.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateResultDownloadRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateResultDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResultDownload", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResultDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateScript(self, request):
        """该接口（CreateScript）用于创建sql脚本。

        :param request: Request instance for CreateScript.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateScriptRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateScript", params, headers=headers)
            response = json.loads(body)
            model = models.CreateScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSparkApp(self, request):
        """创建spark作业

        :param request: Request instance for CreateSparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkApp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSparkAppTask(self, request):
        """启动Spark作业

        :param request: Request instance for CreateSparkAppTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkAppTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkAppTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSparkSessionBatchSQL(self, request):
        """本接口（CreateSparkSessionBatchSQL）用于向Spark作业引擎提交Spark SQL批任务。

        :param request: Request instance for CreateSparkSessionBatchSQL.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkSessionBatchSQLRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkSessionBatchSQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkSessionBatchSQL", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkSessionBatchSQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateStoreLocation(self, request):
        """该接口（CreateStoreLocation）新增或覆盖计算结果存储位置。

        :param request: Request instance for CreateStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTable(self, request):
        """本接口（CreateTable）用于生成建表SQL。

        :param request: Request instance for CreateTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTask(self, request):
        """本接口（CreateTask）用于创建并执行SQL任务。（推荐使用CreateTasks接口）

        :param request: Request instance for CreateTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTasks(self, request):
        """本接口（CreateTasks），用于批量创建并执行SQL任务

        :param request: Request instance for CreateTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateTasksInOrder(self, request):
        """按顺序创建任务（已经废弃，后期不再维护，请使用接口CreateTasks）

        :param request: Request instance for CreateTasksInOrder.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTasksInOrderRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTasksInOrderResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTasksInOrder", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTasksInOrderResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateUser(self, request):
        """创建用户

        :param request: Request instance for CreateUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUser", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateWorkGroup(self, request):
        """创建工作组

        :param request: Request instance for CreateWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNotebookSession(self, request):
        """本接口（DeleteNotebookSession）用于删除交互式session（notebook）

        :param request: Request instance for DeleteNotebookSession.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteNotebookSessionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteNotebookSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNotebookSession", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNotebookSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteScript(self, request):
        """该接口（DeleteScript）用于删除sql脚本。

        :param request: Request instance for DeleteScript.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteScriptRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteScriptResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteScript", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteScriptResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSparkApp(self, request):
        """删除spark作业

        :param request: Request instance for DeleteSparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteSparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteSparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSparkApp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSparkAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUser(self, request):
        """删除用户

        :param request: Request instance for DeleteUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteUsersFromWorkGroup(self, request):
        """从工作组中删除用户

        :param request: Request instance for DeleteUsersFromWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUsersFromWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUsersFromWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsersFromWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersFromWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteWorkGroup(self, request):
        """删除工作组

        :param request: Request instance for DeleteWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDMSDatabase(self, request):
        """DMS元数据获取库

        :param request: Request instance for DescribeDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDMSPartitions(self, request):
        """DMS元数据获取分区

        :param request: Request instance for DescribeDMSPartitions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSPartitionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSPartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDMSPartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDMSPartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDMSTable(self, request):
        """DMS元数据获取表

        :param request: Request instance for DescribeDMSTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDMSTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDMSTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDMSTables(self, request):
        """DMS元数据获取表列表

        :param request: Request instance for DescribeDMSTables.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSTablesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDMSTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDMSTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDMSTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDataEngines(self, request):
        """本接口（DescribeDataEngines）用于查询DataEngines信息列表

        :param request: Request instance for DescribeDataEngines.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEnginesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDatabases(self, request):
        """本接口（DescribeDatabases）用于查询数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeEngineUsageInfo(self, request):
        """本接口根据引擎ID查询数据引擎资源使用情况

        :param request: Request instance for DescribeEngineUsageInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineUsageInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineUsageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEngineUsageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEngineUsageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeForbiddenTablePro(self, request):
        """本接口（DescribeForbiddenTablePro）用于查询被禁用的表属性列表（新）

        :param request: Request instance for DescribeForbiddenTablePro.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeForbiddenTableProRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeForbiddenTableProResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeForbiddenTablePro", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeForbiddenTableProResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLakeFsDirSummary(self, request):
        """查询托管存储指定目录的Summary

        :param request: Request instance for DescribeLakeFsDirSummary.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsDirSummaryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsDirSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLakeFsDirSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLakeFsDirSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLakeFsInfo(self, request):
        """查询用户的托管存储信息

        :param request: Request instance for DescribeLakeFsInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLakeFsInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLakeFsInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotebookSession(self, request):
        """本接口（DescribeNotebookSession）用于查询交互式 session详情信息

        :param request: Request instance for DescribeNotebookSession.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSession", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotebookSessionLog(self, request):
        """本接口（DescribeNotebookSessionLog）用于查询交互式 session日志

        :param request: Request instance for DescribeNotebookSessionLog.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionLogRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSessionLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSessionLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotebookSessionStatement(self, request):
        """本接口（DescribeNotebookSessionStatement）用于查询session 中执行任务的详情

        :param request: Request instance for DescribeNotebookSessionStatement.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionStatementRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionStatementResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSessionStatement", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSessionStatementResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotebookSessionStatementSqlResult(self, request):
        """本接口（DescribeNotebookSessionStatementSqlResult）用于获取statement运行结果。

        :param request: Request instance for DescribeNotebookSessionStatementSqlResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionStatementSqlResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionStatementSqlResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSessionStatementSqlResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSessionStatementSqlResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotebookSessionStatements(self, request):
        """本接口（DescribeNotebookSessionStatements）用于查询Session中执行的任务列表

        :param request: Request instance for DescribeNotebookSessionStatements.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionStatementsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionStatementsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSessionStatements", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSessionStatementsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNotebookSessions(self, request):
        """本接口（DescribeNotebookSessions）用于查询交互式 session列表

        :param request: Request instance for DescribeNotebookSessions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNotebookSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNotebookSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNotebookSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeResultDownload(self, request):
        """查询结果下载任务

        :param request: Request instance for DescribeResultDownload.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeResultDownloadRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeResultDownloadResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResultDownload", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResultDownloadResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeScripts(self, request):
        """该接口（DescribeScripts）用于查询SQL脚本列表

        :param request: Request instance for DescribeScripts.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeScriptsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeScriptsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeScripts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeScriptsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkAppJob(self, request):
        """查询spark作业信息

        :param request: Request instance for DescribeSparkAppJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppJob", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkAppJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkAppJobs(self, request):
        """查询spark作业列表

        :param request: Request instance for DescribeSparkAppJobs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppJobs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkAppJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkAppTasks(self, request):
        """查询Spark作业的运行任务列表

        :param request: Request instance for DescribeSparkAppTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkAppTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkAppTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkAppTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSparkSessionBatchSqlLog(self, request):
        """本接口（DescribeSparkSessionBatchSqlLog）用于获取SparkSQL批任务日志

        :param request: Request instance for DescribeSparkSessionBatchSqlLog.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSqlLogRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSqlLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkSessionBatchSqlLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkSessionBatchSqlLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeStoreLocation(self, request):
        """查询计算结果存储位置。

        :param request: Request instance for DescribeStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTable(self, request):
        """本接口（DescribeTable），用于查询单个表的详细信息。

        :param request: Request instance for DescribeTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTables(self, request):
        """本接口（DescribeTables）用于查询数据表列表。

        :param request: Request instance for DescribeTables.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResult(self, request):
        """查询任务结果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTasks(self, request):
        """该接口（DescribleTasks）用于查询任务列表

        :param request: Request instance for DescribeTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeUsers(self, request):
        """获取用户列表信息

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeViews(self, request):
        """本接口（DescribeViews）用于查询数据视图列表。

        :param request: Request instance for DescribeViews.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeViewsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeViewsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeViews", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeViewsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeWorkGroups(self, request):
        """获取工作组列表

        :param request: Request instance for DescribeWorkGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachUserPolicy(self, request):
        """解绑用户鉴权策略

        :param request: Request instance for DetachUserPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DetachUserPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DetachUserPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachUserPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DetachUserPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachWorkGroupPolicy(self, request):
        """解绑工作组鉴权策略

        :param request: Request instance for DetachWorkGroupPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DetachWorkGroupPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DetachWorkGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachWorkGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DetachWorkGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DropDMSDatabase(self, request):
        """DMS元数据删除库

        :param request: Request instance for DropDMSDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DropDMSDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DropDMSDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDMSDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DropDMSDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DropDMSPartitions(self, request):
        """DMS元数据删除分区

        :param request: Request instance for DropDMSPartitions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DropDMSPartitionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DropDMSPartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDMSPartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DropDMSPartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DropDMSTable(self, request):
        """DMS元数据删除表

        :param request: Request instance for DropDMSTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DropDMSTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DropDMSTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DropDMSTable", params, headers=headers)
            response = json.loads(body)
            model = models.DropDMSTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GenerateCreateMangedTableSql(self, request):
        """生成创建托管表语句

        :param request: Request instance for GenerateCreateMangedTableSql.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GenerateCreateMangedTableSqlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GenerateCreateMangedTableSqlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateCreateMangedTableSql", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateCreateMangedTableSqlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ListTaskJobLogDetail(self, request):
        """本接口（ListTaskJobLogDetail）用于获取spark 作业任务日志详情

        :param request: Request instance for ListTaskJobLogDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListTaskJobLogDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListTaskJobLogDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskJobLogDetail", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskJobLogDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def LockMetaData(self, request):
        """元数据锁

        :param request: Request instance for LockMetaData.
        :type request: :class:`tencentcloud.dlc.v20210125.models.LockMetaDataRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.LockMetaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockMetaData", params, headers=headers)
            response = json.loads(body)
            model = models.LockMetaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGovernEventRule(self, request):
        """修改数据治理事件阈值

        :param request: Request instance for ModifyGovernEventRule.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyGovernEventRuleRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyGovernEventRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGovernEventRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGovernEventRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySparkApp(self, request):
        """更新spark作业

        :param request: Request instance for ModifySparkApp.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySparkApp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySparkAppResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySparkAppBatch(self, request):
        """本接口（ModifySparkAppBatch）用于批量修改Spark作业参数配置

        :param request: Request instance for ModifySparkAppBatch.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppBatchRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppBatchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySparkAppBatch", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySparkAppBatchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyUser(self, request):
        """修改用户信息

        :param request: Request instance for ModifyUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUser", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyWorkGroup(self, request):
        """修改工作组信息

        :param request: Request instance for ModifyWorkGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyWorkGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyWorkGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyWorkGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyWorkGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReportHeartbeatMetaData(self, request):
        """上报元数据心跳

        :param request: Request instance for ReportHeartbeatMetaData.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ReportHeartbeatMetaDataRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ReportHeartbeatMetaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReportHeartbeatMetaData", params, headers=headers)
            response = json.loads(body)
            model = models.ReportHeartbeatMetaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SuspendResumeDataEngine(self, request):
        """本接口用于控制挂起或启动数据引擎

        :param request: Request instance for SuspendResumeDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SuspendResumeDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SuspendResumeDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SuspendResumeDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.SuspendResumeDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SwitchDataEngine(self, request):
        """切换主备集群

        :param request: Request instance for SwitchDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnbindWorkGroupsFromUser(self, request):
        """解绑用户上的用户组

        :param request: Request instance for UnbindWorkGroupsFromUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UnbindWorkGroupsFromUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UnbindWorkGroupsFromUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnbindWorkGroupsFromUser", params, headers=headers)
            response = json.loads(body)
            model = models.UnbindWorkGroupsFromUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnlockMetaData(self, request):
        """元数据解锁

        :param request: Request instance for UnlockMetaData.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UnlockMetaDataRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UnlockMetaDataResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockMetaData", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockMetaDataResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpdateRowFilter(self, request):
        """此接口用于更新行过滤规则。注意只能更新过滤规则，不能更新规格对象catalog，database和table。

        :param request: Request instance for UpdateRowFilter.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateRowFilterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateRowFilterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRowFilter", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRowFilterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)