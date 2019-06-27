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
from tencentcloud.mongodb.v20180408 import models


class MongodbClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'mongodb.tencentcloudapi.com'


    def AssignProject(self, request):
        """本接口(AssignProject)用于指定云数据库实例的所属项目。


        :param request: 调用AssignProject所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.AssignProjectRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.AssignProjectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignProject", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignProjectResponse()
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
        """本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。

        :param request: 调用CreateDBInstance所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceResponse`

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


    def CreateDBInstanceHour(self, request):
        """本接口(CreateDBInstanceHour)用于创建按量计费的MongoDB云数据库实例（包括主实例、灾备实例和只读实例），可通过传入实例规格、实例类型、MongoDB版本、购买时长和数量等信息创建云数据库实例。

        :param request: 调用CreateDBInstanceHour所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.CreateDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDBInstanceHourResponse()
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
        """本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。

        :param request: 调用DescribeDBInstances所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeDBInstancesRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeDBInstancesResponse`

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


    def DescribeSlowLog(self, request):
        """本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。

        :param request: 调用DescribeSlowLog所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeSlowLogRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeSlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSlowLogResponse()
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


    def DescribeSpecInfo(self, request):
        """本接口(DescribeSpecInfo)用于查询实例的售卖规格。

        :param request: 调用DescribeSpecInfo所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.DescribeSpecInfoRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.DescribeSpecInfoResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSpecInfo", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSpecInfoResponse()
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


    def RenameInstance(self, request):
        """本接口(RenameInstance)用于修改云数据库实例的名称。

        :param request: 调用RenameInstance所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.RenameInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.RenameInstanceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenameInstance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenameInstanceResponse()
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


    def SetAutoRenew(self, request):
        """本接口(SetAutoRenew)用于设置包年包月云数据库实例的续费选项。

        :param request: 调用SetAutoRenew所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.SetAutoRenewRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.SetAutoRenewResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetAutoRenew", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetAutoRenewResponse()
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


    def SetPassword(self, request):
        """本接口(SetPassword)用于设置云数据库账户的密码。


        :param request: 调用SetPassword所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.SetPasswordRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.SetPasswordResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetPassword", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetPasswordResponse()
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
        """本接口(TerminateDBInstance)用于销毁按量计费的MongoDB云数据库实例

        :param request: 调用TerminateDBInstance所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.TerminateDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.TerminateDBInstanceResponse`

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
        """本接口(UpgradeDBInstance)用于升级包年包月的MongoDB云数据库实例，可以扩容内存、存储以及Oplog

        :param request: 调用UpgradeDBInstance所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceResponse`

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


    def UpgradeDBInstanceHour(self, request):
        """本接口(UpgradeDBInstanceHour)用于升级按量计费的MongoDB云数据库实例，可以扩容内存、存储以及oplog

        :param request: 调用UpgradeDBInstanceHour所需参数的结构体。
        :type request: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceHourRequest`
        :rtype: :class:`tencentcloud.mongodb.v20180408.models.UpgradeDBInstanceHourResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UpgradeDBInstanceHour", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UpgradeDBInstanceHourResponse()
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