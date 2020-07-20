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


    def TerminateDBInstance(self, request):
        """本接口(TerminateDBInstance)用于主动销毁按量计费实例。

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