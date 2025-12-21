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
from tencentcloud.emr.v20190103 import models
from typing import Dict


class EmrClient(AbstractClient):
    _apiVersion = '2019-01-03'
    _endpoint = 'emr.tencentcloudapi.com'
    _service = 'emr'

    async def AddMetricScaleStrategy(
            self,
            request: models.AddMetricScaleStrategyRequest,
            opts: Dict = None,
    ) -> models.AddMetricScaleStrategyResponse:
        """
        添加扩缩容规则，按负载和时间
        """
        
        kwargs = {}
        kwargs["action"] = "AddMetricScaleStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddMetricScaleStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNodeResourceConfig(
            self,
            request: models.AddNodeResourceConfigRequest,
            opts: Dict = None,
    ) -> models.AddNodeResourceConfigResponse:
        """
        增加当前集群的节点规格配置
        """
        
        kwargs = {}
        kwargs["action"] = "AddNodeResourceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNodeResourceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddUsersForUserManager(
            self,
            request: models.AddUsersForUserManagerRequest,
            opts: Dict = None,
    ) -> models.AddUsersForUserManagerResponse:
        """
        该接口支持安装了OpenLdap组件的集群。
        新增用户列表（用户管理）。
        """
        
        kwargs = {}
        kwargs["action"] = "AddUsersForUserManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddUsersForUserManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDisks(
            self,
            request: models.AttachDisksRequest,
            opts: Dict = None,
    ) -> models.AttachDisksResponse:
        """
        云盘挂载
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ConvertPreToPostCluster(
            self,
            request: models.ConvertPreToPostClusterRequest,
            opts: Dict = None,
    ) -> models.ConvertPreToPostClusterResponse:
        """
        包月集群转按量集群（不含cdb）
        """
        
        kwargs = {}
        kwargs["action"] = "ConvertPreToPostCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ConvertPreToPostClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCloudInstance(
            self,
            request: models.CreateCloudInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateCloudInstanceResponse:
        """
        创建EMR容器集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCloudInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCloudInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        创建EMR集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGroupsSTD(
            self,
            request: models.CreateGroupsSTDRequest,
            opts: Dict = None,
    ) -> models.CreateGroupsSTDResponse:
        """
        用户管理-批量创建用户组
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGroupsSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGroupsSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInstance(
            self,
            request: models.CreateInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceResponse:
        """
        创建EMR集群实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSLInstance(
            self,
            request: models.CreateSLInstanceRequest,
            opts: Dict = None,
    ) -> models.CreateSLInstanceResponse:
        """
        本接口（CreateSLInstance）用于创建Serverless HBase实例
        - 接口调用成功，会创建Serverless HBase实例，创建实例请求成功会返回创建实例的InstaceId和请求的 RequestID。
        - 接口为异步接口，接口返回时操作并未立即完成，实例操作结果可以通过调用DescribeInstancesList查看当前实例的StatusDesc状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAutoScaleStrategy(
            self,
            request: models.DeleteAutoScaleStrategyRequest,
            opts: Dict = None,
    ) -> models.DeleteAutoScaleStrategyResponse:
        """
        删除自动扩缩容规则，后台销毁根据该规则扩缩容出来的节点
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAutoScaleStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAutoScaleStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGroupsSTD(
            self,
            request: models.DeleteGroupsSTDRequest,
            opts: Dict = None,
    ) -> models.DeleteGroupsSTDResponse:
        """
        批量删除用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGroupsSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGroupsSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNodeResourceConfig(
            self,
            request: models.DeleteNodeResourceConfigRequest,
            opts: Dict = None,
    ) -> models.DeleteNodeResourceConfigResponse:
        """
        删除当前集群的节点规格配置
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNodeResourceConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNodeResourceConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteUserManagerUserList(
            self,
            request: models.DeleteUserManagerUserListRequest,
            opts: Dict = None,
    ) -> models.DeleteUserManagerUserListResponse:
        """
        删除用户列表（用户管理）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteUserManagerUserList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteUserManagerUserListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeployYarnConf(
            self,
            request: models.DeployYarnConfRequest,
            opts: Dict = None,
    ) -> models.DeployYarnConfResponse:
        """
        yarn资源调度-部署生效
        """
        
        kwargs = {}
        kwargs["action"] = "DeployYarnConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeployYarnConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScaleGroupGlobalConf(
            self,
            request: models.DescribeAutoScaleGroupGlobalConfRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScaleGroupGlobalConfResponse:
        """
        获取自动扩缩容全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScaleGroupGlobalConf"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScaleGroupGlobalConfResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScaleRecords(
            self,
            request: models.DescribeAutoScaleRecordsRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScaleRecordsResponse:
        """
        获取集群的自动扩缩容的详细记录
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScaleRecords"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScaleRecordsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScaleStrategies(
            self,
            request: models.DescribeAutoScaleStrategiesRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScaleStrategiesResponse:
        """
        获取自动扩缩容规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScaleStrategies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScaleStrategiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterFlowStatusDetail(
            self,
            request: models.DescribeClusterFlowStatusDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterFlowStatusDetailResponse:
        """
        查询EMR任务运行详情状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterFlowStatusDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterFlowStatusDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterNodes(
            self,
            request: models.DescribeClusterNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterNodesResponse:
        """
        查询集群节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCvmQuota(
            self,
            request: models.DescribeCvmQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeCvmQuotaResponse:
        """
        获取账户的CVM配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCvmQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCvmQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDAGInfo(
            self,
            request: models.DescribeDAGInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDAGInfoResponse:
        """
        查询DAG信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDAGInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDAGInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmrApplicationStatics(
            self,
            request: models.DescribeEmrApplicationStaticsRequest,
            opts: Dict = None,
    ) -> models.DescribeEmrApplicationStaticsResponse:
        """
        yarn application 统计接口查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmrApplicationStatics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmrApplicationStaticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeEmrOverviewMetrics(
            self,
            request: models.DescribeEmrOverviewMetricsRequest,
            opts: Dict = None,
    ) -> models.DescribeEmrOverviewMetricsResponse:
        """
        查询监控概览页指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeEmrOverviewMetrics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeEmrOverviewMetricsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalConfig(
            self,
            request: models.DescribeGlobalConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalConfigResponse:
        """
        查询YARN资源调度的全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGroupsSTD(
            self,
            request: models.DescribeGroupsSTDRequest,
            opts: Dict = None,
    ) -> models.DescribeGroupsSTDResponse:
        """
        查询用户组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGroupsSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGroupsSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHBaseTableOverview(
            self,
            request: models.DescribeHBaseTableOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeHBaseTableOverviewResponse:
        """
        获取Hbase表级监控数据概览接口
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHBaseTableOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHBaseTableOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHBaseTableRequestMetric(
            self,
            request: models.DescribeHBaseTableRequestMetricRequest,
            opts: Dict = None,
    ) -> models.DescribeHBaseTableRequestMetricResponse:
        """
        Hbase的表粒度读取和写入速率
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHBaseTableRequestMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHBaseTableRequestMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHBaseTableStoreSizeMetric(
            self,
            request: models.DescribeHBaseTableStoreSizeMetricRequest,
            opts: Dict = None,
    ) -> models.DescribeHBaseTableStoreSizeMetricResponse:
        """
        查询Hbase的表粒度StoreSize大小监控指标数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHBaseTableStoreSizeMetric"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHBaseTableStoreSizeMetricResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHDFSStorageInfo(
            self,
            request: models.DescribeHDFSStorageInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeHDFSStorageInfoResponse:
        """
        查询HDFS存储文件信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHDFSStorageInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHDFSStorageInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHiveQueries(
            self,
            request: models.DescribeHiveQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeHiveQueriesResponse:
        """
        获取hive查询信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHiveQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHiveQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImpalaQueries(
            self,
            request: models.DescribeImpalaQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeImpalaQueriesResponse:
        """
        DescribeImpalaQueries
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImpalaQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImpalaQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInsightList(
            self,
            request: models.DescribeInsightListRequest,
            opts: Dict = None,
    ) -> models.DescribeInsightListResponse:
        """
        获取洞察结果信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInsightList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInsightListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInspectionTaskResult(
            self,
            request: models.DescribeInspectionTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeInspectionTaskResultResponse:
        """
        获取巡检任务结果列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInspectionTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInspectionTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceOplog(
            self,
            request: models.DescribeInstanceOplogRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceOplogResponse:
        """
        获取实例操作日志
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceOplog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceOplogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceRenewNodes(
            self,
            request: models.DescribeInstanceRenewNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceRenewNodesResponse:
        """
        查询待续费节点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceRenewNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceRenewNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        查询集群实例信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesList(
            self,
            request: models.DescribeInstancesListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesListResponse:
        """
        查询集群列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobFlow(
            self,
            request: models.DescribeJobFlowRequest,
            opts: Dict = None,
    ) -> models.DescribeJobFlowResponse:
        """
        查询流程任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeKyuubiQueryInfo(
            self,
            request: models.DescribeKyuubiQueryInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeKyuubiQueryInfoResponse:
        """
        查询Kyuubi查询信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeKyuubiQueryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeKyuubiQueryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeDataDisks(
            self,
            request: models.DescribeNodeDataDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeDataDisksResponse:
        """
        查询节点数据盘信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeDataDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeDataDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeResourceConfigFast(
            self,
            request: models.DescribeNodeResourceConfigFastRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeResourceConfigFastResponse:
        """
        快速获取当前集群的节点规格配置
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeResourceConfigFast"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeResourceConfigFastResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodeSpec(
            self,
            request: models.DescribeNodeSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeSpecResponse:
        """
        查询节点规格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodeSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceSchedule(
            self,
            request: models.DescribeResourceScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceScheduleResponse:
        """
        查询YARN资源调度数据信息。已废弃，请使用`DescribeYarnQueue`去查询队列信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceScheduleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourceScheduleDiffDetail(
            self,
            request: models.DescribeResourceScheduleDiffDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeResourceScheduleDiffDetailResponse:
        """
        YARN资源调度-变更详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourceScheduleDiffDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourceScheduleDiffDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSLInstance(
            self,
            request: models.DescribeSLInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeSLInstanceResponse:
        """
        本接口（DescribeSLInstance）用于查询 Serverless HBase实例基本信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSLInstanceList(
            self,
            request: models.DescribeSLInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeSLInstanceListResponse:
        """
        本接口（DescribeSLInstanceList）用于查询Serverless HBase实例列表详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSLInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSLInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceConfGroupInfos(
            self,
            request: models.DescribeServiceConfGroupInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceConfGroupInfosResponse:
        """
        描述服务配置组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceConfGroupInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceConfGroupInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceNodeInfos(
            self,
            request: models.DescribeServiceNodeInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceNodeInfosResponse:
        """
        查询服务进程信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceNodeInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceNodeInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkApplications(
            self,
            request: models.DescribeSparkApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkApplicationsResponse:
        """
        获取spark应用列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSparkQueries(
            self,
            request: models.DescribeSparkQueriesRequest,
            opts: Dict = None,
    ) -> models.DescribeSparkQueriesResponse:
        """
        查询Spark查询信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSparkQueries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSparkQueriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeStarRocksQueryInfo(
            self,
            request: models.DescribeStarRocksQueryInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeStarRocksQueryInfoResponse:
        """
        查询StarRocks查询信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeStarRocksQueryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeStarRocksQueryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrinoQueryInfo(
            self,
            request: models.DescribeTrinoQueryInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeTrinoQueryInfoResponse:
        """
        查询Trino(PrestoSQL)查询信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrinoQueryInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrinoQueryInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsersForUserManager(
            self,
            request: models.DescribeUsersForUserManagerRequest,
            opts: Dict = None,
    ) -> models.DescribeUsersForUserManagerResponse:
        """
        该接口支持安装了OpenLdap组件的集群。
        批量导出用户。对于kerberos集群，如果需要kertab文件下载地址，可以将NeedKeytabInfo设置为true；注意SupportDownLoadKeyTab为true，但是DownLoadKeyTabUrl为空字符串，表示keytab文件在后台没有准备好（正在生成）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsersForUserManager"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsersForUserManagerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeYarnApplications(
            self,
            request: models.DescribeYarnApplicationsRequest,
            opts: Dict = None,
    ) -> models.DescribeYarnApplicationsResponse:
        """
        DescribeYarnApplications
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeYarnApplications"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeYarnApplicationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeYarnQueue(
            self,
            request: models.DescribeYarnQueueRequest,
            opts: Dict = None,
    ) -> models.DescribeYarnQueueResponse:
        """
        获取资源调度中的队列信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeYarnQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeYarnQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeYarnScheduleHistory(
            self,
            request: models.DescribeYarnScheduleHistoryRequest,
            opts: Dict = None,
    ) -> models.DescribeYarnScheduleHistoryResponse:
        """
        查看yarn资源调度的调度历史。废弃，请使用流程中心查看历史记录。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeYarnScheduleHistory"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeYarnScheduleHistoryResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceRenewEmr(
            self,
            request: models.InquirePriceRenewEmrRequest,
            opts: Dict = None,
    ) -> models.InquirePriceRenewEmrResponse:
        """
        集群续费询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceRenewEmr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceRenewEmrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateInstance(
            self,
            request: models.InquiryPriceCreateInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateInstanceResponse:
        """
        创建实例询价
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewInstance(
            self,
            request: models.InquiryPriceRenewInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewInstanceResponse:
        """
        续费询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceScaleOutInstance(
            self,
            request: models.InquiryPriceScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceScaleOutInstanceResponse:
        """
        扩容询价. 当扩容时候，请通过该接口查询价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceUpdateInstance(
            self,
            request: models.InquiryPriceUpdateInstanceRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceUpdateInstanceResponse:
        """
        变配询价
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceUpdateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceUpdateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoRenewFlag(
            self,
            request: models.ModifyAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoRenewFlagResponse:
        """
        前提：预付费集群
        资源级别开启或关闭自动续费
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAutoScaleStrategy(
            self,
            request: models.ModifyAutoScaleStrategyRequest,
            opts: Dict = None,
    ) -> models.ModifyAutoScaleStrategyResponse:
        """
        修改自动扩缩容规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAutoScaleStrategy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAutoScaleStrategyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalConfig(
            self,
            request: models.ModifyGlobalConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalConfigResponse:
        """
        修改YARN资源调度的全局配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInspectionSettings(
            self,
            request: models.ModifyInspectionSettingsRequest,
            opts: Dict = None,
    ) -> models.ModifyInspectionSettingsResponse:
        """
        设置巡检任务配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInspectionSettings"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInspectionSettingsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceBasic(
            self,
            request: models.ModifyInstanceBasicRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceBasicResponse:
        """
        修改集群名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceBasic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceBasicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPodNum(
            self,
            request: models.ModifyPodNumRequest,
            opts: Dict = None,
    ) -> models.ModifyPodNumResponse:
        """
        调整Pod数量
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPodNum"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPodNumResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResource(
            self,
            request: models.ModifyResourceRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceResponse:
        """
        变配实例
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcePools(
            self,
            request: models.ModifyResourcePoolsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcePoolsResponse:
        """
        已废弃，请使用DeployYarnConf\\n，近一年未被调用

        刷新YARN的动态资源池。已废弃，请使用`DeployYarnConf`
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcePools"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcePoolsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceScheduleConfig(
            self,
            request: models.ModifyResourceScheduleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceScheduleConfigResponse:
        """
        已废弃，请使用ModifyYarnQueueV2来修改队列配置，近一年无相关日志

        修改YARN资源调度的资源配置。已废弃，请使用`ModifyYarnQueueV2`来修改队列配置
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceScheduleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceScheduleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourceScheduler(
            self,
            request: models.ModifyResourceSchedulerRequest,
            opts: Dict = None,
    ) -> models.ModifyResourceSchedulerResponse:
        """
        修改了yarn的资源调度器，点击部署生效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourceScheduler"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourceSchedulerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyResourcesTags(
            self,
            request: models.ModifyResourcesTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyResourcesTagsResponse:
        """
        强制修改标签
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyResourcesTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyResourcesTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySLInstance(
            self,
            request: models.ModifySLInstanceRequest,
            opts: Dict = None,
    ) -> models.ModifySLInstanceResponse:
        """
        本接口（ModifySLInstance）用于Serverless HBase变配实例。
        - 接口调用成功，会创建Serverless HBase实例，创建实例请求成功会返回请求的 RequestID。
        - 接口为异步接口，接口返回时操作并未立即完成，实例操作结果可以通过调用DescribeInstancesList查看当前实例的StatusDesc状态。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySLInstanceBasic(
            self,
            request: models.ModifySLInstanceBasicRequest,
            opts: Dict = None,
    ) -> models.ModifySLInstanceBasicResponse:
        """
        serverless hbase修改实例名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySLInstanceBasic"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySLInstanceBasicResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserGroup(
            self,
            request: models.ModifyUserGroupRequest,
            opts: Dict = None,
    ) -> models.ModifyUserGroupResponse:
        """
        用户管理-修改用户组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUserManagerPwd(
            self,
            request: models.ModifyUserManagerPwdRequest,
            opts: Dict = None,
    ) -> models.ModifyUserManagerPwdResponse:
        """
        修改用户密码（用户管理）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserManagerPwd"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserManagerPwdResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyUsersOfGroupSTD(
            self,
            request: models.ModifyUsersOfGroupSTDRequest,
            opts: Dict = None,
    ) -> models.ModifyUsersOfGroupSTDResponse:
        """
        变更用户组用户信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUsersOfGroupSTD"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUsersOfGroupSTDResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyYarnDeploy(
            self,
            request: models.ModifyYarnDeployRequest,
            opts: Dict = None,
    ) -> models.ModifyYarnDeployResponse:
        """
        该接口已废弃，请使用DeployYarnConf完成部署生效

        部署生效。已废弃，请使用`DeployYarnConf`接口进行部署生效
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyYarnDeploy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyYarnDeployResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyYarnQueueV2(
            self,
            request: models.ModifyYarnQueueV2Request,
            opts: Dict = None,
    ) -> models.ModifyYarnQueueV2Response:
        """
        修改资源调度中队列信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyYarnQueueV2"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyYarnQueueV2Response
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetYarnConfig(
            self,
            request: models.ResetYarnConfigRequest,
            opts: Dict = None,
    ) -> models.ResetYarnConfigResponse:
        """
        修改YARN资源调度的资源配置
        """
        
        kwargs = {}
        kwargs["action"] = "ResetYarnConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetYarnConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResizeDataDisks(
            self,
            request: models.ResizeDataDisksRequest,
            opts: Dict = None,
    ) -> models.ResizeDataDisksResponse:
        """
        云数据盘扩容
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDataDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDataDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunJobFlow(
            self,
            request: models.RunJobFlowRequest,
            opts: Dict = None,
    ) -> models.RunJobFlowResponse:
        """
        创建流程作业
        """
        
        kwargs = {}
        kwargs["action"] = "RunJobFlow"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunJobFlowResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutCluster(
            self,
            request: models.ScaleOutClusterRequest,
            opts: Dict = None,
    ) -> models.ScaleOutClusterResponse:
        """
        扩容集群节点
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        扩容节点
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleOutInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleOutInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetNodeResourceConfigDefault(
            self,
            request: models.SetNodeResourceConfigDefaultRequest,
            opts: Dict = None,
    ) -> models.SetNodeResourceConfigDefaultResponse:
        """
        设置当前集群的某个节点规格配置为默认或取消默认
        """
        
        kwargs = {}
        kwargs["action"] = "SetNodeResourceConfigDefault"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetNodeResourceConfigDefaultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartStopServiceOrMonitor(
            self,
            request: models.StartStopServiceOrMonitorRequest,
            opts: Dict = None,
    ) -> models.StartStopServiceOrMonitorResponse:
        """
        用于启停服务 重启服务等功能
        """
        
        kwargs = {}
        kwargs["action"] = "StartStopServiceOrMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartStopServiceOrMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SyncPodState(
            self,
            request: models.SyncPodStateRequest,
            opts: Dict = None,
    ) -> models.SyncPodStateResponse:
        """
        EMR同步TKE中POD状态
        """
        
        kwargs = {}
        kwargs["action"] = "SyncPodState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SyncPodStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateClusterNodes(
            self,
            request: models.TerminateClusterNodesRequest,
            opts: Dict = None,
    ) -> models.TerminateClusterNodesResponse:
        """
        销毁集群节点
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateClusterNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateClusterNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstance(
            self,
            request: models.TerminateInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateInstanceResponse:
        """
        销毁EMR实例。此接口仅支持弹性MapReduce正式计费版本。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateSLInstance(
            self,
            request: models.TerminateSLInstanceRequest,
            opts: Dict = None,
    ) -> models.TerminateSLInstanceResponse:
        """
        本接口（TerminateSLInstance）用于销毁Serverless HBase实例
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateSLInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateSLInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateTasks(
            self,
            request: models.TerminateTasksRequest,
            opts: Dict = None,
    ) -> models.TerminateTasksResponse:
        """
        缩容Task节点
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateTasks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateTasksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)