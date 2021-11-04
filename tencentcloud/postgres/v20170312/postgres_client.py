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
            body = self.call("AddDBInstanceToReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddDBInstanceToReadOnlyGroupResponse()
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
        """本接口（CloseDBExtranetAccess）用于关闭实例外网链接。

        :param request: Request instance for CloseDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseDBExtranetAccessResponse`

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


    def CloseServerlessDBExtranetAccess(self, request):
        """关闭serverlessDB实例外网

        :param request: Request instance for CloseServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CloseServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloseServerlessDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloseServerlessDBExtranetAccessResponse()
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
        """本接口 (CreateDBInstances) 用于创建一个或者多个PostgreSQL实例,仅发货实例不会进行初始化。

        :param request: Request instance for CreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateDBInstancesResponse`

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


    def CreateInstances(self, request):
        """本接口 (CreateInstances) 用于创建一个或者多个PostgreSQL实例，通过此接口创建的实例无需进行初始化，可直接使用。

        :param request: Request instance for CreateInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateInstancesResponse()
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


    def CreateReadOnlyDBInstance(self, request):
        """本接口(CreateReadOnlyDBInstance)用于创建只读实例

        :param request: Request instance for CreateReadOnlyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReadOnlyDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReadOnlyDBInstanceResponse()
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


    def CreateReadOnlyGroup(self, request):
        """本接口（CreateReadOnlyGroup）用于创建只读组

        :param request: Request instance for CreateReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateReadOnlyGroupResponse()
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


    def CreateServerlessDBInstance(self, request):
        """本接口 (CreateServerlessDBInstance) 用于创建一个ServerlessDB实例，创建成功返回实例ID。

        :param request: Request instance for CreateServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.CreateServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServerlessDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServerlessDBInstanceResponse()
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


    def DeleteReadOnlyGroup(self, request):
        """本接口(DeleteReadOnlyGroup)用于删除指定的只读组

        :param request: Request instance for DeleteReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteReadOnlyGroupResponse()
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


    def DeleteServerlessDBInstance(self, request):
        """本接口 (DeleteServerlessDBInstance) 用于删除一个ServerlessDB实例。

        :param request: Request instance for DeleteServerlessDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DeleteServerlessDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServerlessDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServerlessDBInstanceResponse()
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
        """本接口（DescribeAccounts）用于获取实例用户列表。

        :param request: Request instance for DescribeAccounts.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeAccountsResponse`

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


    def DescribeDBBackups(self, request):
        """本接口（DescribeDBBackups）用于查询实例备份列表。

        :param request: Request instance for DescribeDBBackups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBBackupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBBackups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBBackupsResponse()
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


    def DescribeDBErrlogs(self, request):
        """本接口（DescribeDBErrlogs）用于获取错误日志。

        :param request: Request instance for DescribeDBErrlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBErrlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBErrlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBErrlogsResponse()
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


    def DescribeDBInstanceAttribute(self, request):
        """本接口 (DescribeDBInstanceAttribute) 用于查询某个实例的详情信息。

        :param request: Request instance for DescribeDBInstanceAttribute.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceAttributeResponse()
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


    def DescribeDBInstanceParameters(self, request):
        """获取实例可修改参数列表

        :param request: Request instance for DescribeDBInstanceParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBInstanceParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBInstanceParametersResponse()
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
        """本接口 (DescribeDBInstances) 用于查询一个或多个实例的详细信息。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBInstancesResponse`

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


    def DescribeDBSlowlogs(self, request):
        """本接口（DescribeDBSlowlogs）用于获取慢查询日志。已于2021.09.01日正式废弃，后续此接口将不再返回任何数据，新接口为DescribeSlowQueryList，详细请查看：https://cloud.tencent.com/document/product/409/60540

        :param request: Request instance for DescribeDBSlowlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBSlowlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBSlowlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBSlowlogsResponse()
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


    def DescribeDBXlogs(self, request):
        """本接口（DescribeDBXlogs）用于获取实例Xlog列表。

        :param request: Request instance for DescribeDBXlogs.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDBXlogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDBXlogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDBXlogsResponse()
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
        """接口（DescribeDatabases）用来拉取数据库列表

        :param request: Request instance for DescribeDatabases.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeDatabasesResponse`

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
        """本接口（DescribeOrders）用于获取订单信息。

        :param request: Request instance for DescribeOrders.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeOrdersResponse`

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


    def DescribeParamsEvent(self, request):
        """获取参数修改事件详情

        :param request: Request instance for DescribeParamsEvent.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeParamsEventRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeParamsEventResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeParamsEvent", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeParamsEventResponse()
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
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeProductConfigResponse`

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


    def DescribeReadOnlyGroups(self, request):
        """本接口(DescribeReadOnlyGroups)用于查询用户输入指定实例的只读组

        :param request: Request instance for DescribeReadOnlyGroups.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeReadOnlyGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeReadOnlyGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeReadOnlyGroupsResponse()
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
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeRegionsResponse`

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


    def DescribeServerlessDBInstances(self, request):
        """用于查询一个或多个serverlessDB实例的详细信息

        :param request: Request instance for DescribeServerlessDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeServerlessDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServerlessDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServerlessDBInstancesResponse()
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


    def DescribeSlowQueryAnalysis(self, request):
        """此接口（DescribeSlowQueryAnalysis）用于统计指定时间范围内的所有慢查询，根据SQL语句抽象参数后，进行聚合分析，并返回同类SQL列表。

        :param request: Request instance for DescribeSlowQueryAnalysis.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryAnalysisRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryAnalysisResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowQueryAnalysis", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowQueryAnalysisResponse()
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


    def DescribeSlowQueryList(self, request):
        """此接口（DescribeSlowQueryList）用于查询指定时间范围内的所有慢查询。

        :param request: Request instance for DescribeSlowQueryList.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryListRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeSlowQueryListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowQueryList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowQueryListResponse()
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
        """本接口 (DescribeZones) 用于查询支持的可用区信息。

        :param request: Request instance for DescribeZones.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DescribeZonesResponse`

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


    def DestroyDBInstance(self, request):
        """本接口 (DestroyDBInstance) 用于彻底下线指定DBInstanceId对应的实例，下线后实例数据将彻底删除，无法找回，只能下线隔离中的实例。

        :param request: Request instance for DestroyDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DestroyDBInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DestroyDBInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DestroyDBInstanceResponse()
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


    def DisIsolateDBInstances(self, request):
        """本接口（DisIsolateDBInstances）用于解隔离实例

        :param request: Request instance for DisIsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.DisIsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisIsolateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisIsolateDBInstancesResponse()
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
        """本接口 (InitDBInstances) 用于初始化云数据库PostgreSQL实例。

        :param request: Request instance for InitDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InitDBInstancesResponse`

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


    def InquiryPriceCreateDBInstances(self, request):
        """本接口 (InquiryPriceCreateDBInstances) 用于查询购买一个或多个实例的价格信息。

        :param request: Request instance for InquiryPriceCreateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceCreateDBInstancesResponse`

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
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceRenewDBInstanceResponse`

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
        :type request: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.InquiryPriceUpgradeDBInstanceResponse`

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


    def IsolateDBInstances(self, request):
        """本接口（IsolateDBInstances）用于隔离实例

        :param request: Request instance for IsolateDBInstances.
        :type request: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.IsolateDBInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("IsolateDBInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.IsolateDBInstancesResponse()
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
        """本接口（ModifyAccountRemark）用于修改帐号备注。

        :param request: Request instance for ModifyAccountRemark.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyAccountRemarkResponse`

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
        """本接口（ModifyDBInstanceName）用于修改postgresql实例名字。

        :param request: Request instance for ModifyDBInstanceName.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceNameResponse`

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


    def ModifyDBInstanceParameters(self, request):
        """批量修改参数

        :param request: Request instance for ModifyDBInstanceParameters.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceParametersRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceParametersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceParameters", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceParametersResponse()
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


    def ModifyDBInstanceReadOnlyGroup(self, request):
        """本接口（ModifyDBInstanceReadOnlyGroup）用于修改实例所属的只读组

        :param request: Request instance for ModifyDBInstanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceReadOnlyGroupResponse()
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


    def ModifyDBInstanceSpec(self, request):
        """本接口（ModifyDBInstanceSpec）用于调整实例规格，包括内存、磁盘。

        :param request: Request instance for ModifyDBInstanceSpec.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSpecRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstanceSpecResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDBInstanceSpec", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDBInstanceSpecResponse()
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
        """本接口（ModifyDBInstancesProject）用于将实例转至其他项目。

        :param request: Request instance for ModifyDBInstancesProject.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyDBInstancesProjectResponse`

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


    def ModifyReadOnlyGroupConfig(self, request):
        """本接口(ModifyReadOnlyGroupConfig)用于更新只读组配置信息

        :param request: Request instance for ModifyReadOnlyGroupConfig.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifyReadOnlyGroupConfigResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyReadOnlyGroupConfig", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyReadOnlyGroupConfigResponse()
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


    def ModifySwitchTimePeriod(self, request):
        """当升级完成后，对处于等待切换状态下的实例，强制实例立即切换。

        :param request: Request instance for ModifySwitchTimePeriod.
        :type request: :class:`tencentcloud.postgres.v20170312.models.ModifySwitchTimePeriodRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ModifySwitchTimePeriodResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySwitchTimePeriod", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySwitchTimePeriodResponse()
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
        """本接口（OpenDBExtranetAccess）用于开通外网。

        :param request: Request instance for OpenDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenDBExtranetAccessResponse`

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


    def OpenServerlessDBExtranetAccess(self, request):
        """开通serverlessDB实例外网

        :param request: Request instance for OpenServerlessDBExtranetAccess.
        :type request: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.OpenServerlessDBExtranetAccessResponse`

        """
        try:
            params = request._serialize()
            body = self.call("OpenServerlessDBExtranetAccess", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.OpenServerlessDBExtranetAccessResponse()
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


    def RebalanceReadOnlyGroup(self, request):
        """本接口(RebalanceReadOnlyGroup)用于重新均衡 RO 组内实例的负载。注意，RO 组内 RO 实例会有一次数据库连接瞬断，请确保应用程序能重连数据库，谨慎操作。

        :param request: Request instance for RebalanceReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RebalanceReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RebalanceReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RebalanceReadOnlyGroupResponse()
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


    def RemoveDBInstanceFromReadOnlyGroup(self, request):
        """本接口（RemoveDBInstanceFromReadOnlyGroup）用户将只读实例从只读组中移除

        :param request: Request instance for RemoveDBInstanceFromReadOnlyGroup.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RemoveDBInstanceFromReadOnlyGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveDBInstanceFromReadOnlyGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveDBInstanceFromReadOnlyGroupResponse()
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


    def RenewInstance(self, request):
        """本接口（RenewInstance）用于续费实例。

        :param request: Request instance for RenewInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RenewInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewInstanceResponse()
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
        :type request: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.ResetAccountPasswordResponse`

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
        """本接口（RestartDBInstance）用于重启实例。

        :param request: Request instance for RestartDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.RestartDBInstanceResponse`

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


    def SetAutoRenewFlag(self, request):
        """本接口（SetAutoRenewFlag）用于设置自动续费。

        :param request: Request instance for SetAutoRenewFlag.
        :type request: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.SetAutoRenewFlagResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAutoRenewFlag", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAutoRenewFlagResponse()
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
        """本接口（UpgradeDBInstance）用于升级实例配置。

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.postgres.v20170312.models.UpgradeDBInstanceResponse`

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