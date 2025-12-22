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
from tencentcloud.tcaplusdb.v20190823 import models
from typing import Dict


class TcaplusdbClient(AbstractClient):
    _apiVersion = '2019-08-23'
    _endpoint = 'tcaplusdb.tencentcloudapi.com'
    _service = 'tcaplusdb'

    async def ClearTables(
            self,
            request: models.ClearTablesRequest,
            opts: Dict = None,
    ) -> models.ClearTablesResponse:
        """
        根据给定的表信息，清除表数据。
        """
        
        kwargs = {}
        kwargs["action"] = "ClearTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CompareIdlFiles(
            self,
            request: models.CompareIdlFilesRequest,
            opts: Dict = None,
    ) -> models.CompareIdlFilesResponse:
        """
        选中目标表格，上传并校验改表文件，返回是否允许修改表格结构的结果。
        """
        
        kwargs = {}
        kwargs["action"] = "CompareIdlFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CompareIdlFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBackup(
            self,
            request: models.CreateBackupRequest,
            opts: Dict = None,
    ) -> models.CreateBackupResponse:
        """
        用户创建备份任务
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBackup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBackupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        本接口用于创建TcaplusDB集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshots(
            self,
            request: models.CreateSnapshotsRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotsResponse:
        """
        构造表格过去时间点的快照
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTableGroup(
            self,
            request: models.CreateTableGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTableGroupResponse:
        """
        在TcaplusDB集群下创建表格组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTableGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTableGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTables(
            self,
            request: models.CreateTablesRequest,
            opts: Dict = None,
    ) -> models.CreateTablesResponse:
        """
        根据选择的IDL文件列表，批量创建表格
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBackupRecords(
            self,
            request: models.DeleteBackupRecordsRequest,
            opts: Dict = None,
    ) -> models.DeleteBackupRecordsResponse:
        """
        删除手工备份
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBackupRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBackupRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        删除TcaplusDB集群，必须在集群所属所有资源（包括表格组，表）都已经释放的情况下才会成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIdlFiles(
            self,
            request: models.DeleteIdlFilesRequest,
            opts: Dict = None,
    ) -> models.DeleteIdlFilesResponse:
        """
        指定集群ID和待删除IDL文件的信息，删除目标文件，如果文件正在被表关联则删除失败。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIdlFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIdlFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        删除表格的快照
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableDataFlow(
            self,
            request: models.DeleteTableDataFlowRequest,
            opts: Dict = None,
    ) -> models.DeleteTableDataFlowResponse:
        """
        删除表格的数据订阅
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableGroup(
            self,
            request: models.DeleteTableGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteTableGroupResponse:
        """
        删除表格组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTableIndex(
            self,
            request: models.DeleteTableIndexRequest,
            opts: Dict = None,
    ) -> models.DeleteTableIndexResponse:
        """
        删除表格的分布式索引
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTableIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTableIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTables(
            self,
            request: models.DeleteTablesRequest,
            opts: Dict = None,
    ) -> models.DeleteTablesResponse:
        """
        删除指定的表,第一次调用此接口代表将表移动至回收站，再次调用代表将此表格从回收站中彻底删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeApplications(
            self,
            request: models.DescribeApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeApplicationsResponse:
        """
        获取审批管理的申请单
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBackupRecords(
            self,
            request: models.DescribeBackupRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeBackupRecordsResponse:
        """
        查询备份记录

        查询集群级别时， 将TableGroupId设置为"-1", 将TableName设置为"-1"
        查询集群+表格组级别时， 将TableName设置为"-1"
        查询集群+表格组+表格级别时， 都不能设置为“-1”
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackupRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackupRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterTags(
            self,
            request: models.DescribeClusterTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterTagsResponse:
        """
        获取集群关联的标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        查询TcaplusDB集群列表，包含集群详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIdlFileInfos(
            self,
            request: models.DescribeIdlFileInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeIdlFileInfosResponse:
        """
        查询表描述文件详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIdlFileInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIdlFileInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMachine(
            self,
            request: models.DescribeMachineRequest,
            opts: Dict = None,
    ) -> models.DescribeMachineResponse:
        """
        查询独占集群可以申请的剩余机器
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegions(
            self,
            request: models.DescribeRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionsResponse:
        """
        查询TcaplusDB服务支持的地域列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        查询快照列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableGroupTags(
            self,
            request: models.DescribeTableGroupTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableGroupTagsResponse:
        """
        获取表格组关联的标签列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableGroupTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableGroupTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableGroups(
            self,
            request: models.DescribeTableGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableGroupsResponse:
        """
        查询表格组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTableTags(
            self,
            request: models.DescribeTableTagsRequest,
            opts: Dict = None,
    ) -> models.DescribeTableTagsResponse:
        """
        获取表格标签
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTableTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTableTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTables(
            self,
            request: models.DescribeTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesResponse:
        """
        查询表详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTablesInRecycle(
            self,
            request: models.DescribeTablesInRecycleRequest,
            opts: Dict = None,
    ) -> models.DescribeTablesInRecycleResponse:
        """
        查询回收站中的表详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTablesInRecycle"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTablesInRecycleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTasks(
            self,
            request: models.DescribeTasksRequest,
            opts: Dict = None,
    ) -> models.DescribeTasksResponse:
        """
        查询任务列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUinInWhitelist(
            self,
            request: models.DescribeUinInWhitelistRequest,
            opts: Dict = None,
    ) -> models.DescribeUinInWhitelistResponse:
        """
        查询本用户是否在白名单中，控制是否能创建TDR类型的APP或表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUinInWhitelist"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUinInWhitelistResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRestProxy(
            self,
            request: models.DisableRestProxyRequest,
            opts: Dict = None,
    ) -> models.DisableRestProxyResponse:
        """
        当restful api为关闭状态时，可以通过此接口关闭restful api
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRestProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRestProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRestProxy(
            self,
            request: models.EnableRestProxyRequest,
            opts: Dict = None,
    ) -> models.EnableRestProxyResponse:
        """
        当restful api为关闭状态时，可以通过此接口开启restful api。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRestProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRestProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportSnapshots(
            self,
            request: models.ImportSnapshotsRequest,
            opts: Dict = None,
    ) -> models.ImportSnapshotsResponse:
        """
        将快照数据导入到新表或当前表
        """
        
        kwargs = {}
        kwargs["action"] = "ImportSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MergeTablesData(
            self,
            request: models.MergeTablesDataRequest,
            opts: Dict = None,
    ) -> models.MergeTablesDataResponse:
        """
        合并指定表格
        """
        
        kwargs = {}
        kwargs["action"] = "MergeTablesData"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MergeTablesDataResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCensorship(
            self,
            request: models.ModifyCensorshipRequest,
            opts: Dict = None,
    ) -> models.ModifyCensorshipResponse:
        """
        修改集群审批状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCensorship"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCensorshipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterMachine(
            self,
            request: models.ModifyClusterMachineRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterMachineResponse:
        """
        修改独占集群机器
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterMachine"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterMachineResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterName(
            self,
            request: models.ModifyClusterNameRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNameResponse:
        """
        修改指定的集群名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterPassword(
            self,
            request: models.ModifyClusterPasswordRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterPasswordResponse:
        """
        修改指定集群的密码，后台将在旧密码失效之前同时支持TcaplusDB SDK使用旧密码和新密码访问数据库。在旧密码失效之前不能提交新的密码修改请求，在旧密码失效之后不能提交修改旧密码过期时间的请求。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterTags(
            self,
            request: models.ModifyClusterTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterTagsResponse:
        """
        修改集群标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshots(
            self,
            request: models.ModifySnapshotsRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotsResponse:
        """
        修改表格快照的过期时间
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableGroupName(
            self,
            request: models.ModifyTableGroupNameRequest,
            opts: Dict = None,
    ) -> models.ModifyTableGroupNameResponse:
        """
        修改TcaplusDB表格组名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableGroupName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableGroupNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableGroupTags(
            self,
            request: models.ModifyTableGroupTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyTableGroupTagsResponse:
        """
        修改表格组标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableGroupTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableGroupTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableMemos(
            self,
            request: models.ModifyTableMemosRequest,
            opts: Dict = None,
    ) -> models.ModifyTableMemosResponse:
        """
        修改表备注信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableMemos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableMemosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableQuotas(
            self,
            request: models.ModifyTableQuotasRequest,
            opts: Dict = None,
    ) -> models.ModifyTableQuotasResponse:
        """
        表格扩缩容
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableQuotas"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableQuotasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTableTags(
            self,
            request: models.ModifyTableTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyTableTagsResponse:
        """
        修改表格标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTableTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTableTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTables(
            self,
            request: models.ModifyTablesRequest,
            opts: Dict = None,
    ) -> models.ModifyTablesResponse:
        """
        根据用户选定的表定义IDL文件，批量修改指定的表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverRecycleTables(
            self,
            request: models.RecoverRecycleTablesRequest,
            opts: Dict = None,
    ) -> models.RecoverRecycleTablesResponse:
        """
        恢复回收站中，用户自行删除的表。对欠费待释放的表无效。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverRecycleTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverRecycleTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetBackupExpireRule(
            self,
            request: models.SetBackupExpireRuleRequest,
            opts: Dict = None,
    ) -> models.SetBackupExpireRuleResponse:
        """
        新增、删除、修改备份过期策略， ClusterId必须为具体的集群Id（appid）
        """
        
        kwargs = {}
        kwargs["action"] = "SetBackupExpireRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetBackupExpireRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTableDataFlow(
            self,
            request: models.SetTableDataFlowRequest,
            opts: Dict = None,
    ) -> models.SetTableDataFlowResponse:
        """
        新增、修改表格数据订阅
        """
        
        kwargs = {}
        kwargs["action"] = "SetTableDataFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTableDataFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTableIndex(
            self,
            request: models.SetTableIndexRequest,
            opts: Dict = None,
    ) -> models.SetTableIndexResponse:
        """
        设置表格分布式索引
        """
        
        kwargs = {}
        kwargs["action"] = "SetTableIndex"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTableIndexResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateApply(
            self,
            request: models.UpdateApplyRequest,
            opts: Dict = None,
    ) -> models.UpdateApplyResponse:
        """
        更新申请单状态
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateApply"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateApplyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def VerifyIdlFiles(
            self,
            request: models.VerifyIdlFilesRequest,
            opts: Dict = None,
    ) -> models.VerifyIdlFilesResponse:
        """
        上传并校验创建表格文件，返回校验合法的表格定义
        """
        
        kwargs = {}
        kwargs["action"] = "VerifyIdlFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.VerifyIdlFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)