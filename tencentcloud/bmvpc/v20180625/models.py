# -*- coding: utf8 -*-
# Copyright (c) 2017-2018 THL A29 Limited, a Tencent company. All Rights Reserved.
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

from tencentcloud.common.abstract_model import AbstractModel


class AcceptVpcPeerConnectionRequest(AbstractModel):
    """AcceptVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石对等连接实例ID
        :type VpcPeerConnectionId: str
        """
        self.VpcPeerConnectionId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")


class AcceptVpcPeerConnectionResponse(AbstractModel):
    """AcceptVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AsyncRegisterIpsRequest(AbstractModel):
    """AsyncRegisterIps请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络的唯一ID。
        :type VpcId: str
        :param SubnetId: 子网唯一ID。
        :type SubnetId: str
        :param Ips: 需要注册的IP列表。
        :type Ips: list of str
        """
        self.VpcId = None
        self.SubnetId = None
        self.Ips = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Ips = params.get("Ips")


class AsyncRegisterIpsResponse(AbstractModel):
    """AsyncRegisterIps返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindEipsToNatGatewayRequest(AbstractModel):
    """BindEipsToNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param AssignedEips: 已分配的EIP列表；AssignedEips和AutoAllocEipNum至少输入一个
        :type AssignedEips: list of str
        :param AutoAllocEipNum: 新建EIP数目，系统将会按您的要求生产该数目个数EIP；AssignedEips和AutoAllocEipNum至少输入一个
        :type AutoAllocEipNum: int
        """
        self.NatId = None
        self.VpcId = None
        self.AssignedEips = None
        self.AutoAllocEipNum = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.AssignedEips = params.get("AssignedEips")
        self.AutoAllocEipNum = params.get("AutoAllocEipNum")


class BindEipsToNatGatewayResponse(AbstractModel):
    """BindEipsToNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindIpsToNatGatewayRequest(AbstractModel):
    """BindIpsToNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param IpInfoSet: 部分IP信息，子网下只有该部分IP将加入NAT，仅当网关转发模式为IP方式有效
        :type IpInfoSet: list of IpInfo
        """
        self.NatId = None
        self.VpcId = None
        self.IpInfoSet = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        if params.get("IpInfoSet") is not None:
            self.IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self.IpInfoSet.append(obj)


class BindIpsToNatGatewayResponse(AbstractModel):
    """BindIpsToNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class BindSubnetsToNatGatewayRequest(AbstractModel):
    """BindSubnetsToNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetIds: 子网ID列表，子网下全部IP将加入NAT，不区分网关转发方式
        :type SubnetIds: list of str
        """
        self.NatId = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")


class BindSubnetsToNatGatewayResponse(AbstractModel):
    """BindSubnetsToNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateDockerSubnetWithVlanRequest(AbstractModel):
    """CreateDockerSubnetWithVlan请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 系统分配的私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetSet: 子网信息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self.VpcId = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class CreateDockerSubnetWithVlanResponse(AbstractModel):
    """CreateDockerSubnetWithVlan返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateHostedInterfaceRequest(AbstractModel):
    """CreateHostedInterface请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 托管机器唯一ID 数组
        :type InstanceIds: list of str
        :param VpcId: 私有网络ID或者私有网络统一ID，建议使用统一ID
        :type VpcId: str
        :param SubnetId: 子网ID或者子网统一ID，建议使用统一ID
        :type SubnetId: str
        """
        self.InstanceIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class CreateHostedInterfaceResponse(AbstractModel):
    """CreateHostedInterface返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param ResourceIds: 黑石托管机器ID
        :type ResourceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class CreateInterfacesRequest(AbstractModel):
    """CreateInterfaces请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 物理机实例ID列表
        :type InstanceIds: list of str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        """
        self.InstanceIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class CreateInterfacesResponse(AbstractModel):
    """CreateInterfaces返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param ForwardMode: 转发模式，其中0表示IP方式，1表示网段方式；通过cidr方式可支持更多的IP接入到NAT网关
        :type ForwardMode: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param NatName: NAT名称
        :type NatName: str
        :param MaxConcurrent: 并发连接数规格；取值为1000000、3000000、10000000，分别对应小型、中型、大型NAT网关
        :type MaxConcurrent: int
        :param SubnetIds: 子网ID列表，子网下全部IP将加入NAT，不区分网关转发方式
        :type SubnetIds: list of str
        :param IpInfoSet: 部分IP信息，子网下只有该部分IP将加入NAT，仅当网关转发模式为IP方式有效；IpInfoSet和SubnetIds中的子网ID不能同时存在
        :type IpInfoSet: list of IpInfo
        :param AssignedEips: 已分配的EIP列表, AssignedEips和AutoAllocEipNum至少输入一个
        :type AssignedEips: list of str
        :param AutoAllocEipNum: 新建EIP数目，系统将会按您的要求生产该数目个数EIP, AssignedEips和AutoAllocEipNum至少输入一个
        :type AutoAllocEipNum: int
        :param Exclusive: 独占标识，取值为0和1，默认值为0；0和1分别表示创建共享型NAT网关和独占NAT型网关；由于同一个VPC网络内，指向NAT集群的默认路由只有一条，因此VPC内只能创建一种类型NAT网关；创建独占型NAT网关时，需联系对应架构师进行独占NAT集群搭建，否则无法创建独占型NAT网关。
        :type Exclusive: int
        """
        self.ForwardMode = None
        self.VpcId = None
        self.NatName = None
        self.MaxConcurrent = None
        self.SubnetIds = None
        self.IpInfoSet = None
        self.AssignedEips = None
        self.AutoAllocEipNum = None
        self.Exclusive = None


    def _deserialize(self, params):
        self.ForwardMode = params.get("ForwardMode")
        self.VpcId = params.get("VpcId")
        self.NatName = params.get("NatName")
        self.MaxConcurrent = params.get("MaxConcurrent")
        self.SubnetIds = params.get("SubnetIds")
        if params.get("IpInfoSet") is not None:
            self.IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self.IpInfoSet.append(obj)
        self.AssignedEips = params.get("AssignedEips")
        self.AutoAllocEipNum = params.get("AutoAllocEipNum")
        self.Exclusive = params.get("Exclusive")


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateRoutePoliciesRequest(AbstractModel):
    """CreateRoutePolicies请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RoutePolicySet: 新增的路由
        :type RoutePolicySet: list of RoutePolicy
        """
        self.RouteTableId = None
        self.RoutePolicySet = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("RoutePolicySet") is not None:
            self.RoutePolicySet = []
            for item in params.get("RoutePolicySet"):
                obj = RoutePolicy()
                obj._deserialize(item)
                self.RoutePolicySet.append(obj)


