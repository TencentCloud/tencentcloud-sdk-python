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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Account(AbstractModel):
    r"""账号基本信息，主要有 Uin 和 AppId

    """

    def __init__(self):
        r"""
        :param _AppId: 租户appid
        :type AppId: str
        :param _Uin: 租户uin
        :type Uin: str
        :param _RemainQuota: 剩余可用额度
        :type RemainQuota: int
        :param _Nickname: 租户名称
        :type Nickname: str
        :param _DispatchRuleNum: 下发规则数
        :type DispatchRuleNum: int
        :param _OriginRuleNum: 产品已有规则数
        :type OriginRuleNum: int
        :param _TotalQuota: 总额度
        :type TotalQuota: int
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._AppId = None
        self._Uin = None
        self._RemainQuota = None
        self._Nickname = None
        self._DispatchRuleNum = None
        self._OriginRuleNum = None
        self._TotalQuota = None
        self._MemberId = None

    @property
    def AppId(self):
        r"""租户appid
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""租户uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def RemainQuota(self):
        r"""剩余可用额度
        :rtype: int
        """
        return self._RemainQuota

    @RemainQuota.setter
    def RemainQuota(self, RemainQuota):
        self._RemainQuota = RemainQuota

    @property
    def Nickname(self):
        r"""租户名称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def DispatchRuleNum(self):
        r"""下发规则数
        :rtype: int
        """
        return self._DispatchRuleNum

    @DispatchRuleNum.setter
    def DispatchRuleNum(self, DispatchRuleNum):
        self._DispatchRuleNum = DispatchRuleNum

    @property
    def OriginRuleNum(self):
        r"""产品已有规则数
        :rtype: int
        """
        return self._OriginRuleNum

    @OriginRuleNum.setter
    def OriginRuleNum(self, OriginRuleNum):
        self._OriginRuleNum = OriginRuleNum

    @property
    def TotalQuota(self):
        r"""总额度
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._RemainQuota = params.get("RemainQuota")
        self._Nickname = params.get("Nickname")
        self._DispatchRuleNum = params.get("DispatchRuleNum")
        self._OriginRuleNum = params.get("OriginRuleNum")
        self._TotalQuota = params.get("TotalQuota")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountGroupInfo(AbstractModel):
    r"""账户组信息

    """

    def __init__(self):
        r"""
        :param _GroupId: 账户组ID
        :type GroupId: str
        :param _GroupName: 账户组名称
        :type GroupName: str
        """
        self._GroupId = None
        self._GroupName = None

    @property
    def GroupId(self):
        r"""账户组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""账户组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountGroupQuotaDetail(AbstractModel):
    r"""账号组配额详情

    """

    def __init__(self):
        r"""
        :param _GroupId: 账号组Id
        :type GroupId: str
        :param _GroupName: 账号组名称
        :type GroupName: str
        :param _MemberCount: 账号组成员数
        :type MemberCount: int
        :param _RemainQuota: 取组内 RemainQuota 最小成员的值
        :type RemainQuota: int
        :param _TotalQuota: 同上成员的 TotalQuota
        :type TotalQuota: int
        :param _DispatchRuleNum: 同上成员的 DispatchRuleNum
        :type DispatchRuleNum: int
        :param _OriginRuleNum: 同上成员的 OriginRuleNum
        :type OriginRuleNum: int
        :param _BottleneckUin: 配额最少的成员 Uin
        :type BottleneckUin: str
        :param _Members: 成员列表
        :type Members: list of Account
        """
        self._GroupId = None
        self._GroupName = None
        self._MemberCount = None
        self._RemainQuota = None
        self._TotalQuota = None
        self._DispatchRuleNum = None
        self._OriginRuleNum = None
        self._BottleneckUin = None
        self._Members = None

    @property
    def GroupId(self):
        r"""账号组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""账号组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def MemberCount(self):
        r"""账号组成员数
        :rtype: int
        """
        return self._MemberCount

    @MemberCount.setter
    def MemberCount(self, MemberCount):
        self._MemberCount = MemberCount

    @property
    def RemainQuota(self):
        r"""取组内 RemainQuota 最小成员的值
        :rtype: int
        """
        return self._RemainQuota

    @RemainQuota.setter
    def RemainQuota(self, RemainQuota):
        self._RemainQuota = RemainQuota

    @property
    def TotalQuota(self):
        r"""同上成员的 TotalQuota
        :rtype: int
        """
        return self._TotalQuota

    @TotalQuota.setter
    def TotalQuota(self, TotalQuota):
        self._TotalQuota = TotalQuota

    @property
    def DispatchRuleNum(self):
        r"""同上成员的 DispatchRuleNum
        :rtype: int
        """
        return self._DispatchRuleNum

    @DispatchRuleNum.setter
    def DispatchRuleNum(self, DispatchRuleNum):
        self._DispatchRuleNum = DispatchRuleNum

    @property
    def OriginRuleNum(self):
        r"""同上成员的 OriginRuleNum
        :rtype: int
        """
        return self._OriginRuleNum

    @OriginRuleNum.setter
    def OriginRuleNum(self, OriginRuleNum):
        self._OriginRuleNum = OriginRuleNum

    @property
    def BottleneckUin(self):
        r"""配额最少的成员 Uin
        :rtype: str
        """
        return self._BottleneckUin

    @BottleneckUin.setter
    def BottleneckUin(self, BottleneckUin):
        self._BottleneckUin = BottleneckUin

    @property
    def Members(self):
        r"""成员列表
        :rtype: list of Account
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._MemberCount = params.get("MemberCount")
        self._RemainQuota = params.get("RemainQuota")
        self._TotalQuota = params.get("TotalQuota")
        self._DispatchRuleNum = params.get("DispatchRuleNum")
        self._OriginRuleNum = params.get("OriginRuleNum")
        self._BottleneckUin = params.get("BottleneckUin")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = Account()
                obj._deserialize(item)
                self._Members.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountProductDetailStats(AbstractModel):
    r"""单个产品的风险统计详情

    """

    def __init__(self):
        r"""
        :param _Product: 产品类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Product: str
        :param _ProductName: 产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductName: str
        :param _PolicyCount: 体检策略数
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyCount: int
        :param _UntreatedRiskCount: 待整改风险数
注意：此字段可能返回 null，表示取不到有效值。
        :type UntreatedRiskCount: int
        :param _TotalRiskCount: 总风险数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalRiskCount: int
        :param _TreatedRiskCount: 已处置数
注意：此字段可能返回 null，表示取不到有效值。
        :type TreatedRiskCount: int
        :param _IgnoredRiskCount: 已忽略数
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoredRiskCount: int
        :param _RectifyRate: 整改率，如 50%，无需整改时为 无需整改
