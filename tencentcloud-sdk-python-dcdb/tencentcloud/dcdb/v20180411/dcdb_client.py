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
from tencentcloud.dcdb.v20180411 import models


class DcdbClient(AbstractClient):
    _apiVersion = '2018-04-11'
    _endpoint = 'dcdb.tencentcloudapi.com'


    def CloneAccount(self, request):
        """本接口（CloneAccount）用于克隆实例账户。

        :param request: Request instance for CloneAccount.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloneAccountResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CloseDBExtranetAccessResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CopyAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateAccountResponse`

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


    def CreateDCDBInstance(self, request):
        """本接口（CreateDCDBInstance）用于创建包年包月的云数据库实例，可通过传入实例规格、数据库版本号、购买时长等信息创建云数据库实例。

        :param request: Request instance for CreateDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.CreateDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DeleteAccountResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountPrivilegesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeAccountsResponse`

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


    def DescribeDBLogFiles(self, request):
        """本接口(DescribeDBLogFiles)用于获取数据库的各种日志列表，包括冷备、binlog、errlog和slowlog。

        :param request: Request instance for DescribeDBLogFiles.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBLogFilesResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBParametersResponse`

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


    def DescribeDBSyncMode(self, request):
        """本接口（DescribeDBSyncMode）用于查询云数据库实例的同步模式。

        :param request: Request instance for DescribeDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSyncMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSyncModeResponse()
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


    def DescribeDCDBInstances(self, request):
        """查询云数据库实例列表，支持通过项目ID、实例ID、内网地址、实例名称等来筛选实例。
        如果不指定任何筛选条件，则默认返回10条实例记录，单次请求最多支持返回100条实例记录。

        :param request: Request instance for DescribeDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBInstancesResponse()
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


    def DescribeDCDBPrice(self, request):
        """本接口（DescribeDCDBPrice）用于在购买实例前，查询实例的价格。

        :param request: Request instance for DescribeDCDBPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBPriceResponse()
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


    def DescribeDCDBRenewalPrice(self, request):
        """本接口（DescribeDCDBRenewalPrice）用于在续费分布式数据库实例时，查询续费的价格。

        :param request: Request instance for DescribeDCDBRenewalPrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBRenewalPriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBRenewalPrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBRenewalPriceResponse()
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


    def DescribeDCDBSaleInfo(self, request):
        """本接口(DescribeDCDBSaleInfo)用于查询分布式数据库可售卖的地域和可用区信息。

        :param request: Request instance for DescribeDCDBSaleInfo.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBSaleInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBSaleInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBSaleInfoResponse()
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


    def DescribeDCDBShards(self, request):
        """本接口（DescribeDCDBShards）用于查询云数据库实例的分片信息。

        :param request: Request instance for DescribeDCDBShards.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBShardsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBShards", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBShardsResponse()
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


    def DescribeDCDBUpgradePrice(self, request):
        """本接口（DescribeDCDBUpgradePrice）用于查询升级分布式数据库实例价格。

        :param request: Request instance for DescribeDCDBUpgradePrice.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDCDBUpgradePriceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDCDBUpgradePrice", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDCDBUpgradePriceResponse()
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


    def DescribeDatabaseObjects(self, request):
        """本接口（DescribeDatabaseObjects）用于查询云数据库实例的数据库中的对象列表，包含表、存储过程、视图和函数。

        :param request: Request instance for DescribeDatabaseObjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseObjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseObjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseObjectsResponse()
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


    def DescribeDatabaseTable(self, request):
        """本接口（DescribeDatabaseTable）用于查询云数据库实例的表信息。

        :param request: Request instance for DescribeDatabaseTable.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabaseTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDatabaseTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDatabaseTableResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeDatabasesResponse`

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


    def DescribeOrders(self, request):
        """本接口（DescribeOrders）用于查询分布式数据库订单信息。传入订单ID来查询订单关联的分布式数据库实例，和对应的任务流程ID。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeOrdersResponse`

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


    def DescribeProjects(self, request):
        """本接口（DescribeProjects）用于查询项目列表

        :param request: Request instance for DescribeProjects.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeProjectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProjects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProjectsResponse()
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


    def DescribeShardSpec(self, request):
        """查询可创建的分布式数据库可售卖的分片规格配置。

        :param request: Request instance for DescribeShardSpec.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeShardSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeShardSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeShardSpecResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.DescribeSqlLogsRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.DescribeSqlLogsResponse`

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


    def GrantAccountPrivileges(self, request):
        """本接口（GrantAccountPrivileges）用于给云数据库账号赋权。
        注意：相同用户名，不同Host是不同的账号。

        :param request: Request instance for GrantAccountPrivileges.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.GrantAccountPrivilegesResponse`

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


    def InitDCDBInstances(self, request):
        """本接口(InitDCDBInstances)用于初始化云数据库实例，包括设置默认字符集、表名大小写敏感等。

        :param request: Request instance for InitDCDBInstances.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.InitDCDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InitDCDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InitDCDBInstancesResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyAccountDescriptionResponse`

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


    def ModifyDBInstancesProject(self, request):
        """本接口（ModifyDBInstancesProject）用于修改云数据库实例所属项目。

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBInstancesProjectResponse`

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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBParametersResponse`

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


    def ModifyDBSyncMode(self, request):
        """本接口（ModifyDBSyncMode）用于修改云数据库实例的同步模式。

        :param request: Request instance for ModifyDBSyncMode.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ModifyDBSyncModeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBSyncMode", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBSyncModeResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.OpenDBExtranetAccessResponse`

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


    def RenewDCDBInstance(self, request):
        """本接口（RenewDCDBInstance）用于续费分布式数据库实例。

        :param request: Request instance for RenewDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.RenewDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewDCDBInstanceResponse()
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
        :type request: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.ResetAccountPasswordResponse`

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


    def UpgradeDCDBInstance(self, request):
        """本接口（UpgradeDCDBInstance）用于升级分布式数据库实例。本接口完成下单和支付两个动作，如果发生支付失败的错误，调用用户账户相关接口中的支付订单接口（PayDeals）重新支付即可。

        :param request: Request instance for UpgradeDCDBInstance.
        :type request: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceRequest`
        :rtype: :class:`tencentcloud.dcdb.v20180411.models.UpgradeDCDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDCDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDCDBInstanceResponse()
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