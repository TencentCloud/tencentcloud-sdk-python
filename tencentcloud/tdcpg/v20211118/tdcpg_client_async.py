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
from tencentcloud.tdcpg.v20211118 import models
from typing import Dict


class TdcpgClient(AbstractClient):
    _apiVersion = '2021-11-18'
    _endpoint = 'tdcpg.tencentcloudapi.com'
    _service = 'tdcpg'

    async def CloneClusterToPointInTime(
            self,
            request: models.CloneClusterToPointInTimeRequest,
            opts: Dict = None,
    ) -> models.CloneClusterToPointInTimeResponse:
        """
        使用指定时间点的备份克隆一个新的集群
        """
        
        kwargs = {}
        kwargs["action"] = "CloneClusterToPointInTime"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneClusterToPointInTimeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCluster(
            self,
            request: models.CreateClusterRequest,
            opts: Dict = None,
    ) -> models.CreateClusterResponse:
        """
        创建集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateClusterInstances(
            self,
            request: models.CreateClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.CreateClusterInstancesResponse:
        """
        在集群中新建实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCluster(
            self,
            request: models.DeleteClusterRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterResponse:
        """
        删除集群，集群中的实例和数据都将被删除，且无法恢复。只有当集群状态处于isolated(已隔离)时才生效。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteClusterInstances(
            self,
            request: models.DeleteClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DeleteClusterInstancesResponse:
        """
        删除实例。只有当实例状态处于isolated(已隔离)时才生效。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccounts(
            self,
            request: models.DescribeAccountsRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountsResponse:
        """
        查询数据库账号信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccounts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterBackups(
            self,
            request: models.DescribeClusterBackupsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterBackupsResponse:
        """
        查询集群的备份集
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterBackups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterBackupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterEndpoints(
            self,
            request: models.DescribeClusterEndpointsRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterEndpointsResponse:
        """
        查询集群接入点信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterEndpoints"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterEndpointsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterInstances(
            self,
            request: models.DescribeClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterInstancesResponse:
        """
        查询实例
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusterRecoveryTimeRange(
            self,
            request: models.DescribeClusterRecoveryTimeRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterRecoveryTimeRangeResponse:
        """
        查询集群可回档时间范围
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterRecoveryTimeRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterRecoveryTimeRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClusters(
            self,
            request: models.DescribeClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeClustersResponse:
        """
        查询集群
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeResourcesByDealName(
            self,
            request: models.DescribeResourcesByDealNameRequest,
            opts: Dict = None,
    ) -> models.DescribeResourcesByDealNameResponse:
        """
        根据订单号获取资源信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeResourcesByDealName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeResourcesByDealNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateCluster(
            self,
            request: models.IsolateClusterRequest,
            opts: Dict = None,
    ) -> models.IsolateClusterResponse:
        """
        隔离集群，集群的接入点网络将会断掉无法连接使用数据库。只有当集群状态处于running(运行中)时才生效。
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def IsolateClusterInstances(
            self,
            request: models.IsolateClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.IsolateClusterInstancesResponse:
        """
        隔离实例。此接口只针对状态为running的实例生效，使用场景包括：
         - 批量隔离集群内所有的实例
         - 在读写实例为running(运行中)时，单个/批量隔离只读实例
         - 集群内所有只读实例为isolated(已隔离)时，单独隔离读写实例
        """
        
        kwargs = {}
        kwargs["action"] = "IsolateClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.IsolateClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAccountDescription(
            self,
            request: models.ModifyAccountDescriptionRequest,
            opts: Dict = None,
    ) -> models.ModifyAccountDescriptionResponse:
        """
        修改数据库账号描述
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAccountDescription"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAccountDescriptionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterEndpointWanStatus(
            self,
            request: models.ModifyClusterEndpointWanStatusRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterEndpointWanStatusResponse:
        """
        开启或者关闭接入点外网
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterEndpointWanStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterEndpointWanStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterInstancesSpec(
            self,
            request: models.ModifyClusterInstancesSpecRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterInstancesSpecResponse:
        """
        修改实例规格，此接口只针对状态为running(运行中)的实例生效
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterInstancesSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterInstancesSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClusterName(
            self,
            request: models.ModifyClusterNameRequest,
            opts: Dict = None,
    ) -> models.ModifyClusterNameResponse:
        """
        修改集群名字
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClusterName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClusterNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyClustersAutoRenewFlag(
            self,
            request: models.ModifyClustersAutoRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyClustersAutoRenewFlagResponse:
        """
        修改集群自动续费，只对预付费集群生效。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyClustersAutoRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyClustersAutoRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverCluster(
            self,
            request: models.RecoverClusterRequest,
            opts: Dict = None,
    ) -> models.RecoverClusterResponse:
        """
        恢复集群，恢复集群的接入点网络，恢复后继续连接使用数据库。只有当集群状态处于isolated(已隔离)时才生效。
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RecoverClusterInstances(
            self,
            request: models.RecoverClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.RecoverClusterInstancesResponse:
        """
        恢复实例。此接口的使用场景包括：
         - 读写实例状态为running(运行中)时，批量恢复状态为isolated(已隔离)的只读实例
         - 读写实例状态为isolated(已隔离)时，恢复读写实例
         - 读写实例状态为isolated(已隔离)时，批量恢复读写实例以及状态为isolated(已隔离)的只读实例
        """
        
        kwargs = {}
        kwargs["action"] = "RecoverClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RecoverClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewCluster(
            self,
            request: models.RenewClusterRequest,
            opts: Dict = None,
    ) -> models.RenewClusterResponse:
        """
        续费集群
        """
        
        kwargs = {}
        kwargs["action"] = "RenewCluster"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewClusterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAccountPassword(
            self,
            request: models.ResetAccountPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetAccountPasswordResponse:
        """
        重置数据库账号密码
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAccountPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAccountPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RestartClusterInstances(
            self,
            request: models.RestartClusterInstancesRequest,
            opts: Dict = None,
    ) -> models.RestartClusterInstancesResponse:
        """
        重启实例，此接口只针对状态为running(运行中)的实例生效。
        """
        
        kwargs = {}
        kwargs["action"] = "RestartClusterInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RestartClusterInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransformClusterPayMode(
            self,
            request: models.TransformClusterPayModeRequest,
            opts: Dict = None,
    ) -> models.TransformClusterPayModeResponse:
        """
        转换集群付费模式，目前只支持从 后付费 转换成 与预付费。
        """
        
        kwargs = {}
        kwargs["action"] = "TransformClusterPayMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransformClusterPayModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)