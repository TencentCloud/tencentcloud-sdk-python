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


class AclConfig(AbstractModel):
    """基于端口的acl策略

    """

    def __init__(self):
        r"""
        :param ForwardProtocol: 协议类型, 可取值tcp, udp, all
        :type ForwardProtocol: str
        :param DPortStart: 目的端口起始，可取值范围0~65535
        :type DPortStart: int
        :param DPortEnd: 目的端口结束，可取值范围0~65535
        :type DPortEnd: int
        :param SPortStart: 来源端口起始，可取值范围0~65535
        :type SPortStart: int
        :param SPortEnd: 来源端口结束，可取值范围0~65535
        :type SPortEnd: int
        :param Action: 动作，可取值：drop， transmit， forward
        :type Action: str
        :param Priority: 策略优先级，数字越小，级别越高，该规则越靠前匹配，取值1-1000
注意：此字段可能返回 null，表示取不到有效值。
        :type Priority: int
        """
        self.ForwardProtocol = None
        self.DPortStart = None
        self.DPortEnd = None
        self.SPortStart = None
        self.SPortEnd = None
        self.Action = None
        self.Priority = None


    def _deserialize(self, params):
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.DPortStart = params.get("DPortStart")
        self.DPortEnd = params.get("DPortEnd")
        self.SPortStart = params.get("SPortStart")
        self.SPortEnd = params.get("SPortEnd")
        self.Action = params.get("Action")
        self.Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfigRelation(AbstractModel):
    """端口acl策略配置与高防资源关联

    """

    def __init__(self):
        r"""
        :param AclConfig: acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        :param InstanceDetailList: 实例列表
        :type InstanceDetailList: list of InstanceRelation
        """
        self.AclConfig = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        if params.get("AclConfig") is not None:
            self.AclConfig = AclConfig()
            self.AclConfig._deserialize(params.get("AclConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnycastOutPackRelation(AbstractModel):
    """Anycast转外套餐详情

    """

    def __init__(self):
        r"""
        :param NormalBandwidth: 业务带宽(单位M)
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalBandwidth: int
        :param ForwardRulesLimit: 转发规则数
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardRulesLimit: int
        :param AutoRenewFlag: 自动续费标记
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param CurDeadline: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        """
        self.NormalBandwidth = None
        self.ForwardRulesLimit = None
        self.AutoRenewFlag = None
        self.CurDeadline = None


    def _deserialize(self, params):
        self.NormalBandwidth = params.get("NormalBandwidth")
        self.ForwardRulesLimit = params.get("ForwardRulesLimit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipAddressRequest(AbstractModel):
    """AssociateDDoSEipAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :type InstanceId: str
        :param Eip: 资源实例ID对应的高防弹性公网IP。
        :type Eip: str
        :param CvmInstanceID: 要绑定的实例 ID。实例 ID 形如：ins-11112222。可通过登录控制台查询，也可通过 DescribeInstances 接口返回值中的InstanceId获取。
        :type CvmInstanceID: str
        :param CvmRegion: cvm实例所在地域，例如：ap-hongkong。
        :type CvmRegion: str
        """
        self.InstanceId = None
        self.Eip = None
        self.CvmInstanceID = None
        self.CvmRegion = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Eip = params.get("Eip")
        self.CvmInstanceID = params.get("CvmInstanceID")
        self.CvmRegion = params.get("CvmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipAddressResponse(AbstractModel):
    """AssociateDDoSEipAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class AssociateDDoSEipLoadBalancerRequest(AbstractModel):
    """AssociateDDoSEipLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :type InstanceId: str
        :param Eip: 资源实例ID对应的高防弹性公网IP。
        :type Eip: str
        :param LoadBalancerID: 要绑定的负载均衡ID。负载均衡 ID 形如：lb-0000002i。可通过登录控制台查询，也可通过 DescribeLoadBalancers 接口返回值中的LoadBalancerId获取。
        :type LoadBalancerID: str
        :param LoadBalancerRegion: CLB所在地域，例如：ap-hongkong。
        :type LoadBalancerRegion: str
        :param Vip: CLB内网IP
        :type Vip: str
        """
        self.InstanceId = None
        self.Eip = None
        self.LoadBalancerID = None
        self.LoadBalancerRegion = None
        self.Vip = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Eip = params.get("Eip")
        self.LoadBalancerID = params.get("LoadBalancerID")
        self.LoadBalancerRegion = params.get("LoadBalancerRegion")
        self.Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipLoadBalancerResponse(AbstractModel):
    """AssociateDDoSEipLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BGPIPInstance(AbstractModel):
    """高防IP资产实例信息

    """

    def __init__(self):
        r"""
        :param InstanceDetail: 资产实例的详细信息
        :type InstanceDetail: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        :param SpecificationLimit: 资产实例的规格信息
        :type SpecificationLimit: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceSpecification`
        :param Usage: 资产实例的使用统计信息
        :type Usage: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceUsages`
        :param Region: 资产实例所在的地域
        :type Region: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        :param Status: 资产实例的防护状态，状态码如下：
"idle"：正常状态(无攻击)
"attacking"：攻击中
"blocking"：封堵中
"creating"：创建中
"deblocking"：解封中
"isolate"：回收隔离中
        :type Status: str
        :param ExpiredTime: 购买时间
        :type ExpiredTime: str
        :param CreatedTime: 到期时间
        :type CreatedTime: str
        :param Name: 资产实例的名称
        :type Name: str
        :param PackInfo: 资产实例所属的套餐包信息，
注意：当资产实例不是套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type PackInfo: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        :param StaticPackRelation: 资产实例所属的三网套餐包详情，
注意：当资产实例不是三网套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticPackRelation: :class:`tencentcloud.antiddos.v20200309.models.StaticPackRelation`
        :param ZoneId: 区分高防IP境外线路
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: int
        :param Tgw: 区分集群
注意：此字段可能返回 null，表示取不到有效值。
        :type Tgw: int
        :param EipAddressStatus: 高防弹性公网IP状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)。只对高防弹性公网IP实例有效。
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddressStatus: str
        :param EipFlag: 是否高防弹性公网IP实例，是为1，否为0。
注意：此字段可能返回 null，表示取不到有效值。
        :type EipFlag: int
        :param EipAddressPackRelation: 资产实例所属的高防弹性公网IP套餐包详情，
注意：当资产实例不是高防弹性公网IP套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddressPackRelation: :class:`tencentcloud.antiddos.v20200309.models.EipAddressPackRelation`
        :param EipAddressInfo: 高防弹性公网IP关联的实例信息。
注意：当资产实例不是高防弹性公网IP实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddressInfo: :class:`tencentcloud.antiddos.v20200309.models.EipAddressRelation`
        :param Domain: 建议客户接入的域名，客户可使用域名接入。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param DamDDoSStatus: 是否开启安全加速，是为1，否为0。
        :type DamDDoSStatus: int
        :param V6Flag: 是否Ipv6版本的IP, 是为1，否为0
注意：此字段可能返回 null，表示取不到有效值。
        :type V6Flag: int
        :param BGPIPChannelFlag: 是否渠道版高防IP，是为1，否为0
注意：此字段可能返回 null，表示取不到有效值。
        :type BGPIPChannelFlag: int
        :param TagInfoList: 资源关联标签
注意：此字段可能返回 null，表示取不到有效值。
        :type TagInfoList: list of TagInfo
        :param AnycastOutPackRelation: 资产实例所属的全力防护套餐包详情，
注意：当资产实例不是全力防护套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type AnycastOutPackRelation: :class:`tencentcloud.antiddos.v20200309.models.AnycastOutPackRelation`
        :param InstanceVersion: 资源实例版本
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceVersion: int
        """
        self.InstanceDetail = None
        self.SpecificationLimit = None
        self.Usage = None
        self.Region = None
        self.Status = None
        self.ExpiredTime = None
        self.CreatedTime = None
        self.Name = None
        self.PackInfo = None
        self.StaticPackRelation = None
        self.ZoneId = None
        self.Tgw = None
        self.EipAddressStatus = None
        self.EipFlag = None
        self.EipAddressPackRelation = None
        self.EipAddressInfo = None
        self.Domain = None
        self.DamDDoSStatus = None
        self.V6Flag = None
        self.BGPIPChannelFlag = None
        self.TagInfoList = None
        self.AnycastOutPackRelation = None
        self.InstanceVersion = None


    def _deserialize(self, params):
        if params.get("InstanceDetail") is not None:
            self.InstanceDetail = InstanceRelation()
            self.InstanceDetail._deserialize(params.get("InstanceDetail"))
        if params.get("SpecificationLimit") is not None:
            self.SpecificationLimit = BGPIPInstanceSpecification()
            self.SpecificationLimit._deserialize(params.get("SpecificationLimit"))
        if params.get("Usage") is not None:
            self.Usage = BGPIPInstanceUsages()
            self.Usage._deserialize(params.get("Usage"))
        if params.get("Region") is not None:
            self.Region = RegionInfo()
            self.Region._deserialize(params.get("Region"))
        self.Status = params.get("Status")
        self.ExpiredTime = params.get("ExpiredTime")
        self.CreatedTime = params.get("CreatedTime")
        self.Name = params.get("Name")
        if params.get("PackInfo") is not None:
            self.PackInfo = PackInfo()
            self.PackInfo._deserialize(params.get("PackInfo"))
        if params.get("StaticPackRelation") is not None:
            self.StaticPackRelation = StaticPackRelation()
            self.StaticPackRelation._deserialize(params.get("StaticPackRelation"))
        self.ZoneId = params.get("ZoneId")
        self.Tgw = params.get("Tgw")
        self.EipAddressStatus = params.get("EipAddressStatus")
        self.EipFlag = params.get("EipFlag")
        if params.get("EipAddressPackRelation") is not None:
            self.EipAddressPackRelation = EipAddressPackRelation()
            self.EipAddressPackRelation._deserialize(params.get("EipAddressPackRelation"))
        if params.get("EipAddressInfo") is not None:
            self.EipAddressInfo = EipAddressRelation()
            self.EipAddressInfo._deserialize(params.get("EipAddressInfo"))
        self.Domain = params.get("Domain")
        self.DamDDoSStatus = params.get("DamDDoSStatus")
        self.V6Flag = params.get("V6Flag")
        self.BGPIPChannelFlag = params.get("BGPIPChannelFlag")
        if params.get("TagInfoList") is not None:
            self.TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfoList.append(obj)
        if params.get("AnycastOutPackRelation") is not None:
            self.AnycastOutPackRelation = AnycastOutPackRelation()
            self.AnycastOutPackRelation._deserialize(params.get("AnycastOutPackRelation"))
        self.InstanceVersion = params.get("InstanceVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPInstanceSpecification(AbstractModel):
    """高防IP资产实例的规格信息

    """

    def __init__(self):
        r"""
        :param ProtectBandwidth: 保底防护峰值，单位Mbps
        :type ProtectBandwidth: int
        :param ProtectCCQPS: CC防护峰值，单位qps
        :type ProtectCCQPS: int
        :param NormalBandwidth: 正常业务带宽，单位Mbps
        :type NormalBandwidth: int
        :param ForwardRulesLimit: 转发规则数，单位条
        :type ForwardRulesLimit: int
        :param AutoRenewFlag: 自动续费状态，取值[
0：没有开启自动续费
1：开启了自动续费
]
        :type AutoRenewFlag: int
        :param Line: 高防IP线路，取值为[
1：BGP线路
2：电信
3：联通
4：移动
99：第三方合作线路
]
        :type Line: int
        :param ElasticBandwidth: 弹性防护峰值，单位Mbps
        :type ElasticBandwidth: int
        """
        self.ProtectBandwidth = None
        self.ProtectCCQPS = None
        self.NormalBandwidth = None
        self.ForwardRulesLimit = None
        self.AutoRenewFlag = None
        self.Line = None
        self.ElasticBandwidth = None


    def _deserialize(self, params):
        self.ProtectBandwidth = params.get("ProtectBandwidth")
        self.ProtectCCQPS = params.get("ProtectCCQPS")
        self.NormalBandwidth = params.get("NormalBandwidth")
        self.ForwardRulesLimit = params.get("ForwardRulesLimit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.Line = params.get("Line")
        self.ElasticBandwidth = params.get("ElasticBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPInstanceUsages(AbstractModel):
    """高防IP资产实例的使用信息统计

    """

    def __init__(self):
        r"""
        :param PortRulesUsage: 已使用的端口规则数，单位条
        :type PortRulesUsage: int
        :param DomainRulesUsage: 已使用的域名规则数，单位条
        :type DomainRulesUsage: int
        :param Last7DayAttackCount: 最近7天的攻击次数，单位次
        :type Last7DayAttackCount: int
        """
        self.PortRulesUsage = None
        self.DomainRulesUsage = None
        self.Last7DayAttackCount = None


    def _deserialize(self, params):
        self.PortRulesUsage = params.get("PortRulesUsage")
        self.DomainRulesUsage = params.get("DomainRulesUsage")
        self.Last7DayAttackCount = params.get("Last7DayAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstance(AbstractModel):
    """高防包资产实例信息

    """

    def __init__(self):
        r"""
        :param InstanceDetail: 资产实例的详细信息
        :type InstanceDetail: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        :param SpecificationLimit: 资产实例的规格信息
        :type SpecificationLimit: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceSpecification`
        :param Usage: 资产实例的使用统计信息
        :type Usage: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceUsages`
        :param Region: 资产实例所在的地域
        :type Region: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        :param Status: 资产实例的防护状态，状态码如下：
"idle"：正常状态(无攻击)
"attacking"：攻击中
"blocking"：封堵中
"creating"：创建中
"deblocking"：解封中
"isolate"：回收隔离中
        :type Status: str
        :param CreatedTime: 购买时间
        :type CreatedTime: str
        :param ExpiredTime: 到期时间
        :type ExpiredTime: str
        :param Name: 资产实例的名称
        :type Name: str
        :param PackInfo: 资产实例所属的套餐包信息，
注意：当资产实例不是套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type PackInfo: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        :param EipProductInfos: 高防包绑定的EIP属于的云产品信息
        :type EipProductInfos: list of EipProductInfo
        :param BoundStatus: 高防包绑定状态，取值[
"idle"：绑定已完成
 "bounding"：正在绑定中
"failed"：绑定失败
]
        :type BoundStatus: str
        :param DDoSLevel: 四层防护严格级别
        :type DDoSLevel: str
        :param CCEnable: CC防护开关
        :type CCEnable: int
        :param TagInfoList: 资源关联标签
        :type TagInfoList: list of TagInfo
        :param IpCountNewFlag: 新版本1ip高防包
        :type IpCountNewFlag: int
        """
        self.InstanceDetail = None
        self.SpecificationLimit = None
        self.Usage = None
        self.Region = None
        self.Status = None
        self.CreatedTime = None
        self.ExpiredTime = None
        self.Name = None
        self.PackInfo = None
        self.EipProductInfos = None
        self.BoundStatus = None
        self.DDoSLevel = None
        self.CCEnable = None
        self.TagInfoList = None
        self.IpCountNewFlag = None


    def _deserialize(self, params):
        if params.get("InstanceDetail") is not None:
            self.InstanceDetail = InstanceRelation()
            self.InstanceDetail._deserialize(params.get("InstanceDetail"))
        if params.get("SpecificationLimit") is not None:
            self.SpecificationLimit = BGPInstanceSpecification()
            self.SpecificationLimit._deserialize(params.get("SpecificationLimit"))
        if params.get("Usage") is not None:
            self.Usage = BGPInstanceUsages()
            self.Usage._deserialize(params.get("Usage"))
        if params.get("Region") is not None:
            self.Region = RegionInfo()
            self.Region._deserialize(params.get("Region"))
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        self.ExpiredTime = params.get("ExpiredTime")
        self.Name = params.get("Name")
        if params.get("PackInfo") is not None:
            self.PackInfo = PackInfo()
            self.PackInfo._deserialize(params.get("PackInfo"))
        if params.get("EipProductInfos") is not None:
            self.EipProductInfos = []
            for item in params.get("EipProductInfos"):
                obj = EipProductInfo()
                obj._deserialize(item)
                self.EipProductInfos.append(obj)
        self.BoundStatus = params.get("BoundStatus")
        self.DDoSLevel = params.get("DDoSLevel")
        self.CCEnable = params.get("CCEnable")
        if params.get("TagInfoList") is not None:
            self.TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self.TagInfoList.append(obj)
        self.IpCountNewFlag = params.get("IpCountNewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstanceSpecification(AbstractModel):
    """高防包资产实例的规格信息

    """

    def __init__(self):
        r"""
        :param ProtectBandwidth: 保底防护峰值，单位Gbps
        :type ProtectBandwidth: int
        :param ProtectCountLimit: 防护次数，单位次
        :type ProtectCountLimit: int
        :param ProtectIPNumberLimit: 防护IP数，单位个
        :type ProtectIPNumberLimit: int
        :param AutoRenewFlag: 自动续费状态，取值[
0：没有开启自动续费
1：开启了自动续费
]
        :type AutoRenewFlag: int
        :param UnionPackFlag: 联合产品标记，0代表普通高防包，1代表联合高防包
注意：此字段可能返回 null，表示取不到有效值。
        :type UnionPackFlag: int
        :param ServiceBandWidth: 业务带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceBandWidth: int
        :param BattleEditionFlag: 战斗服版本标记，0表示普通高防包，1表示战斗服高防包
注意：此字段可能返回 null，表示取不到有效值。
        :type BattleEditionFlag: int
        :param ChannelEditionFlag: 渠道版标记，0表示普通高防包，1表示渠道版高防包
注意：此字段可能返回 null，表示取不到有效值。
        :type ChannelEditionFlag: int
        :param EnterpriseFlag: 高防包企业版标记，0表示普通高防包；1表示企业版高防包
注意：此字段可能返回 null，表示取不到有效值。
        :type EnterpriseFlag: int
        :param ElasticLimit: 高防包企业版弹性阈值，0表示未开启；大于0为弹性防护阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type ElasticLimit: int
        """
        self.ProtectBandwidth = None
        self.ProtectCountLimit = None
        self.ProtectIPNumberLimit = None
        self.AutoRenewFlag = None
        self.UnionPackFlag = None
        self.ServiceBandWidth = None
        self.BattleEditionFlag = None
        self.ChannelEditionFlag = None
        self.EnterpriseFlag = None
        self.ElasticLimit = None


    def _deserialize(self, params):
        self.ProtectBandwidth = params.get("ProtectBandwidth")
        self.ProtectCountLimit = params.get("ProtectCountLimit")
        self.ProtectIPNumberLimit = params.get("ProtectIPNumberLimit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.UnionPackFlag = params.get("UnionPackFlag")
        self.ServiceBandWidth = params.get("ServiceBandWidth")
        self.BattleEditionFlag = params.get("BattleEditionFlag")
        self.ChannelEditionFlag = params.get("ChannelEditionFlag")
        self.EnterpriseFlag = params.get("EnterpriseFlag")
        self.ElasticLimit = params.get("ElasticLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstanceUsages(AbstractModel):
    """高防包资产实例的使用信息统计

    """

    def __init__(self):
        r"""
        :param ProtectCountUsage: 已使用的防护次数，单位次
        :type ProtectCountUsage: int
        :param ProtectIPNumberUsage: 已防护的IP数，单位个
        :type ProtectIPNumberUsage: int
        :param Last7DayAttackCount: 最近7天的攻击次数，单位次
        :type Last7DayAttackCount: int
        """
        self.ProtectCountUsage = None
        self.ProtectIPNumberUsage = None
        self.Last7DayAttackCount = None


    def _deserialize(self, params):
        self.ProtectCountUsage = params.get("ProtectCountUsage")
        self.ProtectIPNumberUsage = params.get("ProtectIPNumberUsage")
        self.Last7DayAttackCount = params.get("Last7DayAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlackWhiteIpRelation(AbstractModel):
    """黑白名单IP

    """

    def __init__(self):
        r"""
        :param Ip: IP地址
        :type Ip: str
        :param Type: IP类型，取值[black(黑IP)，white(白IP)]
        :type Type: str
        :param InstanceDetailList: 黑白IP所属的实例
        :type InstanceDetailList: list of InstanceRelation
        :param Mask: ip掩码，0表示32位完整ip
        :type Mask: int
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.Ip = None
        self.Type = None
        self.InstanceDetailList = None
        self.Mask = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Type = params.get("Type")
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        self.Mask = params.get("Mask")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """高防包绑定IP对象

    """

    def __init__(self):
        r"""
        :param Ip: IP地址
        :type Ip: str
        :param BizType: 绑定的产品分类，绑定操作为必填项，解绑操作可不填。取值[public（CVM、CLB产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :type BizType: str
        :param InstanceId: IP所属的资源实例ID，绑定操作为必填项，解绑操作可不填。例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*); 如果绑定的是托管IP没有对应的资源实例ID，请填写"none";
        :type InstanceId: str
        :param DeviceType: 产品分类下的子类型，绑定操作为必填项，解绑操作可不填。取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（弹性公网常规IP）]
        :type DeviceType: str
        :param IspCode: 运营商，绑定操作为必填项，解绑操作可不填。0：电信；1：联通；2：移动；5：BGP
        :type IspCode: int
        """
        self.Ip = None
        self.BizType = None
        self.InstanceId = None
        self.DeviceType = None
        self.IspCode = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.InstanceId = params.get("InstanceId")
        self.DeviceType = params.get("DeviceType")
        self.IspCode = params.get("IspCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLevelPolicy(AbstractModel):
    """CC分级策略

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: Ip
        :type Ip: str
        :param Protocol: 协议
        :type Protocol: str
        :param Domain: 域名
        :type Domain: str
        :param Level: 防护等级，可取值default表示默认策略，loose表示宽松，strict表示严格
        :type Level: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.InstanceId = None
        self.Ip = None
        self.Protocol = None
        self.Domain = None
        self.Level = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.Level = params.get("Level")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPrecisionPlyRecord(AbstractModel):
    """CC精准防护配置项

    """

    def __init__(self):
        r"""
        :param FieldType: 配置项类型，当前仅支持value
        :type FieldType: str
        :param FieldName: 配置字段，可取值cgi， ua， cookie， referer， accept,  srcip
        :type FieldName: str
        :param Value: 配置取值
        :type Value: str
        :param ValueOperator: 配置项值比对方式，可取值equal ，not_equal， include
        :type ValueOperator: str
        """
        self.FieldType = None
        self.FieldName = None
        self.Value = None
        self.ValueOperator = None


    def _deserialize(self, params):
        self.FieldType = params.get("FieldType")
        self.FieldName = params.get("FieldName")
        self.Value = params.get("Value")
        self.ValueOperator = params.get("ValueOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPrecisionPolicy(AbstractModel):
    """CC精准防护策略信息

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略Id
        :type PolicyId: str
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: Ip地址
        :type Ip: str
        :param Protocol: 协议
        :type Protocol: str
        :param Domain: 域名
        :type Domain: str
        :param PolicyAction: 策略方式（丢弃或验证码）
        :type PolicyAction: str
        :param PolicyList: 策略列表
        :type PolicyList: list of CCPrecisionPlyRecord
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.PolicyId = None
        self.InstanceId = None
        self.Ip = None
        self.Protocol = None
        self.Domain = None
        self.PolicyAction = None
        self.PolicyList = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self.PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self.PolicyList.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCReqLimitPolicy(AbstractModel):
    """CC频率限制策略

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略Id
        :type PolicyId: str
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: Ip地址
        :type Ip: str
        :param Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param Domain: 域名
        :type Domain: str
        :param PolicyRecord: 策略项
        :type PolicyRecord: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.PolicyId = None
        self.InstanceId = None
        self.Ip = None
        self.Protocol = None
        self.Domain = None
        self.PolicyRecord = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        if params.get("PolicyRecord") is not None:
            self.PolicyRecord = CCReqLimitPolicyRecord()
            self.PolicyRecord._deserialize(params.get("PolicyRecord"))
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCReqLimitPolicyRecord(AbstractModel):
    """CC频率限制策略项字段

    """

    def __init__(self):
        r"""
        :param Period: 统计周期，可取值1，10，30，60，单位秒
        :type Period: int
        :param RequestNum: 请求数，取值1~20000
        :type RequestNum: int
        :param Action: 频率限制策略方式，可取值alg表示验证码，drop表示丢弃
        :type Action: str
        :param ExecuteDuration: 频率限制策略时长，可取值1~86400，单位秒
        :type ExecuteDuration: int
        :param Mode: 策略项比对方式，可取值include表示包含，equal表示等于
        :type Mode: str
        :param Uri: Uri，三个策略项仅可填其中之一
        :type Uri: str
        :param UserAgent: User-Agent，三个策略项仅可填其中之一
        :type UserAgent: str
        :param Cookie: Cookie，三个策略项仅可填其中之一
        :type Cookie: str
        """
        self.Period = None
        self.RequestNum = None
        self.Action = None
        self.ExecuteDuration = None
        self.Mode = None
        self.Uri = None
        self.UserAgent = None
        self.Cookie = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.RequestNum = params.get("RequestNum")
        self.Action = params.get("Action")
        self.ExecuteDuration = params.get("ExecuteDuration")
        self.Mode = params.get("Mode")
        self.Uri = params.get("Uri")
        self.UserAgent = params.get("UserAgent")
        self.Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCThresholdPolicy(AbstractModel):
    """CC清洗阈值策略

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: Ip地址
        :type Ip: str
        :param Protocol: 协议
        :type Protocol: str
        :param Domain: 域名
        :type Domain: str
        :param Threshold: 清洗阈值
        :type Threshold: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.InstanceId = None
        self.Ip = None
        self.Protocol = None
        self.Domain = None
        self.Threshold = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.Threshold = params.get("Threshold")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcBlackWhiteIpPolicy(AbstractModel):
    """CC四层黑白名单列表

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略Id
        :type PolicyId: str
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP地址
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议
        :type Protocol: str
        :param Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        :param BlackWhiteIp: 黑白名单IP地址
        :type BlackWhiteIp: str
        :param Mask: 掩码
        :type Mask: int
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.PolicyId = None
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None
        self.Type = None
        self.BlackWhiteIp = None
        self.Mask = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.Type = params.get("Type")
        self.BlackWhiteIp = params.get("BlackWhiteIp")
        self.Mask = params.get("Mask")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcGeoIPBlockConfig(AbstractModel):
    """DDoS防护的区域封禁配置

    """

    def __init__(self):
        r"""
        :param RegionType: 区域类型，取值[
oversea(海外)
china(国内)
customized(自定义地区)
]
        :type RegionType: str
        :param Action: 封禁动作，取值[
drop(拦截)
alg(人机校验)
]
        :type Action: str
        :param Id: 配置ID，配置添加成功后生成；添加新配置时不用填写此字段，修改或删除配置时需要填写配置ID
        :type Id: str
        :param AreaList: 当RegionType为customized时，必须填写AreaList；当RegionType为china或oversea时，AreaList为空
        :type AreaList: list of int
        """
        self.RegionType = None
        self.Action = None
        self.Id = None
        self.AreaList = None


    def _deserialize(self, params):
        self.RegionType = params.get("RegionType")
        self.Action = params.get("Action")
        self.Id = params.get("Id")
        self.AreaList = params.get("AreaList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcGeoIpPolicyNew(AbstractModel):
    """CC地域封禁列表详情

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略Id
        :type PolicyId: str
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP地址
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param Action: 用户动作，drop或alg
        :type Action: str
        :param RegionType: 地域类型，分为china, oversea与customized
        :type RegionType: str
        :param AreaList: 用户选择封禁的地域ID列表
        :type AreaList: list of int non-negative
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.PolicyId = None
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None
        self.Action = None
        self.RegionType = None
        self.AreaList = None
        self.CreateTime = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.Action = params.get("Action")
        self.RegionType = params.get("RegionType")
        self.AreaList = params.get("AreaList")
        self.CreateTime = params.get("CreateTime")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdInsL7Rules(AbstractModel):
    """使用证书的规则集合

    """

    def __init__(self):
        r"""
        :param L7Rules: 使用证书的规则列表
        :type L7Rules: list of InsL7Rules
        :param CertId: 证书ID
        :type CertId: str
        """
        self.L7Rules = None
        self.CertId = None


    def _deserialize(self, params):
        if params.get("L7Rules") is not None:
            self.L7Rules = []
            for item in params.get("L7Rules"):
                obj = InsL7Rules()
                obj._deserialize(item)
                self.L7Rules.append(obj)
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectLimitConfig(AbstractModel):
    """连接抑制相关配置

    """

    def __init__(self):
        r"""
        :param SdNewLimit: 基于源IP+目的IP的每秒新建数限制
        :type SdNewLimit: int
        :param DstNewLimit: 基于目的IP的每秒新建数限制
        :type DstNewLimit: int
        :param SdConnLimit: 基于源IP+目的IP的并发连接控制
        :type SdConnLimit: int
        :param DstConnLimit: 基于目的IP+目的端口的并发连接控制
        :type DstConnLimit: int
        :param BadConnThreshold: 基于连接抑制触发阈值，取值范围[0,4294967295]
        :type BadConnThreshold: int
        :param NullConnEnable: 异常连接检测条件，空连接防护开关，，取值范围[0,1]
        :type NullConnEnable: int
        :param ConnTimeout: 异常连接检测条件，连接超时，，取值范围[0,65535]
        :type ConnTimeout: int
        :param SynRate: 异常连接检测条件，syn占比ack百分比，，取值范围[0,100]
        :type SynRate: int
        :param SynLimit: 异常连接检测条件，syn阈值，取值范围[0,100]
        :type SynLimit: int
        """
        self.SdNewLimit = None
        self.DstNewLimit = None
        self.SdConnLimit = None
        self.DstConnLimit = None
        self.BadConnThreshold = None
        self.NullConnEnable = None
        self.ConnTimeout = None
        self.SynRate = None
        self.SynLimit = None


    def _deserialize(self, params):
        self.SdNewLimit = params.get("SdNewLimit")
        self.DstNewLimit = params.get("DstNewLimit")
        self.SdConnLimit = params.get("SdConnLimit")
        self.DstConnLimit = params.get("DstConnLimit")
        self.BadConnThreshold = params.get("BadConnThreshold")
        self.NullConnEnable = params.get("NullConnEnable")
        self.ConnTimeout = params.get("ConnTimeout")
        self.SynRate = params.get("SynRate")
        self.SynLimit = params.get("SynLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectLimitRelation(AbstractModel):
    """连接抑制列表

    """

    def __init__(self):
        r"""
        :param ConnectLimitConfig: 连接抑制配置
        :type ConnectLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.ConnectLimitConfig`
        :param InstanceDetailList: 连接抑制关联的实例信息
        :type InstanceDetailList: list of InstanceRelation
        """
        self.ConnectLimitConfig = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        if params.get("ConnectLimitConfig") is not None:
            self.ConnectLimitConfig = ConnectLimitConfig()
            self.ConnectLimitConfig._deserialize(params.get("ConnectLimitConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlackWhiteIpListRequest(AbstractModel):
    """CreateBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param IpList: IP列表
        :type IpList: list of str
        :param Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        """
        self.InstanceId = None
        self.IpList = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IpList = params.get("IpList")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlackWhiteIpListResponse(AbstractModel):
    """CreateBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgp表示独享包；bgp-multip表示共享包）
        :type Business: str
        :param Id: 资源实例ID
        :type Id: str
        :param BoundDevList: 绑定到资源实例的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要绑定的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :type BoundDevList: list of BoundIpInfo
        :param UnBoundDevList: 与资源实例解绑的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要解绑的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :type UnBoundDevList: list of BoundIpInfo
        :param CopyPolicy: 已弃用，不填
        :type CopyPolicy: str
        """
        self.Business = None
        self.Id = None
        self.BoundDevList = None
        self.UnBoundDevList = None
        self.CopyPolicy = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self.BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self.UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self.UnBoundDevList.append(obj)
        self.CopyPolicy = params.get("CopyPolicy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateCCPrecisionPolicyRequest(AbstractModel):
    """CreateCCPrecisionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP值
        :type Ip: str
        :param Protocol: 协议， 可取值HTTP，HTTPS
        :type Protocol: str
        :param Domain: 域名
        :type Domain: str
        :param PolicyAction: 策略方式，可取值alg表示验证码，drop表示丢弃
        :type PolicyAction: str
        :param PolicyList: 策略记录
        :type PolicyList: list of CCPrecisionPlyRecord
        """
        self.InstanceId = None
        self.Ip = None
        self.Protocol = None
        self.Domain = None
        self.PolicyAction = None
        self.PolicyList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self.PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self.PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCPrecisionPolicyResponse(AbstractModel):
    """CreateCCPrecisionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCCReqLimitPolicyRequest(AbstractModel):
    """CreateCCReqLimitPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP值
        :type Ip: str
        :param Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param Domain: 域名
        :type Domain: str
        :param Policy: 策略项
        :type Policy: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        :param IsGlobal: 是否为兜底频控
        :type IsGlobal: int
        """
        self.InstanceId = None
        self.Ip = None
        self.Protocol = None
        self.Domain = None
        self.Policy = None
        self.IsGlobal = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        if params.get("Policy") is not None:
            self.Policy = CCReqLimitPolicyRecord()
            self.Policy._deserialize(params.get("Policy"))
        self.IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCReqLimitPolicyResponse(AbstractModel):
    """CreateCCReqLimitPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCcBlackWhiteIpListRequest(AbstractModel):
    """CreateCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param IpList: IP列表
        :type IpList: list of IpSegment
        :param Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        :param Ip: Ip地址
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议
        :type Protocol: str
        """
        self.InstanceId = None
        self.IpList = None
        self.Type = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self.IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self.IpList.append(obj)
        self.Type = params.get("Type")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcBlackWhiteIpListResponse(AbstractModel):
    """CreateCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateCcGeoIPBlockConfigRequest(AbstractModel):
    """CreateCcGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例id
        :type InstanceId: str
        :param IP: ip地址
        :type IP: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议类型
        :type Protocol: str
        :param CcGeoIPBlockConfig: CC区域封禁配置，填写参数时配置ID请为空
        :type CcGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        self.InstanceId = None
        self.IP = None
        self.Domain = None
        self.Protocol = None
        self.CcGeoIPBlockConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.IP = params.get("IP")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        if params.get("CcGeoIPBlockConfig") is not None:
            self.CcGeoIPBlockConfig = CcGeoIPBlockConfig()
            self.CcGeoIPBlockConfig._deserialize(params.get("CcGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcGeoIPBlockConfigResponse(AbstractModel):
    """CreateCcGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDDoSAIRequest(AbstractModel):
    """CreateDDoSAI请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIdList: 资源实例ID列表
        :type InstanceIdList: list of str
        :param DDoSAI: AI防护开关，取值[
on(开启)
off(关闭)
]
        :type DDoSAI: str
        """
        self.InstanceIdList = None
        self.DDoSAI = None


    def _deserialize(self, params):
        self.InstanceIdList = params.get("InstanceIdList")
        self.DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSAIResponse(AbstractModel):
    """CreateDDoSAI返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDDoSBlackWhiteIpListRequest(AbstractModel):
    """CreateDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param IpList: IP列表
        :type IpList: list of IpSegment
        :param Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        """
        self.InstanceId = None
        self.IpList = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self.IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self.IpList.append(obj)
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSBlackWhiteIpListResponse(AbstractModel):
    """CreateDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDDoSConnectLimitRequest(AbstractModel):
    """CreateDDoSConnectLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例Id
        :type InstanceId: str
        :param ConnectLimitConfig: 连接抑制配置
        :type ConnectLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.ConnectLimitConfig`
        """
        self.InstanceId = None
        self.ConnectLimitConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ConnectLimitConfig") is not None:
            self.ConnectLimitConfig = ConnectLimitConfig()
            self.ConnectLimitConfig._deserialize(params.get("ConnectLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSConnectLimitResponse(AbstractModel):
    """CreateDDoSConnectLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDDoSGeoIPBlockConfigRequest(AbstractModel):
    """CreateDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param DDoSGeoIPBlockConfig: DDoS区域封禁配置，填写参数时配置ID请为空
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self.InstanceId = None
        self.DDoSGeoIPBlockConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self.DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self.DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSGeoIPBlockConfigResponse(AbstractModel):
    """CreateDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDDoSSpeedLimitConfigRequest(AbstractModel):
    """CreateDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param DDoSSpeedLimitConfig: 访问限速配置，填写参数时配置ID请为空
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self.InstanceId = None
        self.DDoSSpeedLimitConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self.DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self.DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSSpeedLimitConfigResponse(AbstractModel):
    """CreateDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDefaultAlarmThresholdRequest(AbstractModel):
    """CreateDefaultAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param DefaultAlarmConfig: 默认告警阈值配置
        :type DefaultAlarmConfig: :class:`tencentcloud.antiddos.v20200309.models.DefaultAlarmThreshold`
        :param InstanceType: 产品类型，取值[
bgp(表示高防包产品)
bgpip(表示高防IP产品)
]
        :type InstanceType: str
        """
        self.DefaultAlarmConfig = None
        self.InstanceType = None


    def _deserialize(self, params):
        if params.get("DefaultAlarmConfig") is not None:
            self.DefaultAlarmConfig = DefaultAlarmThreshold()
            self.DefaultAlarmConfig._deserialize(params.get("DefaultAlarmConfig"))
        self.InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDefaultAlarmThresholdResponse(AbstractModel):
    """CreateDefaultAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateIPAlarmThresholdConfigRequest(AbstractModel):
    """CreateIPAlarmThresholdConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param IpAlarmThresholdConfigList: IP告警阈值配置列表
        :type IpAlarmThresholdConfigList: list of IPAlarmThresholdRelation
        """
        self.IpAlarmThresholdConfigList = None


    def _deserialize(self, params):
        if params.get("IpAlarmThresholdConfigList") is not None:
            self.IpAlarmThresholdConfigList = []
            for item in params.get("IpAlarmThresholdConfigList"):
                obj = IPAlarmThresholdRelation()
                obj._deserialize(item)
                self.IpAlarmThresholdConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPAlarmThresholdConfigResponse(AbstractModel):
    """CreateIPAlarmThresholdConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateL7RuleCertsRequest(AbstractModel):
    """CreateL7RuleCerts请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertId: SSL证书ID
        :type CertId: str
        :param L7Rules: L7域名转发规则列表
        :type L7Rules: list of InsL7Rules
        """
        self.CertId = None
        self.L7Rules = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        if params.get("L7Rules") is not None:
            self.L7Rules = []
            for item in params.get("L7Rules"):
                obj = InsL7Rules()
                obj._deserialize(item)
                self.L7Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertsResponse(AbstractModel):
    """CreateL7RuleCerts返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreateNewL7RulesRequest(AbstractModel):
    """CreateNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Rules: 规则列表
        :type Rules: list of L7RuleEntry
        :param Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param IdList: 资源ID列表
        :type IdList: list of str
        :param VipList: 资源IP列表
        :type VipList: list of str
        """
        self.Rules = None
        self.Business = None
        self.IdList = None
        self.VipList = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Business = params.get("Business")
        self.IdList = params.get("IdList")
        self.VipList = params.get("VipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesResponse(AbstractModel):
    """CreateNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class CreatePacketFilterConfigRequest(AbstractModel):
    """CreatePacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param PacketFilterConfig: 特征过滤规则
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self.InstanceId = None
        self.PacketFilterConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self.PacketFilterConfig = PacketFilterConfig()
            self.PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePacketFilterConfigResponse(AbstractModel):
    """CreatePacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePortAclConfigListRequest(AbstractModel):
    """CreatePortAclConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIdList: 资源实例ID列表
        :type InstanceIdList: list of str
        :param AclConfig: 端口acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self.InstanceIdList = None
        self.AclConfig = None


    def _deserialize(self, params):
        self.InstanceIdList = params.get("InstanceIdList")
        if params.get("AclConfig") is not None:
            self.AclConfig = AclConfig()
            self.AclConfig._deserialize(params.get("AclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePortAclConfigListResponse(AbstractModel):
    """CreatePortAclConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreatePortAclConfigRequest(AbstractModel):
    """CreatePortAclConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param AclConfig: 端口acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self.InstanceId = None
        self.AclConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AclConfig") is not None:
            self.AclConfig = AclConfig()
            self.AclConfig._deserialize(params.get("AclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePortAclConfigResponse(AbstractModel):
    """CreatePortAclConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateProtocolBlockConfigRequest(AbstractModel):
    """CreateProtocolBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param ProtocolBlockConfig: 协议封禁配置
        :type ProtocolBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        """
        self.InstanceId = None
        self.ProtocolBlockConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("ProtocolBlockConfig") is not None:
            self.ProtocolBlockConfig = ProtocolBlockConfig()
            self.ProtocolBlockConfig._deserialize(params.get("ProtocolBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProtocolBlockConfigResponse(AbstractModel):
    """CreateProtocolBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSchedulingDomainRequest(AbstractModel):
    """CreateSchedulingDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param Product: 代表是否混合云本地化的产品。
hybrid: 宙斯盾本地化
不填写：其他
        :type Product: str
        """
        self.Product = None


    def _deserialize(self, params):
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulingDomainResponse(AbstractModel):
    """CreateSchedulingDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 新创建的域名
        :type Domain: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domain = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.RequestId = params.get("RequestId")


class CreateWaterPrintConfigRequest(AbstractModel):
    """CreateWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param WaterPrintConfig: 水印防护配置
        :type WaterPrintConfig: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        """
        self.InstanceId = None
        self.WaterPrintConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("WaterPrintConfig") is not None:
            self.WaterPrintConfig = WaterPrintConfig()
            self.WaterPrintConfig._deserialize(params.get("WaterPrintConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWaterPrintConfigResponse(AbstractModel):
    """CreateWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateWaterPrintKeyRequest(AbstractModel):
    """CreateWaterPrintKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWaterPrintKeyResponse(AbstractModel):
    """CreateWaterPrintKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DDoSAIRelation(AbstractModel):
    """DDoS防护的AI防护开关

    """

    def __init__(self):
        r"""
        :param DDoSAI: AI防护开关，取值[
on(开启)
off(关闭)
]
        :type DDoSAI: str
        :param InstanceDetailList: AI防护开关所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self.DDoSAI = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        self.DDoSAI = params.get("DDoSAI")
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIPBlockConfig(AbstractModel):
    """DDoS防护的区域封禁配置

    """

    def __init__(self):
        r"""
        :param RegionType: 区域类型，取值[
oversea(境外)
china(国内)
customized(自定义地区)
]
        :type RegionType: str
        :param Action: 封禁动作，取值[
drop(拦截)
trans(放行)
]
        :type Action: str
        :param Id: 配置ID，配置添加成功后生成；添加新配置时不用填写此字段，修改或删除配置时需要填写配置ID
        :type Id: str
        :param AreaList: 当RegionType为customized时，必须填写AreaList，且最多填写128个；
        :type AreaList: list of int
        """
        self.RegionType = None
        self.Action = None
        self.Id = None
        self.AreaList = None


    def _deserialize(self, params):
        self.RegionType = params.get("RegionType")
        self.Action = params.get("Action")
        self.Id = params.get("Id")
        self.AreaList = params.get("AreaList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIPBlockConfigRelation(AbstractModel):
    """DDoS区域封禁配置相关信息

    """

    def __init__(self):
        r"""
        :param GeoIPBlockConfig: DDoS区域封禁配置
        :type GeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        :param InstanceDetailList: 配置所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self.GeoIPBlockConfig = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        if params.get("GeoIPBlockConfig") is not None:
            self.GeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self.GeoIPBlockConfig._deserialize(params.get("GeoIPBlockConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimitConfig(AbstractModel):
    """DDoS访问限速配置

    """

    def __init__(self):
        r"""
        :param Mode: 限速模式，取值[
1(基于源IP限速)
2(基于目的端口限速)
]
        :type Mode: int
        :param SpeedValues: 限速值，每种类型的限速值最多支持1个；该字段数组至少有一种限速值
        :type SpeedValues: list of SpeedValue
        :param DstPortScopes: 此字段已弃用，请填写新字段DstPortList。
        :type DstPortScopes: list of PortSegment
        :param Id: 配置ID，配置添加成功后生成；添加新限制配置时不用填写此字段，修改或删除限速配置时需要填写配置ID
        :type Id: str
        :param ProtocolList: IP protocol numbers, 取值[
ALL(所有协议)
TCP(tcp协议)
UDP(udp协议)
SMP(smp协议)
1;2-100(自定义协议号范围,最多8个)
]
注意：当自定义协议号范围时，只能填写协议号，多个范围;分隔；当填写ALL时不能再填写其他协议或协议号。
        :type ProtocolList: str
        :param DstPortList: 端口范围列表，最多8个，多个;分隔，范围表示用-；此端口范围必须填写；填写样式1:0-65535，样式2:80;443;1000-2000
        :type DstPortList: str
        """
        self.Mode = None
        self.SpeedValues = None
        self.DstPortScopes = None
        self.Id = None
        self.ProtocolList = None
        self.DstPortList = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        if params.get("SpeedValues") is not None:
            self.SpeedValues = []
            for item in params.get("SpeedValues"):
                obj = SpeedValue()
                obj._deserialize(item)
                self.SpeedValues.append(obj)
        if params.get("DstPortScopes") is not None:
            self.DstPortScopes = []
            for item in params.get("DstPortScopes"):
                obj = PortSegment()
                obj._deserialize(item)
                self.DstPortScopes.append(obj)
        self.Id = params.get("Id")
        self.ProtocolList = params.get("ProtocolList")
        self.DstPortList = params.get("DstPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimitConfigRelation(AbstractModel):
    """DDoS访问限速配置相关信息

    """

    def __init__(self):
        r"""
        :param SpeedLimitConfig: DDoS访问限速配置
        :type SpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        :param InstanceDetailList: 配置所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self.SpeedLimitConfig = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        if params.get("SpeedLimitConfig") is not None:
            self.SpeedLimitConfig = DDoSSpeedLimitConfig()
            self.SpeedLimitConfig._deserialize(params.get("SpeedLimitConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultAlarmThreshold(AbstractModel):
    """单IP默认告警阈值配置

    """

    def __init__(self):
        r"""
        :param AlarmType: 告警阈值类型，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type AlarmType: int
        :param AlarmThreshold: 告警阈值，单位Mbps，取值>=0；当作为输入参数时，设置0会删除告警阈值配置；
        :type AlarmThreshold: int
        """
        self.AlarmType = None
        self.AlarmThreshold = None


    def _deserialize(self, params):
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCLevelPolicyRequest(AbstractModel):
    """DeleteCCLevelPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: 配置策略的IP
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议，可取值http
        :type Protocol: str
        """
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCLevelPolicyResponse(AbstractModel):
    """DeleteCCLevelPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCCPrecisionPolicyRequest(AbstractModel):
    """DeleteCCPrecisionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param PolicyId: 策略Id
        :type PolicyId: str
        """
        self.InstanceId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCPrecisionPolicyResponse(AbstractModel):
    """DeleteCCPrecisionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCCRequestLimitPolicyRequest(AbstractModel):
    """DeleteCCRequestLimitPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param PolicyId: 策略Id
        :type PolicyId: str
        """
        self.InstanceId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCRequestLimitPolicyResponse(AbstractModel):
    """DeleteCCRequestLimitPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCCThresholdPolicyRequest(AbstractModel):
    """DeleteCCThresholdPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: 配置策略的IP
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议，可取值http
        :type Protocol: str
        """
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCThresholdPolicyResponse(AbstractModel):
    """DeleteCCThresholdPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcBlackWhiteIpListRequest(AbstractModel):
    """DeleteCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param PolicyId: 策略Id
        :type PolicyId: str
        """
        self.InstanceId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcBlackWhiteIpListResponse(AbstractModel):
    """DeleteCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteCcGeoIPBlockConfigRequest(AbstractModel):
    """DeleteCcGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param CcGeoIPBlockConfig: CC区域封禁配置，填写参数时配置ID不能为空
        :type CcGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        self.InstanceId = None
        self.CcGeoIPBlockConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("CcGeoIPBlockConfig") is not None:
            self.CcGeoIPBlockConfig = CcGeoIPBlockConfig()
            self.CcGeoIPBlockConfig._deserialize(params.get("CcGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcGeoIPBlockConfigResponse(AbstractModel):
    """DeleteCcGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDDoSBlackWhiteIpListRequest(AbstractModel):
    """DeleteDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param IpList: IP列表
        :type IpList: list of IpSegment
        :param Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        """
        self.InstanceId = None
        self.IpList = None
        self.Type = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self.IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self.IpList.append(obj)
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSBlackWhiteIpListResponse(AbstractModel):
    """DeleteDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDDoSGeoIPBlockConfigRequest(AbstractModel):
    """DeleteDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param DDoSGeoIPBlockConfig: DDoS区域封禁配置，填写参数时配置ID不能为空
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self.InstanceId = None
        self.DDoSGeoIPBlockConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self.DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self.DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSGeoIPBlockConfigResponse(AbstractModel):
    """DeleteDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDDoSSpeedLimitConfigRequest(AbstractModel):
    """DeleteDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param DDoSSpeedLimitConfig: 访问限速配置，填写参数时配置ID不能为空
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self.InstanceId = None
        self.DDoSSpeedLimitConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self.DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self.DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSSpeedLimitConfigResponse(AbstractModel):
    """DeleteDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePacketFilterConfigRequest(AbstractModel):
    """DeletePacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param PacketFilterConfig: 特征过滤配置
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self.InstanceId = None
        self.PacketFilterConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self.PacketFilterConfig = PacketFilterConfig()
            self.PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePacketFilterConfigResponse(AbstractModel):
    """DeletePacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeletePortAclConfigRequest(AbstractModel):
    """DeletePortAclConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param AclConfig: 端口acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self.InstanceId = None
        self.AclConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("AclConfig") is not None:
            self.AclConfig = AclConfig()
            self.AclConfig._deserialize(params.get("AclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePortAclConfigResponse(AbstractModel):
    """DeletePortAclConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWaterPrintConfigRequest(AbstractModel):
    """DeleteWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWaterPrintConfigResponse(AbstractModel):
    """DeleteWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteWaterPrintKeyRequest(AbstractModel):
    """DeleteWaterPrintKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param KeyId: 水印密钥ID
        :type KeyId: str
        """
        self.InstanceId = None
        self.KeyId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWaterPrintKeyResponse(AbstractModel):
    """DeleteWaterPrintKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBasicDeviceStatusRequest(AbstractModel):
    """DescribeBasicDeviceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param IpList: IP 资源列表
        :type IpList: list of str
        """
        self.IpList = None


    def _deserialize(self, params):
        self.IpList = params.get("IpList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceStatusResponse(AbstractModel):
    """DescribeBasicDeviceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param Data: 返回资源及状态，状态码：
1 - 封堵状态
2 - 正常状态
3 - 攻击状态
        :type Data: list of KeyValue
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBgpBizTrendRequest(AbstractModel):
    """DescribeBgpBizTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgp-multip表示高防包）
        :type Business: str
        :param StartTime: 统计开始时间。 例：“2020-09-22 00:00:00”
        :type StartTime: str
        :param EndTime: 统计结束时间。 例：“2020-09-22 00:00:00”
        :type EndTime: str
        :param MetricName: 统计纬度，可取值intraffic, outtraffic, inpkg, outpkg
        :type MetricName: str
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param Flag: 0表示固定时间，1表示自定义时间
        :type Flag: int
        """
        self.Business = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.InstanceId = None
        self.Flag = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.InstanceId = params.get("InstanceId")
        self.Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBgpBizTrendResponse(AbstractModel):
    """DescribeBgpBizTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataList: 曲线图各个时间点的值
        :type DataList: list of int non-negative
        :param Total: 曲线图取值个数
        :type Total: int
        :param MetricName: 统计纬度
        :type MetricName: str
        :param MaxData: 返回数组最大值
        :type MaxData: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataList = None
        self.Total = None
        self.MetricName = None
        self.MaxData = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataList = params.get("DataList")
        self.Total = params.get("Total")
        self.MetricName = params.get("MetricName")
        self.MaxData = params.get("MaxData")
        self.RequestId = params.get("RequestId")


class DescribeBizTrendRequest(AbstractModel):
    """DescribeBizTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Statistics: 统计方式，可取值max, min, avg, sum, 如统计纬度是流量速率或包量速率，仅可取值max
        :type Statistics: str
        :param Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param Period: 统计周期，可取值300，1800，3600，21600，86400，单位秒
        :type Period: int
        :param StartTime: 统计开始时间。 例：“2020-09-22 00:00:00”
        :type StartTime: str
        :param EndTime: 统计结束时间。 例：“2020-09-22 00:00:00”
        :type EndTime: str
        :param Id: 资源实例ID
        :type Id: str
        :param MetricName: 统计纬度，可取值connum, new_conn, inactive_conn, intraffic, outtraffic, inpkg, outpkg, qps
        :type MetricName: str
        :param Domain: 统计纬度为qps时，可选特定域名查询
        :type Domain: str
        :param ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :type ProtoInfo: list of ProtocolPort
        """
        self.Statistics = None
        self.Business = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Id = None
        self.MetricName = None
        self.Domain = None
        self.ProtoInfo = None


    def _deserialize(self, params):
        self.Statistics = params.get("Statistics")
        self.Business = params.get("Business")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.Domain = params.get("Domain")
        if params.get("ProtoInfo") is not None:
            self.ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self.ProtoInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizTrendResponse(AbstractModel):
    """DescribeBizTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param DataList: 曲线图各个时间点的值
        :type DataList: list of float
        :param MetricName: 统计纬度
        :type MetricName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DataList = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DataList = params.get("DataList")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeBlackWhiteIpListRequest(AbstractModel):
    """DescribeBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBlackWhiteIpListResponse(AbstractModel):
    """DescribeBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlackIpList: 黑名单IP列表
        :type BlackIpList: list of str
        :param WhiteIpList: 白名单IP列表
        :type WhiteIpList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlackIpList = None
        self.WhiteIpList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlackIpList = params.get("BlackIpList")
        self.WhiteIpList = params.get("WhiteIpList")
        self.RequestId = params.get("RequestId")


class DescribeCCLevelListRequest(AbstractModel):
    """DescribeCCLevelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgp-multip表示高防包）
        :type Business: str
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param InstanceId: 指定实例Id
        :type InstanceId: str
        """
        self.Business = None
        self.Offset = None
        self.Limit = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCLevelListResponse(AbstractModel):
    """DescribeCCLevelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 分级策略列表总数
        :type Total: int
        :param LevelList: 分级策略列表总数
        :type LevelList: list of CCLevelPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.LevelList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("LevelList") is not None:
            self.LevelList = []
            for item in params.get("LevelList"):
                obj = CCLevelPolicy()
                obj._deserialize(item)
                self.LevelList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCLevelPolicyRequest(AbstractModel):
    """DescribeCCLevelPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP值
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        """
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCLevelPolicyResponse(AbstractModel):
    """DescribeCCLevelPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param Level: CC防护等级，可取值loose表示宽松，strict表示严格，normal表示适中， emergency表示攻击紧急， sup_loose表示超级宽松，default表示默认策略（无频控配置下发），customized表示自定义策略
        :type Level: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Level = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Level = params.get("Level")
        self.RequestId = params.get("RequestId")


class DescribeCCPrecisionPlyListRequest(AbstractModel):
    """DescribeCCPrecisionPlyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip-multip：表示高防包；bgpip：表示高防IP）
        :type Business: str
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param InstanceId: 指定特定实例Id
        :type InstanceId: str
        :param Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        """
        self.Business = None
        self.Offset = None
        self.Limit = None
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCPrecisionPlyListResponse(AbstractModel):
    """DescribeCCPrecisionPlyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 策略列表总数
        :type Total: int
        :param PrecisionPolicyList: 策略列表详情
        :type PrecisionPolicyList: list of CCPrecisionPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.PrecisionPolicyList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("PrecisionPolicyList") is not None:
            self.PrecisionPolicyList = []
            for item in params.get("PrecisionPolicyList"):
                obj = CCPrecisionPolicy()
                obj._deserialize(item)
                self.PrecisionPolicyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCReqLimitPolicyListRequest(AbstractModel):
    """DescribeCCReqLimitPolicyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgp-multip表示高防包，bgpip表示高防IP）
        :type Business: str
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param InstanceId: 指定实例Id
        :type InstanceId: str
        :param Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        """
        self.Business = None
        self.Offset = None
        self.Limit = None
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCReqLimitPolicyListResponse(AbstractModel):
    """DescribeCCReqLimitPolicyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 频率限制列表总数
        :type Total: int
        :param RequestLimitPolicyList: 频率限制列表详情
        :type RequestLimitPolicyList: list of CCReqLimitPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.RequestLimitPolicyList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("RequestLimitPolicyList") is not None:
            self.RequestLimitPolicyList = []
            for item in params.get("RequestLimitPolicyList"):
                obj = CCReqLimitPolicy()
                obj._deserialize(item)
                self.RequestLimitPolicyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCThresholdListRequest(AbstractModel):
    """DescribeCCThresholdList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgp-multip表示高防包）
        :type Business: str
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param InstanceId: 指定实例Id
        :type InstanceId: str
        """
        self.Business = None
        self.Offset = None
        self.Limit = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCThresholdListResponse(AbstractModel):
    """DescribeCCThresholdList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 清洗阈值策略列表总数
        :type Total: int
        :param ThresholdList: 清洗阈值策略列表详情
        :type ThresholdList: list of CCThresholdPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ThresholdList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ThresholdList") is not None:
            self.ThresholdList = []
            for item in params.get("ThresholdList"):
                obj = CCThresholdPolicy()
                obj._deserialize(item)
                self.ThresholdList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param Ip: 资源的IP
        :type Ip: str
        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param StartTime: 统计开始时间
        :type StartTime: str
        :param EndTime: 统计结束时间
        :type EndTime: str
        :param MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :type MetricName: str
        :param Domain: 域名，可选
        :type Domain: str
        :param Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        """
        self.Business = None
        self.Ip = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Domain = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Domain = params.get("Domain")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 值个数
        :type Count: int
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param Ip: 资源的IP
        :type Ip: str
        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param StartTime: 统计开始时间
        :type StartTime: str
        :param EndTime: 统计结束时间
        :type EndTime: str
        :param Data: 值数组
        :type Data: list of int non-negative
        :param Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :type MetricName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Business = None
        self.Ip = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Id = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeCcBlackWhiteIpListRequest(AbstractModel):
    """DescribeCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgp-multip：表示高防包；bgpip：表示高防IP）
        :type Business: str
        :param InstanceId: 指定特定实例Id
        :type InstanceId: str
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        :param FilterIp: 筛选IP，需要筛选黑白名单IP时传该字段
        :type FilterIp: str
        :param FilterType: 黑白名单筛选字段，需要筛选黑白名单列表时传该字段
        :type FilterType: str
        """
        self.Business = None
        self.InstanceId = None
        self.Offset = None
        self.Limit = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None
        self.FilterIp = None
        self.FilterType = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.InstanceId = params.get("InstanceId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.FilterIp = params.get("FilterIp")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcBlackWhiteIpListResponse(AbstractModel):
    """DescribeCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: CC四层黑白名单策略列表总数
        :type Total: int
        :param CcBlackWhiteIpList: CC四层黑白名单策略列表详情
        :type CcBlackWhiteIpList: list of CcBlackWhiteIpPolicy
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.CcBlackWhiteIpList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("CcBlackWhiteIpList") is not None:
            self.CcBlackWhiteIpList = []
            for item in params.get("CcBlackWhiteIpList"):
                obj = CcBlackWhiteIpPolicy()
                obj._deserialize(item)
                self.CcBlackWhiteIpList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCcGeoIPBlockConfigListRequest(AbstractModel):
    """DescribeCcGeoIPBlockConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip-multip：表示高防包；bgpip：表示高防IP）
        :type Business: str
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param InstanceId: 指定特定实例ID
        :type InstanceId: str
        :param Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        """
        self.Business = None
        self.Offset = None
        self.Limit = None
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcGeoIPBlockConfigListResponse(AbstractModel):
    """DescribeCcGeoIPBlockConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: CC地域封禁策略列表总数
        :type Total: int
        :param CcGeoIpPolicyList: CC地域封禁策略列表详情
        :type CcGeoIpPolicyList: list of CcGeoIpPolicyNew
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.CcGeoIpPolicyList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("CcGeoIpPolicyList") is not None:
            self.CcGeoIpPolicyList = []
            for item in params.get("CcGeoIpPolicyList"):
                obj = CcGeoIpPolicyNew()
                obj._deserialize(item)
                self.CcGeoIpPolicyList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSBlackWhiteIpListRequest(AbstractModel):
    """DescribeDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self.InstanceId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlackWhiteIpListResponse(AbstractModel):
    """DescribeDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlackIpList: 黑名单IP列表
        :type BlackIpList: list of IpSegment
        :param WhiteIpList: 白名单IP列表
        :type WhiteIpList: list of IpSegment
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlackIpList = None
        self.WhiteIpList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BlackIpList") is not None:
            self.BlackIpList = []
            for item in params.get("BlackIpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self.BlackIpList.append(obj)
        if params.get("WhiteIpList") is not None:
            self.WhiteIpList = []
            for item in params.get("WhiteIpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self.WhiteIpList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSConnectLimitListRequest(AbstractModel):
    """DescribeDDoSConnectLimitList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数
        :type Limit: int
        :param FilterIp: 可选参数，按照IP进行过滤
        :type FilterIp: str
        :param FilterInstanceId: 可选参数，按照实例id进行过滤
        :type FilterInstanceId: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterIp = None
        self.FilterInstanceId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterIp = params.get("FilterIp")
        self.FilterInstanceId = params.get("FilterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSConnectLimitListResponse(AbstractModel):
    """DescribeDDoSConnectLimitList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 连接抑制配置总数
        :type Total: int
        :param ConfigList: 连接抑制配置详情信息
        :type ConfigList: list of ConnectLimitRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConnectLimitRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param Ip: 资源实例的IP
        :type Ip: str
        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param StartTime: 统计开始时间
        :type StartTime: str
        :param EndTime: 统计结束时间
        :type EndTime: str
        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        """
        self.Business = None
        self.Ip = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 值个数
        :type Count: int
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param Ip: 资源的IP
        :type Ip: str
        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param StartTime: 统计开始时间
        :type StartTime: str
        :param EndTime: 统计结束时间
        :type EndTime: str
        :param Data: 值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :type Data: list of int non-negative
        :param Id: 资源ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Business = None
        self.Ip = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.Data = None
        self.Id = None
        self.MetricName = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Business = params.get("Business")
        self.Ip = params.get("Ip")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Data = params.get("Data")
        self.Id = params.get("Id")
        self.MetricName = params.get("MetricName")
        self.RequestId = params.get("RequestId")


class DescribeDefaultAlarmThresholdRequest(AbstractModel):
    """DescribeDefaultAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceType: 产品类型，取值[
bgp(表示高防包产品)
bgpip(表示高防IP产品)
]
        :type InstanceType: str
        :param FilterAlarmType: 告警阈值类型搜索，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type FilterAlarmType: int
        """
        self.InstanceType = None
        self.FilterAlarmType = None


    def _deserialize(self, params):
        self.InstanceType = params.get("InstanceType")
        self.FilterAlarmType = params.get("FilterAlarmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultAlarmThresholdResponse(AbstractModel):
    """DescribeDefaultAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param DefaultAlarmConfigList: 默认告警阈值配置
        :type DefaultAlarmConfigList: list of DefaultAlarmThreshold
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DefaultAlarmConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DefaultAlarmConfigList") is not None:
            self.DefaultAlarmConfigList = []
            for item in params.get("DefaultAlarmConfigList"):
                obj = DefaultAlarmThreshold()
                obj._deserialize(item)
                self.DefaultAlarmConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeL7RulesBySSLCertIdRequest(AbstractModel):
    """DescribeL7RulesBySSLCertId请求参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 域名状态，可取bindable, binded, opened, closed, all，all表示全部状态
        :type Status: str
        :param CertIds: 证书ID列表
        :type CertIds: list of str
        """
        self.Status = None
        self.CertIds = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7RulesBySSLCertIdResponse(AbstractModel):
    """DescribeL7RulesBySSLCertId返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertSet: 证书规则集合
        :type CertSet: list of CertIdInsL7Rules
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self.CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdInsL7Rules()
                obj._deserialize(item)
                self.CertSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListBGPIPInstancesRequest(AbstractModel):
    """DescribeListBGPIPInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :type Limit: int
        :param FilterIp: IP搜索
        :type FilterIp: str
        :param FilterInstanceId: 资产实例ID搜索，例如，bgpip-00000001
        :type FilterInstanceId: str
        :param FilterLine: 高防IP线路搜索，取值为[
1：BGP线路
2：电信
3：联通
4：移动
99：第三方合作线路
]
        :type FilterLine: int
        :param FilterRegion: 地域搜索，例如，ap-guangzhou
        :type FilterRegion: str
        :param FilterName: 名称搜索
        :type FilterName: str
        :param FilterEipType: 是否只获取高防弹性公网IP实例。填写时，只能填写1或者0。当填写1时，表示返回高防弹性公网IP实例。当填写0时，表示返回非高防弹性公网IP实例。
        :type FilterEipType: int
        :param FilterEipEipAddressStatus: 高防弹性公网IP实例的绑定状态搜索条件，取值范围 [BINDING、 BIND、UNBINDING、UNBIND]。该搜索条件只在FilterEipType=1时才有效。
        :type FilterEipEipAddressStatus: list of str
        :param FilterDamDDoSStatus: 是否只获取安全加速实例。填写时，只能填写1或者0。当填写1时，表示返回安全加速实例。当填写0时，表示返回非安全加速实例。
        :type FilterDamDDoSStatus: int
        :param FilterStatus: 获取特定状态的资源，运行中填idle，攻击中填attacking，封堵中填blocking
        :type FilterStatus: str
        :param FilterCname: 获取特定的实例Cname
        :type FilterCname: str
        :param FilterInstanceIdList: 批量查询实例ID对应的高防IP实例资源
        :type FilterInstanceIdList: list of str
        :param FilterTag: 标签搜索
        :type FilterTag: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        :param FilterPackType: 按照套餐类型进行过滤
        :type FilterPackType: list of str
        """
        self.Offset = None
        self.Limit = None
        self.FilterIp = None
        self.FilterInstanceId = None
        self.FilterLine = None
        self.FilterRegion = None
        self.FilterName = None
        self.FilterEipType = None
        self.FilterEipEipAddressStatus = None
        self.FilterDamDDoSStatus = None
        self.FilterStatus = None
        self.FilterCname = None
        self.FilterInstanceIdList = None
        self.FilterTag = None
        self.FilterPackType = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterIp = params.get("FilterIp")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterLine = params.get("FilterLine")
        self.FilterRegion = params.get("FilterRegion")
        self.FilterName = params.get("FilterName")
        self.FilterEipType = params.get("FilterEipType")
        self.FilterEipEipAddressStatus = params.get("FilterEipEipAddressStatus")
        self.FilterDamDDoSStatus = params.get("FilterDamDDoSStatus")
        self.FilterStatus = params.get("FilterStatus")
        self.FilterCname = params.get("FilterCname")
        self.FilterInstanceIdList = params.get("FilterInstanceIdList")
        if params.get("FilterTag") is not None:
            self.FilterTag = TagFilter()
            self.FilterTag._deserialize(params.get("FilterTag"))
        self.FilterPackType = params.get("FilterPackType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBGPIPInstancesResponse(AbstractModel):
    """DescribeListBGPIPInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param InstanceList: 高防IP资产实例列表
        :type InstanceList: list of BGPIPInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = BGPIPInstance()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListBGPInstancesRequest(AbstractModel):
    """DescribeListBGPInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :type Limit: int
        :param FilterIp: IP搜索
        :type FilterIp: str
        :param FilterInstanceId: 资产实例ID搜索，例如，bgp-00000001
        :type FilterInstanceId: str
        :param FilterRegion: 地域搜索，例如，ap-guangzhou
        :type FilterRegion: str
        :param FilterName: 名称搜索
        :type FilterName: str
        :param FilterLine: 按照线路搜索, 1: BGP; 2: 三网
        :type FilterLine: int
        :param FilterStatus: 状态搜索，idle：运行中；attacking：攻击中；blocking：封堵中
        :type FilterStatus: str
        :param FilterBoundStatus: 高防包绑定状态搜索，bounding：绑定中； failed：绑定失败
        :type FilterBoundStatus: str
        :param FilterInstanceIdList: 实例id数组
        :type FilterInstanceIdList: list of str
        :param FilterEnterpriseFlag: 企业版搜索
        :type FilterEnterpriseFlag: int
        :param FilterTag: 标签搜索
        :type FilterTag: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        """
        self.Offset = None
        self.Limit = None
        self.FilterIp = None
        self.FilterInstanceId = None
        self.FilterRegion = None
        self.FilterName = None
        self.FilterLine = None
        self.FilterStatus = None
        self.FilterBoundStatus = None
        self.FilterInstanceIdList = None
        self.FilterEnterpriseFlag = None
        self.FilterTag = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterIp = params.get("FilterIp")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterRegion = params.get("FilterRegion")
        self.FilterName = params.get("FilterName")
        self.FilterLine = params.get("FilterLine")
        self.FilterStatus = params.get("FilterStatus")
        self.FilterBoundStatus = params.get("FilterBoundStatus")
        self.FilterInstanceIdList = params.get("FilterInstanceIdList")
        self.FilterEnterpriseFlag = params.get("FilterEnterpriseFlag")
        if params.get("FilterTag") is not None:
            self.FilterTag = TagFilter()
            self.FilterTag._deserialize(params.get("FilterTag"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBGPInstancesResponse(AbstractModel):
    """DescribeListBGPInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param InstanceList: 高防包资产实例列表
        :type InstanceList: list of BGPInstance
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = BGPInstance()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListBlackWhiteIpListRequest(AbstractModel):
    """DescribeListBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBlackWhiteIpListResponse(AbstractModel):
    """DescribeListBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param IpList: 黑白IP列表
        :type IpList: list of BlackWhiteIpRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.IpList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("IpList") is not None:
            self.IpList = []
            for item in params.get("IpList"):
                obj = BlackWhiteIpRelation()
                obj._deserialize(item)
                self.IpList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListDDoSAIRequest(AbstractModel):
    """DescribeListDDoSAI请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSAIResponse(AbstractModel):
    """DescribeListDDoSAI返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: AI防护开关列表
        :type ConfigList: list of DDoSAIRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSAIRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListDDoSGeoIPBlockConfigRequest(AbstractModel):
    """DescribeListDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSGeoIPBlockConfigResponse(AbstractModel):
    """DescribeListDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: DDoS区域封禁配置列表
        :type ConfigList: list of DDoSGeoIPBlockConfigRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSGeoIPBlockConfigRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListDDoSSpeedLimitConfigRequest(AbstractModel):
    """DescribeListDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSSpeedLimitConfigResponse(AbstractModel):
    """DescribeListDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: 访问限速配置列表
        :type ConfigList: list of DDoSSpeedLimitConfigRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSSpeedLimitConfigRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListIPAlarmConfigRequest(AbstractModel):
    """DescribeListIPAlarmConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterAlarmType: 告警阈值类型搜索，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type FilterAlarmType: int
        :param FilterIp: IP搜索
        :type FilterIp: str
        :param FilterCname: 高防IP实例资源的cname
        :type FilterCname: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterAlarmType = None
        self.FilterIp = None
        self.FilterCname = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterAlarmType = params.get("FilterAlarmType")
        self.FilterIp = params.get("FilterIp")
        self.FilterCname = params.get("FilterCname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListIPAlarmConfigResponse(AbstractModel):
    """DescribeListIPAlarmConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: IP告警阈值配置列表
        :type ConfigList: list of IPAlarmThresholdRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = IPAlarmThresholdRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListListenerRequest(AbstractModel):
    """DescribeListListener请求参数结构体

    """


class DescribeListListenerResponse(AbstractModel):
    """DescribeListListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param Layer4Listeners: 4层转发监听器列表
        :type Layer4Listeners: list of Layer4Rule
        :param Layer7Listeners: 7层转发监听器列表
        :type Layer7Listeners: list of Layer7Rule
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Layer4Listeners = None
        self.Layer7Listeners = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Layer4Listeners") is not None:
            self.Layer4Listeners = []
            for item in params.get("Layer4Listeners"):
                obj = Layer4Rule()
                obj._deserialize(item)
                self.Layer4Listeners.append(obj)
        if params.get("Layer7Listeners") is not None:
            self.Layer7Listeners = []
            for item in params.get("Layer7Listeners"):
                obj = Layer7Rule()
                obj._deserialize(item)
                self.Layer7Listeners.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListPacketFilterConfigRequest(AbstractModel):
    """DescribeListPacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListPacketFilterConfigResponse(AbstractModel):
    """DescribeListPacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: 特征过滤配置
        :type ConfigList: list of PacketFilterRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = PacketFilterRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListPortAclListRequest(AbstractModel):
    """DescribeListPortAclList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: ip搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListPortAclListResponse(AbstractModel):
    """DescribeListPortAclList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param AclList: 端口acl策略
        :type AclList: list of AclConfigRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.AclList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("AclList") is not None:
            self.AclList = []
            for item in params.get("AclList"):
                obj = AclConfigRelation()
                obj._deserialize(item)
                self.AclList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListProtectThresholdConfigRequest(AbstractModel):
    """DescribeListProtectThresholdConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        :param FilterDomain: 域名搜索(查询域名与协议的CC防护阈值时使用）
        :type FilterDomain: str
        :param FilterProtocol: 协议搜索(查询域名与协议的CC防护阈值时使用）
        :type FilterProtocol: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None
        self.FilterDomain = None
        self.FilterProtocol = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        self.FilterDomain = params.get("FilterDomain")
        self.FilterProtocol = params.get("FilterProtocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListProtectThresholdConfigResponse(AbstractModel):
    """DescribeListProtectThresholdConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总记录数
        :type Total: int
        :param ConfigList: 防护阈值配置列表
        :type ConfigList: list of ProtectThresholdRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProtectThresholdRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListProtocolBlockConfigRequest(AbstractModel):
    """DescribeListProtocolBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListProtocolBlockConfigResponse(AbstractModel):
    """DescribeListProtocolBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: 协议封禁配置
        :type ConfigList: list of ProtocolBlockRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProtocolBlockRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListSchedulingDomainRequest(AbstractModel):
    """DescribeListSchedulingDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :type Limit: int
        :param FilterDomain: 调度域名搜索
        :type FilterDomain: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterDomain = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterDomain = params.get("FilterDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListSchedulingDomainResponse(AbstractModel):
    """DescribeListSchedulingDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param DomainList: 调度域名信息列表
        :type DomainList: list of SchedulingDomainInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.DomainList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomainInfo()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListWaterPrintConfigRequest(AbstractModel):
    """DescribeListWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param FilterIp: IP搜索
        :type FilterIp: str
        """
        self.Offset = None
        self.Limit = None
        self.FilterInstanceId = None
        self.FilterIp = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.FilterInstanceId = params.get("FilterInstanceId")
        self.FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListWaterPrintConfigResponse(AbstractModel):
    """DescribeListWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 总数
        :type Total: int
        :param ConfigList: 水印配置列表
        :type ConfigList: list of WaterPrintRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.ConfigList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self.ConfigList = []
            for item in params.get("ConfigList"):
                obj = WaterPrintRelation()
                obj._deserialize(item)
                self.ConfigList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeNewL7RulesErrHealthRequest(AbstractModel):
    """DescribeNewL7RulesErrHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号(bgpip表示高防IP)
        :type Business: str
        :param RuleIdList: 规则Id列表
        :type RuleIdList: list of str
        """
        self.Business = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesErrHealthResponse(AbstractModel):
    """DescribeNewL7RulesErrHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP及错误信息，多个IP用","分割
        :type ErrHealths: list of KeyValue
        :param Total: 异常规则的总数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrHealths = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrHealths") is not None:
            self.ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self.ErrHealths.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeNewL7RulesRequest(AbstractModel):
    """DescribeNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type StatusList: list of int non-negative
        :param Domain: 域名搜索，选填，当需要搜索域名请填写
        :type Domain: str
        :param Ip: IP搜索，选填，当需要搜索IP请填写
        :type Ip: str
        :param Limit: 一页条数，填0表示不分页
        :type Limit: int
        :param Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param Cname: 高防IP实例的Cname
        :type Cname: str
        """
        self.Business = None
        self.StatusList = None
        self.Domain = None
        self.Ip = None
        self.Limit = None
        self.Offset = None
        self.ProtocolList = None
        self.Cname = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.StatusList = params.get("StatusList")
        self.Domain = params.get("Domain")
        self.Ip = params.get("Ip")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        self.ProtocolList = params.get("ProtocolList")
        self.Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesResponse(AbstractModel):
    """DescribeNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Rules: 转发规则列表
        :type Rules: list of NewL7RuleEntry
        :param Healths: 健康检查配置列表
        :type Healths: list of L7RuleHealth
        :param Total: 总规则数
        :type Total: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Rules = None
        self.Healths = None
        self.Total = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = NewL7RuleEntry()
                obj._deserialize(item)
                self.Rules.append(obj)
        if params.get("Healths") is not None:
            self.Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self.Healths.append(obj)
        self.Total = params.get("Total")
        self.RequestId = params.get("RequestId")


class DescribeOverviewAttackTrendRequest(AbstractModel):
    """DescribeOverviewAttackTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 攻击类型，取值ddos， cc
        :type Type: str
        :param Dimension: 纬度，当前仅支持attackcount
        :type Dimension: str
        :param Period: 周期，当前仅支持86400
        :type Period: int
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        """
        self.Type = None
        self.Dimension = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Dimension = params.get("Dimension")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewAttackTrendResponse(AbstractModel):
    """DescribeOverviewAttackTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 攻击类型
        :type Type: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Period: 周期
        :type Period: int
        :param Data: 每个周期点的攻击次数
        :type Data: list of int non-negative
        :param Count: 包含的周期点数
        :type Count: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Type = None
        self.StartTime = None
        self.EndTime = None
        self.Period = None
        self.Data = None
        self.Count = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Period = params.get("Period")
        self.Data = params.get("Data")
        self.Count = params.get("Count")
        self.RequestId = params.get("RequestId")


class DescribeOverviewCCTrendRequest(AbstractModel):
    """DescribeOverviewCCTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp-multip表示共享包；basic表示DDoS基础防护）
        :type Business: str
        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param StartTime: 统计开始时间
        :type StartTime: str
        :param EndTime: 统计结束时间
        :type EndTime: str
        :param MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :type MetricName: str
        :param IpList: 资源的IP
        :type IpList: list of str
        :param Id: 资源实例ID
        :type Id: str
        """
        self.Business = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.IpList = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.IpList = params.get("IpList")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewCCTrendResponse(AbstractModel):
    """DescribeOverviewCCTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 值个数
        :type Count: int
        :param Data: 值数组
        :type Data: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeOverviewDDoSEventListRequest(AbstractModel):
    """DescribeOverviewDDoSEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param AttackStatus: 可选按攻击状态过滤，start：攻击中；end：攻击结束
        :type AttackStatus: str
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 记录条数
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.AttackStatus = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AttackStatus = params.get("AttackStatus")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewDDoSEventListResponse(AbstractModel):
    """DescribeOverviewDDoSEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param Total: 记录总数
        :type Total: int
        :param EventList: 事件列表
        :type EventList: list of OverviewDDoSEvent
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.EventList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        if params.get("EventList") is not None:
            self.EventList = []
            for item in params.get("EventList"):
                obj = OverviewDDoSEvent()
                obj._deserialize(item)
                self.EventList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeOverviewDDoSTrendRequest(AbstractModel):
    """DescribeOverviewDDoSTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp-multip表示高防包；basic表示DDoS基础防护）
        :type Business: str
        :param Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param StartTime: 统计开始时间
        :type StartTime: str
        :param EndTime: 统计结束时间
        :type EndTime: str
        :param MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param IpList: 资源实例的IP列表
        :type IpList: list of str
        :param Id: 资源实例ID
        :type Id: str
        """
        self.Business = None
        self.Period = None
        self.StartTime = None
        self.EndTime = None
        self.MetricName = None
        self.IpList = None
        self.Id = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Period = params.get("Period")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricName = params.get("MetricName")
        self.IpList = params.get("IpList")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewDDoSTrendResponse(AbstractModel):
    """DescribeOverviewDDoSTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param Count: 值个数
        :type Count: int
        :param Data: 值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :type Data: list of int non-negative
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Count = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Count = params.get("Count")
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeOverviewIndexRequest(AbstractModel):
    """DescribeOverviewIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param StartTime: 拉取指标起始时间
        :type StartTime: str
        :param EndTime: 拉取指标结束时间
        :type EndTime: str
        """
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
        


class DescribeOverviewIndexResponse(AbstractModel):
    """DescribeOverviewIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param AllIpCount: IP总数
        :type AllIpCount: int
        :param AntiddosIpCount: 高防IP总数（包含高防包+高防IP）
        :type AntiddosIpCount: int
        :param AttackIpCount: 攻击IP总数
        :type AttackIpCount: int
        :param BlockIpCount: 封堵IP总数
        :type BlockIpCount: int
        :param AntiddosDomainCount: 高防域名总数
        :type AntiddosDomainCount: int
        :param AttackDomainCount: 攻击域名总数
        :type AttackDomainCount: int
        :param MaxAttackFlow: 攻击流量峰值
        :type MaxAttackFlow: int
        :param NewAttackTime: 当前最近一条攻击中的起始时间
        :type NewAttackTime: str
        :param NewAttackIp: 当前最近一条攻击中的IP
        :type NewAttackIp: str
        :param NewAttackType: 当前最近一条攻击中的攻击类型
        :type NewAttackType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllIpCount = None
        self.AntiddosIpCount = None
        self.AttackIpCount = None
        self.BlockIpCount = None
        self.AntiddosDomainCount = None
        self.AttackDomainCount = None
        self.MaxAttackFlow = None
        self.NewAttackTime = None
        self.NewAttackIp = None
        self.NewAttackType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllIpCount = params.get("AllIpCount")
        self.AntiddosIpCount = params.get("AntiddosIpCount")
        self.AttackIpCount = params.get("AttackIpCount")
        self.BlockIpCount = params.get("BlockIpCount")
        self.AntiddosDomainCount = params.get("AntiddosDomainCount")
        self.AttackDomainCount = params.get("AttackDomainCount")
        self.MaxAttackFlow = params.get("MaxAttackFlow")
        self.NewAttackTime = params.get("NewAttackTime")
        self.NewAttackIp = params.get("NewAttackIp")
        self.NewAttackType = params.get("NewAttackType")
        self.RequestId = params.get("RequestId")


class DisassociateDDoSEipAddressRequest(AbstractModel):
    """DisassociateDDoSEipAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :type InstanceId: str
        :param Eip: 资源实例ID对应的高防弹性公网IP。
        :type Eip: str
        """
        self.InstanceId = None
        self.Eip = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Eip = params.get("Eip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateDDoSEipAddressResponse(AbstractModel):
    """DisassociateDDoSEipAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EipAddressPackRelation(AbstractModel):
    """Anycast高防套餐详情

    """

    def __init__(self):
        r"""
        :param IpCount: 套餐IP数量
        :type IpCount: int
        :param AutoRenewFlag: 自动续费标记
        :type AutoRenewFlag: int
        :param CurDeadline: 当前到期时间
        :type CurDeadline: str
        """
        self.IpCount = None
        self.AutoRenewFlag = None
        self.CurDeadline = None


    def _deserialize(self, params):
        self.IpCount = params.get("IpCount")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAddressRelation(AbstractModel):
    """高防弹性公网IP关联信息

    """

    def __init__(self):
        r"""
        :param EipAddressRegion: 高防弹性公网IP绑定的实例地区，例如hk代表香港
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddressRegion: str
        :param EipBoundRscIns: 绑定的资源实例ID。可能是一个CVM。
注意：此字段可能返回 null，表示取不到有效值。
        :type EipBoundRscIns: str
        :param EipBoundRscEni: 绑定的弹性网卡ID
注意：此字段可能返回 null，表示取不到有效值。
        :type EipBoundRscEni: str
        :param EipBoundRscVip: 绑定的资源内网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type EipBoundRscVip: str
        :param ModifyTime: 修改时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyTime: str
        """
        self.EipAddressRegion = None
        self.EipBoundRscIns = None
        self.EipBoundRscEni = None
        self.EipBoundRscVip = None
        self.ModifyTime = None


    def _deserialize(self, params):
        self.EipAddressRegion = params.get("EipAddressRegion")
        self.EipBoundRscIns = params.get("EipBoundRscIns")
        self.EipBoundRscEni = params.get("EipBoundRscEni")
        self.EipBoundRscVip = params.get("EipBoundRscVip")
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipProductInfo(AbstractModel):
    """EIP所属的云产品信息

    """

    def __init__(self):
        r"""
        :param Ip: IP地址
        :type Ip: str
        :param BizType: 云产品类型，取值[
public（CVM产品），
bm（黑石产品），
eni（弹性网卡），
vpngw（VPN网关），
 natgw（NAT网关），
waf（Web应用安全产品），
fpc（金融产品），
gaap（GAAP产品）, 
other(托管IP)
]
        :type BizType: str
        :param DeviceType: 云产品子类型，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :type DeviceType: str
        :param InstanceId: IP所属的云产品实例ID，例如是弹性网卡的IP，InstanceId为弹性网卡的ID(eni-*); 如果是托管IP没有对应的资源实例ID,InstanceId为""
        :type InstanceId: str
        """
        self.Ip = None
        self.BizType = None
        self.DeviceType = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.BizType = params.get("BizType")
        self.DeviceType = params.get("DeviceType")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardListener(AbstractModel):
    """转发监听器

    """

    def __init__(self):
        r"""
        :param FrontendPort: 转发监听端口下限，取值1~65535
        :type FrontendPort: int
        :param ForwardProtocol: 转发协议，取值[
TCP
UDP
]
        :type ForwardProtocol: str
        :param FrontendPortEnd: 转发监听端口上限，取值1~65535
        :type FrontendPortEnd: int
        """
        self.FrontendPort = None
        self.ForwardProtocol = None
        self.FrontendPortEnd = None


    def _deserialize(self, params):
        self.FrontendPort = params.get("FrontendPort")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.FrontendPortEnd = params.get("FrontendPortEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPAlarmThresholdRelation(AbstractModel):
    """单IP告警阈值配置

    """

    def __init__(self):
        r"""
        :param AlarmType: 告警阈值类型，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type AlarmType: int
        :param AlarmThreshold: 告警阈值，单位Mbps，取值>=0；当作为输入参数时，设置0会删除告警阈值配置；
        :type AlarmThreshold: int
        :param InstanceDetailList: 告警阈值所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self.AlarmType = None
        self.AlarmThreshold = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        self.AlarmType = params.get("AlarmType")
        self.AlarmThreshold = params.get("AlarmThreshold")
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPLineInfo(AbstractModel):
    """IP线路信息

    """

    def __init__(self):
        r"""
        :param Type: IP线路类型，取值[
"bgp"：BGP线路IP
"ctcc"：电信线路IP
"cucc"：联通线路IP
"cmcc"：移动线路IP
"abroad"：境外线路IP
]
        :type Type: str
        :param Eip: 线路IP
        :type Eip: str
        :param Cname: 实例对应的cname
        :type Cname: str
        :param ResourceFlag: 资源flag，0：高防包资源，1：高防IP资源，2：非高防资源IP
        :type ResourceFlag: int
        """
        self.Type = None
        self.Eip = None
        self.Cname = None
        self.ResourceFlag = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Eip = params.get("Eip")
        self.Cname = params.get("Cname")
        self.ResourceFlag = params.get("ResourceFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsL7Rules(AbstractModel):
    """实例7层规则

    """

    def __init__(self):
        r"""
        :param Status: 规则状态，0: 正常运行中, 1: 配置规则中(配置生效中), 2: 配置规则失败（配置生效失败）, 3: 删除规则中(删除生效中), 5: 删除规则失败(删除失败), 6: 等待添加规则, 7: 等待删除规则, 8: 等待上传证书, 9: 规则对应的资源不存在，被隔离, 10:等待修改规则, 11:配置修改中
        :type Status: int
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议
        :type Protocol: str
        :param InsId: 实例ID
        :type InsId: str
        :param AppId: 用户AppID
        :type AppId: str
        :param VirtualPort: 高防端口
        :type VirtualPort: str
        :param SSLId: 证书ID
        :type SSLId: str
        """
        self.Status = None
        self.Domain = None
        self.Protocol = None
        self.InsId = None
        self.AppId = None
        self.VirtualPort = None
        self.SSLId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.InsId = params.get("InsId")
        self.AppId = params.get("AppId")
        self.VirtualPort = params.get("VirtualPort")
        self.SSLId = params.get("SSLId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRelation(AbstractModel):
    """资源实例IP信息

    """

    def __init__(self):
        r"""
        :param EipList: 资源实例的IP
        :type EipList: list of str
        :param InstanceId: 资源实例的ID
        :type InstanceId: str
        """
        self.EipList = None
        self.InstanceId = None


    def _deserialize(self, params):
        self.EipList = params.get("EipList")
        self.InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpSegment(AbstractModel):
    """ip段数据结构

    """

    def __init__(self):
        r"""
        :param Ip: ip地址
        :type Ip: str
        :param Mask: ip掩码，如果为32位ip，填0
        :type Mask: int
        """
        self.Ip = None
        self.Mask = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Mask = params.get("Mask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """字段值，K-V形式

    """

    def __init__(self):
        r"""
        :param Key: 字段名称
        :type Key: str
        :param Value: 字段取值
        :type Value: str
        """
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
        


class L4RuleSource(AbstractModel):
    """L4规则回源列表

    """

    def __init__(self):
        r"""
        :param Source: 回源IP或域名
        :type Source: str
        :param Weight: 权重值，取值[0,100]
        :type Weight: int
        :param Port: 8000
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param Backup: 备份源站，1: 备份源站，0: 普通源站
注意：此字段可能返回 null，表示取不到有效值。
        :type Backup: int
        """
        self.Source = None
        self.Weight = None
        self.Port = None
        self.Backup = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Weight = params.get("Weight")
        self.Port = params.get("Port")
        self.Backup = params.get("Backup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param Domain: 转发域名
        :type Domain: str
        :param Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param CCThreshold: HTTPS协议的CC防护阈值
        :type CCThreshold: int
        :param PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpsToHttpEnable: int
        :param CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param RuleName: 规则描述
        :type RuleName: str
        :param CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param VirtualPort: 接入端口值
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPort: int
        :param SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param Id: 同ruleId
        :type Id: str
        :param CCAIEnable: 智能cc开关，取值[0(关闭), 1(开启)]
        :type CCAIEnable: int
        """
        self.KeepTime = None
        self.Domain = None
        self.Protocol = None
        self.SourceType = None
        self.LbType = None
        self.SourceList = None
        self.KeepEnable = None
        self.Status = None
        self.RuleId = None
        self.CCThreshold = None
        self.PrivateKey = None
        self.CCEnable = None
        self.HttpsToHttpEnable = None
        self.CertType = None
        self.Cert = None
        self.CCLevel = None
        self.RuleName = None
        self.CCStatus = None
        self.VirtualPort = None
        self.SSLId = None
        self.Id = None
        self.CCAIEnable = None


    def _deserialize(self, params):
        self.KeepTime = params.get("KeepTime")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.SourceType = params.get("SourceType")
        self.LbType = params.get("LbType")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.KeepEnable = params.get("KeepEnable")
        self.Status = params.get("Status")
        self.RuleId = params.get("RuleId")
        self.CCThreshold = params.get("CCThreshold")
        self.PrivateKey = params.get("PrivateKey")
        self.CCEnable = params.get("CCEnable")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self.CertType = params.get("CertType")
        self.Cert = params.get("Cert")
        self.CCLevel = params.get("CCLevel")
        self.RuleName = params.get("RuleName")
        self.CCStatus = params.get("CCStatus")
        self.VirtualPort = params.get("VirtualPort")
        self.SSLId = params.get("SSLId")
        self.Id = params.get("Id")
        self.CCAIEnable = params.get("CCAIEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """L7规则健康检查参数

    """

    def __init__(self):
        r"""
        :param Status: 配置状态，0： 正常，1：配置中，2：配置失败
        :type Status: int
        :param Enable: =1表示开启；=0表示关闭
        :type Enable: int
        :param RuleId: 规则ID
        :type RuleId: str
        :param Url: 检查目录的URL，默认为/
        :type Url: str
        :param Interval: 检测间隔时间，单位秒
        :type Interval: int
        :param AliveNum: 健康阈值，单位次
        :type AliveNum: int
        :param KickNum: 不健康阈值，单位次
        :type KickNum: int
        :param Method: HTTP请求方式，取值[HEAD,GET]
        :type Method: str
        :param StatusCode: 健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :type StatusCode: int
        :param ProtocolFlag: 是否同时下发http和https规则健康检查配置
        :type ProtocolFlag: int
        :param PassiveEnable: 被动探测开关，=1表示开启；=0表示关闭
        :type PassiveEnable: int
        :param BlockInter: 被动探测不健康屏蔽时间
        :type BlockInter: int
        :param FailedCountInter: 被动探测不健康统计间隔
        :type FailedCountInter: int
        :param FailedThreshold: 被动探测不健康阈值
        :type FailedThreshold: int
        :param PassiveStatusCode: 被动探测判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :type PassiveStatusCode: int
        """
        self.Status = None
        self.Enable = None
        self.RuleId = None
        self.Url = None
        self.Interval = None
        self.AliveNum = None
        self.KickNum = None
        self.Method = None
        self.StatusCode = None
        self.ProtocolFlag = None
        self.PassiveEnable = None
        self.BlockInter = None
        self.FailedCountInter = None
        self.FailedThreshold = None
        self.PassiveStatusCode = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Enable = params.get("Enable")
        self.RuleId = params.get("RuleId")
        self.Url = params.get("Url")
        self.Interval = params.get("Interval")
        self.AliveNum = params.get("AliveNum")
        self.KickNum = params.get("KickNum")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.ProtocolFlag = params.get("ProtocolFlag")
        self.PassiveEnable = params.get("PassiveEnable")
        self.BlockInter = params.get("BlockInter")
        self.FailedCountInter = params.get("FailedCountInter")
        self.FailedThreshold = params.get("FailedThreshold")
        self.PassiveStatusCode = params.get("PassiveStatusCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Layer4Rule(AbstractModel):
    """4层转发规则

    """

    def __init__(self):
        r"""
        :param BackendPort: 源站端口，取值1~65535
        :type BackendPort: int
        :param FrontendPort: 转发端口，取值1~65535
        :type FrontendPort: int
        :param Protocol: 转发协议，取值[
TCP(TCP协议)
UDP(UDP协议)
]
        :type Protocol: str
        :param RealServers: 源站列表
        :type RealServers: list of SourceServer
        :param InstanceDetails: 资源实例
        :type InstanceDetails: list of InstanceRelation
        :param InstanceDetailRule: 规则所属的资源实例
        :type InstanceDetailRule: list of RuleInstanceRelation
        """
        self.BackendPort = None
        self.FrontendPort = None
        self.Protocol = None
        self.RealServers = None
        self.InstanceDetails = None
        self.InstanceDetailRule = None


    def _deserialize(self, params):
        self.BackendPort = params.get("BackendPort")
        self.FrontendPort = params.get("FrontendPort")
        self.Protocol = params.get("Protocol")
        if params.get("RealServers") is not None:
            self.RealServers = []
            for item in params.get("RealServers"):
                obj = SourceServer()
                obj._deserialize(item)
                self.RealServers.append(obj)
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        if params.get("InstanceDetailRule") is not None:
            self.InstanceDetailRule = []
            for item in params.get("InstanceDetailRule"):
                obj = RuleInstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Layer7Rule(AbstractModel):
    """7层转发规则

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param ProxyTypeList: 转发类型列表
        :type ProxyTypeList: list of ProxyTypeInfo
        :param RealServers: 源站列表
        :type RealServers: list of SourceServer
        :param InstanceDetails: 资源实例
        :type InstanceDetails: list of InstanceRelation
        :param InstanceDetailRule: 规则所属的资源实例
        :type InstanceDetailRule: list of RuleInstanceRelation
        """
        self.Domain = None
        self.ProxyTypeList = None
        self.RealServers = None
        self.InstanceDetails = None
        self.InstanceDetailRule = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("ProxyTypeList") is not None:
            self.ProxyTypeList = []
            for item in params.get("ProxyTypeList"):
                obj = ProxyTypeInfo()
                obj._deserialize(item)
                self.ProxyTypeList.append(obj)
        if params.get("RealServers") is not None:
            self.RealServers = []
            for item in params.get("RealServers"):
                obj = SourceServer()
                obj._deserialize(item)
                self.RealServers.append(obj)
        if params.get("InstanceDetails") is not None:
            self.InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetails.append(obj)
        if params.get("InstanceDetailRule") is not None:
            self.InstanceDetailRule = []
            for item in params.get("InstanceDetailRule"):
                obj = RuleInstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListenerCcThreholdConfig(AbstractModel):
    """域名与协议纬度的CC防护阈值

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议（可取值https）
        :type Protocol: str
        :param CCEnable: 开关状态（0：关闭，1：开启）
        :type CCEnable: int
        :param CCThreshold: cc防护阈值
        :type CCThreshold: int
        """
        self.Domain = None
        self.Protocol = None
        self.CCEnable = None
        self.CCThreshold = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelPolicyRequest(AbstractModel):
    """ModifyCCLevelPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP地址
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param Level: CC防护等级，可取值loose表示宽松，strict表示严格，normal表示适中， emergency表示攻击紧急， sup_loose表示超级宽松，default表示默认策略（无频控配置下发），customized表示自定义策略
        :type Level: str
        """
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None
        self.Level = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelPolicyResponse(AbstractModel):
    """ModifyCCLevelPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCCPrecisionPolicyRequest(AbstractModel):
    """ModifyCCPrecisionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param PolicyId: 策略Id
        :type PolicyId: str
        :param PolicyAction: 策略方式。可取值：alg、drop。alg指返回验证码方式验证，drop表示该访问丢弃。
        :type PolicyAction: str
        :param PolicyList: 策略记录
        :type PolicyList: list of CCPrecisionPlyRecord
        """
        self.InstanceId = None
        self.PolicyId = None
        self.PolicyAction = None
        self.PolicyList = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PolicyId = params.get("PolicyId")
        self.PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self.PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self.PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPrecisionPolicyResponse(AbstractModel):
    """ModifyCCPrecisionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCCReqLimitPolicyRequest(AbstractModel):
    """ModifyCCReqLimitPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param PolicyId: 策略Id
        :type PolicyId: str
        :param Policy: 策略项
        :type Policy: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        """
        self.InstanceId = None
        self.PolicyId = None
        self.Policy = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.PolicyId = params.get("PolicyId")
        if params.get("Policy") is not None:
            self.Policy = CCReqLimitPolicyRecord()
            self.Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCReqLimitPolicyResponse(AbstractModel):
    """ModifyCCReqLimitPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCCThresholdPolicyRequest(AbstractModel):
    """ModifyCCThresholdPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例Id
        :type InstanceId: str
        :param Ip: IP地址
        :type Ip: str
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param Threshold: 清洗阈值，-1表示开启“默认”模式
        :type Threshold: int
        """
        self.InstanceId = None
        self.Ip = None
        self.Domain = None
        self.Protocol = None
        self.Threshold = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Ip = params.get("Ip")
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCThresholdPolicyResponse(AbstractModel):
    """ModifyCCThresholdPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCcBlackWhiteIpListRequest(AbstractModel):
    """ModifyCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param IpList: IP列表
        :type IpList: list of IpSegment
        :param Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        :param PolicyId: 策略Id
        :type PolicyId: str
        """
        self.InstanceId = None
        self.IpList = None
        self.Type = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self.IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self.IpList.append(obj)
        self.Type = params.get("Type")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcBlackWhiteIpListResponse(AbstractModel):
    """ModifyCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDDoSBlackWhiteIpListRequest(AbstractModel):
    """ModifyDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源Id
        :type InstanceId: str
        :param OldIpType: 当前黑名单类型，取值black时黑名单；取值white时白名单
        :type OldIpType: str
        :param OldIp: 当前配置的Ip段，包含ip与掩码
        :type OldIp: :class:`tencentcloud.antiddos.v20200309.models.IpSegment`
        :param NewIpType: 修改后黑白名单类型，取值black时黑名单，取值white时白名单
        :type NewIpType: str
        :param NewIp: 当前配置的Ip段，包含ip与掩码
        :type NewIp: :class:`tencentcloud.antiddos.v20200309.models.IpSegment`
        """
        self.InstanceId = None
        self.OldIpType = None
        self.OldIp = None
        self.NewIpType = None
        self.NewIp = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OldIpType = params.get("OldIpType")
        if params.get("OldIp") is not None:
            self.OldIp = IpSegment()
            self.OldIp._deserialize(params.get("OldIp"))
        self.NewIpType = params.get("NewIpType")
        if params.get("NewIp") is not None:
            self.NewIp = IpSegment()
            self.NewIp._deserialize(params.get("NewIp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSBlackWhiteIpListResponse(AbstractModel):
    """ModifyDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDDoSGeoIPBlockConfigRequest(AbstractModel):
    """ModifyDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param DDoSGeoIPBlockConfig: DDoS区域封禁配置，填写参数时配置ID不能为空
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self.InstanceId = None
        self.DDoSGeoIPBlockConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self.DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self.DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSGeoIPBlockConfigResponse(AbstractModel):
    """ModifyDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param Id: 资源ID
        :type Id: str
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param Method: =get表示读取防护等级；=set表示修改防护等级
        :type Method: str
        :param DDoSLevel: 防护等级，取值[low,middle,high]；当Method=set时必填
        :type DDoSLevel: str
        """
        self.Id = None
        self.Business = None
        self.Method = None
        self.DDoSLevel = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Business = params.get("Business")
        self.Method = params.get("Method")
        self.DDoSLevel = params.get("DDoSLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param DDoSLevel: 防护等级，取值[low,middle,high]
        :type DDoSLevel: str
        :param Id: 资源ID
        :type Id: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DDoSLevel = None
        self.Id = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DDoSLevel = params.get("DDoSLevel")
        self.Id = params.get("Id")
        self.RequestId = params.get("RequestId")


class ModifyDDoSSpeedLimitConfigRequest(AbstractModel):
    """ModifyDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param DDoSSpeedLimitConfig: 访问限速配置，填写参数时配置ID不能为空
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self.InstanceId = None
        self.DDoSSpeedLimitConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self.DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self.DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSpeedLimitConfigResponse(AbstractModel):
    """ModifyDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param Threshold: DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
当设置值为0时，表示采用默认值；
        :type Threshold: int
        :param Id: 资源ID
        :type Id: str
        :param Business: 大禹子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        """
        self.Threshold = None
        self.Id = None
        self.Business = None


    def _deserialize(self, params):
        self.Threshold = params.get("Threshold")
        self.Id = params.get("Id")
        self.Business = params.get("Business")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyDomainUsrNameRequest(AbstractModel):
    """ModifyDomainUsrName请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainName: 用户CNAME
        :type DomainName: str
        :param DomainUserName: 域名名称
        :type DomainUserName: str
        """
        self.DomainName = None
        self.DomainUserName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.DomainUserName = params.get("DomainUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUsrNameResponse(AbstractModel):
    """ModifyDomainUsrName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyL7RulesEdgeRequest(AbstractModel):
    """ModifyL7RulesEdge请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（edge表示边界防护产品）
        :type Business: str
        :param Id: 资源ID
        :type Id: str
        :param Rule: 规则
        :type Rule: :class:`tencentcloud.antiddos.v20200309.models.L7RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = L7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyL7RulesEdgeResponse(AbstractModel):
    """ModifyL7RulesEdge返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param Business: 大禹子产品代号（bgpip表示高防IP）
        :type Business: str
        :param Id: 资源ID
        :type Id: str
        :param Rule: 域名转发规则
        :type Rule: :class:`tencentcloud.antiddos.v20200309.models.NewL7RuleEntry`
        """
        self.Business = None
        self.Id = None
        self.Rule = None


    def _deserialize(self, params):
        self.Business = params.get("Business")
        self.Id = params.get("Id")
        if params.get("Rule") is not None:
            self.Rule = NewL7RuleEntry()
            self.Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Success = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self.Success = SuccessCode()
            self.Success._deserialize(params.get("Success"))
        self.RequestId = params.get("RequestId")


class ModifyPacketFilterConfigRequest(AbstractModel):
    """ModifyPacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param PacketFilterConfig: 特征过滤配置
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self.InstanceId = None
        self.PacketFilterConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self.PacketFilterConfig = PacketFilterConfig()
            self.PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPacketFilterConfigResponse(AbstractModel):
    """ModifyPacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyPortAclConfigRequest(AbstractModel):
    """ModifyPortAclConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param OldAclConfig: 旧端口acl策略
        :type OldAclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        :param NewAclConfig: 新端口acl策略
        :type NewAclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self.InstanceId = None
        self.OldAclConfig = None
        self.NewAclConfig = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        if params.get("OldAclConfig") is not None:
            self.OldAclConfig = AclConfig()
            self.OldAclConfig._deserialize(params.get("OldAclConfig"))
        if params.get("NewAclConfig") is not None:
            self.NewAclConfig = AclConfig()
            self.NewAclConfig._deserialize(params.get("NewAclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPortAclConfigResponse(AbstractModel):
    """ModifyPortAclConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NewL7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param Domain: 转发域名
        :type Domain: str
        :param LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param Region: 区域码
        :type Region: int
        :param Id: 资源Id
        :type Id: str
        :param Ip: 资源Ip
        :type Ip: str
        :param RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param RuleName: 规则描述
        :type RuleName: str
        :param CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param CCThreshold: HTTPS协议的CC防护阈值
        :type CCThreshold: int
        :param CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        :param HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :type HttpsToHttpEnable: int
        :param VirtualPort: 接入端口值
注意：此字段可能返回 null，表示取不到有效值。
        :type VirtualPort: int
        :param RewriteHttps: http强制跳转https，1表示打开，0表示关闭
        :type RewriteHttps: int
        :param ErrCode: 规则配置失败时的详细错误原因(仅当Status=2时有效)，1001证书不存在，1002证书获取失败，1003证书上传失败，1004证书已过期
        :type ErrCode: int
        """
        self.Protocol = None
        self.Domain = None
        self.LbType = None
        self.KeepEnable = None
        self.KeepTime = None
        self.SourceType = None
        self.SourceList = None
        self.Region = None
        self.Id = None
        self.Ip = None
        self.RuleId = None
        self.RuleName = None
        self.CertType = None
        self.SSLId = None
        self.Cert = None
        self.PrivateKey = None
        self.Status = None
        self.CCStatus = None
        self.CCEnable = None
        self.CCThreshold = None
        self.CCLevel = None
        self.ModifyTime = None
        self.HttpsToHttpEnable = None
        self.VirtualPort = None
        self.RewriteHttps = None
        self.ErrCode = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Domain = params.get("Domain")
        self.LbType = params.get("LbType")
        self.KeepEnable = params.get("KeepEnable")
        self.KeepTime = params.get("KeepTime")
        self.SourceType = params.get("SourceType")
        if params.get("SourceList") is not None:
            self.SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self.SourceList.append(obj)
        self.Region = params.get("Region")
        self.Id = params.get("Id")
        self.Ip = params.get("Ip")
        self.RuleId = params.get("RuleId")
        self.RuleName = params.get("RuleName")
        self.CertType = params.get("CertType")
        self.SSLId = params.get("SSLId")
        self.Cert = params.get("Cert")
        self.PrivateKey = params.get("PrivateKey")
        self.Status = params.get("Status")
        self.CCStatus = params.get("CCStatus")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        self.CCLevel = params.get("CCLevel")
        self.ModifyTime = params.get("ModifyTime")
        self.HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self.VirtualPort = params.get("VirtualPort")
        self.RewriteHttps = params.get("RewriteHttps")
        self.ErrCode = params.get("ErrCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewDDoSEvent(AbstractModel):
    """防护概览DDoS攻击事件

    """

    def __init__(self):
        r"""
        :param Id: 事件Id
        :type Id: str
        :param Vip: ip
        :type Vip: str
        :param StartTime: 开始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param AttackType: 攻击类型
        :type AttackType: str
        :param AttackStatus: 攻击状态，0：攻击中；1：攻击结束
        :type AttackStatus: int
        :param Mbps: 攻击流量，单位Mbps
        :type Mbps: int
        :param Pps: 攻击包量，单位pps
        :type Pps: int
        :param Business: 业务类型，bgp-multip：高防包；bgpip：高防ip；basic：基础防护
        :type Business: str
        :param InstanceId: 高防实例Id
        :type InstanceId: str
        :param InstanceName: 高防实例名称
        :type InstanceName: str
        """
        self.Id = None
        self.Vip = None
        self.StartTime = None
        self.EndTime = None
        self.AttackType = None
        self.AttackStatus = None
        self.Mbps = None
        self.Pps = None
        self.Business = None
        self.InstanceId = None
        self.InstanceName = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Vip = params.get("Vip")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.AttackType = params.get("AttackType")
        self.AttackStatus = params.get("AttackStatus")
        self.Mbps = params.get("Mbps")
        self.Pps = params.get("Pps")
        self.Business = params.get("Business")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackInfo(AbstractModel):
    """套餐包信息

    """

    def __init__(self):
        r"""
        :param PackType: 套餐包的类型，取值[
staticpack：高防IP三网套餐包
insurance：保险套餐包
]
        :type PackType: str
        :param PackId: 套餐包的ID
        :type PackId: str
        """
        self.PackType = None
        self.PackId = None


    def _deserialize(self, params):
        self.PackType = params.get("PackType")
        self.PackId = params.get("PackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterConfig(AbstractModel):
    """特征过滤配置

    """

    def __init__(self):
        r"""
        :param Protocol: 协议，取值[tcp udp icmp all]
        :type Protocol: str
        :param SportStart: 起始源端口，取值0~65535
        :type SportStart: int
        :param SportEnd: 结束源端口，取值1~65535，必须大于等于起始源端口
        :type SportEnd: int
        :param DportStart: 起始目的端口，取值0~65535
        :type DportStart: int
        :param DportEnd: 结束目的端口，取值1~65535，必须大于等于起始目的端口
        :type DportEnd: int
        :param PktlenMin: 最小报文长度，取值1-1500
        :type PktlenMin: int
        :param PktlenMax: 最大报文长度，取值1-1500，必须大于等于最小报文长度
        :type PktlenMax: int
        :param Action: 动作，取值[
drop(丢弃)
transmit(放行)
drop_black(丢弃并拉黑)
drop_rst(拦截)
drop_black_rst(拦截并拉黑)
forward(继续防护)
]
        :type Action: str
        :param MatchBegin: 检测位置，取值[
begin_l3(IP头)
begin_l4(TCP/UDP头)
begin_l5(T载荷)
no_match(不匹配)
]
        :type MatchBegin: str
        :param MatchType: 检测类型，取值[
sunday(关键字)
pcre(正则表达式)
]
        :type MatchType: str
        :param Str: 检测值，关键字符串或正则表达式,取值[
当检测类型为sunday时，请填写字符串或者16进制字节码，例如\x313233对应的是字符串"123"的16进制字节码;
当检测类型为pcre时, 请填写正则表达式字符串;
]
        :type Str: str
        :param Depth: 从检测位置开始的检测深度，取值[0,1500]
        :type Depth: int
        :param Offset: 从检测位置开始的偏移量，取值范围[0,Depth]
        :type Offset: int
        :param IsNot: 是否包含检测值，取值[
0(包含)
1(不包含)
]
        :type IsNot: int
        :param MatchLogic: 当有第二个检测条件时，与第一检测条件的且或关系，取值[
and(且的关系)
none(当没有第二个检测条件时填写此值)
]
        :type MatchLogic: str
        :param MatchBegin2: 第二个检测位置，取值[
begin_l5(载荷)
no_match(不匹配)
]
        :type MatchBegin2: str
        :param MatchType2: 第二个检测类型，取值[
sunday(关键字)
pcre(正则表达式)
]
        :type MatchType2: str
        :param Str2: 第二个检测值，关键字符串或正则表达式,取值[
当检测类型为sunday时，请填写字符串或者16进制字节码，例如\x313233对应的是字符串"123"的16进制字节码;
当检测类型为pcre时, 请填写正则表达式字符串;
]
        :type Str2: str
        :param Depth2: 从第二个检测位置开始的第二个检测深度，取值[0,1500]
        :type Depth2: int
        :param Offset2: 从第二个检测位置开始的偏移量，取值范围[0,Depth2]
        :type Offset2: int
        :param IsNot2: 第二个检测是否包含检测值，取值[
0(包含)
1(不包含)
]
        :type IsNot2: int
        :param Id: 特征过滤配置添加成功后自动生成的规则ID，当添加新特征过滤配置时，此字段不用填写；
        :type Id: str
        """
        self.Protocol = None
        self.SportStart = None
        self.SportEnd = None
        self.DportStart = None
        self.DportEnd = None
        self.PktlenMin = None
        self.PktlenMax = None
        self.Action = None
        self.MatchBegin = None
        self.MatchType = None
        self.Str = None
        self.Depth = None
        self.Offset = None
        self.IsNot = None
        self.MatchLogic = None
        self.MatchBegin2 = None
        self.MatchType2 = None
        self.Str2 = None
        self.Depth2 = None
        self.Offset2 = None
        self.IsNot2 = None
        self.Id = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.SportStart = params.get("SportStart")
        self.SportEnd = params.get("SportEnd")
        self.DportStart = params.get("DportStart")
        self.DportEnd = params.get("DportEnd")
        self.PktlenMin = params.get("PktlenMin")
        self.PktlenMax = params.get("PktlenMax")
        self.Action = params.get("Action")
        self.MatchBegin = params.get("MatchBegin")
        self.MatchType = params.get("MatchType")
        self.Str = params.get("Str")
        self.Depth = params.get("Depth")
        self.Offset = params.get("Offset")
        self.IsNot = params.get("IsNot")
        self.MatchLogic = params.get("MatchLogic")
        self.MatchBegin2 = params.get("MatchBegin2")
        self.MatchType2 = params.get("MatchType2")
        self.Str2 = params.get("Str2")
        self.Depth2 = params.get("Depth2")
        self.Offset2 = params.get("Offset2")
        self.IsNot2 = params.get("IsNot2")
        self.Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterRelation(AbstractModel):
    """特征过滤相关信息

    """

    def __init__(self):
        r"""
        :param PacketFilterConfig: 特征过滤配置
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        :param InstanceDetailList: 特征过滤配置所属的实例
        :type InstanceDetailList: list of InstanceRelation
        :param ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self.PacketFilterConfig = None
        self.InstanceDetailList = None
        self.ModifyTime = None


    def _deserialize(self, params):
        if params.get("PacketFilterConfig") is not None:
            self.PacketFilterConfig = PacketFilterConfig()
            self.PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        self.ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortSegment(AbstractModel):
    """端口段信息

    """

    def __init__(self):
        r"""
        :param BeginPort: 起始端口，取值1~65535
        :type BeginPort: int
        :param EndPort: 结束端口，取值1~65535，必须不小于起始端口
        :type EndPort: int
        """
        self.BeginPort = None
        self.EndPort = None


    def _deserialize(self, params):
        self.BeginPort = params.get("BeginPort")
        self.EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtectThresholdRelation(AbstractModel):
    """防护阈值配置相关信息

    """

    def __init__(self):
        r"""
        :param DDoSLevel: DDoS防护等级，取值[
low(宽松)
middle(适中)
high(严格)
]
        :type DDoSLevel: str
        :param DDoSThreshold: DDoS清洗阈值，单位Mbps
        :type DDoSThreshold: int
        :param DDoSAI: DDoS的AI防护开关，取值[
on(开启)
off(关闭)
]
        :type DDoSAI: str
        :param CCEnable: CC清洗开关，取值[
0(关闭)
1(开启)
]
        :type CCEnable: int
        :param CCThreshold: CC清洗阈值，单位QPS
        :type CCThreshold: int
        :param InstanceDetailList: 所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        :param ListenerCcThresholdList: 域名与协议纬度的防护阈值
        :type ListenerCcThresholdList: list of ListenerCcThreholdConfig
        """
        self.DDoSLevel = None
        self.DDoSThreshold = None
        self.DDoSAI = None
        self.CCEnable = None
        self.CCThreshold = None
        self.InstanceDetailList = None
        self.ListenerCcThresholdList = None


    def _deserialize(self, params):
        self.DDoSLevel = params.get("DDoSLevel")
        self.DDoSThreshold = params.get("DDoSThreshold")
        self.DDoSAI = params.get("DDoSAI")
        self.CCEnable = params.get("CCEnable")
        self.CCThreshold = params.get("CCThreshold")
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        if params.get("ListenerCcThresholdList") is not None:
            self.ListenerCcThresholdList = []
            for item in params.get("ListenerCcThresholdList"):
                obj = ListenerCcThreholdConfig()
                obj._deserialize(item)
                self.ListenerCcThresholdList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockConfig(AbstractModel):
    """协议封禁配置

    """

    def __init__(self):
        r"""
        :param DropTcp: TCP封禁，取值[0(封禁关)，1(封禁开)]
        :type DropTcp: int
        :param DropUdp: UDP封禁，取值[0(封禁关)，1(封禁开)]
        :type DropUdp: int
        :param DropIcmp: ICMP封禁，取值[0(封禁关)，1(封禁开)]
        :type DropIcmp: int
        :param DropOther: 其他协议封禁，取值[0(封禁关)，1(封禁开)]
        :type DropOther: int
        :param CheckExceptNullConnect: 异常空连接防护，取值[0(防护关)，1(防护开)]
        :type CheckExceptNullConnect: int
        """
        self.DropTcp = None
        self.DropUdp = None
        self.DropIcmp = None
        self.DropOther = None
        self.CheckExceptNullConnect = None


    def _deserialize(self, params):
        self.DropTcp = params.get("DropTcp")
        self.DropUdp = params.get("DropUdp")
        self.DropIcmp = params.get("DropIcmp")
        self.DropOther = params.get("DropOther")
        self.CheckExceptNullConnect = params.get("CheckExceptNullConnect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockRelation(AbstractModel):
    """协议封禁相关信息

    """

    def __init__(self):
        r"""
        :param ProtocolBlockConfig: 协议封禁配置
        :type ProtocolBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        :param InstanceDetailList: 协议封禁配置所属的实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self.ProtocolBlockConfig = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        if params.get("ProtocolBlockConfig") is not None:
            self.ProtocolBlockConfig = ProtocolBlockConfig()
            self.ProtocolBlockConfig._deserialize(params.get("ProtocolBlockConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """Protocol、Port参数

    """

    def __init__(self):
        r"""
        :param Protocol: 协议（tcp；udp）
        :type Protocol: str
        :param Port: 端口
        :type Port: int
        """
        self.Protocol = None
        self.Port = None


    def _deserialize(self, params):
        self.Protocol = params.get("Protocol")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyTypeInfo(AbstractModel):
    """转发类型

    """

    def __init__(self):
        r"""
        :param ProxyPorts: 转发监听端口列表，端口取值1~65535
        :type ProxyPorts: list of int
        :param ProxyType: 转发协议，取值[
http(HTTP协议)
https(HTTPS协议)
]
        :type ProxyType: str
        """
        self.ProxyPorts = None
        self.ProxyType = None


    def _deserialize(self, params):
        self.ProxyPorts = params.get("ProxyPorts")
        self.ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        """
        self.Region = None


    def _deserialize(self, params):
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInstanceRelation(AbstractModel):
    """四七层规则的

    """

    def __init__(self):
        r"""
        :param EipList: 资源实例的IP
        :type EipList: list of str
        :param InstanceId: 资源实例的ID
        :type InstanceId: str
        :param Cname: 资源实例的Cname
        :type Cname: str
        """
        self.EipList = None
        self.InstanceId = None
        self.Cname = None


    def _deserialize(self, params):
        self.EipList = params.get("EipList")
        self.InstanceId = params.get("InstanceId")
        self.Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomainInfo(AbstractModel):
    """调度域名信息

    """

    def __init__(self):
        r"""
        :param Domain: 调度域名
        :type Domain: str
        :param LineIPList: 线路IP列表
        :type LineIPList: list of IPLineInfo
        :param Method: 调度方式，当前仅支持优先级的方式，取值[priority]
        :type Method: str
        :param TTL: 调度域名解析记录的TTL值
        :type TTL: int
        :param Status: 运行状态，取值[
0：未运行
1：运行中
2：运行异常
]
        :type Status: int
        :param CreatedTime: 创建时间
        :type CreatedTime: str
        :param ModifyTime: 最后修改时间
        :type ModifyTime: str
        :param UsrDomainName: 域名名称
注意：此字段可能返回 null，表示取不到有效值。
        :type UsrDomainName: str
        """
        self.Domain = None
        self.LineIPList = None
        self.Method = None
        self.TTL = None
        self.Status = None
        self.CreatedTime = None
        self.ModifyTime = None
        self.UsrDomainName = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("LineIPList") is not None:
            self.LineIPList = []
            for item in params.get("LineIPList"):
                obj = IPLineInfo()
                obj._deserialize(item)
                self.LineIPList.append(obj)
        self.Method = params.get("Method")
        self.TTL = params.get("TTL")
        self.Status = params.get("Status")
        self.CreatedTime = params.get("CreatedTime")
        self.ModifyTime = params.get("ModifyTime")
        self.UsrDomainName = params.get("UsrDomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceServer(AbstractModel):
    """源站信息

    """

    def __init__(self):
        r"""
        :param RealServer: 源站的地址（IP或者域名）
        :type RealServer: str
        :param RsType: 源站的地址类型，取值[
1(域名地址)
2(IP地址)
]
        :type RsType: int
        :param Weight: 源站的回源权重，取值1~100
        :type Weight: int
        """
        self.RealServer = None
        self.RsType = None
        self.Weight = None


    def _deserialize(self, params):
        self.RealServer = params.get("RealServer")
        self.RsType = params.get("RsType")
        self.Weight = params.get("Weight")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedValue(AbstractModel):
    """限速值类型，例如：包速率pps、带宽bps

    """

    def __init__(self):
        r"""
        :param Type: 限速值类型，取值[
1(包速率pps)
2(带宽bps)
]
        :type Type: int
        :param Value: 值大小
        :type Value: int
        """
        self.Type = None
        self.Value = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticPackRelation(AbstractModel):
    """三网高防套餐详情

    """

    def __init__(self):
        r"""
        :param ProtectBandwidth: 保底带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type ProtectBandwidth: int
        :param NormalBandwidth: 业务带宽
注意：此字段可能返回 null，表示取不到有效值。
        :type NormalBandwidth: int
        :param ForwardRulesLimit: 转发规则
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardRulesLimit: int
        :param AutoRenewFlag: 自动续费标记
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        :param CurDeadline: 到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CurDeadline: str
        """
        self.ProtectBandwidth = None
        self.NormalBandwidth = None
        self.ForwardRulesLimit = None
        self.AutoRenewFlag = None
        self.CurDeadline = None


    def _deserialize(self, params):
        self.ProtectBandwidth = params.get("ProtectBandwidth")
        self.NormalBandwidth = params.get("NormalBandwidth")
        self.ForwardRulesLimit = params.get("ForwardRulesLimit")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """操作返回码，只用于返回成功的情况

    """

    def __init__(self):
        r"""
        :param Message: 描述
        :type Message: str
        :param Code: 成功/错误码
        :type Code: str
        """
        self.Message = None
        self.Code = None


    def _deserialize(self, params):
        self.Message = params.get("Message")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchWaterPrintConfigRequest(AbstractModel):
    """SwitchWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 资源实例ID
        :type InstanceId: str
        :param OpenStatus: 水印开启/关闭状态，1表示开启；0表示关闭
        :type OpenStatus: int
        """
        self.InstanceId = None
        self.OpenStatus = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.OpenStatus = params.get("OpenStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchWaterPrintConfigResponse(AbstractModel):
    """SwitchWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TagFilter(AbstractModel):
    """标签类型

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签键值列表
        :type TagValue: list of str
        """
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
        


class TagInfo(AbstractModel):
    """标签信息，用于资源列表返回关联的标签

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
        :type TagValue: str
        """
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
        


class WaterPrintConfig(AbstractModel):
    """水印防护配置

    """

    def __init__(self):
        r"""
        :param Offset: 水印偏移量，取值范围[0, 100)
        :type Offset: int
        :param OpenStatus: 是否开启，取值[
0（手动开启）
1（立即运行）
]
        :type OpenStatus: int
        :param Listeners: 水印所属的转发监听器列表
        :type Listeners: list of ForwardListener
        :param Keys: 水印添加成功后生成的水印密钥列表，一条水印最少1个密钥，最多2个密钥
        :type Keys: list of WaterPrintKey
        :param Verify: 水印检查模式, 取值[
checkall（普通模式）
shortfpcheckall（精简模式）
]
        :type Verify: str
        """
        self.Offset = None
        self.OpenStatus = None
        self.Listeners = None
        self.Keys = None
        self.Verify = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.OpenStatus = params.get("OpenStatus")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ForwardListener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        if params.get("Keys") is not None:
            self.Keys = []
            for item in params.get("Keys"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self.Keys.append(obj)
        self.Verify = params.get("Verify")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """生成的水印密钥

    """

    def __init__(self):
        r"""
        :param KeyVersion: 密钥版本号
        :type KeyVersion: str
        :param KeyContent: 密钥内容
        :type KeyContent: str
        :param KeyId: 密钥ID
        :type KeyId: str
        :param KeyOpenStatus: 密钥启用状态，只有一个取值1(启用)
        :type KeyOpenStatus: int
        :param CreateTime: 密钥生成时间
        :type CreateTime: str
        """
        self.KeyVersion = None
        self.KeyContent = None
        self.KeyId = None
        self.KeyOpenStatus = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.KeyVersion = params.get("KeyVersion")
        self.KeyContent = params.get("KeyContent")
        self.KeyId = params.get("KeyId")
        self.KeyOpenStatus = params.get("KeyOpenStatus")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintRelation(AbstractModel):
    """水印配置相关信息

    """

    def __init__(self):
        r"""
        :param WaterPrintConfig: 水印配置
        :type WaterPrintConfig: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        :param InstanceDetailList: 水印配置所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self.WaterPrintConfig = None
        self.InstanceDetailList = None


    def _deserialize(self, params):
        if params.get("WaterPrintConfig") is not None:
            self.WaterPrintConfig = WaterPrintConfig()
            self.WaterPrintConfig._deserialize(params.get("WaterPrintConfig"))
        if params.get("InstanceDetailList") is not None:
            self.InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self.InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        