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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Address(AbstractModel):
    """描述 EIP 信息

    """

    def __init__(self):
        """
        :param AddressId: EIP的ID，是EIP的唯一标识。\n        :type AddressId: str\n        :param AddressName: EIP名称。\n        :type AddressName: str\n        :param AddressStatus: EIP状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)\n        :type AddressStatus: str\n        :param AddressIp: 外网IP地址\n        :type AddressIp: str\n        :param InstanceId: 绑定的资源实例ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param CreatedTime: 创建时间。ISO 8601 格式：YYYY-MM-DDTHH:mm:ss.sssZ\n        :type CreatedTime: str\n        :param NetworkInterfaceId: 绑定的弹性网卡ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetworkInterfaceId: str\n        :param PrivateAddressIp: 绑定的资源内网ip
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateAddressIp: str\n        :param IsArrears: 资源隔离状态。true表示eip处于隔离状态，false表示资源处于未隔离状态\n        :type IsArrears: bool\n        :param IsBlocked: 资源封堵状态。true表示eip处于封堵状态，false表示eip处于未封堵状态\n        :type IsBlocked: bool\n        :param IsEipDirectConnection: eip是否支持直通模式。true表示eip支持直通模式，false表示资源不支持直通模式\n        :type IsEipDirectConnection: bool\n        :param AddressType: eip资源类型，包括"CalcIP","WanIP","EIP","AnycastEIP"。其中"CalcIP"表示设备ip，“WanIP”表示普通公网ip，“EIP”表示弹性公网ip，“AnycastEip”表示加速EIP\n        :type AddressType: str\n        :param CascadeRelease: eip是否在解绑后自动释放。true表示eip将会在解绑后自动释放，false表示eip在解绑后不会自动释放\n        :type CascadeRelease: bool\n        :param InternetServiceProvider: 运营商，CTCC电信，CUCC联通，CMCC移动
注意：此字段可能返回 null，表示取不到有效值。\n        :type InternetServiceProvider: str\n        :param Bandwidth: 带宽上限
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bandwidth: int\n        :param PayMode: 计费模式
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayMode: str\n        """
        self.AddressId = None
        self.AddressName = None
        self.AddressStatus = None
        self.AddressIp = None
        self.InstanceId = None
        self.CreatedTime = None
        self.NetworkInterfaceId = None
        self.PrivateAddressIp = None
        self.IsArrears = None
        self.IsBlocked = None
        self.IsEipDirectConnection = None
        self.AddressType = None
        self.CascadeRelease = None
        self.InternetServiceProvider = None
        self.Bandwidth = None
        self.PayMode = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.AddressStatus = params.get("AddressStatus")
        self.AddressIp = params.get("AddressIp")
        self.InstanceId = params.get("InstanceId")
        self.CreatedTime = params.get("CreatedTime")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateAddressIp = params.get("PrivateAddressIp")
        self.IsArrears = params.get("IsArrears")
        self.IsBlocked = params.get("IsBlocked")
        self.IsEipDirectConnection = params.get("IsEipDirectConnection")
        self.AddressType = params.get("AddressType")
        self.CascadeRelease = params.get("CascadeRelease")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.Bandwidth = params.get("Bandwidth")
        self.PayMode = params.get("PayMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressInfo(AbstractModel):
    """ip地址相关信息结构体。

    """

    def __init__(self):
        """
        :param PublicIPAddressInfo: 实例的外网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`\n        :param PrivateIPAddressInfo: 实例的内网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIPAddressInfo: :class:`tencentcloud.ecm.v20190719.models.PrivateIPAddressInfo`\n        :param PublicIPv6AddressInfo: 实例的外网ipv6相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicIPv6AddressInfo: :class:`tencentcloud.ecm.v20190719.models.PublicIPAddressInfo`\n        """
        self.PublicIPAddressInfo = None
        self.PrivateIPAddressInfo = None
        self.PublicIPv6AddressInfo = None


    def _deserialize(self, params):
        if params.get("PublicIPAddressInfo") is not None:
            self.PublicIPAddressInfo = PublicIPAddressInfo()
            self.PublicIPAddressInfo._deserialize(params.get("PublicIPAddressInfo"))
        if params.get("PrivateIPAddressInfo") is not None:
            self.PrivateIPAddressInfo = PrivateIPAddressInfo()
            self.PrivateIPAddressInfo._deserialize(params.get("PrivateIPAddressInfo"))
        if params.get("PublicIPv6AddressInfo") is not None:
            self.PublicIPv6AddressInfo = PublicIPAddressInfo()
            self.PublicIPv6AddressInfo._deserialize(params.get("PublicIPv6AddressInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateSpecification(AbstractModel):
    """IP地址模版

    """

    def __init__(self):
        """
        :param AddressId: IP地址ID，例如：eipm-2uw6ujo6。\n        :type AddressId: str\n        :param AddressGroupId: IP地址组ID，例如：eipmg-2uw6ujo6。\n        :type AddressGroupId: str\n        """
        self.AddressId = None
        self.AddressGroupId = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressGroupId = params.get("AddressGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressCount: EIP数量。默认值：1。\n        :type AddressCount: int\n        :param InternetServiceProvider: CMCC：中国移动
CTCC：中国电信
CUCC：中国联通\n        :type InternetServiceProvider: str\n        :param InternetMaxBandwidthOut: 1 Mbps 至 5000 Mbps，默认值：1 Mbps。\n        :type InternetMaxBandwidthOut: int\n        :param Tags: 需要关联的标签列表。\n        :type Tags: list of Tag\n        :param InstanceId: 要绑定的实例 ID。\n        :type InstanceId: str\n        :param NetworkInterfaceId: 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddress: 要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。\n        :type PrivateIpAddress: str\n        """
        self.EcmRegion = None
        self.AddressCount = None
        self.InternetServiceProvider = None
        self.InternetMaxBandwidthOut = None
        self.Tags = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressCount = params.get("AddressCount")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param AddressSet: 申请到的 EIP 的唯一 ID 列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddressSet: list of str\n        :param TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddressSet = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Area(AbstractModel):
    """区域信息

    """

    def __init__(self):
        """
        :param AreaId: 区域ID\n        :type AreaId: str\n        :param AreaName: 区域名称\n        :type AreaName: str\n        """
        self.AreaId = None
        self.AreaName = None


    def _deserialize(self, params):
        self.AreaId = params.get("AreaId")
        self.AreaName = params.get("AreaName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param NetworkInterfaceId: 弹性网卡实例ID，形如：eni-1snva0vd。目前只支持主网卡上分配。\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: 指定的IPv6地址列表，单次最多指定10个。与入参Ipv6AddressCount合并计算配额。与Ipv6AddressCount必填一个。\n        :type Ipv6Addresses: list of Ipv6Address\n        :param Ipv6AddressCount: 自动分配IPv6地址个数，内网IP地址个数总和不能超过配数。与入参Ipv6Addresses合并计算配额。与Ipv6Addresses必填一个。\n        :type Ipv6AddressCount: int\n        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6AddressesResponse(AbstractModel):
    """AssignIpv6Addresses返回参数结构体

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: 分配给弹性网卡的IPv6地址列表。\n        :type Ipv6AddressSet: list of Ipv6Address\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ipv6AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。与SecondaryPrivateIpAddressCount至少提供一个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，与PrivateIpAddresses至少提供一个。内网IP地址个数总和不能超过配额数\n        :type SecondaryPrivateIpAddressCount: int\n        """
        self.NetworkInterfaceId = None
        self.EcmRegion = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.EcmRegion = params.get("EcmRegion")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param PrivateIpAddressSet: 内网IP详细信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PrivateIpAddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PrivateIpAddressSet") is not None:
            self.PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssistantCidr(AbstractModel):
    """VPC辅助CIDR信息。

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。形如：vpc-6v2ht8q5\n        :type VpcId: str\n        :param CidrBlock: 辅助CIDR。形如：172.16.0.0/16\n        :type CidrBlock: str\n        :param AssistantType: 辅助CIDR类型（0：普通辅助CIDR，1：容器辅助CIDR），默认都是0。\n        :type AssistantType: int\n        :param SubnetSet: 辅助CIDR拆分的子网。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetSet: list of Subnet\n        """
        self.VpcId = None
        self.CidrBlock = None
        self.AssistantType = None
        self.SubnetSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlock = params.get("CidrBlock")
        self.AssistantType = params.get("AssistantType")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。\n        :type AddressId: str\n        :param InstanceId: 要绑定的实例 ID。\n        :type InstanceId: str\n        :param NetworkInterfaceId: 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：eni-11112222。NetworkInterfaceId 与 InstanceId 不可同时指定。弹性网卡 ID 可通过DescribeNetworkInterfaces接口返回值中的networkInterfaceId获取。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddress: 要绑定的内网 IP。如果指定了 NetworkInterfaceId 则也必须指定 PrivateIpAddress ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 PrivateIpAddress 是指定的 NetworkInterfaceId 上的一个内网 IP。指定弹性网卡的内网 IP 可通过DescribeNetworkInterfaces接口返回值中的privateIpAddress获取。\n        :type PrivateIpAddress: str\n        """
        self.EcmRegion = None
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssociateSecurityGroupsRequest(AbstractModel):
    """AssociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 要绑定的安全组ID，类似esg-efil73jd，只支持绑定单个安全组。\n        :type SecurityGroupIds: list of str\n        :param InstanceIds: 被绑定的实例ID，类似ein-lesecurk，支持指定多个实例，每次请求批量实例的上限为100。\n        :type InstanceIds: list of str\n        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateSecurityGroupsResponse(AbstractModel):
    """AssociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param InstanceId: 实例ID。形如：ein-r8hr2upy。\n        :type InstanceId: str\n        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Backend(AbstractModel):
    """负责均衡后端信息

    """

    def __init__(self):
        """
        :param InstanceId: 后端服务的唯一 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param Port: 后端服务的监听端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param PrivateIpAddresses: 后端服务的内网 IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIpAddresses: list of str\n        :param RegisteredTime: 后端服务被绑定的时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegisteredTime: str\n        :param EniId: 弹性网卡唯一ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type EniId: str\n        :param PublicIpAddresses: 后端服务的外网 IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicIpAddresses: list of str\n        :param InstanceName: 后端服务的实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        """
        self.InstanceId = None
        self.Port = None
        self.Weight = None
        self.PrivateIpAddresses = None
        self.RegisteredTime = None
        self.EniId = None
        self.PublicIpAddresses = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Port = params.get("Port")
        self.Weight = params.get("Weight")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.RegisteredTime = params.get("RegisteredTime")
        self.EniId = params.get("EniId")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsRequest(AbstractModel):
    """BatchDeregisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID\n        :type LoadBalancerId: str\n        :param Targets: 解绑目标\n        :type Targets: list of BatchTarget\n        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchDeregisterTargetsResponse(AbstractModel):
    """BatchDeregisterTargets返回参数结构体

    """

    def __init__(self):
        """
        :param FailListenerIdSet: 解绑失败的监听器ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailListenerIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchModifyTargetWeightRequest(AbstractModel):
    """BatchModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ModifyList: 要批量修改权重的列表\n        :type ModifyList: list of TargetsWeightRule\n        """
        self.LoadBalancerId = None
        self.ModifyList = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("ModifyList") is not None:
            self.ModifyList = []
            for item in params.get("ModifyList"):
                obj = TargetsWeightRule()
                obj._deserialize(item)
                self.ModifyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyTargetWeightResponse(AbstractModel):
    """BatchModifyTargetWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BatchRegisterTargetsRequest(AbstractModel):
    """BatchRegisterTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡ID\n        :type LoadBalancerId: str\n        :param Targets: 绑定目标\n        :type Targets: list of BatchTarget\n        """
        self.LoadBalancerId = None
        self.Targets = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = BatchTarget()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchRegisterTargetsResponse(AbstractModel):
    """BatchRegisterTargets返回参数结构体

    """

    def __init__(self):
        """
        :param FailListenerIdSet: 绑定失败的监听器ID，如为空表示全部绑定成功。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailListenerIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FailListenerIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.FailListenerIdSet = params.get("FailListenerIdSet")
        self.RequestId = params.get("RequestId")


class BatchTarget(AbstractModel):
    """负责均衡批量目标项

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerId: str\n        :param Port: 绑定端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param InstanceId: 子机ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param EniIp: 弹性网卡ip
注意：此字段可能返回 null，表示取不到有效值。\n        :type EniIp: str\n        :param Weight: 子机权重，范围[0, 100]。绑定时如果不存在，则默认为10。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        """
        self.ListenerId = None
        self.Port = None
        self.InstanceId = None
        self.EniIp = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.EniIp = params.get("EniIp")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class City(AbstractModel):
    """城市信息

    """

    def __init__(self):
        """
        :param CityId: 城市ID\n        :type CityId: str\n        :param CityName: 城市名称\n        :type CityName: str\n        """
        self.CityId = None
        self.CityName = None


    def _deserialize(self, params):
        self.CityId = params.get("CityId")
        self.CityName = params.get("CityName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Country(AbstractModel):
    """国家信息

    """

    def __init__(self):
        """
        :param CountryId: 国家ID\n        :type CountryId: str\n        :param CountryName: 国家名称\n        :type CountryName: str\n        """
        self.CountryId = None
        self.CountryName = None


    def _deserialize(self, params):
        self.CountryId = params.get("CountryId")
        self.CountryName = params.get("CountryName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: HAVIP所在私有网络ID。\n        :type VpcId: str\n        :param SubnetId: HAVIP所在子网ID。\n        :type SubnetId: str\n        :param HaVipName: HAVIP名称。\n        :type HaVipName: str\n        :param Vip: 指定虚拟IP地址，必须在VPC网段内且未被占用。不指定则自动分配。\n        :type Vip: str\n        """
        self.VpcId = None
        self.SubnetId = None
        self.HaVipName = None
        self.Vip = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip返回参数结构体

    """

    def __init__(self):
        """
        :param HaVip: HAVIP对象。\n        :type HaVip: :class:`tencentcloud.ecm.v20190719.models.HaVip`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.HaVip = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HaVip") is not None:
            self.HaVip = HaVip()
            self.HaVip._deserialize(params.get("HaVip"))
        self.RequestId = params.get("RequestId")


class CreateImageRequest(AbstractModel):
    """CreateImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageName: 镜像名称。\n        :type ImageName: str\n        :param InstanceId: 需要制作镜像的实例ID。\n        :type InstanceId: str\n        :param ImageDescription: 镜像描述。\n        :type ImageDescription: str\n        :param ForcePoweroff: 是否执行强制关机以制作镜像。取值范围：
TRUE：表示自动关机后制作镜像
FALSE：表示开机状态制作，目前不支持，需要先手动关机
默认取值：FALSE。\n        :type ForcePoweroff: str\n        """
        self.ImageName = None
        self.InstanceId = None
        self.ImageDescription = None
        self.ForcePoweroff = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.InstanceId = params.get("InstanceId")
        self.ImageDescription = params.get("ImageDescription")
        self.ForcePoweroff = params.get("ForcePoweroff")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateImageResponse(AbstractModel):
    """CreateImage返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务id\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CreateListenerRequest(AbstractModel):
    """CreateListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param Ports: 要将监听器创建到哪些端口，每个端口对应一个新的监听器\n        :type Ports: list of int\n        :param Protocol: 监听器协议： TCP | UDP\n        :type Protocol: str\n        :param ListenerNames: 要创建的监听器名称列表，名称与Ports数组按序一一对应，如不需立即命名，则无需提供此参数\n        :type ListenerNames: list of str\n        :param HealthCheck: 健康检查相关参数\n        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`\n        :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。\n        :type SessionExpireTime: int\n        :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。\n        :type Scheduler: str\n        :param SessionType: 会话保持类型。不传或传NORMAL表示默认会话保持类型。QUIC_CID 表示根据Quic Connection ID做会话保持。QUIC_CID只支持UDP协议。\n        :type SessionType: str\n        """
        self.LoadBalancerId = None
        self.Ports = None
        self.Protocol = None
        self.ListenerNames = None
        self.HealthCheck = None
        self.SessionExpireTime = None
        self.Scheduler = None
        self.SessionType = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.Ports = params.get("Ports")
        self.Protocol = params.get("Protocol")
        self.ListenerNames = params.get("ListenerNames")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.Scheduler = params.get("Scheduler")
        self.SessionType = params.get("SessionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateListenerResponse(AbstractModel):
    """CreateListener返回参数结构体

    """

    def __init__(self):
        """
        :param ListenerIds: 创建的监听器的唯一标识数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateLoadBalancerRequest(AbstractModel):
    """CreateLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM区域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        :param LoadBalancerType: 负载均衡实例的网络类型。目前只支持传入OPEN，表示公网属性。\n        :type LoadBalancerType: str\n        :param VipIsp: CMCC | CTCC | CUCC，分别对应 移动 | 电信 | 联通。\n        :type VipIsp: str\n        :param LoadBalancerName: 负载均衡实例的名称，只在创建一个实例的时候才会生效。规则：1-50 个英文、汉字、数字、连接线“-”或下划线“_”。
注意：如果名称与系统中已有负载均衡实例的名称相同，则系统将会自动生成此次创建的负载均衡实例的名称。\n        :type LoadBalancerName: str\n        :param VpcId: 负载均衡后端目标设备所属的网络 ID，如vpc-12345678。\n        :type VpcId: str\n        :param Number: 创建负载均衡的个数，默认值 1。\n        :type Number: int\n        :param InternetAccessible: 负载均衡的带宽限制等信息。\n        :type InternetAccessible: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`\n        :param Tags: 标签。\n        :type Tags: list of TagInfo\n        :param SecurityGroups: 安全组。\n        :type SecurityGroups: list of str\n        """
        self.EcmRegion = None
        self.LoadBalancerType = None
        self.VipIsp = None
        self.LoadBalancerName = None
        self.VpcId = None
        self.Number = None
        self.InternetAccessible = None
        self.Tags = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.VipIsp = params.get("VipIsp")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.VpcId = params.get("VpcId")
        self.Number = params.get("Number")
        if params.get("InternetAccessible") is not None:
            self.InternetAccessible = LoadBalancerInternetAccessible()
            self.InternetAccessible._deserialize(params.get("InternetAccessible"))
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLoadBalancerResponse(AbstractModel):
    """CreateLoadBalancer返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 由负载均衡实例ID组成的数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LoadBalancerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.RequestId = params.get("RequestId")


class CreateModuleRequest(AbstractModel):
    """CreateModule请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleName: 模块名称，如视频直播模块。限制：模块名称不得以空格开头，长度不得超过60个字符。\n        :type ModuleName: str\n        :param DefaultBandWidth: 默认带宽，单位：M。范围不得超过带宽上下限，详看DescribeConfig。\n        :type DefaultBandWidth: int\n        :param DefaultImageId: 默认镜像，如img-qsdf3ff2。\n        :type DefaultImageId: str\n        :param InstanceType: 机型ID。\n        :type InstanceType: str\n        :param DefaultSystemDiskSize: 默认系统盘大小，单位：G，默认大小为50G。范围不得超过系统盘上下限制，详看DescribeConfig。\n        :type DefaultSystemDiskSize: int\n        :param DefaultDataDiskSize: 默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。\n        :type DefaultDataDiskSize: int\n        :param CloseIpDirect: 是否关闭IP直通。取值范围：
true：表示关闭IP直通
false：表示开通IP直通\n        :type CloseIpDirect: bool\n        :param TagSpecification: 标签列表。\n        :type TagSpecification: list of TagSpecification\n        :param SecurityGroups: 模块默认安全组列表\n        :type SecurityGroups: list of str\n        :param DefaultBandWidthIn: 默认入带宽，单位：M。范围不得超过带宽上下限，详看DescribeConfig。\n        :type DefaultBandWidthIn: int\n        :param DisableWanIp: 是否禁止分配外网IP\n        :type DisableWanIp: bool\n        """
        self.ModuleName = None
        self.DefaultBandWidth = None
        self.DefaultImageId = None
        self.InstanceType = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None
        self.CloseIpDirect = None
        self.TagSpecification = None
        self.SecurityGroups = None
        self.DefaultBandWidthIn = None
        self.DisableWanIp = None


    def _deserialize(self, params):
        self.ModuleName = params.get("ModuleName")
        self.DefaultBandWidth = params.get("DefaultBandWidth")
        self.DefaultImageId = params.get("DefaultImageId")
        self.InstanceType = params.get("InstanceType")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        self.CloseIpDirect = params.get("CloseIpDirect")
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.SecurityGroups = params.get("SecurityGroups")
        self.DefaultBandWidthIn = params.get("DefaultBandWidthIn")
        self.DisableWanIp = params.get("DisableWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateModuleResponse(AbstractModel):
    """CreateModule返回参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID，创建模块成功后分配给该模块的ID。\n        :type ModuleId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ModuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。\n        :type NetworkInterfaceName: str\n        :param SubnetId: 弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。\n        :type SubnetId: str\n        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        :param NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。\n        :type NetworkInterfaceDescription: str\n        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，内网IP地址个数总和不能超过配额数。\n        :type SecondaryPrivateIpAddressCount: int\n        :param SecurityGroupIds: 指定绑定的安全组，例如：['sg-1dd51d']。\n        :type SecurityGroupIds: list of str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.EcmRegion = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterface: 弹性网卡实例。\n        :type NetworkInterface: :class:`tencentcloud.ecm.v20190719.models.NetworkInterface`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetworkInterface = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self.NetworkInterface = NetworkInterface()
            self.NetworkInterface._deserialize(params.get("NetworkInterface"))
        self.RequestId = params.get("RequestId")


class CreateRouteTableRequest(AbstractModel):
    """CreateRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param RouteTableName: 路由表名称，最大长度不能超过60个字节。\n        :type RouteTableName: str\n        :param EcmRegion: ecm地域\n        :type EcmRegion: str\n        """
        self.VpcId = None
        self.RouteTableName = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableName = params.get("RouteTableName")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RouteTable: 路由表对象\n        :type RouteTable: :class:`tencentcloud.ecm.v20190719.models.RouteTable`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RouteTable = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteTable") is not None:
            self.RouteTable = RouteTable()
            self.RouteTable._deserialize(params.get("RouteTable"))
        self.RequestId = params.get("RequestId")


class CreateRoutesRequest(AbstractModel):
    """CreateRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID。\n        :type RouteTableId: str\n        :param Routes: 要创建的路由策略对象。\n        :type Routes: list of Route\n        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 新增的实例个数。\n        :type TotalCount: int\n        :param RouteTableSet: 路由表对象。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableSet: list of RouteTable\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class CreateSecurityGroupPoliciesRequest(AbstractModel):
    """CreateSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type GroupName: str\n        :param GroupDescription: 安全组备注，最多100个字符。\n        :type GroupDescription: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.GroupName = None
        self.GroupDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全组对象。\n        :type SecurityGroup: :class:`tencentcloud.ecm.v20190719.models.SecurityGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param SubnetName: 子网名称，最大长度不能超过60个字节。\n        :type SubnetName: str\n        :param CidrBlock: 子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。\n        :type CidrBlock: str\n        :param Zone: 子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。\n        :type Zone: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.EcmRegion = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        self.EcmRegion = params.get("EcmRegion")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param Subnet: 子网对象。\n        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Subnet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self.Subnet = Subnet()
            self.Subnet._deserialize(params.get("Subnet"))
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcName: vpc名称，最大长度不能超过60个字节。\n        :type VpcName: str\n        :param CidrBlock: vpc的cidr，只能为10.*.0.0/16，172.[16-31].0.0/16，192.168.0.0/16这三个内网网段内。\n        :type CidrBlock: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param EnableMulticast: 是否开启组播。true: 开启, false: 不开启。暂不支持\n        :type EnableMulticast: str\n        :param DnsServers: DNS地址，最多支持4个，暂不支持\n        :type DnsServers: list of str\n        :param DomainName: 域名，暂不支持\n        :type DomainName: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        :param Description: 描述信息\n        :type Description: str\n        """
        self.VpcName = None
        self.CidrBlock = None
        self.EcmRegion = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None
        self.Tags = None
        self.Description = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EcmRegion = params.get("EcmRegion")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回参数结构体

    """

    def __init__(self):
        """
        :param Vpc: Vpc对象。\n        :type Vpc: :class:`tencentcloud.ecm.v20190719.models.VpcInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = VpcInfo()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: HAVIP唯一ID，形如：havip-9o233uri。\n        :type HaVipId: str\n        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteImageRequest(AbstractModel):
    """DeleteImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageIDSet: 镜像ID列表。\n        :type ImageIDSet: list of str\n        """
        self.ImageIDSet = None


    def _deserialize(self, params):
        self.ImageIDSet = params.get("ImageIDSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteImageResponse(AbstractModel):
    """DeleteImage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenerRequest(AbstractModel):
    """DeleteListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerId: 要删除的监听器 ID\n        :type ListenerId: str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenerResponse(AbstractModel):
    """DeleteListener返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerListenersRequest(AbstractModel):
    """DeleteLoadBalancerListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerIds: 指定删除的监听器ID数组，若不填则删除负载均衡的所有监听器\n        :type ListenerIds: list of str\n        """
        self.LoadBalancerId = None
        self.ListenerIds = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerListenersResponse(AbstractModel):
    """DeleteLoadBalancerListeners返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLoadBalancerRequest(AbstractModel):
    """DeleteLoadBalancer请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要删除的负载均衡实例 ID数组，数组大小最大支持20\n        :type LoadBalancerIds: list of str\n        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLoadBalancerResponse(AbstractModel):
    """DeleteLoadBalancer返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteModuleRequest(AbstractModel):
    """DeleteModule请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID。如：em-qn46snq8\n        :type ModuleId: str\n        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteModuleResponse(AbstractModel):
    """DeleteModule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        """
        self.NetworkInterfaceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c\n        :type RouteTableId: str\n        """
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param Routes: 路由策略对象。\n        :type Routes: list of Route\n        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。一个请求中只能删除单个方向的一条或多条规则。支持指定索引（PolicyIndex） 匹配删除和安全组规则匹配删除两种方式，一个请求中只能使用一种匹配方式。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。\n        :type SubnetId: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        """
        self.SubnetId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcRequest(AbstractModel):
    """DeleteVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        """
        self.VpcId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcResponse(AbstractModel):
    """DeleteVpc返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        """
        self.EcmRegion = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 账户 EIP 配额信息。\n        :type QuotaSet: list of EipQuota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = EipQuota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressIds: 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：eip-11112222。参数不支持同时指定AddressIds和Filters。\n        :type AddressIds: list of str\n        :param Filters: 每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定AddressIds和Filters。详细的过滤条件如下：
address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。
address-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。
address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。
address-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。取值范围：详见EIP状态列表。
instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。
private-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。
network-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。
is-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.EcmRegion = None
        self.AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressIds = params.get("AddressIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的 EIP 数量。\n        :type TotalCount: int\n        :param AddressSet: EIP 详细信息列表。\n        :type AddressSet: list of Address\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressSet") is not None:
            self.AddressSet = []
            for item in params.get("AddressSet"):
                obj = Address()
                obj._deserialize(item)
                self.AddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBaseOverviewRequest(AbstractModel):
    """DescribeBaseOverview请求参数结构体

    """


class DescribeBaseOverviewResponse(AbstractModel):
    """DescribeBaseOverview返回参数结构体

    """

    def __init__(self):
        """
        :param ModuleNum: 模块数量，单位：个\n        :type ModuleNum: int\n        :param NodeNum: 节点数量，单位：个\n        :type NodeNum: int\n        :param VcpuNum: cpu核数，单位：个\n        :type VcpuNum: int\n        :param MemoryNum: 内存大小，单位：G\n        :type MemoryNum: int\n        :param StorageNum: 硬盘大小，单位：G\n        :type StorageNum: int\n        :param NetworkNum: 昨日网络峰值,单位：M\n        :type NetworkNum: int\n        :param InstanceNum: 实例数量，单位：台\n        :type InstanceNum: int\n        :param RunningNum: 运行中数量，单位：台\n        :type RunningNum: int\n        :param IsolationNum: 安全隔离数量，单位：台\n        :type IsolationNum: int\n        :param ExpiredNum: 过期实例数量，单位：台\n        :type ExpiredNum: int\n        :param WillExpireNum: 即将过期实例数量，单位：台\n        :type WillExpireNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ModuleNum = None
        self.NodeNum = None
        self.VcpuNum = None
        self.MemoryNum = None
        self.StorageNum = None
        self.NetworkNum = None
        self.InstanceNum = None
        self.RunningNum = None
        self.IsolationNum = None
        self.ExpiredNum = None
        self.WillExpireNum = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ModuleNum = params.get("ModuleNum")
        self.NodeNum = params.get("NodeNum")
        self.VcpuNum = params.get("VcpuNum")
        self.MemoryNum = params.get("MemoryNum")
        self.StorageNum = params.get("StorageNum")
        self.NetworkNum = params.get("NetworkNum")
        self.InstanceNum = params.get("InstanceNum")
        self.RunningNum = params.get("RunningNum")
        self.IsolationNum = params.get("IsolationNum")
        self.ExpiredNum = params.get("ExpiredNum")
        self.WillExpireNum = params.get("WillExpireNum")
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkStorageRange: 网络带宽硬盘大小的范围信息。\n        :type NetworkStorageRange: :class:`tencentcloud.ecm.v20190719.models.NetworkStorageRange`\n        :param ImageWhiteSet: 镜像操作系统白名单。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageWhiteSet: list of str\n        :param InstanceNetworkLimitConfigs: 网络限额信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceNetworkLimitConfigs: list of InstanceNetworkLimitConfig\n        :param ImageLimits: 镜像限额信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageLimits: :class:`tencentcloud.ecm.v20190719.models.ImageLimitConfig`\n        :param DefaultIPDirect: 默认是否IP直通，用于模块创建，虚机购买等具有直通参数场景时的默认参数。\n        :type DefaultIPDirect: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetworkStorageRange = None
        self.ImageWhiteSet = None
        self.InstanceNetworkLimitConfigs = None
        self.ImageLimits = None
        self.DefaultIPDirect = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkStorageRange") is not None:
            self.NetworkStorageRange = NetworkStorageRange()
            self.NetworkStorageRange._deserialize(params.get("NetworkStorageRange"))
        self.ImageWhiteSet = params.get("ImageWhiteSet")
        if params.get("InstanceNetworkLimitConfigs") is not None:
            self.InstanceNetworkLimitConfigs = []
            for item in params.get("InstanceNetworkLimitConfigs"):
                obj = InstanceNetworkLimitConfig()
                obj._deserialize(item)
                self.InstanceNetworkLimitConfigs.append(obj)
        if params.get("ImageLimits") is not None:
            self.ImageLimits = ImageLimitConfig()
            self.ImageLimits._deserialize(params.get("ImageLimits"))
        self.DefaultIPDirect = params.get("DefaultIPDirect")
        self.RequestId = params.get("RequestId")


class DescribeCustomImageTaskRequest(AbstractModel):
    """DescribeCustomImageTask请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 支持key,value查询
task-id: 异步任务ID
image-id: 镜像ID
image-name: 镜像名称\n        :type Filters: list of Filter\n        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomImageTaskResponse(AbstractModel):
    """DescribeCustomImageTask返回参数结构体

    """

    def __init__(self):
        """
        :param ImageTaskSet: 导入任务详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageTaskSet: list of ImageTask\n        :param TotalCount: 总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageTaskSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImageTaskSet") is not None:
            self.ImageTaskSet = []
            for item in params.get("ImageTaskSet"):
                obj = ImageTask()
                obj._deserialize(item)
                self.ImageTaskSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDefaultSubnetRequest(AbstractModel):
    """DescribeDefaultSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM地域\n        :type EcmRegion: str\n        :param Zone: ECM可用区\n        :type Zone: str\n        """
        self.EcmRegion = None
        self.Zone = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultSubnetResponse(AbstractModel):
    """DescribeDefaultSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param Subnet: 默认子网信息，若无子网，则为空数据。\n        :type Subnet: :class:`tencentcloud.ecm.v20190719.models.Subnet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Subnet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self.Subnet = Subnet()
            self.Subnet._deserialize(params.get("Subnet"))
        self.RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipIds: HAVIP数组，HAVIP唯一ID，形如：havip-9o233uri。\n        :type HaVipIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定HaVipIds和Filters。
havip-id - String - HAVIP唯一ID，形如：havip-9o233uri。
havip-name - String - HAVIP名称。
vpc-id - String - HAVIP所在私有网络ID。
subnet-id - String - HAVIP所在子网ID。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认值是0。\n        :type Offset: int\n        :param Limit: 返回数量，默认值是20，最大是100。\n        :type Limit: int\n        :param EcmRegion: Ecm 区域，不填代表全部区域。\n        :type EcmRegion: str\n        """
        self.HaVipIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.HaVipIds = params.get("HaVipIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param HaVipSet: HAVIP对象数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HaVipSet: list of HaVip\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.HaVipSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("HaVipSet") is not None:
            self.HaVipSet = []
            for item in params.get("HaVipSet"):
                obj = HaVip()
                obj._deserialize(item)
                self.HaVipSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImageRequest(AbstractModel):
    """DescribeImage请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，每次请求的Filters的上限为10，详细的过滤条件如下：
image-id - String - 是否必填： 否 - （过滤条件）按照镜像ID进行过滤
image-type - String - 是否必填： 否 - （过滤条件）按照镜像类型进行过滤。取值范围：
PRIVATE_IMAGE: 私有镜像 (本帐户创建的镜像) 
PUBLIC_IMAGE: 公共镜像 (腾讯云官方镜像)
instance-type -String - 是否必填: 否 - (过滤条件) 按机型过滤支持的镜像
image-name - String - 是否必填：否 - (过滤条件) 按镜像的名称模糊匹配，只能提供一个值
image-os - String - 是否必填：否 - (过滤条件) 按镜像系统的名称模糊匹配，只能提供一个值\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。\n        :type Limit: int\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageResponse(AbstractModel):
    """DescribeImage返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 镜像总数\n        :type TotalCount: int\n        :param ImageSet: 镜像数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageSet: list of Image\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ImageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ImageSet") is not None:
            self.ImageSet = []
            for item in params.get("ImageSet"):
                obj = Image()
                obj._deserialize(item)
                self.ImageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeImportImageOsRequest(AbstractModel):
    """DescribeImportImageOs请求参数结构体

    """


class DescribeImportImageOsResponse(AbstractModel):
    """DescribeImportImageOs返回参数结构体

    """

    def __init__(self):
        """
        :param ImportImageOsListSupported: 支持的导入镜像的操作系统类型\n        :type ImportImageOsListSupported: :class:`tencentcloud.ecm.v20190719.models.ImageOsList`\n        :param ImportImageOsVersionSet: 支持的导入镜像的操作系统版本\n        :type ImportImageOsVersionSet: list of OsVersion\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImportImageOsListSupported = None
        self.ImportImageOsVersionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ImportImageOsListSupported") is not None:
            self.ImportImageOsListSupported = ImageOsList()
            self.ImportImageOsListSupported._deserialize(params.get("ImportImageOsListSupported"))
        if params.get("ImportImageOsVersionSet") is not None:
            self.ImportImageOsVersionSet = []
            for item in params.get("ImportImageOsVersionSet"):
                obj = OsVersion()
                obj._deserialize(item)
                self.ImportImageOsVersionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceTypeConfigRequest(AbstractModel):
    """DescribeInstanceTypeConfig请求参数结构体

    """


class DescribeInstanceTypeConfigResponse(AbstractModel):
    """DescribeInstanceTypeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 总数\n        :type TotalCount: int\n        :param InstanceTypeConfigSet: 机型配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceTypeConfigSet: list of InstanceTypeConfig\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceTypeConfigSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceTypeConfigSet") is not None:
            self.InstanceTypeConfigSet = []
            for item in params.get("InstanceTypeConfigSet"):
                obj = InstanceTypeConfig()
                obj._deserialize(item)
                self.InstanceTypeConfigSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstanceVncUrlRequest(AbstractModel):
    """DescribeInstanceVncUrl请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 一个操作的实例ID。可通过DescribeInstances API返回值中的InstanceId获取。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstanceVncUrlResponse(AbstractModel):
    """DescribeInstanceVncUrl返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceVncUrl: 实例的管理终端地址。\n        :type InstanceVncUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceVncUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceVncUrl = params.get("InstanceVncUrl")
        self.RequestId = params.get("RequestId")


class DescribeInstancesDeniedActionsRequest(AbstractModel):
    """DescribeInstancesDeniedActions请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 无\n        :type InstanceIdSet: list of str\n        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesDeniedActionsResponse(AbstractModel):
    """DescribeInstancesDeniedActions返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceOperatorSet: 实例对应的禁止操作\n        :type InstanceOperatorSet: list of InstanceOperator\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceOperatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceOperatorSet") is not None:
            self.InstanceOperatorSet = []
            for item in params.get("InstanceOperatorSet"):
                obj = InstanceOperator()
                obj._deserialize(item)
                self.InstanceOperatorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeInstancesRequest(AbstractModel):
    """DescribeInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
zone      String      是否必填：否     （过滤条件）按照可用区英文标识符过滤。
zone-name      String      是否必填：否     （过滤条件）按照可用区中文名过滤,支持模糊匹配。
module-id      String      是否必填：否     （过滤条件）按照模块ID过滤。
instance-id      String      是否必填：否      （过滤条件）按照实例ID过滤。
instance-name      String      是否必填：否      （过滤条件）按照实例名称过滤,支持模糊匹配。
ip-address      String      是否必填：否      （过滤条件）按照实例的内网/公网IP过滤。
instance-uuid   string 是否必填：否 （过滤条件）按照uuid过滤实例列表。
instance-state  string  是否必填：否 （过滤条件）按照实例状态更新实例列表。
internet-service-provider      String      是否必填：否      （过滤条件）按照实例公网IP所属的运营商进行过滤。
tag-key      String      是否必填：否      （过滤条件）按照标签键进行过滤。
tag:tag-key      String      是否必填：否      （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。
instance-family      String      是否必填：否      （过滤条件）按照机型family过滤。
module-name      String      是否必填：否      （过滤条件）按照模块名称过滤,支持模糊匹配。
image-id      String      是否必填：否      （过滤条件）按照实例的镜像ID过滤。
vpc-id String      是否必填：否      （过滤条件）按照实例的vpc id过滤。
subnet-id String      是否必填：否      （过滤条件）按照实例的subnet id过滤。

若不传Filters参数则表示查询所有相关的实例信息。
单次请求的Filter.Values的上限为5。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20(如果查询结果数目大于等于20)，最大值为100。\n        :type Limit: int\n        :param OrderByField: 指定排序字段。目前支持的可选值如下
timestamp 按实例创建时间排序。
注意：目前仅支持按创建时间排序，后续可能会有扩展。
如果不传，默认按实例创建时间排序\n        :type OrderByField: str\n        :param OrderDirection: 指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序\n        :type OrderDirection: int\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderByField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByField = params.get("OrderByField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeInstancesResponse(AbstractModel):
    """DescribeInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 返回的实例相关信息列表的长度。\n        :type TotalCount: int\n        :param InstanceSet: 返回的实例相关信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceSet: list of Instance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = Instance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenersRequest(AbstractModel):
    """DescribeListeners请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerIds: 要查询的负载均衡监听器 ID数组\n        :type ListenerIds: list of str\n        :param Protocol: 要查询的监听器协议类型，取值 TCP | UDP\n        :type Protocol: str\n        :param Port: 要查询的监听器的端口\n        :type Port: int\n        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenersResponse(AbstractModel):
    """DescribeListeners返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listeners: list of Listener\n        :param TotalCount: 总的监听器个数
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Listeners = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = Listener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalanceTaskStatusRequest(AbstractModel):
    """DescribeLoadBalanceTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 请求ID，即接口返回的 RequestId 参数\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalanceTaskStatusResponse(AbstractModel):
    """DescribeLoadBalanceTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 任务的当前状态。 0：成功，1：失败，2：进行中。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class DescribeLoadBalancersRequest(AbstractModel):
    """DescribeLoadBalancers请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: 区域。如果不传则默认查询所有区域。\n        :type EcmRegion: str\n        :param LoadBalancerIds: 负载均衡实例 ID。\n        :type LoadBalancerIds: list of str\n        :param LoadBalancerName: 负载均衡实例的名称。\n        :type LoadBalancerName: str\n        :param LoadBalancerVips: 负载均衡实例的 VIP 地址，支持多个。\n        :type LoadBalancerVips: list of str\n        :param BackendPrivateIps: 负载均衡绑定的后端服务的内网 IP。\n        :type BackendPrivateIps: list of str\n        :param Offset: 数据偏移量，默认为 0。\n        :type Offset: int\n        :param Limit: 返回负载均衡实例的数量，默认为20，最大值为100。\n        :type Limit: int\n        :param WithBackend: 负载均衡是否绑定后端服务，0：没有绑定后端服务，1：绑定后端服务，-1：查询全部。 
如果不传则默认查询全部。\n        :type WithBackend: int\n        :param VpcId: 负载均衡实例所属私有网络唯一ID，如 vpc-bhqkbhdx。\n        :type VpcId: str\n        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为100。详细的过滤条件如下：
tag-key - String - 是否必填：否 - （过滤条件）按照标签的键过滤。\n        :type Filters: list of Filter\n        :param SecurityGroup: 安全组。\n        :type SecurityGroup: str\n        """
        self.EcmRegion = None
        self.LoadBalancerIds = None
        self.LoadBalancerName = None
        self.LoadBalancerVips = None
        self.BackendPrivateIps = None
        self.Offset = None
        self.Limit = None
        self.WithBackend = None
        self.VpcId = None
        self.Filters = None
        self.SecurityGroup = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.BackendPrivateIps = params.get("BackendPrivateIps")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.WithBackend = params.get("WithBackend")
        self.VpcId = params.get("VpcId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SecurityGroup = params.get("SecurityGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeLoadBalancersResponse(AbstractModel):
    """DescribeLoadBalancers返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 满足过滤条件的负载均衡实例总数。此数值与入参中的Limit无关。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param LoadBalancerSet: 返回的负载均衡实例数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerSet: list of LoadBalancer\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.LoadBalancerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("LoadBalancerSet") is not None:
            self.LoadBalancerSet = []
            for item in params.get("LoadBalancerSet"):
                obj = LoadBalancer()
                obj._deserialize(item)
                self.LoadBalancerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeModuleDetailRequest(AbstractModel):
    """DescribeModuleDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID，如em-qn46snq8。\n        :type ModuleId: str\n        """
        self.ModuleId = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleDetailResponse(AbstractModel):
    """DescribeModuleDetail返回参数结构体

    """

    def __init__(self):
        """
        :param Module: 模块的详细信息，详细见数据结构中的ModuleInfo。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`\n        :param ModuleCounter: 模块的统计信息，详细见数据结构中的ModuleCounterInfo。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModuleCounter: :class:`tencentcloud.ecm.v20190719.models.ModuleCounter`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Module = None
        self.ModuleCounter = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))
        if params.get("ModuleCounter") is not None:
            self.ModuleCounter = ModuleCounter()
            self.ModuleCounter._deserialize(params.get("ModuleCounter"))
        self.RequestId = params.get("RequestId")


class DescribeModuleRequest(AbstractModel):
    """DescribeModule请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
module-name - string - 是否必填：否 - （过滤条件）按照模块名称过滤。
module-id - string - 是否必填：否 - （过滤条件）按照模块ID过滤。
image-id      String      是否必填：否      （过滤条件）按照镜像ID过滤。
instance-family      String      是否必填：否      （过滤条件）按照机型family过滤。
security-group-id - string 是否必填：否 - （过滤条件）按照模块绑定的安全组id过滤。
每次请求的Filters的上限为10，Filter.Values的上限为5。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于Limit的更进一步介绍请参考 API 简介中的相关小节。\n        :type Limit: int\n        :param OrderByField: 指定排序字段。目前支持的可选值如下
instance-num 按实例数量排序。
node-num 按节点数量排序。
timestamp 按实例创建时间排序。
如果不传，默认按实例创建时间排序\n        :type OrderByField: str\n        :param OrderDirection: 指定排序是降序还是升序。0表示降序； 1表示升序。如果不传默认为降序\n        :type OrderDirection: int\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderByField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderByField = params.get("OrderByField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeModuleResponse(AbstractModel):
    """DescribeModule返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的模块数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param ModuleItemSet: 模块详情信息的列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModuleItemSet: list of ModuleItem\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ModuleItemSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ModuleItemSet") is not None:
            self.ModuleItemSet = []
            for item in params.get("ModuleItemSet"):
                obj = ModuleItem()
                obj._deserialize(item)
                self.ModuleItemSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeMonthPeakNetworkRequest(AbstractModel):
    """DescribeMonthPeakNetwork请求参数结构体

    """

    def __init__(self):
        """
        :param Month: 月份时间(xxxx-xx) 如2021-03,默认取当前时间的上一个月份\n        :type Month: str\n        :param Filters: 过滤条件\n        :type Filters: list of Filter\n        """
        self.Month = None
        self.Filters = None


    def _deserialize(self, params):
        self.Month = params.get("Month")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonthPeakNetworkResponse(AbstractModel):
    """DescribeMonthPeakNetwork返回参数结构体

    """

    def __init__(self):
        """
        :param MonthNetWorkData: 无
注意：此字段可能返回 null，表示取不到有效值。\n        :type MonthNetWorkData: list of MonthNetwork\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.MonthNetWorkData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MonthNetWorkData") is not None:
            self.MonthNetWorkData = []
            for item in params.get("MonthNetWorkData"):
                obj = MonthNetwork()
                obj._deserialize(item)
                self.MonthNetWorkData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。\n        :type NetworkInterfaceIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。
network-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。
attachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ein-3nqpdn3i。
groups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。
network-interface-name - String - （过滤条件）网卡实例名称。
network-interface-description - String - （过滤条件）网卡实例描述。
address-ip - String - （过滤条件）内网IPv4地址。
tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。使用请参考示例2
tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3。
is-primary - Boolean - 是否必填：否 - （过滤条件）按照是否主网卡进行过滤。值为true时，仅过滤主网卡；值为false时，仅过滤辅助网卡；次过滤参数为提供时，同时过滤主网卡和辅助网卡。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        """
        self.NetworkInterfaceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param NetworkInterfaceSet: 实例详细信息列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetworkInterfaceSet: list of NetworkInterface\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.NetworkInterfaceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("NetworkInterfaceSet") is not None:
            self.NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self.NetworkInterfaceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNodeRequest(AbstractModel):
    """DescribeNode请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，name取值为： InstanceFamily-实例系列\n        :type Filters: list of Filter\n        """
        self.Filters = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNodeResponse(AbstractModel):
    """DescribeNode返回参数结构体

    """

    def __init__(self):
        """
        :param NodeSet: 节点详细信息的列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type NodeSet: list of Node\n        :param TotalCount: 所有的节点数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NodeSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NodeSet") is not None:
            self.NodeSet = []
            for item in params.get("NodeSet"):
                obj = Node()
                obj._deserialize(item)
                self.NodeSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePeakBaseOverviewRequest(AbstractModel):
    """DescribePeakBaseOverview请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期，不应与当前日期间隔超过90天。\n        :type StartTime: str\n        :param EndTime: 结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天，不应与当前日期间隔超过90天。当开始与结束间隔不超过30天时返回1小时粒度的数据，否则返回3小时粒度的数据。\n        :type EndTime: str\n        """
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakBaseOverviewResponse(AbstractModel):
    """DescribePeakBaseOverview返回参数结构体

    """

    def __init__(self):
        """
        :param PeakFamilyInfoSet: 基础峰值列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PeakFamilyInfoSet: list of PeakFamilyInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PeakFamilyInfoSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakFamilyInfoSet") is not None:
            self.PeakFamilyInfoSet = []
            for item in params.get("PeakFamilyInfoSet"):
                obj = PeakFamilyInfo()
                obj._deserialize(item)
                self.PeakFamilyInfoSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePeakNetworkOverviewRequest(AbstractModel):
    """DescribePeakNetworkOverview请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间（xxxx-xx-xx）如2019-08-14，默认为一周之前的日期，不应与当前日期间隔超过30天。\n        :type StartTime: str\n        :param EndTime: 结束时间（xxxx-xx-xx）如2019-08-14，默认为昨天，不应与当前日期间隔超过30天。当开始与结束间隔不超过1天时会返回1分钟粒度的数据，不超过7天时返回5分钟粒度的数据，否则返回1小时粒度的数据。\n        :type EndTime: str\n        :param Filters: 过滤条件。

region    String      是否必填：否     （过滤条件）按照region过滤，不支持模糊匹配。注意 region 填上需要查询ecm region才能返回数据。
area       String      是否必填：否     （过滤条件）按照大区过滤，不支持模糊匹配。大区包括：china-central、china-east等等，可以通过DescribeNode获得所有大区；也可使用ALL_REGION表示所有地区。
isp         String      是否必填：否     （过滤条件）按照运营商过滤大区流量，运营商包括CTCC、CUCC和CMCC。只和area同时使用，且一次只能指定一种运营商。

region和area只应填写一个。\n        :type Filters: list of Filter\n        :param Period: 统计周期，单位秒。取值60/300。\n        :type Period: int\n        """
        self.StartTime = None
        self.EndTime = None
        self.Filters = None
        self.Period = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePeakNetworkOverviewResponse(AbstractModel):
    """DescribePeakNetworkOverview返回参数结构体

    """

    def __init__(self):
        """
        :param PeakNetworkRegionSet: 网络峰值数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PeakNetworkRegionSet: list of PeakNetworkRegionInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.PeakNetworkRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PeakNetworkRegionSet") is not None:
            self.PeakNetworkRegionSet = []
            for item in params.get("PeakNetworkRegionSet"):
                obj = PeakNetworkRegionInfo()
                obj._deserialize(item)
                self.PeakNetworkRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteConflictsRequest(AbstractModel):
    """DescribeRouteConflicts请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param DestinationCidrBlocks: 要检查的与之冲突的目的端列表\n        :type DestinationCidrBlocks: list of str\n        """
        self.RouteTableId = None
        self.DestinationCidrBlocks = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlocks = params.get("DestinationCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteConflictsResponse(AbstractModel):
    """DescribeRouteConflicts返回参数结构体

    """

    def __init__(self):
        """
        :param RouteConflictSet: 路由策略冲突列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteConflictSet: list of RouteConflict\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RouteConflictSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteConflictSet") is not None:
            self.RouteConflictSet = []
            for item in params.get("RouteConflictSet"):
                obj = RouteConflict()
                obj._deserialize(item)
                self.RouteConflictSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRouteTablesRequest(AbstractModel):
    """DescribeRouteTables请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableIds: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
route-table-id - String - （过滤条件）路由表实例ID。
route-table-name - String - （过滤条件）路由表名称。
vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。
association.main - String - （过滤条件）是否主路由表。\n        :type Filters: list of Filter\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 限数\n        :type Limit: int\n        :param EcmRegion: ECM 地域，传空或不传表示所有区域\n        :type EcmRegion: str\n        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None


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
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量\n        :type TotalCount: int\n        :param RouteTableSet: 路由表列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableSet: list of RouteTable\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeSecurityGroupAssociationStatisticsRequest(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全实例ID，例如esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。\n        :type SecurityGroupIds: list of str\n        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupAssociationStatisticsSet: 安全组关联实例统计。\n        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroupAssociationStatisticsSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupAssociationStatisticsSet") is not None:
            self.SecurityGroupAssociationStatisticsSet = []
            for item in params.get("SecurityGroupAssociationStatisticsSet"):
                obj = SecurityGroupAssociationStatistics()
                obj._deserialize(item)
                self.SecurityGroupAssociationStatisticsSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupLimitsRequest(AbstractModel):
    """DescribeSecurityGroupLimits请求参数结构体

    """


class DescribeSecurityGroupLimitsResponse(AbstractModel):
    """DescribeSecurityGroupLimits返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupLimitSet: 用户安全组配额限制。\n        :type SecurityGroupLimitSet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupLimitSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroupLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupLimitSet") is not None:
            self.SecurityGroupLimitSet = SecurityGroupLimitSet()
            self.SecurityGroupLimitSet._deserialize(params.get("SecurityGroupLimitSet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如：esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。\n        :type SecurityGroupId: str\n        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupPolicySet: 安全组规则集合。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroupPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全组实例ID，例如：esg-33ocnj9n，可通过[DescribeSecurityGroups](https://cloud.tencent.com/document/product/1108/47697)获取。每次请求的实例的上限为100。参数不支持同时指定SecurityGroupIds和Filters。\n        :type SecurityGroupIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定SecurityGroupIds和Filters。
security-group-id - String - （过滤条件）安全组ID。
security-group-name - String - （过滤条件）安全组名称。
tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.SecurityGroupIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param SecurityGroupSet: 安全组对象。\n        :type SecurityGroupSet: list of SecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetIds: 子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。\n        :type SubnetIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
subnet-id - String - Subnet实例名称。
subnet-name - String - 子网名称。只支持单值的模糊查询。
cidr-block - String - 子网网段，形如: 192.168.1.0 。只支持单值的模糊查询。
vpc-id - String - VPC实例ID，形如：vpc-f49l6u0z。
vpc-cidr-block  - String - vpc网段，形如: 192.168.1.0 。只支持单值的模糊查询。
region - String - ECM地域
zone - String - 可用区。
tag-key - String -是否必填：否- 按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - 按照标签键值对进行过滤。\n        :type Filters: list of Filter\n        :param Offset: 偏移量\n        :type Offset: str\n        :param Limit: 返回数量\n        :type Limit: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param Sort: 排序方式：time时间倒序, default按照网络规划排序\n        :type Sort: str\n        """
        self.SubnetIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None
        self.Sort = None


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
        self.EcmRegion = params.get("EcmRegion")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSubnetsResponse(AbstractModel):
    """DescribeSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param SubnetSet: 子网对象。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetSet: list of Subnet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.SubnetSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetHealthRequest(AbstractModel):
    """DescribeTargetHealth请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 要查询的负载均衡实例 ID列表\n        :type LoadBalancerIds: list of str\n        """
        self.LoadBalancerIds = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetHealthResponse(AbstractModel):
    """DescribeTargetHealth返回参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancers: 负载均衡实例列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancers: list of LoadBalancerHealth\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LoadBalancers = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LoadBalancers") is not None:
            self.LoadBalancers = []
            for item in params.get("LoadBalancers"):
                obj = LoadBalancerHealth()
                obj._deserialize(item)
                self.LoadBalancers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTargetsRequest(AbstractModel):
    """DescribeTargets请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerIds: 监听器 ID列表\n        :type ListenerIds: list of str\n        :param Protocol: 监听器协议类型\n        :type Protocol: int\n        :param Port: 监听器端口\n        :type Port: int\n        """
        self.LoadBalancerId = None
        self.ListenerIds = None
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerIds = params.get("ListenerIds")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTargetsResponse(AbstractModel):
    """DescribeTargets返回参数结构体

    """

    def __init__(self):
        """
        :param Listeners: 监听器后端绑定的机器信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listeners: list of ListenerBackend\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerBackend()
                obj._deserialize(item)
                self.Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param TaskId: 异步任务ID。\n        :type TaskId: str\n        """
        self.EcmRegion = None
        self.TaskId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskResultResponse(AbstractModel):
    """DescribeTaskResult返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID。\n        :type TaskId: str\n        :param Result: 执行结果，包括"SUCCESS", "FAILED", "RUNNING"\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeTaskStatusRequest(AbstractModel):
    """DescribeTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param TaskSet: 任务描述\n        :type TaskSet: list of TaskInput\n        """
        self.TaskSet = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskInput()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTaskStatusResponse(AbstractModel):
    """DescribeTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param TaskSet: 任务描述\n        :type TaskSet: list of TaskOutput\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskSet") is not None:
            self.TaskSet = []
            for item in params.get("TaskSet"):
                obj = TaskOutput()
                obj._deserialize(item)
                self.TaskSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。\n        :type VpcIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
vpc-name - String - VPC实例名称，只支持单值的模糊查询。
vpc-id - String - VPC实例ID形如：vpc-f49l6u0z。
cidr-block - String - vpc的cidr，只支持单值的模糊查询。
region - String - vpc的region。
tag-key - String -是否必填：否- 按照标签键进行过滤。
tag:tag-key - String - 是否必填：否 - 按照标签键值对进行过滤。\n        :type Filters: list of Filter\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        :param EcmRegion: 地域\n        :type EcmRegion: str\n        :param Sort: 排序方式：time时间倒序, default按照网络规划排序\n        :type Sort: str\n        """
        self.VpcIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EcmRegion = None
        self.Sort = None


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
        self.EcmRegion = params.get("EcmRegion")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcsResponse(AbstractModel):
    """DescribeVpcs返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param VpcSet: 私有网络对象。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcSet: list of VpcInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param InstanceId: 实例ID。形如：ein-hcs7jkg4\n        :type InstanceId: str\n        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableRoutesRequest(AbstractModel):
    """DisableRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param RouteIds: 路由策略ID。\n        :type RouteIds: list of int non-negative\n        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableRoutesResponse(AbstractModel):
    """DisableRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。\n        :type AddressId: str\n        :param ReallocateNormalPublicIp: 表示解绑 EIP 之后是否分配普通公网 IP。取值范围：
TRUE：表示解绑 EIP 之后分配普通公网 IP。
FALSE：表示解绑 EIP 之后不分配普通公网 IP。
默认取值：FALSE。

只有满足以下条件时才能指定该参数：
只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。
解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 DescribeAddressQuota 接口获取。\n        :type ReallocateNormalPublicIp: bool\n        """
        self.EcmRegion = None
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressId = params.get("AddressId")
        self.ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisassociateSecurityGroupsRequest(AbstractModel):
    """DisassociateSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 要解绑的安全组ID，类似esg-efil73jd，只支持解绑单个安全组。\n        :type SecurityGroupIds: list of str\n        :param InstanceIds: 被解绑的实例ID，类似ein-lesecurk，支持指定多个实例 。\n        :type InstanceIds: list of str\n        """
        self.SecurityGroupIds = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateSecurityGroupsResponse(AbstractModel):
    """DisassociateSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DiskInfo(AbstractModel):
    """磁盘信息

    """

    def __init__(self):
        """
        :param DiskType: 磁盘类型：LOCAL_BASIC\n        :type DiskType: str\n        :param DiskId: 磁盘ID\n        :type DiskId: str\n        :param DiskSize: 磁盘大小（GB）\n        :type DiskSize: int\n        """
        self.DiskType = None
        self.DiskId = None
        self.DiskSize = None


    def _deserialize(self, params):
        self.DiskType = params.get("DiskType")
        self.DiskId = params.get("DiskId")
        self.DiskSize = params.get("DiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipQuota(AbstractModel):
    """描述EIP配额信息

    """

    def __init__(self):
        """
        :param QuotaId: 配额名称，取值范围：
TOTAL_EIP_QUOTA：用户当前地域下EIP的配额数；
DAILY_EIP_APPLY：用户当前地域下今日申购次数；
DAILY_PUBLIC_IP_ASSIGN：用户当前地域下，重新分配公网 IP次数。\n        :type QuotaId: str\n        :param QuotaCurrent: 当前数量\n        :type QuotaCurrent: int\n        :param QuotaLimit: 配额数量\n        :type QuotaLimit: int\n        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param RouteIds: 路由策略ID。\n        :type RouteIds: list of int non-negative\n        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableRoutesResponse(AbstractModel):
    """EnableRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnhancedService(AbstractModel):
    """增强服务

    """

    def __init__(self):
        """
        :param SecurityService: 是否开启云镜服务。\n        :type SecurityService: :class:`tencentcloud.ecm.v20190719.models.RunSecurityServiceEnabled`\n        :param MonitorService: 是否开启云监控服务。\n        :type MonitorService: :class:`tencentcloud.ecm.v20190719.models.RunMonitorServiceEnabled`\n        :param EIPDirectService: 是否开通IP直通。若不指定该参数，则Linux镜像默认开通，windows镜像暂不支持IP直通。\n        :type EIPDirectService: :class:`tencentcloud.ecm.v20190719.models.RunEIPDirectServiceEnabled`\n        """
        self.SecurityService = None
        self.MonitorService = None
        self.EIPDirectService = None


    def _deserialize(self, params):
        if params.get("SecurityService") is not None:
            self.SecurityService = RunSecurityServiceEnabled()
            self.SecurityService._deserialize(params.get("SecurityService"))
        if params.get("MonitorService") is not None:
            self.MonitorService = RunMonitorServiceEnabled()
            self.MonitorService._deserialize(params.get("MonitorService"))
        if params.get("EIPDirectService") is not None:
            self.EIPDirectService = RunEIPDirectServiceEnabled()
            self.EIPDirectService._deserialize(params.get("EIPDirectService"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。

    """

    def __init__(self):
        """
        :param Values: 一个或者多个过滤值。\n        :type Values: list of str\n        :param Name: 过滤键的名称。\n        :type Name: str\n        """
        self.Values = None
        self.Name = None


    def _deserialize(self, params):
        self.Values = params.get("Values")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVip(AbstractModel):
    """HAVIP对象。

    """

    def __init__(self):
        """
        :param HaVipId: HAVIP的ID，是HAVIP的唯一标识。\n        :type HaVipId: str\n        :param HaVipName: HAVIP名称。\n        :type HaVipName: str\n        :param Vip: 虚拟IP地址。\n        :type Vip: str\n        :param VpcId: HAVIP所在私有网络ID。\n        :type VpcId: str\n        :param SubnetId: HAVIP所在子网ID。\n        :type SubnetId: str\n        :param NetworkInterfaceId: HAVIP关联弹性网卡ID。\n        :type NetworkInterfaceId: str\n        :param InstanceId: 被绑定的实例ID。\n        :type InstanceId: str\n        :param AddressIp: 绑定EIP。\n        :type AddressIp: str\n        :param State: 状态：
AVAILABLE：运行中。
UNBIND：未绑定。\n        :type State: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param Business: 使用havip的业务标识。\n        :type Business: str\n        """
        self.HaVipId = None
        self.HaVipName = None
        self.Vip = None
        self.VpcId = None
        self.SubnetId = None
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.AddressIp = None
        self.State = None
        self.CreatedTime = None
        self.Business = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.AddressIp = params.get("AddressIp")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HealthCheck(AbstractModel):
    """负载均衡健康检查

    """

    def __init__(self):
        """
        :param HealthSwitch: 是否开启健康检查：1（开启）、0（关闭）
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthSwitch: int\n        :param TimeOut: 健康检查的响应超时时间，可选值：2~60，默认值：2，单位：秒。响应超时时间要小于检查间隔时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeOut: int\n        :param IntervalTime: 健康检查探测间隔时间，默认值：5，可选值：5~300，单位：秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IntervalTime: int\n        :param HealthNum: 健康阈值，默认值：3，表示当连续探测三次健康则表示该转发正常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthNum: int\n        :param UnHealthyNum: 不健康阈值，默认值：3，表示当连续探测三次不健康则表示该转发异常，可选值：2~10，单位：次。
注意：此字段可能返回 null，表示取不到有效值。\n        :type UnHealthyNum: int\n        :param CheckPort: 自定义探测相关参数。健康检查端口，默认为后端服务的端口，除非您希望指定特定端口，否则建议留空。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CheckPort: int\n        :param ContextType: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查的输入格式，可取值：HEX或TEXT；取值为HEX时，SendContext和RecvContext的字符只能在0123456789ABCDEF中选取且长度必须是偶数位。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContextType: str\n        :param SendContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查发送的请求内容，只允许ASCII可见字符，最大长度限制500。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SendContext: str\n        :param RecvContext: 自定义探测相关参数。健康检查协议CheckType的值取CUSTOM时，必填此字段，代表健康检查返回的结果，只允许ASCII可见字符，最大长度限制500。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RecvContext: str\n        :param CheckType: 自定义探测相关参数。健康检查使用的协议：TCP | CUSTOM（UDP监听器只支持CUSTOM；如果使用自定义健康检查功能，则必传）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CheckType: str\n        """
        self.HealthSwitch = None
        self.TimeOut = None
        self.IntervalTime = None
        self.HealthNum = None
        self.UnHealthyNum = None
        self.CheckPort = None
        self.ContextType = None
        self.SendContext = None
        self.RecvContext = None
        self.CheckType = None


    def _deserialize(self, params):
        self.HealthSwitch = params.get("HealthSwitch")
        self.TimeOut = params.get("TimeOut")
        self.IntervalTime = params.get("IntervalTime")
        self.HealthNum = params.get("HealthNum")
        self.UnHealthyNum = params.get("UnHealthyNum")
        self.CheckPort = params.get("CheckPort")
        self.ContextType = params.get("ContextType")
        self.SendContext = params.get("SendContext")
        self.RecvContext = params.get("RecvContext")
        self.CheckType = params.get("CheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISP(AbstractModel):
    """运营商信息

    """

    def __init__(self):
        """
        :param ISPId: 运营商ID\n        :type ISPId: str\n        :param ISPName: 运营商名称\n        :type ISPName: str\n        """
        self.ISPId = None
        self.ISPName = None


    def _deserialize(self, params):
        self.ISPId = params.get("ISPId")
        self.ISPName = params.get("ISPName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ISPCounter(AbstractModel):
    """运行商统计信息

    """

    def __init__(self):
        """
        :param ProviderName: 运营商名称\n        :type ProviderName: str\n        :param ProviderNodeNum: 节点数量\n        :type ProviderNodeNum: int\n        :param ProvederInstanceNum: 实例数量\n        :type ProvederInstanceNum: int\n        :param ZoneInstanceInfoSet: Zone实例信息结构体数组\n        :type ZoneInstanceInfoSet: list of ZoneInstanceInfo\n        """
        self.ProviderName = None
        self.ProviderNodeNum = None
        self.ProvederInstanceNum = None
        self.ZoneInstanceInfoSet = None


    def _deserialize(self, params):
        self.ProviderName = params.get("ProviderName")
        self.ProviderNodeNum = params.get("ProviderNodeNum")
        self.ProvederInstanceNum = params.get("ProvederInstanceNum")
        if params.get("ZoneInstanceInfoSet") is not None:
            self.ZoneInstanceInfoSet = []
            for item in params.get("ZoneInstanceInfoSet"):
                obj = ZoneInstanceInfo()
                obj._deserialize(item)
                self.ZoneInstanceInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Image(AbstractModel):
    """镜像信息

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID\n        :type ImageId: str\n        :param ImageName: 镜像名称\n        :type ImageName: str\n        :param ImageState: 镜像状态\n        :type ImageState: str\n        :param ImageType: 镜像类型\n        :type ImageType: str\n        :param ImageOsName: 操作系统名称\n        :type ImageOsName: str\n        :param ImageDescription: 镜像描述\n        :type ImageDescription: str\n        :param ImageCreateTime: 镜像导入时间\n        :type ImageCreateTime: str\n        :param Architecture: 操作系统位数\n        :type Architecture: str\n        :param OsType: 操作系统类型\n        :type OsType: str\n        :param OsVersion: 操作系统版本\n        :type OsVersion: str\n        :param Platform: 操作系统平台\n        :type Platform: str\n        :param ImageOwner: 镜像所有者\n        :type ImageOwner: int\n        :param ImageSize: 镜像大小。单位：GB\n        :type ImageSize: int\n        :param SrcImage: 镜像来源信息\n        :type SrcImage: :class:`tencentcloud.ecm.v20190719.models.SrcImage`\n        :param ImageSource: 镜像来源类型\n        :type ImageSource: str\n        :param TaskId: 中间态和失败时候的任务ID\n        :type TaskId: str\n        :param IsSupportCloudInit: 是否支持CloudInit\n        :type IsSupportCloudInit: bool\n        """
        self.ImageId = None
        self.ImageName = None
        self.ImageState = None
        self.ImageType = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.ImageCreateTime = None
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.Platform = None
        self.ImageOwner = None
        self.ImageSize = None
        self.SrcImage = None
        self.ImageSource = None
        self.TaskId = None
        self.IsSupportCloudInit = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageState = params.get("ImageState")
        self.ImageType = params.get("ImageType")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.ImageCreateTime = params.get("ImageCreateTime")
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.Platform = params.get("Platform")
        self.ImageOwner = params.get("ImageOwner")
        self.ImageSize = params.get("ImageSize")
        if params.get("SrcImage") is not None:
            self.SrcImage = SrcImage()
            self.SrcImage._deserialize(params.get("SrcImage"))
        self.ImageSource = params.get("ImageSource")
        self.TaskId = params.get("TaskId")
        self.IsSupportCloudInit = params.get("IsSupportCloudInit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageLimitConfig(AbstractModel):
    """镜像限制配置

    """

    def __init__(self):
        """
        :param MaxImageSize: 支持的最大镜像大小，包括可导入的自定义镜像大小，中心云镜像大小，单位为GB。\n        :type MaxImageSize: int\n        """
        self.MaxImageSize = None


    def _deserialize(self, params):
        self.MaxImageSize = params.get("MaxImageSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOsList(AbstractModel):
    """支持的操作系统类型，根据windows和Linux分类。

    """

    def __init__(self):
        """
        :param Windows: 支持的windows操作系统
注意：此字段可能返回 null，表示取不到有效值。\n        :type Windows: list of str\n        :param Linux: 支持的linux操作系统
注意：此字段可能返回 null，表示取不到有效值。\n        :type Linux: list of str\n        """
        self.Windows = None
        self.Linux = None


    def _deserialize(self, params):
        self.Windows = params.get("Windows")
        self.Linux = params.get("Linux")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageTask(AbstractModel):
    """镜像任务

    """

    def __init__(self):
        """
        :param State: 镜像导入状态， PENDING, PROCESSING, SUCCESS, FAILED\n        :type State: str\n        :param Message: 导入失败(FAILED)时， 说明失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        :param ImageName: 镜像名称\n        :type ImageName: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        """
        self.State = None
        self.Message = None
        self.ImageName = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.State = params.get("State")
        self.Message = params.get("Message")
        self.ImageName = params.get("ImageName")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageUrl(AbstractModel):
    """镜像文件信息

    """

    def __init__(self):
        """
        :param ImageFile: 镜像文件COS链接，如设置私有读写，需授权腾讯云ECM运营账号访问权限。\n        :type ImageFile: str\n        """
        self.ImageFile = None


    def _deserialize(self, params):
        self.ImageFile = params.get("ImageFile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportCustomImageRequest(AbstractModel):
    """ImportCustomImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageName: 镜像名称\n        :type ImageName: str\n        :param Architecture: 导入镜像的操作系统架构，x86_64 或 i386\n        :type Architecture: str\n        :param OsType: 导入镜像的操作系统类型，通过DescribeImportImageOs获取\n        :type OsType: str\n        :param OsVersion: 导入镜像的操作系统版本，通过DescribeImportImageOs获取\n        :type OsVersion: str\n        :param ImageDescription: 镜像描述\n        :type ImageDescription: str\n        :param InitFlag: 镜像启动方式，cloudinit或nbd， 默认cloudinit\n        :type InitFlag: str\n        :param ImageUrls: 镜像文件描述，多层镜像按顺序传入\n        :type ImageUrls: list of ImageUrl\n        """
        self.ImageName = None
        self.Architecture = None
        self.OsType = None
        self.OsVersion = None
        self.ImageDescription = None
        self.InitFlag = None
        self.ImageUrls = None


    def _deserialize(self, params):
        self.ImageName = params.get("ImageName")
        self.Architecture = params.get("Architecture")
        self.OsType = params.get("OsType")
        self.OsVersion = params.get("OsVersion")
        self.ImageDescription = params.get("ImageDescription")
        self.InitFlag = params.get("InitFlag")
        if params.get("ImageUrls") is not None:
            self.ImageUrls = []
            for item in params.get("ImageUrls"):
                obj = ImageUrl()
                obj._deserialize(item)
                self.ImageUrls.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportCustomImageResponse(AbstractModel):
    """ImportCustomImage返回参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID\n        :type ImageId: str\n        :param TaskId: 异步任务ID，可根据DescribeCustomImageTask查询任务信息\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ImageId = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ImportImageRequest(AbstractModel):
    """ImportImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 镜像的Id。\n        :type ImageId: str\n        :param ImageDescription: 镜像的描述。\n        :type ImageDescription: str\n        :param SourceRegion: 源地域\n        :type SourceRegion: str\n        """
        self.ImageId = None
        self.ImageDescription = None
        self.SourceRegion = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageDescription = params.get("ImageDescription")
        self.SourceRegion = params.get("SourceRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImportImageResponse(AbstractModel):
    """ImportImage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Instance(AbstractModel):
    """用于描述实例相关的信息。

    """

    def __init__(self):
        """
        :param InstanceId: 实例ID。\n        :type InstanceId: str\n        :param InstanceName: 实例名称，如ens-34241f3s。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceName: str\n        :param InstanceState: 实例状态。取值范围：
PENDING：表示创建中
LAUNCH_FAILED：表示创建失败
RUNNING：表示运行中
STOPPED：表示关机
STARTING：表示开机中
STOPPING：表示关机中
REBOOTING：表示重启中
SHUTDOWN：表示停止待销毁
TERMINATING：表示销毁中。\n        :type InstanceState: str\n        :param Image: 实例当前使用的镜像的信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Image: :class:`tencentcloud.ecm.v20190719.models.Image`\n        :param SimpleModule: 实例当前所属的模块简要信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SimpleModule: :class:`tencentcloud.ecm.v20190719.models.SimpleModule`\n        :param Position: 实例所在的位置相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`\n        :param Internet: 实例的网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Internet: :class:`tencentcloud.ecm.v20190719.models.Internet`\n        :param InstanceTypeConfig: 实例的配置相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`\n        :param CreateTime: 实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param TagSet: 实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        :param LatestOperation: 实例最后一次操作。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LatestOperation: str\n        :param LatestOperationState: 实例最后一次操作结果。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LatestOperationState: str\n        :param RestrictState: 实例业务状态。取值范围：
NORMAL：表示正常状态的实例
EXPIRED：表示过期的实例
PROTECTIVELY_ISOLATED：表示被安全隔离的实例。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RestrictState: str\n        :param SystemDiskSize: 系统盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SystemDiskSize: int\n        :param DataDiskSize: 数据盘大小，单位GB。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataDiskSize: int\n        :param UUID: 实例UUID
注意：此字段可能返回 null，表示取不到有效值。\n        :type UUID: str\n        :param PayMode: 付费方式。
    0为后付费。
    1为预付费。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PayMode: int\n        :param ExpireTime: 过期时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param IsolatedTime: 隔离时间。格式为yyyy-mm-dd HH:mm:ss。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsolatedTime: str\n        :param RenewFlag: 是否自动续费。
      0为不自动续费。
      1为自动续费。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewFlag: int\n        :param ExpireState: 过期状态。
    NORMAL 表示机器运行正常。
    WILL_EXPIRE 表示即将过期。
    EXPIRED 表示已过期。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireState: str\n        :param SystemDisk: 系统盘信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type SystemDisk: :class:`tencentcloud.ecm.v20190719.models.DiskInfo`\n        :param DataDisks: 数据盘信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type DataDisks: list of DiskInfo\n        :param NewFlag: 新实例标志
注意：此字段可能返回 null，表示取不到有效值。\n        :type NewFlag: int\n        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroupIds: list of str\n        :param VirtualPrivateCloud: VPC属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type VirtualPrivateCloud: :class:`tencentcloud.ecm.v20190719.models.VirtualPrivateCloud`\n        :param ISP: 实例运营商字段。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ISP: str\n        :param PhysicalPosition: 物理位置信息。注意该字段目前为保留字段，均为空值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhysicalPosition: :class:`tencentcloud.ecm.v20190719.models.PhysicalPosition`\n        """
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.Image = None
        self.SimpleModule = None
        self.Position = None
        self.Internet = None
        self.InstanceTypeConfig = None
        self.CreateTime = None
        self.TagSet = None
        self.LatestOperation = None
        self.LatestOperationState = None
        self.RestrictState = None
        self.SystemDiskSize = None
        self.DataDiskSize = None
        self.UUID = None
        self.PayMode = None
        self.ExpireTime = None
        self.IsolatedTime = None
        self.RenewFlag = None
        self.ExpireState = None
        self.SystemDisk = None
        self.DataDisks = None
        self.NewFlag = None
        self.SecurityGroupIds = None
        self.VirtualPrivateCloud = None
        self.ISP = None
        self.PhysicalPosition = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        if params.get("Image") is not None:
            self.Image = Image()
            self.Image._deserialize(params.get("Image"))
        if params.get("SimpleModule") is not None:
            self.SimpleModule = SimpleModule()
            self.SimpleModule._deserialize(params.get("SimpleModule"))
        if params.get("Position") is not None:
            self.Position = Position()
            self.Position._deserialize(params.get("Position"))
        if params.get("Internet") is not None:
            self.Internet = Internet()
            self.Internet._deserialize(params.get("Internet"))
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        self.CreateTime = params.get("CreateTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.LatestOperation = params.get("LatestOperation")
        self.LatestOperationState = params.get("LatestOperationState")
        self.RestrictState = params.get("RestrictState")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.DataDiskSize = params.get("DataDiskSize")
        self.UUID = params.get("UUID")
        self.PayMode = params.get("PayMode")
        self.ExpireTime = params.get("ExpireTime")
        self.IsolatedTime = params.get("IsolatedTime")
        self.RenewFlag = params.get("RenewFlag")
        self.ExpireState = params.get("ExpireState")
        if params.get("SystemDisk") is not None:
            self.SystemDisk = DiskInfo()
            self.SystemDisk._deserialize(params.get("SystemDisk"))
        if params.get("DataDisks") is not None:
            self.DataDisks = []
            for item in params.get("DataDisks"):
                obj = DiskInfo()
                obj._deserialize(item)
                self.DataDisks.append(obj)
        self.NewFlag = params.get("NewFlag")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("VirtualPrivateCloud") is not None:
            self.VirtualPrivateCloud = VirtualPrivateCloud()
            self.VirtualPrivateCloud._deserialize(params.get("VirtualPrivateCloud"))
        self.ISP = params.get("ISP")
        if params.get("PhysicalPosition") is not None:
            self.PhysicalPosition = PhysicalPosition()
            self.PhysicalPosition._deserialize(params.get("PhysicalPosition"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyConfig(AbstractModel):
    """机型族配置

    """

    def __init__(self):
        """
        :param InstanceFamilyName: 机型名称\n        :type InstanceFamilyName: str\n        :param InstanceFamily: 机型ID\n        :type InstanceFamily: str\n        """
        self.InstanceFamilyName = None
        self.InstanceFamily = None


    def _deserialize(self, params):
        self.InstanceFamilyName = params.get("InstanceFamilyName")
        self.InstanceFamily = params.get("InstanceFamily")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceFamilyTypeConfig(AbstractModel):
    """实例系列类型配置

    """

    def __init__(self):
        """
        :param InstanceFamilyType: 实例机型系列类型Id\n        :type InstanceFamilyType: str\n        :param InstanceFamilyTypeName: 实例机型系列类型名称\n        :type InstanceFamilyTypeName: str\n        """
        self.InstanceFamilyType = None
        self.InstanceFamilyTypeName = None


    def _deserialize(self, params):
        self.InstanceFamilyType = params.get("InstanceFamilyType")
        self.InstanceFamilyTypeName = params.get("InstanceFamilyTypeName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkInfo(AbstractModel):
    """实例网卡ip网络信息数组

    """

    def __init__(self):
        """
        :param AddressInfoSet: 实例内外网ip相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddressInfoSet: list of AddressInfo\n        :param NetworkInterfaceId: 网卡ID。\n        :type NetworkInterfaceId: str\n        :param NetworkInterfaceName: 网卡名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetworkInterfaceName: str\n        :param Primary: 主网卡属性。true为主网卡，false为辅助网卡。\n        :type Primary: bool\n        """
        self.AddressInfoSet = None
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.Primary = None


    def _deserialize(self, params):
        if params.get("AddressInfoSet") is not None:
            self.AddressInfoSet = []
            for item in params.get("AddressInfoSet"):
                obj = AddressInfo()
                obj._deserialize(item)
                self.AddressInfoSet.append(obj)
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.Primary = params.get("Primary")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceNetworkLimitConfig(AbstractModel):
    """机器网络资源限制

    """

    def __init__(self):
        """
        :param CpuNum: cpu核数\n        :type CpuNum: int\n        :param NetworkInterfaceLimit: 网卡数量限制\n        :type NetworkInterfaceLimit: int\n        :param InnerIpPerNetworkInterface: 每张网卡内网ip数量限制\n        :type InnerIpPerNetworkInterface: int\n        :param PublicIpPerInstance: 每个实例的外网ip限制\n        :type PublicIpPerInstance: int\n        """
        self.CpuNum = None
        self.NetworkInterfaceLimit = None
        self.InnerIpPerNetworkInterface = None
        self.PublicIpPerInstance = None


    def _deserialize(self, params):
        self.CpuNum = params.get("CpuNum")
        self.NetworkInterfaceLimit = params.get("NetworkInterfaceLimit")
        self.InnerIpPerNetworkInterface = params.get("InnerIpPerNetworkInterface")
        self.PublicIpPerInstance = params.get("PublicIpPerInstance")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceOperator(AbstractModel):
    """实例可执行操作

    """

    def __init__(self):
        """
        :param InstanceId: 实例id\n        :type InstanceId: str\n        :param DeniedActions: 实例禁止的操作
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeniedActions: list of OperatorAction\n        """
        self.InstanceId = None
        self.DeniedActions = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DeniedActions") is not None:
            self.DeniedActions = []
            for item in params.get("DeniedActions"):
                obj = OperatorAction()
                obj._deserialize(item)
                self.DeniedActions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceStatistic(AbstractModel):
    """用于描述实例的统计信息

    """

    def __init__(self):
        """
        :param InstanceType: 实例的类型\n        :type InstanceType: str\n        :param InstanceCount: 实例的个数\n        :type InstanceCount: int\n        """
        self.InstanceType = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceTypeConfig(AbstractModel):
    """机型配置

    """

    def __init__(self):
        """
        :param InstanceFamilyConfig: 机型族配置信息\n        :type InstanceFamilyConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyConfig`\n        :param InstanceType: 机型\n        :type InstanceType: str\n        :param Vcpu: CPU核数\n        :type Vcpu: int\n        :param Memory: 内存大小\n        :type Memory: int\n        :param Frequency: 主频\n        :type Frequency: str\n        :param CpuModelName: 处理器型号\n        :type CpuModelName: str\n        :param InstanceFamilyTypeConfig: 机型族类别配置信息\n        :type InstanceFamilyTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`\n        :param ExtInfo: 机型额外信息 是一个json字符串，如果存在则表示特殊机型，格式如下：{"dataDiskSize":3200,"systemDiskSize":60, "systemDiskSizeShow":"系统盘默认60G","dataDiskSizeShow":"本地NVMe SSD 硬盘3200 GB"}
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtInfo: str\n        :param Vgpu: GPU卡数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Vgpu: float\n        :param GpuModelName: GPU型号
注意：此字段可能返回 null，表示取不到有效值。\n        :type GpuModelName: str\n        """
        self.InstanceFamilyConfig = None
        self.InstanceType = None
        self.Vcpu = None
        self.Memory = None
        self.Frequency = None
        self.CpuModelName = None
        self.InstanceFamilyTypeConfig = None
        self.ExtInfo = None
        self.Vgpu = None
        self.GpuModelName = None


    def _deserialize(self, params):
        if params.get("InstanceFamilyConfig") is not None:
            self.InstanceFamilyConfig = InstanceFamilyConfig()
            self.InstanceFamilyConfig._deserialize(params.get("InstanceFamilyConfig"))
        self.InstanceType = params.get("InstanceType")
        self.Vcpu = params.get("Vcpu")
        self.Memory = params.get("Memory")
        self.Frequency = params.get("Frequency")
        self.CpuModelName = params.get("CpuModelName")
        if params.get("InstanceFamilyTypeConfig") is not None:
            self.InstanceFamilyTypeConfig = InstanceFamilyTypeConfig()
            self.InstanceFamilyTypeConfig._deserialize(params.get("InstanceFamilyTypeConfig"))
        self.ExtInfo = params.get("ExtInfo")
        self.Vgpu = params.get("Vgpu")
        self.GpuModelName = params.get("GpuModelName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Internet(AbstractModel):
    """实例的网络相关信息。

    """

    def __init__(self):
        """
        :param PrivateIPAddressSet: 实例的内网相关信息列表。顺序为主网卡在前，辅助网卡按绑定先后顺序排列。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIPAddressSet: list of PrivateIPAddressInfo\n        :param PublicIPAddressSet: 实例的公网相关信息列表。顺序为主网卡在前，辅助网卡按绑定先后顺序排列。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublicIPAddressSet: list of PublicIPAddressInfo\n        :param InstanceNetworkInfoSet: 实例网络相关信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceNetworkInfoSet: list of InstanceNetworkInfo\n        """
        self.PrivateIPAddressSet = None
        self.PublicIPAddressSet = None
        self.InstanceNetworkInfoSet = None


    def _deserialize(self, params):
        if params.get("PrivateIPAddressSet") is not None:
            self.PrivateIPAddressSet = []
            for item in params.get("PrivateIPAddressSet"):
                obj = PrivateIPAddressInfo()
                obj._deserialize(item)
                self.PrivateIPAddressSet.append(obj)
        if params.get("PublicIPAddressSet") is not None:
            self.PublicIPAddressSet = []
            for item in params.get("PublicIPAddressSet"):
                obj = PublicIPAddressInfo()
                obj._deserialize(item)
                self.PublicIPAddressSet.append(obj)
        if params.get("InstanceNetworkInfoSet") is not None:
            self.InstanceNetworkInfoSet = []
            for item in params.get("InstanceNetworkInfoSet"):
                obj = InstanceNetworkInfo()
                obj._deserialize(item)
                self.InstanceNetworkInfoSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Address(AbstractModel):
    """IPv6地址信息。

    """

    def __init__(self):
        """
        :param Address: IPv6地址，形如：3402:4e00:20:100:0:8cd9:2a67:71f3\n        :type Address: str\n        :param Primary: 是否是主IP。\n        :type Primary: bool\n        :param AddressId: EIP实例ID，形如：eip-hxlqja90。\n        :type AddressId: str\n        :param Description: 描述信息。\n        :type Description: str\n        :param IsWanIpBlocked: 公网IP是否被封堵。\n        :type IsWanIpBlocked: bool\n        :param State: IPv6地址状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的\n        :type State: str\n        """
        self.Address = None
        self.Primary = None
        self.AddressId = None
        self.Description = None
        self.IsWanIpBlocked = None
        self.State = None


    def _deserialize(self, params):
        self.Address = params.get("Address")
        self.Primary = params.get("Primary")
        self.AddressId = params.get("AddressId")
        self.Description = params.get("Description")
        self.IsWanIpBlocked = params.get("IsWanIpBlocked")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Listener(AbstractModel):
    """负载均衡监听器

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerId: str\n        :param Protocol: 监听器协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param Port: 监听器端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param HealthCheck: 监听器的健康检查信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`\n        :param Scheduler: 请求的调度方式
注意：此字段可能返回 null，表示取不到有效值。\n        :type Scheduler: str\n        :param SessionExpireTime: 会话保持时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionExpireTime: int\n        :param ListenerName: 监听器的名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerName: str\n        :param CreateTime: 监听器的创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param SessionType: 监听器的会话类型
注意：此字段可能返回 null，表示取不到有效值。\n        :type SessionType: str\n        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.HealthCheck = None
        self.Scheduler = None
        self.SessionExpireTime = None
        self.ListenerName = None
        self.CreateTime = None
        self.SessionType = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        self.SessionExpireTime = params.get("SessionExpireTime")
        self.ListenerName = params.get("ListenerName")
        self.CreateTime = params.get("CreateTime")
        self.SessionType = params.get("SessionType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerBackend(AbstractModel):
    """监听器后端

    """

    def __init__(self):
        """
        :param ListenerId: 监听器 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerId: str\n        :param Protocol: 监听器的协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param Port: 监听器的端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param Targets: 监听器上绑定的后端服务列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Targets: list of Backend\n        """
        self.ListenerId = None
        self.Protocol = None
        self.Port = None
        self.Targets = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Backend()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerHealth(AbstractModel):
    """监听器健康状态

    """

    def __init__(self):
        """
        :param ListenerId: 监听器ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerId: str\n        :param ListenerName: 监听器名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerName: str\n        :param Protocol: 监听器的协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Protocol: str\n        :param Port: 监听器的端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param Rules: 监听器的转发规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rules: list of RuleHealth\n        """
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.Port = None
        self.Rules = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = RuleHealth()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancer(AbstractModel):
    """负载均衡实例信息

    """

    def __init__(self):
        """
        :param Region: 区域。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Position: 位置信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Position: :class:`tencentcloud.ecm.v20190719.models.Position`\n        :param LoadBalancerId: 负载均衡实例 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerId: str\n        :param LoadBalancerName: 负载均衡实例的名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerName: str\n        :param LoadBalancerType: 负载均衡实例的网络类型：OPEN：公网属性
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerType: str\n        :param LoadBalancerVips: 负载均衡实例的 VIP 列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerVips: list of str\n        :param Status: 负载均衡实例的状态，包括
 0：创建中，1：正常运行。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param CreateTime: 负载均衡实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param StatusTime: 负载均衡实例的上次状态转换时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusTime: str\n        :param VpcId: 私有网络的 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param Tags: 负载均衡实例的标签信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of TagInfo\n        :param VipIsp: 负载均衡IP地址所属的ISP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VipIsp: str\n        :param NetworkAttributes: 负载均衡实例的网络属性。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetworkAttributes: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`\n        :param SecureGroups: 安全组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecureGroups: list of str\n        :param LoadBalancerPassToTarget: 后端机器是否放通来自ELB的流量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerPassToTarget: bool\n        """
        self.Region = None
        self.Position = None
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.LoadBalancerType = None
        self.LoadBalancerVips = None
        self.Status = None
        self.CreateTime = None
        self.StatusTime = None
        self.VpcId = None
        self.Tags = None
        self.VipIsp = None
        self.NetworkAttributes = None
        self.SecureGroups = None
        self.LoadBalancerPassToTarget = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("Position") is not None:
            self.Position = Position()
            self.Position._deserialize(params.get("Position"))
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        self.LoadBalancerType = params.get("LoadBalancerType")
        self.LoadBalancerVips = params.get("LoadBalancerVips")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.StatusTime = params.get("StatusTime")
        self.VpcId = params.get("VpcId")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.VipIsp = params.get("VipIsp")
        if params.get("NetworkAttributes") is not None:
            self.NetworkAttributes = LoadBalancerInternetAccessible()
            self.NetworkAttributes._deserialize(params.get("NetworkAttributes"))
        self.SecureGroups = params.get("SecureGroups")
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerHealth(AbstractModel):
    """负载均衡器健康状态

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerId: str\n        :param LoadBalancerName: 负载均衡实例名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type LoadBalancerName: str\n        :param Listeners: 监听器列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Listeners: list of ListenerHealth\n        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ListenerHealth()
                obj._deserialize(item)
                self.Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LoadBalancerInternetAccessible(AbstractModel):
    """负载均衡的带宽限制等信息。

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: 最大出带宽，单位Mbps。默认值10\n        :type InternetMaxBandwidthOut: int\n        """
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param SourceInstanceId: 弹性网卡当前绑定的ECM实例ID。形如：ein-r8hr2upy。\n        :type SourceInstanceId: str\n        :param DestinationInstanceId: 待迁移的目的ECM实例ID。\n        :type DestinationInstanceId: str\n        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        :param SourceNetworkInterfaceId: 当前内网IP绑定的弹性网卡实例ID，例如：eni-11112222。\n        :type SourceNetworkInterfaceId: str\n        :param DestinationNetworkInterfaceId: 待迁移的目的弹性网卡实例ID。\n        :type DestinationNetworkInterfaceId: str\n        :param PrivateIpAddress: 迁移的内网IP地址，例如：10.0.0.6。\n        :type PrivateIpAddress: str\n        """
        self.EcmRegion = None
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self.DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：eip-11112222。\n        :type AddressId: str\n        :param AddressName: 修改后的 EIP 名称。长度上限为20个字符。\n        :type AddressName: str\n        :param EipDirectConnection: 设定EIP是否直通，"TRUE"表示直通，"FALSE"表示非直通。注意该参数仅对EIP直通功能可见的用户可以设定。\n        :type EipDirectConnection: str\n        """
        self.EcmRegion = None
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")
        self.EipDirectConnection = params.get("EipDirectConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressIds: EIP唯一标识ID，形如'eip-xxxxxxx'\n        :type AddressIds: list of str\n        :param InternetMaxBandwidthOut: 调整带宽目标值\n        :type InternetMaxBandwidthOut: int\n        """
        self.EcmRegion = None
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务TaskId。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyDefaultSubnetRequest(AbstractModel):
    """ModifyDefaultSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM地域\n        :type EcmRegion: str\n        :param Zone: ECM可用区\n        :type Zone: str\n        :param VpcId: 私有网络ID\n        :type VpcId: str\n        :param SubnetId: 子网ID\n        :type SubnetId: str\n        """
        self.EcmRegion = None
        self.Zone = None
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.Zone = params.get("Zone")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDefaultSubnetResponse(AbstractModel):
    """ModifyDefaultSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: HAVIP唯一ID，形如：havip-9o233uri。\n        :type HaVipId: str\n        :param HaVipName: HAVIP名称，可任意命名，但不得超过60个字符。\n        :type HaVipName: str\n        """
        self.HaVipId = None
        self.HaVipName = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyImageAttributeRequest(AbstractModel):
    """ModifyImageAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ImageId: 镜像ID，形如img-gvbnzy6f\n        :type ImageId: str\n        :param ImageName: 设置新的镜像名称；必须满足下列限制：
不得超过20个字符。
- 镜像名称不能与已有镜像重复。\n        :type ImageName: str\n        :param ImageDescription: 设置新的镜像描述；必须满足下列限制：
- 不得超过60个字符。\n        :type ImageDescription: str\n        """
        self.ImageId = None
        self.ImageName = None
        self.ImageDescription = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageDescription = params.get("ImageDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyImageAttributeResponse(AbstractModel):
    """ModifyImageAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyInstancesAttributeRequest(AbstractModel):
    """ModifyInstancesAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待修改的实例ID列表。在单次请求的过程中，请求实例数上限为100。\n        :type InstanceIdSet: list of str\n        :param InstanceName: 修改成功后显示的实例名称，不得超过60个字符，不传则名称显示为空。\n        :type InstanceName: str\n        :param SecurityGroups: 指定实例的安全组Id列表，子机将重新关联指定列表的安全组，原本关联的安全组会被解绑。限制不超过5个。\n        :type SecurityGroups: list of str\n        """
        self.InstanceIdSet = None
        self.InstanceName = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.InstanceName = params.get("InstanceName")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyInstancesAttributeResponse(AbstractModel):
    """ModifyInstancesAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIpv6AddressesAttributeRequest(AbstractModel):
    """ModifyIpv6AddressesAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param NetworkInterfaceId: 弹性网卡实例ID，形如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: 指定的IPv6地址信息。\n        :type Ipv6Addresses: list of Ipv6Address\n        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIpv6AddressesAttributeResponse(AbstractModel):
    """ModifyIpv6AddressesAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyListenerRequest(AbstractModel):
    """ModifyListener请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡监听器 ID\n        :type ListenerId: str\n        :param ListenerName: 新的监听器名称\n        :type ListenerName: str\n        :param SessionExpireTime: 会话保持时间，单位：秒。可选值：30~3600，默认 0，表示不开启。此参数仅适用于TCP/UDP监听器。\n        :type SessionExpireTime: int\n        :param HealthCheck: 健康检查相关参数\n        :type HealthCheck: :class:`tencentcloud.ecm.v20190719.models.HealthCheck`\n        :param Scheduler: 监听器转发的方式。可选值：WRR、LEAST_CONN
分别表示按权重轮询、最小连接数， 默认为 WRR。\n        :type Scheduler: str\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.ListenerName = None
        self.SessionExpireTime = None
        self.HealthCheck = None
        self.Scheduler = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SessionExpireTime = params.get("SessionExpireTime")
        if params.get("HealthCheck") is not None:
            self.HealthCheck = HealthCheck()
            self.HealthCheck._deserialize(params.get("HealthCheck"))
        self.Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyListenerResponse(AbstractModel):
    """ModifyListener返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyLoadBalancerAttributesRequest(AbstractModel):
    """ModifyLoadBalancerAttributes请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡的唯一ID\n        :type LoadBalancerId: str\n        :param LoadBalancerName: 负载均衡实例名称\n        :type LoadBalancerName: str\n        :param InternetChargeInfo: 网络计费及带宽相关参数\n        :type InternetChargeInfo: :class:`tencentcloud.ecm.v20190719.models.LoadBalancerInternetAccessible`\n        :param LoadBalancerPassToTarget: Target是否放通来自ELB的流量。开启放通（true）：只验证ELB上的安全组；不开启放通（false）：需同时验证ELB和后端实例上的安全组。\n        :type LoadBalancerPassToTarget: bool\n        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.InternetChargeInfo = None
        self.LoadBalancerPassToTarget = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("InternetChargeInfo") is not None:
            self.InternetChargeInfo = LoadBalancerInternetAccessible()
            self.InternetChargeInfo._deserialize(params.get("InternetChargeInfo"))
        self.LoadBalancerPassToTarget = params.get("LoadBalancerPassToTarget")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLoadBalancerAttributesResponse(AbstractModel):
    """ModifyLoadBalancerAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleConfigRequest(AbstractModel):
    """ModifyModuleConfig请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID。\n        :type ModuleId: str\n        :param InstanceType: 机型ID。\n        :type InstanceType: str\n        :param DefaultDataDiskSize: 默认数据盘大小，单位：G。范围不得超过数据盘范围大小，详看DescribeConfig。\n        :type DefaultDataDiskSize: int\n        """
        self.ModuleId = None
        self.InstanceType = None
        self.DefaultDataDiskSize = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.InstanceType = params.get("InstanceType")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleConfigResponse(AbstractModel):
    """ModifyModuleConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleDisableWanIpRequest(AbstractModel):
    """ModifyModuleDisableWanIp请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID\n        :type ModuleId: str\n        :param DisableWanIp: 是否禁止分配外网ip,true：统一分配外网ip，false：禁止分配外网ip.\n        :type DisableWanIp: bool\n        """
        self.ModuleId = None
        self.DisableWanIp = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.DisableWanIp = params.get("DisableWanIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleDisableWanIpResponse(AbstractModel):
    """ModifyModuleDisableWanIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleImageRequest(AbstractModel):
    """ModifyModuleImage请求参数结构体

    """

    def __init__(self):
        """
        :param DefaultImageId: 默认镜像ID\n        :type DefaultImageId: str\n        :param ModuleId: 模块ID\n        :type ModuleId: str\n        """
        self.DefaultImageId = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.DefaultImageId = params.get("DefaultImageId")
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleImageResponse(AbstractModel):
    """ModifyModuleImage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleIpDirectRequest(AbstractModel):
    """ModifyModuleIpDirect请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID。\n        :type ModuleId: str\n        :param CloseIpDirect: 是否关闭IP直通。取值范围：
true：表示关闭IP直通
false：表示开通IP直通\n        :type CloseIpDirect: bool\n        """
        self.ModuleId = None
        self.CloseIpDirect = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.CloseIpDirect = params.get("CloseIpDirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleIpDirectResponse(AbstractModel):
    """ModifyModuleIpDirect返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNameRequest(AbstractModel):
    """ModifyModuleName请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID。\n        :type ModuleId: str\n        :param ModuleName: 模块名称。\n        :type ModuleName: str\n        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNameResponse(AbstractModel):
    """ModifyModuleName返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleNetworkRequest(AbstractModel):
    """ModifyModuleNetwork请求参数结构体

    """

    def __init__(self):
        """
        :param ModuleId: 模块Id\n        :type ModuleId: str\n        :param DefaultBandwidth: 默认出带宽上限\n        :type DefaultBandwidth: int\n        :param DefaultBandwidthIn: 默认入带宽上限\n        :type DefaultBandwidthIn: int\n        """
        self.ModuleId = None
        self.DefaultBandwidth = None
        self.DefaultBandwidthIn = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.DefaultBandwidth = params.get("DefaultBandwidth")
        self.DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleNetworkResponse(AbstractModel):
    """ModifyModuleNetwork返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyModuleSecurityGroupsRequest(AbstractModel):
    """ModifyModuleSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIdSet: 安全组列表。不超过5个。\n        :type SecurityGroupIdSet: list of str\n        :param ModuleId: 模块id。\n        :type ModuleId: str\n        """
        self.SecurityGroupIdSet = None
        self.ModuleId = None


    def _deserialize(self, params):
        self.SecurityGroupIdSet = params.get("SecurityGroupIdSet")
        self.ModuleId = params.get("ModuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyModuleSecurityGroupsResponse(AbstractModel):
    """ModifyModuleSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: 指定的内网IP信息。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param EcmRegion: ECM 节点Region信息，形如ap-xian-ecm。\n        :type EcmRegion: str\n        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c\n        :type RouteTableId: str\n        :param RouteTableName: 路由表名称\n        :type RouteTableName: str\n        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type GroupName: str\n        :param GroupDescription: 安全组备注，最多100个字符。\n        :type GroupDescription: str\n        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。 SecurityGroupPolicySet对象必须同时指定新的出（Egress）入（Ingress）站规则。 SecurityGroupPolicy对象不支持自定义索引（PolicyIndex）。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`\n        :param SortPolicys: 排序安全组标识。值为True时，支持安全组排序；SortPolicys不存在或SortPolicys为False时，为修改安全组规则。\n        :type SortPolicys: bool\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None
        self.SortPolicys = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.SortPolicys = params.get("SortPolicys")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySubnetAttributeRequest(AbstractModel):
    """ModifySubnetAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID。形如：subnet-pxir56ns。\n        :type SubnetId: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param SubnetName: 子网名称，最大长度不能超过60个字节。\n        :type SubnetName: str\n        :param EnableBroadcast: 子网是否开启广播。\n        :type EnableBroadcast: str\n        :param Tags: 子网的标签键值\n        :type Tags: list of Tag\n        """
        self.SubnetId = None
        self.EcmRegion = None
        self.SubnetName = None
        self.EnableBroadcast = None
        self.Tags = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.EcmRegion = params.get("EcmRegion")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySubnetAttributeResponse(AbstractModel):
    """ModifySubnetAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetPortRequest(AbstractModel):
    """ModifyTargetPort请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡监听器 ID\n        :type ListenerId: str\n        :param Targets: 要修改端口的后端服务列表\n        :type Targets: list of Target\n        :param NewPort: 后端服务绑定到监听器或转发规则的新端口\n        :type NewPort: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.NewPort = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.NewPort = params.get("NewPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetPortResponse(AbstractModel):
    """ModifyTargetPort返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTargetWeightRequest(AbstractModel):
    """ModifyTargetWeight请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param ListenerId: 负载均衡监听器 ID\n        :type ListenerId: str\n        :param Targets: 要修改权重的后端服务列表\n        :type Targets: list of Target\n        :param Weight: 后端服务新的转发权重，取值范围：0~100，默认值10。如果设置了 Targets.Weight 参数，则此参数不生效。\n        :type Weight: int\n        """
        self.LoadBalancerId = None
        self.ListenerId = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTargetWeightResponse(AbstractModel):
    """ModifyTargetWeight返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。形如：vpc-f49l6u0z。\n        :type VpcId: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param VpcName: 私有网络名称，可任意命名，但不得超过60个字符。\n        :type VpcName: str\n        :param Tags: 标签\n        :type Tags: list of Tag\n        :param Description: 私有网络描述\n        :type Description: str\n        """
        self.VpcId = None
        self.EcmRegion = None
        self.VpcName = None
        self.Tags = None
        self.Description = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EcmRegion = params.get("EcmRegion")
        self.VpcName = params.get("VpcName")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAttributeResponse(AbstractModel):
    """ModifyVpcAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Module(AbstractModel):
    """模块信息

    """

    def __init__(self):
        """
        :param ModuleId: 模块Id。\n        :type ModuleId: str\n        :param ModuleName: 模块名称。\n        :type ModuleName: str\n        :param ModuleState: 模块状态：
NORMAL：正常。
DELETING：删除中 
DELETEFAILED：删除失败。\n        :type ModuleState: str\n        :param DefaultSystemDiskSize: 默认系统盘大小。\n        :type DefaultSystemDiskSize: int\n        :param DefaultDataDiskSize: 默认数据盘大小。\n        :type DefaultDataDiskSize: int\n        :param InstanceTypeConfig: 默认机型。\n        :type InstanceTypeConfig: :class:`tencentcloud.ecm.v20190719.models.InstanceTypeConfig`\n        :param DefaultImage: 默认镜像。\n        :type DefaultImage: :class:`tencentcloud.ecm.v20190719.models.Image`\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        :param DefaultBandwidth: 默认出带宽。\n        :type DefaultBandwidth: int\n        :param TagSet: 标签集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        :param CloseIpDirect: 是否关闭IP直通。\n        :type CloseIpDirect: int\n        :param SecurityGroupIds: 默认安全组id列表。\n        :type SecurityGroupIds: list of str\n        :param DefaultBandwidthIn: 默认入带宽。\n        :type DefaultBandwidthIn: int\n        :param UserData: 自定义脚本数据\n        :type UserData: str\n        """
        self.ModuleId = None
        self.ModuleName = None
        self.ModuleState = None
        self.DefaultSystemDiskSize = None
        self.DefaultDataDiskSize = None
        self.InstanceTypeConfig = None
        self.DefaultImage = None
        self.CreateTime = None
        self.DefaultBandwidth = None
        self.TagSet = None
        self.CloseIpDirect = None
        self.SecurityGroupIds = None
        self.DefaultBandwidthIn = None
        self.UserData = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        self.ModuleState = params.get("ModuleState")
        self.DefaultSystemDiskSize = params.get("DefaultSystemDiskSize")
        self.DefaultDataDiskSize = params.get("DefaultDataDiskSize")
        if params.get("InstanceTypeConfig") is not None:
            self.InstanceTypeConfig = InstanceTypeConfig()
            self.InstanceTypeConfig._deserialize(params.get("InstanceTypeConfig"))
        if params.get("DefaultImage") is not None:
            self.DefaultImage = Image()
            self.DefaultImage._deserialize(params.get("DefaultImage"))
        self.CreateTime = params.get("CreateTime")
        self.DefaultBandwidth = params.get("DefaultBandwidth")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.CloseIpDirect = params.get("CloseIpDirect")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.DefaultBandwidthIn = params.get("DefaultBandwidthIn")
        self.UserData = params.get("UserData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleCounter(AbstractModel):
    """节点统计数据

    """

    def __init__(self):
        """
        :param ISPCounterSet: 运营商统计信息列表\n        :type ISPCounterSet: list of ISPCounter\n        :param ProvinceNum: 省份数量\n        :type ProvinceNum: int\n        :param CityNum: 城市数量\n        :type CityNum: int\n        :param NodeNum: 节点数量\n        :type NodeNum: int\n        :param InstanceNum: 实例数量\n        :type InstanceNum: int\n        """
        self.ISPCounterSet = None
        self.ProvinceNum = None
        self.CityNum = None
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        if params.get("ISPCounterSet") is not None:
            self.ISPCounterSet = []
            for item in params.get("ISPCounterSet"):
                obj = ISPCounter()
                obj._deserialize(item)
                self.ISPCounterSet.append(obj)
        self.ProvinceNum = params.get("ProvinceNum")
        self.CityNum = params.get("CityNum")
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModuleItem(AbstractModel):
    """模块列表Item信息

    """

    def __init__(self):
        """
        :param NodeInstanceNum: 节点实例统计信息\n        :type NodeInstanceNum: :class:`tencentcloud.ecm.v20190719.models.NodeInstanceNum`\n        :param Module: 模块信息\n        :type Module: :class:`tencentcloud.ecm.v20190719.models.Module`\n        """
        self.NodeInstanceNum = None
        self.Module = None


    def _deserialize(self, params):
        if params.get("NodeInstanceNum") is not None:
            self.NodeInstanceNum = NodeInstanceNum()
            self.NodeInstanceNum._deserialize(params.get("NodeInstanceNum"))
        if params.get("Module") is not None:
            self.Module = Module()
            self.Module._deserialize(params.get("Module"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonthNetwork(AbstractModel):
    """客户对应月份的带宽信息

    """

    def __init__(self):
        """
        :param ZoneInfo: 节点zone信息\n        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`\n        :param Month: 带宽月份 示例"202103"\n        :type Month: str\n        :param BandwidthPkgId: 带宽包id 格式如"bwp-xxxxxxxx"\n        :type BandwidthPkgId: str\n        :param Isp: 运营商简称 取值范围"CUCC;CTCC;CMCC"\n        :type Isp: str\n        :param TrafficMaxIn: 入网带宽包峰值,取值范围0.0-xxx.xxx\n        :type TrafficMaxIn: float\n        :param TrafficMaxOut: 出网带宽包峰值,取值范围0.0-xxx.xxx\n        :type TrafficMaxOut: float\n        :param FeeTraffic: 计费带宽,取值范围0.0-xxx.xxx\n        :type FeeTraffic: float\n        :param StartTime: 月计费带宽起始时间 格式"yyyy-mm-dd HH:mm:ss"\n        :type StartTime: str\n        :param EndTime: 月计费带宽结束时间 格式"yyyy-mm-dd HH:mm:ss"\n        :type EndTime: str\n        :param EffectiveDays: 月计费带宽实际有效天数 整形必须大于等于0\n        :type EffectiveDays: int\n        :param MonthDays: 指定月份的实际天数 实例 30\n        :type MonthDays: int\n        :param EffectiveDaysRate: 有效天占比 保留小数点后四位0.2134\n        :type EffectiveDaysRate: float\n        :param BandwidthPkgType: 计费带宽包类型 实例"Address","LoadBalance","AddressIpv6"\n        :type BandwidthPkgType: str\n        """
        self.ZoneInfo = None
        self.Month = None
        self.BandwidthPkgId = None
        self.Isp = None
        self.TrafficMaxIn = None
        self.TrafficMaxOut = None
        self.FeeTraffic = None
        self.StartTime = None
        self.EndTime = None
        self.EffectiveDays = None
        self.MonthDays = None
        self.EffectiveDaysRate = None
        self.BandwidthPkgType = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        self.Month = params.get("Month")
        self.BandwidthPkgId = params.get("BandwidthPkgId")
        self.Isp = params.get("Isp")
        self.TrafficMaxIn = params.get("TrafficMaxIn")
        self.TrafficMaxOut = params.get("TrafficMaxOut")
        self.FeeTraffic = params.get("FeeTraffic")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.EffectiveDays = params.get("EffectiveDays")
        self.MonthDays = params.get("MonthDays")
        self.EffectiveDaysRate = params.get("EffectiveDaysRate")
        self.BandwidthPkgType = params.get("BandwidthPkgType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterface(AbstractModel):
    """弹性网卡

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-f1xjkw1b。\n        :type NetworkInterfaceId: str\n        :param NetworkInterfaceName: 弹性网卡名称。\n        :type NetworkInterfaceName: str\n        :param NetworkInterfaceDescription: 弹性网卡描述。\n        :type NetworkInterfaceDescription: str\n        :param SubnetId: 子网实例ID。\n        :type SubnetId: str\n        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param GroupSet: 绑定的安全组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type GroupSet: list of str\n        :param Primary: 是否是主网卡。\n        :type Primary: bool\n        :param MacAddress: MAC地址。\n        :type MacAddress: str\n        :param State: 弹性网卡状态：
PENDING：创建中
AVAILABLE：可用的
ATTACHING：绑定中
DETACHING：解绑中
DELETING：删除中\n        :type State: str\n        :param PrivateIpAddressSet: 内网IP信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification\n        :param Attachment: 绑定的云服务器对象。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Attachment: :class:`tencentcloud.ecm.v20190719.models.NetworkInterfaceAttachment`\n        :param Zone: 可用区。\n        :type Zone: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param Ipv6AddressSet: IPv6地址列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6AddressSet: list of Ipv6Address\n        :param TagSet: 标签键值对。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        :param EniType: 网卡类型。0 - 弹性网卡；1 - evm弹性网卡。\n        :type EniType: int\n        :param EcmRegion: EcmRegion ecm区域\n        :type EcmRegion: str\n        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SubnetId = None
        self.VpcId = None
        self.GroupSet = None
        self.Primary = None
        self.MacAddress = None
        self.State = None
        self.PrivateIpAddressSet = None
        self.Attachment = None
        self.Zone = None
        self.CreatedTime = None
        self.Ipv6AddressSet = None
        self.TagSet = None
        self.EniType = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SubnetId = params.get("SubnetId")
        self.VpcId = params.get("VpcId")
        self.GroupSet = params.get("GroupSet")
        self.Primary = params.get("Primary")
        self.MacAddress = params.get("MacAddress")
        self.State = params.get("State")
        if params.get("PrivateIpAddressSet") is not None:
            self.PrivateIpAddressSet = []
            for item in params.get("PrivateIpAddressSet"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddressSet.append(obj)
        if params.get("Attachment") is not None:
            self.Attachment = NetworkInterfaceAttachment()
            self.Attachment._deserialize(params.get("Attachment"))
        self.Zone = params.get("Zone")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.EniType = params.get("EniType")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkInterfaceAttachment(AbstractModel):
    """弹性网卡绑定关系

    """

    def __init__(self):
        """
        :param InstanceId: 云主机实例ID。\n        :type InstanceId: str\n        :param DeviceIndex: 网卡在云主机实例内的序号。\n        :type DeviceIndex: int\n        :param InstanceAccountId: 云主机所有者账户信息。\n        :type InstanceAccountId: str\n        :param AttachTime: 绑定时间。\n        :type AttachTime: str\n        """
        self.InstanceId = None
        self.DeviceIndex = None
        self.InstanceAccountId = None
        self.AttachTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceIndex = params.get("DeviceIndex")
        self.InstanceAccountId = params.get("InstanceAccountId")
        self.AttachTime = params.get("AttachTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkStorageRange(AbstractModel):
    """网络硬盘上下限数据

    """

    def __init__(self):
        """
        :param MaxBandwidth: 网络带宽上限\n        :type MaxBandwidth: int\n        :param MaxSystemDiskSize: 数据盘上限\n        :type MaxSystemDiskSize: int\n        :param MinBandwidth: 网络带宽下限\n        :type MinBandwidth: int\n        :param MinSystemDiskSize: 数据盘下限\n        :type MinSystemDiskSize: int\n        :param MaxDataDiskSize: 最大数据盘大小\n        :type MaxDataDiskSize: int\n        :param MinDataDiskSize: 最小数据盘大小\n        :type MinDataDiskSize: int\n        :param SuggestBandwidth: 建议带宽\n        :type SuggestBandwidth: int\n        :param SuggestDataDiskSize: 建议硬盘大小\n        :type SuggestDataDiskSize: int\n        :param SuggestSystemDiskSize: 建议系统盘大小\n        :type SuggestSystemDiskSize: int\n        :param MaxVcpu: Cpu核数峰值\n        :type MaxVcpu: int\n        :param MinVcpu: Cpu核最小值\n        :type MinVcpu: int\n        :param MaxVcpuPerReq: 单次请求最大cpu核数\n        :type MaxVcpuPerReq: int\n        :param PerBandwidth: 带宽步长\n        :type PerBandwidth: int\n        :param PerDataDisk: 数据盘步长\n        :type PerDataDisk: int\n        :param MaxModuleNum: 总模块数量\n        :type MaxModuleNum: int\n        """
        self.MaxBandwidth = None
        self.MaxSystemDiskSize = None
        self.MinBandwidth = None
        self.MinSystemDiskSize = None
        self.MaxDataDiskSize = None
        self.MinDataDiskSize = None
        self.SuggestBandwidth = None
        self.SuggestDataDiskSize = None
        self.SuggestSystemDiskSize = None
        self.MaxVcpu = None
        self.MinVcpu = None
        self.MaxVcpuPerReq = None
        self.PerBandwidth = None
        self.PerDataDisk = None
        self.MaxModuleNum = None


    def _deserialize(self, params):
        self.MaxBandwidth = params.get("MaxBandwidth")
        self.MaxSystemDiskSize = params.get("MaxSystemDiskSize")
        self.MinBandwidth = params.get("MinBandwidth")
        self.MinSystemDiskSize = params.get("MinSystemDiskSize")
        self.MaxDataDiskSize = params.get("MaxDataDiskSize")
        self.MinDataDiskSize = params.get("MinDataDiskSize")
        self.SuggestBandwidth = params.get("SuggestBandwidth")
        self.SuggestDataDiskSize = params.get("SuggestDataDiskSize")
        self.SuggestSystemDiskSize = params.get("SuggestSystemDiskSize")
        self.MaxVcpu = params.get("MaxVcpu")
        self.MinVcpu = params.get("MinVcpu")
        self.MaxVcpuPerReq = params.get("MaxVcpuPerReq")
        self.PerBandwidth = params.get("PerBandwidth")
        self.PerDataDisk = params.get("PerDataDisk")
        self.MaxModuleNum = params.get("MaxModuleNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Node(AbstractModel):
    """节点信息

    """

    def __init__(self):
        """
        :param ZoneInfo: zone信息\n        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`\n        :param Country: 国家信息\n        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`\n        :param Area: 区域信息\n        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`\n        :param Province: 省份信息\n        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`\n        :param City: 城市信息\n        :type City: :class:`tencentcloud.ecm.v20190719.models.City`\n        :param RegionInfo: Region信息\n        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`\n        :param ISPSet: 运营商列表\n        :type ISPSet: list of ISP\n        :param ISPNum: 运营商数量\n        :type ISPNum: int\n        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None
        self.ISPSet = None
        self.ISPNum = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        if params.get("ISPSet") is not None:
            self.ISPSet = []
            for item in params.get("ISPSet"):
                obj = ISP()
                obj._deserialize(item)
                self.ISPSet.append(obj)
        self.ISPNum = params.get("ISPNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NodeInstanceNum(AbstractModel):
    """节点实例数量信息

    """

    def __init__(self):
        """
        :param NodeNum: 节点数量\n        :type NodeNum: int\n        :param InstanceNum: 实例数量\n        :type InstanceNum: int\n        """
        self.NodeNum = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.NodeNum = params.get("NodeNum")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OperatorAction(AbstractModel):
    """操作Action

    """

    def __init__(self):
        """
        :param Action: 可执行操作\n        :type Action: str\n        :param Code: 编码Code
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: str\n        :param Message: 具体信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        """
        self.Action = None
        self.Code = None
        self.Message = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.Code = params.get("Code")
        self.Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OsVersion(AbstractModel):
    """操作系统支持的类型。

    """

    def __init__(self):
        """
        :param OsName: 操作系统类型\n        :type OsName: str\n        :param OsVersions: 支持的操作系统版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type OsVersions: list of str\n        :param Architecture: 支持的操作系统架构
注意：此字段可能返回 null，表示取不到有效值。\n        :type Architecture: list of str\n        """
        self.OsName = None
        self.OsVersions = None
        self.Architecture = None


    def _deserialize(self, params):
        self.OsName = params.get("OsName")
        self.OsVersions = params.get("OsVersions")
        self.Architecture = params.get("Architecture")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakBase(AbstractModel):
    """峰值信息

    """

    def __init__(self):
        """
        :param PeakCpuNum: CPU峰值\n        :type PeakCpuNum: int\n        :param PeakMemoryNum: 内存峰值\n        :type PeakMemoryNum: int\n        :param PeakStorageNum: 硬盘峰值\n        :type PeakStorageNum: int\n        :param RecordTime: 记录时间\n        :type RecordTime: str\n        """
        self.PeakCpuNum = None
        self.PeakMemoryNum = None
        self.PeakStorageNum = None
        self.RecordTime = None


    def _deserialize(self, params):
        self.PeakCpuNum = params.get("PeakCpuNum")
        self.PeakMemoryNum = params.get("PeakMemoryNum")
        self.PeakStorageNum = params.get("PeakStorageNum")
        self.RecordTime = params.get("RecordTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakFamilyInfo(AbstractModel):
    """PeakFamilyInfo 按机型类别分类的cpu等数据的峰值信息

    """

    def __init__(self):
        """
        :param InstanceFamily: 机型类别信息。\n        :type InstanceFamily: :class:`tencentcloud.ecm.v20190719.models.InstanceFamilyTypeConfig`\n        :param PeakBaseSet: 基础数据峰值信息。\n        :type PeakBaseSet: list of PeakBase\n        """
        self.InstanceFamily = None
        self.PeakBaseSet = None


    def _deserialize(self, params):
        if params.get("InstanceFamily") is not None:
            self.InstanceFamily = InstanceFamilyTypeConfig()
            self.InstanceFamily._deserialize(params.get("InstanceFamily"))
        if params.get("PeakBaseSet") is not None:
            self.PeakBaseSet = []
            for item in params.get("PeakBaseSet"):
                obj = PeakBase()
                obj._deserialize(item)
                self.PeakBaseSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetwork(AbstractModel):
    """峰值网络数据

    """

    def __init__(self):
        """
        :param RecordTime: 记录时间。\n        :type RecordTime: str\n        :param PeakInNetwork: 入带宽数据。\n        :type PeakInNetwork: str\n        :param PeakOutNetwork: 出带宽数据。\n        :type PeakOutNetwork: str\n        :param ChargeNetwork: 计费带宽。单位bps\n        :type ChargeNetwork: str\n        """
        self.RecordTime = None
        self.PeakInNetwork = None
        self.PeakOutNetwork = None
        self.ChargeNetwork = None


    def _deserialize(self, params):
        self.RecordTime = params.get("RecordTime")
        self.PeakInNetwork = params.get("PeakInNetwork")
        self.PeakOutNetwork = params.get("PeakOutNetwork")
        self.ChargeNetwork = params.get("ChargeNetwork")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PeakNetworkRegionInfo(AbstractModel):
    """region维度的网络峰值信息

    """

    def __init__(self):
        """
        :param Region: region信息\n        :type Region: str\n        :param PeakNetworkSet: 网络峰值集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type PeakNetworkSet: list of PeakNetwork\n        """
        self.Region = None
        self.PeakNetworkSet = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        if params.get("PeakNetworkSet") is not None:
            self.PeakNetworkSet = []
            for item in params.get("PeakNetworkSet"):
                obj = PeakNetwork()
                obj._deserialize(item)
                self.PeakNetworkSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PhysicalPosition(AbstractModel):
    """物理位置信息

    """

    def __init__(self):
        """
        :param PosId: 机位
注意：此字段可能返回 null，表示取不到有效值。\n        :type PosId: str\n        :param RackId: 机架
注意：此字段可能返回 null，表示取不到有效值。\n        :type RackId: str\n        :param SwitchId: 交换机
注意：此字段可能返回 null，表示取不到有效值。\n        :type SwitchId: str\n        """
        self.PosId = None
        self.RackId = None
        self.SwitchId = None


    def _deserialize(self, params):
        self.PosId = params.get("PosId")
        self.RackId = params.get("RackId")
        self.SwitchId = params.get("SwitchId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Position(AbstractModel):
    """描述实例的位置相关信息。

    """

    def __init__(self):
        """
        :param ZoneInfo: 实例所在的Zone的信息。\n        :type ZoneInfo: :class:`tencentcloud.ecm.v20190719.models.ZoneInfo`\n        :param Country: 实例所在的国家的信息。\n        :type Country: :class:`tencentcloud.ecm.v20190719.models.Country`\n        :param Area: 实例所在的Area的信息。\n        :type Area: :class:`tencentcloud.ecm.v20190719.models.Area`\n        :param Province: 实例所在的省份的信息。\n        :type Province: :class:`tencentcloud.ecm.v20190719.models.Province`\n        :param City: 实例所在的城市的信息。\n        :type City: :class:`tencentcloud.ecm.v20190719.models.City`\n        :param RegionInfo: 实例所在的Region的信息。\n        :type RegionInfo: :class:`tencentcloud.ecm.v20190719.models.RegionInfo`\n        """
        self.ZoneInfo = None
        self.Country = None
        self.Area = None
        self.Province = None
        self.City = None
        self.RegionInfo = None


    def _deserialize(self, params):
        if params.get("ZoneInfo") is not None:
            self.ZoneInfo = ZoneInfo()
            self.ZoneInfo._deserialize(params.get("ZoneInfo"))
        if params.get("Country") is not None:
            self.Country = Country()
            self.Country._deserialize(params.get("Country"))
        if params.get("Area") is not None:
            self.Area = Area()
            self.Area._deserialize(params.get("Area"))
        if params.get("Province") is not None:
            self.Province = Province()
            self.Province._deserialize(params.get("Province"))
        if params.get("City") is not None:
            self.City = City()
            self.City._deserialize(params.get("City"))
        if params.get("RegionInfo") is not None:
            self.RegionInfo = RegionInfo()
            self.RegionInfo._deserialize(params.get("RegionInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIPAddressInfo(AbstractModel):
    """实例的内网ip相关信息。

    """

    def __init__(self):
        """
        :param PrivateIPAddress: 实例的内网ip。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateIPAddress: str\n        """
        self.PrivateIPAddress = None


    def _deserialize(self, params):
        self.PrivateIPAddress = params.get("PrivateIPAddress")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateIpAddressSpecification(AbstractModel):
    """内网IP信息

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 内网IP地址。\n        :type PrivateIpAddress: str\n        :param Primary: 是否是主IP。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Primary: bool\n        :param PublicIpAddress: 公网IP地址。\n        :type PublicIpAddress: str\n        :param AddressId: EIP实例ID，例如：eip-11112222。\n        :type AddressId: str\n        :param Description: 内网IP描述信息。\n        :type Description: str\n        :param IsWanIpBlocked: 公网IP是否被封堵。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsWanIpBlocked: bool\n        :param State: IP状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的\n        :type State: str\n        """
        self.PrivateIpAddress = None
        self.Primary = None
        self.PublicIpAddress = None
        self.AddressId = None
        self.Description = None
        self.IsWanIpBlocked = None
        self.State = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.Primary = params.get("Primary")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.AddressId = params.get("AddressId")
        self.Description = params.get("Description")
        self.IsWanIpBlocked = params.get("IsWanIpBlocked")
        self.State = params.get("State")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Province(AbstractModel):
    """省份信息

    """

    def __init__(self):
        """
        :param ProvinceId: 省份Id\n        :type ProvinceId: str\n        :param ProvinceName: 省份名称\n        :type ProvinceName: str\n        """
        self.ProvinceId = None
        self.ProvinceName = None


    def _deserialize(self, params):
        self.ProvinceId = params.get("ProvinceId")
        self.ProvinceName = params.get("ProvinceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PublicIPAddressInfo(AbstractModel):
    """实例的公网ip相关信息。

    """

    def __init__(self):
        """
        :param ChargeMode: 计费模式。\n        :type ChargeMode: str\n        :param PublicIPAddress: 实例的公网ip。\n        :type PublicIPAddress: str\n        :param ISP: 实例的公网ip所属的运营商。\n        :type ISP: :class:`tencentcloud.ecm.v20190719.models.ISP`\n        :param MaxBandwidthOut: 实例的最大出带宽上限，单位为Mbps。\n        :type MaxBandwidthOut: int\n        :param MaxBandwidthIn: 实例的最大入带宽上限，单位为Mbps。\n        :type MaxBandwidthIn: int\n        """
        self.ChargeMode = None
        self.PublicIPAddress = None
        self.ISP = None
        self.MaxBandwidthOut = None
        self.MaxBandwidthIn = None


    def _deserialize(self, params):
        self.ChargeMode = params.get("ChargeMode")
        self.PublicIPAddress = params.get("PublicIPAddress")
        if params.get("ISP") is not None:
            self.ISP = ISP()
            self.ISP._deserialize(params.get("ISP"))
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")
        self.MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesRequest(AbstractModel):
    """RebootInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。\n        :type InstanceIdSet: list of str\n        :param ForceReboot: 是否在正常重启失败后选择强制重启实例。取值范围：
TRUE：表示在正常重启失败后进行强制重启；
FALSE：表示在正常重启失败后不进行强制重启；
默认取值：FALSE。\n        :type ForceReboot: bool\n        :param StopType: 关机类型。取值范围：
SOFT：表示软关机
HARD：表示硬关机
SOFT_FIRST：表示优先软关机，失败再执行硬关机

默认取值：SOFT。\n        :type StopType: str\n        """
        self.InstanceIdSet = None
        self.ForceReboot = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceReboot = params.get("ForceReboot")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RebootInstancesResponse(AbstractModel):
    """RebootInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RegionInfo(AbstractModel):
    """Region和RegionName

    """

    def __init__(self):
        """
        :param Region: Region\n        :type Region: str\n        :param RegionName: Region名称\n        :type RegionName: str\n        :param RegionId: RegionID\n        :type RegionId: int\n        """
        self.Region = None
        self.RegionName = None
        self.RegionId = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.RegionName = params.get("RegionName")
        self.RegionId = params.get("RegionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param AddressIds: 标识 EIP 的唯一 ID 列表。\n        :type AddressIds: list of str\n        """
        self.EcmRegion = None
        self.AddressIds = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.AddressIds = params.get("AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务TaskId。可以使用DescribeTaskResult接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReleaseIpv6AddressesRequest(AbstractModel):
    """ReleaseIpv6Addresses请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        :param NetworkInterfaceId: 弹性网卡实例ID，形如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: 指定的IPv6地址列表，单次最多指定10个。\n        :type Ipv6Addresses: list of Ipv6Address\n        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("Ipv6Addresses") is not None:
            self.Ipv6Addresses = []
            for item in params.get("Ipv6Addresses"):
                obj = Ipv6Address()
                obj._deserialize(item)
                self.Ipv6Addresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIpv6AddressesResponse(AbstractModel):
    """ReleaseIpv6Addresses返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 任务ID，可以通过DescribeTaskResult查询任务状态\n        :type TaskId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RemovePrivateIpAddressesRequest(AbstractModel):
    """RemovePrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param EcmRegion: ECM 地域，形如ap-xian-ecm。\n        :type EcmRegion: str\n        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-11112222。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        """
        self.EcmRegion = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.EcmRegion = params.get("EcmRegion")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemovePrivateIpAddressesResponse(AbstractModel):
    """RemovePrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID，例如：subnet-3x5lf5q0。可通过DescribeSubnets接口查询。\n        :type SubnetId: str\n        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param EcmRegion: ECM 地域\n        :type EcmRegion: str\n        """
        self.SubnetId = None
        self.RouteTableId = None
        self.EcmRegion = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")
        self.EcmRegion = params.get("EcmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID。\n        :type RouteTableId: str\n        :param Routes: 路由策略对象。\n        :type Routes: list of Route\n        """
        self.RouteTableId = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如esg-33ocnj9n，可通过DescribeSecurityGroups获取\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合对象。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.ecm.v20190719.models.SecurityGroupPolicySet`\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesMaxBandwidthRequest(AbstractModel):
    """ResetInstancesMaxBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重置带宽上限的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。\n        :type InstanceIdSet: list of str\n        :param MaxBandwidthOut: 修改后的最大出带宽上限。\n        :type MaxBandwidthOut: int\n        :param MaxBandwidthIn: 修改后的最大入带宽上限。\n        :type MaxBandwidthIn: int\n        """
        self.InstanceIdSet = None
        self.MaxBandwidthOut = None
        self.MaxBandwidthIn = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.MaxBandwidthOut = params.get("MaxBandwidthOut")
        self.MaxBandwidthIn = params.get("MaxBandwidthIn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesMaxBandwidthResponse(AbstractModel):
    """ResetInstancesMaxBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesPasswordRequest(AbstractModel):
    """ResetInstancesPassword请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重置密码的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。\n        :type InstanceIdSet: list of str\n        :param Password: 新密码，Linux实例密码必须8到16位，至少包括两项[a-z，A-Z]、[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。
Windows实例密码必须12到16位，至少包括三项[a-z]，[A-Z]，[0-9]和[( ) ~ ~ ! @ # $ % ^ & * - + = _ | { } [ ] : ; ' < > , . ? /]中的符号。密码不允许以/符号开头。
如果实例即包含Linux实例又包含Windows实例，则密码复杂度限制按照Windows实例的限制。\n        :type Password: str\n        :param ForceStop: 是否强制关机，默认为false。\n        :type ForceStop: bool\n        :param UserName: 待重置密码的实例的用户名，不得超过64个字符。若未指定用户名，则对于Linux而言，默认重置root用户的密码，对于Windows而言，默认重置administrator的密码。\n        :type UserName: str\n        """
        self.InstanceIdSet = None
        self.Password = None
        self.ForceStop = None
        self.UserName = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.Password = params.get("Password")
        self.ForceStop = params.get("ForceStop")
        self.UserName = params.get("UserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesPasswordResponse(AbstractModel):
    """ResetInstancesPassword返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetInstancesRequest(AbstractModel):
    """ResetInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待重装的实例ID列表。\n        :type InstanceIdSet: list of str\n        :param ImageId: 重装使用的镜像ID，若未指定，则使用各个实例当前的镜像进行重装。\n        :type ImageId: str\n        :param Password: 密码设置，若未指定，则后续将以站内信的形式通知密码。\n        :type Password: str\n        :param EnhancedService: 是否开启云监控和云镜服务，未指定时默认开启。\n        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`\n        :param KeepData: 是否保留数据盘数据，取值"true"/"false"。默认为"true"\n        :type KeepData: str\n        """
        self.InstanceIdSet = None
        self.ImageId = None
        self.Password = None
        self.EnhancedService = None
        self.KeepData = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ImageId = params.get("ImageId")
        self.Password = params.get("Password")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        self.KeepData = params.get("KeepData")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetInstancesResponse(AbstractModel):
    """ResetInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param RouteTableName: 路由表名称，最大长度不能超过60个字节。\n        :type RouteTableName: str\n        :param Routes: 路由策略。\n        :type Routes: list of Route\n        """
        self.RouteTableId = None
        self.RouteTableName = None
        self.Routes = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = Route()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Route(AbstractModel):
    """路由策略

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的IPv4网段\n        :type DestinationCidrBlock: str\n        :param GatewayType: 下一跳类型
NORMAL_CVM：普通云服务器；\n        :type GatewayType: str\n        :param GatewayId: 下一跳地址
这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址
当 GatewayType 为 EIP 时，GatewayId 固定值 '0'\n        :type GatewayId: str\n        :param RouteItemId: 路由策略唯一ID\n        :type RouteItemId: str\n        :param RouteDescription: 路由策略描述\n        :type RouteDescription: str\n        :param Enabled: 是否启用\n        :type Enabled: bool\n        :param RouteType: 路由类型，目前我们支持的类型有：
USER：用户路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和操作 USER 类型的路由。\n        :type RouteType: str\n        :param RouteId: 路由策略ID。IPv4路由策略ID是有意义的值，IPv6路由策略是无意义的值0。后续建议完全使用字符串唯一ID `RouteItemId`操作路由策略\n        :type RouteId: int\n        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteItemId = None
        self.RouteDescription = None
        self.Enabled = None
        self.RouteType = None
        self.RouteId = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteItemId = params.get("RouteItemId")
        self.RouteDescription = params.get("RouteDescription")
        self.Enabled = params.get("Enabled")
        self.RouteType = params.get("RouteType")
        self.RouteId = params.get("RouteId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteConflict(AbstractModel):
    """路由冲突对象

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID\n        :type RouteTableId: str\n        :param DestinationCidrBlock: 要检查的与之冲突的目的端\n        :type DestinationCidrBlock: str\n        :param ConflictSet: 冲突的路由策略列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConflictSet: list of Route\n        """
        self.RouteTableId = None
        self.DestinationCidrBlock = None
        self.ConflictSet = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        if params.get("ConflictSet") is not None:
            self.ConflictSet = []
            for item in params.get("ConflictSet"):
                obj = Route()
                obj._deserialize(item)
                self.ConflictSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTable(AbstractModel):
    """路由表

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID\n        :type VpcId: str\n        :param RouteTableId: 路由表实例ID\n        :type RouteTableId: str\n        :param RouteTableName: 路由表名称\n        :type RouteTableName: str\n        :param AssociationSet: 路由表关联关系
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssociationSet: list of RouteTableAssociation\n        :param RouteSet: IPv4路由策略集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteSet: list of Route\n        :param Main: 是否默认路由表\n        :type Main: bool\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        """
        self.VpcId = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.AssociationSet = None
        self.RouteSet = None
        self.Main = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        if params.get("AssociationSet") is not None:
            self.AssociationSet = []
            for item in params.get("AssociationSet"):
                obj = RouteTableAssociation()
                obj._deserialize(item)
                self.AssociationSet.append(obj)
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.Main = params.get("Main")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RouteTableAssociation(AbstractModel):
    """路由表关联关系

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID\n        :type SubnetId: str\n        :param RouteTableId: 路由表实例ID\n        :type RouteTableId: str\n        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleHealth(AbstractModel):
    """转发规则及健康状态列表

    """

    def __init__(self):
        """
        :param Targets: 本规则上绑定的后端的健康检查状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Targets: list of TargetHealth\n        """
        self.Targets = None


    def _deserialize(self, params):
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = TargetHealth()
                obj._deserialize(item)
                self.Targets.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunEIPDirectServiceEnabled(AbstractModel):
    """IP直通相关的信息

    """

    def __init__(self):
        """
        :param Enabled: 是否开通IP直通。取值范围：
TRUE：表示开通IP直通
FALSE：表示不开通IP直通
默认取值：TRUE。
windows镜像目前不支持IP直通。\n        :type Enabled: bool\n        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesRequest(AbstractModel):
    """RunInstances请求参数结构体

    """

    def __init__(self):
        """
        :param ZoneInstanceCountISPSet: 需要创建实例的可用区及创建数目及运营商的列表。在单次请求的过程中，单个region下的请求创建实例数上限为100\n        :type ZoneInstanceCountISPSet: list of ZoneInstanceCountISP\n        :param Password: 实例登录密码。不同操作系统类型密码复杂度限制不一样，具体如下：
Linux实例密码必须8到30位，至少包括两项[a-z]，[A-Z]、[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? / ]中的特殊符。Windows实例密码必须12到30位，至少包括三项[a-z]，[A-Z]，[0-9] 和 [( ) ` ~ ! @ # $ % ^ & - + = | { } [ ] : ; ' , . ? /]中的特殊符号。\n        :type Password: str\n        :param InternetMaxBandwidthOut: 公网出带宽上限，单位：Mbps。
1.如果未传该参数或者传的值为0，则使用模块下的默认值。
2.如果未传该参数或者传的值为0且未指定模块，则使用InternetMaxBandwidthIn的值\n        :type InternetMaxBandwidthOut: int\n        :param ModuleId: 模块ID。如果未传该参数，则必须传ImageId，InstanceType，DataDiskSize，InternetMaxBandwidthOut参数\n        :type ModuleId: str\n        :param ImageId: 镜像ID。如果未传该参数或者传的值为空，则使用模块下的默认值\n        :type ImageId: str\n        :param InstanceName: 实例显示名称。
不指定实例显示名称则默认显示‘未命名’。
购买多台实例，如果指定模式串{R:x}，表示生成数字[x, x+n-1]，其中n表示购买实例的数量，例如server\_{R:3}，购买1台时，实例显示名称为server\_3；购买2台时，实例显示名称分别为server\_3，server\_4。
支持指定多个模式串{R:x}。
购买多台实例，如果不指定模式串，则在实例显示名称添加后缀1、2...n，其中n表示购买实例的数量，例如server_，购买2台时，实例显示名称分别为server\_1，server\_2。
如果购买的实例属于不同的地域或运营商，则上述规则在每个地域和运营商内独立计数。
最多支持60个字符（包含模式串）。\n        :type InstanceName: str\n        :param HostName: 主机名称
点号（.）和短横线（-）不能作为 HostName 的首尾字符，不能连续使用。
Windows 实例：名字符长度为[2, 15]，允许字母（不限制大小写）、数字和短横线（-）组成，不支持点号（.），不能全是数字。
其他类型（Linux 等）实例：字符长度为[2, 60]，允许支持多个点号，点之间为一段，每段允许字母（不限制大小写）、数字和短横线（-）组成。\n        :type HostName: str\n        :param ClientToken: 用于保证请求幂等性的字符串。目前为保留参数，请勿使用。\n        :type ClientToken: str\n        :param EnhancedService: 增强服务。通过该参数可以指定是否开启云安全、云监控等服务。若不指定该参数，则默认公共镜像开启云监控、云安全服务\n        :type EnhancedService: :class:`tencentcloud.ecm.v20190719.models.EnhancedService`\n        :param TagSpecification: 标签列表\n        :type TagSpecification: list of TagSpecification\n        :param UserData: 提供给实例使用的用户数据，需要以 base64 方式编码，支持的最大数据大小为 16KB\n        :type UserData: str\n        :param InstanceType: 机型。如果未传该参数或者传的值为空，则使用模块下的默认值\n        :type InstanceType: str\n        :param DataDiskSize: 数据盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值\n        :type DataDiskSize: int\n        :param SecurityGroupIds: 实例所属安全组。该参数可以通过调用 DescribeSecurityGroups 的返回值中的sgId字段来获取。若不指定该参数，则绑定默认安全组。\n        :type SecurityGroupIds: list of str\n        :param SystemDiskSize: 系统盘大小，单位是G。如果未传该参数或者传的值为0，则使用模块下的默认值\n        :type SystemDiskSize: int\n        :param InternetMaxBandwidthIn: 公网入带宽上限，单位：Mbps。
1.如果未传该参数或者传的值为0，则使用对应模块的默认值。
2.如果未传该参数或者传的值为0且未指定模块，则使用InternetMaxBandwidthOut\n        :type InternetMaxBandwidthIn: int\n        :param InstanceChargeType: 实例计费类型。其中：
0，按资源维度后付费，计算当日用量峰值，例如CPU，内存，硬盘等，仅适用于非GNR系列机型；
1，按小时后付费，单价：xx元/实例/小时，仅适用于GNR机型，如需开通该计费方式请提工单申请；
2，按月后付费，单价：xx元/实例/月，仅适用于GNR机型；
该字段不填时，非GNR机型会默认选择0；GNR机型默认选择2。\n        :type InstanceChargeType: int\n        """
        self.ZoneInstanceCountISPSet = None
        self.Password = None
        self.InternetMaxBandwidthOut = None
        self.ModuleId = None
        self.ImageId = None
        self.InstanceName = None
        self.HostName = None
        self.ClientToken = None
        self.EnhancedService = None
        self.TagSpecification = None
        self.UserData = None
        self.InstanceType = None
        self.DataDiskSize = None
        self.SecurityGroupIds = None
        self.SystemDiskSize = None
        self.InternetMaxBandwidthIn = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        if params.get("ZoneInstanceCountISPSet") is not None:
            self.ZoneInstanceCountISPSet = []
            for item in params.get("ZoneInstanceCountISPSet"):
                obj = ZoneInstanceCountISP()
                obj._deserialize(item)
                self.ZoneInstanceCountISPSet.append(obj)
        self.Password = params.get("Password")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ModuleId = params.get("ModuleId")
        self.ImageId = params.get("ImageId")
        self.InstanceName = params.get("InstanceName")
        self.HostName = params.get("HostName")
        self.ClientToken = params.get("ClientToken")
        if params.get("EnhancedService") is not None:
            self.EnhancedService = EnhancedService()
            self.EnhancedService._deserialize(params.get("EnhancedService"))
        if params.get("TagSpecification") is not None:
            self.TagSpecification = []
            for item in params.get("TagSpecification"):
                obj = TagSpecification()
                obj._deserialize(item)
                self.TagSpecification.append(obj)
        self.UserData = params.get("UserData")
        self.InstanceType = params.get("InstanceType")
        self.DataDiskSize = params.get("DataDiskSize")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.SystemDiskSize = params.get("SystemDiskSize")
        self.InternetMaxBandwidthIn = params.get("InternetMaxBandwidthIn")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunInstancesResponse(AbstractModel):
    """RunInstances返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 创建中的实例ID列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceIdSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceIdSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.RequestId = params.get("RequestId")


class RunMonitorServiceEnabled(AbstractModel):
    """云监控服务

    """

    def __init__(self):
        """
        :param Enabled: 是否开启。\n        :type Enabled: bool\n        """
        self.Enabled = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RunSecurityServiceEnabled(AbstractModel):
    """云镜服务；

    """

    def __init__(self):
        """
        :param Enabled: 是否开启。\n        :type Enabled: bool\n        :param Version: 云镜版本：0 基础版，1 专业版。目前仅支持基础版\n        :type Version: int\n        """
        self.Enabled = None
        self.Version = None


    def _deserialize(self, params):
        self.Enabled = params.get("Enabled")
        self.Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroup(AbstractModel):
    """安全组对象

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如：esg-ohuuioma。\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type SecurityGroupName: str\n        :param SecurityGroupDesc: 安全组备注，最多100个字符。\n        :type SecurityGroupDesc: str\n        :param IsDefault: 是否是默认安全组，默认安全组不支持删除。\n        :type IsDefault: bool\n        :param CreatedTime: 安全组创建时间。\n        :type CreatedTime: str\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDesc = None
        self.IsDefault = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDesc = params.get("SecurityGroupDesc")
        self.IsDefault = params.get("IsDefault")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupAssociationStatistics(AbstractModel):
    """安全组关联的资源统计

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID。\n        :type SecurityGroupId: str\n        :param ECM: ECM实例数。\n        :type ECM: int\n        :param Module: ECM模块数。\n        :type Module: int\n        :param ENI: 弹性网卡实例数。\n        :type ENI: int\n        :param SG: 被安全组引用数。\n        :type SG: int\n        :param CLB: 负载均衡实例数。\n        :type CLB: int\n        :param InstanceStatistics: 全量实例的绑定统计。\n        :type InstanceStatistics: list of InstanceStatistic\n        :param TotalCount: 所有资源的总计数（不包含被安全组引用数）。\n        :type TotalCount: int\n        """
        self.SecurityGroupId = None
        self.ECM = None
        self.Module = None
        self.ENI = None
        self.SG = None
        self.CLB = None
        self.InstanceStatistics = None
        self.TotalCount = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.ECM = params.get("ECM")
        self.Module = params.get("Module")
        self.ENI = params.get("ENI")
        self.SG = params.get("SG")
        self.CLB = params.get("CLB")
        if params.get("InstanceStatistics") is not None:
            self.InstanceStatistics = []
            for item in params.get("InstanceStatistics"):
                obj = InstanceStatistic()
                obj._deserialize(item)
                self.InstanceStatistics.append(obj)
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupLimitSet(AbstractModel):
    """用户安全组配额限制

    """

    def __init__(self):
        """
        :param SecurityGroupLimit: 可创建安全组总数\n        :type SecurityGroupLimit: int\n        :param SecurityGroupPolicyLimit: 安全组下的最大规则数\n        :type SecurityGroupPolicyLimit: int\n        :param ReferedSecurityGroupLimit: 安全组下嵌套安全组规则数\n        :type ReferedSecurityGroupLimit: int\n        :param SecurityGroupInstanceLimit: 单安全组关联实例数\n        :type SecurityGroupInstanceLimit: int\n        :param InstanceSecurityGroupLimit: 实例关联安全组数\n        :type InstanceSecurityGroupLimit: int\n        :param SecurityGroupModuleLimit: 单安全组关联的模块数\n        :type SecurityGroupModuleLimit: int\n        :param ModuleSecurityGroupLimit: 模块关联的安全组数\n        :type ModuleSecurityGroupLimit: int\n        """
        self.SecurityGroupLimit = None
        self.SecurityGroupPolicyLimit = None
        self.ReferedSecurityGroupLimit = None
        self.SecurityGroupInstanceLimit = None
        self.InstanceSecurityGroupLimit = None
        self.SecurityGroupModuleLimit = None
        self.ModuleSecurityGroupLimit = None


    def _deserialize(self, params):
        self.SecurityGroupLimit = params.get("SecurityGroupLimit")
        self.SecurityGroupPolicyLimit = params.get("SecurityGroupPolicyLimit")
        self.ReferedSecurityGroupLimit = params.get("ReferedSecurityGroupLimit")
        self.SecurityGroupInstanceLimit = params.get("SecurityGroupInstanceLimit")
        self.InstanceSecurityGroupLimit = params.get("InstanceSecurityGroupLimit")
        self.SecurityGroupModuleLimit = params.get("SecurityGroupModuleLimit")
        self.ModuleSecurityGroupLimit = params.get("ModuleSecurityGroupLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicy(AbstractModel):
    """安全组规则对象

    """

    def __init__(self):
        """
        :param PolicyIndex: 安全组规则索引号\n        :type PolicyIndex: int\n        :param Protocol: 协议, 取值: TCP,UDP, ICMP。\n        :type Protocol: str\n        :param Port: 端口(all, 离散port, range)。\n        :type Port: str\n        :param ServiceTemplate: 协议端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。\n        :type ServiceTemplate: :class:`tencentcloud.ecm.v20190719.models.ServiceTemplateSpecification`\n        :param CidrBlock: 网段或IP(互斥)。\n        :type CidrBlock: str\n        :param SecurityGroupId: 安全组实例ID，例如：esg-ohuuioma。\n        :type SecurityGroupId: str\n        :param AddressTemplate: IP地址ID或者ID地址组ID。\n        :type AddressTemplate: :class:`tencentcloud.ecm.v20190719.models.AddressTemplateSpecification`\n        :param Action: ACCEPT 或 DROP。\n        :type Action: str\n        :param PolicyDescription: 安全组规则描述。\n        :type PolicyDescription: str\n        :param ModifyTime: 修改时间，例如 2020-07-22 19：27：23
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModifyTime: str\n        :param Ipv6CidrBlock: 网段或IPv6(互斥)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6CidrBlock: str\n        """
        self.PolicyIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplate = None
        self.CidrBlock = None
        self.SecurityGroupId = None
        self.AddressTemplate = None
        self.Action = None
        self.PolicyDescription = None
        self.ModifyTime = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplateSpecification()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.CidrBlock = params.get("CidrBlock")
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplateSpecification()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.Action = params.get("Action")
        self.PolicyDescription = params.get("PolicyDescription")
        self.ModifyTime = params.get("ModifyTime")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupPolicySet(AbstractModel):
    """安全组规则集合

    """

    def __init__(self):
        """
        :param Version: 安全组规则当前版本。用户每次更新安全规则版本会自动加1，防止更新的路由规则已过期，不填不考虑冲突。\n        :type Version: str\n        :param Egress: 出站规则。其中出站规则和入站规则必须选一个。\n        :type Egress: list of SecurityGroupPolicy\n        :param Ingress: 入站规则。其中出站规则和入站规则必须选一个。\n        :type Ingress: list of SecurityGroupPolicy\n        """
        self.Version = None
        self.Egress = None
        self.Ingress = None


    def _deserialize(self, params):
        self.Version = params.get("Version")
        if params.get("Egress") is not None:
            self.Egress = []
            for item in params.get("Egress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.Egress.append(obj)
        if params.get("Ingress") is not None:
            self.Ingress = []
            for item in params.get("Ingress"):
                obj = SecurityGroupPolicy()
                obj._deserialize(item)
                self.Ingress.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateSpecification(AbstractModel):
    """协议端口模版

    """

    def __init__(self):
        """
        :param ServiceId: 协议端口ID，例如：eppm-f5n1f8da。\n        :type ServiceId: str\n        :param ServiceGroupId: 协议端口组ID，例如：eppmg-f5n1f8da。\n        :type ServiceGroupId: str\n        """
        self.ServiceId = None
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsRequest(AbstractModel):
    """SetLoadBalancerSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerId: 负载均衡实例 ID\n        :type LoadBalancerId: str\n        :param SecurityGroups: 安全组ID构成的数组，一个负载均衡实例最多可绑定5个安全组，如果要解绑所有安全组，可不传此参数，或传入空数组\n        :type SecurityGroups: list of str\n        """
        self.LoadBalancerId = None
        self.SecurityGroups = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.SecurityGroups = params.get("SecurityGroups")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetLoadBalancerSecurityGroupsResponse(AbstractModel):
    """SetLoadBalancerSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetSecurityGroupForLoadbalancersRequest(AbstractModel):
    """SetSecurityGroupForLoadbalancers请求参数结构体

    """

    def __init__(self):
        """
        :param LoadBalancerIds: 负载均衡实例ID数组\n        :type LoadBalancerIds: list of str\n        :param SecurityGroup: 安全组ID，如 esg-12345678\n        :type SecurityGroup: str\n        :param OperationType: ADD 绑定安全组；
DEL 解绑安全组\n        :type OperationType: str\n        """
        self.LoadBalancerIds = None
        self.SecurityGroup = None
        self.OperationType = None


    def _deserialize(self, params):
        self.LoadBalancerIds = params.get("LoadBalancerIds")
        self.SecurityGroup = params.get("SecurityGroup")
        self.OperationType = params.get("OperationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetSecurityGroupForLoadbalancersResponse(AbstractModel):
    """SetSecurityGroupForLoadbalancers返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SimpleModule(AbstractModel):
    """Module的简要信息

    """

    def __init__(self):
        """
        :param ModuleId: 模块ID\n        :type ModuleId: str\n        :param ModuleName: 模块名称\n        :type ModuleName: str\n        """
        self.ModuleId = None
        self.ModuleName = None


    def _deserialize(self, params):
        self.ModuleId = params.get("ModuleId")
        self.ModuleName = params.get("ModuleName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SrcImage(AbstractModel):
    """镜像来源信息

    """

    def __init__(self):
        """
        :param ImageId: 镜像id\n        :type ImageId: str\n        :param ImageName: 镜像名称\n        :type ImageName: str\n        :param ImageOsName: 系统名称\n        :type ImageOsName: str\n        :param ImageDescription: 镜像描述\n        :type ImageDescription: str\n        :param Region: 区域\n        :type Region: str\n        :param RegionID: 区域ID\n        :type RegionID: int\n        :param RegionName: 区域名称\n        :type RegionName: str\n        :param InstanceName: 来源实例名称\n        :type InstanceName: str\n        :param InstanceId: 来源实例ID\n        :type InstanceId: str\n        :param ImageType: 来源镜像类型\n        :type ImageType: str\n        """
        self.ImageId = None
        self.ImageName = None
        self.ImageOsName = None
        self.ImageDescription = None
        self.Region = None
        self.RegionID = None
        self.RegionName = None
        self.InstanceName = None
        self.InstanceId = None
        self.ImageType = None


    def _deserialize(self, params):
        self.ImageId = params.get("ImageId")
        self.ImageName = params.get("ImageName")
        self.ImageOsName = params.get("ImageOsName")
        self.ImageDescription = params.get("ImageDescription")
        self.Region = params.get("Region")
        self.RegionID = params.get("RegionID")
        self.RegionName = params.get("RegionName")
        self.InstanceName = params.get("InstanceName")
        self.InstanceId = params.get("InstanceId")
        self.ImageType = params.get("ImageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesRequest(AbstractModel):
    """StartInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待开启的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。\n        :type InstanceIdSet: list of str\n        """
        self.InstanceIdSet = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartInstancesResponse(AbstractModel):
    """StartInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopInstancesRequest(AbstractModel):
    """StopInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 需要关机的实例ID列表。在单次请求的过程中，单个region下的请求实例数上限为100。\n        :type InstanceIdSet: list of str\n        :param ForceStop: 是否在正常关闭失败后选择强制关闭实例，默认为false，即否。\n        :type ForceStop: bool\n        :param StopType: 实例的关闭模式。取值范围：
SOFT_FIRST：表示在正常关闭失败后进行强制关闭;
HARD：直接强制关闭;
SOFT：仅软关机；
默认为SOFT。\n        :type StopType: str\n        """
        self.InstanceIdSet = None
        self.ForceStop = None
        self.StopType = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.ForceStop = params.get("ForceStop")
        self.StopType = params.get("StopType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopInstancesResponse(AbstractModel):
    """StopInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subnet(AbstractModel):
    """子网对象

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param SubnetId: 子网实例ID，例如：subnet-bthucmmy。\n        :type SubnetId: str\n        :param SubnetName: 子网名称。\n        :type SubnetName: str\n        :param CidrBlock: 子网的 IPv4 CIDR。\n        :type CidrBlock: str\n        :param IsDefault: 是否默认子网。\n        :type IsDefault: bool\n        :param EnableBroadcast: 是否开启广播。\n        :type EnableBroadcast: bool\n        :param RouteTableId: 路由表实例ID，例如：rtb-l2h8d7c2。\n        :type RouteTableId: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param AvailableIpAddressCount: 可用IP数。\n        :type AvailableIpAddressCount: int\n        :param Ipv6CidrBlock: 子网的 IPv6 CIDR。\n        :type Ipv6CidrBlock: str\n        :param NetworkAclId: 关联ACLID\n        :type NetworkAclId: str\n        :param IsRemoteVpcSnat: 是否为 SNAT 地址池子网。\n        :type IsRemoteVpcSnat: bool\n        :param TagSet: 标签键值对。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        :param Zone: 所在区域\n        :type Zone: str\n        :param ZoneName: 可用区名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type ZoneName: str\n        :param InstanceCount: 实例数量
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceCount: int\n        :param VpcCidrBlock: VPC的 IPv4 CIDR。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcCidrBlock: str\n        :param VpcIpv6CidrBlock: VPC的 IPv6 CIDR。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcIpv6CidrBlock: str\n        :param Region: 地域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableBroadcast = None
        self.RouteTableId = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None
        self.NetworkAclId = None
        self.IsRemoteVpcSnat = None
        self.TagSet = None
        self.Zone = None
        self.ZoneName = None
        self.InstanceCount = None
        self.VpcCidrBlock = None
        self.VpcIpv6CidrBlock = None
        self.Region = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableBroadcast = params.get("EnableBroadcast")
        self.RouteTableId = params.get("RouteTableId")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.NetworkAclId = params.get("NetworkAclId")
        self.IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.Zone = params.get("Zone")
        self.ZoneName = params.get("ZoneName")
        self.InstanceCount = params.get("InstanceCount")
        self.VpcCidrBlock = params.get("VpcCidrBlock")
        self.VpcIpv6CidrBlock = params.get("VpcIpv6CidrBlock")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        """
        :param Key: 标签健。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: 标签值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
        self.Key = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息。

    """

    def __init__(self):
        """
        :param TagKey: 标签的键。\n        :type TagKey: str\n        :param TagValue: 标签的值。\n        :type TagValue: str\n        """
        self.TagKey = None
        self.TagValue = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagSpecification(AbstractModel):
    """资源类型的Tag

    """

    def __init__(self):
        """
        :param ResourceType: 资源类型，目前仅支持"instance"、"module"\n        :type ResourceType: str\n        :param Tags: 标签列表\n        :type Tags: list of Tag\n        """
        self.ResourceType = None
        self.Tags = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Target(AbstractModel):
    """负责均衡后端目标

    """

    def __init__(self):
        """
        :param Port: 后端服务的监听端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param InstanceId: 子机ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceId: str\n        :param Weight: 后端服务的转发权重，取值范围：[0, 100]，默认为 10。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        :param EniIp: 绑定弹性网卡时需要传入此参数，代表弹性网卡的IP，弹性网卡必须先绑定至子机，然后才能绑定到负载均衡实例。注意：参数 InstanceId 和 EniIp 只能传入一个且必须传入一个。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EniIp: str\n        """
        self.Port = None
        self.InstanceId = None
        self.Weight = None
        self.EniIp = None


    def _deserialize(self, params):
        self.Port = params.get("Port")
        self.InstanceId = params.get("InstanceId")
        self.Weight = params.get("Weight")
        self.EniIp = params.get("EniIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetHealth(AbstractModel):
    """后端的健康检查状态

    """

    def __init__(self):
        """
        :param IP: Target的内网IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type IP: str\n        :param Port: Target绑定的端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type Port: int\n        :param HealthStatus: 当前健康状态，true：健康，false：不健康（包括尚未开始探测、探测中、状态异常等几种状态）。只有处于健康状态（且权重大于0），负载均衡才会向其转发流量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthStatus: bool\n        :param TargetId: Target的实例ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TargetId: str\n        :param HealthStatusDetail: 当前健康状态的详细信息。如：Alive、Dead、Unknown、Close。Alive状态为健康，Dead状态为异常，Unknown状态包括尚未开始探测、探测中、状态未知，Close为未配置健康检查。
注意：此字段可能返回 null，表示取不到有效值。\n        :type HealthStatusDetail: str\n        """
        self.IP = None
        self.Port = None
        self.HealthStatus = None
        self.TargetId = None
        self.HealthStatusDetail = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Port = params.get("Port")
        self.HealthStatus = params.get("HealthStatus")
        self.TargetId = params.get("TargetId")
        self.HealthStatusDetail = params.get("HealthStatusDetail")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TargetsWeightRule(AbstractModel):
    """目标和权重的描述信息

    """

    def __init__(self):
        """
        :param ListenerId: 负载均衡监听器 ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type ListenerId: str\n        :param Targets: 要修改权重的后端机器列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Targets: list of Target\n        :param Weight: 后端服务新的转发权重，取值范围：0~100。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Weight: int\n        """
        self.ListenerId = None
        self.Targets = None
        self.Weight = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("Targets") is not None:
            self.Targets = []
            for item in params.get("Targets"):
                obj = Target()
                obj._deserialize(item)
                self.Targets.append(obj)
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskInput(AbstractModel):
    """任务查询

    """

    def __init__(self):
        """
        :param Operation: 操作名，即API名称，比如：CreateImage\n        :type Operation: str\n        :param TaskId: 任务id\n        :type TaskId: str\n        """
        self.Operation = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Operation = params.get("Operation")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TaskOutput(AbstractModel):
    """任务查询出参

    """

    def __init__(self):
        """
        :param TaskId: 任务id\n        :type TaskId: str\n        :param Message: 状态描述\n        :type Message: str\n        :param Status: 状态值，SUCCESS/FAILED/OPERATING\n        :type Status: str\n        :param AddTime: 任务提交时间\n        :type AddTime: str\n        :param EndTime: 任务结束时间\n        :type EndTime: str\n        :param Operation: 操作名\n        :type Operation: str\n        """
        self.TaskId = None
        self.Message = None
        self.Status = None
        self.AddTime = None
        self.EndTime = None
        self.Operation = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Message = params.get("Message")
        self.Status = params.get("Status")
        self.AddTime = params.get("AddTime")
        self.EndTime = params.get("EndTime")
        self.Operation = params.get("Operation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesRequest(AbstractModel):
    """TerminateInstances请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceIdSet: 待销毁的实例ID列表。\n        :type InstanceIdSet: list of str\n        :param TerminateDelay: 是否定时销毁，默认为否。\n        :type TerminateDelay: bool\n        :param TerminateTime: 定时销毁的时间，格式形如："2019-08-05 12:01:30"，若非定时销毁，则此参数被忽略。\n        :type TerminateTime: str\n        :param AssociatedResourceDestroy: 是否关联删除已绑定的弹性网卡和弹性IP，默认为true。
当为true时，一并删除弹性网卡和弹性IP；
当为false时，只销毁主机，保留弹性网卡和弹性IP。\n        :type AssociatedResourceDestroy: bool\n        """
        self.InstanceIdSet = None
        self.TerminateDelay = None
        self.TerminateTime = None
        self.AssociatedResourceDestroy = None


    def _deserialize(self, params):
        self.InstanceIdSet = params.get("InstanceIdSet")
        self.TerminateDelay = params.get("TerminateDelay")
        self.TerminateTime = params.get("TerminateTime")
        self.AssociatedResourceDestroy = params.get("AssociatedResourceDestroy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TerminateInstancesResponse(AbstractModel):
    """TerminateInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class VirtualPrivateCloud(AbstractModel):
    """私有网络相关信息配置。

    """

    def __init__(self):
        """
        :param VpcId: 私有网络ID，形如vpc-xxx。\n        :type VpcId: str\n        :param SubnetId: 私有网络子网ID，形如subnet-xxx。\n        :type SubnetId: str\n        :param AsVpcGateway: 是否用作公网网关。公网网关只有在实例拥有公网IP以及处于私有网络下时才能正常使用。取值范围：
TRUE：表示用作公网网关
FALSE：表示不用作公网网关

默认取值：FALSE。\n        :type AsVpcGateway: bool\n        :param PrivateIpAddresses: 私有网络子网 IP 数组，在创建实例、修改实例vpc属性操作中可使用此参数。\n        :type PrivateIpAddresses: list of str\n        :param Ipv6AddressCount: 为弹性网卡指定随机生成的 IPv6 地址数量。\n        :type Ipv6AddressCount: int\n        """
        self.VpcId = None
        self.SubnetId = None
        self.AsVpcGateway = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.AsVpcGateway = params.get("AsVpcGateway")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """私有网络(VPC)对象。

    """

    def __init__(self):
        """
        :param VpcName: VPC名称。\n        :type VpcName: str\n        :param VpcId: VPC实例ID，例如：vpc-azd4dt1c。\n        :type VpcId: str\n        :param CidrBlock: VPC的IPv4 CIDR。\n        :type CidrBlock: str\n        :param IsDefault: 是否默认VPC。\n        :type IsDefault: bool\n        :param EnableMulticast: 是否开启组播。\n        :type EnableMulticast: bool\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param DnsServerSet: DNS列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DnsServerSet: list of str\n        :param DomainName: DHCP域名选项值。\n        :type DomainName: str\n        :param DhcpOptionsId: DHCP选项集ID。\n        :type DhcpOptionsId: str\n        :param EnableDhcp: 是否开启DHCP。\n        :type EnableDhcp: bool\n        :param Ipv6CidrBlock: VPC的IPv6 CIDR。\n        :type Ipv6CidrBlock: str\n        :param TagSet: 标签键值对
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        :param AssistantCidrSet: 辅助CIDR
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssistantCidrSet: list of AssistantCidr\n        :param Region: 地域\n        :type Region: str\n        :param Description: 描述\n        :type Description: str\n        :param RegionName: 地域中文名\n        :type RegionName: str\n        :param SubnetCount: 包含子网数量\n        :type SubnetCount: int\n        :param InstanceCount: 包含实例数量\n        :type InstanceCount: int\n        """
        self.VpcName = None
        self.VpcId = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableMulticast = None
        self.CreatedTime = None
        self.DnsServerSet = None
        self.DomainName = None
        self.DhcpOptionsId = None
        self.EnableDhcp = None
        self.Ipv6CidrBlock = None
        self.TagSet = None
        self.AssistantCidrSet = None
        self.Region = None
        self.Description = None
        self.RegionName = None
        self.SubnetCount = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.VpcId = params.get("VpcId")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableMulticast = params.get("EnableMulticast")
        self.CreatedTime = params.get("CreatedTime")
        self.DnsServerSet = params.get("DnsServerSet")
        self.DomainName = params.get("DomainName")
        self.DhcpOptionsId = params.get("DhcpOptionsId")
        self.EnableDhcp = params.get("EnableDhcp")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.Region = params.get("Region")
        self.Description = params.get("Description")
        self.RegionName = params.get("RegionName")
        self.SubnetCount = params.get("SubnetCount")
        self.InstanceCount = params.get("InstanceCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInfo(AbstractModel):
    """Zone信息

    """

    def __init__(self):
        """
        :param ZoneId: ZoneId\n        :type ZoneId: int\n        :param ZoneName: ZoneName\n        :type ZoneName: str\n        :param Zone: Zone\n        :type Zone: str\n        """
        self.ZoneId = None
        self.ZoneName = None
        self.Zone = None


    def _deserialize(self, params):
        self.ZoneId = params.get("ZoneId")
        self.ZoneName = params.get("ZoneName")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceCountISP(AbstractModel):
    """实例可用区及对应的实例创建数目及运营商的组合；

    """

    def __init__(self):
        """
        :param Zone: 创建实例的可用区。\n        :type Zone: str\n        :param InstanceCount: 在当前可用区欲创建的实例数目。\n        :type InstanceCount: int\n        :param ISP: 运营商如下：
CTCC：中国电信
CUCC：中国联通
CMCC：中国移动
多个运营商用英文分号连接";"，例如："CMCC;CUCC;CTCC"。多运营商需要开通白名单，请直接联系腾讯云客服。\n        :type ISP: str\n        :param VpcId: 指定私有网络编号，SubnetId与VpcId必须同时指定或不指定\n        :type VpcId: str\n        :param SubnetId: 指定子网编号，SubnetId与VpcId必须同时指定或不指定\n        :type SubnetId: str\n        :param PrivateIpAddresses: 指定主网卡内网IP。条件：SubnetId与VpcId必须同时指定，并且IP数量与InstanceCount相同，多IP主机副网卡内网IP在相同子网内通过DHCP获取。\n        :type PrivateIpAddresses: list of str\n        :param Ipv6AddressCount: 为弹性网卡指定随机生成的IPv6地址数量，目前数量不能大于1。\n        :type Ipv6AddressCount: int\n        """
        self.Zone = None
        self.InstanceCount = None
        self.ISP = None
        self.VpcId = None
        self.SubnetId = None
        self.PrivateIpAddresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.InstanceCount = params.get("InstanceCount")
        self.ISP = params.get("ISP")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        self.Ipv6AddressCount = params.get("Ipv6AddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ZoneInstanceInfo(AbstractModel):
    """Zone的实例信息

    """

    def __init__(self):
        """
        :param ZoneName: Zone名称\n        :type ZoneName: str\n        :param InstanceNum: 实例数量\n        :type InstanceNum: int\n        """
        self.ZoneName = None
        self.InstanceNum = None


    def _deserialize(self, params):
        self.ZoneName = params.get("ZoneName")
        self.InstanceNum = params.get("InstanceNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        