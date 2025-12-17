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
from tencentcloud.vpc.v20170312 import models
from typing import Dict


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.tencentcloudapi.com'
    _service = 'vpc'

    async def AcceptAttachCcnInstances(
            self,
            request: models.AcceptAttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.AcceptAttachCcnInstancesResponse:
        """
        本接口（AcceptAttachCcnInstances）用于跨账号关联实例时，云联网所有者接受并同意关联操作。
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptAttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptAttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AcceptVpcPeeringConnection(
            self,
            request: models.AcceptVpcPeeringConnectionRequest,
            opts: Dict = None,
    ) -> models.AcceptVpcPeeringConnectionResponse:
        """
        本接口（AcceptVpcPeeringConnection）用于接受对等连接请求。
        """
        
        kwargs = {}
        kwargs["action"] = "AcceptVpcPeeringConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AcceptVpcPeeringConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddBandwidthPackageResources(
            self,
            request: models.AddBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.AddBandwidthPackageResourcesResponse:
        """
        接口用于添加带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等
        """
        
        kwargs = {}
        kwargs["action"] = "AddBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddIp6Rules(
            self,
            request: models.AddIp6RulesRequest,
            opts: Dict = None,
    ) -> models.AddIp6RulesResponse:
        """
        1. 该接口用于在转换实例下添加IPV6转换规则。
        2. 支持在同一个转换实例下批量添加转换规则，一个账户在一个地域最多50个。
        3. 一个完整的转换规则包括vip6:vport6:protocol:vip:vport，其中vip6:vport6:protocol必须是唯一。
        """
        
        kwargs = {}
        kwargs["action"] = "AddIp6Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddIp6RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AddTemplateMember(
            self,
            request: models.AddTemplateMemberRequest,
            opts: Dict = None,
    ) -> models.AddTemplateMemberResponse:
        """
        增加模板对象中的IP地址、协议端口、IP地址组、协议端口组。
        """
        
        kwargs = {}
        kwargs["action"] = "AddTemplateMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AddTemplateMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AdjustPublicAddress(
            self,
            request: models.AdjustPublicAddressRequest,
            opts: Dict = None,
    ) -> models.AdjustPublicAddressResponse:
        """
        本接口 (AdjustPublicAddress) 用于更换IP地址，支持更换CVM实例的普通公网IP和包月带宽的EIP。
        """
        
        kwargs = {}
        kwargs["action"] = "AdjustPublicAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AdjustPublicAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateAddresses(
            self,
            request: models.AllocateAddressesRequest,
            opts: Dict = None,
    ) -> models.AllocateAddressesResponse:
        """
        本接口 (AllocateAddresses) 用于申请一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * EIP 是专为动态云计算设计的静态 IP 地址。借助 EIP，您可以快速将 EIP 重新映射到您的另一个实例上，从而屏蔽实例故障。
        * 您的 EIP 与腾讯云账户相关联，而不是与某个实例相关联。在您选择显式释放该地址，或欠费超过24小时之前，它会一直与您的腾讯云账户保持关联。
        * 一个腾讯云账户在每个地域能申请的 EIP 最大配额有所限制，可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)，上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/product/215/16701) 接口获取。
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateIPv6Addresses(
            self,
            request: models.AllocateIPv6AddressesRequest,
            opts: Dict = None,
    ) -> models.AllocateIPv6AddressesResponse:
        """
        本接口（AllocateIPv6Addresses）用于申请一个或多个弹性公网IPv6（简称EIPv6）实例。

        - EIPv6 是您在腾讯云某个地域可以独立申请和持有的，固定不变的公网 IPv6 地址，提供与弹性公网 IPv4 一致的产品体验。
        - 通过弹性公网 IPv6，您可以快速将 EIPv6 实例绑定到云资源的内网 IPv6 地址上，实现为云资源快速开通 IPv6 公网带宽。
        - 您还可以按需将 EIPv6 实例绑定到其他云资源上，从而屏蔽实例故障。
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateIPv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateIPv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateIp6AddressesBandwidth(
            self,
            request: models.AllocateIp6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.AllocateIp6AddressesBandwidthResponse:
        """
        本接口（AllocateIp6AddressesBandwidth）用于为传统弹性公网 IPv6 地址开通 IPv6 公网带宽。

        - 传统弹性公网 IPv6 地址默认仅具备内网通信能力，需通过控制台或 API 接口为其分配公网带宽后，才能具备 IPv6 公网通信能力、并于传统弹性公网 IPv6 列表页可见。
        - 支持为一个或多个传统弹性公网 IPv6 实例开通公网带宽。
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateIp6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateIp6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6Addresses(
            self,
            request: models.AssignIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6AddressesResponse:
        """
        本接口（AssignIpv6Addresses）用于弹性网卡申请`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)接口。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 可以指定`IPv6`地址申请，地址类型不能为主`IP`，`IPv6`地址暂时只支持作为辅助`IP`。
        * 地址必须要在弹性网卡所在子网内，而且不能被占用。
        * 在弹性网卡上申请一个到多个辅助`IPv6`地址，接口会在弹性网卡所在子网段内返回指定数量的辅助`IPv6`地址。
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6CidrBlock(
            self,
            request: models.AssignIpv6CidrBlockRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6CidrBlockResponse:
        """
        本接口（AssignIpv6CidrBlock）用于分配IPv6网段。
        * 使用本接口前，您需要已有VPC实例，如果没有可通过接口<a href="https://cloud.tencent.com/document/api/215/15774" title="CreateVpc" target="_blank">CreateVpc</a>创建。
        * 每个VPC只能申请一个IPv6网段。
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6CidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6CidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6SubnetCidrBlock(
            self,
            request: models.AssignIpv6SubnetCidrBlockRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6SubnetCidrBlockResponse:
        """
        本接口（AssignIpv6SubnetCidrBlock）用于分配IPv6子网段。
        * 给子网分配 `IPv6` 网段，要求子网所属 `VPC` 已获得 `IPv6` 网段。如果尚未分配，请先通过接口 `AssignIpv6CidrBlock` 给子网所属 `VPC` 分配一个 `IPv6` 网段。否则无法分配 `IPv6` 子网段。
        * 每个子网只能分配一个IPv6网段。
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6SubnetCidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6SubnetCidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignPrivateIpAddresses(
            self,
            request: models.AssignPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.AssignPrivateIpAddressesResponse:
        """
        本接口（AssignPrivateIpAddresses）用于弹性网卡申请内网 IP。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 可以指定内网IP地址申请，内网IP地址类型不能为主IP，主IP已存在，不能修改，内网IP必须要在弹性网卡所在子网内，而且不能被占用。
        * 在弹性网卡上申请一个到多个辅助内网IP，接口会在弹性网卡所在子网网段内返回指定数量的辅助内网IP。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "AssignPrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignPrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateAddress(
            self,
            request: models.AssociateAddressRequest,
            opts: Dict = None,
    ) -> models.AssociateAddressResponse:
        """
        本接口 (AssociateAddress) 用于将[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        * 将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        * 将 EIP 绑定到主网卡的主内网IP时，如主内网IP已绑定普通公网IP，必须先退还才能绑定EIP。
        * 将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。
        * 将 EIP 绑定到NAT网关，请使用接口[AssociateNatGatewayAddress](https://cloud.tencent.com/document/product/215/36722)。
        * EIP 如果欠费或被封堵，则不能被绑定。
        * 只有状态为 UNBIND 的 EIP 才能够被绑定。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateDhcpIpWithAddressIp(
            self,
            request: models.AssociateDhcpIpWithAddressIpRequest,
            opts: Dict = None,
    ) -> models.AssociateDhcpIpWithAddressIpResponse:
        """
        本接口（AssociateDhcpIpWithAddressIp）用于DhcpIp绑定弹性公网IP（EIP）。<br />
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDhcpIpWithAddressIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDhcpIpWithAddressIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateDirectConnectGatewayNatGateway(
            self,
            request: models.AssociateDirectConnectGatewayNatGatewayRequest,
            opts: Dict = None,
    ) -> models.AssociateDirectConnectGatewayNatGatewayResponse:
        """
        将专线网关与NAT网关绑定，专线网关默认路由指向NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateDirectConnectGatewayNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateDirectConnectGatewayNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateHaVipInstance(
            self,
            request: models.AssociateHaVipInstanceRequest,
            opts: Dict = None,
    ) -> models.AssociateHaVipInstanceResponse:
        """
        本接口（AssociateHaVipInstance）用于HAVIP绑定子机或网卡（限制HaVip的漂移范围）。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateHaVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateHaVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateIPv6Address(
            self,
            request: models.AssociateIPv6AddressRequest,
            opts: Dict = None,
    ) -> models.AssociateIPv6AddressResponse:
        """
        本接口（AssociateIPv6Address）用于将弹性公网IPv6（简称EIPv6）实例绑定到 CVM 或弹性网卡配置的内网 IPv6 地址上。

        - 将 EIPv6 绑定到 CVM 上，其本质是将 EIPv6 绑定到 CVM 弹性网卡所配置的内网 IPv6 地址上。
        - 将 EIPv6 绑定到指定网卡的内网 IPv6 时，需确保该内网 IPv6 地址为未绑定状态，才能执行绑定操作。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateIPv6Address"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateIPv6AddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateInstancesToCcnRouteTable(
            self,
            request: models.AssociateInstancesToCcnRouteTableRequest,
            opts: Dict = None,
    ) -> models.AssociateInstancesToCcnRouteTableResponse:
        """
        本接口（AssociateInstancesToCcnRouteTable）用于将指定的云联网实例关联到指定的云联网路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateInstancesToCcnRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateInstancesToCcnRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateNatGatewayAddress(
            self,
            request: models.AssociateNatGatewayAddressRequest,
            opts: Dict = None,
    ) -> models.AssociateNatGatewayAddressResponse:
        """
        本接口(AssociateNatGatewayAddress)用于NAT网关绑定弹性IP（EIP）。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateNatGatewayAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateNatGatewayAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateNetworkAclSubnets(
            self,
            request: models.AssociateNetworkAclSubnetsRequest,
            opts: Dict = None,
    ) -> models.AssociateNetworkAclSubnetsResponse:
        """
        本接口（AssociateNetworkAclSubnets）用于网络ACL关联VPC下的子网。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateNetworkAclSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateNetworkAclSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateNetworkInterfaceSecurityGroups(
            self,
            request: models.AssociateNetworkInterfaceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateNetworkInterfaceSecurityGroupsResponse:
        """
        本接口（AssociateNetworkInterfaceSecurityGroups）用于弹性网卡绑定安全组（SecurityGroup）。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateNetworkInterfaceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateNetworkInterfaceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachCcnInstances(
            self,
            request: models.AttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachCcnInstancesResponse:
        """
        本接口（AttachCcnInstances）用于将网络实例加载到云联网实例中，网络实例包括VPC和专线网关。<br />
        每个云联网能够关联的网络实例个数是有限的，详情请参考产品文档。如果需要扩充请联系在线客服。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachClassicLinkVpc(
            self,
            request: models.AttachClassicLinkVpcRequest,
            opts: Dict = None,
    ) -> models.AttachClassicLinkVpcResponse:
        """
        本接口(AttachClassicLinkVpc)用于创建私有网络和基础网络设备互通。
        * 私有网络和基础网络设备必须在同一个地域。
        * 私有网络和基础网络的区别详见vpc产品文档-<a href="https://cloud.tencent.com/document/product/215/30720">私有网络与基础网络</a>。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "AttachClassicLinkVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachClassicLinkVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachNetworkInterface(
            self,
            request: models.AttachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.AttachNetworkInterfaceResponse:
        """
        本接口（AttachNetworkInterface）用于弹性网卡绑定云服务器。
        * 一个弹性网卡请至少绑定一个安全组，如需绑定请参见<a href="https://cloud.tencent.com/document/product/215/43132">弹性网卡绑定安全组</a>。
        * 一个云服务器可以绑定多个弹性网卡，但只能绑定一个主网卡。更多限制信息详见<a href="https://cloud.tencent.com/document/product/576/18527">弹性网卡使用限制</a>。
        * 一个弹性网卡只能同时绑定一个云服务器。
        * 只有运行中或者已关机状态的云服务器才能绑定弹性网卡，查看云服务器状态详见<a href="https://cloud.tencent.com/document/api/213/9452#InstanceStatus">腾讯云服务器信息</a>。
        * 弹性网卡绑定的云服务器必须是私有网络的，而且云服务器所在可用区必须和弹性网卡子网的可用区相同。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachSnapshotInstances(
            self,
            request: models.AttachSnapshotInstancesRequest,
            opts: Dict = None,
    ) -> models.AttachSnapshotInstancesResponse:
        """
        本接口（AttachSnapshotInstances）用于快照策略关联实例。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachSnapshotInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachSnapshotInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AuditCrossBorderCompliance(
            self,
            request: models.AuditCrossBorderComplianceRequest,
            opts: Dict = None,
    ) -> models.AuditCrossBorderComplianceResponse:
        """
        本接口（AuditCrossBorderCompliance）用于服务商操作合规化资质审批。
        * 服务商只能操作提交到本服务商的审批单，后台会校验身份。即只授权给服务商的`APPID` 调用本接口。
        * `APPROVED` 状态的审批单，可以再次操作为 `DENY`；`DENY` 状态的审批单，也可以再次操作为 `APPROVED`。
        """
        
        kwargs = {}
        kwargs["action"] = "AuditCrossBorderCompliance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AuditCrossBorderComplianceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckAssistantCidr(
            self,
            request: models.CheckAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.CheckAssistantCidrResponse:
        """
        本接口（CheckAssistantCidr）用于检查辅助CIDR是否与存量路由、对等连接（对端VPC的CIDR）等资源存在冲突。如果存在重叠，则返回重叠的资源。
        * 检测辅助CIDR是否与当前VPC的主CIDR和辅助CIDR存在重叠。
        * 检测辅助CIDR是否与当前VPC的路由的目的端存在重叠。
        * 检测辅助CIDR是否与当前VPC的对等连接，对端VPC下的主CIDR或辅助CIDR存在重叠。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckDefaultSubnet(
            self,
            request: models.CheckDefaultSubnetRequest,
            opts: Dict = None,
    ) -> models.CheckDefaultSubnetResponse:
        """
        本接口（CheckDefaultSubnet）用于预判是否可建默认子网。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckDefaultSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckDefaultSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckGatewayFlowMonitor(
            self,
            request: models.CheckGatewayFlowMonitorRequest,
            opts: Dict = None,
    ) -> models.CheckGatewayFlowMonitorResponse:
        """
        本接口（CheckGatewayFlowMonitor）用于查询网关是否启用流量监控。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckGatewayFlowMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckGatewayFlowMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckNetDetectState(
            self,
            request: models.CheckNetDetectStateRequest,
            opts: Dict = None,
    ) -> models.CheckNetDetectStateResponse:
        """
        本接口（CheckNetDetectState）用于验证网络探测。
        """
        
        kwargs = {}
        kwargs["action"] = "CheckNetDetectState"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckNetDetectStateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CheckTrafficMirror(
            self,
            request: models.CheckTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.CheckTrafficMirrorResponse:
        """
        检查流量镜像的采集端接收端（公网IP类型）
        """
        
        kwargs = {}
        kwargs["action"] = "CheckTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CheckTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ClearRouteTableSelectionPolicies(
            self,
            request: models.ClearRouteTableSelectionPoliciesRequest,
            opts: Dict = None,
    ) -> models.ClearRouteTableSelectionPoliciesResponse:
        """
        本接口（ClearRouteTableSelectionPolicies）用于清空指定云联网的路由表选择策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ClearRouteTableSelectionPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ClearRouteTableSelectionPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CloneSecurityGroup(
            self,
            request: models.CloneSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CloneSecurityGroupResponse:
        """
        本接口（CloneSecurityGroup）用于根据存量的安全组，克隆创建出同样规则配置的安全组。默认仅克隆安全组及其规则信息，可通过入参开启克隆安全组标签信息。
        """
        
        kwargs = {}
        kwargs["action"] = "CloneSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CloneSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressTemplate(
            self,
            request: models.CreateAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateAddressTemplateResponse:
        """
        本接口（CreateAddressTemplate）用于创建IP地址模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAddressTemplateGroup(
            self,
            request: models.CreateAddressTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateAddressTemplateGroupResponse:
        """
        本接口（CreateAddressTemplateGroup）用于创建IP地址模板集合。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAddressTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAddressTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAndAttachNetworkInterface(
            self,
            request: models.CreateAndAttachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.CreateAndAttachNetworkInterfaceResponse:
        """
        本接口（CreateAndAttachNetworkInterface）用于创建弹性网卡并绑定云服务器。
        * 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
        * 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 创建弹性网卡同时可以绑定已有安全组。
        * 创建弹性网卡同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAndAttachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAndAttachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateAssistantCidr(
            self,
            request: models.CreateAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.CreateAssistantCidrResponse:
        """
        本接口（CreateAssistantCidr）用于批量创建辅助CIDR。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateBandwidthPackage(
            self,
            request: models.CreateBandwidthPackageRequest,
            opts: Dict = None,
    ) -> models.CreateBandwidthPackageResponse:
        """
        本接口 (CreateBandwidthPackage) 支持创建[设备带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)和[IP带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateBandwidthPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateBandwidthPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcn(
            self,
            request: models.CreateCcnRequest,
            opts: Dict = None,
    ) -> models.CreateCcnResponse:
        """
        本接口（CreateCcn）用于创建云联网（CCN）。<br />
        * 创建云联网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        * 每个账号能创建的云联网实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCcnRouteTables(
            self,
            request: models.CreateCcnRouteTablesRequest,
            opts: Dict = None,
    ) -> models.CreateCcnRouteTablesResponse:
        """
        本接口（CreateCcnRouteTables）用于给指定的云联网实例新建路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCcnRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCcnRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdcLDCXList(
            self,
            request: models.CreateCdcLDCXListRequest,
            opts: Dict = None,
    ) -> models.CreateCdcLDCXListResponse:
        """
        创建 IDC 通道
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdcLDCXList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdcLDCXListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCdcNetPlanes(
            self,
            request: models.CreateCdcNetPlanesRequest,
            opts: Dict = None,
    ) -> models.CreateCdcNetPlanesResponse:
        """
        创建虚拟连接，用于支持 CDC 多租户模式
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCdcNetPlanes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCdcNetPlanesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateCustomerGateway(
            self,
            request: models.CreateCustomerGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateCustomerGatewayResponse:
        """
        本接口（CreateCustomerGateway）用于创建对端网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateCustomerGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateCustomerGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefaultSecurityGroup(
            self,
            request: models.CreateDefaultSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CreateDefaultSecurityGroupResponse:
        """
        本接口（CreateDefaultSecurityGroup）用于创建（如果项目下未存在默认安全组，则创建；已存在则获取。）默认安全组（SecurityGroup）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/12453">安全组数量限制</a>。
        * 默认安全组会放通所有IPv4规则，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。
        * 创建安全组同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefaultSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefaultSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDefaultVpc(
            self,
            request: models.CreateDefaultVpcRequest,
            opts: Dict = None,
    ) -> models.CreateDefaultVpcResponse:
        """
        本接口（CreateDefaultVpc）用于创建默认私有网络(VPC）。

        默认VPC适用于快速入门和启动公共实例，您可以像使用任何其他VPC一样使用默认VPC。如果您想创建标准VPC，即指定VPC名称、VPC网段、子网网段、子网可用区，请使用常规创建VPC接口（CreateVpc）

        正常情况，本接口并不一定生产默认VPC，而是根据用户账号的网络属性（DescribeAccountAttributes）来决定的
        * 支持基础网络、VPC，返回VpcId为0
        * 只支持VPC，返回默认VPC信息

        您也可以通过 Force 参数，强制返回默认VPC。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDefaultVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDefaultVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDhcpIp(
            self,
            request: models.CreateDhcpIpRequest,
            opts: Dict = None,
    ) -> models.CreateDhcpIpResponse:
        """
        本接口（CreateDhcpIp）用于创建DhcpIp。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDhcpIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDhcpIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnectGateway(
            self,
            request: models.CreateDirectConnectGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectGatewayResponse:
        """
        本接口（CreateDirectConnectGateway）用于创建专线网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnectGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDirectConnectGatewayCcnRoutes(
            self,
            request: models.CreateDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateDirectConnectGatewayCcnRoutesResponse:
        """
        本接口（CreateDirectConnectGatewayCcnRoutes）用于创建专线网关的云联网路由（IDC网段）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateFlowLog(
            self,
            request: models.CreateFlowLogRequest,
            opts: Dict = None,
    ) -> models.CreateFlowLogResponse:
        """
        本接口（CreateFlowLog）用于创建网络流日志。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateFlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateFlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateGlobalRoutes(
            self,
            request: models.CreateGlobalRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateGlobalRoutesResponse:
        """
        本接口（CreateGlobalRoutes）用于创建全局路由。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateGlobalRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateGlobalRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHaVip(
            self,
            request: models.CreateHaVipRequest,
            opts: Dict = None,
    ) -> models.CreateHaVipResponse:
        """
        本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHighPriorityRouteTable(
            self,
            request: models.CreateHighPriorityRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateHighPriorityRouteTableResponse:
        """
        高优路由表创建
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHighPriorityRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHighPriorityRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHighPriorityRoutes(
            self,
            request: models.CreateHighPriorityRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateHighPriorityRoutesResponse:
        """
        创建高优路由表条目。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHighPriorityRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHighPriorityRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateIp6Translators(
            self,
            request: models.CreateIp6TranslatorsRequest,
            opts: Dict = None,
    ) -> models.CreateIp6TranslatorsResponse:
        """
        1. 该接口用于创建IPV6转换IPV4实例，支持批量
        2. 同一个账户在一个地域最多允许创建10个转换实例
        """
        
        kwargs = {}
        kwargs["action"] = "CreateIp6Translators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateIp6TranslatorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLocalGateway(
            self,
            request: models.CreateLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateLocalGatewayResponse:
        """
        本接口（CreateLocalGateway）用于创建用于CDC的本地网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGateway(
            self,
            request: models.CreateNatGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewayResponse:
        """
        本接口(CreateNatGateway)用于创建NAT网关。
        在对新建的NAT网关做其他操作前，需先确认此网关已被创建完成（DescribeNatGateway接口返回的实例State字段为AVAILABLE）。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        本接口(CreateNatGatewayDestinationIpPortTranslationNatRule)用于创建NAT网关端口转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNatGatewaySourceIpTranslationNatRule(
            self,
            request: models.CreateNatGatewaySourceIpTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.CreateNatGatewaySourceIpTranslationNatRuleResponse:
        """
        本接口(CreateNatGatewaySourceIpTranslationNatRule)用于创建NAT网关SNAT规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNatGatewaySourceIpTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNatGatewaySourceIpTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetDetect(
            self,
            request: models.CreateNetDetectRequest,
            opts: Dict = None,
    ) -> models.CreateNetDetectResponse:
        """
        本接口（CreateNetDetect）用于创建网络探测。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkAcl(
            self,
            request: models.CreateNetworkAclRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkAclResponse:
        """
        本接口（CreateNetworkAcl）用于创建新的<a href="https://cloud.tencent.com/document/product/215/20088">网络ACL</a>。
        * 新建的网络ACL的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用ModifyNetworkAclEntries将网络ACL的规则设置为需要的规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkAclEntries(
            self,
            request: models.CreateNetworkAclEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkAclEntriesResponse:
        """
        本接口（CreateNetworkAclEntries）用于增量添加网络ACL三元组的入站规则和出站规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkAclEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkAclEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkAclQuintupleEntries(
            self,
            request: models.CreateNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkAclQuintupleEntriesResponse:
        """
        本接口（CreateNetworkAclQuintupleEntries）用于增量网络ACL五元组的入站规则和出站规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkInterface(
            self,
            request: models.CreateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkInterfaceResponse:
        """
        本接口（CreateNetworkInterface）用于创建弹性网卡。
        * 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
        * 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="https://cloud.tencent.com/document/product/576/18527">弹性网卡使用限制</a>。
        * 创建弹性网卡同时可以绑定已有安全组。
        * 创建弹性网卡同时可以绑定标签, 响应里的标签列表代表添加成功的标签。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateNatGateway(
            self,
            request: models.CreatePrivateNatGatewayRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateNatGatewayResponse:
        """
        本接口（CreatePrivateNatGateway）用于创建私网NAT网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.CreatePrivateNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        本接口（CreatePrivateNatGatewayDestinationIpPortTranslationNatRule）用于创建私网NAT网关目的端口转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateNatGatewayTranslationAclRule(
            self,
            request: models.CreatePrivateNatGatewayTranslationAclRuleRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateNatGatewayTranslationAclRuleResponse:
        """
        本接口（ CreatePrivateNatGatewayTranslationAclRule）用于创建私网NAT网关源端转换访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateNatGatewayTranslationAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateNatGatewayTranslationAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreatePrivateNatGatewayTranslationNatRule(
            self,
            request: models.CreatePrivateNatGatewayTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.CreatePrivateNatGatewayTranslationNatRuleResponse:
        """
        本接口（CreatePrivateNatGatewayTranslationNatRule）用于创建私网NAT网关源端转换规则。
        """
        
        kwargs = {}
        kwargs["action"] = "CreatePrivateNatGatewayTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreatePrivateNatGatewayTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateReserveIpAddresses(
            self,
            request: models.CreateReserveIpAddressesRequest,
            opts: Dict = None,
    ) -> models.CreateReserveIpAddressesResponse:
        """
        创建内网保留IP
        """
        
        kwargs = {}
        kwargs["action"] = "CreateReserveIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateReserveIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicy(
            self,
            request: models.CreateRoutePolicyRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePolicyResponse:
        """
        创建VPC路由接收策略，包括名字，描述和策略条目。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicyAssociations(
            self,
            request: models.CreateRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePolicyAssociationsResponse:
        """
        本接口（CreateRoutePolicyAssociations）用于创建路由接收策略绑定(路由策略实例和路由表实例的绑定关系以及绑定优先级)。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutePolicyEntries(
            self,
            request: models.CreateRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.CreateRoutePolicyEntriesResponse:
        """
        本接口（CreateRoutePolicyEntries）用于创建路由接收策略条目。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRouteTable(
            self,
            request: models.CreateRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateRouteTableResponse:
        """
        本接口(CreateRouteTable)用于创建路由表。
        * 创建了VPC后，系统会创建一个默认路由表，所有新建的子网都会关联到默认路由表。默认情况下您可以直接使用默认路由表来管理您的路由策略。当您的路由策略较多时，您可以调用创建路由表接口创建更多路由表管理您的路由策略。
        * 创建路由表同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRoutes(
            self,
            request: models.CreateRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateRoutesResponse:
        """
        本接口（CreateRoutes）用于创建路由策略。
        * 向指定路由表批量新增路由策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroup(
            self,
            request: models.CreateSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupResponse:
        """
        本接口（CreateSecurityGroup）用于创建新的安全组（SecurityGroup）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/12453">安全组数量限制</a>。
        * 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。
        * 创建安全组同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupPolicies(
            self,
            request: models.CreateSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupPoliciesResponse:
        """
        本接口（CreateSecurityGroupPolicies）用于创建安全组规则（SecurityGroupPolicy）。

        在 SecurityGroupPolicySet 参数中：
        <ul>
        <li>Version 安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。</li>
        <li>在创建出站和入站规则（Egress 和 Ingress）时：<ul>
        <li>Protocol 字段支持输入TCP, UDP, ICMP, ICMPV6, GRE, ALL。</li>
        <li>CidrBlock 字段允许输入符合cidr格式标准的任意字符串。在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        <li>Ipv6CidrBlock 字段允许输入符合IPv6 cidr格式标准的任意字符串。在基础网络中，如果Ipv6CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        <li>SecurityGroupId 字段允许输入与待修改的安全组位于相同项目中的安全组 ID，包括这个安全组 ID 本身，代表安全组下所有云服务器的内网 IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个 ID 所关联的云服务器变化而变化，不需要重新修改。</li>
        <li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受，即 Protocol 字段不是 TCP 或 UDP 时，Protocol 和 Port 是排他关系，不允许同时输入，否则会接口报错。</li>
        <li>Action 字段只允许输入 ACCEPT 或 DROP。</li>
        <li>CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate 四者是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。IPv6CidrBlock和ICMP是排他关系，如需使用，请输入ICMPV6。</li>
        <li>一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。如想在规则最前面插入一条，则填0即可，如果想在最后追加，该字段可不填。</li>
        </ul></li></ul>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSecurityGroupWithPolicies(
            self,
            request: models.CreateSecurityGroupWithPoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateSecurityGroupWithPoliciesResponse:
        """
        本接口（CreateSecurityGroupWithPolicies）用于创建新的安全组（SecurityGroup），并且可以同时添加安全组规则（SecurityGroupPolicy）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/12453">安全组数量限制</a>。
        * 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用<a href="https://cloud.tencent.com/document/product/215/15807">CreateSecurityGroupPolicies</a>
        将安全组的规则设置为需要的规则。

        安全组规则说明：
        * Version安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。
        * Protocol字段支持输入TCP, UDP, ICMP, ICMPV6, GRE, ALL。
        * CidrBlock字段允许输入符合cidr格式标准的任意字符串。(展开)在基础网络中，如果CidrBlock包含您的账户内的云服务器之外的设备在腾讯云的内网IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。
        * Ipv6CidrBlock字段允许输入符合IPv6 cidr格式标准的任意字符串。(展开)在基础网络中，如果Ipv6CidrBlock包含您的账户内的云服务器之外的设备在腾讯云的内网IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。
        * SecurityGroupId字段允许输入与待修改的安全组位于相同项目中的安全组ID，包括这个安全组ID本身，代表安全组下所有云服务器的内网IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个ID所关联的云服务器变化而变化，不需要重新修改。
        * Port字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当Protocol字段是TCP或UDP时，Port字段才被接受，即Protocol字段不是TCP或UDP时，Protocol和Port是排他关系，不允许同时输入，否则会接口报错。
        * Action字段只允许输入ACCEPT或DROP。
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate四者是排他关系，不允许同时输入，Protocol + Port和ServiceTemplate二者是排他关系，不允许同时输入。
        * 请求中可以同时指定入站和出站两个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupWithPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupWithPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceTemplate(
            self,
            request: models.CreateServiceTemplateRequest,
            opts: Dict = None,
    ) -> models.CreateServiceTemplateResponse:
        """
        本接口（CreateServiceTemplate）用于创建协议端口模板。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateServiceTemplateGroup(
            self,
            request: models.CreateServiceTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.CreateServiceTemplateGroupResponse:
        """
        本接口（CreateServiceTemplateGroup）用于创建协议端口模板集合。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateServiceTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateServiceTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSnapshotPolicies(
            self,
            request: models.CreateSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.CreateSnapshotPoliciesResponse:
        """
        本接口（CreateSnapshotPolicies）用于创建快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnet(
            self,
            request: models.CreateSubnetRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetResponse:
        """
        本接口（CreateSubnet）用于创建子网。
        * 创建子网前必须创建好 VPC。
        * 子网创建成功后，子网网段不能修改。子网网段必须在VPC网段内，可以和VPC网段相同（VPC有且只有一个子网时），建议子网网段在VPC网段内，预留网段给其他子网使用。
        * 您可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）。
        * 同一个VPC内，多个子网的网段不能重叠。
        * 子网创建后会自动关联到默认路由表。
        * 创建子网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnets(
            self,
            request: models.CreateSubnetsRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetsResponse:
        """
        本接口（CreateSubnets）用于批量创建子网。
        * 创建子网前必须创建好 VPC。
        * 子网创建成功后，子网网段不能修改。子网网段必须在VPC网段内，可以和VPC网段相同（VPC有且只有一个子网时），建议子网网段在VPC网段内，预留网段给其他子网使用。
        * 您可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）。
        * 同一个VPC内，多个子网的网段不能重叠。
        * 子网创建后会自动关联到默认路由表。
        * 创建子网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrafficMirror(
            self,
            request: models.CreateTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.CreateTrafficMirrorResponse:
        """
        本接口（CreateTrafficMirror）用于创建流量镜像实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateTrafficPackages(
            self,
            request: models.CreateTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.CreateTrafficPackagesResponse:
        """
        本接口 (CreateTrafficPackages) 用于创建共享流量包。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpc(
            self,
            request: models.CreateVpcRequest,
            opts: Dict = None,
    ) -> models.CreateVpcResponse:
        """
        本接口（CreateVpc）用于创建私有网络（VPC）。
        * 用户可以创建的最小网段子网掩码为28（有16个IP地址），10.0.0.0/12，172.16.0.0/12最大网段子网掩码为12（1,048,576个IP地址），192.168.0.0/16最大网段子网掩码为16（65,536个IP地址）如果需要规划VPC网段请参见[网络规划](https://cloud.tencent.com/document/product/215/30313)。
        * 同一个地域能创建的VPC资源个数也是有限制的，详见 <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>，如果需要申请更多资源，请提交[工单申请](https://console.cloud.tencent.com/workorder/category)。
        * 创建VPC同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcEndPoint(
            self,
            request: models.CreateVpcEndPointRequest,
            opts: Dict = None,
    ) -> models.CreateVpcEndPointResponse:
        """
        本接口（CreateVpcEndPoint）用于创建终端节点。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcEndPointService(
            self,
            request: models.CreateVpcEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.CreateVpcEndPointServiceResponse:
        """
        本接口（CreateVpcEndPointService）用于创建终端节点服务。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcEndPointServiceWhiteList(
            self,
            request: models.CreateVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.CreateVpcEndPointServiceWhiteListResponse:
        """
        本接口（CreateVpcEndPointServiceWhiteList）创建终端服务白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpcPeeringConnection(
            self,
            request: models.CreateVpcPeeringConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateVpcPeeringConnectionResponse:
        """
        本接口（CreateVpcPeeringConnection）用于创建私有网络对等连接。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpcPeeringConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcPeeringConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnConnection(
            self,
            request: models.CreateVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.CreateVpnConnectionResponse:
        """
        本接口（CreateVpnConnection）用于创建VPN通道。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnGateway(
            self,
            request: models.CreateVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.CreateVpnGatewayResponse:
        """
        本接口（CreateVpnGateway）用于创建VPN网关。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnGatewayRoutes(
            self,
            request: models.CreateVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.CreateVpnGatewayRoutesResponse:
        """
        创建路由型VPN网关的目的路由
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnGatewaySslClient(
            self,
            request: models.CreateVpnGatewaySslClientRequest,
            opts: Dict = None,
    ) -> models.CreateVpnGatewaySslClientResponse:
        """
        创建SSL-VPN-CLIENT
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnGatewaySslClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnGatewaySslClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpnGatewaySslServer(
            self,
            request: models.CreateVpnGatewaySslServerRequest,
            opts: Dict = None,
    ) -> models.CreateVpnGatewaySslServerResponse:
        """
        本接口（CreateVpnGatewaySslServer）用于创建SSL-VPN Server端。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpnGatewaySslServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpnGatewaySslServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressTemplate(
            self,
            request: models.DeleteAddressTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressTemplateResponse:
        """
        本接口（DeleteAddressTemplate）用于删除IP地址模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAddressTemplateGroup(
            self,
            request: models.DeleteAddressTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteAddressTemplateGroupResponse:
        """
        本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAddressTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAddressTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteAssistantCidr(
            self,
            request: models.DeleteAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.DeleteAssistantCidrResponse:
        """
        本接口（DeleteAssistantCidr）用于删除辅助CIDR。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteBandwidthPackage(
            self,
            request: models.DeleteBandwidthPackageRequest,
            opts: Dict = None,
    ) -> models.DeleteBandwidthPackageResponse:
        """
        接口支持删除共享带宽包，包括[设备带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)和[IP带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteBandwidthPackage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteBandwidthPackageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcn(
            self,
            request: models.DeleteCcnRequest,
            opts: Dict = None,
    ) -> models.DeleteCcnResponse:
        """
        本接口（DeleteCcn）用于删除云联网。
        * 删除后，云联网关联的所有实例间路由将被删除，网络将会中断，请务必确认
        * 删除云联网是不可逆的操作，请谨慎处理。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcn"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcnResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCcnRouteTables(
            self,
            request: models.DeleteCcnRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DeleteCcnRouteTablesResponse:
        """
        本接口（DeleteCcnRouteTables）用于删除云联网路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCcnRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCcnRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCdcLDCXList(
            self,
            request: models.DeleteCdcLDCXListRequest,
            opts: Dict = None,
    ) -> models.DeleteCdcLDCXListResponse:
        """
        删除 IDC通道
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCdcLDCXList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCdcLDCXListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteCdcNetPlanes(
            self,
            request: models.DeleteCdcNetPlanesRequest,
            opts: Dict = None,
    ) -> models.DeleteCdcNetPlanesResponse:
        """
        删除虚拟连接
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteCdcNetPlanes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteCdcNetPlanesResponse
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
        
    async def DeleteDhcpIp(
            self,
            request: models.DeleteDhcpIpRequest,
            opts: Dict = None,
    ) -> models.DeleteDhcpIpResponse:
        """
        本接口（DeleteDhcpIp）用于删除DhcpIp。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDhcpIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDhcpIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnectGateway(
            self,
            request: models.DeleteDirectConnectGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectGatewayResponse:
        """
        本接口（DeleteDirectConnectGateway）用于删除专线网关。
        <li>如果是 NAT 网关，删除专线网关后，NAT 规则以及 ACL 策略都被清理了。</li>
        <li>删除专线网关后，系统会删除路由表中跟该专线网关相关的路由策略。</li>
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnectGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteDirectConnectGatewayCcnRoutes(
            self,
            request: models.DeleteDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteDirectConnectGatewayCcnRoutesResponse:
        """
        本接口（DeleteDirectConnectGatewayCcnRoutes）用于删除专线网关的云联网路由（IDC网段）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteFlowLog(
            self,
            request: models.DeleteFlowLogRequest,
            opts: Dict = None,
    ) -> models.DeleteFlowLogResponse:
        """
        本接口（DeleteFlowLog）用于删除流日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteFlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteFlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteGlobalRoutes(
            self,
            request: models.DeleteGlobalRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteGlobalRoutesResponse:
        """
        删除全局路由。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteGlobalRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteGlobalRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHaVip(
            self,
            request: models.DeleteHaVipRequest,
            opts: Dict = None,
    ) -> models.DeleteHaVipResponse:
        """
        本接口（DeleteHaVip）用于删除高可用虚拟IP（HAVIP）。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHighPriorityRouteTables(
            self,
            request: models.DeleteHighPriorityRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DeleteHighPriorityRouteTablesResponse:
        """
        删除高优路由表
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHighPriorityRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHighPriorityRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHighPriorityRoutes(
            self,
            request: models.DeleteHighPriorityRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteHighPriorityRoutesResponse:
        """
        删除高优路由表的路由条目。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHighPriorityRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHighPriorityRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteIp6Translators(
            self,
            request: models.DeleteIp6TranslatorsRequest,
            opts: Dict = None,
    ) -> models.DeleteIp6TranslatorsResponse:
        """
        1. 该接口用于释放IPV6转换实例，支持批量。
        2.  如果IPV6转换实例建立有转换规则，会一并删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteIp6Translators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteIp6TranslatorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLocalGateway(
            self,
            request: models.DeleteLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteLocalGatewayResponse:
        """
        本接口（DeleteLocalGateway）用于删除CDC的本地网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGateway(
            self,
            request: models.DeleteNatGatewayRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewayResponse:
        """
        本接口（DeleteNatGateway）用于删除NAT网关。
        删除 NAT 网关后，系统会自动删除路由表中包含此 NAT 网关的路由项，同时也会解绑弹性公网IP（EIP）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        本接口（DeleteNatGatewayDestinationIpPortTranslationNatRule）用于删除NAT网关端口转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNatGatewaySourceIpTranslationNatRule(
            self,
            request: models.DeleteNatGatewaySourceIpTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.DeleteNatGatewaySourceIpTranslationNatRuleResponse:
        """
        本接口（DeleteNatGatewaySourceIpTranslationNatRule）用于删除NAT网关端口SNAT转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNatGatewaySourceIpTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNatGatewaySourceIpTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetDetect(
            self,
            request: models.DeleteNetDetectRequest,
            opts: Dict = None,
    ) -> models.DeleteNetDetectResponse:
        """
        本接口（DeleteNetDetect）用于删除网络探测实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkAcl(
            self,
            request: models.DeleteNetworkAclRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkAclResponse:
        """
        本接口（DeleteNetworkAcl）用于删除网络ACL。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkAcl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkAclResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkAclEntries(
            self,
            request: models.DeleteNetworkAclEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkAclEntriesResponse:
        """
        本接口（DeleteNetworkAclEntries）用于删除三元组网络ACL的入站规则和出站规则。在NetworkAclEntrySet参数中：
        * 删除IPv4规则，需要传入NetworkAclIpv4EntryId。
        * 删除IPv6规则，需要传入NetworkAclIpv6EntryId。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkAclEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkAclEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkAclQuintupleEntries(
            self,
            request: models.DeleteNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkAclQuintupleEntriesResponse:
        """
        本接口（DeleteNetworkAclQuintupleEntries）用于删除网络ACL五元组指定的入站规则和出站规则（但不是全量删除该ACL下的所有条目）。在NetworkAclQuintupleEntrySet参数中：NetworkAclQuintupleEntry需要提供NetworkAclQuintupleEntryId。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkInterface(
            self,
            request: models.DeleteNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkInterfaceResponse:
        """
        本接口（DeleteNetworkInterface）用于删除弹性网卡。
        * 弹性网卡上绑定了云服务器时，不能被删除。
        * 删除指定弹性网卡，弹性网卡必须先和子机解绑才能删除。删除之后弹性网卡上所有内网IP都将被退还。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateNatGateway(
            self,
            request: models.DeletePrivateNatGatewayRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateNatGatewayResponse:
        """
        本接口（DeletePrivateNatGateway）用于删除私网NAT网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.DeletePrivateNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        本接口（DeletePrivateNatGatewayDestinationIpPortTranslationNatRule）用于删除私网NAT网关目的端口转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateNatGatewayTranslationAclRule(
            self,
            request: models.DeletePrivateNatGatewayTranslationAclRuleRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateNatGatewayTranslationAclRuleResponse:
        """
        本接口（DeletePrivateNatGatewayTranslationAclRule）用于删除私网NAT网关源端转换访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateNatGatewayTranslationAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateNatGatewayTranslationAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeletePrivateNatGatewayTranslationNatRule(
            self,
            request: models.DeletePrivateNatGatewayTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.DeletePrivateNatGatewayTranslationNatRuleResponse:
        """
        本接口（DeletePrivateNatGatewayTranslationNatRule）用于删除私网NAT网关源端转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "DeletePrivateNatGatewayTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeletePrivateNatGatewayTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteReserveIpAddresses(
            self,
            request: models.DeleteReserveIpAddressesRequest,
            opts: Dict = None,
    ) -> models.DeleteReserveIpAddressesResponse:
        """
        删除内网保留IP
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteReserveIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteReserveIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicy(
            self,
            request: models.DeleteRoutePolicyRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyResponse:
        """
        本接口（DeleteRoutePolicy）用于删除路由接收策略和条目。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicyAssociations(
            self,
            request: models.DeleteRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyAssociationsResponse:
        """
        本接口(DeleteRoutePolicyAssociations)用于删除路由接收策略绑定（路由接收策略对象和路由表的绑定关系）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutePolicyEntries(
            self,
            request: models.DeleteRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutePolicyEntriesResponse:
        """
        本接口(DeleteRoutePolicyEntries)用于删除路由接收策略条目。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRouteTable(
            self,
            request: models.DeleteRouteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteTableResponse:
        """
        本接口（DeleteRouteTable）用于删除路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRouteTable"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRouteTableResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRoutes(
            self,
            request: models.DeleteRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteRoutesResponse:
        """
        本接口(DeleteRoutes)用于对某个路由表批量删除路由策略（Route）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroup(
            self,
            request: models.DeleteSecurityGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupResponse:
        """
        本接口（DeleteSecurityGroup）用于删除安全组（SecurityGroup）。
        * 只有当前账号下的安全组允许被删除。
        * 安全组实例ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要先进行规则修改，再删除安全组。
        * 删除的安全组无法再找回，请谨慎调用。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSecurityGroupPolicies(
            self,
            request: models.DeleteSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteSecurityGroupPoliciesResponse:
        """
        本接口（DeleteSecurityGroupPolicies）用于删除安全组规则（SecurityGroupPolicy）。
        * SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceTemplate(
            self,
            request: models.DeleteServiceTemplateRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceTemplateResponse:
        """
        本接口（DeleteServiceTemplate）用于删除协议端口模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceTemplate"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceTemplateResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteServiceTemplateGroup(
            self,
            request: models.DeleteServiceTemplateGroupRequest,
            opts: Dict = None,
    ) -> models.DeleteServiceTemplateGroupResponse:
        """
        本接口（DeleteServiceTemplateGroup）用于删除协议端口模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteServiceTemplateGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteServiceTemplateGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshotPolicies(
            self,
            request: models.DeleteSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotPoliciesResponse:
        """
        本接口（DeleteSnapshotPolicies）用于删除快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubnet(
            self,
            request: models.DeleteSubnetRequest,
            opts: Dict = None,
    ) -> models.DeleteSubnetResponse:
        """
        本接口（DeleteSubnet）用于删除子网（Subnet）。
        * 删除子网前，请清理该子网下所有资源，包括云服务器、负载均衡、云数据、NoSQL、弹性网卡等资源。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTemplateMember(
            self,
            request: models.DeleteTemplateMemberRequest,
            opts: Dict = None,
    ) -> models.DeleteTemplateMemberResponse:
        """
        删除模板对象中的IP地址、协议端口、IP地址组、协议端口组。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTemplateMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTemplateMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrafficMirror(
            self,
            request: models.DeleteTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.DeleteTrafficMirrorResponse:
        """
        本接口（DeleteTrafficMirror）用于删除流量镜像实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteTrafficPackages(
            self,
            request: models.DeleteTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DeleteTrafficPackagesResponse:
        """
        删除共享带宽包（仅非活动状态的流量包可删除）。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpc(
            self,
            request: models.DeleteVpcRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcResponse:
        """
        本接口（DeleteVpc）用于删除私有网络。
        * 删除前请确保 VPC 内已经没有相关资源，例如云服务器、云数据库、NoSQL、VPN网关、专线网关、负载均衡、对等连接、与之互通的基础网络设备等。
        * 删除私有网络是不可逆的操作，请谨慎处理。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcEndPoint(
            self,
            request: models.DeleteVpcEndPointRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcEndPointResponse:
        """
        本接口（DeleteVpcEndPoint）用于删除终端节点。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcEndPointService(
            self,
            request: models.DeleteVpcEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcEndPointServiceResponse:
        """
        本接口（DeleteVpcEndPointService）用于删除终端节点服务。限制：当有终端节点关联到终端节点服务时，无法删除终端节点服务。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcEndPointServiceWhiteList(
            self,
            request: models.DeleteVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcEndPointServiceWhiteListResponse:
        """
        本接口（DeleteVpcEndPointServiceWhiteList）用于删除终端节点服务白名单。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpcPeeringConnection(
            self,
            request: models.DeleteVpcPeeringConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcPeeringConnectionResponse:
        """
        本接口（DeleteVpcPeeringConnection）用于删除私有网络对等连接。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpcPeeringConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcPeeringConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnConnection(
            self,
            request: models.DeleteVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnConnectionResponse:
        """
        本接口（DeleteVpnConnection）用于删除VPN通道。
        >?本接口为异步接口
        >
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
        
    async def DeleteVpnGatewayRoutes(
            self,
            request: models.DeleteVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnGatewayRoutesResponse:
        """
        本接口（DeleteVpnGatewayRoutes）用于删除VPN网关路由
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnGatewaySslClient(
            self,
            request: models.DeleteVpnGatewaySslClientRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnGatewaySslClientResponse:
        """
        本接口（DeleteVpnGatewaySslClient）用于删除SSL-VPN-CLIENT。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnGatewaySslClient"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnGatewaySslClientResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpnGatewaySslServer(
            self,
            request: models.DeleteVpnGatewaySslServerRequest,
            opts: Dict = None,
    ) -> models.DeleteVpnGatewaySslServerResponse:
        """
        删除SSL-VPN-SERVER 实例
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpnGatewaySslServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpnGatewaySslServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAccountAttributes(
            self,
            request: models.DescribeAccountAttributesRequest,
            opts: Dict = None,
    ) -> models.DescribeAccountAttributesResponse:
        """
        本接口（DescribeAccountAttributes）用于查询用户账号私有属性。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAccountAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAccountAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressBandwidthRange(
            self,
            request: models.DescribeAddressBandwidthRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressBandwidthRangeResponse:
        """
        本接口（DescribeAddressBandwidthRange）用于查询指定EIP的带宽上下限范围。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressBandwidthRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressBandwidthRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressQuota(
            self,
            request: models.DescribeAddressQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressQuotaResponse:
        """
        本接口 (DescribeAddressQuota) 用于查询您账户的[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）在当前地域的配额信息。配额详情可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplateGroupInstances(
            self,
            request: models.DescribeAddressTemplateGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplateGroupInstancesResponse:
        """
        本接口（DescribeAddressTemplateGroupInstances）用于查询参数模板IP地址组口关联的实例列表。本接口不会返回查询的结果，需要根据返回的RequestId调用DescribeVpcTaskResult接口获取结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplateGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplateGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplateGroups(
            self,
            request: models.DescribeAddressTemplateGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplateGroupsResponse:
        """
        本接口（DescribeAddressTemplateGroups）用于查询IP地址模板集合。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplateGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplateGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplateInstances(
            self,
            request: models.DescribeAddressTemplateInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplateInstancesResponse:
        """
        本接口（DescribeAddressTemplateInstances）用于查询参数模板IP地址关联的实例列表。本接口不会返回查询的结果，需要根据返回的RequestId调用DescribeVpcTaskResult接口获取结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressTemplates(
            self,
            request: models.DescribeAddressTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressTemplatesResponse:
        """
        本接口（DescribeAddressTemplates）用于查询IP地址模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddresses(
            self,
            request: models.DescribeAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressesResponse:
        """
        本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的详细信息。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIP。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAssistantCidr(
            self,
            request: models.DescribeAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.DescribeAssistantCidrResponse:
        """
        本接口（DescribeAssistantCidr）用于查询辅助CIDR列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageBandwidthRange(
            self,
            request: models.DescribeBandwidthPackageBandwidthRangeRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageBandwidthRangeResponse:
        """
        查询指定带宽包的带宽上下限范围
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageBandwidthRange"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageBandwidthRangeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageBillUsage(
            self,
            request: models.DescribeBandwidthPackageBillUsageRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageBillUsageResponse:
        """
        本接口 (DescribeBandwidthPackageBillUsage) 用于查询后付费共享带宽包当前的计费用量.
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageBillUsage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageBillUsageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageQuota(
            self,
            request: models.DescribeBandwidthPackageQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageQuotaResponse:
        """
        接口用于查询账户在当前地域的带宽包上限数量以及使用数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackageResources(
            self,
            request: models.DescribeBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackageResourcesResponse:
        """
        本接口 (DescribeBandwidthPackageResources) 用于根据共享带宽包唯一ID查询共享带宽包内的资源列表，支持按条件过滤查询结果和分页查询。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBandwidthPackages(
            self,
            request: models.DescribeBandwidthPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeBandwidthPackagesResponse:
        """
        接口用于查询带宽包详细信息，包括带宽包唯一标识ID，类型，计费模式，名称，资源信息等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBandwidthPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBandwidthPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnAttachedInstances(
            self,
            request: models.DescribeCcnAttachedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnAttachedInstancesResponse:
        """
        本接口（DescribeCcnAttachedInstances）用于查询云联网实例下已关联的网络实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnAttachedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnAttachedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRegionBandwidthLimits(
            self,
            request: models.DescribeCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRegionBandwidthLimitsResponse:
        """
        本接口（DescribeCcnRegionBandwidthLimits）用于查询云联网各地域出带宽上限，该接口只返回已关联网络实例包含的地域。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRouteTableBroadcastPolicys(
            self,
            request: models.DescribeCcnRouteTableBroadcastPolicysRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRouteTableBroadcastPolicysResponse:
        """
        本接口(DescribeCcnRouteTableBroadcastPolicys)用于查询指定云联网路由表的路由传播策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRouteTableBroadcastPolicys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRouteTableBroadcastPolicysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRouteTableInputPolicys(
            self,
            request: models.DescribeCcnRouteTableInputPolicysRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRouteTableInputPolicysResponse:
        """
        本接口(DescribeCcnRouteTableInputPolicys)用于查询指定云联网路由表的路由接收策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRouteTableInputPolicys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRouteTableInputPolicysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRouteTables(
            self,
            request: models.DescribeCcnRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRouteTablesResponse:
        """
        该接口用于查询指定的云联网实例的路由表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcnRoutes(
            self,
            request: models.DescribeCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnRoutesResponse:
        """
        本接口（DescribeCcnRoutes）用于查询已加入云联网（CCN）的路由。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCcns(
            self,
            request: models.DescribeCcnsRequest,
            opts: Dict = None,
    ) -> models.DescribeCcnsResponse:
        """
        本接口（DescribeCcns）用于查询云联网（CCN）列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCcns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCcnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdcLDCXList(
            self,
            request: models.DescribeCdcLDCXListRequest,
            opts: Dict = None,
    ) -> models.DescribeCdcLDCXListResponse:
        """
        查询 IDC通道信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdcLDCXList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdcLDCXListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdcNetPlanes(
            self,
            request: models.DescribeCdcNetPlanesRequest,
            opts: Dict = None,
    ) -> models.DescribeCdcNetPlanesResponse:
        """
        查询虚拟连接
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdcNetPlanes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdcNetPlanesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCdcUsedIdcVlan(
            self,
            request: models.DescribeCdcUsedIdcVlanRequest,
            opts: Dict = None,
    ) -> models.DescribeCdcUsedIdcVlanResponse:
        """
        查询IDC使用的 VLAN
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCdcUsedIdcVlan"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCdcUsedIdcVlanResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeClassicLinkInstances(
            self,
            request: models.DescribeClassicLinkInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeClassicLinkInstancesResponse:
        """
        本接口（DescribeClassicLinkInstances）用于查询私有网络和基础网络设备互通列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeClassicLinkInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeClassicLinkInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderCcnRegionBandwidthLimits(
            self,
            request: models.DescribeCrossBorderCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderCcnRegionBandwidthLimitsResponse:
        """
        本接口（DescribeCrossBorderCcnRegionBandwidthLimits）用于获取要锁定的限速实例列表。
        该接口一般用来封禁地域间限速的云联网实例下的限速实例, 目前联通内部运营系统通过云API调用, 如果是出口限速, 一般使用更粗的云联网实例粒度封禁（DescribeTenantCcns）
        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderCompliance(
            self,
            request: models.DescribeCrossBorderComplianceRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderComplianceResponse:
        """
        本接口（DescribeCrossBorderCompliance）用于查询用户创建的合规化资质审批单。
        服务商可以查询服务名下的任意 `APPID` 创建的审批单；非服务商，只能查询自己审批单。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderCompliance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderComplianceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCrossBorderFlowMonitor(
            self,
            request: models.DescribeCrossBorderFlowMonitorRequest,
            opts: Dict = None,
    ) -> models.DescribeCrossBorderFlowMonitorResponse:
        """
        本接口（DescribeCrossBorderFlowMonitor）用于查询跨境带宽监控数据，该接口目前只提供给服务商联通使用。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCrossBorderFlowMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCrossBorderFlowMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomerGatewayVendors(
            self,
            request: models.DescribeCustomerGatewayVendorsRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomerGatewayVendorsResponse:
        """
        本接口（DescribeCustomerGatewayVendors）用于查询可支持的对端网关厂商信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomerGatewayVendors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomerGatewayVendorsResponse
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
        
    async def DescribeDhcpIps(
            self,
            request: models.DescribeDhcpIpsRequest,
            opts: Dict = None,
    ) -> models.DescribeDhcpIpsResponse:
        """
        本接口（DescribeDhcpIps）用于查询DhcpIp列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDhcpIps"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDhcpIpsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectGatewayCcnRoutes(
            self,
            request: models.DescribeDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectGatewayCcnRoutesResponse:
        """
        本接口（DescribeDirectConnectGatewayCcnRoutes）用于查询专线网关的云联网路由（IDC网段）
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDirectConnectGateways(
            self,
            request: models.DescribeDirectConnectGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeDirectConnectGatewaysResponse:
        """
        本接口（DescribeDirectConnectGateways）用于查询专线网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDirectConnectGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDirectConnectGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowLog(
            self,
            request: models.DescribeFlowLogRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowLogResponse:
        """
        本接口（DescribeFlowLog）用于查询VPC流日志实例信息。
        该接口只支持VPC流日志（即将下线）。云联网以及VPC流日志，通过[DescribeFlowLogs](https://cloud.tencent.com/document/product/215/35012)接口获取。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowLog"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowLogResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeFlowLogs(
            self,
            request: models.DescribeFlowLogsRequest,
            opts: Dict = None,
    ) -> models.DescribeFlowLogsResponse:
        """
        本接口（DescribeFlowLogs）用于查询获取流日志集合。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayFlowMonitorDetail(
            self,
            request: models.DescribeGatewayFlowMonitorDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayFlowMonitorDetailResponse:
        """
        本接口（DescribeGatewayFlowMonitorDetail）用于查询网关流量监控明细。
        * 只支持单个网关实例查询。即入参 `VpnId`、 `DirectConnectGatewayId`、 `PeeringConnectionId`、 `NatId` 最多只支持传一个，且必须传一个。
        * 如果网关有流量，但调用本接口没有返回数据，请在控制台对应网关详情页确认是否开启网关流量监控。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayFlowMonitorDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayFlowMonitorDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGatewayFlowQos(
            self,
            request: models.DescribeGatewayFlowQosRequest,
            opts: Dict = None,
    ) -> models.DescribeGatewayFlowQosResponse:
        """
        本接口（DescribeGatewayFlowQos）用于查询网关来访IP流控带宽。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGatewayFlowQos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGatewayFlowQosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeGlobalRoutes(
            self,
            request: models.DescribeGlobalRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeGlobalRoutesResponse:
        """
        查询全局路由列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeGlobalRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeGlobalRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHaVips(
            self,
            request: models.DescribeHaVipsRequest,
            opts: Dict = None,
    ) -> models.DescribeHaVipsResponse:
        """
        本接口（DescribeHaVips）用于查询高可用虚拟IP（HAVIP）列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHaVips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHaVipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHighPriorityRouteTables(
            self,
            request: models.DescribeHighPriorityRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeHighPriorityRouteTablesResponse:
        """
        查询高优路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHighPriorityRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHighPriorityRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHighPriorityRoutes(
            self,
            request: models.DescribeHighPriorityRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeHighPriorityRoutesResponse:
        """
        查询高优路由表条目信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHighPriorityRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHighPriorityRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIPv6Addresses(
            self,
            request: models.DescribeIPv6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIPv6AddressesResponse:
        """
        本接口（DescribeIPv6Addresses）用于查询一个或多个弹性公网 IPv6（简称 EIPv6）实例的详细信息。

        - 支持查询您在指定地域的弹性公网 IPv6 和传统弹性公网 IPv6 实例信息
        - 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIPv6。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIPv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIPv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceJumbo(
            self,
            request: models.DescribeInstanceJumboRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceJumboResponse:
        """
        本接口用于检查云服务器是否支持巨帧。
        使用限制：
        1. 需要CAM策略授权该接口的操作权限，并且授权对应实例的读取权限(该接口会访问CVM实例，所以会校验是否有实例的CAM权限)。例如：CAM action放通vpc:DescribeInstanceJumbo；resource放通qcs::cvm:ap-guangzhou:uin/2126195383:instance/*。
        2. 实例迁移前后，可能会出现该接口返回的巨帧状态前后不一致（需要检查迁移前后实例所在的宿主机是否都支持巨帧，一种可能的原因为实例迁移到了不支持巨帧的宿主机）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceJumbo"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceJumboResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIp6Addresses(
            self,
            request: models.DescribeIp6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeIp6AddressesResponse:
        """
        本接口（DescribeIp6Addresses）用于查询一个或多个传统弹性公网 IPv6 实例的详细信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIp6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIp6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIp6TranslatorQuota(
            self,
            request: models.DescribeIp6TranslatorQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeIp6TranslatorQuotaResponse:
        """
        查询账户在指定地域IPV6转换实例和规则的配额
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIp6TranslatorQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIp6TranslatorQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIp6Translators(
            self,
            request: models.DescribeIp6TranslatorsRequest,
            opts: Dict = None,
    ) -> models.DescribeIp6TranslatorsResponse:
        """
        1. 该接口用于查询账户下的IPV6转换实例及其绑定的转换规则信息
        2. 支持过滤查询
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIp6Translators"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIp6TranslatorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpGeolocationDatabaseUrl(
            self,
            request: models.DescribeIpGeolocationDatabaseUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeIpGeolocationDatabaseUrlResponse:
        """
        本接口（DescribeIpGeolocationDatabaseUrl）用于获取IP地理位置库下载链接。
        <font color="#FF0000">本接口即将下线，仅供存量用户使用，暂停新增用户。</font>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpGeolocationDatabaseUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpGeolocationDatabaseUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeIpGeolocationInfos(
            self,
            request: models.DescribeIpGeolocationInfosRequest,
            opts: Dict = None,
    ) -> models.DescribeIpGeolocationInfosResponse:
        """
        本接口（DescribeIpGeolocationInfos）用于查询IP地址信息，包括地理位置信息和网络信息。
        <font color="#FF0000">本接口即将下线，仅供存量客户使用，暂停新增用户。</font>
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeIpGeolocationInfos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeIpGeolocationInfosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLocalGateway(
            self,
            request: models.DescribeLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.DescribeLocalGatewayResponse:
        """
        本接口（DescribeLocalGateway）用于查询CDC的本地网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewayDestinationIpPortTranslationNatRules(
            self,
            request: models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse:
        """
        本接口（DescribeNatGatewayDestinationIpPortTranslationNatRules）用于查询NAT网关端口转发规则对象数组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewayDestinationIpPortTranslationNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewayDirectConnectGatewayRoute(
            self,
            request: models.DescribeNatGatewayDirectConnectGatewayRouteRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewayDirectConnectGatewayRouteResponse:
        """
        查询专线绑定NAT的路由
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewayDirectConnectGatewayRoute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewayDirectConnectGatewayRouteResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewayFlowMonitorDetail(
            self,
            request: models.DescribeNatGatewayFlowMonitorDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewayFlowMonitorDetailResponse:
        """
        本接口（DescribeNatGatewayFlowMonitorDetail）用于查询NAT网关流量监控明细。

        - 只支持单个网关实例查询。即入参 `NatGatewayId` 最多只支持传一个，且必须传一个。
        - 如果网关有流量，但调用本接口没有返回数据，请在控制台对应网关详情页确认是否开启网关流量监控。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewayFlowMonitorDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewayFlowMonitorDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewaySourceIpTranslationNatRules(
            self,
            request: models.DescribeNatGatewaySourceIpTranslationNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewaySourceIpTranslationNatRulesResponse:
        """
        本接口（DescribeNatGatewaySourceIpTranslationNatRules）用于查询NAT网关SNAT转发规则对象数组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewaySourceIpTranslationNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewaySourceIpTranslationNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGatewayZones(
            self,
            request: models.DescribeNatGatewayZonesRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewayZonesResponse:
        """
        本接口(DescribeNatGatewayZones)用于查询NAT网关可售卖的可用区信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGatewayZones"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewayZonesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNatGateways(
            self,
            request: models.DescribeNatGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribeNatGatewaysResponse:
        """
        本接口（DescribeNatGateways）用于查询 NAT 网关。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNatGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNatGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetDetectStates(
            self,
            request: models.DescribeNetDetectStatesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetDetectStatesResponse:
        """
        本接口(DescribeNetDetectStates)用于查询网络探测验证结果列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetDetectStates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetDetectStatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetDetects(
            self,
            request: models.DescribeNetDetectsRequest,
            opts: Dict = None,
    ) -> models.DescribeNetDetectsResponse:
        """
        本接口（DescribeNetDetects）用于查询网络探测列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetDetects"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetDetectsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkAccountType(
            self,
            request: models.DescribeNetworkAccountTypeRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkAccountTypeResponse:
        """
        判断用户在网络侧的用户类型，如标准（带宽上移），传统（非上移）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkAccountType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkAccountTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkAclQuintupleEntries(
            self,
            request: models.DescribeNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkAclQuintupleEntriesResponse:
        """
        本接口（DescribeNetworkAclQuintupleEntries）查询入方向或出方向网络ACL五元组条目列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkAcls(
            self,
            request: models.DescribeNetworkAclsRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkAclsResponse:
        """
        本接口（DescribeNetworkAcls）用于查询网络ACL列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkAcls"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkAclsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkInterfaceLimit(
            self,
            request: models.DescribeNetworkInterfaceLimitRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkInterfaceLimitResponse:
        """
        本接口（DescribeNetworkInterfaceLimit）根据CVM实例ID或弹性网卡ID查询弹性网卡配额，返回该CVM实例或弹性网卡能绑定的弹性网卡配额，以及弹性网卡可以分配的IP配额。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkInterfaceLimit"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkInterfaceLimitResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkInterfaces(
            self,
            request: models.DescribeNetworkInterfacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkInterfacesResponse:
        """
        本接口（DescribeNetworkInterfaces）用于查询弹性网卡列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNatGatewayDestinationIpPortTranslationNatRules(
            self,
            request: models.DescribePrivateNatGatewayDestinationIpPortTranslationNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNatGatewayDestinationIpPortTranslationNatRulesResponse:
        """
        本接口（DescribePrivateNatGatewayDestinationIpPortTranslationNatRules）用于查询私网NAT网关目的端口转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNatGatewayDestinationIpPortTranslationNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNatGatewayDestinationIpPortTranslationNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNatGatewayLimits(
            self,
            request: models.DescribePrivateNatGatewayLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNatGatewayLimitsResponse:
        """
        本接口（DescribePrivateNatGatewayLimits）用于查询可创建的私网NAT网关配额数量
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNatGatewayLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNatGatewayLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNatGatewayRegions(
            self,
            request: models.DescribePrivateNatGatewayRegionsRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNatGatewayRegionsResponse:
        """
        本接口（DescribePrivateNatGatewayRegions）用于查询查询私网NAT网关可支持地域
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNatGatewayRegions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNatGatewayRegionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNatGatewayTranslationAclRules(
            self,
            request: models.DescribePrivateNatGatewayTranslationAclRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNatGatewayTranslationAclRulesResponse:
        """
        本接口（DescribePrivateNatGatewayTranslationAclRules）用于查询私网NAT网关源端转换访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNatGatewayTranslationAclRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNatGatewayTranslationAclRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNatGatewayTranslationNatRules(
            self,
            request: models.DescribePrivateNatGatewayTranslationNatRulesRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNatGatewayTranslationNatRulesResponse:
        """
        本接口（DescribePrivateNatGatewayTranslationNatRules）用于查询私网NAT网关源端转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNatGatewayTranslationNatRules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNatGatewayTranslationNatRulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePrivateNatGateways(
            self,
            request: models.DescribePrivateNatGatewaysRequest,
            opts: Dict = None,
    ) -> models.DescribePrivateNatGatewaysResponse:
        """
        本接口（DescribePrivateNatGateways）用于查询私网NAT网关
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePrivateNatGateways"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePrivateNatGatewaysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeProductQuota(
            self,
            request: models.DescribeProductQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeProductQuotaResponse:
        """
        本接口（DescribeProductQuota）用于查询网络产品的配额信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeProductQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeProductQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeReserveIpAddresses(
            self,
            request: models.DescribeReserveIpAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeReserveIpAddressesResponse:
        """
        查询内网保留 IP
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeReserveIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeReserveIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteConflicts(
            self,
            request: models.DescribeRouteConflictsRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteConflictsResponse:
        """
        本接口（DescribeRouteConflicts）用于查询自定义路由策略与云联网路由策略冲突列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteConflicts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteConflictsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteList(
            self,
            request: models.DescribeRouteListRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteListResponse:
        """
        本接口（DescribeRouteList）用于查询路由条目列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoutePolicies(
            self,
            request: models.DescribeRoutePoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeRoutePoliciesResponse:
        """
        本接口（DescribeRoutePolicies）用于查询路由策略列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoutePolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoutePoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRoutePolicyEntries(
            self,
            request: models.DescribeRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.DescribeRoutePolicyEntriesResponse:
        """
        本接口（DescribeRoutePolicyEntries）用于查询路由接收策略条目列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTableAssociatedInstances(
            self,
            request: models.DescribeRouteTableAssociatedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTableAssociatedInstancesResponse:
        """
        本接口（DescribeRouteTableAssociatedInstances）用于查询指定的云联网关联的实例所绑定的路由表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTableAssociatedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTableAssociatedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTableSelectionPolicies(
            self,
            request: models.DescribeRouteTableSelectionPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTableSelectionPoliciesResponse:
        """
        本接口（DescribeRouteTableSelectionPolicies）用于查询云联网路由表选择策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTableSelectionPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTableSelectionPoliciesResponse
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
        
    async def DescribeRoutes(
            self,
            request: models.DescribeRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeRoutesResponse:
        """
        本接口（DescribeRoutes）用于查询路由列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupAssociationStatistics(
            self,
            request: models.DescribeSecurityGroupAssociationStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupAssociationStatisticsResponse:
        """
        本接口（DescribeSecurityGroupAssociationStatistics）用于查询安全组关联的实例统计。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupAssociationStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupAssociationStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupExpandedPolicies(
            self,
            request: models.DescribeSecurityGroupExpandedPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupExpandedPoliciesResponse:
        """
        本接口（DescribeSecurityGroupExpandedPolicies）用于查看参数模板展开后的安全组规则。本接口会通过缓存降低请求后端服务的调用次数，因此拉取结果会存在延迟（缓存超时时间为1分钟）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupExpandedPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupExpandedPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupLimits(
            self,
            request: models.DescribeSecurityGroupLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupLimitsResponse:
        """
        本接口(DescribeSecurityGroupLimits)用于查询用户安全组配额。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupPolicies(
            self,
            request: models.DescribeSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupPoliciesResponse:
        """
        本接口（DescribeSecurityGroupPolicies）用于查询安全组规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupReferences(
            self,
            request: models.DescribeSecurityGroupReferencesRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupReferencesResponse:
        """
        本接口（DescribeSecurityGroupReferences）用于查询安全组被引用信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupReferences"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupReferencesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroups(
            self,
            request: models.DescribeSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupsResponse:
        """
        本接口（DescribeSecurityGroups）用于查询安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceTemplateGroupInstances(
            self,
            request: models.DescribeServiceTemplateGroupInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceTemplateGroupInstancesResponse:
        """
        本接口（DescribeServiceTemplateGroupInstances）用于查询参数模板协议端口组关联的实例列表。本接口不会返回查询的结果，需要根据返回的RequestId调用DescribeVpcTaskResult接口获取结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceTemplateGroupInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceTemplateGroupInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceTemplateGroups(
            self,
            request: models.DescribeServiceTemplateGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceTemplateGroupsResponse:
        """
        本接口（DescribeServiceTemplateGroups）用于查询协议端口模板集合。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceTemplateGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceTemplateGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceTemplateInstances(
            self,
            request: models.DescribeServiceTemplateInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceTemplateInstancesResponse:
        """
        本接口（DescribeServiceTemplateInstances）用于查询参数模板协议端口关联的实例列表。本接口不会返回查询的结果，需要根据返回的RequestId调用DescribeVpcTaskResult接口获取结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceTemplateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceTemplateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeServiceTemplates(
            self,
            request: models.DescribeServiceTemplatesRequest,
            opts: Dict = None,
    ) -> models.DescribeServiceTemplatesResponse:
        """
        本接口（DescribeServiceTemplates）用于查询协议端口模板。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeServiceTemplates"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeServiceTemplatesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSgSnapshotFileContent(
            self,
            request: models.DescribeSgSnapshotFileContentRequest,
            opts: Dict = None,
    ) -> models.DescribeSgSnapshotFileContentResponse:
        """
        本接口（DescribeSgSnapshotFileContent）用于查询安全组快照文件内容。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSgSnapshotFileContent"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSgSnapshotFileContentResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotAttachedInstances(
            self,
            request: models.DescribeSnapshotAttachedInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotAttachedInstancesResponse:
        """
        本接口（DescribeSnapshotAttachedInstances）用于查询快照策略关联实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotAttachedInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotAttachedInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotFiles(
            self,
            request: models.DescribeSnapshotFilesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotFilesResponse:
        """
        本接口（DescribeSnapshotFiles）用于查询快照文件。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotFiles"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotFilesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshotPolicies(
            self,
            request: models.DescribeSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotPoliciesResponse:
        """
        本接口（DescribeSnapshotPolicies）用于查询快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSpecificTrafficPackageUsedDetails(
            self,
            request: models.DescribeSpecificTrafficPackageUsedDetailsRequest,
            opts: Dict = None,
    ) -> models.DescribeSpecificTrafficPackageUsedDetailsResponse:
        """
        本接口 (DescribeSpecificTrafficPackageUsedDetails) 用于查询指定 共享流量包 的用量明细。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSpecificTrafficPackageUsedDetails"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSpecificTrafficPackageUsedDetailsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnetResourceDashboard(
            self,
            request: models.DescribeSubnetResourceDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetResourceDashboardResponse:
        """
        本接口(DescribeSubnetResourceDashboard)用于查看Subnet资源信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnetResourceDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetResourceDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnets(
            self,
            request: models.DescribeSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetsResponse:
        """
        本接口（DescribeSubnets）用于查询子网列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        本接口（DescribeTaskResult）用于查询EIP异步任务执行结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTemplateLimits(
            self,
            request: models.DescribeTemplateLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeTemplateLimitsResponse:
        """
        本接口（DescribeTemplateLimits）用于查询参数模板配额列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTemplateLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTemplateLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTenantCcns(
            self,
            request: models.DescribeTenantCcnsRequest,
            opts: Dict = None,
    ) -> models.DescribeTenantCcnsResponse:
        """
        本接口（DescribeTenantCcns）用于获取要锁定的云联网实例列表。
        该接口一般用来封禁出口限速的云联网实例, 目前联通内部运营系统通过云API调用, 因为出口限速无法按地域间封禁, 只能按更粗的云联网实例粒度封禁, 如果是地域间限速, 一般可以通过更细的限速实例粒度封禁（DescribeCrossBorderCcnRegionBandwidthLimits）
        如有需要, 可以封禁任意云联网实例, 可接入到内部运营系统
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTenantCcns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTenantCcnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficMirrors(
            self,
            request: models.DescribeTrafficMirrorsRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficMirrorsResponse:
        """
        本接口（DescribeTrafficMirrors）用于查询流量镜像实例信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficMirrors"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficMirrorsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficPackages(
            self,
            request: models.DescribeTrafficPackagesRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficPackagesResponse:
        """
        本接口 (DescribeTrafficPackages)  用于查询共享流量包详细信息，包括共享流量包唯一标识ID，名称，流量使用信息等
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficPackages"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficPackagesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTrafficQosPolicy(
            self,
            request: models.DescribeTrafficQosPolicyRequest,
            opts: Dict = None,
    ) -> models.DescribeTrafficQosPolicyResponse:
        """
        查询流量调度规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTrafficQosPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTrafficQosPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeUsedIpAddress(
            self,
            request: models.DescribeUsedIpAddressRequest,
            opts: Dict = None,
    ) -> models.DescribeUsedIpAddressResponse:
        """
        本接口(DescribeUsedIpAddress)用于查询Subnet或者Vpc内的ip的使用情况，
        如ip被占用，返回占用ip的资源类别与id；如未被占用，返回空值
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeUsedIpAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeUsedIpAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcEndPoint(
            self,
            request: models.DescribeVpcEndPointRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcEndPointResponse:
        """
        本接口（DescribeVpcEndPoint）用于查询终端节点列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcEndPoint"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcEndPointResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcEndPointService(
            self,
            request: models.DescribeVpcEndPointServiceRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcEndPointServiceResponse:
        """
        本接口（DescribeVpcEndPointService）用于查询终端节点服务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcEndPointService"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcEndPointServiceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcEndPointServiceWhiteList(
            self,
            request: models.DescribeVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcEndPointServiceWhiteListResponse:
        """
        本接口（DescribeVpcEndPointServiceWhiteList）用于查询终端节点服务的服务白名单列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcInstances(
            self,
            request: models.DescribeVpcInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcInstancesResponse:
        """
        本接口（DescribeVpcInstances）用于查询VPC下的云主机实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcIpv6Addresses(
            self,
            request: models.DescribeVpcIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcIpv6AddressesResponse:
        """
        本接口（DescribeVpcIpv6Addresses）用于查询 `VPC` `IPv6` 信息。
        只能查询已使用的`IPv6`信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcLimits(
            self,
            request: models.DescribeVpcLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcLimitsResponse:
        """
        本接口（DescribeVpcLimits）用于获取私有网络配额，部分私有网络的配额有地域属性。
        LimitTypes取值范围：
        * appid-max-vpcs （每个开发商每个地域可创建的VPC数）。
        * vpc-max-subnets（每个VPC可创建的子网数）。
        * vpc-max-route-tables（每个VPC可创建的路由表数）。
        * route-table-max-policies（每个路由表可添加的策略数）。
        * vpc-max-vpn-gateways（每个VPC可创建的VPN网关数）。
        * appid-max-custom-gateways（每个开发商可创建的对端网关数）。
        * appid-max-vpn-connections（每个开发商可创建的VPN通道数）。
        * custom-gateway-max-vpn-connections（每个对端网关可创建的VPN通道数）。
        * vpn-gateway-max-custom-gateways（每个VPNGW可以创建的通道数）。
        * vpc-max-network-acls（每个VPC可创建的网络ACL数）。
        * network-acl-max-inbound-policies（每个网络ACL可添加的入站规则数）。
        * network-acl-max-outbound-policies（每个网络ACL可添加的出站规则数）。
        * vpc-max-vpcpeers（每个VPC可创建的对等连接数）。
        * vpc-max-available-vpcpeers（每个VPC可创建的有效对等连接数）。
        * vpc-max-basic-network-interconnections（每个VPC可创建的基础网络云主机与VPC互通数）。
        * direct-connection-max-snats（每个专线网关可创建的SNAT数）。
        * direct-connection-max-dnats（每个专线网关可创建的DNAT数）。
        * direct-connection-max-snapts（每个专线网关可创建的SNAPT数）。
        * direct-connection-max-dnapts（每个专线网关可创建的DNAPT数）。
        * vpc-max-nat-gateways（每个VPC可创建的NAT网关数）。
        * nat-gateway-max-eips（每个NAT可以购买的外网IP数量）。
        * vpc-max-enis（每个VPC可创建弹性网卡数）。
        * vpc-max-havips（每个VPC可创建HAVIP数）。
        * eni-max-private-ips（每个ENI可以绑定的内网IP数（ENI未绑定子机））。
        * nat-gateway-max-dnapts（每个NAT网关可创建的DNAPT数）。
        * vpc-max-ipv6s（每个VPC可分配的IPv6地址数）。
        * eni-max-ipv6s（每个ENI可分配的IPv6地址数）。
        * vpc-max-assistant_cidrs（每个VPC可分配的辅助CIDR数）。
        * appid-max-end-point-services （每个开发商每个地域可创建的终端节点服务个数）。
        * appid-max-end-point-service-white-lists （每个开发商每个地域可创建的终端节点服务白名单个数）。
        * vpc-max-cmcc-ipv6-cidrs （每个VPC可创建的移动IPv6 CIDR个数）。
        * vpc-max-ctcc-ipv6-cidrs （每个VPC可创建的电信IPv6 CIDR个数）。
        * vpc-max-cucc-ipv6-cidrs （每个VPC可创建的联调IPv6 CIDR个数）。
        * vpc-max-bgp-ipv6-cidrs （每个VPC可创建的默认IPv6 CIDR个数）。
        * vpc-max-custom-ipv6-cidrs （每个VPC可创建的自定义IPv6 CIDR个数）。
        * vpc-max-ula-ipv6-cidrs （每个VPC可创建的ULA IPv6 CIDR个数）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcPeeringConnections(
            self,
            request: models.DescribeVpcPeeringConnectionsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcPeeringConnectionsResponse:
        """
        查询私有网络对等连接。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcPeeringConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcPeeringConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcPrivateIpAddresses(
            self,
            request: models.DescribeVpcPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcPrivateIpAddressesResponse:
        """
        本接口（DescribeVpcPrivateIpAddresses）用于查询VPC内网IP信息。<br />
        只能查询已使用的IP信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcPrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcPrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcResourceDashboard(
            self,
            request: models.DescribeVpcResourceDashboardRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcResourceDashboardResponse:
        """
        本接口(DescribeVpcResourceDashboard)用于查看VPC资源信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcResourceDashboard"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcResourceDashboardResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcTaskResult(
            self,
            request: models.DescribeVpcTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcTaskResultResponse:
        """
        本接口（DescribeVpcTaskResult）用于查询VPC任务执行结果。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcTaskResultResponse
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
        本接口（DescribeVpnConnections）用于查询VPN通道列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnConnections"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnConnectionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGatewayCcnRoutes(
            self,
            request: models.DescribeVpnGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewayCcnRoutesResponse:
        """
        本接口（DescribeVpnGatewayCcnRoutes）用于查询VPN网关云联网路由。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGatewayRoutes(
            self,
            request: models.DescribeVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewayRoutesResponse:
        """
        本接口（DescribeVpnGatewayRoutes）用于查询VPN网关路由。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGatewaySslClients(
            self,
            request: models.DescribeVpnGatewaySslClientsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewaySslClientsResponse:
        """
        本接口（DescribeVpnGatewaySslClients）用于查询SSL-VPN-CLIENT 列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGatewaySslClients"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewaySslClientsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpnGatewaySslServers(
            self,
            request: models.DescribeVpnGatewaySslServersRequest,
            opts: Dict = None,
    ) -> models.DescribeVpnGatewaySslServersResponse:
        """
        本接口（DescribeVpnGatewaySslServers）用于查询SSL-VPN SERVER 列表信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpnGatewaySslServers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpnGatewaySslServersResponse
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
        
    async def DetachCcnInstances(
            self,
            request: models.DetachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachCcnInstancesResponse:
        """
        本接口（DetachCcnInstances）用于从云联网实例中解关联指定的网络实例。<br />
        解关联网络实例后，相应的路由策略会一并删除。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachClassicLinkVpc(
            self,
            request: models.DetachClassicLinkVpcRequest,
            opts: Dict = None,
    ) -> models.DetachClassicLinkVpcResponse:
        """
        本接口(DetachClassicLinkVpc)用于删除私有网络和基础网络设备互通。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DetachClassicLinkVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachClassicLinkVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachNetworkInterface(
            self,
            request: models.DetachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DetachNetworkInterfaceResponse:
        """
        本接口（DetachNetworkInterface）用于弹性网卡解绑云服务器。
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachSnapshotInstances(
            self,
            request: models.DetachSnapshotInstancesRequest,
            opts: Dict = None,
    ) -> models.DetachSnapshotInstancesResponse:
        """
        本接口（DetachSnapshotInstances）用于快照策略解关联实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachSnapshotInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachSnapshotInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableCcnRoutes(
            self,
            request: models.DisableCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.DisableCcnRoutesResponse:
        """
        本接口（DisableCcnRoutes）用于禁用已经启用的云联网（CCN）路由。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableFlowLogs(
            self,
            request: models.DisableFlowLogsRequest,
            opts: Dict = None,
    ) -> models.DisableFlowLogsResponse:
        """
        本接口（DisableFlowLogs）用于停止流日志。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableGatewayFlowMonitor(
            self,
            request: models.DisableGatewayFlowMonitorRequest,
            opts: Dict = None,
    ) -> models.DisableGatewayFlowMonitorResponse:
        """
        本接口（DisableGatewayFlowMonitor）用于关闭网关流量监控。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableGatewayFlowMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableGatewayFlowMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRoutes(
            self,
            request: models.DisableRoutesRequest,
            opts: Dict = None,
    ) -> models.DisableRoutesResponse:
        """
        本接口（DisableRoutes）用于禁用已启用的子网路由
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableSnapshotPolicies(
            self,
            request: models.DisableSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.DisableSnapshotPoliciesResponse:
        """
        本接口（DisableSnapshotPolicies）用于停用快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "DisableSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableVpnGatewaySslClientCert(
            self,
            request: models.DisableVpnGatewaySslClientCertRequest,
            opts: Dict = None,
    ) -> models.DisableVpnGatewaySslClientCertResponse:
        """
        禁用SSL-VPN-CLIENT 证书
        """
        
        kwargs = {}
        kwargs["action"] = "DisableVpnGatewaySslClientCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableVpnGatewaySslClientCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateAddress(
            self,
            request: models.DisassociateAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateAddressResponse:
        """
        本接口 (DisassociateAddress) 用于解绑[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 支持CVM实例，弹性网卡上的EIP解绑。
        * 不支持NAT上的EIP解绑。NAT上的EIP解绑请参考[DisassociateNatGatewayAddress](https://cloud.tencent.com/document/api/215/36716)。
        * 只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateDhcpIpWithAddressIp(
            self,
            request: models.DisassociateDhcpIpWithAddressIpRequest,
            opts: Dict = None,
    ) -> models.DisassociateDhcpIpWithAddressIpResponse:
        """
        本接口（DisassociateDhcpIpWithAddressIp）用于将DhcpIp已绑定的弹性公网IP（EIP）解除绑定。<br />
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateDhcpIpWithAddressIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateDhcpIpWithAddressIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateDirectConnectGatewayNatGateway(
            self,
            request: models.DisassociateDirectConnectGatewayNatGatewayRequest,
            opts: Dict = None,
    ) -> models.DisassociateDirectConnectGatewayNatGatewayResponse:
        """
        将专线网关与NAT网关解绑，解绑之后，专线网关将不能通过NAT网关访问公网
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateDirectConnectGatewayNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateDirectConnectGatewayNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateHaVipInstance(
            self,
            request: models.DisassociateHaVipInstanceRequest,
            opts: Dict = None,
    ) -> models.DisassociateHaVipInstanceResponse:
        """
        本接口（DisassociateHaVipInstance）用于HAVIP解绑子机或网卡（去掉HaVip飘移范围）。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateHaVipInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateHaVipInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateIPv6Address(
            self,
            request: models.DisassociateIPv6AddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateIPv6AddressResponse:
        """
        本接口（DisassociateIPv6Address）用于解绑弹性公网 IPv6（简称EIPv6）实例。

        - 支持对 CVM、弹性网卡绑定的 EIPv6 实例进行解绑操作。
        - 只有状态为 BIND 和 BIND_ENI 的 EIPv6 实例才能进行解绑操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateIPv6Address"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateIPv6AddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateNatGatewayAddress(
            self,
            request: models.DisassociateNatGatewayAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateNatGatewayAddressResponse:
        """
        本接口（DisassociateNatGatewayAddress）用于NAT网关解绑弹性IP。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateNatGatewayAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateNatGatewayAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateNetworkAclSubnets(
            self,
            request: models.DisassociateNetworkAclSubnetsRequest,
            opts: Dict = None,
    ) -> models.DisassociateNetworkAclSubnetsResponse:
        """
        本接口（DisassociateNetworkAclSubnets）用于网络ACL解关联VPC下的子网。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateNetworkAclSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateNetworkAclSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateNetworkInterfaceSecurityGroups(
            self,
            request: models.DisassociateNetworkInterfaceSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateNetworkInterfaceSecurityGroupsResponse:
        """
        本接口（DisassociateNetworkInterfaceSecurityGroups）用于弹性网卡解绑安全组。支持弹性网卡完全解绑安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateNetworkInterfaceSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateNetworkInterfaceSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateVpcEndPointSecurityGroups(
            self,
            request: models.DisassociateVpcEndPointSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateVpcEndPointSecurityGroupsResponse:
        """
        本接口（DisassociateVpcEndPointSecurityGroups）用于终端节点解绑安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateVpcEndPointSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateVpcEndPointSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadCustomerGatewayConfiguration(
            self,
            request: models.DownloadCustomerGatewayConfigurationRequest,
            opts: Dict = None,
    ) -> models.DownloadCustomerGatewayConfigurationResponse:
        """
        本接口（DownloadCustomerGatewayConfiguration）用于下载VPN通道配置。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadCustomerGatewayConfiguration"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadCustomerGatewayConfigurationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DownloadVpnGatewaySslClientCert(
            self,
            request: models.DownloadVpnGatewaySslClientCertRequest,
            opts: Dict = None,
    ) -> models.DownloadVpnGatewaySslClientCertResponse:
        """
        本接口（DownloadVpnGatewaySslClientCert）用于下载SSL-VPN-CLIENT 客户端证书。
        """
        
        kwargs = {}
        kwargs["action"] = "DownloadVpnGatewaySslClientCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DownloadVpnGatewaySslClientCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableCcnRoutes(
            self,
            request: models.EnableCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.EnableCcnRoutesResponse:
        """
        本接口（EnableCcnRoutes）用于启用已经加入云联网（CCN）的路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableFlowLogs(
            self,
            request: models.EnableFlowLogsRequest,
            opts: Dict = None,
    ) -> models.EnableFlowLogsResponse:
        """
        本接口（EnableFlowLogs）用于启动流日志。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableFlowLogs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableFlowLogsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableGatewayFlowMonitor(
            self,
            request: models.EnableGatewayFlowMonitorRequest,
            opts: Dict = None,
    ) -> models.EnableGatewayFlowMonitorResponse:
        """
        本接口（EnableGatewayFlowMonitor）用于开启网关流量监控。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableGatewayFlowMonitor"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableGatewayFlowMonitorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRoutes(
            self,
            request: models.EnableRoutesRequest,
            opts: Dict = None,
    ) -> models.EnableRoutesResponse:
        """
        本接口（EnableRoutes）用于启用已禁用的子网路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableSnapshotPolicies(
            self,
            request: models.EnableSnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.EnableSnapshotPoliciesResponse:
        """
        本接口（EnableSnapshotPolicies）用于启用快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableSnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableSnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableVpcEndPointConnect(
            self,
            request: models.EnableVpcEndPointConnectRequest,
            opts: Dict = None,
    ) -> models.EnableVpcEndPointConnectResponse:
        """
        本接口（EnableVpcEndPointConnect）用于是否接受终端节点连接请求。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableVpcEndPointConnect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableVpcEndPointConnectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableVpnGatewaySslClientCert(
            self,
            request: models.EnableVpnGatewaySslClientCertRequest,
            opts: Dict = None,
    ) -> models.EnableVpnGatewaySslClientCertResponse:
        """
        本接口（EnableVpnGatewaySslClientCert）用于启用SSL-VPN-CLIENT 证书。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableVpnGatewaySslClientCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableVpnGatewaySslClientCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GenerateVpnConnectionDefaultHealthCheckIp(
            self,
            request: models.GenerateVpnConnectionDefaultHealthCheckIpRequest,
            opts: Dict = None,
    ) -> models.GenerateVpnConnectionDefaultHealthCheckIpResponse:
        """
        本接口（GenerateVpnConnectionDefaultHealthCheckIp）用于获取一对VPN通道健康检查地址。
        """
        
        kwargs = {}
        kwargs["action"] = "GenerateVpnConnectionDefaultHealthCheckIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GenerateVpnConnectionDefaultHealthCheckIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def GetCcnRegionBandwidthLimits(
            self,
            request: models.GetCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.GetCcnRegionBandwidthLimitsResponse:
        """
        本接口（GetCcnRegionBandwidthLimits）用于查询云联网相关地域带宽信息，其中预付费模式的云联网仅支持地域间限速，后付费模式的云联网支持地域间限速和地域出口限速。
        """
        
        kwargs = {}
        kwargs["action"] = "GetCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.GetCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HaVipAssociateAddressIp(
            self,
            request: models.HaVipAssociateAddressIpRequest,
            opts: Dict = None,
    ) -> models.HaVipAssociateAddressIpResponse:
        """
        本接口（HaVipAssociateAddressIp）用于高可用虚拟IP（HAVIP）绑定弹性公网IP（EIP）。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。
        """
        
        kwargs = {}
        kwargs["action"] = "HaVipAssociateAddressIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HaVipAssociateAddressIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def HaVipDisassociateAddressIp(
            self,
            request: models.HaVipDisassociateAddressIpRequest,
            opts: Dict = None,
    ) -> models.HaVipDisassociateAddressIpResponse:
        """
        本接口（HaVipDisassociateAddressIp）用于将高可用虚拟IP（HAVIP）已绑定的弹性公网IP（EIP）解除绑定。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。
        """
        
        kwargs = {}
        kwargs["action"] = "HaVipDisassociateAddressIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.HaVipDisassociateAddressIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquirePriceCreateDirectConnectGateway(
            self,
            request: models.InquirePriceCreateDirectConnectGatewayRequest,
            opts: Dict = None,
    ) -> models.InquirePriceCreateDirectConnectGatewayResponse:
        """
        本接口（DescribePriceCreateDirectConnectGateway）用于创建专线网关询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquirePriceCreateDirectConnectGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquirePriceCreateDirectConnectGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceAllocateAddresses(
            self,
            request: models.InquiryPriceAllocateAddressesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceAllocateAddressesResponse:
        """
        本接口（InquiryPriceAllocateAddresses）用于新购弹性公网IP询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceAllocateAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceAllocateAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceCreateVpnGateway(
            self,
            request: models.InquiryPriceCreateVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceCreateVpnGatewayResponse:
        """
        本接口（InquiryPriceCreateVpnGateway）用于创建VPN网关询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceCreateVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceCreateVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceModifyAddressesBandwidth(
            self,
            request: models.InquiryPriceModifyAddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceModifyAddressesBandwidthResponse:
        """
        本接口（InquiryPriceModifyAddressesBandwidth）用于EIP修改带宽询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceModifyAddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceModifyAddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewAddresses(
            self,
            request: models.InquiryPriceRenewAddressesRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewAddressesResponse:
        """
        本接口（InquiryPriceRenewAddresses）用于续费预付费弹性公网IP询价，只支持包月按带宽预付费的计费模式。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceRenewVpnGateway(
            self,
            request: models.InquiryPriceRenewVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceRenewVpnGatewayResponse:
        """
        本接口（InquiryPriceRenewVpnGateway）用于续费VPN网关询价。目前仅支持IPSEC类型网关的询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceRenewVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceRenewVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def InquiryPriceResetVpnGatewayInternetMaxBandwidth(
            self,
            request: models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse:
        """
        本接口（InquiryPriceResetVpnGatewayInternetMaxBandwidth）用于调整VPN网关带宽上限询价。
        """
        
        kwargs = {}
        kwargs["action"] = "InquiryPriceResetVpnGatewayInternetMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LockCcnBandwidths(
            self,
            request: models.LockCcnBandwidthsRequest,
            opts: Dict = None,
    ) -> models.LockCcnBandwidthsResponse:
        """
        本接口（LockCcnBandwidths）用户锁定云联网限速实例。
        该接口一般用来封禁地域间限速的云联网实例下的限速实例, 目前联通内部运营系统通过云API调用, 如果是出口限速, 一般使用更粗的云联网实例粒度封禁（LockCcns）。
        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统。
        """
        
        kwargs = {}
        kwargs["action"] = "LockCcnBandwidths"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LockCcnBandwidthsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def LockCcns(
            self,
            request: models.LockCcnsRequest,
            opts: Dict = None,
    ) -> models.LockCcnsResponse:
        """
        本接口（LockCcns）用于锁定云联网实例

        该接口一般用来封禁出口限速的云联网实例, 目前联通内部运营系统通过云API调用, 因为出口限速无法按地域间封禁, 只能按更粗的云联网实例粒度封禁, 如果是地域间限速, 一般可以通过更细的限速实例粒度封禁（LockCcnBandwidths）

        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统
        """
        
        kwargs = {}
        kwargs["action"] = "LockCcns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.LockCcnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateBandwidthPackageResources(
            self,
            request: models.MigrateBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.MigrateBandwidthPackageResourcesResponse:
        """
        本接口 (MigrateBandwidthPackageResources) 用于共享带宽包之间迁移资源
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateNetworkInterface(
            self,
            request: models.MigrateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.MigrateNetworkInterfaceResponse:
        """
        本接口（MigrateNetworkInterface）用于弹性网卡迁移。
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) `接口。
        """
        
        kwargs = {}
        kwargs["action"] = "MigrateNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigrateNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigratePrivateIpAddress(
            self,
            request: models.MigratePrivateIpAddressRequest,
            opts: Dict = None,
    ) -> models.MigratePrivateIpAddressResponse:
        """
        本接口（MigratePrivateIpAddress）用于弹性网卡内网IP迁移。
        * 该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。
        * 迁移前后的弹性网卡必须在同一个子网内。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "MigratePrivateIpAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.MigratePrivateIpAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressAttribute(
            self,
            request: models.ModifyAddressAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressAttributeResponse:
        """
        本接口 (ModifyAddressAttribute) 用于修改[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressInternetChargeType(
            self,
            request: models.ModifyAddressInternetChargeTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressInternetChargeTypeResponse:
        """
        该接口用于调整具有带宽属性弹性公网IP的网络计费模式
        * 支持BANDWIDTH_PREPAID_BY_MONTH（包月按带宽预付费）和TRAFFIC_POSTPAID_BY_HOUR（流量按小时后付费）两种网络计费模式之间的切换。
        * 每个弹性公网IP支持调整两次，次数超出则无法调整。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressInternetChargeType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressInternetChargeTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressTemplateAttribute(
            self,
            request: models.ModifyAddressTemplateAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressTemplateAttributeResponse:
        """
        本接口（ModifyAddressTemplateAttribute）用于修改IP地址模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressTemplateAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressTemplateAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressTemplateGroupAttribute(
            self,
            request: models.ModifyAddressTemplateGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressTemplateGroupAttributeResponse:
        """
        本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressTemplateGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressTemplateGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressesBandwidth(
            self,
            request: models.ModifyAddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressesBandwidthResponse:
        """
        本接口（ModifyAddressesBandwidth）用于调整[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)(简称EIP)带宽，支持后付费EIP, 预付费EIP和带宽包EIP
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressesRenewFlag(
            self,
            request: models.ModifyAddressesRenewFlagRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressesRenewFlagResponse:
        """
        本接口（ModifyAddressesRenewFlag）用于调整EIP续费标识。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressesRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressesRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAssistantCidr(
            self,
            request: models.ModifyAssistantCidrRequest,
            opts: Dict = None,
    ) -> models.ModifyAssistantCidrResponse:
        """
        本接口（ModifyAssistantCidr）用于批量修改辅助CIDR，支持新增和删除。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAssistantCidr"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAssistantCidrResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBandwidthPackageAttribute(
            self,
            request: models.ModifyBandwidthPackageAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyBandwidthPackageAttributeResponse:
        """
        接口用于修改带宽包属性，包括带宽包名称和计费模式
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBandwidthPackageAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBandwidthPackageAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyBandwidthPackageBandwidth(
            self,
            request: models.ModifyBandwidthPackageBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyBandwidthPackageBandwidthResponse:
        """
        接口用于调整[共享带宽包](https://cloud.tencent.com/document/product/684/15245)(BWP)带宽
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyBandwidthPackageBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyBandwidthPackageBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnAttachedInstancesAttribute(
            self,
            request: models.ModifyCcnAttachedInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnAttachedInstancesAttributeResponse:
        """
        修改CCN关联实例属性，目前仅修改备注description
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnAttachedInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnAttachedInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnAttribute(
            self,
            request: models.ModifyCcnAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnAttributeResponse:
        """
        本接口（ModifyCcnAttribute）用于修改云联网（CCN）的相关属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnRegionBandwidthLimitsType(
            self,
            request: models.ModifyCcnRegionBandwidthLimitsTypeRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnRegionBandwidthLimitsTypeResponse:
        """
        本接口（ModifyCcnRegionBandwidthLimitsType）用于修改后付费云联网实例修改带宽限速策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnRegionBandwidthLimitsType"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnRegionBandwidthLimitsTypeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCcnRouteTables(
            self,
            request: models.ModifyCcnRouteTablesRequest,
            opts: Dict = None,
    ) -> models.ModifyCcnRouteTablesResponse:
        """
        该接口用于修改云联网路由表名称和备注。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCcnRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCcnRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdcLDCXAttribute(
            self,
            request: models.ModifyCdcLDCXAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCdcLDCXAttributeResponse:
        """
        修改 IDC通道信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdcLDCXAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdcLDCXAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyCdcNetPlaneAttribute(
            self,
            request: models.ModifyCdcNetPlaneAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyCdcNetPlaneAttributeResponse:
        """
        修改虚拟连接
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyCdcNetPlaneAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyCdcNetPlaneAttributeResponse
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
        
    async def ModifyDhcpIpAttribute(
            self,
            request: models.ModifyDhcpIpAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDhcpIpAttributeResponse:
        """
        本接口（ModifyDhcpIpAttribute）用于修改DhcpIp属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDhcpIpAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDhcpIpAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDirectConnectGatewayAttribute(
            self,
            request: models.ModifyDirectConnectGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyDirectConnectGatewayAttributeResponse:
        """
        本接口（ModifyDirectConnectGatewayAttribute）用于修改专线网关属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDirectConnectGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDirectConnectGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyFlowLogAttribute(
            self,
            request: models.ModifyFlowLogAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyFlowLogAttributeResponse:
        """
        本接口（ModifyFlowLogAttribute）用于修改流日志属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyFlowLogAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyFlowLogAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGatewayFlowQos(
            self,
            request: models.ModifyGatewayFlowQosRequest,
            opts: Dict = None,
    ) -> models.ModifyGatewayFlowQosResponse:
        """
        本接口（ModifyGatewayFlowQos）用于调整网关流控带宽。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGatewayFlowQos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGatewayFlowQosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalRouteECMPAlgorithm(
            self,
            request: models.ModifyGlobalRouteECMPAlgorithmRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalRouteECMPAlgorithmResponse:
        """
        修改全局路由表ECMP算法 HASH 策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalRouteECMPAlgorithm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalRouteECMPAlgorithmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyGlobalRoutes(
            self,
            request: models.ModifyGlobalRoutesRequest,
            opts: Dict = None,
    ) -> models.ModifyGlobalRoutesResponse:
        """
        修改全局路由。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyGlobalRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyGlobalRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHaVipAttribute(
            self,
            request: models.ModifyHaVipAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHaVipAttributeResponse:
        """
        本接口（ModifyHaVipAttribute）用于修改高可用虚拟IP（HAVIP）属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHaVipAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHaVipAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHighPriorityRouteAttribute(
            self,
            request: models.ModifyHighPriorityRouteAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHighPriorityRouteAttributeResponse:
        """
        修改高优路由表条目属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHighPriorityRouteAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHighPriorityRouteAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHighPriorityRouteECMPAlgorithm(
            self,
            request: models.ModifyHighPriorityRouteECMPAlgorithmRequest,
            opts: Dict = None,
    ) -> models.ModifyHighPriorityRouteECMPAlgorithmResponse:
        """
        修改高优路由表 HASH 策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHighPriorityRouteECMPAlgorithm"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHighPriorityRouteECMPAlgorithmResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHighPriorityRouteTableAttribute(
            self,
            request: models.ModifyHighPriorityRouteTableAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHighPriorityRouteTableAttributeResponse:
        """
        修改高优路由表属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHighPriorityRouteTableAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHighPriorityRouteTableAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIPv6AddressesAttributes(
            self,
            request: models.ModifyIPv6AddressesAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyIPv6AddressesAttributesResponse:
        """
        本接口（ModifyIPv6AddressesAttributes）用于修改弹性公网 IPv6（简称EIPv6）实例名称。

        - 支持对弹性公网 IPv6 和传统弹性公网 IPv6 实例名称进行修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIPv6AddressesAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIPv6AddressesAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIPv6AddressesBandwidth(
            self,
            request: models.ModifyIPv6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyIPv6AddressesBandwidthResponse:
        """
        本接口（ModifyIPv6AddressesBandwidth）用于调整弹性公网 IPv6（简称EIPv6）实例的带宽上限。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIPv6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIPv6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIp6AddressesBandwidth(
            self,
            request: models.ModifyIp6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyIp6AddressesBandwidthResponse:
        """
        本接口（ModifyIp6AddressesBandwidth）用于调整传统弹性公网 IPv6 实例的带宽上限。

        - 仅支持对传统弹性公网 IPv6 实例的带宽上限进行调整。
        - 如需调整弹性公网 IPv6 实例的带宽上限，请使用 [ModifyIPv6AddressesBandwidth](https://cloud.tencent.com/document/product/215/113674) 接口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIp6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIp6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIp6Rule(
            self,
            request: models.ModifyIp6RuleRequest,
            opts: Dict = None,
    ) -> models.ModifyIp6RuleResponse:
        """
        该接口用于修改IPV6转换规则，当前仅支持修改转换规则名称，IPV4地址和IPV4端口号
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIp6Rule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIp6RuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIp6Translator(
            self,
            request: models.ModifyIp6TranslatorRequest,
            opts: Dict = None,
    ) -> models.ModifyIp6TranslatorResponse:
        """
        该接口用于修改IP6转换实例属性，当前仅支持修改实例名称。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIp6Translator"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIp6TranslatorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpv6AddressesAttribute(
            self,
            request: models.ModifyIpv6AddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyIpv6AddressesAttributeResponse:
        """
        本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡内网IPv6地址属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpv6AddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpv6AddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLocalGateway(
            self,
            request: models.ModifyLocalGatewayRequest,
            opts: Dict = None,
    ) -> models.ModifyLocalGatewayResponse:
        """
        本接口（ModifyLocalGateway）用于修改CDC的本地网关。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLocalGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLocalGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatGatewayAttribute(
            self,
            request: models.ModifyNatGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNatGatewayAttributeResponse:
        """
        本接口（ModifyNatGatewayAttribute）用于修改NAT网关的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        本接口（ModifyNatGatewayDestinationIpPortTranslationNatRule）用于修改NAT网关端口转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNatGatewaySourceIpTranslationNatRule(
            self,
            request: models.ModifyNatGatewaySourceIpTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyNatGatewaySourceIpTranslationNatRuleResponse:
        """
        本接口（ModifyNatGatewaySourceIpTranslationNatRule）用于修改NAT网关SNAT转发规则。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNatGatewaySourceIpTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNatGatewaySourceIpTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetDetect(
            self,
            request: models.ModifyNetDetectRequest,
            opts: Dict = None,
    ) -> models.ModifyNetDetectResponse:
        """
        本接口(ModifyNetDetect)用于修改网络探测参数。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetDetect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetDetectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAclAttribute(
            self,
            request: models.ModifyNetworkAclAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAclAttributeResponse:
        """
        本接口（ModifyNetworkAclAttribute）用于修改网络ACL属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAclAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAclAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAclEntries(
            self,
            request: models.ModifyNetworkAclEntriesRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAclEntriesResponse:
        """
        本接口（ModifyNetworkAclEntries）用于修改（包括添加和删除）网络ACL的入站规则和出站规则。在NetworkAclEntrySet参数中：
        * 若同时传入入站规则和出站规则，则重置原有的入站规则和出站规则，并分别导入传入的规则。
        * 若仅传入入站规则，则仅重置原有的入站规则，并导入传入的规则，不影响原有的出站规则（若仅传入出站规则，处理方式类似入站方向）。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAclEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAclEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkAclQuintupleEntries(
            self,
            request: models.ModifyNetworkAclQuintupleEntriesRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkAclQuintupleEntriesResponse:
        """
        本接口（ModifyNetworkAclQuintupleEntries）用于修改网络ACL五元组的入站规则和出站规则。在NetworkAclQuintupleEntrySet参数中：NetworkAclQuintupleEntry需要提供NetworkAclQuintupleEntryId。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkAclQuintupleEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkAclQuintupleEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkInterfaceAttribute(
            self,
            request: models.ModifyNetworkInterfaceAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkInterfaceAttributeResponse:
        """
        本接口（ModifyNetworkInterfaceAttribute）用于修改弹性网卡属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkInterfaceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkInterfaceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyNetworkInterfaceQos(
            self,
            request: models.ModifyNetworkInterfaceQosRequest,
            opts: Dict = None,
    ) -> models.ModifyNetworkInterfaceQosResponse:
        """
        本接口（ModifyNetworkInterfaceQos）用于修改弹性网卡服务质量。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyNetworkInterfaceQos"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyNetworkInterfaceQosResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateIpAddressesAttribute(
            self,
            request: models.ModifyPrivateIpAddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateIpAddressesAttributeResponse:
        """
        本接口（ModifyPrivateIpAddressesAttribute）用于修改弹性网卡内网IP属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateIpAddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateIpAddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateNatGatewayAttribute(
            self,
            request: models.ModifyPrivateNatGatewayAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateNatGatewayAttributeResponse:
        """
        本接口（ModifyPrivateNatGatewayAttribute）用于修改私网NAT网关属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateNatGatewayAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateNatGatewayAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule(
            self,
            request: models.ModifyPrivateNatGatewayDestinationIpPortTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateNatGatewayDestinationIpPortTranslationNatRuleResponse:
        """
        本接口（ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule）用于修改私网NAT网关目的端口转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateNatGatewayDestinationIpPortTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateNatGatewayTranslationAclRule(
            self,
            request: models.ModifyPrivateNatGatewayTranslationAclRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateNatGatewayTranslationAclRuleResponse:
        """
        本接口（ModifyPrivateNatGatewayTranslationAclRule）用于修改私网NAT网关源端转换访问控制规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateNatGatewayTranslationAclRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateNatGatewayTranslationAclRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateNatGatewayTranslationNatRule(
            self,
            request: models.ModifyPrivateNatGatewayTranslationNatRuleRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateNatGatewayTranslationNatRuleResponse:
        """
        本接口（ModifyPrivateNatGatewayTranslationNatRule）用于修改私网NAT网关源端转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateNatGatewayTranslationNatRule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateNatGatewayTranslationNatRuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyReserveIpAddress(
            self,
            request: models.ModifyReserveIpAddressRequest,
            opts: Dict = None,
    ) -> models.ModifyReserveIpAddressResponse:
        """
        修改内网保留 IP
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyReserveIpAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyReserveIpAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRoutePolicyAttribute(
            self,
            request: models.ModifyRoutePolicyAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRoutePolicyAttributeResponse:
        """
        本接口（ModifyRoutePolicyAttribute）用于修改路由接收策略属性属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRoutePolicyAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRoutePolicyAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRouteTableAttribute(
            self,
            request: models.ModifyRouteTableAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRouteTableAttributeResponse:
        """
        本接口（ModifyRouteTableAttribute）用于修改路由表（RouteTable）属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRouteTableAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRouteTableAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRouteTableSelectionPolicies(
            self,
            request: models.ModifyRouteTableSelectionPoliciesRequest,
            opts: Dict = None,
    ) -> models.ModifyRouteTableSelectionPoliciesResponse:
        """
        该接口用于编辑云联网路由表选择策略
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRouteTableSelectionPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRouteTableSelectionPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupAttribute(
            self,
            request: models.ModifySecurityGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupAttributeResponse:
        """
        本接口（ModifySecurityGroupAttribute）用于修改安全组（SecurityGroupPolicy）属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupPolicies(
            self,
            request: models.ModifySecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupPoliciesResponse:
        """
        本接口（ModifySecurityGroupPolicies）用于重置安全组出站和入站规则（SecurityGroupPolicy）。

        <ul>
        <li>该接口不支持自定义索引 PolicyIndex。</li>
        <li>在 SecurityGroupPolicySet 参数中：<ul>
        	<li> 如果指定 SecurityGroupPolicySet.Version 为0, 表示清空所有规则，并忽略 Egress 和 Ingress。</li>
        	<li> 如果指定 SecurityGroupPolicySet.Version 不为0, 在添加出站和入站规则（Egress 和 Ingress）时：<ul>
        		<li>Protocol 字段支持输入 TCP, UDP, ICMP, ICMPV6, GRE, ALL。</li>
        		<li>CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        		<li>Ipv6CidrBlock 字段允许输入符合 IPv6 cidr 格式标准的任意字符串。在基础网络中，如果Ipv6CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        		<li>SecurityGroupId 字段允许输入与待修改的安全组位于相同项目中的安全组 ID，包括这个安全组 ID 本身，代表安全组下所有云服务器的内网 IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个ID所关联的云服务器变化而变化，不需要重新修改。</li>
        		<li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受。</li>
        		<li>Action 字段只允许输入 ACCEPT 或 DROP。</li>
        		<li>CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate 四者是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。</li>
        </ul></li></ul></li>
        </ul>
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceTemplateAttribute(
            self,
            request: models.ModifyServiceTemplateAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceTemplateAttributeResponse:
        """
        本接口（ModifyServiceTemplateAttribute）用于修改协议端口模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceTemplateAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceTemplateAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyServiceTemplateGroupAttribute(
            self,
            request: models.ModifyServiceTemplateGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyServiceTemplateGroupAttributeResponse:
        """
        本接口（ModifyServiceTemplateGroupAttribute）用于修改协议端口模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyServiceTemplateGroupAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyServiceTemplateGroupAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySnapshotPolicies(
            self,
            request: models.ModifySnapshotPoliciesRequest,
            opts: Dict = None,
    ) -> models.ModifySnapshotPoliciesResponse:
        """
        本接口（ModifySnapshotPolicies）用于修改快照策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySnapshotPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySnapshotPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySubnetAttribute(
            self,
            request: models.ModifySubnetAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySubnetAttributeResponse:
        """
        本接口（ModifySubnetAttribute）用于修改子网属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySubnetAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySubnetAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTemplateMember(
            self,
            request: models.ModifyTemplateMemberRequest,
            opts: Dict = None,
    ) -> models.ModifyTemplateMemberResponse:
        """
        修改模板对象中的IP地址、协议端口、IP地址组、协议端口组。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTemplateMember"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTemplateMemberResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTrafficMirrorAttribute(
            self,
            request: models.ModifyTrafficMirrorAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyTrafficMirrorAttributeResponse:
        """
        本接口（ModifyTrafficMirrorAttribute）用于修改流量镜像实例属性。
        注意：只支持修改名字和描述信息
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTrafficMirrorAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTrafficMirrorAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAttribute(
            self,
            request: models.ModifyVpcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAttributeResponse:
        """
        本接口（ModifyVpcAttribute）用于修改私有网络（VPC）的相关属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcEndPointAttribute(
            self,
            request: models.ModifyVpcEndPointAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcEndPointAttributeResponse:
        """
        本接口（ModifyVpcEndPointAttribute）用于修改终端节点属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcEndPointAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcEndPointAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcEndPointServiceAttribute(
            self,
            request: models.ModifyVpcEndPointServiceAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcEndPointServiceAttributeResponse:
        """
        本接口（ModifyVpcEndPointServiceAttribute）用于修改终端节点服务属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcEndPointServiceAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcEndPointServiceAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcEndPointServiceWhiteList(
            self,
            request: models.ModifyVpcEndPointServiceWhiteListRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcEndPointServiceWhiteListResponse:
        """
        本接口（ModifyVpcEndPointServiceWhiteList）用于修改终端节点服务白名单属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcEndPointServiceWhiteList"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcEndPointServiceWhiteListResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcPeeringConnection(
            self,
            request: models.ModifyVpcPeeringConnectionRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcPeeringConnectionResponse:
        """
        本接口（ModifyVpcPeeringConnection）用于修改私有网络对等连接属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcPeeringConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcPeeringConnectionResponse
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
        
    async def ModifyVpnGatewayCcnRoutes(
            self,
            request: models.ModifyVpnGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewayCcnRoutesResponse:
        """
        本接口（ModifyVpnGatewayCcnRoutes）用于修改VPN网关云联网路由。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewayRoutes(
            self,
            request: models.ModifyVpnGatewayRoutesRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewayRoutesResponse:
        """
        本接口（ModifyVpnGatewayRoutes）用于修改VPN路由是否启用。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewayRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewayRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewaySslClientCert(
            self,
            request: models.ModifyVpnGatewaySslClientCertRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewaySslClientCertResponse:
        """
        更新SslVpnClient证书
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewaySslClientCert"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewaySslClientCertResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpnGatewaySslServer(
            self,
            request: models.ModifyVpnGatewaySslServerRequest,
            opts: Dict = None,
    ) -> models.ModifyVpnGatewaySslServerResponse:
        """
        本接口用于修改 SSL-VPN 服务端属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpnGatewaySslServer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpnGatewaySslServerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def NotifyRoutes(
            self,
            request: models.NotifyRoutesRequest,
            opts: Dict = None,
    ) -> models.NotifyRoutesResponse:
        """
        本接口（NotifyRoutes）用于路由表列表页操作增加“发布到云联网”，发布路由到云联网。
        """
        
        kwargs = {}
        kwargs["action"] = "NotifyRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.NotifyRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RefreshDirectConnectGatewayRouteToNatGateway(
            self,
            request: models.RefreshDirectConnectGatewayRouteToNatGatewayRequest,
            opts: Dict = None,
    ) -> models.RefreshDirectConnectGatewayRouteToNatGatewayResponse:
        """
        刷新专线直连nat路由，更新nat到专线的路由表
        """
        
        kwargs = {}
        kwargs["action"] = "RefreshDirectConnectGatewayRouteToNatGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RefreshDirectConnectGatewayRouteToNatGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectAttachCcnInstances(
            self,
            request: models.RejectAttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.RejectAttachCcnInstancesResponse:
        """
        本接口（RejectAttachCcnInstances）用于跨账号关联实例时，云联网所有者拒绝关联操作。
        """
        
        kwargs = {}
        kwargs["action"] = "RejectAttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectAttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RejectVpcPeeringConnection(
            self,
            request: models.RejectVpcPeeringConnectionRequest,
            opts: Dict = None,
    ) -> models.RejectVpcPeeringConnectionResponse:
        """
        本接口（RejectVpcPeeringConnection）用于驳回对等连接请求。
        """
        
        kwargs = {}
        kwargs["action"] = "RejectVpcPeeringConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RejectVpcPeeringConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseAddresses(
            self,
            request: models.ReleaseAddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseAddressesResponse:
        """
        本接口 (ReleaseAddresses) 用于释放一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。
        * 只有状态为 UNBIND 的 EIP 才能进行释放操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIPv6Addresses(
            self,
            request: models.ReleaseIPv6AddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseIPv6AddressesResponse:
        """
        本接口（ReleaseIPv6Addresses）用于释放一个或多个弹性公网IPv6（简称EIPv6）实例。

        - 支持对已申请到的弹性公网 IPv6 实例进行释放操作，如需再次使用，请重新申请。
        - 只有状态为 UNBIND 的 EIPv6 实例才能进行释放操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIPv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIPv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIp6AddressesBandwidth(
            self,
            request: models.ReleaseIp6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ReleaseIp6AddressesBandwidthResponse:
        """
        本接口（ReleaseIp6AddressesBandwidth）用于为传统弹性公网 IPv6 实例关闭 IPv6 公网带宽。

        - 传统弹性公网 IPv6 实例关闭公网带宽后，仍具备 IPv6 内网通信能力。
        - 如需再次开通 IPv6 公网带宽，请使用 [AllocateIp6AddressesBandwidth](https://cloud.tencent.com/document/product/215/40090) 接口进行开通。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIp6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIp6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveBandwidthPackageResources(
            self,
            request: models.RemoveBandwidthPackageResourcesRequest,
            opts: Dict = None,
    ) -> models.RemoveBandwidthPackageResourcesResponse:
        """
        接口用于删除带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveBandwidthPackageResources"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveBandwidthPackageResourcesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemoveIp6Rules(
            self,
            request: models.RemoveIp6RulesRequest,
            opts: Dict = None,
    ) -> models.RemoveIp6RulesResponse:
        """
        1. 该接口用于删除IPV6转换规则
        2. 支持批量删除同一个转换实例下的多个转换规则
        """
        
        kwargs = {}
        kwargs["action"] = "RemoveIp6Rules"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemoveIp6RulesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewAddresses(
            self,
            request: models.RenewAddressesRequest,
            opts: Dict = None,
    ) -> models.RenewAddressesResponse:
        """
        本接口（RenewAddresses）用于续费包月带宽计费模式的弹性公网IP。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RenewVpnGateway(
            self,
            request: models.RenewVpnGatewayRequest,
            opts: Dict = None,
    ) -> models.RenewVpnGatewayResponse:
        """
        本接口（RenewVpnGateway）用于预付费（包年包月）VPN网关续费。目前只支持IPSEC网关。
        """
        
        kwargs = {}
        kwargs["action"] = "RenewVpnGateway"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RenewVpnGatewayResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceCcnRouteTableBroadcastPolicys(
            self,
            request: models.ReplaceCcnRouteTableBroadcastPolicysRequest,
            opts: Dict = None,
    ) -> models.ReplaceCcnRouteTableBroadcastPolicysResponse:
        """
        本接口(ReplaceCcnRouteTableBroadcastPolicys)用于替换云联网路由表路由传播策略。
        > 特别注意：是全量覆盖，非增量添加

        **路由条件支持以下四种：**

        - 实例类型: `instance-type`，可选值：私有网络 `VPC`、专线网关 `DIRECTCONNECT`、VPN网关 `VPNGW`
        - 实例ID: `instance-id`，例如：`dcg-8zljkrft`、`vpc-jdevjrup`，暂不支持 `Edge` 实例
        - 实例地域: `instance-region`，例如：`ap-guangzhou`<br />产品支持的所有地域列表可通过接口 [DescribeRegions](https://cloud.tencent.com/document/product/1596/77930) 查询，其中参数 `Product` 设置为 `ccn`
        - 路由前缀: `cidr-block`，例如：`10.1.0.0/16`


        **传播条件支持以下三种：**

        - 实例类型: `instance-type`，格式同路由条件
        - 实例ID: `instance-id`，格式同路由条件
        - 实例地域: `instance-region`，格式同路由条件


        **使用限制：**
        - 一条策略内的单个条件类型，最大支持设置 `25` 个条件值
        - 一张路由表，最大支持 `100` 条路由传播策略
        - 路由条件类型中，只有 `cidr-block` 类型支持模糊匹配和精确匹配两种，其它类型只支持精确匹配一种模式
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceCcnRouteTableBroadcastPolicys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceCcnRouteTableBroadcastPolicysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceCcnRouteTableInputPolicys(
            self,
            request: models.ReplaceCcnRouteTableInputPolicysRequest,
            opts: Dict = None,
    ) -> models.ReplaceCcnRouteTableInputPolicysResponse:
        """
        本接口(ReplaceRouteTableInputPolicys)用于替换云联网路由表路由接收策略。
        > 特别注意：是全量覆盖，非增量添加

        **路由条件支持以下四种：**

        - 实例类型: `instance-type`，可选值：私有网络 `VPC`、专线网关 `DIRECTCONNECT`、VPN网关 `VPNGW`
        - 实例ID: `instance-id`，例如：`dcg-8zljkrft`、`vpc-jdevjrup`，暂不支持 `Edge` 实例
        - 实例地域: `instance-region`，例如：`ap-guangzhou`<br />产品支持的所有地域列表可通过接口 [DescribeRegions](https://cloud.tencent.com/document/product/1596/77930) 查询，其中参数 `Product` 设置为 `ccn`
        - 路由前缀: `cidr-block`，例如：`10.1.0.0/16`


        **使用限制：**
        - 一条策略内的单个条件类型，最大支持设置 `25` 个条件值
        - 一张路由表，最大支持 `100` 条路由接收策略
        - 路由条件类型中，只有 `cidr-block` 类型支持模糊匹配和精确匹配两种，其它类型只支持精确匹配一种模式
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceCcnRouteTableInputPolicys"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceCcnRouteTableInputPolicysResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceDirectConnectGatewayCcnRoutes(
            self,
            request: models.ReplaceDirectConnectGatewayCcnRoutesRequest,
            opts: Dict = None,
    ) -> models.ReplaceDirectConnectGatewayCcnRoutesResponse:
        """
        本接口（ReplaceDirectConnectGatewayCcnRoutes）根据路由ID（RouteId）修改指定的路由（Route），支持批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceDirectConnectGatewayCcnRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceDirectConnectGatewayCcnRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceHighPriorityRouteTableAssociation(
            self,
            request: models.ReplaceHighPriorityRouteTableAssociationRequest,
            opts: Dict = None,
    ) -> models.ReplaceHighPriorityRouteTableAssociationResponse:
        """
        替换高优路由表和子网绑定关系。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceHighPriorityRouteTableAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceHighPriorityRouteTableAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceHighPriorityRoutes(
            self,
            request: models.ReplaceHighPriorityRoutesRequest,
            opts: Dict = None,
    ) -> models.ReplaceHighPriorityRoutesResponse:
        """
        替换高优路由表条目信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceHighPriorityRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceHighPriorityRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRoutePolicyAssociations(
            self,
            request: models.ReplaceRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.ReplaceRoutePolicyAssociationsResponse:
        """
        本接口（ReplaceRoutePolicyAssociations）根据路由接收策略实例ID（RoutePolicyId）和路由表实例ID（RouteTableId）修改绑定优先级（Priority），支持批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRoutePolicyEntries(
            self,
            request: models.ReplaceRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.ReplaceRoutePolicyEntriesResponse:
        """
        本接口（ReplaceRoutePolicyEntries）根据路由接收策略规则ID（RoutePolicyEntryId）修改指定的路由策略条目（RoutePolicyEntry），支持批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRouteTableAssociation(
            self,
            request: models.ReplaceRouteTableAssociationRequest,
            opts: Dict = None,
    ) -> models.ReplaceRouteTableAssociationResponse:
        """
        本接口（ReplaceRouteTableAssociation）用于修改子网（Subnet）关联的路由表（RouteTable）。
        * 一个子网只能关联一个路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRouteTableAssociation"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRouteTableAssociationResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRoutes(
            self,
            request: models.ReplaceRoutesRequest,
            opts: Dict = None,
    ) -> models.ReplaceRoutesResponse:
        """
        本接口（ReplaceRoutes）根据路由策略ID（RouteId）修改指定的路由策略（Route），支持批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceSecurityGroupPolicies(
            self,
            request: models.ReplaceSecurityGroupPoliciesRequest,
            opts: Dict = None,
    ) -> models.ReplaceSecurityGroupPoliciesResponse:
        """
        本接口（ReplaceSecurityGroupPolicies）用于批量修改安全组规则（SecurityGroupPolicy）。
        单个请求中只能替换单个方向的一条或多条规则, 必须要指定索引（PolicyIndex）。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceSecurityGroupPolicy(
            self,
            request: models.ReplaceSecurityGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.ReplaceSecurityGroupPolicyResponse:
        """
        本接口（ReplaceSecurityGroupPolicy）用于替换单条安全组规则（SecurityGroupPolicy）。
        单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceSecurityGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceSecurityGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetAttachCcnInstances(
            self,
            request: models.ResetAttachCcnInstancesRequest,
            opts: Dict = None,
    ) -> models.ResetAttachCcnInstancesResponse:
        """
        本接口（ResetAttachCcnInstances）用于跨账号关联实例申请过期时，重新申请关联操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetAttachCcnInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetAttachCcnInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetHighPriorityRoutes(
            self,
            request: models.ResetHighPriorityRoutesRequest,
            opts: Dict = None,
    ) -> models.ResetHighPriorityRoutesResponse:
        """
        重置高优路由表。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetHighPriorityRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetHighPriorityRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetNatGatewayConnection(
            self,
            request: models.ResetNatGatewayConnectionRequest,
            opts: Dict = None,
    ) -> models.ResetNatGatewayConnectionResponse:
        """
        本接口（ResetNatGatewayConnection）用于调整传统型NAT网关并发连接数上限。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetNatGatewayConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetNatGatewayConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutePolicyAssociations(
            self,
            request: models.ResetRoutePolicyAssociationsRequest,
            opts: Dict = None,
    ) -> models.ResetRoutePolicyAssociationsResponse:
        """
        本接口（ResetRoutePolicyAssociations）用于对某个路由表实例已经绑定的路由策略实例解除绑定关系，并重新设置新的绑定路由策略及优先级。<br />
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutePolicyAssociations"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutePolicyAssociationsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutePolicyEntries(
            self,
            request: models.ResetRoutePolicyEntriesRequest,
            opts: Dict = None,
    ) -> models.ResetRoutePolicyEntriesResponse:
        """
        本接口（ResetRoutePolicyEntries）根据路由接收策略规则ID（RoutePolicyId）重置指定的路由接收策略条目（RoutePolicyEntry），支持批量修改。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutePolicyEntries"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutePolicyEntriesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutes(
            self,
            request: models.ResetRoutesRequest,
            opts: Dict = None,
    ) -> models.ResetRoutesResponse:
        """
        本接口（ResetRoutes）用于对某个路由表名称和所有路由策略（Route）进行重新设置。<br /> 注意: 调用本接口时先删除当前路由表中所有路由策略, 再保存新提交的路由策略内容, 会引起网络中断。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetTrafficMirrorFilter(
            self,
            request: models.ResetTrafficMirrorFilterRequest,
            opts: Dict = None,
    ) -> models.ResetTrafficMirrorFilterResponse:
        """
        本接口（ResetTrafficMirrorFilter）用于更新流量镜像实例过滤规则。
        注意：每一个流量镜像实例，不能同时支持按nat网关和五元组两种规则过滤
        """
        
        kwargs = {}
        kwargs["action"] = "ResetTrafficMirrorFilter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetTrafficMirrorFilterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetTrafficMirrorSrcs(
            self,
            request: models.ResetTrafficMirrorSrcsRequest,
            opts: Dict = None,
    ) -> models.ResetTrafficMirrorSrcsResponse:
        """
        本接口（ResetTrafficMirrorSrcs）用于重置流量镜像实例采集对象。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetTrafficMirrorSrcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetTrafficMirrorSrcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetTrafficMirrorTarget(
            self,
            request: models.ResetTrafficMirrorTargetRequest,
            opts: Dict = None,
    ) -> models.ResetTrafficMirrorTargetResponse:
        """
        本接口（ResetTrafficMirrorTarget）用于更新流量镜像实例的接收目的信息。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetTrafficMirrorTarget"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetTrafficMirrorTargetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetVpnConnection(
            self,
            request: models.ResetVpnConnectionRequest,
            opts: Dict = None,
    ) -> models.ResetVpnConnectionResponse:
        """
        本接口（ResetVpnConnection）用于重置VPN通道。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetVpnConnection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetVpnConnectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetVpnGatewayInternetMaxBandwidth(
            self,
            request: models.ResetVpnGatewayInternetMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.ResetVpnGatewayInternetMaxBandwidthResponse:
        """
        本接口（ResetVpnGatewayInternetMaxBandwidth）用于调整VPN网关带宽上限。VPN网关带宽目前仅支持部分带宽范围内升降配，如【5,100】Mbps和【200,1000】Mbps，在各自带宽范围内可提升配额，跨范围提升配额和降配暂不支持，如果是包年包月VPN网关需要在有效期内。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetVpnGatewayInternetMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetVpnGatewayInternetMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResumeSnapshotInstance(
            self,
            request: models.ResumeSnapshotInstanceRequest,
            opts: Dict = None,
    ) -> models.ResumeSnapshotInstanceResponse:
        """
        本接口（ResumeSnapshotInstance）用于根据备份内容恢复安全组策略。
        """
        
        kwargs = {}
        kwargs["action"] = "ResumeSnapshotInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResumeSnapshotInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReturnNormalAddresses(
            self,
            request: models.ReturnNormalAddressesRequest,
            opts: Dict = None,
    ) -> models.ReturnNormalAddressesResponse:
        """
        本接口（ReturnNormalAddresses）用于解绑并释放普通公网IP。
        为完善公网IP的访问管理功能，此接口于2022年12月15日升级优化鉴权功能，升级后子用户调用此接口需向主账号申请CAM策略授权，否则可能调用失败。您可以提前为子账号配置操作授权，详情见[授权指南](https://cloud.tencent.com/document/product/598/34545)。
        """
        
        kwargs = {}
        kwargs["action"] = "ReturnNormalAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReturnNormalAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetCcnRegionBandwidthLimits(
            self,
            request: models.SetCcnRegionBandwidthLimitsRequest,
            opts: Dict = None,
    ) -> models.SetCcnRegionBandwidthLimitsResponse:
        """
        本接口（SetCcnRegionBandwidthLimits）用于设置云联网（CCN）各地域出带宽上限，或者地域间带宽上限。
        """
        
        kwargs = {}
        kwargs["action"] = "SetCcnRegionBandwidthLimits"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetCcnRegionBandwidthLimitsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetVpnGatewaysRenewFlag(
            self,
            request: models.SetVpnGatewaysRenewFlagRequest,
            opts: Dict = None,
    ) -> models.SetVpnGatewaysRenewFlagResponse:
        """
        本接口（SetVpnGatewaysRenewFlag）用于设置VPNGW续费标记。
        """
        
        kwargs = {}
        kwargs["action"] = "SetVpnGatewaysRenewFlag"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetVpnGatewaysRenewFlagResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartTrafficMirror(
            self,
            request: models.StartTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.StartTrafficMirrorResponse:
        """
        本接口（StartTrafficMirror）用于开启流量镜像实例。
        """
        
        kwargs = {}
        kwargs["action"] = "StartTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopTrafficMirror(
            self,
            request: models.StopTrafficMirrorRequest,
            opts: Dict = None,
    ) -> models.StopTrafficMirrorResponse:
        """
        本接口（StopTrafficMirror）用于关闭流量镜像实例。
        """
        
        kwargs = {}
        kwargs["action"] = "StopTrafficMirror"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopTrafficMirrorResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TransformAddress(
            self,
            request: models.TransformAddressRequest,
            opts: Dict = None,
    ) -> models.TransformAddressResponse:
        """
        本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 平台对用户单地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](/document/product/213/1941)）。上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/product/215/16701) 接口获取。
        """
        
        kwargs = {}
        kwargs["action"] = "TransformAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TransformAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6Addresses(
            self,
            request: models.UnassignIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6AddressesResponse:
        """
        本接口（UnassignIpv6Addresses）用于释放弹性网卡`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)接口。
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6CidrBlock(
            self,
            request: models.UnassignIpv6CidrBlockRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6CidrBlockResponse:
        """
        本接口（UnassignIpv6CidrBlock）用于释放IPv6网段。<br />
        网段如果还有IP占用且未回收，则网段无法释放。
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6CidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6CidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6SubnetCidrBlock(
            self,
            request: models.UnassignIpv6SubnetCidrBlockRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6SubnetCidrBlockResponse:
        """
        本接口（UnassignIpv6SubnetCidrBlock）用于释放IPv6子网段。<br />
        子网段如果还有IP占用且未回收，则子网段无法释放。
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6SubnetCidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6SubnetCidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignPrivateIpAddresses(
            self,
            request: models.UnassignPrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.UnassignPrivateIpAddressesResponse:
        """
        本接口（UnassignPrivateIpAddresses）用于弹性网卡退还内网 IP。
        * 退还弹性网卡上的辅助内网IP，接口自动解除关联弹性公网 IP。不能退还弹性网卡的主内网IP。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignPrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignPrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlockCcnBandwidths(
            self,
            request: models.UnlockCcnBandwidthsRequest,
            opts: Dict = None,
    ) -> models.UnlockCcnBandwidthsResponse:
        """
        本接口（UnlockCcnBandwidths）用户解锁云联网限速实例。
        该接口一般用来封禁地域间限速的云联网实例下的限速实例, 目前联通内部运营系统通过云API调用, 如果是出口限速, 一般使用更粗的云联网实例粒度封禁（SecurityUnlockCcns）。
        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统。
        """
        
        kwargs = {}
        kwargs["action"] = "UnlockCcnBandwidths"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlockCcnBandwidthsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnlockCcns(
            self,
            request: models.UnlockCcnsRequest,
            opts: Dict = None,
    ) -> models.UnlockCcnsResponse:
        """
        本接口（UnlockCcns）用于解锁云联网实例

        该接口一般用来解封禁出口限速的云联网实例, 目前联通内部运营系统通过云API调用, 因为出口限速无法按地域间解封禁, 只能按更粗的云联网实例粒度解封禁, 如果是地域间限速, 一般可以通过更细的限速实例粒度解封禁（UnlockCcnBandwidths）

        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统
        """
        
        kwargs = {}
        kwargs["action"] = "UnlockCcns"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnlockCcnsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTrafficMirrorAllFilter(
            self,
            request: models.UpdateTrafficMirrorAllFilterRequest,
            opts: Dict = None,
    ) -> models.UpdateTrafficMirrorAllFilterResponse:
        """
        本接口（UpdateTrafficMirrorAllFilter）用于更新流量镜像实例的过滤规则或者采集对象。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTrafficMirrorAllFilter"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTrafficMirrorAllFilterResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UpdateTrafficMirrorDirection(
            self,
            request: models.UpdateTrafficMirrorDirectionRequest,
            opts: Dict = None,
    ) -> models.UpdateTrafficMirrorDirectionResponse:
        """
        本接口（UpdateTrafficMirrorDirection）用于更新流量镜像实例的采集方向。
        """
        
        kwargs = {}
        kwargs["action"] = "UpdateTrafficMirrorDirection"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UpdateTrafficMirrorDirectionResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def WithdrawNotifyRoutes(
            self,
            request: models.WithdrawNotifyRoutesRequest,
            opts: Dict = None,
    ) -> models.WithdrawNotifyRoutesResponse:
        """
        本接口（WithdrawNotifyRoutes）用于撤销已发布到云联网的路由。路由表列表页操作增加“从云联网撤销”。
        """
        
        kwargs = {}
        kwargs["action"] = "WithdrawNotifyRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.WithdrawNotifyRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)