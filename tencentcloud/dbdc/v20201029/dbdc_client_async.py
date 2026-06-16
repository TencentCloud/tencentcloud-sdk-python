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
from tencentcloud.dbdc.v20201029 import models
from typing import Dict


class DbdcClient(AbstractClient):
    _apiVersion = '2020-10-29'
    _endpoint = 'dbdc.tencentcloudapi.com'
    _service = 'dbdc'

    async def AddNodesToDBCustomCluster(
            self,
            request: models.AddNodesToDBCustomClusterRequest,
            opts: Dict = None,
    ) -> models.AddNodesToDBCustomClusterResponse:
        """
        该接口（AddNodesToDBCustomCluster）用于为 DB Custom 集群上架节点。
        """
        
        kwargs = {}
        kwargs["action"] = "AddNodesToDBCustomCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddNodesToDBCustomClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckRoleAuthorized(
            self,
            request: models.CheckRoleAuthorizedRequest,
            opts: Dict = None,
    ) -> models.CheckRoleAuthorizedResponse:
        """
        检查服务相关角色是否已创建
        """
        
        kwargs = {}
        kwargs["action"] = "CheckRoleAuthorized"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckRoleAuthorizedResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBCustomCluster(
            self,
            request: models.CreateDBCustomClusterRequest,
            opts: Dict = None,
    ) -> models.CreateDBCustomClusterResponse:
        """
        该接口（CreateDBCustomCluster）用于创建 DB Custom 集群。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBCustomCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBCustomClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDBCustomNodes(
            self,
            request: models.CreateDBCustomNodesRequest,
            opts: Dict = None,
    ) -> models.CreateDBCustomNodesResponse:
        """
        该接口（CreateDBCustomNodes）用于创建 DB Custom 节点(需支付)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDBCustomNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDBCustomNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomClusterDetail(
            self,
            request: models.DescribeDBCustomClusterDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomClusterDetailResponse:
        """
        该接口(DescribeDBCustomClusterDetail) 用于查询 DB Custom 集群的详情信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomClusterDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomClusterDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomClusterKubeconfig(
            self,
            request: models.DescribeDBCustomClusterKubeconfigRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomClusterKubeconfigResponse:
        """
        该接口（DescribeDBCustomClusterKubeconfig）用于查询 DB Custom 集群 Kubeconfig。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomClusterKubeconfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomClusterKubeconfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomClusterNodes(
            self,
            request: models.DescribeDBCustomClusterNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomClusterNodesResponse:
        """
        该接口（DescribeDBCustomClusterNodes）用于查询 DB Custom 集群中的节点列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomClusterNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomClusterNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomClusters(
            self,
            request: models.DescribeDBCustomClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomClustersResponse:
        """
        该接口（DescribeDBCustomClusters）为DB Custom 集群列表查询接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomImages(
            self,
            request: models.DescribeDBCustomImagesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomImagesResponse:
        """
        该接口（DescribeDBCustomImages）用于查询 DB Custom 可用的操作系统镜像列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomImages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomImagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomNodes(
            self,
            request: models.DescribeDBCustomNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomNodesResponse:
        """
        该接口（DescribeDBCustomNodes）用于查询 DB Custom 节点列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBCustomTaskStatus(
            self,
            request: models.DescribeDBCustomTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeDBCustomTaskStatusResponse:
        """
        该接口（DescribeDBCustomTaskStatus）用于查询 DB Custom 任务的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBCustomTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBCustomTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDBInstances(
            self,
            request: models.DescribeDBInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeDBInstancesResponse:
        """
        本接口用于查询独享集群内的DB实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDBInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDBInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHostList(
            self,
            request: models.DescribeHostListRequest,
            opts: Dict = None,
    ) -> models.DescribeHostListResponse:
        """
        本接口用于查询主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHostList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHostListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceDetail(
            self,
            request: models.DescribeInstanceDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceDetailResponse:
        """
        本接口用于查询独享集群详情
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceList(
            self,
            request: models.DescribeInstanceListRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceListResponse:
        """
        本接口用于查询独享集群实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        根据不同地域不同用户，获取集群列表信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDBCustomCluster(
            self,
            request: models.DestroyDBCustomClusterRequest,
            opts: Dict = None,
    ) -> models.DestroyDBCustomClusterResponse:
        """
        该接口（DestroyDBCustomCluster）用于销毁 DB Custom 集群。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDBCustomCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDBCustomClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyDBCustomNode(
            self,
            request: models.DestroyDBCustomNodeRequest,
            opts: Dict = None,
    ) -> models.DestroyDBCustomNodeResponse:
        """
        该接口（DestroyDBCustomNode）用于销毁 DB Custom 节点。
        """
        
        kwargs = {}
        kwargs["action"] = "DestroyDBCustomNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DestroyDBCustomNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateDBCustomNode(
            self,
            request: models.IsolateDBCustomNodeRequest,
            opts: Dict = None,
    ) -> models.IsolateDBCustomNodeResponse:
        """
        该接口 (IsolateDBCustomNode) 用于隔离 DB Custom 节点。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateDBCustomNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateDBCustomNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBCustomClusterTags(
            self,
            request: models.ModifyDBCustomClusterTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBCustomClusterTagsResponse:
        """
        该接口（ModifyDBCustomClusterTags）用于修改 DB Custom 集群的标签配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBCustomClusterTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBCustomClusterTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDBCustomNodeTags(
            self,
            request: models.ModifyDBCustomNodeTagsRequest,
            opts: Dict = None,
    ) -> models.ModifyDBCustomNodeTagsResponse:
        """
        该接口（ModifyDBCustomNodeTags）用于修改 DB Custom 节点的标签配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDBCustomNodeTags"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDBCustomNodeTagsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstanceName(
            self,
            request: models.ModifyInstanceNameRequest,
            opts: Dict = None,
    ) -> models.ModifyInstanceNameResponse:
        """
        本接口用于修改集群名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstanceName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstanceNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveNodesFromDBCustomCluster(
            self,
            request: models.RemoveNodesFromDBCustomClusterRequest,
            opts: Dict = None,
    ) -> models.RemoveNodesFromDBCustomClusterResponse:
        """
        该接口（RemoveNodesFromDBCustomCluster）用于从 DB Custom 集群移除节点。
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveNodesFromDBCustomCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveNodesFromDBCustomClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewDBCustomNode(
            self,
            request: models.RenewDBCustomNodeRequest,
            opts: Dict = None,
    ) -> models.RenewDBCustomNodeResponse:
        """
        该接口（RenewDBCustomNode）用于给 DB Custom 节点续费。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewDBCustomNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewDBCustomNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)