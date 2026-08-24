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
from tencentcloud.bdrc.v20260330 import models
from typing import Dict


class BdrcClient(AbstractClient):
    _apiVersion = '2026-03-30'
    _endpoint = 'bdrc.tencentcloudapi.com'
    _service = 'bdrc'

    async def ApplyBackupGroup(
            self,
            request: models.ApplyBackupGroupRequest,
            opts: Dict = None,
    ) -> models.ApplyBackupGroupResponse:
        """
        回滚备份组
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyBackupGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyBackupGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindAutoBackupPolicy(
            self,
            request: models.BindAutoBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.BindAutoBackupPolicyResponse:
        """
        将实例绑定到备份策略上
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoBackupPolicy(
            self,
            request: models.CreateAutoBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoBackupPolicyResponse:
        """
        创建备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupGroup(
            self,
            request: models.CreateBackupGroupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupGroupResponse:
        """
        创建备份组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackupVault(
            self,
            request: models.CreateBackupVaultRequest,
            opts: Dict = None,
    ) -> models.CreateBackupVaultResponse:
        """
        创建备份库
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackupVault"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupVaultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisasterRecoveryProtectGroup(
            self,
            request: models.CreateDisasterRecoveryProtectGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDisasterRecoveryProtectGroupResponse:
        """
        本接口用于创建容灾保护组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisasterRecoveryProtectGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisasterRecoveryProtectGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisasterRecoverySitePair(
            self,
            request: models.CreateDisasterRecoverySitePairRequest,
            opts: Dict = None,
    ) -> models.CreateDisasterRecoverySitePairResponse:
        """
        创建容灾站点对
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisasterRecoverySitePair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisasterRecoverySitePairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisasterRecoveryVpcMapping(
            self,
            request: models.CreateDisasterRecoveryVpcMappingRequest,
            opts: Dict = None,
    ) -> models.CreateDisasterRecoveryVpcMappingResponse:
        """
        本接口用于创建容灾站点VPC网络映射
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisasterRecoveryVpcMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisasterRecoveryVpcMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileBackup(
            self,
            request: models.CreateFileBackupRequest,
            opts: Dict = None,
    ) -> models.CreateFileBackupResponse:
        """
        本接口用于创建文件备份点
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileBackupPlan(
            self,
            request: models.CreateFileBackupPlanRequest,
            opts: Dict = None,
    ) -> models.CreateFileBackupPlanResponse:
        """
        本接口用于创建备份计划
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFileRestoreTask(
            self,
            request: models.CreateFileRestoreTaskRequest,
            opts: Dict = None,
    ) -> models.CreateFileRestoreTaskResponse:
        """
        创建恢复任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFileRestoreTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFileRestoreTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceCopyPair(
            self,
            request: models.CreateInstanceCopyPairRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceCopyPairResponse:
        """
        本接口用于创建CVM复制对
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceCopyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceCopyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceDrillPairs(
            self,
            request: models.CreateInstanceDrillPairsRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceDrillPairsResponse:
        """
        创建cvm演练
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceDrillPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceDrillPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupMapping(
            self,
            request: models.CreateSecurityGroupMappingRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupMappingResponse:
        """
        本接口用于为站点对新增安全组映射，生产端实例绑定的安全组为源端，需要为每个生产端实例绑定的安全组建立映射，在创建复制对时，会自动以映射后的目标安全组作为容灾端实例绑定的安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoBackupPolicies(
            self,
            request: models.DeleteAutoBackupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoBackupPoliciesResponse:
        """
        删除备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoBackupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoBackupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupGroups(
            self,
            request: models.DeleteBackupGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupGroupsResponse:
        """
        删除备份组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupVaults(
            self,
            request: models.DeleteBackupVaultsRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupVaultsResponse:
        """
        删除备份库
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupVaults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupVaultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCopyPairs(
            self,
            request: models.DeleteCopyPairsRequest,
            opts: Dict = None,
    ) -> models.DeleteCopyPairsResponse:
        """
        本接口用于删除容灾复制对
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCopyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCopyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDisasterRecoveryProtectGroups(
            self,
            request: models.DeleteDisasterRecoveryProtectGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteDisasterRecoveryProtectGroupsResponse:
        """
        本接口用于删除容灾保护组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDisasterRecoveryProtectGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDisasterRecoveryProtectGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDisasterRecoverySitePairs(
            self,
            request: models.DeleteDisasterRecoverySitePairsRequest,
            opts: Dict = None,
    ) -> models.DeleteDisasterRecoverySitePairsResponse:
        """
        删除容灾站点对
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDisasterRecoverySitePairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDisasterRecoverySitePairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDisasterRecoveryVpcMapping(
            self,
            request: models.DeleteDisasterRecoveryVpcMappingRequest,
            opts: Dict = None,
    ) -> models.DeleteDisasterRecoveryVpcMappingResponse:
        """
        本接口用于删除容灾站点对vpc映射信息
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDisasterRecoveryVpcMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDisasterRecoveryVpcMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDrillPairs(
            self,
            request: models.DeleteDrillPairsRequest,
            opts: Dict = None,
    ) -> models.DeleteDrillPairsResponse:
        """
        删除演练对/演练组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDrillPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDrillPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileBackupPlans(
            self,
            request: models.DeleteFileBackupPlansRequest,
            opts: Dict = None,
    ) -> models.DeleteFileBackupPlansResponse:
        """
        删除备份计划
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFileBackups(
            self,
            request: models.DeleteFileBackupsRequest,
            opts: Dict = None,
    ) -> models.DeleteFileBackupsResponse:
        """
        删除文件备份点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFileBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFileBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroupMapping(
            self,
            request: models.DeleteSecurityGroupMappingRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupMappingResponse:
        """
        本接口用于删除站点对已添加的安全组映射
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupMapping"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupMappingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoBackupPolicies(
            self,
            request: models.DescribeAutoBackupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoBackupPoliciesResponse:
        """
        查询定期备份策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoBackupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoBackupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupGroupRollbackTasks(
            self,
            request: models.DescribeBackupGroupRollbackTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupGroupRollbackTasksResponse:
        """
        查询备份组恢复任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupGroupRollbackTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupGroupRollbackTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupGroups(
            self,
            request: models.DescribeBackupGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupGroupsResponse:
        """
        查询备份组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupGroupsDeniedActions(
            self,
            request: models.DescribeBackupGroupsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupGroupsDeniedActionsResponse:
        """
        查询操作掩码
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupGroupsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupGroupsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupInstances(
            self,
            request: models.DescribeBackupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupInstancesResponse:
        """
        本接口用来浏览已有受保护实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupOverviewGeneral(
            self,
            request: models.DescribeBackupOverviewGeneralRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupOverviewGeneralResponse:
        """
        查询备份概览信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupOverviewGeneral"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupOverviewGeneralResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupPlans(
            self,
            request: models.DescribeBackupPlansRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupPlansResponse:
        """
        查询整机备份计划
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupVaults(
            self,
            request: models.DescribeBackupVaultsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupVaultsResponse:
        """
        查询备份库信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupVaults"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupVaultsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupVaultsDeniedActions(
            self,
            request: models.DescribeBackupVaultsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupVaultsDeniedActionsResponse:
        """
        查询备份库操作掩码
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupVaultsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupVaultsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCommonBackupPoints(
            self,
            request: models.DescribeCommonBackupPointsRequest,
            opts: Dict = None,
    ) -> models.DescribeCommonBackupPointsResponse:
        """
        查询共同备份点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCommonBackupPoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCommonBackupPointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCopyPairs(
            self,
            request: models.DescribeCopyPairsRequest,
            opts: Dict = None,
    ) -> models.DescribeCopyPairsResponse:
        """
        本接口用来查询容灾复制对
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCopyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCopyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCopyPairsDeniedActions(
            self,
            request: models.DescribeCopyPairsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeCopyPairsDeniedActionsResponse:
        """
        查询复制对掩码
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCopyPairsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCopyPairsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoveryDrillGroups(
            self,
            request: models.DescribeDisasterRecoveryDrillGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoveryDrillGroupsResponse:
        """
        本接口用来查询容灾复制对
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoveryDrillGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoveryDrillGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoveryOverview(
            self,
            request: models.DescribeDisasterRecoveryOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoveryOverviewResponse:
        """
        查询容灾资源概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoveryOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoveryOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoveryProtectGroups(
            self,
            request: models.DescribeDisasterRecoveryProtectGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoveryProtectGroupsResponse:
        """
        本接口用来查询容灾保护组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoveryProtectGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoveryProtectGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoverySitePairs(
            self,
            request: models.DescribeDisasterRecoverySitePairsRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoverySitePairsResponse:
        """
        本接口用来查询容灾站点对
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoverySitePairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoverySitePairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoverySitePairsDeniedActions(
            self,
            request: models.DescribeDisasterRecoverySitePairsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoverySitePairsDeniedActionsResponse:
        """
        查询指定容灾站点对当前不允许执行的操作列表（操作掩码）。前端在展示容灾策略操作菜单时，可基于该接口返回结果灰化或屏蔽相应入口，并向用户提示原因（错误码 + 错误信息）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoverySitePairsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoverySitePairsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisasterRecoverySupportRegion(
            self,
            request: models.DescribeDisasterRecoverySupportRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeDisasterRecoverySupportRegionResponse:
        """
        查询当前地域支持容灾的生产地域配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisasterRecoverySupportRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisasterRecoverySupportRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisks(
            self,
            request: models.DescribeDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksResponse:
        """
        本接口用来查询容灾云硬盘的详情，如系统盘的镜像格式。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDrillPairs(
            self,
            request: models.DescribeDrillPairsRequest,
            opts: Dict = None,
    ) -> models.DescribeDrillPairsResponse:
        """
        查询演练对列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrillPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrillPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDrillPairsDeniedActions(
            self,
            request: models.DescribeDrillPairsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeDrillPairsDeniedActionsResponse:
        """
        查询演练操作掩码
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDrillPairsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDrillPairsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileBackupObjects(
            self,
            request: models.DescribeFileBackupObjectsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileBackupObjectsResponse:
        """
        本接口用来浏览已有备份目录/文件内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileBackupObjects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileBackupObjectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileBackupPlans(
            self,
            request: models.DescribeFileBackupPlansRequest,
            opts: Dict = None,
    ) -> models.DescribeFileBackupPlansResponse:
        """
        本接口用来浏览已有备份计划内容
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileBackupPlans"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileBackupPlansResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileBackups(
            self,
            request: models.DescribeFileBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileBackupsResponse:
        """
        本接口用来浏览已有备份点详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileBackupsDeniedActions(
            self,
            request: models.DescribeFileBackupsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeFileBackupsDeniedActionsResponse:
        """
        本接口用来查询备份操作掩码
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileBackupsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileBackupsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFileRestoreTasks(
            self,
            request: models.DescribeFileRestoreTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeFileRestoreTasksResponse:
        """
        查询备份恢复任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFileRestoreTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFileRestoreTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        本接口用于Agent查询相关Agent任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePriceCreateCopyPairs(
            self,
            request: models.DescribePriceCreateCopyPairsRequest,
            opts: Dict = None,
    ) -> models.DescribePriceCreateCopyPairsResponse:
        """
        本接口（DescribePriceCreateCopyPairs）用于查询创建容灾复制对的价格。支持批量询价，入参为每个复制对的盘容量数组，返回与入参一一对应的后付费每小时价格。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePriceCreateCopyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePriceCreateCopyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectGroupsDeniedActions(
            self,
            request: models.DescribeProtectGroupsDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectGroupsDeniedActionsResponse:
        """
        查询保护组操作掩码
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectGroupsDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectGroupsDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProtectedInstances(
            self,
            request: models.DescribeProtectedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeProtectedInstancesResponse:
        """
        本接口用来浏览已有受保护实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProtectedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProtectedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupMappings(
            self,
            request: models.DescribeSecurityGroupMappingsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupMappingsResponse:
        """
        本接口用于查询安全组映射列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupMappings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupMappingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcMappings(
            self,
            request: models.DescribeVpcMappingsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcMappingsResponse:
        """
        本接口用来查询站点对的vpc映射信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcMappings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcMappingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def FinishFailoverCopyPairs(
            self,
            request: models.FinishFailoverCopyPairsRequest,
            opts: Dict = None,
    ) -> models.FinishFailoverCopyPairsResponse:
        """
        完成切换
        """
        
        kwargs = {}
        kwargs["action"] = "FinishFailoverCopyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.FinishFailoverCopyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoBackupPolicyAttribute(
            self,
            request: models.ModifyAutoBackupPolicyAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoBackupPolicyAttributeResponse:
        """
        修改备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoBackupPolicyAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoBackupPolicyAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupAttribute(
            self,
            request: models.ModifyBackupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupAttributeResponse:
        """
        删除备份组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBackupVaultAttribute(
            self,
            request: models.ModifyBackupVaultAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyBackupVaultAttributeResponse:
        """
        修改备份库信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBackupVaultAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBackupVaultAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCopyPairAttribute(
            self,
            request: models.ModifyCopyPairAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCopyPairAttributeResponse:
        """
        修改容灾复制对
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCopyPairAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCopyPairAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDrillGroupAttribute(
            self,
            request: models.ModifyDrillGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDrillGroupAttributeResponse:
        """
        修改演练组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDrillGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDrillGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDrillPairAttribute(
            self,
            request: models.ModifyDrillPairAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDrillPairAttributeResponse:
        """
        修改演练
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDrillPairAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDrillPairAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileBackupAttribute(
            self,
            request: models.ModifyFileBackupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyFileBackupAttributeResponse:
        """
        修改文件备份信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileBackupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileBackupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileBackupPlan(
            self,
            request: models.ModifyFileBackupPlanRequest,
            opts: Dict = None,
    ) -> models.ModifyFileBackupPlanResponse:
        """
        本接口用于修改已有的备份计划配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileBackupPlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileBackupPlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyProtectGroupAttribute(
            self,
            request: models.ModifyProtectGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyProtectGroupAttributeResponse:
        """
        修改容灾保护组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyProtectGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyProtectGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySitePairAttribute(
            self,
            request: models.ModifySitePairAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySitePairAttributeResponse:
        """
        修改容灾站点对
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySitePairAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySitePairAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportAgentMetrics(
            self,
            request: models.ReportAgentMetricsRequest,
            opts: Dict = None,
    ) -> models.ReportAgentMetricsResponse:
        """
        本接口用于上报Agent指标信息
        """
        
        kwargs = {}
        kwargs["action"] = "ReportAgentMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportAgentMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportGatewayHeartbeat(
            self,
            request: models.ReportGatewayHeartbeatRequest,
            opts: Dict = None,
    ) -> models.ReportGatewayHeartbeatResponse:
        """
        本接口用于Agent心跳上报
        """
        
        kwargs = {}
        kwargs["action"] = "ReportGatewayHeartbeat"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportGatewayHeartbeatResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReportJobProgress(
            self,
            request: models.ReportJobProgressRequest,
            opts: Dict = None,
    ) -> models.ReportJobProgressResponse:
        """
        本接口用于上报Agent任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "ReportJobProgress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReportJobProgressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunCopyPairTasks(
            self,
            request: models.RunCopyPairTasksRequest,
            opts: Dict = None,
    ) -> models.RunCopyPairTasksResponse:
        """
        启动复制对
        """
        
        kwargs = {}
        kwargs["action"] = "RunCopyPairTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunCopyPairTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunFailoverCopyPairs(
            self,
            request: models.RunFailoverCopyPairsRequest,
            opts: Dict = None,
    ) -> models.RunFailoverCopyPairsResponse:
        """
        故障切换
        """
        
        kwargs = {}
        kwargs["action"] = "RunFailoverCopyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunFailoverCopyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunInstancesWithBackupGroup(
            self,
            request: models.RunInstancesWithBackupGroupRequest,
            opts: Dict = None,
    ) -> models.RunInstancesWithBackupGroupResponse:
        """
        备份组新建云服务器
        """
        
        kwargs = {}
        kwargs["action"] = "RunInstancesWithBackupGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunInstancesWithBackupGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopCopyPairTasks(
            self,
            request: models.StopCopyPairTasksRequest,
            opts: Dict = None,
    ) -> models.StopCopyPairTasksResponse:
        """
        停止复制对
        """
        
        kwargs = {}
        kwargs["action"] = "StopCopyPairTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopCopyPairTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoBackupPolicy(
            self,
            request: models.UnbindAutoBackupPolicyRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoBackupPolicyResponse:
        """
        将实例从备份策略上解绑
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoBackupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoBackupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)