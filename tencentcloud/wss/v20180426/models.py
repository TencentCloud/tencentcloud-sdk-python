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


class DeleteCertRequest(AbstractModel):
    """DeleteCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 证书 ID，即通过 GetList 拿到的证书列表的 ID 字段。
        :type Id: str
        :param _ModuleType: 模块名称，应填 ssl。
        :type ModuleType: str
        """
        self._Id = None
        self._ModuleType = None

    @property
    def Id(self):
        """证书 ID，即通过 GetList 拿到的证书列表的 ID 字段。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ModuleType(self):
        """模块名称，应填 ssl。
        :rtype: str
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._ModuleType = params.get("ModuleType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertResponse(AbstractModel):
    """DeleteCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DescribeCertListRequest(AbstractModel):
    """DescribeCertList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ModuleType: 模块名称，应填 ssl。
        :type ModuleType: str
        :param _Offset: 页数，默认第一页。
        :type Offset: int
        :param _Limit: 每页条数，默认每页20条。
        :type Limit: int
        :param _SearchKey: 搜索关键字。
        :type SearchKey: str
        :param _CertType: 证书类型（目前支持:CA=客户端证书,SVR=服务器证书）。
        :type CertType: str
        :param _Id: 证书ID。
        :type Id: str
        :param _WithCert: 是否同时获取证书内容。
        :type WithCert: str
        :param _AltDomain: 如传，则只返回可以给该域名使用的证书。
        :type AltDomain: str
        """
        self._ModuleType = None
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._CertType = None
        self._Id = None
        self._WithCert = None
        self._AltDomain = None

    @property
    def ModuleType(self):
        """模块名称，应填 ssl。
        :rtype: str
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType

    @property
    def Offset(self):
        """页数，默认第一页。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """每页条数，默认每页20条。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SearchKey(self):
        """搜索关键字。
        :rtype: str
        """
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def CertType(self):
        """证书类型（目前支持:CA=客户端证书,SVR=服务器证书）。
        :rtype: str
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def Id(self):
        """证书ID。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def WithCert(self):
        """是否同时获取证书内容。
        :rtype: str
        """
        return self._WithCert

    @WithCert.setter
    def WithCert(self, WithCert):
        self._WithCert = WithCert

    @property
    def AltDomain(self):
        """如传，则只返回可以给该域名使用的证书。
        :rtype: str
        """
        return self._AltDomain

    @AltDomain.setter
    def AltDomain(self, AltDomain):
        self._AltDomain = AltDomain


    def _deserialize(self, params):
        self._ModuleType = params.get("ModuleType")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._CertType = params.get("CertType")
        self._Id = params.get("Id")
        self._WithCert = params.get("WithCert")
        self._AltDomain = params.get("AltDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertListResponse(AbstractModel):
    """DescribeCertList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量。
        :type TotalCount: int
        :param _CertificateSet: 列表。
        :type CertificateSet: list of SSLCertificate
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._CertificateSet = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """总数量。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def CertificateSet(self):
        """列表。
        :rtype: list of SSLCertificate
        """
        return self._CertificateSet

    @CertificateSet.setter
    def CertificateSet(self, CertificateSet):
        self._CertificateSet = CertificateSet

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("CertificateSet") is not None:
            self._CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = SSLCertificate()
                obj._deserialize(item)
                self._CertificateSet.append(obj)
        self._RequestId = params.get("RequestId")


class SSLCertificate(AbstractModel):
    """获取证书列表（SSLCertificate）返回参数键为 CertificateSet 的内容。

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 所属账户
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _From: 证书来源：trustasia = 亚洲诚信， upload = 用户上传
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param _Type: 证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _CertType: 证书类型（目前支持：CA = 客户端证书，SVR = 服务器证书）
注意：此字段可能返回 null，表示取不到有效值。
        :type CertType: str
        :param _ProductZhName: 证书办法者名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param _Domain: 主域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Alias: 别名
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Status: 状态值 0：审核中，1：已通过，2：审核失败，3：已过期，4：已添加云解析记录，5：OV/EV 证书，待提交资料，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param _StatusMsg: 状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param _VerifyType: 验证类型
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param _CertBeginTime: 证书生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param _CertEndTime: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param _InsertTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _ProjectInfo: 项目信息，ProjectId：项目ID，OwnerUin：项目所属的 uin（默认项目为0），Name：项目名称，CreatorUin：创建项目的 uin，CreateTime：项目创建时间，Info：项目说明
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectInfo: :class:`tencentcloud.wss.v20180426.models.SSLProjectInfo`
        :param _Id: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: str
        :param _SubjectAltName: 证书包含的多个域名（包含主域名）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param _TypeName: 证书类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param _StatusName: 状态名称
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param _IsVip: 是否为 VIP 客户
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _IsDv: 是否我 DV 版证书
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param _IsWildcard: 是否为泛域名证书
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param _Cert: 证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Cert: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._Type = None
        self._CertType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._VulnerabilityStatus = None
        self._StatusMsg = None
        self._VerifyType = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._ProjectInfo = None
        self._Id = None
        self._SubjectAltName = None
        self._TypeName = None
        self._StatusName = None
        self._IsVip = None
        self._IsDv = None
        self._IsWildcard = None
        self._IsVulnerability = None
        self._Cert = None

    @property
    def OwnerUin(self):
        """所属账户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        """项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        """证书来源：trustasia = 亚洲诚信， upload = 用户上传
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Type(self):
        """证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def CertType(self):
        """证书类型（目前支持：CA = 客户端证书，SVR = 服务器证书）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def ProductZhName(self):
        """证书办法者名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        """主域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        """别名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        """状态值 0：审核中，1：已通过，2：审核失败，3：已过期，4：已添加云解析记录，5：OV/EV 证书，待提交资料，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def VulnerabilityStatus(self):
        """漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def StatusMsg(self):
        """状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        """验证类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def CertBeginTime(self):
        """证书生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        """证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        """证书过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def ProjectInfo(self):
        """项目信息，ProjectId：项目ID，OwnerUin：项目所属的 uin（默认项目为0），Name：项目名称，CreatorUin：创建项目的 uin，CreateTime：项目创建时间，Info：项目说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.wss.v20180426.models.SSLProjectInfo`
        """
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def Id(self):
        """证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SubjectAltName(self):
        """证书包含的多个域名（包含主域名）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def TypeName(self):
        """证书类型名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StatusName(self):
        """状态名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def IsVip(self):
        """是否为 VIP 客户
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsDv(self):
        """是否我 DV 版证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsWildcard(self):
        """是否为泛域名证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsVulnerability(self):
        """是否启用了漏洞扫描功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def Cert(self):
        """证书
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._Type = params.get("Type")
        self._CertType = params.get("CertType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        if params.get("ProjectInfo") is not None:
            self._ProjectInfo = SSLProjectInfo()
            self._ProjectInfo._deserialize(params.get("ProjectInfo"))
        self._Id = params.get("Id")
        self._SubjectAltName = params.get("SubjectAltName")
        self._TypeName = params.get("TypeName")
        self._StatusName = params.get("StatusName")
        self._IsVip = params.get("IsVip")
        self._IsDv = params.get("IsDv")
        self._IsWildcard = params.get("IsWildcard")
        self._IsVulnerability = params.get("IsVulnerability")
        self._Cert = params.get("Cert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SSLProjectInfo(AbstractModel):
    """获取证书列表接口（SSLProjectInfo）出参键为CertificateSet下的元素ProjectIno详情

    """

    def __init__(self):
        r"""
        :param _ProjectId: 项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _OwnerUin: 项目所属的 uin（默认项目为0）
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: int
        :param _Name: 项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _CreatorUin: 创建项目的 uin
注意：此字段可能返回 null，表示取不到有效值。
        :type CreatorUin: int
        :param _CreateTime: 项目创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Info: 项目说明
注意：此字段可能返回 null，表示取不到有效值。
        :type Info: str
        """
        self._ProjectId = None
        self._OwnerUin = None
        self._Name = None
        self._CreatorUin = None
        self._CreateTime = None
        self._Info = None

    @property
    def ProjectId(self):
        """项目ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def OwnerUin(self):
        """项目所属的 uin（默认项目为0）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def Name(self):
        """项目名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CreatorUin(self):
        """创建项目的 uin
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CreatorUin

    @CreatorUin.setter
    def CreatorUin(self, CreatorUin):
        self._CreatorUin = CreatorUin

    @property
    def CreateTime(self):
        """项目创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Info(self):
        """项目说明
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Info

    @Info.setter
    def Info(self, Info):
        self._Info = Info


    def _deserialize(self, params):
        self._ProjectId = params.get("ProjectId")
        self._OwnerUin = params.get("OwnerUin")
        self._Name = params.get("Name")
        self._CreatorUin = params.get("CreatorUin")
        self._CreateTime = params.get("CreateTime")
        self._Info = params.get("Info")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertRequest(AbstractModel):
    """UploadCert请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cert: 证书内容。
        :type Cert: str
        :param _CertType: 证书类型（目前支持：CA 为客户端证书，SVR 为服务器证书）。
        :type CertType: str
        :param _ProjectId: 项目ID，详见用户指南的 [项目与标签](https://cloud.tencent.com/document/product/598/32738)。
        :type ProjectId: str
        :param _ModuleType: 模块名称，应填 ssl。
        :type ModuleType: str
        :param _Key: 证书私钥，certType=SVR 时必填。
        :type Key: str
        :param _Alias: 证书备注。
        :type Alias: str
        """
        self._Cert = None
        self._CertType = None
        self._ProjectId = None
        self._ModuleType = None
        self._Key = None
        self._Alias = None

    @property
    def Cert(self):
        """证书内容。
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def CertType(self):
        """证书类型（目前支持：CA 为客户端证书，SVR 为服务器证书）。
        :rtype: str
        """
        return self._CertType

    @CertType.setter
    def CertType(self, CertType):
        self._CertType = CertType

    @property
    def ProjectId(self):
        """项目ID，详见用户指南的 [项目与标签](https://cloud.tencent.com/document/product/598/32738)。
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ModuleType(self):
        """模块名称，应填 ssl。
        :rtype: str
        """
        return self._ModuleType

    @ModuleType.setter
    def ModuleType(self, ModuleType):
        self._ModuleType = ModuleType

    @property
    def Key(self):
        """证书私钥，certType=SVR 时必填。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Alias(self):
        """证书备注。
        :rtype: str
        """
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._Cert = params.get("Cert")
        self._CertType = params.get("CertType")
        self._ProjectId = params.get("ProjectId")
        self._ModuleType = params.get("ModuleType")
        self._Key = params.get("Key")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertResponse(AbstractModel):
    """UploadCert返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Id: 证书ID。
        :type Id: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Id = None
        self._RequestId = None

    @property
    def Id(self):
        """证书ID。
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RequestId(self):
        """唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RequestId = params.get("RequestId")