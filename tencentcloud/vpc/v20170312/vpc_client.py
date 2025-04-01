# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
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

import json

from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.common.abstract_client import AbstractClient
from tencentcloud.vpc.v20170312 import models


class VpcClient(AbstractClient):
    _apiVersion = '2017-03-12'
    _endpoint = 'vpc.tencentcloudapi.com'
    _service = 'vpc'


    def AcceptAttachCcnInstances(self, request):
        """本接口（AcceptAttachCcnInstances）用于跨账号关联实例时，云联网所有者接受并同意关联操作。

        :param request: Request instance for AcceptAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AcceptAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptAttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptAttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AcceptVpcPeeringConnection(self, request):
        """本接口（AcceptVpcPeeringConnection）用于接受对等连接请求。

        :param request: Request instance for AcceptVpcPeeringConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AcceptVpcPeeringConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AcceptVpcPeeringConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AcceptVpcPeeringConnection", params, headers=headers)
            response = json.loads(body)
            model = models.AcceptVpcPeeringConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddBandwidthPackageResources(self, request):
        """接口用于添加带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等

        :param request: Request instance for AddBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddBandwidthPackageResources", params, headers=headers)
            response = json.loads(body)
            model = models.AddBandwidthPackageResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddIp6Rules(self, request):
        """1. 该接口用于在转换实例下添加IPV6转换规则。
        2. 支持在同一个转换实例下批量添加转换规则，一个账户在一个地域最多50个。
        3. 一个完整的转换规则包括vip6:vport6:protocol:vip:vport，其中vip6:vport6:protocol必须是唯一。

        :param request: Request instance for AddIp6Rules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddIp6RulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddIp6RulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddIp6Rules", params, headers=headers)
            response = json.loads(body)
            model = models.AddIp6RulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AddTemplateMember(self, request):
        """增加模板对象中的IP地址、协议端口、IP地址组、协议端口组。

        :param request: Request instance for AddTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AddTemplateMember", params, headers=headers)
            response = json.loads(body)
            model = models.AddTemplateMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AdjustPublicAddress(self, request):
        """本接口 (AdjustPublicAddress) 用于更换IP地址，支持更换CVM实例的普通公网IP和包月带宽的EIP。

        :param request: Request instance for AdjustPublicAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AdjustPublicAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AdjustPublicAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AdjustPublicAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AdjustPublicAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateAddresses(self, request):
        """本接口 (AllocateAddresses) 用于申请一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * EIP 是专为动态云计算设计的静态 IP 地址。借助 EIP，您可以快速将 EIP 重新映射到您的另一个实例上，从而屏蔽实例故障。
        * 您的 EIP 与腾讯云账户相关联，而不是与某个实例相关联。在您选择显式释放该地址，或欠费超过24小时之前，它会一直与您的腾讯云账户保持关联。
        * 一个腾讯云账户在每个地域能申请的 EIP 最大配额有所限制，可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)，上述配额可通过 DescribeAddressQuota 接口获取。

        :param request: Request instance for AllocateAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateIPv6Addresses(self, request):
        """本接口（AllocateIPv6Addresses）用于申请一个或多个弹性公网IPv6（简称EIPv6）实例。

        - EIPv6 是您在腾讯云某个地域可以独立申请和持有的，固定不变的公网 IPv6 地址，提供与弹性公网 IPv4 一致的产品体验。
        - 通过弹性公网 IPv6，您可以快速将 EIPv6 实例绑定到云资源的内网 IPv6 地址上，实现为云资源快速开通 IPv6 公网带宽。
        - 您还可以按需将 EIPv6 实例绑定到其他云资源上，从而屏蔽实例故障。

        :param request: Request instance for AllocateIPv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateIPv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateIPv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateIPv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateIPv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AllocateIp6AddressesBandwidth(self, request):
        """本接口（AllocateIp6AddressesBandwidth）用于为传统弹性公网 IPv6 地址开通 IPv6 公网带宽。

        - 传统弹性公网 IPv6 地址默认仅具备内网通信能力，需通过控制台或 API 接口为其分配公网带宽后，才能具备 IPv6 公网通信能力、并于传统弹性公网 IPv6 列表页可见。
        - 支持为一个或多个传统弹性公网 IPv6 实例开通公网带宽。

        :param request: Request instance for AllocateIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AllocateIp6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.AllocateIp6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignIpv6Addresses(self, request):
        """本接口（AssignIpv6Addresses）用于弹性网卡申请`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)接口。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 可以指定`IPv6`地址申请，地址类型不能为主`IP`，`IPv6`地址暂时只支持作为辅助`IP`。
        * 地址必须要在弹性网卡所在子网内，而且不能被占用。
        * 在弹性网卡上申请一个到多个辅助`IPv6`地址，接口会在弹性网卡所在子网段内返回指定数量的辅助`IPv6`地址。

        :param request: Request instance for AssignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignIpv6CidrBlock(self, request):
        """本接口（AssignIpv6CidrBlock）用于分配IPv6网段。
        * 使用本接口前，您需要已有VPC实例，如果没有可通过接口<a href="https://cloud.tencent.com/document/api/215/15774" title="CreateVpc" target="_blank">CreateVpc</a>创建。
        * 每个VPC只能申请一个IPv6网段。

        :param request: Request instance for AssignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6CidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6CidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignIpv6SubnetCidrBlock(self, request):
        """本接口（AssignIpv6SubnetCidrBlock）用于分配IPv6子网段。
        * 给子网分配 `IPv6` 网段，要求子网所属 `VPC` 已获得 `IPv6` 网段。如果尚未分配，请先通过接口 `AssignIpv6CidrBlock` 给子网所属 `VPC` 分配一个 `IPv6` 网段。否则无法分配 `IPv6` 子网段。
        * 每个子网只能分配一个IPv6网段。

        :param request: Request instance for AssignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignIpv6SubnetCidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.AssignIpv6SubnetCidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssignPrivateIpAddresses(self, request):
        """本接口（AssignPrivateIpAddresses）用于弹性网卡申请内网 IP。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 可以指定内网IP地址申请，内网IP地址类型不能为主IP，主IP已存在，不能修改，内网IP必须要在弹性网卡所在子网内，而且不能被占用。
        * 在弹性网卡上申请一个到多个辅助内网IP，接口会在弹性网卡所在子网网段内返回指定数量的辅助内网IP。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssignPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.AssignPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateAddress(self, request):
        """本接口 (AssociateAddress) 用于将[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        * 将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        * 将 EIP 绑定到主网卡的主内网IP时，如主内网IP已绑定普通公网IP，必须先退还才能绑定EIP。
        * 将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。
        * 将 EIP 绑定到内网型CLB实例的功能处于内测阶段，如需使用，请提交[内测申请](https://cloud.tencent.com/apply/p/4kxj7picqci)。
        * 将 EIP 绑定到NAT网关，请使用接口[AssociateNatGatewayAddress](https://cloud.tencent.com/document/product/215/36722)
        * EIP 如果欠费或被封堵，则不能被绑定。
        * 只有状态为 UNBIND 的 EIP 才能够被绑定。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateDhcpIpWithAddressIp(self, request):
        """本接口（AssociateDhcpIpWithAddressIp）用于DhcpIp绑定弹性公网IP（EIP）。<br />
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for AssociateDhcpIpWithAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateDhcpIpWithAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateDhcpIpWithAddressIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDhcpIpWithAddressIp", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateDhcpIpWithAddressIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateDirectConnectGatewayNatGateway(self, request):
        """将专线网关与NAT网关绑定，专线网关默认路由指向NAT网关

        :param request: Request instance for AssociateDirectConnectGatewayNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateDirectConnectGatewayNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateDirectConnectGatewayNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateDirectConnectGatewayNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateDirectConnectGatewayNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateIPv6Address(self, request):
        """本接口（AssociateIPv6Address）用于将弹性公网IPv6（简称EIPv6）实例绑定到 CVM 或弹性网卡配置的内网 IPv6 地址上。

        - 将 EIPv6 绑定到 CVM 上，其本质是将 EIPv6 绑定到 CVM 弹性网卡所配置的内网 IPv6 地址上。
        - 将 EIPv6 绑定到指定网卡的内网 IPv6 时，需确保该内网 IPv6 地址为未绑定状态，才能执行绑定操作。

        :param request: Request instance for AssociateIPv6Address.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateIPv6AddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateIPv6AddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateIPv6Address", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateIPv6AddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateInstancesToCcnRouteTable(self, request):
        """本接口（AssociateInstancesToCcnRouteTable）用于将指定的云联网实例关联到指定的云联网路由表。

        :param request: Request instance for AssociateInstancesToCcnRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateInstancesToCcnRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateInstancesToCcnRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateInstancesToCcnRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateInstancesToCcnRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateNatGatewayAddress(self, request):
        """本接口(AssociateNatGatewayAddress)用于NAT网关绑定弹性IP（EIP）。

        :param request: Request instance for AssociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateNatGatewayAddress", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateNatGatewayAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateNetworkAclSubnets(self, request):
        """本接口（AssociateNetworkAclSubnets）用于网络ACL关联VPC下的子网。

        :param request: Request instance for AssociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateNetworkAclSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateNetworkAclSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AssociateNetworkInterfaceSecurityGroups(self, request):
        """本接口（AssociateNetworkInterfaceSecurityGroups）用于弹性网卡绑定安全组（SecurityGroup）。

        :param request: Request instance for AssociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AssociateNetworkInterfaceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.AssociateNetworkInterfaceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachCcnInstances(self, request):
        """本接口（AttachCcnInstances）用于将网络实例加载到云联网实例中，网络实例包括VPC和专线网关。<br />
        每个云联网能够关联的网络实例个数是有限的，详情请参考产品文档。如果需要扩充请联系在线客服。

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachClassicLinkVpc(self, request):
        """本接口(AttachClassicLinkVpc)用于创建私有网络和基础网络设备互通。
        * 私有网络和基础网络设备必须在同一个地域。
        * 私有网络和基础网络的区别详见vpc产品文档-<a href="https://cloud.tencent.com/document/product/215/30720">私有网络与基础网络</a>。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for AttachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachClassicLinkVpc", params, headers=headers)
            response = json.loads(body)
            model = models.AttachClassicLinkVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachNetworkInterface(self, request):
        """本接口（AttachNetworkInterface）用于弹性网卡绑定云服务器。
        * 一个弹性网卡请至少绑定一个安全组，如需绑定请参见<a href="https://cloud.tencent.com/document/product/215/43132">弹性网卡绑定安全组</a>。
        * 一个云服务器可以绑定多个弹性网卡，但只能绑定一个主网卡。更多限制信息详见<a href="https://cloud.tencent.com/document/product/576/18527">弹性网卡使用限制</a>。
        * 一个弹性网卡只能同时绑定一个云服务器。
        * 只有运行中或者已关机状态的云服务器才能绑定弹性网卡，查看云服务器状态详见<a href="https://cloud.tencent.com/document/api/213/9452#InstanceStatus">腾讯云服务器信息</a>。
        * 弹性网卡绑定的云服务器必须是私有网络的，而且云服务器所在可用区必须和弹性网卡子网的可用区相同。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.AttachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AttachSnapshotInstances(self, request):
        """本接口（AttachSnapshotInstances）用于快照策略关联实例。

        :param request: Request instance for AttachSnapshotInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachSnapshotInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachSnapshotInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AttachSnapshotInstances", params, headers=headers)
            response = json.loads(body)
            model = models.AttachSnapshotInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def AuditCrossBorderCompliance(self, request):
        """本接口（AuditCrossBorderCompliance）用于服务商操作合规化资质审批。
        * 服务商只能操作提交到本服务商的审批单，后台会校验身份。即只授权给服务商的`APPID` 调用本接口。
        * `APPROVED` 状态的审批单，可以再次操作为 `DENY`；`DENY` 状态的审批单，也可以再次操作为 `APPROVED`。

        :param request: Request instance for AuditCrossBorderCompliance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AuditCrossBorderComplianceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AuditCrossBorderComplianceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("AuditCrossBorderCompliance", params, headers=headers)
            response = json.loads(body)
            model = models.AuditCrossBorderComplianceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckAssistantCidr(self, request):
        """本接口（CheckAssistantCidr）用于检查辅助CIDR是否与存量路由、对等连接（对端VPC的CIDR）等资源存在冲突。如果存在重叠，则返回重叠的资源。
        * 检测辅助CIDR是否与当前VPC的主CIDR和辅助CIDR存在重叠。
        * 检测辅助CIDR是否与当前VPC的路由的目的端存在重叠。
        * 检测辅助CIDR是否与当前VPC的对等连接，对端VPC下的主CIDR或辅助CIDR存在重叠。

        :param request: Request instance for CheckAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.CheckAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckDefaultSubnet(self, request):
        """本接口（CheckDefaultSubnet）用于预判是否可建默认子网。

        :param request: Request instance for CheckDefaultSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckDefaultSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.CheckDefaultSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckGatewayFlowMonitor(self, request):
        """本接口（CheckGatewayFlowMonitor）用于查询网关是否启用流量监控。

        :param request: Request instance for CheckGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckGatewayFlowMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.CheckGatewayFlowMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckNetDetectState(self, request):
        """本接口（CheckNetDetectState）用于验证网络探测。

        :param request: Request instance for CheckNetDetectState.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckNetDetectState", params, headers=headers)
            response = json.loads(body)
            model = models.CheckNetDetectStateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CheckTrafficMirror(self, request):
        """检查流量镜像的采集端接收端（公网IP类型）

        :param request: Request instance for CheckTrafficMirror.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CheckTrafficMirror", params, headers=headers)
            response = json.loads(body)
            model = models.CheckTrafficMirrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ClearRouteTableSelectionPolicies(self, request):
        """本接口（ClearRouteTableSelectionPolicies）用于清空指定云联网的路由表选择策略。

        :param request: Request instance for ClearRouteTableSelectionPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ClearRouteTableSelectionPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ClearRouteTableSelectionPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ClearRouteTableSelectionPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ClearRouteTableSelectionPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CloneSecurityGroup(self, request):
        """本接口（CloneSecurityGroup）用于根据存量的安全组，克隆创建出同样规则配置的安全组。默认仅克隆安全组及其规则信息，可通过入参开启克隆安全组标签信息。

        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CloneSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CloneSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CloneSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CloneSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressTemplate(self, request):
        """本接口（CreateAddressTemplate）用于创建IP地址模板。

        :param request: Request instance for CreateAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAddressTemplateGroup(self, request):
        """本接口（CreateAddressTemplateGroup）用于创建IP地址模板集合。

        :param request: Request instance for CreateAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAddressTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAddressTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAndAttachNetworkInterface(self, request):
        """本接口（CreateAndAttachNetworkInterface）用于创建弹性网卡并绑定云服务器。
        * 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
        * 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 创建弹性网卡同时可以绑定已有安全组。
        * 创建弹性网卡同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for CreateAndAttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAndAttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAndAttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAndAttachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAndAttachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateAssistantCidr(self, request):
        """本接口（CreateAssistantCidr）用于批量创建辅助CIDR。

        :param request: Request instance for CreateAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.CreateAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateBandwidthPackage(self, request):
        """本接口 (CreateBandwidthPackage) 支持创建[设备带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)和[IP带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)。

        :param request: Request instance for CreateBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateBandwidthPackage", params, headers=headers)
            response = json.loads(body)
            model = models.CreateBandwidthPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCcn(self, request):
        """本接口（CreateCcn）用于创建云联网（CCN）。<br />
        * 创建云联网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        * 每个账号能创建的云联网实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。

        :param request: Request instance for CreateCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcn", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCcnRouteTables(self, request):
        """本接口（CreateCcnRouteTables）用于给指定的云联网实例新建路由表。

        :param request: Request instance for CreateCcnRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCcnRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCcnRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdcLDCXList(self, request):
        """创建 IDC 通道

        :param request: Request instance for CreateCdcLDCXList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCdcLDCXListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCdcLDCXListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdcLDCXList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdcLDCXListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCdcNetPlanes(self, request):
        """创建虚拟连接，用于支持 CDC 多租户模式

        :param request: Request instance for CreateCdcNetPlanes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCdcNetPlanesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCdcNetPlanesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCdcNetPlanes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCdcNetPlanesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateCustomerGateway(self, request):
        """本接口（CreateCustomerGateway）用于创建对端网关。

        :param request: Request instance for CreateCustomerGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateCustomerGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateCustomerGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDefaultSecurityGroup(self, request):
        """本接口（CreateDefaultSecurityGroup）用于创建（如果项目下未存在默认安全组，则创建；已存在则获取。）默认安全组（SecurityGroup）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/12453">安全组数量限制</a>。
        * 默认安全组会放通所有IPv4规则，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。
        * 创建安全组同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateDefaultSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefaultSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDefaultSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDefaultVpc(self, request):
        """本接口（CreateDefaultVpc）用于创建默认私有网络(VPC）。

        默认VPC适用于快速入门和启动公共实例，您可以像使用任何其他VPC一样使用默认VPC。如果您想创建标准VPC，即指定VPC名称、VPC网段、子网网段、子网可用区，请使用常规创建VPC接口（CreateVpc）

        正常情况，本接口并不一定生产默认VPC，而是根据用户账号的网络属性（DescribeAccountAttributes）来决定的
        * 支持基础网络、VPC，返回VpcId为0
        * 只支持VPC，返回默认VPC信息

        您也可以通过 Force 参数，强制返回默认VPC。

        :param request: Request instance for CreateDefaultVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDefaultVpc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDefaultVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDhcpIp(self, request):
        """本接口（CreateDhcpIp）用于创建DhcpIp。

        :param request: Request instance for CreateDhcpIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDhcpIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDhcpIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDhcpIp", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDhcpIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDirectConnectGateway(self, request):
        """本接口（CreateDirectConnectGateway）用于创建专线网关。

        :param request: Request instance for CreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDirectConnectGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDirectConnectGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateDirectConnectGatewayCcnRoutes(self, request):
        """本接口（CreateDirectConnectGatewayCcnRoutes）用于创建专线网关的云联网路由（IDC网段）

        :param request: Request instance for CreateDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateFlowLog(self, request):
        """本接口（CreateFlowLog）用于创建网络流日志。

        :param request: Request instance for CreateFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateFlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.CreateFlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHaVip(self, request):
        """本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）。

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHaVip", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHaVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHighPriorityRouteTable(self, request):
        """高优路由表创建

        :param request: Request instance for CreateHighPriorityRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHighPriorityRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHighPriorityRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHighPriorityRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHighPriorityRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateHighPriorityRoutes(self, request):
        """创建高优路由表条目。

        :param request: Request instance for CreateHighPriorityRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHighPriorityRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHighPriorityRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateHighPriorityRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateHighPriorityRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateIp6Translators(self, request):
        """1. 该接口用于创建IPV6转换IPV4实例，支持批量
        2. 同一个账户在一个地域最多允许创建10个转换实例

        :param request: Request instance for CreateIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateIp6Translators", params, headers=headers)
            response = json.loads(body)
            model = models.CreateIp6TranslatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateLocalGateway(self, request):
        """本接口（CreateLocalGateway）用于创建用于CDC的本地网关。

        :param request: Request instance for CreateLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGateway(self, request):
        """本接口(CreateNatGateway)用于创建NAT网关。
        在对新建的NAT网关做其他操作前，需先确认此网关已被创建完成（DescribeNatGateway接口返回的实例State字段为AVAILABLE）。

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口(CreateNatGatewayDestinationIpPortTranslationNatRule)用于创建NAT网关端口转发规则。

        :param request: Request instance for CreateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNatGatewaySourceIpTranslationNatRule(self, request):
        """本接口(CreateNatGatewaySourceIpTranslationNatRule)用于创建NAT网关SNAT规则

        :param request: Request instance for CreateNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNatGatewaySourceIpTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNatGatewaySourceIpTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetDetect(self, request):
        """本接口（CreateNetDetect）用于创建网络探测。

        :param request: Request instance for CreateNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetDetect", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkAcl(self, request):
        """本接口（CreateNetworkAcl）用于创建新的<a href="https://cloud.tencent.com/document/product/215/20088">网络ACL</a>。
        * 新建的网络ACL的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用ModifyNetworkAclEntries将网络ACL的规则设置为需要的规则。

        :param request: Request instance for CreateNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkAcl", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkAclEntries(self, request):
        """本接口（CreateNetworkAclEntries）用于增量添加网络ACL三元组的入站规则和出站规则。

        :param request: Request instance for CreateNetworkAclEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkAclEntries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkAclEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkAclQuintupleEntries(self, request):
        """本接口（CreateNetworkAclQuintupleEntries）用于增量网络ACL五元组的入站规则和出站规则。

        :param request: Request instance for CreateNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateNetworkInterface(self, request):
        """本接口（CreateNetworkInterface）用于创建弹性网卡。
        * 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
        * 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 创建弹性网卡同时可以绑定已有安全组。
        * 创建弹性网卡同时可以绑定标签, 响应里的标签列表代表添加成功的标签。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.CreateNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateNatGateway(self, request):
        """本接口（CreatePrivateNatGateway）用于创建私网NAT网关。

        :param request: Request instance for CreatePrivateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（CreatePrivateNatGatewayDestinationIpPortTranslationNatRule）用于创建私网NAT网关目的端口转换规则

        :param request: Request instance for CreatePrivateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateNatGatewayTranslationAclRule(self, request):
        """本接口（ CreatePrivateNatGatewayTranslationAclRule）用于创建私网NAT网关源端转换访问控制规则

        :param request: Request instance for CreatePrivateNatGatewayTranslationAclRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayTranslationAclRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayTranslationAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateNatGatewayTranslationAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateNatGatewayTranslationAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreatePrivateNatGatewayTranslationNatRule(self, request):
        """本接口（CreatePrivateNatGatewayTranslationNatRule）用于创建私网NAT网关源端转换规则。

        :param request: Request instance for CreatePrivateNatGatewayTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreatePrivateNatGatewayTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreatePrivateNatGatewayTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.CreatePrivateNatGatewayTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateReserveIpAddresses(self, request):
        """创建内网保留IP

        :param request: Request instance for CreateReserveIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateReserveIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateReserveIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateReserveIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.CreateReserveIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRouteTable(self, request):
        """本接口(CreateRouteTable)用于创建路由表。
        * 创建了VPC后，系统会创建一个默认路由表，所有新建的子网都会关联到默认路由表。默认情况下您可以直接使用默认路由表来管理您的路由策略。当您的路由策略较多时，您可以调用创建路由表接口创建更多路由表管理您的路由策略。
        * 创建路由表同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateRoutes(self, request):
        """本接口（CreateRoutes）用于创建路由策略。
        * 向指定路由表批量新增路由策略。

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroup(self, request):
        """本接口（CreateSecurityGroup）用于创建新的安全组（SecurityGroup）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/12453">安全组数量限制</a>。
        * 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。
        * 创建安全组同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupPolicies(self, request):
        """本接口（CreateSecurityGroupPolicies）用于创建安全组规则（SecurityGroupPolicy）。

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

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSecurityGroupWithPolicies(self, request):
        """本接口（CreateSecurityGroupWithPolicies）用于创建新的安全组（SecurityGroup），并且可以同时添加安全组规则（SecurityGroupPolicy）。
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

        :param request: Request instance for CreateSecurityGroupWithPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSecurityGroupWithPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSecurityGroupWithPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServiceTemplate(self, request):
        """本接口（CreateServiceTemplate）用于创建协议端口模板。

        :param request: Request instance for CreateServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateServiceTemplateGroup(self, request):
        """本接口（CreateServiceTemplateGroup）用于创建协议端口模板集合。

        :param request: Request instance for CreateServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateServiceTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.CreateServiceTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSnapshotPolicies(self, request):
        """本接口（CreateSnapshotPolicies）用于创建快照策略。

        :param request: Request instance for CreateSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubnet(self, request):
        """本接口（CreateSubnet）用于创建子网。
        * 创建子网前必须创建好 VPC。
        * 子网创建成功后，子网网段不能修改。子网网段必须在VPC网段内，可以和VPC网段相同（VPC有且只有一个子网时），建议子网网段在VPC网段内，预留网段给其他子网使用。
        * 您可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）。
        * 同一个VPC内，多个子网的网段不能重叠。
        * 子网创建后会自动关联到默认路由表。
        * 创建子网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateSubnets(self, request):
        """本接口（CreateSubnets）用于批量创建子网。
        * 创建子网前必须创建好 VPC。
        * 子网创建成功后，子网网段不能修改。子网网段必须在VPC网段内，可以和VPC网段相同（VPC有且只有一个子网时），建议子网网段在VPC网段内，预留网段给其他子网使用。
        * 您可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址）。
        * 同一个VPC内，多个子网的网段不能重叠。
        * 子网创建后会自动关联到默认路由表。
        * 创建子网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.CreateSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrafficMirror(self, request):
        """本接口（CreateTrafficMirror）用于创建流量镜像实例。

        :param request: Request instance for CreateTrafficMirror.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrafficMirror", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrafficMirrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateTrafficPackages(self, request):
        """本接口 (CreateTrafficPackages) 用于创建共享流量包。

        :param request: Request instance for CreateTrafficPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.CreateTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpc(self, request):
        """本接口（CreateVpc）用于创建私有网络（VPC）。
        * 用户可以创建的最小网段子网掩码为28（有16个IP地址），10.0.0.0/12，172.16.0.0/12最大网段子网掩码为12（1,048,576个IP地址），192.168.0.0/16最大网段子网掩码为16（65,536个IP地址）如果需要规划VPC网段请参见[网络规划](https://cloud.tencent.com/document/product/215/30313)。
        * 同一个地域能创建的VPC资源个数也是有限制的，详见 <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>，如果需要申请更多资源，请提交[工单申请](https://console.cloud.tencent.com/workorder/category)。
        * 创建VPC同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpc", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcEndPoint(self, request):
        """本接口（CreateVpcEndPoint）用于创建终端节点。

        :param request: Request instance for CreateVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcEndPointService(self, request):
        """本接口（CreateVpcEndPointService）用于创建终端节点服务。

        :param request: Request instance for CreateVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcEndPointServiceWhiteList(self, request):
        """本接口（CreateVpcEndPointServiceWhiteList）创建终端服务白名单。

        :param request: Request instance for CreateVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpcPeeringConnection(self, request):
        """本接口（CreateVpcPeeringConnection）用于创建私有网络对等连接。

        :param request: Request instance for CreateVpcPeeringConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcPeeringConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcPeeringConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpcPeeringConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpcPeeringConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnConnection(self, request):
        """本接口（CreateVpnConnection）用于创建VPN通道。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for CreateVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnGateway(self, request):
        """本接口（CreateVpnGateway）用于创建VPN网关。

        :param request: Request instance for CreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnGatewayRoutes(self, request):
        """创建路由型VPN网关的目的路由

        :param request: Request instance for CreateVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnGatewaySslClient(self, request):
        """创建SSL-VPN-CLIENT

        :param request: Request instance for CreateVpnGatewaySslClient.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslClientRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnGatewaySslClient", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnGatewaySslClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def CreateVpnGatewaySslServer(self, request):
        """本接口（CreateVpnGatewaySslServer）用于创建SSL-VPN Server端。

        :param request: Request instance for CreateVpnGatewaySslServer.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslServerRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("CreateVpnGatewaySslServer", params, headers=headers)
            response = json.loads(body)
            model = models.CreateVpnGatewaySslServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressTemplate(self, request):
        """本接口（DeleteAddressTemplate）用于删除IP地址模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DeleteAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAddressTemplateGroup(self, request):
        """本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DeleteAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAddressTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAddressTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteAssistantCidr(self, request):
        """本接口（DeleteAssistantCidr）用于删除辅助CIDR。

        :param request: Request instance for DeleteAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteBandwidthPackage(self, request):
        """接口支持删除共享带宽包，包括[设备带宽包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[IP带宽包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)

        :param request: Request instance for DeleteBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteBandwidthPackage", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteBandwidthPackageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCcn(self, request):
        """本接口（DeleteCcn）用于删除云联网。
        * 删除后，云联网关联的所有实例间路由将被删除，网络将会中断，请务必确认
        * 删除云联网是不可逆的操作，请谨慎处理。

        :param request: Request instance for DeleteCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcn", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCcnResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCcnRouteTables(self, request):
        """本接口（DeleteCcnRouteTables）用于删除云联网路由表。

        :param request: Request instance for DeleteCcnRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCcnRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCcnRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCcnRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCdcLDCXList(self, request):
        """删除 IDC通道

        :param request: Request instance for DeleteCdcLDCXList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCdcLDCXListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCdcLDCXListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCdcLDCXList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCdcLDCXListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCdcNetPlanes(self, request):
        """删除虚拟连接

        :param request: Request instance for DeleteCdcNetPlanes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCdcNetPlanesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCdcNetPlanesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCdcNetPlanes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCdcNetPlanesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteCustomerGateway(self, request):
        """本接口（DeleteCustomerGateway）用于删除对端网关。

        :param request: Request instance for DeleteCustomerGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteCustomerGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteCustomerGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDhcpIp(self, request):
        """本接口（DeleteDhcpIp）用于删除DhcpIp。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DeleteDhcpIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDhcpIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDhcpIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDhcpIp", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDhcpIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDirectConnectGateway(self, request):
        """本接口（DeleteDirectConnectGateway）用于删除专线网关。
        <li>如果是 NAT 网关，删除专线网关后，NAT 规则以及 ACL 策略都被清理了。</li>
        <li>删除专线网关后，系统会删除路由表中跟该专线网关相关的路由策略。</li>
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`QueryTask`接口

        :param request: Request instance for DeleteDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDirectConnectGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDirectConnectGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteDirectConnectGatewayCcnRoutes(self, request):
        """本接口（DeleteDirectConnectGatewayCcnRoutes）用于删除专线网关的云联网路由（IDC网段）

        :param request: Request instance for DeleteDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteFlowLog(self, request):
        """本接口（DeleteFlowLog）用于删除流日志。

        :param request: Request instance for DeleteFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteFlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteFlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHaVip(self, request):
        """本接口（DeleteHaVip）用于删除高可用虚拟IP（HAVIP）。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHaVip", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHaVipResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHighPriorityRouteTables(self, request):
        """删除高优路由表

        :param request: Request instance for DeleteHighPriorityRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHighPriorityRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHighPriorityRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHighPriorityRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHighPriorityRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteHighPriorityRoutes(self, request):
        """删除高优路由表的路由条目。

        :param request: Request instance for DeleteHighPriorityRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHighPriorityRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHighPriorityRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteHighPriorityRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteHighPriorityRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteIp6Translators(self, request):
        """1. 该接口用于释放IPV6转换实例，支持批量。
        2.  如果IPV6转换实例建立有转换规则，会一并删除。

        :param request: Request instance for DeleteIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteIp6Translators", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteIp6TranslatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteLocalGateway(self, request):
        """本接口（DeleteLocalGateway）用于删除CDC的本地网关。

        :param request: Request instance for DeleteLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGateway(self, request):
        """本接口（DeleteNatGateway）用于删除NAT网关。
        删除 NAT 网关后，系统会自动删除路由表中包含此 NAT 网关的路由项，同时也会解绑弹性公网IP（EIP）。

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（DeleteNatGatewayDestinationIpPortTranslationNatRule）用于删除NAT网关端口转发规则。

        :param request: Request instance for DeleteNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNatGatewaySourceIpTranslationNatRule(self, request):
        """本接口（DeleteNatGatewaySourceIpTranslationNatRule）用于删除NAT网关端口SNAT转发规则。

        :param request: Request instance for DeleteNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNatGatewaySourceIpTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNatGatewaySourceIpTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetDetect(self, request):
        """本接口（DeleteNetDetect）用于删除网络探测实例。

        :param request: Request instance for DeleteNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetDetect", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkAcl(self, request):
        """本接口（DeleteNetworkAcl）用于删除网络ACL。

        :param request: Request instance for DeleteNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkAcl", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkAclResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkAclEntries(self, request):
        """本接口（DeleteNetworkAclEntries）用于删除三元组网络ACL的入站规则和出站规则。在NetworkAclEntrySet参数中：
        * 删除IPv4规则，需要传入NetworkAclIpv4EntryId。
        * 删除IPv6规则，需要传入NetworkAclIpv6EntryId。

        :param request: Request instance for DeleteNetworkAclEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkAclEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkAclEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkAclQuintupleEntries(self, request):
        """本接口（DeleteNetworkAclQuintupleEntries）用于删除网络ACL五元组指定的入站规则和出站规则（但不是全量删除该ACL下的所有条目）。在NetworkAclQuintupleEntrySet参数中：NetworkAclQuintupleEntry需要提供NetworkAclQuintupleEntryId。

        :param request: Request instance for DeleteNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteNetworkInterface(self, request):
        """本接口（DeleteNetworkInterface）用于删除弹性网卡。
        * 弹性网卡上绑定了云服务器时，不能被删除。
        * 删除指定弹性网卡，弹性网卡必须先和子机解绑才能删除。删除之后弹性网卡上所有内网IP都将被退还。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for DeleteNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateNatGateway(self, request):
        """本接口（DeletePrivateNatGateway）用于删除私网NAT网关。

        :param request: Request instance for DeletePrivateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（DeletePrivateNatGatewayDestinationIpPortTranslationNatRule）用于删除私网NAT网关目的端口转换规则

        :param request: Request instance for DeletePrivateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateNatGatewayTranslationAclRule(self, request):
        """本接口（DeletePrivateNatGatewayTranslationAclRule）用于删除私网NAT网关源端转换访问控制规则

        :param request: Request instance for DeletePrivateNatGatewayTranslationAclRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayTranslationAclRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayTranslationAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateNatGatewayTranslationAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateNatGatewayTranslationAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeletePrivateNatGatewayTranslationNatRule(self, request):
        """本接口（DeletePrivateNatGatewayTranslationNatRule）用于删除私网NAT网关源端转换规则

        :param request: Request instance for DeletePrivateNatGatewayTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeletePrivateNatGatewayTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeletePrivateNatGatewayTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.DeletePrivateNatGatewayTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteReserveIpAddresses(self, request):
        """删除内网保留IP

        :param request: Request instance for DeleteReserveIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteReserveIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteReserveIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteReserveIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteReserveIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRouteTable(self, request):
        """本接口（DeleteRouteTable）用于删除路由表。

        :param request: Request instance for DeleteRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRouteTable", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRouteTableResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteRoutes(self, request):
        """本接口(DeleteRoutes)用于对某个路由表批量删除路由策略（Route）。

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroup(self, request):
        """本接口（DeleteSecurityGroup）用于删除安全组（SecurityGroup）。
        * 只有当前账号下的安全组允许被删除。
        * 安全组实例ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要先进行规则修改，再删除安全组。
        * 删除的安全组无法再找回，请谨慎调用。

        :param request: Request instance for DeleteSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSecurityGroupPolicies(self, request):
        """本接口（DeleteSecurityGroupPolicies）用于用于删除安全组规则（SecurityGroupPolicy）。
        * SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServiceTemplate(self, request):
        """本接口（DeleteServiceTemplate）用于删除协议端口模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DeleteServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceTemplate", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceTemplateResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteServiceTemplateGroup(self, request):
        """本接口（DeleteServiceTemplateGroup）用于删除协议端口模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DeleteServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteServiceTemplateGroup", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteServiceTemplateGroupResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSnapshotPolicies(self, request):
        """本接口（DeleteSnapshotPolicies）用于删除快照策略。

        :param request: Request instance for DeleteSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteSubnet(self, request):
        """本接口（DeleteSubnet）用于删除子网（Subnet）。
        * 删除子网前，请清理该子网下所有资源，包括云服务器、负载均衡、云数据、NoSQL、弹性网卡等资源。

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteSubnet", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteSubnetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTemplateMember(self, request):
        """删除模板对象中的IP地址、协议端口、IP地址组、协议端口组。

        :param request: Request instance for DeleteTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTemplateMember", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTemplateMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrafficMirror(self, request):
        """本接口（DeleteTrafficMirror）用于删除流量镜像实例。

        :param request: Request instance for DeleteTrafficMirror.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrafficMirror", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrafficMirrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteTrafficPackages(self, request):
        """删除共享带宽包（仅非活动状态的流量包可删除）。

        :param request: Request instance for DeleteTrafficPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpc(self, request):
        """本接口（DeleteVpc）用于删除私有网络。
        * 删除前请确保 VPC 内已经没有相关资源，例如云服务器、云数据库、NoSQL、VPN网关、专线网关、负载均衡、对等连接、与之互通的基础网络设备等。
        * 删除私有网络是不可逆的操作，请谨慎处理。

        :param request: Request instance for DeleteVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcEndPoint(self, request):
        """本接口（DeleteVpcEndPoint）用于删除终端节点。

        :param request: Request instance for DeleteVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcEndPointService(self, request):
        """本接口（DeleteVpcEndPointService）用于删除终端节点服务。

        :param request: Request instance for DeleteVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcEndPointServiceWhiteList(self, request):
        """本接口（DeleteVpcEndPointServiceWhiteList）用于删除终端节点服务白名单。

        :param request: Request instance for DeleteVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpcPeeringConnection(self, request):
        """本接口（DeleteVpcPeeringConnection）用于删除私有网络对等连接。

        :param request: Request instance for DeleteVpcPeeringConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcPeeringConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcPeeringConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpcPeeringConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpcPeeringConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnConnection(self, request):
        """本接口（DeleteVpnConnection）用于删除VPN通道。
        >?本接口为异步接口
        >

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGateway(self, request):
        """本接口（DeleteVpnGateway）用于删除VPN网关。

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGatewayRoutes(self, request):
        """本接口（DeleteVpnGatewayRoutes）用于删除VPN网关路由

        :param request: Request instance for DeleteVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGatewaySslClient(self, request):
        """本接口（DeleteVpnGatewaySslClient）用于删除SSL-VPN-CLIENT。

        :param request: Request instance for DeleteVpnGatewaySslClient.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslClientRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslClientResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGatewaySslClient", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewaySslClientResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DeleteVpnGatewaySslServer(self, request):
        """删除SSL-VPN-SERVER 实例

        :param request: Request instance for DeleteVpnGatewaySslServer.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslServerRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DeleteVpnGatewaySslServer", params, headers=headers)
            response = json.loads(body)
            model = models.DeleteVpnGatewaySslServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAccountAttributes(self, request):
        """本接口（DescribeAccountAttributes）用于查询用户账号私有属性。

        :param request: Request instance for DescribeAccountAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAccountAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAccountAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressBandwidthRange(self, request):
        """查询指定EIP的带宽上下限范围。

        :param request: Request instance for DescribeAddressBandwidthRange.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressBandwidthRangeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressBandwidthRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressBandwidthRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressBandwidthRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressQuota(self, request):
        """本接口 (DescribeAddressQuota) 用于查询您账户的[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）在当前地域的配额信息。配额详情可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)。

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressTemplateGroups(self, request):
        """本接口（DescribeAddressTemplateGroups）用于查询IP地址模板集合。

        :param request: Request instance for DescribeAddressTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressTemplateGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressTemplateGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddressTemplates(self, request):
        """本接口（DescribeAddressTemplates）用于查询IP地址模板。

        :param request: Request instance for DescribeAddressTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddressTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAddresses(self, request):
        """本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的详细信息。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIP。

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeAssistantCidr(self, request):
        """本接口（DescribeAssistantCidr）用于查询辅助CIDR列表。

        :param request: Request instance for DescribeAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageBandwidthRange(self, request):
        """查询指定带宽包的带宽上下限范围

        :param request: Request instance for DescribeBandwidthPackageBandwidthRange.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBandwidthRangeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBandwidthRangeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageBandwidthRange", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageBandwidthRangeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageBillUsage(self, request):
        """本接口 (DescribeBandwidthPackageBillUsage) 用于查询后付费共享带宽包当前的计费用量.

        :param request: Request instance for DescribeBandwidthPackageBillUsage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBillUsageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBillUsageResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageBillUsage", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageBillUsageResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageQuota(self, request):
        """接口用于查询账户在当前地域的带宽包上限数量以及使用数量

        :param request: Request instance for DescribeBandwidthPackageQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackageResources(self, request):
        """本接口 (DescribeBandwidthPackageResources) 用于根据共享带宽包唯一ID查询共享带宽包内的资源列表，支持按条件过滤查询结果和分页查询。

        :param request: Request instance for DescribeBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackageResources", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackageResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeBandwidthPackages(self, request):
        """接口用于查询带宽包详细信息，包括带宽包唯一标识ID，类型，计费模式，名称，资源信息等

        :param request: Request instance for DescribeBandwidthPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeBandwidthPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeBandwidthPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnAttachedInstances(self, request):
        """本接口（DescribeCcnAttachedInstances）用于查询云联网实例下已关联的网络实例。

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnAttachedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnAttachedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRegionBandwidthLimits(self, request):
        """本接口（DescribeCcnRegionBandwidthLimits）用于查询云联网各地域出带宽上限，该接口只返回已关联网络实例包含的地域。

        :param request: Request instance for DescribeCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRouteTableBroadcastPolicys(self, request):
        """本接口(DescribeCcnRouteTableBroadcastPolicys)用于查询指定云联网路由表的路由传播策略。

        :param request: Request instance for DescribeCcnRouteTableBroadcastPolicys.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRouteTableBroadcastPolicysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRouteTableBroadcastPolicysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRouteTableBroadcastPolicys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRouteTableBroadcastPolicysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRouteTableInputPolicys(self, request):
        """本接口(DescribeCcnRouteTableInputPolicys)用于查询指定云联网路由表的路由接收策略。

        :param request: Request instance for DescribeCcnRouteTableInputPolicys.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRouteTableInputPolicysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRouteTableInputPolicysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRouteTableInputPolicys", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRouteTableInputPolicysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRouteTables(self, request):
        """该接口用于查询指定的云联网实例的路由表信息。

        :param request: Request instance for DescribeCcnRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcnRoutes(self, request):
        """本接口（DescribeCcnRoutes）用于查询已加入云联网（CCN）的路由。

        :param request: Request instance for DescribeCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCcns(self, request):
        """本接口（DescribeCcns）用于查询云联网（CCN）列表。

        :param request: Request instance for DescribeCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCcns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCcnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdcLDCXList(self, request):
        """查询 IDC通道信息

        :param request: Request instance for DescribeCdcLDCXList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCdcLDCXListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCdcLDCXListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdcLDCXList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdcLDCXListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdcNetPlanes(self, request):
        """查询虚拟连接

        :param request: Request instance for DescribeCdcNetPlanes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCdcNetPlanesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCdcNetPlanesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdcNetPlanes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdcNetPlanesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCdcUsedIdcVlan(self, request):
        """查询IDC使用的 VLAN

        :param request: Request instance for DescribeCdcUsedIdcVlan.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCdcUsedIdcVlanRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCdcUsedIdcVlanResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCdcUsedIdcVlan", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCdcUsedIdcVlanResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeClassicLinkInstances(self, request):
        """本接口（DescribeClassicLinkInstances）用于查询私有网络和基础网络设备互通列表。

        :param request: Request instance for DescribeClassicLinkInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeClassicLinkInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeClassicLinkInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderCcnRegionBandwidthLimits(self, request):
        """本接口（DescribeCrossBorderCcnRegionBandwidthLimits）用于获取要锁定的限速实例列表。
        该接口一般用来封禁地域间限速的云联网实例下的限速实例, 目前联通内部运营系统通过云API调用, 如果是出口限速, 一般使用更粗的云联网实例粒度封禁（DescribeTenantCcns）
        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统

        :param request: Request instance for DescribeCrossBorderCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderCompliance(self, request):
        """本接口（DescribeCrossBorderCompliance）用于查询用户创建的合规化资质审批单。
        服务商可以查询服务名下的任意 `APPID` 创建的审批单；非服务商，只能查询自己审批单。

        :param request: Request instance for DescribeCrossBorderCompliance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderComplianceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderComplianceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderCompliance", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderComplianceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCrossBorderFlowMonitor(self, request):
        """本接口（DescribeCrossBorderFlowMonitor）用于查询跨境带宽监控数据，该接口目前只提供给服务商联通使用。

        :param request: Request instance for DescribeCrossBorderFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCrossBorderFlowMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCrossBorderFlowMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerGatewayVendors(self, request):
        """本接口（DescribeCustomerGatewayVendors）用于查询可支持的对端网关厂商信息。

        :param request: Request instance for DescribeCustomerGatewayVendors.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerGatewayVendors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerGatewayVendorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeCustomerGateways(self, request):
        """本接口（DescribeCustomerGateways）用于查询对端网关列表。

        :param request: Request instance for DescribeCustomerGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeCustomerGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeCustomerGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDhcpIps(self, request):
        """本接口（DescribeDhcpIps）用于查询DhcpIp列表

        :param request: Request instance for DescribeDhcpIps.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDhcpIpsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDhcpIpsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDhcpIps", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDhcpIpsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectGatewayCcnRoutes(self, request):
        """本接口（DescribeDirectConnectGatewayCcnRoutes）用于查询专线网关的云联网路由（IDC网段）

        :param request: Request instance for DescribeDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeDirectConnectGateways(self, request):
        """本接口（DescribeDirectConnectGateways）用于查询专线网关。

        :param request: Request instance for DescribeDirectConnectGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeDirectConnectGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeDirectConnectGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowLog(self, request):
        """本接口（DescribeFlowLog）用于查询流日志实例信息。

        :param request: Request instance for DescribeFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowLog", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowLogResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeFlowLogs(self, request):
        """本接口（DescribeFlowLogs）用于查询获取流日志集合。

        :param request: Request instance for DescribeFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayFlowMonitorDetail(self, request):
        """本接口（DescribeGatewayFlowMonitorDetail）用于查询网关流量监控明细。
        * 只支持单个网关实例查询。即入参 `VpnId`、 `DirectConnectGatewayId`、 `PeeringConnectionId`、 `NatId` 最多只支持传一个，且必须传一个。
        * 如果网关有流量，但调用本接口没有返回数据，请在控制台对应网关详情页确认是否开启网关流量监控。

        :param request: Request instance for DescribeGatewayFlowMonitorDetail.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayFlowMonitorDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayFlowMonitorDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeGatewayFlowQos(self, request):
        """本接口（DescribeGatewayFlowQos）用于查询网关来访IP流控带宽。

        :param request: Request instance for DescribeGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeGatewayFlowQos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeGatewayFlowQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHaVips(self, request):
        """本接口（DescribeHaVips）用于查询高可用虚拟IP（HAVIP）列表。

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHaVips", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHaVipsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHighPriorityRouteTables(self, request):
        """查询高优路由表。

        :param request: Request instance for DescribeHighPriorityRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHighPriorityRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHighPriorityRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHighPriorityRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHighPriorityRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeHighPriorityRoutes(self, request):
        """查询高优路由表条目信息。

        :param request: Request instance for DescribeHighPriorityRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHighPriorityRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHighPriorityRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeHighPriorityRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeHighPriorityRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIPv6Addresses(self, request):
        """本接口（DescribeIPv6Addresses）用于查询一个或多个弹性公网 IPv6（简称 EIPv6）实例的详细信息。

        - 支持查询您在指定地域的弹性公网 IPv6 和传统弹性公网 IPv6 实例信息
        - 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIPv6。

        :param request: Request instance for DescribeIPv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIPv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIPv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIPv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIPv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIp6Addresses(self, request):
        """本接口（DescribeIp6Addresses）用于查询一个或多个传统弹性公网 IPv6 实例的详细信息。

        :param request: Request instance for DescribeIp6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIp6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIp6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIp6TranslatorQuota(self, request):
        """查询账户在指定地域IPV6转换实例和规则的配额

        :param request: Request instance for DescribeIp6TranslatorQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIp6TranslatorQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIp6TranslatorQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIp6Translators(self, request):
        """1. 该接口用于查询账户下的IPV6转换实例及其绑定的转换规则信息
        2. 支持过滤查询

        :param request: Request instance for DescribeIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIp6Translators", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIp6TranslatorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpGeolocationDatabaseUrl(self, request):
        """本接口（DescribeIpGeolocationDatabaseUrl）用于获取IP地理位置库下载链接。
        <font color="#FF0000">本接口即将下线，仅供存量用户使用，暂停新增用户。</font>

        :param request: Request instance for DescribeIpGeolocationDatabaseUrl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationDatabaseUrlRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationDatabaseUrlResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpGeolocationDatabaseUrl", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpGeolocationDatabaseUrlResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeIpGeolocationInfos(self, request):
        """本接口（DescribeIpGeolocationInfos）用于查询IP地址信息，包括地理位置信息和网络信息。
        <font color="#FF0000">本接口即将下线，仅供存量客户使用，暂停新增用户。</font>

        :param request: Request instance for DescribeIpGeolocationInfos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationInfosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationInfosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeIpGeolocationInfos", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeIpGeolocationInfosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeLocalGateway(self, request):
        """本接口（DescribeLocalGateway）用于查询CDC的本地网关。

        :param request: Request instance for DescribeLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewayDestinationIpPortTranslationNatRules(self, request):
        """本接口（DescribeNatGatewayDestinationIpPortTranslationNatRules）用于查询NAT网关端口转发规则对象数组。

        :param request: Request instance for DescribeNatGatewayDestinationIpPortTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewayDestinationIpPortTranslationNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewayDirectConnectGatewayRoute(self, request):
        """查询专线绑定NAT的路由

        :param request: Request instance for DescribeNatGatewayDirectConnectGatewayRoute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDirectConnectGatewayRouteRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDirectConnectGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewayDirectConnectGatewayRoute", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewayDirectConnectGatewayRouteResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewayFlowMonitorDetail(self, request):
        """本接口（DescribeNatGatewayFlowMonitorDetail）用于查询NAT网关流量监控明细。

        - 只支持单个网关实例查询。即入参 `NatGatewayId` 最多只支持传一个，且必须传一个。
        - 如果网关有流量，但调用本接口没有返回数据，请在控制台对应网关详情页确认是否开启网关流量监控。

        :param request: Request instance for DescribeNatGatewayFlowMonitorDetail.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayFlowMonitorDetailRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayFlowMonitorDetailResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewayFlowMonitorDetail", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewayFlowMonitorDetailResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGatewaySourceIpTranslationNatRules(self, request):
        """本接口（DescribeNatGatewaySourceIpTranslationNatRules）用于查询NAT网关SNAT转发规则对象数组。

        :param request: Request instance for DescribeNatGatewaySourceIpTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaySourceIpTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaySourceIpTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGatewaySourceIpTranslationNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewaySourceIpTranslationNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNatGateways(self, request):
        """本接口（DescribeNatGateways）用于查询 NAT 网关。

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNatGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNatGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetDetectStates(self, request):
        """本接口(DescribeNetDetectStates)用于查询网络探测验证结果列表。

        :param request: Request instance for DescribeNetDetectStates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetDetectStates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetDetectStatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetDetects(self, request):
        """本接口（DescribeNetDetects）用于查询网络探测列表。

        :param request: Request instance for DescribeNetDetects.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetDetects", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetDetectsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkAccountType(self, request):
        """判断用户在网络侧的用户类型，如标准（带宽上移），传统（非上移）。

        :param request: Request instance for DescribeNetworkAccountType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAccountTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAccountTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkAccountType", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkAccountTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkAclQuintupleEntries(self, request):
        """本接口（DescribeNetworkAclQuintupleEntries）查询入方向或出方向网络ACL五元组条目列表。

        :param request: Request instance for DescribeNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkAcls(self, request):
        """本接口（DescribeNetworkAcls）用于查询网络ACL列表。

        :param request: Request instance for DescribeNetworkAcls.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkAcls", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkAclsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkInterfaceLimit(self, request):
        """本接口（DescribeNetworkInterfaceLimit）根据CVM实例ID或弹性网卡ID查询弹性网卡配额，返回该CVM实例或弹性网卡能绑定的弹性网卡配额，以及弹性网卡可以分配的IP配额。

        :param request: Request instance for DescribeNetworkInterfaceLimit.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkInterfaceLimit", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkInterfaceLimitResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeNetworkInterfaces(self, request):
        """本接口（DescribeNetworkInterfaces）用于查询弹性网卡列表。

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeNetworkInterfaces", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeNetworkInterfacesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNatGatewayDestinationIpPortTranslationNatRules(self, request):
        """本接口（DescribePrivateNatGatewayDestinationIpPortTranslationNatRules）用于查询私网NAT网关目的端口转换规则

        :param request: Request instance for DescribePrivateNatGatewayDestinationIpPortTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayDestinationIpPortTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayDestinationIpPortTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNatGatewayDestinationIpPortTranslationNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNatGatewayDestinationIpPortTranslationNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNatGatewayLimits(self, request):
        """本接口（DescribePrivateNatGatewayLimits）用于查询可创建的私网NAT网关配额数量

        :param request: Request instance for DescribePrivateNatGatewayLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNatGatewayLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNatGatewayLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNatGatewayRegions(self, request):
        """本接口（DescribePrivateNatGatewayRegions）用于查询查询私网NAT网关可支持地域

        :param request: Request instance for DescribePrivateNatGatewayRegions.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayRegionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayRegionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNatGatewayRegions", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNatGatewayRegionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNatGatewayTranslationAclRules(self, request):
        """本接口（DescribePrivateNatGatewayTranslationAclRules）用于查询私网NAT网关源端转换访问控制规则

        :param request: Request instance for DescribePrivateNatGatewayTranslationAclRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayTranslationAclRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayTranslationAclRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNatGatewayTranslationAclRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNatGatewayTranslationAclRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNatGatewayTranslationNatRules(self, request):
        """本接口（DescribePrivateNatGatewayTranslationNatRules）用于查询私网NAT网关源端转换规则

        :param request: Request instance for DescribePrivateNatGatewayTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewayTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNatGatewayTranslationNatRules", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNatGatewayTranslationNatRulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribePrivateNatGateways(self, request):
        """本接口（DescribePrivateNatGateways）用于查询私网NAT网关

        :param request: Request instance for DescribePrivateNatGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribePrivateNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribePrivateNatGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribePrivateNatGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeProductQuota(self, request):
        """本接口（DescribeProductQuota）用于查询网络产品的配额信息。

        :param request: Request instance for DescribeProductQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeProductQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeProductQuotaResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeProductQuota", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeProductQuotaResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeReserveIpAddresses(self, request):
        """查询内网保留 IP

        :param request: Request instance for DescribeReserveIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeReserveIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeReserveIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeReserveIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeReserveIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteConflicts(self, request):
        """本接口（DescribeRouteConflicts）用于查询自定义路由策略与云联网路由策略冲突列表。

        :param request: Request instance for DescribeRouteConflicts.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteConflictsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteConflictsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteConflicts", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteConflictsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteList(self, request):
        """本接口（DescribeRouteList）用于查询路由条目列表。

        :param request: Request instance for DescribeRouteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTableAssociatedInstances(self, request):
        """本接口（DescribeRouteTableAssociatedInstances）用于查询指定的云联网关联的实例所绑定的路由表信息。

        :param request: Request instance for DescribeRouteTableAssociatedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTableAssociatedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTableAssociatedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTableAssociatedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteTableAssociatedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTableSelectionPolicies(self, request):
        """本接口（DescribeRouteTableSelectionPolicies）用于查询云联网路由表选择策略。

        :param request: Request instance for DescribeRouteTableSelectionPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTableSelectionPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTableSelectionPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTableSelectionPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteTableSelectionPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRouteTables(self, request):
        """本接口（DescribeRouteTables）用于查询路由表。

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeRoutes(self, request):
        """本接口（DescribeRoutes）用于查询路由列表。

        :param request: Request instance for DescribeRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupAssociationStatistics(self, request):
        """本接口（DescribeSecurityGroupAssociationStatistics）用于查询安全组关联的实例统计。

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupAssociationStatistics", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupAssociationStatisticsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupLimits(self, request):
        """本接口(DescribeSecurityGroupLimits)用于查询用户安全组配额。

        :param request: Request instance for DescribeSecurityGroupLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupPolicies(self, request):
        """本接口（DescribeSecurityGroupPolicies）用于查询安全组规则。

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroupReferences(self, request):
        """本接口（DescribeSecurityGroupReferences）用于查询安全组被引用信息。

        :param request: Request instance for DescribeSecurityGroupReferences.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroupReferences", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupReferencesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSecurityGroups(self, request):
        """本接口（DescribeSecurityGroups）用于查询安全组。

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceTemplateGroups(self, request):
        """本接口（DescribeServiceTemplateGroups）用于查询协议端口模板集合。

        :param request: Request instance for DescribeServiceTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceTemplateGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceTemplateGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeServiceTemplates(self, request):
        """本接口（DescribeServiceTemplates）用于查询协议端口模板。

        :param request: Request instance for DescribeServiceTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeServiceTemplates", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeServiceTemplatesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSgSnapshotFileContent(self, request):
        """本接口（DescribeSgSnapshotFileContent）用于查询安全组快照文件内容。

        :param request: Request instance for DescribeSgSnapshotFileContent.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSgSnapshotFileContentRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSgSnapshotFileContentResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSgSnapshotFileContent", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSgSnapshotFileContentResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotAttachedInstances(self, request):
        """本接口（DescribeSnapshotAttachedInstances）用于查询快照策略关联实例列表。

        :param request: Request instance for DescribeSnapshotAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotAttachedInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotAttachedInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotFiles(self, request):
        """本接口（DescribeSnapshotFiles）用于查询快照文件。

        :param request: Request instance for DescribeSnapshotFiles.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotFilesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotFilesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotFiles", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotFilesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSnapshotPolicies(self, request):
        """本接口（DescribeSnapshotPolicies）用于查询快照策略。

        :param request: Request instance for DescribeSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSpecificTrafficPackageUsedDetails(self, request):
        """本接口 (DescribeSpecificTrafficPackageUsedDetails) 用于查询指定 共享流量包 的用量明细。

        :param request: Request instance for DescribeSpecificTrafficPackageUsedDetails.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSpecificTrafficPackageUsedDetailsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSpecificTrafficPackageUsedDetailsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSpecificTrafficPackageUsedDetails", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSpecificTrafficPackageUsedDetailsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnetResourceDashboard(self, request):
        """本接口(DescribeSubnetResourceDashboard)用于查看Subnet资源信息。

        :param request: Request instance for DescribeSubnetResourceDashboard.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetResourceDashboardRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetResourceDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnetResourceDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetResourceDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeSubnets(self, request):
        """本接口（DescribeSubnets）用于查询子网列表。

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTaskResult(self, request):
        """查询EIP异步任务执行结果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTemplateLimits(self, request):
        """本接口（DescribeTemplateLimits）用于查询参数模板配额列表。

        :param request: Request instance for DescribeTemplateLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTemplateLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTemplateLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTemplateLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTemplateLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTenantCcns(self, request):
        """本接口（DescribeTenantCcns）用于获取要锁定的云联网实例列表。
        该接口一般用来封禁出口限速的云联网实例, 目前联通内部运营系统通过云API调用, 因为出口限速无法按地域间封禁, 只能按更粗的云联网实例粒度封禁, 如果是地域间限速, 一般可以通过更细的限速实例粒度封禁（DescribeCrossBorderCcnRegionBandwidthLimits）
        如有需要, 可以封禁任意云联网实例, 可接入到内部运营系统

        :param request: Request instance for DescribeTenantCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTenantCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTenantCcnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTenantCcns", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTenantCcnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrafficMirrors(self, request):
        """本接口（DescribeTrafficMirrors）用于查询流量镜像实例信息。

        :param request: Request instance for DescribeTrafficMirrors.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficMirrorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficMirrorsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrafficMirrors", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrafficMirrorsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrafficPackages(self, request):
        """本接口 (DescribeTrafficPackages)  用于查询共享流量包详细信息，包括共享流量包唯一标识ID，名称，流量使用信息等

        :param request: Request instance for DescribeTrafficPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficPackagesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrafficPackages", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrafficPackagesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeTrafficQosPolicy(self, request):
        """查询流量调度规则

        :param request: Request instance for DescribeTrafficQosPolicy.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficQosPolicyRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTrafficQosPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeTrafficQosPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeTrafficQosPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeUsedIpAddress(self, request):
        """本接口(DescribeUsedIpAddress)用于查询Subnet或者Vpc内的ip的使用情况，
        如ip被占用，返回占用ip的资源类别与id；如未被占用，返回空值

        :param request: Request instance for DescribeUsedIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeUsedIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeUsedIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeUsedIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeUsedIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcEndPoint(self, request):
        """本接口（DescribeVpcEndPoint）用于查询终端节点列表。

        :param request: Request instance for DescribeVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcEndPoint", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcEndPointResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcEndPointService(self, request):
        """本接口（DescribeVpcEndPointService）用于查询终端节点服务列表。

        :param request: Request instance for DescribeVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcEndPointService", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcEndPointServiceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcEndPointServiceWhiteList(self, request):
        """本接口（DescribeVpcEndPointServiceWhiteList）用于查询终端节点服务的服务白名单列表。

        :param request: Request instance for DescribeVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcInstances(self, request):
        """本接口（DescribeVpcInstances）用于查询VPC下的云主机实例列表。

        :param request: Request instance for DescribeVpcInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcIpv6Addresses(self, request):
        """本接口（DescribeVpcIpv6Addresses）用于查询 `VPC` `IPv6` 信息。
        只能查询已使用的`IPv6`信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。

        :param request: Request instance for DescribeVpcIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcLimits(self, request):
        """本接口（DescribeVpcLimits）用于获取私有网络配额，部分私有网络的配额有地域属性。
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

        :param request: Request instance for DescribeVpcLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcLimits", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcPeeringConnections(self, request):
        """查询私有网络对等连接。

        :param request: Request instance for DescribeVpcPeeringConnections.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPeeringConnectionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPeeringConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcPeeringConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcPeeringConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcPrivateIpAddresses(self, request):
        """本接口（DescribeVpcPrivateIpAddresses）用于查询VPC内网IP信息。<br />
        只能查询已使用的IP信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。

        :param request: Request instance for DescribeVpcPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcResourceDashboard(self, request):
        """本接口(DescribeVpcResourceDashboard)用于查看VPC资源信息。

        :param request: Request instance for DescribeVpcResourceDashboard.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcResourceDashboard", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcResourceDashboardResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcTaskResult(self, request):
        """本接口（DescribeVpcTaskResult）用于查询VPC任务执行结果。

        :param request: Request instance for DescribeVpcTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcTaskResultResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcTaskResult", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcTaskResultResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpcs(self, request):
        """本接口（DescribeVpcs）用于查询私有网络列表。

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpcs", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnConnections(self, request):
        """本接口（DescribeVpnConnections）用于查询VPN通道列表。

        :param request: Request instance for DescribeVpnConnections.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnConnections", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnConnectionsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGatewayCcnRoutes(self, request):
        """本接口（DescribeVpnGatewayCcnRoutes）用于查询VPN网关云联网路由。

        :param request: Request instance for DescribeVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGatewayRoutes(self, request):
        """本接口（DescribeVpnGatewayRoutes）用于查询VPN网关路由。

        :param request: Request instance for DescribeVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGatewaySslClients(self, request):
        """本接口（DescribeVpnGatewaySslClients）用于查询SSL-VPN-CLIENT 列表。

        :param request: Request instance for DescribeVpnGatewaySslClients.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslClientsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslClientsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGatewaySslClients", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewaySslClientsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGatewaySslServers(self, request):
        """本接口（DescribeVpnGatewaySslServers）用于查询SSL-VPN SERVER 列表信息。

        :param request: Request instance for DescribeVpnGatewaySslServers.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslServersRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslServersResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGatewaySslServers", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewaySslServersResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DescribeVpnGateways(self, request):
        """本接口（DescribeVpnGateways）用于查询VPN网关列表。

        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DescribeVpnGateways", params, headers=headers)
            response = json.loads(body)
            model = models.DescribeVpnGatewaysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachCcnInstances(self, request):
        """本接口（DetachCcnInstances）用于从云联网实例中解关联指定的网络实例。<br />
        解关联网络实例后，相应的路由策略会一并删除。

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachClassicLinkVpc(self, request):
        """本接口(DetachClassicLinkVpc)用于删除私有网络和基础网络设备互通。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DetachClassicLinkVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachClassicLinkVpcResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachClassicLinkVpc", params, headers=headers)
            response = json.loads(body)
            model = models.DetachClassicLinkVpcResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachNetworkInterface(self, request):
        """本接口（DetachNetworkInterface）用于弹性网卡解绑云服务器。
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.DetachNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DetachSnapshotInstances(self, request):
        """本接口（DetachSnapshotInstances）用于快照策略解关联实例。

        :param request: Request instance for DetachSnapshotInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachSnapshotInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachSnapshotInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DetachSnapshotInstances", params, headers=headers)
            response = json.loads(body)
            model = models.DetachSnapshotInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableCcnRoutes(self, request):
        """本接口（DisableCcnRoutes）用于禁用已经启用的云联网（CCN）路由。

        :param request: Request instance for DisableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DisableCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableFlowLogs(self, request):
        """本接口（DisableFlowLogs）用于停止流日志。

        :param request: Request instance for DisableFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.DisableFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableGatewayFlowMonitor(self, request):
        """本接口（DisableGatewayFlowMonitor）用于关闭网关流量监控。

        :param request: Request instance for DisableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableGatewayFlowMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.DisableGatewayFlowMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableRoutes(self, request):
        """本接口（DisableRoutes）用于禁用已启用的子网路由

        :param request: Request instance for DisableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.DisableRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableSnapshotPolicies(self, request):
        """本接口（DisableSnapshotPolicies）用于停用快照策略。

        :param request: Request instance for DisableSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.DisableSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisableVpnGatewaySslClientCert(self, request):
        """禁用SSL-VPN-CLIENT 证书

        :param request: Request instance for DisableVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisableVpnGatewaySslClientCert", params, headers=headers)
            response = json.loads(body)
            model = models.DisableVpnGatewaySslClientCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateAddress(self, request):
        """本接口 (DisassociateAddress) 用于解绑[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 支持CVM实例，弹性网卡上的EIP解绑
        * 不支持NAT上的EIP解绑。NAT上的EIP解绑请参考[DisassociateNatGatewayAddress](https://cloud.tencent.com/document/api/215/36716)
        * 只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateDhcpIpWithAddressIp(self, request):
        """本接口（DisassociateDhcpIpWithAddressIp）用于将DhcpIp已绑定的弹性公网IP（EIP）解除绑定。<br />
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for DisassociateDhcpIpWithAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateDhcpIpWithAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateDhcpIpWithAddressIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateDhcpIpWithAddressIp", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateDhcpIpWithAddressIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateDirectConnectGatewayNatGateway(self, request):
        """将专线网关与NAT网关解绑，解绑之后，专线网关将不能通过NAT网关访问公网

        :param request: Request instance for DisassociateDirectConnectGatewayNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateDirectConnectGatewayNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateDirectConnectGatewayNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateDirectConnectGatewayNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateDirectConnectGatewayNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateIPv6Address(self, request):
        """本接口（DisassociateIPv6Address）用于解绑弹性公网 IPv6（简称EIPv6）实例。

        - 支持对 CVM、弹性网卡绑定的 EIPv6 实例进行解绑操作。
        - 只有状态为 BIND 和 BIND_ENI 的 EIPv6 实例才能进行解绑操作。

        :param request: Request instance for DisassociateIPv6Address.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateIPv6AddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateIPv6AddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateIPv6Address", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateIPv6AddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateNatGatewayAddress(self, request):
        """本接口（DisassociateNatGatewayAddress）用于NAT网关解绑弹性IP。

        :param request: Request instance for DisassociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateNatGatewayAddress", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateNatGatewayAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateNetworkAclSubnets(self, request):
        """本接口（DisassociateNetworkAclSubnets）用于网络ACL解关联VPC下的子网。

        :param request: Request instance for DisassociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateNetworkAclSubnets", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateNetworkAclSubnetsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateNetworkInterfaceSecurityGroups(self, request):
        """本接口（DisassociateNetworkInterfaceSecurityGroups）用于弹性网卡解绑安全组。支持弹性网卡完全解绑安全组。

        :param request: Request instance for DisassociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateNetworkInterfaceSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateNetworkInterfaceSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DisassociateVpcEndPointSecurityGroups(self, request):
        """本接口（DisassociateVpcEndPointSecurityGroups）用于终端节点解绑安全组。

        :param request: Request instance for DisassociateVpcEndPointSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateVpcEndPointSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateVpcEndPointSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DisassociateVpcEndPointSecurityGroups", params, headers=headers)
            response = json.loads(body)
            model = models.DisassociateVpcEndPointSecurityGroupsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadCustomerGatewayConfiguration(self, request):
        """本接口（DownloadCustomerGatewayConfiguration）用于下载VPN通道配置。

        :param request: Request instance for DownloadCustomerGatewayConfiguration.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadCustomerGatewayConfiguration", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadCustomerGatewayConfigurationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def DownloadVpnGatewaySslClientCert(self, request):
        """本接口（DownloadVpnGatewaySslClientCert）用于下载SSL-VPN-CLIENT 客户端证书。

        :param request: Request instance for DownloadVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("DownloadVpnGatewaySslClientCert", params, headers=headers)
            response = json.loads(body)
            model = models.DownloadVpnGatewaySslClientCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableCcnRoutes(self, request):
        """本接口（EnableCcnRoutes）用于启用已经加入云联网（CCN）的路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。

        :param request: Request instance for EnableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.EnableCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableFlowLogs(self, request):
        """本接口（EnableFlowLogs）用于启动流日志。

        :param request: Request instance for EnableFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableFlowLogsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableFlowLogs", params, headers=headers)
            response = json.loads(body)
            model = models.EnableFlowLogsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableGatewayFlowMonitor(self, request):
        """本接口（EnableGatewayFlowMonitor）用于开启网关流量监控。

        :param request: Request instance for EnableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableGatewayFlowMonitor", params, headers=headers)
            response = json.loads(body)
            model = models.EnableGatewayFlowMonitorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableRoutes(self, request):
        """本接口（EnableRoutes）用于启用已禁用的子网路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。

        :param request: Request instance for EnableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.EnableRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableSnapshotPolicies(self, request):
        """本接口（EnableSnapshotPolicies）用于启用快照策略。

        :param request: Request instance for EnableSnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableSnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableSnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableSnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.EnableSnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableVpcEndPointConnect(self, request):
        """本接口（EnableVpcEndPointConnect）用于是否接受终端节点连接请求。

        :param request: Request instance for EnableVpcEndPointConnect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableVpcEndPointConnectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableVpcEndPointConnectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableVpcEndPointConnect", params, headers=headers)
            response = json.loads(body)
            model = models.EnableVpcEndPointConnectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def EnableVpnGatewaySslClientCert(self, request):
        """本接口（EnableVpnGatewaySslClientCert）用于启用SSL-VPN-CLIENT 证书。

        :param request: Request instance for EnableVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("EnableVpnGatewaySslClientCert", params, headers=headers)
            response = json.loads(body)
            model = models.EnableVpnGatewaySslClientCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GenerateVpnConnectionDefaultHealthCheckIp(self, request):
        """本接口（GenerateVpnConnectionDefaultHealthCheckIp）用于获取一对VPN通道健康检查地址。

        :param request: Request instance for GenerateVpnConnectionDefaultHealthCheckIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.GenerateVpnConnectionDefaultHealthCheckIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.GenerateVpnConnectionDefaultHealthCheckIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GenerateVpnConnectionDefaultHealthCheckIp", params, headers=headers)
            response = json.loads(body)
            model = models.GenerateVpnConnectionDefaultHealthCheckIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def GetCcnRegionBandwidthLimits(self, request):
        """本接口（GetCcnRegionBandwidthLimits）用于查询云联网相关地域带宽信息，其中预付费模式的云联网仅支持地域间限速，后付费模式的云联网支持地域间限速和地域出口限速。

        :param request: Request instance for GetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.GetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.GetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("GetCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.GetCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HaVipAssociateAddressIp(self, request):
        """本接口（HaVipAssociateAddressIp）用于高可用虚拟IP（HAVIP）绑定弹性公网IP（EIP）。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for HaVipAssociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HaVipAssociateAddressIp", params, headers=headers)
            response = json.loads(body)
            model = models.HaVipAssociateAddressIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def HaVipDisassociateAddressIp(self, request):
        """本接口（HaVipDisassociateAddressIp）用于将高可用虚拟IP（HAVIP）已绑定的弹性公网IP（EIP）解除绑定。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for HaVipDisassociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("HaVipDisassociateAddressIp", params, headers=headers)
            response = json.loads(body)
            model = models.HaVipDisassociateAddressIpResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquirePriceCreateDirectConnectGateway(self, request):
        """本接口（DescribePriceCreateDirectConnectGateway）用于创建专线网关询价。

        :param request: Request instance for InquirePriceCreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquirePriceCreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquirePriceCreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquirePriceCreateDirectConnectGateway", params, headers=headers)
            response = json.loads(body)
            model = models.InquirePriceCreateDirectConnectGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceAllocateAddresses(self, request):
        """本接口（InquiryPriceAllocateAddresses）用于新购弹性公网IP询价。

        :param request: Request instance for InquiryPriceAllocateAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceAllocateAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceAllocateAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceAllocateAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceAllocateAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceCreateVpnGateway(self, request):
        """本接口（InquiryPriceCreateVpnGateway）用于创建VPN网关询价。

        :param request: Request instance for InquiryPriceCreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceCreateVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceCreateVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceModifyAddressesBandwidth(self, request):
        """EIP修改带宽询价

        :param request: Request instance for InquiryPriceModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceModifyAddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceModifyAddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewAddresses(self, request):
        """本接口（InquiryPriceRenewAddresses）用于续费预付费弹性公网IP询价。

        :param request: Request instance for InquiryPriceRenewAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceRenewVpnGateway(self, request):
        """本接口（InquiryPriceRenewVpnGateway）用于续费VPN网关询价。目前仅支持IPSEC类型网关的询价。

        :param request: Request instance for InquiryPriceRenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceRenewVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceRenewVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def InquiryPriceResetVpnGatewayInternetMaxBandwidth(self, request):
        """本接口（InquiryPriceResetVpnGatewayInternetMaxBandwidth）用于调整VPN网关带宽上限询价。

        :param request: Request instance for InquiryPriceResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("InquiryPriceResetVpnGatewayInternetMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockCcnBandwidths(self, request):
        """本接口（LockCcnBandwidths）用户锁定云联网限速实例。
        该接口一般用来封禁地域间限速的云联网实例下的限速实例, 目前联通内部运营系统通过云API调用, 如果是出口限速, 一般使用更粗的云联网实例粒度封禁（LockCcns）。
        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统。

        :param request: Request instance for LockCcnBandwidths.
        :type request: :class:`tencentcloud.vpc.v20170312.models.LockCcnBandwidthsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.LockCcnBandwidthsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockCcnBandwidths", params, headers=headers)
            response = json.loads(body)
            model = models.LockCcnBandwidthsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def LockCcns(self, request):
        """本接口（LockCcns）用于锁定云联网实例

        该接口一般用来封禁出口限速的云联网实例, 目前联通内部运营系统通过云API调用, 因为出口限速无法按地域间封禁, 只能按更粗的云联网实例粒度封禁, 如果是地域间限速, 一般可以通过更细的限速实例粒度封禁（LockCcnBandwidths）

        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统

        :param request: Request instance for LockCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.LockCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.LockCcnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("LockCcns", params, headers=headers)
            response = json.loads(body)
            model = models.LockCcnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigrateNetworkInterface(self, request):
        """本接口（MigrateNetworkInterface）用于弹性网卡迁移。
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigrateNetworkInterface", params, headers=headers)
            response = json.loads(body)
            model = models.MigrateNetworkInterfaceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def MigratePrivateIpAddress(self, request):
        """本接口（MigratePrivateIpAddress）用于弹性网卡内网IP迁移。
        * 该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。
        * 迁移前后的弹性网卡必须在同一个子网内。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for MigratePrivateIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigratePrivateIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("MigratePrivateIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.MigratePrivateIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressAttribute(self, request):
        """本接口 (ModifyAddressAttribute) 用于修改[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的名称。

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressInternetChargeType(self, request):
        """该接口用于调整具有带宽属性弹性公网IP的网络计费模式
        * 支持BANDWIDTH_PREPAID_BY_MONTH和TRAFFIC_POSTPAID_BY_HOUR两种网络计费模式之间的切换。
        * 每个弹性公网IP支持调整两次，次数超出则无法调整。

        :param request: Request instance for ModifyAddressInternetChargeType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressInternetChargeTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressInternetChargeTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressInternetChargeType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressInternetChargeTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressTemplateAttribute(self, request):
        """本接口（ModifyAddressTemplateAttribute）用于修改IP地址模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for ModifyAddressTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressTemplateAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressTemplateAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressTemplateGroupAttribute(self, request):
        """本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for ModifyAddressTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressTemplateGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressTemplateGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressesBandwidth(self, request):
        """本接口（ModifyAddressesBandwidth）用于调整[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)(简称EIP)带宽，支持后付费EIP, 预付费EIP和带宽包EIP

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAddressesRenewFlag(self, request):
        """调整EIP续费标识

        :param request: Request instance for ModifyAddressesRenewFlag.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesRenewFlagRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAddressesRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAddressesRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyAssistantCidr(self, request):
        """本接口（ModifyAssistantCidr）用于批量修改辅助CIDR，支持新增和删除。

        :param request: Request instance for ModifyAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyAssistantCidr", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyAssistantCidrResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBandwidthPackageAttribute(self, request):
        """接口用于修改带宽包属性，包括带宽包名字等

        :param request: Request instance for ModifyBandwidthPackageAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBandwidthPackageAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBandwidthPackageAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyBandwidthPackageBandwidth(self, request):
        """接口用于调整[共享带宽包](https://cloud.tencent.com/document/product/684/15245)(BWP)带宽

        :param request: Request instance for ModifyBandwidthPackageBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyBandwidthPackageBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyBandwidthPackageBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnAttachedInstancesAttribute(self, request):
        """修改CCN关联实例属性，目前仅修改备注description

        :param request: Request instance for ModifyCcnAttachedInstancesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttachedInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttachedInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnAttachedInstancesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnAttachedInstancesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnAttribute(self, request):
        """本接口（ModifyCcnAttribute）用于修改云联网（CCN）的相关属性。

        :param request: Request instance for ModifyCcnAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnRegionBandwidthLimitsType(self, request):
        """本接口（ModifyCcnRegionBandwidthLimitsType）用于修改后付费云联网实例修改带宽限速策略。

        :param request: Request instance for ModifyCcnRegionBandwidthLimitsType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnRegionBandwidthLimitsType", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnRegionBandwidthLimitsTypeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCcnRouteTables(self, request):
        """该接口用于修改云联网路由表名称和备注。

        :param request: Request instance for ModifyCcnRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRouteTablesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCcnRouteTables", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCcnRouteTablesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdcLDCXAttribute(self, request):
        """修改 IDC通道信息

        :param request: Request instance for ModifyCdcLDCXAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCdcLDCXAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCdcLDCXAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdcLDCXAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdcLDCXAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCdcNetPlaneAttribute(self, request):
        """修改虚拟连接

        :param request: Request instance for ModifyCdcNetPlaneAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCdcNetPlaneAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCdcNetPlaneAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCdcNetPlaneAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCdcNetPlaneAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyCustomerGatewayAttribute(self, request):
        """本接口（ModifyCustomerGatewayAttribute）用于修改对端网关信息。

        :param request: Request instance for ModifyCustomerGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyCustomerGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyCustomerGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDhcpIpAttribute(self, request):
        """本接口（ModifyDhcpIpAttribute）用于修改DhcpIp属性

        :param request: Request instance for ModifyDhcpIpAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyDhcpIpAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyDhcpIpAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDhcpIpAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDhcpIpAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyDirectConnectGatewayAttribute(self, request):
        """本接口（ModifyDirectConnectGatewayAttribute）用于修改专线网关属性

        :param request: Request instance for ModifyDirectConnectGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyDirectConnectGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyDirectConnectGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyFlowLogAttribute(self, request):
        """本接口（ModifyFlowLogAttribute）用于修改流日志属性。

        :param request: Request instance for ModifyFlowLogAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyFlowLogAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyFlowLogAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyGatewayFlowQos(self, request):
        """本接口（ModifyGatewayFlowQos）用于调整网关流控带宽。

        :param request: Request instance for ModifyGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyGatewayFlowQos", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyGatewayFlowQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHaVipAttribute(self, request):
        """本接口（ModifyHaVipAttribute）用于修改高可用虚拟IP（HAVIP）属性。

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHaVipAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHaVipAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHighPriorityRouteAttribute(self, request):
        """修改高优路由表条目属性。

        :param request: Request instance for ModifyHighPriorityRouteAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHighPriorityRouteAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHighPriorityRouteAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHighPriorityRouteAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHighPriorityRouteAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHighPriorityRouteECMPAlgorithm(self, request):
        """修改高优路由表 HASH 策略。

        :param request: Request instance for ModifyHighPriorityRouteECMPAlgorithm.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHighPriorityRouteECMPAlgorithmRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHighPriorityRouteECMPAlgorithmResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHighPriorityRouteECMPAlgorithm", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHighPriorityRouteECMPAlgorithmResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyHighPriorityRouteTableAttribute(self, request):
        """修改高优路由表属性

        :param request: Request instance for ModifyHighPriorityRouteTableAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHighPriorityRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHighPriorityRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyHighPriorityRouteTableAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyHighPriorityRouteTableAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIPv6AddressesAttributes(self, request):
        """本接口（ModifyIPv6AddressesAttributes）用于修改弹性公网 IPv6（简称EIPv6）实例名称。

        - 支持对弹性公网 IPv6 和传统弹性公网 IPv6 实例名称进行修改。

        :param request: Request instance for ModifyIPv6AddressesAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesAttributesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIPv6AddressesAttributes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIPv6AddressesAttributesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIPv6AddressesBandwidth(self, request):
        """本接口（ModifyIPv6AddressesBandwidth）用于调整弹性公网 IPv6（简称EIPv6）实例的带宽上限。

        :param request: Request instance for ModifyIPv6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIPv6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIPv6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIPv6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIp6AddressesBandwidth(self, request):
        """本接口（ModifyIp6AddressesBandwidth）用于调整传统弹性公网 IPv6 实例的带宽上限。

        - 仅支持对传统弹性公网 IPv6 实例的带宽上限进行调整。
        - 如需调整弹性公网 IPv6 实例的带宽上限，请使用 ModifyIPv6AddressesBandwidth 接口。

        :param request: Request instance for ModifyIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIp6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIp6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIp6Rule(self, request):
        """该接口用于修改IPV6转换规则，当前仅支持修改转换规则名称，IPV4地址和IPV4端口号

        :param request: Request instance for ModifyIp6Rule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6RuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6RuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIp6Rule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIp6RuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIp6Translator(self, request):
        """该接口用于修改IP6转换实例属性，当前仅支持修改实例名称。

        :param request: Request instance for ModifyIp6Translator.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6TranslatorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6TranslatorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIp6Translator", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIp6TranslatorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyIpv6AddressesAttribute(self, request):
        """本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡内网IPv6地址属性。

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyIpv6AddressesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyIpv6AddressesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyLocalGateway(self, request):
        """本接口（ModifyLocalGateway）用于修改CDC的本地网关。

        :param request: Request instance for ModifyLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyLocalGateway", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyLocalGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatGatewayAttribute(self, request):
        """本接口（ModifyNatGatewayAttribute）用于修改NAT网关的属性。

        :param request: Request instance for ModifyNatGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（ModifyNatGatewayDestinationIpPortTranslationNatRule）用于修改NAT网关端口转发规则。

        :param request: Request instance for ModifyNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNatGatewaySourceIpTranslationNatRule(self, request):
        """本接口（ModifyNatGatewaySourceIpTranslationNatRule）用于修改NAT网关SNAT转发规则。

        :param request: Request instance for ModifyNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNatGatewaySourceIpTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNatGatewaySourceIpTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetDetect(self, request):
        """本接口(ModifyNetDetect)用于修改网络探测参数。

        :param request: Request instance for ModifyNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetDetect", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetDetectResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAclAttribute(self, request):
        """本接口（ModifyNetworkAclAttribute）用于修改网络ACL属性。

        :param request: Request instance for ModifyNetworkAclAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAclAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAclAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAclEntries(self, request):
        """本接口（ModifyNetworkAclEntries）用于修改（包括添加和删除）网络ACL的入站规则和出站规则。在NetworkAclEntrySet参数中：
        * 若同时传入入站规则和出站规则，则重置原有的入站规则和出站规则，并分别导入传入的规则。
        * 若仅传入入站规则，则仅重置原有的入站规则，并导入传入的规则，不影响原有的出站规则（若仅传入出站规则，处理方式类似入站方向）。

        :param request: Request instance for ModifyNetworkAclEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAclEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAclEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkAclQuintupleEntries(self, request):
        """本接口（ModifyNetworkAclQuintupleEntries）用于修改网络ACL五元组的入站规则和出站规则。在NetworkAclQuintupleEntrySet参数中：NetworkAclQuintupleEntry需要提供NetworkAclQuintupleEntryId。

        :param request: Request instance for ModifyNetworkAclQuintupleEntries.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclQuintupleEntriesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclQuintupleEntriesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkAclQuintupleEntries", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkAclQuintupleEntriesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkInterfaceAttribute(self, request):
        """本接口（ModifyNetworkInterfaceAttribute）用于修改弹性网卡属性。

        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkInterfaceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkInterfaceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyNetworkInterfaceQos(self, request):
        """本接口（ModifyNetworkInterfaceQos）用于修改弹性网卡服务质量。

        :param request: Request instance for ModifyNetworkInterfaceQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceQosResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyNetworkInterfaceQos", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyNetworkInterfaceQosResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateIpAddressesAttribute(self, request):
        """本接口（ModifyPrivateIpAddressesAttribute）用于修改弹性网卡内网IP属性。

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateIpAddressesAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateIpAddressesAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateNatGatewayAttribute(self, request):
        """本接口（ModifyPrivateNatGatewayAttribute）用于修改私网NAT网关属性

        :param request: Request instance for ModifyPrivateNatGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateNatGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateNatGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule）用于修改私网NAT网关目的端口转换规则

        :param request: Request instance for ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateNatGatewayDestinationIpPortTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateNatGatewayDestinationIpPortTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateNatGatewayTranslationAclRule(self, request):
        """本接口（ModifyPrivateNatGatewayTranslationAclRule）用于修改私网NAT网关源端转换访问控制规则

        :param request: Request instance for ModifyPrivateNatGatewayTranslationAclRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayTranslationAclRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayTranslationAclRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateNatGatewayTranslationAclRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateNatGatewayTranslationAclRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyPrivateNatGatewayTranslationNatRule(self, request):
        """本接口（ModifyPrivateNatGatewayTranslationNatRule）用于修改私网NAT网关源端转换规则

        :param request: Request instance for ModifyPrivateNatGatewayTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateNatGatewayTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyPrivateNatGatewayTranslationNatRule", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyPrivateNatGatewayTranslationNatRuleResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyReserveIpAddress(self, request):
        """修改内网保留 IP

        :param request: Request instance for ModifyReserveIpAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyReserveIpAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyReserveIpAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyReserveIpAddress", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyReserveIpAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRouteTableAttribute(self, request):
        """本接口（ModifyRouteTableAttribute）用于修改路由表（RouteTable）属性。

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRouteTableAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRouteTableAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyRouteTableSelectionPolicies(self, request):
        """该接口用于编辑云联网路由表选择策略

        :param request: Request instance for ModifyRouteTableSelectionPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableSelectionPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableSelectionPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyRouteTableSelectionPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyRouteTableSelectionPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupAttribute(self, request):
        """本接口（ModifySecurityGroupAttribute）用于修改安全组（SecurityGroupPolicy）属性。

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySecurityGroupPolicies(self, request):
        """本接口（ModifySecurityGroupPolicies）用于重置安全组出站和入站规则（SecurityGroupPolicy）。

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

        :param request: Request instance for ModifySecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceTemplateAttribute(self, request):
        """本接口（ModifyServiceTemplateAttribute）用于修改协议端口模板。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for ModifyServiceTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceTemplateAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceTemplateAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyServiceTemplateGroupAttribute(self, request):
        """本接口（ModifyServiceTemplateGroupAttribute）用于修改协议端口模板集合。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for ModifyServiceTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyServiceTemplateGroupAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyServiceTemplateGroupAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySnapshotPolicies(self, request):
        """本接口（ModifySnapshotPolicies）用于修改快照策略。

        :param request: Request instance for ModifySnapshotPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySnapshotPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySnapshotPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySnapshotPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySnapshotPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifySubnetAttribute(self, request):
        """本接口（ModifySubnetAttribute）用于修改子网属性。

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifySubnetAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifySubnetAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTemplateMember(self, request):
        """修改模板对象中的IP地址、协议端口、IP地址组、协议端口组。

        :param request: Request instance for ModifyTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTemplateMember", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTemplateMemberResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyTrafficMirrorAttribute(self, request):
        """本接口（ModifyTrafficMirrorAttribute）用于修改流量镜像实例属性。
        注意：只支持修改名字和描述信息

        :param request: Request instance for ModifyTrafficMirrorAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyTrafficMirrorAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyTrafficMirrorAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyTrafficMirrorAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyTrafficMirrorAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcAttribute(self, request):
        """本接口（ModifyVpcAttribute）用于修改私有网络（VPC）的相关属性。

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcEndPointAttribute(self, request):
        """本接口（ModifyVpcEndPointAttribute）用于修改终端节点属性。

        :param request: Request instance for ModifyVpcEndPointAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcEndPointAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcEndPointAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcEndPointServiceAttribute(self, request):
        """本接口（ModifyVpcEndPointServiceAttribute）用于修改终端节点服务属性。

        :param request: Request instance for ModifyVpcEndPointServiceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcEndPointServiceAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcEndPointServiceAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcEndPointServiceWhiteList(self, request):
        """本接口（ModifyVpcEndPointServiceWhiteList）用于修改终端节点服务白名单属性。

        :param request: Request instance for ModifyVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcEndPointServiceWhiteList", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcEndPointServiceWhiteListResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpcPeeringConnection(self, request):
        """本接口（ModifyVpcPeeringConnection）用于修改私有网络对等连接属性。

        :param request: Request instance for ModifyVpcPeeringConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcPeeringConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcPeeringConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpcPeeringConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpcPeeringConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnConnectionAttribute(self, request):
        """本接口（ModifyVpnConnectionAttribute）用于修改VPN通道。

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnConnectionAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnConnectionAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayAttribute(self, request):
        """本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。

        :param request: Request instance for ModifyVpnGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayAttribute", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayAttributeResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayCcnRoutes(self, request):
        """本接口（ModifyVpnGatewayCcnRoutes）用于修改VPN网关云联网路由。

        :param request: Request instance for ModifyVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewayRoutes(self, request):
        """本接口（ModifyVpnGatewayRoutes）用于修改VPN路由是否启用。

        :param request: Request instance for ModifyVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewayRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewayRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewaySslClientCert(self, request):
        """更新SslVpnClient证书

        :param request: Request instance for ModifyVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewaySslClientCert", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewaySslClientCertResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ModifyVpnGatewaySslServer(self, request):
        """本接口用于修改 SSL-VPN 服务端属性

        :param request: Request instance for ModifyVpnGatewaySslServer.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewaySslServerRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewaySslServerResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ModifyVpnGatewaySslServer", params, headers=headers)
            response = json.loads(body)
            model = models.ModifyVpnGatewaySslServerResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def NotifyRoutes(self, request):
        """本接口（NotifyRoutes）用于路由表列表页操作增加“发布到云联网”，发布路由到云联网。

        :param request: Request instance for NotifyRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.NotifyRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.NotifyRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("NotifyRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.NotifyRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RefreshDirectConnectGatewayRouteToNatGateway(self, request):
        """刷新专线直连nat路由，更新nat到专线的路由表

        :param request: Request instance for RefreshDirectConnectGatewayRouteToNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RefreshDirectConnectGatewayRouteToNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RefreshDirectConnectGatewayRouteToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RefreshDirectConnectGatewayRouteToNatGateway", params, headers=headers)
            response = json.loads(body)
            model = models.RefreshDirectConnectGatewayRouteToNatGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectAttachCcnInstances(self, request):
        """本接口（RejectAttachCcnInstances）用于跨账号关联实例时，云联网所有者拒绝关联操作。

        :param request: Request instance for RejectAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectAttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.RejectAttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RejectVpcPeeringConnection(self, request):
        """本接口（RejectVpcPeeringConnection）用于驳回对等连接请求。

        :param request: Request instance for RejectVpcPeeringConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RejectVpcPeeringConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RejectVpcPeeringConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RejectVpcPeeringConnection", params, headers=headers)
            response = json.loads(body)
            model = models.RejectVpcPeeringConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseAddresses(self, request):
        """本接口 (ReleaseAddresses) 用于释放一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。
        * 只有状态为 UNBIND 的 EIP 才能进行释放操作。

        :param request: Request instance for ReleaseAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseIPv6Addresses(self, request):
        """本接口（ReleaseIPv6Addresses）用于释放一个或多个弹性公网IPv6（简称EIPv6）实例。

        - 支持对已申请到的弹性公网 IPv6 实例进行释放操作，如需再次使用，请重新申请。
        - 只有状态为 UNBIND 的 EIPv6 实例才能进行释放操作。

        :param request: Request instance for ReleaseIPv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseIPv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseIPv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIPv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIPv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReleaseIp6AddressesBandwidth(self, request):
        """本接口（ReleaseIp6AddressesBandwidth）用于为传统弹性公网 IPv6 实例关闭 IPv6 公网带宽。

        - 传统弹性公网 IPv6 实例关闭公网带宽后，仍具备 IPv6 内网通信能力。
        - 如需再次开通 IPv6 公网带宽，请使用 AllocateIp6AddressesBandwidth 接口进行开通。

        :param request: Request instance for ReleaseIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReleaseIp6AddressesBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ReleaseIp6AddressesBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveBandwidthPackageResources(self, request):
        """接口用于删除带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等

        :param request: Request instance for RemoveBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveBandwidthPackageResources", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveBandwidthPackageResourcesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RemoveIp6Rules(self, request):
        """1. 该接口用于删除IPV6转换规则
        2. 支持批量删除同一个转换实例下的多个转换规则

        :param request: Request instance for RemoveIp6Rules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveIp6RulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveIp6RulesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RemoveIp6Rules", params, headers=headers)
            response = json.loads(body)
            model = models.RemoveIp6RulesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewAddresses(self, request):
        """该接口用于续费包月带宽计费模式的弹性公网IP

        :param request: Request instance for RenewAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RenewAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RenewAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.RenewAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def RenewVpnGateway(self, request):
        """本接口（RenewVpnGateway）用于预付费（包年包月）VPN网关续费。目前只支持IPSEC网关。

        :param request: Request instance for RenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("RenewVpnGateway", params, headers=headers)
            response = json.loads(body)
            model = models.RenewVpnGatewayResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceCcnRouteTableBroadcastPolicys(self, request):
        """本接口(ReplaceCcnRouteTableBroadcastPolicys)用于替换云联网路由表路由传播策略。
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

        :param request: Request instance for ReplaceCcnRouteTableBroadcastPolicys.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceCcnRouteTableBroadcastPolicysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceCcnRouteTableBroadcastPolicysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceCcnRouteTableBroadcastPolicys", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceCcnRouteTableBroadcastPolicysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceCcnRouteTableInputPolicys(self, request):
        """本接口(ReplaceRouteTableInputPolicys)用于替换云联网路由表路由接收策略。
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

        :param request: Request instance for ReplaceCcnRouteTableInputPolicys.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceCcnRouteTableInputPolicysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceCcnRouteTableInputPolicysResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceCcnRouteTableInputPolicys", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceCcnRouteTableInputPolicysResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceDirectConnectGatewayCcnRoutes(self, request):
        """本接口（ReplaceDirectConnectGatewayCcnRoutes）根据路由ID（RouteId）修改指定的路由（Route），支持批量修改。

        :param request: Request instance for ReplaceDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceDirectConnectGatewayCcnRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceDirectConnectGatewayCcnRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceHighPriorityRouteTableAssociation(self, request):
        """替换高优路由表和子网绑定关系。

        :param request: Request instance for ReplaceHighPriorityRouteTableAssociation.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceHighPriorityRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceHighPriorityRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceHighPriorityRouteTableAssociation", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceHighPriorityRouteTableAssociationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceHighPriorityRoutes(self, request):
        """替换高优路由表条目信息。

        :param request: Request instance for ReplaceHighPriorityRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceHighPriorityRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceHighPriorityRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceHighPriorityRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceHighPriorityRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceRouteTableAssociation(self, request):
        """本接口（ReplaceRouteTableAssociation）用于修改子网（Subnet）关联的路由表（RouteTable）。
        * 一个子网只能关联一个路由表。

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceRouteTableAssociation", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceRouteTableAssociationResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceRoutes(self, request):
        """本接口（ReplaceRoutes）根据路由策略ID（RouteId）修改指定的路由策略（Route），支持批量修改。

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceSecurityGroupPolicies(self, request):
        """本接口（ReplaceSecurityGroupPolicies）用于批量修改安全组规则（SecurityGroupPolicy）。
        单个请求中只能替换单个方向的一条或多条规则, 必须要指定索引（PolicyIndex）。

        :param request: Request instance for ReplaceSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceSecurityGroupPolicies", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceSecurityGroupPoliciesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReplaceSecurityGroupPolicy(self, request):
        """本接口（ReplaceSecurityGroupPolicy）用于替换单条安全组规则（SecurityGroupPolicy）。
        单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReplaceSecurityGroupPolicy", params, headers=headers)
            response = json.loads(body)
            model = models.ReplaceSecurityGroupPolicyResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetAttachCcnInstances(self, request):
        """本接口（ResetAttachCcnInstances）用于跨账号关联实例申请过期时，重新申请关联操作。

        :param request: Request instance for ResetAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetAttachCcnInstances", params, headers=headers)
            response = json.loads(body)
            model = models.ResetAttachCcnInstancesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetHighPriorityRoutes(self, request):
        """重置高优路由表。

        :param request: Request instance for ResetHighPriorityRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetHighPriorityRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetHighPriorityRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetHighPriorityRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ResetHighPriorityRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetNatGatewayConnection(self, request):
        """本接口（ResetNatGatewayConnection）用来NAT网关并发连接上限。

        :param request: Request instance for ResetNatGatewayConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetNatGatewayConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ResetNatGatewayConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetRoutes(self, request):
        """本接口（ResetRoutes）用于对某个路由表名称和所有路由策略（Route）进行重新设置。<br /> 注意: 调用本接口时先删除当前路由表中所有路由策略, 再保存新提交的路由策略内容, 会引起网络中断。

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.ResetRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetTrafficMirrorFilter(self, request):
        """本接口（ResetTrafficMirrorFilter）用于更新流量镜像实例过滤规则。
        注意：每一个流量镜像实例，不能同时支持按nat网关和五元组两种规则过滤

        :param request: Request instance for ResetTrafficMirrorFilter.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetTrafficMirrorFilterRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetTrafficMirrorFilterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetTrafficMirrorFilter", params, headers=headers)
            response = json.loads(body)
            model = models.ResetTrafficMirrorFilterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetTrafficMirrorSrcs(self, request):
        """本接口（ResetTrafficMirrorSrcs）用于重置流量镜像实例采集对象。

        :param request: Request instance for ResetTrafficMirrorSrcs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetTrafficMirrorSrcsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetTrafficMirrorSrcsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetTrafficMirrorSrcs", params, headers=headers)
            response = json.loads(body)
            model = models.ResetTrafficMirrorSrcsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetTrafficMirrorTarget(self, request):
        """本接口（ResetTrafficMirrorTarget）用于更新流量镜像实例的接收目的信息。

        :param request: Request instance for ResetTrafficMirrorTarget.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetTrafficMirrorTargetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetTrafficMirrorTargetResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetTrafficMirrorTarget", params, headers=headers)
            response = json.loads(body)
            model = models.ResetTrafficMirrorTargetResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetVpnConnection(self, request):
        """本接口（ResetVpnConnection）用于重置VPN通道。

        :param request: Request instance for ResetVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetVpnConnection", params, headers=headers)
            response = json.loads(body)
            model = models.ResetVpnConnectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResetVpnGatewayInternetMaxBandwidth(self, request):
        """本接口（ResetVpnGatewayInternetMaxBandwidth）用于调整VPN网关带宽上限。VPN网关带宽目前仅支持部分带宽范围内升降配，如【5,100】Mbps和【200,1000】Mbps，在各自带宽范围内可提升配额，跨范围提升配额和降配暂不支持，如果是包年包月VPN网关需要在有效期内。

        :param request: Request instance for ResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResetVpnGatewayInternetMaxBandwidth", params, headers=headers)
            response = json.loads(body)
            model = models.ResetVpnGatewayInternetMaxBandwidthResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ResumeSnapshotInstance(self, request):
        """本接口（ResumeSnapshotInstance）用于根据备份内容恢复安全组策略。

        :param request: Request instance for ResumeSnapshotInstance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResumeSnapshotInstanceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResumeSnapshotInstanceResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ResumeSnapshotInstance", params, headers=headers)
            response = json.loads(body)
            model = models.ResumeSnapshotInstanceResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def ReturnNormalAddresses(self, request):
        """本接口（ReturnNormalAddresses）用于解绑并释放普通公网IP。
        为完善公网IP的访问管理功能，此接口于2022年12月15日升级优化鉴权功能，升级后子用户调用此接口需向主账号申请CAM策略授权，否则可能调用失败。您可以提前为子账号配置操作授权，详情见[授权指南](https://cloud.tencent.com/document/product/598/34545)。

        :param request: Request instance for ReturnNormalAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReturnNormalAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReturnNormalAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("ReturnNormalAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.ReturnNormalAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetCcnRegionBandwidthLimits(self, request):
        """本接口（SetCcnRegionBandwidthLimits）用于设置云联网（CCN）各地域出带宽上限，或者地域间带宽上限。

        :param request: Request instance for SetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetCcnRegionBandwidthLimits", params, headers=headers)
            response = json.loads(body)
            model = models.SetCcnRegionBandwidthLimitsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def SetVpnGatewaysRenewFlag(self, request):
        """本接口（SetVpnGatewaysRenewFlag）用于设置VPNGW续费标记。

        :param request: Request instance for SetVpnGatewaysRenewFlag.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetVpnGatewaysRenewFlagRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetVpnGatewaysRenewFlagResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("SetVpnGatewaysRenewFlag", params, headers=headers)
            response = json.loads(body)
            model = models.SetVpnGatewaysRenewFlagResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StartTrafficMirror(self, request):
        """本接口（StartTrafficMirror）用于开启流量镜像实例。

        :param request: Request instance for StartTrafficMirror.
        :type request: :class:`tencentcloud.vpc.v20170312.models.StartTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.StartTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StartTrafficMirror", params, headers=headers)
            response = json.loads(body)
            model = models.StartTrafficMirrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def StopTrafficMirror(self, request):
        """本接口（StopTrafficMirror）用于关闭流量镜像实例。

        :param request: Request instance for StopTrafficMirror.
        :type request: :class:`tencentcloud.vpc.v20170312.models.StopTrafficMirrorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.StopTrafficMirrorResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("StopTrafficMirror", params, headers=headers)
            response = json.loads(body)
            model = models.StopTrafficMirrorResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def TransformAddress(self, request):
        """本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 平台对用户每地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](/document/product/213/1941)）。上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。

        :param request: Request instance for TransformAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.TransformAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.TransformAddressResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("TransformAddress", params, headers=headers)
            response = json.loads(body)
            model = models.TransformAddressResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignIpv6Addresses(self, request):
        """本接口（UnassignIpv6Addresses）用于释放弹性网卡`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)接口。

        :param request: Request instance for UnassignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignIpv6Addresses", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignIpv6AddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignIpv6CidrBlock(self, request):
        """本接口（UnassignIpv6CidrBlock）用于释放IPv6网段。<br />
        网段如果还有IP占用且未回收，则网段无法释放。

        :param request: Request instance for UnassignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignIpv6CidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignIpv6CidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignIpv6SubnetCidrBlock(self, request):
        """本接口（UnassignIpv6SubnetCidrBlock）用于释放IPv6子网段。<br />
        子网段如果还有IP占用且未回收，则子网段无法释放。

        :param request: Request instance for UnassignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignIpv6SubnetCidrBlock", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignIpv6SubnetCidrBlockResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnassignPrivateIpAddresses(self, request):
        """本接口（UnassignPrivateIpAddresses）用于弹性网卡退还内网 IP。
        * 退还弹性网卡上的辅助内网IP，接口自动解除关联弹性公网 IP。不能退还弹性网卡的主内网IP。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询[DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037)
        接口。

        :param request: Request instance for UnassignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnassignPrivateIpAddresses", params, headers=headers)
            response = json.loads(body)
            model = models.UnassignPrivateIpAddressesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnlockCcnBandwidths(self, request):
        """本接口（UnlockCcnBandwidths）用户解锁云联网限速实例。
        该接口一般用来封禁地域间限速的云联网实例下的限速实例, 目前联通内部运营系统通过云API调用, 如果是出口限速, 一般使用更粗的云联网实例粒度封禁（SecurityUnlockCcns）。
        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统。

        :param request: Request instance for UnlockCcnBandwidths.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnlockCcnBandwidthsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnlockCcnBandwidthsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockCcnBandwidths", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockCcnBandwidthsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UnlockCcns(self, request):
        """本接口（UnlockCcns）用于解锁云联网实例

        该接口一般用来解封禁出口限速的云联网实例, 目前联通内部运营系统通过云API调用, 因为出口限速无法按地域间解封禁, 只能按更粗的云联网实例粒度解封禁, 如果是地域间限速, 一般可以通过更细的限速实例粒度解封禁（UnlockCcnBandwidths）

        如有需要, 可以封禁任意限速实例, 可接入到内部运营系统

        :param request: Request instance for UnlockCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnlockCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnlockCcnsResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UnlockCcns", params, headers=headers)
            response = json.loads(body)
            model = models.UnlockCcnsResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTrafficMirrorAllFilter(self, request):
        """本接口（UpdateTrafficMirrorAllFilter）用于更新流量镜像实例的过滤规则或者采集对象。

        :param request: Request instance for UpdateTrafficMirrorAllFilter.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UpdateTrafficMirrorAllFilterRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UpdateTrafficMirrorAllFilterResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTrafficMirrorAllFilter", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTrafficMirrorAllFilterResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def UpdateTrafficMirrorDirection(self, request):
        """本接口（UpdateTrafficMirrorDirection）用于更新流量镜像实例的采集方向。

        :param request: Request instance for UpdateTrafficMirrorDirection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UpdateTrafficMirrorDirectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UpdateTrafficMirrorDirectionResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("UpdateTrafficMirrorDirection", params, headers=headers)
            response = json.loads(body)
            model = models.UpdateTrafficMirrorDirectionResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))


    def WithdrawNotifyRoutes(self, request):
        """本接口（WithdrawNotifyRoutes）用于撤销已发布到云联网的路由。路由表列表页操作增加“从云联网撤销”。

        :param request: Request instance for WithdrawNotifyRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.WithdrawNotifyRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.WithdrawNotifyRoutesResponse`

        """
        try:
            params = request._serialize()
            headers = request.headers
            body = self.call("WithdrawNotifyRoutes", params, headers=headers)
            response = json.loads(body)
            model = models.WithdrawNotifyRoutesResponse()
            model._deserialize(response["Response"])
            return model
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(type(e).__name__, str(e))