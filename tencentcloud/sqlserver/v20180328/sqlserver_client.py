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
from tencentcloud.sqlserver.v20180328 import models


class SqlserverClient(AbstractClient):
    _apiVersion = '2018-03-28'
    _endpoint = 'sqlserver.tencentcloudapi.com'
    _service = 'sqlserver'


    def AssociateSecurityGroups(self, request):
        """本接口(AssociateSecurityGroups)用于安全组批量绑定实例。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.AssociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def BalanceReadOnlyGroup(self, request):
        """本接口（BalanceReadOnlyGroup）用于根据预定义的权重平衡每个只读实例的路由权重。预定义权重可根据接口DescribeReadOnlyGroupAutoWeight查询。

        :param request: Request instance for BalanceReadOnlyGroup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.BalanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.BalanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("BalanceReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.BalanceReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneDB(self, request):
        """本接口（CloneDB）用于克隆数据库，只支持克隆到本实例，克隆时必须指定新库名称。

        :param request: Request instance for CloneDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CloneDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CloneDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneDB", params, headers=headers)
            response = json.loads(body)
            model = models.CloneDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseInterCommunication(self, request):
        """本接口（CloseInterCommunication）用于关闭实例互通。

        :param request: Request instance for CloseInterCommunication.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CloseInterCommunicationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CloseInterCommunicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseInterCommunication", params, headers=headers)
            response = json.loads(body)
            model = models.CloseInterCommunicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteExpansion(self, request):
        """本接口（CompleteExpansion）在实例发起扩容后，实例状态处于“升级待切换”时，可立即完成实例升级切换操作，无需等待可维护时间窗。本接口需要在实例低峰时调用，在完全切换成功前，存在部分库不可访问的风险。

        :param request: Request instance for CompleteExpansion.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CompleteExpansionRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CompleteExpansionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteExpansion", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteExpansionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CompleteMigration(self, request):
        """本接口（CompleteMigration）作用是完成一个迁移任务

        :param request: Request instance for CompleteMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CompleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CompleteMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CompleteMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CompleteMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccount(self, request):
        """本接口（CreateAccount）用于创建实例账号

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackup(self, request):
        """本接口(CreateBackup)用于创建备份。

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBackupMigration(self, request):
        """本接口（CreateBackupMigration）用于创建备份导入任务。

        :param request: Request instance for CreateBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBasicDBInstances(self, request):
        """本接口（CreateBasicDBInstances）用于创建基础版实例 (云盘)。

        :param request: Request instance for CreateBasicDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBasicDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBasicDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBasicDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBasicDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBusinessDBInstances(self, request):
        """本接口（CreateBusinessDBInstances）用于创建商业智能服务实例 (云盘)。

        :param request: Request instance for CreateBusinessDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBusinessDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBusinessDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBusinessIntelligenceFile(self, request):
        """本接口（CreateBusinessIntelligenceFile）用于添加商业智能服务文件。

        :param request: Request instance for CreateBusinessIntelligenceFile.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessIntelligenceFileRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBusinessIntelligenceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBusinessIntelligenceFile", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBusinessIntelligenceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudDBInstances(self, request):
        """本接口（CreateCloudDBInstances）用于创建高可用实例 (云盘)。

        :param request: Request instance for CreateCloudDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloudReadOnlyDBInstances(self, request):
        """本接口（CreateCloudReadOnlyDBInstances）用于创建只读实例 (云盘)。

        :param request: Request instance for CreateCloudReadOnlyDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudReadOnlyDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateCloudReadOnlyDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloudReadOnlyDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloudReadOnlyDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDB(self, request):
        """本接口（CreateDB）用于创建数据库。

        :param request: Request instance for CreateDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDB", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstances(self, request):
        """本接口（CreateDBInstances）用于创建高可用实例 (本地盘)

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIncrementalMigration(self, request):
        """本接口（CreateIncrementalMigration）用于创建增量备份导入任务。

        :param request: Request instance for CreateIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateMigration(self, request):
        """本接口（CreateMigration）作用是创建一个迁移任务

        :param request: Request instance for CreateMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateMigration", params, headers=headers)
            response = json.loads(body)
            model = models.CreateMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePublishSubscribe(self, request):
        """本接口（CreatePublishSubscribe）用于创建两个数据库之间的发布订阅关系。作为订阅者，不能再充当发布者，作为发布者可以有多个订阅者实例。

        :param request: Request instance for CreatePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreatePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreatePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyDBInstances(self, request):
        """本接口（CreateReadOnlyDBInstances）用于创建只读实例 (本地盘)。

        :param request: Request instance for CreateReadOnlyDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateReadOnlyDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateReadOnlyDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccount(self, request):
        """本接口（DeleteAccount）用于删除实例账号。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBackupMigration(self, request):
        """本接口（DeleteBackupMigration）用于删除备份导入任务。

        :param request: Request instance for DeleteBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBusinessIntelligenceFile(self, request):
        """本接口（DeleteBusinessIntelligenceFile）用于删除商业智能文件。

        :param request: Request instance for DeleteBusinessIntelligenceFile.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBusinessIntelligenceFileRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteBusinessIntelligenceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBusinessIntelligenceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBusinessIntelligenceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDB(self, request):
        """本接口(DeleteDB)用于删除数据库。

        :param request: Request instance for DeleteDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDB", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBInstance(self, request):
        """本接口（DeleteDBInstance）用于释放回收站中的SQL server实例(立即下线)。释放后的实例将保存一段时间后物理销毁。其发布订阅将自动解除，其ro副本将自动释放。

        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIncrementalMigration(self, request):
        """本接口（DeleteIncrementalMigration）用于删除增量备份导入任务。

        :param request: Request instance for DeleteIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteMigration(self, request):
        """本接口（DeleteMigration）用于删除迁移任务

        :param request: Request instance for DeleteMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePublishSubscribe(self, request):
        """本接口（DeletePublishSubscribe）用于删除两个数据库间的发布订阅关系。

        :param request: Request instance for DeletePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeletePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeletePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRestoreTask(self, request):
        """本接口(DeleteRestoreTask)用于删除回档任务记录。

        :param request: Request instance for DeleteRestoreTask.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteRestoreTaskRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteRestoreTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRestoreTask", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRestoreTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivilegeByDB(self, request):
        """本接口(DescribeAccountPrivilegeByDB)用于查询数据库关联的账号和权限信息

        :param request: Request instance for DescribeAccountPrivilegeByDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountPrivilegeByDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountPrivilegeByDBResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivilegeByDB", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountPrivilegeByDBResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """本接口（DescribeAccounts）用于拉取实例账户列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccounts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupByFlowId(self, request):
        """本接口(DescribeBackupByFlowId)用于通过备份创建流程的ID查询创建的备份详情，流程ID可从接口CreateBackup中获得。

        :param request: Request instance for DescribeBackupByFlowId.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupByFlowIdRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupByFlowIdResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupByFlowId", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupByFlowIdResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupCommand(self, request):
        """本接口（DescribeBackupCommand）用于查询以规范的格式创建备份的命令。

        :param request: Request instance for DescribeBackupCommand.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupCommandRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupCommandResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupCommand", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupCommandResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupFiles(self, request):
        """本接口(DescribeBackupFiles)用于查询单库备份明细

        :param request: Request instance for DescribeBackupFiles.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupFilesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupMigration(self, request):
        """本接口（DescribeBackupMigration）用于创建增量备份导入任务。

        :param request: Request instance for DescribeBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupMonitor(self, request):
        """本接口(DescribeBackupMonitor)用于查询备份空间使用详情。

        :param request: Request instance for DescribeBackupMonitor.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMonitorRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupStatistical(self, request):
        """本接口(DescribeBackupStatistical)用于查询备份实时统计列表。

        :param request: Request instance for DescribeBackupStatistical.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupStatisticalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupStatisticalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupStatistical", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupStatisticalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupSummary(self, request):
        """本接口(DescribeBackupSummary)用于查询数据库备份概览信息。

        :param request: Request instance for DescribeBackupSummary.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupSummaryRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupSummaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupSummary", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupSummaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupUploadSize(self, request):
        """本接口（DescribeBackupUploadSize）用于查询上传的备份文件大小。在备份上传类型是COS_UPLOAD(备份放在业务的对象存储上)时有效。

        :param request: Request instance for DescribeBackupUploadSize.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupUploadSizeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupUploadSizeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupUploadSize", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupUploadSizeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackups(self, request):
        """本接口(DescribeBackups)用于查询备份列表。

        :param request: Request instance for DescribeBackups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBusinessIntelligenceFile(self, request):
        """本接口（DescribeBusinessIntelligenceFile）用于查询商业智能服务需要的文件。

        :param request: Request instance for DescribeBusinessIntelligenceFile.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBusinessIntelligenceFileRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBusinessIntelligenceFileResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBusinessIntelligenceFile", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBusinessIntelligenceFileResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCollationTimeZone(self, request):
        """本接口(DescribeCollationTimeZone)用于查询实例支持的字符集和时区。

        :param request: Request instance for DescribeCollationTimeZone.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCollationTimeZoneRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCollationTimeZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCollationTimeZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCollationTimeZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBackupStatistical(self, request):
        """本接口(DescribeCrossBackupStatistical)用于查询跨地域备份实时统计列表。

        :param request: Request instance for DescribeCrossBackupStatistical.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossBackupStatisticalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossBackupStatisticalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBackupStatistical", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBackupStatisticalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossRegionZone(self, request):
        """本接口(DescribeCrossRegionZone)根据主实例查询备机的容灾地域和可用区。

        :param request: Request instance for DescribeCrossRegionZone.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionZoneRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionZoneResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossRegionZone", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossRegionZoneResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossRegions(self, request):
        """本接口(DescribeCrossRegions)用于查询跨地域备份的目标地域。

        :param request: Request instance for DescribeCrossRegions.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBCharsets(self, request):
        """本接口（DescribeDBCharsets）用于查询实例支持的数据库字符集。

        :param request: Request instance for DescribeDBCharsets.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBCharsetsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBCharsetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBCharsets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBCharsetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceInter(self, request):
        """本接口（DescribeDBInstanceInter）用于查询互通实例的信息。

        :param request: Request instance for DescribeDBInstanceInter.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstanceInterRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstanceInterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceInter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceInterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """本接口(DescribeDBInstances)用于查询实例列表。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstancesAttribute(self, request):
        """本接口（DescribeDBInstancesAttribute）用于查询实例附属属性

        :param request: Request instance for DescribeDBInstancesAttribute.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBPrivilegeByAccount(self, request):
        """本接口(DescribeDBPrivilegeByAccount)用于查询账号关联的数据库和权限信息

        :param request: Request instance for DescribeDBPrivilegeByAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBPrivilegeByAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBPrivilegeByAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBPrivilegeByAccount", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBPrivilegeByAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBRestoreTime(self, request):
        """本接口（DescribeDBRestoreTime）用于查询可回档的数据库

        :param request: Request instance for DescribeDBRestoreTime.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBRestoreTimeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBRestoreTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBRestoreTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBRestoreTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBs(self, request):
        """本接口（DescribeDBs）用于查询数据库列表。**已废弃，请使用接口DescribeDatabases**

        :param request: Request instance for DescribeDBs.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBsNormal(self, request):
        """本接口(DescribeDBsNormal)用于查询数据库配置信息，此接口不包含数据库的关联账号。**此接口已废弃，请使用DescribeDatabasesNormal。**

        :param request: Request instance for DescribeDBsNormal.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsNormalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsNormalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBsNormal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBsNormalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseNames(self, request):
        """本接口（DescribeDatabaseNames）查询账户关联的数据库名称。

        :param request: Request instance for DescribeDatabaseNames.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabaseNamesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabaseNamesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseNames", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseNamesResponse()
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
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesResponse`

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


    def DescribeDatabasesNormal(self, request):
        """本接口(DescribeDBsNormal)用于查询数据库配置信息，此接口不包含数据库的关联账号

        :param request: Request instance for DescribeDatabasesNormal.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesNormalRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDatabasesNormalResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabasesNormal", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabasesNormalResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowStatus(self, request):
        """本接口(DescribeFlowStatus)用于查询流程状态。

        :param request: Request instance for DescribeFlowStatus.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHASwitchLog(self, request):
        """本接口(DescribeHASwitchLog)用于手动主备切换。

        :param request: Request instance for DescribeHASwitchLog.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeHASwitchLogRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeHASwitchLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHASwitchLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHASwitchLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIncrementalMigration(self, request):
        """本接口（DescribeIncrementalMigration）用于查询增量备份导入任务。

        :param request: Request instance for DescribeIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInquiryPriceParameter(self, request):
        """本接口（DescribeInquiryPriceParameter）用于查询实例询价计费参数。当前接口查询实例新购的计费参数。内部接口用于活动页售卖场景。

        :param request: Request instance for DescribeInquiryPriceParameter.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInquiryPriceParameterRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInquiryPriceParameterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInquiryPriceParameter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInquiryPriceParameterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceByOrders(self, request):
        """本接口（DescribeInstanceByOrders）用于根据订单号查询资源ID

        :param request: Request instance for DescribeInstanceByOrders.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceByOrdersRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceByOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceByOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceByOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParamRecords(self, request):
        """该接口（DescribeInstanceParamRecords）用于查询实例参数修改历史。

        :param request: Request instance for DescribeInstanceParamRecords.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamRecordsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamRecordsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParamRecords", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamRecordsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceParams(self, request):
        """该接口（DescribeInstanceParams）用于查询实例的参数列表。

        :param request: Request instance for DescribeInstanceParams.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceParamsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceParams", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceParamsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTasks(self, request):
        """本接口（DescribeInstanceTasks）用于查询实例相关的异步任务列表。

        :param request: Request instance for DescribeInstanceTasks.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTasksRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceTradeParameter(self, request):
        """本接口（DescribeInstanceTradeParameter）用于查询实例的计费参数，当前接口默认返回创建实例时需要的计费参数。内部接口用于活动页售卖场景。

        :param request: Request instance for DescribeInstanceTradeParameter.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTradeParameterRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeInstanceTradeParameterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceTradeParameter", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceTradeParameterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaintenanceSpan(self, request):
        """本接口（DescribeMaintenanceSpan）根据实例ID查询该实例的可维护时间窗。

        :param request: Request instance for DescribeMaintenanceSpan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMaintenanceSpanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMaintenanceSpanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintenanceSpan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintenanceSpanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationDatabases(self, request):
        """本接口（DescribeMigrationDatabases）的作用是查询待迁移数据库列表

        :param request: Request instance for DescribeMigrationDatabases.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDatabasesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDatabasesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationDatabases", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationDatabasesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrationDetail(self, request):
        """本接口（DescribeMigrationDetail）用于查询迁移任务的详细情况

        :param request: Request instance for DescribeMigrationDetail.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrationDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMigrations(self, request):
        """本接口（DescribeMigrations）根据输入的限定条件，查询符合条件的迁移任务列表

        :param request: Request instance for DescribeMigrations.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMigrations", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMigrationsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """本接口（DescribeOrders）用于查询订单信息

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeOrders", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeOrdersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductConfig(self, request):
        """本接口 (DescribeProductConfig) 用于查询售卖规格配置。

        :param request: Request instance for DescribeProductConfig.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductSpec(self, request):
        """本接口 (DescribeProductSpec) 用于查询全地域售卖规格配置（内部前端使用不公开）

        :param request: Request instance for DescribeProductSpec.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductSpecRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjectSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePublishSubscribe(self, request):
        """本接口（DescribePublishSubscribe）用于查询发布订阅关系列表。

        :param request: Request instance for DescribePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupAutoWeight(self, request):
        """本接口（DescribeReadOnlyGroupAutoWeight）用于查询只读组的自动权重分配结果，在接口BalanceReadOnlyGroup接口中按照自动权重分配结果进行路由权重分配。

        :param request: Request instance for DescribeReadOnlyGroupAutoWeight.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupAutoWeightRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupAutoWeightResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupAutoWeight", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupAutoWeightResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupByReadOnlyInstance(self, request):
        """本接口（DescribeReadOnlyGroupByReadOnlyInstance）用于通过只读副本实例ID查询其所在的只读组。

        :param request: Request instance for DescribeReadOnlyGroupByReadOnlyInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupByReadOnlyInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupByReadOnlyInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupByReadOnlyInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupByReadOnlyInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupDetails(self, request):
        """本接口（DescribeReadOnlyGroupDetails）用于查询只读组详情。

        :param request: Request instance for DescribeReadOnlyGroupDetails.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReadOnlyGroupList(self, request):
        """本接口（DescribeReadOnlyGroupList）用于查询只读组列表。

        :param request: Request instance for DescribeReadOnlyGroupList.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupListRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroupList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegions(self, request):
        """本接口 (DescribeRegions) 用于查询售卖地域信息。

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRegularBackupPlan(self, request):
        """本接口（DescribeRegularBackupPlan）用于查询实例定期备份保留计划

        :param request: Request instance for DescribeRegularBackupPlan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegularBackupPlanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegularBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRegularBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRegularBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTask(self, request):
        """本接口（DescribeRestoreTask）用于查询回档任务列表。

        :param request: Request instance for DescribeRestoreTask.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTaskRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTaskResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTask", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTaskResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRestoreTimeRange(self, request):
        """本接口(DescribeRestoreTimeRange)用于查询按照时间点可回档的时间范围。

        :param request: Request instance for DescribeRestoreTimeRange.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTimeRangeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRestoreTimeRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRestoreTimeRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRestoreTimeRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRollbackTime(self, request):
        """本接口（DescribeRollbackTime）用于查询实例可回档时间范围

        :param request: Request instance for DescribeRollbackTime.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRollbackTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRollbackTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowlogs(self, request):
        """本接口（DescribeSlowlogs）用于获取慢查询日志文件信息

        :param request: Request instance for DescribeSlowlogs.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecSellStatus(self, request):
        """本接口（DescribeSpecSellStatus）用于查询售卖规格状态信息，其中包括售卖状态，参考价格等(实际价格以询价接口为准)。

        :param request: Request instance for DescribeSpecSellStatus.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSpecSellStatusRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSpecSellStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecSellStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecSellStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpgradeInstanceCheck(self, request):
        """本接口（DescribeUpgradeInstanceCheck）用于在实例变配前，预检查实例变配的影响情况等。

        :param request: Request instance for DescribeUpgradeInstanceCheck.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUpgradeInstanceCheckRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUpgradeInstanceCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpgradeInstanceCheck", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpgradeInstanceCheckResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadBackupInfo(self, request):
        """本接口（DescribeUploadBackupInfo）用于查询备份上传权限。

        :param request: Request instance for DescribeUploadBackupInfo.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUploadBackupInfoRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUploadBackupInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadBackupInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadBackupInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUploadIncrementalInfo(self, request):
        """本接口（DescribeUploadIncrementalInfo）用于查询增量备份上传权限。

        :param request: Request instance for DescribeUploadIncrementalInfo.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUploadIncrementalInfoRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeUploadIncrementalInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUploadIncrementalInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUploadIncrementalInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeXEvents(self, request):
        """本接口（DescribeXEvents）用于查询扩展事件列表。

        :param request: Request instance for DescribeXEvents.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeXEventsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeXEventsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeXEvents", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeXEventsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """本接口 (DescribeZones) 用于查询当前可售卖的可用区信息。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeZones", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeZonesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateDBInstances(self, request):
        """本接口（InquiryPriceCreateDBInstances）用于查询申请实例价格。

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewDBInstance(self, request):
        """本接口（InquiryPriceRenewDBInstance）用于查询包年包月实例的续费价格。

        :param request: Request instance for InquiryPriceRenewDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceRenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceUpgradeDBInstance(self, request):
        """本接口（InquiryPriceUpgradeDBInstance）用于查询包年包月实例升级变配的价格。

        :param request: Request instance for InquiryPriceUpgradeDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceUpgradeDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceUpgradeDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivilege(self, request):
        """本接口（ModifyAccountPrivilege）用于修改实例账户权限。

        :param request: Request instance for ModifyAccountPrivilege.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPrivilege", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPrivilegeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountRemark(self, request):
        """本接口（ModifyAccountRemark）用于修改账户备注。

        :param request: Request instance for ModifyAccountRemark.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupMigration(self, request):
        """本接口（ModifyBackupMigration）用于修改备份导入任务。

        :param request: Request instance for ModifyBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupName(self, request):
        """本接口(ModifyBackupName)用于修改备份任务名称。

        :param request: Request instance for ModifyBackupName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupStrategy(self, request):
        """本接口（ModifyBackupStrategy）用于修改备份策略

        :param request: Request instance for ModifyBackupStrategy.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupStrategyRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCloseWanIp(self, request):
        """本接口(ModifyCloseWanIp)用于关闭实例外网。

        :param request: Request instance for ModifyCloseWanIp.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCloseWanIpRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCloseWanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCloseWanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCloseWanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCrossBackupStrategy(self, request):
        """本接口(ModifyCrossBackupStrategy)用于开启、关闭地域备份策略。

        :param request: Request instance for ModifyCrossBackupStrategy.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCrossBackupStrategyRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyCrossBackupStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCrossBackupStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCrossBackupStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBEncryptAttributes(self, request):
        """本接口（ModifyDBEncryptAttributes）用于开启、关闭数据库的TDE加密功能。

        :param request: Request instance for ModifyDBEncryptAttributes.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBEncryptAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBEncryptAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBEncryptAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        """本接口（ModifyDBInstanceName）用于修改实例名字。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceNetwork(self, request):
        """本接口（ModifyDBInstanceNetwork）用于修改运行中实例的网络，仅支持从VPC网络到VPC网络的转换

        :param request: Request instance for ModifyDBInstanceNetwork.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceNote(self, request):
        """本接口（ModifyDBInstanceNote）用于修改实例备注信息。

        :param request: Request instance for ModifyDBInstanceNote.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNoteRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNoteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceNote", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceNoteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceProject(self, request):
        """本接口（ModifyDBInstanceProject）用于修改数据库实例所属项目。

        :param request: Request instance for ModifyDBInstanceProject.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceRenewFlag(self, request):
        """本接口（ModifyDBInstanceRenewFlag）用于修改实例续费标记

        :param request: Request instance for ModifyDBInstanceRenewFlag.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceRenewFlagRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSSL(self, request):
        """本接口（ModifyDBInstanceSSL）用于开启\关闭\更新SSL加密

        :param request: Request instance for ModifyDBInstanceSSL.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSSLRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSSLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSSL", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSSLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBName(self, request):
        """本接口（ModifyDBName）用于更新数据库名。

        :param request: Request instance for ModifyDBName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBRemark(self, request):
        """本接口（ModifyDBRemark）用于修改数据库备注。

        :param request: Request instance for ModifyDBRemark.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBRemark", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBRemarkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDReadable(self, request):
        """本接口（ModifyDReadable）用于开通或者关闭备机只读

        :param request: Request instance for ModifyDReadable.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDReadableRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDReadableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDReadable", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDReadableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseCDC(self, request):
        """本接口(ModifyDatabaseCDC)用于开启、关闭数据库数据变更捕获(CDC)

        :param request: Request instance for ModifyDatabaseCDC.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCDCRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCDCResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseCDC", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseCDCResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseCT(self, request):
        """本接口(ModifyDatabaseCT)用于启用、禁用数据库数据变更跟踪(CT)

        :param request: Request instance for ModifyDatabaseCT.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCTRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseCTResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseCT", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseCTResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseMdf(self, request):
        """本接口(ModifyDatabaseMdf)用于收缩数据库mdf(Shrink mdf)。**本接口已废弃，请使用接口ModifyDatabaseShrinkMDF**。

        :param request: Request instance for ModifyDatabaseMdf.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseMdfRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseMdfResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseMdf", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseMdfResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseShrinkMDF(self, request):
        """本接口(ModifyDatabaseShrinkDMF)用于收缩数据库mdf(Shrink mdf)。

        :param request: Request instance for ModifyDatabaseShrinkMDF.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseShrinkMDFRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDatabaseShrinkMDFResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseShrinkMDF", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseShrinkMDFResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIncrementalMigration(self, request):
        """本接口（ModifyIncrementalMigration）用于修改增量备份导入任务。

        :param request: Request instance for ModifyIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceEncryptAttributes(self, request):
        """本接口（ModifyInstanceEncryptAttributes）用于开通实例的TDE加密功能。

        :param request: Request instance for ModifyInstanceEncryptAttributes.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceEncryptAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceEncryptAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceEncryptAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceParam(self, request):
        """本接口(ModifyInstanceParam)用于修改云数据库实例的参数。
        <b>注意</b>：如果修改的参数是需要<b>重启实例</b>的，那么实例将会按照WaitSwitch参数的设置(可能是立即执行也可能在可维护时间窗内自动执行)在执行参数修改时<b>重启实例</b>。
        您可以通过DescribeInstanceParams接口查询修改参数时是否会重启实例，以免导致您的实例不符合预期重启。

        :param request: Request instance for ModifyInstanceParam.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceParamRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyInstanceParamResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceParam", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceParamResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaintenanceSpan(self, request):
        """本接口（ModifyMaintenanceSpan）用于修改实例的可维护时间窗

        :param request: Request instance for ModifyMaintenanceSpan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMaintenanceSpanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMaintenanceSpanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintenanceSpan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintenanceSpanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMigration(self, request):
        """本接口（ModifyMigration）可以修改已有的迁移任务信息

        :param request: Request instance for ModifyMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMigration", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyOpenWanIp(self, request):
        """本接口(ModifyOpenWanIp)用于开通实例外网。

        :param request: Request instance for ModifyOpenWanIp.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyOpenWanIpRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyOpenWanIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyOpenWanIp", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyOpenWanIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublishSubscribe(self, request):
        """本接口（ModifyPublishSubscribe）用于修改实例的发布订阅关系。

        :param request: Request instance for ModifyPublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublishSubscribe", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublishSubscribeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPublishSubscribeName(self, request):
        """本接口（ModifyPublishSubscribeName）修改发布订阅的名称。

        :param request: Request instance for ModifyPublishSubscribeName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPublishSubscribeName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPublishSubscribeNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReadOnlyGroupDetails(self, request):
        """本接口（ModifyReadOnlyGroupDetails）用于修改只读组详情。

        :param request: Request instance for ModifyReadOnlyGroupDetails.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyReadOnlyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyReadOnlyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReadOnlyGroupDetails", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReadOnlyGroupDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenInterCommunication(self, request):
        """本接口（OpenInterCommunication）用于打开实例的互通，实例互通可以实现商业智能服务相互联通。

        :param request: Request instance for OpenInterCommunication.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.OpenInterCommunicationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.OpenInterCommunicationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenInterCommunication", params, headers=headers)
            response = json.loads(body)
            model = models.OpenInterCommunicationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def QueryMigrationCheckProcess(self, request):
        """本接口（QueryMigrationCheckProcess）的作用是查询迁移检查任务的进度，适用于迁移源的类型为TencentDB for SQLServer 的迁移方式

        :param request: Request instance for QueryMigrationCheckProcess.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.QueryMigrationCheckProcessRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.QueryMigrationCheckProcessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("QueryMigrationCheckProcess", params, headers=headers)
            response = json.loads(body)
            model = models.QueryMigrationCheckProcessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecycleDBInstance(self, request):
        """本接口（RecycleDBInstance）用于主动回收已下线的SQLSERVER实例

        :param request: Request instance for RecycleDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RecycleDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RecycleDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecycleDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RecycleDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RecycleReadOnlyGroup(self, request):
        """本接口（RecycleReadOnlyGroup）立即回收只读组的资源，只读组占用的vip等资源将立即释放且不可找回。

        :param request: Request instance for RecycleReadOnlyGroup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RecycleReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RecycleReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RecycleReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RecycleReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveBackups(self, request):
        """本接口（RemoveBackups）可以删除用户手动创建的备份文件。待删除的备份策略可以是实例备份，也可以是多库备份。

        :param request: Request instance for RemoveBackups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RemoveBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RemoveBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveBackups", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewDBInstance(self, request):
        """本接口（RenewDBInstance）用于续费实例。当被续费实例是按量计费实例时，则按量计费实例转为包年包月计费方式。
        按量计费实例转包年包月询价可通过(InquiryPriceRenewDBInstance)接口获得。

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewPostpaidDBInstance(self, request):
        """本接口（RenewPostpaidDBInstance）用于将通过接口TerminateDBInstance手动隔离的按量计费实例从回收站中恢复。

        :param request: Request instance for RenewPostpaidDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RenewPostpaidDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RenewPostpaidDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewPostpaidDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewPostpaidDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        """本接口（ResetAccountPassword）用于重置实例的账号密码。

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAccountPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAccountPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDBInstance(self, request):
        """本接口（RestartDBInstance）用于重启数据库实例。

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestoreInstance(self, request):
        """本接口（RestoreInstance）用于按照备份集回档数据库。

        :param request: Request instance for RestoreInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RollbackInstance(self, request):
        """本接口（RollbackInstance）用于按照时间点回档实例

        :param request: Request instance for RollbackInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RollbackInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RollbackInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RunMigration(self, request):
        """本接口（RunMigration）用于启动迁移任务，开始迁移

        :param request: Request instance for RunMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RunMigration", params, headers=headers)
            response = json.loads(body)
            model = models.RunMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartBackupMigration(self, request):
        """本接口（StartBackupMigration）用于启动备份导入任务。

        :param request: Request instance for StartBackupMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartBackupMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartBackupMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartBackupMigration", params, headers=headers)
            response = json.loads(body)
            model = models.StartBackupMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartIncrementalMigration(self, request):
        """本接口（StartIncrementalMigration）用于启动增量备份导入任务。

        :param request: Request instance for StartIncrementalMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartIncrementalMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartIncrementalMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartIncrementalMigration", params, headers=headers)
            response = json.loads(body)
            model = models.StartIncrementalMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartInstanceXEvent(self, request):
        """本接口（StartInstanceXEvent）用于开启、关闭扩展事件。

        :param request: Request instance for StartInstanceXEvent.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartInstanceXEventRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartInstanceXEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartInstanceXEvent", params, headers=headers)
            response = json.loads(body)
            model = models.StartInstanceXEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartMigrationCheck(self, request):
        """本接口（StartMigrationCheck）的作用是启动一个迁移前的校验任务，适用于迁移源的类型为TencentDB for SQLServer 的迁移方式

        :param request: Request instance for StartMigrationCheck.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartMigrationCheckRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartMigrationCheckResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartMigrationCheck", params, headers=headers)
            response = json.loads(body)
            model = models.StartMigrationCheckResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopMigration(self, request):
        """本接口（StopMigration）作用是中止一个迁移任务

        :param request: Request instance for StopMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StopMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StopMigrationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopMigration", params, headers=headers)
            response = json.loads(body)
            model = models.StopMigrationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchCloudInstanceHA(self, request):
        """本接口(SwitchCloudInstanceHA)用于手动主备切换。

        :param request: Request instance for SwitchCloudInstanceHA.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.SwitchCloudInstanceHARequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.SwitchCloudInstanceHAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchCloudInstanceHA", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchCloudInstanceHAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDBInstance(self, request):
        """本接口(TerminateDBInstance)用于主动隔离实例，使得实例进入回收站。

        :param request: Request instance for TerminateDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.TerminateDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.TerminateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """本接口（UpgradeDBInstance）用于升级实例

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))