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



from tencentcloud.common.abstract_client_async import AbstractClient
from tencentcloud.mongodb.v20180408 import models
from typing import Dict


class MongodbClient(AbstractClient):
    _apiVersion = '2018-04-08'
    _endpoint = 'mongodb.tencentcloudapi.com'
    _service = 'mongodb'

    async def AssignProject(
            self,
            request: models.AssignProjectRequest,
            opts: Dict = None,
    ) -> models.AssignProjectResponse:
        """
        本接口（AssignProject）用于指定云数据库实例的所属项目。
        """
        
        kwargs = {}
        kwargs["action"] = "AssignProject"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignProjectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstance(
            self,
            request: models.CreateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceResponse:
        """
        本接口(CreateDBInstance)用于创建包年包月的MongoDB云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstanceHour(
            self,
            request: models.CreateDBInstanceHourRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstanceHourResponse:
        """
        本接口(CreateDBInstanceHour)用于创建按量计费的MongoDB云数据库实例，可通过传入实例规格、实例类型、MongoDB版本、购买时长和数量等信息创建云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstanceHour"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstanceHourResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClientConnections(
            self,
            request: models.DescribeClientConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeClientConnectionsResponse:
        """
        本接口(DescribeClientConnections)用于查询实例客户端连接信息，包括连接IP和连接数量。目前只支持3.2版本的MongoDB实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClientConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClientConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口(DescribeDBInstances)用于查询云数据库实例列表，支持通过项目ID、实例ID、实例状态等过滤条件来筛选实例。支持查询主实例、灾备实例和只读实例信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLog(
            self,
            request: models.DescribeSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogResponse:
        """
        本接口(DescribeSlowLogs)用于获取云数据库实例的慢查询日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecInfo(
            self,
            request: models.DescribeSpecInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecInfoResponse:
        """
        本接口(DescribeSpecInfo)用于查询实例的售卖规格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenameInstance(
            self,
            request: models.RenameInstanceRequest,
            opts: Dict = None,
    ) -> models.RenameInstanceResponse:
        """
        本接口(RenameInstance)用于修改云数据库实例的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "RenameInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenameInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAutoRenew(
            self,
            request: models.SetAutoRenewRequest,
            opts: Dict = None,
    ) -> models.SetAutoRenewResponse:
        """
        本接口(SetAutoRenew)用于设置包年包月云数据库实例的续费选项。
        """
        
        kwargs = {}
        kwargs["action"] = "SetAutoRenew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAutoRenewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetPassword(
            self,
            request: models.SetPasswordRequest,
            opts: Dict = None,
    ) -> models.SetPasswordResponse:
        """
        本接口(SetPassword)用于设置（初始化）MongoDB云数据库实例账户密码。
        """
        
        kwargs = {}
        kwargs["action"] = "SetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDBInstance(
            self,
            request: models.TerminateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateDBInstanceResponse:
        """
        本接口(TerminateDBInstance)用于销毁按量计费的MongoDB云数据库实例。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstance(
            self,
            request: models.UpgradeDBInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceResponse:
        """
        本接口(UpgradeDBInstance)用于升级包年包月的MongoDB云数据库实例，可以扩容内存、存储以及Oplog
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeDBInstanceHour(
            self,
            request: models.UpgradeDBInstanceHourRequest,
            opts: Dict = None,
    ) -> models.UpgradeDBInstanceHourResponse:
        """
        本接口(UpgradeDBInstanceHour)用于升级按量计费的MongoDB云数据库实例，可以扩容内存、存储以及oplog
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeDBInstanceHour"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeDBInstanceHourResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)