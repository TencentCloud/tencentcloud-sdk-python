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
from tencentcloud.tdmysql.v20211122 import models


class TdmysqlClient(AbstractClient):
    _apiVersion = '2021-11-22'
    _endpoint = 'tdmysql.tencentcloudapi.com'
    _service = 'tdmysql'


    def CancelIsolateDBInstances(self, request):
        r"""本接口（CancelIsolateDBInstances）提供批量解除隔离实例功能

        :param request: Request instance for CancelIsolateDBInstances.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.CancelIsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.CancelIsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CancelIsolateDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.CancelIsolateDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCloneInstance(self, request):
        r"""本接口（CreateCloneInstance）提供创建克隆实例功能

        :param request: Request instance for CreateCloneInstance.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.CreateCloneInstanceRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.CreateCloneInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCloneInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCloneInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstances(self, request):
        r"""本接口（CreateDBInstances）提供批量创建实例功能

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.CreateDBInstancesResponse`

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


    def CreateDBSBackup(self, request):
        r"""创建实例手工备份  CreateDBSBackup

        :param request: Request instance for CreateDBSBackup.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.CreateDBSBackupRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.CreateDBSBackupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBSBackup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBSBackupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateUsers(self, request):
        r"""本接口（CreateUsers）用于批量创建用户

        :param request: Request instance for CreateUsers.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.CreateUsersRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.CreateUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateUsers", params, headers=headers)
            response = json.loads(body)
            model = models.CreateUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDBSBackupSets(self, request):
        r"""删除实例手工备份 DeleteDBSBackupSets

        :param request: Request instance for DeleteDBSBackupSets.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DeleteDBSBackupSetsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DeleteDBSBackupSetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDBSBackupSets", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDBSBackupSetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteUsers(self, request):
        r"""本接口（DeleteUsers）用于批量删除用户

        :param request: Request instance for DeleteUsers.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DeleteUsersRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DeleteUsersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteUsers", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteUsersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstanceDetail(self, request):
        r"""本接口（DescribeDBInstanceDetail）提供查询实例详情功能

        :param request: Request instance for DescribeDBInstanceDetail.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBInstanceDetailRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBInstanceDetailResponse`

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


    def DescribeDBInstances(self, request):
        r"""本接口（DescribeDBInstances）提供查询实例列表功能

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBInstancesResponse`

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


    def DescribeDBParameters(self, request):
        r"""本接口（DescribeDBParameters）用于获取实例的当前参数设置。

        :param request: Request instance for DescribeDBParameters.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBParametersResponse`

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


    def DescribeDBSArchiveLogs(self, request):
        r"""查询实例归档日志列表 DescribeDBSArchiveLogs

        :param request: Request instance for DescribeDBSArchiveLogs.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSArchiveLogsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSArchiveLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSArchiveLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSArchiveLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSAvailableRecoveryTime(self, request):
        r"""获取可恢复时间 DescribeDBSAvailableRecoveryTime

        :param request: Request instance for DescribeDBSAvailableRecoveryTime.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSAvailableRecoveryTimeRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSAvailableRecoveryTimeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSAvailableRecoveryTime", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSAvailableRecoveryTimeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSBackupPolicy(self, request):
        r"""查询实例备份策略 DescribeDBSBackupPolicy

        :param request: Request instance for DescribeDBSBackupPolicy.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupPolicyRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSBackupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSBackupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSBackupSets(self, request):
        r"""查询实例备份集信息 DescribeDBSBackupSets

        :param request: Request instance for DescribeDBSBackupSets.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupSetsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupSetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSBackupSets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSBackupSetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSBackupStatistics(self, request):
        r"""查询实例备份空间概览 DescribeDBSBackupStatistics

        :param request: Request instance for DescribeDBSBackupStatistics.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupStatisticsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSBackupStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSBackupStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSBackupStatisticsDetail(self, request):
        r"""查询备份集统计详情 DescribeDBSBackupStatisticsDetail

        :param request: Request instance for DescribeDBSBackupStatisticsDetail.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupStatisticsDetailRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSBackupStatisticsDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSBackupStatisticsDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSBackupStatisticsDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSCloneInstances(self, request):
        r"""查询实例克隆列表 DescribeDBSCloneInstances

        :param request: Request instance for DescribeDBSCloneInstances.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSCloneInstancesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSCloneInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSCloneInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSCloneInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBSecurityGroups(self, request):
        r"""本接口（DescribeDBSecurityGroups）用于查询实例安全组信息

        :param request: Request instance for DescribeDBSecurityGroups.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDBSecurityGroupsResponse`

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


    def DescribeDatabaseObjects(self, request):
        r"""本接口（DescribeDatabaseObjects）用于查询云数据库实例的数据库中的对象列表，包含表、存储过程、视图和函数。

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDatabaseObjectsResponse`

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
        r"""本接口（DescribeDatabases）用于查询云数据库实例的数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDatabasesResponse`

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


    def DescribeFlow(self, request):
        r"""本接口（DescribeFlow）用于查询异步任务流程状态

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeFlowResponse`

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


    def DescribeInstanceSSLStatus(self, request):
        r"""本接口（DescribeInstanceSSLStatus）提供实例SSL状态查询

        :param request: Request instance for DescribeInstanceSSLStatus.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeInstanceSSLStatusRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeInstanceSSLStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeInstanceSSLStatus", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeInstanceSSLStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeMaintenanceWindow(self, request):
        r"""查询维护时间窗口配置

        :param request: Request instance for DescribeMaintenanceWindow.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSaleInfo(self, request):
        r"""本接口（DescribeSaleInfo）提供查询可用售卖地域功能

        :param request: Request instance for DescribeSaleInfo.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeSaleInfoRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeSaleInfoResponse`

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


    def DescribeSlowLogs(self, request):
        r"""本接口提供查询慢日志功能

        :param request: Request instance for DescribeSlowLogs.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeSlowLogsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeSlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecs(self, request):
        r"""本接口（DescribeSpecs）提供查询售卖规格功能

        :param request: Request instance for DescribeSpecs.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeSpecsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeSpecsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserPrivileges(self, request):
        r"""本接口（DescribeUserPrivileges）提供查询用户的权限功能

        :param request: Request instance for DescribeUserPrivileges.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeUserPrivilegesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeUserPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsers(self, request):
        r"""本接口（DescribeUsers）提供查询用户列表功能

        :param request: Request instance for DescribeUsers.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeUsersRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeUsersResponse`

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


    def DestroyInstances(self, request):
        r"""本接口（DestroyInstances）提供批量销毁实例功能

        :param request: Request instance for DestroyInstances.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DestroyInstancesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DestroyInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ExpandInstance(self, request):
        r"""本接口（ExpandInstance）提供横向扩容实例功能

        :param request: Request instance for ExpandInstance.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ExpandInstanceRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ExpandInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ExpandInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ExpandInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDBInstance(self, request):
        r"""本接口（IsolateDBInstance）提供批量隔离实例功能

        :param request: Request instance for IsolateDBInstance.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.IsolateDBInstanceRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.IsolateDBInstanceResponse`

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


    def ModifyAutoRenewFlag(self, request):
        r"""本接口（ModifyAutoRenewFlag）用于修改自动续费标志

        :param request: Request instance for ModifyAutoRenewFlag.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAutoRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAutoRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBInstanceSecurityGroups(self, request):
        r"""本接口（ModifyDBInstanceSecurityGroups）用于修改云数据库安全组

        :param request: Request instance for ModifyDBInstanceSecurityGroups.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBInstanceSecurityGroupsResponse`

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


    def ModifyDBInstanceVPort(self, request):
        r"""本接口(ModifyDBInstanceVPort)修改实例VPC端口

        :param request: Request instance for ModifyDBInstanceVPort.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBInstanceVPortRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBInstanceVPortResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBInstanceVPort", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBInstanceVPortResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBParameters(self, request):
        r"""本接口（ModifyDBParameters）用于修改实例参数。

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBParametersResponse`

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


    def ModifyDBSBackupPolicy(self, request):
        r"""修改实例备份策略 ModifyDBSBackupPolicy

        :param request: Request instance for ModifyDBSBackupPolicy.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBSBackupPolicyRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBSBackupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBSBackupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBSBackupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDBSBackupSetComment(self, request):
        r"""修改实例备份备注 ModifyDBSBackupSetComment

        :param request: Request instance for ModifyDBSBackupSetComment.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBSBackupSetCommentRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyDBSBackupSetCommentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDBSBackupSetComment", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDBSBackupSetCommentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceName(self, request):
        r"""本接口（ModifyInstanceName）提供修改实例名称功能

        :param request: Request instance for ModifyInstanceName.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyInstanceNameRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyInstanceNameResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceName", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceNameResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyInstanceNetwork(self, request):
        r"""本接口（ModifyInstanceNetwork）用于修改实例所属网络

        :param request: Request instance for ModifyInstanceNetwork.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyInstanceNetworkResponse`

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


    def ModifyInstanceSSLStatus(self, request):
        r"""本接口（ModifyInstanceSSLStatus）提供开关实例SSL的功能

        :param request: Request instance for ModifyInstanceSSLStatus.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyInstanceSSLStatusRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyInstanceSSLStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyInstanceSSLStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyInstanceSSLStatusResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyMaintenanceWindow(self, request):
        r"""新增/修改实例维护时间窗口配置

        :param request: Request instance for ModifyMaintenanceWindow.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyMaintenanceWindowRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyMaintenanceWindowResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyMaintenanceWindow", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyMaintenanceWindowResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyUserPrivileges(self, request):
        r"""本接口(ModifyPrivileges)修改用户权限

        :param request: Request instance for ModifyUserPrivileges.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyUserPrivilegesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyUserPrivilegesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyUserPrivileges", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyUserPrivilegesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetUserPassword(self, request):
        r"""本接口（ResetUserPassword）提供重置用户密码功能

        :param request: Request instance for ResetUserPassword.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ResetUserPasswordRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ResetUserPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetUserPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetUserPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetUsersPassword(self, request):
        r"""本接口（ResetUsersPassword）用于批量重置用户密码

        :param request: Request instance for ResetUsersPassword.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ResetUsersPasswordRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ResetUsersPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetUsersPassword", params, headers=headers)
            response = json.loads(body)
            model = models.ResetUsersPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RestartDBInstances(self, request):
        r"""本接口（RestartDBInstances）用于重启数据库实例

        :param request: Request instance for RestartDBInstances.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.RestartDBInstancesRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.RestartDBInstancesResponse`

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


    def UpgradeInstance(self, request):
        r"""本接口（UpgradeInstance）提供纵向扩容实例功能

        :param request: Request instance for UpgradeInstance.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.UpgradeInstanceRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.UpgradeInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))