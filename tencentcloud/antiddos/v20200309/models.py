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
        :param _ForwardProtocol: 协议类型, 可取值tcp, udp, all
        :type ForwardProtocol: str
        :param _DPortStart: 目的端口起始，可取值范围0~65535
        :type DPortStart: int
        :param _DPortEnd: 目的端口结束，可取值范围0~65535
        :type DPortEnd: int
        :param _SPortStart: 来源端口起始，可取值范围0~65535
        :type SPortStart: int
        :param _SPortEnd: 来源端口结束，可取值范围0~65535
        :type SPortEnd: int
        :param _Action: 动作，可取值：drop， transmit， forward
        :type Action: str
        :param _Priority: 策略优先级，数字越小，级别越高，该规则越靠前匹配，取值1-1000
        :type Priority: int
        """
        self._ForwardProtocol = None
        self._DPortStart = None
        self._DPortEnd = None
        self._SPortStart = None
        self._SPortEnd = None
        self._Action = None
        self._Priority = None

    @property
    def ForwardProtocol(self):
        """协议类型, 可取值tcp, udp, all
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def DPortStart(self):
        """目的端口起始，可取值范围0~65535
        :rtype: int
        """
        return self._DPortStart

    @DPortStart.setter
    def DPortStart(self, DPortStart):
        self._DPortStart = DPortStart

    @property
    def DPortEnd(self):
        """目的端口结束，可取值范围0~65535
        :rtype: int
        """
        return self._DPortEnd

    @DPortEnd.setter
    def DPortEnd(self, DPortEnd):
        self._DPortEnd = DPortEnd

    @property
    def SPortStart(self):
        """来源端口起始，可取值范围0~65535
        :rtype: int
        """
        return self._SPortStart

    @SPortStart.setter
    def SPortStart(self, SPortStart):
        self._SPortStart = SPortStart

    @property
    def SPortEnd(self):
        """来源端口结束，可取值范围0~65535
        :rtype: int
        """
        return self._SPortEnd

    @SPortEnd.setter
    def SPortEnd(self, SPortEnd):
        self._SPortEnd = SPortEnd

    @property
    def Action(self):
        """动作，可取值：drop， transmit， forward
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Priority(self):
        """策略优先级，数字越小，级别越高，该规则越靠前匹配，取值1-1000
        :rtype: int
        """
        return self._Priority

    @Priority.setter
    def Priority(self, Priority):
        self._Priority = Priority


    def _deserialize(self, params):
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._DPortStart = params.get("DPortStart")
        self._DPortEnd = params.get("DPortEnd")
        self._SPortStart = params.get("SPortStart")
        self._SPortEnd = params.get("SPortEnd")
        self._Action = params.get("Action")
        self._Priority = params.get("Priority")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AclConfigRelation(AbstractModel):
    """端口acl策略配置与高防资源关联

    """

    def __init__(self):
        r"""
        :param _AclConfig: acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        :param _InstanceDetailList: 实例列表
        :type InstanceDetailList: list of InstanceRelation
        """
        self._AclConfig = None
        self._InstanceDetailList = None

    @property
    def AclConfig(self):
        """acl策略
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig

    @property
    def InstanceDetailList(self):
        """实例列表
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnycastOutPackRelation(AbstractModel):
    """Anycast转外套餐详情

    """

    def __init__(self):
        r"""
        :param _NormalBandwidth: 业务带宽(单位M)
        :type NormalBandwidth: int
        :param _ForwardRulesLimit: 转发规则数
        :type ForwardRulesLimit: int
        :param _AutoRenewFlag: 自动续费标记
        :type AutoRenewFlag: int
        :param _CurDeadline: 到期时间
        :type CurDeadline: str
        """
        self._NormalBandwidth = None
        self._ForwardRulesLimit = None
        self._AutoRenewFlag = None
        self._CurDeadline = None

    @property
    def NormalBandwidth(self):
        """业务带宽(单位M)
        :rtype: int
        """
        return self._NormalBandwidth

    @NormalBandwidth.setter
    def NormalBandwidth(self, NormalBandwidth):
        self._NormalBandwidth = NormalBandwidth

    @property
    def ForwardRulesLimit(self):
        """转发规则数
        :rtype: int
        """
        return self._ForwardRulesLimit

    @ForwardRulesLimit.setter
    def ForwardRulesLimit(self, ForwardRulesLimit):
        self._ForwardRulesLimit = ForwardRulesLimit

    @property
    def AutoRenewFlag(self):
        """自动续费标记
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        """到期时间
        :rtype: str
        """
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline


    def _deserialize(self, params):
        self._NormalBandwidth = params.get("NormalBandwidth")
        self._ForwardRulesLimit = params.get("ForwardRulesLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipAddressRequest(AbstractModel):
    """AssociateDDoSEipAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :type InstanceId: str
        :param _Eip: 资源实例ID对应的高防弹性公网IP。
        :type Eip: str
        :param _CvmInstanceID: 要绑定的实例 ID。实例 ID 形如：ins-11112222。可通过登录控制台查询，也可通过 DescribeInstances 接口返回值中的InstanceId获取。
        :type CvmInstanceID: str
        :param _CvmRegion: cvm实例所在地域，例如：ap-hongkong。
        :type CvmRegion: str
        """
        self._InstanceId = None
        self._Eip = None
        self._CvmInstanceID = None
        self._CvmRegion = None

    @property
    def InstanceId(self):
        """资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Eip(self):
        """资源实例ID对应的高防弹性公网IP。
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def CvmInstanceID(self):
        """要绑定的实例 ID。实例 ID 形如：ins-11112222。可通过登录控制台查询，也可通过 DescribeInstances 接口返回值中的InstanceId获取。
        :rtype: str
        """
        return self._CvmInstanceID

    @CvmInstanceID.setter
    def CvmInstanceID(self, CvmInstanceID):
        self._CvmInstanceID = CvmInstanceID

    @property
    def CvmRegion(self):
        """cvm实例所在地域，例如：ap-hongkong。
        :rtype: str
        """
        return self._CvmRegion

    @CvmRegion.setter
    def CvmRegion(self, CvmRegion):
        self._CvmRegion = CvmRegion


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Eip = params.get("Eip")
        self._CvmInstanceID = params.get("CvmInstanceID")
        self._CvmRegion = params.get("CvmRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipAddressResponse(AbstractModel):
    """AssociateDDoSEipAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AssociateDDoSEipLoadBalancerRequest(AbstractModel):
    """AssociateDDoSEipLoadBalancer请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :type InstanceId: str
        :param _Eip: 资源实例ID对应的高防弹性公网IP。
        :type Eip: str
        :param _LoadBalancerID: 要绑定的负载均衡ID。负载均衡 ID 形如：lb-0000002i。可通过登录控制台查询，也可通过 DescribeLoadBalancers 接口返回值中的LoadBalancerId获取。
        :type LoadBalancerID: str
        :param _LoadBalancerRegion: CLB所在地域，例如：ap-hongkong。
        :type LoadBalancerRegion: str
        :param _Vip: CLB内网IP
        :type Vip: str
        """
        self._InstanceId = None
        self._Eip = None
        self._LoadBalancerID = None
        self._LoadBalancerRegion = None
        self._Vip = None

    @property
    def InstanceId(self):
        """资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Eip(self):
        """资源实例ID对应的高防弹性公网IP。
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def LoadBalancerID(self):
        """要绑定的负载均衡ID。负载均衡 ID 形如：lb-0000002i。可通过登录控制台查询，也可通过 DescribeLoadBalancers 接口返回值中的LoadBalancerId获取。
        :rtype: str
        """
        return self._LoadBalancerID

    @LoadBalancerID.setter
    def LoadBalancerID(self, LoadBalancerID):
        self._LoadBalancerID = LoadBalancerID

    @property
    def LoadBalancerRegion(self):
        """CLB所在地域，例如：ap-hongkong。
        :rtype: str
        """
        return self._LoadBalancerRegion

    @LoadBalancerRegion.setter
    def LoadBalancerRegion(self, LoadBalancerRegion):
        self._LoadBalancerRegion = LoadBalancerRegion

    @property
    def Vip(self):
        """CLB内网IP
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Eip = params.get("Eip")
        self._LoadBalancerID = params.get("LoadBalancerID")
        self._LoadBalancerRegion = params.get("LoadBalancerRegion")
        self._Vip = params.get("Vip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AssociateDDoSEipLoadBalancerResponse(AbstractModel):
    """AssociateDDoSEipLoadBalancer返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class BGPIPInstance(AbstractModel):
    """高防IP资产实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceDetail: 资产实例的详细信息
        :type InstanceDetail: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        :param _SpecificationLimit: 资产实例的规格信息
        :type SpecificationLimit: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceSpecification`
        :param _Usage: 资产实例的使用统计信息
        :type Usage: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceUsages`
        :param _Region: 资产实例所在的地域
        :type Region: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        :param _Status: 资产实例的防护状态，状态码如下：
"idle"：正常状态(无攻击)
"attacking"：攻击中
"blocking"：封堵中
"creating"：创建中
"deblocking"：解封中
"isolate"：回收隔离中
        :type Status: str
        :param _ExpiredTime: 到期时间
        :type ExpiredTime: str
        :param _CreatedTime: 购买时间
        :type CreatedTime: str
        :param _Name: 资产实例的名称
        :type Name: str
        :param _PackInfo: 资产实例所属的套餐包信息，
注意：当资产实例不是套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type PackInfo: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        :param _StaticPackRelation: 资产实例所属的三网套餐包详情，
注意：当资产实例不是三网套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type StaticPackRelation: :class:`tencentcloud.antiddos.v20200309.models.StaticPackRelation`
        :param _ZoneId: 区分高防IP境外线路
        :type ZoneId: int
        :param _Tgw: 区分集群
        :type Tgw: int
        :param _EipAddressStatus: 高防弹性公网IP状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)。只对高防弹性公网IP实例有效。
        :type EipAddressStatus: str
        :param _EipFlag: 是否高防弹性公网IP实例，是为1，否为0。
        :type EipFlag: int
        :param _EipAddressPackRelation: 资产实例所属的高防弹性公网IP套餐包详情，
注意：当资产实例不是高防弹性公网IP套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddressPackRelation: :class:`tencentcloud.antiddos.v20200309.models.EipAddressPackRelation`
        :param _EipAddressInfo: 高防弹性公网IP关联的实例信息。
注意：当资产实例不是高防弹性公网IP实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type EipAddressInfo: :class:`tencentcloud.antiddos.v20200309.models.EipAddressRelation`
        :param _Domain: 建议客户接入的域名，客户可使用域名接入。
        :type Domain: str
        :param _DamDDoSStatus: 是否开启安全加速，是为1，否为0。
        :type DamDDoSStatus: int
        :param _V6Flag: 是否Ipv6版本的IP, 是为1，否为0
        :type V6Flag: int
        :param _BGPIPChannelFlag: 是否渠道版高防IP，是为1，否为0
        :type BGPIPChannelFlag: int
        :param _TagInfoList: 资源关联标签
        :type TagInfoList: list of TagInfo
        :param _AnycastOutPackRelation: 资产实例所属的全力防护套餐包详情，
注意：当资产实例不是全力防护套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type AnycastOutPackRelation: :class:`tencentcloud.antiddos.v20200309.models.AnycastOutPackRelation`
        :param _InstanceVersion: 资源实例版本
        :type InstanceVersion: int
        :param _ConvoyId: 重保实例
        :type ConvoyId: str
        :param _ElasticBandwidth: 带宽后付费
        :type ElasticBandwidth: int
        :param _EOFlag: 是否为EO代播的ip: 1是，0不是
        :type EOFlag: int
        """
        self._InstanceDetail = None
        self._SpecificationLimit = None
        self._Usage = None
        self._Region = None
        self._Status = None
        self._ExpiredTime = None
        self._CreatedTime = None
        self._Name = None
        self._PackInfo = None
        self._StaticPackRelation = None
        self._ZoneId = None
        self._Tgw = None
        self._EipAddressStatus = None
        self._EipFlag = None
        self._EipAddressPackRelation = None
        self._EipAddressInfo = None
        self._Domain = None
        self._DamDDoSStatus = None
        self._V6Flag = None
        self._BGPIPChannelFlag = None
        self._TagInfoList = None
        self._AnycastOutPackRelation = None
        self._InstanceVersion = None
        self._ConvoyId = None
        self._ElasticBandwidth = None
        self._EOFlag = None

    @property
    def InstanceDetail(self):
        """资产实例的详细信息
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        """
        return self._InstanceDetail

    @InstanceDetail.setter
    def InstanceDetail(self, InstanceDetail):
        self._InstanceDetail = InstanceDetail

    @property
    def SpecificationLimit(self):
        """资产实例的规格信息
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceSpecification`
        """
        return self._SpecificationLimit

    @SpecificationLimit.setter
    def SpecificationLimit(self, SpecificationLimit):
        self._SpecificationLimit = SpecificationLimit

    @property
    def Usage(self):
        """资产实例的使用统计信息
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.BGPIPInstanceUsages`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Region(self):
        """资产实例所在的地域
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """资产实例的防护状态，状态码如下：
"idle"：正常状态(无攻击)
"attacking"：攻击中
"blocking"：封堵中
"creating"：创建中
"deblocking"：解封中
"isolate"：回收隔离中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpiredTime(self):
        """到期时间
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def CreatedTime(self):
        """购买时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def Name(self):
        """资产实例的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PackInfo(self):
        """资产实例所属的套餐包信息，
注意：当资产实例不是套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        """
        return self._PackInfo

    @PackInfo.setter
    def PackInfo(self, PackInfo):
        self._PackInfo = PackInfo

    @property
    def StaticPackRelation(self):
        """资产实例所属的三网套餐包详情，
注意：当资产实例不是三网套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.StaticPackRelation`
        """
        return self._StaticPackRelation

    @StaticPackRelation.setter
    def StaticPackRelation(self, StaticPackRelation):
        self._StaticPackRelation = StaticPackRelation

    @property
    def ZoneId(self):
        """区分高防IP境外线路
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Tgw(self):
        """区分集群
        :rtype: int
        """
        return self._Tgw

    @Tgw.setter
    def Tgw(self, Tgw):
        self._Tgw = Tgw

    @property
    def EipAddressStatus(self):
        """高防弹性公网IP状态，包含'CREATING'(创建中),'BINDING'(绑定中),'BIND'(已绑定),'UNBINDING'(解绑中),'UNBIND'(已解绑),'OFFLINING'(释放中),'BIND_ENI'(绑定悬空弹性网卡)。只对高防弹性公网IP实例有效。
        :rtype: str
        """
        return self._EipAddressStatus

    @EipAddressStatus.setter
    def EipAddressStatus(self, EipAddressStatus):
        self._EipAddressStatus = EipAddressStatus

    @property
    def EipFlag(self):
        """是否高防弹性公网IP实例，是为1，否为0。
        :rtype: int
        """
        return self._EipFlag

    @EipFlag.setter
    def EipFlag(self, EipFlag):
        self._EipFlag = EipFlag

    @property
    def EipAddressPackRelation(self):
        """资产实例所属的高防弹性公网IP套餐包详情，
注意：当资产实例不是高防弹性公网IP套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.EipAddressPackRelation`
        """
        return self._EipAddressPackRelation

    @EipAddressPackRelation.setter
    def EipAddressPackRelation(self, EipAddressPackRelation):
        self._EipAddressPackRelation = EipAddressPackRelation

    @property
    def EipAddressInfo(self):
        """高防弹性公网IP关联的实例信息。
注意：当资产实例不是高防弹性公网IP实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.EipAddressRelation`
        """
        return self._EipAddressInfo

    @EipAddressInfo.setter
    def EipAddressInfo(self, EipAddressInfo):
        self._EipAddressInfo = EipAddressInfo

    @property
    def Domain(self):
        """建议客户接入的域名，客户可使用域名接入。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def DamDDoSStatus(self):
        """是否开启安全加速，是为1，否为0。
        :rtype: int
        """
        return self._DamDDoSStatus

    @DamDDoSStatus.setter
    def DamDDoSStatus(self, DamDDoSStatus):
        self._DamDDoSStatus = DamDDoSStatus

    @property
    def V6Flag(self):
        """是否Ipv6版本的IP, 是为1，否为0
        :rtype: int
        """
        return self._V6Flag

    @V6Flag.setter
    def V6Flag(self, V6Flag):
        self._V6Flag = V6Flag

    @property
    def BGPIPChannelFlag(self):
        """是否渠道版高防IP，是为1，否为0
        :rtype: int
        """
        return self._BGPIPChannelFlag

    @BGPIPChannelFlag.setter
    def BGPIPChannelFlag(self, BGPIPChannelFlag):
        self._BGPIPChannelFlag = BGPIPChannelFlag

    @property
    def TagInfoList(self):
        """资源关联标签
        :rtype: list of TagInfo
        """
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList

    @property
    def AnycastOutPackRelation(self):
        """资产实例所属的全力防护套餐包详情，
注意：当资产实例不是全力防护套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AnycastOutPackRelation`
        """
        return self._AnycastOutPackRelation

    @AnycastOutPackRelation.setter
    def AnycastOutPackRelation(self, AnycastOutPackRelation):
        self._AnycastOutPackRelation = AnycastOutPackRelation

    @property
    def InstanceVersion(self):
        """资源实例版本
        :rtype: int
        """
        return self._InstanceVersion

    @InstanceVersion.setter
    def InstanceVersion(self, InstanceVersion):
        self._InstanceVersion = InstanceVersion

    @property
    def ConvoyId(self):
        """重保实例
        :rtype: str
        """
        return self._ConvoyId

    @ConvoyId.setter
    def ConvoyId(self, ConvoyId):
        self._ConvoyId = ConvoyId

    @property
    def ElasticBandwidth(self):
        """带宽后付费
        :rtype: int
        """
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth

    @property
    def EOFlag(self):
        """是否为EO代播的ip: 1是，0不是
        :rtype: int
        """
        return self._EOFlag

    @EOFlag.setter
    def EOFlag(self, EOFlag):
        self._EOFlag = EOFlag


    def _deserialize(self, params):
        if params.get("InstanceDetail") is not None:
            self._InstanceDetail = InstanceRelation()
            self._InstanceDetail._deserialize(params.get("InstanceDetail"))
        if params.get("SpecificationLimit") is not None:
            self._SpecificationLimit = BGPIPInstanceSpecification()
            self._SpecificationLimit._deserialize(params.get("SpecificationLimit"))
        if params.get("Usage") is not None:
            self._Usage = BGPIPInstanceUsages()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Region") is not None:
            self._Region = RegionInfo()
            self._Region._deserialize(params.get("Region"))
        self._Status = params.get("Status")
        self._ExpiredTime = params.get("ExpiredTime")
        self._CreatedTime = params.get("CreatedTime")
        self._Name = params.get("Name")
        if params.get("PackInfo") is not None:
            self._PackInfo = PackInfo()
            self._PackInfo._deserialize(params.get("PackInfo"))
        if params.get("StaticPackRelation") is not None:
            self._StaticPackRelation = StaticPackRelation()
            self._StaticPackRelation._deserialize(params.get("StaticPackRelation"))
        self._ZoneId = params.get("ZoneId")
        self._Tgw = params.get("Tgw")
        self._EipAddressStatus = params.get("EipAddressStatus")
        self._EipFlag = params.get("EipFlag")
        if params.get("EipAddressPackRelation") is not None:
            self._EipAddressPackRelation = EipAddressPackRelation()
            self._EipAddressPackRelation._deserialize(params.get("EipAddressPackRelation"))
        if params.get("EipAddressInfo") is not None:
            self._EipAddressInfo = EipAddressRelation()
            self._EipAddressInfo._deserialize(params.get("EipAddressInfo"))
        self._Domain = params.get("Domain")
        self._DamDDoSStatus = params.get("DamDDoSStatus")
        self._V6Flag = params.get("V6Flag")
        self._BGPIPChannelFlag = params.get("BGPIPChannelFlag")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        if params.get("AnycastOutPackRelation") is not None:
            self._AnycastOutPackRelation = AnycastOutPackRelation()
            self._AnycastOutPackRelation._deserialize(params.get("AnycastOutPackRelation"))
        self._InstanceVersion = params.get("InstanceVersion")
        self._ConvoyId = params.get("ConvoyId")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        self._EOFlag = params.get("EOFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPInstanceSpecification(AbstractModel):
    """高防IP资产实例的规格信息

    """

    def __init__(self):
        r"""
        :param _ProtectBandwidth: 保底防护峰值，单位Mbps
        :type ProtectBandwidth: int
        :param _ProtectCCQPS: CC防护峰值，单位qps
        :type ProtectCCQPS: int
        :param _NormalBandwidth: 正常业务带宽，单位Mbps
        :type NormalBandwidth: int
        :param _ForwardRulesLimit: 转发规则数，单位条
        :type ForwardRulesLimit: int
        :param _AutoRenewFlag: 自动续费状态，取值[
0：没有开启自动续费
1：开启了自动续费
]
        :type AutoRenewFlag: int
        :param _Line: 高防IP线路，取值为[
1：BGP线路
2：电信
3：联通
4：移动
99：第三方合作线路
]
        :type Line: int
        :param _ElasticBandwidth: 弹性防护峰值，单位Mbps
        :type ElasticBandwidth: int
        """
        self._ProtectBandwidth = None
        self._ProtectCCQPS = None
        self._NormalBandwidth = None
        self._ForwardRulesLimit = None
        self._AutoRenewFlag = None
        self._Line = None
        self._ElasticBandwidth = None

    @property
    def ProtectBandwidth(self):
        """保底防护峰值，单位Mbps
        :rtype: int
        """
        return self._ProtectBandwidth

    @ProtectBandwidth.setter
    def ProtectBandwidth(self, ProtectBandwidth):
        self._ProtectBandwidth = ProtectBandwidth

    @property
    def ProtectCCQPS(self):
        """CC防护峰值，单位qps
        :rtype: int
        """
        return self._ProtectCCQPS

    @ProtectCCQPS.setter
    def ProtectCCQPS(self, ProtectCCQPS):
        self._ProtectCCQPS = ProtectCCQPS

    @property
    def NormalBandwidth(self):
        """正常业务带宽，单位Mbps
        :rtype: int
        """
        return self._NormalBandwidth

    @NormalBandwidth.setter
    def NormalBandwidth(self, NormalBandwidth):
        self._NormalBandwidth = NormalBandwidth

    @property
    def ForwardRulesLimit(self):
        """转发规则数，单位条
        :rtype: int
        """
        return self._ForwardRulesLimit

    @ForwardRulesLimit.setter
    def ForwardRulesLimit(self, ForwardRulesLimit):
        self._ForwardRulesLimit = ForwardRulesLimit

    @property
    def AutoRenewFlag(self):
        """自动续费状态，取值[
0：没有开启自动续费
1：开启了自动续费
]
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def Line(self):
        """高防IP线路，取值为[
1：BGP线路
2：电信
3：联通
4：移动
99：第三方合作线路
]
        :rtype: int
        """
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def ElasticBandwidth(self):
        """弹性防护峰值，单位Mbps
        :rtype: int
        """
        return self._ElasticBandwidth

    @ElasticBandwidth.setter
    def ElasticBandwidth(self, ElasticBandwidth):
        self._ElasticBandwidth = ElasticBandwidth


    def _deserialize(self, params):
        self._ProtectBandwidth = params.get("ProtectBandwidth")
        self._ProtectCCQPS = params.get("ProtectCCQPS")
        self._NormalBandwidth = params.get("NormalBandwidth")
        self._ForwardRulesLimit = params.get("ForwardRulesLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._Line = params.get("Line")
        self._ElasticBandwidth = params.get("ElasticBandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPInstanceUsages(AbstractModel):
    """高防IP资产实例的使用信息统计

    """

    def __init__(self):
        r"""
        :param _PortRulesUsage: 已使用的端口规则数，单位条
        :type PortRulesUsage: int
        :param _DomainRulesUsage: 已使用的域名规则数，单位条
        :type DomainRulesUsage: int
        :param _Last7DayAttackCount: 最近7天的攻击次数，单位次
        :type Last7DayAttackCount: int
        """
        self._PortRulesUsage = None
        self._DomainRulesUsage = None
        self._Last7DayAttackCount = None

    @property
    def PortRulesUsage(self):
        """已使用的端口规则数，单位条
        :rtype: int
        """
        return self._PortRulesUsage

    @PortRulesUsage.setter
    def PortRulesUsage(self, PortRulesUsage):
        self._PortRulesUsage = PortRulesUsage

    @property
    def DomainRulesUsage(self):
        """已使用的域名规则数，单位条
        :rtype: int
        """
        return self._DomainRulesUsage

    @DomainRulesUsage.setter
    def DomainRulesUsage(self, DomainRulesUsage):
        self._DomainRulesUsage = DomainRulesUsage

    @property
    def Last7DayAttackCount(self):
        """最近7天的攻击次数，单位次
        :rtype: int
        """
        return self._Last7DayAttackCount

    @Last7DayAttackCount.setter
    def Last7DayAttackCount(self, Last7DayAttackCount):
        self._Last7DayAttackCount = Last7DayAttackCount


    def _deserialize(self, params):
        self._PortRulesUsage = params.get("PortRulesUsage")
        self._DomainRulesUsage = params.get("DomainRulesUsage")
        self._Last7DayAttackCount = params.get("Last7DayAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPIPL7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param _Domain: 转发域名
        :type Domain: str
        :param _LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _Region: 区域码
        :type Region: int
        :param _Id: 资源Id
        :type Id: str
        :param _Ip: 资源Ip
        :type Ip: str
        :param _RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param _SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param _Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param _PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param _Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param _CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param _CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param _CCThreshold: HTTPS协议的CC防护阈值（已废弃）
        :type CCThreshold: int
        :param _CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :type HttpsToHttpEnable: int
        :param _VirtualPort: 接入端口值
        :type VirtualPort: int
        :param _RewriteHttps: http强制跳转https，1表示打开，0表示关闭
        :type RewriteHttps: int
        :param _ErrCode: 规则配置失败时的详细错误原因(仅当Status=2时有效)，1001证书不存在，1002证书获取失败，1003证书上传失败，1004证书已过期
        :type ErrCode: int
        :param _Version: 版本
        :type Version: int
        """
        self._Protocol = None
        self._Domain = None
        self._LbType = None
        self._KeepEnable = None
        self._KeepTime = None
        self._SourceType = None
        self._SourceList = None
        self._Region = None
        self._Id = None
        self._Ip = None
        self._RuleId = None
        self._RuleName = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCLevel = None
        self._ModifyTime = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None
        self._RewriteHttps = None
        self._ErrCode = None
        self._Version = None

    @property
    def Protocol(self):
        """转发协议，取值[http, https]
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """转发域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LbType(self):
        """负载均衡方式，取值[1(加权轮询)]
        :rtype: int
        """
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        """会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :rtype: int
        """
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def KeepTime(self):
        """会话保持时间，单位秒
        :rtype: int
        """
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceType(self):
        """回源方式，取值[1(域名回源)，2(IP回源)]
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceList(self):
        """回源列表
        :rtype: list of L4RuleSource
        """
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def Region(self):
        """区域码
        :rtype: int
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Id(self):
        """资源Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        """资源Ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def RuleId(self):
        """规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则描述
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CertType(self):
        """证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :rtype: int
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        """当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :rtype: str
        """
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        """当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        """当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def Status(self):
        """规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CCStatus(self):
        """cc防护状态，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def CCEnable(self):
        """HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        """HTTPS协议的CC防护阈值（已废弃）
        :rtype: int
        """
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def CCLevel(self):
        """HTTPS协议的CC防护等级
        :rtype: str
        """
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def HttpsToHttpEnable(self):
        """是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :rtype: int
        """
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def VirtualPort(self):
        """接入端口值
        :rtype: int
        """
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def RewriteHttps(self):
        """http强制跳转https，1表示打开，0表示关闭
        :rtype: int
        """
        return self._RewriteHttps

    @RewriteHttps.setter
    def RewriteHttps(self, RewriteHttps):
        self._RewriteHttps = RewriteHttps

    @property
    def ErrCode(self):
        """规则配置失败时的详细错误原因(仅当Status=2时有效)，1001证书不存在，1002证书获取失败，1003证书上传失败，1004证书已过期
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def Version(self):
        """版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._KeepTime = params.get("KeepTime")
        self._SourceType = params.get("SourceType")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._Region = params.get("Region")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCLevel = params.get("CCLevel")
        self._ModifyTime = params.get("ModifyTime")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        self._RewriteHttps = params.get("RewriteHttps")
        self._ErrCode = params.get("ErrCode")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstance(AbstractModel):
    """高防包资产实例信息

    """

    def __init__(self):
        r"""
        :param _InstanceDetail: 资产实例的详细信息
        :type InstanceDetail: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        :param _SpecificationLimit: 资产实例的规格信息
        :type SpecificationLimit: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceSpecification`
        :param _Usage: 资产实例的使用统计信息
        :type Usage: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceUsages`
        :param _Region: 资产实例所在的地域
        :type Region: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        :param _Status: 资产实例的防护状态，状态码如下：
"idle"：正常状态(无攻击)
"attacking"：攻击中
"blocking"：封堵中
"creating"：创建中
"deblocking"：解封中
"isolate"：回收隔离中
        :type Status: str
        :param _CreatedTime: 购买时间
        :type CreatedTime: str
        :param _ExpiredTime: 到期时间
        :type ExpiredTime: str
        :param _Name: 资产实例的名称
        :type Name: str
        :param _PackInfo: 资产实例所属的套餐包信息，
注意：当资产实例不是套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :type PackInfo: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        :param _EipProductInfos: 高防包绑定的EIP属于的云产品信息
        :type EipProductInfos: list of EipProductInfo
        :param _BoundStatus: 高防包绑定状态，取值[
"idle"：绑定已完成
 "bounding"：正在绑定中
"failed"：绑定失败
]
        :type BoundStatus: str
        :param _DDoSLevel: 四层防护严格级别
        :type DDoSLevel: str
        :param _CCEnable: CC防护开关
        :type CCEnable: int
        :param _TagInfoList: 资源关联标签
        :type TagInfoList: list of TagInfo
        :param _IpCountNewFlag: 新版本1ip高防包
        :type IpCountNewFlag: int
        :param _VitalityVersion: 攻击封堵套餐标记
        :type VitalityVersion: int
        :param _Line: 网络线路
        :type Line: int
        :param _FreeServiceBandwidth: 不计费的业务带宽
        :type FreeServiceBandwidth: int
        :param _ElasticServiceBandwidth: 弹性业务带宽开关
        :type ElasticServiceBandwidth: int
        :param _GiftServiceBandWidth: 赠送的业务带宽
        :type GiftServiceBandWidth: int
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _BasicPlusFlag: 是否是基础防护加强版 0: 不是 1: 是
        :type BasicPlusFlag: int
        :param _PlanCntFlag: 是否标准版2.0 0: 包含标准版2.0 1: 只查询标准版2.0 2: 不查标准版2.0
        :type PlanCntFlag: int
        :param _TransRegionFlag: 是否跨区域产品 0: 不包含跨区域产品 1: 中国大陆跨区域产品 2: 非中国大陆跨区域产品
        :type TransRegionFlag: int
        :param _SuperPackFlag: 是否为超级高防包
        :type SuperPackFlag: int
        :param _ZoneId: 所属ZoneId
        :type ZoneId: int
        """
        self._InstanceDetail = None
        self._SpecificationLimit = None
        self._Usage = None
        self._Region = None
        self._Status = None
        self._CreatedTime = None
        self._ExpiredTime = None
        self._Name = None
        self._PackInfo = None
        self._EipProductInfos = None
        self._BoundStatus = None
        self._DDoSLevel = None
        self._CCEnable = None
        self._TagInfoList = None
        self._IpCountNewFlag = None
        self._VitalityVersion = None
        self._Line = None
        self._FreeServiceBandwidth = None
        self._ElasticServiceBandwidth = None
        self._GiftServiceBandWidth = None
        self._ModifyTime = None
        self._BasicPlusFlag = None
        self._PlanCntFlag = None
        self._TransRegionFlag = None
        self._SuperPackFlag = None
        self._ZoneId = None

    @property
    def InstanceDetail(self):
        """资产实例的详细信息
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.InstanceRelation`
        """
        return self._InstanceDetail

    @InstanceDetail.setter
    def InstanceDetail(self, InstanceDetail):
        self._InstanceDetail = InstanceDetail

    @property
    def SpecificationLimit(self):
        """资产实例的规格信息
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceSpecification`
        """
        return self._SpecificationLimit

    @SpecificationLimit.setter
    def SpecificationLimit(self, SpecificationLimit):
        self._SpecificationLimit = SpecificationLimit

    @property
    def Usage(self):
        """资产实例的使用统计信息
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.BGPInstanceUsages`
        """
        return self._Usage

    @Usage.setter
    def Usage(self, Usage):
        self._Usage = Usage

    @property
    def Region(self):
        """资产实例所在的地域
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.RegionInfo`
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        """资产实例的防护状态，状态码如下：
"idle"：正常状态(无攻击)
"attacking"：攻击中
"blocking"：封堵中
"creating"：创建中
"deblocking"：解封中
"isolate"：回收隔离中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        """购买时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ExpiredTime(self):
        """到期时间
        :rtype: str
        """
        return self._ExpiredTime

    @ExpiredTime.setter
    def ExpiredTime(self, ExpiredTime):
        self._ExpiredTime = ExpiredTime

    @property
    def Name(self):
        """资产实例的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def PackInfo(self):
        """资产实例所属的套餐包信息，
注意：当资产实例不是套餐包的实例时，此字段为null
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.PackInfo`
        """
        return self._PackInfo

    @PackInfo.setter
    def PackInfo(self, PackInfo):
        self._PackInfo = PackInfo

    @property
    def EipProductInfos(self):
        """高防包绑定的EIP属于的云产品信息
        :rtype: list of EipProductInfo
        """
        return self._EipProductInfos

    @EipProductInfos.setter
    def EipProductInfos(self, EipProductInfos):
        self._EipProductInfos = EipProductInfos

    @property
    def BoundStatus(self):
        """高防包绑定状态，取值[
"idle"：绑定已完成
 "bounding"：正在绑定中
"failed"：绑定失败
]
        :rtype: str
        """
        return self._BoundStatus

    @BoundStatus.setter
    def BoundStatus(self, BoundStatus):
        self._BoundStatus = BoundStatus

    @property
    def DDoSLevel(self):
        """四层防护严格级别
        :rtype: str
        """
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel

    @property
    def CCEnable(self):
        """CC防护开关
        :rtype: int
        """
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def TagInfoList(self):
        """资源关联标签
        :rtype: list of TagInfo
        """
        return self._TagInfoList

    @TagInfoList.setter
    def TagInfoList(self, TagInfoList):
        self._TagInfoList = TagInfoList

    @property
    def IpCountNewFlag(self):
        """新版本1ip高防包
        :rtype: int
        """
        return self._IpCountNewFlag

    @IpCountNewFlag.setter
    def IpCountNewFlag(self, IpCountNewFlag):
        self._IpCountNewFlag = IpCountNewFlag

    @property
    def VitalityVersion(self):
        """攻击封堵套餐标记
        :rtype: int
        """
        return self._VitalityVersion

    @VitalityVersion.setter
    def VitalityVersion(self, VitalityVersion):
        self._VitalityVersion = VitalityVersion

    @property
    def Line(self):
        """网络线路
        :rtype: int
        """
        return self._Line

    @Line.setter
    def Line(self, Line):
        self._Line = Line

    @property
    def FreeServiceBandwidth(self):
        """不计费的业务带宽
        :rtype: int
        """
        return self._FreeServiceBandwidth

    @FreeServiceBandwidth.setter
    def FreeServiceBandwidth(self, FreeServiceBandwidth):
        self._FreeServiceBandwidth = FreeServiceBandwidth

    @property
    def ElasticServiceBandwidth(self):
        """弹性业务带宽开关
        :rtype: int
        """
        return self._ElasticServiceBandwidth

    @ElasticServiceBandwidth.setter
    def ElasticServiceBandwidth(self, ElasticServiceBandwidth):
        self._ElasticServiceBandwidth = ElasticServiceBandwidth

    @property
    def GiftServiceBandWidth(self):
        """赠送的业务带宽
        :rtype: int
        """
        return self._GiftServiceBandWidth

    @GiftServiceBandWidth.setter
    def GiftServiceBandWidth(self, GiftServiceBandWidth):
        self._GiftServiceBandWidth = GiftServiceBandWidth

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def BasicPlusFlag(self):
        """是否是基础防护加强版 0: 不是 1: 是
        :rtype: int
        """
        return self._BasicPlusFlag

    @BasicPlusFlag.setter
    def BasicPlusFlag(self, BasicPlusFlag):
        self._BasicPlusFlag = BasicPlusFlag

    @property
    def PlanCntFlag(self):
        """是否标准版2.0 0: 包含标准版2.0 1: 只查询标准版2.0 2: 不查标准版2.0
        :rtype: int
        """
        return self._PlanCntFlag

    @PlanCntFlag.setter
    def PlanCntFlag(self, PlanCntFlag):
        self._PlanCntFlag = PlanCntFlag

    @property
    def TransRegionFlag(self):
        """是否跨区域产品 0: 不包含跨区域产品 1: 中国大陆跨区域产品 2: 非中国大陆跨区域产品
        :rtype: int
        """
        return self._TransRegionFlag

    @TransRegionFlag.setter
    def TransRegionFlag(self, TransRegionFlag):
        self._TransRegionFlag = TransRegionFlag

    @property
    def SuperPackFlag(self):
        """是否为超级高防包
        :rtype: int
        """
        return self._SuperPackFlag

    @SuperPackFlag.setter
    def SuperPackFlag(self, SuperPackFlag):
        self._SuperPackFlag = SuperPackFlag

    @property
    def ZoneId(self):
        """所属ZoneId
        :rtype: int
        """
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        if params.get("InstanceDetail") is not None:
            self._InstanceDetail = InstanceRelation()
            self._InstanceDetail._deserialize(params.get("InstanceDetail"))
        if params.get("SpecificationLimit") is not None:
            self._SpecificationLimit = BGPInstanceSpecification()
            self._SpecificationLimit._deserialize(params.get("SpecificationLimit"))
        if params.get("Usage") is not None:
            self._Usage = BGPInstanceUsages()
            self._Usage._deserialize(params.get("Usage"))
        if params.get("Region") is not None:
            self._Region = RegionInfo()
            self._Region._deserialize(params.get("Region"))
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ExpiredTime = params.get("ExpiredTime")
        self._Name = params.get("Name")
        if params.get("PackInfo") is not None:
            self._PackInfo = PackInfo()
            self._PackInfo._deserialize(params.get("PackInfo"))
        if params.get("EipProductInfos") is not None:
            self._EipProductInfos = []
            for item in params.get("EipProductInfos"):
                obj = EipProductInfo()
                obj._deserialize(item)
                self._EipProductInfos.append(obj)
        self._BoundStatus = params.get("BoundStatus")
        self._DDoSLevel = params.get("DDoSLevel")
        self._CCEnable = params.get("CCEnable")
        if params.get("TagInfoList") is not None:
            self._TagInfoList = []
            for item in params.get("TagInfoList"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagInfoList.append(obj)
        self._IpCountNewFlag = params.get("IpCountNewFlag")
        self._VitalityVersion = params.get("VitalityVersion")
        self._Line = params.get("Line")
        self._FreeServiceBandwidth = params.get("FreeServiceBandwidth")
        self._ElasticServiceBandwidth = params.get("ElasticServiceBandwidth")
        self._GiftServiceBandWidth = params.get("GiftServiceBandWidth")
        self._ModifyTime = params.get("ModifyTime")
        self._BasicPlusFlag = params.get("BasicPlusFlag")
        self._PlanCntFlag = params.get("PlanCntFlag")
        self._TransRegionFlag = params.get("TransRegionFlag")
        self._SuperPackFlag = params.get("SuperPackFlag")
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstanceSpecification(AbstractModel):
    """高防包资产实例的规格信息

    """

    def __init__(self):
        r"""
        :param _ProtectBandwidth: 保底防护峰值，单位Gbps
        :type ProtectBandwidth: int
        :param _ProtectCountLimit: 防护次数，单位次
        :type ProtectCountLimit: int
        :param _ProtectIPNumberLimit: 防护IP数，单位个
        :type ProtectIPNumberLimit: int
        :param _AutoRenewFlag: 自动续费状态，取值[
0：没有开启自动续费
1：开启了自动续费
]
        :type AutoRenewFlag: int
        :param _UnionPackFlag: 联合产品标记，0代表普通高防包，1代表联合高防包
        :type UnionPackFlag: int
        :param _ServiceBandWidth: 业务带宽
        :type ServiceBandWidth: int
        :param _BattleEditionFlag: 战斗服版本标记，0表示普通高防包，1表示战斗服高防包
        :type BattleEditionFlag: int
        :param _ChannelEditionFlag: 渠道版标记，0表示普通高防包，1表示渠道版高防包
        :type ChannelEditionFlag: int
        :param _EnterpriseFlag: 高防包企业版标记，0表示普通高防包；1表示企业版高防包
        :type EnterpriseFlag: int
        :param _ElasticLimit: 高防包企业版弹性阈值，0表示未开启；大于0为弹性防护阈值
        :type ElasticLimit: int
        :param _DownGradeProtect: 降配后的防护能力，单位Gbps
        :type DownGradeProtect: int
        """
        self._ProtectBandwidth = None
        self._ProtectCountLimit = None
        self._ProtectIPNumberLimit = None
        self._AutoRenewFlag = None
        self._UnionPackFlag = None
        self._ServiceBandWidth = None
        self._BattleEditionFlag = None
        self._ChannelEditionFlag = None
        self._EnterpriseFlag = None
        self._ElasticLimit = None
        self._DownGradeProtect = None

    @property
    def ProtectBandwidth(self):
        """保底防护峰值，单位Gbps
        :rtype: int
        """
        return self._ProtectBandwidth

    @ProtectBandwidth.setter
    def ProtectBandwidth(self, ProtectBandwidth):
        self._ProtectBandwidth = ProtectBandwidth

    @property
    def ProtectCountLimit(self):
        """防护次数，单位次
        :rtype: int
        """
        return self._ProtectCountLimit

    @ProtectCountLimit.setter
    def ProtectCountLimit(self, ProtectCountLimit):
        self._ProtectCountLimit = ProtectCountLimit

    @property
    def ProtectIPNumberLimit(self):
        """防护IP数，单位个
        :rtype: int
        """
        return self._ProtectIPNumberLimit

    @ProtectIPNumberLimit.setter
    def ProtectIPNumberLimit(self, ProtectIPNumberLimit):
        self._ProtectIPNumberLimit = ProtectIPNumberLimit

    @property
    def AutoRenewFlag(self):
        """自动续费状态，取值[
0：没有开启自动续费
1：开启了自动续费
]
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def UnionPackFlag(self):
        """联合产品标记，0代表普通高防包，1代表联合高防包
        :rtype: int
        """
        return self._UnionPackFlag

    @UnionPackFlag.setter
    def UnionPackFlag(self, UnionPackFlag):
        self._UnionPackFlag = UnionPackFlag

    @property
    def ServiceBandWidth(self):
        """业务带宽
        :rtype: int
        """
        return self._ServiceBandWidth

    @ServiceBandWidth.setter
    def ServiceBandWidth(self, ServiceBandWidth):
        self._ServiceBandWidth = ServiceBandWidth

    @property
    def BattleEditionFlag(self):
        """战斗服版本标记，0表示普通高防包，1表示战斗服高防包
        :rtype: int
        """
        return self._BattleEditionFlag

    @BattleEditionFlag.setter
    def BattleEditionFlag(self, BattleEditionFlag):
        self._BattleEditionFlag = BattleEditionFlag

    @property
    def ChannelEditionFlag(self):
        """渠道版标记，0表示普通高防包，1表示渠道版高防包
        :rtype: int
        """
        return self._ChannelEditionFlag

    @ChannelEditionFlag.setter
    def ChannelEditionFlag(self, ChannelEditionFlag):
        self._ChannelEditionFlag = ChannelEditionFlag

    @property
    def EnterpriseFlag(self):
        """高防包企业版标记，0表示普通高防包；1表示企业版高防包
        :rtype: int
        """
        return self._EnterpriseFlag

    @EnterpriseFlag.setter
    def EnterpriseFlag(self, EnterpriseFlag):
        self._EnterpriseFlag = EnterpriseFlag

    @property
    def ElasticLimit(self):
        """高防包企业版弹性阈值，0表示未开启；大于0为弹性防护阈值
        :rtype: int
        """
        return self._ElasticLimit

    @ElasticLimit.setter
    def ElasticLimit(self, ElasticLimit):
        self._ElasticLimit = ElasticLimit

    @property
    def DownGradeProtect(self):
        """降配后的防护能力，单位Gbps
        :rtype: int
        """
        return self._DownGradeProtect

    @DownGradeProtect.setter
    def DownGradeProtect(self, DownGradeProtect):
        self._DownGradeProtect = DownGradeProtect


    def _deserialize(self, params):
        self._ProtectBandwidth = params.get("ProtectBandwidth")
        self._ProtectCountLimit = params.get("ProtectCountLimit")
        self._ProtectIPNumberLimit = params.get("ProtectIPNumberLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._UnionPackFlag = params.get("UnionPackFlag")
        self._ServiceBandWidth = params.get("ServiceBandWidth")
        self._BattleEditionFlag = params.get("BattleEditionFlag")
        self._ChannelEditionFlag = params.get("ChannelEditionFlag")
        self._EnterpriseFlag = params.get("EnterpriseFlag")
        self._ElasticLimit = params.get("ElasticLimit")
        self._DownGradeProtect = params.get("DownGradeProtect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BGPInstanceUsages(AbstractModel):
    """高防包资产实例的使用信息统计

    """

    def __init__(self):
        r"""
        :param _ProtectCountUsage: 已使用的防护次数，单位次
        :type ProtectCountUsage: int
        :param _ProtectIPNumberUsage: 已防护的IP数，单位个
        :type ProtectIPNumberUsage: int
        :param _Last7DayAttackCount: 最近7天的攻击次数，单位次
        :type Last7DayAttackCount: int
        """
        self._ProtectCountUsage = None
        self._ProtectIPNumberUsage = None
        self._Last7DayAttackCount = None

    @property
    def ProtectCountUsage(self):
        """已使用的防护次数，单位次
        :rtype: int
        """
        return self._ProtectCountUsage

    @ProtectCountUsage.setter
    def ProtectCountUsage(self, ProtectCountUsage):
        self._ProtectCountUsage = ProtectCountUsage

    @property
    def ProtectIPNumberUsage(self):
        """已防护的IP数，单位个
        :rtype: int
        """
        return self._ProtectIPNumberUsage

    @ProtectIPNumberUsage.setter
    def ProtectIPNumberUsage(self, ProtectIPNumberUsage):
        self._ProtectIPNumberUsage = ProtectIPNumberUsage

    @property
    def Last7DayAttackCount(self):
        """最近7天的攻击次数，单位次
        :rtype: int
        """
        return self._Last7DayAttackCount

    @Last7DayAttackCount.setter
    def Last7DayAttackCount(self, Last7DayAttackCount):
        self._Last7DayAttackCount = Last7DayAttackCount


    def _deserialize(self, params):
        self._ProtectCountUsage = params.get("ProtectCountUsage")
        self._ProtectIPNumberUsage = params.get("ProtectIPNumberUsage")
        self._Last7DayAttackCount = params.get("Last7DayAttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BlackWhiteIpRelation(AbstractModel):
    """黑白名单IP

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _Type: IP类型，取值[black(黑IP)，white(白IP)]
        :type Type: str
        :param _InstanceDetailList: 黑白IP所属的实例
        :type InstanceDetailList: list of InstanceRelation
        :param _Mask: ip掩码，0表示32位完整ip
        :type Mask: int
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._Ip = None
        self._Type = None
        self._InstanceDetailList = None
        self._Mask = None
        self._ModifyTime = None

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Type(self):
        """IP类型，取值[black(黑IP)，white(白IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def InstanceDetailList(self):
        """黑白IP所属的实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList

    @property
    def Mask(self):
        """ip掩码，0表示32位完整ip
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Type = params.get("Type")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        self._Mask = params.get("Mask")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BoundIpInfo(AbstractModel):
    """高防包绑定IP对象

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _BizType: 绑定的产品分类，绑定操作为必填项，解绑操作可不填。取值[public（CVM、CLB产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :type BizType: str
        :param _InstanceId: IP所属的资源实例ID，绑定操作为必填项，解绑操作可不填。例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*); 如果绑定的是托管IP没有对应的资源实例ID，请填写"none";
        :type InstanceId: str
        :param _DeviceType: 产品分类下的子类型，绑定操作为必填项，解绑操作可不填。取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（弹性公网常规IP）]
        :type DeviceType: str
        :param _IspCode: 运营商，绑定操作为必填项，解绑操作可不填。0：电信；1：联通；2：移动；5：BGP
        :type IspCode: int
        :param _Domain: 域名化资产对应的域名
        :type Domain: str
        """
        self._Ip = None
        self._BizType = None
        self._InstanceId = None
        self._DeviceType = None
        self._IspCode = None
        self._Domain = None

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        """绑定的产品分类，绑定操作为必填项，解绑操作可不填。取值[public（CVM、CLB产品），bm（黑石产品），eni（弹性网卡），vpngw（VPN网关）， natgw（NAT网关），waf（Web应用安全产品），fpc（金融产品），gaap（GAAP产品）, other(托管IP)]
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def InstanceId(self):
        """IP所属的资源实例ID，绑定操作为必填项，解绑操作可不填。例如是弹性网卡的IP，则InstanceId填写弹性网卡的ID(eni-*); 如果绑定的是托管IP没有对应的资源实例ID，请填写"none";
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DeviceType(self):
        """产品分类下的子类型，绑定操作为必填项，解绑操作可不填。取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（弹性公网常规IP）]
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def IspCode(self):
        """运营商，绑定操作为必填项，解绑操作可不填。0：电信；1：联通；2：移动；5：BGP
        :rtype: int
        """
        return self._IspCode

    @IspCode.setter
    def IspCode(self, IspCode):
        self._IspCode = IspCode

    @property
    def Domain(self):
        """域名化资产对应的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._InstanceId = params.get("InstanceId")
        self._DeviceType = params.get("DeviceType")
        self._IspCode = params.get("IspCode")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCLevelPolicy(AbstractModel):
    """CC分级策略

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: Ip
        :type Ip: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Domain: 域名
        :type Domain: str
        :param _Level: 防护等级，可取值default表示默认策略，loose表示宽松，strict表示严格
        :type Level: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._Level = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """Ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Level(self):
        """防护等级，可取值default表示默认策略，loose表示宽松，strict表示严格
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._Level = params.get("Level")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPrecisionPlyRecord(AbstractModel):
    """CC精准防护配置项

    """

    def __init__(self):
        r"""
        :param _FieldType: 配置项类型，当前仅支持value
        :type FieldType: str
        :param _FieldName: 配置字段，可取值cgi， ua， cookie， referer， accept,  srcip
        :type FieldName: str
        :param _Value: 配置取值
        :type Value: str
        :param _ValueOperator: 配置项值比对方式，可取值equal：相等，not_equal：不相等， include：包含
        :type ValueOperator: str
        """
        self._FieldType = None
        self._FieldName = None
        self._Value = None
        self._ValueOperator = None

    @property
    def FieldType(self):
        """配置项类型，当前仅支持value
        :rtype: str
        """
        return self._FieldType

    @FieldType.setter
    def FieldType(self, FieldType):
        self._FieldType = FieldType

    @property
    def FieldName(self):
        """配置字段，可取值cgi， ua， cookie， referer， accept,  srcip
        :rtype: str
        """
        return self._FieldName

    @FieldName.setter
    def FieldName(self, FieldName):
        self._FieldName = FieldName

    @property
    def Value(self):
        """配置取值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueOperator(self):
        """配置项值比对方式，可取值equal：相等，not_equal：不相等， include：包含
        :rtype: str
        """
        return self._ValueOperator

    @ValueOperator.setter
    def ValueOperator(self, ValueOperator):
        self._ValueOperator = ValueOperator


    def _deserialize(self, params):
        self._FieldType = params.get("FieldType")
        self._FieldName = params.get("FieldName")
        self._Value = params.get("Value")
        self._ValueOperator = params.get("ValueOperator")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCPrecisionPolicy(AbstractModel):
    """CC精准防护策略信息

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id
        :type PolicyId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: Ip地址
        :type Ip: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Domain: 域名
        :type Domain: str
        :param _PolicyAction: 策略方式（丢弃或验证码）
        :type PolicyAction: str
        :param _PolicyList: 策略列表
        :type PolicyList: list of CCPrecisionPlyRecord
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._PolicyAction = None
        self._PolicyList = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """Ip地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def PolicyAction(self):
        """策略方式（丢弃或验证码）
        :rtype: str
        """
        return self._PolicyAction

    @PolicyAction.setter
    def PolicyAction(self, PolicyAction):
        self._PolicyAction = PolicyAction

    @property
    def PolicyList(self):
        """策略列表
        :rtype: list of CCPrecisionPlyRecord
        """
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCReqLimitPolicy(AbstractModel):
    """CC频率限制策略

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id
        :type PolicyId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: Ip地址
        :type Ip: str
        :param _Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param _Domain: 域名
        :type Domain: str
        :param _PolicyRecord: 策略项
        :type PolicyRecord: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._PolicyRecord = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """Ip地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        """协议，可取值HTTP，HTTPS
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def PolicyRecord(self):
        """策略项
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        """
        return self._PolicyRecord

    @PolicyRecord.setter
    def PolicyRecord(self, PolicyRecord):
        self._PolicyRecord = PolicyRecord

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        if params.get("PolicyRecord") is not None:
            self._PolicyRecord = CCReqLimitPolicyRecord()
            self._PolicyRecord._deserialize(params.get("PolicyRecord"))
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCReqLimitPolicyRecord(AbstractModel):
    """CC频率限制策略项字段

    """

    def __init__(self):
        r"""
        :param _Period: 统计周期，可取值1，10，30，60，单位秒
        :type Period: int
        :param _RequestNum: 请求数，取值1~20000
        :type RequestNum: int
        :param _Action: 频率限制策略方式，可取值alg表示验证码，drop表示丢弃
        :type Action: str
        :param _ExecuteDuration: 频率限制策略时长，可取值1~86400，单位秒
        :type ExecuteDuration: int
        :param _Mode: 策略项比对方式，可取值include表示包含，equal表示等于
        :type Mode: str
        :param _Uri: Uri，三个策略项仅可填其中之一
        :type Uri: str
        :param _UserAgent: User-Agent，三个策略项仅可填其中之一
        :type UserAgent: str
        :param _Cookie: Cookie，三个策略项仅可填其中之一
        :type Cookie: str
        """
        self._Period = None
        self._RequestNum = None
        self._Action = None
        self._ExecuteDuration = None
        self._Mode = None
        self._Uri = None
        self._UserAgent = None
        self._Cookie = None

    @property
    def Period(self):
        """统计周期，可取值1，10，30，60，单位秒
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def RequestNum(self):
        """请求数，取值1~20000
        :rtype: int
        """
        return self._RequestNum

    @RequestNum.setter
    def RequestNum(self, RequestNum):
        self._RequestNum = RequestNum

    @property
    def Action(self):
        """频率限制策略方式，可取值alg表示验证码，drop表示丢弃
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def ExecuteDuration(self):
        """频率限制策略时长，可取值1~86400，单位秒
        :rtype: int
        """
        return self._ExecuteDuration

    @ExecuteDuration.setter
    def ExecuteDuration(self, ExecuteDuration):
        self._ExecuteDuration = ExecuteDuration

    @property
    def Mode(self):
        """策略项比对方式，可取值include表示包含，equal表示等于
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Uri(self):
        """Uri，三个策略项仅可填其中之一
        :rtype: str
        """
        return self._Uri

    @Uri.setter
    def Uri(self, Uri):
        self._Uri = Uri

    @property
    def UserAgent(self):
        """User-Agent，三个策略项仅可填其中之一
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Cookie(self):
        """Cookie，三个策略项仅可填其中之一
        :rtype: str
        """
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._RequestNum = params.get("RequestNum")
        self._Action = params.get("Action")
        self._ExecuteDuration = params.get("ExecuteDuration")
        self._Mode = params.get("Mode")
        self._Uri = params.get("Uri")
        self._UserAgent = params.get("UserAgent")
        self._Cookie = params.get("Cookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CCThresholdPolicy(AbstractModel):
    """CC清洗阈值策略

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: Ip地址
        :type Ip: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Domain: 域名
        :type Domain: str
        :param _Threshold: 清洗阈值
        :type Threshold: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._Threshold = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """Ip地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Threshold(self):
        """清洗阈值
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._Threshold = params.get("Threshold")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcBlackWhiteIpPolicy(AbstractModel):
    """CC四层黑白名单列表

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id
        :type PolicyId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        :param _BlackWhiteIp: 黑白名单IP地址
        :type BlackWhiteIp: str
        :param _Mask: 掩码
        :type Mask: int
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._Type = None
        self._BlackWhiteIp = None
        self._Mask = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Type(self):
        """IP类型，取值[black(黑名单IP), white(白名单IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def BlackWhiteIp(self):
        """黑白名单IP地址
        :rtype: str
        """
        return self._BlackWhiteIp

    @BlackWhiteIp.setter
    def BlackWhiteIp(self, BlackWhiteIp):
        self._BlackWhiteIp = BlackWhiteIp

    @property
    def Mask(self):
        """掩码
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._Type = params.get("Type")
        self._BlackWhiteIp = params.get("BlackWhiteIp")
        self._Mask = params.get("Mask")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcGeoIPBlockConfig(AbstractModel):
    """DDoS防护的区域封禁配置

    """

    def __init__(self):
        r"""
        :param _RegionType: 区域类型，取值[
oversea(境外)
china(国内)
customized(自定义地区)
]
        :type RegionType: str
        :param _Action: 封禁动作，取值[
drop(拦截)
alg(人机校验)
]
        :type Action: str
        :param _Id: 配置ID，配置添加成功后生成；添加新配置时不用填写此字段，修改或删除配置时需要填写配置ID
        :type Id: str
        :param _AreaList: 当RegionType为customized时，必须填写AreaList；当RegionType为china或oversea时，AreaList为空
        :type AreaList: list of int
        """
        self._RegionType = None
        self._Action = None
        self._Id = None
        self._AreaList = None

    @property
    def RegionType(self):
        """区域类型，取值[
oversea(境外)
china(国内)
customized(自定义地区)
]
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def Action(self):
        """封禁动作，取值[
drop(拦截)
alg(人机校验)
]
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Id(self):
        """配置ID，配置添加成功后生成；添加新配置时不用填写此字段，修改或删除配置时需要填写配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AreaList(self):
        """当RegionType为customized时，必须填写AreaList；当RegionType为china或oversea时，AreaList为空
        :rtype: list of int
        """
        return self._AreaList

    @AreaList.setter
    def AreaList(self, AreaList):
        self._AreaList = AreaList


    def _deserialize(self, params):
        self._RegionType = params.get("RegionType")
        self._Action = params.get("Action")
        self._Id = params.get("Id")
        self._AreaList = params.get("AreaList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcGeoIpPolicyNew(AbstractModel):
    """CC地域封禁列表详情

    """

    def __init__(self):
        r"""
        :param _PolicyId: 策略Id
        :type PolicyId: str
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议，可取值HTTP，HTTPS
        :type Protocol: str
        :param _Action: 用户动作，drop或alg
        :type Action: str
        :param _RegionType: 地域类型，分为china, oversea与customized
        :type RegionType: str
        :param _AreaList: 用户选择封禁的地域ID列表
        :type AreaList: list of int non-negative
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._PolicyId = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._Action = None
        self._RegionType = None
        self._AreaList = None
        self._CreateTime = None
        self._ModifyTime = None

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，可取值HTTP，HTTPS
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Action(self):
        """用户动作，drop或alg
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RegionType(self):
        """地域类型，分为china, oversea与customized
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def AreaList(self):
        """用户选择封禁的地域ID列表
        :rtype: list of int non-negative
        """
        return self._AreaList

    @AreaList.setter
    def AreaList(self, AreaList):
        self._AreaList = AreaList

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._PolicyId = params.get("PolicyId")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._Action = params.get("Action")
        self._RegionType = params.get("RegionType")
        self._AreaList = params.get("AreaList")
        self._CreateTime = params.get("CreateTime")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertIdInsL7Rules(AbstractModel):
    """使用证书的规则集合

    """

    def __init__(self):
        r"""
        :param _L7Rules: 使用证书的规则列表
        :type L7Rules: list of InsL7Rules
        :param _CertId: 证书ID
        :type CertId: str
        """
        self._L7Rules = None
        self._CertId = None

    @property
    def L7Rules(self):
        """使用证书的规则列表
        :rtype: list of InsL7Rules
        """
        return self._L7Rules

    @L7Rules.setter
    def L7Rules(self, L7Rules):
        self._L7Rules = L7Rules

    @property
    def CertId(self):
        """证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        if params.get("L7Rules") is not None:
            self._L7Rules = []
            for item in params.get("L7Rules"):
                obj = InsL7Rules()
                obj._deserialize(item)
                self._L7Rules.append(obj)
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectLimitConfig(AbstractModel):
    """连接抑制相关配置

    """

    def __init__(self):
        r"""
        :param _SdNewLimit: 基于源IP+目的IP的每秒新建数限制
        :type SdNewLimit: int
        :param _DstNewLimit: 基于目的IP的每秒新建数限制
        :type DstNewLimit: int
        :param _SdConnLimit: 基于源IP+目的IP的并发连接控制
        :type SdConnLimit: int
        :param _DstConnLimit: 基于目的IP+目的端口的并发连接控制
        :type DstConnLimit: int
        :param _BadConnThreshold: 基于连接抑制触发阈值，取值范围[0,4294967295]
        :type BadConnThreshold: int
        :param _NullConnEnable: 异常连接检测条件，空连接防护开关，，取值范围[0,1]
        :type NullConnEnable: int
        :param _ConnTimeout: 异常连接检测条件，连接超时，，取值范围[0,65535]
        :type ConnTimeout: int
        :param _SynRate: 异常连接检测条件，syn占比ack百分比，，取值范围[0,100]
        :type SynRate: int
        :param _SynLimit: 异常连接检测条件，syn阈值，取值范围[0,100]
        :type SynLimit: int
        """
        self._SdNewLimit = None
        self._DstNewLimit = None
        self._SdConnLimit = None
        self._DstConnLimit = None
        self._BadConnThreshold = None
        self._NullConnEnable = None
        self._ConnTimeout = None
        self._SynRate = None
        self._SynLimit = None

    @property
    def SdNewLimit(self):
        """基于源IP+目的IP的每秒新建数限制
        :rtype: int
        """
        return self._SdNewLimit

    @SdNewLimit.setter
    def SdNewLimit(self, SdNewLimit):
        self._SdNewLimit = SdNewLimit

    @property
    def DstNewLimit(self):
        """基于目的IP的每秒新建数限制
        :rtype: int
        """
        return self._DstNewLimit

    @DstNewLimit.setter
    def DstNewLimit(self, DstNewLimit):
        self._DstNewLimit = DstNewLimit

    @property
    def SdConnLimit(self):
        """基于源IP+目的IP的并发连接控制
        :rtype: int
        """
        return self._SdConnLimit

    @SdConnLimit.setter
    def SdConnLimit(self, SdConnLimit):
        self._SdConnLimit = SdConnLimit

    @property
    def DstConnLimit(self):
        """基于目的IP+目的端口的并发连接控制
        :rtype: int
        """
        return self._DstConnLimit

    @DstConnLimit.setter
    def DstConnLimit(self, DstConnLimit):
        self._DstConnLimit = DstConnLimit

    @property
    def BadConnThreshold(self):
        """基于连接抑制触发阈值，取值范围[0,4294967295]
        :rtype: int
        """
        return self._BadConnThreshold

    @BadConnThreshold.setter
    def BadConnThreshold(self, BadConnThreshold):
        self._BadConnThreshold = BadConnThreshold

    @property
    def NullConnEnable(self):
        """异常连接检测条件，空连接防护开关，，取值范围[0,1]
        :rtype: int
        """
        return self._NullConnEnable

    @NullConnEnable.setter
    def NullConnEnable(self, NullConnEnable):
        self._NullConnEnable = NullConnEnable

    @property
    def ConnTimeout(self):
        """异常连接检测条件，连接超时，，取值范围[0,65535]
        :rtype: int
        """
        return self._ConnTimeout

    @ConnTimeout.setter
    def ConnTimeout(self, ConnTimeout):
        self._ConnTimeout = ConnTimeout

    @property
    def SynRate(self):
        """异常连接检测条件，syn占比ack百分比，，取值范围[0,100]
        :rtype: int
        """
        return self._SynRate

    @SynRate.setter
    def SynRate(self, SynRate):
        self._SynRate = SynRate

    @property
    def SynLimit(self):
        """异常连接检测条件，syn阈值，取值范围[0,100]
        :rtype: int
        """
        return self._SynLimit

    @SynLimit.setter
    def SynLimit(self, SynLimit):
        self._SynLimit = SynLimit


    def _deserialize(self, params):
        self._SdNewLimit = params.get("SdNewLimit")
        self._DstNewLimit = params.get("DstNewLimit")
        self._SdConnLimit = params.get("SdConnLimit")
        self._DstConnLimit = params.get("DstConnLimit")
        self._BadConnThreshold = params.get("BadConnThreshold")
        self._NullConnEnable = params.get("NullConnEnable")
        self._ConnTimeout = params.get("ConnTimeout")
        self._SynRate = params.get("SynRate")
        self._SynLimit = params.get("SynLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ConnectLimitRelation(AbstractModel):
    """连接抑制列表

    """

    def __init__(self):
        r"""
        :param _ConnectLimitConfig: 连接抑制配置
        :type ConnectLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.ConnectLimitConfig`
        :param _InstanceDetailList: 连接抑制关联的实例信息
        :type InstanceDetailList: list of InstanceRelation
        """
        self._ConnectLimitConfig = None
        self._InstanceDetailList = None

    @property
    def ConnectLimitConfig(self):
        """连接抑制配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ConnectLimitConfig`
        """
        return self._ConnectLimitConfig

    @ConnectLimitConfig.setter
    def ConnectLimitConfig(self, ConnectLimitConfig):
        self._ConnectLimitConfig = ConnectLimitConfig

    @property
    def InstanceDetailList(self):
        """连接抑制关联的实例信息
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("ConnectLimitConfig") is not None:
            self._ConnectLimitConfig = ConnectLimitConfig()
            self._ConnectLimitConfig._deserialize(params.get("ConnectLimitConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlackWhiteIpListRequest(AbstractModel):
    """CreateBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _IpList: IP列表
        :type IpList: list of str
        :param _Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        """IP列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        """IP类型，取值[black(黑名单IP), white(白名单IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IpList = params.get("IpList")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBlackWhiteIpListResponse(AbstractModel):
    """CreateBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateBoundIPRequest(AbstractModel):
    """CreateBoundIP请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgp表示独享包；bgp-multip表示共享包）
        :type Business: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _BoundDevList: 绑定到资源实例的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要绑定的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :type BoundDevList: list of BoundIpInfo
        :param _UnBoundDevList: 与资源实例解绑的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要解绑的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :type UnBoundDevList: list of BoundIpInfo
        :param _CopyPolicy: 已弃用，不填
        :type CopyPolicy: str
        :param _FilterRegion: 如果该资源实例为域名化资产以及跨地域绑定则，该参数必填
        :type FilterRegion: str
        """
        self._Business = None
        self._Id = None
        self._BoundDevList = None
        self._UnBoundDevList = None
        self._CopyPolicy = None
        self._FilterRegion = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgp表示独享包；bgp-multip表示共享包）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        """资源实例ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def BoundDevList(self):
        """绑定到资源实例的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要绑定的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :rtype: list of BoundIpInfo
        """
        return self._BoundDevList

    @BoundDevList.setter
    def BoundDevList(self, BoundDevList):
        self._BoundDevList = BoundDevList

    @property
    def UnBoundDevList(self):
        """与资源实例解绑的IP数组，当资源实例为高防包(独享包)时，数组只允许填1个IP；当没有要解绑的IP时可以为空数组；但是BoundDevList和UnBoundDevList至少有一个不为空；
        :rtype: list of BoundIpInfo
        """
        return self._UnBoundDevList

    @UnBoundDevList.setter
    def UnBoundDevList(self, UnBoundDevList):
        self._UnBoundDevList = UnBoundDevList

    @property
    def CopyPolicy(self):
        """已弃用，不填
        :rtype: str
        """
        return self._CopyPolicy

    @CopyPolicy.setter
    def CopyPolicy(self, CopyPolicy):
        self._CopyPolicy = CopyPolicy

    @property
    def FilterRegion(self):
        """如果该资源实例为域名化资产以及跨地域绑定则，该参数必填
        :rtype: str
        """
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("BoundDevList") is not None:
            self._BoundDevList = []
            for item in params.get("BoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self._BoundDevList.append(obj)
        if params.get("UnBoundDevList") is not None:
            self._UnBoundDevList = []
            for item in params.get("UnBoundDevList"):
                obj = BoundIpInfo()
                obj._deserialize(item)
                self._UnBoundDevList.append(obj)
        self._CopyPolicy = params.get("CopyPolicy")
        self._FilterRegion = params.get("FilterRegion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateBoundIPResponse(AbstractModel):
    """CreateBoundIP返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """成功码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateCCPrecisionPolicyRequest(AbstractModel):
    """CreateCCPrecisionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP值
        :type Ip: str
        :param _Protocol: 协议， 可取值http，https，http/https
        :type Protocol: str
        :param _Domain: 域名
        :type Domain: str
        :param _PolicyAction: 策略方式，可取值alg表示人机校验，drop表示丢弃，trans表示放行
        :type PolicyAction: str
        :param _PolicyList: 策略记录
        :type PolicyList: list of CCPrecisionPlyRecord
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._PolicyAction = None
        self._PolicyList = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP值
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        """协议， 可取值http，https，http/https
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def PolicyAction(self):
        """策略方式，可取值alg表示人机校验，drop表示丢弃，trans表示放行
        :rtype: str
        """
        return self._PolicyAction

    @PolicyAction.setter
    def PolicyAction(self, PolicyAction):
        self._PolicyAction = PolicyAction

    @property
    def PolicyList(self):
        """策略记录
        :rtype: list of CCPrecisionPlyRecord
        """
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCPrecisionPolicyResponse(AbstractModel):
    """CreateCCPrecisionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCCReqLimitPolicyRequest(AbstractModel):
    """CreateCCReqLimitPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP值
        :type Ip: str
        :param _Protocol: 协议，可取值http, https, http/https
        :type Protocol: str
        :param _Domain: 域名
        :type Domain: str
        :param _Policy: 策略项
        :type Policy: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        :param _IsGlobal: 是否为兜底频控 0表示不是 1表示是
        :type IsGlobal: int
        """
        self._InstanceId = None
        self._Ip = None
        self._Protocol = None
        self._Domain = None
        self._Policy = None
        self._IsGlobal = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP值
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Protocol(self):
        """协议，可取值http, https, http/https
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Policy(self):
        """策略项
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy

    @property
    def IsGlobal(self):
        """是否为兜底频控 0表示不是 1表示是
        :rtype: int
        """
        return self._IsGlobal

    @IsGlobal.setter
    def IsGlobal(self, IsGlobal):
        self._IsGlobal = IsGlobal


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        if params.get("Policy") is not None:
            self._Policy = CCReqLimitPolicyRecord()
            self._Policy._deserialize(params.get("Policy"))
        self._IsGlobal = params.get("IsGlobal")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCCReqLimitPolicyResponse(AbstractModel):
    """CreateCCReqLimitPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCcBlackWhiteIpListRequest(AbstractModel):
    """CreateCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _IpList: IP列表
        :type IpList: list of IpSegment
        :param _Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        :param _Ip: Ip地址
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议
        :type Protocol: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        """IP列表
        :rtype: list of IpSegment
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        """IP类型，取值[black(黑名单IP), white(白名单IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Ip(self):
        """Ip地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._Type = params.get("Type")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcBlackWhiteIpListResponse(AbstractModel):
    """CreateCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateCcGeoIPBlockConfigRequest(AbstractModel):
    """CreateCcGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例id
        :type InstanceId: str
        :param _IP: ip地址
        :type IP: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _CcGeoIPBlockConfig: CC区域封禁配置
        :type CcGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._IP = None
        self._Domain = None
        self._Protocol = None
        self._CcGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        """实例id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IP(self):
        """ip地址
        :rtype: str
        """
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CcGeoIPBlockConfig(self):
        """CC区域封禁配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        return self._CcGeoIPBlockConfig

    @CcGeoIPBlockConfig.setter
    def CcGeoIPBlockConfig(self, CcGeoIPBlockConfig):
        self._CcGeoIPBlockConfig = CcGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._IP = params.get("IP")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        if params.get("CcGeoIPBlockConfig") is not None:
            self._CcGeoIPBlockConfig = CcGeoIPBlockConfig()
            self._CcGeoIPBlockConfig._deserialize(params.get("CcGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCcGeoIPBlockConfigResponse(AbstractModel):
    """CreateCcGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDDoSAIRequest(AbstractModel):
    """CreateDDoSAI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdList: 资源实例ID列表
        :type InstanceIdList: list of str
        :param _DDoSAI: AI防护开关，取值[
on(开启)
off(关闭)
]
        :type DDoSAI: str
        """
        self._InstanceIdList = None
        self._DDoSAI = None

    @property
    def InstanceIdList(self):
        """资源实例ID列表
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def DDoSAI(self):
        """AI防护开关，取值[
on(开启)
off(关闭)
]
        :rtype: str
        """
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI


    def _deserialize(self, params):
        self._InstanceIdList = params.get("InstanceIdList")
        self._DDoSAI = params.get("DDoSAI")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSAIResponse(AbstractModel):
    """CreateDDoSAI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDDoSBlackWhiteIpListRequest(AbstractModel):
    """CreateDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _IpList: IP列表
        :type IpList: list of IpSegment
        :param _Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        """IP列表
        :rtype: list of IpSegment
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        """IP类型，取值[black(黑名单IP), white(白名单IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSBlackWhiteIpListResponse(AbstractModel):
    """CreateDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDDoSConnectLimitRequest(AbstractModel):
    """CreateDDoSConnectLimit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例Id
        :type InstanceId: str
        :param _ConnectLimitConfig: 连接抑制配置
        :type ConnectLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.ConnectLimitConfig`
        """
        self._InstanceId = None
        self._ConnectLimitConfig = None

    @property
    def InstanceId(self):
        """资源实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ConnectLimitConfig(self):
        """连接抑制配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ConnectLimitConfig`
        """
        return self._ConnectLimitConfig

    @ConnectLimitConfig.setter
    def ConnectLimitConfig(self, ConnectLimitConfig):
        self._ConnectLimitConfig = ConnectLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ConnectLimitConfig") is not None:
            self._ConnectLimitConfig = ConnectLimitConfig()
            self._ConnectLimitConfig._deserialize(params.get("ConnectLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSConnectLimitResponse(AbstractModel):
    """CreateDDoSConnectLimit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDDoSGeoIPBlockConfigRequest(AbstractModel):
    """CreateDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _DDoSGeoIPBlockConfig: DDoS区域封禁配置，填写参数时配置ID请为空
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._DDoSGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSGeoIPBlockConfig(self):
        """DDoS区域封禁配置，填写参数时配置ID请为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        return self._DDoSGeoIPBlockConfig

    @DDoSGeoIPBlockConfig.setter
    def DDoSGeoIPBlockConfig(self, DDoSGeoIPBlockConfig):
        self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSGeoIPBlockConfigResponse(AbstractModel):
    """CreateDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDDoSSpeedLimitConfigRequest(AbstractModel):
    """CreateDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _DDoSSpeedLimitConfig: 访问限速配置，填写参数时配置ID请为空
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self._InstanceId = None
        self._DDoSSpeedLimitConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSSpeedLimitConfig(self):
        """访问限速配置，填写参数时配置ID请为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        return self._DDoSSpeedLimitConfig

    @DDoSSpeedLimitConfig.setter
    def DDoSSpeedLimitConfig(self, DDoSSpeedLimitConfig):
        self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self._DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDDoSSpeedLimitConfigResponse(AbstractModel):
    """CreateDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateDefaultAlarmThresholdRequest(AbstractModel):
    """CreateDefaultAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DefaultAlarmConfig: 默认告警阈值配置
        :type DefaultAlarmConfig: :class:`tencentcloud.antiddos.v20200309.models.DefaultAlarmThreshold`
        :param _InstanceType: 产品类型，取值[
bgp(表示高防包产品)
bgpip(表示高防IP产品)
]
        :type InstanceType: str
        """
        self._DefaultAlarmConfig = None
        self._InstanceType = None

    @property
    def DefaultAlarmConfig(self):
        """默认告警阈值配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DefaultAlarmThreshold`
        """
        return self._DefaultAlarmConfig

    @DefaultAlarmConfig.setter
    def DefaultAlarmConfig(self, DefaultAlarmConfig):
        self._DefaultAlarmConfig = DefaultAlarmConfig

    @property
    def InstanceType(self):
        """产品类型，取值[
bgp(表示高防包产品)
bgpip(表示高防IP产品)
]
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType


    def _deserialize(self, params):
        if params.get("DefaultAlarmConfig") is not None:
            self._DefaultAlarmConfig = DefaultAlarmThreshold()
            self._DefaultAlarmConfig._deserialize(params.get("DefaultAlarmConfig"))
        self._InstanceType = params.get("InstanceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDefaultAlarmThresholdResponse(AbstractModel):
    """CreateDefaultAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateIPAlarmThresholdConfigRequest(AbstractModel):
    """CreateIPAlarmThresholdConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IpAlarmThresholdConfigList: IP告警阈值配置列表
        :type IpAlarmThresholdConfigList: list of IPAlarmThresholdRelation
        """
        self._IpAlarmThresholdConfigList = None

    @property
    def IpAlarmThresholdConfigList(self):
        """IP告警阈值配置列表
        :rtype: list of IPAlarmThresholdRelation
        """
        return self._IpAlarmThresholdConfigList

    @IpAlarmThresholdConfigList.setter
    def IpAlarmThresholdConfigList(self, IpAlarmThresholdConfigList):
        self._IpAlarmThresholdConfigList = IpAlarmThresholdConfigList


    def _deserialize(self, params):
        if params.get("IpAlarmThresholdConfigList") is not None:
            self._IpAlarmThresholdConfigList = []
            for item in params.get("IpAlarmThresholdConfigList"):
                obj = IPAlarmThresholdRelation()
                obj._deserialize(item)
                self._IpAlarmThresholdConfigList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateIPAlarmThresholdConfigResponse(AbstractModel):
    """CreateIPAlarmThresholdConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateL7RuleCertsRequest(AbstractModel):
    """CreateL7RuleCerts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertId: SSL证书ID
        :type CertId: str
        :param _L7Rules: L7域名转发规则列表
        :type L7Rules: list of InsL7Rules
        """
        self._CertId = None
        self._L7Rules = None

    @property
    def CertId(self):
        """SSL证书ID
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def L7Rules(self):
        """L7域名转发规则列表
        :rtype: list of InsL7Rules
        """
        return self._L7Rules

    @L7Rules.setter
    def L7Rules(self, L7Rules):
        self._L7Rules = L7Rules


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        if params.get("L7Rules") is not None:
            self._L7Rules = []
            for item in params.get("L7Rules"):
                obj = InsL7Rules()
                obj._deserialize(item)
                self._L7Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateL7RuleCertsResponse(AbstractModel):
    """CreateL7RuleCerts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """成功码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreateNewL7RulesRequest(AbstractModel):
    """CreateNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of L7RuleEntry
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _IdList: 资源ID列表
        :type IdList: list of str
        :param _VipList: 资源IP列表
        :type VipList: list of str
        """
        self._Rules = None
        self._Business = None
        self._IdList = None
        self._VipList = None

    @property
    def Rules(self):
        """规则列表
        :rtype: list of L7RuleEntry
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IdList(self):
        """资源ID列表
        :rtype: list of str
        """
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def VipList(self):
        """资源IP列表
        :rtype: list of str
        """
        return self._VipList

    @VipList.setter
    def VipList(self, VipList):
        self._VipList = VipList


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = L7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Business = params.get("Business")
        self._IdList = params.get("IdList")
        self._VipList = params.get("VipList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNewL7RulesResponse(AbstractModel):
    """CreateNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """成功码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class CreatePacketFilterConfigRequest(AbstractModel):
    """CreatePacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _PacketFilterConfig: 特征过滤规则
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self._InstanceId = None
        self._PacketFilterConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PacketFilterConfig(self):
        """特征过滤规则
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePacketFilterConfigResponse(AbstractModel):
    """CreatePacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePortAclConfigListRequest(AbstractModel):
    """CreatePortAclConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceIdList: 资源实例ID列表
        :type InstanceIdList: list of str
        :param _AclConfig: 端口acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self._InstanceIdList = None
        self._AclConfig = None

    @property
    def InstanceIdList(self):
        """资源实例ID列表
        :rtype: list of str
        """
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def AclConfig(self):
        """端口acl策略
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig


    def _deserialize(self, params):
        self._InstanceIdList = params.get("InstanceIdList")
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePortAclConfigListResponse(AbstractModel):
    """CreatePortAclConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePortAclConfigRequest(AbstractModel):
    """CreatePortAclConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _AclConfig: 端口acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self._InstanceId = None
        self._AclConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AclConfig(self):
        """端口acl策略
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePortAclConfigResponse(AbstractModel):
    """CreatePortAclConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateProtocolBlockConfigRequest(AbstractModel):
    """CreateProtocolBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _ProtocolBlockConfig: 协议封禁配置
        :type ProtocolBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        """
        self._InstanceId = None
        self._ProtocolBlockConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def ProtocolBlockConfig(self):
        """协议封禁配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        """
        return self._ProtocolBlockConfig

    @ProtocolBlockConfig.setter
    def ProtocolBlockConfig(self, ProtocolBlockConfig):
        self._ProtocolBlockConfig = ProtocolBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("ProtocolBlockConfig") is not None:
            self._ProtocolBlockConfig = ProtocolBlockConfig()
            self._ProtocolBlockConfig._deserialize(params.get("ProtocolBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProtocolBlockConfigResponse(AbstractModel):
    """CreateProtocolBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSchedulingDomainRequest(AbstractModel):
    """CreateSchedulingDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 代表是否混合云本地化的产品。
hybrid: 宙斯盾本地化
不填写：其他
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        """代表是否混合云本地化的产品。
hybrid: 宙斯盾本地化
不填写：其他
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSchedulingDomainResponse(AbstractModel):
    """CreateSchedulingDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 新创建的域名
        :type Domain: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domain = None
        self._RequestId = None

    @property
    def Domain(self):
        """新创建的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._RequestId = params.get("RequestId")


class CreateWaterPrintConfigRequest(AbstractModel):
    """CreateWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _WaterPrintConfig: 水印防护配置
        :type WaterPrintConfig: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        """
        self._InstanceId = None
        self._WaterPrintConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def WaterPrintConfig(self):
        """水印防护配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        """
        return self._WaterPrintConfig

    @WaterPrintConfig.setter
    def WaterPrintConfig(self, WaterPrintConfig):
        self._WaterPrintConfig = WaterPrintConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("WaterPrintConfig") is not None:
            self._WaterPrintConfig = WaterPrintConfig()
            self._WaterPrintConfig._deserialize(params.get("WaterPrintConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWaterPrintConfigResponse(AbstractModel):
    """CreateWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateWaterPrintKeyRequest(AbstractModel):
    """CreateWaterPrintKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateWaterPrintKeyResponse(AbstractModel):
    """CreateWaterPrintKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DDoSAIRelation(AbstractModel):
    """DDoS防护的AI防护开关

    """

    def __init__(self):
        r"""
        :param _DDoSAI: AI防护开关，取值[
on(开启)
off(关闭)
]
        :type DDoSAI: str
        :param _InstanceDetailList: AI防护开关所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self._DDoSAI = None
        self._InstanceDetailList = None

    @property
    def DDoSAI(self):
        """AI防护开关，取值[
on(开启)
off(关闭)
]
        :rtype: str
        """
        return self._DDoSAI

    @DDoSAI.setter
    def DDoSAI(self, DDoSAI):
        self._DDoSAI = DDoSAI

    @property
    def InstanceDetailList(self):
        """AI防护开关所属的资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        self._DDoSAI = params.get("DDoSAI")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIPBlockConfig(AbstractModel):
    """DDoS防护的区域封禁配置

    """

    def __init__(self):
        r"""
        :param _RegionType: 区域类型，取值[
oversea(境外)
china(国内)
customized(自定义地区)
]
        :type RegionType: str
        :param _Action: 封禁动作，取值[
drop(拦截)
trans(放行)
]
        :type Action: str
        :param _Id: 配置ID，配置添加成功后生成；添加新配置时不用填写此字段，修改或删除配置时需要填写配置ID
        :type Id: str
        :param _AreaList: 当RegionType为customized时，必须填写AreaList，且最多填写128个；
        :type AreaList: list of int
        """
        self._RegionType = None
        self._Action = None
        self._Id = None
        self._AreaList = None

    @property
    def RegionType(self):
        """区域类型，取值[
oversea(境外)
china(国内)
customized(自定义地区)
]
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def Action(self):
        """封禁动作，取值[
drop(拦截)
trans(放行)
]
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Id(self):
        """配置ID，配置添加成功后生成；添加新配置时不用填写此字段，修改或删除配置时需要填写配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def AreaList(self):
        """当RegionType为customized时，必须填写AreaList，且最多填写128个；
        :rtype: list of int
        """
        return self._AreaList

    @AreaList.setter
    def AreaList(self, AreaList):
        self._AreaList = AreaList


    def _deserialize(self, params):
        self._RegionType = params.get("RegionType")
        self._Action = params.get("Action")
        self._Id = params.get("Id")
        self._AreaList = params.get("AreaList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSGeoIPBlockConfigRelation(AbstractModel):
    """DDoS区域封禁配置相关信息

    """

    def __init__(self):
        r"""
        :param _GeoIPBlockConfig: DDoS区域封禁配置
        :type GeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        :param _InstanceDetailList: 配置所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self._GeoIPBlockConfig = None
        self._InstanceDetailList = None

    @property
    def GeoIPBlockConfig(self):
        """DDoS区域封禁配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        return self._GeoIPBlockConfig

    @GeoIPBlockConfig.setter
    def GeoIPBlockConfig(self, GeoIPBlockConfig):
        self._GeoIPBlockConfig = GeoIPBlockConfig

    @property
    def InstanceDetailList(self):
        """配置所属的资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("GeoIPBlockConfig") is not None:
            self._GeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._GeoIPBlockConfig._deserialize(params.get("GeoIPBlockConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimitConfig(AbstractModel):
    """DDoS访问限速配置

    """

    def __init__(self):
        r"""
        :param _Mode: 限速模式，取值[
1(基于源IP限速)
2(基于目的端口限速)
]
        :type Mode: int
        :param _SpeedValues: 限速值，每种类型的限速值最多支持1个；该字段数组至少有一种限速值
        :type SpeedValues: list of SpeedValue
        :param _DstPortScopes: 此字段已弃用，请填写新字段DstPortList。
        :type DstPortScopes: list of PortSegment
        :param _Id: 配置ID，配置添加成功后生成；添加新限制配置时不用填写此字段，修改或删除限速配置时需要填写配置ID
        :type Id: str
        :param _ProtocolList: IP protocol numbers, 取值[
ALL(所有协议)
TCP(tcp协议)
UDP(udp协议)
SMP(smp协议)
1;2-100(自定义协议号范围,最多8个)
]
注意：当自定义协议号范围时，只能填写协议号，多个范围;分隔；当填写ALL时不能再填写其他协议或协议号。
        :type ProtocolList: str
        :param _DstPortList: 端口范围列表，最多8个，多个;分隔，范围表示用-；此端口范围必须填写；填写样式1:0-65535，样式2:80;443;1000-2000
        :type DstPortList: str
        """
        self._Mode = None
        self._SpeedValues = None
        self._DstPortScopes = None
        self._Id = None
        self._ProtocolList = None
        self._DstPortList = None

    @property
    def Mode(self):
        """限速模式，取值[
1(基于源IP限速)
2(基于目的端口限速)
]
        :rtype: int
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def SpeedValues(self):
        """限速值，每种类型的限速值最多支持1个；该字段数组至少有一种限速值
        :rtype: list of SpeedValue
        """
        return self._SpeedValues

    @SpeedValues.setter
    def SpeedValues(self, SpeedValues):
        self._SpeedValues = SpeedValues

    @property
    def DstPortScopes(self):
        """此字段已弃用，请填写新字段DstPortList。
        :rtype: list of PortSegment
        """
        return self._DstPortScopes

    @DstPortScopes.setter
    def DstPortScopes(self, DstPortScopes):
        self._DstPortScopes = DstPortScopes

    @property
    def Id(self):
        """配置ID，配置添加成功后生成；添加新限制配置时不用填写此字段，修改或删除限速配置时需要填写配置ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ProtocolList(self):
        """IP protocol numbers, 取值[
ALL(所有协议)
TCP(tcp协议)
UDP(udp协议)
SMP(smp协议)
1;2-100(自定义协议号范围,最多8个)
]
注意：当自定义协议号范围时，只能填写协议号，多个范围;分隔；当填写ALL时不能再填写其他协议或协议号。
        :rtype: str
        """
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def DstPortList(self):
        """端口范围列表，最多8个，多个;分隔，范围表示用-；此端口范围必须填写；填写样式1:0-65535，样式2:80;443;1000-2000
        :rtype: str
        """
        return self._DstPortList

    @DstPortList.setter
    def DstPortList(self, DstPortList):
        self._DstPortList = DstPortList


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        if params.get("SpeedValues") is not None:
            self._SpeedValues = []
            for item in params.get("SpeedValues"):
                obj = SpeedValue()
                obj._deserialize(item)
                self._SpeedValues.append(obj)
        if params.get("DstPortScopes") is not None:
            self._DstPortScopes = []
            for item in params.get("DstPortScopes"):
                obj = PortSegment()
                obj._deserialize(item)
                self._DstPortScopes.append(obj)
        self._Id = params.get("Id")
        self._ProtocolList = params.get("ProtocolList")
        self._DstPortList = params.get("DstPortList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSSpeedLimitConfigRelation(AbstractModel):
    """DDoS访问限速配置相关信息

    """

    def __init__(self):
        r"""
        :param _SpeedLimitConfig: DDoS访问限速配置
        :type SpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        :param _InstanceDetailList: 配置所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self._SpeedLimitConfig = None
        self._InstanceDetailList = None

    @property
    def SpeedLimitConfig(self):
        """DDoS访问限速配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        return self._SpeedLimitConfig

    @SpeedLimitConfig.setter
    def SpeedLimitConfig(self, SpeedLimitConfig):
        self._SpeedLimitConfig = SpeedLimitConfig

    @property
    def InstanceDetailList(self):
        """配置所属的资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("SpeedLimitConfig") is not None:
            self._SpeedLimitConfig = DDoSSpeedLimitConfig()
            self._SpeedLimitConfig._deserialize(params.get("SpeedLimitConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DefaultAlarmThreshold(AbstractModel):
    """单IP默认告警阈值配置

    """

    def __init__(self):
        r"""
        :param _AlarmType: 告警阈值类型，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type AlarmType: int
        :param _AlarmThreshold: 告警阈值，单位Mbps，取值>=0；当作为输入参数时，设置0会删除告警阈值配置；
        :type AlarmThreshold: int
        """
        self._AlarmType = None
        self._AlarmThreshold = None

    @property
    def AlarmType(self):
        """告警阈值类型，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :rtype: int
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        """告警阈值，单位Mbps，取值>=0；当作为输入参数时，设置0会删除告警阈值配置；
        :rtype: int
        """
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCLevelPolicyRequest(AbstractModel):
    """DeleteCCLevelPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: 配置策略的IP
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议，可取值http
        :type Protocol: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """配置策略的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，可取值http
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCLevelPolicyResponse(AbstractModel):
    """DeleteCCLevelPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCCPrecisionPolicyRequest(AbstractModel):
    """DeleteCCPrecisionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _PolicyId: 策略Id
        :type PolicyId: str
        """
        self._InstanceId = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCPrecisionPolicyResponse(AbstractModel):
    """DeleteCCPrecisionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCCRequestLimitPolicyRequest(AbstractModel):
    """DeleteCCRequestLimitPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _PolicyId: 策略Id
        :type PolicyId: str
        """
        self._InstanceId = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCRequestLimitPolicyResponse(AbstractModel):
    """DeleteCCRequestLimitPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCCThresholdPolicyRequest(AbstractModel):
    """DeleteCCThresholdPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: 配置策略的IP
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议，可取值http
        :type Protocol: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """配置策略的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，可取值http
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCCThresholdPolicyResponse(AbstractModel):
    """DeleteCCThresholdPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCcBlackWhiteIpListRequest(AbstractModel):
    """DeleteCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _PolicyId: 策略Id
        :type PolicyId: str
        """
        self._InstanceId = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcBlackWhiteIpListResponse(AbstractModel):
    """DeleteCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteCcGeoIPBlockConfigRequest(AbstractModel):
    """DeleteCcGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _CcGeoIPBlockConfig: CC区域封禁配置，填写参数时配置ID不能为空
        :type CcGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._CcGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def CcGeoIPBlockConfig(self):
        """CC区域封禁配置，填写参数时配置ID不能为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CcGeoIPBlockConfig`
        """
        return self._CcGeoIPBlockConfig

    @CcGeoIPBlockConfig.setter
    def CcGeoIPBlockConfig(self, CcGeoIPBlockConfig):
        self._CcGeoIPBlockConfig = CcGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("CcGeoIPBlockConfig") is not None:
            self._CcGeoIPBlockConfig = CcGeoIPBlockConfig()
            self._CcGeoIPBlockConfig._deserialize(params.get("CcGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCcGeoIPBlockConfigResponse(AbstractModel):
    """DeleteCcGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDDoSBlackWhiteIpListRequest(AbstractModel):
    """DeleteDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _IpList: IP列表
        :type IpList: list of IpSegment
        :param _Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        """IP列表
        :rtype: list of IpSegment
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        """IP类型，取值[black(黑名单IP), white(白名单IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSBlackWhiteIpListResponse(AbstractModel):
    """DeleteDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDDoSGeoIPBlockConfigRequest(AbstractModel):
    """DeleteDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _DDoSGeoIPBlockConfig: DDoS区域封禁配置，填写参数时配置ID不能为空
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._DDoSGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSGeoIPBlockConfig(self):
        """DDoS区域封禁配置，填写参数时配置ID不能为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        return self._DDoSGeoIPBlockConfig

    @DDoSGeoIPBlockConfig.setter
    def DDoSGeoIPBlockConfig(self, DDoSGeoIPBlockConfig):
        self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSGeoIPBlockConfigResponse(AbstractModel):
    """DeleteDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteDDoSSpeedLimitConfigRequest(AbstractModel):
    """DeleteDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _DDoSSpeedLimitConfig: 访问限速配置，填写参数时配置ID不能为空
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self._InstanceId = None
        self._DDoSSpeedLimitConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSSpeedLimitConfig(self):
        """访问限速配置，填写参数时配置ID不能为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        return self._DDoSSpeedLimitConfig

    @DDoSSpeedLimitConfig.setter
    def DDoSSpeedLimitConfig(self, DDoSSpeedLimitConfig):
        self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self._DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDDoSSpeedLimitConfigResponse(AbstractModel):
    """DeleteDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePacketFilterConfigRequest(AbstractModel):
    """DeletePacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _PacketFilterConfig: 特征过滤配置
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self._InstanceId = None
        self._PacketFilterConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PacketFilterConfig(self):
        """特征过滤配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePacketFilterConfigResponse(AbstractModel):
    """DeletePacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePortAclConfigRequest(AbstractModel):
    """DeletePortAclConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _AclConfig: 端口acl策略
        :type AclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self._InstanceId = None
        self._AclConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def AclConfig(self):
        """端口acl策略
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        return self._AclConfig

    @AclConfig.setter
    def AclConfig(self, AclConfig):
        self._AclConfig = AclConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("AclConfig") is not None:
            self._AclConfig = AclConfig()
            self._AclConfig._deserialize(params.get("AclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePortAclConfigResponse(AbstractModel):
    """DeletePortAclConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWaterPrintConfigRequest(AbstractModel):
    """DeleteWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWaterPrintConfigResponse(AbstractModel):
    """DeleteWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteWaterPrintKeyRequest(AbstractModel):
    """DeleteWaterPrintKey请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _KeyId: 水印密钥ID
        :type KeyId: str
        """
        self._InstanceId = None
        self._KeyId = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def KeyId(self):
        """水印密钥ID
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._KeyId = params.get("KeyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteWaterPrintKeyResponse(AbstractModel):
    """DeleteWaterPrintKey返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeBGPIPL7RulesRequest(AbstractModel):
    """DescribeBGPIPL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type StatusList: list of int non-negative
        :param _Domain: 域名搜索，选填，当需要搜索域名请填写
        :type Domain: str
        :param _Ip: IP搜索，选填，当需要搜索IP请填写
        :type Ip: str
        :param _Limit: 一页条数，默认值100，最大值100，超过100最大返回100条
        :type Limit: int
        :param _Offset: 规则偏移量，取值为(页码-1)*一页条数
        :type Offset: int
        :param _ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param _Cname: 高防IP实例的Cname
        :type Cname: str
        :param _Export: 默认为false，当为true时，将不对各个规则做策略检查，直接导出所有规则
        :type Export: bool
        :param _Source: 源站，模糊查询
        :type Source: str
        """
        self._Business = None
        self._StatusList = None
        self._Domain = None
        self._Ip = None
        self._Limit = None
        self._Offset = None
        self._ProtocolList = None
        self._Cname = None
        self._Export = None
        self._Source = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StatusList(self):
        """状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :rtype: list of int non-negative
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def Domain(self):
        """域名搜索，选填，当需要搜索域名请填写
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        """IP搜索，选填，当需要搜索IP请填写
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Limit(self):
        """一页条数，默认值100，最大值100，超过100最大返回100条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """规则偏移量，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProtocolList(self):
        """转发协议搜索，选填，取值[http, https, http/https]
        :rtype: list of str
        """
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def Cname(self):
        """高防IP实例的Cname
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Export(self):
        """默认为false，当为true时，将不对各个规则做策略检查，直接导出所有规则
        :rtype: bool
        """
        return self._Export

    @Export.setter
    def Export(self, Export):
        self._Export = Export

    @property
    def Source(self):
        """源站，模糊查询
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StatusList = params.get("StatusList")
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProtocolList = params.get("ProtocolList")
        self._Cname = params.get("Cname")
        self._Export = params.get("Export")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBGPIPL7RulesResponse(AbstractModel):
    """DescribeBGPIPL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转发规则列表
        :type Rules: list of BGPIPL7RuleEntry
        :param _Healths: 健康检查配置列表
        :type Healths: list of L7RuleHealth
        :param _Total: 总规则数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Healths = None
        self._Total = None
        self._RequestId = None

    @property
    def Rules(self):
        """转发规则列表
        :rtype: list of BGPIPL7RuleEntry
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Healths(self):
        """健康检查配置列表
        :rtype: list of L7RuleHealth
        """
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def Total(self):
        """总规则数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = BGPIPL7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeBasicDeviceStatusRequest(AbstractModel):
    """DescribeBasicDeviceStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _IpList: IP 资源列表
        :type IpList: list of str
        :param _IdList: 域名化资源传id
        :type IdList: list of str
        :param _FilterRegion: 地域名称
        :type FilterRegion: int
        :param _CnameWafIdList: cnameWaf资源
        :type CnameWafIdList: list of str
        """
        self._IpList = None
        self._IdList = None
        self._FilterRegion = None
        self._CnameWafIdList = None

    @property
    def IpList(self):
        """IP 资源列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def IdList(self):
        """域名化资源传id
        :rtype: list of str
        """
        return self._IdList

    @IdList.setter
    def IdList(self, IdList):
        self._IdList = IdList

    @property
    def FilterRegion(self):
        """地域名称
        :rtype: int
        """
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion

    @property
    def CnameWafIdList(self):
        """cnameWaf资源
        :rtype: list of str
        """
        return self._CnameWafIdList

    @CnameWafIdList.setter
    def CnameWafIdList(self, CnameWafIdList):
        self._CnameWafIdList = CnameWafIdList


    def _deserialize(self, params):
        self._IpList = params.get("IpList")
        self._IdList = params.get("IdList")
        self._FilterRegion = params.get("FilterRegion")
        self._CnameWafIdList = params.get("CnameWafIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBasicDeviceStatusResponse(AbstractModel):
    """DescribeBasicDeviceStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 返回资源及状态，状态码：
1 - 封堵状态
2 - 正常状态
3 - 攻击状态
        :type Data: list of KeyValue
        :param _CLBData: 域名化资产的名称
        :type CLBData: list of KeyValue
        :param _CnameWafData: cnamewaf资源状态
        :type CnameWafData: list of KeyValue
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._CLBData = None
        self._CnameWafData = None
        self._RequestId = None

    @property
    def Data(self):
        """返回资源及状态，状态码：
1 - 封堵状态
2 - 正常状态
3 - 攻击状态
        :rtype: list of KeyValue
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def CLBData(self):
        """域名化资产的名称
        :rtype: list of KeyValue
        """
        return self._CLBData

    @CLBData.setter
    def CLBData(self, CLBData):
        self._CLBData = CLBData

    @property
    def CnameWafData(self):
        """cnamewaf资源状态
        :rtype: list of KeyValue
        """
        return self._CnameWafData

    @CnameWafData.setter
    def CnameWafData(self, CnameWafData):
        self._CnameWafData = CnameWafData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = KeyValue()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("CLBData") is not None:
            self._CLBData = []
            for item in params.get("CLBData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._CLBData.append(obj)
        if params.get("CnameWafData") is not None:
            self._CnameWafData = []
            for item in params.get("CnameWafData"):
                obj = KeyValue()
                obj._deserialize(item)
                self._CnameWafData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeBgpBizTrendRequest(AbstractModel):
    """DescribeBgpBizTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgp-multip表示高防包）
        :type Business: str
        :param _StartTime: 统计开始时间。 例：“2020-09-22 00:00:00”，注意该时间必须为5分钟的倍数
        :type StartTime: str
        :param _EndTime: 统计结束时间。 例：“2020-09-22 00:00:00”，注意该时间必须为5分钟的倍数
        :type EndTime: str
        :param _MetricName: 统计维度，可取值intraffic, outtraffic, inpkg, outpkg； intraffic：入流量 outtraffic：出流量 inpkg：入包速率 outpkg：出包速率
        :type MetricName: str
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _Flag: 0表示固定时间，1表示自定义时间
        :type Flag: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._InstanceId = None
        self._Flag = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgp-multip表示高防包）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StartTime(self):
        """统计开始时间。 例：“2020-09-22 00:00:00”，注意该时间必须为5分钟的倍数
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间。 例：“2020-09-22 00:00:00”，注意该时间必须为5分钟的倍数
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """统计维度，可取值intraffic, outtraffic, inpkg, outpkg； intraffic：入流量 outtraffic：出流量 inpkg：入包速率 outpkg：出包速率
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Flag(self):
        """0表示固定时间，1表示自定义时间
        :rtype: int
        """
        return self._Flag

    @Flag.setter
    def Flag(self, Flag):
        self._Flag = Flag


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._InstanceId = params.get("InstanceId")
        self._Flag = params.get("Flag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBgpBizTrendResponse(AbstractModel):
    """DescribeBgpBizTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 曲线图各个时间点的值
        :type DataList: list of int non-negative
        :param _Total: 曲线图取值个数
        :type Total: int
        :param _MetricName: 统计纬度
        :type MetricName: str
        :param _MaxData: 返回数组最大值
        :type MaxData: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._Total = None
        self._MetricName = None
        self._MaxData = None
        self._RequestId = None

    @property
    def DataList(self):
        """曲线图各个时间点的值
        :rtype: list of int non-negative
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def Total(self):
        """曲线图取值个数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def MetricName(self):
        """统计纬度
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MaxData(self):
        """返回数组最大值
        :rtype: int
        """
        return self._MaxData

    @MaxData.setter
    def MaxData(self, MaxData):
        self._MaxData = MaxData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataList = params.get("DataList")
        self._Total = params.get("Total")
        self._MetricName = params.get("MetricName")
        self._MaxData = params.get("MaxData")
        self._RequestId = params.get("RequestId")


class DescribeBizHttpStatusRequest(AbstractModel):
    """DescribeBizHttpStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Statistics: 统计方式，仅支持sum
        :type Statistics: str
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Period: 统计周期，可取值60，300，1800，3600， 21600，86400，单位秒
        :type Period: int
        :param _StartTime: 统计开始时间。 如2020-02-01 12:04:12
        :type StartTime: str
        :param _EndTime: 统计结束时间。如2020-02-03 18:03:23
        :type EndTime: str
        :param _Id: 资源Id
        :type Id: str
        :param _Domain: 特定域名查询
        :type Domain: str
        :param _ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :type ProtoInfo: list of ProtocolPort
        """
        self._Statistics = None
        self._Business = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._Domain = None
        self._ProtoInfo = None

    @property
    def Statistics(self):
        """统计方式，仅支持sum
        :rtype: str
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Period(self):
        """统计周期，可取值60，300，1800，3600， 21600，86400，单位秒
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间。 如2020-02-01 12:04:12
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间。如2020-02-03 18:03:23
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        """资源Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        """特定域名查询
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProtoInfo(self):
        """协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :rtype: list of ProtocolPort
        """
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo


    def _deserialize(self, params):
        self._Statistics = params.get("Statistics")
        self._Business = params.get("Business")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizHttpStatusResponse(AbstractModel):
    """DescribeBizHttpStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _HttpStatusMap: 业务流量http状态码统计数据
        :type HttpStatusMap: :class:`tencentcloud.antiddos.v20200309.models.HttpStatusMap`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._HttpStatusMap = None
        self._RequestId = None

    @property
    def HttpStatusMap(self):
        """业务流量http状态码统计数据
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.HttpStatusMap`
        """
        return self._HttpStatusMap

    @HttpStatusMap.setter
    def HttpStatusMap(self, HttpStatusMap):
        self._HttpStatusMap = HttpStatusMap

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("HttpStatusMap") is not None:
            self._HttpStatusMap = HttpStatusMap()
            self._HttpStatusMap._deserialize(params.get("HttpStatusMap"))
        self._RequestId = params.get("RequestId")


class DescribeBizMonitorTrendRequest(AbstractModel):
    """DescribeBizMonitorTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _StartTime: 统计开始时间。 例：“2020-09-22 00:00:00”
        :type StartTime: str
        :param _EndTime: 统计结束时间。 例：“2020-09-22 00:00:00”
        :type EndTime: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _MetricName: 统计纬度，可取值intraffic outtraffic inpkg outpkg
        :type MetricName: str
        :param _Period: 时间粒度 60 300 3600 21600 86400
        :type Period: int
        """
        self._Business = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._MetricName = None
        self._Period = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StartTime(self):
        """统计开始时间。 例：“2020-09-22 00:00:00”
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间。 例：“2020-09-22 00:00:00”
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        """资源实例ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        """统计纬度，可取值intraffic outtraffic inpkg outpkg
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Period(self):
        """时间粒度 60 300 3600 21600 86400
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizMonitorTrendResponse(AbstractModel):
    """DescribeBizMonitorTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 曲线图各个时间点的值
        :type DataList: list of float
        :param _MetricName: 统计纬度
        :type MetricName: str
        :param _MaxData: 返回DataList中的最大值
        :type MaxData: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._MetricName = None
        self._MaxData = None
        self._RequestId = None

    @property
    def DataList(self):
        """曲线图各个时间点的值
        :rtype: list of float
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def MetricName(self):
        """统计纬度
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MaxData(self):
        """返回DataList中的最大值
        :rtype: int
        """
        return self._MaxData

    @MaxData.setter
    def MaxData(self, MaxData):
        self._MaxData = MaxData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataList = params.get("DataList")
        self._MetricName = params.get("MetricName")
        self._MaxData = params.get("MaxData")
        self._RequestId = params.get("RequestId")


class DescribeBizTrendRequest(AbstractModel):
    """DescribeBizTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Statistics: 统计方式，可取值max, min, avg, sum, 如统计纬度是流量速率或包量速率，仅可取值max
        :type Statistics: str
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Period: 统计周期，可取值60，300，1800，3600，21600，86400，单位秒
        :type Period: int
        :param _StartTime: 统计开始时间。 例：“2020-09-22 00:00:00”
        :type StartTime: str
        :param _EndTime: 统计结束时间。 例：“2020-09-22 00:00:00”
        :type EndTime: str
        :param _Id: 资源实例ID
        :type Id: str
        :param _MetricName: 统计纬度，可取值connum, new_conn, inactive_conn, intraffic, outtraffic, inpkg, outpkg, qps
        :type MetricName: str
        :param _Domain: 统计纬度为qps时，可选特定域名查询
        :type Domain: str
        :param _ProtoInfo: 协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :type ProtoInfo: list of ProtocolPort
        :param _BusinessType: 业务类型可取值domain, port
port：端口业务
domain：域名业务
        :type BusinessType: str
        """
        self._Statistics = None
        self._Business = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Id = None
        self._MetricName = None
        self._Domain = None
        self._ProtoInfo = None
        self._BusinessType = None

    @property
    def Statistics(self):
        """统计方式，可取值max, min, avg, sum, 如统计纬度是流量速率或包量速率，仅可取值max
        :rtype: str
        """
        return self._Statistics

    @Statistics.setter
    def Statistics(self, Statistics):
        self._Statistics = Statistics

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Period(self):
        """统计周期，可取值60，300，1800，3600，21600，86400，单位秒
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间。 例：“2020-09-22 00:00:00”
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间。 例：“2020-09-22 00:00:00”
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Id(self):
        """资源实例ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        """统计纬度，可取值connum, new_conn, inactive_conn, intraffic, outtraffic, inpkg, outpkg, qps
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Domain(self):
        """统计纬度为qps时，可选特定域名查询
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProtoInfo(self):
        """协议及端口列表，协议可取值TCP, UDP, HTTP, HTTPS，仅统计纬度为连接数时有效
        :rtype: list of ProtocolPort
        """
        return self._ProtoInfo

    @ProtoInfo.setter
    def ProtoInfo(self, ProtoInfo):
        self._ProtoInfo = ProtoInfo

    @property
    def BusinessType(self):
        """业务类型可取值domain, port
port：端口业务
domain：域名业务
        :rtype: str
        """
        return self._BusinessType

    @BusinessType.setter
    def BusinessType(self, BusinessType):
        self._BusinessType = BusinessType


    def _deserialize(self, params):
        self._Statistics = params.get("Statistics")
        self._Business = params.get("Business")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._Domain = params.get("Domain")
        if params.get("ProtoInfo") is not None:
            self._ProtoInfo = []
            for item in params.get("ProtoInfo"):
                obj = ProtocolPort()
                obj._deserialize(item)
                self._ProtoInfo.append(obj)
        self._BusinessType = params.get("BusinessType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBizTrendResponse(AbstractModel):
    """DescribeBizTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DataList: 曲线图各个时间点的值
        :type DataList: list of float
        :param _MetricName: 统计纬度
        :type MetricName: str
        :param _MaxData: 返回DataList中的最大值
        :type MaxData: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DataList = None
        self._MetricName = None
        self._MaxData = None
        self._RequestId = None

    @property
    def DataList(self):
        """曲线图各个时间点的值
        :rtype: list of float
        """
        return self._DataList

    @DataList.setter
    def DataList(self, DataList):
        self._DataList = DataList

    @property
    def MetricName(self):
        """统计纬度
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def MaxData(self):
        """返回DataList中的最大值
        :rtype: int
        """
        return self._MaxData

    @MaxData.setter
    def MaxData(self, MaxData):
        self._MaxData = MaxData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DataList = params.get("DataList")
        self._MetricName = params.get("MetricName")
        self._MaxData = params.get("MaxData")
        self._RequestId = params.get("RequestId")


class DescribeCCLevelListRequest(AbstractModel):
    """DescribeCCLevelList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgp-multip表示高防包）
        :type Business: str
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _InstanceId: 指定实例Id
        :type InstanceId: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgp-multip表示高防包）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        """指定实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCLevelListResponse(AbstractModel):
    """DescribeCCLevelList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 分级策略列表总数
        :type Total: int
        :param _LevelList: 分级策略列表总数
        :type LevelList: list of CCLevelPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._LevelList = None
        self._RequestId = None

    @property
    def Total(self):
        """分级策略列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def LevelList(self):
        """分级策略列表总数
        :rtype: list of CCLevelPolicy
        """
        return self._LevelList

    @LevelList.setter
    def LevelList(self, LevelList):
        self._LevelList = LevelList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("LevelList") is not None:
            self._LevelList = []
            for item in params.get("LevelList"):
                obj = CCLevelPolicy()
                obj._deserialize(item)
                self._LevelList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCLevelPolicyRequest(AbstractModel):
    """DescribeCCLevelPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP值
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议，可取值http、https、http/https
        :type Protocol: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP值
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，可取值http、https、http/https
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCLevelPolicyResponse(AbstractModel):
    """DescribeCCLevelPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Level: CC防护等级，可取值loose表示宽松，strict表示严格，normal表示适中， emergency表示攻击紧急， sup_loose表示超级宽松，default表示默认策略（无频控配置下发），customized表示自定义策略
        :type Level: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Level = None
        self._RequestId = None

    @property
    def Level(self):
        """CC防护等级，可取值loose表示宽松，strict表示严格，normal表示适中， emergency表示攻击紧急， sup_loose表示超级宽松，default表示默认策略（无频控配置下发），customized表示自定义策略
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Level = params.get("Level")
        self._RequestId = params.get("RequestId")


class DescribeCCPrecisionPlyListRequest(AbstractModel):
    """DescribeCCPrecisionPlyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip-multip：表示高防包；bgpip：表示高防IP）
        :type Business: str
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _InstanceId: 指定特定实例Id
        :type InstanceId: str
        :param _Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param _Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param _Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip-multip：表示高防包；bgpip：表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        """指定特定实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址，普通高防IP要传该字段
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名，普通高防IP要传该字段
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，普通高防IP要传该字段
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCPrecisionPlyListResponse(AbstractModel):
    """DescribeCCPrecisionPlyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 策略列表总数
        :type Total: int
        :param _PrecisionPolicyList: 策略列表详情
        :type PrecisionPolicyList: list of CCPrecisionPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._PrecisionPolicyList = None
        self._RequestId = None

    @property
    def Total(self):
        """策略列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def PrecisionPolicyList(self):
        """策略列表详情
        :rtype: list of CCPrecisionPolicy
        """
        return self._PrecisionPolicyList

    @PrecisionPolicyList.setter
    def PrecisionPolicyList(self, PrecisionPolicyList):
        self._PrecisionPolicyList = PrecisionPolicyList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("PrecisionPolicyList") is not None:
            self._PrecisionPolicyList = []
            for item in params.get("PrecisionPolicyList"):
                obj = CCPrecisionPolicy()
                obj._deserialize(item)
                self._PrecisionPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCReqLimitPolicyListRequest(AbstractModel):
    """DescribeCCReqLimitPolicyList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgp-multip表示高防包，bgpip表示高防IP）
        :type Business: str
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _InstanceId: 指定实例Id
        :type InstanceId: str
        :param _Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param _Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param _Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgp-multip表示高防包，bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        """指定实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址，普通高防IP要传该字段
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名，普通高防IP要传该字段
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，普通高防IP要传该字段
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCReqLimitPolicyListResponse(AbstractModel):
    """DescribeCCReqLimitPolicyList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 频率限制列表总数
        :type Total: int
        :param _RequestLimitPolicyList: 频率限制列表详情
        :type RequestLimitPolicyList: list of CCReqLimitPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._RequestLimitPolicyList = None
        self._RequestId = None

    @property
    def Total(self):
        """频率限制列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestLimitPolicyList(self):
        """频率限制列表详情
        :rtype: list of CCReqLimitPolicy
        """
        return self._RequestLimitPolicyList

    @RequestLimitPolicyList.setter
    def RequestLimitPolicyList(self, RequestLimitPolicyList):
        self._RequestLimitPolicyList = RequestLimitPolicyList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("RequestLimitPolicyList") is not None:
            self._RequestLimitPolicyList = []
            for item in params.get("RequestLimitPolicyList"):
                obj = CCReqLimitPolicy()
                obj._deserialize(item)
                self._RequestLimitPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCThresholdListRequest(AbstractModel):
    """DescribeCCThresholdList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgp-multip表示高防包）
        :type Business: str
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _InstanceId: 指定实例Id
        :type InstanceId: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgp-multip表示高防包）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        """指定实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCThresholdListResponse(AbstractModel):
    """DescribeCCThresholdList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 清洗阈值策略列表总数
        :type Total: int
        :param _ThresholdList: 清洗阈值策略列表详情
        :type ThresholdList: list of CCThresholdPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ThresholdList = None
        self._RequestId = None

    @property
    def Total(self):
        """清洗阈值策略列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ThresholdList(self):
        """清洗阈值策略列表详情
        :rtype: list of CCThresholdPolicy
        """
        return self._ThresholdList

    @ThresholdList.setter
    def ThresholdList(self, ThresholdList):
        self._ThresholdList = ThresholdList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ThresholdList") is not None:
            self._ThresholdList = []
            for item in params.get("ThresholdList"):
                obj = CCThresholdPolicy()
                obj._deserialize(item)
                self._ThresholdList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCCTrendRequest(AbstractModel):
    """DescribeCCTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :type MetricName: str
        :param _Domain: 域名，可选
        :type Domain: str
        :param _Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        """
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Domain = None
        self._Id = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        """资源的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Period(self):
        """统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Domain(self):
        """域名，可选
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Id(self):
        """资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Domain = params.get("Domain")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCCTrendResponse(AbstractModel):
    """DescribeCCTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 值个数
        :type Count: int
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Data: 值数组
        :type Data: list of int non-negative
        :param _Id: 资源ID
        :type Id: str
        :param _MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :type MetricName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Id = None
        self._MetricName = None
        self._RequestId = None

    @property
    def Count(self):
        """值个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        """资源的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Period(self):
        """统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        """值数组
        :rtype: list of int non-negative
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Id(self):
        """资源ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        """指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeCcBlackWhiteIpListRequest(AbstractModel):
    """DescribeCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgp-multip：表示高防包；bgpip：表示高防IP）
        :type Business: str
        :param _InstanceId: 指定特定实例Id
        :type InstanceId: str
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param _Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param _Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        :param _FilterIp: 筛选IP，需要筛选黑白名单IP时传该字段
        :type FilterIp: str
        :param _FilterType: 黑白名单筛选字段，需要筛选黑白名单列表时传该字段
        :type FilterType: str
        """
        self._Business = None
        self._InstanceId = None
        self._Offset = None
        self._Limit = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._FilterIp = None
        self._FilterType = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgp-multip：表示高防包；bgpip：表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def InstanceId(self):
        """指定特定实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Ip(self):
        """IP地址，普通高防IP要传该字段
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名，普通高防IP要传该字段
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，普通高防IP要传该字段
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def FilterIp(self):
        """筛选IP，需要筛选黑白名单IP时传该字段
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterType(self):
        """黑白名单筛选字段，需要筛选黑白名单列表时传该字段
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._InstanceId = params.get("InstanceId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._FilterIp = params.get("FilterIp")
        self._FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcBlackWhiteIpListResponse(AbstractModel):
    """DescribeCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: CC四层黑白名单策略列表总数
        :type Total: int
        :param _CcBlackWhiteIpList: CC四层黑白名单策略列表详情
        :type CcBlackWhiteIpList: list of CcBlackWhiteIpPolicy
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._CcBlackWhiteIpList = None
        self._RequestId = None

    @property
    def Total(self):
        """CC四层黑白名单策略列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CcBlackWhiteIpList(self):
        """CC四层黑白名单策略列表详情
        :rtype: list of CcBlackWhiteIpPolicy
        """
        return self._CcBlackWhiteIpList

    @CcBlackWhiteIpList.setter
    def CcBlackWhiteIpList(self, CcBlackWhiteIpList):
        self._CcBlackWhiteIpList = CcBlackWhiteIpList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CcBlackWhiteIpList") is not None:
            self._CcBlackWhiteIpList = []
            for item in params.get("CcBlackWhiteIpList"):
                obj = CcBlackWhiteIpPolicy()
                obj._deserialize(item)
                self._CcBlackWhiteIpList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCcGeoIPBlockConfigListRequest(AbstractModel):
    """DescribeCcGeoIPBlockConfigList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip-multip：表示高防包；bgpip：表示高防IP）
        :type Business: str
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _InstanceId: 指定特定实例ID
        :type InstanceId: str
        :param _Ip: IP地址，普通高防IP要传该字段
        :type Ip: str
        :param _Domain: 域名，普通高防IP要传该字段
        :type Domain: str
        :param _Protocol: 协议，普通高防IP要传该字段
        :type Protocol: str
        """
        self._Business = None
        self._Offset = None
        self._Limit = None
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip-multip：表示高防包；bgpip：表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def InstanceId(self):
        """指定特定实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址，普通高防IP要传该字段
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名，普通高防IP要传该字段
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，普通高防IP要传该字段
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcGeoIPBlockConfigListResponse(AbstractModel):
    """DescribeCcGeoIPBlockConfigList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: CC地域封禁策略列表总数
        :type Total: int
        :param _CcGeoIpPolicyList: CC地域封禁策略列表详情
        :type CcGeoIpPolicyList: list of CcGeoIpPolicyNew
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._CcGeoIpPolicyList = None
        self._RequestId = None

    @property
    def Total(self):
        """CC地域封禁策略列表总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def CcGeoIpPolicyList(self):
        """CC地域封禁策略列表详情
        :rtype: list of CcGeoIpPolicyNew
        """
        return self._CcGeoIpPolicyList

    @CcGeoIpPolicyList.setter
    def CcGeoIpPolicyList(self, CcGeoIpPolicyList):
        self._CcGeoIpPolicyList = CcGeoIpPolicyList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("CcGeoIpPolicyList") is not None:
            self._CcGeoIpPolicyList = []
            for item in params.get("CcGeoIpPolicyList"):
                obj = CcGeoIpPolicyNew()
                obj._deserialize(item)
                self._CcGeoIpPolicyList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSBlackWhiteIpListRequest(AbstractModel):
    """DescribeDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        """
        self._InstanceId = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSBlackWhiteIpListResponse(AbstractModel):
    """DescribeDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BlackIpList: 黑名单IP列表
        :type BlackIpList: list of IpSegment
        :param _WhiteIpList: 白名单IP列表
        :type WhiteIpList: list of IpSegment
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BlackIpList = None
        self._WhiteIpList = None
        self._RequestId = None

    @property
    def BlackIpList(self):
        """黑名单IP列表
        :rtype: list of IpSegment
        """
        return self._BlackIpList

    @BlackIpList.setter
    def BlackIpList(self, BlackIpList):
        self._BlackIpList = BlackIpList

    @property
    def WhiteIpList(self):
        """白名单IP列表
        :rtype: list of IpSegment
        """
        return self._WhiteIpList

    @WhiteIpList.setter
    def WhiteIpList(self, WhiteIpList):
        self._WhiteIpList = WhiteIpList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BlackIpList") is not None:
            self._BlackIpList = []
            for item in params.get("BlackIpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._BlackIpList.append(obj)
        if params.get("WhiteIpList") is not None:
            self._WhiteIpList = []
            for item in params.get("WhiteIpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._WhiteIpList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSConnectLimitListRequest(AbstractModel):
    """DescribeDDoSConnectLimitList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数
        :type Limit: int
        :param _FilterIp: 可选参数，按照IP进行过滤
        :type FilterIp: str
        :param _FilterInstanceId: 可选参数，按照实例id进行过滤
        :type FilterInstanceId: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterIp = None
        self._FilterInstanceId = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterIp(self):
        """可选参数，按照IP进行过滤
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterInstanceId(self):
        """可选参数，按照实例id进行过滤
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterIp = params.get("FilterIp")
        self._FilterInstanceId = params.get("FilterInstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSConnectLimitListResponse(AbstractModel):
    """DescribeDDoSConnectLimitList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 连接抑制配置总数
        :type Total: int
        :param _ConfigList: 连接抑制配置详情信息
        :type ConfigList: list of ConnectLimitRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """连接抑制配置总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """连接抑制配置详情信息
        :rtype: list of ConnectLimitRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ConnectLimitRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDDoSTrendRequest(AbstractModel):
    """DescribeDDoSTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Ip: 资源实例的IP
        :type Ip: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _Id: 资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :type Id: str
        """
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Id = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        """资源实例的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Period(self):
        """统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Id(self):
        """资源实例ID，当Business为basic时，此字段不用填写（因为基础防护没有资源实例）
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSTrendResponse(AbstractModel):
    """DescribeDDoSTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 值个数
        :type Count: int
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :type Business: str
        :param _Ip: 资源的IP
        :type Ip: str
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _Data: 值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :type Data: list of int non-negative
        :param _Id: 资源ID
        :type Id: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._Business = None
        self._Ip = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._Data = None
        self._Id = None
        self._MetricName = None
        self._RequestId = None

    @property
    def Count(self):
        """值个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版；basic表示DDoS基础防护）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Ip(self):
        """资源的IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Period(self):
        """统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Data(self):
        """值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :rtype: list of int non-negative
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Id(self):
        """资源ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MetricName(self):
        """指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Business = params.get("Business")
        self._Ip = params.get("Ip")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Data = params.get("Data")
        self._Id = params.get("Id")
        self._MetricName = params.get("MetricName")
        self._RequestId = params.get("RequestId")


class DescribeDefaultAlarmThresholdRequest(AbstractModel):
    """DescribeDefaultAlarmThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceType: 产品类型，取值[
bgp(表示高防包产品)
bgpip(表示高防IP产品)
]
        :type InstanceType: str
        :param _FilterAlarmType: 告警阈值类型搜索，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type FilterAlarmType: int
        """
        self._InstanceType = None
        self._FilterAlarmType = None

    @property
    def InstanceType(self):
        """产品类型，取值[
bgp(表示高防包产品)
bgpip(表示高防IP产品)
]
        :rtype: str
        """
        return self._InstanceType

    @InstanceType.setter
    def InstanceType(self, InstanceType):
        self._InstanceType = InstanceType

    @property
    def FilterAlarmType(self):
        """告警阈值类型搜索，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :rtype: int
        """
        return self._FilterAlarmType

    @FilterAlarmType.setter
    def FilterAlarmType(self, FilterAlarmType):
        self._FilterAlarmType = FilterAlarmType


    def _deserialize(self, params):
        self._InstanceType = params.get("InstanceType")
        self._FilterAlarmType = params.get("FilterAlarmType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDefaultAlarmThresholdResponse(AbstractModel):
    """DescribeDefaultAlarmThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DefaultAlarmConfigList: 默认告警阈值配置
        :type DefaultAlarmConfigList: list of DefaultAlarmThreshold
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DefaultAlarmConfigList = None
        self._RequestId = None

    @property
    def DefaultAlarmConfigList(self):
        """默认告警阈值配置
        :rtype: list of DefaultAlarmThreshold
        """
        return self._DefaultAlarmConfigList

    @DefaultAlarmConfigList.setter
    def DefaultAlarmConfigList(self, DefaultAlarmConfigList):
        self._DefaultAlarmConfigList = DefaultAlarmConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DefaultAlarmConfigList") is not None:
            self._DefaultAlarmConfigList = []
            for item in params.get("DefaultAlarmConfigList"):
                obj = DefaultAlarmThreshold()
                obj._deserialize(item)
                self._DefaultAlarmConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpBlockListRequest(AbstractModel):
    """DescribeIpBlockList请求参数结构体

    """


class DescribeIpBlockListResponse(AbstractModel):
    """DescribeIpBlockList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _List: IP封堵列表
        :type List: list of IpBlockData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._List = None
        self._RequestId = None

    @property
    def List(self):
        """IP封堵列表
        :rtype: list of IpBlockData
        """
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = IpBlockData()
                obj._deserialize(item)
                self._List.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeL7RulesBySSLCertIdRequest(AbstractModel):
    """DescribeL7RulesBySSLCertId请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 域名状态，可取bindable, binded, opened, closed, all，all表示全部状态
        :type Status: str
        :param _CertIds: 证书ID列表
        :type CertIds: list of str
        """
        self._Status = None
        self._CertIds = None

    @property
    def Status(self):
        """域名状态，可取bindable, binded, opened, closed, all，all表示全部状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertIds(self):
        """证书ID列表
        :rtype: list of str
        """
        return self._CertIds

    @CertIds.setter
    def CertIds(self, CertIds):
        self._CertIds = CertIds


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._CertIds = params.get("CertIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeL7RulesBySSLCertIdResponse(AbstractModel):
    """DescribeL7RulesBySSLCertId返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertSet: 证书规则集合
        :type CertSet: list of CertIdInsL7Rules
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertSet = None
        self._RequestId = None

    @property
    def CertSet(self):
        """证书规则集合
        :rtype: list of CertIdInsL7Rules
        """
        return self._CertSet

    @CertSet.setter
    def CertSet(self, CertSet):
        self._CertSet = CertSet

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertSet") is not None:
            self._CertSet = []
            for item in params.get("CertSet"):
                obj = CertIdInsL7Rules()
                obj._deserialize(item)
                self._CertSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListBGPIPInstancesRequest(AbstractModel):
    """DescribeListBGPIPInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :type Limit: int
        :param _FilterIp: IP搜索
        :type FilterIp: str
        :param _FilterInstanceId: 资产实例ID搜索，例如，bgpip-00000001
        :type FilterInstanceId: str
        :param _FilterLine: 高防IP线路搜索，取值为[
1：BGP线路
2：电信
3：联通
4：移动
99：第三方合作线路
]
        :type FilterLine: int
        :param _FilterRegion: 地域搜索，例如，ap-guangzhou
        :type FilterRegion: str
        :param _FilterName: 名称搜索
        :type FilterName: str
        :param _FilterEipType: 是否只获取高防弹性公网IP实例。填写时，只能填写1或者0。当填写1时，表示返回高防弹性公网IP实例。当填写0时，表示返回非高防弹性公网IP实例。
        :type FilterEipType: int
        :param _FilterEipEipAddressStatus: 高防弹性公网IP实例的绑定状态搜索条件，取值范围 [BINDING、 BIND、UNBINDING、UNBIND]。该搜索条件只在FilterEipType=1时才有效。
        :type FilterEipEipAddressStatus: list of str
        :param _FilterDamDDoSStatus: 是否只获取安全加速实例。填写时，只能填写1或者0。当填写1时，表示返回安全加速实例。当填写0时，表示返回非安全加速实例。
        :type FilterDamDDoSStatus: int
        :param _FilterStatus: 获取特定状态的资源，运行中填idle，攻击中填attacking，封堵中填blocking，试用资源填trial
        :type FilterStatus: str
        :param _FilterCname: 获取特定的实例Cname
        :type FilterCname: str
        :param _FilterInstanceIdList: 批量查询实例ID对应的高防IP实例资源
        :type FilterInstanceIdList: list of str
        :param _FilterTag: 标签搜索
        :type FilterTag: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        :param _FilterPackType: 按照套餐类型进行过滤
        :type FilterPackType: list of str
        :param _FilterConvoy: 重保护航搜索
        :type FilterConvoy: int
        """
        self._Offset = None
        self._Limit = None
        self._FilterIp = None
        self._FilterInstanceId = None
        self._FilterLine = None
        self._FilterRegion = None
        self._FilterName = None
        self._FilterEipType = None
        self._FilterEipEipAddressStatus = None
        self._FilterDamDDoSStatus = None
        self._FilterStatus = None
        self._FilterCname = None
        self._FilterInstanceIdList = None
        self._FilterTag = None
        self._FilterPackType = None
        self._FilterConvoy = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterInstanceId(self):
        """资产实例ID搜索，例如，bgpip-00000001
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterLine(self):
        """高防IP线路搜索，取值为[
1：BGP线路
2：电信
3：联通
4：移动
99：第三方合作线路
]
        :rtype: int
        """
        return self._FilterLine

    @FilterLine.setter
    def FilterLine(self, FilterLine):
        self._FilterLine = FilterLine

    @property
    def FilterRegion(self):
        """地域搜索，例如，ap-guangzhou
        :rtype: str
        """
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion

    @property
    def FilterName(self):
        """名称搜索
        :rtype: str
        """
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName

    @property
    def FilterEipType(self):
        """是否只获取高防弹性公网IP实例。填写时，只能填写1或者0。当填写1时，表示返回高防弹性公网IP实例。当填写0时，表示返回非高防弹性公网IP实例。
        :rtype: int
        """
        return self._FilterEipType

    @FilterEipType.setter
    def FilterEipType(self, FilterEipType):
        self._FilterEipType = FilterEipType

    @property
    def FilterEipEipAddressStatus(self):
        """高防弹性公网IP实例的绑定状态搜索条件，取值范围 [BINDING、 BIND、UNBINDING、UNBIND]。该搜索条件只在FilterEipType=1时才有效。
        :rtype: list of str
        """
        return self._FilterEipEipAddressStatus

    @FilterEipEipAddressStatus.setter
    def FilterEipEipAddressStatus(self, FilterEipEipAddressStatus):
        self._FilterEipEipAddressStatus = FilterEipEipAddressStatus

    @property
    def FilterDamDDoSStatus(self):
        """是否只获取安全加速实例。填写时，只能填写1或者0。当填写1时，表示返回安全加速实例。当填写0时，表示返回非安全加速实例。
        :rtype: int
        """
        return self._FilterDamDDoSStatus

    @FilterDamDDoSStatus.setter
    def FilterDamDDoSStatus(self, FilterDamDDoSStatus):
        self._FilterDamDDoSStatus = FilterDamDDoSStatus

    @property
    def FilterStatus(self):
        """获取特定状态的资源，运行中填idle，攻击中填attacking，封堵中填blocking，试用资源填trial
        :rtype: str
        """
        return self._FilterStatus

    @FilterStatus.setter
    def FilterStatus(self, FilterStatus):
        self._FilterStatus = FilterStatus

    @property
    def FilterCname(self):
        """获取特定的实例Cname
        :rtype: str
        """
        return self._FilterCname

    @FilterCname.setter
    def FilterCname(self, FilterCname):
        self._FilterCname = FilterCname

    @property
    def FilterInstanceIdList(self):
        """批量查询实例ID对应的高防IP实例资源
        :rtype: list of str
        """
        return self._FilterInstanceIdList

    @FilterInstanceIdList.setter
    def FilterInstanceIdList(self, FilterInstanceIdList):
        self._FilterInstanceIdList = FilterInstanceIdList

    @property
    def FilterTag(self):
        """标签搜索
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        """
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def FilterPackType(self):
        """按照套餐类型进行过滤
        :rtype: list of str
        """
        return self._FilterPackType

    @FilterPackType.setter
    def FilterPackType(self, FilterPackType):
        self._FilterPackType = FilterPackType

    @property
    def FilterConvoy(self):
        """重保护航搜索
        :rtype: int
        """
        return self._FilterConvoy

    @FilterConvoy.setter
    def FilterConvoy(self, FilterConvoy):
        self._FilterConvoy = FilterConvoy


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterIp = params.get("FilterIp")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterLine = params.get("FilterLine")
        self._FilterRegion = params.get("FilterRegion")
        self._FilterName = params.get("FilterName")
        self._FilterEipType = params.get("FilterEipType")
        self._FilterEipEipAddressStatus = params.get("FilterEipEipAddressStatus")
        self._FilterDamDDoSStatus = params.get("FilterDamDDoSStatus")
        self._FilterStatus = params.get("FilterStatus")
        self._FilterCname = params.get("FilterCname")
        self._FilterInstanceIdList = params.get("FilterInstanceIdList")
        if params.get("FilterTag") is not None:
            self._FilterTag = TagFilter()
            self._FilterTag._deserialize(params.get("FilterTag"))
        self._FilterPackType = params.get("FilterPackType")
        self._FilterConvoy = params.get("FilterConvoy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBGPIPInstancesResponse(AbstractModel):
    """DescribeListBGPIPInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _InstanceList: 高防IP资产实例列表
        :type InstanceList: list of BGPIPInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def InstanceList(self):
        """高防IP资产实例列表
        :rtype: list of BGPIPInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = BGPIPInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListBGPInstancesRequest(AbstractModel):
    """DescribeListBGPInstances请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :type Limit: int
        :param _FilterIp: IP搜索
        :type FilterIp: str
        :param _FilterInstanceId: 资产实例ID搜索，例如，bgp-00000001
        :type FilterInstanceId: str
        :param _FilterRegion: 地域搜索，例如，ap-guangzhou
        :type FilterRegion: str
        :param _FilterName: 名称搜索
        :type FilterName: str
        :param _FilterLine: 按照线路搜索, 1: BGP; 2: 三网
        :type FilterLine: int
        :param _FilterStatus: 状态搜索，idle：运行中；attacking：攻击中；blocking：封堵中
        :type FilterStatus: str
        :param _FilterBoundStatus: 高防包绑定状态搜索，bounding：绑定中； failed：绑定失败
        :type FilterBoundStatus: str
        :param _FilterInstanceIdList: 实例id数组
        :type FilterInstanceIdList: list of str
        :param _FilterEnterpriseFlag: 企业版搜索,  1：包含重保护航套餐下的企业版列表, 2: 不包含重保护航套餐的企业版列表
        :type FilterEnterpriseFlag: int
        :param _FilterLightFlag: 轻量版搜索
        :type FilterLightFlag: int
        :param _FilterChannelFlag: 定制版搜索
        :type FilterChannelFlag: int
        :param _FilterTag: 标签搜索
        :type FilterTag: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        :param _FilterTrialFlag: 试用资源搜索，1: 应急防护资源；2：PLG试用资源
        :type FilterTrialFlag: int
        :param _FilterConvoy: 重保护航搜索
        :type FilterConvoy: int
        :param _ExcludeAdvancedInfo: 默认false；接口传true，返回数据中不包含高级信息，高级信息包含：InstanceList[0].Usage。
        :type ExcludeAdvancedInfo: bool
        :param _FilterAssetIpList: 资产IP数组
        :type FilterAssetIpList: list of str
        :param _FilterBasicPlusFlag: 是否包含基础防护增强版 0: 不包含 1: 包含
        :type FilterBasicPlusFlag: int
        :param _FilterPlanCntFlag: 是否标准版2.0 0: 包含标准版2.0 0 1: 只查询标准版2.0 0 2: 不查标准版2.0
        :type FilterPlanCntFlag: int
        :param _FilterTransRegionFlag: 是否跨区域产品 0: 不包含跨区域产品 1: 中国大陆跨区域产品 2: 非中国大陆跨区域产品 3: 包含全部
        :type FilterTransRegionFlag: int
        :param _FilterZoneIdList: zoenid列表
        :type FilterZoneIdList: list of int
        """
        self._Offset = None
        self._Limit = None
        self._FilterIp = None
        self._FilterInstanceId = None
        self._FilterRegion = None
        self._FilterName = None
        self._FilterLine = None
        self._FilterStatus = None
        self._FilterBoundStatus = None
        self._FilterInstanceIdList = None
        self._FilterEnterpriseFlag = None
        self._FilterLightFlag = None
        self._FilterChannelFlag = None
        self._FilterTag = None
        self._FilterTrialFlag = None
        self._FilterConvoy = None
        self._ExcludeAdvancedInfo = None
        self._FilterAssetIpList = None
        self._FilterBasicPlusFlag = None
        self._FilterPlanCntFlag = None
        self._FilterTransRegionFlag = None
        self._FilterZoneIdList = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterInstanceId(self):
        """资产实例ID搜索，例如，bgp-00000001
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterRegion(self):
        """地域搜索，例如，ap-guangzhou
        :rtype: str
        """
        return self._FilterRegion

    @FilterRegion.setter
    def FilterRegion(self, FilterRegion):
        self._FilterRegion = FilterRegion

    @property
    def FilterName(self):
        """名称搜索
        :rtype: str
        """
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName

    @property
    def FilterLine(self):
        """按照线路搜索, 1: BGP; 2: 三网
        :rtype: int
        """
        return self._FilterLine

    @FilterLine.setter
    def FilterLine(self, FilterLine):
        self._FilterLine = FilterLine

    @property
    def FilterStatus(self):
        """状态搜索，idle：运行中；attacking：攻击中；blocking：封堵中
        :rtype: str
        """
        return self._FilterStatus

    @FilterStatus.setter
    def FilterStatus(self, FilterStatus):
        self._FilterStatus = FilterStatus

    @property
    def FilterBoundStatus(self):
        """高防包绑定状态搜索，bounding：绑定中； failed：绑定失败
        :rtype: str
        """
        return self._FilterBoundStatus

    @FilterBoundStatus.setter
    def FilterBoundStatus(self, FilterBoundStatus):
        self._FilterBoundStatus = FilterBoundStatus

    @property
    def FilterInstanceIdList(self):
        """实例id数组
        :rtype: list of str
        """
        return self._FilterInstanceIdList

    @FilterInstanceIdList.setter
    def FilterInstanceIdList(self, FilterInstanceIdList):
        self._FilterInstanceIdList = FilterInstanceIdList

    @property
    def FilterEnterpriseFlag(self):
        """企业版搜索,  1：包含重保护航套餐下的企业版列表, 2: 不包含重保护航套餐的企业版列表
        :rtype: int
        """
        return self._FilterEnterpriseFlag

    @FilterEnterpriseFlag.setter
    def FilterEnterpriseFlag(self, FilterEnterpriseFlag):
        self._FilterEnterpriseFlag = FilterEnterpriseFlag

    @property
    def FilterLightFlag(self):
        """轻量版搜索
        :rtype: int
        """
        return self._FilterLightFlag

    @FilterLightFlag.setter
    def FilterLightFlag(self, FilterLightFlag):
        self._FilterLightFlag = FilterLightFlag

    @property
    def FilterChannelFlag(self):
        """定制版搜索
        :rtype: int
        """
        return self._FilterChannelFlag

    @FilterChannelFlag.setter
    def FilterChannelFlag(self, FilterChannelFlag):
        self._FilterChannelFlag = FilterChannelFlag

    @property
    def FilterTag(self):
        """标签搜索
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.TagFilter`
        """
        return self._FilterTag

    @FilterTag.setter
    def FilterTag(self, FilterTag):
        self._FilterTag = FilterTag

    @property
    def FilterTrialFlag(self):
        """试用资源搜索，1: 应急防护资源；2：PLG试用资源
        :rtype: int
        """
        return self._FilterTrialFlag

    @FilterTrialFlag.setter
    def FilterTrialFlag(self, FilterTrialFlag):
        self._FilterTrialFlag = FilterTrialFlag

    @property
    def FilterConvoy(self):
        """重保护航搜索
        :rtype: int
        """
        return self._FilterConvoy

    @FilterConvoy.setter
    def FilterConvoy(self, FilterConvoy):
        self._FilterConvoy = FilterConvoy

    @property
    def ExcludeAdvancedInfo(self):
        """默认false；接口传true，返回数据中不包含高级信息，高级信息包含：InstanceList[0].Usage。
        :rtype: bool
        """
        return self._ExcludeAdvancedInfo

    @ExcludeAdvancedInfo.setter
    def ExcludeAdvancedInfo(self, ExcludeAdvancedInfo):
        self._ExcludeAdvancedInfo = ExcludeAdvancedInfo

    @property
    def FilterAssetIpList(self):
        """资产IP数组
        :rtype: list of str
        """
        return self._FilterAssetIpList

    @FilterAssetIpList.setter
    def FilterAssetIpList(self, FilterAssetIpList):
        self._FilterAssetIpList = FilterAssetIpList

    @property
    def FilterBasicPlusFlag(self):
        """是否包含基础防护增强版 0: 不包含 1: 包含
        :rtype: int
        """
        return self._FilterBasicPlusFlag

    @FilterBasicPlusFlag.setter
    def FilterBasicPlusFlag(self, FilterBasicPlusFlag):
        self._FilterBasicPlusFlag = FilterBasicPlusFlag

    @property
    def FilterPlanCntFlag(self):
        """是否标准版2.0 0: 包含标准版2.0 0 1: 只查询标准版2.0 0 2: 不查标准版2.0
        :rtype: int
        """
        return self._FilterPlanCntFlag

    @FilterPlanCntFlag.setter
    def FilterPlanCntFlag(self, FilterPlanCntFlag):
        self._FilterPlanCntFlag = FilterPlanCntFlag

    @property
    def FilterTransRegionFlag(self):
        """是否跨区域产品 0: 不包含跨区域产品 1: 中国大陆跨区域产品 2: 非中国大陆跨区域产品 3: 包含全部
        :rtype: int
        """
        return self._FilterTransRegionFlag

    @FilterTransRegionFlag.setter
    def FilterTransRegionFlag(self, FilterTransRegionFlag):
        self._FilterTransRegionFlag = FilterTransRegionFlag

    @property
    def FilterZoneIdList(self):
        """zoenid列表
        :rtype: list of int
        """
        return self._FilterZoneIdList

    @FilterZoneIdList.setter
    def FilterZoneIdList(self, FilterZoneIdList):
        self._FilterZoneIdList = FilterZoneIdList


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterIp = params.get("FilterIp")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterRegion = params.get("FilterRegion")
        self._FilterName = params.get("FilterName")
        self._FilterLine = params.get("FilterLine")
        self._FilterStatus = params.get("FilterStatus")
        self._FilterBoundStatus = params.get("FilterBoundStatus")
        self._FilterInstanceIdList = params.get("FilterInstanceIdList")
        self._FilterEnterpriseFlag = params.get("FilterEnterpriseFlag")
        self._FilterLightFlag = params.get("FilterLightFlag")
        self._FilterChannelFlag = params.get("FilterChannelFlag")
        if params.get("FilterTag") is not None:
            self._FilterTag = TagFilter()
            self._FilterTag._deserialize(params.get("FilterTag"))
        self._FilterTrialFlag = params.get("FilterTrialFlag")
        self._FilterConvoy = params.get("FilterConvoy")
        self._ExcludeAdvancedInfo = params.get("ExcludeAdvancedInfo")
        self._FilterAssetIpList = params.get("FilterAssetIpList")
        self._FilterBasicPlusFlag = params.get("FilterBasicPlusFlag")
        self._FilterPlanCntFlag = params.get("FilterPlanCntFlag")
        self._FilterTransRegionFlag = params.get("FilterTransRegionFlag")
        self._FilterZoneIdList = params.get("FilterZoneIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBGPInstancesResponse(AbstractModel):
    """DescribeListBGPInstances返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _InstanceList: 高防包资产实例列表
        :type InstanceList: list of BGPInstance
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._InstanceList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def InstanceList(self):
        """高防包资产实例列表
        :rtype: list of BGPInstance
        """
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = BGPInstance()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListBlackWhiteIpListRequest(AbstractModel):
    """DescribeListBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListBlackWhiteIpListResponse(AbstractModel):
    """DescribeListBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _IpList: 黑白IP列表
        :type IpList: list of BlackWhiteIpRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._IpList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def IpList(self):
        """黑白IP列表
        :rtype: list of BlackWhiteIpRelation
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = BlackWhiteIpRelation()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListDDoSAIRequest(AbstractModel):
    """DescribeListDDoSAI请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSAIResponse(AbstractModel):
    """DescribeListDDoSAI返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: AI防护开关列表
        :type ConfigList: list of DDoSAIRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """AI防护开关列表
        :rtype: list of DDoSAIRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSAIRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListDDoSGeoIPBlockConfigRequest(AbstractModel):
    """DescribeListDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSGeoIPBlockConfigResponse(AbstractModel):
    """DescribeListDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: DDoS区域封禁配置列表
        :type ConfigList: list of DDoSGeoIPBlockConfigRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """DDoS区域封禁配置列表
        :rtype: list of DDoSGeoIPBlockConfigRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSGeoIPBlockConfigRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListDDoSSpeedLimitConfigRequest(AbstractModel):
    """DescribeListDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListDDoSSpeedLimitConfigResponse(AbstractModel):
    """DescribeListDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: 访问限速配置列表
        :type ConfigList: list of DDoSSpeedLimitConfigRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """访问限速配置列表
        :rtype: list of DDoSSpeedLimitConfigRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = DDoSSpeedLimitConfigRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListIPAlarmConfigRequest(AbstractModel):
    """DescribeListIPAlarmConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterAlarmType: 告警阈值类型搜索，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type FilterAlarmType: int
        :param _FilterIp: IP搜索
        :type FilterIp: str
        :param _FilterCname: 高防IP实例资源的cname
        :type FilterCname: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterAlarmType = None
        self._FilterIp = None
        self._FilterCname = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterAlarmType(self):
        """告警阈值类型搜索，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :rtype: int
        """
        return self._FilterAlarmType

    @FilterAlarmType.setter
    def FilterAlarmType(self, FilterAlarmType):
        self._FilterAlarmType = FilterAlarmType

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def FilterCname(self):
        """高防IP实例资源的cname
        :rtype: str
        """
        return self._FilterCname

    @FilterCname.setter
    def FilterCname(self, FilterCname):
        self._FilterCname = FilterCname


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterAlarmType = params.get("FilterAlarmType")
        self._FilterIp = params.get("FilterIp")
        self._FilterCname = params.get("FilterCname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListIPAlarmConfigResponse(AbstractModel):
    """DescribeListIPAlarmConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: IP告警阈值配置列表
        :type ConfigList: list of IPAlarmThresholdRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """IP告警阈值配置列表
        :rtype: list of IPAlarmThresholdRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = IPAlarmThresholdRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListListenerRequest(AbstractModel):
    """DescribeListListener请求参数结构体

    """


class DescribeListListenerResponse(AbstractModel):
    """DescribeListListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Layer4Listeners: 4层转发监听器列表
        :type Layer4Listeners: list of Layer4Rule
        :param _Layer7Listeners: 7层转发监听器列表
        :type Layer7Listeners: list of Layer7Rule
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Layer4Listeners = None
        self._Layer7Listeners = None
        self._RequestId = None

    @property
    def Layer4Listeners(self):
        """4层转发监听器列表
        :rtype: list of Layer4Rule
        """
        return self._Layer4Listeners

    @Layer4Listeners.setter
    def Layer4Listeners(self, Layer4Listeners):
        self._Layer4Listeners = Layer4Listeners

    @property
    def Layer7Listeners(self):
        """7层转发监听器列表
        :rtype: list of Layer7Rule
        """
        return self._Layer7Listeners

    @Layer7Listeners.setter
    def Layer7Listeners(self, Layer7Listeners):
        self._Layer7Listeners = Layer7Listeners

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Layer4Listeners") is not None:
            self._Layer4Listeners = []
            for item in params.get("Layer4Listeners"):
                obj = Layer4Rule()
                obj._deserialize(item)
                self._Layer4Listeners.append(obj)
        if params.get("Layer7Listeners") is not None:
            self._Layer7Listeners = []
            for item in params.get("Layer7Listeners"):
                obj = Layer7Rule()
                obj._deserialize(item)
                self._Layer7Listeners.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListPacketFilterConfigRequest(AbstractModel):
    """DescribeListPacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListPacketFilterConfigResponse(AbstractModel):
    """DescribeListPacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: 特征过滤配置
        :type ConfigList: list of PacketFilterRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """特征过滤配置
        :rtype: list of PacketFilterRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = PacketFilterRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListPortAclListRequest(AbstractModel):
    """DescribeListPortAclList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: ip搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """ip搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListPortAclListResponse(AbstractModel):
    """DescribeListPortAclList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _AclList: 端口acl策略
        :type AclList: list of AclConfigRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._AclList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def AclList(self):
        """端口acl策略
        :rtype: list of AclConfigRelation
        """
        return self._AclList

    @AclList.setter
    def AclList(self, AclList):
        self._AclList = AclList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("AclList") is not None:
            self._AclList = []
            for item in params.get("AclList"):
                obj = AclConfigRelation()
                obj._deserialize(item)
                self._AclList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListProtocolBlockConfigRequest(AbstractModel):
    """DescribeListProtocolBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListProtocolBlockConfigResponse(AbstractModel):
    """DescribeListProtocolBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: 协议封禁配置
        :type ConfigList: list of ProtocolBlockRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """协议封禁配置
        :rtype: list of ProtocolBlockRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = ProtocolBlockRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListSchedulingDomainRequest(AbstractModel):
    """DescribeListSchedulingDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :type Limit: int
        :param _FilterDomain: 调度域名搜索
        :type FilterDomain: str
        :param _Status: 运行状态 0 代表未运行  1 正在运行  2 运行异常 
        :type Status: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterDomain = None
        self._Status = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为20;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterDomain(self):
        """调度域名搜索
        :rtype: str
        """
        return self._FilterDomain

    @FilterDomain.setter
    def FilterDomain(self, FilterDomain):
        self._FilterDomain = FilterDomain

    @property
    def Status(self):
        """运行状态 0 代表未运行  1 正在运行  2 运行异常 
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterDomain = params.get("FilterDomain")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListSchedulingDomainResponse(AbstractModel):
    """DescribeListSchedulingDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _DomainList: 调度域名信息列表
        :type DomainList: list of SchedulingDomainInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._DomainList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def DomainList(self):
        """调度域名信息列表
        :rtype: list of SchedulingDomainInfo
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = SchedulingDomainInfo()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeListWaterPrintConfigRequest(AbstractModel):
    """DescribeListWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 页起始偏移，取值为(页码-1)*一页条数
        :type Offset: int
        :param _Limit: 一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :type Limit: int
        :param _FilterInstanceId: 资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :type FilterInstanceId: str
        :param _FilterIp: IP搜索
        :type FilterIp: str
        """
        self._Offset = None
        self._Limit = None
        self._FilterInstanceId = None
        self._FilterIp = None

    @property
    def Offset(self):
        """页起始偏移，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """一页条数，当Limit=0时，默认一页条数为100;最大取值为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def FilterInstanceId(self):
        """资源实例ID搜索, 支持资源实例前缀通配搜索，例如bgp-*表示获取高防包类型的资源实例
        :rtype: str
        """
        return self._FilterInstanceId

    @FilterInstanceId.setter
    def FilterInstanceId(self, FilterInstanceId):
        self._FilterInstanceId = FilterInstanceId

    @property
    def FilterIp(self):
        """IP搜索
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._FilterInstanceId = params.get("FilterInstanceId")
        self._FilterIp = params.get("FilterIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListWaterPrintConfigResponse(AbstractModel):
    """DescribeListWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 总数
        :type Total: int
        :param _ConfigList: 水印配置列表
        :type ConfigList: list of WaterPrintRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._ConfigList = None
        self._RequestId = None

    @property
    def Total(self):
        """总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def ConfigList(self):
        """水印配置列表
        :rtype: list of WaterPrintRelation
        """
        return self._ConfigList

    @ConfigList.setter
    def ConfigList(self, ConfigList):
        self._ConfigList = ConfigList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("ConfigList") is not None:
            self._ConfigList = []
            for item in params.get("ConfigList"):
                obj = WaterPrintRelation()
                obj._deserialize(item)
                self._ConfigList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeNewL7RulesErrHealthRequest(AbstractModel):
    """DescribeNewL7RulesErrHealth请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号(bgpip表示高防IP)
        :type Business: str
        :param _RuleIdList: 规则Id列表
        :type RuleIdList: list of str
        """
        self._Business = None
        self._RuleIdList = None

    @property
    def Business(self):
        """DDoS防护子产品代号(bgpip表示高防IP)
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def RuleIdList(self):
        """规则Id列表
        :rtype: list of str
        """
        return self._RuleIdList

    @RuleIdList.setter
    def RuleIdList(self, RuleIdList):
        self._RuleIdList = RuleIdList


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesErrHealthResponse(AbstractModel):
    """DescribeNewL7RulesErrHealth返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ErrHealths: 异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP及错误信息，多个IP用","分割
        :type ErrHealths: list of KeyValue
        :param _Total: 异常规则的总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ErrHealths = None
        self._Total = None
        self._RequestId = None

    @property
    def ErrHealths(self):
        """异常规则列表，返回值说明: Key值为规则ID，Value值为异常IP及错误信息，多个IP用","分割
        :rtype: list of KeyValue
        """
        return self._ErrHealths

    @ErrHealths.setter
    def ErrHealths(self, ErrHealths):
        self._ErrHealths = ErrHealths

    @property
    def Total(self):
        """异常规则的总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("ErrHealths") is not None:
            self._ErrHealths = []
            for item in params.get("ErrHealths"):
                obj = KeyValue()
                obj._deserialize(item)
                self._ErrHealths.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeNewL7RulesRequest(AbstractModel):
    """DescribeNewL7Rules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _StatusList: 状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type StatusList: list of int non-negative
        :param _Domain: 域名搜索，选填，当需要搜索域名请填写
        :type Domain: str
        :param _Ip: IP搜索，选填，当需要搜索IP请填写
        :type Ip: str
        :param _Limit: 一页条数，默认值100，最大值100，超过100最大返回100条
        :type Limit: int
        :param _Offset: 规则偏移量，取值为(页码-1)*一页条数
        :type Offset: int
        :param _ProtocolList: 转发协议搜索，选填，取值[http, https, http/https]
        :type ProtocolList: list of str
        :param _Cname: 高防IP实例的Cname
        :type Cname: str
        :param _Export: 默认为false，当为true时，将不对各个规则做策略检查，直接导出所有规则
        :type Export: bool
        """
        self._Business = None
        self._StatusList = None
        self._Domain = None
        self._Ip = None
        self._Limit = None
        self._Offset = None
        self._ProtocolList = None
        self._Cname = None
        self._Export = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def StatusList(self):
        """状态搜索，选填，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :rtype: list of int non-negative
        """
        return self._StatusList

    @StatusList.setter
    def StatusList(self, StatusList):
        self._StatusList = StatusList

    @property
    def Domain(self):
        """域名搜索，选填，当需要搜索域名请填写
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Ip(self):
        """IP搜索，选填，当需要搜索IP请填写
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Limit(self):
        """一页条数，默认值100，最大值100，超过100最大返回100条
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """规则偏移量，取值为(页码-1)*一页条数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def ProtocolList(self):
        """转发协议搜索，选填，取值[http, https, http/https]
        :rtype: list of str
        """
        return self._ProtocolList

    @ProtocolList.setter
    def ProtocolList(self, ProtocolList):
        self._ProtocolList = ProtocolList

    @property
    def Cname(self):
        """高防IP实例的Cname
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Export(self):
        """默认为false，当为true时，将不对各个规则做策略检查，直接导出所有规则
        :rtype: bool
        """
        return self._Export

    @Export.setter
    def Export(self, Export):
        self._Export = Export


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._StatusList = params.get("StatusList")
        self._Domain = params.get("Domain")
        self._Ip = params.get("Ip")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._ProtocolList = params.get("ProtocolList")
        self._Cname = params.get("Cname")
        self._Export = params.get("Export")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNewL7RulesResponse(AbstractModel):
    """DescribeNewL7Rules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 转发规则列表
        :type Rules: list of NewL7RuleEntry
        :param _Healths: 健康检查配置列表
        :type Healths: list of L7RuleHealth
        :param _Total: 总规则数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._Healths = None
        self._Total = None
        self._RequestId = None

    @property
    def Rules(self):
        """转发规则列表
        :rtype: list of NewL7RuleEntry
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Healths(self):
        """健康检查配置列表
        :rtype: list of L7RuleHealth
        """
        return self._Healths

    @Healths.setter
    def Healths(self, Healths):
        self._Healths = Healths

    @property
    def Total(self):
        """总规则数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = NewL7RuleEntry()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("Healths") is not None:
            self._Healths = []
            for item in params.get("Healths"):
                obj = L7RuleHealth()
                obj._deserialize(item)
                self._Healths.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeOverviewAttackTrendRequest(AbstractModel):
    """DescribeOverviewAttackTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 攻击类型，取值ddos， cc
        :type Type: str
        :param _Dimension: 纬度，当前仅支持attackcount
        :type Dimension: str
        :param _Period: 周期，当前仅支持86400
        :type Period: int
        :param _StartTime: 防护概览攻击趋势开始时间
        :type StartTime: str
        :param _EndTime: 防护概览攻击趋势结束时间
        :type EndTime: str
        """
        self._Type = None
        self._Dimension = None
        self._Period = None
        self._StartTime = None
        self._EndTime = None

    @property
    def Type(self):
        """攻击类型，取值ddos， cc
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Dimension(self):
        """纬度，当前仅支持attackcount
        :rtype: str
        """
        return self._Dimension

    @Dimension.setter
    def Dimension(self, Dimension):
        self._Dimension = Dimension

    @property
    def Period(self):
        """周期，当前仅支持86400
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """防护概览攻击趋势开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """防护概览攻击趋势结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Dimension = params.get("Dimension")
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewAttackTrendResponse(AbstractModel):
    """DescribeOverviewAttackTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Type: 攻击类型
        :type Type: str
        :param _StartTime: 防护概览攻击趋势起始时间
        :type StartTime: str
        :param _EndTime: 防护概览攻击趋势结束时间
        :type EndTime: str
        :param _Period: 周期
        :type Period: int
        :param _Data: 每个周期点的攻击次数
        :type Data: list of int non-negative
        :param _Count: 包含的周期点数
        :type Count: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Type = None
        self._StartTime = None
        self._EndTime = None
        self._Period = None
        self._Data = None
        self._Count = None
        self._RequestId = None

    @property
    def Type(self):
        """攻击类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def StartTime(self):
        """防护概览攻击趋势起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """防护概览攻击趋势结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Period(self):
        """周期
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def Data(self):
        """每个周期点的攻击次数
        :rtype: list of int non-negative
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Count(self):
        """包含的周期点数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Period = params.get("Period")
        self._Data = params.get("Data")
        self._Count = params.get("Count")
        self._RequestId = params.get("RequestId")


class DescribeOverviewCCTrendRequest(AbstractModel):
    """DescribeOverviewCCTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :type MetricName: str
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp-multip表示共享包；basic表示DDoS基础防护）
        :type Business: str
        :param _IpList: 资源的IP
        :type IpList: list of str
        :param _Id: 资源实例ID
        :type Id: str
        """
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Business = None
        self._IpList = None
        self._Id = None

    @property
    def Period(self):
        """统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """指标，取值[inqps(总请求峰值，dropqps(攻击请求峰值))，incount(请求次数), dropcount(攻击次数)]
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp-multip表示共享包；basic表示DDoS基础防护）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IpList(self):
        """资源的IP
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Id(self):
        """资源实例ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Business = params.get("Business")
        self._IpList = params.get("IpList")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewCCTrendResponse(AbstractModel):
    """DescribeOverviewCCTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 值个数
        :type Count: int
        :param _Data: 值数组
        :type Data: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._Data = None
        self._RequestId = None

    @property
    def Count(self):
        """值个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Data(self):
        """值数组
        :rtype: list of int non-negative
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeOverviewDDoSEventListRequest(AbstractModel):
    """DescribeOverviewDDoSEventList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _AttackStatus: 可选按攻击状态过滤，start：攻击中；end：攻击结束
        :type AttackStatus: str
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 记录条数
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._AttackStatus = None
        self._Offset = None
        self._Limit = None

    @property
    def StartTime(self):
        """起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AttackStatus(self):
        """可选按攻击状态过滤，start：攻击中；end：攻击结束
        :rtype: str
        """
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def Offset(self):
        """偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """记录条数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AttackStatus = params.get("AttackStatus")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewDDoSEventListResponse(AbstractModel):
    """DescribeOverviewDDoSEventList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 记录总数
        :type Total: int
        :param _EventList: 事件列表
        :type EventList: list of OverviewDDoSEvent
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._EventList = None
        self._RequestId = None

    @property
    def Total(self):
        """记录总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def EventList(self):
        """事件列表
        :rtype: list of OverviewDDoSEvent
        """
        return self._EventList

    @EventList.setter
    def EventList(self, EventList):
        self._EventList = EventList

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("EventList") is not None:
            self._EventList = []
            for item in params.get("EventList"):
                obj = OverviewDDoSEvent()
                obj._deserialize(item)
                self._EventList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOverviewDDoSTrendRequest(AbstractModel):
    """DescribeOverviewDDoSTrend请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Period: 统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :type Period: int
        :param _StartTime: 统计开始时间
        :type StartTime: str
        :param _EndTime: 统计结束时间
        :type EndTime: str
        :param _MetricName: 指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :type MetricName: str
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp-multip表示高防包；basic表示DDoS基础防护）
        :type Business: str
        :param _IpList: 资源实例的IP列表
        :type IpList: list of str
        :param _Id: 资源实例ID
        :type Id: str
        """
        self._Period = None
        self._StartTime = None
        self._EndTime = None
        self._MetricName = None
        self._Business = None
        self._IpList = None
        self._Id = None

    @property
    def Period(self):
        """统计粒度，取值[300(5分钟)，3600(小时)，86400(天)]
        :rtype: int
        """
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def StartTime(self):
        """统计开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """统计结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def MetricName(self):
        """指标，取值[bps(攻击流量带宽，pps(攻击包速率))]
        :rtype: str
        """
        return self._MetricName

    @MetricName.setter
    def MetricName(self, MetricName):
        self._MetricName = MetricName

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp-multip表示高防包；basic表示DDoS基础防护）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def IpList(self):
        """资源实例的IP列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Id(self):
        """资源实例ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id


    def _deserialize(self, params):
        self._Period = params.get("Period")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._MetricName = params.get("MetricName")
        self._Business = params.get("Business")
        self._IpList = params.get("IpList")
        self._Id = params.get("Id")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewDDoSTrendResponse(AbstractModel):
    """DescribeOverviewDDoSTrend返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Count: 值个数
        :type Count: int
        :param _Data: 值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :type Data: list of int non-negative
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Count = None
        self._Data = None
        self._RequestId = None

    @property
    def Count(self):
        """值个数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Data(self):
        """值数组，攻击流量带宽单位为Mbps，包速率单位为pps
        :rtype: list of int non-negative
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Data = params.get("Data")
        self._RequestId = params.get("RequestId")


class DescribeOverviewIndexRequest(AbstractModel):
    """DescribeOverviewIndex请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 拉取指标起始时间
        :type StartTime: str
        :param _EndTime: 拉取指标结束时间
        :type EndTime: str
        """
        self._StartTime = None
        self._EndTime = None

    @property
    def StartTime(self):
        """拉取指标起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """拉取指标结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOverviewIndexResponse(AbstractModel):
    """DescribeOverviewIndex返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllIpCount: IP总数
        :type AllIpCount: int
        :param _AntiddosIpCount: 高防IP总数（包含高防包+高防IP）
        :type AntiddosIpCount: int
        :param _AttackIpCount: 攻击IP总数
        :type AttackIpCount: int
        :param _BlockIpCount: 封堵IP总数
        :type BlockIpCount: int
        :param _AntiddosDomainCount: 高防域名总数
        :type AntiddosDomainCount: int
        :param _AttackDomainCount: 攻击域名总数
        :type AttackDomainCount: int
        :param _MaxAttackFlow: 攻击流量峰值
        :type MaxAttackFlow: int
        :param _NewAttackTime: 当前最近一条攻击中的起始时间
        :type NewAttackTime: str
        :param _NewAttackIp: 当前最近一条攻击中的IP
        :type NewAttackIp: str
        :param _NewAttackType: 当前最近一条攻击中的攻击类型
        :type NewAttackType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllIpCount = None
        self._AntiddosIpCount = None
        self._AttackIpCount = None
        self._BlockIpCount = None
        self._AntiddosDomainCount = None
        self._AttackDomainCount = None
        self._MaxAttackFlow = None
        self._NewAttackTime = None
        self._NewAttackIp = None
        self._NewAttackType = None
        self._RequestId = None

    @property
    def AllIpCount(self):
        """IP总数
        :rtype: int
        """
        return self._AllIpCount

    @AllIpCount.setter
    def AllIpCount(self, AllIpCount):
        self._AllIpCount = AllIpCount

    @property
    def AntiddosIpCount(self):
        """高防IP总数（包含高防包+高防IP）
        :rtype: int
        """
        return self._AntiddosIpCount

    @AntiddosIpCount.setter
    def AntiddosIpCount(self, AntiddosIpCount):
        self._AntiddosIpCount = AntiddosIpCount

    @property
    def AttackIpCount(self):
        """攻击IP总数
        :rtype: int
        """
        return self._AttackIpCount

    @AttackIpCount.setter
    def AttackIpCount(self, AttackIpCount):
        self._AttackIpCount = AttackIpCount

    @property
    def BlockIpCount(self):
        """封堵IP总数
        :rtype: int
        """
        return self._BlockIpCount

    @BlockIpCount.setter
    def BlockIpCount(self, BlockIpCount):
        self._BlockIpCount = BlockIpCount

    @property
    def AntiddosDomainCount(self):
        """高防域名总数
        :rtype: int
        """
        return self._AntiddosDomainCount

    @AntiddosDomainCount.setter
    def AntiddosDomainCount(self, AntiddosDomainCount):
        self._AntiddosDomainCount = AntiddosDomainCount

    @property
    def AttackDomainCount(self):
        """攻击域名总数
        :rtype: int
        """
        return self._AttackDomainCount

    @AttackDomainCount.setter
    def AttackDomainCount(self, AttackDomainCount):
        self._AttackDomainCount = AttackDomainCount

    @property
    def MaxAttackFlow(self):
        """攻击流量峰值
        :rtype: int
        """
        return self._MaxAttackFlow

    @MaxAttackFlow.setter
    def MaxAttackFlow(self, MaxAttackFlow):
        self._MaxAttackFlow = MaxAttackFlow

    @property
    def NewAttackTime(self):
        """当前最近一条攻击中的起始时间
        :rtype: str
        """
        return self._NewAttackTime

    @NewAttackTime.setter
    def NewAttackTime(self, NewAttackTime):
        self._NewAttackTime = NewAttackTime

    @property
    def NewAttackIp(self):
        """当前最近一条攻击中的IP
        :rtype: str
        """
        return self._NewAttackIp

    @NewAttackIp.setter
    def NewAttackIp(self, NewAttackIp):
        self._NewAttackIp = NewAttackIp

    @property
    def NewAttackType(self):
        """当前最近一条攻击中的攻击类型
        :rtype: str
        """
        return self._NewAttackType

    @NewAttackType.setter
    def NewAttackType(self, NewAttackType):
        self._NewAttackType = NewAttackType

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllIpCount = params.get("AllIpCount")
        self._AntiddosIpCount = params.get("AntiddosIpCount")
        self._AttackIpCount = params.get("AttackIpCount")
        self._BlockIpCount = params.get("BlockIpCount")
        self._AntiddosDomainCount = params.get("AntiddosDomainCount")
        self._AttackDomainCount = params.get("AttackDomainCount")
        self._MaxAttackFlow = params.get("MaxAttackFlow")
        self._NewAttackTime = params.get("NewAttackTime")
        self._NewAttackIp = params.get("NewAttackIp")
        self._NewAttackType = params.get("NewAttackType")
        self._RequestId = params.get("RequestId")


class DescribePendingRiskInfoRequest(AbstractModel):
    """DescribePendingRiskInfo请求参数结构体

    """


class DescribePendingRiskInfoResponse(AbstractModel):
    """DescribePendingRiskInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsPaidUsr: 是否为付费用户，true：付费用户， false：普通用户
        :type IsPaidUsr: bool
        :param _AttackingCount: 攻击中的资源数量
        :type AttackingCount: int
        :param _BlockingCount: 封堵中的资源数量
        :type BlockingCount: int
        :param _ExpiredCount: 已过期的资源数量
        :type ExpiredCount: int
        :param _Total: 所有待处理风险事件总数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsPaidUsr = None
        self._AttackingCount = None
        self._BlockingCount = None
        self._ExpiredCount = None
        self._Total = None
        self._RequestId = None

    @property
    def IsPaidUsr(self):
        """是否为付费用户，true：付费用户， false：普通用户
        :rtype: bool
        """
        return self._IsPaidUsr

    @IsPaidUsr.setter
    def IsPaidUsr(self, IsPaidUsr):
        self._IsPaidUsr = IsPaidUsr

    @property
    def AttackingCount(self):
        """攻击中的资源数量
        :rtype: int
        """
        return self._AttackingCount

    @AttackingCount.setter
    def AttackingCount(self, AttackingCount):
        self._AttackingCount = AttackingCount

    @property
    def BlockingCount(self):
        """封堵中的资源数量
        :rtype: int
        """
        return self._BlockingCount

    @BlockingCount.setter
    def BlockingCount(self, BlockingCount):
        self._BlockingCount = BlockingCount

    @property
    def ExpiredCount(self):
        """已过期的资源数量
        :rtype: int
        """
        return self._ExpiredCount

    @ExpiredCount.setter
    def ExpiredCount(self, ExpiredCount):
        self._ExpiredCount = ExpiredCount

    @property
    def Total(self):
        """所有待处理风险事件总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsPaidUsr = params.get("IsPaidUsr")
        self._AttackingCount = params.get("AttackingCount")
        self._BlockingCount = params.get("BlockingCount")
        self._ExpiredCount = params.get("ExpiredCount")
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DisassociateDDoSEipAddressRequest(AbstractModel):
    """DisassociateDDoSEipAddress请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :type InstanceId: str
        :param _Eip: 资源实例ID对应的高防弹性公网IP。
        :type Eip: str
        """
        self._InstanceId = None
        self._Eip = None

    @property
    def InstanceId(self):
        """资源实例ID，实例ID形如：bgpip-0000011x。只能填写高防IP实例。
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Eip(self):
        """资源实例ID对应的高防弹性公网IP。
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Eip = params.get("Eip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisassociateDDoSEipAddressResponse(AbstractModel):
    """DisassociateDDoSEipAddress返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EipAddressPackRelation(AbstractModel):
    """Anycast高防套餐详情

    """

    def __init__(self):
        r"""
        :param _IpCount: 套餐IP数量
        :type IpCount: int
        :param _AutoRenewFlag: 自动续费标记
        :type AutoRenewFlag: int
        :param _CurDeadline: 当前到期时间
        :type CurDeadline: str
        """
        self._IpCount = None
        self._AutoRenewFlag = None
        self._CurDeadline = None

    @property
    def IpCount(self):
        """套餐IP数量
        :rtype: int
        """
        return self._IpCount

    @IpCount.setter
    def IpCount(self, IpCount):
        self._IpCount = IpCount

    @property
    def AutoRenewFlag(self):
        """自动续费标记
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        """当前到期时间
        :rtype: str
        """
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline


    def _deserialize(self, params):
        self._IpCount = params.get("IpCount")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipAddressRelation(AbstractModel):
    """高防弹性公网IP关联信息

    """

    def __init__(self):
        r"""
        :param _EipAddressRegion: 高防弹性公网IP绑定的实例地区，例如hk代表中国香港
        :type EipAddressRegion: str
        :param _EipBoundRscIns: 绑定的资源实例ID。可能是一个CVM。
        :type EipBoundRscIns: str
        :param _EipBoundRscEni: 绑定的弹性网卡ID
        :type EipBoundRscEni: str
        :param _EipBoundRscVip: 绑定的资源内网ip
        :type EipBoundRscVip: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._EipAddressRegion = None
        self._EipBoundRscIns = None
        self._EipBoundRscEni = None
        self._EipBoundRscVip = None
        self._ModifyTime = None

    @property
    def EipAddressRegion(self):
        """高防弹性公网IP绑定的实例地区，例如hk代表中国香港
        :rtype: str
        """
        return self._EipAddressRegion

    @EipAddressRegion.setter
    def EipAddressRegion(self, EipAddressRegion):
        self._EipAddressRegion = EipAddressRegion

    @property
    def EipBoundRscIns(self):
        """绑定的资源实例ID。可能是一个CVM。
        :rtype: str
        """
        return self._EipBoundRscIns

    @EipBoundRscIns.setter
    def EipBoundRscIns(self, EipBoundRscIns):
        self._EipBoundRscIns = EipBoundRscIns

    @property
    def EipBoundRscEni(self):
        """绑定的弹性网卡ID
        :rtype: str
        """
        return self._EipBoundRscEni

    @EipBoundRscEni.setter
    def EipBoundRscEni(self, EipBoundRscEni):
        self._EipBoundRscEni = EipBoundRscEni

    @property
    def EipBoundRscVip(self):
        """绑定的资源内网ip
        :rtype: str
        """
        return self._EipBoundRscVip

    @EipBoundRscVip.setter
    def EipBoundRscVip(self, EipBoundRscVip):
        self._EipBoundRscVip = EipBoundRscVip

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        self._EipAddressRegion = params.get("EipAddressRegion")
        self._EipBoundRscIns = params.get("EipBoundRscIns")
        self._EipBoundRscEni = params.get("EipBoundRscEni")
        self._EipBoundRscVip = params.get("EipBoundRscVip")
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EipProductInfo(AbstractModel):
    """EIP所属的云产品信息

    """

    def __init__(self):
        r"""
        :param _Ip: IP地址
        :type Ip: str
        :param _BizType: 云产品类型，取值[
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
        :param _DeviceType: 云产品子类型，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :type DeviceType: str
        :param _InstanceId: IP所属的云产品实例ID，例如是弹性网卡的IP，InstanceId为弹性网卡的ID(eni-*); 如果是托管IP没有对应的资源实例ID,InstanceId为""
        :type InstanceId: str
        :param _Domain: 域名化资产对应的域名
        :type Domain: str
        """
        self._Ip = None
        self._BizType = None
        self._DeviceType = None
        self._InstanceId = None
        self._Domain = None

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BizType(self):
        """云产品类型，取值[
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
        :rtype: str
        """
        return self._BizType

    @BizType.setter
    def BizType(self, BizType):
        self._BizType = BizType

    @property
    def DeviceType(self):
        """云产品子类型，取值[cvm（CVM），lb（负载均衡器），eni（弹性网卡），vpngw（VPN），natgw（NAT），waf（WAF），fpc（金融），gaap（GAAP），other（托管IP），eip（黑石弹性IP）]
        :rtype: str
        """
        return self._DeviceType

    @DeviceType.setter
    def DeviceType(self, DeviceType):
        self._DeviceType = DeviceType

    @property
    def InstanceId(self):
        """IP所属的云产品实例ID，例如是弹性网卡的IP，InstanceId为弹性网卡的ID(eni-*); 如果是托管IP没有对应的资源实例ID,InstanceId为""
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Domain(self):
        """域名化资产对应的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._BizType = params.get("BizType")
        self._DeviceType = params.get("DeviceType")
        self._InstanceId = params.get("InstanceId")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForwardListener(AbstractModel):
    """转发监听器

    """

    def __init__(self):
        r"""
        :param _FrontendPort: 转发监听端口下限，取值1~65535
        :type FrontendPort: int
        :param _ForwardProtocol: 转发协议，取值[
TCP
UDP
]
        :type ForwardProtocol: str
        :param _FrontendPortEnd: 转发监听端口上限，取值1~65535
        :type FrontendPortEnd: int
        """
        self._FrontendPort = None
        self._ForwardProtocol = None
        self._FrontendPortEnd = None

    @property
    def FrontendPort(self):
        """转发监听端口下限，取值1~65535
        :rtype: int
        """
        return self._FrontendPort

    @FrontendPort.setter
    def FrontendPort(self, FrontendPort):
        self._FrontendPort = FrontendPort

    @property
    def ForwardProtocol(self):
        """转发协议，取值[
TCP
UDP
]
        :rtype: str
        """
        return self._ForwardProtocol

    @ForwardProtocol.setter
    def ForwardProtocol(self, ForwardProtocol):
        self._ForwardProtocol = ForwardProtocol

    @property
    def FrontendPortEnd(self):
        """转发监听端口上限，取值1~65535
        :rtype: int
        """
        return self._FrontendPortEnd

    @FrontendPortEnd.setter
    def FrontendPortEnd(self, FrontendPortEnd):
        self._FrontendPortEnd = FrontendPortEnd


    def _deserialize(self, params):
        self._FrontendPort = params.get("FrontendPort")
        self._ForwardProtocol = params.get("ForwardProtocol")
        self._FrontendPortEnd = params.get("FrontendPortEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpStatusMap(AbstractModel):
    """业务流量的http状态码聚合数据

    """

    def __init__(self):
        r"""
        :param _SourceHttp2xx: http2xx回源状态码
        :type SourceHttp2xx: list of float
        :param _Http5xx: http5xx状态码
        :type Http5xx: list of float
        :param _SourceHttp5xx: http5xx回源状态码
        :type SourceHttp5xx: list of float
        :param _SourceHttp404: http404回源状态码
        :type SourceHttp404: list of float
        :param _Http4xx: http4xx状态码
        :type Http4xx: list of float
        :param _SourceHttp4xx: http4xx回源状态码
        :type SourceHttp4xx: list of float
        :param _Http2xx: http2xx状态码
        :type Http2xx: list of float
        :param _Http404: http404状态码
        :type Http404: list of float
        :param _SourceHttp3xx: http3xx回源状态码
        :type SourceHttp3xx: list of float
        :param _Http3xx: http3xx状态码
        :type Http3xx: list of float
        """
        self._SourceHttp2xx = None
        self._Http5xx = None
        self._SourceHttp5xx = None
        self._SourceHttp404 = None
        self._Http4xx = None
        self._SourceHttp4xx = None
        self._Http2xx = None
        self._Http404 = None
        self._SourceHttp3xx = None
        self._Http3xx = None

    @property
    def SourceHttp2xx(self):
        """http2xx回源状态码
        :rtype: list of float
        """
        return self._SourceHttp2xx

    @SourceHttp2xx.setter
    def SourceHttp2xx(self, SourceHttp2xx):
        self._SourceHttp2xx = SourceHttp2xx

    @property
    def Http5xx(self):
        """http5xx状态码
        :rtype: list of float
        """
        return self._Http5xx

    @Http5xx.setter
    def Http5xx(self, Http5xx):
        self._Http5xx = Http5xx

    @property
    def SourceHttp5xx(self):
        """http5xx回源状态码
        :rtype: list of float
        """
        return self._SourceHttp5xx

    @SourceHttp5xx.setter
    def SourceHttp5xx(self, SourceHttp5xx):
        self._SourceHttp5xx = SourceHttp5xx

    @property
    def SourceHttp404(self):
        """http404回源状态码
        :rtype: list of float
        """
        return self._SourceHttp404

    @SourceHttp404.setter
    def SourceHttp404(self, SourceHttp404):
        self._SourceHttp404 = SourceHttp404

    @property
    def Http4xx(self):
        """http4xx状态码
        :rtype: list of float
        """
        return self._Http4xx

    @Http4xx.setter
    def Http4xx(self, Http4xx):
        self._Http4xx = Http4xx

    @property
    def SourceHttp4xx(self):
        """http4xx回源状态码
        :rtype: list of float
        """
        return self._SourceHttp4xx

    @SourceHttp4xx.setter
    def SourceHttp4xx(self, SourceHttp4xx):
        self._SourceHttp4xx = SourceHttp4xx

    @property
    def Http2xx(self):
        """http2xx状态码
        :rtype: list of float
        """
        return self._Http2xx

    @Http2xx.setter
    def Http2xx(self, Http2xx):
        self._Http2xx = Http2xx

    @property
    def Http404(self):
        """http404状态码
        :rtype: list of float
        """
        return self._Http404

    @Http404.setter
    def Http404(self, Http404):
        self._Http404 = Http404

    @property
    def SourceHttp3xx(self):
        """http3xx回源状态码
        :rtype: list of float
        """
        return self._SourceHttp3xx

    @SourceHttp3xx.setter
    def SourceHttp3xx(self, SourceHttp3xx):
        self._SourceHttp3xx = SourceHttp3xx

    @property
    def Http3xx(self):
        """http3xx状态码
        :rtype: list of float
        """
        return self._Http3xx

    @Http3xx.setter
    def Http3xx(self, Http3xx):
        self._Http3xx = Http3xx


    def _deserialize(self, params):
        self._SourceHttp2xx = params.get("SourceHttp2xx")
        self._Http5xx = params.get("Http5xx")
        self._SourceHttp5xx = params.get("SourceHttp5xx")
        self._SourceHttp404 = params.get("SourceHttp404")
        self._Http4xx = params.get("Http4xx")
        self._SourceHttp4xx = params.get("SourceHttp4xx")
        self._Http2xx = params.get("Http2xx")
        self._Http404 = params.get("Http404")
        self._SourceHttp3xx = params.get("SourceHttp3xx")
        self._Http3xx = params.get("Http3xx")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPAlarmThresholdRelation(AbstractModel):
    """单IP告警阈值配置

    """

    def __init__(self):
        r"""
        :param _AlarmType: 告警阈值类型，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :type AlarmType: int
        :param _AlarmThreshold: 告警阈值，单位Mbps，取值>=0；当作为输入参数时，设置0会删除告警阈值配置；
        :type AlarmThreshold: int
        :param _InstanceDetailList: 告警阈值所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self._AlarmType = None
        self._AlarmThreshold = None
        self._InstanceDetailList = None

    @property
    def AlarmType(self):
        """告警阈值类型，取值[
1(入流量告警阈值)
2(攻击清洗流量告警阈值)
]
        :rtype: int
        """
        return self._AlarmType

    @AlarmType.setter
    def AlarmType(self, AlarmType):
        self._AlarmType = AlarmType

    @property
    def AlarmThreshold(self):
        """告警阈值，单位Mbps，取值>=0；当作为输入参数时，设置0会删除告警阈值配置；
        :rtype: int
        """
        return self._AlarmThreshold

    @AlarmThreshold.setter
    def AlarmThreshold(self, AlarmThreshold):
        self._AlarmThreshold = AlarmThreshold

    @property
    def InstanceDetailList(self):
        """告警阈值所属的资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        self._AlarmType = params.get("AlarmType")
        self._AlarmThreshold = params.get("AlarmThreshold")
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPLineInfo(AbstractModel):
    """IP线路信息

    """

    def __init__(self):
        r"""
        :param _Type: IP线路类型，取值[
"bgp"：BGP线路IP
"ctcc"：电信线路IP
"cucc"：联通线路IP
"cmcc"：移动线路IP
"abroad"：境外线路IP
]
        :type Type: str
        :param _Eip: 线路IP
        :type Eip: str
        :param _Cname: 实例对应的cname
        :type Cname: str
        :param _ResourceFlag: 资源flag，0：高防包资源，1：高防IP资源，2：非高防资源IP
        :type ResourceFlag: int
        :param _Domain: 域名化资产对应的域名
        :type Domain: str
        """
        self._Type = None
        self._Eip = None
        self._Cname = None
        self._ResourceFlag = None
        self._Domain = None

    @property
    def Type(self):
        """IP线路类型，取值[
"bgp"：BGP线路IP
"ctcc"：电信线路IP
"cucc"：联通线路IP
"cmcc"：移动线路IP
"abroad"：境外线路IP
]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Eip(self):
        """线路IP
        :rtype: str
        """
        return self._Eip

    @Eip.setter
    def Eip(self, Eip):
        self._Eip = Eip

    @property
    def Cname(self):
        """实例对应的cname
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def ResourceFlag(self):
        """资源flag，0：高防包资源，1：高防IP资源，2：非高防资源IP
        :rtype: int
        """
        return self._ResourceFlag

    @ResourceFlag.setter
    def ResourceFlag(self, ResourceFlag):
        self._ResourceFlag = ResourceFlag

    @property
    def Domain(self):
        """域名化资产对应的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Eip = params.get("Eip")
        self._Cname = params.get("Cname")
        self._ResourceFlag = params.get("ResourceFlag")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InsL7Rules(AbstractModel):
    """实例7层规则

    """

    def __init__(self):
        r"""
        :param _Status: 规则在中间状态不可修改，只可在（0， 2， 8）状态可编辑。
规则状态，0: 正常运行中, 1: 配置规则中(配置生效中), 2: 配置规则失败（配置生效失败）, 3: 删除规则中(删除生效中), 5: 删除规则失败(删除失败), 6: 等待添加规则, 7: 等待删除规则, 8: 等待上传证书, 9: 规则对应的资源不存在，被隔离, 10:等待修改规则, 11:配置修改中
        :type Status: int
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _InsId: 实例ID
        :type InsId: str
        :param _AppId: 用户AppID
        :type AppId: str
        :param _VirtualPort: 高防端口
        :type VirtualPort: str
        :param _SSLId: 证书ID
        :type SSLId: str
        """
        self._Status = None
        self._Domain = None
        self._Protocol = None
        self._InsId = None
        self._AppId = None
        self._VirtualPort = None
        self._SSLId = None

    @property
    def Status(self):
        """规则在中间状态不可修改，只可在（0， 2， 8）状态可编辑。
规则状态，0: 正常运行中, 1: 配置规则中(配置生效中), 2: 配置规则失败（配置生效失败）, 3: 删除规则中(删除生效中), 5: 删除规则失败(删除失败), 6: 等待添加规则, 7: 等待删除规则, 8: 等待上传证书, 9: 规则对应的资源不存在，被隔离, 10:等待修改规则, 11:配置修改中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def InsId(self):
        """实例ID
        :rtype: str
        """
        return self._InsId

    @InsId.setter
    def InsId(self, InsId):
        self._InsId = InsId

    @property
    def AppId(self):
        """用户AppID
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def VirtualPort(self):
        """高防端口
        :rtype: str
        """
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SSLId(self):
        """证书ID
        :rtype: str
        """
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._InsId = params.get("InsId")
        self._AppId = params.get("AppId")
        self._VirtualPort = params.get("VirtualPort")
        self._SSLId = params.get("SSLId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InstanceRelation(AbstractModel):
    """资源实例IP信息

    """

    def __init__(self):
        r"""
        :param _EipList: 资源实例的IP
        :type EipList: list of str
        :param _InstanceId: 资源实例的ID
        :type InstanceId: str
        """
        self._EipList = None
        self._InstanceId = None

    @property
    def EipList(self):
        """资源实例的IP
        :rtype: list of str
        """
        return self._EipList

    @EipList.setter
    def EipList(self, EipList):
        self._EipList = EipList

    @property
    def InstanceId(self):
        """资源实例的ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId


    def _deserialize(self, params):
        self._EipList = params.get("EipList")
        self._InstanceId = params.get("InstanceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpBlockData(AbstractModel):
    """IP封堵记录

    """

    def __init__(self):
        r"""
        :param _Status: 状态（Blocked：被封堵；UnBlocking：解封中；UnBlockFailed：解封失败）
        :type Status: str
        :param _Ip: 资源IP
        :type Ip: str
        :param _BlockTime: 封堵时间
        :type BlockTime: str
        :param _UnBlockTime: 解封时间（预计解封时间）
        :type UnBlockTime: str
        :param _ActionType: 解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）
        :type ActionType: str
        :param _ProtectFlag: 高防标记，0：非高防，1：高防
        :type ProtectFlag: int
        """
        self._Status = None
        self._Ip = None
        self._BlockTime = None
        self._UnBlockTime = None
        self._ActionType = None
        self._ProtectFlag = None

    @property
    def Status(self):
        """状态（Blocked：被封堵；UnBlocking：解封中；UnBlockFailed：解封失败）
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ip(self):
        """资源IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def BlockTime(self):
        """封堵时间
        :rtype: str
        """
        return self._BlockTime

    @BlockTime.setter
    def BlockTime(self, BlockTime):
        self._BlockTime = BlockTime

    @property
    def UnBlockTime(self):
        """解封时间（预计解封时间）
        :rtype: str
        """
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def ActionType(self):
        """解封类型（user：自助解封；auto：自动解封； update：升级解封；bind：绑定高防包解封）
        :rtype: str
        """
        return self._ActionType

    @ActionType.setter
    def ActionType(self, ActionType):
        self._ActionType = ActionType

    @property
    def ProtectFlag(self):
        """高防标记，0：非高防，1：高防
        :rtype: int
        """
        return self._ProtectFlag

    @ProtectFlag.setter
    def ProtectFlag(self, ProtectFlag):
        self._ProtectFlag = ProtectFlag


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Ip = params.get("Ip")
        self._BlockTime = params.get("BlockTime")
        self._UnBlockTime = params.get("UnBlockTime")
        self._ActionType = params.get("ActionType")
        self._ProtectFlag = params.get("ProtectFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpSegment(AbstractModel):
    """ip段数据结构

    """

    def __init__(self):
        r"""
        :param _Ip: ip地址
        :type Ip: str
        :param _Mask: ip掩码，如果为32位ip，填0
        :type Mask: int
        """
        self._Ip = None
        self._Mask = None

    @property
    def Ip(self):
        """ip地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Mask(self):
        """ip掩码，如果为32位ip，填0
        :rtype: int
        """
        return self._Mask

    @Mask.setter
    def Mask(self, Mask):
        self._Mask = Mask


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Mask = params.get("Mask")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyValue(AbstractModel):
    """字段值，K-V形式

    """

    def __init__(self):
        r"""
        :param _Key: 字段名称
        :type Key: str
        :param _Value: 字段取值
        :type Value: str
        """
        self._Key = None
        self._Value = None

    @property
    def Key(self):
        """字段名称
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Value(self):
        """字段取值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L4RuleSource(AbstractModel):
    """L4规则回源列表

    """

    def __init__(self):
        r"""
        :param _Source: 回源IP或域名
        :type Source: str
        :param _Weight: 权重值，取值[0,100]，暂不支持
        :type Weight: int
        :param _Port: 8000
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Backup: 备份源站，1: 备份源站，0: 普通源站
        :type Backup: int
        """
        self._Source = None
        self._Weight = None
        self._Port = None
        self._Backup = None

    @property
    def Source(self):
        """回源IP或域名
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Weight(self):
        """权重值，取值[0,100]，暂不支持
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Port(self):
        """8000
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Backup(self):
        """备份源站，1: 备份源站，0: 普通源站
        :rtype: int
        """
        return self._Backup

    @Backup.setter
    def Backup(self, Backup):
        self._Backup = Backup


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        self._Backup = params.get("Backup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _Domain: 转发域名
        :type Domain: str
        :param _Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param _Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param _RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param _CCThreshold: HTTPS协议的CC防护阈值
        :type CCThreshold: int
        :param _PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param _CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param _HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :type HttpsToHttpEnable: int
        :param _CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param _Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param _CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param _VirtualPort: 接入端口值
        :type VirtualPort: int
        :param _SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param _Id: 同ruleId
        :type Id: str
        :param _CCAIEnable: 智能cc开关，取值[0(关闭), 1(开启)]
        :type CCAIEnable: int
        """
        self._KeepTime = None
        self._Domain = None
        self._Protocol = None
        self._SourceType = None
        self._LbType = None
        self._SourceList = None
        self._KeepEnable = None
        self._Status = None
        self._RuleId = None
        self._CCThreshold = None
        self._PrivateKey = None
        self._CCEnable = None
        self._HttpsToHttpEnable = None
        self._CertType = None
        self._Cert = None
        self._CCLevel = None
        self._RuleName = None
        self._CCStatus = None
        self._VirtualPort = None
        self._SSLId = None
        self._Id = None
        self._CCAIEnable = None

    @property
    def KeepTime(self):
        """会话保持时间，单位秒
        :rtype: int
        """
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def Domain(self):
        """转发域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """转发协议，取值[http, https]
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SourceType(self):
        """回源方式，取值[1(域名回源)，2(IP回源)]
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def LbType(self):
        """负载均衡方式，取值[1(加权轮询)]
        :rtype: int
        """
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def SourceList(self):
        """回源列表
        :rtype: list of L4RuleSource
        """
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def KeepEnable(self):
        """会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :rtype: int
        """
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def Status(self):
        """规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleId(self):
        """规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def CCThreshold(self):
        """HTTPS协议的CC防护阈值
        :rtype: int
        """
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def PrivateKey(self):
        """当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def CCEnable(self):
        """HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def HttpsToHttpEnable(self):
        """是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :rtype: int
        """
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def CertType(self):
        """证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :rtype: int
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Cert(self):
        """当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def CCLevel(self):
        """HTTPS协议的CC防护等级
        :rtype: str
        """
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def RuleName(self):
        """规则描述
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CCStatus(self):
        """cc防护状态，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def VirtualPort(self):
        """接入端口值
        :rtype: int
        """
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def SSLId(self):
        """当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :rtype: str
        """
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Id(self):
        """同ruleId
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CCAIEnable(self):
        """智能cc开关，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCAIEnable

    @CCAIEnable.setter
    def CCAIEnable(self, CCAIEnable):
        self._CCAIEnable = CCAIEnable


    def _deserialize(self, params):
        self._KeepTime = params.get("KeepTime")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._SourceType = params.get("SourceType")
        self._LbType = params.get("LbType")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._KeepEnable = params.get("KeepEnable")
        self._Status = params.get("Status")
        self._RuleId = params.get("RuleId")
        self._CCThreshold = params.get("CCThreshold")
        self._PrivateKey = params.get("PrivateKey")
        self._CCEnable = params.get("CCEnable")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._CertType = params.get("CertType")
        self._Cert = params.get("Cert")
        self._CCLevel = params.get("CCLevel")
        self._RuleName = params.get("RuleName")
        self._CCStatus = params.get("CCStatus")
        self._VirtualPort = params.get("VirtualPort")
        self._SSLId = params.get("SSLId")
        self._Id = params.get("Id")
        self._CCAIEnable = params.get("CCAIEnable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class L7RuleHealth(AbstractModel):
    """L7规则健康检查参数

    """

    def __init__(self):
        r"""
        :param _Status: 配置状态，0： 正常，1：配置中，2：配置失败
        :type Status: int
        :param _Enable: =1表示开启；=0表示关闭
        :type Enable: int
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Url: 检查目录的URL，默认为/
        :type Url: str
        :param _Interval: 检测间隔时间，单位秒
        :type Interval: int
        :param _AliveNum: 健康阈值，单位次
        :type AliveNum: int
        :param _KickNum: 不健康阈值，单位次
        :type KickNum: int
        :param _Method: HTTP请求方式，取值[HEAD,GET]
        :type Method: str
        :param _StatusCode: 健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :type StatusCode: int
        :param _ProtocolFlag: 是否同时下发http和https规则健康检查配置
        :type ProtocolFlag: int
        :param _PassiveEnable: 被动探测开关，=1表示开启；=0表示关闭
        :type PassiveEnable: int
        :param _BlockInter: 被动探测不健康屏蔽时间
        :type BlockInter: int
        :param _FailedCountInter: 被动探测不健康统计间隔
        :type FailedCountInter: int
        :param _FailedThreshold: 被动探测不健康阈值
        :type FailedThreshold: int
        :param _PassiveStatusCode: 被动探测判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :type PassiveStatusCode: int
        :param _PassiveStatus: 被动探测配置状态，0： 正常，1：配置中，2：配置失败
        :type PassiveStatus: int
        """
        self._Status = None
        self._Enable = None
        self._RuleId = None
        self._Url = None
        self._Interval = None
        self._AliveNum = None
        self._KickNum = None
        self._Method = None
        self._StatusCode = None
        self._ProtocolFlag = None
        self._PassiveEnable = None
        self._BlockInter = None
        self._FailedCountInter = None
        self._FailedThreshold = None
        self._PassiveStatusCode = None
        self._PassiveStatus = None

    @property
    def Status(self):
        """配置状态，0： 正常，1：配置中，2：配置失败
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Enable(self):
        """=1表示开启；=0表示关闭
        :rtype: int
        """
        return self._Enable

    @Enable.setter
    def Enable(self, Enable):
        self._Enable = Enable

    @property
    def RuleId(self):
        """规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Url(self):
        """检查目录的URL，默认为/
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Interval(self):
        """检测间隔时间，单位秒
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def AliveNum(self):
        """健康阈值，单位次
        :rtype: int
        """
        return self._AliveNum

    @AliveNum.setter
    def AliveNum(self, AliveNum):
        self._AliveNum = AliveNum

    @property
    def KickNum(self):
        """不健康阈值，单位次
        :rtype: int
        """
        return self._KickNum

    @KickNum.setter
    def KickNum(self, KickNum):
        self._KickNum = KickNum

    @property
    def Method(self):
        """HTTP请求方式，取值[HEAD,GET]
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def StatusCode(self):
        """健康检查判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :rtype: int
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def ProtocolFlag(self):
        """是否同时下发http和https规则健康检查配置
        :rtype: int
        """
        return self._ProtocolFlag

    @ProtocolFlag.setter
    def ProtocolFlag(self, ProtocolFlag):
        self._ProtocolFlag = ProtocolFlag

    @property
    def PassiveEnable(self):
        """被动探测开关，=1表示开启；=0表示关闭
        :rtype: int
        """
        return self._PassiveEnable

    @PassiveEnable.setter
    def PassiveEnable(self, PassiveEnable):
        self._PassiveEnable = PassiveEnable

    @property
    def BlockInter(self):
        """被动探测不健康屏蔽时间
        :rtype: int
        """
        return self._BlockInter

    @BlockInter.setter
    def BlockInter(self, BlockInter):
        self._BlockInter = BlockInter

    @property
    def FailedCountInter(self):
        """被动探测不健康统计间隔
        :rtype: int
        """
        return self._FailedCountInter

    @FailedCountInter.setter
    def FailedCountInter(self, FailedCountInter):
        self._FailedCountInter = FailedCountInter

    @property
    def FailedThreshold(self):
        """被动探测不健康阈值
        :rtype: int
        """
        return self._FailedThreshold

    @FailedThreshold.setter
    def FailedThreshold(self, FailedThreshold):
        self._FailedThreshold = FailedThreshold

    @property
    def PassiveStatusCode(self):
        """被动探测判定正常状态码，1xx =1, 2xx=2, 3xx=4, 4xx=8,5xx=16，多个状态码值加和
        :rtype: int
        """
        return self._PassiveStatusCode

    @PassiveStatusCode.setter
    def PassiveStatusCode(self, PassiveStatusCode):
        self._PassiveStatusCode = PassiveStatusCode

    @property
    def PassiveStatus(self):
        """被动探测配置状态，0： 正常，1：配置中，2：配置失败
        :rtype: int
        """
        return self._PassiveStatus

    @PassiveStatus.setter
    def PassiveStatus(self, PassiveStatus):
        self._PassiveStatus = PassiveStatus


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Enable = params.get("Enable")
        self._RuleId = params.get("RuleId")
        self._Url = params.get("Url")
        self._Interval = params.get("Interval")
        self._AliveNum = params.get("AliveNum")
        self._KickNum = params.get("KickNum")
        self._Method = params.get("Method")
        self._StatusCode = params.get("StatusCode")
        self._ProtocolFlag = params.get("ProtocolFlag")
        self._PassiveEnable = params.get("PassiveEnable")
        self._BlockInter = params.get("BlockInter")
        self._FailedCountInter = params.get("FailedCountInter")
        self._FailedThreshold = params.get("FailedThreshold")
        self._PassiveStatusCode = params.get("PassiveStatusCode")
        self._PassiveStatus = params.get("PassiveStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Layer4Rule(AbstractModel):
    """4层转发规则

    """

    def __init__(self):
        r"""
        :param _BackendPort: 源站端口，取值1~65535
        :type BackendPort: int
        :param _FrontendPort: 转发端口，取值1~65535
        :type FrontendPort: int
        :param _Protocol: 转发协议，取值[
TCP(TCP协议)
UDP(UDP协议)
]
        :type Protocol: str
        :param _RealServers: 源站列表
        :type RealServers: list of SourceServer
        :param _InstanceDetails: 资源实例
        :type InstanceDetails: list of InstanceRelation
        :param _InstanceDetailRule: 规则所属的资源实例
        :type InstanceDetailRule: list of RuleInstanceRelation
        """
        self._BackendPort = None
        self._FrontendPort = None
        self._Protocol = None
        self._RealServers = None
        self._InstanceDetails = None
        self._InstanceDetailRule = None

    @property
    def BackendPort(self):
        """源站端口，取值1~65535
        :rtype: int
        """
        return self._BackendPort

    @BackendPort.setter
    def BackendPort(self, BackendPort):
        self._BackendPort = BackendPort

    @property
    def FrontendPort(self):
        """转发端口，取值1~65535
        :rtype: int
        """
        return self._FrontendPort

    @FrontendPort.setter
    def FrontendPort(self, FrontendPort):
        self._FrontendPort = FrontendPort

    @property
    def Protocol(self):
        """转发协议，取值[
TCP(TCP协议)
UDP(UDP协议)
]
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RealServers(self):
        """源站列表
        :rtype: list of SourceServer
        """
        return self._RealServers

    @RealServers.setter
    def RealServers(self, RealServers):
        self._RealServers = RealServers

    @property
    def InstanceDetails(self):
        """资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def InstanceDetailRule(self):
        """规则所属的资源实例
        :rtype: list of RuleInstanceRelation
        """
        return self._InstanceDetailRule

    @InstanceDetailRule.setter
    def InstanceDetailRule(self, InstanceDetailRule):
        self._InstanceDetailRule = InstanceDetailRule


    def _deserialize(self, params):
        self._BackendPort = params.get("BackendPort")
        self._FrontendPort = params.get("FrontendPort")
        self._Protocol = params.get("Protocol")
        if params.get("RealServers") is not None:
            self._RealServers = []
            for item in params.get("RealServers"):
                obj = SourceServer()
                obj._deserialize(item)
                self._RealServers.append(obj)
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        if params.get("InstanceDetailRule") is not None:
            self._InstanceDetailRule = []
            for item in params.get("InstanceDetailRule"):
                obj = RuleInstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailRule.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Layer7Rule(AbstractModel):
    """7层转发规则

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _ProxyTypeList: 转发类型列表
        :type ProxyTypeList: list of ProxyTypeInfo
        :param _RealServers: 源站列表
        :type RealServers: list of SourceServer
        :param _InstanceDetails: 资源实例
        :type InstanceDetails: list of InstanceRelation
        :param _InstanceDetailRule: 规则所属的资源实例
        :type InstanceDetailRule: list of RuleInstanceRelation
        :param _Protocol: 协议
        :type Protocol: str
        :param _Vport: 端口号
        :type Vport: int
        """
        self._Domain = None
        self._ProxyTypeList = None
        self._RealServers = None
        self._InstanceDetails = None
        self._InstanceDetailRule = None
        self._Protocol = None
        self._Vport = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProxyTypeList(self):
        """转发类型列表
        :rtype: list of ProxyTypeInfo
        """
        return self._ProxyTypeList

    @ProxyTypeList.setter
    def ProxyTypeList(self, ProxyTypeList):
        self._ProxyTypeList = ProxyTypeList

    @property
    def RealServers(self):
        """源站列表
        :rtype: list of SourceServer
        """
        return self._RealServers

    @RealServers.setter
    def RealServers(self, RealServers):
        self._RealServers = RealServers

    @property
    def InstanceDetails(self):
        """资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetails

    @InstanceDetails.setter
    def InstanceDetails(self, InstanceDetails):
        self._InstanceDetails = InstanceDetails

    @property
    def InstanceDetailRule(self):
        """规则所属的资源实例
        :rtype: list of RuleInstanceRelation
        """
        return self._InstanceDetailRule

    @InstanceDetailRule.setter
    def InstanceDetailRule(self, InstanceDetailRule):
        self._InstanceDetailRule = InstanceDetailRule

    @property
    def Protocol(self):
        """协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Vport(self):
        """端口号
        :rtype: int
        """
        return self._Vport

    @Vport.setter
    def Vport(self, Vport):
        self._Vport = Vport


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("ProxyTypeList") is not None:
            self._ProxyTypeList = []
            for item in params.get("ProxyTypeList"):
                obj = ProxyTypeInfo()
                obj._deserialize(item)
                self._ProxyTypeList.append(obj)
        if params.get("RealServers") is not None:
            self._RealServers = []
            for item in params.get("RealServers"):
                obj = SourceServer()
                obj._deserialize(item)
                self._RealServers.append(obj)
        if params.get("InstanceDetails") is not None:
            self._InstanceDetails = []
            for item in params.get("InstanceDetails"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetails.append(obj)
        if params.get("InstanceDetailRule") is not None:
            self._InstanceDetailRule = []
            for item in params.get("InstanceDetailRule"):
                obj = RuleInstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailRule.append(obj)
        self._Protocol = params.get("Protocol")
        self._Vport = params.get("Vport")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelPolicyRequest(AbstractModel):
    """ModifyCCLevelPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议，可取值http、https、http/https
        :type Protocol: str
        :param _Level: CC防护等级，可取值loose表示宽松，strict表示严格，normal表示适中， emergency表示攻击紧急， sup_loose表示超级宽松，default表示默认策略（无频控配置下发），customized表示自定义策略
        :type Level: str
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._Level = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，可取值http、https、http/https
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Level(self):
        """CC防护等级，可取值loose表示宽松，strict表示严格，normal表示适中， emergency表示攻击紧急， sup_loose表示超级宽松，default表示默认策略（无频控配置下发），customized表示自定义策略
        :rtype: str
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._Level = params.get("Level")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCLevelPolicyResponse(AbstractModel):
    """ModifyCCLevelPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCCPrecisionPolicyRequest(AbstractModel):
    """ModifyCCPrecisionPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _PolicyId: 策略Id
        :type PolicyId: str
        :param _PolicyAction: 策略方式。可取值：alg、drop、trans。alg指返回验证码方式验证，drop表示该访问丢弃，trans表示该访问放行。
        :type PolicyAction: str
        :param _PolicyList: 策略记录
        :type PolicyList: list of CCPrecisionPlyRecord
        """
        self._InstanceId = None
        self._PolicyId = None
        self._PolicyAction = None
        self._PolicyList = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def PolicyAction(self):
        """策略方式。可取值：alg、drop、trans。alg指返回验证码方式验证，drop表示该访问丢弃，trans表示该访问放行。
        :rtype: str
        """
        return self._PolicyAction

    @PolicyAction.setter
    def PolicyAction(self, PolicyAction):
        self._PolicyAction = PolicyAction

    @property
    def PolicyList(self):
        """策略记录
        :rtype: list of CCPrecisionPlyRecord
        """
        return self._PolicyList

    @PolicyList.setter
    def PolicyList(self, PolicyList):
        self._PolicyList = PolicyList


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        self._PolicyAction = params.get("PolicyAction")
        if params.get("PolicyList") is not None:
            self._PolicyList = []
            for item in params.get("PolicyList"):
                obj = CCPrecisionPlyRecord()
                obj._deserialize(item)
                self._PolicyList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCPrecisionPolicyResponse(AbstractModel):
    """ModifyCCPrecisionPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCCReqLimitPolicyRequest(AbstractModel):
    """ModifyCCReqLimitPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _PolicyId: 策略Id
        :type PolicyId: str
        :param _Policy: 策略项
        :type Policy: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        """
        self._InstanceId = None
        self._PolicyId = None
        self._Policy = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId

    @property
    def Policy(self):
        """策略项
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.CCReqLimitPolicyRecord`
        """
        return self._Policy

    @Policy.setter
    def Policy(self, Policy):
        self._Policy = Policy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._PolicyId = params.get("PolicyId")
        if params.get("Policy") is not None:
            self._Policy = CCReqLimitPolicyRecord()
            self._Policy._deserialize(params.get("Policy"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCReqLimitPolicyResponse(AbstractModel):
    """ModifyCCReqLimitPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCCThresholdPolicyRequest(AbstractModel):
    """ModifyCCThresholdPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例Id
        :type InstanceId: str
        :param _Ip: IP地址
        :type Ip: str
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议，可取值http，https，http/https
        :type Protocol: str
        :param _Threshold: 清洗阈值，-1表示开启“默认”模式
        :type Threshold: int
        """
        self._InstanceId = None
        self._Ip = None
        self._Domain = None
        self._Protocol = None
        self._Threshold = None

    @property
    def InstanceId(self):
        """实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议，可取值http，https，http/https
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Threshold(self):
        """清洗阈值，-1表示开启“默认”模式
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._Ip = params.get("Ip")
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._Threshold = params.get("Threshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCCThresholdPolicyResponse(AbstractModel):
    """ModifyCCThresholdPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyCcBlackWhiteIpListRequest(AbstractModel):
    """ModifyCcBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _IpList: IP列表
        :type IpList: list of IpSegment
        :param _Type: IP类型，取值[black(黑名单IP), white(白名单IP)]
        :type Type: str
        :param _PolicyId: 策略Id
        :type PolicyId: str
        """
        self._InstanceId = None
        self._IpList = None
        self._Type = None
        self._PolicyId = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def IpList(self):
        """IP列表
        :rtype: list of IpSegment
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def Type(self):
        """IP类型，取值[black(黑名单IP), white(白名单IP)]
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def PolicyId(self):
        """策略Id
        :rtype: str
        """
        return self._PolicyId

    @PolicyId.setter
    def PolicyId(self, PolicyId):
        self._PolicyId = PolicyId


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("IpList") is not None:
            self._IpList = []
            for item in params.get("IpList"):
                obj = IpSegment()
                obj._deserialize(item)
                self._IpList.append(obj)
        self._Type = params.get("Type")
        self._PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCcBlackWhiteIpListResponse(AbstractModel):
    """ModifyCcBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDDoSBlackWhiteIpListRequest(AbstractModel):
    """ModifyDDoSBlackWhiteIpList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源Id
        :type InstanceId: str
        :param _OldIpType: 当前配置的黑白名单类型，取值black时表示黑名单；取值white时表示白名单
        :type OldIpType: str
        :param _OldIp: 当前配置的Ip段，包含ip与掩码
        :type OldIp: :class:`tencentcloud.antiddos.v20200309.models.IpSegment`
        :param _NewIpType: 修改后黑白名单类型，取值black时黑名单，取值white时白名单
        :type NewIpType: str
        :param _NewIp: 当前配置的Ip段，包含ip与掩码
        :type NewIp: :class:`tencentcloud.antiddos.v20200309.models.IpSegment`
        """
        self._InstanceId = None
        self._OldIpType = None
        self._OldIp = None
        self._NewIpType = None
        self._NewIp = None

    @property
    def InstanceId(self):
        """资源Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldIpType(self):
        """当前配置的黑白名单类型，取值black时表示黑名单；取值white时表示白名单
        :rtype: str
        """
        return self._OldIpType

    @OldIpType.setter
    def OldIpType(self, OldIpType):
        self._OldIpType = OldIpType

    @property
    def OldIp(self):
        """当前配置的Ip段，包含ip与掩码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.IpSegment`
        """
        return self._OldIp

    @OldIp.setter
    def OldIp(self, OldIp):
        self._OldIp = OldIp

    @property
    def NewIpType(self):
        """修改后黑白名单类型，取值black时黑名单，取值white时白名单
        :rtype: str
        """
        return self._NewIpType

    @NewIpType.setter
    def NewIpType(self, NewIpType):
        self._NewIpType = NewIpType

    @property
    def NewIp(self):
        """当前配置的Ip段，包含ip与掩码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.IpSegment`
        """
        return self._NewIp

    @NewIp.setter
    def NewIp(self, NewIp):
        self._NewIp = NewIp


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OldIpType = params.get("OldIpType")
        if params.get("OldIp") is not None:
            self._OldIp = IpSegment()
            self._OldIp._deserialize(params.get("OldIp"))
        self._NewIpType = params.get("NewIpType")
        if params.get("NewIp") is not None:
            self._NewIp = IpSegment()
            self._NewIp._deserialize(params.get("NewIp"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSBlackWhiteIpListResponse(AbstractModel):
    """ModifyDDoSBlackWhiteIpList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDDoSGeoIPBlockConfigRequest(AbstractModel):
    """ModifyDDoSGeoIPBlockConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _DDoSGeoIPBlockConfig: DDoS区域封禁配置，填写参数时配置ID不能为空
        :type DDoSGeoIPBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        self._InstanceId = None
        self._DDoSGeoIPBlockConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSGeoIPBlockConfig(self):
        """DDoS区域封禁配置，填写参数时配置ID不能为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSGeoIPBlockConfig`
        """
        return self._DDoSGeoIPBlockConfig

    @DDoSGeoIPBlockConfig.setter
    def DDoSGeoIPBlockConfig(self, DDoSGeoIPBlockConfig):
        self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSGeoIPBlockConfig") is not None:
            self._DDoSGeoIPBlockConfig = DDoSGeoIPBlockConfig()
            self._DDoSGeoIPBlockConfig._deserialize(params.get("DDoSGeoIPBlockConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSGeoIPBlockConfigResponse(AbstractModel):
    """ModifyDDoSGeoIPBlockConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDDoSLevelRequest(AbstractModel):
    """ModifyDDoSLevel请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 资源ID
        :type Id: str
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _Method: =get表示读取防护等级；=set表示修改防护等级
        :type Method: str
        :param _DDoSLevel: 防护等级，取值[low,middle,high]；当Method=set时必填
        :type DDoSLevel: str
        """
        self._Id = None
        self._Business = None
        self._Method = None
        self._DDoSLevel = None

    @property
    def Id(self):
        """资源ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Method(self):
        """=get表示读取防护等级；=set表示修改防护等级
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def DDoSLevel(self):
        """防护等级，取值[low,middle,high]；当Method=set时必填
        :rtype: str
        """
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Business = params.get("Business")
        self._Method = params.get("Method")
        self._DDoSLevel = params.get("DDoSLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSLevelResponse(AbstractModel):
    """ModifyDDoSLevel返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DDoSLevel: 防护等级，取值[low,middle,high]
        :type DDoSLevel: str
        :param _Id: 资源ID
        :type Id: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DDoSLevel = None
        self._Id = None
        self._RequestId = None

    @property
    def DDoSLevel(self):
        """防护等级，取值[low,middle,high]
        :rtype: str
        """
        return self._DDoSLevel

    @DDoSLevel.setter
    def DDoSLevel(self, DDoSLevel):
        self._DDoSLevel = DDoSLevel

    @property
    def Id(self):
        """资源ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DDoSLevel = params.get("DDoSLevel")
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")


class ModifyDDoSSpeedLimitConfigRequest(AbstractModel):
    """ModifyDDoSSpeedLimitConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _DDoSSpeedLimitConfig: 访问限速配置，填写参数时配置ID不能为空
        :type DDoSSpeedLimitConfig: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        self._InstanceId = None
        self._DDoSSpeedLimitConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def DDoSSpeedLimitConfig(self):
        """访问限速配置，填写参数时配置ID不能为空
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.DDoSSpeedLimitConfig`
        """
        return self._DDoSSpeedLimitConfig

    @DDoSSpeedLimitConfig.setter
    def DDoSSpeedLimitConfig(self, DDoSSpeedLimitConfig):
        self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("DDoSSpeedLimitConfig") is not None:
            self._DDoSSpeedLimitConfig = DDoSSpeedLimitConfig()
            self._DDoSSpeedLimitConfig._deserialize(params.get("DDoSSpeedLimitConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSSpeedLimitConfigResponse(AbstractModel):
    """ModifyDDoSSpeedLimitConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyDDoSThresholdRequest(AbstractModel):
    """ModifyDDoSThreshold请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Threshold: DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
当设置值为0时，表示采用默认值；
        :type Threshold: int
        :param _Id: 资源ID
        :type Id: str
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :type Business: str
        :param _OtherThresholdFlag: 配置其他阈值标志位，1表示配置其他阈值
        :type OtherThresholdFlag: int
        :param _SynFloodThreshold: SYN FLOOD流量阈值
        :type SynFloodThreshold: int
        :param _SynFloodPktThreshold: SYN FLOOD包量阈值
        :type SynFloodPktThreshold: int
        :param _UdpFloodThreshold: UDP FLOOD流量阈值
        :type UdpFloodThreshold: int
        :param _UdpFloodPktThreshold: UDP FLOOD包量阈值
        :type UdpFloodPktThreshold: int
        :param _AckFloodThreshold: ACK FLOOD流量阈值
        :type AckFloodThreshold: int
        :param _AckFloodPktThreshold: ACK FLOOD包量阈值
        :type AckFloodPktThreshold: int
        :param _SynAckFloodThreshold: SYNACK FLOOD流量阈值
        :type SynAckFloodThreshold: int
        :param _SynAckFloodPktThreshold: SYNACK FLOOD包量阈值
        :type SynAckFloodPktThreshold: int
        :param _RstFloodThreshold: RST FLOOD流量阈值
        :type RstFloodThreshold: int
        :param _RstFloodPktThreshold: RST FLOOD包量阈值
        :type RstFloodPktThreshold: int
        """
        self._Threshold = None
        self._Id = None
        self._Business = None
        self._OtherThresholdFlag = None
        self._SynFloodThreshold = None
        self._SynFloodPktThreshold = None
        self._UdpFloodThreshold = None
        self._UdpFloodPktThreshold = None
        self._AckFloodThreshold = None
        self._AckFloodPktThreshold = None
        self._SynAckFloodThreshold = None
        self._SynAckFloodPktThreshold = None
        self._RstFloodThreshold = None
        self._RstFloodPktThreshold = None

    @property
    def Threshold(self):
        """DDoS清洗阈值，取值[0, 60, 80, 100, 150, 200, 250, 300, 400, 500, 700, 1000];
当设置值为0时，表示采用默认值；
        :rtype: int
        """
        return self._Threshold

    @Threshold.setter
    def Threshold(self, Threshold):
        self._Threshold = Threshold

    @property
    def Id(self):
        """资源ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP；bgp表示独享包；bgp-multip表示共享包；net表示高防IP专业版）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def OtherThresholdFlag(self):
        """配置其他阈值标志位，1表示配置其他阈值
        :rtype: int
        """
        return self._OtherThresholdFlag

    @OtherThresholdFlag.setter
    def OtherThresholdFlag(self, OtherThresholdFlag):
        self._OtherThresholdFlag = OtherThresholdFlag

    @property
    def SynFloodThreshold(self):
        """SYN FLOOD流量阈值
        :rtype: int
        """
        return self._SynFloodThreshold

    @SynFloodThreshold.setter
    def SynFloodThreshold(self, SynFloodThreshold):
        self._SynFloodThreshold = SynFloodThreshold

    @property
    def SynFloodPktThreshold(self):
        """SYN FLOOD包量阈值
        :rtype: int
        """
        return self._SynFloodPktThreshold

    @SynFloodPktThreshold.setter
    def SynFloodPktThreshold(self, SynFloodPktThreshold):
        self._SynFloodPktThreshold = SynFloodPktThreshold

    @property
    def UdpFloodThreshold(self):
        """UDP FLOOD流量阈值
        :rtype: int
        """
        return self._UdpFloodThreshold

    @UdpFloodThreshold.setter
    def UdpFloodThreshold(self, UdpFloodThreshold):
        self._UdpFloodThreshold = UdpFloodThreshold

    @property
    def UdpFloodPktThreshold(self):
        """UDP FLOOD包量阈值
        :rtype: int
        """
        return self._UdpFloodPktThreshold

    @UdpFloodPktThreshold.setter
    def UdpFloodPktThreshold(self, UdpFloodPktThreshold):
        self._UdpFloodPktThreshold = UdpFloodPktThreshold

    @property
    def AckFloodThreshold(self):
        """ACK FLOOD流量阈值
        :rtype: int
        """
        return self._AckFloodThreshold

    @AckFloodThreshold.setter
    def AckFloodThreshold(self, AckFloodThreshold):
        self._AckFloodThreshold = AckFloodThreshold

    @property
    def AckFloodPktThreshold(self):
        """ACK FLOOD包量阈值
        :rtype: int
        """
        return self._AckFloodPktThreshold

    @AckFloodPktThreshold.setter
    def AckFloodPktThreshold(self, AckFloodPktThreshold):
        self._AckFloodPktThreshold = AckFloodPktThreshold

    @property
    def SynAckFloodThreshold(self):
        """SYNACK FLOOD流量阈值
        :rtype: int
        """
        return self._SynAckFloodThreshold

    @SynAckFloodThreshold.setter
    def SynAckFloodThreshold(self, SynAckFloodThreshold):
        self._SynAckFloodThreshold = SynAckFloodThreshold

    @property
    def SynAckFloodPktThreshold(self):
        """SYNACK FLOOD包量阈值
        :rtype: int
        """
        return self._SynAckFloodPktThreshold

    @SynAckFloodPktThreshold.setter
    def SynAckFloodPktThreshold(self, SynAckFloodPktThreshold):
        self._SynAckFloodPktThreshold = SynAckFloodPktThreshold

    @property
    def RstFloodThreshold(self):
        """RST FLOOD流量阈值
        :rtype: int
        """
        return self._RstFloodThreshold

    @RstFloodThreshold.setter
    def RstFloodThreshold(self, RstFloodThreshold):
        self._RstFloodThreshold = RstFloodThreshold

    @property
    def RstFloodPktThreshold(self):
        """RST FLOOD包量阈值
        :rtype: int
        """
        return self._RstFloodPktThreshold

    @RstFloodPktThreshold.setter
    def RstFloodPktThreshold(self, RstFloodPktThreshold):
        self._RstFloodPktThreshold = RstFloodPktThreshold


    def _deserialize(self, params):
        self._Threshold = params.get("Threshold")
        self._Id = params.get("Id")
        self._Business = params.get("Business")
        self._OtherThresholdFlag = params.get("OtherThresholdFlag")
        self._SynFloodThreshold = params.get("SynFloodThreshold")
        self._SynFloodPktThreshold = params.get("SynFloodPktThreshold")
        self._UdpFloodThreshold = params.get("UdpFloodThreshold")
        self._UdpFloodPktThreshold = params.get("UdpFloodPktThreshold")
        self._AckFloodThreshold = params.get("AckFloodThreshold")
        self._AckFloodPktThreshold = params.get("AckFloodPktThreshold")
        self._SynAckFloodThreshold = params.get("SynAckFloodThreshold")
        self._SynAckFloodPktThreshold = params.get("SynAckFloodPktThreshold")
        self._RstFloodThreshold = params.get("RstFloodThreshold")
        self._RstFloodPktThreshold = params.get("RstFloodPktThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDDoSThresholdResponse(AbstractModel):
    """ModifyDDoSThreshold返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """成功码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyDomainUsrNameRequest(AbstractModel):
    """ModifyDomainUsrName请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainName: 用户CNAME
        :type DomainName: str
        :param _DomainUserName: 域名名称
        :type DomainUserName: str
        """
        self._DomainName = None
        self._DomainUserName = None

    @property
    def DomainName(self):
        """用户CNAME
        :rtype: str
        """
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def DomainUserName(self):
        """域名名称
        :rtype: str
        """
        return self._DomainUserName

    @DomainUserName.setter
    def DomainUserName(self, DomainUserName):
        self._DomainUserName = DomainUserName


    def _deserialize(self, params):
        self._DomainName = params.get("DomainName")
        self._DomainUserName = params.get("DomainUserName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainUsrNameResponse(AbstractModel):
    """ModifyDomainUsrName返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNewDomainRulesRequest(AbstractModel):
    """ModifyNewDomainRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Business: DDoS防护子产品代号（bgpip表示高防IP）
        :type Business: str
        :param _Id: 资源ID
        :type Id: str
        :param _Rule: 域名转发规则
        :type Rule: :class:`tencentcloud.antiddos.v20200309.models.NewL7RuleEntry`
        """
        self._Business = None
        self._Id = None
        self._Rule = None

    @property
    def Business(self):
        """DDoS防护子产品代号（bgpip表示高防IP）
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def Id(self):
        """资源ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Rule(self):
        """域名转发规则
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.NewL7RuleEntry`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._Business = params.get("Business")
        self._Id = params.get("Id")
        if params.get("Rule") is not None:
            self._Rule = NewL7RuleEntry()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNewDomainRulesResponse(AbstractModel):
    """ModifyNewDomainRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Success: 成功码
        :type Success: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Success = None
        self._RequestId = None

    @property
    def Success(self):
        """成功码
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.SuccessCode`
        """
        return self._Success

    @Success.setter
    def Success(self, Success):
        self._Success = Success

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Success") is not None:
            self._Success = SuccessCode()
            self._Success._deserialize(params.get("Success"))
        self._RequestId = params.get("RequestId")


class ModifyPacketFilterConfigRequest(AbstractModel):
    """ModifyPacketFilterConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _PacketFilterConfig: 特征过滤配置
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        self._InstanceId = None
        self._PacketFilterConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def PacketFilterConfig(self):
        """特征过滤配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPacketFilterConfigResponse(AbstractModel):
    """ModifyPacketFilterConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPortAclConfigRequest(AbstractModel):
    """ModifyPortAclConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _OldAclConfig: 旧端口acl策略
        :type OldAclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        :param _NewAclConfig: 新端口acl策略
        :type NewAclConfig: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        self._InstanceId = None
        self._OldAclConfig = None
        self._NewAclConfig = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OldAclConfig(self):
        """旧端口acl策略
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        return self._OldAclConfig

    @OldAclConfig.setter
    def OldAclConfig(self, OldAclConfig):
        self._OldAclConfig = OldAclConfig

    @property
    def NewAclConfig(self):
        """新端口acl策略
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.AclConfig`
        """
        return self._NewAclConfig

    @NewAclConfig.setter
    def NewAclConfig(self, NewAclConfig):
        self._NewAclConfig = NewAclConfig


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        if params.get("OldAclConfig") is not None:
            self._OldAclConfig = AclConfig()
            self._OldAclConfig._deserialize(params.get("OldAclConfig"))
        if params.get("NewAclConfig") is not None:
            self._NewAclConfig = AclConfig()
            self._NewAclConfig._deserialize(params.get("NewAclConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPortAclConfigResponse(AbstractModel):
    """ModifyPortAclConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NewL7RuleEntry(AbstractModel):
    """L7规则

    """

    def __init__(self):
        r"""
        :param _Protocol: 转发协议，取值[http, https]
        :type Protocol: str
        :param _Domain: 转发域名
        :type Domain: str
        :param _LbType: 负载均衡方式，取值[1(加权轮询)]
        :type LbType: int
        :param _KeepEnable: 会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :type KeepEnable: int
        :param _KeepTime: 会话保持时间，单位秒
        :type KeepTime: int
        :param _SourceType: 回源方式，取值[1(域名回源)，2(IP回源)]
        :type SourceType: int
        :param _SourceList: 回源列表
        :type SourceList: list of L4RuleSource
        :param _Region: 区域码
        :type Region: int
        :param _Id: 资源Id
        :type Id: str
        :param _Ip: 资源Ip
        :type Ip: str
        :param _RuleId: 规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :type RuleId: str
        :param _RuleName: 规则描述
        :type RuleName: str
        :param _CertType: 证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :type CertType: int
        :param _SSLId: 当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :type SSLId: str
        :param _Cert: 当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type Cert: str
        :param _PrivateKey: 当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :type PrivateKey: str
        :param _Status: 规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :type Status: int
        :param _CCStatus: cc防护状态，取值[0(关闭), 1(开启)]
        :type CCStatus: int
        :param _CCEnable: HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :type CCEnable: int
        :param _CCThreshold: HTTPS协议的CC防护阈值（已废弃）
        :type CCThreshold: int
        :param _CCThresholdNew: HTTPS协议的CC防护阈值 -1：默认防御阈值
0: 关闭
大于0：自定义防护阈值
        :type CCThresholdNew: int
        :param _CCLevel: HTTPS协议的CC防护等级
        :type CCLevel: str
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        :param _HttpsToHttpEnable: 是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :type HttpsToHttpEnable: int
        :param _VirtualPort: 接入端口值
        :type VirtualPort: int
        :param _RewriteHttps: http强制跳转https，1表示打开，0表示关闭
        :type RewriteHttps: int
        :param _ErrCode: 规则配置失败时的详细错误原因(仅当Status=2时有效)，1001证书不存在，1002证书获取失败，1003证书上传失败，1004证书已过期
        :type ErrCode: int
        :param _Version: 版本
        :type Version: int
        """
        self._Protocol = None
        self._Domain = None
        self._LbType = None
        self._KeepEnable = None
        self._KeepTime = None
        self._SourceType = None
        self._SourceList = None
        self._Region = None
        self._Id = None
        self._Ip = None
        self._RuleId = None
        self._RuleName = None
        self._CertType = None
        self._SSLId = None
        self._Cert = None
        self._PrivateKey = None
        self._Status = None
        self._CCStatus = None
        self._CCEnable = None
        self._CCThreshold = None
        self._CCThresholdNew = None
        self._CCLevel = None
        self._ModifyTime = None
        self._HttpsToHttpEnable = None
        self._VirtualPort = None
        self._RewriteHttps = None
        self._ErrCode = None
        self._Version = None

    @property
    def Protocol(self):
        """转发协议，取值[http, https]
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Domain(self):
        """转发域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LbType(self):
        """负载均衡方式，取值[1(加权轮询)]
        :rtype: int
        """
        return self._LbType

    @LbType.setter
    def LbType(self, LbType):
        self._LbType = LbType

    @property
    def KeepEnable(self):
        """会话保持开关，取值[0(会话保持关闭)，1(会话保持开启)]
        :rtype: int
        """
        return self._KeepEnable

    @KeepEnable.setter
    def KeepEnable(self, KeepEnable):
        self._KeepEnable = KeepEnable

    @property
    def KeepTime(self):
        """会话保持时间，单位秒
        :rtype: int
        """
        return self._KeepTime

    @KeepTime.setter
    def KeepTime(self, KeepTime):
        self._KeepTime = KeepTime

    @property
    def SourceType(self):
        """回源方式，取值[1(域名回源)，2(IP回源)]
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceList(self):
        """回源列表
        :rtype: list of L4RuleSource
        """
        return self._SourceList

    @SourceList.setter
    def SourceList(self, SourceList):
        self._SourceList = SourceList

    @property
    def Region(self):
        """区域码
        :rtype: int
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Id(self):
        """资源Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Ip(self):
        """资源Ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def RuleId(self):
        """规则ID，当添加新规则时可以不用填写此字段；当修改或者删除规则时需要填写此字段；
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def RuleName(self):
        """规则描述
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def CertType(self):
        """证书来源，当转发协议为https时必须填，取值[2(腾讯云托管证书)]，当转发协议为http时也可以填0
        :rtype: int
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def SSLId(self):
        """当证书来源为腾讯云托管证书时，此字段必须填写托管证书ID
        :rtype: str
        """
        return self._SSLId

    @SSLId.setter
    def SSLId(self, SSLId):
        self._SSLId = SSLId

    @property
    def Cert(self):
        """当证书来源为自有证书时，此字段必须填写证书内容；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def PrivateKey(self):
        """当证书来源为自有证书时，此字段必须填写证书密钥；(因已不再支持自有证书，此字段已弃用，请不用填写此字段)
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def Status(self):
        """规则状态，取值[0(规则配置成功)，1(规则配置生效中)，2(规则配置失败)，3(规则删除生效中)，5(规则删除失败)，6(规则等待配置)，7(规则等待删除)，8(规则待配置证书)]
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CCStatus(self):
        """cc防护状态，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCStatus

    @CCStatus.setter
    def CCStatus(self, CCStatus):
        self._CCStatus = CCStatus

    @property
    def CCEnable(self):
        """HTTPS协议的CC防护状态，取值[0(关闭), 1(开启)]
        :rtype: int
        """
        return self._CCEnable

    @CCEnable.setter
    def CCEnable(self, CCEnable):
        self._CCEnable = CCEnable

    @property
    def CCThreshold(self):
        """HTTPS协议的CC防护阈值（已废弃）
        :rtype: int
        """
        return self._CCThreshold

    @CCThreshold.setter
    def CCThreshold(self, CCThreshold):
        self._CCThreshold = CCThreshold

    @property
    def CCThresholdNew(self):
        """HTTPS协议的CC防护阈值 -1：默认防御阈值
0: 关闭
大于0：自定义防护阈值
        :rtype: int
        """
        return self._CCThresholdNew

    @CCThresholdNew.setter
    def CCThresholdNew(self, CCThresholdNew):
        self._CCThresholdNew = CCThresholdNew

    @property
    def CCLevel(self):
        """HTTPS协议的CC防护等级
        :rtype: str
        """
        return self._CCLevel

    @CCLevel.setter
    def CCLevel(self, CCLevel):
        self._CCLevel = CCLevel

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def HttpsToHttpEnable(self):
        """是否开启Https协议使用Http回源，取值[0(关闭), 1(开启)]，不填写默认是关闭
        :rtype: int
        """
        return self._HttpsToHttpEnable

    @HttpsToHttpEnable.setter
    def HttpsToHttpEnable(self, HttpsToHttpEnable):
        self._HttpsToHttpEnable = HttpsToHttpEnable

    @property
    def VirtualPort(self):
        """接入端口值
        :rtype: int
        """
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort

    @property
    def RewriteHttps(self):
        """http强制跳转https，1表示打开，0表示关闭
        :rtype: int
        """
        return self._RewriteHttps

    @RewriteHttps.setter
    def RewriteHttps(self, RewriteHttps):
        self._RewriteHttps = RewriteHttps

    @property
    def ErrCode(self):
        """规则配置失败时的详细错误原因(仅当Status=2时有效)，1001证书不存在，1002证书获取失败，1003证书上传失败，1004证书已过期
        :rtype: int
        """
        return self._ErrCode

    @ErrCode.setter
    def ErrCode(self, ErrCode):
        self._ErrCode = ErrCode

    @property
    def Version(self):
        """版本
        :rtype: int
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Domain = params.get("Domain")
        self._LbType = params.get("LbType")
        self._KeepEnable = params.get("KeepEnable")
        self._KeepTime = params.get("KeepTime")
        self._SourceType = params.get("SourceType")
        if params.get("SourceList") is not None:
            self._SourceList = []
            for item in params.get("SourceList"):
                obj = L4RuleSource()
                obj._deserialize(item)
                self._SourceList.append(obj)
        self._Region = params.get("Region")
        self._Id = params.get("Id")
        self._Ip = params.get("Ip")
        self._RuleId = params.get("RuleId")
        self._RuleName = params.get("RuleName")
        self._CertType = params.get("CertType")
        self._SSLId = params.get("SSLId")
        self._Cert = params.get("Cert")
        self._PrivateKey = params.get("PrivateKey")
        self._Status = params.get("Status")
        self._CCStatus = params.get("CCStatus")
        self._CCEnable = params.get("CCEnable")
        self._CCThreshold = params.get("CCThreshold")
        self._CCThresholdNew = params.get("CCThresholdNew")
        self._CCLevel = params.get("CCLevel")
        self._ModifyTime = params.get("ModifyTime")
        self._HttpsToHttpEnable = params.get("HttpsToHttpEnable")
        self._VirtualPort = params.get("VirtualPort")
        self._RewriteHttps = params.get("RewriteHttps")
        self._ErrCode = params.get("ErrCode")
        self._Version = params.get("Version")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverviewDDoSEvent(AbstractModel):
    """防护概览DDoS攻击事件

    """

    def __init__(self):
        r"""
        :param _Id: 事件Id
        :type Id: str
        :param _Vip: ip
        :type Vip: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _AttackType: 攻击类型
        :type AttackType: str
        :param _AttackStatus: 攻击状态，0：攻击中；1：攻击结束
        :type AttackStatus: int
        :param _Mbps: 攻击流量，单位Mbps
        :type Mbps: int
        :param _Pps: 攻击包量，单位pps
        :type Pps: int
        :param _Business: 业务类型，bgp-multip：高防包；bgpip：高防ip；basic：基础防护
        :type Business: str
        :param _InstanceId: 高防实例Id
        :type InstanceId: str
        :param _InstanceName: 高防实例名称
        :type InstanceName: str
        """
        self._Id = None
        self._Vip = None
        self._StartTime = None
        self._EndTime = None
        self._AttackType = None
        self._AttackStatus = None
        self._Mbps = None
        self._Pps = None
        self._Business = None
        self._InstanceId = None
        self._InstanceName = None

    @property
    def Id(self):
        """事件Id
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Vip(self):
        """ip
        :rtype: str
        """
        return self._Vip

    @Vip.setter
    def Vip(self, Vip):
        self._Vip = Vip

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def AttackType(self):
        """攻击类型
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def AttackStatus(self):
        """攻击状态，0：攻击中；1：攻击结束
        :rtype: int
        """
        return self._AttackStatus

    @AttackStatus.setter
    def AttackStatus(self, AttackStatus):
        self._AttackStatus = AttackStatus

    @property
    def Mbps(self):
        """攻击流量，单位Mbps
        :rtype: int
        """
        return self._Mbps

    @Mbps.setter
    def Mbps(self, Mbps):
        self._Mbps = Mbps

    @property
    def Pps(self):
        """攻击包量，单位pps
        :rtype: int
        """
        return self._Pps

    @Pps.setter
    def Pps(self, Pps):
        self._Pps = Pps

    @property
    def Business(self):
        """业务类型，bgp-multip：高防包；bgpip：高防ip；basic：基础防护
        :rtype: str
        """
        return self._Business

    @Business.setter
    def Business(self, Business):
        self._Business = Business

    @property
    def InstanceId(self):
        """高防实例Id
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        """高防实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Vip = params.get("Vip")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._AttackType = params.get("AttackType")
        self._AttackStatus = params.get("AttackStatus")
        self._Mbps = params.get("Mbps")
        self._Pps = params.get("Pps")
        self._Business = params.get("Business")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackInfo(AbstractModel):
    """套餐包信息

    """

    def __init__(self):
        r"""
        :param _PackType: 套餐包的类型，取值[
staticpack：高防IP三网套餐包
insurance：保险套餐包
]
        :type PackType: str
        :param _PackId: 套餐包的ID
        :type PackId: str
        """
        self._PackType = None
        self._PackId = None

    @property
    def PackType(self):
        """套餐包的类型，取值[
staticpack：高防IP三网套餐包
insurance：保险套餐包
]
        :rtype: str
        """
        return self._PackType

    @PackType.setter
    def PackType(self, PackType):
        self._PackType = PackType

    @property
    def PackId(self):
        """套餐包的ID
        :rtype: str
        """
        return self._PackId

    @PackId.setter
    def PackId(self, PackId):
        self._PackId = PackId


    def _deserialize(self, params):
        self._PackType = params.get("PackType")
        self._PackId = params.get("PackId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterConfig(AbstractModel):
    """特征过滤配置

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议，取值[tcp udp icmp all]
        :type Protocol: str
        :param _SportStart: 起始源端口，取值0~65535
        :type SportStart: int
        :param _SportEnd: 结束源端口，取值1~65535，必须大于等于起始源端口
        :type SportEnd: int
        :param _DportStart: 起始目的端口，取值0~65535
        :type DportStart: int
        :param _DportEnd: 结束目的端口，取值1~65535，必须大于等于起始目的端口
        :type DportEnd: int
        :param _PktlenMin: 最小报文长度，取值1-1500
        :type PktlenMin: int
        :param _PktlenMax: 最大报文长度，取值1-1500，必须大于等于最小报文长度
        :type PktlenMax: int
        :param _Action: 动作，取值[
drop(丢弃)
transmit(放行)
drop_black(丢弃并拉黑)
drop_rst(拦截)（已废弃，不支持drop_rst）
drop_black_rst(拦截并拉黑)（已废弃，不支持drop_black_rst）
forward(继续防护)
]
        :type Action: str
        :param _MatchBegin: 检测位置，取值[
begin_l3(IP头)
begin_l4(TCP/UDP头)
begin_l5(T载荷)
no_match(不匹配)
]
        :type MatchBegin: str
        :param _MatchType: 检测类型，取值[
sunday(关键字)
pcre(正则表达式) （已废弃，仅支持sunday）
]
        :type MatchType: str
        :param _Str: 检测值，关键字符串或正则表达式,取值[ 当检测类型为sunday时，请填写字符串或者16进制字节码，例如\x313233对应的是字符串"123"的16进制字节码; 最多支持63位; ]
        :type Str: str
        :param _Depth: 从检测位置开始的检测深度，取值[0,1500]
        :type Depth: int
        :param _Offset: 从检测位置开始的偏移量，取值范围[0,Depth]
        :type Offset: int
        :param _IsNot: 是否包含检测值，取值[
0(包含)
1(不包含) （已废弃，仅支持0）
]
        :type IsNot: int
        :param _MatchLogic: 
当有第二个检测条件时，与第一检测条件的且或关系，取值[
and(且的关系) （已废弃，仅支持none）
none(当没有第二个检测条件时填写此值)
]
        :type MatchLogic: str
        :param _MatchBegin2: （已废弃）
        :type MatchBegin2: str
        :param _MatchType2: （已废弃）
        :type MatchType2: str
        :param _Str2: （已废弃）
        :type Str2: str
        :param _Depth2: （已废弃）
        :type Depth2: int
        :param _Offset2: （已废弃）
        :type Offset2: int
        :param _IsNot2: （已废弃）
        :type IsNot2: int
        :param _Id: 特征过滤配置添加成功后自动生成的规则ID，当添加新特征过滤配置时，此字段不用填写；当修改/删除新特征过滤配置时，此字段必填；
        :type Id: str
        :param _PktLenGT: 大于报文长度，取值1+
        :type PktLenGT: int
        """
        self._Protocol = None
        self._SportStart = None
        self._SportEnd = None
        self._DportStart = None
        self._DportEnd = None
        self._PktlenMin = None
        self._PktlenMax = None
        self._Action = None
        self._MatchBegin = None
        self._MatchType = None
        self._Str = None
        self._Depth = None
        self._Offset = None
        self._IsNot = None
        self._MatchLogic = None
        self._MatchBegin2 = None
        self._MatchType2 = None
        self._Str2 = None
        self._Depth2 = None
        self._Offset2 = None
        self._IsNot2 = None
        self._Id = None
        self._PktLenGT = None

    @property
    def Protocol(self):
        """协议，取值[tcp udp icmp all]
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SportStart(self):
        """起始源端口，取值0~65535
        :rtype: int
        """
        return self._SportStart

    @SportStart.setter
    def SportStart(self, SportStart):
        self._SportStart = SportStart

    @property
    def SportEnd(self):
        """结束源端口，取值1~65535，必须大于等于起始源端口
        :rtype: int
        """
        return self._SportEnd

    @SportEnd.setter
    def SportEnd(self, SportEnd):
        self._SportEnd = SportEnd

    @property
    def DportStart(self):
        """起始目的端口，取值0~65535
        :rtype: int
        """
        return self._DportStart

    @DportStart.setter
    def DportStart(self, DportStart):
        self._DportStart = DportStart

    @property
    def DportEnd(self):
        """结束目的端口，取值1~65535，必须大于等于起始目的端口
        :rtype: int
        """
        return self._DportEnd

    @DportEnd.setter
    def DportEnd(self, DportEnd):
        self._DportEnd = DportEnd

    @property
    def PktlenMin(self):
        """最小报文长度，取值1-1500
        :rtype: int
        """
        return self._PktlenMin

    @PktlenMin.setter
    def PktlenMin(self, PktlenMin):
        self._PktlenMin = PktlenMin

    @property
    def PktlenMax(self):
        """最大报文长度，取值1-1500，必须大于等于最小报文长度
        :rtype: int
        """
        return self._PktlenMax

    @PktlenMax.setter
    def PktlenMax(self, PktlenMax):
        self._PktlenMax = PktlenMax

    @property
    def Action(self):
        """动作，取值[
drop(丢弃)
transmit(放行)
drop_black(丢弃并拉黑)
drop_rst(拦截)（已废弃，不支持drop_rst）
drop_black_rst(拦截并拉黑)（已废弃，不支持drop_black_rst）
forward(继续防护)
]
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def MatchBegin(self):
        """检测位置，取值[
begin_l3(IP头)
begin_l4(TCP/UDP头)
begin_l5(T载荷)
no_match(不匹配)
]
        :rtype: str
        """
        return self._MatchBegin

    @MatchBegin.setter
    def MatchBegin(self, MatchBegin):
        self._MatchBegin = MatchBegin

    @property
    def MatchType(self):
        """检测类型，取值[
sunday(关键字)
pcre(正则表达式) （已废弃，仅支持sunday）
]
        :rtype: str
        """
        return self._MatchType

    @MatchType.setter
    def MatchType(self, MatchType):
        self._MatchType = MatchType

    @property
    def Str(self):
        """检测值，关键字符串或正则表达式,取值[ 当检测类型为sunday时，请填写字符串或者16进制字节码，例如\x313233对应的是字符串"123"的16进制字节码; 最多支持63位; ]
        :rtype: str
        """
        return self._Str

    @Str.setter
    def Str(self, Str):
        self._Str = Str

    @property
    def Depth(self):
        """从检测位置开始的检测深度，取值[0,1500]
        :rtype: int
        """
        return self._Depth

    @Depth.setter
    def Depth(self, Depth):
        self._Depth = Depth

    @property
    def Offset(self):
        """从检测位置开始的偏移量，取值范围[0,Depth]
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def IsNot(self):
        """是否包含检测值，取值[
0(包含)
1(不包含) （已废弃，仅支持0）
]
        :rtype: int
        """
        return self._IsNot

    @IsNot.setter
    def IsNot(self, IsNot):
        self._IsNot = IsNot

    @property
    def MatchLogic(self):
        """
当有第二个检测条件时，与第一检测条件的且或关系，取值[
and(且的关系) （已废弃，仅支持none）
none(当没有第二个检测条件时填写此值)
]
        :rtype: str
        """
        return self._MatchLogic

    @MatchLogic.setter
    def MatchLogic(self, MatchLogic):
        self._MatchLogic = MatchLogic

    @property
    def MatchBegin2(self):
        """（已废弃）
        :rtype: str
        """
        return self._MatchBegin2

    @MatchBegin2.setter
    def MatchBegin2(self, MatchBegin2):
        self._MatchBegin2 = MatchBegin2

    @property
    def MatchType2(self):
        """（已废弃）
        :rtype: str
        """
        return self._MatchType2

    @MatchType2.setter
    def MatchType2(self, MatchType2):
        self._MatchType2 = MatchType2

    @property
    def Str2(self):
        """（已废弃）
        :rtype: str
        """
        return self._Str2

    @Str2.setter
    def Str2(self, Str2):
        self._Str2 = Str2

    @property
    def Depth2(self):
        """（已废弃）
        :rtype: int
        """
        return self._Depth2

    @Depth2.setter
    def Depth2(self, Depth2):
        self._Depth2 = Depth2

    @property
    def Offset2(self):
        """（已废弃）
        :rtype: int
        """
        return self._Offset2

    @Offset2.setter
    def Offset2(self, Offset2):
        self._Offset2 = Offset2

    @property
    def IsNot2(self):
        """（已废弃）
        :rtype: int
        """
        return self._IsNot2

    @IsNot2.setter
    def IsNot2(self, IsNot2):
        self._IsNot2 = IsNot2

    @property
    def Id(self):
        """特征过滤配置添加成功后自动生成的规则ID，当添加新特征过滤配置时，此字段不用填写；当修改/删除新特征过滤配置时，此字段必填；
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def PktLenGT(self):
        """大于报文长度，取值1+
        :rtype: int
        """
        return self._PktLenGT

    @PktLenGT.setter
    def PktLenGT(self, PktLenGT):
        self._PktLenGT = PktLenGT


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._SportStart = params.get("SportStart")
        self._SportEnd = params.get("SportEnd")
        self._DportStart = params.get("DportStart")
        self._DportEnd = params.get("DportEnd")
        self._PktlenMin = params.get("PktlenMin")
        self._PktlenMax = params.get("PktlenMax")
        self._Action = params.get("Action")
        self._MatchBegin = params.get("MatchBegin")
        self._MatchType = params.get("MatchType")
        self._Str = params.get("Str")
        self._Depth = params.get("Depth")
        self._Offset = params.get("Offset")
        self._IsNot = params.get("IsNot")
        self._MatchLogic = params.get("MatchLogic")
        self._MatchBegin2 = params.get("MatchBegin2")
        self._MatchType2 = params.get("MatchType2")
        self._Str2 = params.get("Str2")
        self._Depth2 = params.get("Depth2")
        self._Offset2 = params.get("Offset2")
        self._IsNot2 = params.get("IsNot2")
        self._Id = params.get("Id")
        self._PktLenGT = params.get("PktLenGT")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PacketFilterRelation(AbstractModel):
    """特征过滤相关信息

    """

    def __init__(self):
        r"""
        :param _PacketFilterConfig: 特征过滤配置
        :type PacketFilterConfig: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        :param _InstanceDetailList: 特征过滤配置所属的实例
        :type InstanceDetailList: list of InstanceRelation
        :param _ModifyTime: 修改时间
        :type ModifyTime: str
        """
        self._PacketFilterConfig = None
        self._InstanceDetailList = None
        self._ModifyTime = None

    @property
    def PacketFilterConfig(self):
        """特征过滤配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.PacketFilterConfig`
        """
        return self._PacketFilterConfig

    @PacketFilterConfig.setter
    def PacketFilterConfig(self, PacketFilterConfig):
        self._PacketFilterConfig = PacketFilterConfig

    @property
    def InstanceDetailList(self):
        """特征过滤配置所属的实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList

    @property
    def ModifyTime(self):
        """修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime


    def _deserialize(self, params):
        if params.get("PacketFilterConfig") is not None:
            self._PacketFilterConfig = PacketFilterConfig()
            self._PacketFilterConfig._deserialize(params.get("PacketFilterConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        self._ModifyTime = params.get("ModifyTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PortSegment(AbstractModel):
    """端口段信息

    """

    def __init__(self):
        r"""
        :param _BeginPort: 起始端口，取值1~65535
        :type BeginPort: int
        :param _EndPort: 结束端口，取值1~65535，必须不小于起始端口
        :type EndPort: int
        """
        self._BeginPort = None
        self._EndPort = None

    @property
    def BeginPort(self):
        """起始端口，取值1~65535
        :rtype: int
        """
        return self._BeginPort

    @BeginPort.setter
    def BeginPort(self, BeginPort):
        self._BeginPort = BeginPort

    @property
    def EndPort(self):
        """结束端口，取值1~65535，必须不小于起始端口
        :rtype: int
        """
        return self._EndPort

    @EndPort.setter
    def EndPort(self, EndPort):
        self._EndPort = EndPort


    def _deserialize(self, params):
        self._BeginPort = params.get("BeginPort")
        self._EndPort = params.get("EndPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockConfig(AbstractModel):
    """协议封禁配置

    """

    def __init__(self):
        r"""
        :param _DropTcp: TCP封禁，取值[0(封禁关)，1(封禁开)]
        :type DropTcp: int
        :param _DropUdp: UDP封禁，取值[0(封禁关)，1(封禁开)]
        :type DropUdp: int
        :param _DropIcmp: ICMP封禁，取值[0(封禁关)，1(封禁开)]
        :type DropIcmp: int
        :param _DropOther: 其他协议封禁，取值[0(封禁关)，1(封禁开)]
        :type DropOther: int
        :param _CheckExceptNullConnect: 异常空连接防护，取值[0(防护关)，1(防护开)]
        :type CheckExceptNullConnect: int
        :param _PingOfDeath: ping of death防护，取值[0(防护关)，1(防护开)]
        :type PingOfDeath: int
        :param _TearDrop: tear drop防护，取值[0(防护关)，1(防护开)]
        :type TearDrop: int
        """
        self._DropTcp = None
        self._DropUdp = None
        self._DropIcmp = None
        self._DropOther = None
        self._CheckExceptNullConnect = None
        self._PingOfDeath = None
        self._TearDrop = None

    @property
    def DropTcp(self):
        """TCP封禁，取值[0(封禁关)，1(封禁开)]
        :rtype: int
        """
        return self._DropTcp

    @DropTcp.setter
    def DropTcp(self, DropTcp):
        self._DropTcp = DropTcp

    @property
    def DropUdp(self):
        """UDP封禁，取值[0(封禁关)，1(封禁开)]
        :rtype: int
        """
        return self._DropUdp

    @DropUdp.setter
    def DropUdp(self, DropUdp):
        self._DropUdp = DropUdp

    @property
    def DropIcmp(self):
        """ICMP封禁，取值[0(封禁关)，1(封禁开)]
        :rtype: int
        """
        return self._DropIcmp

    @DropIcmp.setter
    def DropIcmp(self, DropIcmp):
        self._DropIcmp = DropIcmp

    @property
    def DropOther(self):
        """其他协议封禁，取值[0(封禁关)，1(封禁开)]
        :rtype: int
        """
        return self._DropOther

    @DropOther.setter
    def DropOther(self, DropOther):
        self._DropOther = DropOther

    @property
    def CheckExceptNullConnect(self):
        """异常空连接防护，取值[0(防护关)，1(防护开)]
        :rtype: int
        """
        return self._CheckExceptNullConnect

    @CheckExceptNullConnect.setter
    def CheckExceptNullConnect(self, CheckExceptNullConnect):
        self._CheckExceptNullConnect = CheckExceptNullConnect

    @property
    def PingOfDeath(self):
        """ping of death防护，取值[0(防护关)，1(防护开)]
        :rtype: int
        """
        return self._PingOfDeath

    @PingOfDeath.setter
    def PingOfDeath(self, PingOfDeath):
        self._PingOfDeath = PingOfDeath

    @property
    def TearDrop(self):
        """tear drop防护，取值[0(防护关)，1(防护开)]
        :rtype: int
        """
        return self._TearDrop

    @TearDrop.setter
    def TearDrop(self, TearDrop):
        self._TearDrop = TearDrop


    def _deserialize(self, params):
        self._DropTcp = params.get("DropTcp")
        self._DropUdp = params.get("DropUdp")
        self._DropIcmp = params.get("DropIcmp")
        self._DropOther = params.get("DropOther")
        self._CheckExceptNullConnect = params.get("CheckExceptNullConnect")
        self._PingOfDeath = params.get("PingOfDeath")
        self._TearDrop = params.get("TearDrop")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolBlockRelation(AbstractModel):
    """协议封禁相关信息

    """

    def __init__(self):
        r"""
        :param _ProtocolBlockConfig: 协议封禁配置
        :type ProtocolBlockConfig: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        :param _InstanceDetailList: 协议封禁配置所属的实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self._ProtocolBlockConfig = None
        self._InstanceDetailList = None

    @property
    def ProtocolBlockConfig(self):
        """协议封禁配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.ProtocolBlockConfig`
        """
        return self._ProtocolBlockConfig

    @ProtocolBlockConfig.setter
    def ProtocolBlockConfig(self, ProtocolBlockConfig):
        self._ProtocolBlockConfig = ProtocolBlockConfig

    @property
    def InstanceDetailList(self):
        """协议封禁配置所属的实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("ProtocolBlockConfig") is not None:
            self._ProtocolBlockConfig = ProtocolBlockConfig()
            self._ProtocolBlockConfig._deserialize(params.get("ProtocolBlockConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProtocolPort(AbstractModel):
    """Protocol、Port参数

    """

    def __init__(self):
        r"""
        :param _Protocol: 协议（tcp；udp）
        :type Protocol: str
        :param _Port: 端口
        :type Port: int
        """
        self._Protocol = None
        self._Port = None

    @property
    def Protocol(self):
        """协议（tcp；udp）
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        """端口
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyTypeInfo(AbstractModel):
    """转发类型

    """

    def __init__(self):
        r"""
        :param _ProxyPorts: 转发监听端口列表，端口取值1~65535
        :type ProxyPorts: list of int
        :param _ProxyType: 转发协议，取值[
http(HTTP协议)
https(HTTPS协议)
]
        :type ProxyType: str
        """
        self._ProxyPorts = None
        self._ProxyType = None

    @property
    def ProxyPorts(self):
        """转发监听端口列表，端口取值1~65535
        :rtype: list of int
        """
        return self._ProxyPorts

    @ProxyPorts.setter
    def ProxyPorts(self, ProxyPorts):
        self._ProxyPorts = ProxyPorts

    @property
    def ProxyType(self):
        """转发协议，取值[
http(HTTP协议)
https(HTTPS协议)
]
        :rtype: str
        """
        return self._ProxyType

    @ProxyType.setter
    def ProxyType(self, ProxyType):
        self._ProxyType = ProxyType


    def _deserialize(self, params):
        self._ProxyPorts = params.get("ProxyPorts")
        self._ProxyType = params.get("ProxyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionInfo(AbstractModel):
    """地域信息

    """

    def __init__(self):
        r"""
        :param _Region: 地域名称，例如，ap-guangzhou
        :type Region: str
        """
        self._Region = None

    @property
    def Region(self):
        """地域名称，例如，ap-guangzhou
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInstanceRelation(AbstractModel):
    """四七层规则对应实例与IP的关系

    """

    def __init__(self):
        r"""
        :param _EipList: 资源实例的IP
        :type EipList: list of str
        :param _InstanceId: 资源实例的ID
        :type InstanceId: str
        :param _Cname: 资源实例的Cname
        :type Cname: str
        """
        self._EipList = None
        self._InstanceId = None
        self._Cname = None

    @property
    def EipList(self):
        """资源实例的IP
        :rtype: list of str
        """
        return self._EipList

    @EipList.setter
    def EipList(self, EipList):
        self._EipList = EipList

    @property
    def InstanceId(self):
        """资源实例的ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Cname(self):
        """资源实例的Cname
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname


    def _deserialize(self, params):
        self._EipList = params.get("EipList")
        self._InstanceId = params.get("InstanceId")
        self._Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchedulingDomainInfo(AbstractModel):
    """调度域名信息

    """

    def __init__(self):
        r"""
        :param _Domain: 调度域名
        :type Domain: str
        :param _LineIPList: 线路IP列表
        :type LineIPList: list of IPLineInfo
        :param _Method: 调度方式，当前仅支持优先级的方式，取值[priority]
        :type Method: str
        :param _TTL: 调度域名解析记录的TTL值
        :type TTL: int
        :param _Status: 运行状态，取值[
0：未运行
1：运行中
2：运行异常
]
        :type Status: int
        :param _CreatedTime: 创建时间
        :type CreatedTime: str
        :param _ModifyTime: 最后修改时间
        :type ModifyTime: str
        :param _UsrDomainName: 域名名称
        :type UsrDomainName: str
        """
        self._Domain = None
        self._LineIPList = None
        self._Method = None
        self._TTL = None
        self._Status = None
        self._CreatedTime = None
        self._ModifyTime = None
        self._UsrDomainName = None

    @property
    def Domain(self):
        """调度域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def LineIPList(self):
        """线路IP列表
        :rtype: list of IPLineInfo
        """
        return self._LineIPList

    @LineIPList.setter
    def LineIPList(self, LineIPList):
        self._LineIPList = LineIPList

    @property
    def Method(self):
        """调度方式，当前仅支持优先级的方式，取值[priority]
        :rtype: str
        """
        return self._Method

    @Method.setter
    def Method(self, Method):
        self._Method = Method

    @property
    def TTL(self):
        """调度域名解析记录的TTL值
        :rtype: int
        """
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def Status(self):
        """运行状态，取值[
0：未运行
1：运行中
2：运行异常
]
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreatedTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreatedTime

    @CreatedTime.setter
    def CreatedTime(self, CreatedTime):
        self._CreatedTime = CreatedTime

    @property
    def ModifyTime(self):
        """最后修改时间
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def UsrDomainName(self):
        """域名名称
        :rtype: str
        """
        return self._UsrDomainName

    @UsrDomainName.setter
    def UsrDomainName(self, UsrDomainName):
        self._UsrDomainName = UsrDomainName


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("LineIPList") is not None:
            self._LineIPList = []
            for item in params.get("LineIPList"):
                obj = IPLineInfo()
                obj._deserialize(item)
                self._LineIPList.append(obj)
        self._Method = params.get("Method")
        self._TTL = params.get("TTL")
        self._Status = params.get("Status")
        self._CreatedTime = params.get("CreatedTime")
        self._ModifyTime = params.get("ModifyTime")
        self._UsrDomainName = params.get("UsrDomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SourceServer(AbstractModel):
    """源站信息

    """

    def __init__(self):
        r"""
        :param _RealServer: 源站的地址（IP或者域名）
        :type RealServer: str
        :param _RsType: 源站的地址类型，取值[
1(域名地址)
2(IP地址)
]
        :type RsType: int
        :param _Weight: 源站的回源权重，取值1~100
        :type Weight: int
        :param _Port: 端口号：0~65535
        :type Port: int
        """
        self._RealServer = None
        self._RsType = None
        self._Weight = None
        self._Port = None

    @property
    def RealServer(self):
        """源站的地址（IP或者域名）
        :rtype: str
        """
        return self._RealServer

    @RealServer.setter
    def RealServer(self, RealServer):
        self._RealServer = RealServer

    @property
    def RsType(self):
        """源站的地址类型，取值[
1(域名地址)
2(IP地址)
]
        :rtype: int
        """
        return self._RsType

    @RsType.setter
    def RsType(self, RsType):
        self._RsType = RsType

    @property
    def Weight(self):
        """源站的回源权重，取值1~100
        :rtype: int
        """
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def Port(self):
        """端口号：0~65535
        :rtype: int
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._RealServer = params.get("RealServer")
        self._RsType = params.get("RsType")
        self._Weight = params.get("Weight")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpeedValue(AbstractModel):
    """限速值类型，例如：包速率pps、带宽bps

    """

    def __init__(self):
        r"""
        :param _Type: 限速值类型，取值[
1(包速率pps)
2(带宽bps)
]
        :type Type: int
        :param _Value: 值大小
        :type Value: int
        """
        self._Type = None
        self._Value = None

    @property
    def Type(self):
        """限速值类型，取值[
1(包速率pps)
2(带宽bps)
]
        :rtype: int
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Value(self):
        """值大小
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StaticPackRelation(AbstractModel):
    """三网高防套餐详情

    """

    def __init__(self):
        r"""
        :param _ProtectBandwidth: 保底带宽
        :type ProtectBandwidth: int
        :param _NormalBandwidth: 业务带宽
        :type NormalBandwidth: int
        :param _ForwardRulesLimit: 转发规则
        :type ForwardRulesLimit: int
        :param _AutoRenewFlag: 自动续费标记
        :type AutoRenewFlag: int
        :param _CurDeadline: 到期时间
        :type CurDeadline: str
        """
        self._ProtectBandwidth = None
        self._NormalBandwidth = None
        self._ForwardRulesLimit = None
        self._AutoRenewFlag = None
        self._CurDeadline = None

    @property
    def ProtectBandwidth(self):
        """保底带宽
        :rtype: int
        """
        return self._ProtectBandwidth

    @ProtectBandwidth.setter
    def ProtectBandwidth(self, ProtectBandwidth):
        self._ProtectBandwidth = ProtectBandwidth

    @property
    def NormalBandwidth(self):
        """业务带宽
        :rtype: int
        """
        return self._NormalBandwidth

    @NormalBandwidth.setter
    def NormalBandwidth(self, NormalBandwidth):
        self._NormalBandwidth = NormalBandwidth

    @property
    def ForwardRulesLimit(self):
        """转发规则
        :rtype: int
        """
        return self._ForwardRulesLimit

    @ForwardRulesLimit.setter
    def ForwardRulesLimit(self, ForwardRulesLimit):
        self._ForwardRulesLimit = ForwardRulesLimit

    @property
    def AutoRenewFlag(self):
        """自动续费标记
        :rtype: int
        """
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag

    @property
    def CurDeadline(self):
        """到期时间
        :rtype: str
        """
        return self._CurDeadline

    @CurDeadline.setter
    def CurDeadline(self, CurDeadline):
        self._CurDeadline = CurDeadline


    def _deserialize(self, params):
        self._ProtectBandwidth = params.get("ProtectBandwidth")
        self._NormalBandwidth = params.get("NormalBandwidth")
        self._ForwardRulesLimit = params.get("ForwardRulesLimit")
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        self._CurDeadline = params.get("CurDeadline")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SuccessCode(AbstractModel):
    """操作返回码，只用于返回成功的情况

    """

    def __init__(self):
        r"""
        :param _Message: 描述
        :type Message: str
        :param _Code: 成功/错误码
        :type Code: str
        """
        self._Message = None
        self._Code = None

    @property
    def Message(self):
        """描述
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def Code(self):
        """成功/错误码
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Message = params.get("Message")
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchWaterPrintConfigRequest(AbstractModel):
    """SwitchWaterPrintConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceId: 资源实例ID
        :type InstanceId: str
        :param _OpenStatus: 水印开启/关闭状态，1表示开启；0表示关闭
        :type OpenStatus: int
        :param _CloudSdkProxy: 是否开启代理，1开启则忽略IP+端口校验；0关闭则需要IP+端口校验
        :type CloudSdkProxy: int
        """
        self._InstanceId = None
        self._OpenStatus = None
        self._CloudSdkProxy = None

    @property
    def InstanceId(self):
        """资源实例ID
        :rtype: str
        """
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def OpenStatus(self):
        """水印开启/关闭状态，1表示开启；0表示关闭
        :rtype: int
        """
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def CloudSdkProxy(self):
        """是否开启代理，1开启则忽略IP+端口校验；0关闭则需要IP+端口校验
        :rtype: int
        """
        return self._CloudSdkProxy

    @CloudSdkProxy.setter
    def CloudSdkProxy(self, CloudSdkProxy):
        self._CloudSdkProxy = CloudSdkProxy


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._OpenStatus = params.get("OpenStatus")
        self._CloudSdkProxy = params.get("CloudSdkProxy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SwitchWaterPrintConfigResponse(AbstractModel):
    """SwitchWaterPrintConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class TagFilter(AbstractModel):
    """标签类型

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签键值列表
        :type TagValue: list of str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签键值列表
        :rtype: list of str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagInfo(AbstractModel):
    """标签信息，用于资源列表返回关联的标签

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
        :type TagKey: str
        :param _TagValue: 标签值
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
        :rtype: str
        """
        return self._TagValue

    @TagValue.setter
    def TagValue(self, TagValue):
        self._TagValue = TagValue


    def _deserialize(self, params):
        self._TagKey = params.get("TagKey")
        self._TagValue = params.get("TagValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintConfig(AbstractModel):
    """水印防护配置

    """

    def __init__(self):
        r"""
        :param _Offset: 水印偏移量，取值范围[0, 100)
        :type Offset: int
        :param _OpenStatus: 是否开启，取值[
0（手动开启）
1（立即运行）
]
        :type OpenStatus: int
        :param _Listeners: 水印所属的转发监听器列表
        :type Listeners: list of ForwardListener
        :param _Keys: 水印添加成功后生成的水印密钥列表，一条水印最少1个密钥，最多2个密钥
        :type Keys: list of WaterPrintKey
        :param _Verify: 水印检查模式, 取值[
checkall（普通模式）
shortfpcheckall（精简模式）
]
        :type Verify: str
        :param _CloudSdkProxy: 是否开启代理，1开启则忽略IP+端口校验；0关闭则需要IP+端口校验
        :type CloudSdkProxy: int
        """
        self._Offset = None
        self._OpenStatus = None
        self._Listeners = None
        self._Keys = None
        self._Verify = None
        self._CloudSdkProxy = None

    @property
    def Offset(self):
        """水印偏移量，取值范围[0, 100)
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def OpenStatus(self):
        """是否开启，取值[
0（手动开启）
1（立即运行）
]
        :rtype: int
        """
        return self._OpenStatus

    @OpenStatus.setter
    def OpenStatus(self, OpenStatus):
        self._OpenStatus = OpenStatus

    @property
    def Listeners(self):
        """水印所属的转发监听器列表
        :rtype: list of ForwardListener
        """
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners

    @property
    def Keys(self):
        """水印添加成功后生成的水印密钥列表，一条水印最少1个密钥，最多2个密钥
        :rtype: list of WaterPrintKey
        """
        return self._Keys

    @Keys.setter
    def Keys(self, Keys):
        self._Keys = Keys

    @property
    def Verify(self):
        """水印检查模式, 取值[
checkall（普通模式）
shortfpcheckall（精简模式）
]
        :rtype: str
        """
        return self._Verify

    @Verify.setter
    def Verify(self, Verify):
        self._Verify = Verify

    @property
    def CloudSdkProxy(self):
        """是否开启代理，1开启则忽略IP+端口校验；0关闭则需要IP+端口校验
        :rtype: int
        """
        return self._CloudSdkProxy

    @CloudSdkProxy.setter
    def CloudSdkProxy(self, CloudSdkProxy):
        self._CloudSdkProxy = CloudSdkProxy


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._OpenStatus = params.get("OpenStatus")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ForwardListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        if params.get("Keys") is not None:
            self._Keys = []
            for item in params.get("Keys"):
                obj = WaterPrintKey()
                obj._deserialize(item)
                self._Keys.append(obj)
        self._Verify = params.get("Verify")
        self._CloudSdkProxy = params.get("CloudSdkProxy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintKey(AbstractModel):
    """生成的水印密钥

    """

    def __init__(self):
        r"""
        :param _KeyVersion: 密钥版本号
        :type KeyVersion: str
        :param _KeyContent: 密钥内容
        :type KeyContent: str
        :param _KeyId: 密钥ID
        :type KeyId: str
        :param _KeyOpenStatus: 密钥启用状态，只有一个取值1(启用)
        :type KeyOpenStatus: int
        :param _CreateTime: 密钥生成时间
        :type CreateTime: str
        """
        self._KeyVersion = None
        self._KeyContent = None
        self._KeyId = None
        self._KeyOpenStatus = None
        self._CreateTime = None

    @property
    def KeyVersion(self):
        """密钥版本号
        :rtype: str
        """
        return self._KeyVersion

    @KeyVersion.setter
    def KeyVersion(self, KeyVersion):
        self._KeyVersion = KeyVersion

    @property
    def KeyContent(self):
        """密钥内容
        :rtype: str
        """
        return self._KeyContent

    @KeyContent.setter
    def KeyContent(self, KeyContent):
        self._KeyContent = KeyContent

    @property
    def KeyId(self):
        """密钥ID
        :rtype: str
        """
        return self._KeyId

    @KeyId.setter
    def KeyId(self, KeyId):
        self._KeyId = KeyId

    @property
    def KeyOpenStatus(self):
        """密钥启用状态，只有一个取值1(启用)
        :rtype: int
        """
        return self._KeyOpenStatus

    @KeyOpenStatus.setter
    def KeyOpenStatus(self, KeyOpenStatus):
        self._KeyOpenStatus = KeyOpenStatus

    @property
    def CreateTime(self):
        """密钥生成时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._KeyVersion = params.get("KeyVersion")
        self._KeyContent = params.get("KeyContent")
        self._KeyId = params.get("KeyId")
        self._KeyOpenStatus = params.get("KeyOpenStatus")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WaterPrintRelation(AbstractModel):
    """水印配置相关信息

    """

    def __init__(self):
        r"""
        :param _WaterPrintConfig: 水印配置
        :type WaterPrintConfig: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        :param _InstanceDetailList: 水印配置所属的资源实例
        :type InstanceDetailList: list of InstanceRelation
        """
        self._WaterPrintConfig = None
        self._InstanceDetailList = None

    @property
    def WaterPrintConfig(self):
        """水印配置
        :rtype: :class:`tencentcloud.antiddos.v20200309.models.WaterPrintConfig`
        """
        return self._WaterPrintConfig

    @WaterPrintConfig.setter
    def WaterPrintConfig(self, WaterPrintConfig):
        self._WaterPrintConfig = WaterPrintConfig

    @property
    def InstanceDetailList(self):
        """水印配置所属的资源实例
        :rtype: list of InstanceRelation
        """
        return self._InstanceDetailList

    @InstanceDetailList.setter
    def InstanceDetailList(self, InstanceDetailList):
        self._InstanceDetailList = InstanceDetailList


    def _deserialize(self, params):
        if params.get("WaterPrintConfig") is not None:
            self._WaterPrintConfig = WaterPrintConfig()
            self._WaterPrintConfig._deserialize(params.get("WaterPrintConfig"))
        if params.get("InstanceDetailList") is not None:
            self._InstanceDetailList = []
            for item in params.get("InstanceDetailList"):
                obj = InstanceRelation()
                obj._deserialize(item)
                self._InstanceDetailList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        