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
        
    async def CreateCloneInstance(
            self,
            request: models.CreateCloneInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCloneInstanceResponse:
        """
        本接口（CreateCloneInstance）提供创建克隆实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloneInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloneInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBInstances(
            self,
            request: models.CreateDBInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateDBInstancesResponse:
        """
        本接口（CreateDBInstances）提供批量创建实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBSBackup(
            self,
            request: models.CreateDBSBackupRequest,
            opts: Dict = None,
    ) -> models.CreateDBSBackupResponse:
        """
        创建实例手工备份  CreateDBSBackup
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBSBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBSBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateUsers(
            self,
            request: models.CreateUsersRequest,
            opts: Dict = None,
    ) -> models.CreateUsersResponse:
        """
        本接口（CreateUsers）用于批量创建用户
        """
        
        kwargs = {}
        kwargs["action"] = "CreateUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDBSBackupSets(
            self,
            request: models.DeleteDBSBackupSetsRequest,
            opts: Dict = None,
    ) -> models.DeleteDBSBackupSetsResponse:
        """
        删除实例手工备份 DeleteDBSBackupSets
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDBSBackupSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDBSBackupSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUsers(
            self,
            request: models.DeleteUsersRequest,
            opts: Dict = None,
    ) -> models.DeleteUsersResponse:
        """
        本接口（DeleteUsers）用于批量删除用户
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUsersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstanceDetail(
            self,
            request: models.DescribeDBInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstanceDetailResponse:
        """
        本接口（DescribeDBInstanceDetail）提供查询实例详情功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口（DescribeDBInstances）提供查询实例列表功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
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
        
    async def DescribeDBSArchiveLogs(
            self,
            request: models.DescribeDBSArchiveLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSArchiveLogsResponse:
        """
        查询实例归档日志列表 DescribeDBSArchiveLogs
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSArchiveLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSArchiveLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSAvailableRecoveryTime(
            self,
            request: models.DescribeDBSAvailableRecoveryTimeRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSAvailableRecoveryTimeResponse:
        """
        获取可恢复时间 DescribeDBSAvailableRecoveryTime
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSAvailableRecoveryTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSAvailableRecoveryTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupPolicy(
            self,
            request: models.DescribeDBSBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupPolicyResponse:
        """
        查询实例备份策略 DescribeDBSBackupPolicy
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupSets(
            self,
            request: models.DescribeDBSBackupSetsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupSetsResponse:
        """
        查询实例备份集信息 DescribeDBSBackupSets
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupSets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupSetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupStatistics(
            self,
            request: models.DescribeDBSBackupStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupStatisticsResponse:
        """
        查询实例备份空间概览 DescribeDBSBackupStatistics
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSBackupStatisticsDetail(
            self,
            request: models.DescribeDBSBackupStatisticsDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSBackupStatisticsDetailResponse:
        """
        查询备份集统计详情 DescribeDBSBackupStatisticsDetail
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSBackupStatisticsDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSBackupStatisticsDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSCloneInstances(
            self,
            request: models.DescribeDBSCloneInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSCloneInstancesResponse:
        """
        查询实例克隆列表 DescribeDBSCloneInstances
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
        
    async def DescribeDatabases(
            self,
            request: models.DescribeDatabasesRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabasesResponse:
        """
        本接口（DescribeDatabases）用于查询云数据库实例的数据库列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabases"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabasesResponse
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
        
    async def DescribeInstanceSSLStatus(
            self,
            request: models.DescribeInstanceSSLStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceSSLStatusResponse:
        """
        本接口（DescribeInstanceSSLStatus）提供实例SSL状态查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceWindow(
            self,
            request: models.DescribeMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceWindowResponse:
        """
        查询维护时间窗口配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSaleInfo(
            self,
            request: models.DescribeSaleInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeSaleInfoResponse:
        """
        本接口（DescribeSaleInfo）提供查询可用售卖地域功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSaleInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSaleInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowLogs(
            self,
            request: models.DescribeSlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowLogsResponse:
        """
        本接口提供查询慢日志功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecs(
            self,
            request: models.DescribeSpecsRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecsResponse:
        """
        本接口（DescribeSpecs）提供查询售卖规格功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserPrivileges(
            self,
            request: models.DescribeUserPrivilegesRequest,
            opts: Dict = None,
    ) -> models.DescribeUserPrivilegesResponse:
        """
        本接口（DescribeUserPrivileges）提供查询用户的权限功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsers(
            self,
            request: models.DescribeUsersRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersResponse:
        """
        本接口（DescribeUsers）提供查询用户列表功能
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersResponse
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
        
    async def ExpandInstance(
            self,
            request: models.ExpandInstanceRequest,
            opts: Dict = None,
    ) -> models.ExpandInstanceResponse:
        """
        本接口（ExpandInstance）提供横向扩容实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "ExpandInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ExpandInstanceResponse
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
        
    async def ModifyDBInstanceVPort(
            self,
            request: models.ModifyDBInstanceVPortRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceVPortResponse:
        """
        本接口(ModifyDBInstanceVPort)修改实例VPC端口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceVPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceVPortResponse
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
        修改实例备份策略 ModifyDBSBackupPolicy
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
        修改实例备份备注 ModifyDBSBackupSetComment
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
        
    async def ModifyInstanceNetwork(
            self,
            request: models.ModifyInstanceNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNetworkResponse:
        """
        本接口（ModifyInstanceNetwork）用于修改实例所属网络
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceSSLStatus(
            self,
            request: models.ModifyInstanceSSLStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceSSLStatusResponse:
        """
        本接口（ModifyInstanceSSLStatus）提供开关实例SSL的功能
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceSSLStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceSSLStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceWindow(
            self,
            request: models.ModifyMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceWindowResponse:
        """
        新增/修改实例维护时间窗口配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserPrivileges(
            self,
            request: models.ModifyUserPrivilegesRequest,
            opts: Dict = None,
    ) -> models.ModifyUserPrivilegesResponse:
        """
        本接口(ModifyPrivileges)修改用户权限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserPrivileges"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserPrivilegesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetUserPassword(
            self,
            request: models.ResetUserPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetUserPasswordResponse:
        """
        本接口（ResetUserPassword）提供重置用户密码功能
        """
        
        kwargs = {}
        kwargs["action"] = "ResetUserPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetUserPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartDBInstances(
            self,
            request: models.RestartDBInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartDBInstancesResponse:
        """
        本接口（RestartDBInstances）用于重启数据库实例
        """
        
        kwargs = {}
        kwargs["action"] = "RestartDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        本接口（UpgradeInstance）提供纵向扩容实例功能
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)