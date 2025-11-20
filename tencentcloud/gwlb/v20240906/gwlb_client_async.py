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
from tencentcloud.gwlb.v20240906 import models
from typing import Dict


class GwlbClient(AbstractClient):
    _apiVersion = '2024-09-06'
    _endpoint = 'gwlb.tencentcloudapi.com'
    _service = 'gwlb'

    async def AssociateTargetGroups(
            self,
            request: models.AssociateTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateTargetGroupsResponse:
        """
        本接口(AssociateTargetGroups)用来将目标组绑定到负载均衡。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 [DescribeTaskStatus](https://cloud.tencent.com/document/product/214/30683) 接口查询本次任务是否成功。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGatewayLoadBalancer(
            self,
            request: models.CreateGatewayLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateGatewayLoadBalancerResponse:
        """
        本接口(CreateGatewayLoadBalancer)用来创建网关负载均衡实例。为了使用网关负载均衡服务，您必须购买一个或多个网关负载均衡实例。成功调用该接口后，会返回网关负载均衡实例的唯一 ID。
        注意：单个账号在每个地域的默认购买配额为：10个。
        本接口为异步接口，接口成功返回后，可使用 [DescribeTaskStatus](https://cloud.tencent.com/document/api/1782/111700) 接口查询负载均衡实例的状态。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGatewayLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGatewayLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTargetGroup(
            self,
            request: models.CreateTargetGroupRequest,
            opts: Dict = None,
    ) -> models.CreateTargetGroupResponse:
        """
        创建目标组。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTargetGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTargetGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGatewayLoadBalancer(
            self,
            request: models.DeleteGatewayLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteGatewayLoadBalancerResponse:
        """
        DeleteGatewayLoadBalancer 接口用以删除指定的一个或多个网关负载均衡实例。成功删除后，会把网关负载均衡实例与后端服务解绑。
        本接口为异步接口，接口返回成功后，需以返回的 RequestId 为入参，调用 [DescribeTaskStatus](https://cloud.tencent.com/document/api/1782/111700) 接口查询本次任务是否成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGatewayLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGatewayLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTargetGroups(
            self,
            request: models.DeleteTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DeleteTargetGroupsResponse:
        """
        删除目标组
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeregisterTargetGroupInstances(
            self,
            request: models.DeregisterTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DeregisterTargetGroupInstancesResponse:
        """
        从目标组中解绑服务器。
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayLoadBalancers(
            self,
            request: models.DescribeGatewayLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayLoadBalancersResponse:
        """
        查询一个地域的网关负载均衡实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayLoadBalancersResources(
            self,
            request: models.DescribeGatewayLoadBalancersResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayLoadBalancersResourcesResponse:
        """
        查询用户在当前地域支持可用区列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayLoadBalancersResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayLoadBalancersResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupInstanceStatus(
            self,
            request: models.DescribeTargetGroupInstanceStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupInstanceStatusResponse:
        """
        查询目标组后端服务状态。目前仅支持网关负载均衡类型的目标组支持查询后端服务状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupInstanceStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupInstanceStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupInstances(
            self,
            request: models.DescribeTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupInstancesResponse:
        """
        获取目标组绑定的服务器信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroupList(
            self,
            request: models.DescribeTargetGroupListRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupListResponse:
        """
        获取目标组列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroupList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetGroups(
            self,
            request: models.DescribeTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetGroupsResponse:
        """
        查询目标组信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        本接口用于查询异步任务的执行状态，对于非查询类的接口（创建/删除负载均衡实例等），在接口调用成功后，都需要使用本接口查询任务最终是否执行成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateTargetGroups(
            self,
            request: models.DisassociateTargetGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateTargetGroupsResponse:
        """
        解除负载均衡和目标组的关联关系。
        本接口为异步接口，本接口返回成功后需以返回的 RequestID 为入参，调用 [DescribeTaskStatus](https://cloud.tencent.com/document/product/214/30683) 接口查询本次任务是否成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateTargetGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateTargetGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateGatewayLoadBalancer(
            self,
            request: models.InquirePriceCreateGatewayLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateGatewayLoadBalancerResponse:
        """
        InquirePriceCreateGatewayLoadBalancer接口查询创建网关负载均衡的价格。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateGatewayLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateGatewayLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatewayLoadBalancerAttribute(
            self,
            request: models.ModifyGatewayLoadBalancerAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyGatewayLoadBalancerAttributeResponse:
        """
        ModifyGatewayLoadBalancerAttribute 接口用于修改负载均衡实例的属性。支持修改负载均衡实例的名称、带宽上限。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatewayLoadBalancerAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatewayLoadBalancerAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupAttribute(
            self,
            request: models.ModifyTargetGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupAttributeResponse:
        """
        修改目标组的名称、健康探测等属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetGroupInstancesWeight(
            self,
            request: models.ModifyTargetGroupInstancesWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetGroupInstancesWeightResponse:
        """
        修改目标组的服务器权重。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetGroupInstancesWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetGroupInstancesWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RegisterTargetGroupInstances(
            self,
            request: models.RegisterTargetGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.RegisterTargetGroupInstancesResponse:
        """
        注册服务器到目标组。
        """
        
        kwargs = {}
        kwargs["action"] = "RegisterTargetGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RegisterTargetGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)