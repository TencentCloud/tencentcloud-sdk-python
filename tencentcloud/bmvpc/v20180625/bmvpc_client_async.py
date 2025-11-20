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
from tencentcloud.bmvpc.v20180625 import models
from typing import Dict


class BmvpcClient(AbstractClient):
    _apiVersion = '2018-06-25'
    _endpoint = 'bmvpc.tencentcloudapi.com'
    _service = 'bmvpc'

    async def AcceptVpcPeerConnection(
            self,
            request: models.AcceptVpcPeerConnectionRequest,
            opts: Dict = None,
    ) -> models.AcceptVpcPeerConnectionResponse:
        """
        接受黑石对等连接
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptVpcPeerConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptVpcPeerConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AsyncRegisterIps(
            self,
            request: models.AsyncRegisterIpsRequest,
            opts: Dict = None,
    ) -> models.AsyncRegisterIpsResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        批量注册虚拟IP，异步接口。通过接口来查询任务进度。每次请求最多注册256个IP
        """
        
        kwargs = {}
        kwargs["action"] = "AsyncRegisterIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AsyncRegisterIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindEipsToNatGateway(
            self,
            request: models.BindEipsToNatGatewayRequest,
            opts: Dict = None,
    ) -> models.BindEipsToNatGatewayResponse:
        """
        NAT网关绑定EIP接口，可将EIP绑定到NAT网关，该EIP作为访问外网的源IP地址，将流量发送到Internet
        """
        
        kwargs = {}
        kwargs["action"] = "BindEipsToNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindEipsToNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindIpsToNatGateway(
            self,
            request: models.BindIpsToNatGatewayRequest,
            opts: Dict = None,
    ) -> models.BindIpsToNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        可用于将子网的部分IP绑定到NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "BindIpsToNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindIpsToNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BindSubnetsToNatGateway(
            self,
            request: models.BindSubnetsToNatGatewayRequest,
            opts: Dict = None,
    ) -> models.BindSubnetsToNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        NAT网关绑定子网后，该子网内全部IP可出公网
        """
        
        kwargs = {}
        kwargs["action"] = "BindSubnetsToNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BindSubnetsToNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomerGateway(
            self,
            request: models.CreateCustomerGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateCustomerGatewayResponse:
        """
        90天无调用

        本接口（CreateCustomerGateway）用于创建对端网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomerGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomerGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDockerSubnetWithVlan(
            self,
            request: models.CreateDockerSubnetWithVlanRequest,
            opts: Dict = None,
    ) -> models.CreateDockerSubnetWithVlanResponse:
        """
        创建黑石Docker子网， 如果不指定VlanId，将会分配2000--2999范围的VlanId; 子网会关闭分布式网关
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDockerSubnetWithVlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDockerSubnetWithVlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHostedInterface(
            self,
            request: models.CreateHostedInterfaceRequest,
            opts: Dict = None,
    ) -> models.CreateHostedInterfaceResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        本接口（CreateHostedInterface）用于黑石托管机器加入带VLANID不为5的子网。

        1) 不能加入vlanId 为5的子网，只能加入VLANID范围为2000-2999的子网。
        2) 每台托管机器最多可以加入20个子网。
        3) 每次调用最多能支持传入10台托管机器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHostedInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHostedInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateInterfaces(
            self,
            request: models.CreateInterfacesRequest,
            opts: Dict = None,
    ) -> models.CreateInterfacesResponse:
        """
        物理机加入子网
        """
        
        kwargs = {}
        kwargs["action"] = "CreateInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGateway(
            self,
            request: models.CreateNatGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        创建NAT网关接口，可针对网段方式、子网全部IP、子网部分IP这三种方式创建NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicies(
            self,
            request: models.CreateRoutePoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePoliciesResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        创建黑石路由表的路由规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnet(
            self,
            request: models.CreateSubnetRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetResponse:
        """
        创建黑石私有网络的子网
        访问管理: 用户可以对VpcId进行授权操作。例如设置资源为["qcs::bmvpc:::unVpc/vpc-xxxxx"]
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVirtualSubnetWithVlan(
            self,
            request: models.CreateVirtualSubnetWithVlanRequest,
            opts: Dict = None,
    ) -> models.CreateVirtualSubnetWithVlanResponse:
        """
        创建黑石虚拟子网， 虚拟子网用于在黑石上创建虚拟网络，与黑石子网要做好规划。虚拟子网会分配2000-2999的VlanId。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVirtualSubnetWithVlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVirtualSubnetWithVlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpc(
            self,
            request: models.CreateVpcRequest,
            opts: Dict = None,
    ) -> models.CreateVpcResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        创建黑石私有网络
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcPeerConnection(
            self,
            request: models.CreateVpcPeerConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateVpcPeerConnectionResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        创建对等连接
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcPeerConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcPeerConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCustomerGateway(
            self,
            request: models.DeleteCustomerGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteCustomerGatewayResponse:
        """
        本接口（DeleteCustomerGateway）用于删除对端网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCustomerGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCustomerGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHostedInterface(
            self,
            request: models.DeleteHostedInterfaceRequest,
            opts: Dict = None,
    ) -> models.DeleteHostedInterfaceResponse:
        """
        本接口用于托管机器从VLANID不为5的子网中移除。
        1) 不能从vlanId 为5的子网中移除。
        2) 每次调用最多能支持传入10台物理机。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHostedInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHostedInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHostedInterfaces(
            self,
            request: models.DeleteHostedInterfacesRequest,
            opts: Dict = None,
    ) -> models.DeleteHostedInterfacesResponse:
        """
        托管机器移除子网批量接口，传入一台托管机器和多个子网，批量移除这些子网。异步接口，接口返回TaskId。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHostedInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHostedInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteInterfaces(
            self,
            request: models.DeleteInterfacesRequest,
            opts: Dict = None,
    ) -> models.DeleteInterfacesResponse:
        """
        物理机移除子网批量接口，传入一台物理机和多个子网，批量移除这些子网。异步接口，接口返回TaskId。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGateway(
            self,
            request: models.DeleteNatGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        删除NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicy(
            self,
            request: models.DeleteRoutePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        删除黑石路由表路由规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubnet(
            self,
            request: models.DeleteSubnetRequest,
            opts: Dict = None,
    ) -> models.DeleteSubnetResponse:
        """
        本接口（DeleteSubnet）用于删除黑石私有网络子网。
        删除子网前，请清理该子网下所有资源，包括物理机、负载均衡、黑石数据库、弹性IP、NAT网关等资源
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVirtualIp(
            self,
            request: models.DeleteVirtualIpRequest,
            opts: Dict = None,
    ) -> models.DeleteVirtualIpResponse:
        """
        退还虚拟IP。此接口只能退还虚拟IP，物理机IP不能退还。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVirtualIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVirtualIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpc(
            self,
            request: models.DeleteVpcRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcResponse:
        """
        本接口(DeleteVpc)用于删除黑石私有网络(VPC)。

        删除私有网络前，请清理该私有网络下所有资源，包括子网、负载均衡、弹性 IP、对等连接、NAT 网关、专线通道、SSLVPN 等资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcPeerConnection(
            self,
            request: models.DeleteVpcPeerConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcPeerConnectionResponse:
        """
        删除黑石对等连接
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcPeerConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcPeerConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnConnection(
            self,
            request: models.DeleteVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnConnectionResponse:
        """
        本接口(DeleteVpnConnection)用于删除VPN通道。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnGateway(
            self,
            request: models.DeleteVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnGatewayResponse:
        """
        本接口（DeleteVpnGateway）用于删除VPN网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeregisterIps(
            self,
            request: models.DeregisterIpsRequest,
            opts: Dict = None,
    ) -> models.DeregisterIpsResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        注销私有网络IP为空闲
        """
        
        kwargs = {}
        kwargs["action"] = "DeregisterIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeregisterIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerGateways(
            self,
            request: models.DescribeCustomerGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerGatewaysResponse:
        """
        本接口（DescribeCustomerGateways）用于查询对端网关列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGateways(
            self,
            request: models.DescribeNatGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewaysResponse:
        """
        获取NAT网关信息，包括NAT网关 ID、网关名称、私有网络、网关并发连接上限、绑定EIP列表等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatSubnets(
            self,
            request: models.DescribeNatSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeNatSubnetsResponse:
        """
        可获取NAT网关绑定的子网信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoutePolicies(
            self,
            request: models.DescribeRoutePoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeRoutePoliciesResponse:
        """
        本接口（DescribeRoutePolicies）用于查询路由表条目。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoutePolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoutePoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTables(
            self,
            request: models.DescribeRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTablesResponse:
        """
        本接口（DescribeRouteTables）用于查询路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetAvailableIps(
            self,
            request: models.DescribeSubnetAvailableIpsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetAvailableIpsResponse:
        """
        获取子网内可用IP列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetAvailableIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetAvailableIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetByDevice(
            self,
            request: models.DescribeSubnetByDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetByDeviceResponse:
        """
        物理机可以加入物理机子网，虚拟子网，DOCKER子网，通过此接口可以查询物理机加入的子网。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetByDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetByDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetByHostedDevice(
            self,
            request: models.DescribeSubnetByHostedDeviceRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetByHostedDeviceResponse:
        """
        托管可以加入物理机子网，虚拟子网，DOCKER子网，通过此接口可以查询托管加入的子网。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetByHostedDevice"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetByHostedDeviceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnets(
            self,
            request: models.DescribeSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetsResponse:
        """
        本接口（DescribeSubnets）用于查询黑石子网列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        根据任务ID，获取任务的执行状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcPeerConnections(
            self,
            request: models.DescribeVpcPeerConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcPeerConnectionsResponse:
        """
        获取对等连接列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcPeerConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcPeerConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcQuota(
            self,
            request: models.DescribeVpcQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcQuotaResponse:
        """
        本接口（DescribeVpcQuota）用于查询用户VPC相关配额限制。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcResource(
            self,
            request: models.DescribeVpcResourceRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcResourceResponse:
        """
        查询黑石私有网络关联资源
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcResource"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcResourceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcView(
            self,
            request: models.DescribeVpcViewRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcViewResponse:
        """
        本接口（DescribeVpcView）用于查询VPC网络拓扑视图。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcView"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcViewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcs(
            self,
            request: models.DescribeVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcsResponse:
        """
        本接口（DescribeVpcs）用于查询私有网络列表。
        本接口不传参数时，返回默认排序下的前20条VPC信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnConnections(
            self,
            request: models.DescribeVpnConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnConnectionsResponse:
        """
        本接口（DescribeVpnConnections）查询VPN通道列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGateways(
            self,
            request: models.DescribeVpnGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewaysResponse:
        """
        本接口（DescribeVpnGateways）用于查询VPN网关列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadCustomerGatewayConfiguration(
            self,
            request: models.DownloadCustomerGatewayConfigurationRequest,
            opts: Dict = None,
    ) -> models.DownloadCustomerGatewayConfigurationResponse:
        """
        90天无调用

        本接口(DownloadCustomerGatewayConfiguration)用于下载VPN通道配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadCustomerGatewayConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadCustomerGatewayConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCustomerGatewayAttribute(
            self,
            request: models.ModifyCustomerGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCustomerGatewayAttributeResponse:
        """
        本接口（ModifyCustomerGatewayAttribute）用于修改对端网关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCustomerGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCustomerGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoutePolicy(
            self,
            request: models.ModifyRoutePolicyRequest,
            opts: Dict = None,
    ) -> models.ModifyRoutePolicyResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        修改自定义路由
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoutePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoutePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRouteTable(
            self,
            request: models.ModifyRouteTableRequest,
            opts: Dict = None,
    ) -> models.ModifyRouteTableResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        修改路由表
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubnetAttribute(
            self,
            request: models.ModifySubnetAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySubnetAttributeResponse:
        """
        修改子网属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubnetAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubnetAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubnetDHCPRelay(
            self,
            request: models.ModifySubnetDHCPRelayRequest,
            opts: Dict = None,
    ) -> models.ModifySubnetDHCPRelayResponse:
        """
        修改子网DHCP Relay属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubnetDHCPRelay"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubnetDHCPRelayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAttribute(
            self,
            request: models.ModifyVpcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAttributeResponse:
        """
        本接口（ModifyVpcAttribute）用于修改VPC的标识名称和控制VPC的监控起停。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcPeerConnection(
            self,
            request: models.ModifyVpcPeerConnectionRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcPeerConnectionResponse:
        """
        修改黑石对等连接
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcPeerConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcPeerConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnConnectionAttribute(
            self,
            request: models.ModifyVpnConnectionAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnConnectionAttributeResponse:
        """
        本接口（ModifyVpnConnectionAttribute）用于修改VPN通道。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnConnectionAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnConnectionAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewayAttribute(
            self,
            request: models.ModifyVpnGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewayAttributeResponse:
        """
        本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectVpcPeerConnection(
            self,
            request: models.RejectVpcPeerConnectionRequest,
            opts: Dict = None,
    ) -> models.RejectVpcPeerConnectionResponse:
        """
        拒绝黑石对等连接申请
        """
        
        kwargs = {}
        kwargs["action"] = "RejectVpcPeerConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectVpcPeerConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetVpnConnection(
            self,
            request: models.ResetVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.ResetVpnConnectionResponse:
        """
        本接口(ResetVpnConnection)用于重置VPN通道。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindEipsFromNatGateway(
            self,
            request: models.UnbindEipsFromNatGatewayRequest,
            opts: Dict = None,
    ) -> models.UnbindEipsFromNatGatewayResponse:
        """
        NAT网关解绑该EIP后，NAT网关将不会使用该EIP作为访问外网的源IP地址
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindEipsFromNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindEipsFromNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindIpsFromNatGateway(
            self,
            request: models.UnbindIpsFromNatGatewayRequest,
            opts: Dict = None,
    ) -> models.UnbindIpsFromNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        NAT网关解绑IP接口，可将子网的部分IP从NAT网关中解绑
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindIpsFromNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindIpsFromNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnbindSubnetsFromNatGateway(
            self,
            request: models.UnbindSubnetsFromNatGatewayRequest,
            opts: Dict = None,
    ) -> models.UnbindSubnetsFromNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        NAT网关解绑子网接口，可将子网解绑NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "UnbindSubnetsFromNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnbindSubnetsFromNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpgradeNatGateway(
            self,
            request: models.UpgradeNatGatewayRequest,
            opts: Dict = None,
    ) -> models.UpgradeNatGatewayResponse:
        """
        黑石1.0接口，业务已下线，90天无调用

        升级NAT网关接口，可NAT网关修改为小型NAT网关、中型NAT网关、以及大型NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "UpgradeNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpgradeNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)