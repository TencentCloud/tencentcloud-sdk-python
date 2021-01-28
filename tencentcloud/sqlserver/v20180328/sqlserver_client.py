# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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
            body = self.call("AssociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloneDB(self, request):
        """本接口（CloneDB）用于克隆数据库，只支持克隆到本实例，克隆时必须指定新库名称。

        :param request: Request instance for CloneDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CloneDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CloneDBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloneDB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneDBResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CompleteExpansion(self, request):
        """本接口（CompleteExpansion）在实例发起扩容后，实例状态处于“升级待切换”时，可立即完成实例升级切换操作，无需等待可维护时间窗。本接口需要在实例低峰时调用，在完全切换成功前，存在部分库不可访问的风险。

        :param request: Request instance for CompleteExpansion.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CompleteExpansionRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CompleteExpansionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteExpansion", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteExpansionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CompleteMigration(self, request):
        """本接口（CompleteMigration）作用是完成一个迁移任务

        :param request: Request instance for CompleteMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CompleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CompleteMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CompleteMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CompleteMigrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAccount(self, request):
        """本接口（CreateAccount）用于创建实例账号

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBackup(self, request):
        """本接口(CreateBackup)用于创建备份。

        :param request: Request instance for CreateBackup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBackupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBackup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBackupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBasicDBInstances(self, request):
        """本接口（CreateBasicDBInstances）用于创建SQL server基础版实例。

        :param request: Request instance for CreateBasicDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateBasicDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateBasicDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBasicDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBasicDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDB(self, request):
        """本接口（CreateDB）用于创建数据库。

        :param request: Request instance for CreateDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDBInstances(self, request):
        """本接口（CreateDBInstances）用于创建实例。

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateMigration(self, request):
        """本接口（CreateMigration）作用是创建一个迁移任务

        :param request: Request instance for CreateMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateMigrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreatePublishSubscribe(self, request):
        """本接口（CreatePublishSubscribe）用于创建两个数据库之间的发布订阅关系。作为订阅者，不能再充当发布者，作为发布者可以有多个订阅者实例。

        :param request: Request instance for CreatePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreatePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreatePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreatePublishSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreatePublishSubscribeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateReadOnlyDBInstances(self, request):
        """本接口（CreateReadOnlyDBInstances）用于添加只读副本实例。

        :param request: Request instance for CreateReadOnlyDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.CreateReadOnlyDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.CreateReadOnlyDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReadOnlyDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReadOnlyDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAccount(self, request):
        """本接口（DeleteAccount）用于删除实例账号。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAccountResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDB(self, request):
        """本接口(DeleteDB)用于删除数据库。

        :param request: Request instance for DeleteDB.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDB", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDBResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDBInstance(self, request):
        """本接口（DeleteDBInstance）用于释放回收站中的SQL server实例。释放后的实例将保存一段时间后物理销毁。其发布订阅将自动解除，其ro副本将自动释放。

        :param request: Request instance for DeleteDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteMigration(self, request):
        """本接口（DeleteMigration）用于删除迁移任务

        :param request: Request instance for DeleteMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeleteMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteMigrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeletePublishSubscribe(self, request):
        """本接口（DeletePublishSubscribe）用于删除两个数据库间的发布订阅关系。

        :param request: Request instance for DeletePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DeletePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DeletePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeletePublishSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeletePublishSubscribeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccounts(self, request):
        """本接口（DescribeAccounts）用于拉取实例账户列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeAccountsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccounts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackupByFlowId(self, request):
        """本接口(DescribeBackupByFlowId)用于通过备份创建流程的ID查询创建的备份详情，流程ID可从接口CreateBackup中获得。

        :param request: Request instance for DescribeBackupByFlowId.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupByFlowIdRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupByFlowIdResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupByFlowId", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupByFlowIdResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBackups(self, request):
        """本接口(DescribeBackups)用于查询备份列表。

        :param request: Request instance for DescribeBackups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCrossRegionZone(self, request):
        """本接口(DescribeCrossRegionZone)根据主实例查询备机的容灾地域和可用区。

        :param request: Request instance for DescribeCrossRegionZone.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionZoneRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeCrossRegionZoneResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCrossRegionZone", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCrossRegionZoneResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBInstances(self, request):
        """本接口(DescribeDBInstances)用于查询实例列表。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBSecurityGroups(self, request):
        """本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDBs(self, request):
        """本接口（DescribeDBs）用于查询数据库列表。

        :param request: Request instance for DescribeDBs.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeDBsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowStatus(self, request):
        """本接口(DescribeFlowStatus)用于查询流程状态。

        :param request: Request instance for DescribeFlowStatus.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeFlowStatusResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowStatus", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowStatusResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMaintenanceSpan(self, request):
        """本接口（DescribeMaintenanceSpan）根据实例ID查询该实例的可维护时间窗。

        :param request: Request instance for DescribeMaintenanceSpan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMaintenanceSpanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMaintenanceSpanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMaintenanceSpan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMaintenanceSpanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrationDatabases(self, request):
        """本接口（DescribeMigrationDatabases）的作用是查询待迁移数据库列表

        :param request: Request instance for DescribeMigrationDatabases.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDatabasesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrationDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationDatabasesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrationDetail(self, request):
        """本接口（DescribeMigrationDetail）用于查询迁移任务的详细情况

        :param request: Request instance for DescribeMigrationDetail.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationDetailResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrationDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeMigrations(self, request):
        """本接口（DescribeMigrations）根据输入的限定条件，查询符合条件的迁移任务列表

        :param request: Request instance for DescribeMigrations.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeMigrationsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeMigrations", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeMigrationsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeOrders(self, request):
        """本接口（DescribeOrders）用于查询订单信息

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeOrdersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeOrders", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeOrdersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProductConfig(self, request):
        """本接口 (DescribeProductConfig) 用于查询售卖规格配置。

        :param request: Request instance for DescribeProductConfig.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProductConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductConfigResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProjectSecurityGroups(self, request):
        """本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeProjectSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjectSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribePublishSubscribe(self, request):
        """本接口（DescribePublishSubscribe）用于查询发布订阅关系列表。

        :param request: Request instance for DescribePublishSubscribe.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribePublishSubscribeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribePublishSubscribeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePublishSubscribe", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePublishSubscribeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReadOnlyGroupByReadOnlyInstance(self, request):
        """本接口（DescribeReadOnlyGroupByReadOnlyInstance）用于通过只读副本实例ID查询其所在的只读组。

        :param request: Request instance for DescribeReadOnlyGroupByReadOnlyInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupByReadOnlyInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupByReadOnlyInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReadOnlyGroupByReadOnlyInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReadOnlyGroupByReadOnlyInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReadOnlyGroupDetails(self, request):
        """本接口（DescribeReadOnlyGroupDetails）用于查询只读组详情。

        :param request: Request instance for DescribeReadOnlyGroupDetails.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReadOnlyGroupDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReadOnlyGroupDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeReadOnlyGroupList(self, request):
        """本接口（DescribeReadOnlyGroupList）用于查询只读组列表。

        :param request: Request instance for DescribeReadOnlyGroupList.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupListRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeReadOnlyGroupListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReadOnlyGroupList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReadOnlyGroupListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRegions(self, request):
        """本接口 (DescribeRegions) 用于查询售卖地域信息。

        :param request: Request instance for DescribeRegions.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRegionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRegions", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRegionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRollbackTime(self, request):
        """本接口（DescribeRollbackTime）用于查询实例可回档时间范围

        :param request: Request instance for DescribeRollbackTime.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeRollbackTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRollbackTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRollbackTimeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSlowlogs(self, request):
        """本接口（DescribeSlowlogs）用于获取慢查询日志文件信息

        :param request: Request instance for DescribeSlowlogs.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeSlowlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowlogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeZones(self, request):
        """本接口 (DescribeZones) 用于查询当前可售卖的可用区信息。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DescribeZonesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeZones", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeZonesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateSecurityGroups(self, request):
        """本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。

        :param request: Request instance for DisassociateSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.DisassociateSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateDBInstances(self, request):
        """本接口（InquiryPriceCreateDBInstances）用于查询申请实例价格。

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceCreateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateDBInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRenewDBInstance(self, request):
        """本接口（InquiryPriceRenewDBInstance）用于查询续费实例的价格。

        :param request: Request instance for InquiryPriceRenewDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceRenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceUpgradeDBInstance(self, request):
        """本接口（InquiryPriceUpgradeDBInstance）用于查询升级实例的价格。

        :param request: Request instance for InquiryPriceUpgradeDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.InquiryPriceUpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceUpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceUpgradeDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccountPrivilege(self, request):
        """本接口（ModifyAccountPrivilege）用于修改实例账户权限。

        :param request: Request instance for ModifyAccountPrivilege.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountPrivilegeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountPrivilege", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountPrivilegeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAccountRemark(self, request):
        """本接口（ModifyAccountRemark）用于修改账户备注。

        :param request: Request instance for ModifyAccountRemark.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyAccountRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountRemarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBackupName(self, request):
        """本接口(ModifyBackupName)用于修改备份名称。

        :param request: Request instance for ModifyBackupName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBackupStrategy(self, request):
        """本接口（ModifyBackupStrategy）用于修改备份策略

        :param request: Request instance for ModifyBackupStrategy.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupStrategyRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyBackupStrategyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupStrategy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupStrategyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceName(self, request):
        """本接口（ModifyDBInstanceName）用于修改实例名字。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceNetwork(self, request):
        """本接口（ModifyDBInstanceNetwork）用于修改运行中实例的网络，仅支持从VPC网络到VPC网络的转换

        :param request: Request instance for ModifyDBInstanceNetwork.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceNetworkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceNetwork", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceNetworkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceProject(self, request):
        """本接口（ModifyDBInstanceProject）用于修改数据库实例所属项目。

        :param request: Request instance for ModifyDBInstanceProject.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceProjectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceRenewFlag(self, request):
        """本接口（ModifyDBInstanceRenewFlag）用于修改实例续费标记

        :param request: Request instance for ModifyDBInstanceRenewFlag.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceRenewFlagRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceRenewFlagResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBName(self, request):
        """本接口（ModifyDBName）用于更新数据库名。

        :param request: Request instance for ModifyDBName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDBRemark(self, request):
        """本接口（ModifyDBRemark）用于修改数据库备注。

        :param request: Request instance for ModifyDBRemark.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyDBRemarkResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBRemark", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBRemarkResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMaintenanceSpan(self, request):
        """本接口（ModifyMaintenanceSpan）用于修改实例的可维护时间窗

        :param request: Request instance for ModifyMaintenanceSpan.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMaintenanceSpanRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMaintenanceSpanResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMaintenanceSpan", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMaintenanceSpanResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyMigration(self, request):
        """本接口（ModifyMigration）可以修改已有的迁移任务信息

        :param request: Request instance for ModifyMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyMigrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPublishSubscribeName(self, request):
        """本接口（ModifyPublishSubscribeName）修改发布订阅的名称。

        :param request: Request instance for ModifyPublishSubscribeName.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeNameRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyPublishSubscribeNameResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPublishSubscribeName", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPublishSubscribeNameResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyReadOnlyGroupDetails(self, request):
        """本接口（ModifyReadOnlyGroupDetails）用于修改只读组详情。

        :param request: Request instance for ModifyReadOnlyGroupDetails.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ModifyReadOnlyGroupDetailsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ModifyReadOnlyGroupDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyReadOnlyGroupDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyReadOnlyGroupDetailsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def QueryMigrationCheckProcess(self, request):
        """本接口（QueryMigrationCheckProcess）的作用是查询迁移检查任务的进度，适用于迁移源的类型为TencentDB for SQLServer 的迁移方式

        :param request: Request instance for QueryMigrationCheckProcess.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.QueryMigrationCheckProcessRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.QueryMigrationCheckProcessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("QueryMigrationCheckProcess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.QueryMigrationCheckProcessResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecycleDBInstance(self, request):
        """本接口（RecycleDBInstance）用于主动回收已下线的SQLSERVER实例

        :param request: Request instance for RecycleDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RecycleDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RecycleDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecycleDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecycleDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RecycleReadOnlyGroup(self, request):
        """本接口（RecycleReadOnlyGroup）立即回收只读组的资源，只读组占用的vip等资源将立即释放且不可找回。

        :param request: Request instance for RecycleReadOnlyGroup.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RecycleReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RecycleReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RecycleReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RecycleReadOnlyGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveBackups(self, request):
        """本接口（RemoveBackups）可以删除用户手动创建的备份文件。待删除的备份策略可以是实例备份，也可以是多库备份。

        :param request: Request instance for RemoveBackups.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RemoveBackupsRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RemoveBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveBackupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewDBInstance(self, request):
        """本接口（RenewDBInstance）用于续费实例。

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RenewDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewPostpaidDBInstance(self, request):
        """本接口（RenewPostpaidDBInstance）用于将通过接口TerminateDBInstance手动隔离的按量计费实例从回收站中恢复。

        :param request: Request instance for RenewPostpaidDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RenewPostpaidDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RenewPostpaidDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewPostpaidDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewPostpaidDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAccountPassword(self, request):
        """本接口（ResetAccountPassword）用于重置实例的账户密码。

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.ResetAccountPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAccountPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAccountPasswordResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestartDBInstance(self, request):
        """本接口（RestartDBInstance）用于重启数据库实例。

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestartDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RestoreInstance(self, request):
        """本接口（RestoreInstance）用于根据备份文件恢复实例。

        :param request: Request instance for RestoreInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RestoreInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestoreInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestoreInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RollbackInstance(self, request):
        """本接口（RollbackInstance）用于回档实例

        :param request: Request instance for RollbackInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RollbackInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RollbackInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RollbackInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RunMigration(self, request):
        """本接口（RunMigration）用于启动迁移任务，开始迁移

        :param request: Request instance for RunMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.RunMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RunMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RunMigrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StartMigrationCheck(self, request):
        """本接口（StartMigrationCheck）的作用是启动一个迁移前的校验任务，适用于迁移源的类型为TencentDB for SQLServer 的迁移方式

        :param request: Request instance for StartMigrationCheck.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StartMigrationCheckRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StartMigrationCheckResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StartMigrationCheck", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StartMigrationCheckResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def StopMigration(self, request):
        """本接口（StopMigration）作用是中止一个迁移任务

        :param request: Request instance for StopMigration.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.StopMigrationRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.StopMigrationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("StopMigration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.StopMigrationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TerminateDBInstance(self, request):
        """本接口(TerminateDBInstance)用于主动隔离实例，使得实例进入回收站。

        :param request: Request instance for TerminateDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.TerminateDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.TerminateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TerminateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TerminateDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UpgradeDBInstance(self, request):
        """本接口（UpgradeDBInstance）用于升级实例

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.sqlserver.v20180328.models.UpgradeDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)