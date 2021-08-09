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


class AcceptAttachCcnInstancesRequest(AbstractModel):
    """AcceptAttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param Instances: 接受关联实例列表。\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AcceptAttachCcnInstancesResponse(AbstractModel):
    """AcceptAttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AccountAttribute(AbstractModel):
    """账户属性对象

    """

    def __init__(self):
        """
        :param AttributeName: 属性名\n        :type AttributeName: str\n        :param AttributeValues: 属性值\n        :type AttributeValues: list of str\n        """
        self.AttributeName = None
        self.AttributeValues = None


    def _deserialize(self, params):
        self.AttributeName = params.get("AttributeName")
        self.AttributeValues = params.get("AttributeValues")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddBandwidthPackageResourcesRequest(AbstractModel):
    """AddBandwidthPackageResources请求参数结构体

    """

    def __init__(self):
        """
        :param ResourceIds: 资源唯一ID，当前支持EIP资源和LB资源，形如'eip-xxxx', 'lb-xxxx'\n        :type ResourceIds: list of str\n        :param BandwidthPackageId: 带宽包唯一标识ID，形如'bwp-xxxx'\n        :type BandwidthPackageId: str\n        :param NetworkType: 带宽包类型，当前支持'BGP'类型，表示内部资源是BGP IP。\n        :type NetworkType: str\n        :param ResourceType: 资源类型，包括'Address', 'LoadBalance'\n        :type ResourceType: str\n        :param Protocol: 带宽包协议类型。当前支持'ipv4'和'ipv6'协议类型。\n        :type Protocol: str\n        """
        self.ResourceIds = None
        self.BandwidthPackageId = None
        self.NetworkType = None
        self.ResourceType = None
        self.Protocol = None


    def _deserialize(self, params):
        self.ResourceIds = params.get("ResourceIds")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.NetworkType = params.get("NetworkType")
        self.ResourceType = params.get("ResourceType")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddBandwidthPackageResourcesResponse(AbstractModel):
    """AddBandwidthPackageResources返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AddIp6RulesRequest(AbstractModel):
    """AddIp6Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxx\n        :type Ip6TranslatorId: str\n        :param Ip6RuleInfos: IPV6转换规则信息\n        :type Ip6RuleInfos: list of Ip6RuleInfo\n        :param Ip6RuleName: IPV6转换规则名称\n        :type Ip6RuleName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddIp6RulesResponse(AbstractModel):
    """AddIp6Rules返回参数结构体

    """

    def __init__(self):
        """
        :param Ip6RuleSet: IPV6转换规则唯一ID数组，形如rule6-xxxxxxxx\n        :type Ip6RuleSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AddressId: `EIP`的`ID`，是`EIP`的唯一标识。\n        :type AddressId: str\n        :param AddressName: `EIP`名称。\n        :type AddressName: str\n        :param AddressStatus: `EIP`状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)\n        :type AddressStatus: str\n        :param AddressIp: 外网IP地址\n        :type AddressIp: str\n        :param InstanceId: 绑定的资源实例`ID`。可能是一个`CVM`，`NAT`。\n        :type InstanceId: str\n        :param CreatedTime: 创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。\n        :type CreatedTime: str\n        :param NetworkInterfaceId: 绑定的弹性网卡ID\n        :type NetworkInterfaceId: str\n        :param PrivateAddressIp: 绑定的资源内网ip\n        :type PrivateAddressIp: str\n        :param IsArrears: 资源隔离状态。true表示eip处于隔离状态，false表示资源处于未隔离状态\n        :type IsArrears: bool\n        :param IsBlocked: 资源封堵状态。true表示eip处于封堵状态，false表示eip处于未封堵状态\n        :type IsBlocked: bool\n        :param IsEipDirectConnection: eip是否支持直通模式。true表示eip支持直通模式，false表示资源不支持直通模式\n        :type IsEipDirectConnection: bool\n        :param AddressType: eip资源类型，包括"CalcIP","WanIP","EIP","AnycastEIP"。其中"CalcIP"表示设备ip，“WanIP”表示普通公网ip，“EIP”表示弹性公网ip，“AnycastEip”表示加速EIP\n        :type AddressType: str\n        :param CascadeRelease: eip是否在解绑后自动释放。true表示eip将会在解绑后自动释放，false表示eip在解绑后不会自动释放\n        :type CascadeRelease: bool\n        :param EipAlgType: EIP ALG开启的协议类型。\n        :type EipAlgType: :class:`tencentcloud.vpc.v20170312.models.AlgType`\n        :param InternetServiceProvider: 弹性公网IP的运营商信息，当前可能返回值包括"CMCC","CTCC","CUCC","BGP"\n        :type InternetServiceProvider: str\n        :param LocalBgp: 是否本地带宽EIP\n        :type LocalBgp: bool\n        :param Bandwidth: 弹性公网IP的带宽值。注意，传统账户类型账户的弹性公网IP没有带宽属性，值为空。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Bandwidth: int\n        :param InternetChargeType: 弹性公网IP的网络计费模式。注意，传统账户类型账户的弹性公网IP没有网络计费模式属性，值为空。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InternetChargeType: str\n        :param TagSet: 弹性公网IP关联的标签列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagSet: list of Tag\n        """
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
        self.EipAlgType = None
        self.InternetServiceProvider = None
        self.LocalBgp = None
        self.Bandwidth = None
        self.InternetChargeType = None
        self.TagSet = None


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
        if params.get("EipAlgType") is not None:
            self.EipAlgType = AlgType()
            self.EipAlgType._deserialize(params.get("EipAlgType"))
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.LocalBgp = params.get("LocalBgp")
        self.Bandwidth = params.get("Bandwidth")
        self.InternetChargeType = params.get("InternetChargeType")
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
        


class AddressChargePrepaid(AbstractModel):
    """用于描述弹性公网IP的费用对象

    """

    def __init__(self):
        """
        :param Period: 购买实例的时长，单位是月。可支持时长：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 24, 36\n        :type Period: int\n        :param AutoRenewFlag: 自动续费标志。0表示手动续费，1表示自动续费，2表示到期不续费。默认缺省为0即手动续费\n        :type AutoRenewFlag: int\n        """
        self.Period = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplate(AbstractModel):
    """IP地址模板

    """

    def __init__(self):
        """
        :param AddressTemplateName: IP地址模板名称。\n        :type AddressTemplateName: str\n        :param AddressTemplateId: IP地址模板实例唯一ID。\n        :type AddressTemplateId: str\n        :param AddressSet: IP地址信息。\n        :type AddressSet: list of str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        """
        self.AddressTemplateName = None
        self.AddressTemplateId = None
        self.AddressSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressSet = params.get("AddressSet")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateGroup(AbstractModel):
    """IP地址模板集合

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP地址模板集合名称。\n        :type AddressTemplateGroupName: str\n        :param AddressTemplateGroupId: IP地址模板集合实例ID，例如：ipmg-dih8xdbq。\n        :type AddressTemplateGroupId: str\n        :param AddressTemplateIdSet: IP地址模板ID。\n        :type AddressTemplateIdSet: list of str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param AddressTemplateSet: IP地址模板实例。\n        :type AddressTemplateSet: list of AddressTemplateItem\n        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateGroupId = None
        self.AddressTemplateIdSet = None
        self.CreatedTime = None
        self.AddressTemplateSet = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateIdSet = params.get("AddressTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("AddressTemplateSet") is not None:
            self.AddressTemplateSet = []
            for item in params.get("AddressTemplateSet"):
                obj = AddressTemplateItem()
                obj._deserialize(item)
                self.AddressTemplateSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateItem(AbstractModel):
    """地址信息

    """

    def __init__(self):
        """
        :param From: 起始地址。\n        :type From: str\n        :param To: 结束地址。\n        :type To: str\n        """
        self.From = None
        self.To = None


    def _deserialize(self, params):
        self.From = params.get("From")
        self.To = params.get("To")
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
        :param AddressId: IP地址ID，例如：ipm-2uw6ujo6。\n        :type AddressId: str\n        :param AddressGroupId: IP地址组ID，例如：ipmg-2uw6ujo6。\n        :type AddressGroupId: str\n        """
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
        


class AlgType(AbstractModel):
    """ALG协议类型

    """

    def __init__(self):
        """
        :param Ftp: Ftp协议Alg功能是否开启\n        :type Ftp: bool\n        :param Sip: Sip协议Alg功能是否开启\n        :type Sip: bool\n        """
        self.Ftp = None
        self.Sip = None


    def _deserialize(self, params):
        self.Ftp = params.get("Ftp")
        self.Sip = params.get("Sip")
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
        :param AddressCount: EIP数量。默认值：1。\n        :type AddressCount: int\n        :param InternetServiceProvider: EIP线路类型。默认值：BGP。
