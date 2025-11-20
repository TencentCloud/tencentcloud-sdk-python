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
from tencentcloud.thpc.v20230321 import models
from typing import Dict


class ThpcClient(AbstractClient):
    _apiVersion = '2023-03-21'
    _endpoint = 'thpc.tencentcloudapi.com'
    _service = 'thpc'

    async def AddClusterStorageOption(
            self,
            request: models.AddClusterStorageOptionRequest,
            opts: Dict = None,
    ) -> models.AddClusterStorageOptionResponse:
        """
        本接口（AddClusterStorageOption）用于添加集群存储选项信息。
        """
        
        kwargs = {}
        kwargs["action"] = "AddClusterStorageOption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddClusterStorageOptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddNodes(
            self,
            request: models.AddNodesRequest,
            opts: Dict = None,
    ) -> models.AddNodesResponse:
        """
        本接口(AddNodes)用于添加一个或者多个计算节点或者登录节点到指定集群。
        """
        
        kwargs = {}
        kwargs["action"] = "AddNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddQueue(
            self,
            request: models.AddQueueRequest,
            opts: Dict = None,
    ) -> models.AddQueueResponse:
        """
        本接口(AddQueue)用于添加队列到指定集群。
        * 本接口为目前只支持SchedulerType为SLURM的集群。
        * 单个集群中队列数量上限为10个。
        """
        
        kwargs = {}
        kwargs["action"] = "AddQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachNodes(
            self,
            request: models.AttachNodesRequest,
            opts: Dict = None,
    ) -> models.AttachNodesResponse:
        """
        本接口 (AttachNodes) 用于绑定一个或者多个计算节点指定资源到指定集群中。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        本接口 (CreateCluster) 用于创建并启动集群。

        * 本接口为异步接口， 当创建集群请求下发成功后会返回一个集群`ID`和一个`RequestId`，此时创建集群操作并未立即完成。在此期间集群的状态将会处于“PENDING”或者“INITING”，集群创建结果可以通过调用 [DescribeClusters](https://cloud.tencent.com/document/product/1527/72100)  接口查询，如果集群状态(ClusterStatus)变为“RUNNING(运行中)”，则代表集群创建成功，“ INIT_FAILED”代表集群创建失败。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateWorkspaces(
            self,
            request: models.CreateWorkspacesRequest,
            opts: Dict = None,
    ) -> models.CreateWorkspacesResponse:
        """
        本接口 (CreateWorkspaces) 用于创建工作空间。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        本接口（DeleteCluster）用于删除一个指定的集群。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterStorageOption(
            self,
            request: models.DeleteClusterStorageOptionRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterStorageOptionResponse:
        """
        本接口 (DeleteClusterStorageOption) 用于删除集群存储选项信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterStorageOption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterStorageOptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteJob(
            self,
            request: models.DeleteJobRequest,
            opts: Dict = None,
    ) -> models.DeleteJobResponse:
        """
        本接口 (DeleteJob) 用于删除一个作业任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNodes(
            self,
            request: models.DeleteNodesRequest,
            opts: Dict = None,
    ) -> models.DeleteNodesResponse:
        """
        本接口(DeleteNodes)用于删除指定集群中一个或者多个计算节点或者登录节点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteQueue(
            self,
            request: models.DeleteQueueRequest,
            opts: Dict = None,
    ) -> models.DeleteQueueResponse:
        """
        本接口(DeleteQueue)用于从指定集群删除队列。
        * 本接口为目前只支持SchedulerType为SLURM的集群。

        * 删除队列时，需要保证队列内不存在节点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteQueue"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteQueueResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAutoScalingConfiguration(
            self,
            request: models.DescribeAutoScalingConfigurationRequest,
            opts: Dict = None,
    ) -> models.DescribeAutoScalingConfigurationResponse:
        """
        本接口(DescribeAutoScalingConfiguration)用于查询集群弹性伸缩配置信息。本接口仅适用于弹性伸缩类型为THPC_AS的集群。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAutoScalingConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAutoScalingConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterActivities(
            self,
            request: models.DescribeClusterActivitiesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterActivitiesResponse:
        """
        本接口（DescribeClusterActivities）用于查询集群活动历史记录列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterActivities"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterActivitiesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterStorageOption(
            self,
            request: models.DescribeClusterStorageOptionRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterStorageOptionResponse:
        """
        本接口 (DescribeClusterStorageOption) 用于查询集群存储选项信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterStorageOption"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterStorageOptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        本接口（DescribeClusters）用于查询集群列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInitNodeScripts(
            self,
            request: models.DescribeInitNodeScriptsRequest,
            opts: Dict = None,
    ) -> models.DescribeInitNodeScriptsResponse:
        """
        本接口 (DescribeInitNodeScripts) 用于查询节点初始化脚本列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInitNodeScripts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInitNodeScriptsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobSubmitInfo(
            self,
            request: models.DescribeJobSubmitInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeJobSubmitInfoResponse:
        """
        本接口用于查询作业的提交信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobSubmitInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobSubmitInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobs(
            self,
            request: models.DescribeJobsRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsResponse:
        """
        本接口 (DescribeJobs) 用于查询作业任务列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeJobsOverview(
            self,
            request: models.DescribeJobsOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeJobsOverviewResponse:
        """
        本接口 (DescribeJobs) 用于查询作业任务列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeJobsOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeJobsOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNodes(
            self,
            request: models.DescribeNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeNodesResponse:
        """
        本接口 (DescribeNodes) 用于查询指定集群节点概览信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQueues(
            self,
            request: models.DescribeQueuesRequest,
            opts: Dict = None,
    ) -> models.DescribeQueuesResponse:
        """
        本接口(DescribeQueues)用于查询指定集群队列概览信息列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQueues"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQueuesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeWorkspaces(
            self,
            request: models.DescribeWorkspacesRequest,
            opts: Dict = None,
    ) -> models.DescribeWorkspacesResponse:
        """
        本接口（DescribeWorkspaces）用于查询工作空间列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachNodes(
            self,
            request: models.DetachNodesRequest,
            opts: Dict = None,
    ) -> models.DetachNodesResponse:
        """
        本接口 (DetachNodes) 用于将一个或者多个计算节点从集群中移除，但是不销毁指定计算资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterDeletionProtection(
            self,
            request: models.ModifyClusterDeletionProtectionRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterDeletionProtectionResponse:
        """
        修改集群删除保护状态
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterDeletionProtection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterDeletionProtectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInitNodeScripts(
            self,
            request: models.ModifyInitNodeScriptsRequest,
            opts: Dict = None,
    ) -> models.ModifyInitNodeScriptsResponse:
        """
        本接口 (ModifyInitNodeScripts) 用于修改节点初始化脚本。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInitNodeScripts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInitNodeScriptsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkspacesAttribute(
            self,
            request: models.ModifyWorkspacesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkspacesAttributeResponse:
        """
        本接口 (ModifyWorkspacesAttribute) 用于修改工作空间的属性（目前只支持修改工作空间的名称）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkspacesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkspacesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyWorkspacesRenewFlag(
            self,
            request: models.ModifyWorkspacesRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkspacesRenewFlagResponse:
        """
        本接口 (ModifyWorkspacesAttribute) 用于修改工作空间的属性（目前只支持修改工作空间的名称）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkspacesRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkspacesRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetAutoScalingConfiguration(
            self,
            request: models.SetAutoScalingConfigurationRequest,
            opts: Dict = None,
    ) -> models.SetAutoScalingConfigurationResponse:
        """
        本接口(SetAutoScalingConfiguration)用于为集群设置集群弹性伸缩配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "SetAutoScalingConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetAutoScalingConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SubmitJob(
            self,
            request: models.SubmitJobRequest,
            opts: Dict = None,
    ) -> models.SubmitJobResponse:
        """
        本接口 (SubmitJob) 用于提交一个作业任务。
        """
        
        kwargs = {}
        kwargs["action"] = "SubmitJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SubmitJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateJob(
            self,
            request: models.TerminateJobRequest,
            opts: Dict = None,
    ) -> models.TerminateJobResponse:
        """
        本接口 (TerminateJob) 用于终止一个作业任务。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateJob"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateJobResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateWorkspaces(
            self,
            request: models.TerminateWorkspacesRequest,
            opts: Dict = None,
    ) -> models.TerminateWorkspacesResponse:
        """
        本接口 (TerminateWorkspaces) 用于主动退还工作空间。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)