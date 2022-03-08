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
            body = self.call("AcceptAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AcceptAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddBandwidthPackageResources(self, request):
        """接口用于添加带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等

        :param request: Request instance for AddBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddBandwidthPackageResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddBandwidthPackageResourcesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("AddIp6Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddIp6RulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AddTemplateMember(self, request):
        """增加模板对象中的IP地址、协议端口、IP地址组、协议端口组。当前仅支持北京、泰国、北美地域请求。

        :param request: Request instance for AddTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AddTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AddTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AddTemplateMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AddTemplateMemberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("AllocateAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AllocateIp6AddressesBandwidth(self, request):
        """该接口用于给IPv6地址初次分配公网带宽

        :param request: Request instance for AllocateIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AllocateIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AllocateIp6AddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AllocateIp6AddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6Addresses(self, request):
        """本接口（AssignIpv6Addresses）用于弹性网卡申请`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。
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
            body = self.call("AssignIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignIpv6CidrBlock(self, request):
        """本接口（AssignIpv6CidrBlock）用于分配IPv6网段。
        * 使用本接口前，您需要已有VPC实例，如果没有可通过接口<a href="https://cloud.tencent.com/document/api/215/15774" title="CreateVpc" target="_blank">CreateVpc</a>创建。
        * 每个VPC只能申请一个IPv6网段

        :param request: Request instance for AssignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignIpv6CidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6CidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("AssignIpv6SubnetCidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignIpv6SubnetCidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssignPrivateIpAddresses(self, request):
        """本接口（AssignPrivateIpAddresses）用于弹性网卡申请内网 IP。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 可以指定内网IP地址申请，内网IP地址类型不能为主IP，主IP已存在，不能修改，内网IP必须要弹性网卡所在子网内，而且不能被占用。
        * 在弹性网卡上申请一个到多个辅助内网IP，接口会在弹性网卡所在子网网段内返回指定数量的辅助内网IP。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for AssignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssignPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssignPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateAddress(self, request):
        """本接口 (AssociateAddress) 用于将[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        * 将 EIP 绑定到实例（CVM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        * 将 EIP 绑定到主网卡的主内网IP上，绑定过程会把其上绑定的普通公网 IP 自动解绑并释放。
        * 将 EIP 绑定到指定网卡的内网 IP上（非主网卡的主内网IP），则必须先解绑该 EIP，才能再绑定新的。
        * 将 EIP 绑定到NAT网关，请使用接口[AssociateNatGatewayAddress](https://cloud.tencent.com/document/product/215/36722)
        * EIP 如果欠费或被封堵，则不能被绑定。
        * 只有状态为 UNBIND 的 EIP 才能够被绑定。

        :param request: Request instance for AssociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("AssociateDhcpIpWithAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateDhcpIpWithAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateDirectConnectGatewayNatGateway(self, request):
        """将专线网关与NAT网关绑定，专线网关默认路由指向NAT网关

        :param request: Request instance for AssociateDirectConnectGatewayNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateDirectConnectGatewayNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateDirectConnectGatewayNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateDirectConnectGatewayNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateDirectConnectGatewayNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateNatGatewayAddress(self, request):
        """本接口(AssociateNatGatewayAddress)用于NAT网关绑定弹性IP（EIP）。

        :param request: Request instance for AssociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateNatGatewayAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateNatGatewayAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateNetworkAclSubnets(self, request):
        """本接口（AssociateNetworkAclSubnets）用于网络ACL关联vpc下的子网。

        :param request: Request instance for AssociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateNetworkAclSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateNetworkAclSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AssociateNetworkInterfaceSecurityGroups(self, request):
        """本接口（AssociateNetworkInterfaceSecurityGroups）用于弹性网卡绑定安全组（SecurityGroup）。

        :param request: Request instance for AssociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AssociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AssociateNetworkInterfaceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AssociateNetworkInterfaceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachCcnInstances(self, request):
        """本接口（AttachCcnInstances）用于将网络实例加载到云联网实例中，网络实例包括VPC和专线网关。<br />
        每个云联网能够关联的网络实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。

        :param request: Request instance for AttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("AttachClassicLinkVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachClassicLinkVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def AttachNetworkInterface(self, request):
        """本接口（AttachNetworkInterface）用于弹性网卡绑定云服务器。
        * 一个云服务器可以绑定多个弹性网卡，但只能绑定一个主网卡。更多限制信息详见<a href="https://cloud.tencent.com/document/product/576/18527">弹性网卡使用限制</a>。
        * 一个弹性网卡只能同时绑定一个云服务器。
        * 只有运行中或者已关机状态的云服务器才能绑定弹性网卡，查看云服务器状态详见<a href="https://cloud.tencent.com/document/api/213/9452#InstanceStatus">腾讯云服务器信息</a>。
        * 弹性网卡绑定的云服务器必须是私有网络的，而且云服务器所在可用区必须和弹性网卡子网的可用区相同。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for AttachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.AttachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("AttachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AttachNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("AuditCrossBorderCompliance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.AuditCrossBorderComplianceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckAssistantCidr(self, request):
        """本接口(CheckAssistantCidr)用于检查辅助CIDR是否与存量路由、对等连接（对端VPC的CIDR）等资源存在冲突。如果存在重叠，则返回重叠的资源。（接口灰度中，如需使用请提工单。）
        * 检测辅助CIDR是否与当前VPC的主CIDR和辅助CIDR存在重叠。
        * 检测辅助CIDR是否与当前VPC的路由的目的端存在重叠。
        * 检测辅助CIDR是否与当前VPC的对等连接，对端VPC下的主CIDR或辅助CIDR存在重叠。

        :param request: Request instance for CheckAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckDefaultSubnet(self, request):
        """本接口（CheckDefaultSubnet）用于预判是否可建默认子网。

        :param request: Request instance for CheckDefaultSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckDefaultSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckDefaultSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckDefaultSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckDefaultSubnetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CheckNetDetectState(self, request):
        """本接口(CheckNetDetectState)用于验证网络探测。

        :param request: Request instance for CheckNetDetectState.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CheckNetDetectStateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CheckNetDetectState", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CheckNetDetectStateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CloneSecurityGroup(self, request):
        """本接口（CloneSecurityGroup）用于根据存量的安全组，克隆创建出同样规则配置的安全组。仅克隆安全组及其规则信息，不会克隆安全组标签信息。

        :param request: Request instance for CloneSecurityGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CloneSecurityGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CloneSecurityGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CloneSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CloneSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAddressTemplate(self, request):
        """本接口（CreateAddressTemplate）用于创建IP地址模板。

        :param request: Request instance for CreateAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAddressTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAddressTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAddressTemplateGroup(self, request):
        """本接口（CreateAddressTemplateGroup）用于创建IP地址模板集合

        :param request: Request instance for CreateAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAddressTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAddressTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateAndAttachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAndAttachNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateAssistantCidr(self, request):
        """本接口(CreateAssistantCidr)用于批量创建辅助CIDR。（接口灰度中，如需使用请提工单。）

        :param request: Request instance for CreateAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateBandwidthPackage(self, request):
        """本接口 (CreateBandwidthPackage) 支持创建[设备带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)和[IP带宽包](https://cloud.tencent.com/document/product/684/15245#bwptype)。

        :param request: Request instance for CreateBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateBandwidthPackage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateBandwidthPackageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCcn(self, request):
        """本接口（CreateCcn）用于创建云联网（CCN）。<br />
        * 创建云联网同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        每个账号能创建的云联网实例个数是有限的，详请参考产品文档。如果需要扩充请联系在线客服。

        :param request: Request instance for CreateCcn.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCcnRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCcnResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCcn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCcnResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateCustomerGateway(self, request):
        """本接口（CreateCustomerGateway）用于创建对端网关。

        :param request: Request instance for CreateCustomerGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateCustomerGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateCustomerGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateDefaultSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDefaultVpc(self, request):
        """本接口（CreateDefaultVpc）用于创建默认私有网络(VPC）。

        默认VPC适用于快速入门和启动公共实例，您可以像使用任何其他VPC一样使用默认VPC。如果您想创建标准VPC，即指定VPC名称、VPC网段、子网网段、子网可用区，请使用常规创建VPC接口（CreateVpc）

        正常情况，本接口并不一定生产默认VPC，而是根据用户账号的网络属性（DescribeAccountAttributes）来决定的
        * 支持基础网络、VPC，返回VpcId为0
        * 只支持VPC，返回默认VPC信息

        您也可以通过 Force 参数，强制返回默认VPC

        :param request: Request instance for CreateDefaultVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDefaultVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDefaultVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDefaultVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDhcpIp(self, request):
        """本接口（CreateDhcpIp）用于创建DhcpIp

        :param request: Request instance for CreateDhcpIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDhcpIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDhcpIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDhcpIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDhcpIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDirectConnectGateway(self, request):
        """本接口（CreateDirectConnectGateway）用于创建专线网关。

        :param request: Request instance for CreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateDirectConnectGatewayCcnRoutes(self, request):
        """本接口（CreateDirectConnectGatewayCcnRoutes）用于创建专线网关的云联网路由（IDC网段）

        :param request: Request instance for CreateDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateFlowLog(self, request):
        """本接口（CreateFlowLog）用于创建流日志

        :param request: Request instance for CreateFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateFlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateFlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateFlowLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateHaVip(self, request):
        """本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）

        :param request: Request instance for CreateHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateHaVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateHaVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateHaVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateIp6Translators(self, request):
        """1. 该接口用于创建IPV6转换IPV4实例，支持批量
        2. 同一个账户在一个地域最多允许创建10个转换实例

        :param request: Request instance for CreateIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateIp6Translators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateIp6TranslatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateLocalGateway(self, request):
        """该接口用于创建用于CDC的本地网关。

        :param request: Request instance for CreateLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateLocalGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateLocalGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNatGateway(self, request):
        """本接口(CreateNatGateway)用于创建NAT网关。
        在对新建的NAT网关做其他操作前，需先确认此网关已被创建完成（DescribeNatGateway接口返回的实例State字段为AVAILABLE）。

        :param request: Request instance for CreateNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口(CreateNatGatewayDestinationIpPortTranslationNatRule)用于创建NAT网关端口转发规则。

        :param request: Request instance for CreateNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNatGatewaySourceIpTranslationNatRule(self, request):
        """本接口(CreateNatGatewaySourceIpTranslationNatRule)用于创建NAT网关SNAT规则

        :param request: Request instance for CreateNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNatGatewaySourceIpTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNatGatewaySourceIpTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetDetect(self, request):
        """本接口(CreateNetDetect)用于创建网络探测。

        :param request: Request instance for CreateNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkAcl(self, request):
        """本接口（CreateNetworkAcl）用于创建新的<a href="https://cloud.tencent.com/document/product/215/20088">网络ACL</a>。
        * 新建的网络ACL的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用ModifyNetworkAclEntries将网络ACL的规则设置为需要的规则。

        :param request: Request instance for CreateNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetworkAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkAclResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateNetworkInterface(self, request):
        """本接口（CreateNetworkInterface）用于创建弹性网卡。
        * 创建弹性网卡时可以指定内网IP，并且可以指定一个主IP，指定的内网IP必须在弹性网卡所在子网内，而且不能被占用。
        * 创建弹性网卡时可以指定需要申请的内网IP数量，系统会随机生成内网IP地址。
        * 一个弹性网卡支持绑定的IP地址是有限制的，更多资源限制信息详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。
        * 创建弹性网卡同时可以绑定已有安全组。
        * 创建弹性网卡同时可以绑定标签, 应答里的标签列表代表添加成功的标签。
        >?本接口为异步接口，可调用 [DescribeVpcTaskResult](https://cloud.tencent.com/document/api/215/59037) 接口查询任务执行结果，待任务执行成功后再进行其他操作。
        >

        :param request: Request instance for CreateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRouteTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateRoutes(self, request):
        """本接口(CreateRoutes)用于创建路由策略。
        * 向指定路由表批量新增路由策略。

        :param request: Request instance for CreateRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
        <li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受，即 Protocol 字段不是 TCP 或 UDP 时，Protocol 和 Port 排他关系，不允许同时输入，否则会接口报错。</li>
        <li>Action 字段只允许输入 ACCEPT 或 DROP。</li>
        <li>CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate 四者是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。</li>
        <li>一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。</li>
        </ul></li></ul>

        :param request: Request instance for CreateSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSecurityGroupWithPolicies(self, request):
        """本接口（CreateSecurityGroupWithPolicies）用于创建新的安全组（SecurityGroup），并且可以同时添加安全组规则（SecurityGroupPolicy）。
        * 每个账户下每个地域的每个项目的<a href="https://cloud.tencent.com/document/product/213/12453">安全组数量限制</a>。
        * 新建的安全组的入站和出站规则默认都是全部拒绝，在创建后通常您需要再调用CreateSecurityGroupPolicies将安全组的规则设置为需要的规则。

        安全组规则说明：
        * Version安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。
        * Protocol字段支持输入TCP, UDP, ICMP, ICMPV6, GRE, ALL。
        * CidrBlock字段允许输入符合cidr格式标准的任意字符串。(展开)在基础网络中，如果CidrBlock包含您的账户内的云服务器之外的设备在腾讯云的内网IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。
        * Ipv6CidrBlock字段允许输入符合IPv6 cidr格式标准的任意字符串。(展开)在基础网络中，如果Ipv6CidrBlock包含您的账户内的云服务器之外的设备在腾讯云的内网IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。
        * SecurityGroupId字段允许输入与待修改的安全组位于相同项目中的安全组ID，包括这个安全组ID本身，代表安全组下所有云服务器的内网IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个ID所关联的云服务器变化而变化，不需要重新修改。
        * Port字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当Protocol字段是TCP或UDP时，Port字段才被接受，即Protocol字段不是TCP或UDP时，Protocol和Port排他关系，不允许同时输入，否则会接口报错。
        * Action字段只允许输入ACCEPT或DROP。
        * CidrBlock, Ipv6CidrBlock, SecurityGroupId, AddressTemplate四者是排他关系，不允许同时输入，Protocol + Port和ServiceTemplate二者是排他关系，不允许同时输入。
        * 一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。

        :param request: Request instance for CreateSecurityGroupWithPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateSecurityGroupWithPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateSecurityGroupWithPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSecurityGroupWithPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceTemplate(self, request):
        """本接口（CreateServiceTemplate）用于创建协议端口模板

        :param request: Request instance for CreateServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateServiceTemplateGroup(self, request):
        """本接口（CreateServiceTemplateGroup）用于创建协议端口模板集合

        :param request: Request instance for CreateServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateServiceTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateServiceTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubnet(self, request):
        """本接口(CreateSubnet)用于创建子网。
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
            body = self.call("CreateSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateSubnets(self, request):
        """本接口(CreateSubnets)用于批量创建子网。
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
            body = self.call("CreateSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpc(self, request):
        """本接口(CreateVpc)用于创建私有网络(VPC)。
        * 用户可以创建的最小网段子网掩码为28（有16个IP地址），最大网段子网掩码为16（65,536个IP地址），如果需要规划VPC网段请参见[网络规划](https://cloud.tencent.com/document/product/215/30313)。
        * 同一个地域能创建的VPC资源个数也是有限制的，详见 <a href="https://cloud.tencent.com/doc/product/215/537" title="VPC使用限制">VPC使用限制</a>，如果需要申请更多资源，请提交[工单申请](https://console.cloud.tencent.com/workorder/category)。
        * 创建VPC同时可以绑定标签, 应答里的标签列表代表添加成功的标签。

        :param request: Request instance for CreateVpc.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpcEndPoint(self, request):
        """创建终端节点。

        :param request: Request instance for CreateVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpcEndPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcEndPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpcEndPointService(self, request):
        """本接口(CreateVpcEndPointService)用于创建终端节点服务。

        :param request: Request instance for CreateVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpcEndPointService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcEndPointServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpcEndPointServiceWhiteList(self, request):
        """创建终端服务白名单。

        :param request: Request instance for CreateVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpcEndPointServiceWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpcEndPointServiceWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("CreateVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnGateway(self, request):
        """本接口（CreateVpnGateway）用于创建VPN网关。

        :param request: Request instance for CreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnGatewayRoutes(self, request):
        """创建路由型VPN网关的目的路由

        :param request: Request instance for CreateVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnGatewayRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnGatewayRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnGatewaySslClient(self, request):
        """创建SSL-VPN-CLIENT

        :param request: Request instance for CreateVpnGatewaySslClient.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslClientRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnGatewaySslClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnGatewaySslClientResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def CreateVpnGatewaySslServer(self, request):
        """创建 Server端

        :param request: Request instance for CreateVpnGatewaySslServer.
        :type request: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslServerRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.CreateVpnGatewaySslServerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("CreateVpnGatewaySslServer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.CreateVpnGatewaySslServerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAddressTemplate(self, request):
        """本接口（DeleteAddressTemplate）用于删除IP地址模板

        :param request: Request instance for DeleteAddressTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAddressTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAddressTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAddressTemplateGroup(self, request):
        """本接口（DeleteAddressTemplateGroup）用于删除IP地址模板集合

        :param request: Request instance for DeleteAddressTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAddressTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAddressTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAddressTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteAssistantCidr(self, request):
        """本接口(DeleteAssistantCidr)用于删除辅助CIDR。（接口灰度中，如需使用请提工单。）

        :param request: Request instance for DeleteAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteBandwidthPackage(self, request):
        """接口支持删除共享带宽包，包括[设备带宽包](https://cloud.tencent.com/document/product/684/15246#.E8.AE.BE.E5.A4.87.E5.B8.A6.E5.AE.BD.E5.8C.85)和[IP带宽包](https://cloud.tencent.com/document/product/684/15246#ip-.E5.B8.A6.E5.AE.BD.E5.8C.85)

        :param request: Request instance for DeleteBandwidthPackage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteBandwidthPackageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteBandwidthPackage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteBandwidthPackageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteCcn", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCcnResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteCustomerGateway(self, request):
        """本接口（DeleteCustomerGateway）用于删除对端网关。

        :param request: Request instance for DeleteCustomerGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteCustomerGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteCustomerGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteCustomerGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteDhcpIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDhcpIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteDirectConnectGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteDirectConnectGatewayCcnRoutes(self, request):
        """本接口（DeleteDirectConnectGatewayCcnRoutes）用于删除专线网关的云联网路由（IDC网段）

        :param request: Request instance for DeleteDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteFlowLog(self, request):
        """本接口（DeleteFlowLog）用于删除流日志

        :param request: Request instance for DeleteFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteFlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteFlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteFlowLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteHaVip(self, request):
        """本接口（DeleteHaVip）用于删除高可用虚拟IP（HAVIP）。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for DeleteHaVip.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteHaVipResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteHaVip", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteHaVipResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteIp6Translators(self, request):
        """1. 该接口用于释放IPV6转换实例，支持批量。
        2.  如果IPV6转换实例建立有转换规则，会一并删除。

        :param request: Request instance for DeleteIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteIp6Translators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteIp6TranslatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteLocalGateway(self, request):
        """该接口用于删除CDC的本地网关。

        :param request: Request instance for DeleteLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteLocalGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteLocalGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNatGateway(self, request):
        """本接口（DeleteNatGateway）用于删除NAT网关。
        删除 NAT 网关后，系统会自动删除路由表中包含此 NAT 网关的路由项，同时也会解绑弹性公网IP（EIP）。

        :param request: Request instance for DeleteNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（DeleteNatGatewayDestinationIpPortTranslationNatRule）用于删除NAT网关端口转发规则。

        :param request: Request instance for DeleteNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNatGatewaySourceIpTranslationNatRule(self, request):
        """本接口（DeleteNatGatewaySourceIpTranslationNatRule）用于删除NAT网关端口SNAT转发规则。

        :param request: Request instance for DeleteNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNatGatewaySourceIpTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNatGatewaySourceIpTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetDetect(self, request):
        """本接口(DeleteNetDetect)用于删除网络探测实例。

        :param request: Request instance for DeleteNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteNetworkAcl(self, request):
        """本接口（DeleteNetworkAcl）用于删除网络ACL。

        :param request: Request instance for DeleteNetworkAcl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteNetworkAclResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteNetworkAcl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkAclResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRouteTable(self, request):
        """删除路由表

        :param request: Request instance for DeleteRouteTable.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRouteTableResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRouteTable", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRouteTableResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteRoutes(self, request):
        """本接口(DeleteRoutes)用于对某个路由表批量删除路由策略（Route）。

        :param request: Request instance for DeleteRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteSecurityGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSecurityGroupPolicies(self, request):
        """本接口（DeleteSecurityGroupPolicies）用于用于删除安全组规则（SecurityGroupPolicy）。
        * SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。

        :param request: Request instance for DeleteSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceTemplate(self, request):
        """本接口（DeleteServiceTemplate）用于删除协议端口模板

        :param request: Request instance for DeleteServiceTemplate.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceTemplate", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceTemplateResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteServiceTemplateGroup(self, request):
        """本接口（DeleteServiceTemplateGroup）用于删除协议端口模板集合

        :param request: Request instance for DeleteServiceTemplateGroup.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteServiceTemplateGroupResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteServiceTemplateGroup", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteServiceTemplateGroupResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteSubnet(self, request):
        """本接口（DeleteSubnet）用于用于删除子网(Subnet)。
        * 删除子网前，请清理该子网下所有资源，包括云服务器、负载均衡、云数据、noSql、弹性网卡等资源。

        :param request: Request instance for DeleteSubnet.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteSubnetResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteSubnet", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteSubnetResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteTemplateMember(self, request):
        """删除模板对象中的IP地址、协议端口、IP地址组、协议端口组。当前仅支持北京、泰国、北美地域请求。

        :param request: Request instance for DeleteTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteTemplateMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteTemplateMemberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DeleteVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpcEndPoint(self, request):
        """删除终端节点。

        :param request: Request instance for DeleteVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpcEndPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcEndPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpcEndPointService(self, request):
        """删除终端节点服务。


        :param request: Request instance for DeleteVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpcEndPointService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcEndPointServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpcEndPointServiceWhiteList(self, request):
        """删除终端节点服务白名单。

        :param request: Request instance for DeleteVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpcEndPointServiceWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpcEndPointServiceWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnConnection(self, request):
        """本接口(DeleteVpnConnection)用于删除VPN通道。

        :param request: Request instance for DeleteVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnGateway(self, request):
        """本接口（DeleteVpnGateway）用于删除VPN网关。目前只支持删除运行中的按量计费的IPSEC网关实例。

        :param request: Request instance for DeleteVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnGatewayRoutes(self, request):
        """本接口（DeleteVpnGatewayCcnRoutes）用于删除VPN网关路由

        :param request: Request instance for DeleteVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnGatewayRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnGatewayRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnGatewaySslClient(self, request):
        """删除SSL-VPN-CLIENT

        :param request: Request instance for DeleteVpnGatewaySslClient.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslClientRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslClientResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnGatewaySslClient", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnGatewaySslClientResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DeleteVpnGatewaySslServer(self, request):
        """删除SSL-VPN-SERVER 实例

        :param request: Request instance for DeleteVpnGatewaySslServer.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslServerRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DeleteVpnGatewaySslServerResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DeleteVpnGatewaySslServer", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DeleteVpnGatewaySslServerResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAccountAttributes(self, request):
        """本接口（DescribeAccountAttributes）用于查询用户账号私有属性。

        :param request: Request instance for DescribeAccountAttributes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAccountAttributesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAccountAttributes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAccountAttributesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressQuota(self, request):
        """本接口 (DescribeAddressQuota) 用于查询您账户的[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）在当前地域的配额信息。配额详情可参见 [EIP 产品简介](https://cloud.tencent.com/document/product/213/5733)。

        :param request: Request instance for DescribeAddressQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressTemplateGroups(self, request):
        """本接口（DescribeAddressTemplateGroups）用于查询IP地址模板集合

        :param request: Request instance for DescribeAddressTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressTemplateGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressTemplateGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddressTemplates(self, request):
        """本接口（DescribeAddressTemplates）用于查询IP地址模板

        :param request: Request instance for DescribeAddressTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddressTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAddresses(self, request):
        """本接口 (DescribeAddresses) 用于查询一个或多个[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的详细信息。
        * 如果参数为空，返回当前用户一定数量（Limit所指定的数量，默认为20）的 EIP。

        :param request: Request instance for DescribeAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeAssistantCidr(self, request):
        """本接口（DescribeAssistantCidr）用于查询辅助CIDR列表。（接口灰度中，如需使用请提工单。）

        :param request: Request instance for DescribeAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBandwidthPackageBillUsage(self, request):
        """本接口 (DescribeBandwidthPackageBillUsage) 用于查询后付费共享带宽包当前的计费用量.

        :param request: Request instance for DescribeBandwidthPackageBillUsage.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBillUsageRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageBillUsageResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBandwidthPackageBillUsage", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBandwidthPackageBillUsageResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBandwidthPackageQuota(self, request):
        """接口用于查询账户在当前地域的带宽包上限数量以及使用数量

        :param request: Request instance for DescribeBandwidthPackageQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBandwidthPackageQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBandwidthPackageQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBandwidthPackageResources(self, request):
        """本接口 (DescribeBandwidthPackageResources) 用于根据共享带宽包唯一ID查询共享带宽包内的资源列表，支持按条件过滤查询结果和分页查询。

        :param request: Request instance for DescribeBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBandwidthPackageResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBandwidthPackageResourcesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeBandwidthPackages(self, request):
        """接口用于查询带宽包详细信息，包括带宽包唯一标识ID，类型，计费模式，名称，资源信息等

        :param request: Request instance for DescribeBandwidthPackages.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeBandwidthPackagesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeBandwidthPackages", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeBandwidthPackagesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnAttachedInstances(self, request):
        """本接口（DescribeCcnAttachedInstances）用于查询云联网实例下已关联的网络实例。

        :param request: Request instance for DescribeCcnAttachedInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnAttachedInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnAttachedInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnAttachedInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnRegionBandwidthLimits(self, request):
        """本接口（DescribeCcnRegionBandwidthLimits）用于查询云联网各地域出带宽上限，该接口只返回已关联网络实例包含的地域

        :param request: Request instance for DescribeCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnRegionBandwidthLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnRegionBandwidthLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcnRoutes(self, request):
        """本接口（DescribeCcnRoutes）用于查询已加入云联网（CCN）的路由

        :param request: Request instance for DescribeCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCcns(self, request):
        """本接口（DescribeCcns）用于查询云联网（CCN）列表。

        :param request: Request instance for DescribeCcns.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCcnsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCcns", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCcnsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeClassicLinkInstances(self, request):
        """本接口(DescribeClassicLinkInstances)用于查询私有网络和基础网络设备互通列表。

        :param request: Request instance for DescribeClassicLinkInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeClassicLinkInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeClassicLinkInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeClassicLinkInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCrossBorderCompliance(self, request):
        """本接口（DescribeCrossBorderCompliance）用于查询用户创建的合规化资质审批单。
        服务商可以查询服务名下的任意 `APPID` 创建的审批单；非服务商，只能查询自己审批单。

        :param request: Request instance for DescribeCrossBorderCompliance.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderComplianceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCrossBorderComplianceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCrossBorderCompliance", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCrossBorderComplianceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomerGatewayVendors(self, request):
        """本接口（DescribeCustomerGatewayVendors）用于查询可支持的对端网关厂商信息。

        :param request: Request instance for DescribeCustomerGatewayVendors.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewayVendorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomerGatewayVendors", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomerGatewayVendorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeCustomerGateways(self, request):
        """本接口（DescribeCustomerGateways）用于查询对端网关列表。

        :param request: Request instance for DescribeCustomerGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeCustomerGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeCustomerGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeCustomerGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDhcpIps(self, request):
        """本接口（DescribeDhcpIps）用于查询DhcpIp列表

        :param request: Request instance for DescribeDhcpIps.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDhcpIpsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDhcpIpsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDhcpIps", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDhcpIpsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDirectConnectGatewayCcnRoutes(self, request):
        """本接口（DescribeDirectConnectGatewayCcnRoutes）用于查询专线网关的云联网路由（IDC网段）

        :param request: Request instance for DescribeDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeDirectConnectGateways(self, request):
        """本接口（DescribeDirectConnectGateways）用于查询专线网关。

        :param request: Request instance for DescribeDirectConnectGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeDirectConnectGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeDirectConnectGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeDirectConnectGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowLog(self, request):
        """本接口（DescribeFlowLog）用于查询流日志实例信息

        :param request: Request instance for DescribeFlowLog.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowLog", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowLogResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeFlowLogs(self, request):
        """本接口（DescribeFlowLogs）用于查询获取流日志集合

        :param request: Request instance for DescribeFlowLogs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeFlowLogsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeFlowLogs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeFlowLogsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DescribeGatewayFlowMonitorDetail", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayFlowMonitorDetailResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeGatewayFlowQos(self, request):
        """本接口（DescribeGatewayFlowQos）用于查询网关来访IP流控带宽。

        :param request: Request instance for DescribeGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeGatewayFlowQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeGatewayFlowQosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeHaVips(self, request):
        """本接口（DescribeHaVips）用于查询高可用虚拟IP（HAVIP）列表。

        :param request: Request instance for DescribeHaVips.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeHaVipsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeHaVips", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeHaVipsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIp6Addresses(self, request):
        """该接口用于查询IPV6地址信息

        :param request: Request instance for DescribeIp6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIp6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIp6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIp6TranslatorQuota(self, request):
        """查询账户在指定地域IPV6转换实例和规则的配额

        :param request: Request instance for DescribeIp6TranslatorQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIp6TranslatorQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIp6TranslatorQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIp6Translators(self, request):
        """1. 该接口用于查询账户下的IPV6转换实例及其绑定的转换规则信息
        2. 支持过滤查询

        :param request: Request instance for DescribeIp6Translators.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIp6TranslatorsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIp6Translators", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIp6TranslatorsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIpGeolocationDatabaseUrl(self, request):
        """本接口（DescribeIpGeolocationDatabaseUrl）用于获取IP地理位置库下载链接。

        :param request: Request instance for DescribeIpGeolocationDatabaseUrl.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationDatabaseUrlRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationDatabaseUrlResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpGeolocationDatabaseUrl", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpGeolocationDatabaseUrlResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeIpGeolocationInfos(self, request):
        """本接口（DescribeIpGeolocationInfos）用于查询IP地址信息，包括地理位置信息和网络信息。
        本接口目前处于内测中，如需使用，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=660&source=0&data_title=%E5%BC%B9%E6%80%A7%E5%85%AC%E7%BD%91%20EIP&level3_id=662&queue=96&scene_code=16400&step=2)。

        :param request: Request instance for DescribeIpGeolocationInfos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationInfosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeIpGeolocationInfosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeIpGeolocationInfos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeIpGeolocationInfosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeLocalGateway(self, request):
        """该接口用于查询CDC的本地网关。

        :param request: Request instance for DescribeLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeLocalGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeLocalGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGatewayDestinationIpPortTranslationNatRules(self, request):
        """本接口（DescribeNatGatewayDestinationIpPortTranslationNatRules）用于查询NAT网关端口转发规则对象数组。

        :param request: Request instance for DescribeNatGatewayDestinationIpPortTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGatewayDestinationIpPortTranslationNatRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGatewayDirectConnectGatewayRoute(self, request):
        """查询专线绑定NAT的路由

        :param request: Request instance for DescribeNatGatewayDirectConnectGatewayRoute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDirectConnectGatewayRouteRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewayDirectConnectGatewayRouteResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGatewayDirectConnectGatewayRoute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewayDirectConnectGatewayRouteResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGatewaySourceIpTranslationNatRules(self, request):
        """本接口（DescribeNatGatewaySourceIpTranslationNatRules）用于查询NAT网关SNAT转发规则对象数组。

        :param request: Request instance for DescribeNatGatewaySourceIpTranslationNatRules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaySourceIpTranslationNatRulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaySourceIpTranslationNatRulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGatewaySourceIpTranslationNatRules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewaySourceIpTranslationNatRulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNatGateways(self, request):
        """本接口（DescribeNatGateways）用于查询 NAT 网关。

        :param request: Request instance for DescribeNatGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNatGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNatGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNatGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetDetectStates(self, request):
        """本接口(DescribeNetDetectStates)用于查询网络探测验证结果列表。

        :param request: Request instance for DescribeNetDetectStates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectStatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetDetectStates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetDetectStatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetDetects(self, request):
        """本接口（DescribeNetDetects）用于查询网络探测列表。

        :param request: Request instance for DescribeNetDetects.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetDetectsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetDetects", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetDetectsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkAcls(self, request):
        """本接口（DescribeNetworkAcls）用于查询网络ACL列表。

        :param request: Request instance for DescribeNetworkAcls.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkAclsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkAcls", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkAclsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkInterfaceLimit(self, request):
        """本接口（DescribeNetworkInterfaceLimit）根据CVM实例ID或弹性网卡ID查询弹性网卡配额，返回该CVM实例或弹性网卡能绑定的弹性网卡配额，以及弹性网卡可以分配的IP配额

        :param request: Request instance for DescribeNetworkInterfaceLimit.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfaceLimitResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInterfaceLimit", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInterfaceLimitResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeNetworkInterfaces(self, request):
        """本接口（DescribeNetworkInterfaces）用于查询弹性网卡列表。

        :param request: Request instance for DescribeNetworkInterfaces.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeNetworkInterfacesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeNetworkInterfaces", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeNetworkInterfacesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeProductQuota(self, request):
        """本接口用于查询网络产品的配额信息

        :param request: Request instance for DescribeProductQuota.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeProductQuotaRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeProductQuotaResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeProductQuota", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeProductQuotaResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRouteConflicts(self, request):
        """本接口（DescribeRouteConflicts）用于查询自定义路由策略与云联网路由策略冲突列表

        :param request: Request instance for DescribeRouteConflicts.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteConflictsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteConflictsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRouteConflicts", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteConflictsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeRouteTables(self, request):
        """本接口（DescribeRouteTables）用于查询路由表。

        :param request: Request instance for DescribeRouteTables.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeRouteTablesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeRouteTables", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeRouteTablesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupAssociationStatistics(self, request):
        """本接口（DescribeSecurityGroupAssociationStatistics）用于查询安全组关联的实例统计。

        :param request: Request instance for DescribeSecurityGroupAssociationStatistics.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupAssociationStatisticsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupAssociationStatistics", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupAssociationStatisticsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupLimits(self, request):
        """本接口(DescribeSecurityGroupLimits)用于查询用户安全组配额。

        :param request: Request instance for DescribeSecurityGroupLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupPolicies(self, request):
        """本接口（DescribeSecurityGroupPolicies）用于查询安全组规则。

        :param request: Request instance for DescribeSecurityGroupPolicies.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupPoliciesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroupReferences(self, request):
        """本接口（DescribeSecurityGroupReferences）用于查询安全组被引用信息。

        :param request: Request instance for DescribeSecurityGroupReferences.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupReferencesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroupReferences", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupReferencesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSecurityGroups(self, request):
        """本接口（DescribeSecurityGroups）用于查询安全组。

        :param request: Request instance for DescribeSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceTemplateGroups(self, request):
        """本接口（DescribeServiceTemplateGroups）用于查询协议端口模板集合

        :param request: Request instance for DescribeServiceTemplateGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplateGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceTemplateGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceTemplateGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeServiceTemplates(self, request):
        """本接口（DescribeServiceTemplates）用于查询协议端口模板

        :param request: Request instance for DescribeServiceTemplates.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeServiceTemplatesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeServiceTemplates", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeServiceTemplatesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeSubnets(self, request):
        """本接口（DescribeSubnets）用于查询子网列表。

        :param request: Request instance for DescribeSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTaskResult(self, request):
        """查询EIP异步任务执行结果

        :param request: Request instance for DescribeTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTaskResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeTemplateLimits(self, request):
        """本接口（DescribeTemplateLimits）用于查询参数模板配额列表。

        :param request: Request instance for DescribeTemplateLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeTemplateLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeTemplateLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeTemplateLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeTemplateLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcEndPoint(self, request):
        """查询终端节点列表。

        :param request: Request instance for DescribeVpcEndPoint.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcEndPoint", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcEndPointResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcEndPointService(self, request):
        """查询终端节点服务列表。

        :param request: Request instance for DescribeVpcEndPointService.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcEndPointService", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcEndPointServiceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcEndPointServiceWhiteList(self, request):
        """查询终端节点服务的服务白名单列表。

        :param request: Request instance for DescribeVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcEndPointServiceWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcEndPointServiceWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcInstances(self, request):
        """本接口（DescribeVpcInstances）用于查询VPC下的云主机实例列表。

        :param request: Request instance for DescribeVpcInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcIpv6Addresses(self, request):
        """本接口（DescribeVpcIpv6Addresses）用于查询 `VPC` `IPv6` 信息。
        只能查询已使用的`IPv6`信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。

        :param request: Request instance for DescribeVpcIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcLimits(self, request):
        """获取私有网络配额，部分私有网络的配额有地域属性。
        LimitTypes取值范围：
        * appid-max-vpcs （每个开发商每个地域可创建的VPC数）
        * vpc-max-subnets（每个VPC可创建的子网数）
        * vpc-max-route-tables（每个VPC可创建的路由表数）
        * route-table-max-policies（每个路由表可添加的策略数）
        * vpc-max-vpn-gateways（每个VPC可创建的VPN网关数）
        * appid-max-custom-gateways（每个开发商可创建的对端网关数）
        * appid-max-vpn-connections（每个开发商可创建的VPN通道数）
        * custom-gateway-max-vpn-connections（每个对端网关可创建的VPN通道数）
        * vpn-gateway-max-custom-gateways（每个VPNGW可以创建的通道数）
        * vpc-max-network-acls（每个VPC可创建的网络ACL数）
        * network-acl-max-inbound-policies（每个网络ACL可添加的入站规则数）
        * network-acl-max-outbound-policies（每个网络ACL可添加的出站规则数）
        * vpc-max-vpcpeers（每个VPC可创建的对等连接数）
        * vpc-max-available-vpcpeers（每个VPC可创建的有效对等连接数）
        * vpc-max-basic-network-interconnections（每个VPC可创建的基础网络云主机与VPC互通数）
        * direct-connection-max-snats（每个专线网关可创建的SNAT数）
        * direct-connection-max-dnats（每个专线网关可创建的DNAT数）
        * direct-connection-max-snapts（每个专线网关可创建的SNAPT数）
        * direct-connection-max-dnapts（每个专线网关可创建的DNAPT数）
        * vpc-max-nat-gateways（每个VPC可创建的NAT网关数）
        * nat-gateway-max-eips（每个NAT可以购买的外网IP数量）
        * vpc-max-enis（每个VPC可创建弹性网卡数）
        * vpc-max-havips（每个VPC可创建HAVIP数）
        * eni-max-private-ips（每个ENI可以绑定的内网IP数（ENI未绑定子机））
        * nat-gateway-max-dnapts（每个NAT网关可创建的DNAPT数）
        * vpc-max-ipv6s（每个VPC可分配的IPv6地址数）
        * eni-max-ipv6s（每个ENI可分配的IPv6地址数）
        * vpc-max-assistant_cidrs（每个VPC可分配的辅助CIDR数）

        :param request: Request instance for DescribeVpcLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcPrivateIpAddresses(self, request):
        """本接口（DescribeVpcPrivateIpAddresses）用于查询VPC内网IP信息。<br />
        只能查询已使用的IP信息，当查询未使用的IP时，本接口不会报错，但不会出现在返回结果里。

        :param request: Request instance for DescribeVpcPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcResourceDashboard(self, request):
        """本接口(DescribeVpcResourceDashboard)用于查看VPC资源信息。

        :param request: Request instance for DescribeVpcResourceDashboard.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcResourceDashboardResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcResourceDashboard", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcResourceDashboardResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcTaskResult(self, request):
        """本接口（DescribeVpcTaskResult）用于查询VPC任务执行结果。

        :param request: Request instance for DescribeVpcTaskResult.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcTaskResultRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcTaskResultResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcTaskResult", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcTaskResultResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpcs(self, request):
        """本接口（DescribeVpcs）用于查询私有网络列表。

        :param request: Request instance for DescribeVpcs.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpcsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpcs", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpcsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnConnections(self, request):
        """本接口（DescribeVpnConnections）查询VPN通道列表。

        :param request: Request instance for DescribeVpnConnections.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnConnectionsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnConnections", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnConnectionsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnGatewayCcnRoutes(self, request):
        """本接口（DescribeVpnGatewayCcnRoutes）用于查询VPN网关云联网路由

        :param request: Request instance for DescribeVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnGatewayRoutes(self, request):
        """查询路由型VPN网关的目的路由

        :param request: Request instance for DescribeVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGatewayRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewayRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnGatewaySslClients(self, request):
        """查询SSL-VPN-CLIENT 列表

        :param request: Request instance for DescribeVpnGatewaySslClients.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslClientsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslClientsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGatewaySslClients", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewaySslClientsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnGatewaySslServers(self, request):
        """查询SSL-VPN SERVER 列表信息

        :param request: Request instance for DescribeVpnGatewaySslServers.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslServersRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaySslServersResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGatewaySslServers", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewaySslServersResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DescribeVpnGateways(self, request):
        """本接口（DescribeVpnGateways）用于查询VPN网关列表。

        :param request: Request instance for DescribeVpnGateways.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DescribeVpnGatewaysResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DescribeVpnGateways", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DescribeVpnGatewaysResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachCcnInstances(self, request):
        """本接口（DetachCcnInstances）用于从云联网实例中解关联指定的网络实例。<br />
        解关联网络实例后，相应的路由策略会一并删除。

        :param request: Request instance for DetachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DetachClassicLinkVpc", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachClassicLinkVpcResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DetachNetworkInterface(self, request):
        """本接口（DetachNetworkInterface）用于弹性网卡解绑云服务器。
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for DetachNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DetachNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DetachNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DetachNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableCcnRoutes(self, request):
        """本接口（DisableCcnRoutes）用于禁用已经启用的云联网（CCN）路由

        :param request: Request instance for DisableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableGatewayFlowMonitor(self, request):
        """本接口（DisableGatewayFlowMonitor）用于关闭网关流量监控。

        :param request: Request instance for DisableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableGatewayFlowMonitor", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableGatewayFlowMonitorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableRoutes(self, request):
        """本接口（DisableRoutes）用于禁用已启用的子网路由

        :param request: Request instance for DisableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisableVpnGatewaySslClientCert(self, request):
        """禁用SSL-VPN-CLIENT 证书

        :param request: Request instance for DisableVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisableVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisableVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisableVpnGatewaySslClientCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisableVpnGatewaySslClientCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateAddress(self, request):
        """本接口 (DisassociateAddress) 用于解绑[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 支持CVM实例，弹性网卡上的EIP解绑
        * 不支持NAT上的EIP解绑。NAT上的EIP解绑请参考[DisassociateNatGatewayAddress](https://cloud.tencent.com/document/api/215/36716)
        * 只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。
        * EIP 如果被封堵，则不能进行解绑定操作。

        :param request: Request instance for DisassociateAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("DisassociateDhcpIpWithAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateDhcpIpWithAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateDirectConnectGatewayNatGateway(self, request):
        """将专线网关与NAT网关解绑，解绑之后，专线网关将不能通过NAT网关访问公网

        :param request: Request instance for DisassociateDirectConnectGatewayNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateDirectConnectGatewayNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateDirectConnectGatewayNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateDirectConnectGatewayNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateDirectConnectGatewayNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateNatGatewayAddress(self, request):
        """本接口（DisassociateNatGatewayAddress）用于NAT网关解绑弹性IP。

        :param request: Request instance for DisassociateNatGatewayAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNatGatewayAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNatGatewayAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNatGatewayAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateNetworkAclSubnets(self, request):
        """本接口（DisassociateNetworkAclSubnets）用于网络ACL解关联vpc下的子网。

        :param request: Request instance for DisassociateNetworkAclSubnets.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkAclSubnetsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNetworkAclSubnets", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNetworkAclSubnetsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateNetworkInterfaceSecurityGroups(self, request):
        """本接口（DisassociateNetworkInterfaceSecurityGroups）用于弹性网卡解绑安全组。支持弹性网卡完全解绑安全组。

        :param request: Request instance for DisassociateNetworkInterfaceSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateNetworkInterfaceSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateNetworkInterfaceSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateNetworkInterfaceSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DisassociateVpcEndPointSecurityGroups(self, request):
        """终端节点解绑安全组。

        :param request: Request instance for DisassociateVpcEndPointSecurityGroups.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DisassociateVpcEndPointSecurityGroupsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DisassociateVpcEndPointSecurityGroupsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DisassociateVpcEndPointSecurityGroups", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DisassociateVpcEndPointSecurityGroupsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadCustomerGatewayConfiguration(self, request):
        """本接口(DownloadCustomerGatewayConfiguration)用于下载VPN通道配置。

        :param request: Request instance for DownloadCustomerGatewayConfiguration.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadCustomerGatewayConfigurationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadCustomerGatewayConfiguration", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadCustomerGatewayConfigurationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def DownloadVpnGatewaySslClientCert(self, request):
        """下载SSL-VPN-CLIENT 客户端证书

        :param request: Request instance for DownloadVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.DownloadVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.DownloadVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("DownloadVpnGatewaySslClientCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.DownloadVpnGatewaySslClientCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableCcnRoutes(self, request):
        """本接口（EnableCcnRoutes）用于启用已经加入云联网（CCN）的路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。

        :param request: Request instance for EnableCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableGatewayFlowMonitor(self, request):
        """本接口（EnableGatewayFlowMonitor）用于开启网关流量监控。

        :param request: Request instance for EnableGatewayFlowMonitor.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableGatewayFlowMonitorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableGatewayFlowMonitor", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableGatewayFlowMonitorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableRoutes(self, request):
        """本接口（EnableRoutes）用于启用已禁用的子网路由。<br />
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。

        :param request: Request instance for EnableRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableVpcEndPointConnect(self, request):
        """是否接受终端节点连接请求。

        :param request: Request instance for EnableVpcEndPointConnect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableVpcEndPointConnectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableVpcEndPointConnectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableVpcEndPointConnect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableVpcEndPointConnectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def EnableVpnGatewaySslClientCert(self, request):
        """启用SSL-VPN-CLIENT 证书

        :param request: Request instance for EnableVpnGatewaySslClientCert.
        :type request: :class:`tencentcloud.vpc.v20170312.models.EnableVpnGatewaySslClientCertRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.EnableVpnGatewaySslClientCertResponse`

        """
        try:
            params = request._serialize()
            body = self.call("EnableVpnGatewaySslClientCert", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.EnableVpnGatewaySslClientCertResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def GetCcnRegionBandwidthLimits(self, request):
        """本接口（GetCcnRegionBandwidthLimits）用于查询云联网相关地域带宽信息，其中预付费模式的云联网仅支持地域间限速，后付费模式的云联网支持地域间限速和地域出口限速。

        :param request: Request instance for GetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.GetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.GetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("GetCcnRegionBandwidthLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.GetCcnRegionBandwidthLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HaVipAssociateAddressIp(self, request):
        """本接口（HaVipAssociateAddressIp）用于高可用虚拟IP（HAVIP）绑定弹性公网IP（EIP）。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for HaVipAssociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipAssociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HaVipAssociateAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HaVipAssociateAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def HaVipDisassociateAddressIp(self, request):
        """本接口（HaVipDisassociateAddressIp）用于将高可用虚拟IP（HAVIP）已绑定的弹性公网IP（EIP）解除绑定。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for HaVipDisassociateAddressIp.
        :type request: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.HaVipDisassociateAddressIpResponse`

        """
        try:
            params = request._serialize()
            body = self.call("HaVipDisassociateAddressIp", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.HaVipDisassociateAddressIpResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquirePriceCreateDirectConnectGateway(self, request):
        """本接口（DescribePriceCreateDirectConnectGateway）用于创建专线网关询价。

        :param request: Request instance for InquirePriceCreateDirectConnectGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquirePriceCreateDirectConnectGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquirePriceCreateDirectConnectGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquirePriceCreateDirectConnectGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquirePriceCreateDirectConnectGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceCreateVpnGateway(self, request):
        """本接口（InquiryPriceCreateVpnGateway）用于创建VPN网关询价。

        :param request: Request instance for InquiryPriceCreateVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceCreateVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceCreateVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceCreateVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceRenewVpnGateway(self, request):
        """本接口（InquiryPriceRenewVpnGateway）用于续费VPN网关询价。目前仅支持IPSEC类型网关的询价。

        :param request: Request instance for InquiryPriceRenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceRenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceRenewVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceRenewVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def InquiryPriceResetVpnGatewayInternetMaxBandwidth(self, request):
        """本接口（InquiryPriceResetVpnGatewayInternetMaxBandwidth）调整VPN网关带宽上限询价。

        :param request: Request instance for InquiryPriceResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("InquiryPriceResetVpnGatewayInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def MigrateNetworkInterface(self, request):
        """本接口（MigrateNetworkInterface）用于弹性网卡迁移。
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for MigrateNetworkInterface.
        :type request: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.MigrateNetworkInterfaceResponse`

        """
        try:
            params = request._serialize()
            body = self.call("MigrateNetworkInterface", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigrateNetworkInterfaceResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("MigratePrivateIpAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.MigratePrivateIpAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressAttribute(self, request):
        """本接口 (ModifyAddressAttribute) 用于修改[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）的名称。

        :param request: Request instance for ModifyAddressAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ModifyAddressInternetChargeType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressInternetChargeTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressTemplateAttribute(self, request):
        """本接口（ModifyAddressTemplateAttribute）用于修改IP地址模板

        :param request: Request instance for ModifyAddressTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressTemplateAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressTemplateAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressTemplateGroupAttribute(self, request):
        """本接口（ModifyAddressTemplateGroupAttribute）用于修改IP地址模板集合

        :param request: Request instance for ModifyAddressTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressTemplateGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressTemplateGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAddressesBandwidth(self, request):
        """本接口（ModifyAddressesBandwidth）用于调整[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)(简称EIP)带宽，支持后付费EIP, 预付费EIP和带宽包EIP

        :param request: Request instance for ModifyAddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyAssistantCidr(self, request):
        """本接口(ModifyAssistantCidr)用于批量修改辅助CIDR，支持新增和删除。（接口灰度中，如需使用请提工单。）

        :param request: Request instance for ModifyAssistantCidr.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyAssistantCidrResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyAssistantCidr", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyAssistantCidrResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyBandwidthPackageAttribute(self, request):
        """接口用于修改带宽包属性，包括带宽包名字等

        :param request: Request instance for ModifyBandwidthPackageAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyBandwidthPackageAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyBandwidthPackageAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyBandwidthPackageAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcnAttachedInstancesAttribute(self, request):
        """修改CCN关联实例属性，目前仅修改备注description

        :param request: Request instance for ModifyCcnAttachedInstancesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttachedInstancesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttachedInstancesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCcnAttachedInstancesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcnAttachedInstancesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcnAttribute(self, request):
        """本接口（ModifyCcnAttribute）用于修改云联网（CCN）的相关属性。

        :param request: Request instance for ModifyCcnAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCcnAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcnAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCcnRegionBandwidthLimitsType(self, request):
        """本接口（ModifyCcnRegionBandwidthLimitsType）用于修改后付费云联网实例修改带宽限速策略。

        :param request: Request instance for ModifyCcnRegionBandwidthLimitsType.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCcnRegionBandwidthLimitsTypeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCcnRegionBandwidthLimitsType", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCcnRegionBandwidthLimitsTypeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyCustomerGatewayAttribute(self, request):
        """本接口（ModifyCustomerGatewayAttribute）用于修改对端网关信息。

        :param request: Request instance for ModifyCustomerGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyCustomerGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyCustomerGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyCustomerGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDhcpIpAttribute(self, request):
        """本接口（ModifyDhcpIpAttribute）用于修改DhcpIp属性

        :param request: Request instance for ModifyDhcpIpAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyDhcpIpAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyDhcpIpAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDhcpIpAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDhcpIpAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyDirectConnectGatewayAttribute(self, request):
        """本接口（ModifyDirectConnectGatewayAttribute）用于修改专线网关属性

        :param request: Request instance for ModifyDirectConnectGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyDirectConnectGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyDirectConnectGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyDirectConnectGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyFlowLogAttribute(self, request):
        """本接口（ModifyFlowLogAttribute）用于修改流日志属性

        :param request: Request instance for ModifyFlowLogAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyFlowLogAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyFlowLogAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyFlowLogAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyGatewayFlowQos(self, request):
        """本接口（ModifyGatewayFlowQos）用于调整网关流控带宽。

        :param request: Request instance for ModifyGatewayFlowQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyGatewayFlowQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyGatewayFlowQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyGatewayFlowQosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyHaVipAttribute(self, request):
        """本接口（ModifyHaVipAttribute）用于修改高可用虚拟IP（HAVIP）属性

        :param request: Request instance for ModifyHaVipAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyHaVipAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyHaVipAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyHaVipAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIp6AddressesBandwidth(self, request):
        """该接口用于修改IPV6地址访问internet的带宽

        :param request: Request instance for ModifyIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIp6AddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIp6AddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIp6Rule(self, request):
        """该接口用于修改IPV6转换规则，当前仅支持修改转换规则名称，IPV4地址和IPV4端口号

        :param request: Request instance for ModifyIp6Rule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6RuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6RuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIp6Rule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIp6RuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIp6Translator(self, request):
        """该接口用于修改IP6转换实例属性，当前仅支持修改实例名称。

        :param request: Request instance for ModifyIp6Translator.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6TranslatorRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIp6TranslatorResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIp6Translator", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIp6TranslatorResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyIpv6AddressesAttribute(self, request):
        """本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡内网IPv6地址属性。

        :param request: Request instance for ModifyIpv6AddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyIpv6AddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyIpv6AddressesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyIpv6AddressesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyLocalGateway(self, request):
        """该接口用于修改CDC的本地网关。

        :param request: Request instance for ModifyLocalGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyLocalGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyLocalGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyLocalGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyLocalGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewayAttribute(self, request):
        """本接口（ModifyNatGatewayAttribute）用于修改NAT网关的属性。

        :param request: Request instance for ModifyNatGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewayDestinationIpPortTranslationNatRule(self, request):
        """本接口（ModifyNatGatewayDestinationIpPortTranslationNatRule）用于修改NAT网关端口转发规则。

        :param request: Request instance for ModifyNatGatewayDestinationIpPortTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewayDestinationIpPortTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNatGatewaySourceIpTranslationNatRule(self, request):
        """本接口（ModifyNatGatewaySourceIpTranslationNatRule）用于修改NAT网关SNAT转发规则。

        :param request: Request instance for ModifyNatGatewaySourceIpTranslationNatRule.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewaySourceIpTranslationNatRuleRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNatGatewaySourceIpTranslationNatRuleResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNatGatewaySourceIpTranslationNatRule", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNatGatewaySourceIpTranslationNatRuleResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetDetect(self, request):
        """本接口(ModifyNetDetect)用于修改网络探测参数。

        :param request: Request instance for ModifyNetDetect.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetDetectResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetDetect", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetDetectResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkAclAttribute(self, request):
        """本接口（ModifyNetworkAclAttribute）用于修改网络ACL属性。

        :param request: Request instance for ModifyNetworkAclAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkAclAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkAclAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkAclAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ModifyNetworkAclEntries", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkAclEntriesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkInterfaceAttribute(self, request):
        """本接口（ModifyNetworkInterfaceAttribute）用于修改弹性网卡属性。

        :param request: Request instance for ModifyNetworkInterfaceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkInterfaceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkInterfaceAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyNetworkInterfaceQos(self, request):
        """修改弹性网卡服务质量

        :param request: Request instance for ModifyNetworkInterfaceQos.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceQosRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyNetworkInterfaceQosResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyNetworkInterfaceQos", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyNetworkInterfaceQosResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyPrivateIpAddressesAttribute(self, request):
        """本接口（ModifyPrivateIpAddressesAttribute）用于修改弹性网卡内网IP属性。

        :param request: Request instance for ModifyPrivateIpAddressesAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyPrivateIpAddressesAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyPrivateIpAddressesAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyPrivateIpAddressesAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyRouteTableAttribute(self, request):
        """本接口（ModifyRouteTableAttribute）用于修改路由表（RouteTable）属性。

        :param request: Request instance for ModifyRouteTableAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyRouteTableAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyRouteTableAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyRouteTableAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupAttribute(self, request):
        """本接口（ModifySecurityGroupAttribute）用于修改安全组（SecurityGroupPolicy）属性。

        :param request: Request instance for ModifySecurityGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySecurityGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySecurityGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySecurityGroupPolicies(self, request):
        """本接口（ModifySecurityGroupPolicies）用于重置安全组出站和入站规则（SecurityGroupPolicy）。

        <ul>
        <li>该接口不支持自定义索引 PolicyIndex。</li>
        <li>在 SecurityGroupPolicySet 参数中：<ul>
        	<li> 如果指定 SecurityGroupPolicySet.Version 为0, 表示清空所有规则，并忽略 Egress 和 Ingress。</li>
        	<li> 如果指定 SecurityGroupPolicySet.Version 不为0, 在添加出站和入站规则（Egress 和 Ingress）时：<ul>
        		<li>Protocol 字段支持输入 TCP, UDP, ICMP, ICMPV6, GRE, ALL。</li>
        		<li>CidrBlock 字段允许输入符合 cidr 格式标准的任意字符串。(展开)在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        		<li>Ipv6CidrBlock 字段允许输入符合 IPv6 cidr 格式标准的任意字符串。(展开)在基础网络中，如果Ipv6CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IPv6，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
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
            body = self.call("ModifySecurityGroupPolicies", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySecurityGroupPoliciesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceTemplateAttribute(self, request):
        """本接口（ModifyServiceTemplateAttribute）用于修改协议端口模板

        :param request: Request instance for ModifyServiceTemplateAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceTemplateAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceTemplateAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyServiceTemplateGroupAttribute(self, request):
        """本接口（ModifyServiceTemplateGroupAttribute）用于修改协议端口模板集合。

        :param request: Request instance for ModifyServiceTemplateGroupAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyServiceTemplateGroupAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyServiceTemplateGroupAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyServiceTemplateGroupAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifySubnetAttribute(self, request):
        """本接口（ModifySubnetAttribute）用于修改子网属性。

        :param request: Request instance for ModifySubnetAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifySubnetAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifySubnetAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifySubnetAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyTemplateMember(self, request):
        """修改模板对象中的IP地址、协议端口、IP地址组、协议端口组。当前仅支持北京、泰国、北美地域请求。

        :param request: Request instance for ModifyTemplateMember.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyTemplateMemberRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyTemplateMemberResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyTemplateMember", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyTemplateMemberResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpcAttribute(self, request):
        """本接口（ModifyVpcAttribute）用于修改私有网络（VPC）的相关属性。

        :param request: Request instance for ModifyVpcAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpcEndPointAttribute(self, request):
        """修改终端节点属性。

        :param request: Request instance for ModifyVpcEndPointAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcEndPointAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcEndPointAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpcEndPointServiceAttribute(self, request):
        """本接口（ModifyVpcEndPointServiceAttribute）用于修改终端节点服务属性。


        :param request: Request instance for ModifyVpcEndPointServiceAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcEndPointServiceAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcEndPointServiceAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpcEndPointServiceWhiteList(self, request):
        """修改终端节点服务白名单属性。

        :param request: Request instance for ModifyVpcEndPointServiceWhiteList.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceWhiteListRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpcEndPointServiceWhiteListResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpcEndPointServiceWhiteList", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpcEndPointServiceWhiteListResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpnConnectionAttribute(self, request):
        """本接口（ModifyVpnConnectionAttribute）用于修改VPN通道。

        :param request: Request instance for ModifyVpnConnectionAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnConnectionAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnConnectionAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnConnectionAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpnGatewayAttribute(self, request):
        """本接口（ModifyVpnGatewayAttribute）用于修改VPN网关属性。

        :param request: Request instance for ModifyVpnGatewayAttribute.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayAttributeResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnGatewayAttribute", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnGatewayAttributeResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpnGatewayCcnRoutes(self, request):
        """本接口（ModifyVpnGatewayCcnRoutes）用于修改VPN网关云联网路由

        :param request: Request instance for ModifyVpnGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ModifyVpnGatewayRoutes(self, request):
        """修改VPN路由是否启用

        :param request: Request instance for ModifyVpnGatewayRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ModifyVpnGatewayRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ModifyVpnGatewayRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ModifyVpnGatewayRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def NotifyRoutes(self, request):
        """路由表列表页操作增加“发布到云联网”，用于发布路由到云联网。

        :param request: Request instance for NotifyRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.NotifyRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.NotifyRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("NotifyRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.NotifyRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RefreshDirectConnectGatewayRouteToNatGateway(self, request):
        """刷新专线直连nat路由，更新nat到专线的路由表

        :param request: Request instance for RefreshDirectConnectGatewayRouteToNatGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RefreshDirectConnectGatewayRouteToNatGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RefreshDirectConnectGatewayRouteToNatGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RefreshDirectConnectGatewayRouteToNatGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RefreshDirectConnectGatewayRouteToNatGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RejectAttachCcnInstances(self, request):
        """本接口（RejectAttachCcnInstances）用于跨账号关联实例时，云联网所有者拒绝关联操作。

        :param request: Request instance for RejectAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RejectAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RejectAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RejectAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


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
            body = self.call("ReleaseAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReleaseIp6AddressesBandwidth(self, request):
        """该接口用于给弹性公网IPv6地址释放带宽。

        :param request: Request instance for ReleaseIp6AddressesBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReleaseIp6AddressesBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReleaseIp6AddressesBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReleaseIp6AddressesBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveBandwidthPackageResources(self, request):
        """接口用于删除带宽包资源，包括[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)和[负载均衡](https://cloud.tencent.com/document/product/214/517)等

        :param request: Request instance for RemoveBandwidthPackageResources.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveBandwidthPackageResourcesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveBandwidthPackageResources", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveBandwidthPackageResourcesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RemoveIp6Rules(self, request):
        """1. 该接口用于删除IPV6转换规则
        2. 支持批量删除同一个转换实例下的多个转换规则

        :param request: Request instance for RemoveIp6Rules.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RemoveIp6RulesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RemoveIp6RulesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RemoveIp6Rules", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RemoveIp6RulesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewAddresses(self, request):
        """该接口用于续费包月带宽计费模式的弹性公网IP

        :param request: Request instance for RenewAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RenewAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RenewAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def RenewVpnGateway(self, request):
        """本接口（RenewVpnGateway）用于预付费（包年包月）VPN网关续费。目前只支持IPSEC网关。

        :param request: Request instance for RenewVpnGateway.
        :type request: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.RenewVpnGatewayResponse`

        """
        try:
            params = request._serialize()
            body = self.call("RenewVpnGateway", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.RenewVpnGatewayResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceDirectConnectGatewayCcnRoutes(self, request):
        """本接口（ReplaceDirectConnectGatewayCcnRoutes）根据路由ID（RouteId）修改指定的路由（Route），支持批量修改。

        :param request: Request instance for ReplaceDirectConnectGatewayCcnRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceDirectConnectGatewayCcnRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceDirectConnectGatewayCcnRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceDirectConnectGatewayCcnRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRouteTableAssociation(self, request):
        """本接口（ReplaceRouteTableAssociation)用于修改子网（Subnet）关联的路由表（RouteTable）。
        * 一个子网只能关联一个路由表。

        :param request: Request instance for ReplaceRouteTableAssociation.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRouteTableAssociationResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceRouteTableAssociation", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceRouteTableAssociationResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceRoutes(self, request):
        """本接口（ReplaceRoutes）根据路由策略ID（RouteId）修改指定的路由策略（Route），支持批量修改。

        :param request: Request instance for ReplaceRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ReplaceSecurityGroupPolicy(self, request):
        """本接口（ReplaceSecurityGroupPolicy）用于替换单条安全组规则（SecurityGroupPolicy）。
        单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。

        :param request: Request instance for ReplaceSecurityGroupPolicy.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ReplaceSecurityGroupPolicyResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ReplaceSecurityGroupPolicy", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ReplaceSecurityGroupPolicyResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetAttachCcnInstances(self, request):
        """本接口（ResetAttachCcnInstances）用于跨账号关联实例申请过期时，重新申请关联操作。

        :param request: Request instance for ResetAttachCcnInstances.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetAttachCcnInstancesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetAttachCcnInstances", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetAttachCcnInstancesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetNatGatewayConnection(self, request):
        """本接口（ResetNatGatewayConnection）用来NAT网关并发连接上限。

        :param request: Request instance for ResetNatGatewayConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetNatGatewayConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetNatGatewayConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetNatGatewayConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetRoutes(self, request):
        """本接口（ResetRoutes）用于对某个路由表名称和所有路由策略（Route）进行重新设置。<br />
        注意: 调用本接口是先删除当前路由表中所有路由策略, 再保存新提交的路由策略内容, 会引起网络中断。

        :param request: Request instance for ResetRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetVpnConnection(self, request):
        """本接口(ResetVpnConnection)用于重置VPN通道。

        :param request: Request instance for ResetVpnConnection.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnConnectionResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetVpnConnection", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetVpnConnectionResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def ResetVpnGatewayInternetMaxBandwidth(self, request):
        """本接口（ResetVpnGatewayInternetMaxBandwidth）调整VPN网关带宽上限。目前支持升级配置，如果是包年包月VPN网关需要在有效期内。

        :param request: Request instance for ResetVpnGatewayInternetMaxBandwidth.
        :type request: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.ResetVpnGatewayInternetMaxBandwidthResponse`

        """
        try:
            params = request._serialize()
            body = self.call("ResetVpnGatewayInternetMaxBandwidth", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.ResetVpnGatewayInternetMaxBandwidthResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def SetCcnRegionBandwidthLimits(self, request):
        """本接口（SetCcnRegionBandwidthLimits）用于设置云联网（CCN）各地域出带宽上限，或者地域间带宽上限。

        :param request: Request instance for SetCcnRegionBandwidthLimits.
        :type request: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.SetCcnRegionBandwidthLimitsResponse`

        """
        try:
            params = request._serialize()
            body = self.call("SetCcnRegionBandwidthLimits", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.SetCcnRegionBandwidthLimitsResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def TransformAddress(self, request):
        """本接口 (TransformAddress) 用于将实例的普通公网 IP 转换为[弹性公网IP](https://cloud.tencent.com/document/product/213/1941)（简称 EIP）。
        * 平台对用户每地域每日解绑 EIP 重新分配普通公网 IP 次数有所限制（可参见 [EIP 产品简介](/document/product/213/1941)）。上述配额可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。

        :param request: Request instance for TransformAddress.
        :type request: :class:`tencentcloud.vpc.v20170312.models.TransformAddressRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.TransformAddressResponse`

        """
        try:
            params = request._serialize()
            body = self.call("TransformAddress", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.TransformAddressResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6Addresses(self, request):
        """本接口（UnassignIpv6Addresses）用于释放弹性网卡`IPv6`地址。<br />
        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for UnassignIpv6Addresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6AddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6Addresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6AddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6CidrBlock(self, request):
        """本接口（UnassignIpv6CidrBlock）用于释放IPv6网段。<br />
        网段如果还有IP占用且未回收，则网段无法释放。

        :param request: Request instance for UnassignIpv6CidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6CidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6CidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6CidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignIpv6SubnetCidrBlock(self, request):
        """本接口（UnassignIpv6SubnetCidrBlock）用于释放IPv6子网段。<br />
        子网段如果还有IP占用且未回收，则子网段无法释放。

        :param request: Request instance for UnassignIpv6SubnetCidrBlock.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignIpv6SubnetCidrBlockResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignIpv6SubnetCidrBlock", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignIpv6SubnetCidrBlockResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def UnassignPrivateIpAddresses(self, request):
        """本接口（UnassignPrivateIpAddresses）用于弹性网卡退还内网 IP。
        * 退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。

        本接口是异步完成，如需查询异步任务执行结果，请使用本接口返回的`RequestId`轮询`DescribeVpcTaskResult`接口。

        :param request: Request instance for UnassignPrivateIpAddresses.
        :type request: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.UnassignPrivateIpAddressesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("UnassignPrivateIpAddresses", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.UnassignPrivateIpAddressesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)


    def WithdrawNotifyRoutes(self, request):
        """路由表列表页操作增加“从云联网撤销”，用于撤销已发布到云联网的路由。

        :param request: Request instance for WithdrawNotifyRoutes.
        :type request: :class:`tencentcloud.vpc.v20170312.models.WithdrawNotifyRoutesRequest`
        :rtype: :class:`tencentcloud.vpc.v20170312.models.WithdrawNotifyRoutesResponse`

        """
        try:
            params = request._serialize()
            body = self.call("WithdrawNotifyRoutes", params)
            response = json.loads(body)
            if "Error" not in response["Response"]:
                model = models.WithdrawNotifyRoutesResponse()
                model._deserialize(response["Response"])
                return model
            else:
                code = response["Response"]["Error"]["Code"]
                message = response["Response"]["Error"]["Message"]
                reqid = response["Response"]["RequestId"]
                raise TencentCloudSDKException(code, message, reqid)
        except Exception as e:
            if isinstance(e, TencentCloudSDKException):
                raise
            else:
                raise TencentCloudSDKException(e.message, e.message)