<ul style="margin:0"><li>已开通静态单线IP白名单的用户，可选值：<ul><li>CMCC：中国移动</li>
<li>CTCC：中国电信</li>
<li>CUCC：中国联通</li></ul>注意：仅部分地域支持静态单线IP。</li></ul>\n        :type InternetServiceProvider: str\n        :param InternetChargeType: EIP计费方式。
<ul style="margin:0"><li>已开通标准账户类型白名单的用户，可选值：<ul><li>BANDWIDTH_PACKAGE：[共享带宽包](https://cloud.tencent.com/document/product/684/15255)付费（需额外开通共享带宽包白名单）</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR：带宽按小时后付费</li>
<li>BANDWIDTH_PREPAID_BY_MONTH：包月按带宽预付费</li>
<li>TRAFFIC_POSTPAID_BY_HOUR：流量按小时后付费</li></ul>默认值：TRAFFIC_POSTPAID_BY_HOUR。</li>
<li>未开通标准账户类型白名单的用户，EIP计费方式与其绑定的实例的计费方式一致，无需传递此参数。</li></ul>\n        :type InternetChargeType: str\n        :param InternetMaxBandwidthOut: EIP出带宽上限，单位：Mbps。
<ul style="margin:0"><li>已开通标准账户类型白名单的用户，可选值范围取决于EIP计费方式：<ul><li>BANDWIDTH_PACKAGE：1 Mbps 至 1000 Mbps</li>
<li>BANDWIDTH_POSTPAID_BY_HOUR：1 Mbps 至 100 Mbps</li>
<li>BANDWIDTH_PREPAID_BY_MONTH：1 Mbps 至 200 Mbps</li>
<li>TRAFFIC_POSTPAID_BY_HOUR：1 Mbps 至 100 Mbps</li></ul>默认值：1 Mbps。</li>
<li>未开通标准账户类型白名单的用户，EIP出带宽上限取决于与其绑定的实例的公网出带宽上限，无需传递此参数。</li></ul>\n        :type InternetMaxBandwidthOut: int\n        :param AddressChargePrepaid: 包月按带宽预付费EIP的计费参数。EIP为包月按带宽预付费时，该参数必传，其余场景不需传递\n        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`\n        :param AddressType: EIP类型。默认值：EIP。
<ul style="margin:0"><li>已开通Anycast公网加速白名单的用户，可选值：<ul><li>AnycastEIP：加速IP，可参见 [Anycast 公网加速](https://cloud.tencent.com/document/product/644)</li></ul>注意：仅部分地域支持加速IP。</li></ul>
<ul style="margin:0"><li>已开通精品IP白名单的用户，可选值：<ul><li>HighQualityEIP：精品IP</li></ul>注意：仅部分地域支持精品IP。</li></ul>\n        :type AddressType: str\n        :param AnycastZone: Anycast发布域。
<ul style="margin:0"><li>已开通Anycast公网加速白名单的用户，可选值：<ul><li>ANYCAST_ZONE_GLOBAL：全球发布域（需要额外开通Anycast全球加速白名单）</li><li>ANYCAST_ZONE_OVERSEAS：境外发布域</li><li><b>[已废弃]</b> ANYCAST_ZONE_A：发布域A（已更新为全球发布域）</li><li><b>[已废弃]</b> ANYCAST_ZONE_B：发布域B（已更新为全球发布域）</li></ul>默认值：ANYCAST_ZONE_OVERSEAS。</li></ul>\n        :type AnycastZone: str\n        :param ApplicableForCLB: <b>[已废弃]</b> AnycastEIP不再区分是否负载均衡。原参数说明如下：
AnycastEIP是否用于绑定负载均衡。
<ul style="margin:0"><li>已开通Anycast公网加速白名单的用户，可选值：<ul><li>TRUE：AnycastEIP可绑定对象为负载均衡</li>
<li>FALSE：AnycastEIP可绑定对象为云服务器、NAT网关、高可用虚拟IP等</li></ul>默认值：FALSE。</li></ul>\n        :type ApplicableForCLB: bool\n        :param Tags: 需要关联的标签列表。\n        :type Tags: list of Tag\n        :param BandwidthPackageId: BGP带宽包唯一ID参数。设定该参数且InternetChargeType为BANDWIDTH_PACKAGE，则表示创建的EIP加入该BGP带宽包并采用带宽包计费\n        :type BandwidthPackageId: str\n        :param AddressName: EIP名称，用于申请EIP时用户自定义该EIP的个性化名称，默认值：未命名\n        :type AddressName: str\n        """
        self.AddressCount = None
        self.InternetServiceProvider = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.AddressChargePrepaid = None
        self.AddressType = None
        self.AnycastZone = None
        self.ApplicableForCLB = None
        self.Tags = None
        self.BandwidthPackageId = None
        self.AddressName = None


    def _deserialize(self, params):
        self.AddressCount = params.get("AddressCount")
        self.InternetServiceProvider = params.get("InternetServiceProvider")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("AddressChargePrepaid") is not None:
            self.AddressChargePrepaid = AddressChargePrepaid()
            self.AddressChargePrepaid._deserialize(params.get("AddressChargePrepaid"))
        self.AddressType = params.get("AddressType")
        self.AnycastZone = params.get("AnycastZone")
        self.ApplicableForCLB = params.get("ApplicableForCLB")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.AddressName = params.get("AddressName")
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
        :param AddressSet: 申请到的 EIP 的唯一 ID 列表。\n        :type AddressSet: list of str\n        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddressSet = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AllocateIp6AddressesBandwidthRequest(AbstractModel):
    """AllocateIp6AddressesBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6Addresses: 需要开通公网访问能力的IPV6地址\n        :type Ip6Addresses: list of str\n        :param InternetMaxBandwidthOut: 带宽，单位Mbps。默认是1Mbps\n        :type InternetMaxBandwidthOut: int\n        :param InternetChargeType: 网络计费模式。IPV6当前对标准账户类型支持"TRAFFIC_POSTPAID_BY_HOUR"，对传统账户类型支持"BANDWIDTH_PACKAGE"。默认网络计费模式是"TRAFFIC_POSTPAID_BY_HOUR"。\n        :type InternetChargeType: str\n        :param BandwidthPackageId: 带宽包id，上移账号，申请带宽包计费模式的ipv6地址需要传入.\n        :type BandwidthPackageId: str\n        """
        self.Ip6Addresses = None
        self.InternetMaxBandwidthOut = None
        self.InternetChargeType = None
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.Ip6Addresses = params.get("Ip6Addresses")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InternetChargeType = params.get("InternetChargeType")
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AllocateIp6AddressesBandwidthResponse(AbstractModel):
    """AllocateIp6AddressesBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param AddressSet: 弹性公网 IPV6 的唯一 ID 列表。\n        :type AddressSet: list of str\n        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddressSet = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AddressSet = params.get("AddressSet")
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssignIpv6AddressesRequest(AbstractModel):
    """AssignIpv6Addresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例`ID`，形如：`eni-m6dyj72l`。\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: 指定的`IPv6`地址列表，单次最多指定10个。与入参`Ipv6AddressCount`合并计算配额。与Ipv6AddressCount必填一个。\n        :type Ipv6Addresses: list of Ipv6Address\n        :param Ipv6AddressCount: 自动分配`IPv6`地址个数，内网IP地址个数总和不能超过配数。与入参`Ipv6Addresses`合并计算配额。与Ipv6Addresses必填一个。\n        :type Ipv6AddressCount: int\n        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None
        self.Ipv6AddressCount = None


    def _deserialize(self, params):
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
        :param Ipv6AddressSet: 分配给弹性网卡的`IPv6`地址列表。\n        :type Ipv6AddressSet: list of Ipv6Address\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class AssignIpv6CidrBlockRequest(AbstractModel):
    """AssignIpv6CidrBlock请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。\n        :type VpcId: str\n        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6CidrBlockResponse(AbstractModel):
    """AssignIpv6CidrBlock返回参数结构体

    """

    def __init__(self):
        """
        :param Ipv6CidrBlock: 分配的 `IPv6` 网段。形如：`3402:4e00:20:1000::/56`\n        :type Ipv6CidrBlock: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ipv6CidrBlock = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.RequestId = params.get("RequestId")


class AssignIpv6SubnetCidrBlockRequest(AbstractModel):
    """AssignIpv6SubnetCidrBlock请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。\n        :type VpcId: str\n        :param Ipv6SubnetCidrBlocks: 分配 `IPv6` 子网段列表。\n        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock\n        """
        self.VpcId = None
        self.Ipv6SubnetCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self.Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlocks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssignIpv6SubnetCidrBlockResponse(AbstractModel):
    """AssignIpv6SubnetCidrBlock返回参数结构体

    """

    def __init__(self):
        """
        :param Ipv6SubnetCidrBlockSet: 分配 `IPv6` 子网段列表。\n        :type Ipv6SubnetCidrBlockSet: list of Ipv6SubnetCidrBlock\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ipv6SubnetCidrBlockSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6SubnetCidrBlockSet") is not None:
            self.Ipv6SubnetCidrBlockSet = []
            for item in params.get("Ipv6SubnetCidrBlockSet"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlockSet.append(obj)
        self.RequestId = params.get("RequestId")


class AssignPrivateIpAddressesRequest(AbstractModel):
    """AssignPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。与SecondaryPrivateIpAddressCount至少提供一个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，与PrivateIpAddresses至少提供一个。内网IP地址个数总和不能超过配额数，详见<a href="/document/product/576/18527">弹性网卡使用限制</a>。\n        :type SecondaryPrivateIpAddressCount: int\n        """
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
        :param PrivateIpAddressSet: 内网IP详细信息。\n        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`\n        :type VpcId: str\n        :param CidrBlock: 辅助CIDR。形如：`172.16.0.0/16`\n        :type CidrBlock: str\n        :param AssistantType: 辅助CIDR类型（0：普通辅助CIDR，1：容器辅助CIDR），默认都是0。\n        :type AssistantType: int\n        :param SubnetSet: 辅助CIDR拆分的子网。
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
        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。\n        :type AddressId: str\n        :param InstanceId: 要绑定的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录[控制台](https://console.cloud.tencent.com/cvm)查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/15728) 接口返回值中的`InstanceId`获取。\n        :type InstanceId: str\n        :param NetworkInterfaceId: 要绑定的弹性网卡 ID。 弹性网卡 ID 形如：`eni-11112222`。`NetworkInterfaceId` 与 `InstanceId` 不可同时指定。弹性网卡 ID 可通过登录[控制台](https://console.cloud.tencent.com/vpc/eni)查询，也可通过[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)接口返回值中的`networkInterfaceId`获取。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddress: 要绑定的内网 IP。如果指定了 `NetworkInterfaceId` 则也必须指定 `PrivateIpAddress` ，表示将 EIP 绑定到指定弹性网卡的指定内网 IP 上。同时要确保指定的 `PrivateIpAddress` 是指定的 `NetworkInterfaceId` 上的一个内网 IP。指定弹性网卡的内网 IP 可通过登录[控制台](https://console.cloud.tencent.com/vpc/eni)查询，也可通过[DescribeNetworkInterfaces](https://cloud.tencent.com/document/api/215/15817)接口返回值中的`privateIpAddress`获取。\n        :type PrivateIpAddress: str\n        :param EipDirectConnection: 指定绑定时是否设置直通。弹性公网 IP 直通请参见 [EIP 直通](https://cloud.tencent.com/document/product/1199/41709)。取值：True、False，默认值为 False。当绑定 CVM 实例、EKS 弹性集群时，可设定此参数为 True。此参数目前处于内测中，如需使用，请提交 [工单申请](https://console.cloud.tencent.com/workorder/category?level1_id=6&level2_id=163&source=0&data_title=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20CLB&level3_id=1071&queue=96&scene_code=34639&step=2)。\n        :type EipDirectConnection: bool\n        """
        self.AddressId = None
        self.InstanceId = None
        self.NetworkInterfaceId = None
        self.PrivateIpAddress = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InstanceId = params.get("InstanceId")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.EipDirectConnection = params.get("EipDirectConnection")
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
        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class AssociateDhcpIpWithAddressIpRequest(AbstractModel):
    """AssociateDhcpIpWithAddressIp请求参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpId: `DhcpIp`唯一`ID`，形如：`dhcpip-9o233uri`。必须是没有绑定`EIP`的`DhcpIp`\n        :type DhcpIpId: str\n        :param AddressIp: 弹性公网`IP`。必须是没有绑定`DhcpIp`的`EIP`\n        :type AddressIp: str\n        """
        self.DhcpIpId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.DhcpIpId = params.get("DhcpIpId")
        self.AddressIp = params.get("AddressIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDhcpIpWithAddressIpResponse(AbstractModel):
    """AssociateDhcpIpWithAddressIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateDirectConnectGatewayNatGatewayRequest(AbstractModel):
    """AssociateDirectConnectGatewayNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 专线网关ID。\n        :type VpcId: str\n        :param NatGatewayId: NAT网关ID。\n        :type NatGatewayId: str\n        :param DirectConnectGatewayId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type DirectConnectGatewayId: str\n        """
        self.VpcId = None
        self.NatGatewayId = None
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDirectConnectGatewayNatGatewayResponse(AbstractModel):
    """AssociateDirectConnectGatewayNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNatGatewayAddressRequest(AbstractModel):
    """AssociateNatGatewayAddress请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param AddressCount: 需要申请的弹性IP个数，系统会按您的要求生产N个弹性IP, 其中AddressCount和PublicAddresses至少传递一个。\n        :type AddressCount: int\n        :param PublicIpAddresses: 绑定NAT网关的弹性IP数组，其中AddressCount和PublicAddresses至少传递一个。\n        :type PublicIpAddresses: list of str\n        :param Zone: 弹性IP可用区，自动分配弹性IP时传递。\n        :type Zone: str\n        """
        self.NatGatewayId = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateNatGatewayAddressResponse(AbstractModel):
    """AssociateNatGatewayAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkAclSubnetsRequest(AbstractModel):
    """AssociateNetworkAclSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkAclId: 网络ACL实例ID。例如：acl-12345678。\n        :type NetworkAclId: str\n        :param SubnetIds: 子网实例ID数组。例如：[subnet-12345678]\n        :type SubnetIds: list of str\n        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateNetworkAclSubnetsResponse(AbstractModel):
    """AssociateNetworkAclSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 弹性网卡实例ID。形如：eni-pxir56ns。每次请求的实例的上限为100。\n        :type NetworkInterfaceIds: list of str\n        :param SecurityGroupIds: 安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。\n        :type SecurityGroupIds: list of str\n        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """AssociateNetworkInterfaceSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachCcnInstancesRequest(AbstractModel):
    """AttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param Instances: 关联网络实例列表\n        :type Instances: list of CcnInstance\n        :param CcnUin: CCN所属UIN（根账号），默认当前账号所属UIN\n        :type CcnUin: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachCcnInstancesResponse(AbstractModel):
    """AttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AttachClassicLinkVpcRequest(AbstractModel):
    """AttachClassicLinkVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID\n        :type VpcId: str\n        :param InstanceIds: CVM实例ID\n        :type InstanceIds: list of str\n        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AttachClassicLinkVpcResponse(AbstractModel):
    """AttachClassicLinkVpc返回参数结构体

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
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param InstanceId: CVM实例ID。形如：ins-r8hr2upy。\n        :type InstanceId: str\n        :param AttachType: 网卡的挂载类型：0 标准型，1扩展型，默认值0。\n        :type AttachType: int\n        """
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.AttachType = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.AttachType = params.get("AttachType")
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


class AuditCrossBorderComplianceRequest(AbstractModel):
    """AuditCrossBorderCompliance请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceProvider: 服务商, 可选值：`UNICOM`。\n        :type ServiceProvider: str\n        :param ComplianceId: 表单唯一`ID`。\n        :type ComplianceId: int\n        :param AuditBehavior: 通过：`APPROVED `，拒绝：`DENY`。\n        :type AuditBehavior: str\n        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.AuditBehavior = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.AuditBehavior = params.get("AuditBehavior")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditCrossBorderComplianceResponse(AbstractModel):
    """AuditCrossBorderCompliance返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BandwidthPackage(AbstractModel):
    """描述带宽包信息的结构

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一标识Id\n        :type BandwidthPackageId: str\n        :param NetworkType: 带宽包类型，包括'BGP','SINGLEISP','ANYCAST'\n        :type NetworkType: str\n        :param ChargeType: 带宽包计费类型，包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'\n        :type ChargeType: str\n        :param BandwidthPackageName: 带宽包名称\n        :type BandwidthPackageName: str\n        :param CreatedTime: 带宽包创建时间。按照`ISO8601`标准表示，并且使用`UTC`时间。格式为：`YYYY-MM-DDThh:mm:ssZ`。\n        :type CreatedTime: str\n        :param Status: 带宽包状态，包括'CREATING','CREATED','DELETING','DELETED'\n        :type Status: str\n        :param ResourceSet: 带宽包资源信息\n        :type ResourceSet: list of Resource\n        :param Bandwidth: 带宽包限速大小。单位：Mbps，-1表示不限速。\n        :type Bandwidth: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BandwidthPackageBillBandwidth(AbstractModel):
    """后付费共享带宽包的当前计费用量

    """

    def __init__(self):
        """
        :param BandwidthUsage: 当前计费用量，单位为 Mbps\n        :type BandwidthUsage: int\n        """
        self.BandwidthUsage = None


    def _deserialize(self, params):
        self.BandwidthUsage = params.get("BandwidthUsage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCN(AbstractModel):
    """云联网（CCN）对象

    """

    def __init__(self):
        """
        :param CcnId: 云联网唯一ID\n        :type CcnId: str\n        :param CcnName: 云联网名称\n        :type CcnName: str\n        :param CcnDescription: 云联网描述信息\n        :type CcnDescription: str\n        :param InstanceCount: 关联实例数量\n        :type InstanceCount: int\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param State: 实例状态， 'ISOLATED': 隔离中（欠费停服），'AVAILABLE'：运行中。\n        :type State: str\n        :param QosLevel: 实例服务质量，’PT’：白金，'AU'：金，'AG'：银。\n        :type QosLevel: str\n        :param InstanceChargeType: 付费类型，PREPAID为预付费，POSTPAID为后付费。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InstanceChargeType: str\n        :param BandwidthLimitType: 限速类型，INTER_REGION_LIMIT为地域间限速；OUTER_REGION_LIMIT为地域出口限速。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BandwidthLimitType: str\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        :param RoutePriorityFlag: 是否支持云联网路由优先级的功能。False：不支持，True：支持。\n        :type RoutePriorityFlag: bool\n        :param RouteTableCount: 实例关联的路由表个数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableCount: int\n        :param RouteTableFlag: 是否开启云联网多路由表特性。False：未开启，True：开启。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableFlag: bool\n        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None
        self.InstanceCount = None
        self.CreateTime = None
        self.State = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None
        self.TagSet = None
        self.RoutePriorityFlag = None
        self.RouteTableCount = None
        self.RouteTableFlag = None


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
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.RoutePriorityFlag = params.get("RoutePriorityFlag")
        self.RouteTableCount = params.get("RouteTableCount")
        self.RouteTableFlag = params.get("RouteTableFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnAttachedInstance(AbstractModel):
    """云联网（CCN）关联实例（Instance）对象

    """

    def __init__(self):
        """
        :param CcnId: 云联网实例ID。\n        :type CcnId: str\n        :param InstanceType: 关联实例类型：
<li>`VPC`：私有网络</li>
<li>`DIRECTCONNECT`：专线网关</li>
<li>`BMVPC`：黑石私有网络</li>\n        :type InstanceType: str\n        :param InstanceId: 关联实例ID。\n        :type InstanceId: str\n        :param InstanceName: 关联实例名称。\n        :type InstanceName: str\n        :param InstanceRegion: 关联实例所属大区，例如：ap-guangzhou。\n        :type InstanceRegion: str\n        :param InstanceUin: 关联实例所属UIN（根账号）。\n        :type InstanceUin: str\n        :param CidrBlock: 关联实例CIDR。\n        :type CidrBlock: list of str\n        :param State: 关联实例状态：
<li>`PENDING`：申请中</li>
<li>`ACTIVE`：已连接</li>
<li>`EXPIRED`：已过期</li>
<li>`REJECTED`：已拒绝</li>
<li>`DELETED`：已删除</li>
<li>`FAILED`：失败的（2小时后将异步强制解关联）</li>
<li>`ATTACHING`：关联中</li>
<li>`DETACHING`：解关联中</li>
<li>`DETACHFAILED`：解关联失败（2小时后将异步强制解关联）</li>\n        :type State: str\n        :param AttachedTime: 关联时间。\n        :type AttachedTime: str\n        :param CcnUin: 云联网所属UIN（根账号）。\n        :type CcnUin: str\n        :param InstanceArea: 关联实例所属的大地域，如: CHINA_MAINLAND\n        :type InstanceArea: str\n        :param Description: 备注\n        :type Description: str\n        :param RouteTableId: 路由表ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableId: str\n        :param RouteTableName: 路由表名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableName: str\n        """
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
        self.InstanceArea = None
        self.Description = None
        self.RouteTableId = None
        self.RouteTableName = None


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
        self.InstanceArea = params.get("InstanceArea")
        self.Description = params.get("Description")
        self.RouteTableId = params.get("RouteTableId")
        self.RouteTableName = params.get("RouteTableName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnBandwidthInfo(AbstractModel):
    """用于描述云联网地域间限速带宽实例的信息。

    """

    def __init__(self):
        """
        :param CcnId: 带宽所属的云联网ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CcnId: str\n        :param CreatedTime: 实例的创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        :param ExpiredTime: 实例的过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpiredTime: str\n        :param RegionFlowControlId: 带宽实例的唯一ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RegionFlowControlId: str\n        :param RenewFlag: 带宽是否自动续费的标记。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewFlag: str\n        :param CcnRegionBandwidthLimit: 描述带宽的地域和限速上限信息。在地域间限速的情况下才会返回参数，出口限速模式不返回。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CcnRegionBandwidthLimit: :class:`tencentcloud.vpc.v20170312.models.CcnRegionBandwidthLimit`\n        """
        self.CcnId = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.RegionFlowControlId = None
        self.RenewFlag = None
        self.CcnRegionBandwidthLimit = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.RegionFlowControlId = params.get("RegionFlowControlId")
        self.RenewFlag = params.get("RenewFlag")
        if params.get("CcnRegionBandwidthLimit") is not None:
            self.CcnRegionBandwidthLimit = CcnRegionBandwidthLimit()
            self.CcnRegionBandwidthLimit._deserialize(params.get("CcnRegionBandwidthLimit"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnInstance(AbstractModel):
    """云联网（CCN）关联实例（Instance）对象。

    """

    def __init__(self):
        """
        :param InstanceId: 关联实例ID。\n        :type InstanceId: str\n        :param InstanceRegion: 关联实例ID所属大区，例如：ap-guangzhou。\n        :type InstanceRegion: str\n        :param InstanceType: 关联实例类型，可选值：
<li>`VPC`：私有网络</li>
<li>`DIRECTCONNECT`：专线网关</li>
<li>`BMVPC`：黑石私有网络</li>
<li>`VPNGW`：VPNGW类型</li>\n        :type InstanceType: str\n        :param Description: 备注\n        :type Description: str\n        :param RouteTableId: 实例关联的路由表ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RouteTableId: str\n        """
        self.InstanceId = None
        self.InstanceRegion = None
        self.InstanceType = None
        self.Description = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceRegion = params.get("InstanceRegion")
        self.InstanceType = params.get("InstanceType")
        self.Description = params.get("Description")
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnRegionBandwidthLimit(AbstractModel):
    """云联网（CCN）地域出带宽上限

    """

    def __init__(self):
        """
        :param Region: 地域，例如：ap-guangzhou\n        :type Region: str\n        :param BandwidthLimit: 出带宽上限，单位：Mbps\n        :type BandwidthLimit: int\n        :param IsBm: 是否黑石地域，默认`false`。\n        :type IsBm: bool\n        :param DstRegion: 目的地域，例如：ap-shanghai
注意：此字段可能返回 null，表示取不到有效值。\n        :type DstRegion: str\n        :param DstIsBm: 目的地域是否为黑石地域，默认`false`。\n        :type DstIsBm: bool\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcnRoute(AbstractModel):
    """CCN路由策略对象

    """

    def __init__(self):
        """
        :param RouteId: 路由策略ID\n        :type RouteId: str\n        :param DestinationCidrBlock: 目的端\n        :type DestinationCidrBlock: str\n        :param InstanceType: 下一跳类型（关联实例类型），所有类型：VPC、DIRECTCONNECT\n        :type InstanceType: str\n        :param InstanceId: 下一跳（关联实例）\n        :type InstanceId: str\n        :param InstanceName: 下一跳名称（关联实例名称）\n        :type InstanceName: str\n        :param InstanceRegion: 下一跳所属地域（关联实例所属地域）\n        :type InstanceRegion: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        :param Enabled: 路由是否启用\n        :type Enabled: bool\n        :param InstanceUin: 关联实例所属UIN（根账号）\n        :type InstanceUin: str\n        :param ExtraState: 路由的扩展状态\n        :type ExtraState: str\n        :param IsBgp: 是否动态路由\n        :type IsBgp: bool\n        :param RoutePriority: 路由优先级\n        :type RoutePriority: int\n        :param InstanceExtraName: 下一跳扩展名称（关联实例的扩展名称）\n        :type InstanceExtraName: str\n        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.InstanceType = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceRegion = None
        self.UpdateTime = None
        self.Enabled = None
        self.InstanceUin = None
        self.ExtraState = None
        self.IsBgp = None
        self.RoutePriority = None
        self.InstanceExtraName = None


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
        self.ExtraState = params.get("ExtraState")
        self.IsBgp = params.get("IsBgp")
        self.RoutePriority = params.get("RoutePriority")
        self.InstanceExtraName = params.get("InstanceExtraName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAssistantCidrRequest(AbstractModel):
    """CheckAssistantCidr请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`\n        :type VpcId: str\n        :param NewCidrBlocks: 待添加的负载CIDR。CIDR数组，格式如["10.0.0.0/16", "172.16.0.0/16"]。入参NewCidrBlocks和OldCidrBlocks至少需要其一。\n        :type NewCidrBlocks: list of str\n        :param OldCidrBlocks: 待删除的负载CIDR。CIDR数组，格式如["10.0.0.0/16", "172.16.0.0/16"]。入参NewCidrBlocks和OldCidrBlocks至少需要其一。\n        :type OldCidrBlocks: list of str\n        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckAssistantCidrResponse(AbstractModel):
    """CheckAssistantCidr返回参数结构体

    """

    def __init__(self):
        """
        :param ConflictSourceSet: 冲突资源信息数组。\n        :type ConflictSourceSet: list of ConflictSource\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ConflictSourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ConflictSourceSet") is not None:
            self.ConflictSourceSet = []
            for item in params.get("ConflictSourceSet"):
                obj = ConflictSource()
                obj._deserialize(item)
                self.ConflictSourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class CheckDefaultSubnetRequest(AbstractModel):
    """CheckDefaultSubnet请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。\n        :type Zone: str\n        """
        self.Zone = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDefaultSubnetResponse(AbstractModel):
    """CheckDefaultSubnet返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 检查结果。true为可以创建默认子网，false为不可以创建默认子网。\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CheckNetDetectStateRequest(AbstractModel):
    """CheckNetDetectState请求参数结构体

    """

    def __init__(self):
        """
        :param DetectDestinationIp: 探测目的IPv4地址数组，最多两个。\n        :type DetectDestinationIp: list of str\n        :param NextHopType: 下一跳类型，目前我们支持的类型有：
VPN：VPN网关；
DIRECTCONNECT：专线网关；
PEERCONNECTION：对等连接；
NAT：NAT网关；
NORMAL_CVM：普通云服务器；\n        :type NextHopType: str\n        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；\n        :type NextHopDestination: str\n        :param NetDetectId: 网络探测实例ID。形如：netd-12345678。该参数与（VpcId，SubnetId，NetDetectName），至少要有一个。当NetDetectId存在时，使用NetDetectId。\n        :type NetDetectId: str\n        :param VpcId: `VPC`实例`ID`。形如：`vpc-12345678`。该参数与（SubnetId，NetDetectName）配合使用，与NetDetectId至少要有一个。当NetDetectId存在时，使用NetDetectId。\n        :type VpcId: str\n        :param SubnetId: 子网实例ID。形如：subnet-12345678。该参数与（VpcId，NetDetectName）配合使用，与NetDetectId至少要有一个。当NetDetectId存在时，使用NetDetectId。\n        :type SubnetId: str\n        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。该参数与（VpcId，SubnetId）配合使用，与NetDetectId至少要有一个。当NetDetectId存在时，使用NetDetectId。\n        :type NetDetectName: str\n        """
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectId = None
        self.VpcId = None
        self.SubnetId = None
        self.NetDetectName = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectId = params.get("NetDetectId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetDetectName = params.get("NetDetectName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckNetDetectStateResponse(AbstractModel):
    """CheckNetDetectState返回参数结构体

    """

    def __init__(self):
        """
        :param NetDetectIpStateSet: 网络探测验证结果对象数组。\n        :type NetDetectIpStateSet: list of NetDetectIpState\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetDetectIpStateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectIpStateSet") is not None:
            self.NetDetectIpStateSet = []
            for item in params.get("NetDetectIpStateSet"):
                obj = NetDetectIpState()
                obj._deserialize(item)
                self.NetDetectIpStateSet.append(obj)
        self.RequestId = params.get("RequestId")


class CidrForCcn(AbstractModel):
    """用于发布云联网的cidr信息

    """

    def __init__(self):
        """
        :param Cidr: local cidr值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cidr: str\n        :param PublishedToVbc: 是否发布到了云联网。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublishedToVbc: bool\n        """
        self.Cidr = None
        self.PublishedToVbc = None


    def _deserialize(self, params):
        self.Cidr = params.get("Cidr")
        self.PublishedToVbc = params.get("PublishedToVbc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClassicLinkInstance(AbstractModel):
    """私有网络和基础网络互通设备

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID\n        :type VpcId: str\n        :param InstanceId: 云服务器实例唯一ID\n        :type InstanceId: str\n        """
        self.VpcId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneSecurityGroupRequest(AbstractModel):
    """CloneSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。未提供参数时，克隆后的安全组名称和SecurityGroupId对应的安全组名称相同。\n        :type GroupName: str\n        :param GroupDescription: 安全组备注，最多100个字符。未提供参数时，克隆后的安全组备注和SecurityGroupId对应的安全组备注相同。\n        :type GroupDescription: str\n        :param ProjectId: 项目ID，默认0。可在qcloud控制台项目管理页面查询到。\n        :type ProjectId: str\n        :param RemoteRegion: 源Region,跨地域克隆安全组时，需要传入源安全组所属地域信息，例如：克隆广州的安全组到上海，则这里需要传入广州安全的地域信息：ap-guangzhou。\n        :type RemoteRegion: str\n        """
        self.SecurityGroupId = None
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.RemoteRegion = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        self.RemoteRegion = params.get("RemoteRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloneSecurityGroupResponse(AbstractModel):
    """CloneSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全组对象。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class ConflictItem(AbstractModel):
    """冲突资源条目信息。

    """

    def __init__(self):
        """
        :param ConfilctId: 冲突资源的ID\n        :type ConfilctId: str\n        :param DestinationItem: 冲突目的资源\n        :type DestinationItem: str\n        """
        self.ConfilctId = None
        self.DestinationItem = None


    def _deserialize(self, params):
        self.ConfilctId = params.get("ConfilctId")
        self.DestinationItem = params.get("DestinationItem")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConflictSource(AbstractModel):
    """冲突资源信息。

    """

    def __init__(self):
        """
        :param ConflictSourceId: 冲突资源ID\n        :type ConflictSourceId: str\n        :param SourceItem: 冲突资源\n        :type SourceItem: str\n        :param ConflictItemSet: 冲突资源条目信息\n        :type ConflictItemSet: list of ConflictItem\n        """
        self.ConflictSourceId = None
        self.SourceItem = None
        self.ConflictItemSet = None


    def _deserialize(self, params):
        self.ConflictSourceId = params.get("ConflictSourceId")
        self.SourceItem = params.get("SourceItem")
        if params.get("ConflictItemSet") is not None:
            self.ConflictItemSet = []
            for item in params.get("ConflictItemSet"):
                obj = ConflictItem()
                obj._deserialize(item)
                self.ConflictItemSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateGroupRequest(AbstractModel):
    """CreateAddressTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroupName: IP地址模版集合名称。\n        :type AddressTemplateGroupName: str\n        :param AddressTemplateIds: IP地址模版实例ID，例如：ipm-mdunqeb6。\n        :type AddressTemplateIds: list of str\n        """
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateGroupResponse(AbstractModel):
    """CreateAddressTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroup: IP地址模板集合对象。\n        :type AddressTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AddressTemplateName: IP地址模版名称\n        :type AddressTemplateName: str\n        :param Addresses: 地址信息，支持 IP、CIDR、IP 范围。\n        :type Addresses: list of str\n        """
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAddressTemplateResponse(AbstractModel):
    """CreateAddressTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplate: IP地址模板对象。\n        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplate`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddressTemplate = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplate()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.RequestId = params.get("RequestId")


class CreateAndAttachNetworkInterfaceRequest(AbstractModel):
    """CreateAndAttachNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。\n        :type NetworkInterfaceName: str\n        :param SubnetId: 弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。\n        :type SubnetId: str\n        :param InstanceId: 云服务器实例ID。\n        :type InstanceId: str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。\n        :type SecondaryPrivateIpAddressCount: int\n        :param SecurityGroupIds: 指定绑定的安全组，例如：['sg-1dd51d']。\n        :type SecurityGroupIds: list of str\n        :param NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。\n        :type NetworkInterfaceDescription: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        :param AttachType: 绑定类型：0 标准型 1 扩展型。\n        :type AttachType: int\n        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.InstanceId = None
        self.PrivateIpAddresses = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.NetworkInterfaceDescription = None
        self.Tags = None
        self.AttachType = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        if params.get("PrivateIpAddresses") is not None:
            self.PrivateIpAddresses = []
            for item in params.get("PrivateIpAddresses"):
                obj = PrivateIpAddressSpecification()
                obj._deserialize(item)
                self.PrivateIpAddresses.append(obj)
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.AttachType = params.get("AttachType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAndAttachNetworkInterfaceResponse(AbstractModel):
    """CreateAndAttachNetworkInterface返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterface: 弹性网卡实例。\n        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetworkInterface = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkInterface") is not None:
            self.NetworkInterface = NetworkInterface()
            self.NetworkInterface._deserialize(params.get("NetworkInterface"))
        self.RequestId = params.get("RequestId")


class CreateAssistantCidrRequest(AbstractModel):
    """CreateAssistantCidr请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`\n        :type VpcId: str\n        :param CidrBlocks: CIDR数组，格式如["10.0.0.0/16", "172.16.0.0/16"]\n        :type CidrBlocks: list of str\n        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAssistantCidrResponse(AbstractModel):
    """CreateAssistantCidr返回参数结构体

    """

    def __init__(self):
        """
        :param AssistantCidrSet: 辅助CIDR数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssistantCidrSet: list of AssistantCidr\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AssistantCidrSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateBandwidthPackageRequest(AbstractModel):
    """CreateBandwidthPackage请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkType: 带宽包类型，包括'HIGH_QUALITY_BGP', 'BGP'，'SINGLEISP'，'ANYCAST'\n        :type NetworkType: str\n        :param ChargeType: 带宽包计费类型，包括‘TOP5_POSTPAID_BY_MONTH’，‘PERCENT95_POSTPAID_BY_MONTH’\n        :type ChargeType: str\n        :param BandwidthPackageName: 带宽包名字\n        :type BandwidthPackageName: str\n        :param BandwidthPackageCount: 带宽包数量(传统账户类型只能填1)\n        :type BandwidthPackageCount: int\n        :param InternetMaxBandwidth: 带宽包限速大小。单位：Mbps，-1表示不限速。该功能当前内测中，暂不对外开放。\n        :type InternetMaxBandwidth: int\n        :param Tags: 需要关联的标签列表。\n        :type Tags: list of Tag\n        :param Protocol: 带宽包协议类型。当前支持'ipv4'和'ipv6'协议带宽包，默认值是'ipv4'。\n        :type Protocol: str\n        """
        self.NetworkType = None
        self.ChargeType = None
        self.BandwidthPackageName = None
        self.BandwidthPackageCount = None
        self.InternetMaxBandwidth = None
        self.Tags = None
        self.Protocol = None


    def _deserialize(self, params):
        self.NetworkType = params.get("NetworkType")
        self.ChargeType = params.get("ChargeType")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.BandwidthPackageCount = params.get("BandwidthPackageCount")
        self.InternetMaxBandwidth = params.get("InternetMaxBandwidth")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBandwidthPackageResponse(AbstractModel):
    """CreateBandwidthPackage返回参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一ID\n        :type BandwidthPackageId: str\n        :param BandwidthPackageIds: 带宽包唯一ID列表(申请数量大于1时有效)\n        :type BandwidthPackageIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CcnName: CCN名称，最大长度不能超过60个字节。\n        :type CcnName: str\n        :param CcnDescription: CCN描述信息，最大长度不能超过100个字节。\n        :type CcnDescription: str\n        :param QosLevel: CCN服务质量，'PT'：白金，'AU'：金，'AG'：银，默认为‘AU’。\n        :type QosLevel: str\n        :param InstanceChargeType: 计费模式，PREPAID：表示预付费，即包年包月，POSTPAID：表示后付费，即按量计费。默认：POSTPAID。\n        :type InstanceChargeType: str\n        :param BandwidthLimitType: 限速类型，OUTER_REGION_LIMIT表示地域出口限速，INTER_REGION_LIMIT为地域间限速，默认为OUTER_REGION_LIMIT。预付费模式仅支持地域间限速，后付费模式支持地域间限速和地域出口限速。\n        :type BandwidthLimitType: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.CcnName = None
        self.CcnDescription = None
        self.QosLevel = None
        self.InstanceChargeType = None
        self.BandwidthLimitType = None
        self.Tags = None


    def _deserialize(self, params):
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        self.QosLevel = params.get("QosLevel")
        self.InstanceChargeType = params.get("InstanceChargeType")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
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
        


class CreateCcnResponse(AbstractModel):
    """CreateCcn返回参数结构体

    """

    def __init__(self):
        """
        :param Ccn: 云联网（CCN）对象。\n        :type Ccn: :class:`tencentcloud.vpc.v20170312.models.CCN`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CustomerGatewayName: 对端网关名称，可任意命名，但不得超过60个字符。\n        :type CustomerGatewayName: str\n        :param IpAddress: 对端网关公网IP。\n        :type IpAddress: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.Tags = None


    def _deserialize(self, params):
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
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
        


class CreateCustomerGatewayResponse(AbstractModel):
    """CreateCustomerGateway返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGateway: 对端网关对象\n        :type CustomerGateway: :class:`tencentcloud.vpc.v20170312.models.CustomerGateway`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CustomerGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CustomerGateway") is not None:
            self.CustomerGateway = CustomerGateway()
            self.CustomerGateway._deserialize(params.get("CustomerGateway"))
        self.RequestId = params.get("RequestId")


class CreateDefaultSecurityGroupRequest(AbstractModel):
    """CreateDefaultSecurityGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ProjectId: 项目ID，默认0。可在qcloud控制台项目管理页面查询到。\n        :type ProjectId: str\n        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDefaultSecurityGroupResponse(AbstractModel):
    """CreateDefaultSecurityGroup返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全组对象。\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateDefaultVpcRequest(AbstractModel):
    """CreateDefaultVpc请求参数结构体

    """

    def __init__(self):
        """
        :param Zone: 子网所在的可用区，该参数可通过[DescribeZones](https://cloud.tencent.com/document/product/213/15707)接口获取，例如ap-guangzhou-1，不指定时将随机选择可用区。\n        :type Zone: str\n        :param Force: 是否强制返回默认VPC。\n        :type Force: bool\n        """
        self.Zone = None
        self.Force = None


    def _deserialize(self, params):
        self.Zone = params.get("Zone")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDefaultVpcResponse(AbstractModel):
    """CreateDefaultVpc返回参数结构体

    """

    def __init__(self):
        """
        :param Vpc: 默认VPC和子网ID\n        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.DefaultVpcSubnet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Vpc = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Vpc") is not None:
            self.Vpc = DefaultVpcSubnet()
            self.Vpc._deserialize(params.get("Vpc"))
        self.RequestId = params.get("RequestId")


class CreateDhcpIpRequest(AbstractModel):
    """CreateDhcpIp请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私有网络`ID`。\n        :type VpcId: str\n        :param SubnetId: 子网`ID`。\n        :type SubnetId: str\n        :param DhcpIpName: `DhcpIp`名称。\n        :type DhcpIpName: str\n        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数。总数不能超过64个。\n        :type SecondaryPrivateIpAddressCount: int\n        """
        self.VpcId = None
        self.SubnetId = None
        self.DhcpIpName = None
        self.SecondaryPrivateIpAddressCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DhcpIpName = params.get("DhcpIpName")
        self.SecondaryPrivateIpAddressCount = params.get("SecondaryPrivateIpAddressCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDhcpIpResponse(AbstractModel):
    """CreateDhcpIp返回参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpSet: 新创建的`DhcpIp`信息\n        :type DhcpIpSet: list of DhcpIp\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DhcpIpSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DhcpIpSet") is not None:
            self.DhcpIpSet = []
            for item in params.get("DhcpIpSet"):
                obj = DhcpIp()
                obj._deserialize(item)
                self.DhcpIpSet.append(obj)
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：dcg-prpqlmg1\n        :type DirectConnectGatewayId: str\n        :param Routes: 需要连通的IDC网段列表\n        :type Routes: list of DirectConnectGatewayCcnRoute\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """CreateDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDirectConnectGatewayRequest(AbstractModel):
    """CreateDirectConnectGateway请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayName: 专线网关名称\n        :type DirectConnectGatewayName: str\n        :param NetworkType: 关联网络类型，可选值：
<li>VPC - 私有网络</li>
<li>CCN - 云联网</li>\n        :type NetworkType: str\n        :param NetworkInstanceId: <li>NetworkType 为 VPC 时，这里传值为私有网络实例ID</li>
<li>NetworkType 为 CCN 时，这里传值为云联网实例ID</li>\n        :type NetworkInstanceId: str\n        :param GatewayType: 网关类型，可选值：
<li>NORMAL - （默认）标准型，注：云联网只支持标准型</li>
<li>NAT - NAT型</li>NAT类型支持网络地址转换配置，类型确定后不能修改；一个私有网络可以创建一个NAT类型的专线网关和一个非NAT类型的专线网关\n        :type GatewayType: str\n        :param ModeType: 云联网路由发布模式，可选值：`standard`（标准模式）、`exquisite`（精细模式）。只有云联网类型专线网关才支持`ModeType`。\n        :type ModeType: str\n        :param Zone: 专线网关可用区\n        :type Zone: str\n        """
        self.DirectConnectGatewayName = None
        self.NetworkType = None
        self.NetworkInstanceId = None
        self.GatewayType = None
        self.ModeType = None
        self.Zone = None


    def _deserialize(self, params):
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.NetworkType = params.get("NetworkType")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        self.GatewayType = params.get("GatewayType")
        self.ModeType = params.get("ModeType")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDirectConnectGatewayResponse(AbstractModel):
    """CreateDirectConnectGateway返回参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGateway: 专线网关对象。\n        :type DirectConnectGateway: :class:`tencentcloud.vpc.v20170312.models.DirectConnectGateway`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DirectConnectGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DirectConnectGateway") is not None:
            self.DirectConnectGateway = DirectConnectGateway()
            self.DirectConnectGateway._deserialize(params.get("DirectConnectGateway"))
        self.RequestId = params.get("RequestId")


class CreateFlowLogRequest(AbstractModel):
    """CreateFlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私用网络ID或者统一ID，建议使用统一ID\n        :type VpcId: str\n        :param FlowLogName: 流日志实例名字\n        :type FlowLogName: str\n        :param ResourceType: 流日志所属资源类型，VPC|SUBNET|NETWORKINTERFACE\n        :type ResourceType: str\n        :param ResourceId: 资源唯一ID\n        :type ResourceId: str\n        :param TrafficType: 流日志采集类型，ACCEPT|REJECT|ALL\n        :type TrafficType: str\n        :param CloudLogId: 流日志存储ID\n        :type CloudLogId: str\n        :param FlowLogDescription: 流日志实例描述\n        :type FlowLogDescription: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.VpcId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.FlowLogDescription = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.FlowLogDescription = params.get("FlowLogDescription")
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
        


class CreateFlowLogResponse(AbstractModel):
    """CreateFlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param FlowLog: 创建的流日志信息\n        :type FlowLog: list of FlowLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowLog = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.RequestId = params.get("RequestId")


class CreateHaVipRequest(AbstractModel):
    """CreateHaVip请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `HAVIP`所在私有网络`ID`。\n        :type VpcId: str\n        :param SubnetId: `HAVIP`所在子网`ID`。\n        :type SubnetId: str\n        :param HaVipName: `HAVIP`名称。\n        :type HaVipName: str\n        :param Vip: 指定虚拟IP地址，必须在`VPC`网段内且未被占用。不指定则自动分配。\n        :type Vip: str\n        """
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
        :param HaVip: `HAVIP`对象。\n        :type HaVip: :class:`tencentcloud.vpc.v20170312.models.HaVip`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Ip6TranslatorName: 转换实例名称\n        :type Ip6TranslatorName: str\n        :param Ip6TranslatorCount: 创建转换实例数量，默认是1个\n        :type Ip6TranslatorCount: int\n        :param Ip6InternetServiceProvider: 转换实例运营商属性，可取"CMCC","CTCC","CUCC","BGP"\n        :type Ip6InternetServiceProvider: str\n        """
        self.Ip6TranslatorName = None
        self.Ip6TranslatorCount = None
        self.Ip6InternetServiceProvider = None


    def _deserialize(self, params):
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")
        self.Ip6TranslatorCount = params.get("Ip6TranslatorCount")
        self.Ip6InternetServiceProvider = params.get("Ip6InternetServiceProvider")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIp6TranslatorsResponse(AbstractModel):
    """CreateIp6Translators返回参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorSet: 转换实例的唯一ID数组，形如"ip6-xxxxxxxx"\n        :type Ip6TranslatorSet: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ip6TranslatorSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Ip6TranslatorSet = params.get("Ip6TranslatorSet")
        self.RequestId = params.get("RequestId")


class CreateLocalGatewayRequest(AbstractModel):
    """CreateLocalGateway请求参数结构体

    """

    def __init__(self):
        """
        :param LocalGatewayName: 本地网关名称\n        :type LocalGatewayName: str\n        :param VpcId: VPC实例ID\n        :type VpcId: str\n        :param CdcId: CDC实例ID\n        :type CdcId: str\n        """
        self.LocalGatewayName = None
        self.VpcId = None
        self.CdcId = None


    def _deserialize(self, params):
        self.LocalGatewayName = params.get("LocalGatewayName")
        self.VpcId = params.get("VpcId")
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateLocalGatewayResponse(AbstractModel):
    """CreateLocalGateway返回参数结构体

    """

    def __init__(self):
        """
        :param LocalGateway: 本地网关信息\n        :type LocalGateway: :class:`tencentcloud.vpc.v20170312.models.LocalGateway`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LocalGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LocalGateway") is not None:
            self.LocalGateway = LocalGateway()
            self.LocalGateway._deserialize(params.get("LocalGateway"))
        self.RequestId = params.get("RequestId")


class CreateNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param DestinationIpPortTranslationNatRules: NAT网关的端口转换规则。\n        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule\n        """
        self.NatGatewayId = None
        self.DestinationIpPortTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("DestinationIpPortTranslationNatRules") is not None:
            self.DestinationIpPortTranslationNatRules = []
            for item in params.get("DestinationIpPortTranslationNatRules"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """CreateNatGatewayDestinationIpPortTranslationNatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNatGatewayRequest(AbstractModel):
    """CreateNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayName: NAT网关名称\n        :type NatGatewayName: str\n        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param InternetMaxBandwidthOut: NAT网关最大外网出带宽(单位:Mbps)，支持的参数值：`20, 50, 100, 200, 500, 1000, 2000, 5000`，默认: `100Mbps`。\n        :type InternetMaxBandwidthOut: int\n        :param MaxConcurrentConnection: NAT网关并发连接上限，支持参数值：`1000000、3000000、10000000`，默认值为`100000`。\n        :type MaxConcurrentConnection: int\n        :param AddressCount: 需要申请的弹性IP个数，系统会按您的要求生产N个弹性IP，其中AddressCount和PublicAddresses至少传递一个。\n        :type AddressCount: int\n        :param PublicIpAddresses: 绑定NAT网关的弹性IP数组，其中AddressCount和PublicAddresses至少传递一个。\n        :type PublicIpAddresses: list of str\n        :param Zone: 可用区，形如：`ap-guangzhou-1`。\n        :type Zone: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        :param SubnetId: NAT网关所属子网\n        :type SubnetId: str\n        """
        self.NatGatewayName = None
        self.VpcId = None
        self.InternetMaxBandwidthOut = None
        self.MaxConcurrentConnection = None
        self.AddressCount = None
        self.PublicIpAddresses = None
        self.Zone = None
        self.Tags = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.NatGatewayName = params.get("NatGatewayName")
        self.VpcId = params.get("VpcId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        self.AddressCount = params.get("AddressCount")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewayResponse(AbstractModel):
    """CreateNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT网关对象数组。\n        :type NatGatewaySet: list of NatGateway\n        :param TotalCount: 符合条件的 NAT网关对象数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NatGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewaySet") is not None:
            self.NatGatewaySet = []
            for item in params.get("NatGatewaySet"):
                obj = NatGateway()
                obj._deserialize(item)
                self.NatGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class CreateNatGatewaySourceIpTranslationNatRuleRequest(AbstractModel):
    """CreateNatGatewaySourceIpTranslationNatRule请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如："nat-df45454"\n        :type NatGatewayId: str\n        :param SourceIpTranslationNatRules: NAT网关的SNAT转换规则\n        :type SourceIpTranslationNatRules: list of SourceIpTranslationNatRule\n        """
        self.NatGatewayId = None
        self.SourceIpTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceIpTranslationNatRules") is not None:
            self.SourceIpTranslationNatRules = []
            for item in params.get("SourceIpTranslationNatRules"):
                obj = SourceIpTranslationNatRule()
                obj._deserialize(item)
                self.SourceIpTranslationNatRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatGatewaySourceIpTranslationNatRuleResponse(AbstractModel):
    """CreateNatGatewaySourceIpTranslationNatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateNetDetectRequest(AbstractModel):
    """CreateNetDetect请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-12345678`\n        :type VpcId: str\n        :param SubnetId: 子网实例ID。形如：subnet-12345678。\n        :type SubnetId: str\n        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。\n        :type NetDetectName: str\n        :param DetectDestinationIp: 探测目的IPv4地址数组。最多两个。\n        :type DetectDestinationIp: list of str\n        :param NextHopType: 下一跳类型，目前我们支持的类型有：
VPN：VPN网关；
DIRECTCONNECT：专线网关；
PEERCONNECTION：对等连接；
NAT：NAT网关；
NORMAL_CVM：普通云服务器；
CCN：云联网网关；\n        :type NextHopType: str\n        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；
下一跳类型为CCN，取值云联网ID，形如：ccn-12345678；\n        :type NextHopDestination: str\n        :param NetDetectDescription: 网络探测描述。\n        :type NetDetectDescription: str\n        """
        self.VpcId = None
        self.SubnetId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectDescription = params.get("NetDetectDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetDetectResponse(AbstractModel):
    """CreateNetDetect返回参数结构体

    """

    def __init__(self):
        """
        :param NetDetect: 网络探测（NetDetect）对象。\n        :type NetDetect: :class:`tencentcloud.vpc.v20170312.models.NetDetect`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetDetect = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetect") is not None:
            self.NetDetect = NetDetect()
            self.NetDetect._deserialize(params.get("NetDetect"))
        self.RequestId = params.get("RequestId")


class CreateNetworkAclRequest(AbstractModel):
    """CreateNetworkAcl请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param NetworkAclName: 网络ACL名称，最大长度不能超过60个字节。\n        :type NetworkAclName: str\n        """
        self.VpcId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclName = params.get("NetworkAclName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNetworkAclResponse(AbstractModel):
    """CreateNetworkAcl返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkAcl: 网络ACL实例。\n        :type NetworkAcl: :class:`tencentcloud.vpc.v20170312.models.NetworkAcl`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetworkAcl = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkAcl") is not None:
            self.NetworkAcl = NetworkAcl()
            self.NetworkAcl._deserialize(params.get("NetworkAcl"))
        self.RequestId = params.get("RequestId")


class CreateNetworkInterfaceRequest(AbstractModel):
    """CreateNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。\n        :type NetworkInterfaceName: str\n        :param SubnetId: 弹性网卡所在的子网实例ID，例如：subnet-0ap8nwca。\n        :type SubnetId: str\n        :param NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。\n        :type NetworkInterfaceDescription: str\n        :param SecondaryPrivateIpAddressCount: 新申请的内网IP地址个数，内网IP地址个数总和不能超过配数。\n        :type SecondaryPrivateIpAddressCount: int\n        :param SecurityGroupIds: 指定绑定的安全组，例如：['sg-1dd51d']。\n        :type SecurityGroupIds: list of str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.VpcId = None
        self.NetworkInterfaceName = None
        self.SubnetId = None
        self.NetworkInterfaceDescription = None
        self.SecondaryPrivateIpAddressCount = None
        self.SecurityGroupIds = None
        self.PrivateIpAddresses = None
        self.Tags = None


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
        :param NetworkInterface: 弹性网卡实例。\n        :type NetworkInterface: :class:`tencentcloud.vpc.v20170312.models.NetworkInterface`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param RouteTableName: 路由表名称，最大长度不能超过60个字节。\n        :type RouteTableName: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.VpcId = None
        self.RouteTableName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.RouteTableName = params.get("RouteTableName")
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
        


class CreateRouteTableResponse(AbstractModel):
    """CreateRouteTable返回参数结构体

    """

    def __init__(self):
        """
        :param RouteTable: 路由表对象。\n        :type RouteTable: :class:`tencentcloud.vpc.v20170312.models.RouteTable`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        


class CreateRoutesResponse(AbstractModel):
    """CreateRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 新增的实例个数。\n        :type TotalCount: int\n        :param RouteTableSet: 路由表对象。\n        :type RouteTableSet: list of RouteTable\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
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
        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type GroupName: str\n        :param GroupDescription: 安全组备注，最多100个字符。\n        :type GroupDescription: str\n        :param ProjectId: 项目ID，默认0。可在qcloud控制台项目管理页面查询到。\n        :type ProjectId: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.Tags = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
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
        :param SecurityGroup: 安全组对象。\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroup = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroup") is not None:
            self.SecurityGroup = SecurityGroup()
            self.SecurityGroup._deserialize(params.get("SecurityGroup"))
        self.RequestId = params.get("RequestId")


class CreateSecurityGroupWithPoliciesRequest(AbstractModel):
    """CreateSecurityGroupWithPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type GroupName: str\n        :param GroupDescription: 安全组备注，最多100个字符。\n        :type GroupDescription: str\n        :param ProjectId: 项目ID，默认0。可在qcloud控制台项目管理页面查询到。\n        :type ProjectId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
        self.GroupName = None
        self.GroupDescription = None
        self.ProjectId = None
        self.SecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.GroupName = params.get("GroupName")
        self.GroupDescription = params.get("GroupDescription")
        self.ProjectId = params.get("ProjectId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupWithPoliciesResponse(AbstractModel):
    """CreateSecurityGroupWithPolicies返回参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroup: 安全组对象。\n        :type SecurityGroup: :class:`tencentcloud.vpc.v20170312.models.SecurityGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ServiceTemplateGroupName: 协议端口模板集合名称\n        :type ServiceTemplateGroupName: str\n        :param ServiceTemplateIds: 协议端口模板实例ID，例如：ppm-4dw6agho。\n        :type ServiceTemplateIds: list of str\n        """
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceTemplateGroupResponse(AbstractModel):
    """CreateServiceTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroup: 协议端口模板集合对象。\n        :type ServiceTemplateGroup: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateGroup`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param ServiceTemplateName: 协议端口模板名称\n        :type ServiceTemplateName: str\n        :param Services: 支持单个端口、多个端口、连续端口及所有端口，协议支持：TCP、UDP、ICMP、GRE 协议。\n        :type Services: list of str\n        """
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateServiceTemplateResponse(AbstractModel):
    """CreateServiceTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplate: 协议端口模板对象。\n        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplate`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpcId: 待操作的VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param SubnetName: 子网名称，最大长度不能超过60个字节。\n        :type SubnetName: str\n        :param CidrBlock: 子网网段，子网网段必须在VPC网段内，相同VPC内子网网段不能重叠。\n        :type CidrBlock: str\n        :param Zone: 子网所在的可用区ID，不同子网选择不同可用区可以做跨可用区灾备。\n        :type Zone: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        :param CdcId: CDC实例ID。\n        :type CdcId: str\n        """
        self.VpcId = None
        self.SubnetName = None
        self.CidrBlock = None
        self.Zone = None
        self.Tags = None
        self.CdcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetName = params.get("SubnetName")
        self.CidrBlock = params.get("CidrBlock")
        self.Zone = params.get("Zone")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CdcId = params.get("CdcId")
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
        :param Subnet: 子网对象。\n        :type Subnet: :class:`tencentcloud.vpc.v20170312.models.Subnet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`\n        :type VpcId: str\n        :param Subnets: 子网对象列表。\n        :type Subnets: list of SubnetInput\n        :param Tags: 指定绑定的标签列表，注意这里的标签集合为列表中所有子网对象所共享，不能为每个子网对象单独指定标签，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        :param CdcId: 需要增加到的CDC实例ID。\n        :type CdcId: str\n        """
        self.VpcId = None
        self.Subnets = None
        self.Tags = None
        self.CdcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Subnets") is not None:
            self.Subnets = []
            for item in params.get("Subnets"):
                obj = SubnetInput()
                obj._deserialize(item)
                self.Subnets.append(obj)
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CdcId = params.get("CdcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSubnetsResponse(AbstractModel):
    """CreateSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param SubnetSet: 新创建的子网列表。\n        :type SubnetSet: list of Subnet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class CreateVpcEndPointRequest(AbstractModel):
    """CreateVpcEndPoint请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param SubnetId: 子网实例ID。\n        :type SubnetId: str\n        :param EndPointName: 终端节点名称。\n        :type EndPointName: str\n        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        :param EndPointVip: 终端节点VIP，可以指定IP申请。\n        :type EndPointVip: str\n        :param SecurityGroupId: 安全组ID。\n        :type SecurityGroupId: str\n        """
        self.VpcId = None
        self.SubnetId = None
        self.EndPointName = None
        self.EndPointServiceId = None
        self.EndPointVip = None
        self.SecurityGroupId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EndPointName = params.get("EndPointName")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.EndPointVip = params.get("EndPointVip")
        self.SecurityGroupId = params.get("SecurityGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcEndPointResponse(AbstractModel):
    """CreateVpcEndPoint返回参数结构体

    """

    def __init__(self):
        """
        :param EndPoint: 终端节点对象详细信息。\n        :type EndPoint: :class:`tencentcloud.vpc.v20170312.models.EndPoint`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EndPoint = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPoint") is not None:
            self.EndPoint = EndPoint()
            self.EndPoint._deserialize(params.get("EndPoint"))
        self.RequestId = params.get("RequestId")


class CreateVpcEndPointServiceRequest(AbstractModel):
    """CreateVpcEndPointService请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param EndPointServiceName: 终端节点服务名称。\n        :type EndPointServiceName: str\n        :param AutoAcceptFlag: 是否自动接受。\n        :type AutoAcceptFlag: bool\n        :param ServiceInstanceId: 后端服务ID，比如lb-xxx。\n        :type ServiceInstanceId: str\n        :param IsPassService: 是否是PassService类型。\n        :type IsPassService: bool\n        """
        self.VpcId = None
        self.EndPointServiceName = None
        self.AutoAcceptFlag = None
        self.ServiceInstanceId = None
        self.IsPassService = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.EndPointServiceName = params.get("EndPointServiceName")
        self.AutoAcceptFlag = params.get("AutoAcceptFlag")
        self.ServiceInstanceId = params.get("ServiceInstanceId")
        self.IsPassService = params.get("IsPassService")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcEndPointServiceResponse(AbstractModel):
    """CreateVpcEndPointService返回参数结构体

    """

    def __init__(self):
        """
        :param EndPointService: 终端节点服务对象详细信息。\n        :type EndPointService: :class:`tencentcloud.vpc.v20170312.models.EndPointService`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EndPointService = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPointService") is not None:
            self.EndPointService = EndPointService()
            self.EndPointService._deserialize(params.get("EndPointService"))
        self.RequestId = params.get("RequestId")


class CreateVpcEndPointServiceWhiteListRequest(AbstractModel):
    """CreateVpcEndPointServiceWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param UserUin: UIN。\n        :type UserUin: str\n        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        :param Description: 白名单描述。\n        :type Description: str\n        """
        self.UserUin = None
        self.EndPointServiceId = None
        self.Description = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcEndPointServiceWhiteListResponse(AbstractModel):
    """CreateVpcEndPointServiceWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVpcRequest(AbstractModel):
    """CreateVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcName: vpc名称，最大长度不能超过60个字节。\n        :type VpcName: str\n        :param CidrBlock: vpc的cidr，仅能在10.0.0.0/16，172.16.0.0/16，192.168.0.0/16这三个内网网段内。\n        :type CidrBlock: str\n        :param EnableMulticast: 是否开启组播。true: 开启, false: 不开启。\n        :type EnableMulticast: str\n        :param DnsServers: DNS地址，最多支持4个。\n        :type DnsServers: list of str\n        :param DomainName: DHCP使用的域名。\n        :type DomainName: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]。\n        :type Tags: list of Tag\n        """
        self.VpcName = None
        self.CidrBlock = None
        self.EnableMulticast = None
        self.DnsServers = None
        self.DomainName = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcName = params.get("VpcName")
        self.CidrBlock = params.get("CidrBlock")
        self.EnableMulticast = params.get("EnableMulticast")
        self.DnsServers = params.get("DnsServers")
        self.DomainName = params.get("DomainName")
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
        


class CreateVpcResponse(AbstractModel):
    """CreateVpc返回参数结构体

    """

    def __init__(self):
        """
        :param Vpc: Vpc对象。\n        :type Vpc: :class:`tencentcloud.vpc.v20170312.models.Vpc`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpcId: VPC实例ID。可通过[DescribeVpcs](https://cloud.tencent.com/document/product/215/15778)接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param CustomerGatewayId: 对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。\n        :type CustomerGatewayId: str\n        :param VpnConnectionName: 通道名称，可任意命名，但不得超过60个字符。\n        :type VpnConnectionName: str\n        :param PreShareKey: 预共享密钥。\n        :type PreShareKey: str\n        :param SecurityPolicyDatabases: SPD策略组，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。\n        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase\n        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议\n        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`\n        :param IPSECOptionsSpecification: IPSec配置，腾讯云提供IPSec安全会话设置\n        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        :param EnableHealthCheck: 是否支持隧道内健康检查\n        :type EnableHealthCheck: bool\n        :param HealthCheckLocalIp: 健康检查本端地址\n        :type HealthCheckLocalIp: str\n        :param HealthCheckRemoteIp: 健康检查对端地址\n        :type HealthCheckRemoteIp: str\n        """
        self.VpcId = None
        self.VpnGatewayId = None
        self.CustomerGatewayId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None
        self.Tags = None
        self.EnableHealthCheck = None
        self.HealthCheckLocalIp = None
        self.HealthCheckRemoteIp = None


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
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tag()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        self.HealthCheckLocalIp = params.get("HealthCheckLocalIp")
        self.HealthCheckRemoteIp = params.get("HealthCheckRemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpnConnectionResponse(AbstractModel):
    """CreateVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param VpnConnection: 通道实例对象。\n        :type VpnConnection: :class:`tencentcloud.vpc.v20170312.models.VpnConnection`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpcId: VPC实例ID。可通过[DescribeVpcs](https://cloud.tencent.com/document/product/215/15778)接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param VpnGatewayName: VPN网关名称，最大长度不能超过60个字节。\n        :type VpnGatewayName: str\n        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps\n        :type InternetMaxBandwidthOut: int\n        :param InstanceChargeType: VPN网关计费模式，PREPAID：表示预付费，即包年包月，POSTPAID_BY_HOUR：表示后付费，即按量计费。默认：POSTPAID_BY_HOUR，如果指定预付费模式，参数InstanceChargePrepaid必填。\n        :type InstanceChargeType: str\n        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        :param Zone: 可用区，如：ap-guangzhou-2。\n        :type Zone: str\n        :param Type: VPN网关类型。值“CCN”云联网类型VPN网关\n        :type Type: str\n        :param Tags: 指定绑定的标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type Tags: list of Tag\n        """
        self.VpcId = None
        self.VpnGatewayName = None
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None
        self.Zone = None
        self.Type = None
        self.Tags = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        self.Zone = params.get("Zone")
        self.Type = params.get("Type")
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
        


class CreateVpnGatewayResponse(AbstractModel):
    """CreateVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param VpnGateway: VPN网关对象\n        :type VpnGateway: :class:`tencentcloud.vpc.v20170312.models.VpnGateway`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.VpnGateway = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpnGateway") is not None:
            self.VpnGateway = VpnGateway()
            self.VpnGateway._deserialize(params.get("VpnGateway"))
        self.RequestId = params.get("RequestId")


class CreateVpnGatewayRoutesRequest(AbstractModel):
    """CreateVpnGatewayRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关的ID\n        :type VpnGatewayId: str\n        :param Routes: VPN网关目的路由列表\n        :type Routes: list of VpnGatewayRoute\n        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpnGatewayRoutesResponse(AbstractModel):
    """CreateVpnGatewayRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param Routes: VPN网关目的路由\n        :type Routes: list of VpnGatewayRoute\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Routes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.RequestId = params.get("RequestId")


class CrossBorderCompliance(AbstractModel):
    """合规化审批单

    """

    def __init__(self):
        """
        :param ServiceProvider: 服务商，可选值：`UNICOM`。\n        :type ServiceProvider: str\n        :param ComplianceId: 合规化审批单`ID`。\n        :type ComplianceId: int\n        :param Company: 公司全称。\n        :type Company: str\n        :param UniformSocialCreditCode: 统一社会信用代码。\n        :type UniformSocialCreditCode: str\n        :param LegalPerson: 法定代表人。\n        :type LegalPerson: str\n        :param IssuingAuthority: 发证机关。\n        :type IssuingAuthority: str\n        :param BusinessLicense: 营业执照。\n        :type BusinessLicense: str\n        :param BusinessAddress: 营业执照住所。\n        :type BusinessAddress: str\n        :param PostCode: 邮编。\n        :type PostCode: int\n        :param Manager: 经办人。\n        :type Manager: str\n        :param ManagerId: 经办人身份证号。\n        :type ManagerId: str\n        :param ManagerIdCard: 经办人身份证。\n        :type ManagerIdCard: str\n        :param ManagerAddress: 经办人身份证地址。\n        :type ManagerAddress: str\n        :param ManagerTelephone: 经办人联系电话。\n        :type ManagerTelephone: str\n        :param Email: 电子邮箱。\n        :type Email: str\n        :param ServiceHandlingForm: 服务受理单。\n        :type ServiceHandlingForm: str\n        :param AuthorizationLetter: 授权函。\n        :type AuthorizationLetter: str\n        :param SafetyCommitment: 信息安全承诺书。\n        :type SafetyCommitment: str\n        :param ServiceStartDate: 服务开始时间。\n        :type ServiceStartDate: str\n        :param ServiceEndDate: 服务截止时间。\n        :type ServiceEndDate: str\n        :param State: 状态。待审批：`PENDING`，已通过：`APPROVED`，已拒绝：`DENY`。\n        :type State: str\n        :param CreatedTime: 审批单创建时间。\n        :type CreatedTime: str\n        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.Company = None
        self.UniformSocialCreditCode = None
        self.LegalPerson = None
        self.IssuingAuthority = None
        self.BusinessLicense = None
        self.BusinessAddress = None
        self.PostCode = None
        self.Manager = None
        self.ManagerId = None
        self.ManagerIdCard = None
        self.ManagerAddress = None
        self.ManagerTelephone = None
        self.Email = None
        self.ServiceHandlingForm = None
        self.AuthorizationLetter = None
        self.SafetyCommitment = None
        self.ServiceStartDate = None
        self.ServiceEndDate = None
        self.State = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.Company = params.get("Company")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.LegalPerson = params.get("LegalPerson")
        self.IssuingAuthority = params.get("IssuingAuthority")
        self.BusinessLicense = params.get("BusinessLicense")
        self.BusinessAddress = params.get("BusinessAddress")
        self.PostCode = params.get("PostCode")
        self.Manager = params.get("Manager")
        self.ManagerId = params.get("ManagerId")
        self.ManagerIdCard = params.get("ManagerIdCard")
        self.ManagerAddress = params.get("ManagerAddress")
        self.ManagerTelephone = params.get("ManagerTelephone")
        self.Email = params.get("Email")
        self.ServiceHandlingForm = params.get("ServiceHandlingForm")
        self.AuthorizationLetter = params.get("AuthorizationLetter")
        self.SafetyCommitment = params.get("SafetyCommitment")
        self.ServiceStartDate = params.get("ServiceStartDate")
        self.ServiceEndDate = params.get("ServiceEndDate")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerGateway(AbstractModel):
    """对端网关

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 用户网关唯一ID\n        :type CustomerGatewayId: str\n        :param CustomerGatewayName: 网关名称\n        :type CustomerGatewayName: str\n        :param IpAddress: 公网地址\n        :type IpAddress: str\n        :param CreatedTime: 创建时间\n        :type CreatedTime: str\n        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None
        self.IpAddress = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        self.IpAddress = params.get("IpAddress")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CustomerGatewayVendor(AbstractModel):
    """对端网关厂商信息对象。

    """

    def __init__(self):
        """
        :param Platform: 平台。\n        :type Platform: str\n        :param SoftwareVersion: 软件版本。\n        :type SoftwareVersion: str\n        :param VendorName: 供应商名称。\n        :type VendorName: str\n        """
        self.Platform = None
        self.SoftwareVersion = None
        self.VendorName = None


    def _deserialize(self, params):
        self.Platform = params.get("Platform")
        self.SoftwareVersion = params.get("SoftwareVersion")
        self.VendorName = params.get("VendorName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CvmInstance(AbstractModel):
    """云主机实例信息。

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param SubnetId: 子网实例ID。\n        :type SubnetId: str\n        :param InstanceId: 云主机实例ID\n        :type InstanceId: str\n        :param InstanceName: 云主机名称。\n        :type InstanceName: str\n        :param InstanceState: 云主机状态。\n        :type InstanceState: str\n        :param CPU: 实例的CPU核数，单位：核。\n        :type CPU: int\n        :param Memory: 实例内存容量，单位：GB。\n        :type Memory: int\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param InstanceType: 实例机型。\n        :type InstanceType: str\n        :param EniLimit: 实例弹性网卡配额（包含主网卡）。\n        :type EniLimit: int\n        :param EniIpLimit: 实例弹性网卡内网IP配额（包含主网卡）。\n        :type EniIpLimit: int\n        :param InstanceEniCount: 实例已绑定弹性网卡的个数（包含主网卡）。\n        :type InstanceEniCount: int\n        """
        self.VpcId = None
        self.SubnetId = None
        self.InstanceId = None
        self.InstanceName = None
        self.InstanceState = None
        self.CPU = None
        self.Memory = None
        self.CreatedTime = None
        self.InstanceType = None
        self.EniLimit = None
        self.EniIpLimit = None
        self.InstanceEniCount = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.InstanceState = params.get("InstanceState")
        self.CPU = params.get("CPU")
        self.Memory = params.get("Memory")
        self.CreatedTime = params.get("CreatedTime")
        self.InstanceType = params.get("InstanceType")
        self.EniLimit = params.get("EniLimit")
        self.EniIpLimit = params.get("EniIpLimit")
        self.InstanceEniCount = params.get("InstanceEniCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultVpcSubnet(AbstractModel):
    """默认VPC和子网

    """

    def __init__(self):
        """
        :param VpcId: 默认VpcId\n        :type VpcId: str\n        :param SubnetId: 默认SubnetId\n        :type SubnetId: str\n        """
        self.VpcId = None
        self.SubnetId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressTemplateGroupRequest(AbstractModel):
    """DeleteAddressTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP地址模板集合实例ID，例如：ipmg-90cex8mq。\n        :type AddressTemplateGroupId: str\n        """
        self.AddressTemplateGroupId = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressTemplateGroupResponse(AbstractModel):
    """DeleteAddressTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAddressTemplateRequest(AbstractModel):
    """DeleteAddressTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP地址模板实例ID，例如：ipm-09o5m8kc。\n        :type AddressTemplateId: str\n        """
        self.AddressTemplateId = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAddressTemplateResponse(AbstractModel):
    """DeleteAddressTemplate返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteAssistantCidrRequest(AbstractModel):
    """DeleteAssistantCidr请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`\n        :type VpcId: str\n        :param CidrBlocks: CIDR数组，格式如["10.0.0.0/16", "172.16.0.0/16"]\n        :type CidrBlocks: list of str\n        """
        self.VpcId = None
        self.CidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.CidrBlocks = params.get("CidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteAssistantCidrResponse(AbstractModel):
    """DeleteAssistantCidr返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteBandwidthPackageRequest(AbstractModel):
    """DeleteBandwidthPackage请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 待删除带宽包唯一ID\n        :type BandwidthPackageId: str\n        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteBandwidthPackageResponse(AbstractModel):
    """DeleteBandwidthPackage返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcnRequest(AbstractModel):
    """DeleteCcn请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcnResponse(AbstractModel):
    """DeleteCcn返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCustomerGatewayRequest(AbstractModel):
    """DeleteCustomerGateway请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。\n        :type CustomerGatewayId: str\n        """
        self.CustomerGatewayId = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCustomerGatewayResponse(AbstractModel):
    """DeleteCustomerGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDhcpIpRequest(AbstractModel):
    """DeleteDhcpIp请求参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpId: `DhcpIp`的`ID`，是`DhcpIp`的唯一标识。\n        :type DhcpIpId: str\n        """
        self.DhcpIpId = None


    def _deserialize(self, params):
        self.DhcpIpId = params.get("DhcpIpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDhcpIpResponse(AbstractModel):
    """DeleteDhcpIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：dcg-prpqlmg1\n        :type DirectConnectGatewayId: str\n        :param RouteIds: 路由ID。形如：ccnr-f49l6u0z。\n        :type RouteIds: list of str\n        """
        self.DirectConnectGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DeleteDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDirectConnectGatewayRequest(AbstractModel):
    """DeleteDirectConnectGateway请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关唯一`ID`，形如：`dcg-9o233uri`。\n        :type DirectConnectGatewayId: str\n        """
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDirectConnectGatewayResponse(AbstractModel):
    """DeleteDirectConnectGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFlowLogRequest(AbstractModel):
    """DeleteFlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私用网络ID或者统一ID，建议使用统一ID\n        :type VpcId: str\n        :param FlowLogId: 流日志唯一ID\n        :type FlowLogId: str\n        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFlowLogResponse(AbstractModel):
    """DeleteFlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteHaVipRequest(AbstractModel):
    """DeleteHaVip请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。\n        :type HaVipId: str\n        """
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


class DeleteIp6TranslatorsRequest(AbstractModel):
    """DeleteIp6Translators请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: 待释放的IPV6转换实例的唯一ID，形如‘ip6-xxxxxxxx’\n        :type Ip6TranslatorIds: list of str\n        """
        self.Ip6TranslatorIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteIp6TranslatorsResponse(AbstractModel):
    """DeleteIp6Translators返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteLocalGatewayRequest(AbstractModel):
    """DeleteLocalGateway请求参数结构体

    """

    def __init__(self):
        """
        :param LocalGatewayId: 本地网关实例ID\n        :type LocalGatewayId: str\n        :param CdcId: CDC实例ID\n        :type CdcId: str\n        :param VpcId: VPC实例ID\n        :type VpcId: str\n        """
        self.LocalGatewayId = None
        self.CdcId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.LocalGatewayId = params.get("LocalGatewayId")
        self.CdcId = params.get("CdcId")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteLocalGatewayResponse(AbstractModel):
    """DeleteLocalGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param DestinationIpPortTranslationNatRules: NAT网关的端口转换规则。\n        :type DestinationIpPortTranslationNatRules: list of DestinationIpPortTranslationNatRule\n        """
        self.NatGatewayId = None
        self.DestinationIpPortTranslationNatRules = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("DestinationIpPortTranslationNatRules") is not None:
            self.DestinationIpPortTranslationNatRules = []
            for item in params.get("DestinationIpPortTranslationNatRules"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """DeleteNatGatewayDestinationIpPortTranslationNatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewayRequest(AbstractModel):
    """DeleteNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        """
        self.NatGatewayId = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewayResponse(AbstractModel):
    """DeleteNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNatGatewaySourceIpTranslationNatRuleRequest(AbstractModel):
    """DeleteNatGatewaySourceIpTranslationNatRule请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param NatGatewaySnatIds: NAT网关的SNAT ID列表，形如：`snat-df43254`。\n        :type NatGatewaySnatIds: list of str\n        """
        self.NatGatewayId = None
        self.NatGatewaySnatIds = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewaySnatIds = params.get("NatGatewaySnatIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatGatewaySourceIpTranslationNatRuleResponse(AbstractModel):
    """DeleteNatGatewaySourceIpTranslationNatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetDetectRequest(AbstractModel):
    """DeleteNetDetect请求参数结构体

    """

    def __init__(self):
        """
        :param NetDetectId: 网络探测实例`ID`。形如：`netd-12345678`\n        :type NetDetectId: str\n        """
        self.NetDetectId = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetDetectResponse(AbstractModel):
    """DeleteNetDetect返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteNetworkAclRequest(AbstractModel):
    """DeleteNetworkAcl请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkAclId: 网络ACL实例ID。例如：acl-12345678。\n        :type NetworkAclId: str\n        """
        self.NetworkAclId = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNetworkAclResponse(AbstractModel):
    """DeleteNetworkAcl返回参数结构体

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
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        """
        self.NetworkInterfaceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
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
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        """
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
        :param RouteTableId: 路由表实例ID。\n        :type RouteTableId: str\n        :param Routes: 路由策略对象，删除路由策略时，仅需使用Route的RouteId字段。\n        :type Routes: list of Route\n        """
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
        :param RouteSet: 已删除的路由策略详情。\n        :type RouteSet: list of Route\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class DeleteSecurityGroupPoliciesRequest(AbstractModel):
    """DeleteSecurityGroupPolicies请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。一个请求中只能删除单个方向的一条或多条规则。支持指定索引（PolicyIndex） 匹配删除和安全组规则匹配删除两种方式，一个请求中只能使用一种匹配方式。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
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
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        """
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


class DeleteServiceTemplateGroupRequest(AbstractModel):
    """DeleteServiceTemplateGroup请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 协议端口模板集合实例ID，例如：ppmg-n17uxvve。\n        :type ServiceTemplateGroupId: str\n        """
        self.ServiceTemplateGroupId = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceTemplateGroupResponse(AbstractModel):
    """DeleteServiceTemplateGroup返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteServiceTemplateRequest(AbstractModel):
    """DeleteServiceTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 协议端口模板实例ID，例如：ppm-e6dy460g。\n        :type ServiceTemplateId: str\n        """
        self.ServiceTemplateId = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteServiceTemplateResponse(AbstractModel):
    """DeleteServiceTemplate返回参数结构体

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
        :param SubnetId: 子网实例ID。可通过DescribeSubnets接口返回值中的SubnetId获取。\n        :type SubnetId: str\n        """
        self.SubnetId = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
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


class DeleteVpcEndPointRequest(AbstractModel):
    """DeleteVpcEndPoint请求参数结构体

    """

    def __init__(self):
        """
        :param EndPointId: 终端节点ID。\n        :type EndPointId: str\n        """
        self.EndPointId = None


    def _deserialize(self, params):
        self.EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcEndPointResponse(AbstractModel):
    """DeleteVpcEndPoint返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcEndPointServiceRequest(AbstractModel):
    """DeleteVpcEndPointService请求参数结构体

    """

    def __init__(self):
        """
        :param EndPointServiceId: 终端节点ID。\n        :type EndPointServiceId: str\n        """
        self.EndPointServiceId = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcEndPointServiceResponse(AbstractModel):
    """DeleteVpcEndPointService返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpcEndPointServiceWhiteListRequest(AbstractModel):
    """DeleteVpcEndPointServiceWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param UserUin: 用户UIN数组。\n        :type UserUin: list of str\n        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        """
        self.UserUin = None
        self.EndPointServiceId = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.EndPointServiceId = params.get("EndPointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcEndPointServiceWhiteListResponse(AbstractModel):
    """DeleteVpcEndPointServiceWhiteList返回参数结构体

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
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        """
        self.VpcId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
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


class DeleteVpnConnectionRequest(AbstractModel):
    """DeleteVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。\n        :type VpnConnectionId: str\n        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnConnectionResponse(AbstractModel):
    """DeleteVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRequest(AbstractModel):
    """DeleteVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        """
        self.VpnGatewayId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnGatewayResponse(AbstractModel):
    """DeleteVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteVpnGatewayRoutesRequest(AbstractModel):
    """DeleteVpnGatewayRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID\n        :type VpnGatewayId: str\n        :param RouteIds: 路由ID信息列表\n        :type RouteIds: list of str\n        """
        self.VpnGatewayId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpnGatewayRoutesResponse(AbstractModel):
    """DeleteVpnGatewayRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AccountAttributeSet: 用户账号属性对象\n        :type AccountAttributeSet: list of AccountAttribute\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param QuotaSet: 账户 EIP 配额信息。\n        :type QuotaSet: list of Quota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
<li>address-template-group-id - String - （过滤条件）IP地址模板实集合例ID，例如：ipmg-mdunqeb6。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        


class DescribeAddressTemplateGroupsResponse(AbstractModel):
    """DescribeAddressTemplateGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param AddressTemplateGroupSet: IP地址模板。\n        :type AddressTemplateGroupSet: list of AddressTemplateGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
<li>address-template-id - String - （过滤条件）IP地址模板实例ID，例如：ipm-mdunqeb6。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        


class DescribeAddressTemplatesResponse(AbstractModel):
    """DescribeAddressTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param AddressTemplateSet: IP地址模版。\n        :type AddressTemplateSet: list of AddressTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param AddressIds: 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。参数不支持同时指定`AddressIds`和`Filters.address-id`。\n        :type AddressIds: list of str\n        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。详细的过滤条件如下：
<li> address-id - String - 是否必填：否 - （过滤条件）按照 EIP 的唯一 ID 过滤。EIP 唯一 ID 形如：eip-11112222。</li>
<li> address-name - String - 是否必填：否 - （过滤条件）按照 EIP 名称过滤。不支持模糊过滤。</li>
<li> address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。</li>
<li> address-status - String - 是否必填：否 - （过滤条件）按照 EIP 的状态过滤。状态包含：'CREATING'，'BINDING'，'BIND'，'UNBINDING'，'UNBIND'，'OFFLINING'，'BIND_ENI'。</li>
<li> instance-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的实例 ID 过滤。实例 ID 形如：ins-11112222。</li>
<li> private-ip-address - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的内网 IP 过滤。</li>
<li> network-interface-id - String - 是否必填：否 - （过滤条件）按照 EIP 绑定的弹性网卡 ID 过滤。弹性网卡 ID 形如：eni-11112222。</li>
<li> is-arrears - String - 是否必填：否 - （过滤条件）按照 EIP 是否欠费进行过滤。（TRUE：EIP 处于欠费状态|FALSE：EIP 费用状态正常）</li>
<li> address-type - String - 是否必填：否 - （过滤条件）按照 IP类型 进行过滤。可选值：'EIP'，'AnycastEIP'，'HighQualityEIP'</li>
<li> address-isp - String - 是否必填：否 - （过滤条件）按照 运营商类型 进行过滤。可选值：'BGP'，'CMCC'，'CUCC', 'CTCC'</li>
<li> dedicated-cluster-id - String - 是否必填：否 - （过滤条件）按照 CDC 的唯一 ID 过滤。CDC 唯一 ID 形如：cluster-11112222。</li>
<li> tag-key - String - 是否必填：否 - （过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 - （过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。tag-key使用具体的标签键进行替换。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Limit: int\n        """
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


class DescribeAssistantCidrRequest(AbstractModel):
    """DescribeAssistantCidr请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: `VPC`实例`ID`数组。形如：[`vpc-6v2ht8q5`]\n        :type VpcIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAssistantCidrResponse(AbstractModel):
    """DescribeAssistantCidr返回参数结构体

    """

    def __init__(self):
        """
        :param AssistantCidrSet: 符合条件的辅助CIDR数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssistantCidrSet: list of AssistantCidr\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AssistantCidrSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackageBillUsageRequest(AbstractModel):
    """DescribeBandwidthPackageBillUsage请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 后付费共享带宽包的唯一ID\n        :type BandwidthPackageId: str\n        """
        self.BandwidthPackageId = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBandwidthPackageBillUsageResponse(AbstractModel):
    """DescribeBandwidthPackageBillUsage返回参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageBillBandwidthSet: 当前计费用量\n        :type BandwidthPackageBillBandwidthSet: list of BandwidthPackageBillBandwidth\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.BandwidthPackageBillBandwidthSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BandwidthPackageBillBandwidthSet") is not None:
            self.BandwidthPackageBillBandwidthSet = []
            for item in params.get("BandwidthPackageBillBandwidthSet"):
                obj = BandwidthPackageBillBandwidth()
                obj._deserialize(item)
                self.BandwidthPackageBillBandwidthSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackageQuotaRequest(AbstractModel):
    """DescribeBandwidthPackageQuota请求参数结构体

    """


class DescribeBandwidthPackageQuotaResponse(AbstractModel):
    """DescribeBandwidthPackageQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 带宽包配额详细信息\n        :type QuotaSet: list of Quota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeBandwidthPackageResourcesRequest(AbstractModel):
    """DescribeBandwidthPackageResources请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 标识 共享带宽包 的唯一 ID 列表。共享带宽包 唯一 ID 形如：`bwp-11112222`。\n        :type BandwidthPackageId: str\n        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。详细的过滤条件如下：
<li> resource-id - String - 是否必填：否 - （过滤条件）按照 共享带宽包内资源 的唯一 ID 过滤。共享带宽包内资源 唯一 ID 形如：eip-11112222。</li>
<li> resource-type - String - 是否必填：否 - （过滤条件）按照 共享带宽包内资源 类型过滤，目前仅支持 弹性IP 和 负载均衡 两种类型，可选值为 Address 和 LoadBalance。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Limit: int\n        """
        self.BandwidthPackageId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
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
        


class DescribeBandwidthPackageResourcesResponse(AbstractModel):
    """DescribeBandwidthPackageResources返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的 共享带宽包内资源 数量。\n        :type TotalCount: int\n        :param ResourceSet: 共享带宽包内资源 详细信息列表。\n        :type ResourceSet: list of Resource\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCount = None
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = Resource()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBandwidthPackagesRequest(AbstractModel):
    """DescribeBandwidthPackages请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageIds: 带宽包唯一ID列表\n        :type BandwidthPackageIds: list of str\n        :param Filters: 每次请求的`Filters`的上限为10。参数不支持同时指定`BandwidthPackageIds`和`Filters`。详细的过滤条件如下：
<li> bandwidth-package_id - String - 是否必填：否 - （过滤条件）按照带宽包的唯一标识ID过滤。</li>
<li> bandwidth-package-name - String - 是否必填：否 - （过滤条件）按照 带宽包名称过滤。不支持模糊过滤。</li>
<li> network-type - String - 是否必填：否 - （过滤条件）按照带宽包的类型过滤。类型包括'HIGH_QUALITY_BGP','BGP','SINGLEISP'和'ANYCAST'。</li>
<li> charge-type - String - 是否必填：否 - （过滤条件）按照带宽包的计费类型过滤。计费类型包括'TOP5_POSTPAID_BY_MONTH'和'PERCENT95_POSTPAID_BY_MONTH'。</li>
<li> resource.resource-type - String - 是否必填：否 - （过滤条件）按照带宽包资源类型过滤。资源类型包括'Address'和'LoadBalance'</li>
<li> resource.resource-id - String - 是否必填：否 - （过滤条件）按照带宽包资源Id过滤。资源Id形如'eip-xxxx','lb-xxxx'</li>
<li> resource.address-ip - String - 是否必填：否 - （过滤条件）按照带宽包资源Ip过滤。</li>
<li> tag-key - String - 是否必填：否 - （过滤条件）按照标签键进行过滤。</li>
<li> tag-value - String - 是否必填：否 - （过滤条件）按照标签值进行过滤。</li>
<li> tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。tag-key使用具体的标签键进行替换。</li>\n        :type Filters: list of Filter\n        :param Offset: 查询带宽包偏移量\n        :type Offset: int\n        :param Limit: 查询带宽包数量限制\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBandwidthPackagesResponse(AbstractModel):
    """DescribeBandwidthPackages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的带宽包数量\n        :type TotalCount: int\n        :param BandwidthPackageSet: 描述带宽包详细信息\n        :type BandwidthPackageSet: list of BandwidthPackage\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        :param Filters: 过滤条件：
<li>ccn-id - String -（过滤条件）CCN实例ID。</li>
<li>instance-type - String -（过滤条件）关联实例类型。</li>
<li>instance-region - String -（过滤条件）关联实例所属地域。</li>
<li>instance-id - String -（过滤条件）关联实例实例ID。</li>\n        :type Filters: list of Filter\n        :param CcnId: 云联网实例ID\n        :type CcnId: str\n        :param OrderField: 排序字段。支持：`CcnId` `InstanceType` `InstanceId` `InstanceName` `InstanceRegion` `AttachedTime` `State`。\n        :type OrderField: str\n        :param OrderDirection: 排序方法。顺序：`ASC`，倒序：`DESC`。\n        :type OrderDirection: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnAttachedInstancesResponse(AbstractModel):
    """DescribeCcnAttachedInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param InstanceSet: 关联实例列表。\n        :type InstanceSet: list of CcnAttachedInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        """
        self.CcnId = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnRegionBandwidthLimitsResponse(AbstractModel):
    """DescribeCcnRegionBandwidthLimits返回参数结构体

    """

    def __init__(self):
        """
        :param CcnRegionBandwidthLimitSet: 云联网（CCN）各地域出带宽上限\n        :type CcnRegionBandwidthLimitSet: list of CcnRegionBandwidthLimit\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CcnId: CCN实例ID，形如：ccn-gree226l。\n        :type CcnId: str\n        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。\n        :type RouteIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定RouteIds和Filters。
<li>route-id - String -（过滤条件）路由策略ID。</li>
<li>cidr-block - String -（过滤条件）目的端。</li>
<li>instance-type - String -（过滤条件）下一跳类型。</li>
<li>instance-region - String -（过滤条件）下一跳所属地域。</li>
<li>instance-id - String -（过滤条件）下一跳实例ID。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnRoutesResponse(AbstractModel):
    """DescribeCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param RouteSet: CCN路由策略对象。\n        :type RouteSet: list of CcnRoute\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CcnIds: CCN实例ID。形如：ccn-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定CcnIds和Filters。\n        :type CcnIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定CcnIds和Filters。
<li>ccn-id - String - （过滤条件）CCN唯一ID，形如：vpc-f49l6u0z。</li>
<li>ccn-name - String - （过滤条件）CCN名称。</li>
<li>ccn-description - String - （过滤条件）CCN描述。</li>
<li>state - String - （过滤条件）实例状态， 'ISOLATED': 隔离中（欠费停服），'AVAILABLE'：运行中。</li>
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例：查询绑定了标签的CCN列表。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        :param OrderField: 排序字段。支持：`CcnId` `CcnName` `CreateTime` `State` `QosLevel`\n        :type OrderField: str\n        :param OrderDirection: 排序方法。顺序：`ASC`，倒序：`DESC`。\n        :type OrderDirection: str\n        """
        self.CcnIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.OrderField = None
        self.OrderDirection = None


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
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcnsResponse(AbstractModel):
    """DescribeCcns返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param CcnSet: CCN对象。\n        :type CcnSet: list of CCN\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
<li>vm-ip - String - （过滤条件）基础网络云服务器IP。</li>\n        :type Filters: list of FilterObject\n        :param Offset: 偏移量\n        :type Offset: str\n        :param Limit: 返回数量\n        :type Limit: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeClassicLinkInstancesResponse(AbstractModel):
    """DescribeClassicLinkInstances返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param ClassicLinkInstanceSet: 私有网络和基础网络互通设备。\n        :type ClassicLinkInstanceSet: list of ClassicLinkInstance\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCrossBorderComplianceRequest(AbstractModel):
    """DescribeCrossBorderCompliance请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceProvider: （精确匹配）服务商，可选值：`UNICOM`。\n        :type ServiceProvider: str\n        :param ComplianceId: （精确匹配）合规化审批单`ID`。\n        :type ComplianceId: int\n        :param Company: （模糊查询）公司名称。\n        :type Company: str\n        :param UniformSocialCreditCode: （精确匹配）统一社会信用代码。\n        :type UniformSocialCreditCode: str\n        :param LegalPerson: （模糊查询）法定代表人。\n        :type LegalPerson: str\n        :param IssuingAuthority: （模糊查询）发证机关。\n        :type IssuingAuthority: str\n        :param BusinessAddress: （模糊查询）营业执照住所。\n        :type BusinessAddress: str\n        :param PostCode: （精确匹配）邮编。\n        :type PostCode: int\n        :param Manager: （模糊查询）经办人。\n        :type Manager: str\n        :param ManagerId: （精确查询）经办人身份证号。\n        :type ManagerId: str\n        :param ManagerAddress: （模糊查询）经办人身份证地址。\n        :type ManagerAddress: str\n        :param ManagerTelephone: （精确匹配）经办人联系电话。\n        :type ManagerTelephone: str\n        :param Email: （精确匹配）电子邮箱。\n        :type Email: str\n        :param ServiceStartDate: （精确匹配）服务开始日期，如：`2020-07-28`。\n        :type ServiceStartDate: str\n        :param ServiceEndDate: （精确匹配）服务结束日期，如：`2021-07-28`。\n        :type ServiceEndDate: str\n        :param State: （精确匹配）状态。待审批：`PENDING`，通过：`APPROVED `，拒绝：`DENY`。\n        :type State: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        """
        self.ServiceProvider = None
        self.ComplianceId = None
        self.Company = None
        self.UniformSocialCreditCode = None
        self.LegalPerson = None
        self.IssuingAuthority = None
        self.BusinessAddress = None
        self.PostCode = None
        self.Manager = None
        self.ManagerId = None
        self.ManagerAddress = None
        self.ManagerTelephone = None
        self.Email = None
        self.ServiceStartDate = None
        self.ServiceEndDate = None
        self.State = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.ServiceProvider = params.get("ServiceProvider")
        self.ComplianceId = params.get("ComplianceId")
        self.Company = params.get("Company")
        self.UniformSocialCreditCode = params.get("UniformSocialCreditCode")
        self.LegalPerson = params.get("LegalPerson")
        self.IssuingAuthority = params.get("IssuingAuthority")
        self.BusinessAddress = params.get("BusinessAddress")
        self.PostCode = params.get("PostCode")
        self.Manager = params.get("Manager")
        self.ManagerId = params.get("ManagerId")
        self.ManagerAddress = params.get("ManagerAddress")
        self.ManagerTelephone = params.get("ManagerTelephone")
        self.Email = params.get("Email")
        self.ServiceStartDate = params.get("ServiceStartDate")
        self.ServiceEndDate = params.get("ServiceEndDate")
        self.State = params.get("State")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCrossBorderComplianceResponse(AbstractModel):
    """DescribeCrossBorderCompliance返回参数结构体

    """

    def __init__(self):
        """
        :param CrossBorderComplianceSet: 合规化审批单列表。\n        :type CrossBorderComplianceSet: list of CrossBorderCompliance\n        :param TotalCount: 合规化审批单总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CrossBorderComplianceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CrossBorderComplianceSet") is not None:
            self.CrossBorderComplianceSet = []
            for item in params.get("CrossBorderComplianceSet"):
                obj = CrossBorderCompliance()
                obj._deserialize(item)
                self.CrossBorderComplianceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCustomerGatewayVendorsRequest(AbstractModel):
    """DescribeCustomerGatewayVendors请求参数结构体

    """


class DescribeCustomerGatewayVendorsResponse(AbstractModel):
    """DescribeCustomerGatewayVendors返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayVendorSet: 对端网关厂商信息对象。\n        :type CustomerGatewayVendorSet: list of CustomerGatewayVendor\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CustomerGatewayIds: 对端网关ID，例如：cgw-2wqq41m9。每次请求的实例的上限为100。参数不支持同时指定CustomerGatewayIds和Filters。\n        :type CustomerGatewayIds: list of str\n        :param Filters: 过滤条件，详见下表：实例过滤条件表。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定CustomerGatewayIds和Filters。
<li>customer-gateway-id - String - （过滤条件）用户网关唯一ID形如：`cgw-mgp33pll`。</li>
<li>customer-gateway-name - String - （过滤条件）用户网关名称形如：`test-cgw`。</li>
<li>ip-address - String - （过滤条件）公网地址形如：`58.211.1.12`。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCustomerGatewaysResponse(AbstractModel):
    """DescribeCustomerGateways返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewaySet: 对端网关对象列表\n        :type CustomerGatewaySet: list of CustomerGateway\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDhcpIpsRequest(AbstractModel):
    """DescribeDhcpIps请求参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpIds: DhcpIp实例ID。形如：dhcpip-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定DhcpIpIds和Filters。\n        :type DhcpIpIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定DhcpIpIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。</li>
<li>dhcpip-id - String - （过滤条件）DhcpIp实例ID，形如：dhcpip-pxir56ns。</li>
<li>dhcpip-name - String - （过滤条件）DhcpIp实例名称。</li>
<li>address-ip - String - （过滤条件）DhcpIp实例的IP，根据IP精确查找。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.DhcpIpIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DhcpIpIds = params.get("DhcpIpIds")
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
        


class DescribeDhcpIpsResponse(AbstractModel):
    """DescribeDhcpIps返回参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpSet: 实例详细信息列表。\n        :type DhcpIpSet: list of DhcpIp\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DhcpIpSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DhcpIpSet") is not None:
            self.DhcpIpSet = []
            for item in params.get("DhcpIpSet"):
                obj = DhcpIp()
                obj._deserialize(item)
                self.DhcpIpSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：`dcg-prpqlmg1`。\n        :type DirectConnectGatewayId: str\n        :param CcnRouteType: 云联网路由学习类型，可选值：
<li>`BGP` - 自动学习。</li>
<li>`STATIC` - 静态，即用户配置，默认值。</li>\n        :type CcnRouteType: str\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param Limit: 返回数量。\n        :type Limit: int\n        """
        self.DirectConnectGatewayId = None
        self.CcnRouteType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.CcnRouteType = params.get("CcnRouteType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """DescribeDirectConnectGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param RouteSet: 云联网路由（IDC网段）列表。\n        :type RouteSet: list of DirectConnectGatewayCcnRoute\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param DirectConnectGatewayIds: 专线网关唯一`ID`，形如：`dcg-9o233uri`。\n        :type DirectConnectGatewayIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定`DirectConnectGatewayIds`和`Filters`。
<li>direct-connect-gateway-id - String - 专线网关唯一`ID`，形如：`dcg-9o233uri`。</li>
<li>direct-connect-gateway-name - String - 专线网关名称，默认模糊查询。</li>
<li>direct-connect-gateway-ip - String - 专线网关`IP`。</li>
<li>gateway-type - String - 网关类型，可选值：`NORMAL`（普通型）、`NAT`（NAT型）。</li>
<li>network-type- String - 网络类型，可选值：`VPC`（私有网络类型）、`CCN`（云联网类型）。</li>
<li>ccn-id - String - 专线网关所在云联网`ID`。</li>
<li>vpc-id - String - 专线网关所在私有网络`ID`。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param Limit: 返回数量。\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDirectConnectGatewaysResponse(AbstractModel):
    """DescribeDirectConnectGateways返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param DirectConnectGatewaySet: 专线网关对象数组。\n        :type DirectConnectGatewaySet: list of DirectConnectGateway\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeFlowLogRequest(AbstractModel):
    """DescribeFlowLog请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私用网络ID或者统一ID，建议使用统一ID\n        :type VpcId: str\n        :param FlowLogId: 流日志唯一ID\n        :type FlowLogId: str\n        """
        self.VpcId = None
        self.FlowLogId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowLogResponse(AbstractModel):
    """DescribeFlowLog返回参数结构体

    """

    def __init__(self):
        """
        :param FlowLog: 流日志信息\n        :type FlowLog: list of FlowLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowLog = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFlowLogsRequest(AbstractModel):
    """DescribeFlowLogs请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私用网络ID或者统一ID，建议使用统一ID\n        :type VpcId: str\n        :param FlowLogId: 流日志唯一ID\n        :type FlowLogId: str\n        :param FlowLogName: 流日志实例名字\n        :type FlowLogName: str\n        :param ResourceType: 流日志所属资源类型，VPC|SUBNET|NETWORKINTERFACE\n        :type ResourceType: str\n        :param ResourceId: 资源唯一ID\n        :type ResourceId: str\n        :param TrafficType: 流日志采集类型，ACCEPT|REJECT|ALL\n        :type TrafficType: str\n        :param CloudLogId: 流日志存储ID\n        :type CloudLogId: str\n        :param CloudLogState: 流日志存储ID状态\n        :type CloudLogState: str\n        :param OrderField: 按某个字段排序,支持字段：flowLogName,createTime，默认按createTime\n        :type OrderField: str\n        :param OrderDirection: 升序（asc）还是降序（desc）,默认：desc\n        :type OrderDirection: str\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 每页行数，默认为10\n        :type Limit: int\n        :param Filters: 过滤条件，参数不支持同时指定FlowLogIds和Filters。
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。</li>\n        :type Filters: :class:`tencentcloud.vpc.v20170312.models.Filter`\n        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.CloudLogState = None
        self.OrderField = None
        self.OrderDirection = None
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.CloudLogState = params.get("CloudLogState")
        self.OrderField = params.get("OrderField")
        self.OrderDirection = params.get("OrderDirection")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = Filter()
            self.Filters._deserialize(params.get("Filters"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFlowLogsResponse(AbstractModel):
    """DescribeFlowLogs返回参数结构体

    """

    def __init__(self):
        """
        :param FlowLog: 流日志实例集合\n        :type FlowLog: list of FlowLog\n        :param TotalNum: 流日志总数目\n        :type TotalNum: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.FlowLog = None
        self.TotalNum = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("FlowLog") is not None:
            self.FlowLog = []
            for item in params.get("FlowLog"):
                obj = FlowLog()
                obj._deserialize(item)
                self.FlowLog.append(obj)
        self.TotalNum = params.get("TotalNum")
        self.RequestId = params.get("RequestId")


class DescribeGatewayFlowMonitorDetailRequest(AbstractModel):
    """DescribeGatewayFlowMonitorDetail请求参数结构体

    """

    def __init__(self):
        """
        :param TimePoint: 时间点。表示要查询这分钟内的明细。如：`2019-02-28 18:15:20`，将查询 `18:15` 这一分钟内的明细。\n        :type TimePoint: str\n        :param VpnId: VPN网关实例ID，形如：`vpn-ltjahce6`。\n        :type VpnId: str\n        :param DirectConnectGatewayId: 专线网关实例ID，形如：`dcg-ltjahce6`。\n        :type DirectConnectGatewayId: str\n        :param PeeringConnectionId: 对等连接实例ID，形如：`pcx-ltjahce6`。\n        :type PeeringConnectionId: str\n        :param NatId: NAT网关实例ID，形如：`nat-ltjahce6`。\n        :type NatId: str\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param Limit: 返回数量。\n        :type Limit: int\n        :param OrderField: 排序字段。支持 `InPkg` `OutPkg` `InTraffic` `OutTraffic`。\n        :type OrderField: str\n        :param OrderDirection: 排序方法。顺序：`ASC`，倒序：`DESC`。\n        :type OrderDirection: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayFlowMonitorDetailResponse(AbstractModel):
    """DescribeGatewayFlowMonitorDetail返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param GatewayFlowMonitorDetailSet: 网关流量监控明细。\n        :type GatewayFlowMonitorDetailSet: list of GatewayFlowMonitorDetail\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeGatewayFlowQosRequest(AbstractModel):
    """DescribeGatewayFlowQos请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: 网关实例ID，目前我们支持的网关实例类型有，
专线网关实例ID，形如，`dcg-ltjahce6`；
Nat网关实例ID，形如，`nat-ltjahce6`；
VPN网关实例ID，形如，`vpn-ltjahce6`。\n        :type GatewayId: str\n        :param IpAddresses: 限流的云服务器内网IP。\n        :type IpAddresses: list of str\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.GatewayId = None
        self.IpAddresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.IpAddresses = params.get("IpAddresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGatewayFlowQosResponse(AbstractModel):
    """DescribeGatewayFlowQos返回参数结构体

    """

    def __init__(self):
        """
        :param GatewayQosSet: 实例详细信息列表。\n        :type GatewayQosSet: list of GatewayQos\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.GatewayQosSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GatewayQosSet") is not None:
            self.GatewayQosSet = []
            for item in params.get("GatewayQosSet"):
                obj = GatewayQos()
                obj._deserialize(item)
                self.GatewayQosSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHaVipsRequest(AbstractModel):
    """DescribeHaVips请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipIds: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。\n        :type HaVipIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定`HaVipIds`和`Filters`。
<li>havip-id - String - `HAVIP`唯一`ID`，形如：`havip-9o233uri`。</li>
<li>havip-name - String - `HAVIP`名称。</li>
<li>vpc-id - String - `HAVIP`所在私有网络`ID`。</li>
<li>subnet-id - String - `HAVIP`所在子网`ID`。</li>
<li>vip - String - `HAVIP`的地址`VIP`。</li>
<li>address-ip - String - `HAVIP`绑定的弹性公网`IP`。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        """
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
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param HaVipSet: `HAVIP`对象数组。\n        :type HaVipSet: list of HaVip\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeIp6AddressesRequest(AbstractModel):
    """DescribeIp6Addresses请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6AddressIds: 标识 IPV6 的唯一 ID 列表。IPV6 唯一 ID 形如：`eip-11112222`。参数不支持同时指定`Ip6AddressIds`和`Filters`。\n        :type Ip6AddressIds: list of str\n        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`AddressIds`和`Filters`。详细的过滤条件如下：
<li> address-ip - String - 是否必填：否 - （过滤条件）按照 EIP 的 IP 地址过滤。</li>
<li> network-interface-id - String - 是否必填：否 - （过滤条件）按照弹性网卡的唯一ID过滤。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Limit: int\n        """
        self.Ip6AddressIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Ip6AddressIds = params.get("Ip6AddressIds")
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
        


class DescribeIp6AddressesResponse(AbstractModel):
    """DescribeIp6Addresses返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的 IPV6 数量。\n        :type TotalCount: int\n        :param AddressSet: IPV6 详细信息列表。\n        :type AddressSet: list of Address\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeIp6TranslatorQuotaRequest(AbstractModel):
    """DescribeIp6TranslatorQuota请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorIds: 待查询IPV6转换实例的唯一ID列表，形如ip6-xxxxxxxx\n        :type Ip6TranslatorIds: list of str\n        """
        self.Ip6TranslatorIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorIds = params.get("Ip6TranslatorIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIp6TranslatorQuotaResponse(AbstractModel):
    """DescribeIp6TranslatorQuota返回参数结构体

    """

    def __init__(self):
        """
        :param QuotaSet: 账户在指定地域的IPV6转换实例及规则配额信息
QUOTAID属性是TOTAL_TRANSLATOR_QUOTA，表示账户在指定地域的IPV6转换实例配额信息；QUOTAID属性是IPV6转换实例唯一ID（形如ip6-xxxxxxxx），表示账户在该转换实例允许创建的转换规则配额\n        :type QuotaSet: list of Quota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Ip6TranslatorIds: IPV6转换实例唯一ID数组，形如ip6-xxxxxxxx\n        :type Ip6TranslatorIds: list of str\n        :param Filters: 每次请求的`Filters`的上限为10，`Filter.Values`的上限为5。参数不支持同时指定`Ip6TranslatorIds`和`Filters`。详细的过滤条件如下：
<li> ip6-translator-id - String - 是否必填：否 - （过滤条件）按照IPV6转换实例的唯一ID过滤,形如ip6-xxxxxxx。</li>
<li> ip6-translator-vip6 - String - 是否必填：否 - （过滤条件）按照IPV6地址过滤。不支持模糊过滤。</li>
<li> ip6-translator-name - String - 是否必填：否 - （过滤条件）按照IPV6转换实例名称过滤。不支持模糊过滤。</li>
<li> ip6-translator-status - String - 是否必填：否 - （过滤条件）按照IPV6转换实例的状态过滤。状态取值范围为"CREATING","RUNNING","DELETING","MODIFYING"\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIp6TranslatorsResponse(AbstractModel):
    """DescribeIp6Translators返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合过滤条件的IPV6转换实例数量。\n        :type TotalCount: int\n        :param Ip6TranslatorSet: 符合过滤条件的IPV6转换实例详细信息\n        :type Ip6TranslatorSet: list of Ip6Translator\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeIpGeolocationDatabaseUrlRequest(AbstractModel):
    """DescribeIpGeolocationDatabaseUrl请求参数结构体

    """

    def __init__(self):
        """
        :param Type: IP地理位置库协议类型，目前仅支持"ipv4"。\n        :type Type: str\n        """
        self.Type = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpGeolocationDatabaseUrlResponse(AbstractModel):
    """DescribeIpGeolocationDatabaseUrl返回参数结构体

    """

    def __init__(self):
        """
        :param DownLoadUrl: IP地理位置库下载链接地址。\n        :type DownLoadUrl: str\n        :param ExpiredAt: 链接到期时间。按照`ISO8601`标准表示，并且使用`UTC`时间。\n        :type ExpiredAt: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DownLoadUrl = None
        self.ExpiredAt = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DownLoadUrl = params.get("DownLoadUrl")
        self.ExpiredAt = params.get("ExpiredAt")
        self.RequestId = params.get("RequestId")


class DescribeIpGeolocationInfosRequest(AbstractModel):
    """DescribeIpGeolocationInfos请求参数结构体

    """

    def __init__(self):
        """
        :param AddressIps: 查询IP地址列表，支持IPv4和IPv6。\n        :type AddressIps: list of str\n        :param Fields: 查询IP地址的字段信息，包括"Country","Province","City","Region","Isp","AsName","AsId"\n        :type Fields: :class:`tencentcloud.vpc.v20170312.models.IpField`\n        """
        self.AddressIps = None
        self.Fields = None


    def _deserialize(self, params):
        self.AddressIps = params.get("AddressIps")
        if params.get("Fields") is not None:
            self.Fields = IpField()
            self.Fields._deserialize(params.get("Fields"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpGeolocationInfosResponse(AbstractModel):
    """DescribeIpGeolocationInfos返回参数结构体

    """

    def __init__(self):
        """
        :param AddressInfo: IP地址信息列表\n        :type AddressInfo: list of IpGeolocationInfo\n        :param Total: IP地址信息个数\n        :type Total: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AddressInfo = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AddressInfo") is not None:
            self.AddressInfo = []
            for item in params.get("AddressInfo"):
                obj = IpGeolocationInfo()
                obj._deserialize(item)
                self.AddressInfo.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeLocalGatewayRequest(AbstractModel):
    """DescribeLocalGateway请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 查询条件：
vpc-id：按照VPCID过滤，local-gateway-name：按照本地网关名称过滤，名称支持模糊搜索，local-gateway-id：按照本地网关实例ID过滤，cdc-id：按照cdc实例ID过滤查询。\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于`Offset`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。关于`Limit`的更进一步介绍请参考 API [简介](https://cloud.tencent.com/document/api/213/11646)中的相关小节。\n        :type Limit: int\n        """
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
        


class DescribeLocalGatewayResponse(AbstractModel):
    """DescribeLocalGateway返回参数结构体

    """

    def __init__(self):
        """
        :param LocalGatewaySet: 本地网关信息集合\n        :type LocalGatewaySet: list of LocalGateway\n        :param TotalCount: 本地网关总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LocalGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("LocalGatewaySet") is not None:
            self.LocalGatewaySet = []
            for item in params.get("LocalGatewaySet"):
                obj = LocalGateway()
                obj._deserialize(item)
                self.LocalGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewayDestinationIpPortTranslationNatRulesRequest(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayIds: NAT网关ID。\n        :type NatGatewayIds: list of str\n        :param Filters: 过滤条件:
参数不支持同时指定NatGatewayIds和Filters。
<li> nat-gateway-id，NAT网关的ID，如`nat-0yi4hekt`</li>
<li> vpc-id，私有网络VPC的ID，如`vpc-0yi4hekt`</li>
<li> public-ip-address， 弹性IP，如`139.199.232.238`。</li>
<li>public-port， 公网端口。</li>
<li>private-ip-address， 内网IP，如`10.0.0.1`。</li>
<li>private-port， 内网端口。</li>
<li>description，规则描述。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.NatGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayIds = params.get("NatGatewayIds")
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
        


class DescribeNatGatewayDestinationIpPortTranslationNatRulesResponse(AbstractModel):
    """DescribeNatGatewayDestinationIpPortTranslationNatRules返回参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayDestinationIpPortTranslationNatRuleSet: NAT网关端口转发规则对象数组。\n        :type NatGatewayDestinationIpPortTranslationNatRuleSet: list of NatGatewayDestinationIpPortTranslationNatRule\n        :param TotalCount: 符合条件的NAT网关端口转发规则对象数目。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NatGatewayDestinationIpPortTranslationNatRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewayDestinationIpPortTranslationNatRuleSet") is not None:
            self.NatGatewayDestinationIpPortTranslationNatRuleSet = []
            for item in params.get("NatGatewayDestinationIpPortTranslationNatRuleSet"):
                obj = NatGatewayDestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.NatGatewayDestinationIpPortTranslationNatRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewaySourceIpTranslationNatRulesRequest(AbstractModel):
    """DescribeNatGatewaySourceIpTranslationNatRules请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关统一 ID，形如：`nat-123xx454`。\n        :type NatGatewayId: str\n        :param Filters: 过滤条件:
<li> resource-id，Subnet的ID或者Cvm ID，如`subnet-0yi4hekt`</li>
<li> public-ip-address，弹性IP，如`139.199.232.238`</li>
<li>description，规则描述。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.NatGatewayId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
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
        


class DescribeNatGatewaySourceIpTranslationNatRulesResponse(AbstractModel):
    """DescribeNatGatewaySourceIpTranslationNatRules返回参数结构体

    """

    def __init__(self):
        """
        :param SourceIpTranslationNatRuleSet: NAT网关SNAT规则对象数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceIpTranslationNatRuleSet: list of SourceIpTranslationNatRule\n        :param TotalCount: 符合条件的NAT网关端口转发规则对象数目。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SourceIpTranslationNatRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SourceIpTranslationNatRuleSet") is not None:
            self.SourceIpTranslationNatRuleSet = []
            for item in params.get("SourceIpTranslationNatRuleSet"):
                obj = SourceIpTranslationNatRule()
                obj._deserialize(item)
                self.SourceIpTranslationNatRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNatGatewaysRequest(AbstractModel):
    """DescribeNatGateways请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayIds: NAT网关统一 ID，形如：`nat-123xx454`。\n        :type NatGatewayIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定NatGatewayIds和Filters。
<li>nat-gateway-id - String - （过滤条件）协议端口模板实例ID，形如：`nat-123xx454`。</li>
<li>vpc-id - String - （过滤条件）私有网络 唯一ID，形如：`vpc-123xx454`。</li>
<li>nat-gateway-name - String - （过滤条件）协议端口模板实例ID，形如：`test_nat`。</li>
<li>tag-key - String - （过滤条件）标签键，形如：`test-key`。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.NatGatewayIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NatGatewayIds = params.get("NatGatewayIds")
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
        


class DescribeNatGatewaysResponse(AbstractModel):
    """DescribeNatGateways返回参数结构体

    """

    def __init__(self):
        """
        :param NatGatewaySet: NAT网关对象数组。\n        :type NatGatewaySet: list of NatGateway\n        :param TotalCount: 符合条件的NAT网关对象个数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NatGatewaySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NatGatewaySet") is not None:
            self.NatGatewaySet = []
            for item in params.get("NatGatewaySet"):
                obj = NatGateway()
                obj._deserialize(item)
                self.NatGatewaySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetDetectStatesRequest(AbstractModel):
    """DescribeNetDetectStates请求参数结构体

    """

    def __init__(self):
        """
        :param NetDetectIds: 网络探测实例`ID`数组。形如：[`netd-12345678`]\n        :type NetDetectIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定NetDetectIds和Filters。
<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.NetDetectIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetDetectIds = params.get("NetDetectIds")
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
        


class DescribeNetDetectStatesResponse(AbstractModel):
    """DescribeNetDetectStates返回参数结构体

    """

    def __init__(self):
        """
        :param NetDetectStateSet: 符合条件的网络探测验证结果对象数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetDetectStateSet: list of NetDetectState\n        :param TotalCount: 符合条件的网络探测验证结果对象数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetDetectStateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectStateSet") is not None:
            self.NetDetectStateSet = []
            for item in params.get("NetDetectStateSet"):
                obj = NetDetectState()
                obj._deserialize(item)
                self.NetDetectStateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetDetectsRequest(AbstractModel):
    """DescribeNetDetects请求参数结构体

    """

    def __init__(self):
        """
        :param NetDetectIds: 网络探测实例`ID`数组。形如：[`netd-12345678`]\n        :type NetDetectIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定NetDetectIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-12345678</li>
<li>net-detect-id - String - （过滤条件）网络探测实例ID，形如：netd-12345678</li>
<li>subnet-id - String - （过滤条件）子网实例ID，形如：subnet-12345678</li>
<li>net-detect-name - String - （过滤条件）网络探测名称</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
        self.NetDetectIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.NetDetectIds = params.get("NetDetectIds")
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
        


class DescribeNetDetectsResponse(AbstractModel):
    """DescribeNetDetects返回参数结构体

    """

    def __init__(self):
        """
        :param NetDetectSet: 符合条件的网络探测对象数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetDetectSet: list of NetDetect\n        :param TotalCount: 符合条件的网络探测对象数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetDetectSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetDetectSet") is not None:
            self.NetDetectSet = []
            for item in params.get("NetDetectSet"):
                obj = NetDetect()
                obj._deserialize(item)
                self.NetDetectSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetworkAclsRequest(AbstractModel):
    """DescribeNetworkAcls请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，参数不支持同时指定NetworkAclIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-12345678。</li>
<li>network-acl-id - String - （过滤条件）网络ACL实例ID，形如：acl-12345678。</li>
<li>network-acl-name - String - （过滤条件）网络ACL实例名称。</li>\n        :type Filters: list of Filter\n        :param NetworkAclIds: 网络ACL实例ID数组。形如：[acl-12345678]。每次请求的实例的上限为100。参数不支持同时指定NetworkAclIds和Filters。\n        :type NetworkAclIds: list of str\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最小值为1，最大值为100。\n        :type Limit: int\n        """
        self.Filters = None
        self.NetworkAclIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.NetworkAclIds = params.get("NetworkAclIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkAclsResponse(AbstractModel):
    """DescribeNetworkAcls返回参数结构体

    """

    def __init__(self):
        """
        :param NetworkAclSet: 实例详细信息列表。\n        :type NetworkAclSet: list of NetworkAcl\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.NetworkAclSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("NetworkAclSet") is not None:
            self.NetworkAclSet = []
            for item in params.get("NetworkAclSet"):
                obj = NetworkAcl()
                obj._deserialize(item)
                self.NetworkAclSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfaceLimitRequest(AbstractModel):
    """DescribeNetworkInterfaceLimit请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 要查询的CVM实例ID或弹性网卡ID\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNetworkInterfaceLimitResponse(AbstractModel):
    """DescribeNetworkInterfaceLimit返回参数结构体

    """

    def __init__(self):
        """
        :param EniQuantity: 标准型弹性网卡配额\n        :type EniQuantity: int\n        :param EniPrivateIpAddressQuantity: 每个标准型弹性网卡可以分配的IP配额\n        :type EniPrivateIpAddressQuantity: int\n        :param ExtendEniQuantity: 扩展型网卡配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtendEniQuantity: int\n        :param ExtendEniPrivateIpAddressQuantity: 每个扩展型弹性网卡可以分配的IP配额
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExtendEniPrivateIpAddressQuantity: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EniQuantity = None
        self.EniPrivateIpAddressQuantity = None
        self.ExtendEniQuantity = None
        self.ExtendEniPrivateIpAddressQuantity = None
        self.RequestId = None


    def _deserialize(self, params):
        self.EniQuantity = params.get("EniQuantity")
        self.EniPrivateIpAddressQuantity = params.get("EniPrivateIpAddressQuantity")
        self.ExtendEniQuantity = params.get("ExtendEniQuantity")
        self.ExtendEniPrivateIpAddressQuantity = params.get("ExtendEniPrivateIpAddressQuantity")
        self.RequestId = params.get("RequestId")


class DescribeNetworkInterfacesRequest(AbstractModel):
    """DescribeNetworkInterfaces请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 弹性网卡实例ID查询。形如：eni-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定NetworkInterfaceIds和Filters。\n        :type NetworkInterfaceIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定NetworkInterfaceIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>subnet-id - String - （过滤条件）所属子网实例ID，形如：subnet-f49l6u0z。</li>
<li>network-interface-id - String - （过滤条件）弹性网卡实例ID，形如：eni-5k56k7k7。</li>
<li>attachment.instance-id - String - （过滤条件）绑定的云服务器实例ID，形如：ins-3nqpdn3i。</li>
<li>groups.security-group-id - String - （过滤条件）绑定的安全组实例ID，例如：sg-f9ekbxeq。</li>
<li>network-interface-name - String - （过滤条件）网卡实例名称。</li>
<li>network-interface-description - String - （过滤条件）网卡实例描述。</li>
<li>address-ip - String - （过滤条件）内网IPv4地址，单IP后缀模糊匹配，多IP精确匹配。可以与`ip-exact-match`配合做单IP的精确匹配查询。</li>
<li>ip-exact-match - Boolean - （过滤条件）内网IPv4精确匹配查询，存在多值情况，只取第一个。</li>
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。使用请参考示例2</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3。</li>
<li>is-primary - Boolean - 是否必填：否 - （过滤条件）按照是否主网卡进行过滤。值为true时，仅过滤主网卡；值为false时，仅过滤辅助网卡；此过滤参数未提供时，同时过滤主网卡和辅助网卡。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
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
        :param NetworkInterfaceSet: 实例详细信息列表。\n        :type NetworkInterfaceSet: list of NetworkInterface\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeProductQuotaRequest(AbstractModel):
    """DescribeProductQuota请求参数结构体

    """

    def __init__(self):
        """
        :param Product: 查询的网络产品名称，如vpc、ccn等\n        :type Product: str\n        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProductQuotaResponse(AbstractModel):
    """DescribeProductQuota返回参数结构体

    """

    def __init__(self):
        """
        :param ProductQuotaSet: ProductQuota对象数组\n        :type ProductQuotaSet: list of ProductQuota\n        :param TotalCount: 符合条件的产品类型个数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ProductQuotaSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProductQuotaSet") is not None:
            self.ProductQuotaSet = []
            for item in params.get("ProductQuotaSet"):
                obj = ProductQuota()
                obj._deserialize(item)
                self.ProductQuotaSet.append(obj)
        self.TotalCount = params.get("TotalCount")
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
        :param RouteConflictSet: 路由策略冲突列表\n        :type RouteConflictSet: list of RouteConflict\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
<li>route-table-id - String - （过滤条件）路由表实例ID。</li>
<li>route-table-name - String - （过滤条件）路由表名称。</li>
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>association.main - String - （过滤条件）是否主路由表。</li>
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2。</li>\n        :type Filters: list of Filter\n        :param RouteTableIds: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableIds: list of str\n        :param Offset: 偏移量。\n        :type Offset: str\n        :param Limit: 请求对象个数。\n        :type Limit: str\n        """
        self.Filters = None
        self.RouteTableIds = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.RouteTableIds = params.get("RouteTableIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RouteTableSet: 路由表对象。\n        :type RouteTableSet: list of RouteTable\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SecurityGroupIds: 安全实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupIds: list of str\n        """
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
        :param SecurityGroupLimitSet: 用户安全组配额限制。\n        :type SecurityGroupLimitSet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupLimitSet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SecurityGroupId: 安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        """
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
        :param SecurityGroupPolicySet: 安全组规则集合。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SecurityGroupPolicySet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupReferencesRequest(AbstractModel):
    """DescribeSecurityGroupReferences请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全组实例ID数组。格式如：['sg-12345678']\n        :type SecurityGroupIds: list of str\n        """
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupReferencesResponse(AbstractModel):
    """DescribeSecurityGroupReferences返回参数结构体

    """

    def __init__(self):
        """
        :param ReferredSecurityGroupSet: 安全组被引用信息。\n        :type ReferredSecurityGroupSet: list of ReferredSecurityGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ReferredSecurityGroupSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ReferredSecurityGroupSet") is not None:
            self.ReferredSecurityGroupSet = []
            for item in params.get("ReferredSecurityGroupSet"):
                obj = ReferredSecurityGroup()
                obj._deserialize(item)
                self.ReferredSecurityGroupSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityGroupsRequest(AbstractModel):
    """DescribeSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。参数不支持同时指定SecurityGroupIds和Filters。\n        :type SecurityGroupIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定SecurityGroupIds和Filters。
<li>security-group-id - String - （过滤条件）安全组ID。</li>
<li>project-id - Integer - （过滤条件）项目ID。</li>
<li>security-group-name - String - （过滤条件）安全组名称。</li>
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。使用请参考示例2。</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例3。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        :param SecurityGroupSet: 安全组对象。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroupSet: list of SecurityGroup\n        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
<li>service-template-group-id - String - （过滤条件）协议端口模板集合实例ID，例如：ppmg-e6dy460g。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        


class DescribeServiceTemplateGroupsResponse(AbstractModel):
    """DescribeServiceTemplateGroups返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param ServiceTemplateGroupSet: 协议端口模板集合。\n        :type ServiceTemplateGroupSet: list of ServiceTemplateGroup\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
<li>service-template-id - String - （过滤条件）协议端口模板实例ID，例如：ppm-e6dy460g。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        


class DescribeServiceTemplatesResponse(AbstractModel):
    """DescribeServiceTemplates返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param ServiceTemplateSet: 协议端口模板对象。\n        :type ServiceTemplateSet: list of ServiceTemplate\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param SubnetIds: 子网实例ID查询。形如：subnet-pxir56ns。每次请求的实例的上限为100。参数不支持同时指定SubnetIds和Filters。\n        :type SubnetIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定SubnetIds和Filters。
<li>subnet-id - String - （过滤条件）Subnet实例名称。</li>
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>cidr-block - String - （过滤条件）子网网段，形如: 192.168.1.0 。</li>
<li>is-default - Boolean - （过滤条件）是否是默认子网。</li>
<li>is-remote-vpc-snat - Boolean - （过滤条件）是否为VPC SNAT地址池子网。</li>
<li>subnet-name - String - （过滤条件）子网名称。</li>
<li>zone - String - （过滤条件）可用区。</li>
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2。</li>
<li>cdc-id - String - 是否必填：否 - （过滤条件）按照cdc信息进行过滤。过滤出来制定cdc下的子网。</li>
<li>is-cdc-subnet - String - 是否必填：否 - （过滤条件）按照是否是cdc子网进行过滤。取值：“0”-非cdc子网，“1”--cdc子网</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param SubnetSet: 子网对象。\n        :type SubnetSet: list of Subnet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTaskResultRequest(AbstractModel):
    """DescribeTaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务ID。TaskId和DealName必填一个参数\n        :type TaskId: int\n        :param DealName: 计费订单号。TaskId和DealName必填一个参数\n        :type DealName: str\n        """
        self.TaskId = None
        self.DealName = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.DealName = params.get("DealName")
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
        :param TaskId: 任务ID\n        :type TaskId: int\n        :param Result: 执行结果，包括"SUCCESS", "FAILED", "RUNNING"\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeTemplateLimitsRequest(AbstractModel):
    """DescribeTemplateLimits请求参数结构体

    """


class DescribeTemplateLimitsResponse(AbstractModel):
    """DescribeTemplateLimits返回参数结构体

    """

    def __init__(self):
        """
        :param TemplateLimit: 参数模板配额对象。\n        :type TemplateLimit: :class:`tencentcloud.vpc.v20170312.models.TemplateLimit`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TemplateLimit = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TemplateLimit") is not None:
            self.TemplateLimit = TemplateLimit()
            self.TemplateLimit._deserialize(params.get("TemplateLimit"))
        self.RequestId = params.get("RequestId")


class DescribeVpcEndPointRequest(AbstractModel):
    """DescribeVpcEndPoint请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li> end-point-service-id- String - （过滤条件）终端节点服务ID。</li>
<li>end-point-name - String - （过滤条件）终端节点实例名称。</li>
<li> end-point-id- String - （过滤条件）终端节点实例ID。</li>
<li> vpc-id- String - （过滤条件）VPC实例ID。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 单页返回数量，默认为20，最大值为100。\n        :type Limit: int\n        :param EndPointId: 终端节点ID列表。\n        :type EndPointId: list of str\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EndPointId = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcEndPointResponse(AbstractModel):
    """DescribeVpcEndPoint返回参数结构体

    """

    def __init__(self):
        """
        :param EndPointSet: 终端节点对象。\n        :type EndPointSet: list of EndPoint\n        :param TotalCount: 符合查询条件的终端节点个数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EndPointSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPointSet") is not None:
            self.EndPointSet = []
            for item in params.get("EndPointSet"):
                obj = EndPoint()
                obj._deserialize(item)
                self.EndPointSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcEndPointServiceRequest(AbstractModel):
    """DescribeVpcEndPointService请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件。
<li> service-id- String - （过滤条件）终端节点服务唯一ID。</li>
<li>service-name - String - （过滤条件）终端节点实例名称。</li>
<li>service-instance-id - String - （过滤条件）后端服务的唯一ID，比如lb-xxx。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 单页返回数量，默认为20，最大值为100。\n        :type Limit: int\n        :param EndPointServiceIds: 终端节点服务ID。\n        :type EndPointServiceIds: list of str\n        """
        self.Filters = None
        self.Offset = None
        self.Limit = None
        self.EndPointServiceIds = None


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.EndPointServiceIds = params.get("EndPointServiceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcEndPointServiceResponse(AbstractModel):
    """DescribeVpcEndPointService返回参数结构体

    """

    def __init__(self):
        """
        :param EndPointServiceSet: 终端节点服务对象数组。\n        :type EndPointServiceSet: list of EndPointService\n        :param TotalCount: 符合查询条件的个数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.EndPointServiceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("EndPointServiceSet") is not None:
            self.EndPointServiceSet = []
            for item in params.get("EndPointServiceSet"):
                obj = EndPointService()
                obj._deserialize(item)
                self.EndPointServiceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcEndPointServiceWhiteListRequest(AbstractModel):
    """DescribeVpcEndPointServiceWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 单页返回数量，默认为20，最大值为100。\n        :type Limit: int\n        :param Filters: 过滤条件。
<li> user-uin String - （过滤条件）用户UIN。</li>
<li> end-point-service-id String - （过滤条件）终端节点服务ID。</li>\n        :type Filters: list of Filter\n        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
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
        


class DescribeVpcEndPointServiceWhiteListResponse(AbstractModel):
    """DescribeVpcEndPointServiceWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param VpcEndpointServiceUserSet: 白名单对象数组。\n        :type VpcEndpointServiceUserSet: list of VpcEndPointServiceUser\n        :param TotalCount: 符合条件的白名单个数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.VpcEndpointServiceUserSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcEndpointServiceUserSet") is not None:
            self.VpcEndpointServiceUserSet = []
            for item in params.get("VpcEndpointServiceUserSet"):
                obj = VpcEndPointServiceUser()
                obj._deserialize(item)
                self.VpcEndpointServiceUserSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcInstancesRequest(AbstractModel):
    """DescribeVpcInstances请求参数结构体

    """

    def __init__(self):
        """
        :param Filters: 过滤条件，参数不支持同时指定RouteTableIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID，形如：vpc-f49l6u0z。</li>
<li>instance-id - String - （过滤条件）云主机实例ID。</li>
<li>instance-name - String - （过滤条件）云主机名称。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param Limit: 请求对象个数。\n        :type Limit: int\n        """
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
        


class DescribeVpcInstancesResponse(AbstractModel):
    """DescribeVpcInstances返回参数结构体

    """

    def __init__(self):
        """
        :param InstanceSet: 云主机实例列表。\n        :type InstanceSet: list of CvmInstance\n        :param TotalCount: 满足条件的云主机实例个数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.InstanceSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = CvmInstance()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcIpv6AddressesRequest(AbstractModel):
    """DescribeVpcIpv6Addresses请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。\n        :type VpcId: str\n        :param Ipv6Addresses: `IP`地址列表，批量查询单次请求最多支持`10`个。\n        :type Ipv6Addresses: list of str\n        :param Offset: 偏移量。\n        :type Offset: int\n        :param Limit: 返回数量。\n        :type Limit: int\n        """
        self.VpcId = None
        self.Ipv6Addresses = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6Addresses = params.get("Ipv6Addresses")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcIpv6AddressesResponse(AbstractModel):
    """DescribeVpcIpv6Addresses返回参数结构体

    """

    def __init__(self):
        """
        :param Ipv6AddressSet: `IPv6`地址列表。\n        :type Ipv6AddressSet: list of VpcIpv6Address\n        :param TotalCount: `IPv6`地址总数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Ipv6AddressSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ipv6AddressSet") is not None:
            self.Ipv6AddressSet = []
            for item in params.get("Ipv6AddressSet"):
                obj = VpcIpv6Address()
                obj._deserialize(item)
                self.Ipv6AddressSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpcLimitsRequest(AbstractModel):
    """DescribeVpcLimits请求参数结构体

    """

    def __init__(self):
        """
        :param LimitTypes: 配额名称。每次最大查询100个配额类型。\n        :type LimitTypes: list of str\n        """
        self.LimitTypes = None


    def _deserialize(self, params):
        self.LimitTypes = params.get("LimitTypes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcLimitsResponse(AbstractModel):
    """DescribeVpcLimits返回参数结构体

    """

    def __init__(self):
        """
        :param VpcLimitSet: 私有网络配额\n        :type VpcLimitSet: list of VpcLimit\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.VpcLimitSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("VpcLimitSet") is not None:
            self.VpcLimitSet = []
            for item in params.get("VpcLimitSet"):
                obj = VpcLimit()
                obj._deserialize(item)
                self.VpcLimitSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcPrivateIpAddressesRequest(AbstractModel):
    """DescribeVpcPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。\n        :type VpcId: str\n        :param PrivateIpAddresses: 内网`IP`地址列表，批量查询单次请求最多支持`10`个。\n        :type PrivateIpAddresses: list of str\n        """
        self.VpcId = None
        self.PrivateIpAddresses = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.PrivateIpAddresses = params.get("PrivateIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcPrivateIpAddressesResponse(AbstractModel):
    """DescribeVpcPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param VpcPrivateIpAddressSet: 内网`IP`地址信息列表。\n        :type VpcPrivateIpAddressSet: list of VpcPrivateIpAddress\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeVpcResourceDashboardRequest(AbstractModel):
    """DescribeVpcResourceDashboard请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: Vpc实例ID，例如：vpc-f1xjkw1b。\n        :type VpcIds: list of str\n        """
        self.VpcIds = None


    def _deserialize(self, params):
        self.VpcIds = params.get("VpcIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcResourceDashboardResponse(AbstractModel):
    """DescribeVpcResourceDashboard返回参数结构体

    """

    def __init__(self):
        """
        :param ResourceDashboardSet: 资源对象列表。\n        :type ResourceDashboardSet: list of ResourceDashboard\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ResourceDashboardSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ResourceDashboardSet") is not None:
            self.ResourceDashboardSet = []
            for item in params.get("ResourceDashboardSet"):
                obj = ResourceDashboard()
                obj._deserialize(item)
                self.ResourceDashboardSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpcTaskResultRequest(AbstractModel):
    """DescribeVpcTaskResult请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务请求返回的RequestId。\n        :type TaskId: str\n        """
        self.TaskId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcTaskResultResponse(AbstractModel):
    """DescribeVpcTaskResult返回参数结构体

    """

    def __init__(self):
        """
        :param Status: 异步任务执行结果。结果：SUCCESS、FAILED、RUNNING。3者其中之一。其中SUCCESS表示任务执行成功，FAILED表示任务执行失败，RUNNING表示任务执行中。\n        :type Status: str\n        :param Output: 异步任务执行输出。\n        :type Output: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Status = None
        self.Output = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Output = params.get("Output")
        self.RequestId = params.get("RequestId")


class DescribeVpcsRequest(AbstractModel):
    """DescribeVpcs请求参数结构体

    """

    def __init__(self):
        """
        :param VpcIds: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。\n        :type VpcIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定VpcIds和Filters。
<li>vpc-name - String - （过滤条件）VPC实例名称。</li>
<li>is-default - String - （过滤条件）是否默认VPC。</li>
<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>
<li>cidr-block - String - （过滤条件）vpc的cidr。</li>
<li>tag-key - String -是否必填：否- （过滤条件）按照标签键进行过滤。</li>
<li>tag:tag-key - String - 是否必填：否 - （过滤条件）按照标签键值对进行过滤。 tag-key使用具体的标签键进行替换。使用请参考示例2。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。\n        :type Offset: str\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: str\n        """
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
        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param VpcSet: VPC对象。\n        :type VpcSet: list of Vpc\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpnConnectionIds: VPN通道实例ID。形如：vpnx-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnConnectionIds和Filters。\n        :type VpnConnectionIds: list of str\n        :param Filters: 过滤条件。每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定VpnConnectionIds和Filters。
<li>vpc-id - String - VPC实例ID，形如：`vpc-0a36uwkr`。</li>
<li>vpn-gateway-id - String - VPN网关实例ID，形如：`vpngw-p4lmqawn`。</li>
<li>customer-gateway-id - String - 对端网关实例ID，形如：`cgw-l4rblw63`。</li>
<li>vpn-connection-name - String - 通道名称，形如：`test-vpn`。</li>
<li>vpn-connection-id - String - 通道实例ID，形如：`vpnx-5p7vkch8"`。</li>\n        :type Filters: list of Filter\n        :param Offset: 偏移量，默认为0。关于Offset的更进一步介绍请参考 API 简介中的相关小节。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnConnectionsResponse(AbstractModel):
    """DescribeVpnConnections返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param VpnConnectionSet: VPN通道实例。\n        :type VpnConnectionSet: list of VpnConnection\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeVpnGatewayCcnRoutesRequest(AbstractModel):
    """DescribeVpnGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID\n        :type VpnGatewayId: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        """
        self.VpnGatewayId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnGatewayCcnRoutesResponse(AbstractModel):
    """DescribeVpnGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RouteSet: 云联网路由（IDC网段）列表。\n        :type RouteSet: list of VpngwCcnRoutes\n        :param TotalCount: 符合条件的对象数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RouteSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RouteSet") is not None:
            self.RouteSet = []
            for item in params.get("RouteSet"):
                obj = VpngwCcnRoutes()
                obj._deserialize(item)
                self.RouteSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewayRoutesRequest(AbstractModel):
    """DescribeVpnGatewayRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关的ID\n        :type VpnGatewayId: str\n        :param Filters: 过滤条件,  条件包括(DestinationCidr, InstanceId,InstanceType)\n        :type Filters: list of Filter\n        :param Offset: 偏移量, 默认0\n        :type Offset: int\n        :param Limit: 单页个数, 默认20, 最大值100\n        :type Limit: int\n        """
        self.VpnGatewayId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
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
        


class DescribeVpnGatewayRoutesResponse(AbstractModel):
    """DescribeVpnGatewayRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param Routes: VPN网关目的路由\n        :type Routes: list of VpnGatewayRoute\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Routes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVpnGatewaysRequest(AbstractModel):
    """DescribeVpnGateways请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayIds: VPN网关实例ID。形如：vpngw-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpnGatewayIds和Filters。\n        :type VpnGatewayIds: list of str\n        :param Filters: 过滤条件，参数不支持同时指定VpnGatewayIds和Filters。
<li>vpc-id - String - （过滤条件）VPC实例ID形如：vpc-f49l6u0z。</li>
<li>vpn-gateway-id - String - （过滤条件）VPN实例ID形如：vpngw-5aluhh9t。</li>
<li>vpn-gateway-name - String - （过滤条件）VPN实例名称。</li>
<li>type - String - （过滤条件）VPN网关类型：'IPSEC', 'SSL'。</li>
<li>public-ip-address- String - （过滤条件）公网IP。</li>
<li>renew-flag - String - （过滤条件）网关续费类型，手动续费：'NOTIFY_AND_MANUAL_RENEW'、自动续费：'NOTIFY_AND_AUTO_RENEW'。</li>
<li>zone - String - （过滤条件）VPN所在可用区，形如：ap-guangzhou-2。</li>\n        :type Filters: list of FilterObject\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 请求对象个数\n        :type Limit: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpnGatewaysResponse(AbstractModel):
    """DescribeVpnGateways返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 符合条件的实例数量。\n        :type TotalCount: int\n        :param VpnGatewaySet: VPN网关实例详细信息列表。\n        :type VpnGatewaySet: list of VpnGateway\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DestinationIpPortTranslationNatRule(AbstractModel):
    """NAT网关的端口转发规则

    """

    def __init__(self):
        """
        :param IpProtocol: 网络协议，可选值：`TCP`、`UDP`。\n        :type IpProtocol: str\n        :param PublicIpAddress: 弹性IP。\n        :type PublicIpAddress: str\n        :param PublicPort: 公网端口。\n        :type PublicPort: int\n        :param PrivateIpAddress: 内网地址。\n        :type PrivateIpAddress: str\n        :param PrivatePort: 内网端口。\n        :type PrivatePort: int\n        :param Description: NAT网关转发规则描述。\n        :type Description: str\n        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesRequest(AbstractModel):
    """DetachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param Instances: 要解关联网络实例列表\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachCcnInstancesResponse(AbstractModel):
    """DetachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachClassicLinkVpcRequest(AbstractModel):
    """DetachClassicLinkVpc请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type VpcId: str\n        :param InstanceIds: CVM实例ID查询。形如：ins-r8hr2upy。\n        :type InstanceIds: list of str\n        """
        self.VpcId = None
        self.InstanceIds = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.InstanceIds = params.get("InstanceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DetachClassicLinkVpcResponse(AbstractModel):
    """DetachClassicLinkVpc返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DetachNetworkInterfaceRequest(AbstractModel):
    """DetachNetworkInterface请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param InstanceId: CVM实例ID。形如：ins-r8hr2upy。\n        :type InstanceId: str\n        """
        self.NetworkInterfaceId = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
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


class DhcpIp(AbstractModel):
    """描述 DhcpIp 信息

    """

    def __init__(self):
        """
        :param DhcpIpId: `DhcpIp`的`ID`，是`DhcpIp`的唯一标识。\n        :type DhcpIpId: str\n        :param VpcId: `DhcpIp`所在私有网络`ID`。\n        :type VpcId: str\n        :param SubnetId: `DhcpIp`所在子网`ID`。\n        :type SubnetId: str\n        :param DhcpIpName: `DhcpIp`的名称。\n        :type DhcpIpName: str\n        :param PrivateIpAddress: IP地址。\n        :type PrivateIpAddress: str\n        :param AddressIp: 绑定`EIP`。\n        :type AddressIp: str\n        :param NetworkInterfaceId: `DhcpIp`关联弹性网卡`ID`。\n        :type NetworkInterfaceId: str\n        :param InstanceId: 被绑定的实例`ID`。\n        :type InstanceId: str\n        :param State: 状态：
<li>`AVAILABLE`：运行中</li>
<li>`UNBIND`：未绑定</li>\n        :type State: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        """
        self.DhcpIpId = None
        self.VpcId = None
        self.SubnetId = None
        self.DhcpIpName = None
        self.PrivateIpAddress = None
        self.AddressIp = None
        self.NetworkInterfaceId = None
        self.InstanceId = None
        self.State = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.DhcpIpId = params.get("DhcpIpId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.DhcpIpName = params.get("DhcpIpName")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.AddressIp = params.get("AddressIp")
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.InstanceId = params.get("InstanceId")
        self.State = params.get("State")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectGateway(AbstractModel):
    """专线网关对象。

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关`ID`。\n        :type DirectConnectGatewayId: str\n        :param DirectConnectGatewayName: 专线网关名称。\n        :type DirectConnectGatewayName: str\n        :param VpcId: 专线网关关联`VPC`实例`ID`。\n        :type VpcId: str\n        :param NetworkType: 关联网络类型：
<li>`VPC` - 私有网络</li>
<li>`CCN` - 云联网</li>\n        :type NetworkType: str\n        :param NetworkInstanceId: 关联网络实例`ID`：
<li>`NetworkType`为`VPC`时，这里为私有网络实例`ID`</li>
<li>`NetworkType`为`CCN`时，这里为云联网实例`ID`</li>\n        :type NetworkInstanceId: str\n        :param GatewayType: 网关类型：
<li>NORMAL - 标准型，注：云联网只支持标准型</li>
<li>NAT - NAT型</li>
NAT类型支持网络地址转换配置，类型确定后不能修改；一个私有网络可以创建一个NAT类型的专线网关和一个非NAT类型的专线网关\n        :type GatewayType: str\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        :param DirectConnectGatewayIp: 专线网关IP。\n        :type DirectConnectGatewayIp: str\n        :param CcnId: 专线网关关联`CCN`实例`ID`。\n        :type CcnId: str\n        :param CcnRouteType: 云联网路由学习类型：
<li>`BGP` - 自动学习。</li>
<li>`STATIC` - 静态，即用户配置。</li>\n        :type CcnRouteType: str\n        :param EnableBGP: 是否启用BGP。\n        :type EnableBGP: bool\n        :param EnableBGPCommunity: 开启和关闭BGP的community属性。\n        :type EnableBGPCommunity: bool\n        :param NatGatewayId: 绑定的NAT网关ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NatGatewayId: str\n        :param VXLANSupport: 专线网关是否支持VXLAN架构
注意：此字段可能返回 null，表示取不到有效值。\n        :type VXLANSupport: list of bool\n        :param ModeType: 云联网路由发布模式：`standard`（标准模式）、`exquisite`（精细模式）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ModeType: str\n        :param LocalZone: 是否为localZone专线网关。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocalZone: bool\n        :param Zone: 专线网关所在可用区
注意：此字段可能返回 null，表示取不到有效值。\n        :type Zone: str\n        """
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
        self.EnableBGPCommunity = None
        self.NatGatewayId = None
        self.VXLANSupport = None
        self.ModeType = None
        self.LocalZone = None
        self.Zone = None


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
        self.EnableBGPCommunity = params.get("EnableBGPCommunity")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VXLANSupport = params.get("VXLANSupport")
        self.ModeType = params.get("ModeType")
        self.LocalZone = params.get("LocalZone")
        self.Zone = params.get("Zone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DirectConnectGatewayCcnRoute(AbstractModel):
    """专线网关云联网路由（IDC网段）对象

    """

    def __init__(self):
        """
        :param RouteId: 路由ID。\n        :type RouteId: str\n        :param DestinationCidrBlock: IDC网段。\n        :type DestinationCidrBlock: str\n        :param ASPath: `BGP`的`AS-Path`属性。\n        :type ASPath: list of str\n        """
        self.RouteId = None
        self.DestinationCidrBlock = None
        self.ASPath = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.ASPath = params.get("ASPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCcnRoutesRequest(AbstractModel):
    """DisableCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。\n        :type RouteIds: list of str\n        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCcnRoutesResponse(AbstractModel):
    """DisableCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisableGatewayFlowMonitorRequest(AbstractModel):
    """DisableGatewayFlowMonitor请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: 网关实例ID，目前我们支持的网关实例类型有，
专线网关实例ID，形如，`dcg-ltjahce6`；
Nat网关实例ID，形如，`nat-ltjahce6`；
VPN网关实例ID，形如，`vpn-ltjahce6`。\n        :type GatewayId: str\n        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableGatewayFlowMonitorResponse(AbstractModel):
    """DisableGatewayFlowMonitor返回参数结构体

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
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param RouteIds: 路由策略ID。不能和RouteItemIds同时使用，但至少输入一个。该参数取值可通过查询路由列表（[DescribeRouteTables](https://cloud.tencent.com/document/product/215/15763)）获取。\n        :type RouteIds: list of int non-negative\n        :param RouteItemIds: 路由策略唯一ID。不能和RouteIds同时使用，但至少输入一个。该参数取值可通过查询路由列表（[DescribeRouteTables](https://cloud.tencent.com/document/product/215/15763)）获取。\n        :type RouteItemIds: list of str\n        """
        self.RouteTableId = None
        self.RouteIds = None
        self.RouteItemIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")
        self.RouteItemIds = params.get("RouteItemIds")
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
        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。\n        :type AddressId: str\n        :param ReallocateNormalPublicIp: 表示解绑 EIP 之后是否分配普通公网 IP。取值范围：<br><li>TRUE：表示解绑 EIP 之后分配普通公网 IP。<br><li>FALSE：表示解绑 EIP 之后不分配普通公网 IP。<br>默认取值：FALSE。<br><br>只有满足以下条件时才能指定该参数：<br><li> 只有在解绑主网卡的主内网 IP 上的 EIP 时才能指定该参数。<br><li>解绑 EIP 后重新分配普通公网 IP 操作一个账号每天最多操作 10 次；详情可通过 [DescribeAddressQuota](https://cloud.tencent.com/document/api/213/1378) 接口获取。\n        :type ReallocateNormalPublicIp: bool\n        """
        self.AddressId = None
        self.ReallocateNormalPublicIp = None


    def _deserialize(self, params):
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
        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisassociateDhcpIpWithAddressIpRequest(AbstractModel):
    """DisassociateDhcpIpWithAddressIp请求参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpId: `DhcpIp`唯一`ID`，形如：`dhcpip-9o233uri`。必须是已绑定`EIP`的`DhcpIp`。\n        :type DhcpIpId: str\n        """
        self.DhcpIpId = None


    def _deserialize(self, params):
        self.DhcpIpId = params.get("DhcpIpId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateDhcpIpWithAddressIpResponse(AbstractModel):
    """DisassociateDhcpIpWithAddressIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateDirectConnectGatewayNatGatewayRequest(AbstractModel):
    """DisassociateDirectConnectGatewayNatGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 专线网关ID。\n        :type VpcId: str\n        :param NatGatewayId: NAT网关ID。\n        :type NatGatewayId: str\n        :param DirectConnectGatewayId: VPC实例ID。可通过DescribeVpcs接口返回值中的VpcId获取。\n        :type DirectConnectGatewayId: str\n        """
        self.VpcId = None
        self.NatGatewayId = None
        self.DirectConnectGatewayId = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateDirectConnectGatewayNatGatewayResponse(AbstractModel):
    """DisassociateDirectConnectGatewayNatGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNatGatewayAddressRequest(AbstractModel):
    """DisassociateNatGatewayAddress请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param PublicIpAddresses: 待解绑NAT网关的弹性IP数组。\n        :type PublicIpAddresses: list of str\n        """
        self.NatGatewayId = None
        self.PublicIpAddresses = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateNatGatewayAddressResponse(AbstractModel):
    """DisassociateNatGatewayAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkAclSubnetsRequest(AbstractModel):
    """DisassociateNetworkAclSubnets请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkAclId: 网络ACL实例ID。例如：acl-12345678。\n        :type NetworkAclId: str\n        :param SubnetIds: 子网实例ID数组。例如：[subnet-12345678]\n        :type SubnetIds: list of str\n        """
        self.NetworkAclId = None
        self.SubnetIds = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.SubnetIds = params.get("SubnetIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateNetworkAclSubnetsResponse(AbstractModel):
    """DisassociateNetworkAclSubnets返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateNetworkInterfaceSecurityGroupsRequest(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 弹性网卡实例ID。形如：eni-pxir56ns。每次请求的实例的上限为100。\n        :type NetworkInterfaceIds: list of str\n        :param SecurityGroupIds: 安全组实例ID，例如：sg-33ocnj9n，可通过DescribeSecurityGroups获取。每次请求的实例的上限为100。\n        :type SecurityGroupIds: list of str\n        """
        self.NetworkInterfaceIds = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateNetworkInterfaceSecurityGroupsResponse(AbstractModel):
    """DisassociateNetworkInterfaceSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DisassociateVpcEndPointSecurityGroupsRequest(AbstractModel):
    """DisassociateVpcEndPointSecurityGroups请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupIds: 安全组ID数组。\n        :type SecurityGroupIds: list of str\n        :param EndPointId: 终端节点ID。\n        :type EndPointId: str\n        """
        self.SecurityGroupIds = None
        self.EndPointId = None


    def _deserialize(self, params):
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        self.EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateVpcEndPointSecurityGroupsResponse(AbstractModel):
    """DisassociateVpcEndPointSecurityGroups返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DownloadCustomerGatewayConfigurationRequest(AbstractModel):
    """DownloadCustomerGatewayConfiguration请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。\n        :type VpnConnectionId: str\n        :param CustomerGatewayVendor: 对端网关厂商信息对象，可通过DescribeCustomerGatewayVendors获取。\n        :type CustomerGatewayVendor: :class:`tencentcloud.vpc.v20170312.models.CustomerGatewayVendor`\n        :param InterfaceName: 通道接入设备物理接口名称。\n        :type InterfaceName: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCustomerGatewayConfigurationResponse(AbstractModel):
    """DownloadCustomerGatewayConfiguration返回参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayConfiguration: XML格式配置信息。\n        :type CustomerGatewayConfiguration: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param RouteIds: CCN路由策略唯一ID。形如：ccnr-f49l6u0z。\n        :type RouteIds: list of str\n        """
        self.CcnId = None
        self.RouteIds = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.RouteIds = params.get("RouteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCcnRoutesResponse(AbstractModel):
    """EnableCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableGatewayFlowMonitorRequest(AbstractModel):
    """EnableGatewayFlowMonitor请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: 网关实例ID，目前我们支持的网关实例有，
专线网关实例ID，形如，`dcg-ltjahce6`；
Nat网关实例ID，形如，`nat-ltjahce6`；
VPN网关实例ID，形如，`vpn-ltjahce6`。\n        :type GatewayId: str\n        """
        self.GatewayId = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableGatewayFlowMonitorResponse(AbstractModel):
    """EnableGatewayFlowMonitor返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableRoutesRequest(AbstractModel):
    """EnableRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param RouteIds: 路由策略ID。不能和RouteItemIds同时使用，但至少输入一个。该参数取值可通过查询路由列表（[DescribeRouteTables](https://cloud.tencent.com/document/product/215/15763)）获取。\n        :type RouteIds: list of int non-negative\n        :param RouteItemIds: 路由策略唯一ID。不能和RouteIds同时使用，但至少输入一个。该参数取值可通过查询路由列表（[DescribeRouteTables](https://cloud.tencent.com/document/product/215/15763)）获取。\n        :type RouteItemIds: list of str\n        """
        self.RouteTableId = None
        self.RouteIds = None
        self.RouteItemIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteIds = params.get("RouteIds")
        self.RouteItemIds = params.get("RouteItemIds")
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


class EnableVpcEndPointConnectRequest(AbstractModel):
    """EnableVpcEndPointConnect请求参数结构体

    """

    def __init__(self):
        """
        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        :param EndPointId: 终端节点ID。\n        :type EndPointId: list of str\n        :param AcceptFlag: 是否接受终端节点连接请求。\n        :type AcceptFlag: bool\n        """
        self.EndPointServiceId = None
        self.EndPointId = None
        self.AcceptFlag = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.EndPointId = params.get("EndPointId")
        self.AcceptFlag = params.get("AcceptFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableVpcEndPointConnectResponse(AbstractModel):
    """EnableVpcEndPointConnect返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EndPoint(AbstractModel):
    """终端节点详情。

    """

    def __init__(self):
        """
        :param EndPointId: 终端节点ID。\n        :type EndPointId: str\n        :param VpcId: VPCID。\n        :type VpcId: str\n        :param SubnetId: 子网ID。\n        :type SubnetId: str\n        :param EndPointOwner: APPID。\n        :type EndPointOwner: str\n        :param EndPointName: 终端节点名称。\n        :type EndPointName: str\n        :param ServiceVpcId: 终端节点服务的VPCID。\n        :type ServiceVpcId: str\n        :param ServiceVip: 终端节点服务的VIP。\n        :type ServiceVip: str\n        :param EndPointServiceId: 终端节点服务的ID。\n        :type EndPointServiceId: str\n        :param EndPointVip: 终端节点的VIP。\n        :type EndPointVip: str\n        :param State: 终端节点状态，ACTIVE：可用，PENDING：待接受，ACCEPTING：接受中，REJECTED：已拒绝，FAILED：失败。\n        :type State: str\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        :param GroupSet: 终端节点绑定的安全组实例ID列表。\n        :type GroupSet: list of str\n        :param ServiceName: 终端节点服务名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceName: str\n        """
        self.EndPointId = None
        self.VpcId = None
        self.SubnetId = None
        self.EndPointOwner = None
        self.EndPointName = None
        self.ServiceVpcId = None
        self.ServiceVip = None
        self.EndPointServiceId = None
        self.EndPointVip = None
        self.State = None
        self.CreateTime = None
        self.GroupSet = None
        self.ServiceName = None


    def _deserialize(self, params):
        self.EndPointId = params.get("EndPointId")
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.EndPointOwner = params.get("EndPointOwner")
        self.EndPointName = params.get("EndPointName")
        self.ServiceVpcId = params.get("ServiceVpcId")
        self.ServiceVip = params.get("ServiceVip")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.EndPointVip = params.get("EndPointVip")
        self.State = params.get("State")
        self.CreateTime = params.get("CreateTime")
        self.GroupSet = params.get("GroupSet")
        self.ServiceName = params.get("ServiceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EndPointService(AbstractModel):
    """终端节点服务对象。

    """

    def __init__(self):
        """
        :param EndPointServiceId: 终端节点服务ID\n        :type EndPointServiceId: str\n        :param VpcId: VPCID。\n        :type VpcId: str\n        :param ServiceOwner: APPID。\n        :type ServiceOwner: str\n        :param ServiceName: 终端节点服务名称。\n        :type ServiceName: str\n        :param ServiceVip: 后端服务的VIP。\n        :type ServiceVip: str\n        :param ServiceInstanceId: 后端服务的ID，比如lb-xxx。\n        :type ServiceInstanceId: str\n        :param AutoAcceptFlag: 是否自动接受。\n        :type AutoAcceptFlag: bool\n        :param EndPointCount: 关联的终端节点个数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndPointCount: int\n        :param EndPointSet: 终端节点对象数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type EndPointSet: list of EndPoint\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        """
        self.EndPointServiceId = None
        self.VpcId = None
        self.ServiceOwner = None
        self.ServiceName = None
        self.ServiceVip = None
        self.ServiceInstanceId = None
        self.AutoAcceptFlag = None
        self.EndPointCount = None
        self.EndPointSet = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.VpcId = params.get("VpcId")
        self.ServiceOwner = params.get("ServiceOwner")
        self.ServiceName = params.get("ServiceName")
        self.ServiceVip = params.get("ServiceVip")
        self.ServiceInstanceId = params.get("ServiceInstanceId")
        self.AutoAcceptFlag = params.get("AutoAcceptFlag")
        self.EndPointCount = params.get("EndPointCount")
        if params.get("EndPointSet") is not None:
            self.EndPointSet = []
            for item in params.get("EndPointSet"):
                obj = EndPoint()
                obj._deserialize(item)
                self.EndPointSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤器

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。\n        :type Name: str\n        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterObject(AbstractModel):
    """过滤器键值对

    """

    def __init__(self):
        """
        :param Name: 属性名称, 若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。\n        :type Name: str\n        :param Values: 属性值, 若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。\n        :type Values: list of str\n        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowLog(AbstractModel):
    """流日志

    """

    def __init__(self):
        """
        :param VpcId: 私用网络ID或者统一ID，建议使用统一ID\n        :type VpcId: str\n        :param FlowLogId: 流日志唯一ID\n        :type FlowLogId: str\n        :param FlowLogName: 流日志实例名字\n        :type FlowLogName: str\n        :param ResourceType: 流日志所属资源类型，VPC|SUBNET|NETWORKINTERFACE\n        :type ResourceType: str\n        :param ResourceId: 资源唯一ID\n        :type ResourceId: str\n        :param TrafficType: 流日志采集类型，ACCEPT|REJECT|ALL\n        :type TrafficType: str\n        :param CloudLogId: 流日志存储ID\n        :type CloudLogId: str\n        :param CloudLogState: 流日志存储ID状态\n        :type CloudLogState: str\n        :param FlowLogDescription: 流日志描述信息\n        :type FlowLogDescription: str\n        :param CreatedTime: 流日志创建时间\n        :type CreatedTime: str\n        :param TagSet: 标签列表，例如：[{"Key": "city", "Value": "shanghai"}]\n        :type TagSet: list of Tag\n        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.ResourceType = None
        self.ResourceId = None
        self.TrafficType = None
        self.CloudLogId = None
        self.CloudLogState = None
        self.FlowLogDescription = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.TrafficType = params.get("TrafficType")
        self.CloudLogId = params.get("CloudLogId")
        self.CloudLogState = params.get("CloudLogState")
        self.FlowLogDescription = params.get("FlowLogDescription")
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
        


class GatewayFlowMonitorDetail(AbstractModel):
    """网关流量监控明细

    """

    def __init__(self):
        """
        :param PrivateIpAddress: 来源`IP`。\n        :type PrivateIpAddress: str\n        :param InPkg: 入包量。\n        :type InPkg: int\n        :param OutPkg: 出包量。\n        :type OutPkg: int\n        :param InTraffic: 入流量，单位：`Byte`。\n        :type InTraffic: int\n        :param OutTraffic: 出流量，单位：`Byte`。\n        :type OutTraffic: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GatewayQos(AbstractModel):
    """网关流控带宽信息

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param IpAddress: 云服务器内网IP。\n        :type IpAddress: str\n        :param Bandwidth: 流控带宽值。\n        :type Bandwidth: int\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        """
        self.VpcId = None
        self.IpAddress = None
        self.Bandwidth = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.IpAddress = params.get("IpAddress")
        self.Bandwidth = params.get("Bandwidth")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """GetCcnRegionBandwidthLimits请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param Filters: 过滤条件。
<li>sregion - String - （过滤条件）源地域，形如：ap-guangzhou。</li>
<li>dregion - String - （过滤条件）目的地域，形如：ap-shanghai-bm</li>\n        :type Filters: list of Filter\n        :param SortedBy: 排序条件，目前支持带宽（BandwidthLimit）和过期时间（ExpireTime）\n        :type SortedBy: str\n        :param Offset: 偏移量\n        :type Offset: int\n        :param Limit: 返回数量\n        :type Limit: int\n        :param OrderBy: 排序方式，'ASC':升序,'DESC':降序。\n        :type OrderBy: str\n        """
        self.CcnId = None
        self.Filters = None
        self.SortedBy = None
        self.Offset = None
        self.Limit = None
        self.OrderBy = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.SortedBy = params.get("SortedBy")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.OrderBy = params.get("OrderBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """GetCcnRegionBandwidthLimits返回参数结构体

    """

    def __init__(self):
        """
        :param CcnBandwidthSet: 云联网（CCN）各地域出带宽带宽详情。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CcnBandwidthSet: list of CcnBandwidthInfo\n        :param TotalCount: 符合条件的对象数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CcnBandwidthSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CcnBandwidthSet") is not None:
            self.CcnBandwidthSet = []
            for item in params.get("CcnBandwidthSet"):
                obj = CcnBandwidthInfo()
                obj._deserialize(item)
                self.CcnBandwidthSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class HaVip(AbstractModel):
    """描述 HAVIP 信息

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`的`ID`，是`HAVIP`的唯一标识。\n        :type HaVipId: str\n        :param HaVipName: `HAVIP`名称。\n        :type HaVipName: str\n        :param Vip: 虚拟IP地址。\n        :type Vip: str\n        :param VpcId: `HAVIP`所在私有网络`ID`。\n        :type VpcId: str\n        :param SubnetId: `HAVIP`所在子网`ID`。\n        :type SubnetId: str\n        :param NetworkInterfaceId: `HAVIP`关联弹性网卡`ID`。\n        :type NetworkInterfaceId: str\n        :param InstanceId: 被绑定的实例`ID`。\n        :type InstanceId: str\n        :param AddressIp: 绑定`EIP`。\n        :type AddressIp: str\n        :param State: 状态：
<li>`AVAILABLE`：运行中</li>
<li>`UNBIND`：未绑定</li>\n        :type State: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param Business: 使用havip的业务标识。\n        :type Business: str\n        """
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
        


class HaVipAssociateAddressIpRequest(AbstractModel):
    """HaVipAssociateAddressIp请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。必须是没有绑定`EIP`的`HAVIP`\n        :type HaVipId: str\n        :param AddressIp: 弹性公网`IP`。必须是没有绑定`HAVIP`的`EIP`\n        :type AddressIp: str\n        """
        self.HaVipId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        self.AddressIp = params.get("AddressIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVipAssociateAddressIpResponse(AbstractModel):
    """HaVipAssociateAddressIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class HaVipDisassociateAddressIpRequest(AbstractModel):
    """HaVipDisassociateAddressIp请求参数结构体

    """

    def __init__(self):
        """
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。必须是已绑定`EIP`的`HAVIP`。\n        :type HaVipId: str\n        """
        self.HaVipId = None


    def _deserialize(self, params):
        self.HaVipId = params.get("HaVipId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HaVipDisassociateAddressIpResponse(AbstractModel):
    """HaVipDisassociateAddressIp返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class IKEOptionsSpecification(AbstractModel):
    """IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议

    """

    def __init__(self):
        """
        :param PropoEncryAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBS-192', 'AES-CBC-256', 'DES-CBC'，'SM4', 默认为3DES-CBC\n        :type PropoEncryAlgorithm: str\n        :param PropoAuthenAlgorithm: 认证算法：可选值：'MD5', 'SHA1'，'SHA-256' 默认为MD5\n        :type PropoAuthenAlgorithm: str\n        :param ExchangeMode: 协商模式：可选值：'AGGRESSIVE', 'MAIN'，默认为MAIN\n        :type ExchangeMode: str\n        :param LocalIdentity: 本端标识类型：可选值：'ADDRESS', 'FQDN'，默认为ADDRESS\n        :type LocalIdentity: str\n        :param RemoteIdentity: 对端标识类型：可选值：'ADDRESS', 'FQDN'，默认为ADDRESS\n        :type RemoteIdentity: str\n        :param LocalAddress: 本端标识，当LocalIdentity选为ADDRESS时，LocalAddress必填。localAddress默认为vpn网关公网IP\n        :type LocalAddress: str\n        :param RemoteAddress: 对端标识，当RemoteIdentity选为ADDRESS时，RemoteAddress必填\n        :type RemoteAddress: str\n        :param LocalFqdnName: 本端标识，当LocalIdentity选为FQDN时，LocalFqdnName必填\n        :type LocalFqdnName: str\n        :param RemoteFqdnName: 对端标识，当remoteIdentity选为FQDN时，RemoteFqdnName必填\n        :type RemoteFqdnName: str\n        :param DhGroupName: DH group，指定IKE交换密钥时使用的DH组，可选值：'GROUP1', 'GROUP2', 'GROUP5', 'GROUP14', 'GROUP24'，\n        :type DhGroupName: str\n        :param IKESaLifetimeSeconds: IKE SA Lifetime，单位：秒，设置IKE SA的生存周期，取值范围：60-604800\n        :type IKESaLifetimeSeconds: int\n        :param IKEVersion: IKE版本\n        :type IKEVersion: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPSECOptionsSpecification(AbstractModel):
    """IPSec配置，腾讯云提供IPSec安全会话设置

    """

    def __init__(self):
        """
        :param EncryptAlgorithm: 加密算法，可选值：'3DES-CBC', 'AES-CBC-128', 'AES-CBC-192', 'AES-CBC-256', 'DES-CBC', 'SM4', 'NULL'， 默认为AES-CBC-128\n        :type EncryptAlgorithm: str\n        :param IntegrityAlgorith: 认证算法：可选值：'MD5', 'SHA1'，'SHA-256' 默认为\n        :type IntegrityAlgorith: str\n        :param IPSECSaLifetimeSeconds: IPsec SA lifetime(s)：单位秒，取值范围：180-604800\n        :type IPSECSaLifetimeSeconds: int\n        :param PfsDhGroup: PFS：可选值：'NULL', 'DH-GROUP1', 'DH-GROUP2', 'DH-GROUP5', 'DH-GROUP14', 'DH-GROUP24'，默认为NULL\n        :type PfsDhGroup: str\n        :param IPSECSaLifetimeTraffic: IPsec SA lifetime(KB)：单位KB，取值范围：2560-604800\n        :type IPSECSaLifetimeTraffic: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquirePriceCreateDirectConnectGatewayRequest(AbstractModel):
    """InquirePriceCreateDirectConnectGateway请求参数结构体

    """


class InquirePriceCreateDirectConnectGatewayResponse(AbstractModel):
    """InquirePriceCreateDirectConnectGateway返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCost: 专线网关标准接入费用
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCost: int\n        :param RealTotalCost: 专线网关真实接入费用
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealTotalCost: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TotalCost = None
        self.RealTotalCost = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCost = params.get("TotalCost")
        self.RealTotalCost = params.get("RealTotalCost")
        self.RequestId = params.get("RequestId")


class InquiryPriceCreateVpnGatewayRequest(AbstractModel):
    """InquiryPriceCreateVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。\n        :type InternetMaxBandwidthOut: int\n        :param InstanceChargeType: VPN网关计费模式，PREPAID：表示预付费，即包年包月，POSTPAID_BY_HOUR：表示后付费，即按量计费。默认：POSTPAID_BY_HOUR，如果指定预付费模式，参数InstanceChargePrepaid必填。\n        :type InstanceChargeType: str\n        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        """
        self.InternetMaxBandwidthOut = None
        self.InstanceChargeType = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.InstanceChargeType = params.get("InstanceChargeType")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateVpnGatewayResponse(AbstractModel):
    """InquiryPriceCreateVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 商品价格。\n        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param InstanceChargePrepaid: 预付费模式，即包年包月相关参数设置。通过该参数可以指定包年包月实例的购买时长、是否设置自动续费等属性。若指定实例的付费模式为预付费则该参数必传。\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceRenewVpnGatewayResponse(AbstractModel):
    """InquiryPriceRenewVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 商品价格。\n        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。\n        :type InternetMaxBandwidthOut: int\n        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """InquiryPriceResetVpnGatewayInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param Price: 商品价格。\n        :type Price: :class:`tencentcloud.vpc.v20170312.models.Price`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Period: 购买实例的时长，单位：月。取值范围：1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36。\n        :type Period: int\n        :param RenewFlag: 自动续费标识。取值范围： NOTIFY_AND_AUTO_RENEW：通知过期且自动续费， NOTIFY_AND_MANUAL_RENEW：通知过期不自动续费。默认：NOTIFY_AND_MANUAL_RENEW\n        :type RenewFlag: str\n        """
        self.Period = None
        self.RenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RenewFlag = params.get("RenewFlag")
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
        


class Ip6Rule(AbstractModel):
    """IPV6转换规则

    """

    def __init__(self):
        """
        :param Ip6RuleId: IPV6转换规则唯一ID，形如rule6-xxxxxxxx\n        :type Ip6RuleId: str\n        :param Ip6RuleName: IPV6转换规则名称\n        :type Ip6RuleName: str\n        :param Vip6: IPV6地址\n        :type Vip6: str\n        :param Vport6: IPV6端口号\n        :type Vport6: int\n        :param Protocol: 协议类型，支持TCP/UDP\n        :type Protocol: str\n        :param Vip: IPV4地址\n        :type Vip: str\n        :param Vport: IPV4端口号\n        :type Vport: int\n        :param RuleStatus: 转换规则状态，限于CREATING,RUNNING,DELETING,MODIFYING\n        :type RuleStatus: str\n        :param CreatedTime: 转换规则创建时间\n        :type CreatedTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ip6RuleInfo(AbstractModel):
    """IPV6转换规则

    """

    def __init__(self):
        """
        :param Vport6: IPV6端口号，可在0~65535范围取值\n        :type Vport6: int\n        :param Protocol: 协议类型，支持TCP/UDP\n        :type Protocol: str\n        :param Vip: IPV4地址\n        :type Vip: str\n        :param Vport: IPV4端口号，可在0~65535范围取值\n        :type Vport: int\n        """
        self.Vport6 = None
        self.Protocol = None
        self.Vip = None
        self.Vport = None


    def _deserialize(self, params):
        self.Vport6 = params.get("Vport6")
        self.Protocol = params.get("Protocol")
        self.Vip = params.get("Vip")
        self.Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ip6Translator(AbstractModel):
    """IPV6转换实例信息

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxx\n        :type Ip6TranslatorId: str\n        :param Ip6TranslatorName: IPV6转换实例名称\n        :type Ip6TranslatorName: str\n        :param Vip6: IPV6地址\n        :type Vip6: str\n        :param IspName: IPV6转换地址所属运营商\n        :type IspName: str\n        :param TranslatorStatus: 转换实例状态，限于CREATING,RUNNING,DELETING,MODIFYING\n        :type TranslatorStatus: str\n        :param CreatedTime: IPV6转换实例创建时间\n        :type CreatedTime: str\n        :param Ip6RuleCount: 绑定的IPV6转换规则数量\n        :type Ip6RuleCount: int\n        :param IP6RuleSet: IPV6转换规则信息\n        :type IP6RuleSet: list of Ip6Rule\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpField(AbstractModel):
    """IP在线查询的字段信息

    """

    def __init__(self):
        """
        :param Country: 国家字段信息\n        :type Country: bool\n        :param Province: 省、州、郡一级行政区域字段信息\n        :type Province: bool\n        :param City: 市一级行政区域字段信息\n        :type City: bool\n        :param Region: 市内区域字段信息\n        :type Region: bool\n        :param Isp: 接入运营商字段信息\n        :type Isp: bool\n        :param AsName: 骨干运营商字段信息\n        :type AsName: bool\n        :param AsId: 骨干As号\n        :type AsId: bool\n        :param Comment: 注释字段\n        :type Comment: bool\n        """
        self.Country = None
        self.Province = None
        self.City = None
        self.Region = None
        self.Isp = None
        self.AsName = None
        self.AsId = None
        self.Comment = None


    def _deserialize(self, params):
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Region = params.get("Region")
        self.Isp = params.get("Isp")
        self.AsName = params.get("AsName")
        self.AsId = params.get("AsId")
        self.Comment = params.get("Comment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpGeolocationInfo(AbstractModel):
    """IP地理位置信息

    """

    def __init__(self):
        """
        :param Country: 国家信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Country: str\n        :param Province: 省、州、郡一级行政区域信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Province: str\n        :param City: 市一级行政区域信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        :param Region: 市内区域信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Region: str\n        :param Isp: 接入运营商信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Isp: str\n        :param AsName: 骨干运营商名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type AsName: str\n        :param AsId: 骨干运营商AS号
注意：此字段可能返回 null，表示取不到有效值。\n        :type AsId: str\n        :param Comment: 注释信息。目前的填充值为移动接入用户的APN值，如无APN属性则为空
注意：此字段可能返回 null，表示取不到有效值。\n        :type Comment: str\n        :param AddressIp: IP地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type AddressIp: str\n        """
        self.Country = None
        self.Province = None
        self.City = None
        self.Region = None
        self.Isp = None
        self.AsName = None
        self.AsId = None
        self.Comment = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.Country = params.get("Country")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Region = params.get("Region")
        self.Isp = params.get("Isp")
        self.AsName = params.get("AsName")
        self.AsId = params.get("AsId")
        self.Comment = params.get("Comment")
        self.AddressIp = params.get("AddressIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Address(AbstractModel):
    """`IPv6`地址信息。

    """

    def __init__(self):
        """
        :param Address: `IPv6`地址，形如：`3402:4e00:20:100:0:8cd9:2a67:71f3`\n        :type Address: str\n        :param Primary: 是否是主`IP`。\n        :type Primary: bool\n        :param AddressId: `EIP`实例`ID`，形如：`eip-hxlqja90`。\n        :type AddressId: str\n        :param Description: 描述信息。\n        :type Description: str\n        :param IsWanIpBlocked: 公网IP是否被封堵。\n        :type IsWanIpBlocked: bool\n        :param State: `IPv6`地址状态：
<li>`PENDING`：生产中</li>
<li>`MIGRATING`：迁移中</li>
<li>`DELETING`：删除中</li>
<li>`AVAILABLE`：可用的</li>\n        :type State: str\n        """
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
        


class Ipv6SubnetCidrBlock(AbstractModel):
    """IPv6子网段对象。

    """

    def __init__(self):
        """
        :param SubnetId: 子网实例`ID`。形如：`subnet-pxir56ns`。\n        :type SubnetId: str\n        :param Ipv6CidrBlock: `IPv6`子网段。形如：`3402:4e00:20:1001::/64`\n        :type Ipv6CidrBlock: str\n        """
        self.SubnetId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ItemPrice(AbstractModel):
    """单项计费价格信息

    """

    def __init__(self):
        """
        :param UnitPrice: 按量计费后付费单价，单位：元。\n        :type UnitPrice: float\n        :param ChargeUnit: 按量计费后付费计价单元，可取值范围： HOUR：表示计价单元是按每小时来计算。当前涉及该计价单元的场景有：实例按小时后付费（POSTPAID_BY_HOUR）、带宽按小时后付费（BANDWIDTH_POSTPAID_BY_HOUR）： GB：表示计价单元是按每GB来计算。当前涉及该计价单元的场景有：流量按小时后付费（TRAFFIC_POSTPAID_BY_HOUR）。\n        :type ChargeUnit: str\n        :param OriginalPrice: 预付费商品的原价，单位：元。\n        :type OriginalPrice: float\n        :param DiscountPrice: 预付费商品的折扣价，单位：元。\n        :type DiscountPrice: float\n        """
        self.UnitPrice = None
        self.ChargeUnit = None
        self.OriginalPrice = None
        self.DiscountPrice = None


    def _deserialize(self, params):
        self.UnitPrice = params.get("UnitPrice")
        self.ChargeUnit = params.get("ChargeUnit")
        self.OriginalPrice = params.get("OriginalPrice")
        self.DiscountPrice = params.get("DiscountPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LocalGateway(AbstractModel):
    """本地网关信息

    """

    def __init__(self):
        """
        :param CdcId: CDC实例ID\n        :type CdcId: str\n        :param VpcId: VPC实例ID\n        :type VpcId: str\n        :param UniqLocalGwId: 本地网关实例ID\n        :type UniqLocalGwId: str\n        :param LocalGatewayName: 本地网关名称\n        :type LocalGatewayName: str\n        :param LocalGwIp: 本地网关IP地址\n        :type LocalGwIp: str\n        :param CreateTime: 本地网关创建时间\n        :type CreateTime: str\n        """
        self.CdcId = None
        self.VpcId = None
        self.UniqLocalGwId = None
        self.LocalGatewayName = None
        self.LocalGwIp = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.CdcId = params.get("CdcId")
        self.VpcId = params.get("VpcId")
        self.UniqLocalGwId = params.get("UniqLocalGwId")
        self.LocalGatewayName = params.get("LocalGatewayName")
        self.LocalGwIp = params.get("LocalGwIp")
        self.CreateTime = params.get("CreateTime")
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
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param SourceInstanceId: 弹性网卡当前绑定的CVM实例ID。形如：ins-r8hr2upy。\n        :type SourceInstanceId: str\n        :param DestinationInstanceId: 待迁移的目的CVM实例ID。\n        :type DestinationInstanceId: str\n        :param AttachType: 网卡绑定类型：0 标准型 1 扩展型。\n        :type AttachType: int\n        """
        self.NetworkInterfaceId = None
        self.SourceInstanceId = None
        self.DestinationInstanceId = None
        self.AttachType = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.SourceInstanceId = params.get("SourceInstanceId")
        self.DestinationInstanceId = params.get("DestinationInstanceId")
        self.AttachType = params.get("AttachType")
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
        :param SourceNetworkInterfaceId: 当内网IP绑定的弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type SourceNetworkInterfaceId: str\n        :param DestinationNetworkInterfaceId: 待迁移的目的弹性网卡实例ID。\n        :type DestinationNetworkInterfaceId: str\n        :param PrivateIpAddress: 迁移的内网IP地址，例如：10.0.0.6。\n        :type PrivateIpAddress: str\n        """
        self.SourceNetworkInterfaceId = None
        self.DestinationNetworkInterfaceId = None
        self.PrivateIpAddress = None


    def _deserialize(self, params):
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
        :param AddressId: 标识 EIP 的唯一 ID。EIP 唯一 ID 形如：`eip-11112222`。\n        :type AddressId: str\n        :param AddressName: 修改后的 EIP 名称。长度上限为20个字符。\n        :type AddressName: str\n        :param EipDirectConnection: 设定EIP是否直通，"TRUE"表示直通，"FALSE"表示非直通。注意该参数仅对EIP直通功能可见的用户可以设定。\n        :type EipDirectConnection: str\n        """
        self.AddressId = None
        self.AddressName = None
        self.EipDirectConnection = None


    def _deserialize(self, params):
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


class ModifyAddressInternetChargeTypeRequest(AbstractModel):
    """ModifyAddressInternetChargeType请求参数结构体

    """

    def __init__(self):
        """
        :param AddressId: 弹性公网IP的唯一ID，形如eip-xxx\n        :type AddressId: str\n        :param InternetChargeType: 弹性公网IP调整目标计费模式，只支持"BANDWIDTH_PREPAID_BY_MONTH"和"TRAFFIC_POSTPAID_BY_HOUR"\n        :type InternetChargeType: str\n        :param InternetMaxBandwidthOut: 弹性公网IP调整目标带宽值\n        :type InternetMaxBandwidthOut: int\n        :param AddressChargePrepaid: 包月带宽网络计费模式参数。弹性公网IP的调整目标计费模式是"BANDWIDTH_PREPAID_BY_MONTH"时，必传该参数。\n        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`\n        """
        self.AddressId = None
        self.InternetChargeType = None
        self.InternetMaxBandwidthOut = None
        self.AddressChargePrepaid = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.InternetChargeType = params.get("InternetChargeType")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        if params.get("AddressChargePrepaid") is not None:
            self.AddressChargePrepaid = AddressChargePrepaid()
            self.AddressChargePrepaid._deserialize(params.get("AddressChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressInternetChargeTypeResponse(AbstractModel):
    """ModifyAddressInternetChargeType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateAttributeRequest(AbstractModel):
    """ModifyAddressTemplateAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateId: IP地址模板实例ID，例如：ipm-mdunqeb6。\n        :type AddressTemplateId: str\n        :param AddressTemplateName: IP地址模板名称。\n        :type AddressTemplateName: str\n        :param Addresses: 地址信息，支持 IP、CIDR、IP 范围。\n        :type Addresses: list of str\n        """
        self.AddressTemplateId = None
        self.AddressTemplateName = None
        self.Addresses = None


    def _deserialize(self, params):
        self.AddressTemplateId = params.get("AddressTemplateId")
        self.AddressTemplateName = params.get("AddressTemplateName")
        self.Addresses = params.get("Addresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressTemplateAttributeResponse(AbstractModel):
    """ModifyAddressTemplateAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyAddressTemplateGroupAttributeRequest(AbstractModel):
    """ModifyAddressTemplateGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param AddressTemplateGroupId: IP地址模板集合实例ID，例如：ipmg-2uw6ujo6。\n        :type AddressTemplateGroupId: str\n        :param AddressTemplateGroupName: IP地址模板集合名称。\n        :type AddressTemplateGroupName: str\n        :param AddressTemplateIds: IP地址模板实例ID， 例如：ipm-mdunqeb6。\n        :type AddressTemplateIds: list of str\n        """
        self.AddressTemplateGroupId = None
        self.AddressTemplateGroupName = None
        self.AddressTemplateIds = None


    def _deserialize(self, params):
        self.AddressTemplateGroupId = params.get("AddressTemplateGroupId")
        self.AddressTemplateGroupName = params.get("AddressTemplateGroupName")
        self.AddressTemplateIds = params.get("AddressTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAddressTemplateGroupAttributeResponse(AbstractModel):
    """ModifyAddressTemplateGroupAttribute返回参数结构体

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
        :param AddressIds: EIP唯一标识ID列表，形如'eip-xxxx'\n        :type AddressIds: list of str\n        :param InternetMaxBandwidthOut: 调整带宽目标值\n        :type InternetMaxBandwidthOut: int\n        :param StartTime: 包月带宽起始时间(已废弃，输入无效)\n        :type StartTime: str\n        :param EndTime: 包月带宽结束时间(已废弃，输入无效)\n        :type EndTime: str\n        """
        self.AddressIds = None
        self.InternetMaxBandwidthOut = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
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
        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ModifyAssistantCidrRequest(AbstractModel):
    """ModifyAssistantCidr请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-6v2ht8q5`\n        :type VpcId: str\n        :param NewCidrBlocks: 待添加的辅助CIDR。CIDR数组，格式如["10.0.0.0/16", "172.16.0.0/16"]，入参NewCidrBlocks和OldCidrBlocks至少需要其一。\n        :type NewCidrBlocks: list of str\n        :param OldCidrBlocks: 待删除的辅助CIDR。CIDR数组，格式如["10.0.0.0/16", "172.16.0.0/16"]，入参NewCidrBlocks和OldCidrBlocks至少需要其一。\n        :type OldCidrBlocks: list of str\n        """
        self.VpcId = None
        self.NewCidrBlocks = None
        self.OldCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NewCidrBlocks = params.get("NewCidrBlocks")
        self.OldCidrBlocks = params.get("OldCidrBlocks")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyAssistantCidrResponse(AbstractModel):
    """ModifyAssistantCidr返回参数结构体

    """

    def __init__(self):
        """
        :param AssistantCidrSet: 辅助CIDR数组。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssistantCidrSet: list of AssistantCidr\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AssistantCidrSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AssistantCidrSet") is not None:
            self.AssistantCidrSet = []
            for item in params.get("AssistantCidrSet"):
                obj = AssistantCidr()
                obj._deserialize(item)
                self.AssistantCidrSet.append(obj)
        self.RequestId = params.get("RequestId")


class ModifyBandwidthPackageAttributeRequest(AbstractModel):
    """ModifyBandwidthPackageAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一标识ID\n        :type BandwidthPackageId: str\n        :param BandwidthPackageName: 带宽包名称\n        :type BandwidthPackageName: str\n        :param ChargeType: 带宽包计费模式\n        :type ChargeType: str\n        """
        self.BandwidthPackageId = None
        self.BandwidthPackageName = None
        self.ChargeType = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.BandwidthPackageName = params.get("BandwidthPackageName")
        self.ChargeType = params.get("ChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyBandwidthPackageAttributeResponse(AbstractModel):
    """ModifyBandwidthPackageAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttachedInstancesAttributeRequest(AbstractModel):
    """ModifyCcnAttachedInstancesAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param Instances: 关联网络实例列表\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcnAttachedInstancesAttributeResponse(AbstractModel):
    """ModifyCcnAttachedInstancesAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnAttributeRequest(AbstractModel):
    """ModifyCcnAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param CcnName: CCN名称，最大长度不能超过60个字节。\n        :type CcnName: str\n        :param CcnDescription: CCN描述信息，最大长度不能超过100个字节。\n        :type CcnDescription: str\n        """
        self.CcnId = None
        self.CcnName = None
        self.CcnDescription = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.CcnName = params.get("CcnName")
        self.CcnDescription = params.get("CcnDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcnAttributeResponse(AbstractModel):
    """ModifyCcnAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcnRegionBandwidthLimitsTypeRequest(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: 云联网实例ID。\n        :type CcnId: str\n        :param BandwidthLimitType: 云联网限速类型，INTER_REGION_LIMIT：地域间限速，OUTER_REGION_LIMIT：地域出口限速。\n        :type BandwidthLimitType: str\n        """
        self.CcnId = None
        self.BandwidthLimitType = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        self.BandwidthLimitType = params.get("BandwidthLimitType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcnRegionBandwidthLimitsTypeResponse(AbstractModel):
    """ModifyCcnRegionBandwidthLimitsType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCustomerGatewayAttributeRequest(AbstractModel):
    """ModifyCustomerGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param CustomerGatewayId: 对端网关ID，例如：cgw-2wqq41m9，可通过DescribeCustomerGateways接口查询对端网关。\n        :type CustomerGatewayId: str\n        :param CustomerGatewayName: 对端网关名称，可任意命名，但不得超过60个字符。\n        :type CustomerGatewayName: str\n        """
        self.CustomerGatewayId = None
        self.CustomerGatewayName = None


    def _deserialize(self, params):
        self.CustomerGatewayId = params.get("CustomerGatewayId")
        self.CustomerGatewayName = params.get("CustomerGatewayName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCustomerGatewayAttributeResponse(AbstractModel):
    """ModifyCustomerGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDhcpIpAttributeRequest(AbstractModel):
    """ModifyDhcpIpAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DhcpIpId: `DhcpIp`唯一`ID`，形如：`dhcpip-9o233uri`。\n        :type DhcpIpId: str\n        :param DhcpIpName: `DhcpIp`名称，可任意命名，但不得超过60个字符。\n        :type DhcpIpName: str\n        """
        self.DhcpIpId = None
        self.DhcpIpName = None


    def _deserialize(self, params):
        self.DhcpIpId = params.get("DhcpIpId")
        self.DhcpIpName = params.get("DhcpIpName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDhcpIpAttributeResponse(AbstractModel):
    """ModifyDhcpIpAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDirectConnectGatewayAttributeRequest(AbstractModel):
    """ModifyDirectConnectGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关唯一`ID`，形如：`dcg-9o233uri`。\n        :type DirectConnectGatewayId: str\n        :param DirectConnectGatewayName: 专线网关名称，可任意命名，但不得超过60个字符。\n        :type DirectConnectGatewayName: str\n        :param CcnRouteType: 云联网路由学习类型，可选值：`BGP`（自动学习）、`STATIC`（静态，即用户配置）。只有云联网类型专线网关且开启了BGP功能才支持修改`CcnRouteType`。\n        :type CcnRouteType: str\n        :param ModeType: 云联网路由发布模式，可选值：`standard`（标准模式）、`exquisite`（精细模式）。只有云联网类型专线网关才支持修改`ModeType`。\n        :type ModeType: str\n        """
        self.DirectConnectGatewayId = None
        self.DirectConnectGatewayName = None
        self.CcnRouteType = None
        self.ModeType = None


    def _deserialize(self, params):
        self.DirectConnectGatewayId = params.get("DirectConnectGatewayId")
        self.DirectConnectGatewayName = params.get("DirectConnectGatewayName")
        self.CcnRouteType = params.get("CcnRouteType")
        self.ModeType = params.get("ModeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDirectConnectGatewayAttributeResponse(AbstractModel):
    """ModifyDirectConnectGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyFlowLogAttributeRequest(AbstractModel):
    """ModifyFlowLogAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 私用网络ID或者统一ID，建议使用统一ID\n        :type VpcId: str\n        :param FlowLogId: 流日志唯一ID\n        :type FlowLogId: str\n        :param FlowLogName: 流日志实例名字\n        :type FlowLogName: str\n        :param FlowLogDescription: 流日志实例描述\n        :type FlowLogDescription: str\n        """
        self.VpcId = None
        self.FlowLogId = None
        self.FlowLogName = None
        self.FlowLogDescription = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.FlowLogId = params.get("FlowLogId")
        self.FlowLogName = params.get("FlowLogName")
        self.FlowLogDescription = params.get("FlowLogDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyFlowLogAttributeResponse(AbstractModel):
    """ModifyFlowLogAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyGatewayFlowQosRequest(AbstractModel):
    """ModifyGatewayFlowQos请求参数结构体

    """

    def __init__(self):
        """
        :param GatewayId: 网关实例ID，目前我们支持的网关实例类型有，
专线网关实例ID，形如，`dcg-ltjahce6`；
Nat网关实例ID，形如，`nat-ltjahce6`；
VPN网关实例ID，形如，`vpn-ltjahce6`。\n        :type GatewayId: str\n        :param Bandwidth: 流控带宽值。取值大于0，表示限流到指定的Mbps；取值等于0，表示完全限流；取值为-1，不限流。\n        :type Bandwidth: int\n        :param IpAddresses: 限流的云服务器内网IP。\n        :type IpAddresses: list of str\n        """
        self.GatewayId = None
        self.Bandwidth = None
        self.IpAddresses = None


    def _deserialize(self, params):
        self.GatewayId = params.get("GatewayId")
        self.Bandwidth = params.get("Bandwidth")
        self.IpAddresses = params.get("IpAddresses")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGatewayFlowQosResponse(AbstractModel):
    """ModifyGatewayFlowQos返回参数结构体

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
        :param HaVipId: `HAVIP`唯一`ID`，形如：`havip-9o233uri`。\n        :type HaVipId: str\n        :param HaVipName: `HAVIP`名称，可任意命名，但不得超过60个字符。\n        :type HaVipName: str\n        """
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


class ModifyIp6AddressesBandwidthRequest(AbstractModel):
    """ModifyIp6AddressesBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param InternetMaxBandwidthOut: 修改的目标带宽，单位Mbps\n        :type InternetMaxBandwidthOut: int\n        :param Ip6Addresses: IPV6地址。Ip6Addresses和Ip6AddressId必须且只能传一个\n        :type Ip6Addresses: list of str\n        :param Ip6AddressIds: IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ip6Addresses和Ip6AddressId必须且只能传一个\n        :type Ip6AddressIds: list of str\n        """
        self.InternetMaxBandwidthOut = None
        self.Ip6Addresses = None
        self.Ip6AddressIds = None


    def _deserialize(self, params):
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.Ip6Addresses = params.get("Ip6Addresses")
        self.Ip6AddressIds = params.get("Ip6AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIp6AddressesBandwidthResponse(AbstractModel):
    """ModifyIp6AddressesBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6RuleRequest(AbstractModel):
    """ModifyIp6Rule请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxx\n        :type Ip6TranslatorId: str\n        :param Ip6RuleId: IPV6转换规则唯一ID，形如rule6-xxxxxxxx\n        :type Ip6RuleId: str\n        :param Ip6RuleName: IPV6转换规则修改后的名称\n        :type Ip6RuleName: str\n        :param Vip: IPV6转换规则修改后的IPV4地址\n        :type Vip: str\n        :param Vport: IPV6转换规则修改后的IPV4端口号\n        :type Vport: int\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIp6RuleResponse(AbstractModel):
    """ModifyIp6Rule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyIp6TranslatorRequest(AbstractModel):
    """ModifyIp6Translator请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换实例唯一ID，形如ip6-xxxxxxxxx\n        :type Ip6TranslatorId: str\n        :param Ip6TranslatorName: IPV6转换实例修改名称\n        :type Ip6TranslatorName: str\n        """
        self.Ip6TranslatorId = None
        self.Ip6TranslatorName = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6TranslatorName = params.get("Ip6TranslatorName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyIp6TranslatorResponse(AbstractModel):
    """ModifyIp6Translator返回参数结构体

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
        :param NetworkInterfaceId: 弹性网卡实例`ID`，形如：`eni-m6dyj72l`。\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: 指定的内网IPv6`地址信息。\n        :type Ipv6Addresses: list of Ipv6Address\n        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
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


class ModifyLocalGatewayRequest(AbstractModel):
    """ModifyLocalGateway请求参数结构体

    """

    def __init__(self):
        """
        :param LocalGatewayName: 本地网关名称\n        :type LocalGatewayName: str\n        :param CdcId: CDC实例ID\n        :type CdcId: str\n        :param LocalGatewayId: 本地网关实例ID\n        :type LocalGatewayId: str\n        :param VpcId: VPC实例ID\n        :type VpcId: str\n        """
        self.LocalGatewayName = None
        self.CdcId = None
        self.LocalGatewayId = None
        self.VpcId = None


    def _deserialize(self, params):
        self.LocalGatewayName = params.get("LocalGatewayName")
        self.CdcId = params.get("CdcId")
        self.LocalGatewayId = params.get("LocalGatewayId")
        self.VpcId = params.get("VpcId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyLocalGatewayResponse(AbstractModel):
    """ModifyLocalGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayAttributeRequest(AbstractModel):
    """ModifyNatGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param NatGatewayName: NAT网关的名称，形如：`test_nat`。\n        :type NatGatewayName: str\n        :param InternetMaxBandwidthOut: NAT网关最大外网出带宽(单位:Mbps)。\n        :type InternetMaxBandwidthOut: int\n        :param ModifySecurityGroup: 是否修改NAT网关绑定的安全组。\n        :type ModifySecurityGroup: bool\n        :param SecurityGroupIds: NAT网关绑定的安全组列表，最终状态，空列表表示删除所有安全组，形如: `['sg-1n232323', 'sg-o4242424']`\n        :type SecurityGroupIds: list of str\n        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.InternetMaxBandwidthOut = None
        self.ModifySecurityGroup = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.ModifySecurityGroup = params.get("ModifySecurityGroup")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatGatewayAttributeResponse(AbstractModel):
    """ModifyNatGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewayDestinationIpPortTranslationNatRuleRequest(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df45454`。\n        :type NatGatewayId: str\n        :param SourceNatRule: 源NAT网关的端口转换规则。\n        :type SourceNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`\n        :param DestinationNatRule: 目的NAT网关的端口转换规则。\n        :type DestinationNatRule: :class:`tencentcloud.vpc.v20170312.models.DestinationIpPortTranslationNatRule`\n        """
        self.NatGatewayId = None
        self.SourceNatRule = None
        self.DestinationNatRule = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceNatRule") is not None:
            self.SourceNatRule = DestinationIpPortTranslationNatRule()
            self.SourceNatRule._deserialize(params.get("SourceNatRule"))
        if params.get("DestinationNatRule") is not None:
            self.DestinationNatRule = DestinationIpPortTranslationNatRule()
            self.DestinationNatRule._deserialize(params.get("DestinationNatRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatGatewayDestinationIpPortTranslationNatRuleResponse(AbstractModel):
    """ModifyNatGatewayDestinationIpPortTranslationNatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNatGatewaySourceIpTranslationNatRuleRequest(AbstractModel):
    """ModifyNatGatewaySourceIpTranslationNatRule请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID，形如：`nat-df453454`。\n        :type NatGatewayId: str\n        :param SourceIpTranslationNatRule: NAT网关的SNAT转换规则。\n        :type SourceIpTranslationNatRule: :class:`tencentcloud.vpc.v20170312.models.SourceIpTranslationNatRule`\n        """
        self.NatGatewayId = None
        self.SourceIpTranslationNatRule = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        if params.get("SourceIpTranslationNatRule") is not None:
            self.SourceIpTranslationNatRule = SourceIpTranslationNatRule()
            self.SourceIpTranslationNatRule._deserialize(params.get("SourceIpTranslationNatRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatGatewaySourceIpTranslationNatRuleResponse(AbstractModel):
    """ModifyNatGatewaySourceIpTranslationNatRule返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetDetectRequest(AbstractModel):
    """ModifyNetDetect请求参数结构体

    """

    def __init__(self):
        """
        :param NetDetectId: 网络探测实例`ID`。形如：`netd-12345678`\n        :type NetDetectId: str\n        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。\n        :type NetDetectName: str\n        :param DetectDestinationIp: 探测目的IPv4地址数组，最多两个。\n        :type DetectDestinationIp: list of str\n        :param NextHopType: 下一跳类型，目前我们支持的类型有：
VPN：VPN网关；
DIRECTCONNECT：专线网关；
PEERCONNECTION：对等连接；
NAT：NAT网关；
NORMAL_CVM：普通云服务器；\n        :type NextHopType: str\n        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；\n        :type NextHopDestination: str\n        :param NetDetectDescription: 网络探测描述。\n        :type NetDetectDescription: str\n        """
        self.NetDetectId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NetDetectDescription = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NetDetectDescription = params.get("NetDetectDescription")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetDetectResponse(AbstractModel):
    """ModifyNetDetect返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclAttributeRequest(AbstractModel):
    """ModifyNetworkAclAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkAclId: 网络ACL实例ID。例如：acl-12345678。\n        :type NetworkAclId: str\n        :param NetworkAclName: 网络ACL名称，最大长度不能超过60个字节。\n        :type NetworkAclName: str\n        """
        self.NetworkAclId = None
        self.NetworkAclName = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkAclAttributeResponse(AbstractModel):
    """ModifyNetworkAclAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkAclEntriesRequest(AbstractModel):
    """ModifyNetworkAclEntries请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkAclId: 网络ACL实例ID。例如：acl-12345678。\n        :type NetworkAclId: str\n        :param NetworkAclEntrySet: 网络ACL规则集。\n        :type NetworkAclEntrySet: :class:`tencentcloud.vpc.v20170312.models.NetworkAclEntrySet`\n        """
        self.NetworkAclId = None
        self.NetworkAclEntrySet = None


    def _deserialize(self, params):
        self.NetworkAclId = params.get("NetworkAclId")
        if params.get("NetworkAclEntrySet") is not None:
            self.NetworkAclEntrySet = NetworkAclEntrySet()
            self.NetworkAclEntrySet._deserialize(params.get("NetworkAclEntrySet"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkAclEntriesResponse(AbstractModel):
    """ModifyNetworkAclEntries返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkInterfaceAttributeRequest(AbstractModel):
    """ModifyNetworkInterfaceAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-pxir56ns。\n        :type NetworkInterfaceId: str\n        :param NetworkInterfaceName: 弹性网卡名称，最大长度不能超过60个字节。\n        :type NetworkInterfaceName: str\n        :param NetworkInterfaceDescription: 弹性网卡描述，可任意命名，但不得超过60个字符。\n        :type NetworkInterfaceDescription: str\n        :param SecurityGroupIds: 指定绑定的安全组，例如:['sg-1dd51d']。\n        :type SecurityGroupIds: list of str\n        """
        self.NetworkInterfaceId = None
        self.NetworkInterfaceName = None
        self.NetworkInterfaceDescription = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.NetworkInterfaceId = params.get("NetworkInterfaceId")
        self.NetworkInterfaceName = params.get("NetworkInterfaceName")
        self.NetworkInterfaceDescription = params.get("NetworkInterfaceDescription")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkInterfaceAttributeResponse(AbstractModel):
    """ModifyNetworkInterfaceAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyNetworkInterfaceQosRequest(AbstractModel):
    """ModifyNetworkInterfaceQos请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceIds: 弹性网卡ID，支持批量修改。\n        :type NetworkInterfaceIds: list of str\n        :param QosLevel: 服务质量，可选值：AU、AG、PT，分别代表金、银、白金三个等级。\n        :type QosLevel: str\n        """
        self.NetworkInterfaceIds = None
        self.QosLevel = None


    def _deserialize(self, params):
        self.NetworkInterfaceIds = params.get("NetworkInterfaceIds")
        self.QosLevel = params.get("QosLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNetworkInterfaceQosResponse(AbstractModel):
    """ModifyNetworkInterfaceQos返回参数结构体

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
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: 指定的内网IP信息。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        """
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
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        """
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
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param GroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type GroupName: str\n        :param GroupDescription: 安全组备注，最多100个字符。\n        :type GroupDescription: str\n        """
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
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合。 SecurityGroupPolicySet对象必须同时指定新的出（Egress）入（Ingress）站规则。 SecurityGroupPolicy对象不支持自定义索引（PolicyIndex）。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        :param SortPolicys: 排序安全组标识，默认值为False。当SortPolicys为False时，不改变安全组规则排序；当SortPolicys为True时，系统将严格按照SecurityGroupPolicySet参数传入的安全组规则及顺序进行重置，考虑到人为输入参数可能存在遗漏风险，建议通过控制台对安全组规则进行排序。\n        :type SortPolicys: bool\n        """
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


class ModifyServiceTemplateAttributeRequest(AbstractModel):
    """ModifyServiceTemplateAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 协议端口模板实例ID，例如：ppm-529nwwj8。\n        :type ServiceTemplateId: str\n        :param ServiceTemplateName: 协议端口模板名称。\n        :type ServiceTemplateName: str\n        :param Services: 支持单个端口、多个端口、连续端口及所有端口，协议支持：TCP、UDP、ICMP、GRE 协议。\n        :type Services: list of str\n        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.Services = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.Services = params.get("Services")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceTemplateAttributeResponse(AbstractModel):
    """ModifyServiceTemplateAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyServiceTemplateGroupAttributeRequest(AbstractModel):
    """ModifyServiceTemplateGroupAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 协议端口模板集合实例ID，例如：ppmg-ei8hfd9a。\n        :type ServiceTemplateGroupId: str\n        :param ServiceTemplateGroupName: 协议端口模板集合名称。\n        :type ServiceTemplateGroupName: str\n        :param ServiceTemplateIds: 协议端口模板实例ID，例如：ppm-4dw6agho。\n        :type ServiceTemplateIds: list of str\n        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIds = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIds = params.get("ServiceTemplateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyServiceTemplateGroupAttributeResponse(AbstractModel):
    """ModifyServiceTemplateGroupAttribute返回参数结构体

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
        :param SubnetId: 子网实例ID。形如：subnet-pxir56ns。\n        :type SubnetId: str\n        :param SubnetName: 子网名称，最大长度不能超过60个字节。\n        :type SubnetName: str\n        :param EnableBroadcast: 子网是否开启广播。\n        :type EnableBroadcast: str\n        """
        self.SubnetId = None
        self.SubnetName = None
        self.EnableBroadcast = None


    def _deserialize(self, params):
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.EnableBroadcast = params.get("EnableBroadcast")
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


class ModifyVpcAttributeRequest(AbstractModel):
    """ModifyVpcAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。形如：vpc-f49l6u0z。每次请求的实例的上限为100。参数不支持同时指定VpcIds和Filters。\n        :type VpcId: str\n        :param VpcName: 私有网络名称，可任意命名，但不得超过60个字符。\n        :type VpcName: str\n        :param EnableMulticast: 是否开启组播。true: 开启, false: 关闭。\n        :type EnableMulticast: str\n        :param DnsServers: DNS地址，最多支持4个，第1个默认为主，其余为备\n        :type DnsServers: list of str\n        :param DomainName: 域名\n        :type DomainName: str\n        """
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


class ModifyVpcEndPointAttributeRequest(AbstractModel):
    """ModifyVpcEndPointAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param EndPointId: 终端节点ID。\n        :type EndPointId: str\n        :param EndPointName: 终端节点名称。\n        :type EndPointName: str\n        :param SecurityGroupIds: 安全组ID列表。\n        :type SecurityGroupIds: list of str\n        """
        self.EndPointId = None
        self.EndPointName = None
        self.SecurityGroupIds = None


    def _deserialize(self, params):
        self.EndPointId = params.get("EndPointId")
        self.EndPointName = params.get("EndPointName")
        self.SecurityGroupIds = params.get("SecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcEndPointAttributeResponse(AbstractModel):
    """ModifyVpcEndPointAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcEndPointServiceAttributeRequest(AbstractModel):
    """ModifyVpcEndPointServiceAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        :param VpcId: VPCID。\n        :type VpcId: str\n        :param EndPointServiceName: 终端节点服务名称。\n        :type EndPointServiceName: str\n        :param AutoAcceptFlag: 是否自动接受。\n        :type AutoAcceptFlag: bool\n        :param ServiceInstanceId: 后端服务的ID，比如lb-xxx。\n        :type ServiceInstanceId: str\n        """
        self.EndPointServiceId = None
        self.VpcId = None
        self.EndPointServiceName = None
        self.AutoAcceptFlag = None
        self.ServiceInstanceId = None


    def _deserialize(self, params):
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.VpcId = params.get("VpcId")
        self.EndPointServiceName = params.get("EndPointServiceName")
        self.AutoAcceptFlag = params.get("AutoAcceptFlag")
        self.ServiceInstanceId = params.get("ServiceInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcEndPointServiceAttributeResponse(AbstractModel):
    """ModifyVpcEndPointServiceAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpcEndPointServiceWhiteListRequest(AbstractModel):
    """ModifyVpcEndPointServiceWhiteList请求参数结构体

    """

    def __init__(self):
        """
        :param UserUin: 用户UIN。\n        :type UserUin: str\n        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        :param Description: 白名单描述信息。\n        :type Description: str\n        """
        self.UserUin = None
        self.EndPointServiceId = None
        self.Description = None


    def _deserialize(self, params):
        self.UserUin = params.get("UserUin")
        self.EndPointServiceId = params.get("EndPointServiceId")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcEndPointServiceWhiteListResponse(AbstractModel):
    """ModifyVpcEndPointServiceWhiteList返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnConnectionAttributeRequest(AbstractModel):
    """ModifyVpnConnectionAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。\n        :type VpnConnectionId: str\n        :param VpnConnectionName: VPN通道名称，可任意命名，但不得超过60个字符。\n        :type VpnConnectionName: str\n        :param PreShareKey: 预共享密钥。\n        :type PreShareKey: str\n        :param SecurityPolicyDatabases: SPD策略组，例如：{"10.0.0.5/24":["172.123.10.5/16"]}，10.0.0.5/24是vpc内网段172.123.10.5/16是IDC网段。用户指定VPC内哪些网段可以和您IDC中哪些网段通信。\n        :type SecurityPolicyDatabases: list of SecurityPolicyDatabase\n        :param IKEOptionsSpecification: IKE配置（Internet Key Exchange，因特网密钥交换），IKE具有一套自我保护机制，用户配置网络安全协议。\n        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`\n        :param IPSECOptionsSpecification: IPSec配置，腾讯云提供IPSec安全会话设置。\n        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`\n        :param EnableHealthCheck: 是否启用通道健康检查\n        :type EnableHealthCheck: bool\n        :param HealthCheckLocalIp: 本端通道探测ip\n        :type HealthCheckLocalIp: str\n        :param HealthCheckRemoteIp: 对端通道探测ip\n        :type HealthCheckRemoteIp: str\n        """
        self.VpnConnectionId = None
        self.VpnConnectionName = None
        self.PreShareKey = None
        self.SecurityPolicyDatabases = None
        self.IKEOptionsSpecification = None
        self.IPSECOptionsSpecification = None
        self.EnableHealthCheck = None
        self.HealthCheckLocalIp = None
        self.HealthCheckRemoteIp = None


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
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        self.HealthCheckLocalIp = params.get("HealthCheckLocalIp")
        self.HealthCheckRemoteIp = params.get("HealthCheckRemoteIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnConnectionAttributeResponse(AbstractModel):
    """ModifyVpnConnectionAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayAttributeRequest(AbstractModel):
    """ModifyVpnGatewayAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param VpnGatewayName: VPN网关名称，最大长度不能超过60个字节。\n        :type VpnGatewayName: str\n        :param InstanceChargeType: VPN网关计费模式，目前只支持预付费（即包年包月）到后付费（即按量计费）的转换。即参数只支持：POSTPAID_BY_HOUR。\n        :type InstanceChargeType: str\n        """
        self.VpnGatewayId = None
        self.VpnGatewayName = None
        self.InstanceChargeType = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnGatewayName = params.get("VpnGatewayName")
        self.InstanceChargeType = params.get("InstanceChargeType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayAttributeResponse(AbstractModel):
    """ModifyVpnGatewayAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayCcnRoutesRequest(AbstractModel):
    """ModifyVpnGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID\n        :type VpnGatewayId: str\n        :param Routes: 云联网路由（IDC网段）列表\n        :type Routes: list of VpngwCcnRoutes\n        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpngwCcnRoutes()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayCcnRoutesResponse(AbstractModel):
    """ModifyVpnGatewayCcnRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyVpnGatewayRoutesRequest(AbstractModel):
    """ModifyVpnGatewayRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: Vpn网关id\n        :type VpnGatewayId: str\n        :param Routes: 路由修改参数\n        :type Routes: list of VpnGatewayRouteModify\n        """
        self.VpnGatewayId = None
        self.Routes = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRouteModify()
                obj._deserialize(item)
                self.Routes.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpnGatewayRoutesResponse(AbstractModel):
    """ModifyVpnGatewayRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param Routes: VPN路由信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Routes: list of VpnGatewayRoute\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Routes = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Routes") is not None:
            self.Routes = []
            for item in params.get("Routes"):
                obj = VpnGatewayRoute()
                obj._deserialize(item)
                self.Routes.append(obj)
        self.RequestId = params.get("RequestId")


class NatGateway(AbstractModel):
    """NAT网关对象。

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关的ID。\n        :type NatGatewayId: str\n        :param NatGatewayName: NAT网关的名称。\n        :type NatGatewayName: str\n        :param CreatedTime: NAT网关创建的时间。\n        :type CreatedTime: str\n        :param State: NAT网关的状态。
 'PENDING'：生产中，'DELETING'：删除中，'AVAILABLE'：运行中，'UPDATING'：升级中，
‘FAILED’：失败。\n        :type State: str\n        :param InternetMaxBandwidthOut: 网关最大外网出带宽(单位:Mbps)。\n        :type InternetMaxBandwidthOut: int\n        :param MaxConcurrentConnection: 网关并发连接上限。\n        :type MaxConcurrentConnection: int\n        :param PublicIpAddressSet: 绑定NAT网关的公网IP对象数组。\n        :type PublicIpAddressSet: list of NatGatewayAddress\n        :param NetworkState: NAT网关网络状态。“AVAILABLE”:运行中, “UNAVAILABLE”:不可用, “INSUFFICIENT”:欠费停服。\n        :type NetworkState: str\n        :param DestinationIpPortTranslationNatRuleSet: NAT网关的端口转发规则。\n        :type DestinationIpPortTranslationNatRuleSet: list of DestinationIpPortTranslationNatRule\n        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param Zone: NAT网关所在的可用区。\n        :type Zone: str\n        :param DirectConnectGatewayIds: 绑定的专线网关ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DirectConnectGatewayIds: list of str\n        :param SubnetId: 所属子网ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubnetId: str\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        :param SecurityGroupSet: NAT网关绑定的安全组列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityGroupSet: list of str\n        :param SourceIpTranslationNatRuleSet: NAT网关的SNAT转发规则。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SourceIpTranslationNatRuleSet: list of SourceIpTranslationNatRule\n        :param IsExclusive: 是否独享型NAT。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsExclusive: bool\n        :param ExclusiveGatewayBandwidth: 独享型NAT所在的网关集群的带宽(单位:Mbps)，当IsExclusive为false时无此字段。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExclusiveGatewayBandwidth: int\n        """
        self.NatGatewayId = None
        self.NatGatewayName = None
        self.CreatedTime = None
        self.State = None
        self.InternetMaxBandwidthOut = None
        self.MaxConcurrentConnection = None
        self.PublicIpAddressSet = None
        self.NetworkState = None
        self.DestinationIpPortTranslationNatRuleSet = None
        self.VpcId = None
        self.Zone = None
        self.DirectConnectGatewayIds = None
        self.SubnetId = None
        self.TagSet = None
        self.SecurityGroupSet = None
        self.SourceIpTranslationNatRuleSet = None
        self.IsExclusive = None
        self.ExclusiveGatewayBandwidth = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.NatGatewayName = params.get("NatGatewayName")
        self.CreatedTime = params.get("CreatedTime")
        self.State = params.get("State")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        if params.get("PublicIpAddressSet") is not None:
            self.PublicIpAddressSet = []
            for item in params.get("PublicIpAddressSet"):
                obj = NatGatewayAddress()
                obj._deserialize(item)
                self.PublicIpAddressSet.append(obj)
        self.NetworkState = params.get("NetworkState")
        if params.get("DestinationIpPortTranslationNatRuleSet") is not None:
            self.DestinationIpPortTranslationNatRuleSet = []
            for item in params.get("DestinationIpPortTranslationNatRuleSet"):
                obj = DestinationIpPortTranslationNatRule()
                obj._deserialize(item)
                self.DestinationIpPortTranslationNatRuleSet.append(obj)
        self.VpcId = params.get("VpcId")
        self.Zone = params.get("Zone")
        self.DirectConnectGatewayIds = params.get("DirectConnectGatewayIds")
        self.SubnetId = params.get("SubnetId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.SecurityGroupSet = params.get("SecurityGroupSet")
        if params.get("SourceIpTranslationNatRuleSet") is not None:
            self.SourceIpTranslationNatRuleSet = []
            for item in params.get("SourceIpTranslationNatRuleSet"):
                obj = SourceIpTranslationNatRule()
                obj._deserialize(item)
                self.SourceIpTranslationNatRuleSet.append(obj)
        self.IsExclusive = params.get("IsExclusive")
        self.ExclusiveGatewayBandwidth = params.get("ExclusiveGatewayBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatGatewayAddress(AbstractModel):
    """NAT网关绑定的弹性IP

    """

    def __init__(self):
        """
        :param AddressId: 弹性公网IP（EIP）的唯一 ID，形如：`eip-11112222`。\n        :type AddressId: str\n        :param PublicIpAddress: 外网IP地址，形如：`123.121.34.33`。\n        :type PublicIpAddress: str\n        :param IsBlocked: 资源封堵状态。true表示弹性ip处于封堵状态，false表示弹性ip处于未封堵状态。\n        :type IsBlocked: bool\n        """
        self.AddressId = None
        self.PublicIpAddress = None
        self.IsBlocked = None


    def _deserialize(self, params):
        self.AddressId = params.get("AddressId")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.IsBlocked = params.get("IsBlocked")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatGatewayDestinationIpPortTranslationNatRule(AbstractModel):
    """NAT网关的端口转发规则

    """

    def __init__(self):
        """
        :param IpProtocol: 网络协议，可选值：`TCP`、`UDP`。\n        :type IpProtocol: str\n        :param PublicIpAddress: 弹性IP。\n        :type PublicIpAddress: str\n        :param PublicPort: 公网端口。\n        :type PublicPort: int\n        :param PrivateIpAddress: 内网地址。\n        :type PrivateIpAddress: str\n        :param PrivatePort: 内网端口。\n        :type PrivatePort: int\n        :param Description: NAT网关转发规则描述。\n        :type Description: str\n        :param NatGatewayId: NAT网关的ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NatGatewayId: str\n        :param VpcId: 私有网络VPC的ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param CreatedTime: NAT网关转发规则创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        """
        self.IpProtocol = None
        self.PublicIpAddress = None
        self.PublicPort = None
        self.PrivateIpAddress = None
        self.PrivatePort = None
        self.Description = None
        self.NatGatewayId = None
        self.VpcId = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.IpProtocol = params.get("IpProtocol")
        self.PublicIpAddress = params.get("PublicIpAddress")
        self.PublicPort = params.get("PublicPort")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PrivatePort = params.get("PrivatePort")
        self.Description = params.get("Description")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetect(AbstractModel):
    """网络探测对象。

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。形如：`vpc-12345678`\n        :type VpcId: str\n        :param VpcName: `VPC`实例名称。\n        :type VpcName: str\n        :param SubnetId: 子网实例ID。形如：subnet-12345678。\n        :type SubnetId: str\n        :param SubnetName: 子网实例名称。\n        :type SubnetName: str\n        :param NetDetectId: 网络探测实例ID。形如：netd-12345678。\n        :type NetDetectId: str\n        :param NetDetectName: 网络探测名称，最大长度不能超过60个字节。\n        :type NetDetectName: str\n        :param DetectDestinationIp: 探测目的IPv4地址数组，最多两个。\n        :type DetectDestinationIp: list of str\n        :param DetectSourceIp: 系统自动分配的探测源IPv4数组。长度为2。\n        :type DetectSourceIp: list of str\n        :param NextHopType: 下一跳类型，目前我们支持的类型有：
VPN：VPN网关；
DIRECTCONNECT：专线网关；
PEERCONNECTION：对等连接；
NAT：NAT网关；
NORMAL_CVM：普通云服务器；
CCN：云联网网关；\n        :type NextHopType: str\n        :param NextHopDestination: 下一跳目的网关，取值与“下一跳类型”相关：
下一跳类型为VPN，取值VPN网关ID，形如：vpngw-12345678；
下一跳类型为DIRECTCONNECT，取值专线网关ID，形如：dcg-12345678；
下一跳类型为PEERCONNECTION，取值对等连接ID，形如：pcx-12345678；
下一跳类型为NAT，取值Nat网关，形如：nat-12345678；
下一跳类型为NORMAL_CVM，取值云服务器IPv4地址，形如：10.0.0.12；
下一跳类型为CCN，取值云联网网关，形如：ccn-12345678；\n        :type NextHopDestination: str\n        :param NextHopName: 下一跳网关名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NextHopName: str\n        :param NetDetectDescription: 网络探测描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NetDetectDescription: str\n        :param CreateTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        """
        self.VpcId = None
        self.VpcName = None
        self.SubnetId = None
        self.SubnetName = None
        self.NetDetectId = None
        self.NetDetectName = None
        self.DetectDestinationIp = None
        self.DetectSourceIp = None
        self.NextHopType = None
        self.NextHopDestination = None
        self.NextHopName = None
        self.NetDetectDescription = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.VpcName = params.get("VpcName")
        self.SubnetId = params.get("SubnetId")
        self.SubnetName = params.get("SubnetName")
        self.NetDetectId = params.get("NetDetectId")
        self.NetDetectName = params.get("NetDetectName")
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.DetectSourceIp = params.get("DetectSourceIp")
        self.NextHopType = params.get("NextHopType")
        self.NextHopDestination = params.get("NextHopDestination")
        self.NextHopName = params.get("NextHopName")
        self.NetDetectDescription = params.get("NetDetectDescription")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetectIpState(AbstractModel):
    """网络探测目的IP的验证结果。

    """

    def __init__(self):
        """
        :param DetectDestinationIp: 探测目的IPv4地址。\n        :type DetectDestinationIp: str\n        :param State: 探测结果。
0：成功；
-1：查询不到路由丢包；
-2：外出ACL丢包；
-3：IN ACL丢包；
-4：其他错误；\n        :type State: int\n        :param Delay: 时延，单位毫秒\n        :type Delay: int\n        :param PacketLossRate: 丢包率\n        :type PacketLossRate: int\n        """
        self.DetectDestinationIp = None
        self.State = None
        self.Delay = None
        self.PacketLossRate = None


    def _deserialize(self, params):
        self.DetectDestinationIp = params.get("DetectDestinationIp")
        self.State = params.get("State")
        self.Delay = params.get("Delay")
        self.PacketLossRate = params.get("PacketLossRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetDetectState(AbstractModel):
    """网络探测验证结果。

    """

    def __init__(self):
        """
        :param NetDetectId: 网络探测实例ID。形如：netd-12345678。\n        :type NetDetectId: str\n        :param NetDetectIpStateSet: 网络探测目的IP验证结果对象数组。\n        :type NetDetectIpStateSet: list of NetDetectIpState\n        """
        self.NetDetectId = None
        self.NetDetectIpStateSet = None


    def _deserialize(self, params):
        self.NetDetectId = params.get("NetDetectId")
        if params.get("NetDetectIpStateSet") is not None:
            self.NetDetectIpStateSet = []
            for item in params.get("NetDetectIpStateSet"):
                obj = NetDetectIpState()
                obj._deserialize(item)
                self.NetDetectIpStateSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAcl(AbstractModel):
    """网络ACL

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。\n        :type VpcId: str\n        :param NetworkAclId: 网络ACL实例`ID`。\n        :type NetworkAclId: str\n        :param NetworkAclName: 网络ACL名称，最大长度为60。\n        :type NetworkAclName: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param SubnetSet: 网络ACL关联的子网数组。\n        :type SubnetSet: list of Subnet\n        :param IngressEntries: 网络ACl入站规则。\n        :type IngressEntries: list of NetworkAclEntry\n        :param EgressEntries: 网络ACL出站规则。\n        :type EgressEntries: list of NetworkAclEntry\n        """
        self.VpcId = None
        self.NetworkAclId = None
        self.NetworkAclName = None
        self.CreatedTime = None
        self.SubnetSet = None
        self.IngressEntries = None
        self.EgressEntries = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.NetworkAclId = params.get("NetworkAclId")
        self.NetworkAclName = params.get("NetworkAclName")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("SubnetSet") is not None:
            self.SubnetSet = []
            for item in params.get("SubnetSet"):
                obj = Subnet()
                obj._deserialize(item)
                self.SubnetSet.append(obj)
        if params.get("IngressEntries") is not None:
            self.IngressEntries = []
            for item in params.get("IngressEntries"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.IngressEntries.append(obj)
        if params.get("EgressEntries") is not None:
            self.EgressEntries = []
            for item in params.get("EgressEntries"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.EgressEntries.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAclEntry(AbstractModel):
    """网络ACL规则。

    """

    def __init__(self):
        """
        :param ModifyTime: 修改时间。\n        :type ModifyTime: str\n        :param Protocol: 协议, 取值: TCP,UDP, ICMP, ALL。\n        :type Protocol: str\n        :param Port: 端口(all, 单个port,  range)。当Protocol为ALL或ICMP时，不能指定Port。\n        :type Port: str\n        :param CidrBlock: 网段或IP(互斥)。\n        :type CidrBlock: str\n        :param Ipv6CidrBlock: 网段或IPv6(互斥)。\n        :type Ipv6CidrBlock: str\n        :param Action: ACCEPT 或 DROP。\n        :type Action: str\n        :param Description: 规则描述，最大长度100。\n        :type Description: str\n        """
        self.ModifyTime = None
        self.Protocol = None
        self.Port = None
        self.CidrBlock = None
        self.Ipv6CidrBlock = None
        self.Action = None
        self.Description = None


    def _deserialize(self, params):
        self.ModifyTime = params.get("ModifyTime")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.Action = params.get("Action")
        self.Description = params.get("Description")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NetworkAclEntrySet(AbstractModel):
    """网络ACL规则集合

    """

    def __init__(self):
        """
        :param Ingress: 入站规则。\n        :type Ingress: list of NetworkAclEntry\n        :param Egress: 出站规则。\n        :type Egress: list of NetworkAclEntry\n        """
        self.Ingress = None
        self.Egress = None


    def _deserialize(self, params):
        if params.get("Ingress") is not None:
            self.Ingress = []
            for item in params.get("Ingress"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.Ingress.append(obj)
        if params.get("Egress") is not None:
            self.Egress = []
            for item in params.get("Egress"):
                obj = NetworkAclEntry()
                obj._deserialize(item)
                self.Egress.append(obj)
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
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-f1xjkw1b。\n        :type NetworkInterfaceId: str\n        :param NetworkInterfaceName: 弹性网卡名称。\n        :type NetworkInterfaceName: str\n        :param NetworkInterfaceDescription: 弹性网卡描述。\n        :type NetworkInterfaceDescription: str\n        :param SubnetId: 子网实例ID。\n        :type SubnetId: str\n        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param GroupSet: 绑定的安全组。\n        :type GroupSet: list of str\n        :param Primary: 是否是主网卡。\n        :type Primary: bool\n        :param MacAddress: MAC地址。\n        :type MacAddress: str\n        :param State: 弹性网卡状态：
<li>`PENDING`：创建中</li>
<li>`AVAILABLE`：可用的</li>
<li>`ATTACHING`：绑定中</li>
<li>`DETACHING`：解绑中</li>
<li>`DELETING`：删除中</li>\n        :type State: str\n        :param PrivateIpAddressSet: 内网IP信息。\n        :type PrivateIpAddressSet: list of PrivateIpAddressSpecification\n        :param Attachment: 绑定的云服务器对象。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Attachment: :class:`tencentcloud.vpc.v20170312.models.NetworkInterfaceAttachment`\n        :param Zone: 可用区。\n        :type Zone: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param Ipv6AddressSet: `IPv6`地址列表。\n        :type Ipv6AddressSet: list of Ipv6Address\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        :param EniType: 网卡类型。0 - 弹性网卡；1 - evm弹性网卡。\n        :type EniType: int\n        :param Business: 网卡绑定的子机类型：cvm，eks。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Business: str\n        :param CdcId: 网卡所关联的CDC实例ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CdcId: str\n        :param AttachType: 弹性网卡类型：0:标准型/1:扩展型。默认值为0。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AttachType: int\n        """
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
        self.Business = None
        self.CdcId = None
        self.AttachType = None


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
        self.Business = params.get("Business")
        self.CdcId = params.get("CdcId")
        self.AttachType = params.get("AttachType")
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
        


class NotifyRoutesRequest(AbstractModel):
    """NotifyRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param RouteItemIds: 路由策略唯一ID。\n        :type RouteItemIds: list of str\n        """
        self.RouteTableId = None
        self.RouteItemIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteItemIds = params.get("RouteItemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NotifyRoutesResponse(AbstractModel):
    """NotifyRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Price(AbstractModel):
    """价格

    """

    def __init__(self):
        """
        :param InstancePrice: 实例价格。\n        :type InstancePrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`\n        :param BandwidthPrice: 网络价格。\n        :type BandwidthPrice: :class:`tencentcloud.vpc.v20170312.models.ItemPrice`\n        """
        self.InstancePrice = None
        self.BandwidthPrice = None


    def _deserialize(self, params):
        if params.get("InstancePrice") is not None:
            self.InstancePrice = ItemPrice()
            self.InstancePrice._deserialize(params.get("InstancePrice"))
        if params.get("BandwidthPrice") is not None:
            self.BandwidthPrice = ItemPrice()
            self.BandwidthPrice._deserialize(params.get("BandwidthPrice"))
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
        :param PrivateIpAddress: 内网IP地址。\n        :type PrivateIpAddress: str\n        :param Primary: 是否是主IP。\n        :type Primary: bool\n        :param PublicIpAddress: 公网IP地址。\n        :type PublicIpAddress: str\n        :param AddressId: EIP实例ID，例如：eip-11112222。\n        :type AddressId: str\n        :param Description: 内网IP描述信息。\n        :type Description: str\n        :param IsWanIpBlocked: 公网IP是否被封堵。\n        :type IsWanIpBlocked: bool\n        :param State: IP状态：
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
        


class ProductQuota(AbstractModel):
    """描述网络中心每个产品的配额信息

    """

    def __init__(self):
        """
        :param QuotaId: 产品配额ID\n        :type QuotaId: str\n        :param QuotaName: 产品配额名称\n        :type QuotaName: str\n        :param QuotaCurrent: 产品当前配额\n        :type QuotaCurrent: int\n        :param QuotaLimit: 产品配额上限\n        :type QuotaLimit: int\n        :param QuotaRegion: 产品配额是否有地域属性\n        :type QuotaRegion: bool\n        """
        self.QuotaId = None
        self.QuotaName = None
        self.QuotaCurrent = None
        self.QuotaLimit = None
        self.QuotaRegion = None


    def _deserialize(self, params):
        self.QuotaId = params.get("QuotaId")
        self.QuotaName = params.get("QuotaName")
        self.QuotaCurrent = params.get("QuotaCurrent")
        self.QuotaLimit = params.get("QuotaLimit")
        self.QuotaRegion = params.get("QuotaRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """描述配额信息

    """

    def __init__(self):
        """
        :param QuotaId: 配额名称，取值范围：<br><li>`TOTAL_EIP_QUOTA`：用户当前地域下EIP的配额数；<br><li>`DAILY_EIP_APPLY`：用户当前地域下今日申购次数；<br><li>`DAILY_PUBLIC_IP_ASSIGN`：用户当前地域下，重新分配公网 IP次数。\n        :type QuotaId: str\n        :param QuotaCurrent: 当前数量\n        :type QuotaCurrent: int\n        :param QuotaLimit: 配额数量\n        :type QuotaLimit: int\n        """
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
        


class ReferredSecurityGroup(AbstractModel):
    """安全组被引用信息

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID。\n        :type SecurityGroupId: str\n        :param ReferredSecurityGroupIds: 引用安全组实例ID（SecurityGroupId）的所有安全组实例ID。\n        :type ReferredSecurityGroupIds: list of str\n        """
        self.SecurityGroupId = None
        self.ReferredSecurityGroupIds = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.ReferredSecurityGroupIds = params.get("ReferredSecurityGroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectAttachCcnInstancesRequest(AbstractModel):
    """RejectAttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param Instances: 拒绝关联实例列表。\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RejectAttachCcnInstancesResponse(AbstractModel):
    """RejectAttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReleaseAddressesRequest(AbstractModel):
    """ReleaseAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param AddressIds: 标识 EIP 的唯一 ID 列表。EIP 唯一 ID 形如：`eip-11112222`。\n        :type AddressIds: list of str\n        """
        self.AddressIds = None


    def _deserialize(self, params):
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
        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ReleaseIp6AddressesBandwidthRequest(AbstractModel):
    """ReleaseIp6AddressesBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6Addresses: IPV6地址。Ip6Addresses和Ip6AddressIds必须且只能传一个\n        :type Ip6Addresses: list of str\n        :param Ip6AddressIds: IPV6地址对应的唯一ID，形如eip-xxxxxxxx。Ip6Addresses和Ip6AddressIds必须且只能传一个。\n        :type Ip6AddressIds: list of str\n        """
        self.Ip6Addresses = None
        self.Ip6AddressIds = None


    def _deserialize(self, params):
        self.Ip6Addresses = params.get("Ip6Addresses")
        self.Ip6AddressIds = params.get("Ip6AddressIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReleaseIp6AddressesBandwidthResponse(AbstractModel):
    """ReleaseIp6AddressesBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 异步任务TaskId。可以使用[DescribeTaskResult](https://cloud.tencent.com/document/api/215/36271)接口查询任务状态。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class RemoveBandwidthPackageResourcesRequest(AbstractModel):
    """RemoveBandwidthPackageResources请求参数结构体

    """

    def __init__(self):
        """
        :param BandwidthPackageId: 带宽包唯一标识ID，形如'bwp-xxxx'\n        :type BandwidthPackageId: str\n        :param ResourceType: 资源类型，包括‘Address’, ‘LoadBalance’\n        :type ResourceType: str\n        :param ResourceIds: 资源ID，可支持资源形如'eip-xxxx', 'lb-xxxx'\n        :type ResourceIds: list of str\n        """
        self.BandwidthPackageId = None
        self.ResourceType = None
        self.ResourceIds = None


    def _deserialize(self, params):
        self.BandwidthPackageId = params.get("BandwidthPackageId")
        self.ResourceType = params.get("ResourceType")
        self.ResourceIds = params.get("ResourceIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveBandwidthPackageResourcesResponse(AbstractModel):
    """RemoveBandwidthPackageResources返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RemoveIp6RulesRequest(AbstractModel):
    """RemoveIp6Rules请求参数结构体

    """

    def __init__(self):
        """
        :param Ip6TranslatorId: IPV6转换规则所属的转换实例唯一ID，形如ip6-xxxxxxxx\n        :type Ip6TranslatorId: str\n        :param Ip6RuleIds: 待删除IPV6转换规则，形如rule6-xxxxxxxx\n        :type Ip6RuleIds: list of str\n        """
        self.Ip6TranslatorId = None
        self.Ip6RuleIds = None


    def _deserialize(self, params):
        self.Ip6TranslatorId = params.get("Ip6TranslatorId")
        self.Ip6RuleIds = params.get("Ip6RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveIp6RulesResponse(AbstractModel):
    """RemoveIp6Rules返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewAddressesRequest(AbstractModel):
    """RenewAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param AddressIds: EIP唯一标识ID列表，形如'eip-xxxx'\n        :type AddressIds: list of str\n        :param AddressChargePrepaid: 续费参数\n        :type AddressChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.AddressChargePrepaid`\n        """
        self.AddressIds = None
        self.AddressChargePrepaid = None


    def _deserialize(self, params):
        self.AddressIds = params.get("AddressIds")
        if params.get("AddressChargePrepaid") is not None:
            self.AddressChargePrepaid = AddressChargePrepaid()
            self.AddressChargePrepaid._deserialize(params.get("AddressChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewAddressesResponse(AbstractModel):
    """RenewAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RenewVpnGatewayRequest(AbstractModel):
    """RenewVpnGateway请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param InstanceChargePrepaid: 预付费计费模式。\n        :type InstanceChargePrepaid: :class:`tencentcloud.vpc.v20170312.models.InstanceChargePrepaid`\n        """
        self.VpnGatewayId = None
        self.InstanceChargePrepaid = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        if params.get("InstanceChargePrepaid") is not None:
            self.InstanceChargePrepaid = InstanceChargePrepaid()
            self.InstanceChargePrepaid._deserialize(params.get("InstanceChargePrepaid"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewVpnGatewayResponse(AbstractModel):
    """RenewVpnGateway返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ReplaceDirectConnectGatewayCcnRoutesRequest(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param DirectConnectGatewayId: 专线网关ID，形如：dcg-prpqlmg1\n        :type DirectConnectGatewayId: str\n        :param Routes: 需要连通的IDC网段列表\n        :type Routes: list of DirectConnectGatewayCcnRoute\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceDirectConnectGatewayCcnRoutesResponse(AbstractModel):
    """ReplaceDirectConnectGatewayCcnRoutes返回参数结构体

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
        :param SubnetId: 子网实例ID，例如：subnet-3x5lf5q0。可通过DescribeSubnets接口查询。\n        :type SubnetId: str\n        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        """
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
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param Routes: 路由策略对象。需要指定路由策略ID（RouteId）。\n        :type Routes: list of Route\n        """
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
        :param OldRouteSet: 原路由策略信息。\n        :type OldRouteSet: list of Route\n        :param NewRouteSet: 修改后的路由策略信息。\n        :type NewRouteSet: list of Route\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.OldRouteSet = None
        self.NewRouteSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("OldRouteSet") is not None:
            self.OldRouteSet = []
            for item in params.get("OldRouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.OldRouteSet.append(obj)
        if params.get("NewRouteSet") is not None:
            self.NewRouteSet = []
            for item in params.get("NewRouteSet"):
                obj = Route()
                obj._deserialize(item)
                self.NewRouteSet.append(obj)
        self.RequestId = params.get("RequestId")


class ReplaceSecurityGroupPolicyRequest(AbstractModel):
    """ReplaceSecurityGroupPolicy请求参数结构体

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如sg-33ocnj9n，可通过DescribeSecurityGroups获取。\n        :type SecurityGroupId: str\n        :param SecurityGroupPolicySet: 安全组规则集合对象。\n        :type SecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        :param OriginalSecurityGroupPolicySet: 旧的安全组规则集合对象，可选，日志记录用。\n        :type OriginalSecurityGroupPolicySet: :class:`tencentcloud.vpc.v20170312.models.SecurityGroupPolicySet`\n        """
        self.SecurityGroupId = None
        self.SecurityGroupPolicySet = None
        self.OriginalSecurityGroupPolicySet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("SecurityGroupPolicySet") is not None:
            self.SecurityGroupPolicySet = SecurityGroupPolicySet()
            self.SecurityGroupPolicySet._deserialize(params.get("SecurityGroupPolicySet"))
        if params.get("OriginalSecurityGroupPolicySet") is not None:
            self.OriginalSecurityGroupPolicySet = SecurityGroupPolicySet()
            self.OriginalSecurityGroupPolicySet._deserialize(params.get("OriginalSecurityGroupPolicySet"))
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


class ResetAttachCcnInstancesRequest(AbstractModel):
    """ResetAttachCcnInstances请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param CcnUin: CCN所属UIN（根账号）。\n        :type CcnUin: str\n        :param Instances: 重新申请关联网络实例列表。\n        :type Instances: list of CcnInstance\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetAttachCcnInstancesResponse(AbstractModel):
    """ResetAttachCcnInstances返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetNatGatewayConnectionRequest(AbstractModel):
    """ResetNatGatewayConnection请求参数结构体

    """

    def __init__(self):
        """
        :param NatGatewayId: NAT网关ID。\n        :type NatGatewayId: str\n        :param MaxConcurrentConnection: NAT网关并发连接上限，形如：1000000、3000000、10000000。\n        :type MaxConcurrentConnection: int\n        """
        self.NatGatewayId = None
        self.MaxConcurrentConnection = None


    def _deserialize(self, params):
        self.NatGatewayId = params.get("NatGatewayId")
        self.MaxConcurrentConnection = params.get("MaxConcurrentConnection")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetNatGatewayConnectionResponse(AbstractModel):
    """ResetNatGatewayConnection返回参数结构体

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


class ResetVpnConnectionRequest(AbstractModel):
    """ResetVpnConnection请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param VpnConnectionId: VPN通道实例ID。形如：vpnx-f49l6u0z。\n        :type VpnConnectionId: str\n        """
        self.VpnGatewayId = None
        self.VpnConnectionId = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.VpnConnectionId = params.get("VpnConnectionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetVpnConnectionResponse(AbstractModel):
    """ResetVpnConnection返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResetVpnGatewayInternetMaxBandwidthRequest(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth请求参数结构体

    """

    def __init__(self):
        """
        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param InternetMaxBandwidthOut: 公网带宽设置。可选带宽规格：5, 10, 20, 50, 100；单位：Mbps。\n        :type InternetMaxBandwidthOut: int\n        """
        self.VpnGatewayId = None
        self.InternetMaxBandwidthOut = None


    def _deserialize(self, params):
        self.VpnGatewayId = params.get("VpnGatewayId")
        self.InternetMaxBandwidthOut = params.get("InternetMaxBandwidthOut")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResetVpnGatewayInternetMaxBandwidthResponse(AbstractModel):
    """ResetVpnGatewayInternetMaxBandwidth返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Resource(AbstractModel):
    """描述带宽包资源信息的结构

    """

    def __init__(self):
        """
        :param ResourceType: 带宽包资源类型，包括'Address'和'LoadBalance'\n        :type ResourceType: str\n        :param ResourceId: 带宽包资源Id，形如'eip-xxxx', 'lb-xxxx'\n        :type ResourceId: str\n        :param AddressIp: 带宽包资源Ip\n        :type AddressIp: str\n        """
        self.ResourceType = None
        self.ResourceId = None
        self.AddressIp = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        self.AddressIp = params.get("AddressIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceDashboard(AbstractModel):
    """VPC资源看板（各资源个数）

    """

    def __init__(self):
        """
        :param VpcId: Vpc实例ID，例如：vpc-bq4bzxpj。\n        :type VpcId: str\n        :param SubnetId: 子网实例ID，例如：subnet-bthucmmy。\n        :type SubnetId: str\n        :param Classiclink: 基础网络互通。\n        :type Classiclink: int\n        :param Dcg: 专线网关。\n        :type Dcg: int\n        :param Pcx: 对等连接。\n        :type Pcx: int\n        :param Ip: 统计当前除云服务器 IP、弹性网卡IP和网络探测IP以外的所有已使用的IP总数。云服务器 IP、弹性网卡IP和网络探测IP单独计数。\n        :type Ip: int\n        :param Nat: NAT网关。\n        :type Nat: int\n        :param Vpngw: VPN网关。\n        :type Vpngw: int\n        :param FlowLog: 流日志。\n        :type FlowLog: int\n        :param NetworkDetect: 网络探测。\n        :type NetworkDetect: int\n        :param NetworkACL: 网络ACL。\n        :type NetworkACL: int\n        :param CVM: 云主机。\n        :type CVM: int\n        :param LB: 负载均衡。\n        :type LB: int\n        :param CDB: 关系型数据库。\n        :type CDB: int\n        :param Cmem: 云数据库 TencentDB for Memcached。\n        :type Cmem: int\n        :param CTSDB: 时序数据库。\n        :type CTSDB: int\n        :param MariaDB: 数据库 TencentDB for MariaDB（TDSQL）。\n        :type MariaDB: int\n        :param SQLServer: 数据库 TencentDB for SQL Server。\n        :type SQLServer: int\n        :param Postgres: 云数据库 TencentDB for PostgreSQL。\n        :type Postgres: int\n        :param NAS: 网络附加存储。\n        :type NAS: int\n        :param Greenplumn: Snova云数据仓库。\n        :type Greenplumn: int\n        :param Ckafka: 消息队列 CKAFKA。\n        :type Ckafka: int\n        :param Grocery: Grocery。\n        :type Grocery: int\n        :param HSM: 数据加密服务。\n        :type HSM: int\n        :param Tcaplus: 游戏存储 Tcaplus。\n        :type Tcaplus: int\n        :param Cnas: Cnas。\n        :type Cnas: int\n        :param TiDB: HTAP 数据库 TiDB。\n        :type TiDB: int\n        :param Emr: EMR 集群。\n        :type Emr: int\n        :param SEAL: SEAL。\n        :type SEAL: int\n        :param CFS: 文件存储 CFS。\n        :type CFS: int\n        :param Oracle: Oracle。\n        :type Oracle: int\n        :param ElasticSearch: ElasticSearch服务。\n        :type ElasticSearch: int\n        :param TBaaS: 区块链服务。\n        :type TBaaS: int\n        :param Itop: Itop。\n        :type Itop: int\n        :param DBAudit: 云数据库审计。\n        :type DBAudit: int\n        :param CynosDBPostgres: 企业级云数据库 CynosDB for Postgres。\n        :type CynosDBPostgres: int\n        :param Redis: 数据库 TencentDB for Redis。\n        :type Redis: int\n        :param MongoDB: 数据库 TencentDB for MongoDB。\n        :type MongoDB: int\n        :param DCDB: 分布式数据库 TencentDB for TDSQL。\n        :type DCDB: int\n        :param CynosDBMySQL: 企业级云数据库 CynosDB for MySQL。\n        :type CynosDBMySQL: int\n        :param Subnet: 子网。\n        :type Subnet: int\n        :param RouteTable: 路由表。\n        :type RouteTable: int\n        """
        self.VpcId = None
        self.SubnetId = None
        self.Classiclink = None
        self.Dcg = None
        self.Pcx = None
        self.Ip = None
        self.Nat = None
        self.Vpngw = None
        self.FlowLog = None
        self.NetworkDetect = None
        self.NetworkACL = None
        self.CVM = None
        self.LB = None
        self.CDB = None
        self.Cmem = None
        self.CTSDB = None
        self.MariaDB = None
        self.SQLServer = None
        self.Postgres = None
        self.NAS = None
        self.Greenplumn = None
        self.Ckafka = None
        self.Grocery = None
        self.HSM = None
        self.Tcaplus = None
        self.Cnas = None
        self.TiDB = None
        self.Emr = None
        self.SEAL = None
        self.CFS = None
        self.Oracle = None
        self.ElasticSearch = None
        self.TBaaS = None
        self.Itop = None
        self.DBAudit = None
        self.CynosDBPostgres = None
        self.Redis = None
        self.MongoDB = None
        self.DCDB = None
        self.CynosDBMySQL = None
        self.Subnet = None
        self.RouteTable = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.SubnetId = params.get("SubnetId")
        self.Classiclink = params.get("Classiclink")
        self.Dcg = params.get("Dcg")
        self.Pcx = params.get("Pcx")
        self.Ip = params.get("Ip")
        self.Nat = params.get("Nat")
        self.Vpngw = params.get("Vpngw")
        self.FlowLog = params.get("FlowLog")
        self.NetworkDetect = params.get("NetworkDetect")
        self.NetworkACL = params.get("NetworkACL")
        self.CVM = params.get("CVM")
        self.LB = params.get("LB")
        self.CDB = params.get("CDB")
        self.Cmem = params.get("Cmem")
        self.CTSDB = params.get("CTSDB")
        self.MariaDB = params.get("MariaDB")
        self.SQLServer = params.get("SQLServer")
        self.Postgres = params.get("Postgres")
        self.NAS = params.get("NAS")
        self.Greenplumn = params.get("Greenplumn")
        self.Ckafka = params.get("Ckafka")
        self.Grocery = params.get("Grocery")
        self.HSM = params.get("HSM")
        self.Tcaplus = params.get("Tcaplus")
        self.Cnas = params.get("Cnas")
        self.TiDB = params.get("TiDB")
        self.Emr = params.get("Emr")
        self.SEAL = params.get("SEAL")
        self.CFS = params.get("CFS")
        self.Oracle = params.get("Oracle")
        self.ElasticSearch = params.get("ElasticSearch")
        self.TBaaS = params.get("TBaaS")
        self.Itop = params.get("Itop")
        self.DBAudit = params.get("DBAudit")
        self.CynosDBPostgres = params.get("CynosDBPostgres")
        self.Redis = params.get("Redis")
        self.MongoDB = params.get("MongoDB")
        self.DCDB = params.get("DCDB")
        self.CynosDBMySQL = params.get("CynosDBMySQL")
        self.Subnet = params.get("Subnet")
        self.RouteTable = params.get("RouteTable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Route(AbstractModel):
    """路由策略对象

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的网段，取值不能在私有网络网段内，例如：112.20.51.0/24。\n        :type DestinationCidrBlock: str\n        :param GatewayType: 下一跳类型，目前我们支持的类型有：
CVM：公网网关类型的云服务器；
VPN：VPN网关；
DIRECTCONNECT：专线网关；
PEERCONNECTION：对等连接；
HAVIP：高可用虚拟IP；
NAT：NAT网关; 
NORMAL_CVM：普通云服务器；
EIP：云服务器的公网IP；
LOCAL_GATEWAY：本地网关。\n        :type GatewayType: str\n        :param GatewayId: 下一跳地址，这里只需要指定不同下一跳类型的网关ID，系统会自动匹配到下一跳地址。
特别注意：当 GatewayType 为 EIP 时，GatewayId 固定值 '0'\n        :type GatewayId: str\n        :param RouteId: 路由策略ID。IPv4路由策略ID是有意义的值，IPv6路由策略是无意义的值0。后续建议完全使用字符串唯一ID `RouteItemId`操作路由策略。
该字段在删除时必填，其他字段无需填写。\n        :type RouteId: int\n        :param RouteDescription: 路由策略描述。\n        :type RouteDescription: str\n        :param Enabled: 是否启用\n        :type Enabled: bool\n        :param RouteType: 路由类型，目前我们支持的类型有：
USER：用户路由；
NETD：网络探测路由，创建网络探测实例时，系统默认下发，不可编辑与删除；
CCN：云联网路由，系统默认下发，不可编辑与删除。
用户只能添加和操作 USER 类型的路由。\n        :type RouteType: str\n        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param DestinationIpv6CidrBlock: 目的IPv6网段，取值不能在私有网络网段内，例如：2402:4e00:1000:810b::/64。\n        :type DestinationIpv6CidrBlock: str\n        :param RouteItemId: 路由唯一策略ID。\n        :type RouteItemId: str\n        :param PublishedToVbc: 路由策略是否发布到云联网。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PublishedToVbc: bool\n        :param CreatedTime: 路由策略创建时间\n        :type CreatedTime: str\n        """
        self.DestinationCidrBlock = None
        self.GatewayType = None
        self.GatewayId = None
        self.RouteId = None
        self.RouteDescription = None
        self.Enabled = None
        self.RouteType = None
        self.RouteTableId = None
        self.DestinationIpv6CidrBlock = None
        self.RouteItemId = None
        self.PublishedToVbc = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.GatewayType = params.get("GatewayType")
        self.GatewayId = params.get("GatewayId")
        self.RouteId = params.get("RouteId")
        self.RouteDescription = params.get("RouteDescription")
        self.Enabled = params.get("Enabled")
        self.RouteType = params.get("RouteType")
        self.RouteTableId = params.get("RouteTableId")
        self.DestinationIpv6CidrBlock = params.get("DestinationIpv6CidrBlock")
        self.RouteItemId = params.get("RouteItemId")
        self.PublishedToVbc = params.get("PublishedToVbc")
        self.CreatedTime = params.get("CreatedTime")
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
        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param DestinationCidrBlock: 要检查的与之冲突的目的端\n        :type DestinationCidrBlock: str\n        :param ConflictSet: 冲突的路由策略列表\n        :type ConflictSet: list of Route\n        """
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
    """路由表对象

    """

    def __init__(self):
        """
        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param RouteTableId: 路由表实例ID，例如：rtb-azd4dt1c。\n        :type RouteTableId: str\n        :param RouteTableName: 路由表名称。\n        :type RouteTableName: str\n        :param AssociationSet: 路由表关联关系。\n        :type AssociationSet: list of RouteTableAssociation\n        :param RouteSet: IPv4路由策略集合。\n        :type RouteSet: list of Route\n        :param Main: 是否默认路由表。\n        :type Main: bool\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        :param LocalCidrForCcn: local路由是否发布云联网。
注意：此字段可能返回 null，表示取不到有效值。\n        :type LocalCidrForCcn: list of CidrForCcn\n        """
        self.VpcId = None
        self.RouteTableId = None
        self.RouteTableName = None
        self.AssociationSet = None
        self.RouteSet = None
        self.Main = None
        self.CreatedTime = None
        self.TagSet = None
        self.LocalCidrForCcn = None


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
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("LocalCidrForCcn") is not None:
            self.LocalCidrForCcn = []
            for item in params.get("LocalCidrForCcn"):
                obj = CidrForCcn()
                obj._deserialize(item)
                self.LocalCidrForCcn.append(obj)
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
        :param SubnetId: 子网实例ID。\n        :type SubnetId: str\n        :param RouteTableId: 路由表实例ID。\n        :type RouteTableId: str\n        """
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
        


class SecurityGroup(AbstractModel):
    """安全组对象

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID，例如：sg-ohuuioma。\n        :type SecurityGroupId: str\n        :param SecurityGroupName: 安全组名称，可任意命名，但不得超过60个字符。\n        :type SecurityGroupName: str\n        :param SecurityGroupDesc: 安全组备注，最多100个字符。\n        :type SecurityGroupDesc: str\n        :param ProjectId: 项目id，默认0。可在qcloud控制台项目管理页面查询到。\n        :type ProjectId: str\n        :param IsDefault: 是否是默认安全组，默认安全组不支持删除。\n        :type IsDefault: bool\n        :param CreatedTime: 安全组创建时间。\n        :type CreatedTime: str\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        """
        self.SecurityGroupId = None
        self.SecurityGroupName = None
        self.SecurityGroupDesc = None
        self.ProjectId = None
        self.IsDefault = None
        self.CreatedTime = None
        self.TagSet = None


    def _deserialize(self, params):
        self.SecurityGroupId = params.get("SecurityGroupId")
        self.SecurityGroupName = params.get("SecurityGroupName")
        self.SecurityGroupDesc = params.get("SecurityGroupDesc")
        self.ProjectId = params.get("ProjectId")
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
    """安全组关联的实例统计

    """

    def __init__(self):
        """
        :param SecurityGroupId: 安全组实例ID。\n        :type SecurityGroupId: str\n        :param CVM: 云服务器实例数。\n        :type CVM: int\n        :param CDB: MySQL数据库实例数。\n        :type CDB: int\n        :param ENI: 弹性网卡实例数。\n        :type ENI: int\n        :param SG: 被安全组引用数。\n        :type SG: int\n        :param CLB: 负载均衡实例数。\n        :type CLB: int\n        :param InstanceStatistics: 全量实例的绑定统计。\n        :type InstanceStatistics: list of InstanceStatistic\n        :param TotalCount: 所有资源的总计数（不包含被安全组引用数）。\n        :type TotalCount: int\n        """
        self.SecurityGroupId = None
        self.CVM = None
        self.CDB = None
        self.ENI = None
        self.SG = None
        self.CLB = None
        self.InstanceStatistics = None
        self.TotalCount = None


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
        self.TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupLimitSet(AbstractModel):
    """用户安全组配额限制。

    """

    def __init__(self):
        """
        :param SecurityGroupLimit: 每个项目每个地域可创建安全组数\n        :type SecurityGroupLimit: int\n        :param SecurityGroupPolicyLimit: 安全组下的最大规则数\n        :type SecurityGroupPolicyLimit: int\n        :param ReferedSecurityGroupLimit: 安全组下嵌套安全组规则数\n        :type ReferedSecurityGroupLimit: int\n        :param SecurityGroupInstanceLimit: 单安全组关联实例数\n        :type SecurityGroupInstanceLimit: int\n        :param InstanceSecurityGroupLimit: 实例关联安全组数\n        :type InstanceSecurityGroupLimit: int\n        """
        self.SecurityGroupLimit = None
        self.SecurityGroupPolicyLimit = None
        self.ReferedSecurityGroupLimit = None
        self.SecurityGroupInstanceLimit = None
        self.InstanceSecurityGroupLimit = None


    def _deserialize(self, params):
        self.SecurityGroupLimit = params.get("SecurityGroupLimit")
        self.SecurityGroupPolicyLimit = params.get("SecurityGroupPolicyLimit")
        self.ReferedSecurityGroupLimit = params.get("ReferedSecurityGroupLimit")
        self.SecurityGroupInstanceLimit = params.get("SecurityGroupInstanceLimit")
        self.InstanceSecurityGroupLimit = params.get("InstanceSecurityGroupLimit")
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
        :param PolicyIndex: 安全组规则索引号，值会随着安全组规则的变更动态变化。使用PolicyIndex时，请先调用`DescribeSecurityGroupPolicies`获取到规则的PolicyIndex，并且结合返回值中的Version一起使用处理规则。\n        :type PolicyIndex: int\n        :param Protocol: 协议, 取值: TCP,UDP,ICMP,ICMPv6,ALL。\n        :type Protocol: str\n        :param Port: 端口(all, 离散port,  range)。\n        :type Port: str\n        :param ServiceTemplate: 协议端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。\n        :type ServiceTemplate: :class:`tencentcloud.vpc.v20170312.models.ServiceTemplateSpecification`\n        :param CidrBlock: 网段或IP(互斥)。\n        :type CidrBlock: str\n        :param Ipv6CidrBlock: 网段或IPv6(互斥)。\n        :type Ipv6CidrBlock: str\n        :param SecurityGroupId: 安全组实例ID，例如：sg-ohuuioma。\n        :type SecurityGroupId: str\n        :param AddressTemplate: IP地址ID或者ID地址组ID。\n        :type AddressTemplate: :class:`tencentcloud.vpc.v20170312.models.AddressTemplateSpecification`\n        :param Action: ACCEPT 或 DROP。\n        :type Action: str\n        :param PolicyDescription: 安全组规则描述。\n        :type PolicyDescription: str\n        :param ModifyTime: 安全组最近修改时间。\n        :type ModifyTime: str\n        """
        self.PolicyIndex = None
        self.Protocol = None
        self.Port = None
        self.ServiceTemplate = None
        self.CidrBlock = None
        self.Ipv6CidrBlock = None
        self.SecurityGroupId = None
        self.AddressTemplate = None
        self.Action = None
        self.PolicyDescription = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyIndex = params.get("PolicyIndex")
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self.ServiceTemplate = ServiceTemplateSpecification()
            self.ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self.SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self.AddressTemplate = AddressTemplateSpecification()
            self.AddressTemplate._deserialize(params.get("AddressTemplate"))
        self.Action = params.get("Action")
        self.PolicyDescription = params.get("PolicyDescription")
        self.ModifyTime = params.get("ModifyTime")
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
        :param Version: 安全组规则当前版本。用户每次更新安全规则版本会自动加1，防止更新的路由规则已过期，不填不考虑冲突。\n        :type Version: str\n        :param Egress: 出站规则。\n        :type Egress: list of SecurityGroupPolicy\n        :param Ingress: 入站规则。\n        :type Ingress: list of SecurityGroupPolicy\n        """
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
        


class SecurityPolicyDatabase(AbstractModel):
    """SecurityPolicyDatabase策略

    """

    def __init__(self):
        """
        :param LocalCidrBlock: 本端网段\n        :type LocalCidrBlock: str\n        :param RemoteCidrBlock: 对端网段\n        :type RemoteCidrBlock: list of str\n        """
        self.LocalCidrBlock = None
        self.RemoteCidrBlock = None


    def _deserialize(self, params):
        self.LocalCidrBlock = params.get("LocalCidrBlock")
        self.RemoteCidrBlock = params.get("RemoteCidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplate(AbstractModel):
    """协议端口模板

    """

    def __init__(self):
        """
        :param ServiceTemplateId: 协议端口实例ID，例如：ppm-f5n1f8da。\n        :type ServiceTemplateId: str\n        :param ServiceTemplateName: 模板名称。\n        :type ServiceTemplateName: str\n        :param ServiceSet: 协议端口信息。\n        :type ServiceSet: list of str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        """
        self.ServiceTemplateId = None
        self.ServiceTemplateName = None
        self.ServiceSet = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ServiceTemplateId = params.get("ServiceTemplateId")
        self.ServiceTemplateName = params.get("ServiceTemplateName")
        self.ServiceSet = params.get("ServiceSet")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateGroup(AbstractModel):
    """协议端口模板集合

    """

    def __init__(self):
        """
        :param ServiceTemplateGroupId: 协议端口模板集合实例ID，例如：ppmg-2klmrefu。\n        :type ServiceTemplateGroupId: str\n        :param ServiceTemplateGroupName: 协议端口模板集合名称。\n        :type ServiceTemplateGroupName: str\n        :param ServiceTemplateIdSet: 协议端口模板实例ID。\n        :type ServiceTemplateIdSet: list of str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param ServiceTemplateSet: 协议端口模板实例信息。\n        :type ServiceTemplateSet: list of ServiceTemplate\n        """
        self.ServiceTemplateGroupId = None
        self.ServiceTemplateGroupName = None
        self.ServiceTemplateIdSet = None
        self.CreatedTime = None
        self.ServiceTemplateSet = None


    def _deserialize(self, params):
        self.ServiceTemplateGroupId = params.get("ServiceTemplateGroupId")
        self.ServiceTemplateGroupName = params.get("ServiceTemplateGroupName")
        self.ServiceTemplateIdSet = params.get("ServiceTemplateIdSet")
        self.CreatedTime = params.get("CreatedTime")
        if params.get("ServiceTemplateSet") is not None:
            self.ServiceTemplateSet = []
            for item in params.get("ServiceTemplateSet"):
                obj = ServiceTemplate()
                obj._deserialize(item)
                self.ServiceTemplateSet.append(obj)
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
        :param ServiceId: 协议端口ID，例如：ppm-f5n1f8da。\n        :type ServiceId: str\n        :param ServiceGroupId: 协议端口组ID，例如：ppmg-f5n1f8da。\n        :type ServiceGroupId: str\n        """
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
        


class SetCcnRegionBandwidthLimitsRequest(AbstractModel):
    """SetCcnRegionBandwidthLimits请求参数结构体

    """

    def __init__(self):
        """
        :param CcnId: CCN实例ID。形如：ccn-f49l6u0z。\n        :type CcnId: str\n        :param CcnRegionBandwidthLimits: 云联网（CCN）各地域出带宽上限。\n        :type CcnRegionBandwidthLimits: list of CcnRegionBandwidthLimit\n        :param SetDefaultLimitFlag: 是否恢复云联网地域出口/地域间带宽限速为默认值（1Gbps）。false表示不恢复；true表示恢复。恢复默认值后，限速实例将不在控制台展示。该参数默认为 false，不恢复。\n        :type SetDefaultLimitFlag: bool\n        """
        self.CcnId = None
        self.CcnRegionBandwidthLimits = None
        self.SetDefaultLimitFlag = None


    def _deserialize(self, params):
        self.CcnId = params.get("CcnId")
        if params.get("CcnRegionBandwidthLimits") is not None:
            self.CcnRegionBandwidthLimits = []
            for item in params.get("CcnRegionBandwidthLimits"):
                obj = CcnRegionBandwidthLimit()
                obj._deserialize(item)
                self.CcnRegionBandwidthLimits.append(obj)
        self.SetDefaultLimitFlag = params.get("SetDefaultLimitFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetCcnRegionBandwidthLimitsResponse(AbstractModel):
    """SetCcnRegionBandwidthLimits返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SourceIpTranslationNatRule(AbstractModel):
    """NAT的SNAT规则

    """

    def __init__(self):
        """
        :param ResourceId: 资源ID\n        :type ResourceId: str\n        :param ResourceType: 资源类型，目前包含SUBNET、NETWORKINTERFACE
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResourceType: str\n        :param PrivateIpAddress: 源IP/网段\n        :type PrivateIpAddress: str\n        :param PublicIpAddresses: 弹性IP地址池\n        :type PublicIpAddresses: list of str\n        :param Description: 描述\n        :type Description: str\n        :param NatGatewaySnatId: Snat规则ID\n        :type NatGatewaySnatId: str\n        :param NatGatewayId: NAT网关的ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type NatGatewayId: str\n        :param VpcId: 私有网络VPC的ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VpcId: str\n        :param CreatedTime: NAT网关SNAT规则创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreatedTime: str\n        """
        self.ResourceId = None
        self.ResourceType = None
        self.PrivateIpAddress = None
        self.PublicIpAddresses = None
        self.Description = None
        self.NatGatewaySnatId = None
        self.NatGatewayId = None
        self.VpcId = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.ResourceType = params.get("ResourceType")
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.PublicIpAddresses = params.get("PublicIpAddresses")
        self.Description = params.get("Description")
        self.NatGatewaySnatId = params.get("NatGatewaySnatId")
        self.NatGatewayId = params.get("NatGatewayId")
        self.VpcId = params.get("VpcId")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Subnet(AbstractModel):
    """子网对象

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`。\n        :type VpcId: str\n        :param SubnetId: 子网实例`ID`，例如：subnet-bthucmmy。\n        :type SubnetId: str\n        :param SubnetName: 子网名称。\n        :type SubnetName: str\n        :param CidrBlock: 子网的 `IPv4` `CIDR`。\n        :type CidrBlock: str\n        :param IsDefault: 是否默认子网。\n        :type IsDefault: bool\n        :param EnableBroadcast: 是否开启广播。\n        :type EnableBroadcast: bool\n        :param Zone: 可用区。\n        :type Zone: str\n        :param RouteTableId: 路由表实例ID，例如：rtb-l2h8d7c2。\n        :type RouteTableId: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param AvailableIpAddressCount: 可用`IPv4`数。\n        :type AvailableIpAddressCount: int\n        :param Ipv6CidrBlock: 子网的 `IPv6` `CIDR`。\n        :type Ipv6CidrBlock: str\n        :param NetworkAclId: 关联`ACL`ID\n        :type NetworkAclId: str\n        :param IsRemoteVpcSnat: 是否为 `SNAT` 地址池子网。\n        :type IsRemoteVpcSnat: bool\n        :param TotalIpAddressCount: 子网`IPv4`总数。\n        :type TotalIpAddressCount: int\n        :param TagSet: 标签键值对。\n        :type TagSet: list of Tag\n        :param CdcId: CDC实例ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CdcId: str\n        :param IsCdcSubnet: 是否是CDC所属子网。0:否 1:是
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsCdcSubnet: int\n        """
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
        self.NetworkAclId = None
        self.IsRemoteVpcSnat = None
        self.TotalIpAddressCount = None
        self.TagSet = None
        self.CdcId = None
        self.IsCdcSubnet = None


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
        self.NetworkAclId = params.get("NetworkAclId")
        self.IsRemoteVpcSnat = params.get("IsRemoteVpcSnat")
        self.TotalIpAddressCount = params.get("TotalIpAddressCount")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = Tag()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.CdcId = params.get("CdcId")
        self.IsCdcSubnet = params.get("IsCdcSubnet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubnetInput(AbstractModel):
    """子网对象

    """

    def __init__(self):
        """
        :param CidrBlock: 子网的`CIDR`。\n        :type CidrBlock: str\n        :param SubnetName: 子网名称。\n        :type SubnetName: str\n        :param Zone: 可用区。形如：`ap-guangzhou-2`。\n        :type Zone: str\n        :param RouteTableId: 指定关联路由表，形如：`rtb-3ryrwzuu`。\n        :type RouteTableId: str\n        """
        self.CidrBlock = None
        self.SubnetName = None
        self.Zone = None
        self.RouteTableId = None


    def _deserialize(self, params):
        self.CidrBlock = params.get("CidrBlock")
        self.SubnetName = params.get("SubnetName")
        self.Zone = params.get("Zone")
        self.RouteTableId = params.get("RouteTableId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        """
        :param Key: 标签键
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param Value: 标签值
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
        


class TemplateLimit(AbstractModel):
    """参数模板配额

    """

    def __init__(self):
        """
        :param AddressTemplateMemberLimit: 参数模板IP地址成员配额。\n        :type AddressTemplateMemberLimit: int\n        :param AddressTemplateGroupMemberLimit: 参数模板IP地址组成员配额。\n        :type AddressTemplateGroupMemberLimit: int\n        :param ServiceTemplateMemberLimit: 参数模板I协议端口成员配额。\n        :type ServiceTemplateMemberLimit: int\n        :param ServiceTemplateGroupMemberLimit: 参数模板协议端口组成员配额。\n        :type ServiceTemplateGroupMemberLimit: int\n        """
        self.AddressTemplateMemberLimit = None
        self.AddressTemplateGroupMemberLimit = None
        self.ServiceTemplateMemberLimit = None
        self.ServiceTemplateGroupMemberLimit = None


    def _deserialize(self, params):
        self.AddressTemplateMemberLimit = params.get("AddressTemplateMemberLimit")
        self.AddressTemplateGroupMemberLimit = params.get("AddressTemplateGroupMemberLimit")
        self.ServiceTemplateMemberLimit = params.get("ServiceTemplateMemberLimit")
        self.ServiceTemplateGroupMemberLimit = params.get("ServiceTemplateGroupMemberLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformAddressRequest(AbstractModel):
    """TransformAddress请求参数结构体

    """

    def __init__(self):
        """
        :param InstanceId: 待操作有普通公网 IP 的实例 ID。实例 ID 形如：`ins-11112222`。可通过登录[控制台](https://console.cloud.tencent.com/cvm)查询，也可通过 [DescribeInstances](https://cloud.tencent.com/document/api/213/9389) 接口返回值中的`InstanceId`获取。\n        :type InstanceId: str\n        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransformAddressResponse(AbstractModel):
    """TransformAddress返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6AddressesRequest(AbstractModel):
    """UnassignIpv6Addresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例`ID`，形如：`eni-m6dyj72l`。\n        :type NetworkInterfaceId: str\n        :param Ipv6Addresses: 指定的`IPv6`地址列表，单次最多指定10个。\n        :type Ipv6Addresses: list of Ipv6Address\n        """
        self.NetworkInterfaceId = None
        self.Ipv6Addresses = None


    def _deserialize(self, params):
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
        


class UnassignIpv6AddressesResponse(AbstractModel):
    """UnassignIpv6Addresses返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6CidrBlockRequest(AbstractModel):
    """UnassignIpv6CidrBlock请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: `VPC`实例`ID`，形如：`vpc-f49l6u0z`。\n        :type VpcId: str\n        :param Ipv6CidrBlock: `IPv6`网段。形如：`3402:4e00:20:1000::/56`\n        :type Ipv6CidrBlock: str\n        """
        self.VpcId = None
        self.Ipv6CidrBlock = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        self.Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignIpv6CidrBlockResponse(AbstractModel):
    """UnassignIpv6CidrBlock返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignIpv6SubnetCidrBlockRequest(AbstractModel):
    """UnassignIpv6SubnetCidrBlock请求参数结构体

    """

    def __init__(self):
        """
        :param VpcId: 子网所在私有网络`ID`。形如：`vpc-f49l6u0z`。\n        :type VpcId: str\n        :param Ipv6SubnetCidrBlocks: `IPv6` 子网段列表。\n        :type Ipv6SubnetCidrBlocks: list of Ipv6SubnetCidrBlock\n        """
        self.VpcId = None
        self.Ipv6SubnetCidrBlocks = None


    def _deserialize(self, params):
        self.VpcId = params.get("VpcId")
        if params.get("Ipv6SubnetCidrBlocks") is not None:
            self.Ipv6SubnetCidrBlocks = []
            for item in params.get("Ipv6SubnetCidrBlocks"):
                obj = Ipv6SubnetCidrBlock()
                obj._deserialize(item)
                self.Ipv6SubnetCidrBlocks.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignIpv6SubnetCidrBlockResponse(AbstractModel):
    """UnassignIpv6SubnetCidrBlock返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UnassignPrivateIpAddressesRequest(AbstractModel):
    """UnassignPrivateIpAddresses请求参数结构体

    """

    def __init__(self):
        """
        :param NetworkInterfaceId: 弹性网卡实例ID，例如：eni-m6dyj72l。\n        :type NetworkInterfaceId: str\n        :param PrivateIpAddresses: 指定的内网IP信息，单次最多指定10个。\n        :type PrivateIpAddresses: list of PrivateIpAddressSpecification\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UnassignPrivateIpAddressesResponse(AbstractModel):
    """UnassignPrivateIpAddresses返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Vpc(AbstractModel):
    """私有网络(VPC)对象。

    """

    def __init__(self):
        """
        :param VpcName: `VPC`名称。\n        :type VpcName: str\n        :param VpcId: `VPC`实例`ID`，例如：vpc-azd4dt1c。\n        :type VpcId: str\n        :param CidrBlock: `VPC`的`IPv4` `CIDR`。\n        :type CidrBlock: str\n        :param IsDefault: 是否默认`VPC`。\n        :type IsDefault: bool\n        :param EnableMulticast: 是否开启组播。\n        :type EnableMulticast: bool\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param DnsServerSet: `DNS`列表。\n        :type DnsServerSet: list of str\n        :param DomainName: `DHCP`域名选项值。\n        :type DomainName: str\n        :param DhcpOptionsId: `DHCP`选项集`ID`。\n        :type DhcpOptionsId: str\n        :param EnableDhcp: 是否开启`DHCP`。\n        :type EnableDhcp: bool\n        :param Ipv6CidrBlock: `VPC`的`IPv6` `CIDR`。\n        :type Ipv6CidrBlock: str\n        :param TagSet: 标签键值对\n        :type TagSet: list of Tag\n        :param AssistantCidrSet: 辅助CIDR
注意：此字段可能返回 null，表示取不到有效值。\n        :type AssistantCidrSet: list of AssistantCidr\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcEndPointServiceUser(AbstractModel):
    """终端节点服务的服务白名单对象详情。

    """

    def __init__(self):
        """
        :param Owner: AppId。\n        :type Owner: int\n        :param UserUin: Uin。\n        :type UserUin: str\n        :param Description: 描述信息。\n        :type Description: str\n        :param CreateTime: 创建时间。\n        :type CreateTime: str\n        :param EndPointServiceId: 终端节点服务ID。\n        :type EndPointServiceId: str\n        """
        self.Owner = None
        self.UserUin = None
        self.Description = None
        self.CreateTime = None
        self.EndPointServiceId = None


    def _deserialize(self, params):
        self.Owner = params.get("Owner")
        self.UserUin = params.get("UserUin")
        self.Description = params.get("Description")
        self.CreateTime = params.get("CreateTime")
        self.EndPointServiceId = params.get("EndPointServiceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcIpv6Address(AbstractModel):
    """VPC内网IPv6对象。

    """

    def __init__(self):
        """
        :param Ipv6Address: `VPC`内`IPv6`地址。\n        :type Ipv6Address: str\n        :param CidrBlock: 所属子网 `IPv6` `CIDR`。\n        :type CidrBlock: str\n        :param Ipv6AddressType: `IPv6`类型。\n        :type Ipv6AddressType: str\n        :param CreatedTime: `IPv6`申请时间。\n        :type CreatedTime: str\n        """
        self.Ipv6Address = None
        self.CidrBlock = None
        self.Ipv6AddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.Ipv6Address = params.get("Ipv6Address")
        self.CidrBlock = params.get("CidrBlock")
        self.Ipv6AddressType = params.get("Ipv6AddressType")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcLimit(AbstractModel):
    """私有网络配额

    """

    def __init__(self):
        """
        :param LimitType: 私有网络配额描述\n        :type LimitType: str\n        :param LimitValue: 私有网络配额值\n        :type LimitValue: int\n        """
        self.LimitType = None
        self.LimitValue = None


    def _deserialize(self, params):
        self.LimitType = params.get("LimitType")
        self.LimitValue = params.get("LimitValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcPrivateIpAddress(AbstractModel):
    """VPC内网IP对象。

    """

    def __init__(self):
        """
        :param PrivateIpAddress: `VPC`内网`IP`。\n        :type PrivateIpAddress: str\n        :param CidrBlock: 所属子网`CIDR`。\n        :type CidrBlock: str\n        :param PrivateIpAddressType: 内网`IP`类型。\n        :type PrivateIpAddressType: str\n        :param CreatedTime: `IP`申请时间。\n        :type CreatedTime: str\n        """
        self.PrivateIpAddress = None
        self.CidrBlock = None
        self.PrivateIpAddressType = None
        self.CreatedTime = None


    def _deserialize(self, params):
        self.PrivateIpAddress = params.get("PrivateIpAddress")
        self.CidrBlock = params.get("CidrBlock")
        self.PrivateIpAddressType = params.get("PrivateIpAddressType")
        self.CreatedTime = params.get("CreatedTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnConnection(AbstractModel):
    """VPN通道对象。

    """

    def __init__(self):
        """
        :param VpnConnectionId: 通道实例ID。\n        :type VpnConnectionId: str\n        :param VpnConnectionName: 通道名称。\n        :type VpnConnectionName: str\n        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param VpnGatewayId: VPN网关实例ID。\n        :type VpnGatewayId: str\n        :param CustomerGatewayId: 对端网关实例ID。\n        :type CustomerGatewayId: str\n        :param PreShareKey: 预共享密钥。\n        :type PreShareKey: str\n        :param VpnProto: 通道传输协议。\n        :type VpnProto: str\n        :param EncryptProto: 通道加密协议。\n        :type EncryptProto: str\n        :param RouteType: 路由类型。\n        :type RouteType: str\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param State: 通道的生产状态，PENDING：生产中，AVAILABLE：运行中，DELETING：删除中。\n        :type State: str\n        :param NetStatus: 通道连接状态，AVAILABLE：已连接。\n        :type NetStatus: str\n        :param SecurityPolicyDatabaseSet: SPD。\n        :type SecurityPolicyDatabaseSet: list of SecurityPolicyDatabase\n        :param IKEOptionsSpecification: IKE选项。\n        :type IKEOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IKEOptionsSpecification`\n        :param IPSECOptionsSpecification: IPSEC选择。\n        :type IPSECOptionsSpecification: :class:`tencentcloud.vpc.v20170312.models.IPSECOptionsSpecification`\n        :param EnableHealthCheck: 是否支持健康状态探测\n        :type EnableHealthCheck: bool\n        :param HealthCheckLocalIp: 本端探测ip\n        :type HealthCheckLocalIp: str\n        :param HealthCheckRemoteIp: 对端探测ip\n        :type HealthCheckRemoteIp: str\n        :param HealthCheckStatus: 通道健康检查状态，AVAILABLE：正常，UNAVAILABLE：不正常。 未配置健康检查不返回该对象\n        :type HealthCheckStatus: str\n        """
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
        self.EnableHealthCheck = None
        self.HealthCheckLocalIp = None
        self.HealthCheckRemoteIp = None
        self.HealthCheckStatus = None


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
        self.EnableHealthCheck = params.get("EnableHealthCheck")
        self.HealthCheckLocalIp = params.get("HealthCheckLocalIp")
        self.HealthCheckRemoteIp = params.get("HealthCheckRemoteIp")
        self.HealthCheckStatus = params.get("HealthCheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGateway(AbstractModel):
    """VPN网关对象。

    """

    def __init__(self):
        """
        :param VpnGatewayId: 网关实例ID。\n        :type VpnGatewayId: str\n        :param VpcId: VPC实例ID。\n        :type VpcId: str\n        :param VpnGatewayName: 网关实例名称。\n        :type VpnGatewayName: str\n        :param Type: 网关实例类型：'IPSEC', 'SSL','CCN'。\n        :type Type: str\n        :param State: 网关实例状态， 'PENDING'：生产中，'DELETING'：删除中，'AVAILABLE'：运行中。\n        :type State: str\n        :param PublicIpAddress: 网关公网IP。\n        :type PublicIpAddress: str\n        :param RenewFlag: 网关续费类型：'NOTIFY_AND_MANUAL_RENEW'：手动续费，'NOTIFY_AND_AUTO_RENEW'：自动续费，'NOT_NOTIFY_AND_NOT_RENEW'：到期不续费。\n        :type RenewFlag: str\n        :param InstanceChargeType: 网关付费类型：POSTPAID_BY_HOUR：按小时后付费，PREPAID：包年包月预付费，\n        :type InstanceChargeType: str\n        :param InternetMaxBandwidthOut: 网关出带宽。\n        :type InternetMaxBandwidthOut: int\n        :param CreatedTime: 创建时间。\n        :type CreatedTime: str\n        :param ExpiredTime: 预付费网关过期时间。\n        :type ExpiredTime: str\n        :param IsAddressBlocked: 公网IP是否被封堵。\n        :type IsAddressBlocked: bool\n        :param NewPurchasePlan: 计费模式变更，PREPAID_TO_POSTPAID：包年包月预付费到期转按小时后付费。\n        :type NewPurchasePlan: str\n        :param RestrictState: 网关计费装，PROTECTIVELY_ISOLATED：被安全隔离的实例，NORMAL：正常。\n        :type RestrictState: str\n        :param Zone: 可用区，如：ap-guangzhou-2\n        :type Zone: str\n        :param VpnGatewayQuotaSet: 网关带宽配额信息\n        :type VpnGatewayQuotaSet: list of VpnGatewayQuota\n        :param Version: 网关实例版本信息\n        :type Version: str\n        :param NetworkInstanceId: Type值为CCN时，该值表示云联网实例ID\n        :type NetworkInstanceId: str\n        """
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
        self.VpnGatewayQuotaSet = None
        self.Version = None
        self.NetworkInstanceId = None


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
        if params.get("VpnGatewayQuotaSet") is not None:
            self.VpnGatewayQuotaSet = []
            for item in params.get("VpnGatewayQuotaSet"):
                obj = VpnGatewayQuota()
                obj._deserialize(item)
                self.VpnGatewayQuotaSet.append(obj)
        self.Version = params.get("Version")
        self.NetworkInstanceId = params.get("NetworkInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGatewayQuota(AbstractModel):
    """VPN网关配额对象

    """

    def __init__(self):
        """
        :param Bandwidth: 带宽配额\n        :type Bandwidth: int\n        :param Cname: 配额中文名称\n        :type Cname: str\n        :param Name: 配额英文名称\n        :type Name: str\n        """
        self.Bandwidth = None
        self.Cname = None
        self.Name = None


    def _deserialize(self, params):
        self.Bandwidth = params.get("Bandwidth")
        self.Cname = params.get("Cname")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGatewayRoute(AbstractModel):
    """Vpn网关目的路由

    """

    def __init__(self):
        """
        :param DestinationCidrBlock: 目的端IDC网段\n        :type DestinationCidrBlock: str\n        :param InstanceType: 下一跳类型（关联实例类型）可选值:"VPNCONN"(VPN通道), "CCN"(CCN实例)\n        :type InstanceType: str\n        :param InstanceId: 下一跳实例ID\n        :type InstanceId: str\n        :param Priority: 优先级, 可选值: 0, 100\n        :type Priority: int\n        :param Status: 启用状态, 可选值: "ENABLE"(启用), "DISABLE"(禁用)\n        :type Status: str\n        :param RouteId: 路由条目ID\n        :type RouteId: str\n        :param Type: 路由类型, 可选值: "VPC"(VPC路由), "CCN"(云联网传播路由), "Static"(静态路由), "BGP"(BGP路由)\n        :type Type: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
        self.DestinationCidrBlock = None
        self.InstanceType = None
        self.InstanceId = None
        self.Priority = None
        self.Status = None
        self.RouteId = None
        self.Type = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.DestinationCidrBlock = params.get("DestinationCidrBlock")
        self.InstanceType = params.get("InstanceType")
        self.InstanceId = params.get("InstanceId")
        self.Priority = params.get("Priority")
        self.Status = params.get("Status")
        self.RouteId = params.get("RouteId")
        self.Type = params.get("Type")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpnGatewayRouteModify(AbstractModel):
    """修改VPN状态参数

    """

    def __init__(self):
        """
        :param RouteId: Vpn网关路由ID\n        :type RouteId: str\n        :param Status: Vpn网关状态, ENABEL 启用, DISABLE禁用\n        :type Status: str\n        """
        self.RouteId = None
        self.Status = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpngwCcnRoutes(AbstractModel):
    """VPN网关云联网路由信息

    """

    def __init__(self):
        """
        :param RouteId: 路由信息ID\n        :type RouteId: str\n        :param Status: 路由信息是否启用
ENABLE：启用该路由
DISABLE：不启用该路由\n        :type Status: str\n        """
        self.RouteId = None
        self.Status = None


    def _deserialize(self, params):
        self.RouteId = params.get("RouteId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawNotifyRoutesRequest(AbstractModel):
    """WithdrawNotifyRoutes请求参数结构体

    """

    def __init__(self):
        """
        :param RouteTableId: 路由表唯一ID。\n        :type RouteTableId: str\n        :param RouteItemIds: 路由策略唯一ID。\n        :type RouteItemIds: list of str\n        """
        self.RouteTableId = None
        self.RouteItemIds = None


    def _deserialize(self, params):
        self.RouteTableId = params.get("RouteTableId")
        self.RouteItemIds = params.get("RouteItemIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WithdrawNotifyRoutesResponse(AbstractModel):
    """WithdrawNotifyRoutes返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")