class CreateRoutePoliciesResponse(AbstractModel):
    """CreateRoutePolicies返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 系统分配的私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetSet: 子网信息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self.VpcId = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVirtualSubnetWithVlanRequest(AbstractModel):
    """CreateVirtualSubnetWithVlan请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 系统分配的私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetSet: 子网信息
        :type SubnetSet: list of SubnetCreateInputInfo
        """
        self.VpcId = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetCreateInputInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)


class CreateVirtualSubnetWithVlanResponse(AbstractModel):
    """CreateVirtualSubnetWithVlan返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVpcPeerConnectionRequest(AbstractModel):
    """CreateVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 本端VPC唯一ID
        :type VpcId: str
        :param PeerVpcId: 对端VPC唯一ID
        :type PeerVpcId: str
        :param PeerRegion: 对端地域，取值范围为gz,sh,bj,hk,cd,de,sh_bm,gz_bm,bj_bm,cq_bm等
        :type PeerRegion: str
        :param VpcPeerConnectionName: 对等连接名称
        :type VpcPeerConnectionName: str
        :param PeerUin: 对端账户OwnerUin（默认值为本端账户）
        :type PeerUin: str
        :param Bandwidth: 跨地域必传，带宽上限值
        :type Bandwidth: int
        """
        self.VpcId = None
        self.PeerVpcId = None
        self.PeerRegion = None
        self.VpcPeerConnectionName = None
        self.PeerUin = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PeerVpcId = params.get("PeerVpcId")
        self.PeerRegion = params.get("PeerRegion")
        self.VpcPeerConnectionName = params.get("VpcPeerConnectionName")
        self.PeerUin = params.get("PeerUin")
        self.Bandwidth = params.get("Bandwidth")


class CreateVpcPeerConnectionResponse(AbstractModel):
    """CreateVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcName: 私有网络的名称
        :type VpcName: str
        :param CidrBlock: 私有网络的CIDR
        :type CidrBlock: str
        :param Zone: 私有网络的可用区
        :type Zone: str
        :param SubnetSet: 子网信息
        :type SubnetSet: list of VpcSubnetCreateInfo
        :param EnableMonitoring: 是否启用内网监控
        :type EnableMonitoring: bool
        """
        self.VpcName = None
        self.CidrBlock = None
        self.Zone = None
        self.SubnetSet = None
        self.EnableMonitoring = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = VpcSubnetCreateInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.EnableMonitoring = params.get("EnableMonitoring")


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CustomerGateway(AbstractModel):
    """对端网关

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 用户网关唯一ID
        :type CustomerGatewayId: str
        :param CustomerGatewayName: 网关名称
        :type CustomerGatewayName: str
        :param IpAddress: 公网地址
        :type IpAddress: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param VpnConnNum: VPN通道引用个数
注意：此字段可能返回 null，表示取不到有效值。
        :type VpnConnNum: int
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreateTime = None
        self.VpnConnNum = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreateTime = params.get("CreateTime")
        self.VpnConnNum = params.get("VpnConnNum")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 对端网关ID，例如：bmcgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
        :type CustomerGatewayId: str
        """
        self.CustomerGatewayId = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")


class DeleteCustomerGatewayResponse(AbstractModel):
    """DeleteCustomerGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteHostedInterfaceRequest(AbstractModel):
    """DeleteHostedInterface请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIds: 托管机器唯一ID 数组
        :type InstanceIds: list of str
        :param VpcId: 私有网络ID或者私有网络统一ID，建议使用统一ID
        :type VpcId: str
        :param SubnetId: 子网ID或者子网统一ID，建议使用统一ID
        :type SubnetId: str
        """
        self.InstanceIds = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteHostedInterfaceResponse(AbstractModel):
    """DeleteHostedInterface返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param ResourceIds: 黑石托管机器ID
        :type ResourceIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.ResourceIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.ResourceIds = params.get("ResourceIds")
        self.RequestId = params.get("RequestId")


class DeleteHostedInterfacesRequest(AbstractModel):
    """DeleteHostedInterfaces请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param SubnetIds: 物理机ID
        :type SubnetIds: list of str
        """
        self.InstanceId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SubnetIds = params.get("SubnetIds")


class DeleteHostedInterfacesResponse(AbstractModel):
    """DeleteHostedInterfaces返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteInterfacesRequest(AbstractModel):
    """DeleteInterfaces请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param SubnetIds: 子网的唯一ID列表
        :type SubnetIds: list of str
        """
        self.InstanceId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.SubnetIds = params.get("SubnetIds")


class DeleteInterfacesResponse(AbstractModel):
    """DeleteInterfaces返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        """
        self.NatId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteRoutePolicyRequest(AbstractModel):
    """DeleteRoutePolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RoutePolicyId: 路由表策略ID
        :type RoutePolicyId: str
        """
        self.RouteTableId = None
        self.RoutePolicyId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RoutePolicyId = params.get("RoutePolicyId")


class DeleteRoutePolicyResponse(AbstractModel):
    """DeleteRoutePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param SubnetId: 子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVirtualIpRequest(AbstractModel):
    """DeleteVirtualIp请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络唯一ID。
        :type VpcId: str
        :param Ips: 退还的IP列表。
        :type Ips: list of str
        """
        self.VpcId = None
        self.Ips = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ips = params.get("Ips")


class DeleteVirtualIpResponse(AbstractModel):
    """DeleteVirtualIp返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVpcPeerConnectionRequest(AbstractModel):
    """DeleteVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石对等连接实例ID
        :type VpcPeerConnectionId: str
        """
        self.VpcPeerConnectionId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")


class DeleteVpcPeerConnectionResponse(AbstractModel):
    """DeleteVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID。
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        """
        self.VpnGatewayId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")


class DeleteVpnGatewayResponse(AbstractModel):
    """DeleteVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DeregisterIpsRequest(AbstractModel):
    """DeregisterIps请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param IpSet: 注销指定IP的列表
        :type IpSet: list of str
        :param SubnetId: 私有网络子网ID
        :type SubnetId: str
        """
        self.VpcId = None
        self.IpSet = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.IpSet = params.get("IpSet")
        self.SubnetId = params.get("SubnetId")


