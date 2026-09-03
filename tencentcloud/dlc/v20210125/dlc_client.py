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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.dlc.v20210125 import models


class DlcClient(AbstractClient):
    _apiVersion = '2021-01-25'
    _endpoint = 'dlc.tencentcloudapi.com'
    _service = 'dlc'


    def AddDMSPartitions(self, request):
        r"""DMS元数据新增分区

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


    def AddDeployment(self, request):
        r"""为已有推理服务新增部署

        :param request: Request instance for AddDeployment.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AddDeploymentRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AddDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.AddDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddOptimizerEngines(self, request):
        r"""添加数据优化资源

        :param request: Request instance for AddOptimizerEngines.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AddOptimizerEnginesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AddOptimizerEnginesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddOptimizerEngines", params, headers=headers)
            response = json.loads(body)
            model = models.AddOptimizerEnginesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddUsersToWorkGroup(self, request):
        r"""添加用户到工作组

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
        r"""DMS元数据更新库

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
        r"""DMS元数据更新分区

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
        r"""DMS元数据更新表

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


    def AlterTableComment(self, request):
        r"""修改表备注

        :param request: Request instance for AlterTableComment.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AlterTableCommentRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AlterTableCommentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AlterTableComment", params, headers=headers)
            response = json.loads(body)
            model = models.AlterTableCommentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignMangedTableProperties(self, request):
        r"""分配原生表表属性

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


    def AssociateDatasourceHouse(self, request):
        r"""绑定数据源和队列

        :param request: Request instance for AssociateDatasourceHouse.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AssociateDatasourceHouseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AssociateDatasourceHouseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDatasourceHouse", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateDatasourceHouseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachDataMaskPolicy(self, request):
        r"""绑定数据脱敏策略

        :param request: Request instance for AttachDataMaskPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.AttachDataMaskPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.AttachDataMaskPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachDataMaskPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.AttachDataMaskPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachUserPolicy(self, request):
        r"""绑定鉴权策略到用户

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
        r"""绑定鉴权策略到工作组

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


    def BindApiKey(self, request):
        r"""绑定 API Key 到推理服务

        :param request: Request instance for BindApiKey.
        :type request: :class:`tencentcloud.dlc.v20210125.models.BindApiKeyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.BindApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BindApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.BindApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BindWorkGroupsToUser(self, request):
        r"""绑定工作组到用户

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
        r"""本接口（CancelNotebookSessionStatement）用于取消session中执行的任务

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
        r"""本接口（CancelNotebookSessionStatementBatch）用于批量取消Session 中执行的任务

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


    def CancelRayJob(self, request):
        r"""根据任务ID取消正在运行的Ray任务

        :param request: Request instance for CancelRayJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelRayJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelRayJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelRayJob", params, headers=headers)
            response = json.loads(body)
            model = models.CancelRayJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelSparkSessionBatchSQL(self, request):
        r"""本接口（CancelSparkSessionBatchSQL）用于取消Spark SQL批任务。

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
        r"""本接口（CancelTask），用于取消任务

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


    def CancelTasks(self, request):
        r"""批量取消任务

        :param request: Request instance for CancelTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTasks", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CancelTrainingJobInstance(self, request):
        r"""暂停（取消）实例

        :param request: Request instance for CancelTrainingJobInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CancelTrainingJobInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CancelTrainingJobInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelTrainingJobInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CancelTrainingJobInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckApiKeyName(self, request):
        r"""检查 API Key 名称是否重复

        :param request: Request instance for CheckApiKeyName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckApiKeyNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckApiKeyNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckApiKeyName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckApiKeyNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDataEngineConfigPairsValidity(self, request):
        r"""本接口（CheckDataEngineConfigPairsValidity）用于检查引擎用户自定义参数的有效性

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
        r"""本接口（CheckDataEngineImageCanBeRollback）用于查看集群是否能回滚。

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
        r"""本接口（CheckDataEngineImageCanBeUpgrade）用于查看集群镜像是否能够升级。

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


    def CheckJobSpecName(self, request):
        r"""训练作业配置与普通 RayJob 配置共用 job_spec 表及 (appId, name) 唯一命名空间，重名检查统一挂在本接口，供两类前端表单复用

        :param request: Request instance for CheckJobSpecName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckJobSpecNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckJobSpecNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckJobSpecName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckJobSpecNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckLockMetaData(self, request):
        r"""元数据锁检查

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


    def CheckModelIdentifier(self, request):
        r"""检查模型标识符是否重复

        :param request: Request instance for CheckModelIdentifier.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckModelIdentifierRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckModelIdentifierResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckModelIdentifier", params, headers=headers)
            response = json.loads(body)
            model = models.CheckModelIdentifierResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckModifyPartition(self, request):
        r"""变配校验：判断用户的目标配置是否可以执行变配。校验逻辑：对于缩容场景（目标值 < 当前值），检查 default 队列的 min 值是否足够承受缩容差值。

        :param request: Request instance for CheckModifyPartition.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckModifyPartitionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckModifyPartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckModifyPartition", params, headers=headers)
            response = json.loads(body)
            model = models.CheckModifyPartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckQueueName(self, request):
        r"""资源队列名称合法性检测：校验队列名称是否合法，包括非空校验、格式校验（以小写字母开头，只允许小写字母、数字和连字符，长度1~11）和同分区下重名校验。

        :param request: Request instance for CheckQueueName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckQueueNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckQueueNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckQueueName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckQueueNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckResourceName(self, request):
        r"""校验资源名称合法性

        :param request: Request instance for CheckResourceName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckResourceNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckResourceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckResourceName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckResourceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckServiceName(self, request):
        r"""检查推理服务名称是否重复

        :param request: Request instance for CheckServiceName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CheckServiceNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CheckServiceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckServiceName", params, headers=headers)
            response = json.loads(body)
            model = models.CheckServiceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CopyJobSpec(self, request):
        r"""复制一份已有的作业配置

        :param request: Request instance for CopyJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CopyJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CopyJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.CopyJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateApiKey(self, request):
        r"""创建 API Key

        :param request: Request instance for CreateApiKey.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateApiKeyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.CreateApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBenchmarkTask(self, request):
        r"""创建性能评测任务

        :param request: Request instance for CreateBenchmarkTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateBenchmarkTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateBenchmarkTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBenchmarkTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBenchmarkTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCHDFSBindingProduct(self, request):
        r"""此接口（CreateCHDFSBindingProduct）用于创建元数据加速桶和产品绑定关系

        :param request: Request instance for CreateCHDFSBindingProduct.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateCHDFSBindingProductRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateCHDFSBindingProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCHDFSBindingProduct", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCHDFSBindingProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateClusterGroup(self, request):
        r"""创建集群组

        :param request: Request instance for CreateClusterGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateClusterGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateClusterGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateClusterGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateClusterGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDMSDatabase(self, request):
        r"""DMS元数据创建库

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
        r"""DMS元数据创建表

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
        r"""为用户创建数据引擎

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


    def CreateDataMaskStrategy(self, request):
        r"""创建数据脱敏策略

        :param request: Request instance for CreateDataMaskStrategy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDataMaskStrategyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDataMaskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDataMaskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDataMaskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDatabase(self, request):
        r"""本接口（CreateDatabase）用于生成建库SQL语句。

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


    def CreateDatasourceConnection(self, request):
        r"""创建数据源

        :param request: Request instance for CreateDatasourceConnection.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateDatasourceConnectionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateDatasourceConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDatasourceConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDatasourceConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateExportTask(self, request):
        r"""该接口（CreateExportTask）用于创建导出任务

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
        r"""该接口（CreateImportTask）用于创建导入任务

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


    def CreateInferenceModel(self, request):
        r"""创建推理模型（模型上传）

        :param request: Request instance for CreateInferenceModel.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateInferenceModelRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateInferenceModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInferenceModel", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInferenceModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInferenceService(self, request):
        r"""创建推理服务（含默认部署）

        :param request: Request instance for CreateInferenceService.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateInferenceServiceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateInternalTable(self, request):
        r"""创建托管存储内表（该接口已废弃）

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


    def CreateJobSpec(self, request):
        r"""创建作业配置

        :param request: Request instance for CreateJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.CreateJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLab(self, request):
        r"""创建实验室

        :param request: Request instance for CreateLab.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateLabRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateLabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLab", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMetaDatabase(self, request):
        r"""本接口（CreateMetaDatabase）用于创建元数据库

        :param request: Request instance for CreateMetaDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateMetaDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateMetaDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMetaDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMetaDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMlflowServer(self, request):
        r"""创建 MlFlow Server

        :param request: Request instance for CreateMlflowServer.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateMlflowServerRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateMlflowServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMlflowServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMlflowServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateModelVersion(self, request):
        r"""创建模型新版本

        :param request: Request instance for CreateModelVersion.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateModelVersionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateModelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateModelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.CreateModelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNotebookSession(self, request):
        r"""本接口（CreateNotebookSession）用于创建交互式session（notebook）

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
        r"""本接口（CreateNotebookSessionStatement）用于在session中执行代码片段

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
        r"""本接口（CreateNotebookSessionStatementSupportBatchSQL）用于创建交互式session并执行SQL任务

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


    def CreatePartition(self, request):
        r"""新增资源包

        :param request: Request instance for CreatePartition.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreatePartitionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreatePartitionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePartition", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePartitionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePartitionQueue(self, request):
        r"""新增资源队列：在指定分区下创建一个新的资源队列，支持设置队列名称、描述、资源规格列表和队列类型。

        :param request: Request instance for CreatePartitionQueue.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreatePartitionQueueRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreatePartitionQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePartitionQueue", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePartitionQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRayCluster(self, request):
        r"""创建集群

        :param request: Request instance for CreateRayCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateRayClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateRayClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRayCluster", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRayClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResourceConfig(self, request):
        r"""创建资源配置模板

        :param request: Request instance for CreateResourceConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateResourceConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.CreateResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateResultDownload(self, request):
        r"""创建查询结果下载任务

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
        r"""该接口（CreateScript）用于创建sql脚本。

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
        r"""创建spark作业

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


    def CreateSparkAppForTDLC(self, request):
        r"""创建tdlc spark作业

        :param request: Request instance for CreateSparkAppForTDLC.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppForTDLCRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkAppForTDLCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkAppForTDLC", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkAppForTDLCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSparkAppTask(self, request):
        r"""启动Spark作业

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
        r"""本接口（CreateSparkSessionBatchSQL）用于向Spark作业引擎提交Spark SQL批任务。

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


    def CreateSparkSubmitTask(self, request):
        r"""本接口（CreateSparkSubmitTask）用于提交SparkSbumit批流任务。

        :param request: Request instance for CreateSparkSubmitTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateSparkSubmitTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateSparkSubmitTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSparkSubmitTask", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSparkSubmitTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStandardEngineResourceGroup(self, request):
        r"""创建标准引擎资源组

        :param request: Request instance for CreateStandardEngineResourceGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateStandardEngineResourceGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateStandardEngineResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateStandardEngineResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateStandardEngineResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateStoreLocation(self, request):
        r"""该接口（CreateStoreLocation）新增或覆盖计算结果存储位置。

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
        r"""本接口（CreateTable）用于生成建表SQL。

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
        r"""本接口（CreateTask）用于创建并执行SQL任务。（推荐使用CreateTasks接口）

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
        r"""本接口（CreateTasks），用于批量创建并执行SQL任务

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
        r"""废弃接口，申请下线

        按顺序创建任务（已经废弃，后期不再维护，请使用接口CreateTasks）

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


    def CreateTcIcebergTable(self, request):
        r"""创建TIceberg表

        :param request: Request instance for CreateTcIcebergTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTcIcebergTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTcIcebergTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTcIcebergTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTcIcebergTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrainingJobInstance(self, request):
        r"""基于配置创建实例并提交 RayJob

        :param request: Request instance for CreateTrainingJobInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateTrainingJobInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateTrainingJobInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrainingJobInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrainingJobInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUser(self, request):
        r"""创建用户

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


    def CreateUserRole(self, request):
        r"""创建用户角色

        :param request: Request instance for CreateUserRole.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateUserRoleRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateUserRoleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserRole", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserRoleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUserVpcConnection(self, request):
        r"""创建用户vpc连接到指定引擎网络

        :param request: Request instance for CreateUserVpcConnection.
        :type request: :class:`tencentcloud.dlc.v20210125.models.CreateUserVpcConnectionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.CreateUserVpcConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUserVpcConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUserVpcConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateWorkGroup(self, request):
        r"""创建工作组

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


    def DeleteApiKey(self, request):
        r"""删除 API Key

        :param request: Request instance for DeleteApiKey.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteApiKeyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteApiKeyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteApiKey", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteApiKeyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBenchmarkTask(self, request):
        r"""删除性能评测任务

        :param request: Request instance for DeleteBenchmarkTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteBenchmarkTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteBenchmarkTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBenchmarkTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBenchmarkTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCHDFSBindingProduct(self, request):
        r"""此接口（DeleteCHDFSBindingProduct）用于删除元数据加速桶和产品绑定关系

        :param request: Request instance for DeleteCHDFSBindingProduct.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteCHDFSBindingProductRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteCHDFSBindingProductResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCHDFSBindingProduct", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCHDFSBindingProductResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteClusterGroup(self, request):
        r"""删除集群组

        :param request: Request instance for DeleteClusterGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteClusterGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteClusterGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteClusterGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteClusterGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDataEngine(self, request):
        r"""删除数据引擎

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


    def DeleteDataMaskStrategy(self, request):
        r"""删除数据脱敏策略

        :param request: Request instance for DeleteDataMaskStrategy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteDataMaskStrategyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteDataMaskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDataMaskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDataMaskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDeployment(self, request):
        r"""删除指定部署

        :param request: Request instance for DeleteDeployment.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteDeploymentRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteInferenceService(self, request):
        r"""删除推理服务（含所有部署）

        :param request: Request instance for DeleteInferenceService.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteInferenceServiceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteJobSpec(self, request):
        r"""根据配置ID删除作业配置

        :param request: Request instance for DeleteJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLab(self, request):
        r"""删除数据实验室

        :param request: Request instance for DeleteLab.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteLabRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteLabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLab", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMetaDatabase(self, request):
        r"""本接口（DeleteMetaDatabase）用于一键删除元数据库

        :param request: Request instance for DeleteMetaDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteMetaDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteMetaDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMetaDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMetaDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMlflowServer(self, request):
        r"""删除 MlFlow Server 请求

        :param request: Request instance for DeleteMlflowServer.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteMlflowServerRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteMlflowServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMlflowServer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMlflowServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModel(self, request):
        r"""删除模型及其所有版本（平台托管模型同时删除 COS 文件，用户自带桶仅删除元数据）

        :param request: Request instance for DeleteModel.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteModelRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModel", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteModelVersion(self, request):
        r"""删除模型版本（平台托管模型同时删除 COS 文件，用户自带桶仅删除元数据）

        :param request: Request instance for DeleteModelVersion.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteModelVersionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteModelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteModelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteModelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNativeSparkSession(self, request):
        r"""根据spark session名称销毁eg spark session

        :param request: Request instance for DeleteNativeSparkSession.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteNativeSparkSessionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteNativeSparkSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNativeSparkSession", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNativeSparkSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNotebookSession(self, request):
        r"""本接口（DeleteNotebookSession）用于删除交互式session（notebook）

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


    def DeletePartitionQueue(self, request):
        r"""删除资源队列

        :param request: Request instance for DeletePartitionQueue.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeletePartitionQueueRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeletePartitionQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePartitionQueue", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePartitionQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRayCluster(self, request):
        r"""删除集群

        :param request: Request instance for DeleteRayCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteRayClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteRayClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRayCluster", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRayClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRayJob(self, request):
        r"""根据任务ID删除Ray任务

        :param request: Request instance for DeleteRayJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteRayJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteRayJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRayJob", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRayJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteResourceConfig(self, request):
        r"""删除资源配置模板

        :param request: Request instance for DeleteResourceConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteResourceConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteScript(self, request):
        r"""该接口（DeleteScript）用于删除sql脚本。

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
        r"""删除spark作业

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


    def DeleteStandardEngineResourceGroup(self, request):
        r"""删除标准引擎资源组

        :param request: Request instance for DeleteStandardEngineResourceGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteStandardEngineResourceGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteStandardEngineResourceGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteStandardEngineResourceGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteStandardEngineResourceGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTable(self, request):
        r"""删除表

        :param request: Request instance for DeleteTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteThirdPartyAccessUser(self, request):
        r"""本接口（RegisterThirdPartyAccessUser）用于移除第三方平台访问

        :param request: Request instance for DeleteThirdPartyAccessUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteThirdPartyAccessUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteThirdPartyAccessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteThirdPartyAccessUser", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteThirdPartyAccessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrainingJobInstance(self, request):
        r"""删除训练作业实例（软删除本地元数据，仅终态实例可删除）

        :param request: Request instance for DeleteTrainingJobInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteTrainingJobInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteTrainingJobInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrainingJobInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrainingJobInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrainingJobSpec(self, request):
        r"""删除训练作业配置

        :param request: Request instance for DeleteTrainingJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteTrainingJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteTrainingJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrainingJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrainingJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUser(self, request):
        r"""删除用户

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


    def DeleteUserVpcConnection(self, request):
        r"""删除用户vpc到引擎网络的连接

        :param request: Request instance for DeleteUserVpcConnection.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DeleteUserVpcConnectionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DeleteUserVpcConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUserVpcConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUserVpcConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsersFromWorkGroup(self, request):
        r"""从工作组中删除用户

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
        r"""删除工作组

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
        r"""查询sql查询界面高级设置

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


    def DescribeBindablePrometheus(self, request):
        r"""查询 TKE 集群可绑定的托管 Prometheus 实例列表。若 TKE 已绑定，返回 Bound=true 与 BoundInstance；若未绑定，返回 Bound=false 与候选列表 Instances（同 VPC 实例前置）。

        :param request: Request instance for DescribeBindablePrometheus.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeBindablePrometheusRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeBindablePrometheusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBindablePrometheus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBindablePrometheusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClsTopics(self, request):
        r"""查询 CLS 日志主题列表：TopicName 走模糊匹配，TopicId 走精确匹配，两者均可为空；分页返回。

        :param request: Request instance for DescribeClsTopics.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeClsTopicsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeClsTopicsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClsTopics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClsTopicsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterEventLogSwitch(self, request):
        r"""查询指定 TKE 集群是否开启了事件日志。已开启时同时返回关联的 CLS 日志集 ID、日志主题 ID 与主题所在地域。

        :param request: Request instance for DescribeClusterEventLogSwitch.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterEventLogSwitchRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterEventLogSwitchResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterEventLogSwitch", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterEventLogSwitchResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterGroup(self, request):
        r"""根据集群组 ID 获取集群组详情。支持通过 IncludeDeleted 参数控制是否返回已软删除的记录（用于悬挂 cluster 回显场景）。

        :param request: Request instance for DescribeClusterGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterGroupClusters(self, request):
        r"""计算组关联 cluster 使用情况响应

        :param request: Request instance for DescribeClusterGroupClusters.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterGroupClustersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterGroupClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterGroupClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterGroupClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClusterMonitorInfos(self, request):
        r"""查询任务监控指标信息

        :param request: Request instance for DescribeClusterMonitorInfos.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterMonitorInfosRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeClusterMonitorInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClusterMonitorInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClusterMonitorInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDLCCatalogAccess(self, request):
        r"""查询DLC Catalog授权列表

        :param request: Request instance for DescribeDLCCatalogAccess.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCCatalogAccessRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDLCCatalogAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDLCCatalogAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDLCCatalogAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDMSDatabase(self, request):
        r"""DMS元数据获取库

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
        r"""DMS元数据获取分区

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
        r"""DMS元数据获取表

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
        r"""DMS元数据获取表列表

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
        r"""本接口根据名称用于获取数据引擎详细信息

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
        r"""查询数据引擎事件

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
        r"""本接口（DescribeDataEngineImageVersions）用于获取独享集群大版本镜像列表。

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
        r"""本接口（DescribeDataEnginePythonSparkImages）用于获取PYSPARK镜像列表

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


    def DescribeDataEngineSessionParameters(self, request):
        r"""本接口（DescribeDataEngineSessionParameters）用于获取指定小版本下的Session配置。

        :param request: Request instance for DescribeDataEngineSessionParameters.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineSessionParametersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEngineSessionParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEngineSessionParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEngineSessionParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataEngines(self, request):
        r"""本接口（DescribeDataEngines）用于查询DataEngines信息列表.

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


    def DescribeDataEnginesScaleDetail(self, request):
        r"""查询引擎规格详情

        :param request: Request instance for DescribeDataEnginesScaleDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginesScaleDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataEnginesScaleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataEnginesScaleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataEnginesScaleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDataMaskStrategies(self, request):
        r"""查询数据脱敏列表接口

        :param request: Request instance for DescribeDataMaskStrategies.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDataMaskStrategiesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDataMaskStrategiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDataMaskStrategies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDataMaskStrategiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabase(self, request):
        r"""本接口（DescribeDatabase）,查询数据库详细信息

        :param request: Request instance for DescribeDatabase.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeDatabaseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeDatabaseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabase", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        r"""本接口（DescribeDatabases）用于查询数据库列表。

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
        r"""本接口（DescribeDatasourceConnection）用于查询数据源信息

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


    def DescribeEmrClusterInfo(self, request):
        r"""按 EMR 集群 ID 精确查询单个 EMR 集群的详细信息，包含 VPC、COS Bucket、关联 TKE 集群 ID、资源用量等。

        :param request: Request instance for DescribeEmrClusterInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeEmrClusterInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeEmrClusterInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEmrClusterInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEmrClusterInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEngineNetworks(self, request):
        r"""查询引擎网络信息

        :param request: Request instance for DescribeEngineNetworks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineNetworksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineNetworksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEngineNetworks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEngineNetworksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEngineNodeSpec(self, request):
        r"""查询引擎可用的节点规格

        :param request: Request instance for DescribeEngineNodeSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineNodeSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeEngineNodeSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEngineNodeSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEngineNodeSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEngineUsageInfo(self, request):
        r"""本接口根据引擎ID查询数据引擎资源使用情况

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


    def DescribeFlowDetailList(self, request):
        r"""分页查询指定分区的流程详情列表，包含每个流程的基本信息和活动列表

        :param request: Request instance for DescribeFlowDetailList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeFlowDetailListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeFlowDetailListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowDetailList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowDetailListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowList(self, request):
        r"""查询指定分区的流程列表

        :param request: Request instance for DescribeFlowList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeFlowListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeFlowListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeForbiddenTablePro(self, request):
        r"""本接口（DescribeForbiddenTablePro）用于查询被禁用的表属性列表（新）

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
        r"""查询托管存储指定目录的Summary

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
        r"""查询用户的托管存储信息

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
        r"""获取LakeFs上task执行结果访问信息

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


    def DescribeMCPSubUin(self, request):
        r"""获取账户子账户信息

        :param request: Request instance for DescribeMCPSubUin.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMCPSubUinRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMCPSubUinResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMCPSubUin", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMCPSubUinResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMCPTask(self, request):
        r"""该接口（DescribeTasks）用于查询任务列表

        :param request: Request instance for DescribeMCPTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMCPTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMCPTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMCPTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMCPTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMCPTaskResult(self, request):
        r"""获取任务结果查询

        :param request: Request instance for DescribeMCPTaskResult.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMCPTaskResultRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMCPTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMCPTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMCPTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMlFlowConfig(self, request):
        r"""查询训练实例的 MLflow 接入配置。
        MlFlowMode 表示接入的 mlflow 模式，支持 local=Sidecar / remote=已有 Server / none=不启用。云上默认为 remote。
        MlFlowUrl 表示访问的 MLflow URL。
        RunID, ExperimentID 对应MLflow 实验追踪用的参数 RunID, ExperimentID

        :param request: Request instance for DescribeMlFlowConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMlFlowConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMlFlowConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMlFlowConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMlFlowConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMlflowServer(self, request):
        r"""查询 MlFlow Server 状态

        :param request: Request instance for DescribeMlflowServer.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMlflowServerRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMlflowServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMlflowServer", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMlflowServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMlflowServerEvents(self, request):
        r"""查询 MlFlow Server K8s 事件

        :param request: Request instance for DescribeMlflowServerEvents.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMlflowServerEventsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMlflowServerEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMlflowServerEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMlflowServerEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMlflowServerPods(self, request):
        r"""MlFlow Server Pod 列表响应

        :param request: Request instance for DescribeMlflowServerPods.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeMlflowServerPodsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeMlflowServerPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMlflowServerPods", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMlflowServerPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelEngines(self, request):
        r"""根据模型 UID 查询该模型可选的推理引擎列表。后端自动根据模型的 SupportedEngines 声明或 ModelType 进行引擎过滤

        :param request: Request instance for DescribeModelEngines.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeModelEnginesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeModelEnginesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelEngines", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelEnginesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeModelTaskOptions(self, request):
        r"""查询指定模型类型下可选的任务类型列表。

        :param request: Request instance for DescribeModelTaskOptions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeModelTaskOptionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeModelTaskOptionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeModelTaskOptions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeModelTaskOptionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNativeSparkSessions(self, request):
        r"""根据资源组获取spark session列表

        :param request: Request instance for DescribeNativeSparkSessions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNativeSparkSessionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNativeSparkSessionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNativeSparkSessions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNativeSparkSessionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkConnections(self, request):
        r"""查询网络配置列表

        :param request: Request instance for DescribeNetworkConnections.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeNetworkConnectionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeNetworkConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNotebookSession(self, request):
        r"""本接口（DescribeNotebookSession）用于查询交互式 session详情信息

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
        r"""本接口（DescribeNotebookSessionLog）用于查询交互式 session日志

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
        r"""本接口（DescribeNotebookSessionStatement）用于查询session 中执行任务的详情

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
        r"""本接口（DescribeNotebookSessionStatementSqlResult）用于获取statement运行结果。

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
        r"""本接口（DescribeNotebookSessionStatements）用于查询Session中执行的任务列表

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
        r"""本接口（DescribeNotebookSessions）用于查询交互式 session列表

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


    def DescribeOtherCHDFSBindingList(self, request):
        r"""此接口（DescribeOtherCHDFSBindingList）用于查询其他产品元数据加速桶绑定列表

        :param request: Request instance for DescribeOtherCHDFSBindingList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeOtherCHDFSBindingListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeOtherCHDFSBindingListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOtherCHDFSBindingList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOtherCHDFSBindingListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePartitionDetail(self, request):
        r"""获取指定资源分区详情

        :param request: Request instance for DescribePartitionDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribePartitionDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribePartitionDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePartitionDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePartitionDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePartitionQueues(self, request):
        r"""查询指定分区的所有队列列表

        :param request: Request instance for DescribePartitionQueues.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribePartitionQueuesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribePartitionQueuesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePartitionQueues", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePartitionQueuesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePartitions(self, request):
        r"""获取分区列表信息

        :param request: Request instance for DescribePartitions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribePartitionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribePartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePostTrainingPreset(self, request):
        r"""获取零代码后训练的推荐参数和资源规格配置

        :param request: Request instance for DescribePostTrainingPreset.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribePostTrainingPresetRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribePostTrainingPresetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePostTrainingPreset", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePostTrainingPresetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRecommendedParams(self, request):
        r"""获取推荐的高级参数

        :param request: Request instance for DescribeRecommendedParams.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeRecommendedParamsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeRecommendedParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRecommendedParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRecommendedParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResourceGroupUsageInfo(self, request):
        r"""本接口根据资源组ID查询资源组CU使用情况

        :param request: Request instance for DescribeResourceGroupUsageInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeResourceGroupUsageInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeResourceGroupUsageInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeResourceGroupUsageInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeResourceGroupUsageInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeResultDownload(self, request):
        r"""查询结果下载任务

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


    def DescribeSaleRegions(self, request):
        r"""查询可售卖的地域列表，仅返回状态为AVAILABLE的地域

        :param request: Request instance for DescribeSaleRegions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSaleRegionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSaleRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSaleRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSaleRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSaleResourceInfo(self, request):
        r"""查询当前地域可售卖的资源规格、最大配额，以及库存情况。StatusCategory 与 DescribePartitionAvailableQuota 数据同源，将实时可新增数量映射为库存分级；当请求 Region 与资源池实际部署地域不一致，或服务 cold-start 快照尚未就绪时，StatusCategory 为 null。

        :param request: Request instance for DescribeSaleResourceInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSaleResourceInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSaleResourceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSaleResourceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSaleResourceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeScripts(self, request):
        r"""该接口（DescribeScripts）用于查询SQL脚本列表

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


    def DescribeSessionImageVersion(self, request):
        r"""获取指定大版本下所有小版本的所有内置镜像

        :param request: Request instance for DescribeSessionImageVersion.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSessionImageVersionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSessionImageVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSessionImageVersion", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSessionImageVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkAppJob(self, request):
        r"""查询spark作业信息

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
        r"""查询spark作业列表

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
        r"""查询Spark作业的运行任务列表

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
        r"""本接口（DescribeSparkSessionBatchSQL）用于查询Spark SQL批任务运行状态

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


    def DescribeSparkSessionBatchSQLCost(self, request):
        r"""本接口（DescribeSparkSessionBatchSQLCost）用于查询Spark SQL批任务消耗

        :param request: Request instance for DescribeSparkSessionBatchSQLCost.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSQLCostRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSparkSessionBatchSQLCostResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSparkSessionBatchSQLCost", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSparkSessionBatchSQLCostResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSparkSessionBatchSqlLog(self, request):
        r"""本接口（DescribeSparkSessionBatchSqlLog）用于查询Spark SQL批任务日志

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


    def DescribeStandardEngineResourceGroupConfigInfo(self, request):
        r"""查询标准引擎资源组信息

        :param request: Request instance for DescribeStandardEngineResourceGroupConfigInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeStandardEngineResourceGroupConfigInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeStandardEngineResourceGroupConfigInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStandardEngineResourceGroupConfigInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStandardEngineResourceGroupConfigInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStandardEngineResourceGroups(self, request):
        r"""查询标准引擎资源组信息

        :param request: Request instance for DescribeStandardEngineResourceGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeStandardEngineResourceGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeStandardEngineResourceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeStandardEngineResourceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeStandardEngineResourceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeStoreLocation(self, request):
        r"""查询计算结果存储位置。

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


    def DescribeSubUserAccessPolicy(self, request):
        r"""本接口（DescribeSubUserAccessPolicy）用于开通了第三方平台访问的用户，查询其子用户的访问策略

        :param request: Request instance for DescribeSubUserAccessPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeSubUserAccessPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeSubUserAccessPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubUserAccessPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubUserAccessPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTCLakeMetaInstance(self, request):
        r"""是否成功开通TCLake

        :param request: Request instance for DescribeTCLakeMetaInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTCLakeMetaInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTCLakeMetaInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTCLakeMetaInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTCLakeMetaInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTable(self, request):
        r"""本接口（DescribeTable），用于查询单个表的详细信息。

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


    def DescribeTablePartitions(self, request):
        r"""本接口（DescribeTablePartitions）用于查询数据表分区信息

        :param request: Request instance for DescribeTablePartitions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTablePartitionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTablePartitionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTablePartitions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTablePartitionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTables(self, request):
        r"""本接口（DescribeTables）用于查询数据表列表。

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
        r"""本接口（DescribeTables）用于查询数据表名称列表

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


    def DescribeTaskDetail(self, request):
        r"""该接口（DescribeTaskDetail）用于查询历史任务详情

        :param request: Request instance for DescribeTaskDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskList(self, request):
        r"""该接口（DescribleTasks）用于查询任务列表

        :param request: Request instance for DescribeTaskList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskLog(self, request):
        r"""本接口（DescribeTaskLog）用于获取spark 作业任务日志详情

        :param request: Request instance for DescribeTaskLog.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskLogRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskMonitorInfos(self, request):
        r"""查询任务监控指标信息

        :param request: Request instance for DescribeTaskMonitorInfos.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskMonitorInfosRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskMonitorInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskMonitorInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskMonitorInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskResourceUsage(self, request):
        r"""返回任务洞察资源用量

        :param request: Request instance for DescribeTaskResourceUsage.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResourceUsageRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTaskResourceUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResourceUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResourceUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskResult(self, request):
        r"""查询任务结果，仅支持30天以内的任务查询结果，且返回数据大小超过近50M会进行截断。

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
        r"""该接口（DescribeTasks）用于查询任务列表

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


    def DescribeTasksAnalysis(self, request):
        r"""该接口用于洞察分析列表

        :param request: Request instance for DescribeTasksAnalysis.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksAnalysisRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasksCostInfo(self, request):
        r"""该接口（DescribeTasksCostInfo）用于查询任务消耗

        :param request: Request instance for DescribeTasksCostInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksCostInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksCostInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksCostInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksCostInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTasksOverview(self, request):
        r"""查看任务概览页

        :param request: Request instance for DescribeTasksOverview.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksOverviewRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTasksOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTasksOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTasksOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeThirdPartyAccessUser(self, request):
        r"""本接口（RegisterThirdPartyAccessUser）查询开通第三方平台访问的用户信息

        :param request: Request instance for DescribeThirdPartyAccessUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeThirdPartyAccessUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeThirdPartyAccessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeThirdPartyAccessUser", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeThirdPartyAccessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTkeClusterImportInfo(self, request):
        r"""按 EMR 集群 ID 查询已导入的 TKE 集群详情，返回 tke_cluster 表中该条导入记录的核心字段，并对 LoadBalancerId / PrometheusInstanceId / ContainerLogTopicId 三个 ID 分别回查腾讯云 API 获取对应名称一并返回。名称查询失败或查不到时对应字段返回空字符串，不影响主接口返回。

        :param request: Request instance for DescribeTkeClusterImportInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTkeClusterImportInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTkeClusterImportInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTkeClusterImportInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTkeClusterImportInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingCheckpoints(self, request):
        r"""列出训练实例 Checkpoint 文件列表的响应

        :param request: Request instance for DescribeTrainingCheckpoints.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTrainingCheckpointsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTrainingCheckpointsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingCheckpoints", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingCheckpointsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingJobInstance(self, request):
        r"""查询训练实例详情

        :param request: Request instance for DescribeTrainingJobInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTrainingJobInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTrainingJobInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingJobInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingJobInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrainingJobSpec(self, request):
        r"""获取训练作业配置详情

        :param request: Request instance for DescribeTrainingJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeTrainingJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeTrainingJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrainingJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrainingJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUDFPolicy(self, request):
        r"""获取UDF权限信息

        :param request: Request instance for DescribeUDFPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUDFPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUDFPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUDFPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUDFPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpdatableDataEngines(self, request):
        r"""查询可更新配置的引擎列表

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
        r"""查询用户自定义引擎参数

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
        r"""获取用户详细信息

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


    def DescribeUserRegisterTime(self, request):
        r"""该接口（DescribeUserRegisterTime）用于查询当前用户注册时间，并判断是否是老用户。

        :param request: Request instance for DescribeUserRegisterTime.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserRegisterTimeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserRegisterTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserRegisterTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserRegisterTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserRoles(self, request):
        r"""列举用户角色信息

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
        r"""获取用户类型

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


    def DescribeUserVpcConnection(self, request):
        r"""查询用户vpc到引擎网络的连接

        :param request: Request instance for DescribeUserVpcConnection.
        :type request: :class:`tencentcloud.dlc.v20210125.models.DescribeUserVpcConnectionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.DescribeUserVpcConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserVpcConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserVpcConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsers(self, request):
        r"""获取用户列表信息

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
        r"""本接口（DescribeViews）用于查询数据视图列表。

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
        r"""获取工作组详细信息

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
        r"""获取工作组列表

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
        r"""解绑用户鉴权策略

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
        r"""解绑工作组鉴权策略

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
        r"""DMS元数据删除库

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
        r"""DMS元数据删除分区

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
        r"""DMS元数据删除表

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
        r"""生成创建托管表语句

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


    def GenerateInternalTable(self, request):
        r"""建表

        :param request: Request instance for GenerateInternalTable.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GenerateInternalTableRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GenerateInternalTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateInternalTable", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateInternalTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetExampleDetail(self, request):
        r"""根据 exampleId 获取单个案例详情

        :param request: Request instance for GetExampleDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetExampleDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetExampleDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetExampleDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetExampleDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInferenceModel(self, request):
        r"""获取单个模型详情

        :param request: Request instance for GetInferenceModel.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetInferenceModelRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetInferenceModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInferenceModel", params, headers=headers)
            response = json.loads(body)
            model = models.GetInferenceModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetInferenceService(self, request):
        r"""获取单个推理服务详情

        :param request: Request instance for GetInferenceService.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetInferenceServiceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.GetInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetJobSpec(self, request):
        r"""根据配置ID获取作业配置详情

        :param request: Request instance for GetJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.GetJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabDetail(self, request):
        r"""获取实验室详情

        :param request: Request instance for GetLabDetail.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabDetailRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabDetail", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabEvent(self, request):
        r"""获取实验室的事件流（基于 K8s Event + CLS 日志）

        :param request: Request instance for GetLabEvent.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabEventRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabEvent", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabHistory(self, request):
        r"""获取实验室的状态变更历史记录

        :param request: Request instance for GetLabHistory.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabHistoryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabHistory", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabPodYaml(self, request):
        r"""获取数据实验室Pod的YAML内容

        :param request: Request instance for GetLabPodYaml.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabPodYamlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabPodYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabPodYaml", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabPodYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabPods(self, request):
        r"""获取数据实验室的Pod列表

        :param request: Request instance for GetLabPods.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabPodsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabPods", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabServiceUrls(self, request):
        r"""获取实验室ide访问地址

        :param request: Request instance for GetLabServiceUrls.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabServiceUrlsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabServiceUrlsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabServiceUrls", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabServiceUrlsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetLabYaml(self, request):
        r"""获取数据实验室对应的RayCluster YAML内容

        :param request: Request instance for GetLabYaml.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetLabYamlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetLabYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetLabYaml", params, headers=headers)
            response = json.loads(body)
            model = models.GetLabYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetModelConfig(self, request):
        r"""获取模型 config.json 配置（默认最新版本）

        :param request: Request instance for GetModelConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetModelConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetModelConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetModelConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetModelConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetModelFiles(self, request):
        r"""获取模型文件树（默认最新版本）

        :param request: Request instance for GetModelFiles.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetModelFilesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetModelFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetModelFiles", params, headers=headers)
            response = json.loads(body)
            model = models.GetModelFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetModelReadme(self, request):
        r"""获取模型 README 信息（默认最新版本）

        :param request: Request instance for GetModelReadme.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetModelReadmeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetModelReadmeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetModelReadme", params, headers=headers)
            response = json.loads(body)
            model = models.GetModelReadmeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetOptimizerPolicy(self, request):
        r"""GetOptimizerPolicy

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


    def GetRayCluster(self, request):
        r"""获取Ray集群详情请求

        :param request: Request instance for GetRayCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayCluster", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayClusterEvent(self, request):
        r"""获取Ray集群的事件流（基于 K8s Event + CLS 日志）

        :param request: Request instance for GetRayClusterEvent.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterEventRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayClusterEvent", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayClusterEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayClusterHistory(self, request):
        r"""获取集群状态历史

        :param request: Request instance for GetRayClusterHistory.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterHistoryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayClusterHistory", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayClusterHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayClusterPodYaml(self, request):
        r"""获取集群Pod的YAML内容

        :param request: Request instance for GetRayClusterPodYaml.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterPodYamlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterPodYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayClusterPodYaml", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayClusterPodYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayClusterPods(self, request):
        r"""获取集群的Pod列表

        :param request: Request instance for GetRayClusterPods.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterPodsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayClusterPods", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayClusterPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayClusterYaml(self, request):
        r"""获取RayCluster的YAML内容

        :param request: Request instance for GetRayClusterYaml.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterYamlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayClusterYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayClusterYaml", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayClusterYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJob(self, request):
        r"""根据任务ID获取Ray任务详情

        :param request: Request instance for GetRayJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJob", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJobEvent(self, request):
        r"""通过 ResourceManager 调用 CLS SearchLog API 查询作业相关日志。不返回总数，使用 Context 进行翻页，ListOver 标识是否还有更多数据。

        :param request: Request instance for GetRayJobEvent.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobEventRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJobEvent", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJobEventLog(self, request):
        r"""获取作业事件日志

        :param request: Request instance for GetRayJobEventLog.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobEventLogRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobEventLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJobEventLog", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobEventLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJobHistory(self, request):
        r"""根据任务ID获取Ray任务的历史执行记录

        :param request: Request instance for GetRayJobHistory.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobHistoryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobHistoryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJobHistory", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobHistoryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJobPodYaml(self, request):
        r"""获取Pod的YAML内容

        :param request: Request instance for GetRayJobPodYaml.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobPodYamlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobPodYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJobPodYaml", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobPodYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJobPods(self, request):
        r"""获取作业的Pod列表

        :param request: Request instance for GetRayJobPods.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobPodsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobPodsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJobPods", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobPodsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetRayJobYaml(self, request):
        r"""获取RayJob的YAML内容

        :param request: Request instance for GetRayJobYaml.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetRayJobYamlRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetRayJobYamlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetRayJobYaml", params, headers=headers)
            response = json.loads(body)
            model = models.GetRayJobYamlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetResourceConfig(self, request):
        r"""获取资源配置模板详情

        :param request: Request instance for GetResourceConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GetResourceConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GetResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.GetResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantDLCCatalogAccess(self, request):
        r"""授权访问DLC Catalog

        :param request: Request instance for GrantDLCCatalogAccess.
        :type request: :class:`tencentcloud.dlc.v20210125.models.GrantDLCCatalogAccessRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.GrantDLCCatalogAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantDLCCatalogAccess", params, headers=headers)
            response = json.loads(body)
            model = models.GrantDLCCatalogAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportExternalCluster(self, request):
        r"""通过 ClusterType 区分两种导入模式：TKE（直接导入裸 TKE 集群，ClusterId 为 TKE 集群 ID）或 EMR（通过 EMR 集群导入，ClusterId 为 EMR 集群 ID，底层会关联查询对应的 TKE 集群 ID 一并落库）。两种模式均将 TKE 集群 ID 存入 tke_cluster 表。接口是异步的，返回的 WorkflowId 可用于轮询注册进度；ResourcePoolId / ResourcePoolCode 为资源池的唯一标识。

        :param request: Request instance for ImportExternalCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ImportExternalClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ImportExternalClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportExternalCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ImportExternalClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ImportTkeCluster(self, request):
        r"""将用户在控制台选择的 EMR-TKE 集群及配套的 COS Bucket、Prometheus 实例、负载均衡、容器日志主题等资源，注册为 DLC 的外部资源池（EXTERNAL_TKE）。接口是异步的，返回的 WorkflowId 可用于轮询注册进度；ResourcePoolId / ResourcePoolCode 为资源池的唯一标识。

        :param request: Request instance for ImportTkeCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ImportTkeClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ImportTkeClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ImportTkeCluster", params, headers=headers)
            response = json.loads(body)
            model = models.ImportTkeClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitializeTCLake(self, request):
        r"""开通TCLake

        :param request: Request instance for InitializeTCLake.
        :type request: :class:`tencentcloud.dlc.v20210125.models.InitializeTCLakeRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.InitializeTCLakeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitializeTCLake", params, headers=headers)
            response = json.loads(body)
            model = models.InitializeTCLakeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LaunchStandardEngineResourceGroups(self, request):
        r"""启动标准引擎资源组

        :param request: Request instance for LaunchStandardEngineResourceGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.LaunchStandardEngineResourceGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.LaunchStandardEngineResourceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LaunchStandardEngineResourceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.LaunchStandardEngineResourceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListApiKeys(self, request):
        r"""列出 API Key

        :param request: Request instance for ListApiKeys.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListApiKeysRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListApiKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListApiKeys", params, headers=headers)
            response = json.loads(body)
            model = models.ListApiKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListAvailableApiKeys(self, request):
        r"""列出空闲 API Key（未绑定服务）

        :param request: Request instance for ListAvailableApiKeys.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListAvailableApiKeysRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListAvailableApiKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListAvailableApiKeys", params, headers=headers)
            response = json.loads(body)
            model = models.ListAvailableApiKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListBenchmarkSummary(self, request):
        r"""查询评测排行榜（所有模型的评测汇总数据）

        :param request: Request instance for ListBenchmarkSummary.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListBenchmarkSummaryRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListBenchmarkSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListBenchmarkSummary", params, headers=headers)
            response = json.loads(body)
            model = models.ListBenchmarkSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListBenchmarkTasks(self, request):
        r"""列出性能评测任务

        :param request: Request instance for ListBenchmarkTasks.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListBenchmarkTasksRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListBenchmarkTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListBenchmarkTasks", params, headers=headers)
            response = json.loads(body)
            model = models.ListBenchmarkTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListClusterGroups(self, request):
        r"""列出所有集群组

        :param request: Request instance for ListClusterGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListClusterGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListClusterGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListClusterGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ListClusterGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDeploymentReplicas(self, request):
        r"""列出部署的副本列表

        :param request: Request instance for ListDeploymentReplicas.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListDeploymentReplicasRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListDeploymentReplicasResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDeploymentReplicas", params, headers=headers)
            response = json.loads(body)
            model = models.ListDeploymentReplicasResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListDeployments(self, request):
        r"""列出推理服务的部署列表

        :param request: Request instance for ListDeployments.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListDeploymentsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListDeploymentsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListDeployments", params, headers=headers)
            response = json.loads(body)
            model = models.ListDeploymentsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListExampleCategories(self, request):
        r"""获取所有案例分类

        :param request: Request instance for ListExampleCategories.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListExampleCategoriesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListExampleCategoriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListExampleCategories", params, headers=headers)
            response = json.loads(body)
            model = models.ListExampleCategoriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListExampleDifficulties(self, request):
        r"""获取所有案例分类

        :param request: Request instance for ListExampleDifficulties.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListExampleDifficultiesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListExampleDifficultiesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListExampleDifficulties", params, headers=headers)
            response = json.loads(body)
            model = models.ListExampleDifficultiesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListExampleTags(self, request):
        r"""返回标签去重列表，按出现频次从高到低排序。

        :param request: Request instance for ListExampleTags.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListExampleTagsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListExampleTagsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListExampleTags", params, headers=headers)
            response = json.loads(body)
            model = models.ListExampleTagsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListExamples(self, request):
        r"""案例列表

        :param request: Request instance for ListExamples.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListExamplesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListExamplesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListExamples", params, headers=headers)
            response = json.loads(body)
            model = models.ListExamplesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListImages(self, request):
        r"""列出所有镜像

        :param request: Request instance for ListImages.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListImagesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListImagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListImages", params, headers=headers)
            response = json.loads(body)
            model = models.ListImagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListInferenceEngines(self, request):
        r"""列出推理引擎

        :param request: Request instance for ListInferenceEngines.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListInferenceEnginesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListInferenceEnginesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListInferenceEngines", params, headers=headers)
            response = json.loads(body)
            model = models.ListInferenceEnginesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListInferenceModels(self, request):
        r"""列出推理模型（支持关键词过滤 + 分页）

        :param request: Request instance for ListInferenceModels.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListInferenceModelsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListInferenceModelsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListInferenceModels", params, headers=headers)
            response = json.loads(body)
            model = models.ListInferenceModelsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListInferenceServices(self, request):
        r"""列出推理服务（支持关键词和状态过滤 + 分页）

        :param request: Request instance for ListInferenceServices.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListInferenceServicesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListInferenceServicesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListInferenceServices", params, headers=headers)
            response = json.loads(body)
            model = models.ListInferenceServicesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJobSpecs(self, request):
        r"""分页查询作业配置列表

        :param request: Request instance for ListJobSpecs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListJobSpecsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListJobSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJobSpecs", params, headers=headers)
            response = json.loads(body)
            model = models.ListJobSpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListJobsBySpec(self, request):
        r"""分页查询某作业配置下产生的所有作业实例

        :param request: Request instance for ListJobsBySpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListJobsBySpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListJobsBySpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListJobsBySpec", params, headers=headers)
            response = json.loads(body)
            model = models.ListJobsBySpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListLabs(self, request):
        r"""列出实验室列表

        :param request: Request instance for ListLabs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListLabsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListLabsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListLabs", params, headers=headers)
            response = json.loads(body)
            model = models.ListLabsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListMlflowServerTrainingInstances(self, request):
        r"""查询 MlFlow Server 关联的训练实例列表

        :param request: Request instance for ListMlflowServerTrainingInstances.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListMlflowServerTrainingInstancesRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListMlflowServerTrainingInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListMlflowServerTrainingInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ListMlflowServerTrainingInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListMlflowServers(self, request):
        r"""列出 MlFlow Server

        :param request: Request instance for ListMlflowServers.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListMlflowServersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListMlflowServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListMlflowServers", params, headers=headers)
            response = json.loads(body)
            model = models.ListMlflowServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListModelVersions(self, request):
        r"""列出模型所有版本

        :param request: Request instance for ListModelVersions.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListModelVersionsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListModelVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListModelVersions", params, headers=headers)
            response = json.loads(body)
            model = models.ListModelVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRayClusterJobs(self, request):
        r"""查询指定 Ray 集群下提交的所有作业，分页返回。底层委托给 ListRayJobs，强制注入 ClusterId 作为过滤条件。

        :param request: Request instance for ListRayClusterJobs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListRayClusterJobsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListRayClusterJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRayClusterJobs", params, headers=headers)
            response = json.loads(body)
            model = models.ListRayClusterJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRayClusters(self, request):
        r"""列出所有集群

        :param request: Request instance for ListRayClusters.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListRayClustersRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListRayClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRayClusters", params, headers=headers)
            response = json.loads(body)
            model = models.ListRayClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRayJobs(self, request):
        r"""根据集群ID列出所有Ray任务

        :param request: Request instance for ListRayJobs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListRayJobsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListRayJobsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRayJobs", params, headers=headers)
            response = json.loads(body)
            model = models.ListRayJobsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListRegionLbs(self, request):
        r"""列出用户在指定地域下的 CLB 负载均衡实例，返回实例 ID、名称与网络类型（OPEN/INTERNAL）。

        :param request: Request instance for ListRegionLbs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListRegionLbsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListRegionLbsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListRegionLbs", params, headers=headers)
            response = json.loads(body)
            model = models.ListRegionLbsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListResourceConfigs(self, request):
        r"""列出所有资源配置模板

        :param request: Request instance for ListResourceConfigs.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListResourceConfigsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListResourceConfigsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListResourceConfigs", params, headers=headers)
            response = json.loads(body)
            model = models.ListResourceConfigsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListServiceApiKeys(self, request):
        r"""列出指定推理服务绑定的 API Key

        :param request: Request instance for ListServiceApiKeys.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListServiceApiKeysRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListServiceApiKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListServiceApiKeys", params, headers=headers)
            response = json.loads(body)
            model = models.ListServiceApiKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTaskJobLogDetail(self, request):
        r"""本接口（ListTaskJobLogDetail）用于获取spark 作业任务日志详情

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


    def ListTaskJobLogName(self, request):
        r"""本接口（ListTaskJobLogName）用于获取spark-jar日志名称列表

        :param request: Request instance for ListTaskJobLogName.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListTaskJobLogNameRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListTaskJobLogNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTaskJobLogName", params, headers=headers)
            response = json.loads(body)
            model = models.ListTaskJobLogNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTkeCosBuckets(self, request):
        r"""获取tke纳管cos列表

        :param request: Request instance for ListTkeCosBuckets.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListTkeCosBucketsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListTkeCosBucketsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTkeCosBuckets", params, headers=headers)
            response = json.loads(body)
            model = models.ListTkeCosBucketsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTrainingJobInstance(self, request):
        r"""列出训练作业实例

        :param request: Request instance for ListTrainingJobInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListTrainingJobInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListTrainingJobInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTrainingJobInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ListTrainingJobInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ListTrainingJobSpec(self, request):
        r"""获取训练作业配置的列表。

        :param request: Request instance for ListTrainingJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ListTrainingJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ListTrainingJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ListTrainingJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ListTrainingJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockMetaData(self, request):
        r"""元数据锁

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
        r"""修改sql查询界面高级设置。

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


    def ModifyClusterPriority(self, request):
        r"""修改集群的调度优先级（1-9，数字越大优先级越高）

        :param request: Request instance for ModifyClusterPriority.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyClusterPriorityRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyClusterPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyClusterPriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyClusterPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDataEngineDescription(self, request):
        r"""修改引擎描述信息

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
        r"""修改数据治理事件阈值

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


    def ModifyLabPriority(self, request):
        r"""修改实验室的调度优先级（1-9，数字越大优先级越高）

        :param request: Request instance for ModifyLabPriority.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyLabPriorityRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyLabPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLabPriority", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLabPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPartitionDescription(self, request):
        r"""修改分区描述

        :param request: Request instance for ModifyPartitionDescription.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyPartitionDescriptionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyPartitionDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPartitionDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPartitionDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPartitionQueue(self, request):
        r"""编辑资源队列：根据队列ID修改指定资源队列的名称、描述、资源规格列表和队列类型等信息。

        :param request: Request instance for ModifyPartitionQueue.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyPartitionQueueRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyPartitionQueueResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPartitionQueue", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPartitionQueueResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySparkApp(self, request):
        r"""更新spark作业

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
        r"""本接口（ModifySparkAppBatch）用于批量修改Spark作业参数配置

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


    def ModifySparkAppForTDLC(self, request):
        r"""更新tdlc spark作业

        :param request: Request instance for ModifySparkAppForTDLC.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppForTDLCRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifySparkAppForTDLCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySparkAppForTDLC", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySparkAppForTDLCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTrainingJobSpec(self, request):
        r"""就地更新训练作业配置

        :param request: Request instance for ModifyTrainingJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ModifyTrainingJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ModifyTrainingJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTrainingJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTrainingJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUser(self, request):
        r"""修改用户信息

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
        r"""修改用户类型。只有管理员用户能够调用该接口进行操作

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
        r"""修改工作组信息

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


    def PauseStandardEngineResourceGroups(self, request):
        r"""暂停标准引擎session

        :param request: Request instance for PauseStandardEngineResourceGroups.
        :type request: :class:`tencentcloud.dlc.v20210125.models.PauseStandardEngineResourceGroupsRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.PauseStandardEngineResourceGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("PauseStandardEngineResourceGroups", params, headers=headers)
            response = json.loads(body)
            model = models.PauseStandardEngineResourceGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDashboardOverview(self, request):
        r"""返回指定时间范围内所有推理服务的聚合 KPI 值。

        :param request: Request instance for QueryDashboardOverview.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryDashboardOverviewRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryDashboardOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDashboardOverview", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDashboardOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryDashboardServiceList(self, request):
        r"""查询监控大盘服务列表

        :param request: Request instance for QueryDashboardServiceList.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryDashboardServiceListRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryDashboardServiceListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryDashboardServiceList", params, headers=headers)
            response = json.loads(body)
            model = models.QueryDashboardServiceListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryInternalTableWarehouse(self, request):
        r"""本接口（QueryInternalTableWarehouse）用于获取原生表warehouse路径

        :param request: Request instance for QueryInternalTableWarehouse.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryInternalTableWarehouseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryInternalTableWarehouseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryInternalTableWarehouse", params, headers=headers)
            response = json.loads(body)
            model = models.QueryInternalTableWarehouseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMonitorOverview(self, request):
        r"""查询监控概览数据（瞬时值）

        :param request: Request instance for QueryMonitorOverview.
        :type request: :class:`tencentcloud.dlc.v20210125.models.QueryMonitorOverviewRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.QueryMonitorOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMonitorOverview", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMonitorOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryResult(self, request):
        r"""获取任务结果查询

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
        r"""该接口（QueryTaskCostDetail）用于查询任务消耗明细

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


    def RegisterThirdPartyAccessUser(self, request):
        r"""本接口（RegisterThirdPartyAccessUser）用于开通第三方平台访问

        :param request: Request instance for RegisterThirdPartyAccessUser.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RegisterThirdPartyAccessUserRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RegisterThirdPartyAccessUserResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RegisterThirdPartyAccessUser", params, headers=headers)
            response = json.loads(body)
            model = models.RegisterThirdPartyAccessUserResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDataEngine(self, request):
        r"""续费数据引擎

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
        r"""上报元数据心跳

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


    def RerunBenchmarkTask(self, request):
        r"""重新运行性能评测任务

        :param request: Request instance for RerunBenchmarkTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RerunBenchmarkTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RerunBenchmarkTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RerunBenchmarkTask", params, headers=headers)
            response = json.loads(body)
            model = models.RerunBenchmarkTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDataEngine(self, request):
        r"""重启引擎

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


    def RestartDeployment(self, request):
        r"""再次运行部署（以当前配置重新部署）

        :param request: Request instance for RestartDeployment.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RestartDeploymentRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RestartDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartInferenceService(self, request):
        r"""重启推理服务（操作所有部署）。

        :param request: Request instance for RestartInferenceService.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RestartInferenceServiceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RestartInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.RestartInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeTrainingJobInstance(self, request):
        r"""断点续训（克隆实例）

        :param request: Request instance for ResumeTrainingJobInstance.
        :type request: :class:`tencentcloud.dlc.v20210125.models.ResumeTrainingJobInstanceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.ResumeTrainingJobInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeTrainingJobInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeTrainingJobInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RevokeDLCCatalogAccess(self, request):
        r"""撤销DLC Catalog访问权限

        :param request: Request instance for RevokeDLCCatalogAccess.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RevokeDLCCatalogAccessRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RevokeDLCCatalogAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RevokeDLCCatalogAccess", params, headers=headers)
            response = json.loads(body)
            model = models.RevokeDLCCatalogAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackDataEngineImage(self, request):
        r"""回滚引擎镜像版本

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


    def RunJobSpec(self, request):
        r"""基于指定作业配置提交一次作业实例

        :param request: Request instance for RunJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.RunJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.RunJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.RunJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetOptimizerPolicy(self, request):
        r"""设置优化策略的接口

        :param request: Request instance for SetOptimizerPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SetOptimizerPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SetOptimizerPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetOptimizerPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.SetOptimizerPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartLab(self, request):
        r"""启动实验室

        :param request: Request instance for StartLab.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StartLabRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StartLabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartLab", params, headers=headers)
            response = json.loads(body)
            model = models.StartLabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMlflowServer(self, request):
        r"""启动 MlFlow Server（apply K8s 资源，幂等可重试）

        :param request: Request instance for StartMlflowServer.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StartMlflowServerRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StartMlflowServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMlflowServer", params, headers=headers)
            response = json.loads(body)
            model = models.StartMlflowServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartRayCluster(self, request):
        r"""启动集群

        :param request: Request instance for StartRayCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StartRayClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StartRayClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartRayCluster", params, headers=headers)
            response = json.loads(body)
            model = models.StartRayClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopBenchmarkTask(self, request):
        r"""停止性能评测任务

        :param request: Request instance for StopBenchmarkTask.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StopBenchmarkTaskRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StopBenchmarkTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopBenchmarkTask", params, headers=headers)
            response = json.loads(body)
            model = models.StopBenchmarkTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopDeployment(self, request):
        r"""停止部署

        :param request: Request instance for StopDeployment.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StopDeploymentRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StopDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.StopDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopInferenceService(self, request):
        r"""停止推理服务（操作所有部署）。

        :param request: Request instance for StopInferenceService.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StopInferenceServiceRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StopInferenceServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopInferenceService", params, headers=headers)
            response = json.loads(body)
            model = models.StopInferenceServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopLab(self, request):
        r"""停止实验室

        :param request: Request instance for StopLab.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StopLabRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StopLabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopLab", params, headers=headers)
            response = json.loads(body)
            model = models.StopLabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMlflowServer(self, request):
        r"""停止 MlFlow Server

        :param request: Request instance for StopMlflowServer.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StopMlflowServerRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StopMlflowServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMlflowServer", params, headers=headers)
            response = json.loads(body)
            model = models.StopMlflowServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopRayCluster(self, request):
        r"""停止集群

        :param request: Request instance for StopRayCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.StopRayClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.StopRayClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopRayCluster", params, headers=headers)
            response = json.loads(body)
            model = models.StopRayClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SubmitTrainingJob(self, request):
        r"""断点续训（克隆实例）

        :param request: Request instance for SubmitTrainingJob.
        :type request: :class:`tencentcloud.dlc.v20210125.models.SubmitTrainingJobRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.SubmitTrainingJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SubmitTrainingJob", params, headers=headers)
            response = json.loads(body)
            model = models.SubmitTrainingJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SuspendResumeDataEngine(self, request):
        r"""本接口用于控制挂起或启动数据引擎

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
        r"""切换主备集群

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
        r"""切换引擎镜像版本

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
        r"""解绑用户上的用户组

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


    def UnboundDatasourceHouse(self, request):
        r"""解绑数据源与队列

        :param request: Request instance for UnboundDatasourceHouse.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UnboundDatasourceHouseRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UnboundDatasourceHouseResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnboundDatasourceHouse", params, headers=headers)
            response = json.loads(body)
            model = models.UnboundDatasourceHouseResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnlockMetaData(self, request):
        r"""元数据解锁

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


    def UpdateApiKeyStatus(self, request):
        r"""更新 API Key 状态

        :param request: Request instance for UpdateApiKeyStatus.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateApiKeyStatusRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateApiKeyStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateApiKeyStatus", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateApiKeyStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateClusterGroup(self, request):
        r"""更新集群组

        :param request: Request instance for UpdateClusterGroup.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateClusterGroupRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateClusterGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateClusterGroup", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateClusterGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDataEngine(self, request):
        r"""本接口用于更新数据引擎配置

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
        r"""用户某种操作，触发引擎配置修改

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


    def UpdateDataMaskStrategy(self, request):
        r"""更新数据脱敏策略

        :param request: Request instance for UpdateDataMaskStrategy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateDataMaskStrategyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateDataMaskStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDataMaskStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDataMaskStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateDeployment(self, request):
        r"""更新部署配置

        :param request: Request instance for UpdateDeployment.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateDeploymentRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateEngineResourceGroupNetworkConfigInfo(self, request):
        r"""更新标准引擎资源组网络配置信息

        :param request: Request instance for UpdateEngineResourceGroupNetworkConfigInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateEngineResourceGroupNetworkConfigInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateEngineResourceGroupNetworkConfigInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateEngineResourceGroupNetworkConfigInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateEngineResourceGroupNetworkConfigInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateInferenceModel(self, request):
        r"""更新推理模型（编辑标签、描述、参数量）

        :param request: Request instance for UpdateInferenceModel.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateInferenceModelRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateInferenceModelResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateInferenceModel", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateInferenceModelResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateJobSpec(self, request):
        r"""更新已有作业配置的字段

        :param request: Request instance for UpdateJobSpec.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateJobSpecRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateJobSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateJobSpec", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateJobSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateJobSpecPriority(self, request):
        r"""修改作业配置的调度优先级（1-9，数字越大优先级越高）

        :param request: Request instance for UpdateJobSpecPriority.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateJobSpecPriorityRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateJobSpecPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateJobSpecPriority", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateJobSpecPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateLab(self, request):
        r"""更新实验室配置：仅在 CREATED / STOPPED / FAILED 终态可用；变更落 MySQL，下次 Start 按新 spec 创建 K8s 资源

        :param request: Request instance for UpdateLab.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateLabRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateLabResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateLab", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateLabResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateNetworkConnection(self, request):
        r"""更新网络配置

        :param request: Request instance for UpdateNetworkConnection.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateNetworkConnectionRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateNetworkConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateNetworkConnection", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateNetworkConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRayCluster(self, request):
        r"""更新集群配置：仅在 CREATED / STOPPED / FAILED 终态可用；变更落 MySQL，下次 Start 按新 spec 创建 K8s 资源

        :param request: Request instance for UpdateRayCluster.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateRayClusterRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateRayClusterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRayCluster", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRayClusterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRayJobPriority(self, request):
        r"""更新处于 SUBMITTED/PENDING 状态的作业的优先级。仅 SUBMITTED/PENDING 状态的作业允许调整优先级。内部通过调用 Neutrino 的 UpdateJobConfig 接口更新 ENVIRONMENT 配置中的 priority 字段。

        :param request: Request instance for UpdateRayJobPriority.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateRayJobPriorityRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateRayJobPriorityResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateRayJobPriority", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateRayJobPriorityResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateResourceConfig(self, request):
        r"""更新资源配置模板

        :param request: Request instance for UpdateResourceConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateResourceConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateResourceConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateResourceConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateResourceConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateRowFilter(self, request):
        r"""此接口用于更新行过滤规则。注意只能更新过滤规则，不能更新规格对象catalog，database和table。

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


    def UpdateServiceAuthConfig(self, request):
        r"""更新推理服务的 API-Key 鉴权配置（启用/停用）

        :param request: Request instance for UpdateServiceAuthConfig.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateServiceAuthConfigRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateServiceAuthConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateServiceAuthConfig", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateServiceAuthConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateStandardEngineResourceGroupBaseInfo(self, request):
        r"""更新标准引擎资源组基础信息

        :param request: Request instance for UpdateStandardEngineResourceGroupBaseInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateStandardEngineResourceGroupBaseInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateStandardEngineResourceGroupBaseInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateStandardEngineResourceGroupBaseInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateStandardEngineResourceGroupBaseInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateStandardEngineResourceGroupConfigInfo(self, request):
        r"""更新标准引擎资源组基础信息

        :param request: Request instance for UpdateStandardEngineResourceGroupConfigInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateStandardEngineResourceGroupConfigInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateStandardEngineResourceGroupConfigInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateStandardEngineResourceGroupConfigInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateStandardEngineResourceGroupConfigInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateStandardEngineResourceGroupResourceInfo(self, request):
        r"""更新标准引擎资源组基础信息

        :param request: Request instance for UpdateStandardEngineResourceGroupResourceInfo.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateStandardEngineResourceGroupResourceInfoRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateStandardEngineResourceGroupResourceInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateStandardEngineResourceGroupResourceInfo", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateStandardEngineResourceGroupResourceInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUDFPolicy(self, request):
        r"""UDP权限修改

        :param request: Request instance for UpdateUDFPolicy.
        :type request: :class:`tencentcloud.dlc.v20210125.models.UpdateUDFPolicyRequest`
        :rtype: :class:`tencentcloud.dlc.v20210125.models.UpdateUDFPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateUDFPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateUDFPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateUserDataEngineConfig(self, request):
        r"""修改用户引擎自定义配置

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
        r"""升级引擎镜像

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