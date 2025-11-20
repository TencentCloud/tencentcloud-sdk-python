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
from tencentcloud.cdwdoris.v20211228 import models
from typing import Dict


class CdwdorisClient(AbstractClient):
    _apiVersion = '2021-12-28'
    _endpoint = 'cdwdoris.tencentcloudapi.com'
    _service = 'cdwdoris'

    async def ActionAlterUser(
            self,
            request: models.ActionAlterUserRequest,
            opts: Dict = None,
    ) -> models.ActionAlterUserResponse:
        """
        新增和修改用户接口
        """
        
        kwargs = {}
        kwargs["action"] = "ActionAlterUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActionAlterUserResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CancelBackupJob(
            self,
            request: models.CancelBackupJobRequest,
            opts: Dict = None,
    ) -> models.CancelBackupJobResponse:
        """
        取消对应的备份实例任务
        """
        
        kwargs = {}
        kwargs["action"] = "CancelBackupJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CancelBackupJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckCoolDownWorkingVariableConfigCorrect(
            self,
            request: models.CheckCoolDownWorkingVariableConfigCorrectRequest,
            opts: Dict = None,
    ) -> models.CheckCoolDownWorkingVariableConfigCorrectResponse:
        """
        查询冷热分层生效变量和配置是否正确
        """
        
        kwargs = {}
        kwargs["action"] = "CheckCoolDownWorkingVariableConfigCorrect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckCoolDownWorkingVariableConfigCorrectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackUpSchedule(
            self,
            request: models.CreateBackUpScheduleRequest,
            opts: Dict = None,
    ) -> models.CreateBackUpScheduleResponse:
        """
        创建或者修改备份策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackUpSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackUpScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCoolDownPolicy(
            self,
            request: models.CreateCoolDownPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateCoolDownPolicyResponse:
        """
        创建冷热分层策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCoolDownPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCoolDownPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstanceNew(
            self,
            request: models.CreateInstanceNewRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceNewResponse:
        """
        通过API创建集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkloadGroup(
            self,
            request: models.CreateWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.CreateWorkloadGroupResponse:
        """
        创建资源组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackUpData(
            self,
            request: models.DeleteBackUpDataRequest,
            opts: Dict = None,
    ) -> models.DeleteBackUpDataResponse:
        """
        删除备份数据
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackUpData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackUpDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteWorkloadGroup(
            self,
            request: models.DeleteWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteWorkloadGroupResponse:
        """
        删除资源组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAreaRegion(
            self,
            request: models.DescribeAreaRegionRequest,
            opts: Dict = None,
    ) -> models.DescribeAreaRegionResponse:
        """
        集群列表页上显示地域信息及各个地域的集群总数
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAreaRegion"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAreaRegionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpJob(
            self,
            request: models.DescribeBackUpJobRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpJobResponse:
        """
        查询备份实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpJobDetail(
            self,
            request: models.DescribeBackUpJobDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpJobDetailResponse:
        """
        查询备份任务详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpJobDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpJobDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpSchedules(
            self,
            request: models.DescribeBackUpSchedulesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpSchedulesResponse:
        """
        获取备份、迁移的调度任务信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpSchedules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpSchedulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpTables(
            self,
            request: models.DescribeBackUpTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpTablesResponse:
        """
        获取可备份表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackUpTaskDetail(
            self,
            request: models.DescribeBackUpTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpTaskDetailResponse:
        """
        查询备份任务进度详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterConfigs(
            self,
            request: models.DescribeClusterConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterConfigsResponse:
        """
        获取集群的最新的几个配置文件（config.xml、metrika.xml、user.xml）的内容，显示给用户
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterConfigsHistory(
            self,
            request: models.DescribeClusterConfigsHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterConfigsHistoryResponse:
        """
        获取集群配置文件修改历史
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterConfigsHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterConfigsHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCoolDownBackends(
            self,
            request: models.DescribeCoolDownBackendsRequest,
            opts: Dict = None,
    ) -> models.DescribeCoolDownBackendsResponse:
        """
        查询冷热分层backend节点信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCoolDownBackends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCoolDownBackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCoolDownPolicies(
            self,
            request: models.DescribeCoolDownPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeCoolDownPoliciesResponse:
        """
        查询冷热分层策略列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCoolDownPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCoolDownPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCoolDownTableData(
            self,
            request: models.DescribeCoolDownTableDataRequest,
            opts: Dict = None,
    ) -> models.DescribeCoolDownTableDataResponse:
        """
        查询冷热分层Table数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCoolDownTableData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCoolDownTableDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseAuditDownload(
            self,
            request: models.DescribeDatabaseAuditDownloadRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseAuditDownloadResponse:
        """
        下载数据库审计日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseAuditDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseAuditDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDatabaseAuditRecords(
            self,
            request: models.DescribeDatabaseAuditRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeDatabaseAuditRecordsResponse:
        """
        获取数据库审计记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDatabaseAuditRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDatabaseAuditRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        根据集群ID查询某个集群的具体信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodes(
            self,
            request: models.DescribeInstanceNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesResponse:
        """
        获取集群节点信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodesInfo(
            self,
            request: models.DescribeInstanceNodesInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesInfoResponse:
        """
        获取BE/FE节点角色
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodesInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodesRole(
            self,
            request: models.DescribeInstanceNodesRoleRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesRoleResponse:
        """
        获取集群节点角色
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodesRole"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesRoleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOperations(
            self,
            request: models.DescribeInstanceOperationsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOperationsResponse:
        """
        在集群详情页面，拉取该集群的操作
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOperations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOperationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceState(
            self,
            request: models.DescribeInstanceStateRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceStateResponse:
        """
        集群详情页中显示集群状态、流程进度等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceUsedSubnets(
            self,
            request: models.DescribeInstanceUsedSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceUsedSubnetsResponse:
        """
        获取集群已使用子网信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceUsedSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceUsedSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        获取集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesHealthState(
            self,
            request: models.DescribeInstancesHealthStateRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesHealthStateResponse:
        """
        集群健康检查
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesHealthState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesHealthStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRestoreTaskDetail(
            self,
            request: models.DescribeRestoreTaskDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeRestoreTaskDetailResponse:
        """
        查询恢复任务进度详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRestoreTaskDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRestoreTaskDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryRecords(
            self,
            request: models.DescribeSlowQueryRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryRecordsResponse:
        """
        获取慢查询列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSlowQueryRecordsDownload(
            self,
            request: models.DescribeSlowQueryRecordsDownloadRequest,
            opts: Dict = None,
    ) -> models.DescribeSlowQueryRecordsDownloadResponse:
        """
        下载慢查询文件
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSlowQueryRecordsDownload"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSlowQueryRecordsDownloadResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpec(
            self,
            request: models.DescribeSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecResponse:
        """
        拉取集群节点规格列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSqlApis(
            self,
            request: models.DescribeSqlApisRequest,
            opts: Dict = None,
    ) -> models.DescribeSqlApisResponse:
        """
        针对驱动sql命令查询集群接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSqlApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSqlApisResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableList(
            self,
            request: models.DescribeTableListRequest,
            opts: Dict = None,
    ) -> models.DescribeTableListResponse:
        """
        获取指定数据源和库下的表列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserBindWorkloadGroup(
            self,
            request: models.DescribeUserBindWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeUserBindWorkloadGroupResponse:
        """
        获取当前集群各用户绑定的资源信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserBindWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserBindWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkloadGroup(
            self,
            request: models.DescribeWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkloadGroupResponse:
        """
        获取资源组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstance(
            self,
            request: models.DestroyInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyInstanceResponse:
        """
        销毁集群
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterConfigs(
            self,
            request: models.ModifyClusterConfigsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterConfigsResponse:
        """
        在集群配置页面修改集群配置文件接口，xml模式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCoolDownPolicy(
            self,
            request: models.ModifyCoolDownPolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyCoolDownPolicyResponse:
        """
        修改冷热分层策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCoolDownPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCoolDownPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstance(
            self,
            request: models.ModifyInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceResponse:
        """
        修改集群名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceKeyValConfigs(
            self,
            request: models.ModifyInstanceKeyValConfigsRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceKeyValConfigsResponse:
        """
        KV模式修改配置接口
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceKeyValConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceKeyValConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNodeStatus(
            self,
            request: models.ModifyNodeStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyNodeStatusResponse:
        """
        修改节点状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodeStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodeStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroups(
            self,
            request: models.ModifySecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupsResponse:
        """
        更改安全组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserBindWorkloadGroup(
            self,
            request: models.ModifyUserBindWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyUserBindWorkloadGroupResponse:
        """
        修改用户绑定的资源组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserBindWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserBindWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserPrivilegesV3(
            self,
            request: models.ModifyUserPrivilegesV3Request,
            opts: Dict = None,
    ) -> models.ModifyUserPrivilegesV3Response:
        """
        修改用户权限,支持catalog，全部db，部分db表三种权限设置类别
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserPrivilegesV3"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserPrivilegesV3Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkloadGroup(
            self,
            request: models.ModifyWorkloadGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkloadGroupResponse:
        """
        修改资源组信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkloadGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkloadGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkloadGroupStatus(
            self,
            request: models.ModifyWorkloadGroupStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkloadGroupStatusResponse:
        """
        开启或关闭资源组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkloadGroupStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkloadGroupStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenCoolDown(
            self,
            request: models.OpenCoolDownRequest,
            opts: Dict = None,
    ) -> models.OpenCoolDownResponse:
        """
        开始启用冷热分层
        """
        
        kwargs = {}
        kwargs["action"] = "OpenCoolDown"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenCoolDownResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenCoolDownPolicy(
            self,
            request: models.OpenCoolDownPolicyRequest,
            opts: Dict = None,
    ) -> models.OpenCoolDownPolicyResponse:
        """
        开通、描述降冷策略接口
        """
        
        kwargs = {}
        kwargs["action"] = "OpenCoolDownPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenCoolDownPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverBackUpJob(
            self,
            request: models.RecoverBackUpJobRequest,
            opts: Dict = None,
    ) -> models.RecoverBackUpJobResponse:
        """
        备份恢复
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverBackUpJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverBackUpJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReduceInstance(
            self,
            request: models.ReduceInstanceRequest,
            opts: Dict = None,
    ) -> models.ReduceInstanceResponse:
        """
        集群缩容
        """
        
        kwargs = {}
        kwargs["action"] = "ReduceInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReduceInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeDisk(
            self,
            request: models.ResizeDiskRequest,
            opts: Dict = None,
    ) -> models.ResizeDiskResponse:
        """
        扩容云盘
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartClusterForConfigs(
            self,
            request: models.RestartClusterForConfigsRequest,
            opts: Dict = None,
    ) -> models.RestartClusterForConfigsResponse:
        """
        重启集群让配置文件生效
        """
        
        kwargs = {}
        kwargs["action"] = "RestartClusterForConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartClusterForConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartClusterForNode(
            self,
            request: models.RestartClusterForNodeRequest,
            opts: Dict = None,
    ) -> models.RestartClusterForNodeResponse:
        """
        集群滚动重启
        """
        
        kwargs = {}
        kwargs["action"] = "RestartClusterForNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartClusterForNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        水平扩容节点
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleUpInstance(
            self,
            request: models.ScaleUpInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleUpInstanceResponse:
        """
        计算资源垂直变配
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCoolDown(
            self,
            request: models.UpdateCoolDownRequest,
            opts: Dict = None,
    ) -> models.UpdateCoolDownResponse:
        """
        更新集群冷热分层信息
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCoolDown"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCoolDownResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)