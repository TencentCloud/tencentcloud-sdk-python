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
from tencentcloud.thpc.v20220401 import models
from typing import Dict


class ThpcClient(AbstractClient):
    _apiVersion = '2022-04-01'
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
        
    async def BindAutoScalingGroup(
            self,
            request: models.BindAutoScalingGroupRequest,
            opts: Dict = None,
    ) -> models.BindAutoScalingGroupResponse:
        """
        本接口(BindAutoScalingGroup)用于为集群队列绑定弹性伸缩组
        """
        
        kwargs = {}
        kwargs["action"] = "BindAutoScalingGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindAutoScalingGroupResponse
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