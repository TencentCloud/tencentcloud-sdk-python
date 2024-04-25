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
from tencentcloud.dcdb.v20180411 import models


class DcdbClient(AbstractClient):
    _apiVersion = '2018-04-11'
    _endpoint = 'dcdb.tencentcloudapi.com'
    _service = 'dcdb'


    def ActiveHourDCDBInstance(self, request):
        """解隔离TDSQL按量计费实例

        :param request: Request instance for ActiveHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ActiveHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ActiveHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ActiveHourDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.AssociateSecurityGroupsResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CancelDcnJobResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountResponse`

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


    def CreateDCDBInstance(self, request):
        """本接口（CreateDCDBInstance）用于创建包年包月的TDSQL实例，可通过传入实例规格、数据库版本号、购买时长等信息创建云数据库实例。

        :param request: Request instance for CreateDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDedicatedClusterDCDBInstance(self, request):
        """创建TDSQL独享集群实例

        :param request: Request instance for CreateDedicatedClusterDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDedicatedClusterDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDedicatedClusterDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDedicatedClusterDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDedicatedClusterDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHourDCDBInstance(self, request):
        """创建TDSQL按量计费实例

        :param request: Request instance for CreateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTmpDCDBInstance(self, request):
        """回档TDSQL实例

        :param request: Request instance for CreateTmpDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateTmpDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateTmpDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTmpDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTmpDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeBackupFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeBackupFilesResponse`

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


    def DescribeDBEncryptAttributes(self, request):
        """本接口(DescribeDBEncryptAttributes)用于查询实例数据加密状态。

        :param request: Request instance for DescribeDBEncryptAttributes.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBEncryptAttributesResponse`

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


    def DescribeDBLogFiles(self, request):
        """本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSecurityGroupsResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSlowLogsResponse`

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


    def DescribeDBSyncMode(self, request):
        """本接口（DescribeDBSyncMode）用于查询云数据库实例的同步模式。

        :param request: Request instance for DescribeDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDBSyncMode", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDBSyncModeResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBTmpInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBTmpInstancesResponse`

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


    def DescribeDCDBInstanceDetail(self, request):
        """本接口（DescribeDCDBInstanceDetail）用于获取TDSQL实例详情

        :param request: Request instance for DescribeDCDBInstanceDetail.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceDetailRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstanceDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBInstanceDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBInstanceNodeInfo(self, request):
        """本接口（DescribeDCDBInstanceNodeInfo）用于获取实例节点信息

        :param request: Request instance for DescribeDCDBInstanceNodeInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstanceNodeInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstanceNodeInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBInstanceNodeInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBInstances(self, request):
        """查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回10条实例记录，单次请求最多支持返回100条实例记录。

        :param request: Request instance for DescribeDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBPrice(self, request):
        """本接口（DescribeDCDBPrice）用于在购买实例前，查询实例的价格。

        :param request: Request instance for DescribeDCDBPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBRenewalPrice(self, request):
        """本接口（DescribeDCDBRenewalPrice）用于在续费分布式数据库实例时，查询续费的价格。

        :param request: Request instance for DescribeDCDBRenewalPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBRenewalPrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBRenewalPriceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBSaleInfo(self, request):
        """本接口(DescribeDCDBSaleInfo)用于查询分布式数据库可售卖的地域和可用区信息。

        :param request: Request instance for DescribeDCDBSaleInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBSaleInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBSaleInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBShards(self, request):
        """本接口（DescribeDCDBShards）用于查询云数据库实例的分片信息。

        :param request: Request instance for DescribeDCDBShards.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBShards", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBShardsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDCDBUpgradePrice(self, request):
        """本接口（DescribeDCDBUpgradePrice）用于查询变配分布式数据库实例价格。

        :param request: Request instance for DescribeDCDBUpgradePrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDCDBUpgradePrice", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDCDBUpgradePriceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDcnDetailResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFileDownloadUrlResponse`

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
        """本接口（DescribeFlow）用于查询流程状态

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeFlowResponse`

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


    def DescribeLogFileRetentionPeriod(self, request):
        """本接口(DescribeLogFileRetentionPeriod)用于查看数据库备份日志的备份天数的设置情况。

        :param request: Request instance for DescribeLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeLogFileRetentionPeriodResponse`

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
        """本接口（DescribeOrders）用于查询分布式数据库订单信息。传入订单ID来查询订单关联的分布式数据库实例，和对应的任务流程ID。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersResponse`

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


    def DescribeProjectSecurityGroups(self, request):
        """本接口（DescribeProjectSecurityGroups）用于查询项目安全组信息

        :param request: Request instance for DescribeProjectSecurityGroups.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectSecurityGroupsResponse`

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


    def DescribeProjects(self, request):
        """本接口（DescribeProjects）用于查询项目列表

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProjects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProjectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeShardSpec(self, request):
        """查询可创建的分布式数据库可售卖的分片规格配置。

        :param request: Request instance for DescribeShardSpec.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeShardSpec", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeShardSpecResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUserTasks(self, request):
        """本接口（DescribeUserTasks）用于拉取用户任务列表

        :param request: Request instance for DescribeUserTasks.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeUserTasksRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeUserTasksResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUserTasks", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUserTasksResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyDCDBInstance(self, request):
        """本接口(DestroyDCDBInstance)用于销毁已隔离的TDSQL包年包月实例。

        :param request: Request instance for DestroyDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DestroyHourDCDBInstance(self, request):
        """本接口（DestroyHourDCDBInstance）用于TDSQL销毁按量计费实例。

        :param request: Request instance for DestroyHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DestroyHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DestroyHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.DestroyHourDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DisassociateSecurityGroupsResponse`

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
        """相当于在所有分片的mysqld中执行flush logs，完成切分的binlog将展示在各个分片控制台binlog列表里。

        :param request: Request instance for FlushBinlog.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.FlushBinlogRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.FlushBinlogResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesResponse`

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


    def InitDCDBInstances(self, request):
        """本接口(InitDCDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。

        :param request: Request instance for InitDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InitDCDBInstances", params, headers=headers)
            response = json.loads(body)
            model = models.InitDCDBInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def IsolateDCDBInstance(self, request):
        """本接口(IsolateDCDBInstance)用于隔离分布式数据库TDSQL实例（包年包月），隔离后不能通过IP和端口访问数据库。隔离的实例可在回收站中进行开机。若为欠费隔离，请尽快进行充值。

        :param request: Request instance for IsolateDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateDedicatedDBInstanceResponse`

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


    def IsolateHourDCDBInstance(self, request):
        """隔离TDSQL按量计费实例

        :param request: Request instance for IsolateHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.IsolateHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("IsolateHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.IsolateHourDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.KillSessionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.KillSessionResponse`

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


    def ModifyAccountConfig(self, request):
        """修改账号的一些配置，比如 max_user_connections

        :param request: Request instance for ModifyAccountConfig.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountConfigRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountConfigResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAccountConfig", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAccountConfigResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountPrivilegesResponse`

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


    def ModifyDBEncryptAttributes(self, request):
        """本接口(ModifyDBEncryptAttributes)用于修改实例数据加密。

        :param request: Request instance for ModifyDBEncryptAttributes.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBEncryptAttributesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBEncryptAttributesResponse`

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
        """本接口（ModifyDBInstanceName）用于修改实例名字

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceNameResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstanceSecurityGroupsResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeResponse`

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
        """本接口（ModifyInstanceNetwork）用于修改实例所属网络。

        :param request: Request instance for ModifyInstanceNetwork.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceNetworkRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceNetworkResponse`

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
        """本接口（ModifyInstanceVip）用于修改实例Vip

        :param request: Request instance for ModifyInstanceVip.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVipRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVipResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVportRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyInstanceVportResponse`

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


    def ModifyRealServerAccessStrategy(self, request):
        """本接口(ModifyRealServerAccessStrategy)用于修改云数据库的VPCGW到RS的访问策略。

        **注意**
        - 修改策略后只对新建立的连接生效，老连接不受影响
        - 就近访问只针对实例是跨可用区部署有用，单可用区部署实例就近与否并无作用
        - DB每个Node对应一个proxy，如果开启就近访问，将会把连接集中到对应可用区的proxy上，可能造成热点问题，这种情况下如果是线上业务，请务必根据自己的业务请求量测试符合预期后再进行就近策略变更

        :param request: Request instance for ModifyRealServerAccessStrategy.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyRealServerAccessStrategyRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyRealServerAccessStrategyResponse`

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


    def OpenDBExtranetAccess(self, request):
        """本接口（OpenDBExtranetAccess）用于开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例，可使用查询实例列表接口获取外网域名和端口信息。

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessResponse`

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


    def RenewDCDBInstance(self, request):
        """本接口（RenewDCDBInstance）用于续费分布式数据库实例。

        :param request: Request instance for RenewDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenewDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordResponse`

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


    def SwitchDBInstanceHA(self, request):
        """本接口(SwitchDBInstanceHA)用于实例主备切换。

        :param request: Request instance for SwitchDBInstanceHA.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHARequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.SwitchDBInstanceHAResponse`

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
        """本接口（TerminateDedicatedDBInstance）用于销毁已隔离的独享分布式数据库实例。

        :param request: Request instance for TerminateDedicatedDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.TerminateDedicatedDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.TerminateDedicatedDBInstanceResponse`

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


    def UpgradeDCDBInstance(self, request):
        """本接口（UpgradeDCDBInstance）用于升级分布式数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。

        :param request: Request instance for UpgradeDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDedicatedDCDBInstance(self, request):
        """本接口（UpgradeDedicatedDCDBInstance）用于升级TDSQL独享集群实例

        :param request: Request instance for UpgradeDedicatedDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDedicatedDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDedicatedDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDedicatedDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDedicatedDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeHourDCDBInstance(self, request):
        """本接口（UpgradeHourDCDBInstance）用于升级分布式数据库TDSQL按量计费实例。

        :param request: Request instance for UpgradeHourDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeHourDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeHourDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeHourDCDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeHourDCDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))