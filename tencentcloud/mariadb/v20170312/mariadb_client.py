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
from tencentcloud.mariadb.v20170312 import models


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.tencentcloudapi.com'
    _service = 'mariadb'


    def ActivateHourDBInstance(self, request):
        """解隔离MariaDB按量计费实例

        :param request: Request instance for ActivateHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ActivateHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ActivateHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActivateHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ActivateHourDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateSecurityGroups(self, request):
        """本接口 (AssociateSecurityGroups) 用于安全组批量绑定云资源。

        :param request: Request instance for AssociateSecurityGroups.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.AssociateSecurityGroupsResponse`

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


    def CancelDcnJob(self, request):
        """本接口（CancelDcnJob）用于取消DCN同步

        :param request: Request instance for CancelDcnJob.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CancelDcnJobRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CancelDcnJobResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelDcnJob", params, headers=headers)
            response = json.loads(body)
            model = models.CancelDcnJobResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneAccount(self, request):
        """本接口（CloneAccount）用于克隆实例账户。

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneAccount", params, headers=headers)
            response = json.loads(body)
            model = models.CloneAccountResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloseDBExtranetAccess(self, request):
        """本接口(CloseDBExtranetAccess)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问，查询实例列表接口将不返回对应实例的外网域名和端口信息。

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessResponse`

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


    def CopyAccountPrivileges(self, request):
        """本接口（CopyAccountPrivileges）用于复制云数据库账号的权限。
        注意：相同用户名，不同Host是不同的账号，Readonly属性相同的账号之间才能复制权限。

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CopyAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.CopyAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAccount(self, request):
        """本接口（CreateAccount）用于创建云数据库账号。一个实例可以创建多个不同的账号，相同的用户名+不同的host是不同的账号。

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountResponse`

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


    def CreateDBInstance(self, request):
        """本接口（CreateDBInstance）用于创建包年包月的MariaDB云数据库实例，可通过传入实例规格、数据库版本号、购买时长和数量等信息创建云数据库实例。

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDedicatedClusterDBInstance(self, request):
        """创建Mariadb独享集群实例

        :param request: Request instance for CreateDedicatedClusterDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateDedicatedClusterDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateDedicatedClusterDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHourDBInstance(self, request):
        """创建MariaDB按量计费实例

        :param request: Request instance for CreateHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHourDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTmpInstances(self, request):
        """本接口（CreateTmpInstances）用于创建临时实例。

        :param request: Request instance for CreateTmpInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateTmpInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateTmpInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTmpInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTmpInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAccount(self, request):
        """本接口（DeleteAccount）用于删除云数据库账号。用户名+host唯一确定一个账号。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountResponse`

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


    def DescribeAccountPrivileges(self, request):
        """本接口（DescribeAccountPrivileges）用于查询云数据库账号权限。
        注意：注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesResponse`

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
        """本接口（DescribeAccounts）用于查询指定云数据库实例的账号列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsResponse`

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


    def DescribeBackupFiles(self, request):
        """本接口(DescribeBackupFiles)用于查看备份文件列表。

        :param request: Request instance for DescribeBackupFiles.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupFilesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupFilesResponse`

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


    def DescribeBackupTime(self, request):
        """本接口（DescribeBackupTime）用于获取云数据库的备份时间。后台系统将根据此配置定期进行实例备份。

        :param request: Request instance for DescribeBackupTime.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupTimeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBackupTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBackupTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBEncryptAttributes(self, request):
        """本接口(DescribeDBEncryptAttributes)用于查询实例数据加密状态。

        :param request: Request instance for DescribeDBEncryptAttributes.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBEncryptAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBEncryptAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBEncryptAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceDetail(self, request):
        """本接口(DescribeDBInstanceDetail)用于查询指定实例的详细信息。

        :param request: Request instance for DescribeDBInstanceDetail.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceDetailRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceSpecs(self, request):
        """本接口(DescribeDBInstanceSpecs)用于查询可创建的云数据库可售卖的规格配置。

        :param request: Request instance for DescribeDBInstanceSpecs.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceSpecsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBInstanceSpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBInstanceSpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回20条实例记录，单次请求最多支持返回100条实例记录。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBLogFiles(self, request):
        """本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBLogFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBLogFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBParameters(self, request):
        """本接口(DescribeDBParameters)用于获取数据库的当前参数设置。

        :param request: Request instance for DescribeDBParameters.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBParameters", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        """本接口（DescribeDBSecurityGroups）用于查询实例安全组信息

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeDBSlowLogs(self, request):
        """本接口(DescribeDBSlowLogs)用于查询慢查询日志列表。

        :param request: Request instance for DescribeDBSlowLogs.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBTmpInstances(self, request):
        """本接口（DescribeDBTmpInstances）用于获取实例回档生成的临时实例

        :param request: Request instance for DescribeDBTmpInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBTmpInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBTmpInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBTmpInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBTmpInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabaseObjects(self, request):
        """本接口（DescribeDatabaseObjects）用于查询云数据库实例的数据库中的对象列表，包含表、存储过程、视图和函数。

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseObjectsResponse`

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


    def DescribeDatabaseTable(self, request):
        """本接口（DescribeDatabaseTable）用于查询云数据库实例的表信息。

        :param request: Request instance for DescribeDatabaseTable.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabaseTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDatabaseTable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDatabaseTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDatabases(self, request):
        """本接口（DescribeDatabases）用于查询云数据库实例的数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesResponse`

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


    def DescribeDcnDetail(self, request):
        """获取实例灾备详情

        :param request: Request instance for DescribeDcnDetail.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDcnDetailRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDcnDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDcnDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDcnDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFileDownloadUrl(self, request):
        """本接口(DescribeFileDownloadUrl)用于获取数据库指定备份或日志文件的下载连接。

        :param request: Request instance for DescribeFileDownloadUrl.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeFileDownloadUrlRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeFileDownloadUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFileDownloadUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFileDownloadUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlow(self, request):
        """本接口（DescribeFlow）用于查询流程状态。

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeInstanceNodeInfo(self, request):
        """本接口（DescribeInstanceNodeInfo）用于获取数据库实例主备节点信息

        :param request: Request instance for DescribeInstanceNodeInfo.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLogFileRetentionPeriod(self, request):
        """本接口(DescribeLogFileRetentionPeriod)用于查看数据库备份日志的备份天数的设置情况。

        :param request: Request instance for DescribeLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLogFileRetentionPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLogFileRetentionPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeOrders(self, request):
        """本接口（DescribeOrders）用于查询云数据库订单信息。传入订单ID来查询订单关联的云数据库实例，和对应的任务流程ID。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeOrdersResponse`

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


    def DescribePrice(self, request):
        """本接口（DescribePrice）用于在购买实例前，查询实例的价格。

        :param request: Request instance for DescribePrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribePriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribePriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProjectSecurityGroups(self, request):
        """本接口（DescribeProjectSecurityGroups）用于查询项目安全组信息

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribeRenewalPrice(self, request):
        """本接口（DescribeRenewalPrice）用于在续费云数据库实例时，查询续费的价格。

        :param request: Request instance for DescribeRenewalPrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeRenewalPriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRenewalPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRenewalPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSaleInfo(self, request):
        """本接口(DescribeSaleInfo)用于查询云数据库可售卖的地域和可用区信息。

        :param request: Request instance for DescribeSaleInfo.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeSaleInfoRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeSaleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSaleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSaleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUpgradePrice(self, request):
        """本接口（DescribeUpgradePrice）用于在扩容云数据库实例时，查询变配的价格。

        :param request: Request instance for DescribeUpgradePrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeUpgradePriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUpgradePrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUpgradePriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyDBInstance(self, request):
        """本接口(DestroyDBInstance)用于销毁已隔离的包年包月实例。

        :param request: Request instance for DestroyDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DestroyDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DestroyDBInstanceResponse`

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


    def DestroyHourDBInstance(self, request):
        """本接口（DestroyHourDBInstance）用于销毁MariaDB按量计费实例。

        :param request: Request instance for DestroyHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DestroyHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DestroyHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyHourDBInstanceResponse()
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
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DisassociateSecurityGroupsResponse`

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


    def FlushBinlog(self, request):
        """相当于在mysqld中执行flush logs，完成切分的binlog将展示在实例控制台binlog列表里。

        :param request: Request instance for FlushBinlog.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.FlushBinlogRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.FlushBinlogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("FlushBinlog", params, headers=headers)
            response = json.loads(body)
            model = models.FlushBinlogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GrantAccountPrivileges(self, request):
        """本接口（GrantAccountPrivileges）用于给云数据库账号赋权。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GrantAccountPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.GrantAccountPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InitDBInstances(self, request):
        """本接口(InitDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.InitDBInstancesResponse`

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


    def IsolateDBInstance(self, request):
        """本接口(IsolateDBInstance)用于隔离云数据库MariaDB实例（包年包月），隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.IsolateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDedicatedDBInstance(self, request):
        """本接口（IsolateDedicatedDBInstance）用于隔离独享云数据库实例。

        :param request: Request instance for IsolateDedicatedDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.IsolateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.IsolateDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDedicatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateHourDBInstance(self, request):
        """隔离MariaDB按量计费实例

        :param request: Request instance for IsolateHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.IsolateHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.IsolateHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateHourDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def KillSession(self, request):
        """本接口（KillSession）用于杀死指定会话。

        :param request: Request instance for KillSession.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.KillSessionRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.KillSessionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("KillSession", params, headers=headers)
            response = json.loads(body)
            model = models.KillSessionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountDescription(self, request):
        """本接口（ModifyAccountDescription）用于修改云数据库账号备注。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountDescription", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountDescriptionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAccountPrivileges(self, request):
        """本接口(ModifyAccountPrivileges)用于修改云数据库的账户的权限信息。

        **注意**
        - 系统保留库："mysql"，只开放["SELECT"]权限
        - 只读账号授予读写权限会报错
        - 不传权限参数表示保留现有权限，如需清除，请在复杂类型Privileges字段传空数组

        :param request: Request instance for ModifyAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountPrivilegesResponse`

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


    def ModifyBackupTime(self, request):
        """本接口（ModifyBackupTime）用于设置云数据库实例的备份时间。后台系统将根据此配置定期进行实例备份。

        :param request: Request instance for ModifyBackupTime.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyBackupTimeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyBackupTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBackupTime", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBackupTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBEncryptAttributes(self, request):
        """本接口(ModifyDBEncryptAttributes)用于修改实例数据加密。

        :param request: Request instance for ModifyDBEncryptAttributes.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBEncryptAttributesResponse`

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
        """本接口（ModifyDBInstanceName）用于修改云数据库实例的名称。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstanceSecurityGroups(self, request):
        """本接口（ModifyDBInstanceSecurityGroups）用于修改云数据库安全组

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBInstancesProject(self, request):
        """本接口（ModifyDBInstancesProject）用于修改云数据库实例所属项目。

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectResponse`

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


    def ModifyDBParameters(self, request):
        """本接口(ModifyDBParameters)用于修改数据库参数。

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBParameters", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBParametersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBSyncMode(self, request):
        """本接口（ModifyDBSyncMode）用于修改云数据库实例的同步模式。

        :param request: Request instance for ModifyDBSyncMode.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBSyncMode", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBSyncModeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceNetwork(self, request):
        """本接口（ModifyInstanceNetwork）用于修改实例所属网络

        :param request: Request instance for ModifyInstanceNetwork.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceNetworkResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceNetwork", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNetworkResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceVip(self, request):
        """本接口（ModifyInstanceVip）用于修改实例VIP

        :param request: Request instance for ModifyInstanceVip.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVipRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceVip", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceVport(self, request):
        """本接口（ModifyInstanceVport）用于修改实例VPORT

        :param request: Request instance for ModifyInstanceVport.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVportRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyInstanceVportResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceVport", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceVportResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLogFileRetentionPeriod(self, request):
        """本接口(ModifyLogFileRetentionPeriod)用于修改数据库备份日志保存天数。

        :param request: Request instance for ModifyLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLogFileRetentionPeriod", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLogFileRetentionPeriodResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRealServerAccessStrategy(self, request):
        """本接口(ModifyRealServerAccessStrategy)用于修改云数据库的VPCGW到RS的访问策略。

        **注意**
        - 修改策略后只对新建立的连接生效，老连接不受影响
        - 就近访问只针对实例是跨可用区部署有用，单可用区部署实例就近与否并无作用
        - DB每个Node对应一个proxy，如果开启就近访问，将会把连接集中到对应可用区的proxy上，可能造成热点问题，这种情况下如果是线上业务，请务必根据自己的业务请求量测试符合预期后再进行就近策略变更

        :param request: Request instance for ModifyRealServerAccessStrategy.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyRealServerAccessStrategyRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyRealServerAccessStrategyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRealServerAccessStrategy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRealServerAccessStrategyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySyncTaskAttribute(self, request):
        """本接口 (ModifySyncTaskAttribute) 用于修改同步任务的属性（目前只支持修改任务名称）

        :param request: Request instance for ModifySyncTaskAttribute.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifySyncTaskAttributeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifySyncTaskAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySyncTaskAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySyncTaskAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def OpenDBExtranetAccess(self, request):
        """本接口（OpenDBExtranetAccess）用于开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例，可使用查询实例列表接口获取外网域名和端口信息。

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.OpenDBExtranetAccessResponse`

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


    def RenewDBInstance(self, request):
        """本接口（RenewDBInstance）用于续费云数据库实例。

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.RenewDBInstanceResponse`

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


    def ResetAccountPassword(self, request):
        """本接口（ResetAccountPassword）用于重置云数据库账号的密码。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordResponse`

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


    def RestartDBInstances(self, request):
        """本接口（RestartDBInstances）用于重启数据库实例

        :param request: Request instance for RestartDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.RestartDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.RestartDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RestartDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RestartDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SwitchDBInstanceHA(self, request):
        """本接口（SwitchDBInstanceHA）用于发起实例主备切换。

        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.SwitchDBInstanceHARequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.SwitchDBInstanceHAResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SwitchDBInstanceHA", params, headers=headers)
            response = json.loads(body)
            model = models.SwitchDBInstanceHAResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDedicatedDBInstance(self, request):
        """本接口（TerminateDedicatedDBInstance）用于销毁已隔离的独享云数据库实例。

        :param request: Request instance for TerminateDedicatedDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.TerminateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.TerminateDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDedicatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """本接口(UpgradeDBInstance)用于扩容云数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDBInstanceResponse`

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


    def UpgradeDedicatedDBInstance(self, request):
        """本接口(UpgradeDedicatedDBInstance)用于扩容独享云数据库实例。

        :param request: Request instance for UpgradeDedicatedDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDedicatedDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDedicatedDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDedicatedDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeHourDBInstance(self, request):
        """升级MariaDB按量计费实例

        :param request: Request instance for UpgradeHourDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.UpgradeHourDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.UpgradeHourDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeHourDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeHourDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))