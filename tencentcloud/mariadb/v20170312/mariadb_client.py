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
from tencentcloud.mariadb.v20170312 import models


class MariadbClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'mariadb.tencentcloudapi.com'


    def CloneAccount(self, request):
        """本接口（CloneAccount）用于克隆实例账户。

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloneAccountResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloneAccount", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneAccountResponse()
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


    def CloseDBExtranetAccess(self, request):
        """本接口(CloseDBExtranetAccess)用于关闭云数据库实例的外网访问。关闭外网访问后，外网地址将不可访问，查询实例列表接口将不返回对应实例的外网域名和端口信息。

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CloseDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseDBExtranetAccessResponse()
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


    def CopyAccountPrivileges(self, request):
        """本接口（CopyAccountPrivileges）用于复制云数据库账号的权限。
        注意：相同用户名，不同Host是不同的账号，Readonly属性相同的账号之间才能复制权限。

        :param request: Request instance for CopyAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CopyAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CopyAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CopyAccountPrivilegesResponse()
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
        """本接口（CreateAccount）用于创建云数据库账号。一个实例可以创建多个不同的账号，相同的用户名+不同的host是不同的账号。

        :param request: Request instance for CreateAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateAccountResponse`

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


    def CreateDBInstance(self, request):
        """本接口（CreateDBInstance）用于创建包年包月的云数据库实例，可通过传入实例规格、数据库版本号、购买时长和数量等信息创建云数据库实例。

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceResponse()
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


    def CreateTmpInstances(self, request):
        """本接口（CreateTmpInstances）用于创建临时实例。

        :param request: Request instance for CreateTmpInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.CreateTmpInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.CreateTmpInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateTmpInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateTmpInstancesResponse()
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
        """本接口（DeleteAccount）用于删除云数据库账号。用户名+host唯一确定一个账号。

        :param request: Request instance for DeleteAccount.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DeleteAccountResponse`

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


    def DescribeAccountPrivileges(self, request):
        """本接口（DescribeAccountPrivileges）用于查询云数据库账号权限。
        注意：注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for DescribeAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountPrivilegesResponse()
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
        """本接口（DescribeAccounts）用于查询指定云数据库实例的账号列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeAccountsResponse`

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


    def DescribeBackupTime(self, request):
        """本接口（DescribeBackupTime）用于获取云数据库的备份时间。后台系统将根据此配置定期进行实例备份。

        :param request: Request instance for DescribeBackupTime.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupTimeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeBackupTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBackupTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBackupTimeResponse()
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


    def DescribeDBInstanceSpecs(self, request):
        """本接口(DescribeDBInstanceSpecs)用于查询可创建的云数据库可售卖的规格配置。

        :param request: Request instance for DescribeDBInstanceSpecs.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceSpecsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstanceSpecsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceSpecs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceSpecsResponse()
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
        """本接口（DescribeDBInstances）用于查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回20条实例记录，单次请求最多支持返回100条实例记录。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBLogFiles(self, request):
        """本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBLogFilesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBLogFiles", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBLogFilesResponse()
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


    def DescribeDBParameters(self, request):
        """本接口(DescribeDBParameters)用于获取数据库的当前参数设置。

        :param request: Request instance for DescribeDBParameters.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBParametersResponse()
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


    def DescribeDBPerformance(self, request):
        """本接口(DescribeDBPerformance)用于查看数据库实例当前性能数据。

        :param request: Request instance for DescribeDBPerformance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPerformance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPerformanceResponse()
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


    def DescribeDBPerformanceDetails(self, request):
        """本接口(DescribeDBPerformanceDetails)用于查看实例性能数据详情。

        :param request: Request instance for DescribeDBPerformanceDetails.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceDetailsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBPerformanceDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBPerformanceDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBPerformanceDetailsResponse()
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


    def DescribeDBResourceUsage(self, request):
        """本接口(DescribeDBResourceUsage)用于查看数据库实例资源的使用情况。

        :param request: Request instance for DescribeDBResourceUsage.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBResourceUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBResourceUsageResponse()
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


    def DescribeDBResourceUsageDetails(self, request):
        """本接口(DescribeDBResourceUsageDetails)用于查看数据库实例当前性能数据。

        :param request: Request instance for DescribeDBResourceUsageDetails.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageDetailsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBResourceUsageDetailsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBResourceUsageDetails", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBResourceUsageDetailsResponse()
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


    def DescribeDBSlowLogs(self, request):
        """本接口(DescribeDBSlowLogs)用于查询慢查询日志列表。

        :param request: Request instance for DescribeDBSlowLogs.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDBSlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowLogsResponse()
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


    def DescribeDatabases(self, request):
        """本接口（DescribeDatabases）用于查询云数据库实例的数据库列表。

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeDatabasesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabases", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabasesResponse()
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


    def DescribeFlow(self, request):
        """本接口（DescribeFlow）用于查询流程状态。

        :param request: Request instance for DescribeFlow.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeFlowRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeFlowResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlow", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowResponse()
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


    def DescribeLogFileRetentionPeriod(self, request):
        """本接口(DescribeLogFileRetentionPeriod)用于查看数据库备份日志的备份天数的设置情况。

        :param request: Request instance for DescribeLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLogFileRetentionPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLogFileRetentionPeriodResponse()
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
        """本接口（DescribeOrders）用于查询云数据库订单信息。传入订单Id来查询订单关联的云数据库实例，和对应的任务流程ID。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeOrdersResponse`

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


    def DescribePrice(self, request):
        """本接口（DescribePrice）用于在购买实例前，查询实例的价格。

        :param request: Request instance for DescribePrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribePriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribePriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribePrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribePriceResponse()
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


    def DescribeRenewalPrice(self, request):
        """本接口（DescribeRenewalPrice）用于在续费云数据库实例时，查询续费的价格。

        :param request: Request instance for DescribeRenewalPrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeRenewalPriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRenewalPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRenewalPriceResponse()
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


    def DescribeSaleInfo(self, request):
        """本接口(DescribeSaleInfo)用于查询云数据库可售卖的地域和可用区信息。

        :param request: Request instance for DescribeSaleInfo.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeSaleInfoRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeSaleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSaleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSaleInfoResponse()
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


    def DescribeSqlLogs(self, request):
        """本接口（DescribeSqlLogs）用于获取实例SQL日志。

        :param request: Request instance for DescribeSqlLogs.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeSqlLogsRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeSqlLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSqlLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSqlLogsResponse()
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


    def DescribeUpgradePrice(self, request):
        """本接口（DescribeUpgradePrice）用于在扩容云数据库实例时，查询扩容的价格。

        :param request: Request instance for DescribeUpgradePrice.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.DescribeUpgradePriceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.DescribeUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeUpgradePrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeUpgradePriceResponse()
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


    def GrantAccountPrivileges(self, request):
        """本接口（GrantAccountPrivileges）用于给云数据库账号赋权。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.GrantAccountPrivilegesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GrantAccountPrivileges", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GrantAccountPrivilegesResponse()
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


    def InitDBInstances(self, request):
        """本接口(InitDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.InitDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDBInstancesResponse()
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


    def ModifyAccountDescription(self, request):
        """本接口（ModifyAccountDescription）用于修改云数据库账号备注。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for ModifyAccountDescription.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyAccountDescriptionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAccountDescription", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAccountDescriptionResponse()
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


    def ModifyBackupTime(self, request):
        """本接口（ModifyBackupTime）用于设置云数据库实例的备份时间。后台系统将根据此配置定期进行实例备份。

        :param request: Request instance for ModifyBackupTime.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyBackupTimeRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyBackupTimeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBackupTime", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBackupTimeResponse()
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
        """本接口（ModifyDBInstanceName）用于修改云数据库实例的名称。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstancesProject(self, request):
        """本接口（ModifyDBInstancesProject）用于修改云数据库实例所属项目。

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBInstancesProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstancesProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstancesProjectResponse()
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


    def ModifyDBParameters(self, request):
        """本接口(ModifyDBParameters)用于修改数据库参数。

        :param request: Request instance for ModifyDBParameters.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyDBParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBParametersResponse()
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


    def ModifyLogFileRetentionPeriod(self, request):
        """本接口(ModifyLogFileRetentionPeriod)用于修改数据库备份日志保存天数。

        :param request: Request instance for ModifyLogFileRetentionPeriod.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ModifyLogFileRetentionPeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLogFileRetentionPeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLogFileRetentionPeriodResponse()
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


    def OpenDBExtranetAccess(self, request):
        """本接口（OpenDBExtranetAccess）用于开通云数据库实例的外网访问。开通外网访问后，您可通过外网域名和端口访问实例，可使用查询实例列表接口获取外网域名和端口信息。

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.OpenDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenDBExtranetAccessResponse()
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
        """本接口（RenewDBInstance）用于续费云数据库实例。

        :param request: Request instance for RenewDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.RenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.RenewDBInstanceResponse`

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
        """本接口（ResetAccountPassword）用于重置云数据库账号的密码。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for ResetAccountPassword.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.ResetAccountPasswordResponse`

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


    def RestartDBInstances(self, request):
        """本接口（RestartDBInstances）用于重启数据库实例

        :param request: Request instance for RestartDBInstances.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.RestartDBInstancesRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.RestartDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RestartDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RestartDBInstancesResponse()
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
        """本接口(UpgradeDBInstance)用于扩容云数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.mariadb.v20170312.models.UpgradeDBInstanceResponse`

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