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
from tencentcloud.postgres.v20170312 import models


class PostgresClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'postgres.tencentcloudapi.com'
    _service = 'postgres'


    def AddDBInstanceToReadOnlyGroup(self, request):
        """本接口（AddDBInstanceToReadOnlyGroup）用于添加只读实例到只读组

        :param request: Request instance for AddDBInstanceToReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.AddDBInstanceToReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.AddDBInstanceToReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddDBInstanceToReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.AddDBInstanceToReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneDBInstance(self, request):
        """用于克隆实例，支持指定备份集、指定时间点进行克隆。

        :param request: Request instance for CloneDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloneDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloneDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CloneDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseDBExtranetAccess(self, request):
        """本接口（CloseDBExtranetAccess）用于关闭实例公网地址。

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CloseDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseServerlessDBExtranetAccess(self, request):
        """本接口（CloseServerlessDBExtranetAccess）用于关闭serverlessDB实例公网地址

        :param request: Request instance for CloseServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloseServerlessDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CloseServerlessDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccount(self, request):
        """此接口用于创建数据账号，返回的Oid为账号唯一标识。与数据库系统表pg_roles中记录的oid一致。

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateAccountResponse`

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


    def CreateBaseBackup(self, request):
        """本接口（CreateBaseBackup）用于创建实例的数据备份。

        :param request: Request instance for CreateBaseBackup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateBaseBackupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateBaseBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBaseBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBaseBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstanceNetworkAccess(self, request):
        """本接口（CreateDBInstanceNetworkAccess）用于创建实例网络。

        :param request: Request instance for CreateDBInstanceNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstanceNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstanceNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstances(self, request):
        """本接口（CreateDBInstances）用于创建一个或者多个PostgreSQL实例,仅发货实例不会进行初始化。本接口已废弃，推荐使用接口[CreateInstances](https://cloud.tencent.com/document/api/409/56107)替代。

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesResponse`

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


    def CreateDatabase(self, request):
        """此接口用于创建数据库，需指定数据库名及所有者。

        :param request: Request instance for CreateDatabase.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDatabaseRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDatabaseResponse`

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


    def CreateInstances(self, request):
        """本接口 (CreateInstances) 用于创建一个或者多个PostgreSQL实例，通过此接口创建的实例无需进行初始化，可直接使用。
        <li>实例创建成功后将自动开机启动，实例状态变为“运行中”。</li>
        <li>预付费实例的购买会预先扣除本次实例购买所需金额，按小时后付费实例购买会预先冻结本次实例购买一小时内所需金额，在调用本接口前请确保账户余额充足。</li>

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateParameterTemplate(self, request):
        """本接口 (CreateParameterTemplate) 用于创建参数模板。

        :param request: Request instance for CreateParameterTemplate.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateParameterTemplateRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateParameterTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateParameterTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateParameterTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyDBInstance(self, request):
        """本接口(CreateReadOnlyDBInstance)用于创建只读实例

        :param request: Request instance for CreateReadOnlyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyGroup(self, request):
        """本接口（CreateReadOnlyGroup）用于创建只读组

        :param request: Request instance for CreateReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReadOnlyGroupNetworkAccess(self, request):
        """本接口（CreateReadOnlyGroupNetworkAccess）用于创建RO组的网络。

        :param request: Request instance for CreateReadOnlyGroupNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReadOnlyGroupNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReadOnlyGroupNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServerlessDBInstance(self, request):
        """本接口 (CreateServerlessDBInstance) 用于创建一个ServerlessDB实例，创建成功返回实例ID。

        :param request: Request instance for CreateServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServerlessDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServerlessDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccount(self, request):
        """此接口用于删除数据库账号，需要同时输入Oid与UserName，避免误删。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteAccountResponse`

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


    def DeleteBaseBackup(self, request):
        """本接口（DeleteBaseBackup）用于删除实例指定数据备份。

        :param request: Request instance for DeleteBaseBackup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteBaseBackupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteBaseBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBaseBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBaseBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBInstanceNetworkAccess(self, request):
        """可对实例进行网络的删除操作。

        :param request: Request instance for DeleteDBInstanceNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteDBInstanceNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteDBInstanceNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBInstanceNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBInstanceNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLogBackup(self, request):
        """本接口（DeleteLogBackup）用于删除实例指定日志备份。

        :param request: Request instance for DeleteLogBackup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteLogBackupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteLogBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLogBackup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLogBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteParameterTemplate(self, request):
        """本接口（DeleteParameterTemplate）主要用于删除某个参数模板。

        :param request: Request instance for DeleteParameterTemplate.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteParameterTemplateRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteParameterTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteParameterTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteParameterTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReadOnlyGroup(self, request):
        """本接口(DeleteReadOnlyGroup)用于删除指定的只读组

        :param request: Request instance for DeleteReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReadOnlyGroupNetworkAccess(self, request):
        """可对RO组进行网络的删除操作。

        :param request: Request instance for DeleteReadOnlyGroupNetworkAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupNetworkAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupNetworkAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReadOnlyGroupNetworkAccess", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReadOnlyGroupNetworkAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServerlessDBInstance(self, request):
        """本接口 (DeleteServerlessDBInstance) 用于删除一个ServerlessDB实例。

        :param request: Request instance for DeleteServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServerlessDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServerlessDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountPrivileges(self, request):
        """查询数据库账号对某数据库对象拥有的权限列表。

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccounts(self, request):
        """本接口（DescribeAccounts）用于查询实例的数据库账号列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsResponse`

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


    def DescribeAvailableRecoveryTime(self, request):
        """本接口（DescribeAvailableRecoveryTime）用于查询实例可恢复的时间范围。

        :param request: Request instance for DescribeAvailableRecoveryTime.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAvailableRecoveryTimeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAvailableRecoveryTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAvailableRecoveryTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAvailableRecoveryTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadRestriction(self, request):
        """本接口（DescribeBackupDownloadRestriction）用于查询备份文件下载限制。

        :param request: Request instance for DescribeBackupDownloadRestriction.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupDownloadURL(self, request):
        """本接口 (DescribeBackupDownloadURL) 用于查询指定备份集的下载地址，可包括全量备份集、增量日志备份集。

        :param request: Request instance for DescribeBackupDownloadURL.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadURLRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupDownloadURLResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupDownloadURL", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupDownloadURLResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupOverview(self, request):
        """本接口（DescribeBackupOverview）用于查询用户的备份概览信息。返回用户当前备份个数、备份占用容量、免费容量、收费容量等信息（容量单位为字节）。

        :param request: Request instance for DescribeBackupOverview.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupOverviewRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupOverviewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupOverview", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupOverviewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupPlans(self, request):
        """本接口 (DescribeBackupPlans) 用于实例所有的备份计划查询

        :param request: Request instance for DescribeBackupPlans.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupPlansRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupPlansResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupPlans", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupPlansResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBackupSummaries(self, request):
        """本接口(DescribeBackupSummaries)用于查询实例备份的统计信息，返回以实例为维度的备份个数、占用容量等信息（容量单位为字节）。

        :param request: Request instance for DescribeBackupSummaries.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupSummariesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBackupSummariesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupSummaries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupSummariesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBaseBackups(self, request):
        """本接口（DescribeBaseBackups）用于查询数据备份列表。

        :param request: Request instance for DescribeBaseBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeBaseBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeBaseBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBaseBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBaseBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClasses(self, request):
        """本接口（DescribeClasses）用于查询实例售卖规格。

        :param request: Request instance for DescribeClasses.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeClassesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeClassesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClasses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCloneDBInstanceSpec(self, request):
        """本接口（DescribeCloneDBInstanceSpec）用于查询克隆实例可选择的最小规格，包括SpecCode和磁盘。

        :param request: Request instance for DescribeCloneDBInstanceSpec.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeCloneDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeCloneDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCloneDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCloneDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBBackups(self, request):
        """本接口（DescribeDBBackups）用于查询实例备份列表。本接口已废弃，推荐使用接口[DescribeBaseBackups](https://cloud.tencent.com/document/api/409/89022)替代。

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBErrlogs(self, request):
        """本接口（DescribeDBErrlogs）用于查询错误日志。

        :param request: Request instance for DescribeDBErrlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBErrlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBErrlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceAttribute(self, request):
        """本接口 (DescribeDBInstanceAttribute) 用于查询某个实例的详情信息。

        :param request: Request instance for DescribeDBInstanceAttribute.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceHAConfig(self, request):
        """本接口（DescribeDBInstanceHAConfig）用于查询实例HA配置信息。其中HA配置信息包括：
        <li>允许备节点切换为主节点的条件配置
        <li>半同步实例使用同步复制或异步复制的条件配置

        :param request: Request instance for DescribeDBInstanceHAConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceHAConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceHAConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceHAConfig", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceHAConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceParameters(self, request):
        """本接口（DescribeDBInstanceAttribute）用于查询实例的参数信息。

        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceSecurityGroups(self, request):
        """本接口（DescribeDBInstanceSecurityGroups）用于查询实例安全组。

        :param request: Request instance for DescribeDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """本接口 (DescribeDBInstances) 用于查询一个或多个实例的详细信息。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBSlowlogs(self, request):
        """本接口（DescribeDBSlowlogs）用于获取慢查询日志。本接口已于2021.09.01日废弃，后续此接口将不再返回任何数据，推荐使用接口[DescribeSlowQueryList](https://cloud.tencent.com/document/api/409/60540)替代。

        :param request: Request instance for DescribeDBSlowlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSlowlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSlowlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBVersions(self, request):
        """本接口（DescribeDBVersions）用于查询支持的数据库版本。

        :param request: Request instance for DescribeDBVersions.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBVersionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBVersionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBVersions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBVersionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBXlogs(self, request):
        """本接口（DescribeDBXlogs）用于获取实例Xlog列表。本接口已废弃，推荐使用接口[DescribeLogBackups](https://cloud.tencent.com/document/api/409/89021)替代。

        :param request: Request instance for DescribeDBXlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBXlogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBXlogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseObjects(self, request):
        """本接口用于查询数据库对象列表。例如查询test数据库下的模式列表。

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabaseObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseObjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """接口（DescribeDatabases）用来查询实例的数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesResponse`

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


    def DescribeDedicatedClusters(self, request):
        """查询专属集群

        :param request: Request instance for DescribeDedicatedClusters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDedicatedClustersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDedicatedClustersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDedicatedClusters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDedicatedClustersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDefaultParameters(self, request):
        """本接口（DescribeDefaultParameters）主要用于查询某个数据库版本和引擎支持的所有参数。

        :param request: Request instance for DescribeDefaultParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDefaultParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDefaultParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDefaultParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDefaultParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeEncryptionKeys(self, request):
        """本接口 （DescribeEncryptionKeys） 用于查询实例的密钥信息列表。

        :param request: Request instance for DescribeEncryptionKeys.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeEncryptionKeysRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeEncryptionKeysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeEncryptionKeys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeEncryptionKeysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogBackups(self, request):
        """本接口（DescribeLogBackups）用于查询日志备份列表。

        :param request: Request instance for DescribeLogBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeLogBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeLogBackupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogBackups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogBackupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """本接口（DescribeOrders）用于查询订单信息。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersResponse`

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


    def DescribeParameterTemplateAttributes(self, request):
        """本接口（DescribeParameterTemplateAttributes）用于查询某个参数模板的具体内容，包括基本信息和参数信息。

        :param request: Request instance for DescribeParameterTemplateAttributes.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplateAttributesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplateAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParameterTemplateAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParameterTemplateAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParameterTemplates(self, request):
        """本接口 (DescribeParameterTemplates) 用于查询参数模板列表。

        :param request: Request instance for DescribeParameterTemplates.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplatesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParameterTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParameterTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParameterTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeParamsEvent(self, request):
        """本接口（DescribeParamsEvent）用于查询参数修改事件。

        :param request: Request instance for DescribeParamsEvent.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParamsEventRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParamsEventResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeParamsEvent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeParamsEventResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductConfig(self, request):
        """本接口（DescribeProductConfig）用于查询售卖规格配置。本接口已废弃，推荐使用新接口[DescribeClasses](https://cloud.tencent.com/document/api/409/89019)。

        :param request: Request instance for DescribeProductConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigResponse`

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


    def DescribeReadOnlyGroups(self, request):
        """本接口（DescribeReadOnlyGroups）用于查询只读组列表

        :param request: Request instance for DescribeReadOnlyGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReadOnlyGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReadOnlyGroupsResponse()
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
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsResponse`

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


    def DescribeServerlessDBInstances(self, request):
        """用于查询一个或多个serverlessDB实例的详细信息

        :param request: Request instance for DescribeServerlessDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServerlessDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServerlessDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryAnalysis(self, request):
        """此接口（DescribeSlowQueryAnalysis）用于统计指定时间范围内的所有慢查询，根据SQL语句抽象参数后，进行聚合分析，并返回同类SQL列表。

        :param request: Request instance for DescribeSlowQueryAnalysis.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryAnalysisRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryAnalysisResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryAnalysis", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryAnalysisResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSlowQueryList(self, request):
        """此接口（DescribeSlowQueryList）用于查询指定时间范围内的所有慢查询。

        :param request: Request instance for DescribeSlowQueryList.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryListRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowQueryList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowQueryListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeZones(self, request):
        """本接口 (DescribeZones) 用于查询支持的可用区信息。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesResponse`

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


    def DestroyDBInstance(self, request):
        """本接口 (DestroyDBInstance) 用于彻底销毁指定DBInstanceId对应的实例，销毁后实例数据将彻底删除，无法找回，调用前请仔细确认要操作的实例。只能销毁隔离中的实例。

        :param request: Request instance for DestroyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisIsolateDBInstances(self, request):
        """本接口（DisIsolateDBInstances）用于解隔离实例

        :param request: Request instance for DisIsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisIsolateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DisIsolateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitDBInstances(self, request):
        """本接口（InitDBInstances）用于初始化云数据库PostgreSQL实例。本接口已废弃，推荐使用接口[CreateInstances](https://cloud.tencent.com/document/api/409/56107)替代。

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InitDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateDBInstances(self, request):
        """本接口 (InquiryPriceCreateDBInstances) 用于查询购买实例的价格信息。

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesResponse`

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
        """本接口（InquiryPriceRenewDBInstance）用于查询续费实例的价格。

        :param request: Request instance for InquiryPriceRenewDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceResponse`

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
        """本接口（InquiryPriceUpgradeDBInstance）用于查询升级实例的价格。只支持按量计费实例。

        :param request: Request instance for InquiryPriceUpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceResponse`

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


    def IsolateDBInstances(self, request):
        """本接口（IsolateDBInstances）用于隔离实例。

        :param request: Request instance for IsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockAccount(self, request):
        """此接口用于锁定数据库账号，锁定后账号当前连接会断开，并且无法建立新连接。

        :param request: Request instance for LockAccount.
        :type request: :class:`tencentcloud.postgres.v20170312.models.LockAccountRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.LockAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockAccount", params, headers=headers)
            response = json.loads(body)
            model = models.LockAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """修改某账号对某数据库对象的权限、修改账号类型。

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountRemark(self, request):
        """本接口（ModifyAccountRemark）用于修改账号备注。

        :param request: Request instance for ModifyAccountRemark.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkResponse`

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


    def ModifyBackupDownloadRestriction(self, request):
        """本接口（ModifyBackupDownloadRestriction）用于修改备份文件下载限制。

        :param request: Request instance for ModifyBackupDownloadRestriction.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupDownloadRestrictionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupDownloadRestrictionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupDownloadRestriction", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupDownloadRestrictionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBackupPlan(self, request):
        """本接口 (ModifyBackupPlan) 用于实例备份计划的修改，默认是在每天的凌晨开始全量备份，备份保留时长是7天。可以根据此接口指定时间进行实例的备份。

        :param request: Request instance for ModifyBackupPlan.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupPlanRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyBackupPlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupPlan", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupPlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBaseBackupExpireTime(self, request):
        """本接口（ModifyBaseBackupExpireTime）用于修改实例指定数据备份的过期时间。

        :param request: Request instance for ModifyBaseBackupExpireTime.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyBaseBackupExpireTimeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyBaseBackupExpireTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBaseBackupExpireTime", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBaseBackupExpireTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceChargeType(self, request):
        """支持实例的计费类型转换（目前仅支持按量计费转包年包月）

        :param request: Request instance for ModifyDBInstanceChargeType.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceChargeTypeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceChargeTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceChargeType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceChargeTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceDeployment(self, request):
        """本接口（ModifyDBInstanceDeployment）用于修改节点可用区部署方式，仅支持主实例。

        :param request: Request instance for ModifyDBInstanceDeployment.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceDeploymentRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceDeploymentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceDeployment", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceDeploymentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceHAConfig(self, request):
        """本接口（ModifyDBInstanceHAConfig）用于修改实例HA配置信息。其中HA配置信息包括：
        <li>允许备节点切换为主节点的条件配置
        <li>半同步实例使用同步复制或异步复制的条件配置

        :param request: Request instance for ModifyDBInstanceHAConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceHAConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceHAConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceHAConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceHAConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceName(self, request):
        """本接口（ModifyDBInstanceName）用于修改postgresql实例名字。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstanceParameters(self, request):
        """本接口 (ModifyDBInstanceParameters) 用于修改实例参数。

        :param request: Request instance for ModifyDBInstanceParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceParameters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceReadOnlyGroup(self, request):
        """本接口（ModifyDBInstanceReadOnlyGroup）用于修改实例所属的只读组

        :param request: Request instance for ModifyDBInstanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口（ModifyDBInstanceSecurityGroups）用于修改实例安全组。

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBInstanceSpec(self, request):
        """本接口（ModifyDBInstanceSpec）用于修改实例规格，包括内存、磁盘。

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceSpec", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstancesProject(self, request):
        """本接口（ModifyDBInstancesProject）用于修改实例所属项目。

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstancesProject", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstancesProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDatabaseOwner(self, request):
        """修改数据库所有者

        :param request: Request instance for ModifyDatabaseOwner.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDatabaseOwnerRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDatabaseOwnerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDatabaseOwner", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDatabaseOwnerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyParameterTemplate(self, request):
        """本接口（ModifyParameterTemplate）主要用于修改参数模板名称，描述等配置，也可用于管理参数模板中的参数列表。

        :param request: Request instance for ModifyParameterTemplate.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyParameterTemplateRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyParameterTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyParameterTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyParameterTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReadOnlyGroupConfig(self, request):
        """本接口(ModifyReadOnlyGroupConfig)用于更新只读组配置信息

        :param request: Request instance for ModifyReadOnlyGroupConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReadOnlyGroupConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReadOnlyGroupConfigResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySwitchTimePeriod(self, request):
        """当升级完成后，对处于等待切换状态下的实例，强制实例立即切换。

        :param request: Request instance for ModifySwitchTimePeriod.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifySwitchTimePeriodRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifySwitchTimePeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySwitchTimePeriod", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySwitchTimePeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBExtranetAccess(self, request):
        """本接口（OpenDBExtranetAccess）用于开通实例公网地址。

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenServerlessDBExtranetAccess(self, request):
        """本接口（OpenServerlessDBExtranetAccess）用于开通serverlessDB实例公网地址。

        :param request: Request instance for OpenServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("OpenServerlessDBExtranetAccess", params, headers=headers)
            response = json.loads(body)
            model = models.OpenServerlessDBExtranetAccessResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RebalanceReadOnlyGroup(self, request):
        """本接口(RebalanceReadOnlyGroup)用于重新均衡 RO 组内实例的负载。注意，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库，谨慎操作。

        :param request: Request instance for RebalanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RebalanceReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RebalanceReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveDBInstanceFromReadOnlyGroup(self, request):
        """本接口（RemoveDBInstanceFromReadOnlyGroup）用户将只读实例从只读组中移除

        :param request: Request instance for RemoveDBInstanceFromReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveDBInstanceFromReadOnlyGroup", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveDBInstanceFromReadOnlyGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewInstance(self, request):
        """本接口（RenewInstance）用于续费实例。

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAccountPassword(self, request):
        """本接口（ResetAccountPassword）用于重置实例的账户密码。

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordResponse`

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
        """本接口（RestartDBInstance）用于重启实例。

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceResponse`

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


    def RestoreDBInstanceObjects(self, request):
        """根据备份集或恢复目标时间，在原实例上恢复数据库相关对象，例如数据库、表。

        :param request: Request instance for RestoreDBInstanceObjects.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RestoreDBInstanceObjectsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RestoreDBInstanceObjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestoreDBInstanceObjects", params, headers=headers)
            response = json.loads(body)
            model = models.RestoreDBInstanceObjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAutoRenewFlag(self, request):
        """本接口（SetAutoRenewFlag）用于设置自动续费。

        :param request: Request instance for SetAutoRenewFlag.
        :type request: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.SetAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDBInstancePrimary(self, request):
        """本接口（SwitchDBInstancePrimary）用于切换实例主备关系。
        <li>通过主动发起切换，可以验证业务能否正确处理实例主备切换的场景
        <li>通过使用强制切换，可以在备节点延迟不满足切换条件时，强制发起主从切换
        <li>只有主实例可以执行该操作

        :param request: Request instance for SwitchDBInstancePrimary.
        :type request: :class:`tencentcloud.postgres.v20170312.models.SwitchDBInstancePrimaryRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SwitchDBInstancePrimaryResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstancePrimary", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDBInstancePrimaryResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnlockAccount(self, request):
        """解除数据库账号的锁定，解锁后账号可以登陆数据库。

        :param request: Request instance for UnlockAccount.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UnlockAccountRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UnlockAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockAccount", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """本接口（UpgradeDBInstance）用于升级实例配置。本接口已废弃，推荐使用接口[ModifyDBInstanceSpec](https://cloud.tencent.com/document/api/409/63689)替代。

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceResponse`

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


    def UpgradeDBInstanceKernelVersion(self, request):
        """本接口（UpgradeDBInstanceKernelVersion）用于升级实例的内核版本号。

        :param request: Request instance for UpgradeDBInstanceKernelVersion.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceKernelVersionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceKernelVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceKernelVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceKernelVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstanceMajorVersion(self, request):
        """本接口（UpgradeDBInstanceMajorVersion）用于升级实例内核大版本，例如从PostgreSQL 12升级到PostgreSQL 15。

        :param request: Request instance for UpgradeDBInstanceMajorVersion.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceMajorVersionRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceMajorVersionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceMajorVersion", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceMajorVersionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))