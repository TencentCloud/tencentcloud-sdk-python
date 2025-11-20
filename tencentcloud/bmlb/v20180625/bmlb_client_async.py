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
from tencentcloud.bmlb.v20180625 import models
from typing import Dict


class BmlbClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmlb.tencentcloudapi.com'
    _service = 'bmlb'

    async def BindL4Backends(
            self,
            request: models.BindL4BackendsRequest,
            opts: Dict = None,
    ) -> models.BindL4BackendsResponse:
        """
        绑定黑石服务器到四层监听器。服务器包括物理服务器、虚拟机以及半托管机器。
        """
        
        kwargs = {}
        kwargs["action"] = "BindL4Backends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindL4BackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindL7Backends(
            self,
            request: models.BindL7BackendsRequest,
            opts: Dict = None,
    ) -> models.BindL7BackendsResponse:
        """
        绑定黑石物理服务器或半托管服务器到七层转发路径。
        """
        
        kwargs = {}
        kwargs["action"] = "BindL7Backends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindL7BackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindTrafficMirrorListeners(
            self,
            request: models.BindTrafficMirrorListenersRequest,
            opts: Dict = None,
    ) -> models.BindTrafficMirrorListenersResponse:
        """
        绑定黑石服务器七层监听器到流量镜像实例。
        """
        
        kwargs = {}
        kwargs["action"] = "BindTrafficMirrorListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindTrafficMirrorListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindTrafficMirrorReceivers(
            self,
            request: models.BindTrafficMirrorReceiversRequest,
            opts: Dict = None,
    ) -> models.BindTrafficMirrorReceiversResponse:
        """
        绑定黑石物理服务器成为流量镜像接收机。
        """
        
        kwargs = {}
        kwargs["action"] = "BindTrafficMirrorReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindTrafficMirrorReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL4Listeners(
            self,
            request: models.CreateL4ListenersRequest,
            opts: Dict = None,
    ) -> models.CreateL4ListenersResponse:
        """
        创建黑石四层负载均衡监听器功能。黑石负载均衡四层监听器提供了转发用户请求的具体规则，包括端口、协议、会话保持、健康检查等参数。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL4Listeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL4ListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7Listeners(
            self,
            request: models.CreateL7ListenersRequest,
            opts: Dict = None,
    ) -> models.CreateL7ListenersResponse:
        """
        创建黑石负载均衡七层监听器功能。负载均衡七层监听器提供了转发用户请求的具体规则，包括端口、协议等参数。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7Listeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7ListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateL7Rules(
            self,
            request: models.CreateL7RulesRequest,
            opts: Dict = None,
    ) -> models.CreateL7RulesResponse:
        """
        创建黑石负载均衡七层转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancers(
            self,
            request: models.CreateLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancersResponse:
        """
        用来创建黑石负载均衡。为了使用黑石负载均衡服务，您必须要创建一个或者多个负载均衡实例。通过成功调用该接口，会返回负载均衡实例的唯一ID。用户可以购买的黑石负载均衡实例类型分为：公网类型、内网类型。公网类型负载均衡对应一个BGP VIP，可用于快速访问公网负载均衡绑定的物理服务器；内网类型负载均衡对应一个腾讯云内部的VIP，不能通过Internet访问，可快速访问内网负载均衡绑定的物理服务器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrafficMirror(
            self,
            request: models.CreateTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.CreateTrafficMirrorResponse:
        """
        创建流量镜像实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL7Domains(
            self,
            request: models.DeleteL7DomainsRequest,
            opts: Dict = None,
    ) -> models.DeleteL7DomainsResponse:
        """
        删除黑石负载均衡七层转发域名。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL7Domains"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL7DomainsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteL7Rules(
            self,
            request: models.DeleteL7RulesRequest,
            opts: Dict = None,
    ) -> models.DeleteL7RulesResponse:
        """
        删除黑石负载均衡七层转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListeners(
            self,
            request: models.DeleteListenersRequest,
            opts: Dict = None,
    ) -> models.DeleteListenersResponse:
        """
        删除黑石负载均衡监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancer(
            self,
            request: models.DeleteLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerResponse:
        """
        删除用户指定的黑石负载均衡实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrafficMirror(
            self,
            request: models.DeleteTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.DeleteTrafficMirrorResponse:
        """
        删除已创建的黑石流量镜像实例，删除过程是异步执行的，因此需要使用查询任务接口获取删除的结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCertDetail(
            self,
            request: models.DescribeCertDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeCertDetailResponse:
        """
        获取黑石负载均衡证书详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCertDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCertDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDevicesBindInfo(
            self,
            request: models.DescribeDevicesBindInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeDevicesBindInfoResponse:
        """
        查询黑石物理机和虚机以及托管服务器绑定的黑石负载均衡详情。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDevicesBindInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDevicesBindInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4Backends(
            self,
            request: models.DescribeL4BackendsRequest,
            opts: Dict = None,
    ) -> models.DescribeL4BackendsResponse:
        """
        获取黑石负载均衡四层监听器绑定的主机列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4Backends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4BackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4ListenerInfo(
            self,
            request: models.DescribeL4ListenerInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeL4ListenerInfoResponse:
        """
        查找绑定了某主机或者指定监听器名称的黑石负载均衡四层监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4ListenerInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4ListenerInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL4Listeners(
            self,
            request: models.DescribeL4ListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeL4ListenersResponse:
        """
        获取黑石负载均衡四层监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL4Listeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL4ListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7Backends(
            self,
            request: models.DescribeL7BackendsRequest,
            opts: Dict = None,
    ) -> models.DescribeL7BackendsResponse:
        """
        获取黑石负载均衡七层监听器绑定的主机列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7Backends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7BackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7ListenerInfo(
            self,
            request: models.DescribeL7ListenerInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeL7ListenerInfoResponse:
        """
        查找绑定了某主机或者有某转发域名黑石负载均衡七层监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7ListenerInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7ListenerInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7Listeners(
            self,
            request: models.DescribeL7ListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeL7ListenersResponse:
        """
        获取黑石负载均衡七层监听器列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7Listeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7ListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7ListenersEx(
            self,
            request: models.DescribeL7ListenersExRequest,
            opts: Dict = None,
    ) -> models.DescribeL7ListenersExResponse:
        """
        获取指定VPC下的7层监听器(支持模糊匹配)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7ListenersEx"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7ListenersExResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeL7Rules(
            self,
            request: models.DescribeL7RulesRequest,
            opts: Dict = None,
    ) -> models.DescribeL7RulesResponse:
        """
        获取黑石负载均衡七层转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeL7Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeL7RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerPortInfo(
            self,
            request: models.DescribeLoadBalancerPortInfoRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerPortInfoResponse:
        """
        获取黑石负载均衡端口相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerPortInfo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerPortInfoResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancerTaskResult(
            self,
            request: models.DescribeLoadBalancerTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancerTaskResultResponse:
        """
        查询负载均衡实例异步任务的执行情况。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancerTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancerTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancers(
            self,
            request: models.DescribeLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersResponse:
        """
        获取黑石负载均衡实例列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficMirrorListeners(
            self,
            request: models.DescribeTrafficMirrorListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficMirrorListenersResponse:
        """
        获取流量镜像的监听器列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficMirrorListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficMirrorListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficMirrorReceiverHealthStatus(
            self,
            request: models.DescribeTrafficMirrorReceiverHealthStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficMirrorReceiverHealthStatusResponse:
        """
        获取流量镜像接收机健康状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficMirrorReceiverHealthStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficMirrorReceiverHealthStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficMirrorReceivers(
            self,
            request: models.DescribeTrafficMirrorReceiversRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficMirrorReceiversResponse:
        """
        获取指定流量镜像实例的接收机信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficMirrorReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficMirrorReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficMirrors(
            self,
            request: models.DescribeTrafficMirrorsRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficMirrorsResponse:
        """
        获取流量镜像实例的列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficMirrors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficMirrorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4BackendPort(
            self,
            request: models.ModifyL4BackendPortRequest,
            opts: Dict = None,
    ) -> models.ModifyL4BackendPortResponse:
        """
        修改黑石负载均衡四层监听器后端实例端口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4BackendPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4BackendPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4BackendProbePort(
            self,
            request: models.ModifyL4BackendProbePortRequest,
            opts: Dict = None,
    ) -> models.ModifyL4BackendProbePortResponse:
        """
        修改黑石负载均衡四层监听器后端探测端口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4BackendProbePort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4BackendProbePortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4BackendWeight(
            self,
            request: models.ModifyL4BackendWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyL4BackendWeightResponse:
        """
        修改黑石负载均衡四层监听器后端实例权重功能。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4BackendWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4BackendWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL4Listener(
            self,
            request: models.ModifyL4ListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyL4ListenerResponse:
        """
        修改黑石负载均衡四层监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL4Listener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL4ListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7BackendPort(
            self,
            request: models.ModifyL7BackendPortRequest,
            opts: Dict = None,
    ) -> models.ModifyL7BackendPortResponse:
        """
        修改黑石负载均衡七层转发路径后端实例端口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7BackendPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7BackendPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7BackendWeight(
            self,
            request: models.ModifyL7BackendWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyL7BackendWeightResponse:
        """
        修改黑石负载均衡七层转发路径后端实例权重。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7BackendWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7BackendWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7Listener(
            self,
            request: models.ModifyL7ListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyL7ListenerResponse:
        """
        修改黑石负载均衡七层监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7Listener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7ListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyL7Locations(
            self,
            request: models.ModifyL7LocationsRequest,
            opts: Dict = None,
    ) -> models.ModifyL7LocationsResponse:
        """
        修改黑石负载均衡七层转发路径。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyL7Locations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyL7LocationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancer(
            self,
            request: models.ModifyLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerResponse:
        """
        根据输入参数来修改黑石负载均衡实例的基本配置信息。可能的信息包括负载均衡实例的名称，域名前缀。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerChargeMode(
            self,
            request: models.ModifyLoadBalancerChargeModeRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerChargeModeResponse:
        """
        更改黑石负载均衡的计费方式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerChargeMode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerChargeModeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceCert(
            self,
            request: models.ReplaceCertRequest,
            opts: Dict = None,
    ) -> models.ReplaceCertResponse:
        """
        更新黑石负载均衡证书。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTrafficMirrorAlias(
            self,
            request: models.SetTrafficMirrorAliasRequest,
            opts: Dict = None,
    ) -> models.SetTrafficMirrorAliasResponse:
        """
        设置流量镜像的别名。
        """
        
        kwargs = {}
        kwargs["action"] = "SetTrafficMirrorAlias"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTrafficMirrorAliasResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetTrafficMirrorHealthSwitch(
            self,
            request: models.SetTrafficMirrorHealthSwitchRequest,
            opts: Dict = None,
    ) -> models.SetTrafficMirrorHealthSwitchResponse:
        """
        设置流量镜像的健康检查参数。
        """
        
        kwargs = {}
        kwargs["action"] = "SetTrafficMirrorHealthSwitch"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetTrafficMirrorHealthSwitchResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindL4Backends(
            self,
            request: models.UnbindL4BackendsRequest,
            opts: Dict = None,
    ) -> models.UnbindL4BackendsResponse:
        """
        解绑黑石负载均衡四层监听器物理服务器。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindL4Backends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindL4BackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindL7Backends(
            self,
            request: models.UnbindL7BackendsRequest,
            opts: Dict = None,
    ) -> models.UnbindL7BackendsResponse:
        """
        解绑黑石物理服务器或者托管服务器到七层转发路径功能。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindL7Backends"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindL7BackendsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindTrafficMirrorListeners(
            self,
            request: models.UnbindTrafficMirrorListenersRequest,
            opts: Dict = None,
    ) -> models.UnbindTrafficMirrorListenersResponse:
        """
        解绑流量镜像监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindTrafficMirrorListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindTrafficMirrorListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindTrafficMirrorReceivers(
            self,
            request: models.UnbindTrafficMirrorReceiversRequest,
            opts: Dict = None,
    ) -> models.UnbindTrafficMirrorReceiversResponse:
        """
        从流量镜像实例上解绑流量镜像接收机。
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindTrafficMirrorReceivers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindTrafficMirrorReceiversResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UploadCert(
            self,
            request: models.UploadCertRequest,
            opts: Dict = None,
    ) -> models.UploadCertResponse:
        """
        创建黑石负载均衡证书。
        """
        
        kwargs = {}
        kwargs["action"] = "UploadCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UploadCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)