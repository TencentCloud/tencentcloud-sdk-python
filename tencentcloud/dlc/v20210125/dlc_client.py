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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignMangedTableProperties(self, request):
        """分配原生表表属性

        :param request: Request instance for AssignMangedTableProperties.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AssignMangedTablePropertiesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AssignMangedTablePropertiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignMangedTableProperties", params, headers=headers)
            response = json.loads(body)
            model = models.AssignMangedTablePropertiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineConfigPairsValidity(self, request):
        """本接口（CheckDataEngineConfigPairsValidity）用于检查引擎用户自定义参数的有效性

        :param request: Request instance for CheckDataEngineConfigPairsValidity.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineConfigPairsValidityRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineConfigPairsValidityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDataEngineConfigPairsValidity", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDataEngineConfigPairsValidityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineImageCanBeRollback(self, request):
        """本接口（CheckDataEngineImageCanBeRollback）用于查看集群是否能回滚。

        :param request: Request instance for CheckDataEngineImageCanBeRollback.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeRollbackRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeRollbackResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDataEngineImageCanBeRollback", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDataEngineImageCanBeRollbackResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineImageCanBeUpgrade(self, request):
        """本接口（CheckDataEngineImageCanBeUpgrade）用于查看集群镜像是否能够升级。

        :param request: Request instance for CheckDataEngineImageCanBeUpgrade.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeUpgradeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckDataEngineImageCanBeUpgradeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDataEngineImageCanBeUpgrade", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDataEngineImageCanBeUpgradeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataEngine(self, request):
        """删除数据引擎

        :param request: Request instance for DeleteDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAdvancedStoreLocation(self, request):
        """查询sql查询界面高级设置

        :param request: Request instance for DescribeAdvancedStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeAdvancedStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeAdvancedStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAdvancedStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAdvancedStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEngine(self, request):
        """本接口根据名称用于获取数据引擎详细信息

        :param request: Request instance for DescribeDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEngineEvents(self, request):
        """查询数据引擎事件

        :param request: Request instance for DescribeDataEngineEvents.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineEventsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngineEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEngineEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEngineImageVersions(self, request):
        """本接口（DescribeDataEngineImageVersions）用于获取独享集群大版本镜像列表。

        :param request: Request instance for DescribeDataEngineImageVersions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineImageVersionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineImageVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngineImageVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEngineImageVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEnginePythonSparkImages(self, request):
        """本接口（DescribeDataEnginePythonSparkImages）用于获取PYSPARK镜像列表

        :param request: Request instance for DescribeDataEnginePythonSparkImages.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginePythonSparkImagesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginePythonSparkImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEnginePythonSparkImages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEnginePythonSparkImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatasourceConnection(self, request):
        """本接口（DescribeDatasourceConnection）用于查询数据源信息

        :param request: Request instance for DescribeDatasourceConnection.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDatasourceConnectionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDatasourceConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatasourceConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatasourceConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLakeFsTaskResult(self, request):
        """获取LakeFs上task执行结果访问信息

        :param request: Request instance for DescribeLakeFsTaskResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsTaskResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeLakeFsTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLakeFsTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLakeFsTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkSessionBatchSQL(self, request):
        """本接口（DescribeSparkSessionBatchSQL）用于查询Spark SQL批任务运行状态

        :param request: Request instance for DescribeSparkSessionBatchSQL.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSQLRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSQLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkSessionBatchSQL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkSessionBatchSQLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkSessionBatchSqlLog(self, request):
        """本接口（DescribeSparkSessionBatchSqlLog）用于查询Spark SQL批任务日志

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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTablesName(self, request):
        """本接口（DescribeTables）用于查询数据表名称列表

        :param request: Request instance for DescribeTablesName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTablesNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablesName", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablesNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpdatableDataEngines(self, request):
        """查询可更新配置的引擎列表

        :param request: Request instance for DescribeUpdatableDataEngines.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUpdatableDataEnginesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUpdatableDataEnginesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpdatableDataEngines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpdatableDataEnginesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserDataEngineConfig(self, request):
        """查询用户自定义引擎参数

        :param request: Request instance for DescribeUserDataEngineConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserDataEngineConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserDataEngineConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserDataEngineConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserDataEngineConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserInfo(self, request):
        """获取用户详细信息

        :param request: Request instance for DescribeUserInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoles(self, request):
        """列举用户角色信息

        :param request: Request instance for DescribeUserRoles.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserRolesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserRolesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRoles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRolesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserType(self, request):
        """获取用户类型

        :param request: Request instance for DescribeUserType.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserTypeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeWorkGroupInfo(self, request):
        """获取工作组详细信息

        :param request: Request instance for DescribeWorkGroupInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeWorkGroupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeWorkGroupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeWorkGroupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOptimizerPolicy(self, request):
        """GetOptimizerPolicy

        :param request: Request instance for GetOptimizerPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetOptimizerPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetOptimizerPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetOptimizerPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.GetOptimizerPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAdvancedStoreLocation(self, request):
        """修改sql查询界面高级设置。

        :param request: Request instance for ModifyAdvancedStoreLocation.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyAdvancedStoreLocationRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyAdvancedStoreLocationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAdvancedStoreLocation", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAdvancedStoreLocationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataEngineDescription(self, request):
        """修改引擎描述信息

        :param request: Request instance for ModifyDataEngineDescription.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyDataEngineDescriptionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyDataEngineDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDataEngineDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDataEngineDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserType(self, request):
        """修改用户类型。只有管理员用户能够调用该接口进行操作

        :param request: Request instance for ModifyUserType.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyUserTypeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyUserTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryResult(self, request):
        """获取任务结果查询

        :param request: Request instance for QueryResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryResult", params, headers=headers)
            response = json.loads(body)
            model = models.QueryResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryTaskCostDetail(self, request):
        """该接口（QueryTaskCostDetail）用于查询任务消耗明细

        :param request: Request instance for QueryTaskCostDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryTaskCostDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryTaskCostDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryTaskCostDetail", params, headers=headers)
            response = json.loads(body)
            model = models.QueryTaskCostDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDataEngine(self, request):
        """续费数据引擎

        :param request: Request instance for RenewDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RenewDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RenewDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDataEngine(self, request):
        """重启引擎

        :param request: Request instance for RestartDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RestartDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RestartDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackDataEngineImage(self, request):
        """回滚引擎镜像版本

        :param request: Request instance for RollbackDataEngineImage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RollbackDataEngineImageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RollbackDataEngineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackDataEngineImage", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackDataEngineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDataEngineImage(self, request):
        """切换引擎镜像版本

        :param request: Request instance for SwitchDataEngineImage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineImageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SwitchDataEngineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDataEngineImage", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDataEngineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataEngine(self, request):
        """本接口用于更新数据引擎配置

        :param request: Request instance for UpdateDataEngine.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataEngine", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataEngineResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataEngineConfig(self, request):
        """用户某种操作，触发引擎配置修改

        :param request: Request instance for UpdateDataEngineConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateDataEngineConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataEngineConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataEngineConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


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
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserDataEngineConfig(self, request):
        """修改用户引擎自定义配置

        :param request: Request instance for UpdateUserDataEngineConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateUserDataEngineConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateUserDataEngineConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUserDataEngineConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUserDataEngineConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDataEngineImage(self, request):
        """升级引擎镜像

        :param request: Request instance for UpgradeDataEngineImage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpgradeDataEngineImageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpgradeDataEngineImageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDataEngineImage", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDataEngineImageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))