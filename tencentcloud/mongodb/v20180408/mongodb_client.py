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
from tencentcloud.mongodb.v20180408 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'mongodb.tencentcloudapi.com'
    _service = 'mongodb'


    def AssignProject(self, request):
        """本接口（AssignProject）用于指定云数据库实例的所属项目。

        :param request: Request instance for AssignProject.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.AssignProjectRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignProject", params, headers=headers)
            response = json.loads(body)
            model = models.AssignProjectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDBInstance(self, request):
        """本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。

        :param request: Request instance for CreateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceResponse`

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


    def CreateDBInstanceHour(self, request):
        """本接口(CreateDBInstanceHour)用于创建按量计费的MongoDB云数据库实例，可通过传入实例规格、实例类型、MongoDB版本、购买时长和数量等信息创建云数据库实例。

        :param request: Request instance for CreateDBInstanceHour.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDBInstanceHour", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDBInstanceHourResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClientConnections(self, request):
        """本接口(DescribeClientConnections)用于查询实例客户端连接信息，包括连接IP和连接数量。目前只支持3.2版本的MongoDB实例。

        :param request: Request instance for DescribeClientConnections.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeClientConnectionsRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeClientConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClientConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClientConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDBInstances(self, request):
        """本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。

        :param request: Request instance for DescribeDBInstances.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeDBInstancesResponse`

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


    def DescribeSlowLog(self, request):
        """本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。

        :param request: Request instance for DescribeSlowLog.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeSlowLogRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecInfo(self, request):
        """本接口(DescribeSpecInfo)用于查询实例的售卖规格。

        :param request: Request instance for DescribeSpecInfo.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeSpecInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecInfo", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecInfoResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenameInstance(self, request):
        """本接口(RenameInstance)用于修改云数据库实例的名称。

        :param request: Request instance for RenameInstance.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.RenameInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenameInstance", params, headers=headers)
            response = json.loads(body)
            model = models.RenameInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetAutoRenew(self, request):
        """本接口(SetAutoRenew)用于设置包年包月云数据库实例的续费选项。

        :param request: Request instance for SetAutoRenew.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.SetAutoRenewRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.SetAutoRenewResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetAutoRenew", params, headers=headers)
            response = json.loads(body)
            model = models.SetAutoRenewResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetPassword(self, request):
        """本接口(SetPassword)用于设置（初始化）MongoDB云数据库实例账户密码。

        :param request: Request instance for SetPassword.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.SetPasswordRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.SetPasswordResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetPassword", params, headers=headers)
            response = json.loads(body)
            model = models.SetPasswordResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TerminateDBInstance(self, request):
        """本接口(TerminateDBInstance)用于销毁按量计费的MongoDB云数据库实例。

        :param request: Request instance for TerminateDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.TerminateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.TerminateDBInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TerminateDBInstance", params, headers=headers)
            response = json.loads(body)
            model = models.TerminateDBInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpgradeDBInstance(self, request):
        """本接口(UpgradeDBInstance)用于升级包年包月的MongoDB云数据库实例，可以扩容内存、存储以及Oplog

        :param request: Request instance for UpgradeDBInstance.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceResponse`

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


    def UpgradeDBInstanceHour(self, request):
        """本接口(UpgradeDBInstanceHour)用于升级按量计费的MongoDB云数据库实例，可以扩容内存、存储以及oplog

        :param request: Request instance for UpgradeDBInstanceHour.
        :type request: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpgradeDBInstanceHour", params, headers=headers)
            response = json.loads(body)
            model = models.UpgradeDBInstanceHourResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))