class DeregisterIpsResponse(AbstractModel):
    """DeregisterIps返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayIds: 对端网关ID，例如：bmcgw-2wqq41m9。每次请求的实例的上限为100。参数不支持同时指定CustomerGatewayIds和Filters。
        :type CustomerGatewayIds: list of str
        :param Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定CustomerGatewayIds和Filters。
<li>customergateway-name - String - （过滤条件）对端网关名称。</li>
<li>ip-address - String - （过滤条件)对端网关地址。</li>
<li>customergateway-id - String - （过滤条件）对端网关唯一ID。</li>
<li>zone - String - （过滤条件）对端所在可用区，形如：ap-guangzhou-2。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self.CustomerGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CustomerGatewayIds = params.get("CustomerGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCustomerGatewaysResponse(AbstractModel):
    """DescribeCustomerGateways返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewaySet: 对端网关对象列表
        :type CustomerGatewaySet: list of CustomerGateway
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGatewaySet") is not None:
            self.CustomerGatewaySet = []
            for item in params.get("CustomerGatewaySet"):
                obj = CustomerGateway()
                obj._deserialize(item)
                self.CustomerGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param NatName: NAT名称
        :type NatName: str
        :param SearchKey: 搜索字段
        :type SearchKey: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param Offset: 起始值
        :type Offset: int
        :param Limit: 偏移值，默认值为 20
        :type Limit: int
        """
        self.NatId = None
        self.NatName = None
        self.SearchKey = None
        self.VpcId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.NatName = params.get("NatName")
        self.SearchKey = params.get("SearchKey")
        self.VpcId = params.get("VpcId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways返回参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayInfoSet: NAT网关信息列表
        :type NatGatewayInfoSet: list of NatGatewayInfo
        :param TotalCount: 总数目
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NatGatewayInfoSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewayInfoSet") is not None:
            self.NatGatewayInfoSet = []
            for item in params.get("NatGatewayInfoSet"):
                obj = NatGatewayInfo()
                obj._deserialize(item)
                self.NatGatewayInfoSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatSubnetsRequest(AbstractModel):
    """DescribeNatSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        """
        self.NatId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")


class DescribeNatSubnetsResponse(AbstractModel):
    """DescribeNatSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param NatSubnetInfoSet: NAT子网信息
        :type NatSubnetInfoSet: list of NatSubnetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NatSubnetInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatSubnetInfoSet") is not None:
            self.NatSubnetInfoSet = []
            for item in params.get("NatSubnetInfoSet"):
                obj = NatSubnetInfo()
                obj._deserialize(item)
                self.NatSubnetInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRoutePoliciesRequest(AbstractModel):
    """DescribeRoutePolicies请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-afg8md3c。
        :type RouteTableId: str
        :param RoutePolicyIds: 路由策略实例ID，例如：rti-azd4dt1c。
        :type RoutePolicyIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定RoutePolicyIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
route-policy-id - String - （过滤条件）路由策略ID。
route-policy-description-like - String -（过滤条件）路由项备注。
route-policy-type - String - （过滤条件）路由项策略类型。
destination-cidr-like - String - （过滤条件）路由项目的地址。
gateway-id-like - String - （过滤条件）路由项下一跳网关。
gateway-type - String - （过滤条件）路由项下一条网关类型。
enable - Bool - （过滤条件）路由策略是否启用。
        :type Filters: list of Filter
        :param Offset: 初始行的偏移量，默认为0。
        :type Offset: int
        :param Limit: 每页行数，默认为20。
        :type Limit: int
        """
        self.RouteTableId = None
        self.RoutePolicyIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RoutePolicyIds = params.get("RoutePolicyIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeRoutePoliciesResponse(AbstractModel):
    """DescribeRoutePolicies返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 路由策略数
        :type TotalCount: int
        :param RoutePolicySet: 路由策略列表
        :type RoutePolicySet: list of RoutePolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RoutePolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RoutePolicySet") is not None:
            self.RoutePolicySet = []
            for item in params.get("RoutePolicySet"):
                obj = RoutePolicy()
                obj._deserialize(item)
                self.RoutePolicySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableIds: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
route-table-name - String - （过滤条件）路由表名称。
route-table-id-like - String - （模糊过滤条件）路由表实例ID。
route-table-name-like - String - （模糊过滤条件）路由表名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
zone - String - （过滤条件）可用区。
        :type Filters: list of Filter
        :param Offset: 初始行的偏移量，默认为0。
        :type Offset: int
        :param Limit: 每页行数，默认为20。
        :type Limit: int
        :param OrderField: 排序字段, 支持按“RouteTableId”，“VpcId”, "RouteTableName", "CreateTime"
        :type OrderField: str
        :param OrderDirection: 排序方向, “asc”、“desc”
        :type OrderDirection: str
        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.RouteTableIds = params.get("RouteTableIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 路由表个数
        :type TotalCount: int
        :param RouteTableSet: 路由表列表
        :type RouteTableSet: list of RouteTable
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteTableSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteTableSet") is not None:
            self.RouteTableSet = []
            for item in params.get("RouteTableSet"):
                obj = RouteTable()
                obj._deserialize(item)
                self.RouteTableSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetAvailableIpsRequest(AbstractModel):
    """DescribeSubnetAvailableIps请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: 私有网络子网ID
        :type SubnetId: str
        :param Cidr: CIDR前缀，例如10.0.1
        :type Cidr: str
        """
        self.SubnetId = None
        self.Cidr = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Cidr = params.get("Cidr")


class DescribeSubnetAvailableIpsResponse(AbstractModel):
    """DescribeSubnetAvailableIps返回参数结构体

    """

    def __init__(self):
        """
        :param IpSet: 可用IP的范围列表
        :type IpSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IpSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IpSet = params.get("IpSet")
        self.RequestId = params.get("RequestId")


class DescribeSubnetByDeviceRequest(AbstractModel):
    """DescribeSubnetByDevice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 物理机ID
        :type InstanceId: str
        :param Types: 子网类型。0: 物理机子网; 7: DOCKER子网 8: 虚拟子网
        :type Types: list of int non-negative
        :param Offset: 查询的起始位置。
        :type Offset: int
        :param Limit: 查询的个数。
        :type Limit: int
        """
        self.InstanceId = None
        self.Types = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Types = params.get("Types")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetByDeviceResponse(AbstractModel):
    """DescribeSubnetByDevice返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 子网个数
        :type TotalCount: int
        :param Data: 子网列表
        :type Data: list of SubnetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetByHostedDeviceRequest(AbstractModel):
    """DescribeSubnetByHostedDevice请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 托管机器ID, 如chm-xasdfx2j
        :type InstanceId: str
        :param Types: 子网类型。0: 物理机子网; 7: DOCKER子网 8: 虚拟子网
        :type Types: list of int non-negative
        :param Offset: 查询的起始位置。
        :type Offset: int
        :param Limit: 查询的个数。
        :type Limit: int
        """
        self.InstanceId = None
        self.Types = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Types = params.get("Types")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetByHostedDeviceResponse(AbstractModel):
    """DescribeSubnetByHostedDevice返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 子网个数
        :type TotalCount: int
        :param Data: 子网列表
        :type Data: list of SubnetInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetIds: 子网实例ID查询。形如：subnet-pxir56ns。参数不支持同时指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
subnet-id - String - （过滤条件）Subnet实例名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
cidr-block - String - （过滤条件）vpc的cidr。
subnet-name - String - （过滤条件）子网名称。
zone - String - （过滤条件）可用区。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SubnetIds = params.get("SubnetIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param SubnetSet: 子网列表信息
        :type SubnetSet: list of SubnetInfo
        :param TotalCount: 返回的子网总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubnetSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = SubnetInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务状态，其中0表示任务执行成功，1表示任务执行失败，2表示任务正在执行中
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeVpcQuotaRequest(AbstractModel):
    """DescribeVpcQuota请求参数结构体

    """

    def __init__(self):
        """
        :param TypeIds: 类型
        :type TypeIds: list of int non-negative
        """
        self.TypeIds = None


    def _deserialize(self, params):
        self.TypeIds = params.get("TypeIds")


class DescribeVpcQuotaResponse(AbstractModel):
    """DescribeVpcQuota返回参数结构体

    """

    def __init__(self):
        """
        :param VpcQuotaSet: 配额信息
        :type VpcQuotaSet: list of VpcQuota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcQuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcQuotaSet") is not None:
            self.VpcQuotaSet = []
            for item in params.get("VpcQuotaSet"):
                obj = VpcQuota()
                obj._deserialize(item)
                self.VpcQuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcResourceRequest(AbstractModel):
    """DescribeVpcResource请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: 私有网络实例ID
        :type VpcIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
vpc-id - String - （过滤条件）私有网络实例ID，形如：vpc-f49l6u0z。
vpc-name - String - （过滤条件）私有网络名称。
zone - String - （过滤条件）可用区。
state - String - （过滤条件）VPC状态。
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcResourceResponse(AbstractModel):
    """DescribeVpcResource返回参数结构体

    """

    def __init__(self):
        """
        :param VpcResourceSet: VPC数据
        :type VpcResourceSet: list of VpcResource
        :param TotalCount: VPC个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcResourceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcResourceSet") is not None:
            self.VpcResourceSet = []
            for item in params.get("VpcResourceSet"):
                obj = VpcResource()
                obj._deserialize(item)
                self.VpcResourceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcViewRequest(AbstractModel):
    """DescribeVpcView请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络唯一ID
        :type VpcId: str
        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")


class DescribeVpcViewResponse(AbstractModel):
    """DescribeVpcView返回参数结构体

    """

    def __init__(self):
        """
        :param VpcView: VPC视图信息
        :type VpcView: :class:`tencentcloud.bmvpc.v20180625.models.VpcViewInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcView = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcView") is not None:
            self.VpcView = VpcViewInfo()
            self.VpcView._deserialize(params.get("VpcView"))
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。
        :type VpcIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
vpc-name - String - （过滤条件）VPC实例名称。
vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。
cidr-block - String - （过滤条件）vpc的cidr。
state - String - （过滤条件）VPC状态。(pending | available).
zone -  String - （过滤条件）VPC的可用区。
        :type Filters: list of Filter
        :param Offset: 初始行的偏移量，默认为0。
        :type Offset: int
        :param Limit: 每页行数，默认为20。
        :type Limit: int
        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回参数结构体

    """

    def __init__(self):
        """
        :param VpcSet: VPC列表
        :type VpcSet: list of VpcInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param VendorName: 厂商,取值 h3c，cisco
        :type VendorName: str
        """
        self.VpnConnectionId = None
        self.VendorName = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VendorName = params.get("VendorName")


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: 配置信息。
        :type CustomerGatewayConfiguration: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewayConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomerGatewayConfiguration = params.get("CustomerGatewayConfiguration")
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
        :type Name: str
        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class IKEOptionsSpecification(AbstractModel):
    """IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议

    """

    def __init__(self):
        """
        :param PropoEncryAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBS-192', 'AES-CBC-256', 'DES-CBC'，默认为3DES-CBC
        :type PropoEncryAlgorithm: str
        :param PropoAuthenAlgorithm: 认证算法：可选值：'MD5', 'SHA1'，默认为MD5
        :type PropoAuthenAlgorithm: str
        :param ExchangeMode: 协商模式：可选值：'AGGRESSIVE', 'MAIN'，默认为MAIN
        :type ExchangeMode: str
        :param LocalIdentity: 本端标识类型：可选值：'ADDRESS', 'FQDN'，默认为ADDRESS
        :type LocalIdentity: str
        :param RemoteIdentity: 对端标识类型：可选值：'ADDRESS', 'FQDN'，默认为ADDRESS
        :type RemoteIdentity: str
        :param LocalAddress: 本端标识，当LocalIdentity选为ADDRESS时，LocalAddress必填。localAddress默认为vpn网关公网IP
        :type LocalAddress: str
        :param RemoteAddress: 对端标识，当RemoteIdentity选为ADDRESS时，RemoteAddress必填
        :type RemoteAddress: str
        :param LocalFqdnName: 本端标识，当LocalIdentity选为FQDN时，LocalFqdnName必填
        :type LocalFqdnName: str
        :param RemoteFqdnName: 对端标识，当remoteIdentity选为FQDN时，RemoteFqdnName必填
        :type RemoteFqdnName: str
        :param DhGroupName: DH group，指定IKE交换密钥时使用的DH组，可选值：'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', 'GROUP24'，
        :type DhGroupName: str
        :param IKESaLifetimeSeconds: IKE SA Lifetime，单位：秒，设置IKE SA的生存周期，取值范围：60-604800
        :type IKESaLifetimeSeconds: int
        :param IKEVersion: IKE版本
        :type IKEVersion: str
        """
        self.PropoEncryAlgorithm = None
        self.PropoAuthenAlgorithm = None
        self.ExchangeMode = None
        self.LocalIdentity = None
        self.RemoteIdentity = None
        self.LocalAddress = None
        self.RemoteAddress = None
        self.LocalFqdnName = None
        self.RemoteFqdnName = None
        self.DhGroupName = None
        self.IKESaLifetimeSeconds = None
        self.IKEVersion = None


    def _deserialize(self, params):
        self.PropoEncryAlgorithm = params.get("PropoEncryAlgorithm")
        self.PropoAuthenAlgorithm = params.get("PropoAuthenAlgorithm")
        self.ExchangeMode = params.get("ExchangeMode")
        self.LocalIdentity = params.get("LocalIdentity")
        self.RemoteIdentity = params.get("RemoteIdentity")
        self.LocalAddress = params.get("LocalAddress")
        self.RemoteAddress = params.get("RemoteAddress")
        self.LocalFqdnName = params.get("LocalFqdnName")
        self.RemoteFqdnName = params.get("RemoteFqdnName")
        self.DhGroupName = params.get("DhGroupName")
        self.IKESaLifetimeSeconds = params.get("IKESaLifetimeSeconds")
        self.IKEVersion = params.get("IKEVersion")


class IPSECOptionsSpecification(AbstractModel):
    """IPSec配置，腾讯云提供IPSec安全会话设置

    """

    def __init__(self):
        """
        :param PfsDhGroup: PFS：可选值：'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', 'DH-GROUP24'，默认为NULL
        :type PfsDhGroup: str
        :param IPSECSaLifetimeTraffic: IPsec SA lifetime(KB)：单位KB，取值范围：2560-604800
        :type IPSECSaLifetimeTraffic: int
        :param EncryptAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', 'NULL'， 默认为AES-CBC-128
        :type EncryptAlgorithm: str
        :param IntegrityAlgorith: 认证算法：可选值：'MD5', 'SHA1'，默认为
        :type IntegrityAlgorith: str
        :param IPSECSaLifetimeSeconds: IPsec SA lifetime(s)：单位秒，取值范围：180-604800
        :type IPSECSaLifetimeSeconds: int
        :param SecurityProto: 安全协议，默认为ESP
        :type SecurityProto: str
        """
        self.PfsDhGroup = None
        self.IPSECSaLifetimeTraffic = None
        self.EncryptAlgorithm = None
        self.IntegrityAlgorith = None
        self.IPSECSaLifetimeSeconds = None
        self.SecurityProto = None


    def _deserialize(self, params):
        self.PfsDhGroup = params.get("PfsDhGroup")
        self.IPSECSaLifetimeTraffic = params.get("IPSECSaLifetimeTraffic")
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.IntegrityAlgorith = params.get("IntegrityAlgorith")
        self.IPSECSaLifetimeSeconds = params.get("IPSECSaLifetimeSeconds")
        self.SecurityProto = params.get("SecurityProto")


class IpInfo(AbstractModel):
    """NAT IP信息

    """

    def __init__(self):
        """
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param Ips: IP列表
        :type Ips: list of str
        """
        self.SubnetId = None
        self.Ips = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ips = params.get("Ips")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 对端网关ID，例如：bmcgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
        :type CustomerGatewayId: str
        :param CustomerGatewayName: 对端网关名称，可任意命名，但不得超过60个字符。
        :type CustomerGatewayName: str
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")


class ModifyCustomerGatewayAttributeResponse(AbstractModel):
    """ModifyCustomerGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRoutePolicyRequest(AbstractModel):
    """ModifyRoutePolicy请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RoutePolicy: 修改的路由
        :type RoutePolicy: :class:`tencentcloud.bmvpc.v20180625.models.RoutePolicy`
        """
        self.RouteTableId = None
        self.RoutePolicy = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("RoutePolicy") is not None:
            self.RoutePolicy = RoutePolicy()
            self.RoutePolicy._deserialize(params.get("RoutePolicy"))


class ModifyRoutePolicyResponse(AbstractModel):
    """ModifyRoutePolicy返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyRouteTableRequest(AbstractModel):
    """ModifyRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表ID
        :type RouteTableId: str
        :param RouteTableName: 路由表名称
        :type RouteTableName: str
        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")


class ModifyRouteTableResponse(AbstractModel):
    """ModifyRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param SubnetName: 子网名称
        :type SubnetName: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubnetDHCPRelayRequest(AbstractModel):
    """ModifySubnetDHCPRelay请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param EnableDHCP: 是否开启DHCP Relay
        :type EnableDHCP: bool
        :param ServerIps: DHCP服务器IP
        :type ServerIps: list of str
        :param ReservedIpCount: 预留IP个数
        :type ReservedIpCount: int
        """
        self.VpcId = None
        self.SubnetId = None
        self.EnableDHCP = None
        self.ServerIps = None
        self.ReservedIpCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EnableDHCP = params.get("EnableDHCP")
        self.ServerIps = params.get("ServerIps")
        self.ReservedIpCount = params.get("ReservedIpCount")


class ModifySubnetDHCPRelayResponse(AbstractModel):
    """ModifySubnetDHCPRelay返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param VpcName: 私有网络名称
        :type VpcName: str
        :param EnableMonitor: 是否开启内网监控，0为关闭，1为开启
        :type EnableMonitor: bool
        """
        self.VpcId = None
        self.VpcName = None
        self.EnableMonitor = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.EnableMonitor = params.get("EnableMonitor")


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcPeerConnectionRequest(AbstractModel):
    """ModifyVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石对等连接唯一ID
        :type VpcPeerConnectionId: str
        :param Bandwidth: 对等连接带宽
        :type Bandwidth: int
        :param VpcPeerConnectionName: 对等连接名称
        :type VpcPeerConnectionName: str
        """
        self.VpcPeerConnectionId = None
        self.Bandwidth = None
        self.VpcPeerConnectionName = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")
        self.Bandwidth = params.get("Bandwidth")
        self.VpcPeerConnectionName = params.get("VpcPeerConnectionName")


class ModifyVpcPeerConnectionResponse(AbstractModel):
    """ModifyVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param VpcId: VPC实例ID
        :type VpcId: str
        :param VpnConnectionName: VPN通道名称，可任意命名，但不得超过60个字符。
        :type VpnConnectionName: str
        :param PreShareKey: 预共享密钥。
        :type PreShareKey: str
        :param SecurityPolicyDatabases: SPD策略组，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议。
        :type IKEOptionsSpecification: :class:`tencentcloud.bmvpc.v20180625.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec配置，腾讯云提供IPSec安全会话设置。
        :type IPSECOptionsSpecification: :class:`tencentcloud.bmvpc.v20180625.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpcId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpcId = params.get("VpcId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.PreShareKey = params.get("PreShareKey")
        if params.get("SecurityPolicyDatabases") is not None:
            self.SecurityPolicyDatabases = []
            for item in params.get("SecurityPolicyDatabases"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabases.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class ModifyVpnConnectionAttributeResponse(AbstractModel):
    """ModifyVpnConnectionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayAttributeRequest(AbstractModel):
    """ModifyVpnGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param VpnGatewayName: VPN网关名称，最大长度不能超过60个字节。
        :type VpnGatewayName: str
        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")


class ModifyVpnGatewayAttributeResponse(AbstractModel):
    """ModifyVpnGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NatGatewayInfo(AbstractModel):
    """NAT详情

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID
        :type NatId: str
        :param NatName: 网关名称
        :type NatName: str
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param VpcName: 私有网络名称
        :type VpcName: str
        :param ProductionStatus: 网关状态，其中0表示创建中，1表示运行中，2表示创建失败
        :type ProductionStatus: int
        :param Eips: EIP列表
        :type Eips: list of str
        :param MaxConcurrent: 并发连接数规格，取值为1000000, 3000000, 10000000
        :type MaxConcurrent: int
        :param Zone: 可用区
        :type Zone: str
        :param Exclusive: 独占标识，其中0表示共享，1表示独占，默认值为0
        :type Exclusive: int
        :param ForwardMode: 转发模式，其中0表示IP方式，1表示网段方式
        :type ForwardMode: int
        :param VpcCidrBlock: 私有网络网段
        :type VpcCidrBlock: str
        :param Type: 网关类型，取值为 small，middle，big，分别对应小型、中型、大型
        :type Type: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.NatId = None
        self.NatName = None
        self.VpcId = None
        self.VpcName = None
        self.ProductionStatus = None
        self.Eips = None
        self.MaxConcurrent = None
        self.Zone = None
        self.Exclusive = None
        self.ForwardMode = None
        self.VpcCidrBlock = None
        self.Type = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.NatName = params.get("NatName")
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.ProductionStatus = params.get("ProductionStatus")
        self.Eips = params.get("Eips")
        self.MaxConcurrent = params.get("MaxConcurrent")
        self.Zone = params.get("Zone")
        self.Exclusive = params.get("Exclusive")
        self.ForwardMode = params.get("ForwardMode")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")


class NatSubnetInfo(AbstractModel):
    """NAT子网信息

    """

    def __init__(self):
        """
        :param Name: 子网名称
        :type Name: str
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param SubnetNatType: NAT子网类型，其中0表示绑定部分IP的NAT子网，1表示绑定全部IP的NAT子网，2表示绑定网关方式的NAT子网
        :type SubnetNatType: int
        :param CidrBlock: 子网网段
        :type CidrBlock: str
        """
        self.Name = None
        self.SubnetId = None
        self.SubnetNatType = None
        self.CidrBlock = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.SubnetId = params.get("SubnetId")
        self.SubnetNatType = params.get("SubnetNatType")
        self.CidrBlock = params.get("CidrBlock")


class RejectVpcPeerConnectionRequest(AbstractModel):
    """RejectVpcPeerConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcPeerConnectionId: 黑石对等连接实例ID
        :type VpcPeerConnectionId: str
        """
        self.VpcPeerConnectionId = None


    def _deserialize(self, params):
        self.VpcPeerConnectionId = params.get("VpcPeerConnectionId")


class RejectVpcPeerConnectionResponse(AbstractModel):
    """RejectVpcPeerConnection返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC唯一ID
        :type VpcId: str
        :param VpnConnectionId: VPN通道实例ID。形如：bmvpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpcId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnConnectionId = params.get("VpnConnectionId")


class ResetVpnConnectionResponse(AbstractModel):
    """ResetVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RoutePolicy(AbstractModel):
    """路由条目

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的网段
        :type DestinationCidrBlock: str
        :param GatewayType: 下一跳类型，目前我们支持的类型有：
LOCAL：物理机默认路由；
VPN：VPN网关；
PEERCONNECTION：对等连接；
CPM：物理机自定义路由；
CCN：云联网；
TGW：公网默认路由；
SSLVPN : SSH SSL VPN网关。
        :type GatewayType: str
        :param GatewayId: 下一跳地址，这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址。
        :type GatewayId: str
        :param RouteDescription: 路由策略描述。
        :type RouteDescription: str
        :param RoutePolicyId: 路由策略ID
        :type RoutePolicyId: str
        :param RoutePolicyType: 路由类型，目前我们支持的类型有：
USER：用户自定义路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和编辑USER 类型的路由。
        :type RoutePolicyType: str
        :param Enabled: 是否启用
        :type Enabled: bool
        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteDescription = None
        self.RoutePolicyId = None
        self.RoutePolicyType = None
        self.Enabled = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteDescription = params.get("RouteDescription")
        self.RoutePolicyId = params.get("RoutePolicyId")
        self.RoutePolicyType = params.get("RoutePolicyType")
        self.Enabled = params.get("Enabled")


class RouteTable(AbstractModel):
    """路由表对象

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。
        :type VpcId: str
        :param VpcName: VPC的名称
        :type VpcName: str
        :param VpcCidrBlock: VPC的CIDR
        :type VpcCidrBlock: str
        :param Zone: 可用区
        :type Zone: str
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        """
        self.VpcId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.Zone = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        self.CreateTime = params.get("CreateTime")


class SecurityPolicyDatabase(AbstractModel):
    """SecurityPolicyDatabase策略

    """

    def __init__(self):
        """
        :param LocalCidrBlock: 本端网段
        :type LocalCidrBlock: str
        :param RemoteCidrBlock: 对端网段
        :type RemoteCidrBlock: list of str
        """
        self.LocalCidrBlock = None
        self.RemoteCidrBlock = None


    def _deserialize(self, params):
        self.LocalCidrBlock = params.get("LocalCidrBlock")
        self.RemoteCidrBlock = params.get("RemoteCidrBlock")


class SubnetCreateInputInfo(AbstractModel):
    """创建子网时的子网类型

    """

    def __init__(self):
        """
        :param SubnetName: 子网名称，可任意命名，但不得超过60个字符
        :type SubnetName: str
        :param CidrBlock: 子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠
        :type CidrBlock: str
        :param DistributedFlag: 是否开启子网分布式网关，默认传1，传0为关闭子网分布式网关。关闭分布式网关子网用于云服务器化子网，此子网中只能有一台物理机，同时此物理机及其上子机只能在此子网中
        :type DistributedFlag: int
        :param DhcpEnable: 是否开启dhcp relay ，关闭为0，开启为1。默认为0
        :type DhcpEnable: int
        :param DhcpServerIp: DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP
        :type DhcpServerIp: list of str
        :param IpReserve: 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段
        :type IpReserve: int
        :param VlanId: 子网绑定的vlanId。VlanId取值范围为2000-2999。创建物理机子网，VlanId默认为5; 创建docker子网或者虚拟子网，VlanId默认会分配2000--2999未使用的数值。
        :type VlanId: int
        :param Zone: 黑石子网的可用区
        :type Zone: str
        :param IsSmartNic: 是否25G子网，1为是，0为否。
        :type IsSmartNic: int
        """
        self.SubnetName = None
        self.CidrBlock = None
        self.DistributedFlag = None
        self.DhcpEnable = None
        self.DhcpServerIp = None
        self.IpReserve = None
        self.VlanId = None
        self.Zone = None
        self.IsSmartNic = None


    def _deserialize(self, params):
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.DistributedFlag = params.get("DistributedFlag")
        self.DhcpEnable = params.get("DhcpEnable")
        self.DhcpServerIp = params.get("DhcpServerIp")
        self.IpReserve = params.get("IpReserve")
        self.VlanId = params.get("VlanId")
        self.Zone = params.get("Zone")
        self.IsSmartNic = params.get("IsSmartNic")


class SubnetInfo(AbstractModel):
    """黑石子网的信息

    """

    def __init__(self):
        """
        :param VpcId: 私有网络的唯一ID。
        :type VpcId: str
        :param VpcName: VPC的名称。
        :type VpcName: str
        :param VpcCidrBlock: VPC的CIDR。
        :type VpcCidrBlock: str
        :param SubnetId: 私有网络的唯一ID
        :type SubnetId: str
        :param SubnetName: 子网名称。
        :type SubnetName: str
        :param CidrBlock: 子网CIDR。
        :type CidrBlock: str
        :param Type: 子网类型。0: 黑石物理机子网; 6: ccs子网; 7 Docker子网; 8: 虚拟机子网
        :type Type: int
        :param ZoneId: 可用区ID。
        :type ZoneId: int
        :param CpmNum: 子网物理机的个数
        :type CpmNum: int
        :param VlanId: 子网的VlanId。
        :type VlanId: int
        :param DistributedFlag: 是否开启分布式网关 ，关闭为0，开启为1。
        :type DistributedFlag: int
        :param DhcpEnable: 是否开启dhcp relay ，关闭为0，开启为1。默认为0。
        :type DhcpEnable: int
        :param DhcpServerIp: DHCP SERVER 的IP地址数组。IP地址为相同VPC的子网内分配的IP。
        :type DhcpServerIp: list of str
        :param IpReserve: 预留的IP个数。从该子网的最大可分配IP倒序分配N个IP 用于DHCP 动态分配使用的地址段。
        :type IpReserve: int
        :param AvailableIpNum: 子网中可用的IP个数
        :type AvailableIpNum: int
        :param TotalIpNum: 子网中总共的IP个数
        :type TotalIpNum: int
        :param SubnetCreateTime: 子网创建时间
        :type SubnetCreateTime: str
        :param IsSmartNic: 25G子网标识
        :type IsSmartNic: int
        """
        self.VpcId = None
        self.VpcName = None
        self.VpcCidrBlock = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Type = None
        self.ZoneId = None
        self.CpmNum = None
        self.VlanId = None
        self.DistributedFlag = None
        self.DhcpEnable = None
        self.DhcpServerIp = None
        self.IpReserve = None
        self.AvailableIpNum = None
        self.TotalIpNum = None
        self.SubnetCreateTime = None
        self.IsSmartNic = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Type = params.get("Type")
        self.ZoneId = params.get("ZoneId")
        self.CpmNum = params.get("CpmNum")
        self.VlanId = params.get("VlanId")
        self.DistributedFlag = params.get("DistributedFlag")
        self.DhcpEnable = params.get("DhcpEnable")
        self.DhcpServerIp = params.get("DhcpServerIp")
        self.IpReserve = params.get("IpReserve")
        self.AvailableIpNum = params.get("AvailableIpNum")
        self.TotalIpNum = params.get("TotalIpNum")
        self.SubnetCreateTime = params.get("SubnetCreateTime")
        self.IsSmartNic = params.get("IsSmartNic")


class UnbindEipsFromNatGatewayRequest(AbstractModel):
    """UnbindEipsFromNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param AssignedEips: 已分配的EIP列表
        :type AssignedEips: list of str
        """
        self.NatId = None
        self.VpcId = None
        self.AssignedEips = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.AssignedEips = params.get("AssignedEips")


class UnbindEipsFromNatGatewayResponse(AbstractModel):
    """UnbindEipsFromNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindIpsFromNatGatewayRequest(AbstractModel):
    """UnbindIpsFromNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param IpInfoSet: 部分IP信息；子网须以部分IP将加入NAT网关
        :type IpInfoSet: list of IpInfo
        """
        self.NatId = None
        self.VpcId = None
        self.IpInfoSet = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        if params.get("IpInfoSet") is not None:
            self.IpInfoSet = []
            for item in params.get("IpInfoSet"):
                obj = IpInfo()
                obj._deserialize(item)
                self.IpInfoSet.append(obj)


class UnbindIpsFromNatGatewayResponse(AbstractModel):
    """UnbindIpsFromNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UnbindSubnetsFromNatGatewayRequest(AbstractModel):
    """UnbindSubnetsFromNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param SubnetIds: 子网ID列表，子网不区分加入NAT网关的转发方式
        :type SubnetIds: list of str
        """
        self.NatId = None
        self.VpcId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.SubnetIds = params.get("SubnetIds")


class UnbindSubnetsFromNatGatewayResponse(AbstractModel):
    """UnbindSubnetsFromNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class UpgradeNatGatewayRequest(AbstractModel):
    """UpgradeNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatId: NAT网关ID，例如：nat-kdm476mp
        :type NatId: str
        :param VpcId: 私有网络ID，例如：vpc-kd7d06of
        :type VpcId: str
        :param MaxConcurrent: 并发连接数规格；取值为1000000、3000000、10000000，分别对应小型、中型、大型NAT网关
        :type MaxConcurrent: int
        """
        self.NatId = None
        self.VpcId = None
        self.MaxConcurrent = None


    def _deserialize(self, params):
        self.NatId = params.get("NatId")
        self.VpcId = params.get("VpcId")
        self.MaxConcurrent = params.get("MaxConcurrent")


class UpgradeNatGatewayResponse(AbstractModel):
    """UpgradeNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID
        :type TaskId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class VpcInfo(AbstractModel):
    """VPC信息

    """

    def __init__(self):
        """
        :param VpcId: 私有网络的唯一ID。
        :type VpcId: str
        :param VpcName: VPC的名称。
        :type VpcName: str
        :param CidrBlock: VPC的CIDR。
        :type CidrBlock: str
        :param Zone: 可用区
        :type Zone: str
        :param State: VPC状态
        :type State: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        """
        self.VpcId = None
        self.VpcName = None
        self.CidrBlock = None
        self.Zone = None
        self.State = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")


class VpcQuota(AbstractModel):
    """VPC限额信息

    """

    def __init__(self):
        """
        :param TypeId: 配额类型ID
        :type TypeId: int
        :param Quota: 配额
        :type Quota: int
        """
        self.TypeId = None
        self.Quota = None


    def _deserialize(self, params):
        self.TypeId = params.get("TypeId")
        self.Quota = params.get("Quota")


class VpcResource(AbstractModel):
    """VPC占用资源

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param VpcName: 私有网络名称
        :type VpcName: str
        :param CidrBlock: 私有网络的CIDR
        :type CidrBlock: str
        :param SubnetNum: 子网个数
        :type SubnetNum: int
        :param NatNum: NAT个数
        :type NatNum: int
        :param State: VPC状态
        :type State: str
        :param MonitorFlag: 是否开启监控
        :type MonitorFlag: bool
        :param CpmNum: 物理机个数
        :type CpmNum: int
        :param LeaveIpNum: 可用IP个数
        :type LeaveIpNum: int
        :param LbNum: 负载均衡个数
        :type LbNum: int
        :param TrafficMirrorNum: 流量镜像网关个数
        :type TrafficMirrorNum: int
        :param EipNum: 弹性IP个数
        :type EipNum: int
        :param PlgwNum: 专线网关个数
        :type PlgwNum: int
        :param PlvpNum: 专线通道个数
        :type PlvpNum: int
        :param SslVpnGwNum: ssl vpn网关个数
        :type SslVpnGwNum: int
        :param VpcPeerNum: 对等链接个数
        :type VpcPeerNum: int
        :param IpsecVpnGwNum: ipsec vpn网关个数
        :type IpsecVpnGwNum: int
        :param Zone: 可用区
        :type Zone: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param IsOld: 是否老专区VPC
        :type IsOld: bool
        """
        self.VpcId = None
        self.VpcName = None
        self.CidrBlock = None
        self.SubnetNum = None
        self.NatNum = None
        self.State = None
        self.MonitorFlag = None
        self.CpmNum = None
        self.LeaveIpNum = None
        self.LbNum = None
        self.TrafficMirrorNum = None
        self.EipNum = None
        self.PlgwNum = None
        self.PlvpNum = None
        self.SslVpnGwNum = None
        self.VpcPeerNum = None
        self.IpsecVpnGwNum = None
        self.Zone = None
        self.CreateTime = None
        self.IsOld = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetNum = params.get("SubnetNum")
        self.NatNum = params.get("NatNum")
        self.State = params.get("State")
        self.MonitorFlag = params.get("MonitorFlag")
        self.CpmNum = params.get("CpmNum")
        self.LeaveIpNum = params.get("LeaveIpNum")
        self.LbNum = params.get("LbNum")
        self.TrafficMirrorNum = params.get("TrafficMirrorNum")
        self.EipNum = params.get("EipNum")
        self.PlgwNum = params.get("PlgwNum")
        self.PlvpNum = params.get("PlvpNum")
        self.SslVpnGwNum = params.get("SslVpnGwNum")
        self.VpcPeerNum = params.get("VpcPeerNum")
        self.IpsecVpnGwNum = params.get("IpsecVpnGwNum")
        self.Zone = params.get("Zone")
        self.CreateTime = params.get("CreateTime")
        self.IsOld = params.get("IsOld")


class VpcSubnetCreateInfo(AbstractModel):
    """创建VPC下默认子网

    """

    def __init__(self):
        """
        :param SubnetName: 子网名称
        :type SubnetName: str
        :param CidrBlock: 子网的CIDR
        :type CidrBlock: str
        :param Zone: 子网的可用区
        :type Zone: str
        """
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None


    def _deserialize(self, params):
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")


class VpcSubnetViewInfo(AbstractModel):
    """VPC视图子网信息

    """

    def __init__(self):
        """
        :param SubnetId: 子网ID
        :type SubnetId: str
        :param SubnetName: 子网名称
        :type SubnetName: str
        :param CidrBlock: 子网CIDR
        :type CidrBlock: str
        :param CpmNum: 子网下设备个数
        :type CpmNum: int
        :param LbNum: 内网负载均衡个数
        :type LbNum: int
        :param Zone: 子网所在可用区
        :type Zone: str
        """
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.CpmNum = None
        self.LbNum = None
        self.Zone = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.CpmNum = params.get("CpmNum")
        self.LbNum = params.get("LbNum")
        self.Zone = params.get("Zone")


class VpcViewInfo(AbstractModel):
    """VPC视图信息

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID
        :type VpcId: str
        :param VpcName: 私有网络名称
        :type VpcName: str
        :param CidrBlock: 私有网络CIDR
        :type CidrBlock: str
        :param Zone: 私有网络所在可用区
        :type Zone: str
        :param LbNum: 外网负载均衡个数
        :type LbNum: int
        :param EipNum: 弹性公网IP个数
        :type EipNum: int
        :param NatNum: NAT网关个数
        :type NatNum: int
        :param SubnetSet: 子网列表
        :type SubnetSet: list of VpcSubnetViewInfo
        """
        self.VpcId = None
        self.VpcName = None
        self.CidrBlock = None
        self.Zone = None
        self.LbNum = None
        self.EipNum = None
        self.NatNum = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.LbNum = params.get("LbNum")
        self.EipNum = params.get("EipNum")
        self.NatNum = params.get("NatNum")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = VpcSubnetViewInfo()
                obj._deserialize(item)
                self.SubnetSet.append(obj)