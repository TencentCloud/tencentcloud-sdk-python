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
from tencentcloud.cdwch.v20200915 import models
from typing import Dict


class CdwchClient(AbstractClient):
    _apiVersion = '2020-09-15'
    _endpoint = 'cdwch.tencentcloudapi.com'
    _service = 'cdwch'

    async def ActionAlterCkUser(
            self,
            request: models.ActionAlterCkUserRequest,
            opts: Dict = None,
    ) -> models.ActionAlterCkUserResponse:
        """
        新增和修改用户接口
        """
        
        kwargs = {}
        kwargs["action"] = "ActionAlterCkUser"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ActionAlterCkUserResponse
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
        
    async def CreateInstanceNew(
            self,
            request: models.CreateInstanceNewRequest,
            opts: Dict = None,
    ) -> models.CreateInstanceNewResponse:
        """
        创建集群
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInstanceNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInstanceNewResponse
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
        
    async def DescribeBackUpJob(
            self,
            request: models.DescribeBackUpJobRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpJobResponse:
        """
        查询备份任务列表
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
        
    async def DescribeBackUpSchedule(
            self,
            request: models.DescribeBackUpScheduleRequest,
            opts: Dict = None,
    ) -> models.DescribeBackUpScheduleResponse:
        """
        查询备份策略信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBackUpSchedule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBackUpScheduleResponse
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
        
    async def DescribeCNInstances(
            self,
            request: models.DescribeCNInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeCNInstancesResponse:
        """
        获取云原生实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCNInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCNInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCkSqlApis(
            self,
            request: models.DescribeCkSqlApisRequest,
            opts: Dict = None,
    ) -> models.DescribeCkSqlApisResponse:
        """
        查询集群用户、集群表，数据库等相关信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCkSqlApis"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCkSqlApisResponse
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
        
    async def DescribeInstance(
            self,
            request: models.DescribeInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceResponse:
        """
        根据实例ID查询某个实例的具体信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceClusters(
            self,
            request: models.DescribeInstanceClustersRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceClustersResponse:
        """
        集群vcluster列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceClusters"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceClustersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceKeyValConfigs(
            self,
            request: models.DescribeInstanceKeyValConfigsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceKeyValConfigsResponse:
        """
        在集群详情页面获取所有参数列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceKeyValConfigs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceKeyValConfigsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceNodes(
            self,
            request: models.DescribeInstanceNodesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceNodesResponse:
        """
        获取实例节点信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceNodes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceNodesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceShards(
            self,
            request: models.DescribeInstanceShardsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceShardsResponse:
        """
        获取实例shard信息列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceShards"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceShardsResponse
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
        
    async def DescribeInstancesNew(
            self,
            request: models.DescribeInstancesNewRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesNewResponse:
        """
        获取实例列表，供外部sdk使用
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesNew"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesNewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpec(
            self,
            request: models.DescribeSpecRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecResponse:
        """
        购买页拉取集群的数据节点和zookeeper节点的规格列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpec"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DestroyInstance(
            self,
            request: models.DestroyInstanceRequest,
            opts: Dict = None,
    ) -> models.DestroyInstanceResponse:
        """
        销毁集群 open api
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
        
    async def ModifyUserNewPrivilege(
            self,
            request: models.ModifyUserNewPrivilegeRequest,
            opts: Dict = None,
    ) -> models.ModifyUserNewPrivilegeResponse:
        """
        针对集群账号的权限做管控（新版）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyUserNewPrivilege"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyUserNewPrivilegeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def OpenBackUp(
            self,
            request: models.OpenBackUpRequest,
            opts: Dict = None,
    ) -> models.OpenBackUpResponse:
        """
        开启或者关闭策略
        """
        
        kwargs = {}
        kwargs["action"] = "OpenBackUp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.OpenBackUpResponse
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
        
    async def ResizeDisk(
            self,
            request: models.ResizeDiskRequest,
            opts: Dict = None,
    ) -> models.ResizeDiskResponse:
        """
        扩容磁盘，包含扩容数据节点，zk节点
        """
        
        kwargs = {}
        kwargs["action"] = "ResizeDisk"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResizeDiskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleCNOutUpInstance(
            self,
            request: models.ScaleCNOutUpInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleCNOutUpInstanceResponse:
        """
        open-api接口提供弹性伸缩云原生集群能力
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleCNOutUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleCNOutUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ScaleOutInstance(
            self,
            request: models.ScaleOutInstanceRequest,
            opts: Dict = None,
    ) -> models.ScaleOutInstanceResponse:
        """
        调整clickhouse节点数量
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
        垂直扩缩容节点规格，修改节点cvm的规格cpu，内存。 规格变化阶段，服务不可用。
        """
        
        kwargs = {}
        kwargs["action"] = "ScaleUpInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ScaleUpInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)