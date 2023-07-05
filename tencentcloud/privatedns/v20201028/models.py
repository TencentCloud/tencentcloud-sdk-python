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


class AccountVpcInfo(AbstractModel):
    """私有域解析账号Vpc信息

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: VpcId： vpc-xadsafsdasd
        :type UniqVpcId: str
        :param _Region: Vpc所属地区: ap-guangzhou, ap-shanghai
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Uin: Vpc所属账号: 123456789
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param _VpcName: vpc资源名称：testname
注意：此字段可能返回 null，表示取不到有效值。
        :type VpcName: str
        """
        self._UniqVpcId = None
        self._Region = None
        self._Uin = None
        self._VpcName = None

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        self._Uin = params.get("Uin")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOut(AbstractModel):
    """查询关联账号VPC列表出参

    """

    def __init__(self):
        r"""
        :param _VpcId: VpcId： vpc-xadsafsdasd
        :type VpcId: str
        :param _Region: Vpc所属地区: ap-guangzhou, ap-shanghai
        :type Region: str
        :param _Uin: Vpc所属账号: 123456789
        :type Uin: str
        :param _VpcName: vpc资源名称：testname
        :type VpcName: str
        """
        self._VpcId = None
        self._Region = None
        self._Uin = None
        self._VpcName = None

    @property
    def VpcId(self):
        return self._VpcId

    @VpcId.setter
    def VpcId(self, VpcId):
        self._VpcId = VpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def VpcName(self):
        return self._VpcName

    @VpcName.setter
    def VpcName(self, VpcName):
        self._VpcName = VpcName


    def _deserialize(self, params):
        self._VpcId = params.get("VpcId")
        self._Region = params.get("Region")
        self._Uin = params.get("Uin")
        self._VpcName = params.get("VpcName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccountVpcInfoOutput(AbstractModel):
    """关联的VPC出参

    """

    def __init__(self):
        r"""
        :param _Uin: 关联账户的uin
        :type Uin: str
        :param _UniqVpcId: vpcid
        :type UniqVpcId: str
        :param _Region: 地域
        :type Region: str
        """
        self._Uin = None
        self._UniqVpcId = None
        self._Region = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLog(AbstractModel):
    """操作日志

    """

    def __init__(self):
        r"""
        :param _Resource: 日志类型
        :type Resource: str
        :param _Metric: 日志表名
        :type Metric: str
        :param _TotalCount: 日志总数
        :type TotalCount: int
        :param _DataSet: 日志列表
        :type DataSet: list of AuditLogInfo
        """
        self._Resource = None
        self._Metric = None
        self._TotalCount = None
        self._DataSet = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Metric = params.get("Metric")
        self._TotalCount = params.get("TotalCount")
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = AuditLogInfo()
                obj._deserialize(item)
                self._DataSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuditLogInfo(AbstractModel):
    """日志详情

    """

    def __init__(self):
        r"""
        :param _Date: 时间
        :type Date: str
        :param _OperatorUin: 操作人uin
        :type OperatorUin: str
        :param _Content: 日志内容
        :type Content: str
        """
        self._Date = None
        self._OperatorUin = None
        self._Content = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def OperatorUin(self):
        return self._OperatorUin

    @OperatorUin.setter
    def OperatorUin(self, OperatorUin):
        self._OperatorUin = OperatorUin

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._OperatorUin = params.get("OperatorUin")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateDNSAccountRequest(AbstractModel):
    """CreatePrivateDNSAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Account: 私有域解析账号
        :type Account: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        self._Account = None

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = PrivateDNSAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateDNSAccountResponse(AbstractModel):
    """CreatePrivateDNSAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreatePrivateZoneRecordRequest(AbstractModel):
    """CreatePrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _SubDomain: 子域名，例如 "www", "m", "@"
        :type SubDomain: str
        :param _RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :type RecordValue: str
        :param _Weight: 记录权重，值为1-100
        :type Weight: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        """
        self._ZoneId = None
        self._RecordType = None
        self._SubDomain = None
        self._RecordValue = None
        self._Weight = None
        self._MX = None
        self._TTL = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordType = params.get("RecordType")
        self._SubDomain = params.get("SubDomain")
        self._RecordValue = params.get("RecordValue")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneRecordResponse(AbstractModel):
    """CreatePrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录Id
        :type RecordId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RecordId = None
        self._RequestId = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._RequestId = params.get("RequestId")


class CreatePrivateZoneRequest(AbstractModel):
    """CreatePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名，格式必须是标准的TLD
        :type Domain: str
        :param _TagSet: 创建私有域的同时，为其打上标签
        :type TagSet: list of TagInfo
        :param _VpcSet: 创建私有域的同时，将其关联至VPC
        :type VpcSet: list of VpcInfo
        :param _Remark: 备注
        :type Remark: str
        :param _DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED。默认值为ENABLED
        :type DnsForwardStatus: str
        :param _Vpcs: 创建私有域的同时，将其关联至VPC
        :type Vpcs: list of VpcInfo
        :param _AccountVpcSet: 创建私有域同时绑定关联账号的VPC
        :type AccountVpcSet: list of AccountVpcInfo
        :param _CnameSpeedupStatus: 是否CNAME加速：ENABLED，DISABLED，默认值为ENABLED
        :type CnameSpeedupStatus: str
        """
        self._Domain = None
        self._TagSet = None
        self._VpcSet = None
        self._Remark = None
        self._DnsForwardStatus = None
        self._Vpcs = None
        self._AccountVpcSet = None
        self._CnameSpeedupStatus = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TagSet(self):
        return self._TagSet

    @TagSet.setter
    def TagSet(self, TagSet):
        self._TagSet = TagSet

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DnsForwardStatus(self):
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Vpcs(self):
        return self._Vpcs

    @Vpcs.setter
    def Vpcs(self, Vpcs):
        self._Vpcs = Vpcs

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def CnameSpeedupStatus(self):
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("TagSet") is not None:
            self._TagSet = []
            for item in params.get("TagSet"):
                obj = TagInfo()
                obj._deserialize(item)
                self._TagSet.append(obj)
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._Remark = params.get("Remark")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Vpcs") is not None:
            self._Vpcs = []
            for item in params.get("Vpcs"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._Vpcs.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePrivateZoneResponse(AbstractModel):
    """CreatePrivateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID, zone-xxxxxx
        :type ZoneId: str
        :param _Domain: 私有域名
        :type Domain: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._Domain = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Domain = params.get("Domain")
        self._RequestId = params.get("RequestId")


class DatePoint(AbstractModel):
    """时间统计值

    """

    def __init__(self):
        r"""
        :param _Date: 时间
        :type Date: str
        :param _Value: 值
        :type Value: int
        """
        self._Date = None
        self._Value = None

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Date = params.get("Date")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndPointRequest(AbstractModel):
    """DeleteEndPoint请求参数结构体

    """

    def __init__(self):
        r"""
        :param _EndPointId: 终端节点ID
        :type EndPointId: str
        """
        self._EndPointId = None

    @property
    def EndPointId(self):
        return self._EndPointId

    @EndPointId.setter
    def EndPointId(self, EndPointId):
        self._EndPointId = EndPointId


    def _deserialize(self, params):
        self._EndPointId = params.get("EndPointId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteEndPointResponse(AbstractModel):
    """DeleteEndPoint返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePrivateDNSAccountRequest(AbstractModel):
    """DeletePrivateDNSAccount请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Account: 私有域解析账号
        :type Account: :class:`tencentcloud.privatedns.v20201028.models.PrivateDNSAccount`
        """
        self._Account = None

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account


    def _deserialize(self, params):
        if params.get("Account") is not None:
            self._Account = PrivateDNSAccount()
            self._Account._deserialize(params.get("Account"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateDNSAccountResponse(AbstractModel):
    """DeletePrivateDNSAccount返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePrivateZoneRecordRequest(AbstractModel):
    """DeletePrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordId: 记录ID
        :type RecordId: str
        :param _RecordIdSet: 记录ID数组，RecordId 优先
        :type RecordIdSet: list of str
        """
        self._ZoneId = None
        self._RecordId = None
        self._RecordIdSet = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordIdSet(self):
        return self._RecordIdSet

    @RecordIdSet.setter
    def RecordIdSet(self, RecordIdSet):
        self._RecordIdSet = RecordIdSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        self._RecordIdSet = params.get("RecordIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneRecordResponse(AbstractModel):
    """DeletePrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeletePrivateZoneRequest(AbstractModel):
    """DeletePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _ZoneIdSet: 私有域ID数组，ZoneId 优先
        :type ZoneIdSet: list of str
        """
        self._ZoneId = None
        self._ZoneIdSet = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def ZoneIdSet(self):
        return self._ZoneIdSet

    @ZoneIdSet.setter
    def ZoneIdSet(self, ZoneIdSet):
        self._ZoneIdSet = ZoneIdSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._ZoneIdSet = params.get("ZoneIdSet")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePrivateZoneResponse(AbstractModel):
    """DeletePrivateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeAccountVpcListRequest(AbstractModel):
    """DescribeAccountVpcList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _AccountUin: 关联账号的uin
        :type AccountUin: str
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._AccountUin = None
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def AccountUin(self):
        return self._AccountUin

    @AccountUin.setter
    def AccountUin(self, AccountUin):
        self._AccountUin = AccountUin

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._AccountUin = params.get("AccountUin")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccountVpcListResponse(AbstractModel):
    """DescribeAccountVpcList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: VPC数量
        :type TotalCount: int
        :param _VpcSet: VPC 列表
        :type VpcSet: list of AccountVpcInfoOut
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VpcSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = AccountVpcInfoOut()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeAuditLogRequest(AbstractModel):
    """DescribeAuditLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRangeBegin: 请求量统计起始时间
        :type TimeRangeBegin: str
        :param _Filters: 筛选参数：ZoneId：私有域ID；Domain：私有域；OperatorUin：操作者账号ID
        :type Filters: list of Filter
        :param _TimeRangeEnd: 请求量统计结束时间
        :type TimeRangeEnd: str
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        """
        self._TimeRangeBegin = None
        self._Filters = None
        self._TimeRangeEnd = None
        self._Offset = None
        self._Limit = None

    @property
    def TimeRangeBegin(self):
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAuditLogResponse(AbstractModel):
    """DescribeAuditLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 操作日志列表
        :type Data: list of AuditLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = AuditLog()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard请求参数结构体

    """


class DescribeDashboardResponse(AbstractModel):
    """DescribeDashboard返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneTotal: 私有域解析总数
        :type ZoneTotal: int
        :param _ZoneVpcCount: 私有域关联VPC数量
        :type ZoneVpcCount: int
        :param _RequestTotalCount: 历史请求量总数
        :type RequestTotalCount: int
        :param _FlowUsage: 流量包用量
        :type FlowUsage: list of FlowUsage
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneTotal = None
        self._ZoneVpcCount = None
        self._RequestTotalCount = None
        self._FlowUsage = None
        self._RequestId = None

    @property
    def ZoneTotal(self):
        return self._ZoneTotal

    @ZoneTotal.setter
    def ZoneTotal(self, ZoneTotal):
        self._ZoneTotal = ZoneTotal

    @property
    def ZoneVpcCount(self):
        return self._ZoneVpcCount

    @ZoneVpcCount.setter
    def ZoneVpcCount(self, ZoneVpcCount):
        self._ZoneVpcCount = ZoneVpcCount

    @property
    def RequestTotalCount(self):
        return self._RequestTotalCount

    @RequestTotalCount.setter
    def RequestTotalCount(self, RequestTotalCount):
        self._RequestTotalCount = RequestTotalCount

    @property
    def FlowUsage(self):
        return self._FlowUsage

    @FlowUsage.setter
    def FlowUsage(self, FlowUsage):
        self._FlowUsage = FlowUsage

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneTotal = params.get("ZoneTotal")
        self._ZoneVpcCount = params.get("ZoneVpcCount")
        self._RequestTotalCount = params.get("RequestTotalCount")
        if params.get("FlowUsage") is not None:
            self._FlowUsage = []
            for item in params.get("FlowUsage"):
                obj = FlowUsage()
                obj._deserialize(item)
                self._FlowUsage.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateDNSAccountListRequest(AbstractModel):
    """DescribePrivateDNSAccountList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateDNSAccountListResponse(AbstractModel):
    """DescribePrivateDNSAccountList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 私有域解析账号数量
        :type TotalCount: int
        :param _AccountSet: 私有域解析账号列表
        :type AccountSet: list of PrivateDNSAccount
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._AccountSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AccountSet(self):
        return self._AccountSet

    @AccountSet.setter
    def AccountSet(self, AccountSet):
        self._AccountSet = AccountSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("AccountSet") is not None:
            self._AccountSet = []
            for item in params.get("AccountSet"):
                obj = PrivateDNSAccount()
                obj._deserialize(item)
                self._AccountSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneListRequest(AbstractModel):
    """DescribePrivateZoneList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大100，默认20
        :type Limit: int
        :param _Filters: 过滤参数
        :type Filters: list of Filter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneListResponse(AbstractModel):
    """DescribePrivateZoneList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 私有域数量
        :type TotalCount: int
        :param _PrivateZoneSet: 私有域列表
        :type PrivateZoneSet: list of PrivateZone
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._PrivateZoneSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def PrivateZoneSet(self):
        return self._PrivateZoneSet

    @PrivateZoneSet.setter
    def PrivateZoneSet(self, PrivateZoneSet):
        self._PrivateZoneSet = PrivateZoneSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("PrivateZoneSet") is not None:
            self._PrivateZoneSet = []
            for item in params.get("PrivateZoneSet"):
                obj = PrivateZone()
                obj._deserialize(item)
                self._PrivateZoneSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneRecordListRequest(AbstractModel):
    """DescribePrivateZoneRecordList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID: zone-xxxxxx
        :type ZoneId: str
        :param _Filters: 过滤参数（支持使用Value、RecordType过滤）
        :type Filters: list of Filter
        :param _Offset: 分页偏移量，从0开始
        :type Offset: int
        :param _Limit: 分页限制数目， 最大200，默认20
        :type Limit: int
        """
        self._ZoneId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
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
        


class DescribePrivateZoneRecordListResponse(AbstractModel):
    """DescribePrivateZoneRecordList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 解析记录数量
        :type TotalCount: int
        :param _RecordSet: 解析记录列表
        :type RecordSet: list of PrivateZoneRecord
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordSet(self):
        return self._RecordSet

    @RecordSet.setter
    def RecordSet(self, RecordSet):
        self._RecordSet = RecordSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordSet") is not None:
            self._RecordSet = []
            for item in params.get("RecordSet"):
                obj = PrivateZoneRecord()
                obj._deserialize(item)
                self._RecordSet.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneRequest(AbstractModel):
    """DescribePrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 域名，格式必须是标准的TLD
        :type ZoneId: str
        """
        self._ZoneId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePrivateZoneResponse(AbstractModel):
    """DescribePrivateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PrivateZone: 私有域详情
        :type PrivateZone: :class:`tencentcloud.privatedns.v20201028.models.PrivateZone`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PrivateZone = None
        self._RequestId = None

    @property
    def PrivateZone(self):
        return self._PrivateZone

    @PrivateZone.setter
    def PrivateZone(self, PrivateZone):
        self._PrivateZone = PrivateZone

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PrivateZone") is not None:
            self._PrivateZone = PrivateZone()
            self._PrivateZone._deserialize(params.get("PrivateZone"))
        self._RequestId = params.get("RequestId")


class DescribePrivateZoneServiceRequest(AbstractModel):
    """DescribePrivateZoneService请求参数结构体

    """


class DescribePrivateZoneServiceResponse(AbstractModel):
    """DescribePrivateZoneService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: 私有域解析服务开通状态。ENABLED已开通，DISABLED未开通
        :type ServiceStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class DescribeQuotaUsageRequest(AbstractModel):
    """DescribeQuotaUsage请求参数结构体

    """


class DescribeQuotaUsageResponse(AbstractModel):
    """DescribeQuotaUsage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TldQuota: Tld额度使用情况
        :type TldQuota: :class:`tencentcloud.privatedns.v20201028.models.TldQuota`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TldQuota = None
        self._RequestId = None

    @property
    def TldQuota(self):
        return self._TldQuota

    @TldQuota.setter
    def TldQuota(self, TldQuota):
        self._TldQuota = TldQuota

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TldQuota") is not None:
            self._TldQuota = TldQuota()
            self._TldQuota._deserialize(params.get("TldQuota"))
        self._RequestId = params.get("RequestId")


class DescribeRequestDataRequest(AbstractModel):
    """DescribeRequestData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TimeRangeBegin: 请求量统计起始时间，格式：2020-11-22 00:00:00
        :type TimeRangeBegin: str
        :param _Filters: 筛选参数：
        :type Filters: list of Filter
        :param _TimeRangeEnd: 请求量统计结束时间，格式：2020-11-22 23:59:59
        :type TimeRangeEnd: str
        """
        self._TimeRangeBegin = None
        self._Filters = None
        self._TimeRangeEnd = None

    @property
    def TimeRangeBegin(self):
        return self._TimeRangeBegin

    @TimeRangeBegin.setter
    def TimeRangeBegin(self, TimeRangeBegin):
        self._TimeRangeBegin = TimeRangeBegin

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def TimeRangeEnd(self):
        return self._TimeRangeEnd

    @TimeRangeEnd.setter
    def TimeRangeEnd(self, TimeRangeEnd):
        self._TimeRangeEnd = TimeRangeEnd


    def _deserialize(self, params):
        self._TimeRangeBegin = params.get("TimeRangeBegin")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._TimeRangeEnd = params.get("TimeRangeEnd")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRequestDataResponse(AbstractModel):
    """DescribeRequestData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 请求量统计表
        :type Data: list of MetricData
        :param _Interval: 请求量单位时间: Day：天，Hour：小时
        :type Interval: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = MetricData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """筛选参数

    """

    def __init__(self):
        r"""
        :param _Name: 参数名
        :type Name: str
        :param _Values: 参数值数组
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FlowUsage(AbstractModel):
    """流量包用量

    """

    def __init__(self):
        r"""
        :param _FlowType: 流量包类型：ZONE 私有域；TRAFFIC 解析流量包
        :type FlowType: str
        :param _TotalQuantity: 流量包总额度
        :type TotalQuantity: int
        :param _AvailableQuantity: 流量包可用额度
        :type AvailableQuantity: int
        """
        self._FlowType = None
        self._TotalQuantity = None
        self._AvailableQuantity = None

    @property
    def FlowType(self):
        return self._FlowType

    @FlowType.setter
    def FlowType(self, FlowType):
        self._FlowType = FlowType

    @property
    def TotalQuantity(self):
        return self._TotalQuantity

    @TotalQuantity.setter
    def TotalQuantity(self, TotalQuantity):
        self._TotalQuantity = TotalQuantity

    @property
    def AvailableQuantity(self):
        return self._AvailableQuantity

    @AvailableQuantity.setter
    def AvailableQuantity(self, AvailableQuantity):
        self._AvailableQuantity = AvailableQuantity


    def _deserialize(self, params):
        self._FlowType = params.get("FlowType")
        self._TotalQuantity = params.get("TotalQuantity")
        self._AvailableQuantity = params.get("AvailableQuantity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricData(AbstractModel):
    """统计数据表

    """

    def __init__(self):
        r"""
        :param _Resource: 资源描述
        :type Resource: str
        :param _Metric: 表名
        :type Metric: str
        :param _DataSet: 表数据
        :type DataSet: list of DatePoint
        :param _MetricCount: 查询范围内的请求总量
注意：此字段可能返回 null，表示取不到有效值。
        :type MetricCount: int
        """
        self._Resource = None
        self._Metric = None
        self._DataSet = None
        self._MetricCount = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Metric(self):
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DataSet(self):
        return self._DataSet

    @DataSet.setter
    def DataSet(self, DataSet):
        self._DataSet = DataSet

    @property
    def MetricCount(self):
        return self._MetricCount

    @MetricCount.setter
    def MetricCount(self, MetricCount):
        self._MetricCount = MetricCount


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        self._Metric = params.get("Metric")
        if params.get("DataSet") is not None:
            self._DataSet = []
            for item in params.get("DataSet"):
                obj = DatePoint()
                obj._deserialize(item)
                self._DataSet.append(obj)
        self._MetricCount = params.get("MetricCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordRequest(AbstractModel):
    """ModifyPrivateZoneRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordId: 记录ID
        :type RecordId: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _SubDomain: 子域名，例如 "www", "m", "@"
        :type SubDomain: str
        :param _RecordValue: 记录值，例如 IP：192.168.10.2，CNAME：cname.qcloud.com.，MX：mail.qcloud.com.
        :type RecordValue: str
        :param _Weight: 记录权重，值为1-100
        :type Weight: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
        :type MX: int
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        """
        self._ZoneId = None
        self._RecordId = None
        self._RecordType = None
        self._SubDomain = None
        self._RecordValue = None
        self._Weight = None
        self._MX = None
        self._TTL = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordId = params.get("RecordId")
        self._RecordType = params.get("RecordType")
        self._SubDomain = params.get("SubDomain")
        self._RecordValue = params.get("RecordValue")
        self._Weight = params.get("Weight")
        self._MX = params.get("MX")
        self._TTL = params.get("TTL")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneRecordResponse(AbstractModel):
    """ModifyPrivateZoneRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateZoneRequest(AbstractModel):
    """ModifyPrivateZone请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _Remark: 备注
        :type Remark: str
        :param _DnsForwardStatus: 是否开启子域名递归, ENABLED， DISABLED
        :type DnsForwardStatus: str
        :param _CnameSpeedupStatus: 是否开启CNAME加速：ENABLED， DISABLED
        :type CnameSpeedupStatus: str
        """
        self._ZoneId = None
        self._Remark = None
        self._DnsForwardStatus = None
        self._CnameSpeedupStatus = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def DnsForwardStatus(self):
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def CnameSpeedupStatus(self):
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._Remark = params.get("Remark")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneResponse(AbstractModel):
    """ModifyPrivateZone返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPrivateZoneVpcRequest(AbstractModel):
    """ModifyPrivateZoneVpc请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _VpcSet: 私有域关联的全部VPC列表
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 私有域账号关联的全部VPC列表
        :type AccountVpcSet: list of AccountVpcInfo
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfo()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPrivateZoneVpcResponse(AbstractModel):
    """ModifyPrivateZoneVpc返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID, zone-xxxxxx
        :type ZoneId: str
        :param _VpcSet: 解析域关联的VPC列表
        :type VpcSet: list of VpcInfo
        :param _AccountVpcSet: 私有域账号关联的全部VPC列表
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._VpcSet = None
        self._AccountVpcSet = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._RequestId = params.get("RequestId")


class ModifyRecordsStatusRequest(AbstractModel):
    """ModifyRecordsStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordIds: 解析记录ID列表
        :type RecordIds: list of int
        :param _Status: enabled：生效，disabled：失效
        :type Status: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRecordsStatusResponse(AbstractModel):
    """ModifyRecordsStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域ID
        :type ZoneId: str
        :param _RecordIds: 解析记录ID列表
        :type RecordIds: list of int
        :param _Status: enabled：生效，disabled：失效
        :type Status: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ZoneId = None
        self._RecordIds = None
        self._Status = None
        self._RequestId = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def RecordIds(self):
        return self._RecordIds

    @RecordIds.setter
    def RecordIds(self, RecordIds):
        self._RecordIds = RecordIds

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._RecordIds = params.get("RecordIds")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class PrivateDNSAccount(AbstractModel):
    """私有域解析账号

    """

    def __init__(self):
        r"""
        :param _Uin: 主账号Uin
        :type Uin: str
        :param _Account: 主账号名称
        :type Account: str
        :param _Nickname: 用户昵称
        :type Nickname: str
        """
        self._Uin = None
        self._Account = None
        self._Nickname = None

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def Account(self):
        return self._Account

    @Account.setter
    def Account(self, Account):
        self._Account = Account

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname


    def _deserialize(self, params):
        self._Uin = params.get("Uin")
        self._Account = params.get("Account")
        self._Nickname = params.get("Nickname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZone(AbstractModel):
    """私有域信息

    """

    def __init__(self):
        r"""
        :param _ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param _OwnerUin: 域名所有者uin
        :type OwnerUin: int
        :param _Domain: 私有域名
        :type Domain: str
        :param _CreatedOn: 创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 修改时间
        :type UpdatedOn: str
        :param _RecordCount: 记录数
        :type RecordCount: int
        :param _Remark: 备注
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        :param _VpcSet: 绑定的Vpc列表
        :type VpcSet: list of VpcInfo
        :param _Status: 私有域状态：正常解析：ENABLED, 暂停解析：SUSPEND, 锁定：FROZEN
        :type Status: str
        :param _DnsForwardStatus: 域名递归解析状态：开通：ENABLED, 关闭，DISABLED
        :type DnsForwardStatus: str
        :param _Tags: 标签键值对集合
        :type Tags: list of TagInfo
        :param _AccountVpcSet: 绑定的关联账号的vpc列表
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountVpcSet: list of AccountVpcInfoOutput
        :param _IsCustomTld: 是否自定义TLD
注意：此字段可能返回 null，表示取不到有效值。
        :type IsCustomTld: bool
        :param _CnameSpeedupStatus: CNAME加速状态：开通：ENABLED, 关闭，DISABLED
        :type CnameSpeedupStatus: str
        :param _ForwardRuleName: 转发规则名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardRuleName: str
        :param _ForwardRuleType: 转发规则类型：云上到云下，DOWN；云下到云上，UP，目前只支持DOWN
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardRuleType: str
        :param _ForwardAddress: 转发的地址
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardAddress: str
        :param _EndPointName: 终端节点名称
注意：此字段可能返回 null，表示取不到有效值。
        :type EndPointName: str
        """
        self._ZoneId = None
        self._OwnerUin = None
        self._Domain = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._RecordCount = None
        self._Remark = None
        self._VpcSet = None
        self._Status = None
        self._DnsForwardStatus = None
        self._Tags = None
        self._AccountVpcSet = None
        self._IsCustomTld = None
        self._CnameSpeedupStatus = None
        self._ForwardRuleName = None
        self._ForwardRuleType = None
        self._ForwardAddress = None
        self._EndPointName = None

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def RecordCount(self):
        return self._RecordCount

    @RecordCount.setter
    def RecordCount(self, RecordCount):
        self._RecordCount = RecordCount

    @property
    def Remark(self):
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def VpcSet(self):
        return self._VpcSet

    @VpcSet.setter
    def VpcSet(self, VpcSet):
        self._VpcSet = VpcSet

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def DnsForwardStatus(self):
        return self._DnsForwardStatus

    @DnsForwardStatus.setter
    def DnsForwardStatus(self, DnsForwardStatus):
        self._DnsForwardStatus = DnsForwardStatus

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def AccountVpcSet(self):
        return self._AccountVpcSet

    @AccountVpcSet.setter
    def AccountVpcSet(self, AccountVpcSet):
        self._AccountVpcSet = AccountVpcSet

    @property
    def IsCustomTld(self):
        return self._IsCustomTld

    @IsCustomTld.setter
    def IsCustomTld(self, IsCustomTld):
        self._IsCustomTld = IsCustomTld

    @property
    def CnameSpeedupStatus(self):
        return self._CnameSpeedupStatus

    @CnameSpeedupStatus.setter
    def CnameSpeedupStatus(self, CnameSpeedupStatus):
        self._CnameSpeedupStatus = CnameSpeedupStatus

    @property
    def ForwardRuleName(self):
        return self._ForwardRuleName

    @ForwardRuleName.setter
    def ForwardRuleName(self, ForwardRuleName):
        self._ForwardRuleName = ForwardRuleName

    @property
    def ForwardRuleType(self):
        return self._ForwardRuleType

    @ForwardRuleType.setter
    def ForwardRuleType(self, ForwardRuleType):
        self._ForwardRuleType = ForwardRuleType

    @property
    def ForwardAddress(self):
        return self._ForwardAddress

    @ForwardAddress.setter
    def ForwardAddress(self, ForwardAddress):
        self._ForwardAddress = ForwardAddress

    @property
    def EndPointName(self):
        return self._EndPointName

    @EndPointName.setter
    def EndPointName(self, EndPointName):
        self._EndPointName = EndPointName


    def _deserialize(self, params):
        self._ZoneId = params.get("ZoneId")
        self._OwnerUin = params.get("OwnerUin")
        self._Domain = params.get("Domain")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._RecordCount = params.get("RecordCount")
        self._Remark = params.get("Remark")
        if params.get("VpcSet") is not None:
            self._VpcSet = []
            for item in params.get("VpcSet"):
                obj = VpcInfo()
                obj._deserialize(item)
                self._VpcSet.append(obj)
        self._Status = params.get("Status")
        self._DnsForwardStatus = params.get("DnsForwardStatus")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = TagInfo()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("AccountVpcSet") is not None:
            self._AccountVpcSet = []
            for item in params.get("AccountVpcSet"):
                obj = AccountVpcInfoOutput()
                obj._deserialize(item)
                self._AccountVpcSet.append(obj)
        self._IsCustomTld = params.get("IsCustomTld")
        self._CnameSpeedupStatus = params.get("CnameSpeedupStatus")
        self._ForwardRuleName = params.get("ForwardRuleName")
        self._ForwardRuleType = params.get("ForwardRuleType")
        self._ForwardAddress = params.get("ForwardAddress")
        self._EndPointName = params.get("EndPointName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PrivateZoneRecord(AbstractModel):
    """私有域信息

    """

    def __init__(self):
        r"""
        :param _RecordId: 记录id
        :type RecordId: str
        :param _ZoneId: 私有域id: zone-xxxxxxxx
        :type ZoneId: str
        :param _SubDomain: 子域名
        :type SubDomain: str
        :param _RecordType: 记录类型，可选的记录类型为："A", "AAAA", "CNAME", "MX", "TXT", "PTR"
        :type RecordType: str
        :param _RecordValue: 记录值
        :type RecordValue: str
        :param _TTL: 记录缓存时间，数值越小生效越快，取值1-86400s, 默认 600
        :type TTL: int
        :param _MX: MX优先级：记录类型为MX时必填。取值范围：5,10,15,20,30,40,50
注意：此字段可能返回 null，表示取不到有效值。
        :type MX: int
        :param _Status: 记录状态：ENABLED
        :type Status: str
        :param _Weight: 记录权重，值为1-100
注意：此字段可能返回 null，表示取不到有效值。
        :type Weight: int
        :param _CreatedOn: 记录创建时间
        :type CreatedOn: str
        :param _UpdatedOn: 记录更新时间
        :type UpdatedOn: str
        :param _Extra: 附加信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Extra: str
        :param _Enabled: 0暂停，1启用
注意：此字段可能返回 null，表示取不到有效值。
        :type Enabled: int
        """
        self._RecordId = None
        self._ZoneId = None
        self._SubDomain = None
        self._RecordType = None
        self._RecordValue = None
        self._TTL = None
        self._MX = None
        self._Status = None
        self._Weight = None
        self._CreatedOn = None
        self._UpdatedOn = None
        self._Extra = None
        self._Enabled = None

    @property
    def RecordId(self):
        return self._RecordId

    @RecordId.setter
    def RecordId(self, RecordId):
        self._RecordId = RecordId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RecordValue(self):
        return self._RecordValue

    @RecordValue.setter
    def RecordValue(self, RecordValue):
        self._RecordValue = RecordValue

    @property
    def TTL(self):
        return self._TTL

    @TTL.setter
    def TTL(self, TTL):
        self._TTL = TTL

    @property
    def MX(self):
        return self._MX

    @MX.setter
    def MX(self, MX):
        self._MX = MX

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Weight(self):
        return self._Weight

    @Weight.setter
    def Weight(self, Weight):
        self._Weight = Weight

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn

    @property
    def UpdatedOn(self):
        return self._UpdatedOn

    @UpdatedOn.setter
    def UpdatedOn(self, UpdatedOn):
        self._UpdatedOn = UpdatedOn

    @property
    def Extra(self):
        return self._Extra

    @Extra.setter
    def Extra(self, Extra):
        self._Extra = Extra

    @property
    def Enabled(self):
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled


    def _deserialize(self, params):
        self._RecordId = params.get("RecordId")
        self._ZoneId = params.get("ZoneId")
        self._SubDomain = params.get("SubDomain")
        self._RecordType = params.get("RecordType")
        self._RecordValue = params.get("RecordValue")
        self._TTL = params.get("TTL")
        self._MX = params.get("MX")
        self._Status = params.get("Status")
        self._Weight = params.get("Weight")
        self._CreatedOn = params.get("CreatedOn")
        self._UpdatedOn = params.get("UpdatedOn")
        self._Extra = params.get("Extra")
        self._Enabled = params.get("Enabled")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubscribePrivateZoneServiceRequest(AbstractModel):
    """SubscribePrivateZoneService请求参数结构体

    """


class SubscribePrivateZoneServiceResponse(AbstractModel):
    """SubscribePrivateZoneService返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ServiceStatus: 私有域解析服务开通状态
        :type ServiceStatus: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ServiceStatus = None
        self._RequestId = None

    @property
    def ServiceStatus(self):
        return self._ServiceStatus

    @ServiceStatus.setter
    def ServiceStatus(self, ServiceStatus):
        self._ServiceStatus = ServiceStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ServiceStatus = params.get("ServiceStatus")
        self._RequestId = params.get("RequestId")


class TagInfo(AbstractModel):
    """标签

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
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        


class TldQuota(AbstractModel):
    """Tld额度

    """

    def __init__(self):
        r"""
        :param _Total: 总共额度
        :type Total: int
        :param _Used: 已使用额度
        :type Used: int
        :param _Stock: 库存
        :type Stock: int
        :param _Quota: 用户限额
        :type Quota: int
        """
        self._Total = None
        self._Used = None
        self._Stock = None
        self._Quota = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Stock(self):
        return self._Stock

    @Stock.setter
    def Stock(self, Stock):
        self._Stock = Stock

    @property
    def Quota(self):
        return self._Quota

    @Quota.setter
    def Quota(self, Quota):
        self._Quota = Quota


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Stock = params.get("Stock")
        self._Quota = params.get("Quota")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VpcInfo(AbstractModel):
    """Vpc信息

    """

    def __init__(self):
        r"""
        :param _UniqVpcId: VpcId： vpc-xadsafsdasd
        :type UniqVpcId: str
        :param _Region: Vpc所属地区: ap-guangzhou, ap-shanghai
        :type Region: str
        """
        self._UniqVpcId = None
        self._Region = None

    @property
    def UniqVpcId(self):
        return self._UniqVpcId

    @UniqVpcId.setter
    def UniqVpcId(self, UniqVpcId):
        self._UniqVpcId = UniqVpcId

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._UniqVpcId = params.get("UniqVpcId")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        