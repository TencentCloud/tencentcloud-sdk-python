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