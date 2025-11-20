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
from tencentcloud.cfs.v20190719 import models
from typing import Dict


class CfsClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'cfs.tencentcloudapi.com'
    _service = 'cfs'

    async def ApplyPathLifecyclePolicy(
            self,
            request: models.ApplyPathLifecyclePolicyRequest,
            opts: Dict = None,
    ) -> models.ApplyPathLifecyclePolicyResponse:
        """
        配置生命周期策略关联到的目录列表
        """
        
        kwargs = {}
        kwargs["action"] = "ApplyPathLifecyclePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ApplyPathLifecyclePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindAutoSnapshotPolicy(
            self,
            request: models.BindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.BindAutoSnapshotPolicyResponse:
        """
        文件系统绑定快照策略，可以同时绑定多个fs，一个fs 只能跟一个策略绑定
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAccessCert(
            self,
            request: models.CreateAccessCertRequest,
            opts: Dict = None,
    ) -> models.CreateAccessCertResponse:
        """
        创建用于访问文件系统的凭证
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAccessCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAccessCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAutoSnapshotPolicy(
            self,
            request: models.CreateAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.CreateAutoSnapshotPolicyResponse:
        """
        创建定期快照策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsFileSystem(
            self,
            request: models.CreateCfsFileSystemRequest,
            opts: Dict = None,
    ) -> models.CreateCfsFileSystemResponse:
        """
        用于添加新文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsPGroup(
            self,
            request: models.CreateCfsPGroupRequest,
            opts: Dict = None,
    ) -> models.CreateCfsPGroupResponse:
        """
        本接口（CreateCfsPGroup）用于创建权限组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsRule(
            self,
            request: models.CreateCfsRuleRequest,
            opts: Dict = None,
    ) -> models.CreateCfsRuleResponse:
        """
        本接口（CreateCfsRule）用于创建权限组规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCfsSnapshot(
            self,
            request: models.CreateCfsSnapshotRequest,
            opts: Dict = None,
    ) -> models.CreateCfsSnapshotResponse:
        """
        创建文件系统快照
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCfsSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCfsSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDataFlow(
            self,
            request: models.CreateDataFlowRequest,
            opts: Dict = None,
    ) -> models.CreateDataFlowResponse:
        """
        创建数据流动接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifecycleDataTask(
            self,
            request: models.CreateLifecycleDataTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLifecycleDataTaskResponse:
        """
        支持主动沉降/预热接口
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifecycleDataTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifecycleDataTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifecyclePolicy(
            self,
            request: models.CreateLifecyclePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateLifecyclePolicyResponse:
        """
        创建文件存储生命周期策略
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifecyclePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifecyclePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLifecyclePolicyDownloadTask(
            self,
            request: models.CreateLifecyclePolicyDownloadTaskRequest,
            opts: Dict = None,
    ) -> models.CreateLifecyclePolicyDownloadTaskResponse:
        """
        下载生命周期任务中文件列表
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLifecyclePolicyDownloadTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLifecyclePolicyDownloadTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateMigrationTask(
            self,
            request: models.CreateMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.CreateMigrationTaskResponse:
        """
        用于创建迁移任务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoSnapshotPolicy(
            self,
            request: models.DeleteAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoSnapshotPolicyResponse:
        """
        删除快照定期策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsFileSystem(
            self,
            request: models.DeleteCfsFileSystemRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsFileSystemResponse:
        """
        用于删除文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsPGroup(
            self,
            request: models.DeleteCfsPGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsPGroupResponse:
        """
        本接口（DeleteCfsPGroup）用于删除权限组，只有未绑定文件系统的权限组才能够被此接口删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsRule(
            self,
            request: models.DeleteCfsRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsRuleResponse:
        """
        本接口（DeleteCfsRule）用于删除权限组规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCfsSnapshot(
            self,
            request: models.DeleteCfsSnapshotRequest,
            opts: Dict = None,
    ) -> models.DeleteCfsSnapshotResponse:
        """
        删除文件系统快照
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCfsSnapshot"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCfsSnapshotResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDataFlow(
            self,
            request: models.DeleteDataFlowRequest,
            opts: Dict = None,
    ) -> models.DeleteDataFlowResponse:
        """
        删除数据流动
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLifecyclePolicy(
            self,
            request: models.DeleteLifecyclePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteLifecyclePolicyResponse:
        """
        删除生命周期管理策略
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLifecyclePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLifecyclePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteMigrationTask(
            self,
            request: models.DeleteMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.DeleteMigrationTaskResponse:
        """
        用于删除迁移任务。不支持删除等待中、创建中、运行中、取消中、终止中状态的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserQuota(
            self,
            request: models.DeleteUserQuotaRequest,
            opts: Dict = None,
    ) -> models.DeleteUserQuotaResponse:
        """
        指定条件删除文件系统配额（仅部分Turbo实例能使用，若需要调用请提交工单与我们联系）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoSnapshotPolicies(
            self,
            request: models.DescribeAutoSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoSnapshotPoliciesResponse:
        """
        查询文件系统快照定期策略列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAvailableZoneInfo(
            self,
            request: models.DescribeAvailableZoneInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeAvailableZoneInfoResponse:
        """
        本接口（DescribeAvailableZoneInfo）用于查询区域的可用情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAvailableZoneInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAvailableZoneInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBucketList(
            self,
            request: models.DescribeBucketListRequest,
            opts: Dict = None,
    ) -> models.DescribeBucketListResponse:
        """
        用于获取数据源桶列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBucketList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBucketListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsFileSystemClients(
            self,
            request: models.DescribeCfsFileSystemClientsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsFileSystemClientsResponse:
        """
        查询挂载该文件系统的客户端。此功能需要客户端安装CFS监控插件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsFileSystemClients"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsFileSystemClientsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsFileSystems(
            self,
            request: models.DescribeCfsFileSystemsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsFileSystemsResponse:
        """
        本接口（DescribeCfsFileSystems）用于查询文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsFileSystems"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsFileSystemsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsPGroups(
            self,
            request: models.DescribeCfsPGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsPGroupsResponse:
        """
        本接口（DescribeCfsPGroups）用于查询权限组列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsPGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsPGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsRules(
            self,
            request: models.DescribeCfsRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsRulesResponse:
        """
        本接口（DescribeCfsRules）用于查询权限组规则列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsServiceStatus(
            self,
            request: models.DescribeCfsServiceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsServiceStatusResponse:
        """
        本接口（DescribeCfsServiceStatus）用于查询用户使用CFS的服务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsServiceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsServiceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsSnapshotOverview(
            self,
            request: models.DescribeCfsSnapshotOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsSnapshotOverviewResponse:
        """
        文件系统快照概览
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsSnapshotOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsSnapshotOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCfsSnapshots(
            self,
            request: models.DescribeCfsSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeCfsSnapshotsResponse:
        """
        查询文件系统快照列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCfsSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCfsSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDataFlow(
            self,
            request: models.DescribeDataFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeDataFlowResponse:
        """
        查询数据流动信息接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLifecycleDataTask(
            self,
            request: models.DescribeLifecycleDataTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeLifecycleDataTaskResponse:
        """
        查询生命周期任务的接口。仅支持查询最近三个月内的任务数据。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLifecycleDataTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLifecycleDataTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLifecyclePolicies(
            self,
            request: models.DescribeLifecyclePoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeLifecyclePoliciesResponse:
        """
        查询生命周期管理策略
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLifecyclePolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLifecyclePoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMigrationTasks(
            self,
            request: models.DescribeMigrationTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeMigrationTasksResponse:
        """
        用于获取迁移任务列表。
        此接口需提交工单，开启白名单之后才能使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMigrationTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMigrationTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMountTargets(
            self,
            request: models.DescribeMountTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeMountTargetsResponse:
        """
        本接口（DescribeMountTargets）用于查询文件系统挂载点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMountTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMountTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotOperationLogs(
            self,
            request: models.DescribeSnapshotOperationLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotOperationLogsResponse:
        """
        查询快照操作日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotOperationLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotOperationLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUserQuota(
            self,
            request: models.DescribeUserQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeUserQuotaResponse:
        """
        查询文件系统配额（仅部分Turbo实例能使用，若需要调用请提交工单与我们联系）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUserQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUserQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DoDirectoryOperation(
            self,
            request: models.DoDirectoryOperationRequest,
            opts: Dict = None,
    ) -> models.DoDirectoryOperationResponse:
        """
        文件系统目录操作接口
        """
        
        kwargs = {}
        kwargs["action"] = "DoDirectoryOperation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DoDirectoryOperationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDataFlow(
            self,
            request: models.ModifyDataFlowRequest,
            opts: Dict = None,
    ) -> models.ModifyDataFlowResponse:
        """
        修改数据流动相关参数
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFileSystemAutoScaleUpRule(
            self,
            request: models.ModifyFileSystemAutoScaleUpRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyFileSystemAutoScaleUpRuleResponse:
        """
        用来设置文件系统扩容策略，该接口只支持turbo文件系统
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFileSystemAutoScaleUpRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFileSystemAutoScaleUpRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLifecyclePolicy(
            self,
            request: models.ModifyLifecyclePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyLifecyclePolicyResponse:
        """
        更新文件存储生命周期策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLifecyclePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLifecyclePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleUpFileSystem(
            self,
            request: models.ScaleUpFileSystemRequest,
            opts: Dict = None,
    ) -> models.ScaleUpFileSystemResponse:
        """
        该接口用于对turbo 文件系统扩容使用,该接口只支持扩容不支持缩容。turbo标准型扩容步长是10240GIB，turbo性能型扩容步长是5120GIB
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpFileSystem"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpFileSystemResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetUserQuota(
            self,
            request: models.SetUserQuotaRequest,
            opts: Dict = None,
    ) -> models.SetUserQuotaResponse:
        """
        设置文件系统配额，提供UID/GID的配额设置的接口（仅部分Turbo实例能使用，若需要调用请提交工单与我们联系）
        """
        
        kwargs = {}
        kwargs["action"] = "SetUserQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetUserQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SignUpCfsService(
            self,
            request: models.SignUpCfsServiceRequest,
            opts: Dict = None,
    ) -> models.SignUpCfsServiceResponse:
        """
        本接口（SignUpCfsService）用于开通CFS服务。
        """
        
        kwargs = {}
        kwargs["action"] = "SignUpCfsService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SignUpCfsServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopLifecycleDataTask(
            self,
            request: models.StopLifecycleDataTaskRequest,
            opts: Dict = None,
    ) -> models.StopLifecycleDataTaskResponse:
        """
        终止生命周期任务的接口
        """
        
        kwargs = {}
        kwargs["action"] = "StopLifecycleDataTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopLifecycleDataTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopMigrationTask(
            self,
            request: models.StopMigrationTaskRequest,
            opts: Dict = None,
    ) -> models.StopMigrationTaskResponse:
        """
        用于终止迁移任务，可以终止等待中、运行中状态的任务。
        """
        
        kwargs = {}
        kwargs["action"] = "StopMigrationTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopMigrationTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindAutoSnapshotPolicy(
            self,
            request: models.UnbindAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.UnbindAutoSnapshotPolicyResponse:
        """
        解除文件系统绑定的快照策略
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateAutoSnapshotPolicy(
            self,
            request: models.UpdateAutoSnapshotPolicyRequest,
            opts: Dict = None,
    ) -> models.UpdateAutoSnapshotPolicyResponse:
        """
        更新定期自动快照策略
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateAutoSnapshotPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateAutoSnapshotPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsFileSystemName(
            self,
            request: models.UpdateCfsFileSystemNameRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsFileSystemNameResponse:
        """
        本接口（UpdateCfsFileSystemName）用于更新文件系统名
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsFileSystemName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsFileSystemNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsFileSystemPGroup(
            self,
            request: models.UpdateCfsFileSystemPGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsFileSystemPGroupResponse:
        """
        本接口（UpdateCfsFileSystemPGroup）用于更新文件系统所使用的权限组
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsFileSystemPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsFileSystemPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsFileSystemSizeLimit(
            self,
            request: models.UpdateCfsFileSystemSizeLimitRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsFileSystemSizeLimitResponse:
        """
        本接口（UpdateCfsFileSystemSizeLimit）用于更新文件系统存储容量限制。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsFileSystemSizeLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsFileSystemSizeLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsPGroup(
            self,
            request: models.UpdateCfsPGroupRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsPGroupResponse:
        """
        本接口（UpdateCfsPGroup）更新权限组信息。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsPGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsPGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsRule(
            self,
            request: models.UpdateCfsRuleRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsRuleResponse:
        """
        本接口（UpdateCfsRule）用于更新权限规则。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateCfsSnapshotAttribute(
            self,
            request: models.UpdateCfsSnapshotAttributeRequest,
            opts: Dict = None,
    ) -> models.UpdateCfsSnapshotAttributeResponse:
        """
        更新文件系统快照名称及保留时长
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateCfsSnapshotAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateCfsSnapshotAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateFileSystemBandwidthLimit(
            self,
            request: models.UpdateFileSystemBandwidthLimitRequest,
            opts: Dict = None,
    ) -> models.UpdateFileSystemBandwidthLimitResponse:
        """
        更新文件系统吞吐
        仅吞吐型支持此接口
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateFileSystemBandwidthLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateFileSystemBandwidthLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)