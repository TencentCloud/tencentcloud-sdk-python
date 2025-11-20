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
from tencentcloud.ecm.v20190719 import models
from typing import Dict


class EcmClient(AbstractClient):
    _apiVersion = '2019-07-19'
    _endpoint = 'ecm.tencentcloudapi.com'
    _service = 'ecm'

    async def AllocateAddresses(
            self,
            request: models.AllocateAddressesRequest,
            opts: Dict = None,
    ) -> models.AllocateAddressesResponse:
        """
        申请一个或多个弹性公网IP（简称 EIP）
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AllocateIpv6AddressesBandwidth(
            self,
            request: models.AllocateIpv6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.AllocateIpv6AddressesBandwidthResponse:
        """
        本接口用于给IPv6地址分配公网带宽
        """
        
        kwargs = {}
        kwargs["action"] = "AllocateIpv6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AllocateIpv6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6Addresses(
            self,
            request: models.AssignIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6AddressesResponse:
        """
        本接口（AssignIpv6Addresses）用于弹性网卡申请IPv6地址。
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

        使用本接口前，您需要已有VPC实例，如果没有可通过接口CreateVpc创建。
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6CidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6CidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssignIpv6CidrBlocks(
            self,
            request: models.AssignIpv6CidrBlocksRequest,
            opts: Dict = None,
    ) -> models.AssignIpv6CidrBlocksResponse:
        """
        本接口（AssignIpv6CidrBlocks）用于分配IPv6网段。

        使用本接口前，您需要已有VPC实例，如果没有可通过接口CreateVpc创建。
        每个VPC 可以同时支持运营商网络('CMCC'-中国移动, 'CTCC'-中国电信, 'CUCC'-中国联调)。本接口可以同时申请不同类型的IPv6网段
        """
        
        kwargs = {}
        kwargs["action"] = "AssignIpv6CidrBlocks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssignIpv6CidrBlocksResponse
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

        给子网分配 IPv6 网段，要求子网所属 VPC 已获得 IPv6 网段。如果尚未分配，请先通过接口 AssignIpv6CidrBlock 给子网所属 VPC 分配一个 IPv6 网段。否则无法分配 IPv6 子网段。
        每个子网只能分配一个IPv6网段。
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
        弹性网卡申请内网 IP
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
        将弹性公网IP（简称 EIP）绑定到实例或弹性网卡的指定内网 IP 上。
        将 EIP 绑定到实例（ECM）上，其本质是将 EIP 绑定到实例上主网卡的主内网 IP 上。
        将 EIP 绑定到指定网卡的内网 IP上，内网IP已经绑定了EIP或普通公网IP，则反馈失败。必须先解绑该 EIP，才能再绑定新的。
        只有状态为 UNBIND 的 EIP 才能够绑定内网IP。
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AssociateSecurityGroups(
            self,
            request: models.AssociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.AssociateSecurityGroupsResponse:
        """
        绑定安全组
        """
        
        kwargs = {}
        kwargs["action"] = "AssociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AssociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachDisks(
            self,
            request: models.AttachDisksRequest,
            opts: Dict = None,
    ) -> models.AttachDisksResponse:
        """
        CBS在ECM早已下线

        本接口（AttachDisks）用于挂载云硬盘。

        * 支持批量操作，将多块云盘挂载到同一云主机。如果多个云盘中存在不允许挂载的云盘，则操作不执行，返回特定的错误码。
        * 本接口为异步接口，当挂载云盘的请求成功返回时，表示后台已发起挂载云盘的操作，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态由“ATTACHING”变为“ATTACHED”，则为挂载成功。
        """
        
        kwargs = {}
        kwargs["action"] = "AttachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def AttachNetworkInterface(
            self,
            request: models.AttachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.AttachNetworkInterfaceResponse:
        """
        弹性网卡绑定云主机
        """
        
        kwargs = {}
        kwargs["action"] = "AttachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.AttachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchDeregisterTargets(
            self,
            request: models.BatchDeregisterTargetsRequest,
            opts: Dict = None,
    ) -> models.BatchDeregisterTargetsResponse:
        """
        批量解绑后端服务。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchDeregisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchDeregisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchModifyTargetWeight(
            self,
            request: models.BatchModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.BatchModifyTargetWeightResponse:
        """
        批量修改监听器绑定的后端机器的转发权重。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def BatchRegisterTargets(
            self,
            request: models.BatchRegisterTargetsRequest,
            opts: Dict = None,
    ) -> models.BatchRegisterTargetsResponse:
        """
        批量绑定后端目标。
        """
        
        kwargs = {}
        kwargs["action"] = "BatchRegisterTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.BatchRegisterTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateDisks(
            self,
            request: models.CreateDisksRequest,
            opts: Dict = None,
    ) -> models.CreateDisksResponse:
        """
        CBS在ECM早已下线

        本接口（CreateDisks）用于创建云硬盘。

        * 预付费云盘的购买会预先扣除本次云盘购买所需金额，在调用本接口前请确保账户余额充足。
        * 本接口支持传入数据盘快照来创建云盘，实现将快照数据复制到新购云盘上。
        * 本接口为异步接口，当创建请求下发成功后会返回一个新建的云盘ID列表，此时云盘的创建并未立即完成。可以通过调用[DescribeDisks](/document/product/362/16315)接口根据DiskId查询对应云盘，如果能查到云盘，且状态为'UNATTACHED'或'ATTACHED'，则表示创建成功。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateHaVip(
            self,
            request: models.CreateHaVipRequest,
            opts: Dict = None,
    ) -> models.CreateHaVipResponse:
        """
        本接口（CreateHaVip）用于创建高可用虚拟IP（HAVIP）
        """
        
        kwargs = {}
        kwargs["action"] = "CreateHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateImage(
            self,
            request: models.CreateImageRequest,
            opts: Dict = None,
    ) -> models.CreateImageResponse:
        """
        本接口(CreateImage)用于将实例的系统盘制作为新镜像，创建后的镜像可以用于创建实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateKeyPair(
            self,
            request: models.CreateKeyPairRequest,
            opts: Dict = None,
    ) -> models.CreateKeyPairResponse:
        """
        用于创建一个 OpenSSH RSA 密钥对，可以用于登录 Linux 实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateKeyPair"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateKeyPairResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateListener(
            self,
            request: models.CreateListenerRequest,
            opts: Dict = None,
    ) -> models.CreateListenerResponse:
        """
        创建负载均衡监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateLoadBalancer(
            self,
            request: models.CreateLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.CreateLoadBalancerResponse:
        """
        购买负载均衡实例。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateModule(
            self,
            request: models.CreateModuleRequest,
            opts: Dict = None,
    ) -> models.CreateModuleResponse:
        """
        创建模块
        """
        
        kwargs = {}
        kwargs["action"] = "CreateModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateNetworkInterface(
            self,
            request: models.CreateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.CreateNetworkInterfaceResponse:
        """
        创建弹性网卡
        """
        
        kwargs = {}
        kwargs["action"] = "CreateNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateRouteTable(
            self,
            request: models.CreateRouteTableRequest,
            opts: Dict = None,
    ) -> models.CreateRouteTableResponse:
        """
        创建了VPC后，系统会创建一个默认路由表，所有新建的子网都会关联到默认路由表。默认情况下您可以直接使用默认路由表来管理您的路由策略。当您的路由策略较多时，您可以调用创建路由表接口创建更多路由表管理您的路由策略。
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
        创建路由策略
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
        创建安全组
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
        <p>本接口（CreateSecurityGroupPolicies）用于创建安全组规则（SecurityGroupPolicy）。</p>
        <p>在 SecurityGroupPolicySet 参数中：</p>
        <ul>
        <li>Version 安全组规则版本号，用户每次更新安全规则版本会自动加1，防止您更新的路由规则已过期，不填不考虑冲突。</li>
        <li>在创建出站和入站规则（Egress 和 Ingress）时：<ul>
        <li>Protocol 字段支持输入TCP, UDP, ICMP, GRE, ALL。</li>
        <li>CidrBlock 字段允许输入符合cidr格式标准的任意字符串。在基础网络中，如果 CidrBlock 包含您的账户内的云服务器之外的设备在腾讯云的内网 IP，并不代表此规则允许您访问这些设备，租户之间网络隔离规则优先于安全组中的内网规则。</li>
        <li>SecurityGroupId 字段允许输入与待修改的安全组位于相同项目中的安全组 ID，包括这个安全组 ID 本身，代表安全组下所有云服务器的内网 IP。使用这个字段时，这条规则用来匹配网络报文的过程中会随着被使用的这个 ID 所关联的云服务器变化而变化，不需要重新修改。</li>
        <li>Port 字段允许输入一个单独端口号，或者用减号分隔的两个端口号代表端口范围，例如80或8000-8010。只有当 Protocol 字段是 TCP 或 UDP 时，Port 字段才被接受，即 Protocol 字段不是 TCP 或 UDP 时，Protocol 和 Port 排他关系，不允许同时输入，否则会接口报错。</li>
        <li>Action 字段只允许输入 ACCEPT 或 DROP。</li>
        <li>CidrBlock, SecurityGroupId, AddressTemplate 是排他关系，不允许同时输入，Protocol + Port 和 ServiceTemplate 二者是排他关系，不允许同时输入。</li>
        <li>一次请求中只能创建单个方向的规则, 如果需要指定索引（PolicyIndex）参数, 多条规则的索引必须一致。</li>
        </ul></li></ul>
        <p>默认接口请求频率限制：20次/秒。</p>
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateSubnet(
            self,
            request: models.CreateSubnetRequest,
            opts: Dict = None,
    ) -> models.CreateSubnetResponse:
        """
        创建子网，若创建成功，则此子网会成为此可用区的默认子网。
        """
        
        kwargs = {}
        kwargs["action"] = "CreateSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def CreateVpc(
            self,
            request: models.CreateVpcRequest,
            opts: Dict = None,
    ) -> models.CreateVpcResponse:
        """
        创建私有网络
        """
        
        kwargs = {}
        kwargs["action"] = "CreateVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.CreateVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteHaVip(
            self,
            request: models.DeleteHaVipRequest,
            opts: Dict = None,
    ) -> models.DeleteHaVipResponse:
        """
        用于删除高可用虚拟IP（HAVIP）
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteHaVip"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteHaVipResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteImage(
            self,
            request: models.DeleteImageRequest,
            opts: Dict = None,
    ) -> models.DeleteImageResponse:
        """
        删除镜像
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteListener(
            self,
            request: models.DeleteListenerRequest,
            opts: Dict = None,
    ) -> models.DeleteListenerResponse:
        """
        删除负载均衡监听器。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancer(
            self,
            request: models.DeleteLoadBalancerRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerResponse:
        """
        删除负载均衡实例。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancer"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteLoadBalancerListeners(
            self,
            request: models.DeleteLoadBalancerListenersRequest,
            opts: Dict = None,
    ) -> models.DeleteLoadBalancerListenersResponse:
        """
        删除负载均衡多个监听器
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteLoadBalancerListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteLoadBalancerListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteModule(
            self,
            request: models.DeleteModuleRequest,
            opts: Dict = None,
    ) -> models.DeleteModuleResponse:
        """
        删除业务模块
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteNetworkInterface(
            self,
            request: models.DeleteNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DeleteNetworkInterfaceResponse:
        """
        删除弹性网卡
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteRouteTable(
            self,
            request: models.DeleteRouteTableRequest,
            opts: Dict = None,
    ) -> models.DeleteRouteTableResponse:
        """
        删除路由表
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
        对某个路由表批量删除路由策略
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
        只有当前账号下的安全组允许被删除。
        安全组实例ID如果在其他安全组的规则中被引用，则无法直接删除。这种情况下，需要先进行规则修改，再删除安全组。
        删除的安全组无法再找回，请谨慎调用。
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
        SecurityGroupPolicySet.Version 用于指定要操作的安全组的版本。传入 Version 版本号若不等于当前安全组的最新版本，将返回失败；若不传 Version 则直接删除指定PolicyIndex的规则。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSnapshots(
            self,
            request: models.DeleteSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DeleteSnapshotsResponse:
        """
        CBS在ECM早已下线

        本接口（DeleteSnapshots）用于删除快照。

        * 快照必须处于NORMAL状态，快照状态可以通过[DescribeSnapshots](/document/product/362/15647)接口查询，见输出参数中SnapshotState字段解释。
        * 支持批量操作。如果多个快照存在无法删除的快照，则操作不执行，以返回特定的错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteSubnet(
            self,
            request: models.DeleteSubnetRequest,
            opts: Dict = None,
    ) -> models.DeleteSubnetResponse:
        """
        删除子网，若子网为可用区下的默认子网，则默认子网会回退到系统自动创建的默认子网，非用户最新创建的子网。若默认子网不满足需求，可调用设置默认子网接口设置。
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DeleteVpc(
            self,
            request: models.DeleteVpcRequest,
            opts: Dict = None,
    ) -> models.DeleteVpcResponse:
        """
        删除私有网络
        """
        
        kwargs = {}
        kwargs["action"] = "DeleteVpc"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DeleteVpcResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddressQuota(
            self,
            request: models.DescribeAddressQuotaRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressQuotaResponse:
        """
        查询您账户的弹性公网IP（简称 EIP）在当前地域的配额信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddressQuota"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressQuotaResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeAddresses(
            self,
            request: models.DescribeAddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeAddressesResponse:
        """
        查询弹性公网IP列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeBaseOverview(
            self,
            request: models.DescribeBaseOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribeBaseOverviewResponse:
        """
        获取概览页统计的基本数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeBaseOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeBaseOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeConfig(
            self,
            request: models.DescribeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeConfigResponse:
        """
        获取带宽硬盘等数据的限制
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeCustomImageTask(
            self,
            request: models.DescribeCustomImageTaskRequest,
            opts: Dict = None,
    ) -> models.DescribeCustomImageTaskResponse:
        """
        查询导入镜像任务
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeCustomImageTask"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeCustomImageTaskResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDefaultSubnet(
            self,
            request: models.DescribeDefaultSubnetRequest,
            opts: Dict = None,
    ) -> models.DescribeDefaultSubnetResponse:
        """
        查询可用区的默认子网
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDefaultSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDefaultSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeDisks(
            self,
            request: models.DescribeDisksRequest,
            opts: Dict = None,
    ) -> models.DescribeDisksResponse:
        """
        CBS在ECM早已下线

        本接口（DescribeDisks）用于查询云硬盘列表。

        * 可以根据云硬盘ID、云硬盘类型或者云硬盘状态等信息来查询云硬盘的详细信息，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        * 如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的云硬盘列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeHaVips(
            self,
            request: models.DescribeHaVipsRequest,
            opts: Dict = None,
    ) -> models.DescribeHaVipsResponse:
        """
        用于查询高可用虚拟IP（HAVIP）列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeHaVips"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeHaVipsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImage(
            self,
            request: models.DescribeImageRequest,
            opts: Dict = None,
    ) -> models.DescribeImageResponse:
        """
        展示镜像列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeImportImageOs(
            self,
            request: models.DescribeImportImageOsRequest,
            opts: Dict = None,
    ) -> models.DescribeImportImageOsResponse:
        """
        查询外部导入镜像支持的OS列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeImportImageOs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeImportImageOsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceTypeConfig(
            self,
            request: models.DescribeInstanceTypeConfigRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceTypeConfigResponse:
        """
        获取机型配置列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceTypeConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceTypeConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstanceVncUrl(
            self,
            request: models.DescribeInstanceVncUrlRequest,
            opts: Dict = None,
    ) -> models.DescribeInstanceVncUrlResponse:
        """
        查询实例管理终端地址
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstanceVncUrl"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstanceVncUrlResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstances(
            self,
            request: models.DescribeInstancesRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesResponse:
        """
        获取实例的相关信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeInstancesDeniedActions(
            self,
            request: models.DescribeInstancesDeniedActionsRequest,
            opts: Dict = None,
    ) -> models.DescribeInstancesDeniedActionsResponse:
        """
        通过实例id获取当前禁止的操作
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeInstancesDeniedActions"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeInstancesDeniedActionsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeListeners(
            self,
            request: models.DescribeListenersRequest,
            opts: Dict = None,
    ) -> models.DescribeListenersResponse:
        """
        查询负载均衡的监听器列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeListeners"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeListenersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalanceTaskStatus(
            self,
            request: models.DescribeLoadBalanceTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalanceTaskStatusResponse:
        """
        查询负载均衡相关的任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalanceTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalanceTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeLoadBalancers(
            self,
            request: models.DescribeLoadBalancersRequest,
            opts: Dict = None,
    ) -> models.DescribeLoadBalancersResponse:
        """
        查询负载均衡实例列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeLoadBalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeLoadBalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModule(
            self,
            request: models.DescribeModuleRequest,
            opts: Dict = None,
    ) -> models.DescribeModuleResponse:
        """
        获取模块列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModule"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModuleResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeModuleDetail(
            self,
            request: models.DescribeModuleDetailRequest,
            opts: Dict = None,
    ) -> models.DescribeModuleDetailResponse:
        """
        展示模块详细信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeModuleDetail"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeModuleDetailResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeMonthPeakNetwork(
            self,
            request: models.DescribeMonthPeakNetworkRequest,
            opts: Dict = None,
    ) -> models.DescribeMonthPeakNetworkResponse:
        """
        获取客户节点上的出入带宽月峰和计费带宽信息
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeMonthPeakNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeMonthPeakNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNetworkInterfaces(
            self,
            request: models.DescribeNetworkInterfacesRequest,
            opts: Dict = None,
    ) -> models.DescribeNetworkInterfacesResponse:
        """
        查询弹性网卡列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNetworkInterfaces"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNetworkInterfacesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeNode(
            self,
            request: models.DescribeNodeRequest,
            opts: Dict = None,
    ) -> models.DescribeNodeResponse:
        """
        获取节点列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeNode"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeNodeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePackingQuotaGroup(
            self,
            request: models.DescribePackingQuotaGroupRequest,
            opts: Dict = None,
    ) -> models.DescribePackingQuotaGroupResponse:
        """
        使用本接口获取某种机型在某些区域的装箱配额（当使用虚拟机型时，返回的是一组相互关联的装箱配额）。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePackingQuotaGroup"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePackingQuotaGroupResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakBaseOverview(
            self,
            request: models.DescribePeakBaseOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePeakBaseOverviewResponse:
        """
        CPU 内存 硬盘等基础信息峰值数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakBaseOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakBaseOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePeakNetworkOverview(
            self,
            request: models.DescribePeakNetworkOverviewRequest,
            opts: Dict = None,
    ) -> models.DescribePeakNetworkOverviewResponse:
        """
        获取网络峰值数据
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePeakNetworkOverview"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePeakNetworkOverviewResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribePriceRunInstance(
            self,
            request: models.DescribePriceRunInstanceRequest,
            opts: Dict = None,
    ) -> models.DescribePriceRunInstanceResponse:
        """
        查询实例价格
        """
        
        kwargs = {}
        kwargs["action"] = "DescribePriceRunInstance"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribePriceRunInstanceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRegionIpv6Addresses(
            self,
            request: models.DescribeRegionIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.DescribeRegionIpv6AddressesResponse:
        """
        该接口（DescribeRegionIpv6Addresses）用于查询ECM地域之下的IPV6地址信息。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRegionIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRegionIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteConflicts(
            self,
            request: models.DescribeRouteConflictsRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteConflictsResponse:
        """
        查询自定义路由策略与云联网路由策略冲突列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteConflicts"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteConflictsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeRouteTables(
            self,
            request: models.DescribeRouteTablesRequest,
            opts: Dict = None,
    ) -> models.DescribeRouteTablesResponse:
        """
        查询路由表对象列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeRouteTables"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeRouteTablesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupAssociationStatistics(
            self,
            request: models.DescribeSecurityGroupAssociationStatisticsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupAssociationStatisticsResponse:
        """
        查询安全组关联实例统计
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupAssociationStatistics"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupAssociationStatisticsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroupLimits(
            self,
            request: models.DescribeSecurityGroupLimitsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupLimitsResponse:
        """
        查询用户安全组配额
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
        查询安全组规则
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupPoliciesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSecurityGroups(
            self,
            request: models.DescribeSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DescribeSecurityGroupsResponse:
        """
        查看安全组
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSnapshots(
            self,
            request: models.DescribeSnapshotsRequest,
            opts: Dict = None,
    ) -> models.DescribeSnapshotsResponse:
        """
        CBS在ECM早已下线

        本接口（DescribeSnapshots）用于查询快照的详细信息。

        * 根据快照ID、创建快照的云硬盘ID、创建快照的云硬盘类型等对结果进行过滤，不同条件之间为与(AND)的关系，过滤信息详细请见过滤器`Filter`。
        *  如果参数为空，返回当前用户一定数量（`Limit`所指定的数量，默认为20）的快照列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSnapshots"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSnapshotsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeSubnets(
            self,
            request: models.DescribeSubnetsRequest,
            opts: Dict = None,
    ) -> models.DescribeSubnetsResponse:
        """
        查询子网列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeSubnets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeSubnetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargetHealth(
            self,
            request: models.DescribeTargetHealthRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetHealthResponse:
        """
        获取负载均衡后端服务的健康检查状态。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargetHealth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetHealthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTargets(
            self,
            request: models.DescribeTargetsRequest,
            opts: Dict = None,
    ) -> models.DescribeTargetsResponse:
        """
        查询负载均衡绑定的后端服务列表。
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTargets"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTargetsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskResult(
            self,
            request: models.DescribeTaskResultRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskResultResponse:
        """
        查询EIP异步任务执行结果
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeTaskStatus(
            self,
            request: models.DescribeTaskStatusRequest,
            opts: Dict = None,
    ) -> models.DescribeTaskStatusResponse:
        """
        本接口(DescribeTaskStatus)用于获取异步任务状态
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeTaskStatus"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeTaskStatusResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DescribeVpcs(
            self,
            request: models.DescribeVpcsRequest,
            opts: Dict = None,
    ) -> models.DescribeVpcsResponse:
        """
        查询私有网络列表
        """
        
        kwargs = {}
        kwargs["action"] = "DescribeVpcs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DescribeVpcsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachDisks(
            self,
            request: models.DetachDisksRequest,
            opts: Dict = None,
    ) -> models.DetachDisksResponse:
        """
        CBS在ECM早已下线

        本接口（DetachDisks）用于卸载云硬盘。

        * 支持批量操作，卸载挂载在同一主机上的多块云盘。如果多块云盘中存在不允许卸载的云盘，则操作不执行，返回特定的错误码。
        * 本接口为异步接口，当请求成功返回时，云盘并未立即从主机卸载，可通过接口[DescribeDisks](/document/product/362/16315)来查询对应云盘的状态，如果云盘的状态由“ATTACHED”变为“UNATTACHED”，则为卸载成功。
        """
        
        kwargs = {}
        kwargs["action"] = "DetachDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DetachNetworkInterface(
            self,
            request: models.DetachNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.DetachNetworkInterfaceResponse:
        """
        弹性网卡解绑云主机
        """
        
        kwargs = {}
        kwargs["action"] = "DetachNetworkInterface"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DetachNetworkInterfaceResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisableRoutes(
            self,
            request: models.DisableRoutesRequest,
            opts: Dict = None,
    ) -> models.DisableRoutesResponse:
        """
        禁用已启用的子网路由
        """
        
        kwargs = {}
        kwargs["action"] = "DisableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateAddress(
            self,
            request: models.DisassociateAddressRequest,
            opts: Dict = None,
    ) -> models.DisassociateAddressResponse:
        """
        解绑弹性公网IP（简称 EIP）
        只有状态为 BIND 和 BIND_ENI 的 EIP 才能进行解绑定操作。
        EIP 如果被封堵，则不能进行解绑定操作。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateAddress"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateAddressResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateInstancesKeyPairs(
            self,
            request: models.DisassociateInstancesKeyPairsRequest,
            opts: Dict = None,
    ) -> models.DisassociateInstancesKeyPairsResponse:
        """
        用于解除实例的密钥绑定关系。
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateInstancesKeyPairs"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateInstancesKeyPairsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def DisassociateSecurityGroups(
            self,
            request: models.DisassociateSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.DisassociateSecurityGroupsResponse:
        """
        解绑安全组
        """
        
        kwargs = {}
        kwargs["action"] = "DisassociateSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.DisassociateSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def EnableRoutes(
            self,
            request: models.EnableRoutesRequest,
            opts: Dict = None,
    ) -> models.EnableRoutesResponse:
        """
        启用已禁用的子网路由。
        本接口会校验启用后，是否与已有路由冲突，如果冲突，则无法启用，失败处理。路由冲突时，需要先禁用与之冲突的路由，才能启用该路由。
        """
        
        kwargs = {}
        kwargs["action"] = "EnableRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.EnableRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportCustomImage(
            self,
            request: models.ImportCustomImageRequest,
            opts: Dict = None,
    ) -> models.ImportCustomImageResponse:
        """
        导入自定义镜像，支持 RAW、VHD、QCOW2、VMDK 镜像格式
        """
        
        kwargs = {}
        kwargs["action"] = "ImportCustomImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportCustomImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ImportImage(
            self,
            request: models.ImportImageRequest,
            opts: Dict = None,
    ) -> models.ImportImageResponse:
        """
        从CVM产品导入镜像到ECM
        """
        
        kwargs = {}
        kwargs["action"] = "ImportImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ImportImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def MigrateNetworkInterface(
            self,
            request: models.MigrateNetworkInterfaceRequest,
            opts: Dict = None,
    ) -> models.MigrateNetworkInterfaceResponse:
        """
        弹性网卡迁移
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
        弹性网卡内网IP迁移。
        该接口用于将一个内网IP从一个弹性网卡上迁移到另外一个弹性网卡，主IP地址不支持迁移。
        迁移前后的弹性网卡必须在同一个子网内。
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
        修改弹性公网IP属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyAddressesBandwidth(
            self,
            request: models.ModifyAddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyAddressesBandwidthResponse:
        """
        调整弹性公网IP带宽
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyAddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyAddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyDefaultSubnet(
            self,
            request: models.ModifyDefaultSubnetRequest,
            opts: Dict = None,
    ) -> models.ModifyDefaultSubnetResponse:
        """
        修改在一个可用区下创建实例时使用的默认子网（创建实例时，未填写VPC参数时使用的sunbetId）
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyDefaultSubnet"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyDefaultSubnetResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyHaVipAttribute(
            self,
            request: models.ModifyHaVipAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyHaVipAttributeResponse:
        """
        用于修改高可用虚拟IP（HAVIP）属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyHaVipAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyHaVipAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyImageAttribute(
            self,
            request: models.ModifyImageAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyImageAttributeResponse:
        """
        本接口（ModifyImageAttribute）用于修改镜像属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyImageAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyImageAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyInstancesAttribute(
            self,
            request: models.ModifyInstancesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyInstancesAttributeResponse:
        """
        修改实例的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyInstancesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyInstancesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpv6AddressesAttribute(
            self,
            request: models.ModifyIpv6AddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyIpv6AddressesAttributeResponse:
        """
        本接口（ModifyIpv6AddressesAttribute）用于修改弹性网卡IPv6地址属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpv6AddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpv6AddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyIpv6AddressesBandwidth(
            self,
            request: models.ModifyIpv6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ModifyIpv6AddressesBandwidthResponse:
        """
        该接口(ModifyIpv6AddressesBandwidth)用于修改IPV6地址访问internet的带宽
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyIpv6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyIpv6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyListener(
            self,
            request: models.ModifyListenerRequest,
            opts: Dict = None,
    ) -> models.ModifyListenerResponse:
        """
        修改负载均衡监听器属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyListener"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyListenerResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyLoadBalancerAttributes(
            self,
            request: models.ModifyLoadBalancerAttributesRequest,
            opts: Dict = None,
    ) -> models.ModifyLoadBalancerAttributesResponse:
        """
        修改负载均衡实例的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyLoadBalancerAttributes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyLoadBalancerAttributesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleConfig(
            self,
            request: models.ModifyModuleConfigRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleConfigResponse:
        """
        修改模块配置，已关联实例的模块不支持调整配置。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleConfig"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleConfigResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleDisableWanIp(
            self,
            request: models.ModifyModuleDisableWanIpRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleDisableWanIpResponse:
        """
        修改模块是否禁止分配外网ip的属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleDisableWanIp"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleDisableWanIpResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleImage(
            self,
            request: models.ModifyModuleImageRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleImageResponse:
        """
        修改模块的默认镜像
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleImage"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleImageResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleIpDirect(
            self,
            request: models.ModifyModuleIpDirectRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleIpDirectResponse:
        """
        修改模块IP直通。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleIpDirect"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleIpDirectResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleName(
            self,
            request: models.ModifyModuleNameRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleNameResponse:
        """
        修改模块名称
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleName"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleNameResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleNetwork(
            self,
            request: models.ModifyModuleNetworkRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleNetworkResponse:
        """
        修改模块默认带宽上限
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleNetwork"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleNetworkResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyModuleSecurityGroups(
            self,
            request: models.ModifyModuleSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.ModifyModuleSecurityGroupsResponse:
        """
        修改模块默认安全组
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyModuleSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyModuleSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyPrivateIpAddressesAttribute(
            self,
            request: models.ModifyPrivateIpAddressesAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyPrivateIpAddressesAttributeResponse:
        """
        用于修改弹性网卡内网IP属性。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyPrivateIpAddressesAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyPrivateIpAddressesAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyRouteTableAttribute(
            self,
            request: models.ModifyRouteTableAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyRouteTableAttributeResponse:
        """
        修改路由表属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyRouteTableAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyRouteTableAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifySecurityGroupAttribute(
            self,
            request: models.ModifySecurityGroupAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifySecurityGroupAttributeResponse:
        """
        修改安全组属性
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
        修改安全组出站和入站规则
        """
        
        kwargs = {}
        kwargs["action"] = "ModifySecurityGroupPolicies"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifySecurityGroupPoliciesResponse
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
        
    async def ModifyTargetPort(
            self,
            request: models.ModifyTargetPortRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetPortResponse:
        """
        修改监听器绑定的后端机器的端口。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetPort"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetPortResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyTargetWeight(
            self,
            request: models.ModifyTargetWeightRequest,
            opts: Dict = None,
    ) -> models.ModifyTargetWeightResponse:
        """
        修改监听器绑定的后端机器的转发权重。
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyTargetWeight"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyTargetWeightResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ModifyVpcAttribute(
            self,
            request: models.ModifyVpcAttributeRequest,
            opts: Dict = None,
    ) -> models.ModifyVpcAttributeResponse:
        """
        修改私有网络（VPC）的相关属性
        """
        
        kwargs = {}
        kwargs["action"] = "ModifyVpcAttribute"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ModifyVpcAttributeResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def QueryVpcTaskResult(
            self,
            request: models.QueryVpcTaskResultRequest,
            opts: Dict = None,
    ) -> models.QueryVpcTaskResultResponse:
        """
        查询私有网络下Vpc、子网、havip等异步任务请求结果
        """
        
        kwargs = {}
        kwargs["action"] = "QueryVpcTaskResult"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.QueryVpcTaskResultResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RebootInstances(
            self,
            request: models.RebootInstancesRequest,
            opts: Dict = None,
    ) -> models.RebootInstancesResponse:
        """
        只有状态为RUNNING的实例才可以进行此操作；接口调用成功时，实例会进入REBOOTING状态；重启实例成功时，实例会进入RUNNING状态；支持强制重启，强制重启的效果等同于关闭物理计算机的电源开关再重新启动。强制重启可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常重启时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "RebootInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RebootInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseAddresses(
            self,
            request: models.ReleaseAddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseAddressesResponse:
        """
        释放一个或多个弹性公网IP（简称 EIP）。
        该操作不可逆，释放后 EIP 关联的 IP 地址将不再属于您的名下。
        只有状态为 UNBIND 的 EIP 才能进行释放操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIpv6Addresses(
            self,
            request: models.ReleaseIpv6AddressesRequest,
            opts: Dict = None,
    ) -> models.ReleaseIpv6AddressesResponse:
        """
        本接口（UnassignIpv6Addresses）用于释放弹性网卡IPv6地址。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIpv6Addresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIpv6AddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReleaseIpv6AddressesBandwidth(
            self,
            request: models.ReleaseIpv6AddressesBandwidthRequest,
            opts: Dict = None,
    ) -> models.ReleaseIpv6AddressesBandwidthResponse:
        """
        该接口用于给弹性公网IPv6地址释放带宽。
        """
        
        kwargs = {}
        kwargs["action"] = "ReleaseIpv6AddressesBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReleaseIpv6AddressesBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RemovePrivateIpAddresses(
            self,
            request: models.RemovePrivateIpAddressesRequest,
            opts: Dict = None,
    ) -> models.RemovePrivateIpAddressesResponse:
        """
        弹性网卡退还内网 IP。
        退还弹性网卡上的辅助内网IP，接口自动解关联弹性公网 IP。不能退还弹性网卡的主内网IP。
        """
        
        kwargs = {}
        kwargs["action"] = "RemovePrivateIpAddresses"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RemovePrivateIpAddressesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceRouteTableAssociation(
            self,
            request: models.ReplaceRouteTableAssociationRequest,
            opts: Dict = None,
    ) -> models.ReplaceRouteTableAssociationResponse:
        """
        修改子网关联的路由表，一个子网只能关联一个路由表。
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
        替换路由策略
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ReplaceSecurityGroupPolicy(
            self,
            request: models.ReplaceSecurityGroupPolicyRequest,
            opts: Dict = None,
    ) -> models.ReplaceSecurityGroupPolicyResponse:
        """
        替换单条安全组路由规则, 单个请求中只能替换单个方向的一条规则, 必须要指定索引（PolicyIndex）。
        """
        
        kwargs = {}
        kwargs["action"] = "ReplaceSecurityGroupPolicy"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ReplaceSecurityGroupPolicyResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstances(
            self,
            request: models.ResetInstancesRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesResponse:
        """
        重装实例，若指定了ImageId参数，则使用指定的镜像重装；否则按照当前实例使用的镜像进行重装；若未指定密码，则密码通过站内信形式随后发送。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesMaxBandwidth(
            self,
            request: models.ResetInstancesMaxBandwidthRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesMaxBandwidthResponse:
        """
        重置实例的最大带宽上限。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesMaxBandwidth"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesMaxBandwidthResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetInstancesPassword(
            self,
            request: models.ResetInstancesPasswordRequest,
            opts: Dict = None,
    ) -> models.ResetInstancesPasswordResponse:
        """
        重置处于运行中状态的实例的密码，需要显式指定强制关机参数ForceStop。如果没有显式指定强制关机参数，则只有处于关机状态的实例才允许执行重置密码操作。
        """
        
        kwargs = {}
        kwargs["action"] = "ResetInstancesPassword"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetInstancesPasswordResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def ResetRoutes(
            self,
            request: models.ResetRoutesRequest,
            opts: Dict = None,
    ) -> models.ResetRoutesResponse:
        """
        对某个路由表名称和所有路由策略（Route）进行重新设置
        """
        
        kwargs = {}
        kwargs["action"] = "ResetRoutes"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.ResetRoutesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def RunInstances(
            self,
            request: models.RunInstancesRequest,
            opts: Dict = None,
    ) -> models.RunInstancesResponse:
        """
        创建ECM实例。
        """
        
        kwargs = {}
        kwargs["action"] = "RunInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.RunInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetLoadBalancerSecurityGroups(
            self,
            request: models.SetLoadBalancerSecurityGroupsRequest,
            opts: Dict = None,
    ) -> models.SetLoadBalancerSecurityGroupsResponse:
        """
        设置负载均衡实例的安全组。
        """
        
        kwargs = {}
        kwargs["action"] = "SetLoadBalancerSecurityGroups"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetLoadBalancerSecurityGroupsResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def SetSecurityGroupForLoadbalancers(
            self,
            request: models.SetSecurityGroupForLoadbalancersRequest,
            opts: Dict = None,
    ) -> models.SetSecurityGroupForLoadbalancersResponse:
        """
        绑定或解绑一个安全组到多个负载均衡实例。
        """
        
        kwargs = {}
        kwargs["action"] = "SetSecurityGroupForLoadbalancers"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.SetSecurityGroupForLoadbalancersResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StartInstances(
            self,
            request: models.StartInstancesRequest,
            opts: Dict = None,
    ) -> models.StartInstancesResponse:
        """
        只有状态为STOPPED的实例才可以进行此操作；接口调用成功时，实例会进入STARTING状态；启动实例成功时，实例会进入RUNNING状态。
        """
        
        kwargs = {}
        kwargs["action"] = "StartInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StartInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def StopInstances(
            self,
            request: models.StopInstancesRequest,
            opts: Dict = None,
    ) -> models.StopInstancesResponse:
        """
        只有处于"RUNNING"状态的实例才能够进行关机操作；
        调用成功时，实例会进入STOPPING状态；关闭实例成功时，实例会进入STOPPED状态；
        支持强制关闭，强制关机的效果等同于关闭物理计算机的电源开关，强制关机可能会导致数据丢失或文件系统损坏，请仅在服务器不能正常关机时使用。
        """
        
        kwargs = {}
        kwargs["action"] = "StopInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.StopInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateDisks(
            self,
            request: models.TerminateDisksRequest,
            opts: Dict = None,
    ) -> models.TerminateDisksResponse:
        """
        CBS在ECM早已下线

        本接口（TerminateDisks）用于退还云硬盘。

        * 不再使用的云盘，可通过本接口主动退还。
        * 本接口支持退还预付费云盘和按小时后付费云盘。按小时后付费云盘可直接退还，预付费云盘需符合退还规则。
        * 支持批量操作，每次请求批量云硬盘的上限为50。如果批量云盘存在不允许操作的，请求会以特定错误码返回。
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateDisks"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateDisksResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def TerminateInstances(
            self,
            request: models.TerminateInstancesRequest,
            opts: Dict = None,
    ) -> models.TerminateInstancesResponse:
        """
        销毁实例
        """
        
        kwargs = {}
        kwargs["action"] = "TerminateInstances"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.TerminateInstancesResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)
        
    async def UnassignIpv6SubnetCidrBlock(
            self,
            request: models.UnassignIpv6SubnetCidrBlockRequest,
            opts: Dict = None,
    ) -> models.UnassignIpv6SubnetCidrBlockResponse:
        """
        本接口（UnassignIpv6SubnetCidrBlock）用于释放IPv6子网段。
        子网段如果还有IP占用且未回收，则子网段无法释放。
        """
        
        kwargs = {}
        kwargs["action"] = "UnassignIpv6SubnetCidrBlock"
        kwargs["params"] = request._serialize()
        kwargs["resp_cls"] = models.UnassignIpv6SubnetCidrBlockResponse
        kwargs["headers"] = request.headers
        kwargs["opts"] = opts or {}
        
        return await self.call_and_deserialize(**kwargs)