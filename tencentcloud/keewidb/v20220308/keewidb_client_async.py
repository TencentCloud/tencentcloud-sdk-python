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
from tencentcloud.keewidb.v20220308 import models
from typing import Dict


class KeewidbClient(AbstractClient):
    _apiVersion = '2022-03-08'
    _endpoint = 'keewidb.tencentcloudapi.com'
    _service = 'keewidb'

    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        本接口 (AssociateSecurityGroups) 用于安全组批量绑定多个指定实例。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ChangeInstanceMaster(
            self,
            request: models.ChangeInstanceMasterRequest,
            opts: Dict = None,
    ) -> models.ChangeInstanceMasterResponse:
        """
        本接口（ChangeInstanceMaster）用于将副本节点提升为主节点。
        """
        
        kwargs = {}
        kwargs["action"] = "ChangeInstanceMaster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ChangeInstanceMasterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CleanUpInstance(
            self,
            request: models.CleanUpInstanceRequest,
            opts: Dict = None,
    ) -> models.CleanUpInstanceResponse:
        """
        本接口（CleanUpInstance）用于立即下线回收站已隔离的实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CleanUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CleanUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearInstance(
            self,
            request: models.ClearInstanceRequest,
            opts: Dict = None,
    ) -> models.ClearInstanceResponse:
        """
        本接口（ClearInstance）用于清空实例数据。
        > **说明**：在清空数据流程中，系统将自动进行数据备份，耗时较长，请您耐心等待并提前做好时间规划。
        """
        
        kwargs = {}
        kwargs["action"] = "ClearInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupManually(
            self,
            request: models.CreateBackupManuallyRequest,
            opts: Dict = None,
    ) -> models.CreateBackupManuallyResponse:
        """
        手动发起备份
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupManually"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupManuallyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstances(
            self,
            request: models.CreateInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateInstancesResponse:
        """
        创建数据库实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoBackupConfig(
            self,
            request: models.DescribeAutoBackupConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoBackupConfigResponse:
        """
        本接口（DescribeAutoBackupConfig）用于获取自动备份配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConnectionConfig(
            self,
            request: models.DescribeConnectionConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeConnectionConfigResponse:
        """
        本接口（DescribeConnectionConfig）用于查询实例连接配置，包括出流量和入流量带宽、最大连接数限制。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConnectionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConnectionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBSecurityGroups(
            self,
            request: models.DescribeDBSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDBSecurityGroupsResponse:
        """
        本接口(DescribeDBSecurityGroups)用于查询实例的安全组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceBackups(
            self,
            request: models.DescribeInstanceBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceBackupsResponse:
        """
        本接口（DescribeInstanceBackups）用于查询实例全量备份列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceBinlogs(
            self,
            request: models.DescribeInstanceBinlogsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceBinlogsResponse:
        """
        本接口（DescribeInstanceBinlogs）用于查询增量备份列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceBinlogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceBinlogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDealDetail(
            self,
            request: models.DescribeInstanceDealDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDealDetailResponse:
        """
        本接口（DescribeInstanceDealDetail）用于查询预付费订单信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDealDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDealDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodeInfo(
            self,
            request: models.DescribeInstanceNodeInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodeInfoResponse:
        """
        本接口（DescribeInstanceNodeInfo）查询实例节点信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodeInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodeInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParamRecords(
            self,
            request: models.DescribeInstanceParamRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamRecordsResponse:
        """
        本接口（DescribeInstanceParamRecords）查询参数配置修改历史列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParamRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceParams(
            self,
            request: models.DescribeInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceParamsResponse:
        """
        本接口（DescribeInstanceParams）用于查询实例的参数列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceReplicas(
            self,
            request: models.DescribeInstanceReplicasRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceReplicasResponse:
        """
        本接口（DescribeInstanceReplicas）用于获取实例副本节点信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceReplicas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceReplicasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        本接口（DescribeInstances）可以根据地域、网络、实例id、标签、计费方式等条件，搜索查询实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMaintenanceWindow(
            self,
            request: models.DescribeMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.DescribeMaintenanceWindowResponse:
        """
        本接口（DescribeMaintenanceWindow）用于查询实例维护时间窗。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductInfo(
            self,
            request: models.DescribeProductInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeProductInfoResponse:
        """
        本接口查询指定可用区和实例类型下keewidb 的售卖规格， 如果用户不在购买白名单中，将不能查询该可用区或该类型的售卖规格详情。申请购买某地域白名单可以提交工单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProjectSecurityGroups(
            self,
            request: models.DescribeProjectSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeProjectSecurityGroupsResponse:
        """
        本接口(DescribeProjectSecurityGroups)用于查询项目的安全组详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProjectSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProjectSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProxySlowLog(
            self,
            request: models.DescribeProxySlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeProxySlowLogResponse:
        """
        本接口（DescribeProxySlowLog）用于查询代理（Proxy）慢日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProxySlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProxySlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskInfo(
            self,
            request: models.DescribeTaskInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskInfoResponse:
        """
        本接口（DescribeTaskInfo）用于查询异步任务结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskList(
            self,
            request: models.DescribeTaskListRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskListResponse:
        """
        本接口（DescribeTaskList）用于查询任务列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTendisSlowLog(
            self,
            request: models.DescribeTendisSlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeTendisSlowLogResponse:
        """
        本接口（DescribeTendisSlowLog）用于查询实例慢日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTendisSlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTendisSlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPostpaidInstance(
            self,
            request: models.DestroyPostpaidInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPostpaidInstanceResponse:
        """
        本接口（DestroyPostpaidInstance）用于退还按量计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPostpaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPostpaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyPrepaidInstance(
            self,
            request: models.DestroyPrepaidInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyPrepaidInstanceResponse:
        """
        本接口（DestroyPrepaidInstance）用于退还包年包月计费实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyPrepaidInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyPrepaidInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        本接口(DisassociateSecurityGroups)用于安全组批量解绑实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoBackupConfig(
            self,
            request: models.ModifyAutoBackupConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoBackupConfigResponse:
        """
        本接口（ModifyAutoBackupConfig）用于修改自动备份配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoBackupConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoBackupConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyConnectionConfig(
            self,
            request: models.ModifyConnectionConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyConnectionConfigResponse:
        """
        本接口（ModifyConnectionConfig）用于修改实例的连接配置，包括带宽和最大连接数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyConnectionConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyConnectionConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBInstanceSecurityGroups(
            self,
            request: models.ModifyDBInstanceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBInstanceSecurityGroupsResponse:
        """
        本接口(ModifyDBInstanceSecurityGroups)用于修改实例绑定的安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBInstanceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBInstanceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        本接口（ModifyInstance）用于修改实例相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceParams(
            self,
            request: models.ModifyInstanceParamsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceParamsResponse:
        """
        本接口（ModifyInstanceParams）用于修改实例参数配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceParams"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceParamsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyMaintenanceWindow(
            self,
            request: models.ModifyMaintenanceWindowRequest,
            opts: Dict = None,
    ) -> models.ModifyMaintenanceWindowResponse:
        """
        本接口（ModifyMaintenanceWindow）修改实例维护时间窗时间。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyMaintenanceWindow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyMaintenanceWindowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkConfig(
            self,
            request: models.ModifyNetworkConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkConfigResponse:
        """
        本接口（ModifyNetworkConfig）用于修改实例网络配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewInstance(
            self,
            request: models.RenewInstanceRequest,
            opts: Dict = None,
    ) -> models.RenewInstanceResponse:
        """
        本接口（RenewInstance）用于为包年包月计费实例续费。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetPassword(
            self,
            request: models.ResetPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetPasswordResponse:
        """
        本接口（ResetPassword）用于重置数据库访问密码。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartUpInstance(
            self,
            request: models.StartUpInstanceRequest,
            opts: Dict = None,
    ) -> models.StartUpInstanceResponse:
        """
        本接口（StartUpInstance）用于按量计费实例解隔离
        """
        
        kwargs = {}
        kwargs["action"] = "StartUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeInstance(
            self,
            request: models.UpgradeInstanceRequest,
            opts: Dict = None,
    ) -> models.UpgradeInstanceResponse:
        """
        本接口（UpgradeInstance）用于对实例进行配置变更。
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)