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


class AcceptAttachCcnInstancesRequest(AbstractModel):
    """AcceptAttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 接受关联实例列表。
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class AcceptAttachCcnInstancesResponse(AbstractModel):
    """AcceptAttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccountAttribute(AbstractModel):
    """账户属性对象

    """

    def __init__(self):
        """
        :param AttributeName: 属性名
        :type AttributeName: str
        :param AttributeValues: 属性值
        :type AttributeValues: list of str
        """
        self.AttributeName = None
        self.AttributeValues = None


    def _deserialize(self, params):
        self.AttributeName = params.get("AttributeName")
        self.AttributeValues = params.get("AttributeValues")


class AddBandwidthPackageResourcesRequest(AbstractModel):
    """AddBandwidthPackageResources请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceIds: 资源Id，形如'eip-xxxx', 'lb-xxxx'
        :type ResourceIds: list of str
        :param BandwidthPackageId: 带宽包唯一标识ID，形如'bwp-xxxx'
        :type BandwidthPackageId: str
        :param NetworkType: 带宽包类型，包括'BGP', 'SINGLEISP', 'ANYCAST'
        :type NetworkType: str
        :param ResourceType: 资源类型，包括'Address', 'LoadBalance'
        :type ResourceType: str
        """
        self.ResourceIds = None
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ResourceType = params.get("ResourceType")


class AddBandwidthPackageResourcesResponse(AbstractModel):
    """AddBandwidthPackageResources返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddIp6RulesRequest(AbstractModel):
    """AddIp6Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6RuleInfos: IPV6转换规则信息
        :type Ip6RuleInfos: list of Ip6RuleInfo
        :param Ip6RuleName: IPV6转换规则名称
        :type Ip6RuleName: str
        """
        self.Ip6TranslatorId = None
        self.Ip6RuleInfos = None
        self.Ip6RuleName = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        if params.get("Ip6RuleInfos") is not None:
            self.Ip6RuleInfos = []
            for item in params.get("Ip6RuleInfos"):
                obj = Ip6RuleInfo()
                obj._deserialize(item)
                self.Ip6RuleInfos.append(obj)
        self.Ip6RuleName = params.get("Ip6RuleName")


class AddIp6RulesResponse(AbstractModel):
    """AddIp6Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Ip6RuleSet: IPV6转换规则唯一ID数组，形如rule6-xxxxxxxx
        :type Ip6RuleSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ip6RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip6RuleSet = params.get("Ip6RuleSet")
        self.RequestId = params.get("RequestId")


class Address(AbstractModel):
    """描述 EIP 信息

    """

    def __init__(self):
        """
        :param AddressId: `EIP`的`ID`，是`EIP`的唯一标识。
        :type AddressId: str
        :param AddressName: `EIP`名称。
        :type AddressName: str
        :param AddressStatus: `EIP`状态。
        :type AddressStatus: str
        :param AddressIp: 外网IP地址
        :type AddressIp: str
        :param InstanceId: 绑定的资源实例`ID`。可能是一个`CVM`，`NAT`。
        :type InstanceId: str
        :param CreatedTime: 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param NetworkInterfaceId: 绑定的弹性网卡ID
        :type NetworkInterfaceId: str
        :param PrivateAddressIp: 绑定的资源内网ip
        :type PrivateAddressIp: str
        :param IsArrears: 资源隔离状态。true表示eip处于隔离状态，false表示资源处于未隔离装填
        :type IsArrears: bool
        :param IsBlocked: 资源封堵状态。true表示eip处于封堵状态，false表示eip处于未封堵状态
        :type IsBlocked: bool
        :param IsEipDirectConnection: eip是否支持直通模式。true表示eip支持直通模式，false表示资源不支持直通模式
        :type IsEipDirectConnection: bool
        :param AddressType: eip资源类型，包括"CalcIP","WanIP","EIP","AnycastEIP"。其中"CalcIP"表示设备ip，“WanIP”表示普通公网ip，“EIP”表示弹性公网ip，“AnycastEip”表示加速EIP
        :type AddressType: str
        :param CascadeRelease: eip是否在解绑后自动释放。true表示eip将会在解绑后自动释放，false表示eip在解绑后不会自动释放
        :type CascadeRelease: bool
        """
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


class AddressTemplate(AbstractModel):
    """IP地址模板

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP地址模板名称。
        :type AddressTemplateName: str
        :param AddressTemplateId: IP地址模板实例唯一ID。
        :type AddressTemplateId: str
        :param AddressSet: IP地址信息。
        :type AddressSet: list of str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        """
        self.AddressTemplateName = None
        self.AddressTemplateId = None
        self.AddressSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressSet = params.get("AddressSet")
        self.CreatedTime = params.get("CreatedTime")


class AddressTemplateGroup(AbstractModel):
    """IP地址模板集合

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP地址模板集合名称。
        :type AddressTemplateGroupName: str
        :param AddressTemplateGroupId: IP地址模板集合实例ID，例如：ipmg-dih8xdbq。
        :type AddressTemplateGroupId: str
        :param AddressTemplateIdSet: IP地址模板ID。
        :type AddressTemplateIdSet: list of str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateGroupId = None
        self.AddressTemplateIdSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateIdSet = params.get("AddressTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")


class AddressTemplateSpecification(AbstractModel):
    """IP地址模版

    """

    def __init__(self):
        """
        :param AddressId: IP地址ID，例如：ipm-2uw6ujo6。
        :type AddressId: str
        :param AddressGroupId: IP地址组ID，例如：ipmg-2uw6ujo6。
        :type AddressGroupId: str
        """
        self.AddressId = None
        self.AddressGroupId = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressGroupId = params.get("AddressGroupId")


class AllocateAddressesRequest(AbstractModel):
    """AllocateAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param AddressCount: 申请 EIP 数量，默认值为1。
        :type AddressCount: int
        """
        self.AddressCount = None


    def _deserialize(self, params):
        self.AddressCount = params.get("AddressCount")


class AllocateAddressesResponse(AbstractModel):
    """AllocateAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param AddressSet: 申请到的 EIP 的唯一 ID 列表。
        :type AddressSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。
        :type SecondaryPrivateIpAddressCount: int
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")