注意：此字段可能返回 null，表示取不到有效值。
        :type RectifyRate: str
        :param _LastCheckTime: 最近一次体检时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastCheckTime: str
        :param _SubcategoryIds: 子类 ID 列表
        :type SubcategoryIds: list of str
        :param _IsOverdue: 是否超时未体检
        :type IsOverdue: bool
        """
        self._Product = None
        self._ProductName = None
        self._PolicyCount = None
        self._UntreatedRiskCount = None
        self._TotalRiskCount = None
        self._TreatedRiskCount = None
        self._IgnoredRiskCount = None
        self._RectifyRate = None
        self._LastCheckTime = None
        self._SubcategoryIds = None
        self._IsOverdue = None

    @property
    def Product(self):
        r"""产品类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ProductName(self):
        r"""产品名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductName

    @ProductName.setter
    def ProductName(self, ProductName):
        self._ProductName = ProductName

    @property
    def PolicyCount(self):
        r"""体检策略数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyCount

    @PolicyCount.setter
    def PolicyCount(self, PolicyCount):
        self._PolicyCount = PolicyCount

    @property
    def UntreatedRiskCount(self):
        r"""待整改风险数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UntreatedRiskCount

    @UntreatedRiskCount.setter
    def UntreatedRiskCount(self, UntreatedRiskCount):
        self._UntreatedRiskCount = UntreatedRiskCount

    @property
    def TotalRiskCount(self):
        r"""总风险数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalRiskCount

    @TotalRiskCount.setter
    def TotalRiskCount(self, TotalRiskCount):
        self._TotalRiskCount = TotalRiskCount

    @property
    def TreatedRiskCount(self):
        r"""已处置数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TreatedRiskCount

    @TreatedRiskCount.setter
    def TreatedRiskCount(self, TreatedRiskCount):
        self._TreatedRiskCount = TreatedRiskCount

    @property
    def IgnoredRiskCount(self):
        r"""已忽略数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IgnoredRiskCount

    @IgnoredRiskCount.setter
    def IgnoredRiskCount(self, IgnoredRiskCount):
        self._IgnoredRiskCount = IgnoredRiskCount

    @property
    def RectifyRate(self):
        r"""整改率，如 50%，无需整改时为 无需整改
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RectifyRate

    @RectifyRate.setter
    def RectifyRate(self, RectifyRate):
        self._RectifyRate = RectifyRate

    @property
    def LastCheckTime(self):
        r"""最近一次体检时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastCheckTime

    @LastCheckTime.setter
    def LastCheckTime(self, LastCheckTime):
        self._LastCheckTime = LastCheckTime

    @property
    def SubcategoryIds(self):
        r"""子类 ID 列表
        :rtype: list of str
        """
        return self._SubcategoryIds

    @SubcategoryIds.setter
    def SubcategoryIds(self, SubcategoryIds):
        self._SubcategoryIds = SubcategoryIds

    @property
    def IsOverdue(self):
        r"""是否超时未体检
        :rtype: bool
        """
        return self._IsOverdue

    @IsOverdue.setter
    def IsOverdue(self, IsOverdue):
        self._IsOverdue = IsOverdue


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ProductName = params.get("ProductName")
        self._PolicyCount = params.get("PolicyCount")
        self._UntreatedRiskCount = params.get("UntreatedRiskCount")
        self._TotalRiskCount = params.get("TotalRiskCount")
        self._TreatedRiskCount = params.get("TreatedRiskCount")
        self._IgnoredRiskCount = params.get("IgnoredRiskCount")
        self._RectifyRate = params.get("RectifyRate")
        self._LastCheckTime = params.get("LastCheckTime")
        self._SubcategoryIds = params.get("SubcategoryIds")
        self._IsOverdue = params.get("IsOverdue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountStatsGroup(AbstractModel):
    r"""按账号分组的风险统计数据

    """

    def __init__(self):
        r"""
        :param _Member: 成员账号信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Member: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        :param _UntreatedRiskCount: 该账号下所有产品待整改风险数汇总
注意：此字段可能返回 null，表示取不到有效值。
        :type UntreatedRiskCount: int
        :param _ProductStats: 该账号下各产品维度的风险统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductStats: list of AccountProductDetailStats
        :param _RectifyRate: 整改率
        :type RectifyRate: str
        """
        self._Member = None
        self._UntreatedRiskCount = None
        self._ProductStats = None
        self._RectifyRate = None

    @property
    def Member(self):
        r"""成员账号信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._Member

    @Member.setter
    def Member(self, Member):
        self._Member = Member

    @property
    def UntreatedRiskCount(self):
        r"""该账号下所有产品待整改风险数汇总
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UntreatedRiskCount

    @UntreatedRiskCount.setter
    def UntreatedRiskCount(self, UntreatedRiskCount):
        self._UntreatedRiskCount = UntreatedRiskCount

    @property
    def ProductStats(self):
        r"""该账号下各产品维度的风险统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AccountProductDetailStats
        """
        return self._ProductStats

    @ProductStats.setter
    def ProductStats(self, ProductStats):
        self._ProductStats = ProductStats

    @property
    def RectifyRate(self):
        r"""整改率
        :rtype: str
        """
        return self._RectifyRate

    @RectifyRate.setter
    def RectifyRate(self, RectifyRate):
        self._RectifyRate = RectifyRate


    def _deserialize(self, params):
        if params.get("Member") is not None:
            self._Member = MemberInfo()
            self._Member._deserialize(params.get("Member"))
        self._UntreatedRiskCount = params.get("UntreatedRiskCount")
        if params.get("ProductStats") is not None:
            self._ProductStats = []
            for item in params.get("ProductStats"):
                obj = AccountProductDetailStats()
                obj._deserialize(item)
                self._ProductStats.append(obj)
        self._RectifyRate = params.get("RectifyRate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddressTemplateSpecification(AbstractModel):
    r"""安全组地址模板

    """

    def __init__(self):
        r"""
        :param _AddressId: IP地址ID，例如：ipm-2uw6ujo6。
        :type AddressId: str
        :param _AddressGroupId:  IP地址组ID，例如：ipmg-2uw6ujo6。
        :type AddressGroupId: str
        """
        self._AddressId = None
        self._AddressGroupId = None

    @property
    def AddressId(self):
        r"""IP地址ID，例如：ipm-2uw6ujo6。
        :rtype: str
        """
        return self._AddressId

    @AddressId.setter
    def AddressId(self, AddressId):
        self._AddressId = AddressId

    @property
    def AddressGroupId(self):
        r""" IP地址组ID，例如：ipmg-2uw6ujo6。
        :rtype: str
        """
        return self._AddressGroupId

    @AddressGroupId.setter
    def AddressGroupId(self, AddressGroupId):
        self._AddressGroupId = AddressGroupId


    def _deserialize(self, params):
        self._AddressId = params.get("AddressId")
        self._AddressGroupId = params.get("AddressGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AnalysisSgRuleInfoResp(AbstractModel):
    r"""企业安全组规则列表信息

    """

    def __init__(self):
        r"""
        :param _Id: <p>规则id  等同RuleUuid</p>
        :type Id: int
        :param _RuleId: <p>规则Id</p>
        :type RuleId: str
        :param _OrderIndex: <p>排序</p>
        :type OrderIndex: int
        :param _CfwOrderIndex: <p>云防排序</p>
        :type CfwOrderIndex: int
        :param _SourceId: <p>源规则内容</p>
        :type SourceId: str
        :param _SourceType: <p>源规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)</p><p>枚举值：</p><ul><li>0： IP / CIDR</li><li>1： VPC 实例</li><li>2： 子网 </li><li>3： CVM 实例</li><li>4： CLB 实例</li><li>5： ENI（弹性网卡）实例</li><li>6： CDB（云数据库）实例</li><li>7： 参数模板</li><li>8： 标签</li><li>9： 地域</li></ul>
        :type SourceType: int
        :param _TargetId: <p>目的规则内容</p>
        :type TargetId: str
        :param _TargetType: <p>目的规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9/100<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)<br>100表示资产分组(resourcegroup)</p><p>枚举值：</p><ul><li>0： IP / CIDR</li><li>1： VPC 实例</li><li>2： 子网 </li><li>3： CVM 实例</li><li>4： CLB 实例</li><li>5： ENI（弹性网卡）实例</li><li>6： CDB（云数据库）实例</li><li>7： 参数模板</li><li>8： 标签</li><li>9： 地域</li></ul>
        :type TargetType: int
        :param _Protocol: <p>协议名称<br>取值范围:TCP/ANY/ICMP/UDP<br>ANY:表示所有</p>
        :type Protocol: str
        :param _Port: <p>端口</p>
        :type Port: str
        :param _Strategy: <p>规则策略<br>取值范围:1/2<br>1:阻断<br>2:放行</p>
        :type Strategy: int
        :param _Detail: <p>描述</p>
        :type Detail: str
        :param _Region: <p>地域</p>
        :type Region: str
        :param _ServiceTemplateId: <p>服务模板id</p>
        :type ServiceTemplateId: str
        :param _SouInstanceName: <p>源资产名称</p>
        :type SouInstanceName: str
        :param _SouPublicIp: <p>源资产公网ip</p>
        :type SouPublicIp: str
        :param _SouPrivateIp: <p>源资产内网ip</p>
        :type SouPrivateIp: str
        :param _SouCidr: <p>源资产网段信息</p>
        :type SouCidr: str
        :param _SouParameterName: <p>源模板名称</p>
        :type SouParameterName: str
        :param _InstanceName: <p>目的资产名称</p>
        :type InstanceName: str
        :param _PublicIp: <p>目的资产公网ip</p>
        :type PublicIp: str
        :param _PrivateIp: <p>目的资产内网ip</p>
        :type PrivateIp: str
        :param _Cidr: <p>目的资产网段信息</p>
        :type Cidr: str
        :param _ParameterName: <p>目的模板名称</p>
        :type ParameterName: str
        :param _ProtocolPortName: <p>端口模板名称</p>
        :type ProtocolPortName: str
        :param _DnsParseCount: <p>域名解析的IP统计</p>
        :type DnsParseCount: :class:`tencentcloud.fwm.v20250611.models.SgDnsParseCount`
        :param _Scope: <p>规则生效范围</p>
        :type Scope: str
        :param _RulePartition: <p>分区：<br>1防火墙管理最前分区<br>2是云防规则<br>3防火墙管理最后分区</p>
        :type RulePartition: int
        :param _GroupId: <p>规则组Id</p>
        :type GroupId: str
        :param _GroupName: <p>规则组名称</p>
        :type GroupName: str
        :param _GroupRuleId: <p>规则组内规则id</p>
        :type GroupRuleId: str
        :param _StrategyId: <p>策略Id</p>
        :type StrategyId: str
        :param _IpVersion: <p>ip类型</p>
        :type IpVersion: str
        :param _BelongMember: <p>成员信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongMember: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        self._Id = None
        self._RuleId = None
        self._OrderIndex = None
        self._CfwOrderIndex = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Detail = None
        self._Region = None
        self._ServiceTemplateId = None
        self._SouInstanceName = None
        self._SouPublicIp = None
        self._SouPrivateIp = None
        self._SouCidr = None
        self._SouParameterName = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ParameterName = None
        self._ProtocolPortName = None
        self._DnsParseCount = None
        self._Scope = None
        self._RulePartition = None
        self._GroupId = None
        self._GroupName = None
        self._GroupRuleId = None
        self._StrategyId = None
        self._IpVersion = None
        self._BelongMember = None

    @property
    def Id(self):
        r"""<p>规则id  等同RuleUuid</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RuleId(self):
        r"""<p>规则Id</p>
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def OrderIndex(self):
        r"""<p>排序</p>
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def CfwOrderIndex(self):
        r"""<p>云防排序</p>
        :rtype: int
        """
        return self._CfwOrderIndex

    @CfwOrderIndex.setter
    def CfwOrderIndex(self, CfwOrderIndex):
        self._CfwOrderIndex = CfwOrderIndex

    @property
    def SourceId(self):
        r"""<p>源规则内容</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        r"""<p>源规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)</p><p>枚举值：</p><ul><li>0： IP / CIDR</li><li>1： VPC 实例</li><li>2： 子网 </li><li>3： CVM 实例</li><li>4： CLB 实例</li><li>5： ENI（弹性网卡）实例</li><li>6： CDB（云数据库）实例</li><li>7： 参数模板</li><li>8： 标签</li><li>9： 地域</li></ul>
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        r"""<p>目的规则内容</p>
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        r"""<p>目的规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9/100<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)<br>100表示资产分组(resourcegroup)</p><p>枚举值：</p><ul><li>0： IP / CIDR</li><li>1： VPC 实例</li><li>2： 子网 </li><li>3： CVM 实例</li><li>4： CLB 实例</li><li>5： ENI（弹性网卡）实例</li><li>6： CDB（云数据库）实例</li><li>7： 参数模板</li><li>8： 标签</li><li>9： 地域</li></ul>
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        r"""<p>协议名称<br>取值范围:TCP/ANY/ICMP/UDP<br>ANY:表示所有</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""<p>端口</p>
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        r"""<p>规则策略<br>取值范围:1/2<br>1:阻断<br>2:放行</p>
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Detail(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Region(self):
        r"""<p>地域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ServiceTemplateId(self):
        r"""<p>服务模板id</p>
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def SouInstanceName(self):
        r"""<p>源资产名称</p>
        :rtype: str
        """
        return self._SouInstanceName

    @SouInstanceName.setter
    def SouInstanceName(self, SouInstanceName):
        self._SouInstanceName = SouInstanceName

    @property
    def SouPublicIp(self):
        r"""<p>源资产公网ip</p>
        :rtype: str
        """
        return self._SouPublicIp

    @SouPublicIp.setter
    def SouPublicIp(self, SouPublicIp):
        self._SouPublicIp = SouPublicIp

    @property
    def SouPrivateIp(self):
        r"""<p>源资产内网ip</p>
        :rtype: str
        """
        return self._SouPrivateIp

    @SouPrivateIp.setter
    def SouPrivateIp(self, SouPrivateIp):
        self._SouPrivateIp = SouPrivateIp

    @property
    def SouCidr(self):
        r"""<p>源资产网段信息</p>
        :rtype: str
        """
        return self._SouCidr

    @SouCidr.setter
    def SouCidr(self, SouCidr):
        self._SouCidr = SouCidr

    @property
    def SouParameterName(self):
        r"""<p>源模板名称</p>
        :rtype: str
        """
        return self._SouParameterName

    @SouParameterName.setter
    def SouParameterName(self, SouParameterName):
        self._SouParameterName = SouParameterName

    @property
    def InstanceName(self):
        r"""<p>目的资产名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        r"""<p>目的资产公网ip</p>
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""<p>目的资产内网ip</p>
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        r"""<p>目的资产网段信息</p>
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ParameterName(self):
        r"""<p>目的模板名称</p>
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ProtocolPortName(self):
        r"""<p>端口模板名称</p>
        :rtype: str
        """
        return self._ProtocolPortName

    @ProtocolPortName.setter
    def ProtocolPortName(self, ProtocolPortName):
        self._ProtocolPortName = ProtocolPortName

    @property
    def DnsParseCount(self):
        r"""<p>域名解析的IP统计</p>
        :rtype: :class:`tencentcloud.fwm.v20250611.models.SgDnsParseCount`
        """
        return self._DnsParseCount

    @DnsParseCount.setter
    def DnsParseCount(self, DnsParseCount):
        self._DnsParseCount = DnsParseCount

    @property
    def Scope(self):
        r"""<p>规则生效范围</p>
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def RulePartition(self):
        r"""<p>分区：<br>1防火墙管理最前分区<br>2是云防规则<br>3防火墙管理最后分区</p>
        :rtype: int
        """
        return self._RulePartition

    @RulePartition.setter
    def RulePartition(self, RulePartition):
        self._RulePartition = RulePartition

    @property
    def GroupId(self):
        r"""<p>规则组Id</p>
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""<p>规则组名称</p>
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupRuleId(self):
        r"""<p>规则组内规则id</p>
        :rtype: str
        """
        return self._GroupRuleId

    @GroupRuleId.setter
    def GroupRuleId(self, GroupRuleId):
        self._GroupRuleId = GroupRuleId

    @property
    def StrategyId(self):
        r"""<p>策略Id</p>
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def IpVersion(self):
        r"""<p>ip类型</p>
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def BelongMember(self):
        r"""<p>成员信息</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._BelongMember

    @BelongMember.setter
    def BelongMember(self, BelongMember):
        self._BelongMember = BelongMember


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RuleId = params.get("RuleId")
        self._OrderIndex = params.get("OrderIndex")
        self._CfwOrderIndex = params.get("CfwOrderIndex")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Detail = params.get("Detail")
        self._Region = params.get("Region")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._SouInstanceName = params.get("SouInstanceName")
        self._SouPublicIp = params.get("SouPublicIp")
        self._SouPrivateIp = params.get("SouPrivateIp")
        self._SouCidr = params.get("SouCidr")
        self._SouParameterName = params.get("SouParameterName")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ParameterName = params.get("ParameterName")
        self._ProtocolPortName = params.get("ProtocolPortName")
        if params.get("DnsParseCount") is not None:
            self._DnsParseCount = SgDnsParseCount()
            self._DnsParseCount._deserialize(params.get("DnsParseCount"))
        self._Scope = params.get("Scope")
        self._RulePartition = params.get("RulePartition")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._GroupRuleId = params.get("GroupRuleId")
        self._StrategyId = params.get("StrategyId")
        self._IpVersion = params.get("IpVersion")
        if params.get("BelongMember") is not None:
            self._BelongMember = MemberInfo()
            self._BelongMember._deserialize(params.get("BelongMember"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelIgnorePolicyRiskRequest(AbstractModel):
    r"""CancelIgnorePolicyRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskId: 风险ID
        :type RiskId: str
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._RiskId = None
        self._MemberId = None

    @property
    def RiskId(self):
        r"""风险ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelIgnorePolicyRiskResponse(AbstractModel):
    r"""CancelIgnorePolicyRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CommonFilter(AbstractModel):
    r"""通用筛选条件

    """

    def __init__(self):
        r"""
        :param _Name: <p>筛选字段名。支持：SecurityGroupId、FwGroupId、IP（IP地址模糊搜索）、InstanceName（实例名称模糊搜索）、VpcId（VPC ID精确搜索）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Values: <p>筛选值列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        :param _OperatorType: <p>操作类型。1=等于，7=in，9=模糊匹配</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type OperatorType: int
        """
        self._Name = None
        self._Values = None
        self._OperatorType = None

    @property
    def Name(self):
        r"""<p>筛选字段名。支持：SecurityGroupId、FwGroupId、IP（IP地址模糊搜索）、InstanceName（实例名称模糊搜索）、VpcId（VPC ID精确搜索）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        r"""<p>筛选值列表</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def OperatorType(self):
        r"""<p>操作类型。1=等于，7=in，9=模糊匹配</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OperatorType

    @OperatorType.setter
    def OperatorType(self, OperatorType):
        self._OperatorType = OperatorType


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        self._OperatorType = params.get("OperatorType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnalyzePolicyTaskRequest(AbstractModel):
    r"""CreateAnalyzePolicyTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Products: 产品类型
        :type Products: list of str
        :param _MemberIdSet: 成员Id 列表
        :type MemberIdSet: list of str
        """
        self._Products = None
        self._MemberIdSet = None

    @property
    def Products(self):
        r"""产品类型
        :rtype: list of str
        """
        return self._Products

    @Products.setter
    def Products(self, Products):
        self._Products = Products

    @property
    def MemberIdSet(self):
        r"""成员Id 列表
        :rtype: list of str
        """
        return self._MemberIdSet

    @MemberIdSet.setter
    def MemberIdSet(self, MemberIdSet):
        self._MemberIdSet = MemberIdSet


    def _deserialize(self, params):
        self._Products = params.get("Products")
        self._MemberIdSet = params.get("MemberIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateAnalyzePolicyTaskResponse(AbstractModel):
    r"""CreateAnalyzePolicyTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 任务状态 ，1 表示执行中
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""任务状态 ，1 表示执行中
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CreateEdgeAclRuleGroupRequest(AbstractModel):
    r"""CreateEdgeAclRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 规则组名称，长度1-50字符
        :type GroupName: str
        :param _Product: 产品类型，固定为 cfw_edge_acl
        :type Product: str
        :param _Rules: 规则列表
        :type Rules: list of EdgeAclRuleInfo
        """
        self._GroupName = None
        self._Product = None
        self._Rules = None

    @property
    def GroupName(self):
        r"""规则组名称，长度1-50字符
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Product(self):
        r"""产品类型，固定为 cfw_edge_acl
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of EdgeAclRuleInfo
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Product = params.get("Product")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = EdgeAclRuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeAclRuleGroupResponse(AbstractModel):
    r"""CreateEdgeAclRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建的规则组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""创建的规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateEdgeAclRuleRequest(AbstractModel):
    r"""CreateEdgeAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rules: 规则列表
        :type Rules: list of EdgeAclRuleInfo
        """
        self._GroupId = None
        self._Rules = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of EdgeAclRuleInfo
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = EdgeAclRuleInfo()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgeAclRuleResponse(AbstractModel):
    r"""CreateEdgeAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateNatAclRuleGroupRequest(AbstractModel):
    r"""CreateNatAclRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 规则组名称
        :type GroupName: str
        :param _Product: 产品类型，固定为 cfw_nat_acl
        :type Product: str
        :param _Rules: 规则列表
        :type Rules: list of NatAclRule
        """
        self._GroupName = None
        self._Product = None
        self._Rules = None

    @property
    def GroupName(self):
        r"""规则组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Product(self):
        r"""产品类型，固定为 cfw_nat_acl
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of NatAclRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Product = params.get("Product")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = NatAclRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatAclRuleGroupResponse(AbstractModel):
    r"""CreateNatAclRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建的规则组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""创建的规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateNatAclRuleRequest(AbstractModel):
    r"""CreateNatAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rules: 规则列表
        :type Rules: list of NatAclRule
        """
        self._GroupId = None
        self._Rules = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of NatAclRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = NatAclRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateNatAclRuleResponse(AbstractModel):
    r"""CreateNatAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateSecurityGroupRuleGroupRequest(AbstractModel):
    r"""CreateSecurityGroupRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 规则组ID
        :type GroupName: str
        :param _Product: 产品类型
        :type Product: str
        :param _Rules: 规则列表
        :type Rules: list of SecurityGroupRule
        """
        self._GroupName = None
        self._Product = None
        self._Rules = None

    @property
    def GroupName(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Product(self):
        r"""产品类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of SecurityGroupRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Product = params.get("Product")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRuleGroupResponse(AbstractModel):
    r"""CreateSecurityGroupRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建的规则组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""创建的规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateSecurityGroupRuleRequest(AbstractModel):
    r"""CreateSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _Rules: 规则列表
        :type Rules: list of SecurityGroupRule
        """
        self._GroupId = None
        self._Rules = None

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of SecurityGroupRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = SecurityGroupRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityGroupRuleResponse(AbstractModel):
    r"""CreateSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateStrategyRequest(AbstractModel):
    r"""CreateStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品类型
        :type Product: str
        :param _ReceiveAccount: 下发账号
        :type ReceiveAccount: list of str
        :param _PreStrategy: 前区规则组
        :type PreStrategy: list of StrategyReq
        :param _PostStrategy: 后区规则组
        :type PostStrategy: list of StrategyReq
        :param _ReceiveGroup: 下发账号组
        :type ReceiveGroup: list of str
        """
        self._Product = None
        self._ReceiveAccount = None
        self._PreStrategy = None
        self._PostStrategy = None
        self._ReceiveGroup = None

    @property
    def Product(self):
        r"""产品类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ReceiveAccount(self):
        r"""下发账号
        :rtype: list of str
        """
        return self._ReceiveAccount

    @ReceiveAccount.setter
    def ReceiveAccount(self, ReceiveAccount):
        self._ReceiveAccount = ReceiveAccount

    @property
    def PreStrategy(self):
        r"""前区规则组
        :rtype: list of StrategyReq
        """
        return self._PreStrategy

    @PreStrategy.setter
    def PreStrategy(self, PreStrategy):
        self._PreStrategy = PreStrategy

    @property
    def PostStrategy(self):
        r"""后区规则组
        :rtype: list of StrategyReq
        """
        return self._PostStrategy

    @PostStrategy.setter
    def PostStrategy(self, PostStrategy):
        self._PostStrategy = PostStrategy

    @property
    def ReceiveGroup(self):
        r"""下发账号组
        :rtype: list of str
        """
        return self._ReceiveGroup

    @ReceiveGroup.setter
    def ReceiveGroup(self, ReceiveGroup):
        self._ReceiveGroup = ReceiveGroup


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ReceiveAccount = params.get("ReceiveAccount")
        if params.get("PreStrategy") is not None:
            self._PreStrategy = []
            for item in params.get("PreStrategy"):
                obj = StrategyReq()
                obj._deserialize(item)
                self._PreStrategy.append(obj)
        if params.get("PostStrategy") is not None:
            self._PostStrategy = []
            for item in params.get("PostStrategy"):
                obj = StrategyReq()
                obj._deserialize(item)
                self._PostStrategy.append(obj)
        self._ReceiveGroup = params.get("ReceiveGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateStrategyResponse(AbstractModel):
    r"""CreateStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateVpcAclRuleGroupRequest(AbstractModel):
    r"""CreateVpcAclRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupName: 规则组名称
        :type GroupName: str
        :param _Product: 产品类型，固定为 cfw_vpc_acl
        :type Product: str
        :param _Rules: 规则列表
        :type Rules: list of VpcAclRule
        """
        self._GroupName = None
        self._Product = None
        self._Rules = None

    @property
    def GroupName(self):
        r"""规则组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def Product(self):
        r"""产品类型，固定为 cfw_vpc_acl
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of VpcAclRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        self._Product = params.get("Product")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = VpcAclRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcAclRuleGroupResponse(AbstractModel):
    r"""CreateVpcAclRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 创建的规则组ID
        :type GroupId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._GroupId = None
        self._RequestId = None

    @property
    def GroupId(self):
        r"""创建的规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RequestId = params.get("RequestId")


class CreateVpcAclRuleRequest(AbstractModel):
    r"""CreateVpcAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rules: 规则列表
        :type Rules: list of VpcAclRule
        """
        self._GroupId = None
        self._Rules = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of VpcAclRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = VpcAclRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVpcAclRuleResponse(AbstractModel):
    r"""CreateVpcAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteEdgeAclRuleRequest(AbstractModel):
    r"""DeleteEdgeAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _RuleIds: 要删除的规则ID列表
        :type RuleIds: list of str
        """
        self._GroupId = None
        self._RuleIds = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RuleIds(self):
        r"""要删除的规则ID列表
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEdgeAclRuleResponse(AbstractModel):
    r"""DeleteEdgeAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteNatAclRuleRequest(AbstractModel):
    r"""DeleteNatAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _RuleIds: 规则ID列表
        :type RuleIds: list of str
        """
        self._GroupId = None
        self._RuleIds = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RuleIds(self):
        r"""规则ID列表
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteNatAclRuleResponse(AbstractModel):
    r"""DeleteNatAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteRuleGroupRequest(AbstractModel):
    r"""DeleteRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupIds: 规则组Id列表
        :type GroupIds: list of str
        """
        self._GroupIds = None

    @property
    def GroupIds(self):
        r"""规则组Id列表
        :rtype: list of str
        """
        return self._GroupIds

    @GroupIds.setter
    def GroupIds(self, GroupIds):
        self._GroupIds = GroupIds


    def _deserialize(self, params):
        self._GroupIds = params.get("GroupIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleGroupResponse(AbstractModel):
    r"""DeleteRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteSecurityGroupRuleRequest(AbstractModel):
    r"""DeleteSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _RuleIds: 规则列表
        :type RuleIds: list of str
        """
        self._GroupId = None
        self._RuleIds = None

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RuleIds(self):
        r"""规则列表
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityGroupRuleResponse(AbstractModel):
    r"""DeleteSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteStrategyRequest(AbstractModel):
    r"""DeleteStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyIds: 策略Id列表
        :type StrategyIds: list of str
        """
        self._StrategyIds = None

    @property
    def StrategyIds(self):
        r"""策略Id列表
        :rtype: list of str
        """
        return self._StrategyIds

    @StrategyIds.setter
    def StrategyIds(self, StrategyIds):
        self._StrategyIds = StrategyIds


    def _deserialize(self, params):
        self._StrategyIds = params.get("StrategyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteStrategyResponse(AbstractModel):
    r"""DeleteStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteVpcAclRuleRequest(AbstractModel):
    r"""DeleteVpcAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _RuleIds: 规则ID列表
        :type RuleIds: list of str
        """
        self._GroupId = None
        self._RuleIds = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RuleIds(self):
        r"""规则ID列表
        :rtype: list of str
        """
        return self._RuleIds

    @RuleIds.setter
    def RuleIds(self, RuleIds):
        self._RuleIds = RuleIds


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteVpcAclRuleResponse(AbstractModel):
    r"""DeleteVpcAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeEdgeAclRulesRequest(AbstractModel):
    r"""DescribeEdgeAclRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Direction: 规则方向：0-出向，1-入向
        :type Direction: int
        :param _Filters: 过滤条件列表，支持按 RuleId、Direction、Protocol、RuleAction 等字段过滤
        :type Filters: list of CommonFilter
        :param _Limit: 分页大小，默认100，最大1000
        :type Limit: int
        :param _Offset: 分页偏移，默认0
        :type Offset: int
        :param _Order: 排序顺序，asc:升序 desc:降序
        :type Order: str
        :param _By: 排序字段，支持 Sequence、RuleId 等
        :type By: str
        """
        self._GroupId = None
        self._Direction = None
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._Order = None
        self._By = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Direction(self):
        r"""规则方向：0-出向，1-入向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Filters(self):
        r"""过滤条件列表，支持按 RuleId、Direction、Protocol、RuleAction 等字段过滤
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""分页大小，默认100，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Order(self):
        r"""排序顺序，asc:升序 desc:降序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段，支持 Sequence、RuleId 等
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Direction = params.get("Direction")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgeAclRulesResponse(AbstractModel):
    r"""DescribeEdgeAclRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 规则总数
        :type TotalCount: int
        :param _Rules: 规则列表
        :type Rules: list of EdgeAclRuleResp
        :param _AllTotalCount: 不过滤的总数
        :type AllTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Rules = None
        self._AllTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""规则总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of EdgeAclRuleResp
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def AllTotalCount(self):
        r"""不过滤的总数
        :rtype: int
        """
        return self._AllTotalCount

    @AllTotalCount.setter
    def AllTotalCount(self, AllTotalCount):
        self._AllTotalCount = AllTotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = EdgeAclRuleResp()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._AllTotalCount = params.get("AllTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeNatAclRulesRequest(AbstractModel):
    r"""DescribeNatAclRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Direction: 规则方向：0-出向，1-入向
        :type Direction: int
        :param _Filters: 过滤条件
        :type Filters: list of CommonFilter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量
        :type Limit: int
        :param _Order: 排序顺序，asc:升序 desc:降序
        :type Order: str
        :param _By: 排序字段
        :type By: str
        """
        self._GroupId = None
        self._Direction = None
        self._Filters = None
        self._Offset = None
        self._Limit = None
        self._Order = None
        self._By = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Direction(self):
        r"""规则方向：0-出向，1-入向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Order(self):
        r"""排序顺序，asc:升序 desc:降序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Direction = params.get("Direction")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Order = params.get("Order")
        self._By = params.get("By")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeNatAclRulesResponse(AbstractModel):
    r"""DescribeNatAclRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of NatAclRuleResp
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _AllTotalCount: 不过滤的总数
        :type AllTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._TotalCount = None
        self._AllTotalCount = None
        self._RequestId = None

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of NatAclRuleResp
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AllTotalCount(self):
        r"""不过滤的总数
        :rtype: int
        """
        return self._AllTotalCount

    @AllTotalCount.setter
    def AllTotalCount(self, AllTotalCount):
        self._AllTotalCount = AllTotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
                obj = NatAclRuleResp()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AllTotalCount = params.get("AllTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeOrganMembersRequest(AbstractModel):
    r"""DescribeOrganMembers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Filters: 搜索过滤条件列表，支持按成员 ID、账号名称、身份、纳管状态等字段筛选
        :type Filters: list of CommonFilter
        :param _Limit: 分页大小，默认 20
        :type Limit: int
        :param _Offset: 分页偏移量，默认 0
        :type Offset: int
        :param _By: 排序字段，如 MemberCreateTime
        :type By: str
        :param _Order: 排序方式：asc 升序，desc 降序
        :type Order: str
        """
        self._Filters = None
        self._Limit = None
        self._Offset = None
        self._By = None
        self._Order = None

    @property
    def Filters(self):
        r"""搜索过滤条件列表，支持按成员 ID、账号名称、身份、纳管状态等字段筛选
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""分页大小，默认 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def By(self):
        r"""排序字段，如 MemberCreateTime
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        r"""排序方式：asc 升序，desc 降序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._By = params.get("By")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOrganMembersResponse(AbstractModel):
    r"""DescribeOrganMembers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 集团成员总数
        :type TotalCount: int
        :param _Members: 集团成员列表
        :type Members: list of OrganMemberItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Members = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""集团成员总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Members(self):
        r"""集团成员列表
        :rtype: list of OrganMemberItem
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = OrganMemberItem()
                obj._deserialize(item)
                self._Members.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOrganSummaryRequest(AbstractModel):
    r"""DescribeOrganSummary请求参数结构体

    """


class DescribeOrganSummaryResponse(AbstractModel):
    r"""DescribeOrganSummary返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Summary: 集团概览
        :type Summary: :class:`tencentcloud.fwm.v20250611.models.OrganSummary`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Summary = None
        self._RequestId = None

    @property
    def Summary(self):
        r"""集团概览
        :rtype: :class:`tencentcloud.fwm.v20250611.models.OrganSummary`
        """
        return self._Summary

    @Summary.setter
    def Summary(self, Summary):
        self._Summary = Summary

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Summary") is not None:
            self._Summary = OrganSummary()
            self._Summary._deserialize(params.get("Summary"))
        self._RequestId = params.get("RequestId")


class DescribePolicyRiskAccountProductStatsRequest(AbstractModel):
    r"""DescribePolicyRiskAccountProductStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小，按账号分页，默认20，最大100
        :type Limit: int
        :param _Offset: 分页偏移，默认0
        :type Offset: int
        :param _Filters: 筛选条件列表。支持的筛选字段：AccountName（账号名称模糊搜索）、AccountId（账号Uin精确搜索）、OnlyUntreated（仅看待整改，值为1时生效）、OnlyOverdue（仅超时未体检，值为1时生效）
        :type Filters: list of CommonFilter
        """
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def Limit(self):
        r"""分页大小，按账号分页，默认20，最大100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移，默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        r"""筛选条件列表。支持的筛选字段：AccountName（账号名称模糊搜索）、AccountId（账号Uin精确搜索）、OnlyUntreated（仅看待整改，值为1时生效）、OnlyOverdue（仅超时未体检，值为1时生效）
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePolicyRiskAccountProductStatsResponse(AbstractModel):
    r"""DescribePolicyRiskAccountProductStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountStats: 按账号分组的风险统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountStats: list of AccountStatsGroup
        :param _TotalCount: 满足条件的账号总数
        :type TotalCount: int
        :param _OverdueAccountCount: 超时未体检的账号数
        :type OverdueAccountCount: int
        :param _OverdueProductCount: 超时未体检的产品数
        :type OverdueProductCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AccountStats = None
        self._TotalCount = None
        self._OverdueAccountCount = None
        self._OverdueProductCount = None
        self._RequestId = None

    @property
    def AccountStats(self):
        r"""按账号分组的风险统计列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AccountStatsGroup
        """
        return self._AccountStats

    @AccountStats.setter
    def AccountStats(self, AccountStats):
        self._AccountStats = AccountStats

    @property
    def TotalCount(self):
        r"""满足条件的账号总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OverdueAccountCount(self):
        r"""超时未体检的账号数
        :rtype: int
        """
        return self._OverdueAccountCount

    @OverdueAccountCount.setter
    def OverdueAccountCount(self, OverdueAccountCount):
        self._OverdueAccountCount = OverdueAccountCount

    @property
    def OverdueProductCount(self):
        r"""超时未体检的产品数
        :rtype: int
        """
        return self._OverdueProductCount

    @OverdueProductCount.setter
    def OverdueProductCount(self, OverdueProductCount):
        self._OverdueProductCount = OverdueProductCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("AccountStats") is not None:
            self._AccountStats = []
            for item in params.get("AccountStats"):
                obj = AccountStatsGroup()
                obj._deserialize(item)
                self._AccountStats.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._OverdueAccountCount = params.get("OverdueAccountCount")
        self._OverdueProductCount = params.get("OverdueProductCount")
        self._RequestId = params.get("RequestId")


class DescribeRiskAnalysisDetailsRequest(AbstractModel):
    r"""DescribeRiskAnalysisDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 风险ID
        :type Id: str
        :param _SearchType: 查询类型，analyze实时数据分析，task定时分析结果
        :type SearchType: str
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._Id = None
        self._SearchType = None
        self._MemberId = None

    @property
    def Id(self):
        r"""风险ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SearchType(self):
        r"""查询类型，analyze实时数据分析，task定时分析结果
        :rtype: str
        """
        return self._SearchType

    @SearchType.setter
    def SearchType(self, SearchType):
        self._SearchType = SearchType

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SearchType = params.get("SearchType")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskAnalysisDetailsResponse(AbstractModel):
    r"""DescribeRiskAnalysisDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EnterpriseSecurityGroupRule: 风险企业安全组规则列表
        :type EnterpriseSecurityGroupRule: list of AnalysisSgRuleInfoResp
        :param _SecurityGroupPolicy: 风险安全组规则列表
        :type SecurityGroupPolicy: list of SecurityGroupRiskPolicy
        :param _Status: 实时分析状态，1分析执行中请轮询，0分析已结束
        :type Status: int
        :param _EnterpriseSecurityGroupRuleIPV6: 风险企业安全组IPV6规则列表
        :type EnterpriseSecurityGroupRuleIPV6: list of AnalysisSgRuleInfoResp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EnterpriseSecurityGroupRule = None
        self._SecurityGroupPolicy = None
        self._Status = None
        self._EnterpriseSecurityGroupRuleIPV6 = None
        self._RequestId = None

    @property
    def EnterpriseSecurityGroupRule(self):
        r"""风险企业安全组规则列表
        :rtype: list of AnalysisSgRuleInfoResp
        """
        return self._EnterpriseSecurityGroupRule

    @EnterpriseSecurityGroupRule.setter
    def EnterpriseSecurityGroupRule(self, EnterpriseSecurityGroupRule):
        self._EnterpriseSecurityGroupRule = EnterpriseSecurityGroupRule

    @property
    def SecurityGroupPolicy(self):
        r"""风险安全组规则列表
        :rtype: list of SecurityGroupRiskPolicy
        """
        return self._SecurityGroupPolicy

    @SecurityGroupPolicy.setter
    def SecurityGroupPolicy(self, SecurityGroupPolicy):
        self._SecurityGroupPolicy = SecurityGroupPolicy

    @property
    def Status(self):
        r"""实时分析状态，1分析执行中请轮询，0分析已结束
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def EnterpriseSecurityGroupRuleIPV6(self):
        r"""风险企业安全组IPV6规则列表
        :rtype: list of AnalysisSgRuleInfoResp
        """
        return self._EnterpriseSecurityGroupRuleIPV6

    @EnterpriseSecurityGroupRuleIPV6.setter
    def EnterpriseSecurityGroupRuleIPV6(self, EnterpriseSecurityGroupRuleIPV6):
        self._EnterpriseSecurityGroupRuleIPV6 = EnterpriseSecurityGroupRuleIPV6

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EnterpriseSecurityGroupRule") is not None:
            self._EnterpriseSecurityGroupRule = []
            for item in params.get("EnterpriseSecurityGroupRule"):
                obj = AnalysisSgRuleInfoResp()
                obj._deserialize(item)
                self._EnterpriseSecurityGroupRule.append(obj)
        if params.get("SecurityGroupPolicy") is not None:
            self._SecurityGroupPolicy = []
            for item in params.get("SecurityGroupPolicy"):
                obj = SecurityGroupRiskPolicy()
                obj._deserialize(item)
                self._SecurityGroupPolicy.append(obj)
        self._Status = params.get("Status")
        if params.get("EnterpriseSecurityGroupRuleIPV6") is not None:
            self._EnterpriseSecurityGroupRuleIPV6 = []
            for item in params.get("EnterpriseSecurityGroupRuleIPV6"):
                obj = AnalysisSgRuleInfoResp()
                obj._deserialize(item)
                self._EnterpriseSecurityGroupRuleIPV6.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskCategoryStatsRequest(AbstractModel):
    r"""DescribeRiskCategoryStats请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 分页大小,默认20
        :type Limit: int
        :param _Offset: 分页偏移量,默认0
        :type Offset: int
        :param _Product: 产品类型
        :type Product: str
        :param _Filters: 筛选器
        :type Filters: list of CommonFilter
        :param _By: 排序字段："RuleCount", "TreatedCount", "IgnoredCount", "UntreatedCount", "DisposalRate"
        :type By: str
        :param _Order: 顺序
        :type Order: str
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._Limit = None
        self._Offset = None
        self._Product = None
        self._Filters = None
        self._By = None
        self._Order = None
        self._MemberId = None

    @property
    def Limit(self):
        r"""分页大小,默认20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""分页偏移量,默认0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Product(self):
        r"""产品类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Filters(self):
        r"""筛选器
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def By(self):
        r"""排序字段："RuleCount", "TreatedCount", "IgnoredCount", "UntreatedCount", "DisposalRate"
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def Order(self):
        r"""顺序
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Product = params.get("Product")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._By = params.get("By")
        self._Order = params.get("Order")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskCategoryStatsResponse(AbstractModel):
    r"""DescribeRiskCategoryStats返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 风险分类总数
        :type Total: int
        :param _Data: 风险分类统计列表
        :type Data: list of RiskCategoryItem
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Data = None
        self._RequestId = None

    @property
    def Total(self):
        r"""风险分类总数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Data(self):
        r"""风险分类统计列表
        :rtype: list of RiskCategoryItem
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = RiskCategoryItem()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeRiskListRequest(AbstractModel):
    r"""DescribeRiskList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Limit: 条数限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        :param _Product: 产品类型
        :type Product: str
        :param _Filters: 筛选条件
        :type Filters: list of CommonFilter
        :param _Order: 排序方式
        :type Order: str
        :param _By: 排序字段
        :type By: str
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._Limit = None
        self._Offset = None
        self._Product = None
        self._Filters = None
        self._Order = None
        self._By = None
        self._MemberId = None

    @property
    def Limit(self):
        r"""条数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Product(self):
        r"""产品类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Filters(self):
        r"""筛选条件
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        r"""排序方式
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def By(self):
        r"""排序字段
        :rtype: str
        """
        return self._By

    @By.setter
    def By(self, By):
        self._By = By

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        self._Product = params.get("Product")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._By = params.get("By")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRiskListResponse(AbstractModel):
    r"""DescribeRiskList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PolicyRiskLst: 策略问题列表
        :type PolicyRiskLst: list of PolicyRisk
        :param _Total: 策略问题数
        :type Total: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PolicyRiskLst = None
        self._Total = None
        self._RequestId = None

    @property
    def PolicyRiskLst(self):
        r"""策略问题列表
        :rtype: list of PolicyRisk
        """
        return self._PolicyRiskLst

    @PolicyRiskLst.setter
    def PolicyRiskLst(self, PolicyRiskLst):
        self._PolicyRiskLst = PolicyRiskLst

    @property
    def Total(self):
        r"""策略问题数
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PolicyRiskLst") is not None:
            self._PolicyRiskLst = []
            for item in params.get("PolicyRiskLst"):
                obj = PolicyRisk()
                obj._deserialize(item)
                self._PolicyRiskLst.append(obj)
        self._Total = params.get("Total")
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupRuleRequest(AbstractModel):
    r"""DescribeSecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _RuleId: 规则Id
        :type RuleId: str
        """
        self._GroupId = None
        self._RuleId = None

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._RuleId = params.get("RuleId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupRuleResponse(AbstractModel):
    r"""DescribeSecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rule: 规则详情
        :type Rule: :class:`tencentcloud.fwm.v20250611.models.SgRuleResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rule = None
        self._RequestId = None

    @property
    def Rule(self):
        r"""规则详情
        :rtype: :class:`tencentcloud.fwm.v20250611.models.SgRuleResp`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Rule") is not None:
            self._Rule = SgRuleResp()
            self._Rule._deserialize(params.get("Rule"))
        self._RequestId = params.get("RequestId")


class DescribeSecurityGroupRulesRequest(AbstractModel):
    r"""DescribeSecurityGroupRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _Filters: 模糊搜索关键词
        :type Filters: list of CommonFilter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量
        :type Limit: int
        """
        self._GroupId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Filters(self):
        r"""模糊搜索关键词
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityGroupRulesResponse(AbstractModel):
    r"""DescribeSecurityGroupRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of SecGroupRuleResp
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _AllTotalCount: 不过滤的规则总数
        :type AllTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._TotalCount = None
        self._AllTotalCount = None
        self._RequestId = None

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of SecGroupRuleResp
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AllTotalCount(self):
        r"""不过滤的规则总数
        :rtype: int
        """
        return self._AllTotalCount

    @AllTotalCount.setter
    def AllTotalCount(self, AllTotalCount):
        self._AllTotalCount = AllTotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
                obj = SecGroupRuleResp()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AllTotalCount = params.get("AllTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeStrategiesRequest(AbstractModel):
    r"""DescribeStrategies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品类型
        :type Product: str
        :param _ExecArea: 执行区域：pre是前区，post 是后区
        :type ExecArea: str
        :param _Filters: 筛选条件
        :type Filters: list of CommonFilter
        :param _Limit: 条数限制
        :type Limit: int
        :param _Offset: 偏移量
        :type Offset: int
        """
        self._Product = None
        self._ExecArea = None
        self._Filters = None
        self._Limit = None
        self._Offset = None

    @property
    def Product(self):
        r"""产品类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ExecArea(self):
        r"""执行区域：pre是前区，post 是后区
        :rtype: str
        """
        return self._ExecArea

    @ExecArea.setter
    def ExecArea(self, ExecArea):
        self._ExecArea = ExecArea

    @property
    def Filters(self):
        r"""筛选条件
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Limit(self):
        r"""条数限制
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._Product = params.get("Product")
        self._ExecArea = params.get("ExecArea")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategiesResponse(AbstractModel):
    r"""DescribeStrategies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _Strategies: 策略列表
        :type Strategies: list of StrategyResp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Strategies = None
        self._RequestId = None

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Strategies(self):
        r"""策略列表
        :rtype: list of StrategyResp
        """
        return self._Strategies

    @Strategies.setter
    def Strategies(self, Strategies):
        self._Strategies = Strategies

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Strategies") is not None:
            self._Strategies = []
            for item in params.get("Strategies"):
                obj = StrategyResp()
                obj._deserialize(item)
                self._Strategies.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStrategyAccountsRequest(AbstractModel):
    r"""DescribeStrategyAccounts请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 下发产品 secgroup // 企业安全组
        :type Product: str
        :param _Filters: 筛选器
        :type Filters: list of CommonFilter
        """
        self._Product = None
        self._Filters = None

    @property
    def Product(self):
        r"""下发产品 secgroup // 企业安全组
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Filters(self):
        r"""筛选器
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Product = params.get("Product")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategyAccountsResponse(AbstractModel):
    r"""DescribeStrategyAccounts返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Accounts: 账号列表
        :type Accounts: list of Account
        :param _AccountGroups: 账号组列表
        :type AccountGroups: list of AccountGroupQuotaDetail
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Accounts = None
        self._AccountGroups = None
        self._RequestId = None

    @property
    def Accounts(self):
        r"""账号列表
        :rtype: list of Account
        """
        return self._Accounts

    @Accounts.setter
    def Accounts(self, Accounts):
        self._Accounts = Accounts

    @property
    def AccountGroups(self):
        r"""账号组列表
        :rtype: list of AccountGroupQuotaDetail
        """
        return self._AccountGroups

    @AccountGroups.setter
    def AccountGroups(self, AccountGroups):
        self._AccountGroups = AccountGroups

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Accounts") is not None:
            self._Accounts = []
            for item in params.get("Accounts"):
                obj = Account()
                obj._deserialize(item)
                self._Accounts.append(obj)
        if params.get("AccountGroups") is not None:
            self._AccountGroups = []
            for item in params.get("AccountGroups"):
                obj = AccountGroupQuotaDetail()
                obj._deserialize(item)
                self._AccountGroups.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeStrategyDispatchStatusRequest(AbstractModel):
    r"""DescribeStrategyDispatchStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Product: 产品
        :type Product: str
        """
        self._Product = None

    @property
    def Product(self):
        r"""产品
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
        


class DescribeStrategyDispatchStatusResponse(AbstractModel):
    r"""DescribeStrategyDispatchStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Progress: 进度
        :type Progress: float
        :param _StartTime: 下发开始时间
        :type StartTime: str
        :param _EndTime: 下发结束时间
        :type EndTime: str
        :param _Status: 下发状态，0无变动，1下发中，2下发成功，3下发失败，4更新待下发
        :type Status: int
        :param _RuleGroupNum: 下发规则组数量
        :type RuleGroupNum: int
        :param _ErrorMsg: 下发失败错误信息
        :type ErrorMsg: str
        :param _DispatchStrategyList: 下发关联策略id列表
        :type DispatchStrategyList: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Progress = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._RuleGroupNum = None
        self._ErrorMsg = None
        self._DispatchStrategyList = None
        self._RequestId = None

    @property
    def Progress(self):
        r"""进度
        :rtype: float
        """
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def StartTime(self):
        r"""下发开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        r"""下发结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        r"""下发状态，0无变动，1下发中，2下发成功，3下发失败，4更新待下发
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RuleGroupNum(self):
        r"""下发规则组数量
        :rtype: int
        """
        return self._RuleGroupNum

    @RuleGroupNum.setter
    def RuleGroupNum(self, RuleGroupNum):
        self._RuleGroupNum = RuleGroupNum

    @property
    def ErrorMsg(self):
        r"""下发失败错误信息
        :rtype: str
        """
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def DispatchStrategyList(self):
        r"""下发关联策略id列表
        :rtype: list of str
        """
        return self._DispatchStrategyList

    @DispatchStrategyList.setter
    def DispatchStrategyList(self, DispatchStrategyList):
        self._DispatchStrategyList = DispatchStrategyList

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Progress = params.get("Progress")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._RuleGroupNum = params.get("RuleGroupNum")
        self._ErrorMsg = params.get("ErrorMsg")
        self._DispatchStrategyList = params.get("DispatchStrategyList")
        self._RequestId = params.get("RequestId")


class DescribeStrategyRequest(AbstractModel):
    r"""DescribeStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略Id
        :type StrategyId: str
        """
        self._StrategyId = None

    @property
    def StrategyId(self):
        r"""策略Id
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeStrategyResponse(AbstractModel):
    r"""DescribeStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Strategy: 策略详情
        :type Strategy: :class:`tencentcloud.fwm.v20250611.models.StrategyResp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Strategy = None
        self._RequestId = None

    @property
    def Strategy(self):
        r"""策略详情
        :rtype: :class:`tencentcloud.fwm.v20250611.models.StrategyResp`
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Strategy") is not None:
            self._Strategy = StrategyResp()
            self._Strategy._deserialize(params.get("Strategy"))
        self._RequestId = params.get("RequestId")


class DescribeVpcAclRulesRequest(AbstractModel):
    r"""DescribeVpcAclRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Filters: 过滤条件
        :type Filters: list of CommonFilter
        :param _Offset: 偏移量
        :type Offset: int
        :param _Limit: 数量
        :type Limit: int
        """
        self._GroupId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Filters(self):
        r"""过滤条件
        :rtype: list of CommonFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        r"""偏移量
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        r"""数量
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = CommonFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVpcAclRulesResponse(AbstractModel):
    r"""DescribeVpcAclRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Rules: 规则列表
        :type Rules: list of VpcAclRuleResp
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _AllTotalCount: 不过滤的总数
        :type AllTotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Rules = None
        self._TotalCount = None
        self._AllTotalCount = None
        self._RequestId = None

    @property
    def Rules(self):
        r"""规则列表
        :rtype: list of VpcAclRuleResp
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def TotalCount(self):
        r"""总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AllTotalCount(self):
        r"""不过滤的总数
        :rtype: int
        """
        return self._AllTotalCount

    @AllTotalCount.setter
    def AllTotalCount(self, AllTotalCount):
        self._AllTotalCount = AllTotalCount

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
                obj = VpcAclRuleResp()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AllTotalCount = params.get("AllTotalCount")
        self._RequestId = params.get("RequestId")


class DispatchStrategyRequest(AbstractModel):
    r"""DispatchStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 1:下发，2:中止
        :type Status: int
        :param _Product: 产品
        :type Product: str
        """
        self._Status = None
        self._Product = None

    @property
    def Status(self):
        r"""1:下发，2:中止
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Product(self):
        r"""产品
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DispatchStrategyResponse(AbstractModel):
    r"""DispatchStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 返回状态
        :type Status: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._RequestId = None

    @property
    def Status(self):
        r"""返回状态
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class EdgeAclRuleInfo(AbstractModel):
    r"""互联网边界规则

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID，修改规则时必填
        :type RuleId: str
        :param _OrderIndex: 规则执行顺序，数字越小优先级越高，创建规则组时必须从1开始严格递增
        :type OrderIndex: int
        :param _Direction: 规则方向：0-出站，1-入站
        :type Direction: int
        :param _SourceContent: 源地址内容，根据 SourceType 不同有不同的格式：ip 时为 IP/CIDR，domain 时为域名，template 时为模板ID，instance 时为实例ID列表（逗号分隔），tag 时为标签键值对（格式：key:value）
        :type SourceContent: str
        :param _SourceType: 源地址类型：ip-IP地址，domain-域名，template-参数模板，instance-实例，tag-标签
        :type SourceType: str
        :param _TargetContent: 目标地址内容，格式同 SourceContent
        :type TargetContent: str
        :param _TargetType: 目标地址类型：ip-IP地址，domain-域名，template-参数模板，instance-实例，tag-标签
        :type TargetType: str
        :param _Port: 端口，支持单端口、端口范围和逗号分隔的多端口，如：80、1-65535、80,443,8080
        :type Port: str
        :param _Protocol: 协议类型：TCP、UDP、ICMP、ANY
        :type Protocol: str
        :param _RuleAction: 规则动作：accept-放行，drop-阻断，log-观察
        :type RuleAction: str
        :param _Description: 规则描述，长度0-256字符
        :type Description: str
        :param _Scope: 生效范围：serial，串行；side，旁路；all，全局	
        :type Scope: str
        :param _BelongMemberId: 规则归属的成员账号ID（多账号场景下使用）。当 SourceType 或 TargetType 为 instance 或 tag 时，此参数必填，用于指定实例/标签所属的成员账号
        :type BelongMemberId: str
        :param _ParamTemplateId: 参数模板
        :type ParamTemplateId: str
        """
        self._RuleId = None
        self._OrderIndex = None
        self._Direction = None
        self._SourceContent = None
        self._SourceType = None
        self._TargetContent = None
        self._TargetType = None
        self._Port = None
        self._Protocol = None
        self._RuleAction = None
        self._Description = None
        self._Scope = None
        self._BelongMemberId = None
        self._ParamTemplateId = None

    @property
    def RuleId(self):
        r"""规则ID，修改规则时必填
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def OrderIndex(self):
        r"""规则执行顺序，数字越小优先级越高，创建规则组时必须从1开始严格递增
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Direction(self):
        r"""规则方向：0-出站，1-入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def SourceContent(self):
        r"""源地址内容，根据 SourceType 不同有不同的格式：ip 时为 IP/CIDR，domain 时为域名，template 时为模板ID，instance 时为实例ID列表（逗号分隔），tag 时为标签键值对（格式：key:value）
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""源地址类型：ip-IP地址，domain-域名，template-参数模板，instance-实例，tag-标签
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetContent(self):
        r"""目标地址内容，格式同 SourceContent
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        r"""目标地址类型：ip-IP地址，domain-域名，template-参数模板，instance-实例，tag-标签
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Port(self):
        r"""端口，支持单端口、端口范围和逗号分隔的多端口，如：80、1-65535、80,443,8080
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        r"""协议类型：TCP、UDP、ICMP、ANY
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        r"""规则动作：accept-放行，drop-阻断，log-观察
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        r"""规则描述，长度0-256字符
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Scope(self):
        r"""生效范围：serial，串行；side，旁路；all，全局	
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def BelongMemberId(self):
        r"""规则归属的成员账号ID（多账号场景下使用）。当 SourceType 或 TargetType 为 instance 或 tag 时，此参数必填，用于指定实例/标签所属的成员账号
        :rtype: str
        """
        return self._BelongMemberId

    @BelongMemberId.setter
    def BelongMemberId(self, BelongMemberId):
        self._BelongMemberId = BelongMemberId

    @property
    def ParamTemplateId(self):
        r"""参数模板
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._OrderIndex = params.get("OrderIndex")
        self._Direction = params.get("Direction")
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._Scope = params.get("Scope")
        self._BelongMemberId = params.get("BelongMemberId")
        self._ParamTemplateId = params.get("ParamTemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgeAclRuleResp(AbstractModel):
    r"""互联网边界规则响应结构

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Sequence: 规则执行顺序
        :type Sequence: int
        :param _Direction: 规则方向：0-出站，1-入站
        :type Direction: int
        :param _SourceContent: 源地址内容
        :type SourceContent: str
        :param _SourceType: 源地址类型
        :type SourceType: str
        :param _SourceName: 源地址名称（当类型为模板/实例/标签时返回对应名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceName: str
        :param _TargetContent: 目标地址内容
        :type TargetContent: str
        :param _TargetType: 目标地址类型
        :type TargetType: str
        :param _TargetName: 目标地址名称（当类型为模板/实例/标签时返回对应名称）
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetName: str
        :param _Port: 目标端口
        :type Port: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _RuleAction: 规则动作：accept-放行，drop-阻断，log-观察
        :type RuleAction: str
        :param _Description: 规则描述
        :type Description: str
        :param _Scope: 规则生效范围
        :type Scope: str
        :param _CountryName: 地域名称1（正则匹配时使用）
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryName: str
        :param _CityName: 地域名称2（正则匹配时使用）
注意：此字段可能返回 null，表示取不到有效值。
        :type CityName: str
        :param _ParamTemplateId: 参数模板ID（当类型为模板时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateId: str
        :param _ParamTemplateName: 参数模板名称（当类型为模板时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateName: str
        :param _Invalid: 规则是否失效：0-有效，1-失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Invalid: int
        :param _BelongMember: 规则归属的成员账号
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongMember: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        :param _CountryCode: 国家Id
        :type CountryCode: int
        :param _CityCode: 城市Id
        :type CityCode: int
        :param _IsRegion: 0为正常规则,1为地域规则
        :type IsRegion: int
        :param _CloudCode: 云厂商code
        :type CloudCode: str
        :param _IsCloud: 0为正常规则,1为云厂商规则
        :type IsCloud: int
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _CountryKey: 地区简称
        :type CountryKey: str
        :param _CityKey: 省份、城市简称
        :type CityKey: str
        :param _CreateTime: 规则创建时间
        :type CreateTime: str
        :param _UpdateTime: 规则最近更新时间
        :type UpdateTime: str
        :param _DnsParseCnt: 域名数
        :type DnsParseCnt: int
        """
        self._RuleId = None
        self._Sequence = None
        self._Direction = None
        self._SourceContent = None
        self._SourceType = None
        self._SourceName = None
        self._TargetContent = None
        self._TargetType = None
        self._TargetName = None
        self._Port = None
        self._Protocol = None
        self._RuleAction = None
        self._Description = None
        self._Scope = None
        self._CountryName = None
        self._CityName = None
        self._ParamTemplateId = None
        self._ParamTemplateName = None
        self._Invalid = None
        self._BelongMember = None
        self._CountryCode = None
        self._CityCode = None
        self._IsRegion = None
        self._CloudCode = None
        self._IsCloud = None
        self._InstanceName = None
        self._CountryKey = None
        self._CityKey = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DnsParseCnt = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Sequence(self):
        r"""规则执行顺序
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def Direction(self):
        r"""规则方向：0-出站，1-入站
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def SourceContent(self):
        r"""源地址内容
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""源地址类型
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceName(self):
        r"""源地址名称（当类型为模板/实例/标签时返回对应名称）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def TargetContent(self):
        r"""目标地址内容
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        r"""目标地址类型
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetName(self):
        r"""目标地址名称（当类型为模板/实例/标签时返回对应名称）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def Port(self):
        r"""目标端口
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        r"""协议类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        r"""规则动作：accept-放行，drop-阻断，log-观察
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Scope(self):
        r"""规则生效范围
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def CountryName(self):
        r"""地域名称1（正则匹配时使用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName

    @property
    def CityName(self):
        r"""地域名称2（正则匹配时使用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName

    @property
    def ParamTemplateId(self):
        r"""参数模板ID（当类型为模板时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def ParamTemplateName(self):
        r"""参数模板名称（当类型为模板时返回）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateName

    @ParamTemplateName.setter
    def ParamTemplateName(self, ParamTemplateName):
        self._ParamTemplateName = ParamTemplateName

    @property
    def Invalid(self):
        r"""规则是否失效：0-有效，1-失效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid

    @property
    def BelongMember(self):
        r"""规则归属的成员账号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._BelongMember

    @BelongMember.setter
    def BelongMember(self, BelongMember):
        self._BelongMember = BelongMember

    @property
    def CountryCode(self):
        r"""国家Id
        :rtype: int
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def CityCode(self):
        r"""城市Id
        :rtype: int
        """
        return self._CityCode

    @CityCode.setter
    def CityCode(self, CityCode):
        self._CityCode = CityCode

    @property
    def IsRegion(self):
        r"""0为正常规则,1为地域规则
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CloudCode(self):
        r"""云厂商code
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def IsCloud(self):
        r"""0为正常规则,1为云厂商规则
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def InstanceName(self):
        r"""实例名称
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def CountryKey(self):
        r"""地区简称
        :rtype: str
        """
        return self._CountryKey

    @CountryKey.setter
    def CountryKey(self, CountryKey):
        self._CountryKey = CountryKey

    @property
    def CityKey(self):
        r"""省份、城市简称
        :rtype: str
        """
        return self._CityKey

    @CityKey.setter
    def CityKey(self, CityKey):
        self._CityKey = CityKey

    @property
    def CreateTime(self):
        r"""规则创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""规则最近更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DnsParseCnt(self):
        r"""域名数
        :rtype: int
        """
        return self._DnsParseCnt

    @DnsParseCnt.setter
    def DnsParseCnt(self, DnsParseCnt):
        self._DnsParseCnt = DnsParseCnt


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Sequence = params.get("Sequence")
        self._Direction = params.get("Direction")
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._SourceName = params.get("SourceName")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._TargetName = params.get("TargetName")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._Scope = params.get("Scope")
        self._CountryName = params.get("CountryName")
        self._CityName = params.get("CityName")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._ParamTemplateName = params.get("ParamTemplateName")
        self._Invalid = params.get("Invalid")
        if params.get("BelongMember") is not None:
            self._BelongMember = MemberInfo()
            self._BelongMember._deserialize(params.get("BelongMember"))
        self._CountryCode = params.get("CountryCode")
        self._CityCode = params.get("CityCode")
        self._IsRegion = params.get("IsRegion")
        self._CloudCode = params.get("CloudCode")
        self._IsCloud = params.get("IsCloud")
        self._InstanceName = params.get("InstanceName")
        self._CountryKey = params.get("CountryKey")
        self._CityKey = params.get("CityKey")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DnsParseCnt = params.get("DnsParseCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnorePolicyRiskRequest(AbstractModel):
    r"""IgnorePolicyRisk请求参数结构体

    """

    def __init__(self):
        r"""
        :param _RiskId: 策略问题ID
        :type RiskId: str
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._RiskId = None
        self._MemberId = None

    @property
    def RiskId(self):
        r"""策略问题ID
        :rtype: str
        """
        return self._RiskId

    @RiskId.setter
    def RiskId(self, RiskId):
        self._RiskId = RiskId

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._RiskId = params.get("RiskId")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IgnorePolicyRiskResponse(AbstractModel):
    r"""IgnorePolicyRisk返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MemberInfo(AbstractModel):
    r"""成员信息

    """

    def __init__(self):
        r"""
        :param _AppId: 成员AppId
        :type AppId: str
        :param _Uin: 成员Uin
        :type Uin: str
        :param _Nickname: 成员昵称
        :type Nickname: str
        :param _MemberId: 成员Id
        :type MemberId: str
        """
        self._AppId = None
        self._Uin = None
        self._Nickname = None
        self._MemberId = None

    @property
    def AppId(self):
        r"""成员AppId
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""成员Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""成员昵称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def MemberId(self):
        r"""成员Id
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._MemberId = params.get("MemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeAclRuleRequest(AbstractModel):
    r"""ModifyEdgeAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rule: 要修改的规则，必须包含RuleId
        :type Rule: :class:`tencentcloud.fwm.v20250611.models.EdgeAclRuleInfo`
        """
        self._GroupId = None
        self._Rule = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rule(self):
        r"""要修改的规则，必须包含RuleId
        :rtype: :class:`tencentcloud.fwm.v20250611.models.EdgeAclRuleInfo`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rule") is not None:
            self._Rule = EdgeAclRuleInfo()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeAclRuleResponse(AbstractModel):
    r"""ModifyEdgeAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyEdgeAclRuleSequenceRequest(AbstractModel):
    r"""ModifyEdgeAclRuleSequence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Direction: 出入站方向 0=出向，1=入向
        :type Direction: int
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Sequences: 规则序号调整列表，必须包含所有受影响的规则
        :type Sequences: list of SequenceIndex
        """
        self._Direction = None
        self._GroupId = None
        self._Sequences = None

    @property
    def Direction(self):
        r"""出入站方向 0=出向，1=入向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Sequences(self):
        r"""规则序号调整列表，必须包含所有受影响的规则
        :rtype: list of SequenceIndex
        """
        return self._Sequences

    @Sequences.setter
    def Sequences(self, Sequences):
        self._Sequences = Sequences


    def _deserialize(self, params):
        self._Direction = params.get("Direction")
        self._GroupId = params.get("GroupId")
        if params.get("Sequences") is not None:
            self._Sequences = []
            for item in params.get("Sequences"):
                obj = SequenceIndex()
                obj._deserialize(item)
                self._Sequences.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyEdgeAclRuleSequenceResponse(AbstractModel):
    r"""ModifyEdgeAclRuleSequence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNatAclRuleRequest(AbstractModel):
    r"""ModifyNatAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.fwm.v20250611.models.NatAclRule`
        """
        self._GroupId = None
        self._Rule = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.fwm.v20250611.models.NatAclRule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rule") is not None:
            self._Rule = NatAclRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatAclRuleResponse(AbstractModel):
    r"""ModifyNatAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyNatAclRuleSequenceRequest(AbstractModel):
    r"""ModifyNatAclRuleSequence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Sequences: 序号调整列表
        :type Sequences: list of SequenceIndex
        :param _Direction: 规则方向：1-入站规则，0-出站规则
        :type Direction: int
        """
        self._GroupId = None
        self._Sequences = None
        self._Direction = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Sequences(self):
        r"""序号调整列表
        :rtype: list of SequenceIndex
        """
        return self._Sequences

    @Sequences.setter
    def Sequences(self, Sequences):
        self._Sequences = Sequences

    @property
    def Direction(self):
        r"""规则方向：1-入站规则，0-出站规则
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Sequences") is not None:
            self._Sequences = []
            for item in params.get("Sequences"):
                obj = SequenceIndex()
                obj._deserialize(item)
                self._Sequences.append(obj)
        self._Direction = params.get("Direction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyNatAclRuleSequenceResponse(AbstractModel):
    r"""ModifyNatAclRuleSequence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyRuleGroupRequest(AbstractModel):
    r"""ModifyRuleGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组名称
        :type GroupId: str
        :param _GroupName: 规则组名称
        :type GroupName: str
        """
        self._GroupId = None
        self._GroupName = None

    @property
    def GroupId(self):
        r"""规则组名称
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""规则组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleGroupResponse(AbstractModel):
    r"""ModifyRuleGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifySecurityGroupRuleRequest(AbstractModel):
    r"""ModifySecurityGroupRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.fwm.v20250611.models.SecurityGroupRule`
        """
        self._GroupId = None
        self._Rule = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.fwm.v20250611.models.SecurityGroupRule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rule") is not None:
            self._Rule = SecurityGroupRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityGroupRuleResponse(AbstractModel):
    r"""ModifySecurityGroupRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyStrategyRequest(AbstractModel):
    r"""ModifyStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略Id
        :type StrategyId: str
        :param _ReceiveAccount: 下发规则接收账号
        :type ReceiveAccount: list of str
        :param _Sequence: 优先级
        :type Sequence: int
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _ReceiveGroup: 下发规则接收账号组
        :type ReceiveGroup: list of str
        """
        self._StrategyId = None
        self._ReceiveAccount = None
        self._Sequence = None
        self._GroupId = None
        self._ReceiveGroup = None

    @property
    def StrategyId(self):
        r"""策略Id
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def ReceiveAccount(self):
        r"""下发规则接收账号
        :rtype: list of str
        """
        return self._ReceiveAccount

    @ReceiveAccount.setter
    def ReceiveAccount(self, ReceiveAccount):
        self._ReceiveAccount = ReceiveAccount

    @property
    def Sequence(self):
        r"""优先级
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def ReceiveGroup(self):
        r"""下发规则接收账号组
        :rtype: list of str
        """
        return self._ReceiveGroup

    @ReceiveGroup.setter
    def ReceiveGroup(self, ReceiveGroup):
        self._ReceiveGroup = ReceiveGroup


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._ReceiveAccount = params.get("ReceiveAccount")
        self._Sequence = params.get("Sequence")
        self._GroupId = params.get("GroupId")
        self._ReceiveGroup = params.get("ReceiveGroup")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStrategyResponse(AbstractModel):
    r"""ModifyStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyStrategySequenceRequest(AbstractModel):
    r"""ModifyStrategySequence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Sequences: 优先级列表
        :type Sequences: list of SequenceIndex
        :param _ExecArea: 执行区域
        :type ExecArea: str
        :param _Product: 产品类型
        :type Product: str
        """
        self._Sequences = None
        self._ExecArea = None
        self._Product = None

    @property
    def Sequences(self):
        r"""优先级列表
        :rtype: list of SequenceIndex
        """
        return self._Sequences

    @Sequences.setter
    def Sequences(self, Sequences):
        self._Sequences = Sequences

    @property
    def ExecArea(self):
        r"""执行区域
        :rtype: str
        """
        return self._ExecArea

    @ExecArea.setter
    def ExecArea(self, ExecArea):
        self._ExecArea = ExecArea

    @property
    def Product(self):
        r"""产品类型
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        if params.get("Sequences") is not None:
            self._Sequences = []
            for item in params.get("Sequences"):
                obj = SequenceIndex()
                obj._deserialize(item)
                self._Sequences.append(obj)
        self._ExecArea = params.get("ExecArea")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyStrategySequenceResponse(AbstractModel):
    r"""ModifyStrategySequence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyVpcAclRuleRequest(AbstractModel):
    r"""ModifyVpcAclRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Rule: 规则
        :type Rule: :class:`tencentcloud.fwm.v20250611.models.VpcAclRule`
        """
        self._GroupId = None
        self._Rule = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Rule(self):
        r"""规则
        :rtype: :class:`tencentcloud.fwm.v20250611.models.VpcAclRule`
        """
        return self._Rule

    @Rule.setter
    def Rule(self, Rule):
        self._Rule = Rule


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Rule") is not None:
            self._Rule = VpcAclRule()
            self._Rule._deserialize(params.get("Rule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAclRuleResponse(AbstractModel):
    r"""ModifyVpcAclRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyVpcAclRuleSequenceRequest(AbstractModel):
    r"""ModifyVpcAclRuleSequence请求参数结构体

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组ID
        :type GroupId: str
        :param _Sequences: 序号调整列表
        :type Sequences: list of SequenceIndex
        """
        self._GroupId = None
        self._Sequences = None

    @property
    def GroupId(self):
        r"""规则组ID
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Sequences(self):
        r"""序号调整列表
        :rtype: list of SequenceIndex
        """
        return self._Sequences

    @Sequences.setter
    def Sequences(self, Sequences):
        self._Sequences = Sequences


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        if params.get("Sequences") is not None:
            self._Sequences = []
            for item in params.get("Sequences"):
                obj = SequenceIndex()
                obj._deserialize(item)
                self._Sequences.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyVpcAclRuleSequenceResponse(AbstractModel):
    r"""ModifyVpcAclRuleSequence返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        r"""唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class NatAclRule(AbstractModel):
    r"""NAT边界规则

    """

    def __init__(self):
        r"""
        :param _SourceContent: <p>源地址内容</p>
        :type SourceContent: str
        :param _SourceType: <p>源类型：ip/url/template/instance/tag</p>
        :type SourceType: str
        :param _TargetContent: <p>目的地址内容</p>
        :type TargetContent: str
        :param _TargetType: <p>目的类型：ip/url/template/instance/tag</p>
        :type TargetType: str
        :param _Protocol: <p>协议：TCP/UDP/ICMP/ANY/HTTP/HTTPS/DNS/FTP等</p>
        :type Protocol: str
        :param _RuleAction: <p>动作：accept/drop/log</p>
        :type RuleAction: str
        :param _OrderIndex: <p>优先级（从1开始）</p>
        :type OrderIndex: int
        :param _Scope: <p>规则生效范围：ALL-全局生效，ap-xxx-地域生效，cfwnat-xxx-NAT防火墙实例生效</p>
        :type Scope: str
        :param _Direction: <p>规则方向：1-入站规则，0-出站规则</p>
        :type Direction: int
        :param _RuleId: <p>规则ID（修改时必填）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param _Port: <p>端口（ICMP协议时为空）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param _Description: <p>规则描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _ParamTemplateId: <p>端口模板ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateId: str
        :param _BelongMemberId: <p>规则归属的成员账号ID(当Scope为cfwnat-xxx或SourceType/DestType为instance/tag时必填)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongMemberId: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._TargetContent = None
        self._TargetType = None
        self._Protocol = None
        self._RuleAction = None
        self._OrderIndex = None
        self._Scope = None
        self._Direction = None
        self._RuleId = None
        self._Port = None
        self._Description = None
        self._ParamTemplateId = None
        self._BelongMemberId = None

    @property
    def SourceContent(self):
        r"""<p>源地址内容</p>
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""<p>源类型：ip/url/template/instance/tag</p>
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetContent(self):
        r"""<p>目的地址内容</p>
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        r"""<p>目的类型：ip/url/template/instance/tag</p>
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        r"""<p>协议：TCP/UDP/ICMP/ANY/HTTP/HTTPS/DNS/FTP等</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        r"""<p>动作：accept/drop/log</p>
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def OrderIndex(self):
        r"""<p>优先级（从1开始）</p>
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def Scope(self):
        r"""<p>规则生效范围：ALL-全局生效，ap-xxx-地域生效，cfwnat-xxx-NAT防火墙实例生效</p>
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def Direction(self):
        r"""<p>规则方向：1-入站规则，0-出站规则</p>
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RuleId(self):
        r"""<p>规则ID（修改时必填）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Port(self):
        r"""<p>端口（ICMP协议时为空）</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Description(self):
        r"""<p>规则描述</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamTemplateId(self):
        r"""<p>端口模板ID</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def BelongMemberId(self):
        r"""<p>规则归属的成员账号ID(当Scope为cfwnat-xxx或SourceType/DestType为instance/tag时必填)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BelongMemberId

    @BelongMemberId.setter
    def BelongMemberId(self, BelongMemberId):
        self._BelongMemberId = BelongMemberId


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._OrderIndex = params.get("OrderIndex")
        self._Scope = params.get("Scope")
        self._Direction = params.get("Direction")
        self._RuleId = params.get("RuleId")
        self._Port = params.get("Port")
        self._Description = params.get("Description")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._BelongMemberId = params.get("BelongMemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NatAclRuleResp(AbstractModel):
    r"""NAT边界规则响应结构

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Sequence: 优先级
        :type Sequence: int
        :param _Direction: 规则方向：0-出向，1-入向
        :type Direction: int
        :param _SourceContent: 源地址内容
        :type SourceContent: str
        :param _SourceType: 源类型
        :type SourceType: str
        :param _SourceName: 源资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceName: str
        :param _TargetContent: 目的地址内容
        :type TargetContent: str
        :param _TargetType: 目的类型
        :type TargetType: str
        :param _TargetName: 目的资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TargetName: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _RuleAction: 动作：accept/drop/log
        :type RuleAction: str
        :param _Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _Scope: 规则生效范围
        :type Scope: str
        :param _ScopeDesc: 规则生效范围描述
注意：此字段可能返回 null，表示取不到有效值。
        :type ScopeDesc: str
        :param _FwInsId: 防火墙实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type FwInsId: str
        :param _CountryName: 国家名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryName: str
        :param _CityName: 城市名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CityName: str
        :param _CountryCode: 国家代码
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryCode: int
        :param _CityCode: 城市代码
注意：此字段可能返回 null，表示取不到有效值。
        :type CityCode: int
        :param _CountryKey: 国家键值
注意：此字段可能返回 null，表示取不到有效值。
        :type CountryKey: str
        :param _CityKey: 城市键值
注意：此字段可能返回 null，表示取不到有效值。
        :type CityKey: str
        :param _IsRegion: 是否地域规则：0-否，1-是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsRegion: int
        :param _CloudCode: 云厂商代码
注意：此字段可能返回 null，表示取不到有效值。
        :type CloudCode: str
        :param _IsCloud: 是否云厂商规则：0-否，1-是
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCloud: int
        :param _ParamTemplateId: 端口模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateId: str
        :param _ParamTemplateName: 端口模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateName: str
        :param _Invalid: 规则是否失效：0-有效，1-失效
注意：此字段可能返回 null，表示取不到有效值。
        :type Invalid: int
        :param _BelongMember: 规则归属的成员账号
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongMember: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _DnsParseCnt: 域名数
        :type DnsParseCnt: int
        """
        self._RuleId = None
        self._Sequence = None
        self._Direction = None
        self._SourceContent = None
        self._SourceType = None
        self._SourceName = None
        self._TargetContent = None
        self._TargetType = None
        self._TargetName = None
        self._Port = None
        self._Protocol = None
        self._RuleAction = None
        self._Description = None
        self._Scope = None
        self._ScopeDesc = None
        self._FwInsId = None
        self._CountryName = None
        self._CityName = None
        self._CountryCode = None
        self._CityCode = None
        self._CountryKey = None
        self._CityKey = None
        self._IsRegion = None
        self._CloudCode = None
        self._IsCloud = None
        self._ParamTemplateId = None
        self._ParamTemplateName = None
        self._Invalid = None
        self._BelongMember = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DnsParseCnt = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Sequence(self):
        r"""优先级
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def Direction(self):
        r"""规则方向：0-出向，1-入向
        :rtype: int
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def SourceContent(self):
        r"""源地址内容
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""源类型
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceName(self):
        r"""源资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def TargetContent(self):
        r"""目的地址内容
        :rtype: str
        """
        return self._TargetContent

    @TargetContent.setter
    def TargetContent(self, TargetContent):
        self._TargetContent = TargetContent

    @property
    def TargetType(self):
        r"""目的类型
        :rtype: str
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def TargetName(self):
        r"""目的资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TargetName

    @TargetName.setter
    def TargetName(self, TargetName):
        self._TargetName = TargetName

    @property
    def Port(self):
        r"""端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Protocol(self):
        r"""协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        r"""动作：accept/drop/log
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        r"""规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Scope(self):
        r"""规则生效范围
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ScopeDesc(self):
        r"""规则生效范围描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ScopeDesc

    @ScopeDesc.setter
    def ScopeDesc(self, ScopeDesc):
        self._ScopeDesc = ScopeDesc

    @property
    def FwInsId(self):
        r"""防火墙实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FwInsId

    @FwInsId.setter
    def FwInsId(self, FwInsId):
        self._FwInsId = FwInsId

    @property
    def CountryName(self):
        r"""国家名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CountryName

    @CountryName.setter
    def CountryName(self, CountryName):
        self._CountryName = CountryName

    @property
    def CityName(self):
        r"""城市名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CityName

    @CityName.setter
    def CityName(self, CityName):
        self._CityName = CityName

    @property
    def CountryCode(self):
        r"""国家代码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CountryCode

    @CountryCode.setter
    def CountryCode(self, CountryCode):
        self._CountryCode = CountryCode

    @property
    def CityCode(self):
        r"""城市代码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CityCode

    @CityCode.setter
    def CityCode(self, CityCode):
        self._CityCode = CityCode

    @property
    def CountryKey(self):
        r"""国家键值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CountryKey

    @CountryKey.setter
    def CountryKey(self, CountryKey):
        self._CountryKey = CountryKey

    @property
    def CityKey(self):
        r"""城市键值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CityKey

    @CityKey.setter
    def CityKey(self, CityKey):
        self._CityKey = CityKey

    @property
    def IsRegion(self):
        r"""是否地域规则：0-否，1-是
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsRegion

    @IsRegion.setter
    def IsRegion(self, IsRegion):
        self._IsRegion = IsRegion

    @property
    def CloudCode(self):
        r"""云厂商代码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CloudCode

    @CloudCode.setter
    def CloudCode(self, CloudCode):
        self._CloudCode = CloudCode

    @property
    def IsCloud(self):
        r"""是否云厂商规则：0-否，1-是
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._IsCloud

    @IsCloud.setter
    def IsCloud(self, IsCloud):
        self._IsCloud = IsCloud

    @property
    def ParamTemplateId(self):
        r"""端口模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def ParamTemplateName(self):
        r"""端口模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateName

    @ParamTemplateName.setter
    def ParamTemplateName(self, ParamTemplateName):
        self._ParamTemplateName = ParamTemplateName

    @property
    def Invalid(self):
        r"""规则是否失效：0-有效，1-失效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid

    @property
    def BelongMember(self):
        r"""规则归属的成员账号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._BelongMember

    @BelongMember.setter
    def BelongMember(self, BelongMember):
        self._BelongMember = BelongMember

    @property
    def CreateTime(self):
        r"""创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DnsParseCnt(self):
        r"""域名数
        :rtype: int
        """
        return self._DnsParseCnt

    @DnsParseCnt.setter
    def DnsParseCnt(self, DnsParseCnt):
        self._DnsParseCnt = DnsParseCnt


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Sequence = params.get("Sequence")
        self._Direction = params.get("Direction")
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._SourceName = params.get("SourceName")
        self._TargetContent = params.get("TargetContent")
        self._TargetType = params.get("TargetType")
        self._TargetName = params.get("TargetName")
        self._Port = params.get("Port")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._Scope = params.get("Scope")
        self._ScopeDesc = params.get("ScopeDesc")
        self._FwInsId = params.get("FwInsId")
        self._CountryName = params.get("CountryName")
        self._CityName = params.get("CityName")
        self._CountryCode = params.get("CountryCode")
        self._CityCode = params.get("CityCode")
        self._CountryKey = params.get("CountryKey")
        self._CityKey = params.get("CityKey")
        self._IsRegion = params.get("IsRegion")
        self._CloudCode = params.get("CloudCode")
        self._IsCloud = params.get("IsCloud")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._ParamTemplateName = params.get("ParamTemplateName")
        self._Invalid = params.get("Invalid")
        if params.get("BelongMember") is not None:
            self._BelongMember = MemberInfo()
            self._BelongMember._deserialize(params.get("BelongMember"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DnsParseCnt = params.get("DnsParseCnt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganMemberItem(AbstractModel):
    r"""集团成员信息

    """

    def __init__(self):
        r"""
        :param _MemberId: 成员 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberId: str
        :param _AppId: 成员账号 AppId
注意：此字段可能返回 null，表示取不到有效值。
        :type AppId: str
        :param _Uin: 账号Uin
        :type Uin: str
        :param _Nickname: 账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Nickname: str
        :param _SubAccountCount: 子账号数量
注意：此字段可能返回 null，表示取不到有效值。
        :type SubAccountCount: int
        :param _NodeName: 所属组织架构节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type NodeName: str
        :param _Role: 成员身份：admin-管理员，delegatedAdmin-委派管理员，member-普通成员
注意：此字段可能返回 null，表示取不到有效值。
        :type Role: str
        :param _RoleDisplay: 成员身份显示名称（前端展示用）
注意：此字段可能返回 null，表示取不到有效值。
        :type RoleDisplay: str
        :param _AccountGroup: 所属账户组 
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroup: :class:`tencentcloud.fwm.v20250611.models.AccountGroupInfo`
        :param _CfwManaged: 云防火墙纳管状态：0-未纳管，1-已纳管
注意：此字段可能返回 null，表示取不到有效值。
        :type CfwManaged: int
        :param _CfwShareRole: 云防火墙共享角色：sharer-共享者，user-使用者，none-未设置
注意：此字段可能返回 null，表示取不到有效值。
        :type CfwShareRole: str
        :param _CfwShareRoleDisplay: 云防火墙共享角色显示名称（前端展示用）
注意：此字段可能返回 null，表示取不到有效值。
        :type CfwShareRoleDisplay: str
        :param _CfwSharerAppId: 云防火墙共享者 AppId，成员角色为使用者时有值
注意：此字段可能返回 null，表示取不到有效值。
        :type CfwSharerAppId: str
        :param _CfwInstanceId: 云防火墙计费实例 ID，非空表示已购买云防火墙
注意：此字段可能返回 null，表示取不到有效值。
        :type CfwInstanceId: str
        :param _PolicyAnalysisEnabled: 策略分析权限：0-关闭，1-开启
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyAnalysisEnabled: int
        :param _MemberCreateTime: 成员加入集团时间
注意：此字段可能返回 null，表示取不到有效值。
        :type MemberCreateTime: str
        :param _JoinType: 账号加入方式
        :type JoinType: str
        """
        self._MemberId = None
        self._AppId = None
        self._Uin = None
        self._Nickname = None
        self._SubAccountCount = None
        self._NodeName = None
        self._Role = None
        self._RoleDisplay = None
        self._AccountGroup = None
        self._CfwManaged = None
        self._CfwShareRole = None
        self._CfwShareRoleDisplay = None
        self._CfwSharerAppId = None
        self._CfwInstanceId = None
        self._PolicyAnalysisEnabled = None
        self._MemberCreateTime = None
        self._JoinType = None

    @property
    def MemberId(self):
        r"""成员 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MemberId

    @MemberId.setter
    def MemberId(self, MemberId):
        self._MemberId = MemberId

    @property
    def AppId(self):
        r"""成员账号 AppId
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Uin(self):
        r"""账号Uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""账号名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def SubAccountCount(self):
        r"""子账号数量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._SubAccountCount

    @SubAccountCount.setter
    def SubAccountCount(self, SubAccountCount):
        self._SubAccountCount = SubAccountCount

    @property
    def NodeName(self):
        r"""所属组织架构节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._NodeName

    @NodeName.setter
    def NodeName(self, NodeName):
        self._NodeName = NodeName

    @property
    def Role(self):
        r"""成员身份：admin-管理员，delegatedAdmin-委派管理员，member-普通成员
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Role

    @Role.setter
    def Role(self, Role):
        self._Role = Role

    @property
    def RoleDisplay(self):
        r"""成员身份显示名称（前端展示用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RoleDisplay

    @RoleDisplay.setter
    def RoleDisplay(self, RoleDisplay):
        self._RoleDisplay = RoleDisplay

    @property
    def AccountGroup(self):
        r"""所属账户组 
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.AccountGroupInfo`
        """
        return self._AccountGroup

    @AccountGroup.setter
    def AccountGroup(self, AccountGroup):
        self._AccountGroup = AccountGroup

    @property
    def CfwManaged(self):
        r"""云防火墙纳管状态：0-未纳管，1-已纳管
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CfwManaged

    @CfwManaged.setter
    def CfwManaged(self, CfwManaged):
        self._CfwManaged = CfwManaged

    @property
    def CfwShareRole(self):
        r"""云防火墙共享角色：sharer-共享者，user-使用者，none-未设置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CfwShareRole

    @CfwShareRole.setter
    def CfwShareRole(self, CfwShareRole):
        self._CfwShareRole = CfwShareRole

    @property
    def CfwShareRoleDisplay(self):
        r"""云防火墙共享角色显示名称（前端展示用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CfwShareRoleDisplay

    @CfwShareRoleDisplay.setter
    def CfwShareRoleDisplay(self, CfwShareRoleDisplay):
        self._CfwShareRoleDisplay = CfwShareRoleDisplay

    @property
    def CfwSharerAppId(self):
        r"""云防火墙共享者 AppId，成员角色为使用者时有值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CfwSharerAppId

    @CfwSharerAppId.setter
    def CfwSharerAppId(self, CfwSharerAppId):
        self._CfwSharerAppId = CfwSharerAppId

    @property
    def CfwInstanceId(self):
        r"""云防火墙计费实例 ID，非空表示已购买云防火墙
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CfwInstanceId

    @CfwInstanceId.setter
    def CfwInstanceId(self, CfwInstanceId):
        self._CfwInstanceId = CfwInstanceId

    @property
    def PolicyAnalysisEnabled(self):
        r"""策略分析权限：0-关闭，1-开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PolicyAnalysisEnabled

    @PolicyAnalysisEnabled.setter
    def PolicyAnalysisEnabled(self, PolicyAnalysisEnabled):
        self._PolicyAnalysisEnabled = PolicyAnalysisEnabled

    @property
    def MemberCreateTime(self):
        r"""成员加入集团时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._MemberCreateTime

    @MemberCreateTime.setter
    def MemberCreateTime(self, MemberCreateTime):
        self._MemberCreateTime = MemberCreateTime

    @property
    def JoinType(self):
        r"""账号加入方式
        :rtype: str
        """
        return self._JoinType

    @JoinType.setter
    def JoinType(self, JoinType):
        self._JoinType = JoinType


    def _deserialize(self, params):
        self._MemberId = params.get("MemberId")
        self._AppId = params.get("AppId")
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._SubAccountCount = params.get("SubAccountCount")
        self._NodeName = params.get("NodeName")
        self._Role = params.get("Role")
        self._RoleDisplay = params.get("RoleDisplay")
        if params.get("AccountGroup") is not None:
            self._AccountGroup = AccountGroupInfo()
            self._AccountGroup._deserialize(params.get("AccountGroup"))
        self._CfwManaged = params.get("CfwManaged")
        self._CfwShareRole = params.get("CfwShareRole")
        self._CfwShareRoleDisplay = params.get("CfwShareRoleDisplay")
        self._CfwSharerAppId = params.get("CfwSharerAppId")
        self._CfwInstanceId = params.get("CfwInstanceId")
        self._PolicyAnalysisEnabled = params.get("PolicyAnalysisEnabled")
        self._MemberCreateTime = params.get("MemberCreateTime")
        self._JoinType = params.get("JoinType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OrganSummary(AbstractModel):
    r"""集团概览

    """

    def __init__(self):
        r"""
        :param _GroupName: 集团名称
        :type GroupName: str
        :param _AdminInfo: 管理员账号信息
        :type AdminInfo: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        :param _AdminCount: 管理员/委派管理员数量
        :type AdminCount: int
        :param _JoinedMemberCount: 已接入成员数
        :type JoinedMemberCount: int
        :param _MemberLimit: 接入成员上限（-1表示无上限）
        :type MemberLimit: int
        :param _MemberLimitDisplay: 接入成员上限显示
        :type MemberLimitDisplay: str
        :param _CfwSharerCount: 规格共享者数量
        :type CfwSharerCount: int
        :param _CfwUserCount: 规格使用者数量
        :type CfwUserCount: int
        :param _Departments: 部门名称列表
        :type Departments: list of str
        :param _ManagedMemberCount: 纳管账号数
        :type ManagedMemberCount: int
        :param _ManagedProductCount: 纳管产品数
        :type ManagedProductCount: int
        :param _CfwManageCount: 纳管账号数
        :type CfwManageCount: int
        """
        self._GroupName = None
        self._AdminInfo = None
        self._AdminCount = None
        self._JoinedMemberCount = None
        self._MemberLimit = None
        self._MemberLimitDisplay = None
        self._CfwSharerCount = None
        self._CfwUserCount = None
        self._Departments = None
        self._ManagedMemberCount = None
        self._ManagedProductCount = None
        self._CfwManageCount = None

    @property
    def GroupName(self):
        r"""集团名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def AdminInfo(self):
        r"""管理员账号信息
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._AdminInfo

    @AdminInfo.setter
    def AdminInfo(self, AdminInfo):
        self._AdminInfo = AdminInfo

    @property
    def AdminCount(self):
        r"""管理员/委派管理员数量
        :rtype: int
        """
        return self._AdminCount

    @AdminCount.setter
    def AdminCount(self, AdminCount):
        self._AdminCount = AdminCount

    @property
    def JoinedMemberCount(self):
        r"""已接入成员数
        :rtype: int
        """
        return self._JoinedMemberCount

    @JoinedMemberCount.setter
    def JoinedMemberCount(self, JoinedMemberCount):
        self._JoinedMemberCount = JoinedMemberCount

    @property
    def MemberLimit(self):
        r"""接入成员上限（-1表示无上限）
        :rtype: int
        """
        return self._MemberLimit

    @MemberLimit.setter
    def MemberLimit(self, MemberLimit):
        self._MemberLimit = MemberLimit

    @property
    def MemberLimitDisplay(self):
        r"""接入成员上限显示
        :rtype: str
        """
        return self._MemberLimitDisplay

    @MemberLimitDisplay.setter
    def MemberLimitDisplay(self, MemberLimitDisplay):
        self._MemberLimitDisplay = MemberLimitDisplay

    @property
    def CfwSharerCount(self):
        r"""规格共享者数量
        :rtype: int
        """
        return self._CfwSharerCount

    @CfwSharerCount.setter
    def CfwSharerCount(self, CfwSharerCount):
        self._CfwSharerCount = CfwSharerCount

    @property
    def CfwUserCount(self):
        r"""规格使用者数量
        :rtype: int
        """
        return self._CfwUserCount

    @CfwUserCount.setter
    def CfwUserCount(self, CfwUserCount):
        self._CfwUserCount = CfwUserCount

    @property
    def Departments(self):
        r"""部门名称列表
        :rtype: list of str
        """
        return self._Departments

    @Departments.setter
    def Departments(self, Departments):
        self._Departments = Departments

    @property
    def ManagedMemberCount(self):
        r"""纳管账号数
        :rtype: int
        """
        return self._ManagedMemberCount

    @ManagedMemberCount.setter
    def ManagedMemberCount(self, ManagedMemberCount):
        self._ManagedMemberCount = ManagedMemberCount

    @property
    def ManagedProductCount(self):
        r"""纳管产品数
        :rtype: int
        """
        return self._ManagedProductCount

    @ManagedProductCount.setter
    def ManagedProductCount(self, ManagedProductCount):
        self._ManagedProductCount = ManagedProductCount

    @property
    def CfwManageCount(self):
        r"""纳管账号数
        :rtype: int
        """
        return self._CfwManageCount

    @CfwManageCount.setter
    def CfwManageCount(self, CfwManageCount):
        self._CfwManageCount = CfwManageCount


    def _deserialize(self, params):
        self._GroupName = params.get("GroupName")
        if params.get("AdminInfo") is not None:
            self._AdminInfo = MemberInfo()
            self._AdminInfo._deserialize(params.get("AdminInfo"))
        self._AdminCount = params.get("AdminCount")
        self._JoinedMemberCount = params.get("JoinedMemberCount")
        self._MemberLimit = params.get("MemberLimit")
        self._MemberLimitDisplay = params.get("MemberLimitDisplay")
        self._CfwSharerCount = params.get("CfwSharerCount")
        self._CfwUserCount = params.get("CfwUserCount")
        self._Departments = params.get("Departments")
        self._ManagedMemberCount = params.get("ManagedMemberCount")
        self._ManagedProductCount = params.get("ManagedProductCount")
        self._CfwManageCount = params.get("CfwManageCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PolicyRisk(AbstractModel):
    r"""策略风险

    """

    def __init__(self):
        r"""
        :param _Id: 问题对应的唯一uuid
        :type Id: str
        :param _RiskCategory: 风险大类
        :type RiskCategory: str
        :param _RiskSubCategory: 风险子类
        :type RiskSubCategory: str
        :param _RuleType: 规则分类
        :type RuleType: str
        :param _RiskLevel: 风险等级，0：低风险
1：中风险
2：高风险
        :type RiskLevel: int
        :param _Product: 安全组
        :type Product: str
        :param _SgRuleId: 风险包含的企业安全组规则ID
        :type SgRuleId: list of str
        :param _RuleCount: 风险包含安全组ID内的问题规则数
        :type RuleCount: int
        :param _SgId: 风险包含的安全组ID
        :type SgId: list of str
        :param _RiskFeature: 风险特征
        :type RiskFeature: str
        :param _Suggestion: 处置建议
        :type Suggestion: str
        :param _Status: 处置状态，0：未处理，1：已处理，2：忽略
        :type Status: int
        :param _FoundTime: 发现时间
        :type FoundTime: str
        :param _DisposalTime: 处置时间
        :type DisposalTime: str
        :param _Region: 安全组地域
        :type Region: str
        :param _Direction: Ingress入站，Egress出站
        :type Direction: str
        :param _RiskReason: 风险原因
        :type RiskReason: str
        """
        self._Id = None
        self._RiskCategory = None
        self._RiskSubCategory = None
        self._RuleType = None
        self._RiskLevel = None
        self._Product = None
        self._SgRuleId = None
        self._RuleCount = None
        self._SgId = None
        self._RiskFeature = None
        self._Suggestion = None
        self._Status = None
        self._FoundTime = None
        self._DisposalTime = None
        self._Region = None
        self._Direction = None
        self._RiskReason = None

    @property
    def Id(self):
        r"""问题对应的唯一uuid
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RiskCategory(self):
        r"""风险大类
        :rtype: str
        """
        return self._RiskCategory

    @RiskCategory.setter
    def RiskCategory(self, RiskCategory):
        self._RiskCategory = RiskCategory

    @property
    def RiskSubCategory(self):
        r"""风险子类
        :rtype: str
        """
        return self._RiskSubCategory

    @RiskSubCategory.setter
    def RiskSubCategory(self, RiskSubCategory):
        self._RiskSubCategory = RiskSubCategory

    @property
    def RuleType(self):
        r"""规则分类
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RiskLevel(self):
        r"""风险等级，0：低风险
1：中风险
2：高风险
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def Product(self):
        r"""安全组
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def SgRuleId(self):
        r"""风险包含的企业安全组规则ID
        :rtype: list of str
        """
        return self._SgRuleId

    @SgRuleId.setter
    def SgRuleId(self, SgRuleId):
        self._SgRuleId = SgRuleId

    @property
    def RuleCount(self):
        r"""风险包含安全组ID内的问题规则数
        :rtype: int
        """
        return self._RuleCount

    @RuleCount.setter
    def RuleCount(self, RuleCount):
        self._RuleCount = RuleCount

    @property
    def SgId(self):
        r"""风险包含的安全组ID
        :rtype: list of str
        """
        return self._SgId

    @SgId.setter
    def SgId(self, SgId):
        self._SgId = SgId

    @property
    def RiskFeature(self):
        r"""风险特征
        :rtype: str
        """
        return self._RiskFeature

    @RiskFeature.setter
    def RiskFeature(self, RiskFeature):
        self._RiskFeature = RiskFeature

    @property
    def Suggestion(self):
        r"""处置建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def Status(self):
        r"""处置状态，0：未处理，1：已处理，2：忽略
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def FoundTime(self):
        r"""发现时间
        :rtype: str
        """
        return self._FoundTime

    @FoundTime.setter
    def FoundTime(self, FoundTime):
        self._FoundTime = FoundTime

    @property
    def DisposalTime(self):
        r"""处置时间
        :rtype: str
        """
        return self._DisposalTime

    @DisposalTime.setter
    def DisposalTime(self, DisposalTime):
        self._DisposalTime = DisposalTime

    @property
    def Region(self):
        r"""安全组地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Direction(self):
        r"""Ingress入站，Egress出站
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def RiskReason(self):
        r"""风险原因
        :rtype: str
        """
        return self._RiskReason

    @RiskReason.setter
    def RiskReason(self, RiskReason):
        self._RiskReason = RiskReason


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RiskCategory = params.get("RiskCategory")
        self._RiskSubCategory = params.get("RiskSubCategory")
        self._RuleType = params.get("RuleType")
        self._RiskLevel = params.get("RiskLevel")
        self._Product = params.get("Product")
        self._SgRuleId = params.get("SgRuleId")
        self._RuleCount = params.get("RuleCount")
        self._SgId = params.get("SgId")
        self._RiskFeature = params.get("RiskFeature")
        self._Suggestion = params.get("Suggestion")
        self._Status = params.get("Status")
        self._FoundTime = params.get("FoundTime")
        self._DisposalTime = params.get("DisposalTime")
        self._Region = params.get("Region")
        self._Direction = params.get("Direction")
        self._RiskReason = params.get("RiskReason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReceiveAccount(AbstractModel):
    r"""账号信息

    """

    def __init__(self):
        r"""
        :param _Uin: 租户 uin
        :type Uin: str
        :param _Nickname: 租户名称
        :type Nickname: str
        :param _ReceiverType: 0=账号uin，1=账号组
        :type ReceiverType: int
        :param _Members: 只有ReceiverType 是 1 时 才返回账号列表
        :type Members: list of MemberInfo
        """
        self._Uin = None
        self._Nickname = None
        self._ReceiverType = None
        self._Members = None

    @property
    def Uin(self):
        r"""租户 uin
        :rtype: str
        """
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Nickname(self):
        r"""租户名称
        :rtype: str
        """
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def ReceiverType(self):
        r"""0=账号uin，1=账号组
        :rtype: int
        """
        return self._ReceiverType

    @ReceiverType.setter
    def ReceiverType(self, ReceiverType):
        self._ReceiverType = ReceiverType

    @property
    def Members(self):
        r"""只有ReceiverType 是 1 时 才返回账号列表
        :rtype: list of MemberInfo
        """
        return self._Members

    @Members.setter
    def Members(self, Members):
        self._Members = Members


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Nickname = params.get("Nickname")
        self._ReceiverType = params.get("ReceiverType")
        if params.get("Members") is not None:
            self._Members = []
            for item in params.get("Members"):
                obj = MemberInfo()
                obj._deserialize(item)
                self._Members.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RiskCategoryItem(AbstractModel):
    r"""风险分类统计项

    """

    def __init__(self):
        r"""
        :param _CategoryId: 风险大类ID
        :type CategoryId: str
        :param _CategoryName: 风险大类名称
        :type CategoryName: str
        :param _SubcategoryId: 风险子类ID
        :type SubcategoryId: str
        :param _SubcategoryName: 风险子类名称
        :type SubcategoryName: str
        :param _RiskLevel: 风险等级(0-低危,1-中危,2-高危)
        :type RiskLevel: int
        :param _RiskLevelName: 风险等级名称(低/中/高)
        :type RiskLevelName: str
        :param _Description: 风险描述
        :type Description: str
        :param _Suggestion: 处置建议
        :type Suggestion: str
        :param _RuleCount: 该类风险的规则数量
        :type RuleCount: int
        :param _TreatedCount: 已处置数量
        :type TreatedCount: int
        :param _IgnoredCount: 已忽略数量
        :type IgnoredCount: int
        :param _UntreatedCount: 待整改数量
        :type UntreatedCount: int
        :param _DisposalRate: 整改率(百分比字符串)
        :type DisposalRate: int
        :param _HasRisk: 是否有未处理风险
-1: 未体检
0: 无风险
1: 有风险
        :type HasRisk: int
        :param _RemediationStatus: 整改状态：
Completed： 已整改完成（整改率 100%）
Incomplete： 未整改完成（整改率 < 100%）
-：未体检/无数据
        :type RemediationStatus: str
        """
        self._CategoryId = None
        self._CategoryName = None
        self._SubcategoryId = None
        self._SubcategoryName = None
        self._RiskLevel = None
        self._RiskLevelName = None
        self._Description = None
        self._Suggestion = None
        self._RuleCount = None
        self._TreatedCount = None
        self._IgnoredCount = None
        self._UntreatedCount = None
        self._DisposalRate = None
        self._HasRisk = None
        self._RemediationStatus = None

    @property
    def CategoryId(self):
        r"""风险大类ID
        :rtype: str
        """
        return self._CategoryId

    @CategoryId.setter
    def CategoryId(self, CategoryId):
        self._CategoryId = CategoryId

    @property
    def CategoryName(self):
        r"""风险大类名称
        :rtype: str
        """
        return self._CategoryName

    @CategoryName.setter
    def CategoryName(self, CategoryName):
        self._CategoryName = CategoryName

    @property
    def SubcategoryId(self):
        r"""风险子类ID
        :rtype: str
        """
        return self._SubcategoryId

    @SubcategoryId.setter
    def SubcategoryId(self, SubcategoryId):
        self._SubcategoryId = SubcategoryId

    @property
    def SubcategoryName(self):
        r"""风险子类名称
        :rtype: str
        """
        return self._SubcategoryName

    @SubcategoryName.setter
    def SubcategoryName(self, SubcategoryName):
        self._SubcategoryName = SubcategoryName

    @property
    def RiskLevel(self):
        r"""风险等级(0-低危,1-中危,2-高危)
        :rtype: int
        """
        return self._RiskLevel

    @RiskLevel.setter
    def RiskLevel(self, RiskLevel):
        self._RiskLevel = RiskLevel

    @property
    def RiskLevelName(self):
        r"""风险等级名称(低/中/高)
        :rtype: str
        """
        return self._RiskLevelName

    @RiskLevelName.setter
    def RiskLevelName(self, RiskLevelName):
        self._RiskLevelName = RiskLevelName

    @property
    def Description(self):
        r"""风险描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def Suggestion(self):
        r"""处置建议
        :rtype: str
        """
        return self._Suggestion

    @Suggestion.setter
    def Suggestion(self, Suggestion):
        self._Suggestion = Suggestion

    @property
    def RuleCount(self):
        r"""该类风险的规则数量
        :rtype: int
        """
        return self._RuleCount

    @RuleCount.setter
    def RuleCount(self, RuleCount):
        self._RuleCount = RuleCount

    @property
    def TreatedCount(self):
        r"""已处置数量
        :rtype: int
        """
        return self._TreatedCount

    @TreatedCount.setter
    def TreatedCount(self, TreatedCount):
        self._TreatedCount = TreatedCount

    @property
    def IgnoredCount(self):
        r"""已忽略数量
        :rtype: int
        """
        return self._IgnoredCount

    @IgnoredCount.setter
    def IgnoredCount(self, IgnoredCount):
        self._IgnoredCount = IgnoredCount

    @property
    def UntreatedCount(self):
        r"""待整改数量
        :rtype: int
        """
        return self._UntreatedCount

    @UntreatedCount.setter
    def UntreatedCount(self, UntreatedCount):
        self._UntreatedCount = UntreatedCount

    @property
    def DisposalRate(self):
        r"""整改率(百分比字符串)
        :rtype: int
        """
        return self._DisposalRate

    @DisposalRate.setter
    def DisposalRate(self, DisposalRate):
        self._DisposalRate = DisposalRate

    @property
    def HasRisk(self):
        r"""是否有未处理风险
-1: 未体检
0: 无风险
1: 有风险
        :rtype: int
        """
        return self._HasRisk

    @HasRisk.setter
    def HasRisk(self, HasRisk):
        self._HasRisk = HasRisk

    @property
    def RemediationStatus(self):
        r"""整改状态：
Completed： 已整改完成（整改率 100%）
Incomplete： 未整改完成（整改率 < 100%）
-：未体检/无数据
        :rtype: str
        """
        return self._RemediationStatus

    @RemediationStatus.setter
    def RemediationStatus(self, RemediationStatus):
        self._RemediationStatus = RemediationStatus


    def _deserialize(self, params):
        self._CategoryId = params.get("CategoryId")
        self._CategoryName = params.get("CategoryName")
        self._SubcategoryId = params.get("SubcategoryId")
        self._SubcategoryName = params.get("SubcategoryName")
        self._RiskLevel = params.get("RiskLevel")
        self._RiskLevelName = params.get("RiskLevelName")
        self._Description = params.get("Description")
        self._Suggestion = params.get("Suggestion")
        self._RuleCount = params.get("RuleCount")
        self._TreatedCount = params.get("TreatedCount")
        self._IgnoredCount = params.get("IgnoredCount")
        self._UntreatedCount = params.get("UntreatedCount")
        self._DisposalRate = params.get("DisposalRate")
        self._HasRisk = params.get("HasRisk")
        self._RemediationStatus = params.get("RemediationStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecGroupRuleResp(AbstractModel):
    r"""企业安全组规则列表信息

    """

    def __init__(self):
        r"""
        :param _OrderIndex: <p>排序</p>
        :type OrderIndex: int
        :param _RuleId: <p>主键id</p>
        :type RuleId: str
        :param _IpVersion: <p>ip类型</p>
        :type IpVersion: str
        :param _SourceId: <p>源规则内容</p>
        :type SourceId: str
        :param _SourceType: <p>源规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9/100<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)<br>100表示资产分组(resourcegroup)</p>
        :type SourceType: int
        :param _TargetId: <p>目的规则内容</p>
        :type TargetId: str
        :param _TargetType: <p>目的规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9/100<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)<br>100表示资产分组(resourcegroup)</p>
        :type TargetType: int
        :param _Protocol: <p>协议名称<br>取值范围:TCP/ANY/ICMP/UDP<br>ANY:表示所有</p>
        :type Protocol: str
        :param _Port: <p>端口</p>
        :type Port: str
        :param _Strategy: <p>策略</p>
        :type Strategy: int
        :param _Detail: <p>描述</p>
        :type Detail: str
        :param _Region: <p>地域</p>
        :type Region: str
        :param _ServiceTemplateId: <p>服务模板id</p>
        :type ServiceTemplateId: str
        :param _SouInstanceName: <p>源资产名称</p>
        :type SouInstanceName: str
        :param _SouPublicIp: <p>源资产公网ip</p>
        :type SouPublicIp: str
        :param _SouPrivateIp: <p>源资产内网ip</p>
        :type SouPrivateIp: str
        :param _SouCidr: <p>源资产网段信息</p>
        :type SouCidr: str
        :param _SouParameterName: <p>源模板名称</p>
        :type SouParameterName: str
        :param _InstanceName: <p>目的资产名称</p>
        :type InstanceName: str
        :param _PublicIp: <p>目的资产公网ip</p>
        :type PublicIp: str
        :param _PrivateIp: <p>目的资产内网ip</p>
        :type PrivateIp: str
        :param _Cidr: <p>目的资产网段信息</p>
        :type Cidr: str
        :param _ParameterName: <p>目的模板名称</p>
        :type ParameterName: str
        :param _ProtocolPortName: <p>端口模板名称</p>
        :type ProtocolPortName: str
        :param _Id: <p>规则id  等同RuleUuid</p>
        :type Id: int
        :param _DnsParseCount: <p>域名解析的IP统计</p>
        :type DnsParseCount: :class:`tencentcloud.fwm.v20250611.models.SgDnsParseCount`
        :param _Scope: <p>规则生效范围</p>
        :type Scope: str
        :param _IsNew: <p>规则最近一次是否有改动 取值范围：0/1 0:否 1:是</p>
        :type IsNew: int
        :param _BelongMember: <p>规则归属的成员账号（当FwGroupId为cfwg-xxx或SourceType/DestType为instance/tag时必填)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongMember: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        self._OrderIndex = None
        self._RuleId = None
        self._IpVersion = None
        self._SourceId = None
        self._SourceType = None
        self._TargetId = None
        self._TargetType = None
        self._Protocol = None
        self._Port = None
        self._Strategy = None
        self._Detail = None
        self._Region = None
        self._ServiceTemplateId = None
        self._SouInstanceName = None
        self._SouPublicIp = None
        self._SouPrivateIp = None
        self._SouCidr = None
        self._SouParameterName = None
        self._InstanceName = None
        self._PublicIp = None
        self._PrivateIp = None
        self._Cidr = None
        self._ParameterName = None
        self._ProtocolPortName = None
        self._Id = None
        self._DnsParseCount = None
        self._Scope = None
        self._IsNew = None
        self._BelongMember = None

    @property
    def OrderIndex(self):
        r"""<p>排序</p>
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def RuleId(self):
        r"""<p>主键id</p>
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def IpVersion(self):
        r"""<p>ip类型</p>
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def SourceId(self):
        r"""<p>源规则内容</p>
        :rtype: str
        """
        return self._SourceId

    @SourceId.setter
    def SourceId(self, SourceId):
        self._SourceId = SourceId

    @property
    def SourceType(self):
        r"""<p>源规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9/100<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)<br>100表示资产分组(resourcegroup)</p>
        :rtype: int
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TargetId(self):
        r"""<p>目的规则内容</p>
        :rtype: str
        """
        return self._TargetId

    @TargetId.setter
    def TargetId(self, TargetId):
        self._TargetId = TargetId

    @property
    def TargetType(self):
        r"""<p>目的规则类型<br>取值范围 0/1/2/3/4/5/6/7/8/9/100<br>0表示ip(net),<br>1表示VPC实例(instance)<br>2表示子网实例(instance)<br>3表示CVM实例(instance)<br>4表示CLB实例(instance)<br>5表示ENI实例(instance)<br>6表示数据库实例(instance)<br>7表示模板(template)<br>8表示标签(tag)<br>9表示地域(region)<br>100表示资产分组(resourcegroup)</p>
        :rtype: int
        """
        return self._TargetType

    @TargetType.setter
    def TargetType(self, TargetType):
        self._TargetType = TargetType

    @property
    def Protocol(self):
        r"""<p>协议名称<br>取值范围:TCP/ANY/ICMP/UDP<br>ANY:表示所有</p>
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""<p>端口</p>
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Strategy(self):
        r"""<p>策略</p>
        :rtype: int
        """
        return self._Strategy

    @Strategy.setter
    def Strategy(self, Strategy):
        self._Strategy = Strategy

    @property
    def Detail(self):
        r"""<p>描述</p>
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Region(self):
        r"""<p>地域</p>
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ServiceTemplateId(self):
        r"""<p>服务模板id</p>
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def SouInstanceName(self):
        r"""<p>源资产名称</p>
        :rtype: str
        """
        return self._SouInstanceName

    @SouInstanceName.setter
    def SouInstanceName(self, SouInstanceName):
        self._SouInstanceName = SouInstanceName

    @property
    def SouPublicIp(self):
        r"""<p>源资产公网ip</p>
        :rtype: str
        """
        return self._SouPublicIp

    @SouPublicIp.setter
    def SouPublicIp(self, SouPublicIp):
        self._SouPublicIp = SouPublicIp

    @property
    def SouPrivateIp(self):
        r"""<p>源资产内网ip</p>
        :rtype: str
        """
        return self._SouPrivateIp

    @SouPrivateIp.setter
    def SouPrivateIp(self, SouPrivateIp):
        self._SouPrivateIp = SouPrivateIp

    @property
    def SouCidr(self):
        r"""<p>源资产网段信息</p>
        :rtype: str
        """
        return self._SouCidr

    @SouCidr.setter
    def SouCidr(self, SouCidr):
        self._SouCidr = SouCidr

    @property
    def SouParameterName(self):
        r"""<p>源模板名称</p>
        :rtype: str
        """
        return self._SouParameterName

    @SouParameterName.setter
    def SouParameterName(self, SouParameterName):
        self._SouParameterName = SouParameterName

    @property
    def InstanceName(self):
        r"""<p>目的资产名称</p>
        :rtype: str
        """
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def PublicIp(self):
        r"""<p>目的资产公网ip</p>
        :rtype: str
        """
        return self._PublicIp

    @PublicIp.setter
    def PublicIp(self, PublicIp):
        self._PublicIp = PublicIp

    @property
    def PrivateIp(self):
        r"""<p>目的资产内网ip</p>
        :rtype: str
        """
        return self._PrivateIp

    @PrivateIp.setter
    def PrivateIp(self, PrivateIp):
        self._PrivateIp = PrivateIp

    @property
    def Cidr(self):
        r"""<p>目的资产网段信息</p>
        :rtype: str
        """
        return self._Cidr

    @Cidr.setter
    def Cidr(self, Cidr):
        self._Cidr = Cidr

    @property
    def ParameterName(self):
        r"""<p>目的模板名称</p>
        :rtype: str
        """
        return self._ParameterName

    @ParameterName.setter
    def ParameterName(self, ParameterName):
        self._ParameterName = ParameterName

    @property
    def ProtocolPortName(self):
        r"""<p>端口模板名称</p>
        :rtype: str
        """
        return self._ProtocolPortName

    @ProtocolPortName.setter
    def ProtocolPortName(self, ProtocolPortName):
        self._ProtocolPortName = ProtocolPortName

    @property
    def Id(self):
        r"""<p>规则id  等同RuleUuid</p>
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def DnsParseCount(self):
        r"""<p>域名解析的IP统计</p>
        :rtype: :class:`tencentcloud.fwm.v20250611.models.SgDnsParseCount`
        """
        return self._DnsParseCount

    @DnsParseCount.setter
    def DnsParseCount(self, DnsParseCount):
        self._DnsParseCount = DnsParseCount

    @property
    def Scope(self):
        r"""<p>规则生效范围</p>
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def IsNew(self):
        r"""<p>规则最近一次是否有改动 取值范围：0/1 0:否 1:是</p>
        :rtype: int
        """
        return self._IsNew

    @IsNew.setter
    def IsNew(self, IsNew):
        self._IsNew = IsNew

    @property
    def BelongMember(self):
        r"""<p>规则归属的成员账号（当FwGroupId为cfwg-xxx或SourceType/DestType为instance/tag时必填)</p>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._BelongMember

    @BelongMember.setter
    def BelongMember(self, BelongMember):
        self._BelongMember = BelongMember


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._RuleId = params.get("RuleId")
        self._IpVersion = params.get("IpVersion")
        self._SourceId = params.get("SourceId")
        self._SourceType = params.get("SourceType")
        self._TargetId = params.get("TargetId")
        self._TargetType = params.get("TargetType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._Strategy = params.get("Strategy")
        self._Detail = params.get("Detail")
        self._Region = params.get("Region")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._SouInstanceName = params.get("SouInstanceName")
        self._SouPublicIp = params.get("SouPublicIp")
        self._SouPrivateIp = params.get("SouPrivateIp")
        self._SouCidr = params.get("SouCidr")
        self._SouParameterName = params.get("SouParameterName")
        self._InstanceName = params.get("InstanceName")
        self._PublicIp = params.get("PublicIp")
        self._PrivateIp = params.get("PrivateIp")
        self._Cidr = params.get("Cidr")
        self._ParameterName = params.get("ParameterName")
        self._ProtocolPortName = params.get("ProtocolPortName")
        self._Id = params.get("Id")
        if params.get("DnsParseCount") is not None:
            self._DnsParseCount = SgDnsParseCount()
            self._DnsParseCount._deserialize(params.get("DnsParseCount"))
        self._Scope = params.get("Scope")
        self._IsNew = params.get("IsNew")
        if params.get("BelongMember") is not None:
            self._BelongMember = MemberInfo()
            self._BelongMember._deserialize(params.get("BelongMember"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRiskPolicy(AbstractModel):
    r"""安全组风险规则详情

    """

    def __init__(self):
        r"""
        :param _PolicyIndex: 安全组规则索引号
        :type PolicyIndex: int
        :param _Protocol:  协议, 取值: TCP,UDP,ICMP,ICMPv6,ALL。
        :type Protocol: str
        :param _Port: 端口(all, 离散port,  range)。
        :type Port: str
        :param _ServiceTemplate: 端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。
        :type ServiceTemplate: :class:`tencentcloud.fwm.v20250611.models.ServiceTemplateSpecification`
        :param _CidrBlock: 网段或IP(互斥)。
        :type CidrBlock: str
        :param _Ipv6CidrBlock: 网段或IPv6(互斥)。
        :type Ipv6CidrBlock: str
        :param _SecurityGroupId: 安全组实例ID，例如：sg-ohuuioma。
        :type SecurityGroupId: str
        :param _AddressTemplate: IP地址ID或者ID地址组ID。
        :type AddressTemplate: :class:`tencentcloud.fwm.v20250611.models.AddressTemplateSpecification`
        :param _Action: 动作：ACCEPT 或 DROP。
        :type Action: str
        :param _PolicyDescription: 安全组规则描述。
        :type PolicyDescription: str
        :param _Version: 安全组规则当前版本
        :type Version: str
        :param _Direction: 规则方向，Egress出站规则，Ingress入站规则
        :type Direction: str
        :param _ModifyTime: 安全组最近修改时间。
        :type ModifyTime: str
        :param _Region: 安全组所在地域
        :type Region: str
        """
        self._PolicyIndex = None
        self._Protocol = None
        self._Port = None
        self._ServiceTemplate = None
        self._CidrBlock = None
        self._Ipv6CidrBlock = None
        self._SecurityGroupId = None
        self._AddressTemplate = None
        self._Action = None
        self._PolicyDescription = None
        self._Version = None
        self._Direction = None
        self._ModifyTime = None
        self._Region = None

    @property
    def PolicyIndex(self):
        r"""安全组规则索引号
        :rtype: int
        """
        return self._PolicyIndex

    @PolicyIndex.setter
    def PolicyIndex(self, PolicyIndex):
        self._PolicyIndex = PolicyIndex

    @property
    def Protocol(self):
        r""" 协议, 取值: TCP,UDP,ICMP,ICMPv6,ALL。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""端口(all, 离散port,  range)。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceTemplate(self):
        r"""端口ID或者协议端口组ID。ServiceTemplate和Protocol+Port互斥。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.ServiceTemplateSpecification`
        """
        return self._ServiceTemplate

    @ServiceTemplate.setter
    def ServiceTemplate(self, ServiceTemplate):
        self._ServiceTemplate = ServiceTemplate

    @property
    def CidrBlock(self):
        r"""网段或IP(互斥)。
        :rtype: str
        """
        return self._CidrBlock

    @CidrBlock.setter
    def CidrBlock(self, CidrBlock):
        self._CidrBlock = CidrBlock

    @property
    def Ipv6CidrBlock(self):
        r"""网段或IPv6(互斥)。
        :rtype: str
        """
        return self._Ipv6CidrBlock

    @Ipv6CidrBlock.setter
    def Ipv6CidrBlock(self, Ipv6CidrBlock):
        self._Ipv6CidrBlock = Ipv6CidrBlock

    @property
    def SecurityGroupId(self):
        r"""安全组实例ID，例如：sg-ohuuioma。
        :rtype: str
        """
        return self._SecurityGroupId

    @SecurityGroupId.setter
    def SecurityGroupId(self, SecurityGroupId):
        self._SecurityGroupId = SecurityGroupId

    @property
    def AddressTemplate(self):
        r"""IP地址ID或者ID地址组ID。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.AddressTemplateSpecification`
        """
        return self._AddressTemplate

    @AddressTemplate.setter
    def AddressTemplate(self, AddressTemplate):
        self._AddressTemplate = AddressTemplate

    @property
    def Action(self):
        r"""动作：ACCEPT 或 DROP。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def PolicyDescription(self):
        r"""安全组规则描述。
        :rtype: str
        """
        return self._PolicyDescription

    @PolicyDescription.setter
    def PolicyDescription(self, PolicyDescription):
        self._PolicyDescription = PolicyDescription

    @property
    def Version(self):
        r"""安全组规则当前版本
        :rtype: str
        """
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def Direction(self):
        r"""规则方向，Egress出站规则，Ingress入站规则
        :rtype: str
        """
        return self._Direction

    @Direction.setter
    def Direction(self, Direction):
        self._Direction = Direction

    @property
    def ModifyTime(self):
        r"""安全组最近修改时间。
        :rtype: str
        """
        return self._ModifyTime

    @ModifyTime.setter
    def ModifyTime(self, ModifyTime):
        self._ModifyTime = ModifyTime

    @property
    def Region(self):
        r"""安全组所在地域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._PolicyIndex = params.get("PolicyIndex")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        if params.get("ServiceTemplate") is not None:
            self._ServiceTemplate = ServiceTemplateSpecification()
            self._ServiceTemplate._deserialize(params.get("ServiceTemplate"))
        self._CidrBlock = params.get("CidrBlock")
        self._Ipv6CidrBlock = params.get("Ipv6CidrBlock")
        self._SecurityGroupId = params.get("SecurityGroupId")
        if params.get("AddressTemplate") is not None:
            self._AddressTemplate = AddressTemplateSpecification()
            self._AddressTemplate._deserialize(params.get("AddressTemplate"))
        self._Action = params.get("Action")
        self._PolicyDescription = params.get("PolicyDescription")
        self._Version = params.get("Version")
        self._Direction = params.get("Direction")
        self._ModifyTime = params.get("ModifyTime")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityGroupRule(AbstractModel):
    r"""规则数据结构描述

    """

    def __init__(self):
        r"""
        :param _IpVersion: ip类型
        :type IpVersion: str
        :param _SourceContent: 源地址
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceContent: str
        :param _SourceType: 源类型
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceType: str
        :param _DestContent: 目的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type DestContent: str
        :param _DestType: 目的类型
注意：此字段可能返回 null，表示取不到有效值。
        :type DestType: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param _ServiceTemplateId: 模板
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceTemplateId: str
        :param _RuleAction: 动作
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleAction: str
        :param _Description: 描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _OrderIndex: 优先级
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderIndex: int
        :param _RuleId: rule id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param _Scope: 生效范围
注意：此字段可能返回 null，表示取不到有效值。
        :type Scope: str
        :param _ProtocolPortType: 端口类型
        :type ProtocolPortType: int
        :param _BelongMemberId: 规则归属的成员账号ID（当FwGroupId为cfwg-xxx或SourceType/DestType为instance/tag时必填）
        :type BelongMemberId: str
        """
        self._IpVersion = None
        self._SourceContent = None
        self._SourceType = None
        self._DestContent = None
        self._DestType = None
        self._Protocol = None
        self._Port = None
        self._ServiceTemplateId = None
        self._RuleAction = None
        self._Description = None
        self._OrderIndex = None
        self._RuleId = None
        self._Scope = None
        self._ProtocolPortType = None
        self._BelongMemberId = None

    @property
    def IpVersion(self):
        r"""ip类型
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def SourceContent(self):
        r"""源地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""源类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DestContent(self):
        r"""目的地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        r"""目的类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def Protocol(self):
        r"""协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ServiceTemplateId(self):
        r"""模板
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def RuleAction(self):
        r"""动作
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        r"""描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def OrderIndex(self):
        r"""优先级
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def RuleId(self):
        r"""rule id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Scope(self):
        r"""生效范围
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope

    @property
    def ProtocolPortType(self):
        r"""端口类型
        :rtype: int
        """
        return self._ProtocolPortType

    @ProtocolPortType.setter
    def ProtocolPortType(self, ProtocolPortType):
        self._ProtocolPortType = ProtocolPortType

    @property
    def BelongMemberId(self):
        r"""规则归属的成员账号ID（当FwGroupId为cfwg-xxx或SourceType/DestType为instance/tag时必填）
        :rtype: str
        """
        return self._BelongMemberId

    @BelongMemberId.setter
    def BelongMemberId(self, BelongMemberId):
        self._BelongMemberId = BelongMemberId


    def _deserialize(self, params):
        self._IpVersion = params.get("IpVersion")
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._OrderIndex = params.get("OrderIndex")
        self._RuleId = params.get("RuleId")
        self._Scope = params.get("Scope")
        self._ProtocolPortType = params.get("ProtocolPortType")
        self._BelongMemberId = params.get("BelongMemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SequenceIndex(AbstractModel):
    r"""规则序号调整结构

    """

    def __init__(self):
        r"""
        :param _OrderIndex: 原规则序号
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderIndex: int
        :param _NewOrderIndex: 新规则序号
注意：此字段可能返回 null，表示取不到有效值。
        :type NewOrderIndex: int
        """
        self._OrderIndex = None
        self._NewOrderIndex = None

    @property
    def OrderIndex(self):
        r"""原规则序号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def NewOrderIndex(self):
        r"""新规则序号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._NewOrderIndex

    @NewOrderIndex.setter
    def NewOrderIndex(self, NewOrderIndex):
        self._NewOrderIndex = NewOrderIndex


    def _deserialize(self, params):
        self._OrderIndex = params.get("OrderIndex")
        self._NewOrderIndex = params.get("NewOrderIndex")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServiceTemplateSpecification(AbstractModel):
    r"""安全组服务模板

    """

    def __init__(self):
        r"""
        :param _ServiceId:  协议端口ID，例如：ppm-f5n1f8da。
        :type ServiceId: str
        :param _ServiceGroupId: 协议端口组ID，例如：ppmg-f5n1f8da
        :type ServiceGroupId: str
        """
        self._ServiceId = None
        self._ServiceGroupId = None

    @property
    def ServiceId(self):
        r""" 协议端口ID，例如：ppm-f5n1f8da。
        :rtype: str
        """
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceGroupId(self):
        r"""协议端口组ID，例如：ppmg-f5n1f8da
        :rtype: str
        """
        return self._ServiceGroupId

    @ServiceGroupId.setter
    def ServiceGroupId(self, ServiceGroupId):
        self._ServiceGroupId = ServiceGroupId


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceGroupId = params.get("ServiceGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SgDnsParseCount(AbstractModel):
    r"""企业安全组域名解析的IP统计

    """

    def __init__(self):
        r"""
        :param _ValidCount: 有效下发的IP个数，离散数据
        :type ValidCount: int
        :param _InvalidCount: 未下发的IP个数，离散数据
        :type InvalidCount: int
        """
        self._ValidCount = None
        self._InvalidCount = None

    @property
    def ValidCount(self):
        r"""有效下发的IP个数，离散数据
        :rtype: int
        """
        return self._ValidCount

    @ValidCount.setter
    def ValidCount(self, ValidCount):
        self._ValidCount = ValidCount

    @property
    def InvalidCount(self):
        r"""未下发的IP个数，离散数据
        :rtype: int
        """
        return self._InvalidCount

    @InvalidCount.setter
    def InvalidCount(self, InvalidCount):
        self._InvalidCount = InvalidCount


    def _deserialize(self, params):
        self._ValidCount = params.get("ValidCount")
        self._InvalidCount = params.get("InvalidCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SgRuleResp(AbstractModel):
    r"""规则列表响应数据结构

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则Id
        :type RuleId: str
        :param _Sequence: 优先级
        :type Sequence: int
        :param _Region: 区域
        :type Region: str
        :param _IpVersion: ip类型
        :type IpVersion: str
        :param _SrcContent: 源内容
        :type SrcContent: str
        :param _SrcType: 源类型
        :type SrcType: str
        :param _DstContent: 目的内容
        :type DstContent: str
        :param _DstType: 目的类型
        :type DstType: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _ProtocolPortType: 协议端口参数模板
        :type ProtocolPortType: int
        :param _ServiceTemplateId: 协议端口参数模板id
        :type ServiceTemplateId: str
        :param _DstPort: 端口段,支持单端口,多端口和端口段
        :type DstPort: str
        :param _RuleAction: 策略，1阻断，2放行
        :type RuleAction: str
        :param _Detail: 描述
        :type Detail: str
        :param _RuleSource: 规则来源，0为用户控制台添加
        :type RuleSource: str
        :param _Scope: 生效范围,字节位,1:SG 企业安全组,2:LH 轻量服务器
        :type Scope: str
        """
        self._RuleId = None
        self._Sequence = None
        self._Region = None
        self._IpVersion = None
        self._SrcContent = None
        self._SrcType = None
        self._DstContent = None
        self._DstType = None
        self._Protocol = None
        self._ProtocolPortType = None
        self._ServiceTemplateId = None
        self._DstPort = None
        self._RuleAction = None
        self._Detail = None
        self._RuleSource = None
        self._Scope = None

    @property
    def RuleId(self):
        r"""规则Id
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Sequence(self):
        r"""优先级
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def Region(self):
        r"""区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def IpVersion(self):
        r"""ip类型
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def SrcContent(self):
        r"""源内容
        :rtype: str
        """
        return self._SrcContent

    @SrcContent.setter
    def SrcContent(self, SrcContent):
        self._SrcContent = SrcContent

    @property
    def SrcType(self):
        r"""源类型
        :rtype: str
        """
        return self._SrcType

    @SrcType.setter
    def SrcType(self, SrcType):
        self._SrcType = SrcType

    @property
    def DstContent(self):
        r"""目的内容
        :rtype: str
        """
        return self._DstContent

    @DstContent.setter
    def DstContent(self, DstContent):
        self._DstContent = DstContent

    @property
    def DstType(self):
        r"""目的类型
        :rtype: str
        """
        return self._DstType

    @DstType.setter
    def DstType(self, DstType):
        self._DstType = DstType

    @property
    def Protocol(self):
        r"""协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def ProtocolPortType(self):
        r"""协议端口参数模板
        :rtype: int
        """
        return self._ProtocolPortType

    @ProtocolPortType.setter
    def ProtocolPortType(self, ProtocolPortType):
        self._ProtocolPortType = ProtocolPortType

    @property
    def ServiceTemplateId(self):
        r"""协议端口参数模板id
        :rtype: str
        """
        return self._ServiceTemplateId

    @ServiceTemplateId.setter
    def ServiceTemplateId(self, ServiceTemplateId):
        self._ServiceTemplateId = ServiceTemplateId

    @property
    def DstPort(self):
        r"""端口段,支持单端口,多端口和端口段
        :rtype: str
        """
        return self._DstPort

    @DstPort.setter
    def DstPort(self, DstPort):
        self._DstPort = DstPort

    @property
    def RuleAction(self):
        r"""策略，1阻断，2放行
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Detail(self):
        r"""描述
        :rtype: str
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def RuleSource(self):
        r"""规则来源，0为用户控制台添加
        :rtype: str
        """
        return self._RuleSource

    @RuleSource.setter
    def RuleSource(self, RuleSource):
        self._RuleSource = RuleSource

    @property
    def Scope(self):
        r"""生效范围,字节位,1:SG 企业安全组,2:LH 轻量服务器
        :rtype: str
        """
        return self._Scope

    @Scope.setter
    def Scope(self, Scope):
        self._Scope = Scope


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Sequence = params.get("Sequence")
        self._Region = params.get("Region")
        self._IpVersion = params.get("IpVersion")
        self._SrcContent = params.get("SrcContent")
        self._SrcType = params.get("SrcType")
        self._DstContent = params.get("DstContent")
        self._DstType = params.get("DstType")
        self._Protocol = params.get("Protocol")
        self._ProtocolPortType = params.get("ProtocolPortType")
        self._ServiceTemplateId = params.get("ServiceTemplateId")
        self._DstPort = params.get("DstPort")
        self._RuleAction = params.get("RuleAction")
        self._Detail = params.get("Detail")
        self._RuleSource = params.get("RuleSource")
        self._Scope = params.get("Scope")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StrategyReq(AbstractModel):
    r"""创建策略的策略数据结构

    """

    def __init__(self):
        r"""
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _Sequence: 优先级
        :type Sequence: int
        """
        self._GroupId = None
        self._Sequence = None

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def Sequence(self):
        r"""优先级
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._GroupId = params.get("GroupId")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StrategyResp(AbstractModel):
    r"""查询策略时策略列表参数

    """

    def __init__(self):
        r"""
        :param _StrategyId: 策略Id
        :type StrategyId: str
        :param _GroupId: 规则组Id
        :type GroupId: str
        :param _GroupName: 规则组名称
        :type GroupName: str
        :param _RuleCount: 规则数
        :type RuleCount: int
        :param _RuleStatus: 策略状态
        :type RuleStatus: int
        :param _ReceiveAccount: 下发账号
        :type ReceiveAccount: list of ReceiveAccount
        :param _Sequence: 优先级
        :type Sequence: int
        :param _ErrMsg: 下发失败原因
        :type ErrMsg: str
        :param _ErrorType: 下发失败原因类型
        :type ErrorType: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _CreateBy: 创建人
        :type CreateBy: str
        :param _UpdateBy: 更新人
        :type UpdateBy: str
        :param _ExecArea: 执行区域
        :type ExecArea: str
        :param _CreateName: 创建人名称
        :type CreateName: str
        :param _UpdateName: 更新人名称
        :type UpdateName: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        """
        self._StrategyId = None
        self._GroupId = None
        self._GroupName = None
        self._RuleCount = None
        self._RuleStatus = None
        self._ReceiveAccount = None
        self._Sequence = None
        self._ErrMsg = None
        self._ErrorType = None
        self._UpdateTime = None
        self._CreateBy = None
        self._UpdateBy = None
        self._ExecArea = None
        self._CreateName = None
        self._UpdateName = None
        self._CreateTime = None

    @property
    def StrategyId(self):
        r"""策略Id
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def GroupId(self):
        r"""规则组Id
        :rtype: str
        """
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def GroupName(self):
        r"""规则组名称
        :rtype: str
        """
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def RuleCount(self):
        r"""规则数
        :rtype: int
        """
        return self._RuleCount

    @RuleCount.setter
    def RuleCount(self, RuleCount):
        self._RuleCount = RuleCount

    @property
    def RuleStatus(self):
        r"""策略状态
        :rtype: int
        """
        return self._RuleStatus

    @RuleStatus.setter
    def RuleStatus(self, RuleStatus):
        self._RuleStatus = RuleStatus

    @property
    def ReceiveAccount(self):
        r"""下发账号
        :rtype: list of ReceiveAccount
        """
        return self._ReceiveAccount

    @ReceiveAccount.setter
    def ReceiveAccount(self, ReceiveAccount):
        self._ReceiveAccount = ReceiveAccount

    @property
    def Sequence(self):
        r"""优先级
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def ErrMsg(self):
        r"""下发失败原因
        :rtype: str
        """
        return self._ErrMsg

    @ErrMsg.setter
    def ErrMsg(self, ErrMsg):
        self._ErrMsg = ErrMsg

    @property
    def ErrorType(self):
        r"""下发失败原因类型
        :rtype: str
        """
        return self._ErrorType

    @ErrorType.setter
    def ErrorType(self, ErrorType):
        self._ErrorType = ErrorType

    @property
    def UpdateTime(self):
        r"""更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateBy(self):
        r"""创建人
        :rtype: str
        """
        return self._CreateBy

    @CreateBy.setter
    def CreateBy(self, CreateBy):
        self._CreateBy = CreateBy

    @property
    def UpdateBy(self):
        r"""更新人
        :rtype: str
        """
        return self._UpdateBy

    @UpdateBy.setter
    def UpdateBy(self, UpdateBy):
        self._UpdateBy = UpdateBy

    @property
    def ExecArea(self):
        r"""执行区域
        :rtype: str
        """
        return self._ExecArea

    @ExecArea.setter
    def ExecArea(self, ExecArea):
        self._ExecArea = ExecArea

    @property
    def CreateName(self):
        r"""创建人名称
        :rtype: str
        """
        return self._CreateName

    @CreateName.setter
    def CreateName(self, CreateName):
        self._CreateName = CreateName

    @property
    def UpdateName(self):
        r"""更新人名称
        :rtype: str
        """
        return self._UpdateName

    @UpdateName.setter
    def UpdateName(self, UpdateName):
        self._UpdateName = UpdateName

    @property
    def CreateTime(self):
        r"""创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._StrategyId = params.get("StrategyId")
        self._GroupId = params.get("GroupId")
        self._GroupName = params.get("GroupName")
        self._RuleCount = params.get("RuleCount")
        self._RuleStatus = params.get("RuleStatus")
        if params.get("ReceiveAccount") is not None:
            self._ReceiveAccount = []
            for item in params.get("ReceiveAccount"):
                obj = ReceiveAccount()
                obj._deserialize(item)
                self._ReceiveAccount.append(obj)
        self._Sequence = params.get("Sequence")
        self._ErrMsg = params.get("ErrMsg")
        self._ErrorType = params.get("ErrorType")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateBy = params.get("CreateBy")
        self._UpdateBy = params.get("UpdateBy")
        self._ExecArea = params.get("ExecArea")
        self._CreateName = params.get("CreateName")
        self._UpdateName = params.get("UpdateName")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcAclRule(AbstractModel):
    r"""VPC边界规则

    """

    def __init__(self):
        r"""
        :param _SourceContent: 源地址内容
        :type SourceContent: str
        :param _SourceType: 源类型：ip/url/template/instance/tag
        :type SourceType: str
        :param _DestContent: 目的地址内容
        :type DestContent: str
        :param _DestType: 目的类型：ip/url/template/instance/tag
        :type DestType: str
        :param _Protocol: 协议：TCP/UDP/ICMP/ANY/HTTP/HTTPS/DNS/FTP等
        :type Protocol: str
        :param _RuleAction: 动作：accept/drop/log
        :type RuleAction: str
        :param _OrderIndex: 优先级（从1开始）
        :type OrderIndex: int
        :param _EdgeId: 边界防火墙ID：ALL表示全局，CFWS-xxx表示指定边界
        :type EdgeId: str
        :param _FwGroupId: 防火墙实例ID（规则生效范围）：ALL-全局生效，ccn-xxx-云联网实例，cfwg-xxx-防火墙组实例
        :type FwGroupId: str
        :param _RuleId: 规则ID（修改时必填）
        :type RuleId: str
        :param _Port: 端口（ICMP协议时为空）
        :type Port: str
        :param _Description: 规则描述
        :type Description: str
        :param _ParamTemplateId: 端口模板ID
        :type ParamTemplateId: str
        :param _BelongMemberId: 规则归属的成员账号ID（当FwGroupId为cfwg-xxx或SourceType/DestType为instance/tag时必填）
        :type BelongMemberId: str
        """
        self._SourceContent = None
        self._SourceType = None
        self._DestContent = None
        self._DestType = None
        self._Protocol = None
        self._RuleAction = None
        self._OrderIndex = None
        self._EdgeId = None
        self._FwGroupId = None
        self._RuleId = None
        self._Port = None
        self._Description = None
        self._ParamTemplateId = None
        self._BelongMemberId = None

    @property
    def SourceContent(self):
        r"""源地址内容
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""源类型：ip/url/template/instance/tag
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def DestContent(self):
        r"""目的地址内容
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        r"""目的类型：ip/url/template/instance/tag
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def Protocol(self):
        r"""协议：TCP/UDP/ICMP/ANY/HTTP/HTTPS/DNS/FTP等
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def RuleAction(self):
        r"""动作：accept/drop/log
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def OrderIndex(self):
        r"""优先级（从1开始）
        :rtype: int
        """
        return self._OrderIndex

    @OrderIndex.setter
    def OrderIndex(self, OrderIndex):
        self._OrderIndex = OrderIndex

    @property
    def EdgeId(self):
        r"""边界防火墙ID：ALL表示全局，CFWS-xxx表示指定边界
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def FwGroupId(self):
        r"""防火墙实例ID（规则生效范围）：ALL-全局生效，ccn-xxx-云联网实例，cfwg-xxx-防火墙组实例
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def RuleId(self):
        r"""规则ID（修改时必填）
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Port(self):
        r"""端口（ICMP协议时为空）
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Description(self):
        r"""规则描述
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def ParamTemplateId(self):
        r"""端口模板ID
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def BelongMemberId(self):
        r"""规则归属的成员账号ID（当FwGroupId为cfwg-xxx或SourceType/DestType为instance/tag时必填）
        :rtype: str
        """
        return self._BelongMemberId

    @BelongMemberId.setter
    def BelongMemberId(self, BelongMemberId):
        self._BelongMemberId = BelongMemberId


    def _deserialize(self, params):
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._Protocol = params.get("Protocol")
        self._RuleAction = params.get("RuleAction")
        self._OrderIndex = params.get("OrderIndex")
        self._EdgeId = params.get("EdgeId")
        self._FwGroupId = params.get("FwGroupId")
        self._RuleId = params.get("RuleId")
        self._Port = params.get("Port")
        self._Description = params.get("Description")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._BelongMemberId = params.get("BelongMemberId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcAclRuleResp(AbstractModel):
    r"""VPC边界规则响应结构

    """

    def __init__(self):
        r"""
        :param _RuleId: 规则ID
        :type RuleId: str
        :param _Sequence: 优先级
        :type Sequence: int
        :param _IpVersion: IP版本：ipv4或ipv6
        :type IpVersion: str
        :param _SourceContent: 源地址内容
        :type SourceContent: str
        :param _SourceType: 源类型
        :type SourceType: str
        :param _SourceName: 源资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceName: str
        :param _DestContent: 目的地址内容
        :type DestContent: str
        :param _DestType: 目的类型
        :type DestType: str
        :param _DestName: 目的资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :type DestName: str
        :param _Protocol: 协议
        :type Protocol: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: str
        :param _ParamTemplateId: 端口模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateId: str
        :param _ParamTemplateName: 端口模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamTemplateName: str
        :param _RuleAction: 动作：accept/drop/log
        :type RuleAction: str
        :param _Description: 规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Description: str
        :param _EdgeId: 边界防火墙ID
        :type EdgeId: str
        :param _FwGroupId: 防火墙实例ID
        :type FwGroupId: str
        :param _Invalid: 规则是否失效：0-有效，1-失效
        :type Invalid: int
        :param _BelongMember: 规则归属的成员账号
注意：此字段可能返回 null，表示取不到有效值。
        :type BelongMember: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        :param _CreateTime: 规则创建时间
        :type CreateTime: str
        :param _UpdateTime: 规则修改时间
        :type UpdateTime: str
        :param _DnsParseCnt: 域名数
        :type DnsParseCnt: int
        :param _FwGroupName: 防火墙组名称
        :type FwGroupName: str
        """
        self._RuleId = None
        self._Sequence = None
        self._IpVersion = None
        self._SourceContent = None
        self._SourceType = None
        self._SourceName = None
        self._DestContent = None
        self._DestType = None
        self._DestName = None
        self._Protocol = None
        self._Port = None
        self._ParamTemplateId = None
        self._ParamTemplateName = None
        self._RuleAction = None
        self._Description = None
        self._EdgeId = None
        self._FwGroupId = None
        self._Invalid = None
        self._BelongMember = None
        self._CreateTime = None
        self._UpdateTime = None
        self._DnsParseCnt = None
        self._FwGroupName = None

    @property
    def RuleId(self):
        r"""规则ID
        :rtype: str
        """
        return self._RuleId

    @RuleId.setter
    def RuleId(self, RuleId):
        self._RuleId = RuleId

    @property
    def Sequence(self):
        r"""优先级
        :rtype: int
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence

    @property
    def IpVersion(self):
        r"""IP版本：ipv4或ipv6
        :rtype: str
        """
        return self._IpVersion

    @IpVersion.setter
    def IpVersion(self, IpVersion):
        self._IpVersion = IpVersion

    @property
    def SourceContent(self):
        r"""源地址内容
        :rtype: str
        """
        return self._SourceContent

    @SourceContent.setter
    def SourceContent(self, SourceContent):
        self._SourceContent = SourceContent

    @property
    def SourceType(self):
        r"""源类型
        :rtype: str
        """
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def SourceName(self):
        r"""源资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SourceName

    @SourceName.setter
    def SourceName(self, SourceName):
        self._SourceName = SourceName

    @property
    def DestContent(self):
        r"""目的地址内容
        :rtype: str
        """
        return self._DestContent

    @DestContent.setter
    def DestContent(self, DestContent):
        self._DestContent = DestContent

    @property
    def DestType(self):
        r"""目的类型
        :rtype: str
        """
        return self._DestType

    @DestType.setter
    def DestType(self, DestType):
        self._DestType = DestType

    @property
    def DestName(self):
        r"""目的资产名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DestName

    @DestName.setter
    def DestName(self, DestName):
        self._DestName = DestName

    @property
    def Protocol(self):
        r"""协议
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Port(self):
        r"""端口
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def ParamTemplateId(self):
        r"""端口模板ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateId

    @ParamTemplateId.setter
    def ParamTemplateId(self, ParamTemplateId):
        self._ParamTemplateId = ParamTemplateId

    @property
    def ParamTemplateName(self):
        r"""端口模板名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParamTemplateName

    @ParamTemplateName.setter
    def ParamTemplateName(self, ParamTemplateName):
        self._ParamTemplateName = ParamTemplateName

    @property
    def RuleAction(self):
        r"""动作：accept/drop/log
        :rtype: str
        """
        return self._RuleAction

    @RuleAction.setter
    def RuleAction(self, RuleAction):
        self._RuleAction = RuleAction

    @property
    def Description(self):
        r"""规则描述
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Description

    @Description.setter
    def Description(self, Description):
        self._Description = Description

    @property
    def EdgeId(self):
        r"""边界防火墙ID
        :rtype: str
        """
        return self._EdgeId

    @EdgeId.setter
    def EdgeId(self, EdgeId):
        self._EdgeId = EdgeId

    @property
    def FwGroupId(self):
        r"""防火墙实例ID
        :rtype: str
        """
        return self._FwGroupId

    @FwGroupId.setter
    def FwGroupId(self, FwGroupId):
        self._FwGroupId = FwGroupId

    @property
    def Invalid(self):
        r"""规则是否失效：0-有效，1-失效
        :rtype: int
        """
        return self._Invalid

    @Invalid.setter
    def Invalid(self, Invalid):
        self._Invalid = Invalid

    @property
    def BelongMember(self):
        r"""规则归属的成员账号
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.fwm.v20250611.models.MemberInfo`
        """
        return self._BelongMember

    @BelongMember.setter
    def BelongMember(self, BelongMember):
        self._BelongMember = BelongMember

    @property
    def CreateTime(self):
        r"""规则创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        r"""规则修改时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def DnsParseCnt(self):
        r"""域名数
        :rtype: int
        """
        return self._DnsParseCnt

    @DnsParseCnt.setter
    def DnsParseCnt(self, DnsParseCnt):
        self._DnsParseCnt = DnsParseCnt

    @property
    def FwGroupName(self):
        r"""防火墙组名称
        :rtype: str
        """
        return self._FwGroupName

    @FwGroupName.setter
    def FwGroupName(self, FwGroupName):
        self._FwGroupName = FwGroupName


    def _deserialize(self, params):
        self._RuleId = params.get("RuleId")
        self._Sequence = params.get("Sequence")
        self._IpVersion = params.get("IpVersion")
        self._SourceContent = params.get("SourceContent")
        self._SourceType = params.get("SourceType")
        self._SourceName = params.get("SourceName")
        self._DestContent = params.get("DestContent")
        self._DestType = params.get("DestType")
        self._DestName = params.get("DestName")
        self._Protocol = params.get("Protocol")
        self._Port = params.get("Port")
        self._ParamTemplateId = params.get("ParamTemplateId")
        self._ParamTemplateName = params.get("ParamTemplateName")
        self._RuleAction = params.get("RuleAction")
        self._Description = params.get("Description")
        self._EdgeId = params.get("EdgeId")
        self._FwGroupId = params.get("FwGroupId")
        self._Invalid = params.get("Invalid")
        if params.get("BelongMember") is not None:
            self._BelongMember = MemberInfo()
            self._BelongMember._deserialize(params.get("BelongMember"))
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._DnsParseCnt = params.get("DnsParseCnt")
        self._FwGroupName = params.get("FwGroupName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        