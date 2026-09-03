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
        
    async def BindClusterVpc(
            self,
            request: models.BindClusterVpcRequest,
            opts: Dict = None,
    ) -> models.BindClusterVpcResponse:
        """
        本接口 (BindClusterVpc) 用于为IDC集群绑定VPC和子网。

        * 绑定VPC后，集群可在该VPC内开启专线/VPN代理。
        * VpcId和SubnetId为必填参数，且子网必须属于指定的VPC。
        * 若集群已开通代理，需先关闭代理（DisableClusterDedicatedProxy）再变更VPC绑定。
        """
        
        kwargs = {}
        kwargs["action"] = "BindClusterVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindClusterVpcResponse
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
        
    async def CreateScheduledAction(
            self,
            request: models.CreateScheduledActionRequest,
            opts: Dict = None,
    ) -> models.CreateScheduledActionResponse:
        """
        为指定集群队列创建定时伸缩任务，按计划时间自动调整队列的节点数量。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateScheduledActionResponse
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
        
    async def DeleteScheduledAction(
            self,
            request: models.DeleteScheduledActionRequest,
            opts: Dict = None,
    ) -> models.DeleteScheduledActionResponse:
        """
        删除指定的定时伸缩任务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteScheduledActionResponse
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
        
    async def DescribeClusterDedicatedProxy(
            self,
            request: models.DescribeClusterDedicatedProxyRequest,
            opts: Dict = None,
    ) -> models.DescribeClusterDedicatedProxyResponse:
        """
        本接口 (DescribeClusterDedicatedProxy) 用于查询IDC集群专线/VPN代理的状态。

        * 返回终端节点（EndPoint）的当前状态，包括是否就绪、VIP地址等信息。
        * 若代理未开通，EndPointReady返回false，EndPointStatus为UNKNOWN。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClusterDedicatedProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClusterDedicatedProxyResponse
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
        
    async def DescribeInstanceFamilies(
            self,
            request: models.DescribeInstanceFamiliesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceFamiliesResponse:
        """
        查询指定集群可用的机型族列表，用于弹性伸缩配置时选择机型族。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceFamilies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceFamiliesResponse
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
        
    async def DescribeQueueAutoScaling(
            self,
            request: models.DescribeQueueAutoScalingRequest,
            opts: Dict = None,
    ) -> models.DescribeQueueAutoScalingResponse:
        """
        查询指定集群的队列弹性伸缩配置信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQueueAutoScaling"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQueueAutoScalingResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeQueueAutoScalingOverview(
            self,
            request: models.DescribeQueueAutoScalingOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeQueueAutoScalingOverviewResponse:
        """
        查询指定集群的队列弹性伸缩概览信息，包括期望容量、当前容量、当前动态节点数、有效定时任务数等。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeQueueAutoScalingOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeQueueAutoScalingOverviewResponse
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
        
    async def DescribeScheduledActions(
            self,
            request: models.DescribeScheduledActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeScheduledActionsResponse:
        """
        查询指定集群队列的定时伸缩任务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeScheduledActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeScheduledActionsResponse
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
        
    async def DisableClusterDedicatedProxy(
            self,
            request: models.DisableClusterDedicatedProxyRequest,
            opts: Dict = None,
    ) -> models.DisableClusterDedicatedProxyResponse:
        """
        本接口 (DisableClusterDedicatedProxy) 用于关闭IDC集群的专线/VPN代理。

        * 关闭后，系统将删除VPC终端节点（EndPoint），断开IDC集群与云上VPC的网络连接。
        * 若代理未开通，调用将返回ProxyNotEnabled错误。
        * 操作不可逆，关闭后需重新调用EnableClusterDedicatedProxy开启。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableClusterDedicatedProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableClusterDedicatedProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableClusterDedicatedProxy(
            self,
            request: models.EnableClusterDedicatedProxyRequest,
            opts: Dict = None,
    ) -> models.EnableClusterDedicatedProxyResponse:
        """
        本接口 (EnableClusterDedicatedProxy) 用于开启IDC集群的专线/VPN代理。

        * 开启后，系统将自动创建VPC终端节点（EndPoint），实现IDC集群与云上VPC的网络互通。
        * 若代理已开通，重复调用将幂等返回已有EndPoint信息。
        * SubnetId与VpcId需同时指定或同时不指定。若不指定，则使用集群已绑定的VPC和子网。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableClusterDedicatedProxy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableClusterDedicatedProxyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateRegisterCode(
            self,
            request: models.GenerateRegisterCodeRequest,
            opts: Dict = None,
    ) -> models.GenerateRegisterCodeResponse:
        """
        本接口(GenerateRegisterCode)用于为队列创建一个注册码，注册码用于IDC机器的注册纳管。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateRegisterCode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateRegisterCodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateRegisterCommand(
            self,
            request: models.GenerateRegisterCommandRequest,
            opts: Dict = None,
    ) -> models.GenerateRegisterCommandResponse:
        """
        本接口 (GenerateRegisterCommand) 用于生成IDC集群的节点注册命令。

        * 返回的注册命令可直接在IDC机器上以root身份执行，将该机器纳管进指定的IDC集群。
        * 当<code>Proxy=true</code>时，系统会先确保集群专线代理就绪（自动开启终端节点并轮询至ACTIVE），再签发注册码并渲染带代理VIP的注册命令；若在超时窗口内代理仍未就绪，将返回<code>FailedOperation.ProxyNotReady</code>。
        * 当<code>Proxy=false</code>时，IDC机器需可直连集群，直接签发注册码并渲染注册命令。
        * VpcId与SubnetId需同时指定或同时不指定；仅当<code>Proxy=true</code>且集群未绑定VPC时二者必填。当<code>Proxy=false</code>时二者不生效，若仍传入将返回<code>InvalidParameterValue.ParametersNotSupported</code>。
        * 若集群此前已开启专线代理并绑定了VPC/子网，本次传入的VpcId/SubnetId与已绑定值不一致时，将返回<code>UnsupportedOperation.VpcAlreadyBound</code>（不支持改绑）。
        * 仅支持IDC类型集群，对非IDC集群调用将返回<code>InvalidParameterValue.ParametersNotSupported</code>。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateRegisterCommand"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateRegisterCommandResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateWorkspaces(
            self,
            request: models.InquirePriceCreateWorkspacesRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateWorkspacesResponse:
        """
        本接口(InquirePriceCreateWorkspaces)用于创建实例询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateWorkspaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateWorkspacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceModifyWorkspacesChargeType(
            self,
            request: models.InquirePriceModifyWorkspacesChargeTypeRequest,
            opts: Dict = None,
    ) -> models.InquirePriceModifyWorkspacesChargeTypeResponse:
        """
        查询按量计费工作空间转换为包年包月的价格。不会创建订单或变更资源。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceModifyWorkspacesChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceModifyWorkspacesChargeTypeResponse
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
        
    async def ModifyNodeAttribute(
            self,
            request: models.ModifyNodeAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNodeAttributeResponse:
        """
        本接口用于修改节点属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNodeAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNodeAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyScheduledAction(
            self,
            request: models.ModifyScheduledActionRequest,
            opts: Dict = None,
    ) -> models.ModifyScheduledActionResponse:
        """
        修改指定的定时伸缩任务配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyScheduledAction"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyScheduledActionResponse
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
        
    async def ModifyWorkspacesChargeType(
            self,
            request: models.ModifyWorkspacesChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyWorkspacesChargeTypeResponse:
        """
        正式提交按量计费工作空间转包年包月订单。仅支持 ONLINE 且计费模式为 POSTPAID_BY_HOUR 的工作空间。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyWorkspacesChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyWorkspacesChargeTypeResponse
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
        
    async def SetQueueAutoScaling(
            self,
            request: models.SetQueueAutoScalingRequest,
            opts: Dict = None,
    ) -> models.SetQueueAutoScalingResponse:
        """
        为指定集群的队列配置弹性伸缩策略，包括伸缩容量、扩容方式等。
        """
        
        kwargs = {}
        kwargs["action"] = "SetQueueAutoScaling"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetQueueAutoScalingResponse
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