class AssignPrivateIpAddressesResponse(AbstractModel):
    """AssignPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param PrivateIpAddressSet: 内网IP详细信息。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class AssociateAddressRequest(AbstractModel):
    """AssociateAddress请求参数结构体

    """

    def __init__(self):
        """
        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressId: str
        :param InstanceId: 要绑定的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录[控制台](https://console.cloud.tencent.com/cvm)查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        :param NetworkInterfaceId: 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：`eni-11112222`。`NetworkInterfaceId` 与 `InstanceId` 不可同时指定。弹性网卡 ID 可通过登录[控制台](https://console.cloud.tencent.com/vpc/eni)查询，也可通过[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)接口返回值中的`networkInterfaceId`获取。
        :type NetworkInterfaceId: str
        :param PrivateIpAddress: 要绑定的内网 IP。如果指定了 `NetworkInterfaceId` 则也必须指定 `PrivateIpAddress` ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 `PrivateIpAddress` 是指定的 `NetworkInterfaceId` 上的一个内网 IP。指定弹性网卡的内网 IP 可通过登录[控制台](https://console.cloud.tencent.com/vpc/eni)查询，也可通过[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)接口返回值中的`privateIpAddress`获取。
        :type PrivateIpAddress: str
        """
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class AssociateAddressResponse(AbstractModel):
    """AssociateAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 关联网络实例列表
        :type Instances: list of CcnInstance
        :param CcnUin: CCN所属UIN（根账号），默认当前账号所属UIN
        :type CcnUin: str
        """
        self.CcnId = None
        self.Instances = None
        self.CcnUin = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)
        self.CcnUin = params.get("CcnUin")


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachClassicLinkVpcRequest(AbstractModel):
    """AttachClassicLinkVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID
        :type VpcId: str
        :param InstanceIds: CVM实例ID
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class AttachClassicLinkVpcResponse(AbstractModel):
    """AttachClassicLinkVpc返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachNetworkInterfaceRequest(AbstractModel):
    """AttachNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param InstanceId: CVM实例ID。形如：ins-r8hr2upy。
        :type InstanceId: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")


class AttachNetworkInterfaceResponse(AbstractModel):
    """AttachNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BandwidthPackage(AbstractModel):
    """描述带宽包信息的结构

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一标识Id
        :type BandwidthPackageId: str
        :param NetworkType: 带宽包类型，包括'BGP','SINGLEISP','ANYCAST'
        :type NetworkType: str
        :param ChargeType: 带宽包计费类型，包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'
        :type ChargeType: str
        :param BandwidthPackageName: 带宽包名称
        :type BandwidthPackageName: str
        :param CreatedTime: 带宽包创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。
        :type CreatedTime: str
        :param Status: 带宽包状态，包括'CREATING','CREATED','DELETING','DELETED'
        :type Status: str
        :param ResourceSet: 带宽包资源信息
        :type ResourceSet: list of Resource
        :param Bandwidth: 带宽包限速大小。单位：Mbps，-1表示不限速。
        :type Bandwidth: int
        """
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.CreatedTime = None
        self.Status = None
        self.ResourceSet = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.CreatedTime = params.get("CreatedTime")
        self.Status = params.get("Status")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.Bandwidth = params.get("Bandwidth")


class CCN(AbstractModel):
    """云联网（CCN）对象

    """

    def __init__(self):
        """
        :param CcnId: 云联网唯一ID
        :type CcnId: str
        :param CcnName: 云联网名称
        :type CcnName: str
        :param CcnDescription: 云联网描述信息
        :type CcnDescription: str
        :param InstanceCount: 关联实例数量
        :type InstanceCount: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param State: 实例状态， 'ISOLATED': 隔离中（欠费停服），'AVAILABLE'：运行中。
        :type State: str
        :param QosLevel: 实例服务质量，’PT’：白金，'AU'：金，'AG'：银。
        :type QosLevel: str
        :param InstanceChargeType: 付费类型，PREPAID为预付费，POSTPAID为后付费。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceChargeType: str
        :param BandwidthLimitType: 限速类型，INTER_REGION_LIMIT为地域间限速；OUTER_REGION_LIMIT为地域出口限速。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthLimitType: str
        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None
        self.InstanceCount = None
        self.CreateTime = None
        self.State = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.InstanceCount = params.get("InstanceCount")
        self.CreateTime = params.get("CreateTime")
        self.State = params.get("State")
        self.QosLevel = params.get("QosLevel")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.BandwidthLimitType = params.get("BandwidthLimitType")


class CcnAttachedInstance(AbstractModel):
    """云联网（CCN）关联实例（Instance）对象

    """

    def __init__(self):
        """
        :param CcnId: 云联网实例ID。
        :type CcnId: str
        :param InstanceType: 关联实例类型：
<li>`VPC`：私有网络</li>
<li>`DIRECTCONNECT`：专线网关</li>
<li>`BMVPC`：黑石私有网络</li>
        :type InstanceType: str
        :param InstanceId: 关联实例ID。
        :type InstanceId: str
        :param InstanceName: 关联实例名称。
        :type InstanceName: str
        :param InstanceRegion: 关联实例所属大区，例如：ap-guangzhou。
        :type InstanceRegion: str
        :param InstanceUin: 关联实例所属UIN（根账号）。
        :type InstanceUin: str
        :param CidrBlock: 关联实例CIDR。
        :type CidrBlock: list of str
        :param State: 关联实例状态：
<li>`PENDING`：申请中</li>
<li>`ACTIVE`：已连接</li>
<li>`EXPIRED`：已过期</li>
<li>`REJECTED`：已拒绝</li>
<li>`DELETED`：已删除</li>
<li>`FAILED`：失败的（2小时后将异步强制解关联）</li>
<li>`ATTACHING`：关联中</li>
<li>`DETACHING`：解关联中</li>
<li>`DETACHFAILED`：解关联失败（2小时后将异步强制解关联）</li>
        :type State: str
        :param AttachedTime: 关联时间。
        :type AttachedTime: str
        :param CcnUin: 云联网所属UIN（根账号）。
        :type CcnUin: str
        """
        self.CcnId = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.InstanceUin = None
        self.CidrBlock = None
        self.State = None
        self.AttachedTime = None
        self.CcnUin = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceUin = params.get("InstanceUin")
        self.CidrBlock = params.get("CidrBlock")
        self.State = params.get("State")
        self.AttachedTime = params.get("AttachedTime")
        self.CcnUin = params.get("CcnUin")


class CcnInstance(AbstractModel):
    """云联网（CCN）关联实例（Instance）对象。

    """

    def __init__(self):
        """
        :param InstanceId: 关联实例ID。
        :type InstanceId: str
        :param InstanceRegion: 关联实例ID所属大区，例如：ap-guangzhou。
        :type InstanceRegion: str
        :param InstanceType: 关联实例类型，可选值：
<li>`VPC`：私有网络</li>
<li>`DIRECTCONNECT`：专线网关</li>
<li>`BMVPC`：黑石私有网络</li>
        :type InstanceType: str
        """
        self.InstanceId = None
        self.InstanceRegion = None
        self.InstanceType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceType = params.get("InstanceType")


class CcnRegionBandwidthLimit(AbstractModel):
    """云联网（CCN）地域出带宽上限

    """

    def __init__(self):
        """
        :param Region: 地域，例如：ap-guangzhou
        :type Region: str
        :param BandwidthLimit: 出带宽上限，单位：Mbps
        :type BandwidthLimit: int
        :param IsBm: 是否黑石地域，默认`false`。
        :type IsBm: bool
        :param DstRegion: 目的地域，例如：ap-shanghai
注意：此字段可能返回 null，表示取不到有效值。
        :type DstRegion: str
        :param DstIsBm: 目的地域是否为黑石地域，默认`false`。
        :type DstIsBm: bool
        """
        self.Region = None
        self.BandwidthLimit = None
        self.IsBm = None
        self.DstRegion = None
        self.DstIsBm = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        self.BandwidthLimit = params.get("BandwidthLimit")
        self.IsBm = params.get("IsBm")
        self.DstRegion = params.get("DstRegion")
        self.DstIsBm = params.get("DstIsBm")


class CcnRoute(AbstractModel):
    """CCN路由策略对象

    """

    def __init__(self):
        """
        :param RouteId: 路由策略ID
        :type RouteId: str
        :param DestinationCidrBlock: 目的端
        :type DestinationCidrBlock: str
        :param InstanceType: 下一跳类型（关联实例类型），所有类型：VPC、DIRECTCONNECT
        :type InstanceType: str
        :param InstanceId: 下一跳（关联实例）
        :type InstanceId: str
        :param InstanceName: 下一跳名称（关联实例名称）
        :type InstanceName: str
        :param InstanceRegion: 下一跳所属地域（关联实例所属地域）
        :type InstanceRegion: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        :param Enabled: 路由是否启用
        :type Enabled: bool
        :param InstanceUin: 关联实例所属UIN（根账号）
        :type InstanceUin: str
        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.UpdateTime = None
        self.Enabled = None
        self.InstanceUin = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceRegion = params.get("InstanceRegion")
        self.UpdateTime = params.get("UpdateTime")
        self.Enabled = params.get("Enabled")
        self.InstanceUin = params.get("InstanceUin")


class ClassicLinkInstance(AbstractModel):
    """私有网络和基础网络互通设备

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID
        :type VpcId: str
        :param InstanceId: 云服务器实例唯一ID
        :type InstanceId: str
        """
        self.VpcId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceId = params.get("InstanceId")


class CreateAddressTemplateGroupRequest(AbstractModel):
    """CreateAddressTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP地址模版集合名称。
        :type AddressTemplateGroupName: str
        :param AddressTemplateIds: IP地址模版实例ID，例如：ipm-mdunqeb6。
        :type AddressTemplateIds: list of str
        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")


class CreateAddressTemplateGroupResponse(AbstractModel):
    """CreateAddressTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroup: IP地址模板集合对象。
        :type AddressTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AddressTemplateGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplateGroup") is not None:
            self.AddressTemplateGroup = AddressTemplateGroup()
            self.AddressTemplateGroup._deserialize(params.get("AddressTemplateGroup"))
        self.RequestId = params.get("RequestId")


class CreateAddressTemplateRequest(AbstractModel):
    """CreateAddressTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP地址模版名称
        :type AddressTemplateName: str
        :param Addresses: 地址信息，支持 IP、CIDR、IP 范围。
        :type Addresses: list of str
        """
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")


class CreateAddressTemplateResponse(AbstractModel):
    """CreateAddressTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplate: IP地址模板对象。
        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AddressTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplate()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.RequestId = params.get("RequestId")


class CreateBandwidthPackageRequest(AbstractModel):
    """CreateBandwidthPackage请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkType: 带宽包类型，包括'BGP'，'SINGLEISP'，'ANYCAST'
        :type NetworkType: str
        :param ChargeType: 带宽包计费类型，包括‘TOP5_POSTPAID_BY_MONTH’，‘PERCENT95_POSTPAID_BY_MONTH’
        :type ChargeType: str
        :param BandwidthPackageName: 带宽包名字
        :type BandwidthPackageName: str
        :param BandwidthPackageCount: 带宽包数量(非上移账户只能填1)
        :type BandwidthPackageCount: int
        :param InternetMaxBandwidth: 带宽包限速大小。单位：Mbps，-1表示不限速。
        :type InternetMaxBandwidth: int
        """
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.BandwidthPackageCount = None
        self.InternetMaxBandwidth = None


    def _deserialize(self, params):
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.BandwidthPackageCount = params.get("BandwidthPackageCount")
        self.InternetMaxBandwidth = params.get("InternetMaxBandwidth")


class CreateBandwidthPackageResponse(AbstractModel):
    """CreateBandwidthPackage返回参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包Id
        :type BandwidthPackageId: str
        :param BandwidthPackageIds: 带宽包Ids(申请数量大于1时有效)
        :type BandwidthPackageIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BandwidthPackageId = None
        self.BandwidthPackageIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageIds = params.get("BandwidthPackageIds")
        self.RequestId = params.get("RequestId")


class CreateCcnRequest(AbstractModel):
    """CreateCcn请求参数结构体

    """

    def __init__(self):
        """
        :param CcnName: CCN名称，最大长度不能超过60个字节。
        :type CcnName: str
        :param CcnDescription: CCN描述信息，最大长度不能超过100个字节。
        :type CcnDescription: str
        :param QosLevel: CCN服务质量，'PT'：白金，'AU'：金，'AG'：银，默认为‘AU’。
        :type QosLevel: str
        """
        self.CcnName = None
        self.CcnDescription = None
        self.QosLevel = None


    def _deserialize(self, params):
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.QosLevel = params.get("QosLevel")


class CreateCcnResponse(AbstractModel):
    """CreateCcn返回参数结构体

    """

    def __init__(self):
        """
        :param Ccn: 云联网（CCN）对象。
        :type Ccn: :class:`tencentcloud.vpc.v20170312.models.CCN`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ccn = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ccn") is not None:
            self.Ccn = CCN()
            self.Ccn._deserialize(params.get("Ccn"))
        self.RequestId = params.get("RequestId")


class CreateCustomerGatewayRequest(AbstractModel):
    """CreateCustomerGateway请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayName: 对端网关名称，可任意命名，但不得超过60个字符。
        :type CustomerGatewayName: str
        :param IpAddress: 对端网关公网IP。
        :type IpAddress: str
        """
        self.CustomerGatewayName = None
        self.IpAddress = None


    def _deserialize(self, params):
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGateway: 对端网关对象
        :type CustomerGateway: :class:`tencentcloud.vpc.v20170312.models.CustomerGateway`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGateway") is not None:
            self.CustomerGateway = CustomerGateway()
            self.CustomerGateway._deserialize(params.get("CustomerGateway"))
        self.RequestId = params.get("RequestId")


class CreateDefaultVpcRequest(AbstractModel):
    """CreateDefaultVpc请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 子网所在的可用区ID，不指定将随机选择可用区
        :type Zone: str
        :param Force: 是否强制返回默认VPC
        :type Force: bool
        """
        self.Zone = None
        self.Force = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Force = params.get("Force")


class CreateDefaultVpcResponse(AbstractModel):
    """CreateDefaultVpc返回参数结构体

    """

    def __init__(self):
        """
        :param Vpc: 默认VPC和子网ID
        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.DefaultVpcSubnet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = DefaultVpcSubnet()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：dcg-prpqlmg1
        :type DirectConnectGatewayId: str
        :param Routes: 需要连通的IDC网段列表
        :type Routes: list of DirectConnectGatewayCcnRoute
        """
        self.DirectConnectGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.Routes.append(obj)


class CreateDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayRequest(AbstractModel):
    """CreateDirectConnectGateway请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayName: 专线网关名称
        :type DirectConnectGatewayName: str
        :param NetworkType: 关联网络类型，可选值：
<li>VPC - 私有网络</li>
<li>CCN - 云联网</li>
        :type NetworkType: str
        :param NetworkInstanceId: <li>NetworkType 为 VPC 时，这里传值为私有网络实例ID</li>
<li>NetworkType 为 CCN 时，这里传值为云联网实例ID</li>
        :type NetworkInstanceId: str
        :param GatewayType: 网关类型，可选值：
<li>NORMAL - （默认）标准型，注：云联网只支持标准型</li>
<li>NAT - NAT型</li>NAT类型支持网络地址转换配置，类型确定后不能修改；一个私有网络可以创建一个NAT类型的专线网关和一个非NAT类型的专线网关
        :type GatewayType: str
        """
        self.DirectConnectGatewayName = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")


class CreateDirectConnectGatewayResponse(AbstractModel):
    """CreateDirectConnectGateway返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGateway: 专线网关对象。
        :type DirectConnectGateway: :class:`tencentcloud.vpc.v20170312.models.DirectConnectGateway`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DirectConnectGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectGateway") is not None:
            self.DirectConnectGateway = DirectConnectGateway()
            self.DirectConnectGateway._deserialize(params.get("DirectConnectGateway"))
        self.RequestId = params.get("RequestId")


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `HAVIP`所在私有网络`ID`。
        :type VpcId: str
        :param SubnetId: `HAVIP`所在子网`ID`。
        :type SubnetId: str
        :param HaVipName: `HAVIP`名称。
        :type HaVipName: str
        :param Vip: 指定虚拟IP地址，必须在`VPC`网段内且未被占用。不指定则自动分配。
        :type Vip: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.HaVipName = None
        self.Vip = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.HaVipName = params.get("HaVipName")
        self.Vip = params.get("Vip")


class CreateHaVipResponse(AbstractModel):
    """CreateHaVip返回参数结构体

    """

    def __init__(self):
        """
        :param HaVip: `HAVIP`对象。
        :type HaVip: :class:`tencentcloud.vpc.v20170312.models.HaVip`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.HaVip = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("HaVip") is not None:
            self.HaVip = HaVip()
            self.HaVip._deserialize(params.get("HaVip"))
        self.RequestId = params.get("RequestId")


class CreateIp6TranslatorsRequest(AbstractModel):
    """CreateIp6Translators请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorName: 转换实例名称
        :type Ip6TranslatorName: str
        :param Ip6TranslatorCount: 创建转换实例数量，默认是1个
        :type Ip6TranslatorCount: int
        :param Ip6InternetServiceProvider: 转换实例运营商属性，可取"CMCC","CTCC","CUCC","BGP"
        :type Ip6InternetServiceProvider: str
        """
        self.Ip6TranslatorName = None
        self.Ip6TranslatorCount = None
        self.Ip6InternetServiceProvider = None


    def _deserialize(self, params):
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")
        self.Ip6TranslatorCount = params.get("Ip6TranslatorCount")
        self.Ip6InternetServiceProvider = params.get("Ip6InternetServiceProvider")


class CreateIp6TranslatorsResponse(AbstractModel):
    """CreateIp6Translators返回参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorSet: 转换实例的唯一ID数组，形如"ip6-xxxxxxxx"
        :type Ip6TranslatorSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ip6TranslatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip6TranslatorSet = params.get("Ip6TranslatorSet")
        self.RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。
        :type NetworkInterfaceName: str
        :param SubnetId: 弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。
        :type SubnetId: str
        :param NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。
        :type NetworkInterfaceDescription: str
        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。
        :type SecondaryPrivateIpAddressCount: int
        :param SecurityGroupIds: 指定绑定的安全组，例如：['sg-1dd51d']。
        :type SecurityGroupIds: list of str
        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class CreateNetworkInterfaceResponse(AbstractModel):
    """CreateNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterface: 弹性网卡实例。
        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param RouteTableName: 路由表名称，最大长度不能超过60个字节。
        :type RouteTableName: str
        """
        self.VpcId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableName = params.get("RouteTableName")


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RouteTable: 路由表对象。
        :type RouteTable: :class:`tencentcloud.vpc.v20170312.models.RouteTable`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param RouteTableId: 路由表实例ID。
        :type RouteTableId: str
        :param Routes: 路由策略对象。
        :type Routes: list of Route
        """
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


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupPoliciesRequest(AbstractModel):
    """CreateSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全组规则集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class CreateSecurityGroupPoliciesResponse(AbstractModel):
    """CreateSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupRequest(AbstractModel):
    """CreateSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。
        :type GroupName: str
        :param GroupDescription: 安全组备注，最多100个字符。
        :type GroupDescription: str
        :param ProjectId: 项目id，默认0。可在qcloud控制台项目管理页面查询到。
        :type ProjectId: str
        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")


class CreateSecurityGroupResponse(AbstractModel):
    """CreateSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全组对象。
        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateServiceTemplateGroupRequest(AbstractModel):
    """CreateServiceTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupName: 协议端口模板集合名称
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIds: 协议端口模板实例ID，例如：ppm-4dw6agho。
        :type ServiceTemplateIds: list of str
        """
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")


class CreateServiceTemplateGroupResponse(AbstractModel):
    """CreateServiceTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroup: 协议端口模板集合对象。
        :type ServiceTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateGroup`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceTemplateGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceTemplateGroup") is not None:
            self.ServiceTemplateGroup = ServiceTemplateGroup()
            self.ServiceTemplateGroup._deserialize(params.get("ServiceTemplateGroup"))
        self.RequestId = params.get("RequestId")


class CreateServiceTemplateRequest(AbstractModel):
    """CreateServiceTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateName: 协议端口模板名称
        :type ServiceTemplateName: str
        :param Services: 支持单个端口、多个端口、连续端口及所有端口，协议支持：TCP、UDP、ICMP、GRE 协议。
        :type Services: list of str
        """
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")


class CreateServiceTemplateResponse(AbstractModel):
    """CreateServiceTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplate: 协议端口模板对象。
        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplate`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ServiceTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplate()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.RequestId = params.get("RequestId")


class CreateSubnetRequest(AbstractModel):
    """CreateSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param SubnetName: 子网名称，最大长度不能超过60个字节。
        :type SubnetName: str
        :param CidrBlock: 子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。
        :type CidrBlock: str
        :param Zone: 子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。
        :type Zone: str
        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")


class CreateSubnetResponse(AbstractModel):
    """CreateSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param Subnet: 子网对象。
        :type Subnet: :class:`tencentcloud.vpc.v20170312.models.Subnet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Subnet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Subnet") is not None:
            self.Subnet = Subnet()
            self.Subnet._deserialize(params.get("Subnet"))
        self.RequestId = params.get("RequestId")


class CreateSubnetsRequest(AbstractModel):
    """CreateSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`
        :type VpcId: str
        :param Subnets: 子网对象列表。
        :type Subnets: list of SubnetInput
        """
        self.VpcId = None
        self.Subnets = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Subnets") is not None:
            self.Subnets = []
            for item in params.get("Subnets"):
                obj = SubnetInput()
                obj._deserialize(item)
                self.Subnets.append(obj)


class CreateSubnetsResponse(AbstractModel):
    """CreateSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param SubnetSet: 新创建的子网列表。
        :type SubnetSet: list of Subnet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubnetSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcName: vpc名称，最大长度不能超过60个字节。
        :type VpcName: str
        :param CidrBlock: vpc的cidr，只能为10.0.0.0/16，172.16.0.0/12，192.168.0.0/16这三个内网网段内。
        :type CidrBlock: str
        :param EnableMulticast: 是否开启组播。true: 开启, false: 不开启。
        :type EnableMulticast: str
        :param DnsServers: DNS地址，最多支持4个
        :type DnsServers: list of str
        :param DomainName: 域名
        :type DomainName: str
        """
        self.VpcName = None
        self.CidrBlock = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回参数结构体

    """

    def __init__(self):
        """
        :param Vpc: Vpc对象。
        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.Vpc`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = Vpc()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateVpnConnectionRequest(AbstractModel):
    """CreateVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param CustomerGatewayId: 对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
        :type CustomerGatewayId: str
        :param VpnConnectionName: 通道名称，可任意命名，但不得超过60个字符。
        :type VpnConnectionName: str
        :param PreShareKey: 预共享密钥。
        :type PreShareKey: str
        :param SecurityPolicyDatabases: SPD策略组，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec配置，腾讯云提供IPSec安全会话设置
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
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


class CreateVpnConnectionResponse(AbstractModel):
    """CreateVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param VpnConnection: 通道实例对象。
        :type VpnConnection: :class:`tencentcloud.vpc.v20170312.models.VpnConnection`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpnConnection = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnConnection") is not None:
            self.VpnConnection = VpnConnection()
            self.VpnConnection._deserialize(params.get("VpnConnection"))
        self.RequestId = params.get("RequestId")


class CreateVpnGatewayRequest(AbstractModel):
    """CreateVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param VpnGatewayName: VPN网关名称，最大长度不能超过60个字节。
        :type VpnGatewayName: str
        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps
        :type InternetMaxBandwidthOut: int
        :param InstanceChargeType: VPN网关计费模式，PREPAID：表示预付费，即包年包月，POSTPAID_BY_HOUR：表示后付费，即按量计费。默认：POSTPAID_BY_HOUR，如果指定预付费模式，参数InstanceChargePrepaid必填。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        :param Zone: 可用区，如：ap-guangzhou-2。
        :type Zone: str
        """
        self.VpcId = None
        self.VpnGatewayName = None
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.Zone = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.Zone = params.get("Zone")


class CreateVpnGatewayResponse(AbstractModel):
    """CreateVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param VpnGateway: VPN网关对象
        :type VpnGateway: :class:`tencentcloud.vpc.v20170312.models.VpnGateway`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpnGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnGateway") is not None:
            self.VpnGateway = VpnGateway()
            self.VpnGateway._deserialize(params.get("VpnGateway"))
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
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreatedTime = params.get("CreatedTime")


class CustomerGatewayVendor(AbstractModel):
    """对端网关厂商信息对象。

    """

    def __init__(self):
        """
        :param Platform: 平台。
        :type Platform: str
        :param SoftwareVersion: 软件版本。
        :type SoftwareVersion: str
        :param VendorName: 供应商名称。
        :type VendorName: str
        """
        self.Platform = None
        self.SoftwareVersion = None
        self.VendorName = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.SoftwareVersion = params.get("SoftwareVersion")
        self.VendorName = params.get("VendorName")


class DefaultVpcSubnet(AbstractModel):
    """默认VPC和子网

    """

    def __init__(self):
        """
        :param VpcId: 默认VpcId
        :type VpcId: str
        :param SubnetId: 默认SubnetId
        :type SubnetId: str
        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")


class DeleteAddressTemplateGroupRequest(AbstractModel):
    """DeleteAddressTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP地址模板集合实例ID，例如：ipmg-90cex8mq。
        :type AddressTemplateGroupId: str
        """
        self.AddressTemplateGroupId = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")


class DeleteAddressTemplateGroupResponse(AbstractModel):
    """DeleteAddressTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAddressTemplateRequest(AbstractModel):
    """DeleteAddressTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP地址模板实例ID，例如：ipm-09o5m8kc。
        :type AddressTemplateId: str
        """
        self.AddressTemplateId = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")


class DeleteAddressTemplateResponse(AbstractModel):
    """DeleteAddressTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBandwidthPackageRequest(AbstractModel):
    """DeleteBandwidthPackage请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 待删除带宽包bwpId
        :type BandwidthPackageId: str
        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")


class DeleteBandwidthPackageResponse(AbstractModel):
    """DeleteBandwidthPackage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcnRequest(AbstractModel):
    """DeleteCcn请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")


class DeleteCcnResponse(AbstractModel):
    """DeleteCcn返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
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


class DeleteDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：dcg-prpqlmg1
        :type DirectConnectGatewayId: str
        :param RouteIds: 路由ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        """
        self.DirectConnectGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteIds = params.get("RouteIds")


class DeleteDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayRequest(AbstractModel):
    """DeleteDirectConnectGateway请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关唯一`ID`，形如：`dcg-9o233uri`。
        :type DirectConnectGatewayId: str
        """
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")


class DeleteDirectConnectGatewayResponse(AbstractModel):
    """DeleteDirectConnectGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。
        :type HaVipId: str
        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")


class DeleteHaVipResponse(AbstractModel):
    """DeleteHaVip返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteIp6TranslatorsRequest(AbstractModel):
    """DeleteIp6Translators请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: 待释放的IPV6转换实例的唯一ID，形如‘ip6-xxxxxxxx’
        :type Ip6TranslatorIds: list of str
        """
        self.Ip6TranslatorIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")


class DeleteIp6TranslatorsResponse(AbstractModel):
    """DeleteIp6Translators返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkInterfaceRequest(AbstractModel):
    """DeleteNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        """
        self.NetworkInterfaceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")


class DeleteNetworkInterfaceResponse(AbstractModel):
    """DeleteNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRouteTableRequest(AbstractModel):
    """DeleteRouteTable请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        """
        self.RouteTableId = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")


class DeleteRouteTableResponse(AbstractModel):
    """DeleteRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRoutesRequest(AbstractModel):
    """DeleteRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID。
        :type RouteTableId: str
        :param Routes: 路由策略对象。
        :type Routes: list of Route
        """
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


class DeleteRoutesResponse(AbstractModel):
    """DeleteRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全组规则集合。一个请求中只能删除单个方向的一条或多条规则。支持指定索引（PolicyIndex） 匹配删除和安全组规则匹配删除两种方式，一个请求中只能使用一种匹配方式。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class DeleteSecurityGroupPoliciesResponse(AbstractModel):
    """DeleteSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupRequest(AbstractModel):
    """DeleteSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")


class DeleteSecurityGroupResponse(AbstractModel):
    """DeleteSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateGroupRequest(AbstractModel):
    """DeleteServiceTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 协议端口模板集合实例ID，例如：ppmg-n17uxvve。
        :type ServiceTemplateGroupId: str
        """
        self.ServiceTemplateGroupId = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")


class DeleteServiceTemplateGroupResponse(AbstractModel):
    """DeleteServiceTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateRequest(AbstractModel):
    """DeleteServiceTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 协议端口模板实例ID，例如：ppm-e6dy460g。
        :type ServiceTemplateId: str
        """
        self.ServiceTemplateId = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")


class DeleteServiceTemplateResponse(AbstractModel):
    """DeleteServiceTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSubnetRequest(AbstractModel):
    """DeleteSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。
        :type SubnetId: str
        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")


class DeleteSubnetResponse(AbstractModel):
    """DeleteSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccountAttributesRequest(AbstractModel):
    """DescribeAccountAttributes请求参数结构体

    """


class DescribeAccountAttributesResponse(AbstractModel):
    """DescribeAccountAttributes返回参数结构体

    """

    def __init__(self):
        """
        :param AccountAttributeSet: 用户账号属性对象
        :type AccountAttributeSet: list of AccountAttribute
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccountAttributeSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccountAttributeSet") is not None:
            self.AccountAttributeSet = []
            for item in params.get("AccountAttributeSet"):
                obj = AccountAttribute()
                obj._deserialize(item)
                self.AccountAttributeSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressQuotaRequest(AbstractModel):
    """DescribeAddressQuota请求参数结构体

    """


class DescribeAddressQuotaResponse(AbstractModel):
    """DescribeAddressQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 账户 EIP 配额信息。
        :type QuotaSet: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressTemplateGroupsRequest(AbstractModel):
    """DescribeAddressTemplateGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>address-template-group-name - String - （过滤条件）IP地址模板集合名称。</li>
<li>address-template-group-id - String - （过滤条件）IP地址模板实集合例ID，例如：ipmg-mdunqeb6。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: str
        """
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


class DescribeAddressTemplateGroupsResponse(AbstractModel):
    """DescribeAddressTemplateGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param AddressTemplateGroupSet: IP地址模板。
        :type AddressTemplateGroupSet: list of AddressTemplateGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressTemplateGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressTemplateGroupSet") is not None:
            self.AddressTemplateGroupSet = []
            for item in params.get("AddressTemplateGroupSet"):
                obj = AddressTemplateGroup()
                obj._deserialize(item)
                self.AddressTemplateGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressTemplatesRequest(AbstractModel):
    """DescribeAddressTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>address-template-name - String - （过滤条件）IP地址模板名称。</li>
<li>address-template-id - String - （过滤条件）IP地址模板实例ID，例如：ipm-mdunqeb6。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: str
        """
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


class DescribeAddressTemplatesResponse(AbstractModel):
    """DescribeAddressTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param AddressTemplateSet: IP地址模版。
        :type AddressTemplateSet: list of AddressTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AddressTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AddressTemplateSet") is not None:
            self.AddressTemplateSet = []
            for item in params.get("AddressTemplateSet"):
                obj = AddressTemplate()
                obj._deserialize(item)
                self.AddressTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAddressesRequest(AbstractModel):
    """DescribeAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param AddressIds: 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。参数不支持同时指定`AddressIds`和`Filters`。
        :type AddressIds: list of str
        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。详细的过滤条件如下：
<li> address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。</li>
<li> address-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。</li>
<li> address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。</li>
<li> address-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。取值范围：[详见EIP状态列表](https://cloud.tencent.com/document/api/213/9452#eip_state)。</li>
<li> instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。</li>
<li> private-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。</li>
<li> network-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。</li>
<li> is-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。
        :type Limit: int
        """
        self.AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeAddressesResponse(AbstractModel):
    """DescribeAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的 EIP 数量。
        :type TotalCount: int
        :param AddressSet: EIP 详细信息列表。
        :type AddressSet: list of Address
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeBandwidthPackageQuotaRequest(AbstractModel):
    """DescribeBandwidthPackageQuota请求参数结构体

    """


class DescribeBandwidthPackageQuotaResponse(AbstractModel):
    """DescribeBandwidthPackageQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 带宽包配额数据结构
        :type QuotaSet: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackagesRequest(AbstractModel):
    """DescribeBandwidthPackages请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageIds: 带宽包Id，支持批量
        :type BandwidthPackageIds: list of str
        :param Filters: 每次请求的`Filters`的上限为10。参数不支持同时指定`BandwidthPackageIds`和`Filters`。详细的过滤条件如下：
<li> bandwidth-package_id - String - 是否必填：否 - （过滤条件）按照带宽包的唯一标识ID过滤。</li>
<li> bandwidth-package-name - String - 是否必填：否 - （过滤条件）按照 带宽包名称过滤。不支持模糊过滤。</li>
<li> network-type - String - 是否必填：否 - （过滤条件）按照带宽包的类型过滤。类型包括'BGP','SINGLEISP'和'ANYCAST'。</li>
<li> charge-type - String - 是否必填：否 - （过滤条件）按照带宽包的计费类型过滤。计费类型包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'</li>
<li> resource.resource-type - String - 是否必填：否 - （过滤条件）按照带宽包资源类型过滤。资源类型包括'Address'和'LoadBalance'</li>
<li> resource.resource-id - String - 是否必填：否 - （过滤条件）按照带宽包资源Id过滤。资源Id形如'eip-xxxx','lb-xxxx'</li>
<li> resource.address-ip - String - 是否必填：否 - （过滤条件）按照带宽包资源Ip过滤。</li>
        :type Filters: list of Filter
        :param Offset: 查询带宽包偏移量
        :type Offset: int
        :param Limit: 查询带宽包数量限制
        :type Limit: int
        """
        self.BandwidthPackageIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BandwidthPackageIds = params.get("BandwidthPackageIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeBandwidthPackagesResponse(AbstractModel):
    """DescribeBandwidthPackages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的带宽包数量
        :type TotalCount: int
        :param BandwidthPackageSet: 描述带宽包详细信息
        :type BandwidthPackageSet: list of BandwidthPackage
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.BandwidthPackageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("BandwidthPackageSet") is not None:
            self.BandwidthPackageSet = []
            for item in params.get("BandwidthPackageSet"):
                obj = BandwidthPackage()
                obj._deserialize(item)
                self.BandwidthPackageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnAttachedInstancesRequest(AbstractModel):
    """DescribeCcnAttachedInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        :param Filters: 过滤条件：
<li>ccn-id - String -（过滤条件）CCN实例ID。</li>
<li>instance-type - String -（过滤条件）关联实例类型。</li>
<li>instance-region - String -（过滤条件）关联实例所属地域。</li>
<li>instance-id - String -（过滤条件）关联实例实例ID。</li>
        :type Filters: list of Filter
        :param CcnId: 云联网实例ID
        :type CcnId: str
        :param OrderField: 排序字段。支持：`CcnId` `InstanceType` `InstanceId` `InstanceName` `InstanceRegion` `AttachedTime` `State`。
        :type OrderField: str
        :param OrderDirection: 排序方法。顺序：`ASC`，倒序：`DESC`。
        :type OrderDirection: str
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.CcnId = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.CcnId = params.get("CcnId")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param InstanceSet: 关联实例列表。
        :type InstanceSet: list of CcnAttachedInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CcnAttachedInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnRegionBandwidthLimitsRequest(AbstractModel):
    """DescribeCcnRegionBandwidthLimits请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")


class DescribeCcnRegionBandwidthLimitsResponse(AbstractModel):
    """DescribeCcnRegionBandwidthLimits返回参数结构体

    """

    def __init__(self):
        """
        :param CcnRegionBandwidthLimitSet: 云联网（CCN）各地域出带宽上限
        :type CcnRegionBandwidthLimitSet: list of CcnRegionBandwidthLimit
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CcnRegionBandwidthLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnRegionBandwidthLimitSet") is not None:
            self.CcnRegionBandwidthLimitSet = []
            for item in params.get("CcnRegionBandwidthLimitSet"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnRoutesRequest(AbstractModel):
    """DescribeCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID，形如：ccn-gree226l。
        :type CcnId: str
        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定RouteIds和Filters。
<li>route-id - String -（过滤条件）路由策略ID。</li>
<li>cidr-block - String -（过滤条件）目的端。</li>
<li>instance-type - String -（过滤条件）下一跳类型。</li>
<li>instance-region - String -（过滤条件）下一跳所属地域。</li>
<li>instance-id - String -（过滤条件）下一跳实例ID。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.CcnId = None
        self.RouteIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCcnRoutesResponse(AbstractModel):
    """DescribeCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param RouteSet: CCN路由策略对象。
        :type RouteSet: list of CcnRoute
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = CcnRoute()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcnsRequest(AbstractModel):
    """DescribeCcns请求参数结构体

    """

    def __init__(self):
        """
        :param CcnIds: CCN实例ID。形如：ccn-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定CcnIds和Filters。
        :type CcnIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定CcnIds和Filters。
<li>ccn-id - String - （过滤条件）CCN唯一ID，形如：vpc-f49l6u0z。</li>
<li>ccn-name - String - （过滤条件）CCN名称。</li>
<li>ccn-description - String - （过滤条件）CCN描述。</li>
<li>state - String - （过滤条件）实例状态， 'ISOLATED': 隔离中（欠费停服），'AVAILABLE'：运行中。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.CcnIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CcnIds = params.get("CcnIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeCcnsResponse(AbstractModel):
    """DescribeCcns返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param CcnSet: CCN对象。
        :type CcnSet: list of CCN
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.CcnSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("CcnSet") is not None:
            self.CcnSet = []
            for item in params.get("CcnSet"):
                obj = CCN()
                obj._deserialize(item)
                self.CcnSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeClassicLinkInstancesRequest(AbstractModel):
    """DescribeClassicLinkInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>vpc-id - String - （过滤条件）VPC实例ID。</li>
<li>vm-ip - String - （过滤条件）基础网络云主机IP。</li>
        :type Filters: list of FilterObject
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 返回数量
        :type Limit: str
        """
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterObject()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeClassicLinkInstancesResponse(AbstractModel):
    """DescribeClassicLinkInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param ClassicLinkInstanceSet: 私有网络和基础网络互通设备。
        :type ClassicLinkInstanceSet: list of ClassicLinkInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ClassicLinkInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ClassicLinkInstanceSet") is not None:
            self.ClassicLinkInstanceSet = []
            for item in params.get("ClassicLinkInstanceSet"):
                obj = ClassicLinkInstance()
                obj._deserialize(item)
                self.ClassicLinkInstanceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewayVendorsRequest(AbstractModel):
    """DescribeCustomerGatewayVendors请求参数结构体

    """


class DescribeCustomerGatewayVendorsResponse(AbstractModel):
    """DescribeCustomerGatewayVendors返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayVendorSet: 对端网关厂商信息对象。
        :type CustomerGatewayVendorSet: list of CustomerGatewayVendor
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewayVendorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGatewayVendorSet") is not None:
            self.CustomerGatewayVendorSet = []
            for item in params.get("CustomerGatewayVendorSet"):
                obj = CustomerGatewayVendor()
                obj._deserialize(item)
                self.CustomerGatewayVendorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewaysRequest(AbstractModel):
    """DescribeCustomerGateways请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayIds: 对端网关ID，例如：cgw-2wqq41m9。每次请求的实例的上限为100。参数不支持同时指定CustomerGatewayIds和Filters。
        :type CustomerGatewayIds: list of str
        :param Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定CustomerGatewayIds和Filters。
<li>customer-gateway-id - String - （过滤条件）用户网关唯一ID形如：`cgw-mgp33pll`。</li>
<li>customer-gateway-name - String - （过滤条件）用户网关名称形如：`test-cgw`。</li>
<li>ip-address - String - （过滤条件）公网地址形如：`58.211.1.12`。</li>
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


class DescribeDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：`dcg-prpqlmg1`。
        :type DirectConnectGatewayId: str
        :param CcnRouteType: 云联网路由学习类型，可选值：
<li>`BGP` - 自动学习。</li>
<li>`STATIC` - 静态，即用户配置，默认值。</li>
        :type CcnRouteType: str
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回数量。
        :type Limit: int
        """
        self.DirectConnectGatewayId = None
        self.CcnRouteType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param RouteSet: 云联网路由（IDC网段）列表。
        :type RouteSet: list of DirectConnectGatewayCcnRoute
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectGatewaysRequest(AbstractModel):
    """DescribeDirectConnectGateways请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayIds: 专线网关唯一`ID`，形如：`dcg-9o233uri`。
        :type DirectConnectGatewayIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定`DirectConnectGatewayIds`和`Filters`。
<li>direct-connect-gateway-id - String - 专线网关唯一`ID`，形如：`dcg-9o233uri`。</li>
<li>direct-connect-gateway-name - String - 专线网关名称，默认模糊查询。</li>
<li>direct-connect-gateway-ip - String - 专线网关`IP`。</li>
<li>gateway-type - String - 网关类型，可选值：`NORMAL`（普通型）、`NAT`（NAT型）。</li>
<li>network-type- String - 网络类型，可选值：`VPC`（私有网络类型）、`CCN`（云联网类型）。</li>
<li>ccn-id - String - 专线网关所在云联网`ID`。</li>
<li>vpc-id - String - 专线网关所在私有网络`ID`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回数量。
        :type Limit: int
        """
        self.DirectConnectGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayIds = params.get("DirectConnectGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDirectConnectGatewaysResponse(AbstractModel):
    """DescribeDirectConnectGateways返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param DirectConnectGatewaySet: 专线网关对象数组。
        :type DirectConnectGatewaySet: list of DirectConnectGateway
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DirectConnectGatewaySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DirectConnectGatewaySet") is not None:
            self.DirectConnectGatewaySet = []
            for item in params.get("DirectConnectGatewaySet"):
                obj = DirectConnectGateway()
                obj._deserialize(item)
                self.DirectConnectGatewaySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeGatewayFlowMonitorDetailRequest(AbstractModel):
    """DescribeGatewayFlowMonitorDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TimePoint: 时间点。表示要查询这分钟内的明细。如：`2019-02-28 18:15:20`，将查询 `18:15` 这一分钟内的明细。
        :type TimePoint: str
        :param VpnId: VPN网关实例ID，形如：`vpn-ltjahce6`。
        :type VpnId: str
        :param DirectConnectGatewayId: 专线网关实例ID，形如：`dcg-ltjahce6`。
        :type DirectConnectGatewayId: str
        :param PeeringConnectionId: 对等连接实例ID，形如：`pcx-ltjahce6`。
        :type PeeringConnectionId: str
        :param NatId: NAT网关实例ID，形如：`nat-ltjahce6`。
        :type NatId: str
        :param Offset: 偏移量。
        :type Offset: int
        :param Limit: 返回数量。
        :type Limit: int
        :param OrderField: 排序字段。支持 `InPkg` `OutPkg` `InTraffic` `OutTraffic`。
        :type OrderField: str
        :param OrderDirection: 排序方法。顺序：`ASC`，倒序：`DESC`。
        :type OrderDirection: str
        """
        self.TimePoint = None
        self.VpnId = None
        self.DirectConnectGatewayId = None
        self.PeeringConnectionId = None
        self.NatId = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


    def _deserialize(self, params):
        self.TimePoint = params.get("TimePoint")
        self.VpnId = params.get("VpnId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.PeeringConnectionId = params.get("PeeringConnectionId")
        self.NatId = params.get("NatId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")


class DescribeGatewayFlowMonitorDetailResponse(AbstractModel):
    """DescribeGatewayFlowMonitorDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param GatewayFlowMonitorDetailSet: 网关流量监控明细。
        :type GatewayFlowMonitorDetailSet: list of GatewayFlowMonitorDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.GatewayFlowMonitorDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("GatewayFlowMonitorDetailSet") is not None:
            self.GatewayFlowMonitorDetailSet = []
            for item in params.get("GatewayFlowMonitorDetailSet"):
                obj = GatewayFlowMonitorDetail()
                obj._deserialize(item)
                self.GatewayFlowMonitorDetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipIds: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。
        :type HaVipIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定`HaVipIds`和`Filters`。
<li>havip-id - String - `HAVIP`唯一`ID`，形如：`havip-9o233uri`。</li>
<li>havip-name - String - `HAVIP`名称。</li>
<li>vpc-id - String - `HAVIP`所在私有网络`ID`。</li>
<li>subnet-id - String - `HAVIP`所在子网`ID`。</li>
<li>address-ip - String - `HAVIP`绑定的弹性公网`IP`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 返回数量
        :type Limit: int
        """
        self.HaVipIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


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


class DescribeHaVipsResponse(AbstractModel):
    """DescribeHaVips返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param HaVipSet: `HAVIP`对象数组。
        :type HaVipSet: list of HaVip
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeIp6TranslatorQuotaRequest(AbstractModel):
    """DescribeIp6TranslatorQuota请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: 待查询IPV6转换实例的唯一ID列表，形如ip6-xxxxxxxx
        :type Ip6TranslatorIds: list of str
        """
        self.Ip6TranslatorIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")


class DescribeIp6TranslatorQuotaResponse(AbstractModel):
    """DescribeIp6TranslatorQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 账户在指定地域的IPV6转换实例及规则配额信息
QUOTAID属性是TOTAL_TRANSLATOR_QUOTA，表示账户在指定地域的IPV6转换实例配额信息；QUOTAID属性是IPV6转转换实例唯一ID（形如ip6-xxxxxxxx），表示账户在该转换实例允许创建的转换规则配额
        :type QuotaSet: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.QuotaSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("QuotaSet") is not None:
            self.QuotaSet = []
            for item in params.get("QuotaSet"):
                obj = Quota()
                obj._deserialize(item)
                self.QuotaSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeIp6TranslatorsRequest(AbstractModel):
    """DescribeIp6Translators请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: IPV6转换实例唯一ID数组，形如ip6-xxxxxxxx
        :type Ip6TranslatorIds: list of str
        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`Ip6TranslatorIds`和`Filters`。详细的过滤条件如下：
<li> ip6-translator-id - String - 是否必填：否 - （过滤条件）按照IPV6转换实例的唯一ID过滤,形如ip6-xxxxxxx。</li>
<li> ip6-translator-vip6 - String - 是否必填：否 - （过滤条件）按照IPV6地址过滤。不支持模糊过滤。</li>
<li> ip6-translator-name - String - 是否必填：否 - （过滤条件）按照IPV6转换实例名称过滤。不支持模糊过滤。</li>
<li> ip6-translator-status - String - 是否必填：否 - （过滤条件）按照IPV6转换实例的状态过滤。状态取值范围为"CREATING","RUNNING","DELETING","MODIFYING"
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。
        :type Limit: int
        """
        self.Ip6TranslatorIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeIp6TranslatorsResponse(AbstractModel):
    """DescribeIp6Translators返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的IPV6转换实例数量。
        :type TotalCount: int
        :param Ip6TranslatorSet: 符合过滤条件的IPV6转换实例详细信息
        :type Ip6TranslatorSet: list of Ip6Translator
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Ip6TranslatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Ip6TranslatorSet") is not None:
            self.Ip6TranslatorSet = []
            for item in params.get("Ip6TranslatorSet"):
                obj = Ip6Translator()
                obj._deserialize(item)
                self.Ip6TranslatorSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。
        :type NetworkInterfaceIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。</li>
<li>network-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。</li>
<li>attachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ins-3nqpdn3i。</li>
<li>groups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。</li>
<li>network-interface-name - String - （过滤条件）网卡实例名称。</li>
<li>network-interface-description - String - （过滤条件）网卡实例描述。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self.NetworkInterfaceIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


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


class DescribeNetworkInterfacesResponse(AbstractModel):
    """DescribeNetworkInterfaces返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceSet: 实例详细信息列表。
        :type NetworkInterfaceSet: list of NetworkInterface
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.NetworkInterfaceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterfaceSet") is not None:
            self.NetworkInterfaceSet = []
            for item in params.get("NetworkInterfaceSet"):
                obj = NetworkInterface()
                obj._deserialize(item)
                self.NetworkInterfaceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRouteConflictsRequest(AbstractModel):
    """DescribeRouteConflicts请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param DestinationCidrBlocks: 要检查的与之冲突的目的端列表
        :type DestinationCidrBlocks: list of str
        """
        self.RouteTableId = None
        self.DestinationCidrBlocks = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationCidrBlocks = params.get("DestinationCidrBlocks")


class DescribeRouteConflictsResponse(AbstractModel):
    """DescribeRouteConflicts返回参数结构体

    """

    def __init__(self):
        """
        :param RouteConflictSet: 路由策略冲突列表
        :type RouteConflictSet: list of RouteConflict
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param RouteTableIds: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
<li>route-table-id - String - （过滤条件）路由表实例ID。</li>
<li>route-table-name - String - （过滤条件）路由表名称。</li>
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>association.main - String - （过滤条件）是否主路由表。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量。
        :type Offset: str
        :param Limit: 请求对象个数。
        :type Limit: str
        """
        self.RouteTableIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


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


class DescribeRouteTablesResponse(AbstractModel):
    """DescribeRouteTables返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RouteTableSet: 路由表对象。
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


class DescribeSecurityGroupAssociationStatisticsRequest(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupIds: list of str
        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class DescribeSecurityGroupAssociationStatisticsResponse(AbstractModel):
    """DescribeSecurityGroupAssociationStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupAssociationStatisticsSet: 安全组关联实例统计。
        :type SecurityGroupAssociationStatisticsSet: list of SecurityGroupAssociationStatistics
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeSecurityGroupPoliciesRequest(AbstractModel):
    """DescribeSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        """
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")


class DescribeSecurityGroupPoliciesResponse(AbstractModel):
    """DescribeSecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupPolicySet: 安全组规则集合。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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
        :param SecurityGroupIds: 安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。参数不支持同时指定SecurityGroupIds和Filters。
        :type SecurityGroupIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定SecurityGroupIds和Filters。
<li>project-id - Integer - （过滤条件）项目id。</li>
<li>security-group-name - String - （过滤条件）安全组名称。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量。
        :type Offset: str
        :param Limit: 返回数量。
        :type Limit: str
        """
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


class DescribeSecurityGroupsResponse(AbstractModel):
    """DescribeSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupSet: 安全组对象。
        :type SecurityGroupSet: list of SecurityGroup
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SecurityGroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupSet") is not None:
            self.SecurityGroupSet = []
            for item in params.get("SecurityGroupSet"):
                obj = SecurityGroup()
                obj._deserialize(item)
                self.SecurityGroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeServiceTemplateGroupsRequest(AbstractModel):
    """DescribeServiceTemplateGroups请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>service-template-group-name - String - （过滤条件）协议端口模板集合名称。</li>
<li>service-template-group-id - String - （过滤条件）协议端口模板集合实例ID，例如：ppmg-e6dy460g。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: str
        """
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


class DescribeServiceTemplateGroupsResponse(AbstractModel):
    """DescribeServiceTemplateGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param ServiceTemplateGroupSet: 协议端口模板集合。
        :type ServiceTemplateGroupSet: list of ServiceTemplateGroup
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceTemplateGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceTemplateGroupSet") is not None:
            self.ServiceTemplateGroupSet = []
            for item in params.get("ServiceTemplateGroupSet"):
                obj = ServiceTemplateGroup()
                obj._deserialize(item)
                self.ServiceTemplateGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeServiceTemplatesRequest(AbstractModel):
    """DescribeServiceTemplates请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li>service-template-name - String - （过滤条件）协议端口模板名称。</li>
<li>service-template-id - String - （过滤条件）协议端口模板实例ID，例如：ppm-e6dy460g。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。
        :type Offset: str
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: str
        """
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


class DescribeServiceTemplatesResponse(AbstractModel):
    """DescribeServiceTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param ServiceTemplateSet: 协议端口模板对象。
        :type ServiceTemplateSet: list of ServiceTemplate
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ServiceTemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ServiceTemplateSet") is not None:
            self.ServiceTemplateSet = []
            for item in params.get("ServiceTemplateSet"):
                obj = ServiceTemplate()
                obj._deserialize(item)
                self.ServiceTemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSubnetsRequest(AbstractModel):
    """DescribeSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetIds: 子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。
        :type SubnetIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
<li>subnet-id - String - （过滤条件）Subnet实例名称。</li>
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>cidr-block - String - （过滤条件）vpc的cidr。</li>
<li>is-default - Boolean - （过滤条件）是否是默认子网。</li>
<li>subnet-name - String - （过滤条件）子网名称。</li>
<li>zone - String - （过滤条件）可用区。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 返回数量
        :type Limit: str
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
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param SubnetSet: 子网对象。
        :type SubnetSet: list of Subnet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
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


class DescribeVpcPrivateIpAddressesRequest(AbstractModel):
    """DescribeVpcPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。
        :type VpcId: str
        :param PrivateIpAddresses: 内网`IP`地址列表，批量查询单次请求最多支持`10`个。
        :type PrivateIpAddresses: list of str
        """
        self.VpcId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")


class DescribeVpcPrivateIpAddressesResponse(AbstractModel):
    """DescribeVpcPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param VpcPrivateIpAddressSet: 内网`IP`地址信息列表。
        :type VpcPrivateIpAddressSet: list of VpcPrivateIpAddress
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.VpcPrivateIpAddressSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcPrivateIpAddressSet") is not None:
            self.VpcPrivateIpAddressSet = []
            for item in params.get("VpcPrivateIpAddressSet"):
                obj = VpcPrivateIpAddress()
                obj._deserialize(item)
                self.VpcPrivateIpAddressSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。
        :type VpcIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
<li>vpc-name - String - （过滤条件）VPC实例名称。</li>
<li>is-default - String - （过滤条件）是否默认VPC。</li>
<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>
<li>cidr-block - String - （过滤条件）vpc的cidr。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量
        :type Offset: str
        :param Limit: 返回数量
        :type Limit: str
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
        :param TotalCount: 符合条件的对象数。
        :type TotalCount: int
        :param VpcSet: VPC对象。
        :type VpcSet: list of Vpc
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpcSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self.VpcSet = []
            for item in params.get("VpcSet"):
                obj = Vpc()
                obj._deserialize(item)
                self.VpcSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnConnectionsRequest(AbstractModel):
    """DescribeVpnConnections请求参数结构体

    """

    def __init__(self):
        """
        :param VpnConnectionIds: VPN通道实例ID。形如：vpnx-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnConnectionIds和Filters。
        :type VpnConnectionIds: list of str
        :param Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpnConnectionIds和Filters。
<li>vpc-id - String - VPC实例ID，形如：`vpc-0a36uwkr`。</li>
<li>vpn-gateway-id - String - VPN网关实例ID，形如：`vpngw-p4lmqawn`。</li>
<li>customer-gateway-id - String - 对端网关实例ID，形如：`cgw-l4rblw63`。</li>
<li>vpn-connection-name - String - 通道名称，形如：`test-vpn`。</li>
<li>vpn-connection-id - String - 通道实例ID，形如：`vpnx-5p7vkch8"`。</li>
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        """
        self.VpnConnectionIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnConnectionIds = params.get("VpnConnectionIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnConnectionsResponse(AbstractModel):
    """DescribeVpnConnections返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param VpnConnectionSet: VPN通道实例。
        :type VpnConnectionSet: list of VpnConnection
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpnConnectionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpnConnectionSet") is not None:
            self.VpnConnectionSet = []
            for item in params.get("VpnConnectionSet"):
                obj = VpnConnection()
                obj._deserialize(item)
                self.VpnConnectionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayIds: VPN网关实例ID。形如：vpngw-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnGatewayIds和Filters。
        :type VpnGatewayIds: list of str
        :param Filters: 过滤条件，参数不支持同时指定VpnGatewayIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>
<li>vpn-gateway-id - String - （过滤条件）VPN实例ID形如：vpngw-5aluhh9t。</li>
<li>vpn-gateway-name - String - （过滤条件）VPN实例名称。</li>
<li>type - String - （过滤条件）VPN网关类型：'IPSEC', 'SSL'。</li>
<li>public-ip-address- String - （过滤条件）公网IP。</li>
<li>renew-flag - String - （过滤条件）网关续费类型，手动续费：'NOTIFY_AND_MANUAL_RENEW'、自动续费：'NOTIFY_AND_AUTO_RENEW'。</li>
<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>
        :type Filters: list of FilterObject
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 请求对象个数
        :type Limit: int
        """
        self.VpnGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayIds = params.get("VpnGatewayIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = FilterObject()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVpnGatewaysResponse(AbstractModel):
    """DescribeVpnGateways返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。
        :type TotalCount: int
        :param VpnGatewaySet: VPN网关实例详细信息列表。
        :type VpnGatewaySet: list of VpnGateway
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VpnGatewaySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VpnGatewaySet") is not None:
            self.VpnGatewaySet = []
            for item in params.get("VpnGatewaySet"):
                obj = VpnGateway()
                obj._deserialize(item)
                self.VpnGatewaySet.append(obj)
        self.RequestId = params.get("RequestId")


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 要解关联网络实例列表
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachClassicLinkVpcRequest(AbstractModel):
    """DetachClassicLinkVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。
        :type VpcId: str
        :param InstanceIds: CVM实例ID查询。形如：ins-r8hr2upy。
        :type InstanceIds: list of str
        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")


class DetachClassicLinkVpcResponse(AbstractModel):
    """DetachClassicLinkVpc返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param InstanceId: CVM实例ID。形如：ins-r8hr2upy。
        :type InstanceId: str
        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")


class DetachNetworkInterfaceResponse(AbstractModel):
    """DetachNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DirectConnectGateway(AbstractModel):
    """专线网关对象。

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关`ID`。
        :type DirectConnectGatewayId: str
        :param DirectConnectGatewayName: 专线网关名称。
        :type DirectConnectGatewayName: str
        :param VpcId: 专线网关关联`VPC`实例`ID`。
        :type VpcId: str
        :param NetworkType: 关联网络类型：
<li>`VPC` - 私有网络</li>
<li>`CCN` - 云联网</li>
        :type NetworkType: str
        :param NetworkInstanceId: 关联网络实例`ID`：
<li>`NetworkType`为`VPC`时，这里为私有网络实例`ID`</li>
<li>`NetworkType`为`CCN`时，这里为云联网实例`ID`</li>
        :type NetworkInstanceId: str
        :param GatewayType: 网关类型：
<li>NORMAL - 标准型，注：云联网只支持标准型</li>
<li>NAT - NAT型</li>
NAT类型支持网络地址转换配置，类型确定后不能修改；一个私有网络可以创建一个NAT类型的专线网关和一个非NAT类型的专线网关
        :type GatewayType: str
        :param CreateTime: 创建时间。
        :type CreateTime: str
        :param DirectConnectGatewayIp: 专线网关IP。
        :type DirectConnectGatewayIp: str
        :param CcnId: 专线网关关联`CCN`实例`ID`。
        :type CcnId: str
        :param CcnRouteType: 云联网路由学习类型：
<li>`BGP` - 自动学习。</li>
<li>`STATIC` - 静态，即用户配置。</li>
        :type CcnRouteType: str
        :param EnableBGP: 是否启用BGP。
        :type EnableBGP: bool
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.VpcId = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None
        self.CreateTime = None
        self.DirectConnectGatewayIp = None
        self.CcnId = None
        self.CcnRouteType = None
        self.EnableBGP = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.VpcId = params.get("VpcId")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")
        self.CreateTime = params.get("CreateTime")
        self.DirectConnectGatewayIp = params.get("DirectConnectGatewayIp")
        self.CcnId = params.get("CcnId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.EnableBGP = params.get("EnableBGP")


class DirectConnectGatewayCcnRoute(AbstractModel):
    """专线网关云联网路由（IDC网段）对象

    """

    def __init__(self):
        """
        :param RouteId: 路由ID。
        :type RouteId: str
        :param DestinationCidrBlock: IDC网段。
        :type DestinationCidrBlock: str
        :param ASPath: `BGP`的`AS-Path`属性。
        :type ASPath: list of str
        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.ASPath = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.ASPath = params.get("ASPath")


class DisableCcnRoutesRequest(AbstractModel):
    """DisableCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")


class DisableCcnRoutesResponse(AbstractModel):
    """DisableCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableRoutesRequest(AbstractModel):
    """DisableRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param RouteIds: 路由策略唯一ID。
        :type RouteIds: list of int non-negative
        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")


class DisableRoutesResponse(AbstractModel):
    """DisableRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateAddressRequest(AbstractModel):
    """DisassociateAddress请求参数结构体

    """

    def __init__(self):
        """
        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressId: str
        :param ReallocateNormalPublicIp: 表示解绑 EIP 之后是否分配普通公网 IP。取值范围：<br><li>TRUE：表示解绑 EIP 之后分配普通公网 IP。<br><li>FALSE：表示解绑 EIP 之后不分配普通公网 IP。<br>默认取值：FALSE。<br><br>只有满足以下条件时才能指定该参数：<br><li> 只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。<br><li>解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。
        :type ReallocateNormalPublicIp: bool
        """
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.ReallocateNormalPublicIp = params.get("ReallocateNormalPublicIp")


class DisassociateAddressResponse(AbstractModel):
    """DisassociateAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param CustomerGatewayVendor: 对端网关厂商信息对象，可通过DescribeCustomerGatewayVendors获取。
        :type CustomerGatewayVendor: :class:`tencentcloud.vpc.v20170312.models.CustomerGatewayVendor`
        :param InterfaceName: 通道接入设备物理接口名称。
        :type InterfaceName: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None
        self.CustomerGatewayVendor = None
        self.InterfaceName = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        if params.get("CustomerGatewayVendor") is not None:
            self.CustomerGatewayVendor = CustomerGatewayVendor()
            self.CustomerGatewayVendor._deserialize(params.get("CustomerGatewayVendor"))
        self.InterfaceName = params.get("InterfaceName")


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: XML格式配置信息。
        :type CustomerGatewayConfiguration: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CustomerGatewayConfiguration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CustomerGatewayConfiguration = params.get("CustomerGatewayConfiguration")
        self.RequestId = params.get("RequestId")


class EnableCcnRoutesRequest(AbstractModel):
    """EnableCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。
        :type RouteIds: list of str
        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")


class EnableCcnRoutesResponse(AbstractModel):
    """EnableCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。
        :type RouteTableId: str
        :param RouteIds: 路由策略唯一ID。
        :type RouteIds: list of int non-negative
        """
        self.RouteTableId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")


class EnableRoutesResponse(AbstractModel):
    """EnableRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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


class FilterObject(AbstractModel):
    """过滤器键值对

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


class GatewayFlowMonitorDetail(AbstractModel):
    """网关流量监控明细

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 来源`IP`。
        :type PrivateIpAddress: str
        :param InPkg: 入包量。
        :type InPkg: int
        :param OutPkg: 出包量。
        :type OutPkg: int
        :param InTraffic: 入带宽，单位：`Byte`。
        :type InTraffic: int
        :param OutTraffic: 出带宽，单位：`Byte`。
        :type OutTraffic: int
        """
        self.PrivateIpAddress = None
        self.InPkg = None
        self.OutPkg = None
        self.InTraffic = None
        self.OutTraffic = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.InPkg = params.get("InPkg")
        self.OutPkg = params.get("OutPkg")
        self.InTraffic = params.get("InTraffic")
        self.OutTraffic = params.get("OutTraffic")


class HaVip(AbstractModel):
    """描述 HAVIP 信息

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`的`ID`，是`HAVIP`的唯一标识。
        :type HaVipId: str
        :param HaVipName: `HAVIP`名称。
        :type HaVipName: str
        :param Vip: 虚拟IP地址。
        :type Vip: str
        :param VpcId: `HAVIP`所在私有网络`ID`。
        :type VpcId: str
        :param SubnetId: `HAVIP`所在子网`ID`。
        :type SubnetId: str
        :param NetworkInterfaceId: `HAVIP`关联弹性网卡`ID`。
        :type NetworkInterfaceId: str
        :param InstanceId: 被绑定的实例`ID`。
        :type InstanceId: str
        :param AddressIp: 绑定`EIP`。
        :type AddressIp: str
        :param State: 状态：
<li>`AVAILABLE`：运行中</li>
<li>`UNBIND`：未绑定</li>
        :type State: str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        """
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


class HaVipAssociateAddressIpRequest(AbstractModel):
    """HaVipAssociateAddressIp请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。必须是没有绑定`EIP`的`HAVIP`
        :type HaVipId: str
        :param AddressIp: 弹性公网`IP`。必须是没有绑定`HAVIP`的`EIP`
        :type AddressIp: str
        """
        self.HaVipId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.AddressIp = params.get("AddressIp")


class HaVipAssociateAddressIpResponse(AbstractModel):
    """HaVipAssociateAddressIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class HaVipDisassociateAddressIpRequest(AbstractModel):
    """HaVipDisassociateAddressIp请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。必须是已绑定`EIP`的`HAVIP`。
        :type HaVipId: str
        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")


class HaVipDisassociateAddressIpResponse(AbstractModel):
    """HaVipDisassociateAddressIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
        :param EncryptAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', 'NULL'， 默认为AES-CBC-128
        :type EncryptAlgorithm: str
        :param IntegrityAlgorith: 认证算法：可选值：'MD5', 'SHA1'，默认为
        :type IntegrityAlgorith: str
        :param IPSECSaLifetimeSeconds: IPsec SA lifetime(s)：单位秒，取值范围：180-604800
        :type IPSECSaLifetimeSeconds: int
        :param PfsDhGroup: PFS：可选值：'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', 'DH-GROUP24'，默认为NULL
        :type PfsDhGroup: str
        :param IPSECSaLifetimeTraffic: IPsec SA lifetime(KB)：单位KB，取值范围：2560-604800
        :type IPSECSaLifetimeTraffic: int
        """
        self.EncryptAlgorithm = None
        self.IntegrityAlgorith = None
        self.IPSECSaLifetimeSeconds = None
        self.PfsDhGroup = None
        self.IPSECSaLifetimeTraffic = None


    def _deserialize(self, params):
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.IntegrityAlgorith = params.get("IntegrityAlgorith")
        self.IPSECSaLifetimeSeconds = params.get("IPSECSaLifetimeSeconds")
        self.PfsDhGroup = params.get("PfsDhGroup")
        self.IPSECSaLifetimeTraffic = params.get("IPSECSaLifetimeTraffic")


class InquiryPriceCreateVpnGatewayRequest(AbstractModel):
    """InquiryPriceCreateVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。
        :type InternetMaxBandwidthOut: int
        :param InstanceChargeType: VPN网关计费模式，PREPAID：表示预付费，即包年包月，POSTPAID_BY_HOUR：表示后付费，即按量计费。默认：POSTPAID_BY_HOUR，如果指定预付费模式，参数InstanceChargePrepaid必填。
        :type InstanceChargeType: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceCreateVpnGatewayResponse(AbstractModel):
    """InquiryPriceCreateVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 商品价格。
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceRenewVpnGatewayRequest(AbstractModel):
    """InquiryPriceRenewVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class InquiryPriceRenewVpnGatewayResponse(AbstractModel):
    """InquiryPriceRenewVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 商品价格。
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InquiryPriceResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。
        :type InternetMaxBandwidthOut: int
        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 商品价格。
        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Price = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Price") is not None:
            self.Price = Price()
            self.Price._deserialize(params.get("Price"))
        self.RequestId = params.get("RequestId")


class InstanceChargePrepaid(AbstractModel):
    """预付费（包年包月）计费对象。

    """

    def __init__(self):
        """
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36。
        :type Period: int
        :param RenewFlag: 自动续费标识。取值范围： NOTIFY_AND_AUTO_RENEW：通知过期且自动续费， NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费。默认：NOTIFY_AND_MANUAL_RENEW
        :type RenewFlag: str
        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")


class InstanceStatistic(AbstractModel):
    """用于描述实例的统计信息

    """

    def __init__(self):
        """
        :param InstanceType: 实例的类型
        :type InstanceType: str
        :param InstanceCount: 实例的个数
        :type InstanceCount: int
        """
        self.InstanceType = None
        self.InstanceCount = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.InstanceCount = params.get("InstanceCount")


class Ip6Rule(AbstractModel):
    """IPV6转换规则

    """

    def __init__(self):
        """
        :param Ip6RuleId: IPV6转换规则唯一ID，形如rule6-xxxxxxxx
        :type Ip6RuleId: str
        :param Ip6RuleName: IPV6转换规则名称
        :type Ip6RuleName: str
        :param Vip6: IPV6地址
        :type Vip6: str
        :param Vport6: IPV6端口号
        :type Vport6: int
        :param Protocol: 协议类型，支持TCP/UDP
        :type Protocol: str
        :param Vip: IPV4地址
        :type Vip: str
        :param Vport: IPV4端口号
        :type Vport: int
        :param RuleStatus: 转换规则状态，限于CREATING,RUNNING,DELETING,MODIFYING
        :type RuleStatus: str
        :param CreatedTime: 转换规则创建时间
        :type CreatedTime: str
        """
        self.Ip6RuleId = None
        self.Ip6RuleName = None
        self.Vip6 = None
        self.Vport6 = None
        self.Protocol = None
        self.Vip = None
        self.Vport = None
        self.RuleStatus = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.Ip6RuleId = params.get("Ip6RuleId")
        self.Ip6RuleName = params.get("Ip6RuleName")
        self.Vip6 = params.get("Vip6")
        self.Vport6 = params.get("Vport6")
        self.Protocol = params.get("Protocol")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        self.RuleStatus = params.get("RuleStatus")
        self.CreatedTime = params.get("CreatedTime")


class Ip6RuleInfo(AbstractModel):
    """IPV6转换规则

    """

    def __init__(self):
        """
        :param Vport6: IPV6端口号，可在0~65535范围取值
        :type Vport6: int
        :param Protocol: 协议类型，支持TCP/UDP
        :type Protocol: str
        :param Vip: IPV4地址
        :type Vip: str
        :param Vport: IPV4端口号，可在0~65535范围取值
        :type Vport: int
        """
        self.Vport6 = None
        self.Protocol = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vport6 = params.get("Vport6")
        self.Protocol = params.get("Protocol")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class Ip6Translator(AbstractModel):
    """IPV6转换实例信息

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6TranslatorName: IPV6转换实例名称
        :type Ip6TranslatorName: str
        :param Vip6: IPV6地址
        :type Vip6: str
        :param IspName: IPV6转换地址所属运营商
        :type IspName: str
        :param TranslatorStatus: 转换实例状态，限于CREATING,RUNNING,DELETING,MODIFYING
        :type TranslatorStatus: str
        :param CreatedTime: IPV6转换实例创建时间
        :type CreatedTime: str
        :param Ip6RuleCount: 绑定的IPV6转换规则数量
        :type Ip6RuleCount: int
        :param IP6RuleSet: IPV6转换规则信息
        :type IP6RuleSet: list of Ip6Rule
        """
        self.Ip6TranslatorId = None
        self.Ip6TranslatorName = None
        self.Vip6 = None
        self.IspName = None
        self.TranslatorStatus = None
        self.CreatedTime = None
        self.Ip6RuleCount = None
        self.IP6RuleSet = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")
        self.Vip6 = params.get("Vip6")
        self.IspName = params.get("IspName")
        self.TranslatorStatus = params.get("TranslatorStatus")
        self.CreatedTime = params.get("CreatedTime")
        self.Ip6RuleCount = params.get("Ip6RuleCount")
        if params.get("IP6RuleSet") is not None:
            self.IP6RuleSet = []
            for item in params.get("IP6RuleSet"):
                obj = Ip6Rule()
                obj._deserialize(item)
                self.IP6RuleSet.append(obj)


class Ipv6Address(AbstractModel):
    """`IPv6`地址信息。

    """

    def __init__(self):
        """
        :param Address: `IPv6`地址，形如：`3402:4e00:20:100:0:8cd9:2a67:71f3`
        :type Address: str
        :param Primary: 是否是主`IP`。
        :type Primary: bool
        :param AddressId: `EIP`实例`ID`，形如：`eip-hxlqja90`。
        :type AddressId: str
        :param Description: 描述信息。
        :type Description: str
        :param IsWanIpBlocked: 公网IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param State: `IPv6`地址状态：
<li>`PENDING`：生产中</li>
<li>`MIGRATING`：迁移中</li>
<li>`DELETING`：删除中</li>
<li>`AVAILABLE`：可用的</li>
        :type State: str
        """
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


class ItemPrice(AbstractModel):
    """单项计费价格信息

    """

    def __init__(self):
        """
        :param UnitPrice: 按量计费后付费单价，单位：元。
        :type UnitPrice: float
        :param ChargeUnit: 按量计费后付费计价单元，可取值范围： HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）： GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。
        :type ChargeUnit: str
        :param OriginalPrice: 预付费商品的原价，单位：元。
        :type OriginalPrice: float
        :param DiscountPrice: 预付费商品的折扣价，单位：元。
        :type DiscountPrice: float
        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")


class MigrateNetworkInterfaceRequest(AbstractModel):
    """MigrateNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param SourceInstanceId: 弹性网卡当前绑定的CVM实例ID。形如：ins-r8hr2upy。
        :type SourceInstanceId: str
        :param DestinationInstanceId: 待迁移的目的CVM实例ID。
        :type DestinationInstanceId: str
        """
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")


class MigrateNetworkInterfaceResponse(AbstractModel):
    """MigrateNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MigratePrivateIpAddressRequest(AbstractModel):
    """MigratePrivateIpAddress请求参数结构体

    """

    def __init__(self):
        """
        :param SourceNetworkInterfaceId: 当内网IP绑定的弹性网卡实例ID，例如：eni-m6dyj72l。
        :type SourceNetworkInterfaceId: str
        :param DestinationNetworkInterfaceId: 待迁移的目的弹性网卡实例ID。
        :type DestinationNetworkInterfaceId: str
        :param PrivateIpAddress: 迁移的内网IP地址，例如：10.0.0.6。
        :type PrivateIpAddress: str
        """
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
        self.SourceNetworkInterfaceId = params.get("SourceNetworkInterfaceId")
        self.DestinationNetworkInterfaceId = params.get("DestinationNetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")


class MigratePrivateIpAddressResponse(AbstractModel):
    """MigratePrivateIpAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressAttributeRequest(AbstractModel):
    """ModifyAddressAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressId: str
        :param AddressName: 修改后的 EIP 名称。长度上限为20个字符。
        :type AddressName: str
        """
        self.AddressId = None
        self.AddressName = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.AddressName = params.get("AddressName")


class ModifyAddressAttributeResponse(AbstractModel):
    """ModifyAddressAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateAttributeRequest(AbstractModel):
    """ModifyAddressTemplateAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP地址模板实例ID，例如：ipm-mdunqeb6。
        :type AddressTemplateId: str
        :param AddressTemplateName: IP地址模板名称。
        :type AddressTemplateName: str
        :param Addresses: 地址信息，支持 IP、CIDR、IP 范围。
        :type Addresses: list of str
        """
        self.AddressTemplateId = None
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")


class ModifyAddressTemplateAttributeResponse(AbstractModel):
    """ModifyAddressTemplateAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateGroupAttributeRequest(AbstractModel):
    """ModifyAddressTemplateGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP地址模板集合实例ID，例如：ipmg-2uw6ujo6。
        :type AddressTemplateGroupId: str
        :param AddressTemplateGroupName: IP地址模板集合名称。
        :type AddressTemplateGroupName: str
        :param AddressTemplateIds: IP地址模板实例ID， 例如：ipm-mdunqeb6。
        :type AddressTemplateIds: list of str
        """
        self.AddressTemplateGroupId = None
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")


class ModifyAddressTemplateGroupAttributeResponse(AbstractModel):
    """ModifyAddressTemplateGroupAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressesBandwidthRequest(AbstractModel):
    """ModifyAddressesBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param AddressIds: EIP唯一标识id，形如'eip-xxxx'
        :type AddressIds: list of str
        :param InternetMaxBandwidthOut: 调整带宽目标值
        :type InternetMaxBandwidthOut: int
        :param StartTime: 包月带宽起始时间
        :type StartTime: str
        :param EndTime: 包月带宽结束时间
        :type EndTime: str
        """
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")


class ModifyAddressesBandwidthResponse(AbstractModel):
    """ModifyAddressesBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyBandwidthPackageAttributeRequest(AbstractModel):
    """ModifyBandwidthPackageAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一标识ID
        :type BandwidthPackageId: str
        :param BandwidthPackageName: 带宽包名称
        :type BandwidthPackageName: str
        """
        self.BandwidthPackageId = None
        self.BandwidthPackageName = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageName = params.get("BandwidthPackageName")


class ModifyBandwidthPackageAttributeResponse(AbstractModel):
    """ModifyBandwidthPackageAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttributeRequest(AbstractModel):
    """ModifyCcnAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param CcnName: CCN名称，最大长度不能超过60个字节。
        :type CcnName: str
        :param CcnDescription: CCN描述信息，最大长度不能超过100个字节。
        :type CcnDescription: str
        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")


class ModifyCcnAttributeResponse(AbstractModel):
    """ModifyCcnAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。
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


class ModifyDirectConnectGatewayAttributeRequest(AbstractModel):
    """ModifyDirectConnectGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关唯一`ID`，形如：`dcg-9o233uri`。
        :type DirectConnectGatewayId: str
        :param DirectConnectGatewayName: 专线网关名称，可任意命名，但不得超过60个字符。
        :type DirectConnectGatewayName: str
        :param CcnRouteType: 云联网路由学习类型，可选值：`BGP`（自动学习）、`STATIC`（静态，即用户配置）。只有云联网类型专线网关且开启了BGP功能才支持修改`CcnRouteType`。
        :type CcnRouteType: str
        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.CcnRouteType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.CcnRouteType = params.get("CcnRouteType")


class ModifyDirectConnectGatewayAttributeResponse(AbstractModel):
    """ModifyDirectConnectGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHaVipAttributeRequest(AbstractModel):
    """ModifyHaVipAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。
        :type HaVipId: str
        :param HaVipName: `HAVIP`名称，可任意命名，但不得超过60个字符。
        :type HaVipName: str
        """
        self.HaVipId = None
        self.HaVipName = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.HaVipName = params.get("HaVipName")


class ModifyHaVipAttributeResponse(AbstractModel):
    """ModifyHaVipAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6RuleRequest(AbstractModel):
    """ModifyIp6Rule请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6RuleId: IPV6转换规则唯一ID，形如rule6-xxxxxxxx
        :type Ip6RuleId: str
        :param Ip6RuleName: IPV6转换规则修改后的名称
        :type Ip6RuleName: str
        :param Vip: IPV6转换规则修改后的IPV4地址
        :type Vip: str
        :param Vport: IPV6转换规则修改后的IPV4端口号
        :type Vport: int
        """
        self.Ip6TranslatorId = None
        self.Ip6RuleId = None
        self.Ip6RuleName = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6RuleId = params.get("Ip6RuleId")
        self.Ip6RuleName = params.get("Ip6RuleName")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")


class ModifyIp6RuleResponse(AbstractModel):
    """ModifyIp6Rule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6TranslatorRequest(AbstractModel):
    """ModifyIp6Translator请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6TranslatorName: IPV6转换实例修改名称
        :type Ip6TranslatorName: str
        """
        self.Ip6TranslatorId = None
        self.Ip6TranslatorName = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")


class ModifyIp6TranslatorResponse(AbstractModel):
    """ModifyIp6Translator返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-pxir56ns。
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。
        :type NetworkInterfaceDescription: str
        :param SecurityGroupIds: 指定绑定的安全组，例如:['sg-1dd51d']。
        :type SecurityGroupIds: list of str
        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecurityGroupIds = params.get("SecurityGroupIds")


class ModifyNetworkInterfaceAttributeResponse(AbstractModel):
    """ModifyNetworkInterfaceAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPrivateIpAddressesAttributeRequest(AbstractModel):
    """ModifyPrivateIpAddressesAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内网IP信息。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class ModifyPrivateIpAddressesAttributeResponse(AbstractModel):
    """ModifyPrivateIpAddressesAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRouteTableAttributeRequest(AbstractModel):
    """ModifyRouteTableAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        """
        self.RouteTableId = None
        self.RouteTableName = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")


class ModifyRouteTableAttributeResponse(AbstractModel):
    """ModifyRouteTableAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupAttributeRequest(AbstractModel):
    """ModifySecurityGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。
        :type GroupName: str
        :param GroupDescription: 安全组备注，最多100个字符。
        :type GroupDescription: str
        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")


class ModifySecurityGroupAttributeResponse(AbstractModel):
    """ModifySecurityGroupAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityGroupPoliciesRequest(AbstractModel):
    """ModifySecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全组规则集合。 SecurityGroupPolicySet对象必须同时指定新的出（Egress）入（Ingress）站规则。 SecurityGroupPolicy对象不支持自定义索引（PolicyIndex）。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class ModifySecurityGroupPoliciesResponse(AbstractModel):
    """ModifySecurityGroupPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateAttributeRequest(AbstractModel):
    """ModifyServiceTemplateAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 协议端口模板实例ID，例如：ppm-529nwwj8。
        :type ServiceTemplateId: str
        :param ServiceTemplateName: 协议端口模板名称。
        :type ServiceTemplateName: str
        :param Services: 支持单个端口、多个端口、连续端口及所有端口，协议支持：TCP、UDP、ICMP、GRE 协议。
        :type Services: list of str
        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")


class ModifyServiceTemplateAttributeResponse(AbstractModel):
    """ModifyServiceTemplateAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateGroupAttributeRequest(AbstractModel):
    """ModifyServiceTemplateGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 协议端口模板集合实例ID，例如：ppmg-ei8hfd9a。
        :type ServiceTemplateGroupId: str
        :param ServiceTemplateGroupName: 协议端口模板集合名称。
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIds: 协议端口模板实例ID，例如：ppm-4dw6agho。
        :type ServiceTemplateIds: list of str
        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")


class ModifyServiceTemplateGroupAttributeResponse(AbstractModel):
    """ModifyServiceTemplateGroupAttribute返回参数结构体

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
        :param SubnetId: 子网实例ID。形如：subnet-pxir56ns。
        :type SubnetId: str
        :param SubnetName: 子网名称，最大长度不能超过60个字节。
        :type SubnetName: str
        :param EnableBroadcast: 子网是否开启广播。
        :type EnableBroadcast: str
        """
        self.SubnetId = None
        self.SubnetName = None
        self.EnableBroadcast = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")


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


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。
        :type VpcId: str
        :param VpcName: 私有网络名称，可任意命名，但不得超过60个字符。
        :type VpcName: str
        :param EnableMulticast: 是否开启组播。true: 开启, false: 关闭。
        :type EnableMulticast: str
        :param DnsServers: DNS地址，最多支持4个，第1个默认为主，其余为备
        :type DnsServers: list of str
        :param DomainName: 域名
        :type DomainName: str
        """
        self.VpcId = None
        self.VpcName = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")


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


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        :param VpnConnectionName: VPN通道名称，可任意命名，但不得超过60个字符。
        :type VpnConnectionName: str
        :param PreShareKey: 预共享密钥。
        :type PreShareKey: str
        :param SecurityPolicyDatabases: SPD策略组，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。
        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议。
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSec配置，腾讯云提供IPSec安全会话设置。
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
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
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
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
        :param InstanceChargeType: VPN网关计费模式，目前只支持预付费（即包年包月）到后付费（即按量计费）的转换。即参数只支持：POSTPAID_BY_HOUR。
        :type InstanceChargeType: str
        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InstanceChargeType = params.get("InstanceChargeType")


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


class NetworkInterface(AbstractModel):
    """弹性网卡

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-f1xjkw1b。
        :type NetworkInterfaceId: str
        :param NetworkInterfaceName: 弹性网卡名称。
        :type NetworkInterfaceName: str
        :param NetworkInterfaceDescription: 弹性网卡描述。
        :type NetworkInterfaceDescription: str
        :param SubnetId: 子网实例ID。
        :type SubnetId: str
        :param VpcId: VPC实例ID。
        :type VpcId: str
        :param GroupSet: 绑定的安全组。
        :type GroupSet: list of str
        :param Primary: 是否是主网卡。
        :type Primary: bool
        :param MacAddress: MAC地址。
        :type MacAddress: str
        :param State: 弹性网卡状态：
<li>`PENDING`：创建中</li>
<li>`AVAILABLE`：可用的</li>
<li>`ATTACHING`：绑定中</li>
<li>`DETACHING`：解绑中</li>
<li>`DELETING`：删除中</li>
        :type State: str
        :param PrivateIpAddressSet: 内网IP信息。
        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification
        :param Attachment: 绑定的云服务器对象。
注意：此字段可能返回 null，表示取不到有效值。
        :type Attachment: :class:`tencentcloud.vpc.v20170312.models.NetworkInterfaceAttachment`
        :param Zone: 可用区。
        :type Zone: str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        :param Ipv6AddressSet: `IPv6`地址列表。
        :type Ipv6AddressSet: list of Ipv6Address
        """
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


class NetworkInterfaceAttachment(AbstractModel):
    """弹性网卡绑定关系

    """

    def __init__(self):
        """
        :param InstanceId: 云主机实例ID。
        :type InstanceId: str
        :param DeviceIndex: 网卡在云主机实例内的序号。
        :type DeviceIndex: int
        :param InstanceAccountId: 云主机所有者账户信息。
        :type InstanceAccountId: str
        :param AttachTime: 绑定时间。
        :type AttachTime: str
        """
        self.InstanceId = None
        self.DeviceIndex = None
        self.InstanceAccountId = None
        self.AttachTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.DeviceIndex = params.get("DeviceIndex")
        self.InstanceAccountId = params.get("InstanceAccountId")
        self.AttachTime = params.get("AttachTime")


class Price(AbstractModel):
    """价格

    """

    def __init__(self):
        """
        :param InstancePrice: 实例价格。
        :type InstancePrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`
        :param BandwidthPrice: 网络价格。
        :type BandwidthPrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`
        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))


class PrivateIpAddressSpecification(AbstractModel):
    """内网IP信息

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 内网IP地址。
        :type PrivateIpAddress: str
        :param Primary: 是否是主IP。
        :type Primary: bool
        :param PublicIpAddress: 公网IP地址。
        :type PublicIpAddress: str
        :param AddressId: EIP实例ID，例如：eip-11112222。
        :type AddressId: str
        :param Description: 内网IP描述信息。
        :type Description: str
        :param IsWanIpBlocked: 公网IP是否被封堵。
        :type IsWanIpBlocked: bool
        :param State: IP状态：
PENDING：生产中
MIGRATING：迁移中
DELETING：删除中
AVAILABLE：可用的
        :type State: str
        """
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


class Quota(AbstractModel):
    """描述了配额信息

    """

    def __init__(self):
        """
        :param QuotaId: 配额名称，取值范围：<br><li>`TOTAL_EIP_QUOTA`：用户当前地域下EIP的配额数；<br><li>`DAILY_EIP_APPLY`：用户当前地域下今日申购次数；<br><li>`DAILY_PUBLIC_IP_ASSIGN`：用户当前地域下，重新分配公网 IP次数。
        :type QuotaId: str
        :param QuotaCurrent: 当前数量
        :type QuotaCurrent: int
        :param QuotaLimit: 配额数量
        :type QuotaLimit: int
        """
        self.QuotaId = None
        self.QuotaCurrent = None
        self.QuotaLimit = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")


class RejectAttachCcnInstancesRequest(AbstractModel):
    """RejectAttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param Instances: 拒绝关联实例列表。
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class RejectAttachCcnInstancesResponse(AbstractModel):
    """RejectAttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param AddressIds: 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。
        :type AddressIds: list of str
        """
        self.AddressIds = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")


class ReleaseAddressesResponse(AbstractModel):
    """ReleaseAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveBandwidthPackageResourcesRequest(AbstractModel):
    """RemoveBandwidthPackageResources请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一标识ID，形如'bwp-xxxx'
        :type BandwidthPackageId: str
        :param ResourceType: 资源类型，包括‘Address’, ‘LoadBalance’
        :type ResourceType: str
        :param ResourceIds: 资源Id，形如'eip-xxxx', 'lb-xxxx'
        :type ResourceIds: list of str
        """
        self.BandwidthPackageId = None
        self.ResourceType = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceIds = params.get("ResourceIds")


class RemoveBandwidthPackageResourcesResponse(AbstractModel):
    """RemoveBandwidthPackageResources返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveIp6RulesRequest(AbstractModel):
    """RemoveIp6Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换规则所属的转换实例唯一ID，形如ip6-xxxxxxxx
        :type Ip6TranslatorId: str
        :param Ip6RuleIds: 待删除IPV6转换规则，形如rule6-xxxxxxxx
        :type Ip6RuleIds: list of str
        """
        self.Ip6TranslatorId = None
        self.Ip6RuleIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6RuleIds = params.get("Ip6RuleIds")


class RemoveIp6RulesResponse(AbstractModel):
    """RemoveIp6Rules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewVpnGatewayRequest(AbstractModel):
    """RenewVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param InstanceChargePrepaid: 预付费计费模式。
        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`
        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))


class RenewVpnGatewayResponse(AbstractModel):
    """RenewVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：dcg-prpqlmg1
        :type DirectConnectGatewayId: str
        :param Routes: 需要连通的IDC网段列表
        :type Routes: list of DirectConnectGatewayCcnRoute
        """
        self.DirectConnectGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = DirectConnectGatewayCcnRoute()
                obj._deserialize(item)
                self.Routes.append(obj)


class ReplaceDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRouteTableAssociationRequest(AbstractModel):
    """ReplaceRouteTableAssociation请求参数结构体

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID，例如：subnet-3x5lf5q0。可通过DescribeSubnets接口查询。
        :type SubnetId: str
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")


class ReplaceRouteTableAssociationResponse(AbstractModel):
    """ReplaceRouteTableAssociation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceRoutesRequest(AbstractModel):
    """ReplaceRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param Routes: 路由策略对象。需要指定路由策略ID（RouteId）。
        :type Routes: list of Route
        """
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


class ReplaceRoutesResponse(AbstractModel):
    """ReplaceRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。
        :type SecurityGroupId: str
        :param SecurityGroupPolicySet: 安全组规则集合对象。
        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`
        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))


class ReplaceSecurityGroupPolicyResponse(AbstractModel):
    """ReplaceSecurityGroupPolicy返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetAttachCcnInstancesRequest(AbstractModel):
    """ResetAttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param CcnUin: CCN所属UIN（根账号）。
        :type CcnUin: str
        :param Instances: 重新申请关联网络实例列表。
        :type Instances: list of CcnInstance
        """
        self.CcnId = None
        self.CcnUin = None
        self.Instances = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnUin = params.get("CcnUin")
        if params.get("Instances") is not None:
            self.Instances = []
            for item in params.get("Instances"):
                obj = CcnInstance()
                obj._deserialize(item)
                self.Instances.append(obj)


class ResetAttachCcnInstancesResponse(AbstractModel):
    """ResetAttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetRoutesRequest(AbstractModel):
    """ResetRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名称，最大长度不能超过60个字节。
        :type RouteTableName: str
        :param Routes: 路由策略。
        :type Routes: list of Route
        """
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


class ResetRoutesResponse(AbstractModel):
    """ResetRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。
        :type VpnConnectionId: str
        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
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


class ResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。
        :type InternetMaxBandwidthOut: int
        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")


class ResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """描述带宽包资源信息的结构

    """

    def __init__(self):
        """
        :param ResourceType: 带宽包资源类型，包括'Address'和'LoadBalance'
        :type ResourceType: str
        :param ResourceId: 带宽包资源Id，形如'eip-xxxx', 'lb-xxxx'
        :type ResourceId: str
        :param AddressIp: 带宽包资源Ip
        :type AddressIp: str
        """
        self.ResourceType = None
        self.ResourceId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.AddressIp = params.get("AddressIp")


class Route(AbstractModel):
    """路由策略对象

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的网段，取值不能在私有网络网段内，例如：112.20.51.0/24。
        :type DestinationCidrBlock: str
        :param GatewayType: 下一跳类型，目前我们支持的类型有：
CVM：公网网关类型的云主机；
VPN：VPN网关；
DIRECTCONNECT：专线网关；
PEERCONNECTION：对等连接；
SSLVPN：sslvpn网关；
NAT：NAT网关; 
NORMAL_CVM：普通云主机；
EIP：云主机的公网IP；
CCN：云联网。
        :type GatewayType: str
        :param GatewayId: 下一跳地址，这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址。
特别注意：当 GatewayType 为 EIP 时，GatewayId 固定值 '0'
        :type GatewayId: str
        :param RouteId: 路由策略ID。
        :type RouteId: int
        :param RouteDescription: 路由策略描述。
        :type RouteDescription: str
        :param Enabled: 是否启用
        :type Enabled: bool
        :param RouteType: 路由类型，目前我们支持的类型有：
USER：用户路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和操作 USER 类型的路由。
        :type RouteType: str
        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteId = None
        self.RouteDescription = None
        self.Enabled = None
        self.RouteType = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteId = params.get("RouteId")
        self.RouteDescription = params.get("RouteDescription")
        self.Enabled = params.get("Enabled")
        self.RouteType = params.get("RouteType")


class RouteConflict(AbstractModel):
    """路由冲突对象

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param DestinationCidrBlock: 要检查的与之冲突的目的端
        :type DestinationCidrBlock: str
        :param ConflictSet: 冲突的路由策略列表
        :type ConflictSet: list of Route
        """
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


class RouteTable(AbstractModel):
    """路由表对象

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。
        :type VpcId: str
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。
        :type RouteTableId: str
        :param RouteTableName: 路由表名称。
        :type RouteTableName: str
        :param AssociationSet: 路由表关联关系。
        :type AssociationSet: list of RouteTableAssociation
        :param RouteSet: 路由表策略集合。
        :type RouteSet: list of Route
        :param Main: 是否默认路由表。
        :type Main: bool
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        """
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


class RouteTableAssociation(AbstractModel):
    """路由表关联关系

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例ID。
        :type SubnetId: str
        :param RouteTableId: 路由表实例ID。
        :type RouteTableId: str
        """
        self.SubnetId = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.RouteTableId = params.get("RouteTableId")


class SecurityGroup(AbstractModel):
    """安全组对象

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如：sg-ohuuioma。
        :type SecurityGroupId: str
        :param SecurityGroupName: 安全组名称，可任意命名，但不得超过60个字符。
        :type SecurityGroupName: str
        :param SecurityGroupDesc: 安全组备注，最多100个字符。
        :type SecurityGroupDesc: str
        :param ProjectId: 项目id，默认0。可在qcloud控制台项目管理页面查询到。
        :type ProjectId: str
        :param IsDefault: 是否是默认安全组，默认安全组不支持删除。
        :type IsDefault: bool
        :param CreatedTime: 安全组创建时间。
        :type CreatedTime: str
        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDesc = None
        self.ProjectId = None
        self.IsDefault = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDesc = params.get("SecurityGroupDesc")
        self.ProjectId = params.get("ProjectId")
        self.IsDefault = params.get("IsDefault")
        self.CreatedTime = params.get("CreatedTime")


class SecurityGroupAssociationStatistics(AbstractModel):
    """安全组关联的实例统计

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID。
        :type SecurityGroupId: str
        :param CVM: 云主机实例数。
        :type CVM: int
        :param CDB: 数据库实例数。
        :type CDB: int
        :param ENI: 弹性网卡实例数。
        :type ENI: int
        :param SG: 被安全组引用数。
        :type SG: int
        :param CLB: 负载均衡实例数。
        :type CLB: int
        :param InstanceStatistics: 全量实例的绑定统计。
        :type InstanceStatistics: list of InstanceStatistic
        """
        self.SecurityGroupId = None
        self.CVM = None
        self.CDB = None
        self.ENI = None
        self.SG = None
        self.CLB = None
        self.InstanceStatistics = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.CVM = params.get("CVM")
        self.CDB = params.get("CDB")
        self.ENI = params.get("ENI")
        self.SG = params.get("SG")
        self.CLB = params.get("CLB")
        if params.get("InstanceStatistics") is not None:
            self.InstanceStatistics = []
            for item in params.get("InstanceStatistics"):
                obj = InstanceStatistic()
                obj._deserialize(item)
                self.InstanceStatistics.append(obj)


class SecurityGroupPolicy(AbstractModel):
    """安全组规则对象

    """

    def __init__(self):
        """
        :param PolicyIndex: 安全组规则索引号。
        :type PolicyIndex: int
        :param Protocol: 协议, 取值: TCP,UDP, ICMP。
        :type Protocol: str
        :param Port: 端口(all, 离散port,  range)。
        :type Port: str
        :param ServiceTemplate: 协议端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。
        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateSpecification`
        :param CidrBlock: 网段或IP(互斥)。
        :type CidrBlock: str
        :param SecurityGroupId: 安全组实例ID，例如：sg-ohuuioma。
        :type SecurityGroupId: str
        :param AddressTemplate: IP地址ID或者ID地址组ID。
        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateSpecification`
        :param Action: ACCEPT 或 DROP。
        :type Action: str
        :param PolicyDescription: 安全组规则描述。
        :type PolicyDescription: str
        """
        self.PolicyIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplate = None
        self.CidrBlock = None
        self.SecurityGroupId = None
        self.AddressTemplate = None
        self.Action = None
        self.PolicyDescription = None


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


class SecurityGroupPolicySet(AbstractModel):
    """安全组规则集合

    """

    def __init__(self):
        """
        :param Version: 安全组规则当前版本。用户每次更新安全规则版本会自动加1，防止更新的路由规则已过期，不填不考虑冲突。
        :type Version: str
        :param Egress: 出站规则。
        :type Egress: list of SecurityGroupPolicy
        :param Ingress: 入站规则。
        :type Ingress: list of SecurityGroupPolicy
        """
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


class ServiceTemplate(AbstractModel):
    """协议端口模板

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 协议端口实例ID，例如：ppm-f5n1f8da。
        :type ServiceTemplateId: str
        :param ServiceTemplateName: 模板名称。
        :type ServiceTemplateName: str
        :param ServiceSet: 协议端口信息。
        :type ServiceSet: list of str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.ServiceSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.ServiceSet = params.get("ServiceSet")
        self.CreatedTime = params.get("CreatedTime")


class ServiceTemplateGroup(AbstractModel):
    """协议端口模板集合

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 协议端口模板集合实例ID，例如：ppmg-2klmrefu。
        :type ServiceTemplateGroupId: str
        :param ServiceTemplateGroupName: 协议端口模板集合名称。
        :type ServiceTemplateGroupName: str
        :param ServiceTemplateIdSet: 协议端口模板实例ID。
        :type ServiceTemplateIdSet: list of str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIdSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIdSet = params.get("ServiceTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")


class ServiceTemplateSpecification(AbstractModel):
    """协议端口模版

    """

    def __init__(self):
        """
        :param ServiceId: 协议端口ID，例如：ppm-f5n1f8da。
        :type ServiceId: str
        :param ServiceGroupId: 协议端口组ID，例如：ppmg-f5n1f8da。
        :type ServiceGroupId: str
        """
        self.ServiceId = None
        self.ServiceGroupId = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceGroupId = params.get("ServiceGroupId")


class SetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """SetCcnRegionBandwidthLimits请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。
        :type CcnId: str
        :param CcnRegionBandwidthLimits: 云联网（CCN）各地域出带宽上限。
        :type CcnRegionBandwidthLimits: list of CcnRegionBandwidthLimit
        """
        self.CcnId = None
        self.CcnRegionBandwidthLimits = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("CcnRegionBandwidthLimits") is not None:
            self.CcnRegionBandwidthLimits = []
            for item in params.get("CcnRegionBandwidthLimits"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimits.append(obj)


class SetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """SetCcnRegionBandwidthLimits返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Subnet(AbstractModel):
    """子网对象

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。
        :type VpcId: str
        :param SubnetId: 子网实例`ID`，例如：subnet-bthucmmy。
        :type SubnetId: str
        :param SubnetName: 子网名称。
        :type SubnetName: str
        :param CidrBlock: 子网的 `IPv4` `CIDR`。
        :type CidrBlock: str
        :param IsDefault: 是否默认子网。
        :type IsDefault: bool
        :param EnableBroadcast: 是否开启广播。
        :type EnableBroadcast: bool
        :param Zone: 可用区。
        :type Zone: str
        :param RouteTableId: 路由表实例ID，例如：rtb-l2h8d7c2。
        :type RouteTableId: str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        :param AvailableIpAddressCount: 可用`IP`数。
        :type AvailableIpAddressCount: int
        :param Ipv6CidrBlock: 子网的 `IPv6` `CIDR`。
        :type Ipv6CidrBlock: str
        """
        self.VpcId = None
        self.SubnetId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.IsDefault = None
        self.EnableBroadcast = None
        self.Zone = None
        self.RouteTableId = None
        self.CreatedTime = None
        self.AvailableIpAddressCount = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.IsDefault = params.get("IsDefault")
        self.EnableBroadcast = params.get("EnableBroadcast")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
        self.CreatedTime = params.get("CreatedTime")
        self.AvailableIpAddressCount = params.get("AvailableIpAddressCount")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")


class SubnetInput(AbstractModel):
    """子网对象

    """

    def __init__(self):
        """
        :param CidrBlock: 子网的`CIDR`。
        :type CidrBlock: str
        :param SubnetName: 子网名称。
        :type SubnetName: str
        :param Zone: 可用区。形如：`ap-guangzhou-2`。
        :type Zone: str
        :param RouteTableId: 指定关联路由表，形如：`rtb-3ryrwzuu`。
        :type RouteTableId: str
        """
        self.CidrBlock = None
        self.SubnetName = None
        self.Zone = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")


class TransformAddressRequest(AbstractModel):
    """TransformAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作有普通公网 IP 的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录[控制台](https://console.cloud.tencent.com/cvm)查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) 接口返回值中的`InstanceId`获取。
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")


class TransformAddressResponse(AbstractModel):
    """TransformAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignPrivateIpAddressesRequest(AbstractModel):
    """UnassignPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。
        :type NetworkInterfaceId: str
        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。
        :type PrivateIpAddresses: list of PrivateIpAddressSpecification
        """
        self.NetworkInterfaceId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)


class UnassignPrivateIpAddressesResponse(AbstractModel):
    """UnassignPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Vpc(AbstractModel):
    """私有网络(VPC)对象。

    """

    def __init__(self):
        """
        :param VpcName: `VPC`名称。
        :type VpcName: str
        :param VpcId: `VPC`实例`ID`，例如：vpc-azd4dt1c。
        :type VpcId: str
        :param CidrBlock: `VPC`的`IPv4` `CIDR`。
        :type CidrBlock: str
        :param IsDefault: 是否默认`VPC`。
        :type IsDefault: bool
        :param EnableMulticast: 是否开启组播。
        :type EnableMulticast: bool
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        :param DnsServerSet: `DNS`列表。
        :type DnsServerSet: list of str
        :param DomainName: `DHCP`域名选项值。
        :type DomainName: str
        :param DhcpOptionsId: `DHCP`选项集`ID`。
        :type DhcpOptionsId: str
        :param EnableDhcp: 是否开启`DHCP`。
        :type EnableDhcp: bool
        :param Ipv6CidrBlock: `VPC`的`IPv6` `CIDR`。
        :type Ipv6CidrBlock: str
        """
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


class VpcPrivateIpAddress(AbstractModel):
    """VPC内网IP对象。

    """

    def __init__(self):
        """
        :param PrivateIpAddress: `VPC`内网`IP`。
        :type PrivateIpAddress: str
        :param CidrBlock: 所属子网`CIDR`。
        :type CidrBlock: str
        :param PrivateIpAddressType: 内网`IP`类型。
        :type PrivateIpAddressType: str
        :param CreatedTime: `IP`申请时间。
        :type CreatedTime: str
        """
        self.PrivateIpAddress = None
        self.CidrBlock = None
        self.PrivateIpAddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.CidrBlock = params.get("CidrBlock")
        self.PrivateIpAddressType = params.get("PrivateIpAddressType")
        self.CreatedTime = params.get("CreatedTime")


class VpnConnection(AbstractModel):
    """VPN通道对象。

    """

    def __init__(self):
        """
        :param VpnConnectionId: 通道实例ID。
        :type VpnConnectionId: str
        :param VpnConnectionName: 通道名称。
        :type VpnConnectionName: str
        :param VpcId: VPC实例ID。
        :type VpcId: str
        :param VpnGatewayId: VPN网关实例ID。
        :type VpnGatewayId: str
        :param CustomerGatewayId: 对端网关实例ID。
        :type CustomerGatewayId: str
        :param PreShareKey: 预共享密钥。
        :type PreShareKey: str
        :param VpnProto: 通道传输协议。
        :type VpnProto: str
        :param EncryptProto: 通道加密协议。
        :type EncryptProto: str
        :param RouteType: 路由类型。
        :type RouteType: str
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        :param State: 通道的生产状态，PENDING：生产中，AVAILABLE：运行中，DELETING：删除中。
        :type State: str
        :param NetStatus: 通道连接状态，AVAILABLE：已连接。
        :type NetStatus: str
        :param SecurityPolicyDatabaseSet: SPD。
        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase
        :param IKEOptionsSpecification: IKE选项。
        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`
        :param IPSECOptionsSpecification: IPSEC选择。
        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`
        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.PreShareKey = None
        self.VpnProto = None
        self.EncryptProto = None
        self.RouteType = None
        self.CreatedTime = None
        self.State = None
        self.NetStatus = None
        self.SecurityPolicyDatabaseSet = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None


    def _deserialize(self, params):
        self.VpnConnectionId = params.get("VpnConnectionId")
        self.VpnConnectionName = params.get("VpnConnectionName")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.PreShareKey = params.get("PreShareKey")
        self.VpnProto = params.get("VpnProto")
        self.EncryptProto = params.get("EncryptProto")
        self.RouteType = params.get("RouteType")
        self.CreatedTime = params.get("CreatedTime")
        self.State = params.get("State")
        self.NetStatus = params.get("NetStatus")
        if params.get("SecurityPolicyDatabaseSet") is not None:
            self.SecurityPolicyDatabaseSet = []
            for item in params.get("SecurityPolicyDatabaseSet"):
                obj = SecurityPolicyDatabase()
                obj._deserialize(item)
                self.SecurityPolicyDatabaseSet.append(obj)
        if params.get("IKEOptionsSpecification") is not None:
            self.IKEOptionsSpecification = IKEOptionsSpecification()
            self.IKEOptionsSpecification._deserialize(params.get("IKEOptionsSpecification"))
        if params.get("IPSECOptionsSpecification") is not None:
            self.IPSECOptionsSpecification = IPSECOptionsSpecification()
            self.IPSECOptionsSpecification._deserialize(params.get("IPSECOptionsSpecification"))


class VpnGateway(AbstractModel):
    """VPN网关对象。

    """

    def __init__(self):
        """
        :param VpnGatewayId: 网关实例ID。
        :type VpnGatewayId: str
        :param VpcId: VPC实例ID。
        :type VpcId: str
        :param VpnGatewayName: 网关实例名称。
        :type VpnGatewayName: str
        :param Type: 网关实例类型：'IPSEC', 'SSL'。
        :type Type: str
        :param State: 网关实例状态， 'PENDING'：生产中，'DELETING'：删除中，'AVAILABLE'：运行中。
        :type State: str
        :param PublicIpAddress: 网关公网IP。
        :type PublicIpAddress: str
        :param RenewFlag: 网关续费类型：'NOTIFY_AND_MANUAL_RENEW'：手动续费，'NOTIFY_AND_AUTO_RENEW'：自动续费，'NOT_NOTIFY_AND_NOT_RENEW'：到期不续费。
        :type RenewFlag: str
        :param InstanceChargeType: 网关付费类型：POSTPAID_BY_HOUR：按小时后付费，PREPAID：包年包月预付费，
        :type InstanceChargeType: str
        :param InternetMaxBandwidthOut: 网关出带宽。
        :type InternetMaxBandwidthOut: int
        :param CreatedTime: 创建时间。
        :type CreatedTime: str
        :param ExpiredTime: 预付费网关过期时间。
        :type ExpiredTime: str
        :param IsAddressBlocked: 公网IP是否被封堵。
        :type IsAddressBlocked: bool
        :param NewPurchasePlan: 计费模式变更，PREPAID_TO_POSTPAID：包年包月预付费到期转按小时后付费。
        :type NewPurchasePlan: str
        :param RestrictState: 网关计费装，PROTECTIVELY_ISOLATED：被安全隔离的实例，NORMAL：正常。
        :type RestrictState: str
        :param Zone: 可用区，如：ap-guangzhou-2
        :type Zone: str
        """
        self.VpnGatewayId = None
        self.VpcId = None
        self.VpnGatewayName = None
        self.Type = None
        self.State = None
        self.PublicIpAddress = None
        self.RenewFlag = None
        self.InstanceChargeType = None
        self.InternetMaxBandwidthOut = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.IsAddressBlocked = None
        self.NewPurchasePlan = None
        self.RestrictState = None
        self.Zone = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.Type = params.get("Type")
        self.State = params.get("State")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.RenewFlag = params.get("RenewFlag")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.IsAddressBlocked = params.get("IsAddressBlocked")
        self.NewPurchasePlan = params.get("NewPurchasePlan")
        self.RestrictState = params.get("RestrictState")
        self.Zone = params.get("Zone")