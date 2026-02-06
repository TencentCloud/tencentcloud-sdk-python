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
from tencentcloud.tdmysql.v20211122 import models
from typing import Dict


class TdmysqlClient(AbstractClient):
    _apiVersion = '2021-11-22'
    _endpoint = 'tdmysql.tencentcloudapi.com'
    _service = 'tdmysql'

    async def CancelIsolateDBInstances(
            self,
            request: models.CancelIsolateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CancelIsolateDBInstancesResponse:
        """
        本接口（CancelIsolateDBInstances）提供批量解除隔离实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "CancelIsolateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelIsolateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBSBackup(
            self,
            request: models.CreateDBSBackupRequest,
            opts: Dict = None,
    ) -> models.CreateDBSBackupResponse:
        """
        创建实例备份集
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBSBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBSBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBSBackupSets(
            self,
            request: models.DeleteDBSBackupSetsRequest,
            opts: Dict = None,
    ) -> models.DeleteDBSBackupSetsResponse:
        """
        删除实例备份集
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBSBackupSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBSBackupSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBillingEnable(
            self,
            request: models.DescribeBillingEnableRequest,
            opts: Dict = None,
    ) -> models.DescribeBillingEnableResponse:
        """
        已无地方调用

        本接口（DescribeBillingEnable）用于查询计费是否开启
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBillingEnable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBillingEnableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBParameters(
            self,
            request: models.DescribeDBParametersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBParametersResponse:
        """
        本接口（DescribeDBParameters）用于获取实例的当前参数设置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSAvailableRecoveryTime(
            self,
            request: models.DescribeDBSAvailableRecoveryTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSAvailableRecoveryTimeResponse:
        """
        可恢复时间查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSAvailableRecoveryTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSAvailableRecoveryTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSCloneInstances(
            self,
            request: models.DescribeDBSCloneInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSCloneInstancesResponse:
        """
        查询实例克隆列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSCloneInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSCloneInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        本接口（DescribeDBSecurityGroups）用于查询实例安全组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseObjects(
            self,
            request: models.DescribeDatabaseObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseObjectsResponse:
        """
        本接口（DescribeDatabaseObjects）用于查询云数据库实例的数据库中的对象列表，包含表、存储过程、视图和函数。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseTable(
            self,
            request: models.DescribeDatabaseTableRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseTableResponse:
        """
        冗余接口，无人调用

        本接口（DescribeDatabaseTable）用于查询云数据库实例的表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlow(
            self,
            request: models.DescribeFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowResponse:
        """
        本接口（DescribeFlow）用于查询异步任务流程状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstances(
            self,
            request: models.DestroyInstancesRequest,
            opts: Dict = None,
    ) -> models.DestroyInstancesResponse:
        """
        本接口（DestroyInstances）提供批量销毁实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBInstance(
            self,
            request: models.IsolateDBInstanceRequest,
            opts: Dict = None,
    ) -> models.IsolateDBInstanceResponse:
        """
        本接口（IsolateDBInstance）提供批量隔离实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        本接口（ModifyAutoRenewFlag）用于修改自动续费标志
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBinlogStatus(
            self,
            request: models.ModifyBinlogStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyBinlogStatusResponse:
        """
        接口功能已被 ModifyInstanceCdc 完全覆盖

        修改binlog状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBinlogStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBinlogStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口（ModifyDBInstanceSecurityGroups）用于修改云数据库安全组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBParameters(
            self,
            request: models.ModifyDBParametersRequest,
            opts: Dict = None,
    ) -> models.ModifyDBParametersResponse:
        """
        本接口（ModifyDBParameters）用于修改实例参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBParameters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBParametersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBSBackupPolicy(
            self,
            request: models.ModifyDBSBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyDBSBackupPolicyResponse:
        """
        修改实例备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBSBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBSBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBSBackupSetComment(
            self,
            request: models.ModifyDBSBackupSetCommentRequest,
            opts: Dict = None,
    ) -> models.ModifyDBSBackupSetCommentResponse:
        """
        修改备份集备注
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBSBackupSetComment"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBSBackupSetCommentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        本接口（ModifyInstanceName）提供修改实例名称功能
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)