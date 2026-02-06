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


    def CreateDBSBackup(self, request):
        r"""创建实例备份集

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


    def DeleteDBSBackupSets(self, request):
        r"""删除实例备份集

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


    def DescribeBillingEnable(self, request):
        r"""已无地方调用

        本接口（DescribeBillingEnable）用于查询计费是否开启

        :param request: Request instance for DescribeBillingEnable.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeBillingEnableRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeBillingEnableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBillingEnable", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBillingEnableResponse()
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


    def DescribeDBSAvailableRecoveryTime(self, request):
        r"""可恢复时间查询

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


    def DescribeDBSCloneInstances(self, request):
        r"""查询实例克隆列表

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


    def DescribeDatabaseTable(self, request):
        r"""冗余接口，无人调用

        本接口（DescribeDatabaseTable）用于查询云数据库实例的表信息。

        :param request: Request instance for DescribeDatabaseTable.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.DescribeDatabaseTableResponse`

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


    def ModifyBinlogStatus(self, request):
        r"""接口功能已被 ModifyInstanceCdc 完全覆盖

        修改binlog状态

        :param request: Request instance for ModifyBinlogStatus.
        :type request: :class:`tencentcloud.tdmysql.v20211122.models.ModifyBinlogStatusRequest`
        :rtype: :class:`tencentcloud.tdmysql.v20211122.models.ModifyBinlogStatusResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBinlogStatus", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBinlogStatusResponse()
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
        r"""修改实例备份策略

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
        r"""修改备份集备注

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