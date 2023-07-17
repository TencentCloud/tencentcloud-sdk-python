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


class ApiGatewayInstanceDetail(AbstractModel):
    """apiGateway实例详情

    """

    def __init__(self):
        r"""
        :param _ServiceId: 实例ID
        :type ServiceId: str
        :param _ServiceName: 实例名称
        :type ServiceName: str
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Protocol: 使用协议
        :type Protocol: str
        """
        self._ServiceId = None
        self._ServiceName = None
        self._Domain = None
        self._CertId = None
        self._Protocol = None

    @property
    def ServiceId(self):
        return self._ServiceId

    @ServiceId.setter
    def ServiceId(self, ServiceId):
        self._ServiceId = ServiceId

    @property
    def ServiceName(self):
        return self._ServiceName

    @ServiceName.setter
    def ServiceName(self, ServiceName):
        self._ServiceName = ServiceName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol


    def _deserialize(self, params):
        self._ServiceId = params.get("ServiceId")
        self._ServiceName = params.get("ServiceName")
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DvAuthMethod: 验证方式：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。
        :type DvAuthMethod: str
        :param _DomainName: 域名。
        :type DomainName: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _PackageType: 证书类型，目前仅支持类型2。2 = TrustAsia TLS RSA CA。
        :type PackageType: str
        :param _ContactEmail: 邮箱。
        :type ContactEmail: str
        :param _ContactPhone: 手机。
        :type ContactPhone: str
        :param _ValidityPeriod: 有效期，默认12个月，目前仅支持12个月。
        :type ValidityPeriod: str
        :param _CsrEncryptAlgo: 加密算法，支持 RSA及ECC。
        :type CsrEncryptAlgo: str
        :param _CsrKeyParameter: 密钥对参数，RSA仅支持2048。ECC仅支持prime256v1
        :type CsrKeyParameter: str
        :param _CsrKeyPassword: CSR 的加密密码。
        :type CsrKeyPassword: str
        :param _Alias: 备注名称。
        :type Alias: str
        :param _OldCertificateId: 原证书 ID，用于重新申请。
        :type OldCertificateId: str
        :param _PackageId: 权益包ID，用于免费证书扩容包使用
        :type PackageId: str
        :param _DeleteDnsAutoRecord: 签发后是否删除自动域名验证记录， 默认为否；仅域名为DNS_AUTO验证类型支持传参
        :type DeleteDnsAutoRecord: bool
        """
        self._DvAuthMethod = None
        self._DomainName = None
        self._ProjectId = None
        self._PackageType = None
        self._ContactEmail = None
        self._ContactPhone = None
        self._ValidityPeriod = None
        self._CsrEncryptAlgo = None
        self._CsrKeyParameter = None
        self._CsrKeyPassword = None
        self._Alias = None
        self._OldCertificateId = None
        self._PackageId = None
        self._DeleteDnsAutoRecord = None

    @property
    def DvAuthMethod(self):
        return self._DvAuthMethod

    @DvAuthMethod.setter
    def DvAuthMethod(self, DvAuthMethod):
        self._DvAuthMethod = DvAuthMethod

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ContactEmail(self):
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPhone(self):
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def CsrEncryptAlgo(self):
        return self._CsrEncryptAlgo

    @CsrEncryptAlgo.setter
    def CsrEncryptAlgo(self, CsrEncryptAlgo):
        self._CsrEncryptAlgo = CsrEncryptAlgo

    @property
    def CsrKeyParameter(self):
        return self._CsrKeyParameter

    @CsrKeyParameter.setter
    def CsrKeyParameter(self, CsrKeyParameter):
        self._CsrKeyParameter = CsrKeyParameter

    @property
    def CsrKeyPassword(self):
        return self._CsrKeyPassword

    @CsrKeyPassword.setter
    def CsrKeyPassword(self, CsrKeyPassword):
        self._CsrKeyPassword = CsrKeyPassword

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def DeleteDnsAutoRecord(self):
        return self._DeleteDnsAutoRecord

    @DeleteDnsAutoRecord.setter
    def DeleteDnsAutoRecord(self, DeleteDnsAutoRecord):
        self._DeleteDnsAutoRecord = DeleteDnsAutoRecord


    def _deserialize(self, params):
        self._DvAuthMethod = params.get("DvAuthMethod")
        self._DomainName = params.get("DomainName")
        self._ProjectId = params.get("ProjectId")
        self._PackageType = params.get("PackageType")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactPhone = params.get("ContactPhone")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self._CsrKeyParameter = params.get("CsrKeyParameter")
        self._CsrKeyPassword = params.get("CsrKeyPassword")
        self._Alias = params.get("Alias")
        self._OldCertificateId = params.get("OldCertificateId")
        self._PackageId = params.get("PackageId")
        self._DeleteDnsAutoRecord = params.get("DeleteDnsAutoRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 取消订单成功的证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CdnInstanceDetail(AbstractModel):
    """CDN实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 已部署证书ID
        :type CertId: str
        :param _Status: 域名状态
        :type Status: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertHostingInfo(AbstractModel):
    """云资源配置详情

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID
        :type CertId: str
        :param _RenewCertId: 已替换的新证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewCertId: str
        :param _ResourceType: 云资源托管 ，CDN或CLB：部分开启，CDN,CLB：已开启，null：未开启托管
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._CertId = None
        self._RenewCertId = None
        self._ResourceType = None
        self._CreateTime = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def RenewCertId(self):
        return self._RenewCertId

    @RenewCertId.setter
    def RenewCertId(self, RenewCertId):
        self._RenewCertId = RenewCertId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._RenewCertId = params.get("RenewCertId")
        self._ResourceType = params.get("ResourceType")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificate(AbstractModel):
    """CLB证书详情

    """

    def __init__(self):
        r"""
        :param _CertId: 证书ID
        :type CertId: str
        :param _DnsNames: 证书绑定的域名
        :type DnsNames: list of str
        """
        self._CertId = None
        self._DnsNames = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def DnsNames(self):
        return self._DnsNames

    @DnsNames.setter
    def DnsNames(self, DnsNames):
        self._DnsNames = DnsNames


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._DnsNames = params.get("DnsNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateExtra(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 数组下，key为CertificateExtra 的内容。

    """

    def __init__(self):
        r"""
        :param _DomainNumber: 证书可配置域名数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNumber: str
        :param _OriginCertificateId: 原始证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCertificateId: str
        :param _ReplacedBy: 重颁发证书原始 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedBy: str
        :param _ReplacedFor: 重颁发证书新 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedFor: str
        :param _RenewOrder: 新订单证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewOrder: str
        :param _SMCert: 是否是国密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type SMCert: int
        """
        self._DomainNumber = None
        self._OriginCertificateId = None
        self._ReplacedBy = None
        self._ReplacedFor = None
        self._RenewOrder = None
        self._SMCert = None

    @property
    def DomainNumber(self):
        return self._DomainNumber

    @DomainNumber.setter
    def DomainNumber(self, DomainNumber):
        self._DomainNumber = DomainNumber

    @property
    def OriginCertificateId(self):
        return self._OriginCertificateId

    @OriginCertificateId.setter
    def OriginCertificateId(self, OriginCertificateId):
        self._OriginCertificateId = OriginCertificateId

    @property
    def ReplacedBy(self):
        return self._ReplacedBy

    @ReplacedBy.setter
    def ReplacedBy(self, ReplacedBy):
        self._ReplacedBy = ReplacedBy

    @property
    def ReplacedFor(self):
        return self._ReplacedFor

    @ReplacedFor.setter
    def ReplacedFor(self, ReplacedFor):
        self._ReplacedFor = ReplacedFor

    @property
    def RenewOrder(self):
        return self._RenewOrder

    @RenewOrder.setter
    def RenewOrder(self, RenewOrder):
        self._RenewOrder = RenewOrder

    @property
    def SMCert(self):
        return self._SMCert

    @SMCert.setter
    def SMCert(self, SMCert):
        self._SMCert = SMCert


    def _deserialize(self, params):
        self._DomainNumber = params.get("DomainNumber")
        self._OriginCertificateId = params.get("OriginCertificateId")
        self._ReplacedBy = params.get("ReplacedBy")
        self._ReplacedFor = params.get("ReplacedFor")
        self._RenewOrder = params.get("RenewOrder")
        self._SMCert = params.get("SMCert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificates(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 的内容。

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _From: 证书来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param _PackageType: 证书套餐类型：
null = 用户上传证书（没有套餐类型），
1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param _ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param _Domain: 主域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Status: 状态。0：审核中，1：已通过，2：审核失败，3：已过期，4：验证方式为 DNS_AUTO 类型的证书， 已添加DNS记录，5：企业证书，待提交，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函，9：证书吊销中，10：已吊销，11：重颁发中，12：待上传吊销确认函，13：免费证书待提交资料状态，14：已退款，
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param _StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param _VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param _CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param _CertEndTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书有效期，单位（月）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param _InsertTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param _SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param _PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param _StatusName: 状态名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param _IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param _IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param _RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param _ProjectInfo: 项目信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param _BoundResource: 关联的云资源，暂不可用
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundResource: list of str
        :param _Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param _IsIgnore: 是否已忽略到期通知
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnore: bool
        :param _IsSM: 是否国密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSM: bool
        :param _EncryptAlgorithm: 证书算法
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptAlgorithm: str
        :param _CAEncryptAlgorithms: 上传CA证书的加密算法
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEncryptAlgorithms: list of str
        :param _CAEndTimes: 上传CA证书的过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEndTimes: list of str
        :param _CACommonNames: 上传CA证书的通用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CACommonNames: list of str
        :param _PreAuditInfo: 证书预审核信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PreAuditInfo: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        :param _AutoRenewFlag: 是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._PackageType = None
        self._CertificateType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._CertificateExtra = None
        self._VulnerabilityStatus = None
        self._StatusMsg = None
        self._VerifyType = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._CertificateId = None
        self._SubjectAltName = None
        self._PackageTypeName = None
        self._StatusName = None
        self._IsVip = None
        self._IsDv = None
        self._IsWildcard = None
        self._IsVulnerability = None
        self._RenewAble = None
        self._ProjectInfo = None
        self._BoundResource = None
        self._Deployable = None
        self._Tags = None
        self._IsIgnore = None
        self._IsSM = None
        self._EncryptAlgorithm = None
        self._CAEncryptAlgorithms = None
        self._CAEndTimes = None
        self._CACommonNames = None
        self._PreAuditInfo = None
        self._AutoRenewFlag = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProductZhName(self):
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CertificateExtra(self):
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def VulnerabilityStatus(self):
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def CertBeginTime(self):
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def PackageTypeName(self):
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsDv(self):
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsWildcard(self):
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsVulnerability(self):
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def ProjectInfo(self):
        return self._ProjectInfo

    @ProjectInfo.setter
    def ProjectInfo(self, ProjectInfo):
        self._ProjectInfo = ProjectInfo

    @property
    def BoundResource(self):
        return self._BoundResource

    @BoundResource.setter
    def BoundResource(self, BoundResource):
        self._BoundResource = BoundResource

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def IsIgnore(self):
        return self._IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, IsIgnore):
        self._IsIgnore = IsIgnore

    @property
    def IsSM(self):
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def EncryptAlgorithm(self):
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def CAEncryptAlgorithms(self):
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CAEndTimes(self):
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def CACommonNames(self):
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def PreAuditInfo(self):
        return self._PreAuditInfo

    @PreAuditInfo.setter
    def PreAuditInfo(self, PreAuditInfo):
        self._PreAuditInfo = PreAuditInfo

    @property
    def AutoRenewFlag(self):
        return self._AutoRenewFlag

    @AutoRenewFlag.setter
    def AutoRenewFlag(self, AutoRenewFlag):
        self._AutoRenewFlag = AutoRenewFlag


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._PackageType = params.get("PackageType")
        self._CertificateType = params.get("CertificateType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._CertificateId = params.get("CertificateId")
        self._SubjectAltName = params.get("SubjectAltName")
        self._PackageTypeName = params.get("PackageTypeName")
        self._StatusName = params.get("StatusName")
        self._IsVip = params.get("IsVip")
        self._IsDv = params.get("IsDv")
        self._IsWildcard = params.get("IsWildcard")
        self._IsVulnerability = params.get("IsVulnerability")
        self._RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self._ProjectInfo = ProjectInfo()
            self._ProjectInfo._deserialize(params.get("ProjectInfo"))
        self._BoundResource = params.get("BoundResource")
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._IsIgnore = params.get("IsIgnore")
        self._IsSM = params.get("IsSM")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        self._CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self._CAEndTimes = params.get("CAEndTimes")
        self._CACommonNames = params.get("CACommonNames")
        if params.get("PreAuditInfo") is not None:
            self._PreAuditInfo = PreAuditInfo()
            self._PreAuditInfo._deserialize(params.get("PreAuditInfo"))
        self._AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateChainRequest(AbstractModel):
    """CheckCertificateChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateChain: 待检查的证书链
        :type CertificateChain: str
        """
        self._CertificateChain = None

    @property
    def CertificateChain(self):
        return self._CertificateChain

    @CertificateChain.setter
    def CertificateChain(self, CertificateChain):
        self._CertificateChain = CertificateChain


    def _deserialize(self, params):
        self._CertificateChain = params.get("CertificateChain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateChainResponse(AbstractModel):
    """CheckCertificateChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IsValid: true为通过检查，false为未通过检查。
        :type IsValid: bool
        :param _IsTrustedCA: true为可信CA，false为不可信CA。
        :type IsTrustedCA: bool
        :param _Chains: 包含证书链中每一段证书的通用名称。
        :type Chains: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IsValid = None
        self._IsTrustedCA = None
        self._Chains = None
        self._RequestId = None

    @property
    def IsValid(self):
        return self._IsValid

    @IsValid.setter
    def IsValid(self, IsValid):
        self._IsValid = IsValid

    @property
    def IsTrustedCA(self):
        return self._IsTrustedCA

    @IsTrustedCA.setter
    def IsTrustedCA(self, IsTrustedCA):
        self._IsTrustedCA = IsTrustedCA

    @property
    def Chains(self):
        return self._Chains

    @Chains.setter
    def Chains(self, Chains):
        self._Chains = Chains

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._IsValid = params.get("IsValid")
        self._IsTrustedCA = params.get("IsTrustedCA")
        self._Chains = params.get("Chains")
        self._RequestId = params.get("RequestId")


class ClbInstanceDetail(AbstractModel):
    """clb实例详情

    """

    def __init__(self):
        r"""
        :param _LoadBalancerId: CLB实例ID
        :type LoadBalancerId: str
        :param _LoadBalancerName: CLB实例名称
        :type LoadBalancerName: str
        :param _Listeners: CLB监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ClbListener
        """
        self._LoadBalancerId = None
        self._LoadBalancerName = None
        self._Listeners = None

    @property
    def LoadBalancerId(self):
        return self._LoadBalancerId

    @LoadBalancerId.setter
    def LoadBalancerId(self, LoadBalancerId):
        self._LoadBalancerId = LoadBalancerId

    @property
    def LoadBalancerName(self):
        return self._LoadBalancerName

    @LoadBalancerName.setter
    def LoadBalancerName(self, LoadBalancerName):
        self._LoadBalancerName = LoadBalancerName

    @property
    def Listeners(self):
        return self._Listeners

    @Listeners.setter
    def Listeners(self, Listeners):
        self._Listeners = Listeners


    def _deserialize(self, params):
        self._LoadBalancerId = params.get("LoadBalancerId")
        self._LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self._Listeners = []
            for item in params.get("Listeners"):
                obj = ClbListener()
                obj._deserialize(item)
                self._Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListener(AbstractModel):
    """CLB实例监听器

    """

    def __init__(self):
        r"""
        :param _ListenerId: 监听器ID
        :type ListenerId: str
        :param _ListenerName: 监听器名称
        :type ListenerName: str
        :param _SniSwitch: 是否开启SNI，1为开启，0为关闭
        :type SniSwitch: int
        :param _Protocol: 监听器协议类型， HTTPS|TCP_SSL
        :type Protocol: str
        :param _Certificate: 监听器绑定的证书数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _Rules: 监听器规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ClbListenerRule
        :param _NoMatchDomains: 不匹配域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self._ListenerId = None
        self._ListenerName = None
        self._SniSwitch = None
        self._Protocol = None
        self._Certificate = None
        self._Rules = None
        self._NoMatchDomains = None

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def Rules(self):
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def NoMatchDomains(self):
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._SniSwitch = params.get("SniSwitch")
        self._Protocol = params.get("Protocol")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ClbListenerRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerRule(AbstractModel):
    """CLB监听器规则

    """

    def __init__(self):
        r"""
        :param _LocationId: 规则ID
        :type LocationId: str
        :param _Domain: 规则绑定的域名
        :type Domain: str
        :param _IsMatch: 规则是否匹配待绑定证书的域名
        :type IsMatch: bool
        :param _Certificate: 规则已绑定的证书数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param _NoMatchDomains: 不匹配域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self._LocationId = None
        self._Domain = None
        self._IsMatch = None
        self._Certificate = None
        self._NoMatchDomains = None

    @property
    def LocationId(self):
        return self._LocationId

    @LocationId.setter
    def LocationId(self, LocationId):
        self._LocationId = LocationId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def IsMatch(self):
        return self._IsMatch

    @IsMatch.setter
    def IsMatch(self, IsMatch):
        self._IsMatch = IsMatch

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def NoMatchDomains(self):
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._LocationId = params.get("LocationId")
        self._Domain = params.get("Domain")
        self._IsMatch = params.get("IsMatch")
        if params.get("Certificate") is not None:
            self._Certificate = Certificate()
            self._Certificate._deserialize(params.get("Certificate"))
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _VerifyType: 域名验证方式
        :type VerifyType: str
        """
        self._CertificateId = None
        self._VerifyType = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OrderId: CA机构侧订单号。
        :type OrderId: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :type Status: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OrderId = None
        self._Status = None
        self._RequestId = None

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

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
        self._OrderId = params.get("OrderId")
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class CompanyInfo(AbstractModel):
    """公司信息

    """

    def __init__(self):
        r"""
        :param _CompanyName: 公司名称
        :type CompanyName: str
        :param _CompanyId: 公司ID
        :type CompanyId: int
        :param _CompanyCountry: 公司所在国家
        :type CompanyCountry: str
        :param _CompanyProvince: 公司所在省份
        :type CompanyProvince: str
        :param _CompanyCity: 公司所在城市
        :type CompanyCity: str
        :param _CompanyAddress: 公司所在详细地址
        :type CompanyAddress: str
        :param _CompanyPhone: 公司电话
        :type CompanyPhone: str
        :param _IdType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IdType: str
        :param _IdNumber: ID号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdNumber: str
        """
        self._CompanyName = None
        self._CompanyId = None
        self._CompanyCountry = None
        self._CompanyProvince = None
        self._CompanyCity = None
        self._CompanyAddress = None
        self._CompanyPhone = None
        self._IdType = None
        self._IdNumber = None

    @property
    def CompanyName(self):
        return self._CompanyName

    @CompanyName.setter
    def CompanyName(self, CompanyName):
        self._CompanyName = CompanyName

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def CompanyCountry(self):
        return self._CompanyCountry

    @CompanyCountry.setter
    def CompanyCountry(self, CompanyCountry):
        self._CompanyCountry = CompanyCountry

    @property
    def CompanyProvince(self):
        return self._CompanyProvince

    @CompanyProvince.setter
    def CompanyProvince(self, CompanyProvince):
        self._CompanyProvince = CompanyProvince

    @property
    def CompanyCity(self):
        return self._CompanyCity

    @CompanyCity.setter
    def CompanyCity(self, CompanyCity):
        self._CompanyCity = CompanyCity

    @property
    def CompanyAddress(self):
        return self._CompanyAddress

    @CompanyAddress.setter
    def CompanyAddress(self, CompanyAddress):
        self._CompanyAddress = CompanyAddress

    @property
    def CompanyPhone(self):
        return self._CompanyPhone

    @CompanyPhone.setter
    def CompanyPhone(self, CompanyPhone):
        self._CompanyPhone = CompanyPhone

    @property
    def IdType(self):
        return self._IdType

    @IdType.setter
    def IdType(self, IdType):
        self._IdType = IdType

    @property
    def IdNumber(self):
        return self._IdNumber

    @IdNumber.setter
    def IdNumber(self, IdNumber):
        self._IdNumber = IdNumber


    def _deserialize(self, params):
        self._CompanyName = params.get("CompanyName")
        self._CompanyId = params.get("CompanyId")
        self._CompanyCountry = params.get("CompanyCountry")
        self._CompanyProvince = params.get("CompanyProvince")
        self._CompanyCity = params.get("CompanyCity")
        self._CompanyAddress = params.get("CompanyAddress")
        self._CompanyPhone = params.get("CompanyPhone")
        self._IdType = params.get("IdType")
        self._IdNumber = params.get("IdNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteCertificateRequest(AbstractModel):
    """CompleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteCertificateResponse(AbstractModel):
    """CompleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class CosInstanceDetail(AbstractModel):
    """COS实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 已绑定的证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Status: ENABLED: 域名上线状态
DISABLED:域名下线状态
        :type Status: str
        :param _Bucket: 存储桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Region: 存储桶地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self._Domain = None
        self._CertId = None
        self._Status = None
        self._Bucket = None
        self._Region = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        self._Bucket = params.get("Bucket")
        self._Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateByPackageRequest(AbstractModel):
    """CreateCertificateByPackage请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductPid: 证书产品PID。
        :type ProductPid: int
        :param _PackageIds: 要消耗的权益包ID。
        :type PackageIds: list of str
        :param _DomainCount: 证书域名数量。
        :type DomainCount: str
        :param _Period: 多年期证书年限。
        :type Period: int
        :param _OldCertificateId: 要续费的原证书ID（续费时填写）。
        :type OldCertificateId: str
        :param _RenewGenCsrMethod: 续费时CSR生成方式（original、upload、online）。
        :type RenewGenCsrMethod: str
        :param _RenewCsr: 续费时选择上传CSR时填写CSR。
        :type RenewCsr: str
        :param _RenewAlgorithmType: 续费证书CSR的算法类型。
        :type RenewAlgorithmType: str
        :param _RenewAlgorithmParam: 续费证书CSR的算法参数。
        :type RenewAlgorithmParam: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _Tags: 标签。
        :type Tags: list of Tags
        :param _RenewKeyPass: 续费证书的私钥密码。
        :type RenewKeyPass: str
        :param _DomainNames: 批量购买证书时预填写的域名。
        :type DomainNames: str
        :param _CertificateCount: 批量购买证书数量。
        :type CertificateCount: int
        :param _ManagerId: 预填写的管理人ID。
        :type ManagerId: int
        :param _CompanyId: 预填写的公司ID。
        :type CompanyId: int
        :param _VerifyType: 验证方式
        :type VerifyType: str
        """
        self._ProductPid = None
        self._PackageIds = None
        self._DomainCount = None
        self._Period = None
        self._OldCertificateId = None
        self._RenewGenCsrMethod = None
        self._RenewCsr = None
        self._RenewAlgorithmType = None
        self._RenewAlgorithmParam = None
        self._ProjectId = None
        self._Tags = None
        self._RenewKeyPass = None
        self._DomainNames = None
        self._CertificateCount = None
        self._ManagerId = None
        self._CompanyId = None
        self._VerifyType = None

    @property
    def ProductPid(self):
        return self._ProductPid

    @ProductPid.setter
    def ProductPid(self, ProductPid):
        self._ProductPid = ProductPid

    @property
    def PackageIds(self):
        return self._PackageIds

    @PackageIds.setter
    def PackageIds(self, PackageIds):
        self._PackageIds = PackageIds

    @property
    def DomainCount(self):
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def Period(self):
        return self._Period

    @Period.setter
    def Period(self, Period):
        self._Period = Period

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def RenewGenCsrMethod(self):
        return self._RenewGenCsrMethod

    @RenewGenCsrMethod.setter
    def RenewGenCsrMethod(self, RenewGenCsrMethod):
        self._RenewGenCsrMethod = RenewGenCsrMethod

    @property
    def RenewCsr(self):
        return self._RenewCsr

    @RenewCsr.setter
    def RenewCsr(self, RenewCsr):
        self._RenewCsr = RenewCsr

    @property
    def RenewAlgorithmType(self):
        return self._RenewAlgorithmType

    @RenewAlgorithmType.setter
    def RenewAlgorithmType(self, RenewAlgorithmType):
        self._RenewAlgorithmType = RenewAlgorithmType

    @property
    def RenewAlgorithmParam(self):
        return self._RenewAlgorithmParam

    @RenewAlgorithmParam.setter
    def RenewAlgorithmParam(self, RenewAlgorithmParam):
        self._RenewAlgorithmParam = RenewAlgorithmParam

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RenewKeyPass(self):
        return self._RenewKeyPass

    @RenewKeyPass.setter
    def RenewKeyPass(self, RenewKeyPass):
        self._RenewKeyPass = RenewKeyPass

    @property
    def DomainNames(self):
        return self._DomainNames

    @DomainNames.setter
    def DomainNames(self, DomainNames):
        self._DomainNames = DomainNames

    @property
    def CertificateCount(self):
        return self._CertificateCount

    @CertificateCount.setter
    def CertificateCount(self, CertificateCount):
        self._CertificateCount = CertificateCount

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._ProductPid = params.get("ProductPid")
        self._PackageIds = params.get("PackageIds")
        self._DomainCount = params.get("DomainCount")
        self._Period = params.get("Period")
        self._OldCertificateId = params.get("OldCertificateId")
        self._RenewGenCsrMethod = params.get("RenewGenCsrMethod")
        self._RenewCsr = params.get("RenewCsr")
        self._RenewAlgorithmType = params.get("RenewAlgorithmType")
        self._RenewAlgorithmParam = params.get("RenewAlgorithmParam")
        self._ProjectId = params.get("ProjectId")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._RenewKeyPass = params.get("RenewKeyPass")
        self._DomainNames = params.get("DomainNames")
        self._CertificateCount = params.get("CertificateCount")
        self._ManagerId = params.get("ManagerId")
        self._CompanyId = params.get("CompanyId")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateByPackageResponse(AbstractModel):
    """CreateCertificateByPackage返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID。
        :type CertificateId: str
        :param _CertificateIds: 批量购买证书时返回多个证书ID。
        :type CertificateIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._CertificateIds = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CertificateIds = params.get("CertificateIds")
        self._RequestId = params.get("RequestId")


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ProductId: 证书商品ID，3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书，25 = Wotrus 域名型证书，26 = Wotrus 域名型多域名证书，27 = Wotrus 域名型通配符证书，28 = Wotrus 企业型证书，29 = Wotrus 企业型多域名证书，30 = Wotrus 企业型通配符证书，31 = Wotrus 增强型证书，32 = Wotrus 增强型多域名证书，33 = DNSPod 国密域名型证书，34 = DNSPod 国密域名型多域名证书，35 = DNSPod 国密域名型通配符证书，37 = DNSPod 国密企业型证书，38 = DNSPod 国密企业型多域名证书，39 = DNSPod 国密企业型通配符证书，40 = DNSPod 国密增强型证书，41 = DNSPod 国密增强型多域名证书，42 = TrustAsia 域名型通配符多域名证书。
        :type ProductId: int
        :param _DomainNum: 证书包含的域名数量
        :type DomainNum: int
        :param _TimeSpan: 证书年限，当前只支持 1 年证书的购买
        :type TimeSpan: int
        """
        self._ProductId = None
        self._DomainNum = None
        self._TimeSpan = None

    @property
    def ProductId(self):
        return self._ProductId

    @ProductId.setter
    def ProductId(self, ProductId):
        self._ProductId = ProductId

    @property
    def DomainNum(self):
        return self._DomainNum

    @DomainNum.setter
    def DomainNum(self, DomainNum):
        self._DomainNum = DomainNum

    @property
    def TimeSpan(self):
        return self._TimeSpan

    @TimeSpan.setter
    def TimeSpan(self, TimeSpan):
        self._TimeSpan = TimeSpan


    def _deserialize(self, params):
        self._ProductId = params.get("ProductId")
        self._DomainNum = params.get("DomainNum")
        self._TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表
        :type CertificateIds: list of str
        :param _DealIds: 订单号列表
        :type DealIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateIds = None
        self._DealIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def DealIds(self):
        return self._DealIds

    @DealIds.setter
    def DealIds(self, DealIds):
        self._DealIds = DealIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._DealIds = params.get("DealIds")
        self._RequestId = params.get("RequestId")


class DdosInstanceDetail(AbstractModel):
    """ddos复杂类型

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _CertId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _VirtualPort: 转发端口
        :type VirtualPort: str
        """
        self._Domain = None
        self._InstanceId = None
        self._Protocol = None
        self._CertId = None
        self._VirtualPort = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def VirtualPort(self):
        return self._VirtualPort

    @VirtualPort.setter
    def VirtualPort(self, VirtualPort):
        self._VirtualPort = VirtualPort


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._InstanceId = params.get("InstanceId")
        self._Protocol = params.get("Protocol")
        self._CertId = params.get("CertId")
        self._VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeleteResult: 删除结果（true：删除成功，false：删除失败）
        :type DeleteResult: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeleteResult = None
        self._RequestId = None

    @property
    def DeleteResult(self):
        return self._DeleteResult

    @DeleteResult.setter
    def DeleteResult(self, DeleteResult):
        self._DeleteResult = DeleteResult

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeleteResult = params.get("DeleteResult")
        self._RequestId = params.get("RequestId")


class DeleteManagerRequest(AbstractModel):
    """DeleteManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        """
        self._ManagerId = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteManagerResponse(AbstractModel):
    """DeleteManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ManagerId = None
        self._RequestId = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._RequestId = params.get("RequestId")


class DeployCertificateInstanceRequest(AbstractModel):
    """DeployCertificateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _InstanceIdList: 需要部署实例列表
        :type InstanceIdList: list of str
        :param _ResourceType: 部署的云资源类型
        :type ResourceType: str
        :param _Status: 部署云资源状态：
云直播：
-1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :type Status: int
        """
        self._CertificateId = None
        self._InstanceIdList = None
        self._ResourceType = None
        self._Status = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def InstanceIdList(self):
        return self._InstanceIdList

    @InstanceIdList.setter
    def InstanceIdList(self, InstanceIdList):
        self._InstanceIdList = InstanceIdList

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._InstanceIdList = params.get("InstanceIdList")
        self._ResourceType = params.get("ResourceType")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateInstanceResponse(AbstractModel):
    """DeployCertificateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 云资源部署任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordId: int
        :param _DeployStatus: 部署状态，1表示部署成功，0表示部署失败
        :type DeployStatus: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._DeployStatus = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployStatus(self):
        return self._DeployStatus

    @DeployStatus.setter
    def DeployStatus(self, DeployStatus):
        self._DeployStatus = DeployStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployStatus = params.get("DeployStatus")
        self._RequestId = params.get("RequestId")


class DeployCertificateRecordRetryRequest(AbstractModel):
    """DeployCertificateRecordRetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        :param _DeployRecordDetailId: 待重试部署记录详情ID
        :type DeployRecordDetailId: int
        """
        self._DeployRecordId = None
        self._DeployRecordDetailId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployRecordDetailId(self):
        return self._DeployRecordDetailId

    @DeployRecordDetailId.setter
    def DeployRecordDetailId(self, DeployRecordDetailId):
        self._DeployRecordDetailId = DeployRecordDetailId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateRecordRetryResponse(AbstractModel):
    """DeployCertificateRecordRetry返回参数结构体

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


class DeployCertificateRecordRollbackRequest(AbstractModel):
    """DeployCertificateRecordRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        """
        self._DeployRecordId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateRecordRollbackResponse(AbstractModel):
    """DeployCertificateRecordRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 回滚部署记录ID
        :type DeployRecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._RequestId = params.get("RequestId")


class DeployRecordDetail(AbstractModel):
    """部署记录详情

    """

    def __init__(self):
        r"""
        :param _Id: 部署记录详情ID
        :type Id: int
        :param _CertId: 部署证书ID
        :type CertId: str
        :param _OldCertId: 原绑定证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OldCertId: str
        :param _InstanceId: 部署实例ID
        :type InstanceId: str
        :param _InstanceName: 部署实例名称
        :type InstanceName: str
        :param _ListenerId: 部署监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _Domains: 部署域名列表
        :type Domains: list of str
        :param _Protocol: 部署监听器协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _Status: 部署状态
        :type Status: int
        :param _ErrorMsg: 部署错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _CreateTime: 部署记录详情创建时间
        :type CreateTime: str
        :param _UpdateTime: 部署记录详情最后一次更新时间
        :type UpdateTime: str
        :param _ListenerName: 部署监听器名称
        :type ListenerName: str
        :param _SniSwitch: 是否开启SNI
        :type SniSwitch: int
        :param _Bucket: COS存储桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Namespace: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _SecretName: secret名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._InstanceId = None
        self._InstanceName = None
        self._ListenerId = None
        self._Domains = None
        self._Protocol = None
        self._Status = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._ListenerName = None
        self._SniSwitch = None
        self._Bucket = None
        self._Namespace = None
        self._SecretName = None
        self._Port = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ListenerId = params.get("ListenerId")
        self._Domains = params.get("Domains")
        self._Protocol = params.get("Protocol")
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._ListenerName = params.get("ListenerName")
        self._SniSwitch = params.get("SniSwitch")
        self._Bucket = params.get("Bucket")
        self._Namespace = params.get("Namespace")
        self._SecretName = params.get("SecretName")
        self._Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployRecordInfo(AbstractModel):
    """部署记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 部署记录ID
        :type Id: int
        :param _CertId: 部署证书ID
        :type CertId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _Region: 部署地域
        :type Region: str
        :param _Status: 部署状态
        :type Status: int
        :param _CreateTime: 部署时间
        :type CreateTime: str
        :param _UpdateTime: 最近一次更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._CertId = None
        self._ResourceType = None
        self._Region = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._ResourceType = params.get("ResourceType")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployedResources(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _Count: 数量
        :type Count: int
        :param _Type: 资源标识:clb,cdn,live,waf,antiddos
        :type Type: str
        :param _ResourceIds: 不建议使用。字段返回和Resources相同。本字段后续只返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param _Resources: 关联资源ID或关联域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of str
        """
        self._CertificateId = None
        self._Count = None
        self._Type = None
        self._ResourceIds = None
        self._Resources = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Count(self):
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def ResourceIds(self):
        return self._ResourceIds

    @ResourceIds.setter
    def ResourceIds(self, ResourceIds):
        self._ResourceIds = ResourceIds

    @property
    def Resources(self):
        return self._Resources

    @Resources.setter
    def Resources(self, Resources):
        self._Resources = Resources


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Count = params.get("Count")
        self._Type = params.get("Type")
        self._ResourceIds = params.get("ResourceIds")
        self._Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param _PackageType: 证书套餐类型：null = 用户上传证书（没有套餐类型），1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书，25 = Wotrus 域名型证书，26 = Wotrus 域名型多域名证书，27 = Wotrus 域名型通配符证书，28 = Wotrus 企业型证书，29 = Wotrus 企业型多域名证书，30 = Wotrus 企业型通配符证书，31 = Wotrus 增强型证书，32 = Wotrus 增强型多域名证书，33 = DNSPod 国密域名型证书，34 = DNSPod 国密域名型多域名证书，35 = DNSPod 国密域名型通配符证书，37 = DNSPod 国密企业型证书，38 = DNSPod 国密企业型多域名证书，39 = DNSPod 国密企业型通配符证书，40 = DNSPod 国密增强型证书，41 = DNSPod 国密增强型多域名证书，42 = TrustAsia 域名型通配符多域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param _Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param _VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param _VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param _CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param _CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书有效期：单位（月）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param _InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _CertificatePrivateKey: 证书私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePrivateKey: str
        :param _CertificatePublicKey: 证书公钥（即证书内容）
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePublicKey: str
        :param _DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param _VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param _CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param _TypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param _StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param _SubjectAltName: 证书包含的多个域名（不包含主域名，主域名使用Domain字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param _IsVip: 是否为付费证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param _IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param _SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param _RenewAble: 是否可续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param _Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param _Tags: 关联标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param _RootCert: 根证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RootCert: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        :param _EncryptCert: 国密加密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptCert: str
        :param _EncryptPrivateKey: 国密加密私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptPrivateKey: str
        :param _CertFingerprint: 签名证书 SHA1指纹
注意：此字段可能返回 null，表示取不到有效值。
        :type CertFingerprint: str
        :param _EncryptCertFingerprint: 加密证书 SHA1指纹 （国密证书特有）
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptCertFingerprint: str
        :param _EncryptAlgorithm: 证书算法
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptAlgorithm: str
        :param _DvRevokeAuthDetail: DV证书吊销验证值
注意：此字段可能返回 null，表示取不到有效值。
        :type DvRevokeAuthDetail: list of DvAuths
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._CertificateType = None
        self._PackageType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._StatusMsg = None
        self._VerifyType = None
        self._VulnerabilityStatus = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._OrderId = None
        self._CertificateExtra = None
        self._CertificatePrivateKey = None
        self._CertificatePublicKey = None
        self._DvAuthDetail = None
        self._VulnerabilityReport = None
        self._CertificateId = None
        self._TypeName = None
        self._StatusName = None
        self._SubjectAltName = None
        self._IsVip = None
        self._IsWildcard = None
        self._IsDv = None
        self._IsVulnerability = None
        self._SubmittedData = None
        self._RenewAble = None
        self._Deployable = None
        self._Tags = None
        self._RootCert = None
        self._EncryptCert = None
        self._EncryptPrivateKey = None
        self._CertFingerprint = None
        self._EncryptCertFingerprint = None
        self._EncryptAlgorithm = None
        self._DvRevokeAuthDetail = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def CertificatePrivateKey(self):
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificatePublicKey(self):
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def DvAuthDetail(self):
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def TypeName(self):
        return self._TypeName

    @TypeName.setter
    def TypeName(self, TypeName):
        self._TypeName = TypeName

    @property
    def StatusName(self):
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def SubmittedData(self):
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def RenewAble(self):
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def RootCert(self):
        return self._RootCert

    @RootCert.setter
    def RootCert(self, RootCert):
        self._RootCert = RootCert

    @property
    def EncryptCert(self):
        return self._EncryptCert

    @EncryptCert.setter
    def EncryptCert(self, EncryptCert):
        self._EncryptCert = EncryptCert

    @property
    def EncryptPrivateKey(self):
        return self._EncryptPrivateKey

    @EncryptPrivateKey.setter
    def EncryptPrivateKey(self, EncryptPrivateKey):
        self._EncryptPrivateKey = EncryptPrivateKey

    @property
    def CertFingerprint(self):
        return self._CertFingerprint

    @CertFingerprint.setter
    def CertFingerprint(self, CertFingerprint):
        self._CertFingerprint = CertFingerprint

    @property
    def EncryptCertFingerprint(self):
        return self._EncryptCertFingerprint

    @EncryptCertFingerprint.setter
    def EncryptCertFingerprint(self, EncryptCertFingerprint):
        self._EncryptCertFingerprint = EncryptCertFingerprint

    @property
    def EncryptAlgorithm(self):
        return self._EncryptAlgorithm

    @EncryptAlgorithm.setter
    def EncryptAlgorithm(self, EncryptAlgorithm):
        self._EncryptAlgorithm = EncryptAlgorithm

    @property
    def DvRevokeAuthDetail(self):
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._CertificateType = params.get("CertificateType")
        self._PackageType = params.get("PackageType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self._DvAuthDetail = DvAuthDetail()
            self._DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self._VulnerabilityReport = params.get("VulnerabilityReport")
        self._CertificateId = params.get("CertificateId")
        self._TypeName = params.get("TypeName")
        self._StatusName = params.get("StatusName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._IsVip = params.get("IsVip")
        self._IsWildcard = params.get("IsWildcard")
        self._IsDv = params.get("IsDv")
        self._IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self._SubmittedData = SubmittedData()
            self._SubmittedData._deserialize(params.get("SubmittedData"))
        self._RenewAble = params.get("RenewAble")
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        if params.get("RootCert") is not None:
            self._RootCert = RootCertificates()
            self._RootCert._deserialize(params.get("RootCert"))
        self._EncryptCert = params.get("EncryptCert")
        self._EncryptPrivateKey = params.get("EncryptPrivateKey")
        self._CertFingerprint = params.get("CertFingerprint")
        self._EncryptCertFingerprint = params.get("EncryptCertFingerprint")
        self._EncryptAlgorithm = params.get("EncryptAlgorithm")
        if params.get("DvRevokeAuthDetail") is not None:
            self._DvRevokeAuthDetail = []
            for item in params.get("DvRevokeAuthDetail"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvRevokeAuthDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认为0。
        :type Offset: int
        :param _Limit: 请求日志数量，默认为20。
        :type Limit: int
        :param _StartTime: 开始时间，默认15天前。
        :type StartTime: str
        :param _EndTime: 结束时间，默认现在时间。
        :type EndTime: str
        """
        self._Offset = None
        self._Limit = None
        self._StartTime = None
        self._EndTime = None

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
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AllTotal: 当前查询条件日志总数。
        :type AllTotal: int
        :param _TotalCount: 本次请求返回的日志数量。
        :type TotalCount: int
        :param _OperateLogs: 证书操作日志列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateLogs: list of OperationLog
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AllTotal = None
        self._TotalCount = None
        self._OperateLogs = None
        self._RequestId = None

    @property
    def AllTotal(self):
        return self._AllTotal

    @AllTotal.setter
    def AllTotal(self, AllTotal):
        self._AllTotal = AllTotal

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def OperateLogs(self):
        return self._OperateLogs

    @OperateLogs.setter
    def OperateLogs(self, OperateLogs):
        self._OperateLogs = OperateLogs

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AllTotal = params.get("AllTotal")
        self._TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self._OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self._OperateLogs.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param _ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param _From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param _PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param _ProductZhName: 证书颁发者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param _Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param _Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param _Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param _StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param _VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param _VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param _CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param _CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param _ValidityPeriod: 证书有效期：单位(月)。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param _InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param _OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param _CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param _DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param _VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param _CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param _PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param _StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param _SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param _IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param _IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param _IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param _IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param _RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param _SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param _Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param _Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param _CAEncryptAlgorithms: CA证书的所有加密方式	
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEncryptAlgorithms: list of str
        :param _CACommonNames: CA证书的所有通用名称	
注意：此字段可能返回 null，表示取不到有效值。
        :type CACommonNames: list of str
        :param _CAEndTimes: CA证书所有的到期时间	
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEndTimes: list of str
        :param _DvRevokeAuthDetail: DV证书吊销验证值
注意：此字段可能返回 null，表示取不到有效值。
        :type DvRevokeAuthDetail: list of DvAuths
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._OwnerUin = None
        self._ProjectId = None
        self._From = None
        self._CertificateType = None
        self._PackageType = None
        self._ProductZhName = None
        self._Domain = None
        self._Alias = None
        self._Status = None
        self._StatusMsg = None
        self._VerifyType = None
        self._VulnerabilityStatus = None
        self._CertBeginTime = None
        self._CertEndTime = None
        self._ValidityPeriod = None
        self._InsertTime = None
        self._OrderId = None
        self._CertificateExtra = None
        self._DvAuthDetail = None
        self._VulnerabilityReport = None
        self._CertificateId = None
        self._PackageTypeName = None
        self._StatusName = None
        self._SubjectAltName = None
        self._IsVip = None
        self._IsWildcard = None
        self._IsDv = None
        self._IsVulnerability = None
        self._RenewAble = None
        self._SubmittedData = None
        self._Deployable = None
        self._Tags = None
        self._CAEncryptAlgorithms = None
        self._CACommonNames = None
        self._CAEndTimes = None
        self._DvRevokeAuthDetail = None
        self._RequestId = None

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def PackageType(self):
        return self._PackageType

    @PackageType.setter
    def PackageType(self, PackageType):
        self._PackageType = PackageType

    @property
    def ProductZhName(self):
        return self._ProductZhName

    @ProductZhName.setter
    def ProductZhName(self, ProductZhName):
        self._ProductZhName = ProductZhName

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def StatusMsg(self):
        return self._StatusMsg

    @StatusMsg.setter
    def StatusMsg(self, StatusMsg):
        self._StatusMsg = StatusMsg

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def VulnerabilityStatus(self):
        return self._VulnerabilityStatus

    @VulnerabilityStatus.setter
    def VulnerabilityStatus(self, VulnerabilityStatus):
        self._VulnerabilityStatus = VulnerabilityStatus

    @property
    def CertBeginTime(self):
        return self._CertBeginTime

    @CertBeginTime.setter
    def CertBeginTime(self, CertBeginTime):
        self._CertBeginTime = CertBeginTime

    @property
    def CertEndTime(self):
        return self._CertEndTime

    @CertEndTime.setter
    def CertEndTime(self, CertEndTime):
        self._CertEndTime = CertEndTime

    @property
    def ValidityPeriod(self):
        return self._ValidityPeriod

    @ValidityPeriod.setter
    def ValidityPeriod(self, ValidityPeriod):
        self._ValidityPeriod = ValidityPeriod

    @property
    def InsertTime(self):
        return self._InsertTime

    @InsertTime.setter
    def InsertTime(self, InsertTime):
        self._InsertTime = InsertTime

    @property
    def OrderId(self):
        return self._OrderId

    @OrderId.setter
    def OrderId(self, OrderId):
        self._OrderId = OrderId

    @property
    def CertificateExtra(self):
        return self._CertificateExtra

    @CertificateExtra.setter
    def CertificateExtra(self, CertificateExtra):
        self._CertificateExtra = CertificateExtra

    @property
    def DvAuthDetail(self):
        return self._DvAuthDetail

    @DvAuthDetail.setter
    def DvAuthDetail(self, DvAuthDetail):
        self._DvAuthDetail = DvAuthDetail

    @property
    def VulnerabilityReport(self):
        return self._VulnerabilityReport

    @VulnerabilityReport.setter
    def VulnerabilityReport(self, VulnerabilityReport):
        self._VulnerabilityReport = VulnerabilityReport

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def PackageTypeName(self):
        return self._PackageTypeName

    @PackageTypeName.setter
    def PackageTypeName(self, PackageTypeName):
        self._PackageTypeName = PackageTypeName

    @property
    def StatusName(self):
        return self._StatusName

    @StatusName.setter
    def StatusName(self, StatusName):
        self._StatusName = StatusName

    @property
    def SubjectAltName(self):
        return self._SubjectAltName

    @SubjectAltName.setter
    def SubjectAltName(self, SubjectAltName):
        self._SubjectAltName = SubjectAltName

    @property
    def IsVip(self):
        return self._IsVip

    @IsVip.setter
    def IsVip(self, IsVip):
        self._IsVip = IsVip

    @property
    def IsWildcard(self):
        return self._IsWildcard

    @IsWildcard.setter
    def IsWildcard(self, IsWildcard):
        self._IsWildcard = IsWildcard

    @property
    def IsDv(self):
        return self._IsDv

    @IsDv.setter
    def IsDv(self, IsDv):
        self._IsDv = IsDv

    @property
    def IsVulnerability(self):
        return self._IsVulnerability

    @IsVulnerability.setter
    def IsVulnerability(self, IsVulnerability):
        self._IsVulnerability = IsVulnerability

    @property
    def RenewAble(self):
        return self._RenewAble

    @RenewAble.setter
    def RenewAble(self, RenewAble):
        self._RenewAble = RenewAble

    @property
    def SubmittedData(self):
        return self._SubmittedData

    @SubmittedData.setter
    def SubmittedData(self, SubmittedData):
        self._SubmittedData = SubmittedData

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def CAEncryptAlgorithms(self):
        return self._CAEncryptAlgorithms

    @CAEncryptAlgorithms.setter
    def CAEncryptAlgorithms(self, CAEncryptAlgorithms):
        self._CAEncryptAlgorithms = CAEncryptAlgorithms

    @property
    def CACommonNames(self):
        return self._CACommonNames

    @CACommonNames.setter
    def CACommonNames(self, CACommonNames):
        self._CACommonNames = CACommonNames

    @property
    def CAEndTimes(self):
        return self._CAEndTimes

    @CAEndTimes.setter
    def CAEndTimes(self, CAEndTimes):
        self._CAEndTimes = CAEndTimes

    @property
    def DvRevokeAuthDetail(self):
        return self._DvRevokeAuthDetail

    @DvRevokeAuthDetail.setter
    def DvRevokeAuthDetail(self, DvRevokeAuthDetail):
        self._DvRevokeAuthDetail = DvRevokeAuthDetail

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        self._From = params.get("From")
        self._CertificateType = params.get("CertificateType")
        self._PackageType = params.get("PackageType")
        self._ProductZhName = params.get("ProductZhName")
        self._Domain = params.get("Domain")
        self._Alias = params.get("Alias")
        self._Status = params.get("Status")
        self._StatusMsg = params.get("StatusMsg")
        self._VerifyType = params.get("VerifyType")
        self._VulnerabilityStatus = params.get("VulnerabilityStatus")
        self._CertBeginTime = params.get("CertBeginTime")
        self._CertEndTime = params.get("CertEndTime")
        self._ValidityPeriod = params.get("ValidityPeriod")
        self._InsertTime = params.get("InsertTime")
        self._OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self._CertificateExtra = CertificateExtra()
            self._CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self._DvAuthDetail = DvAuthDetail()
            self._DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self._VulnerabilityReport = params.get("VulnerabilityReport")
        self._CertificateId = params.get("CertificateId")
        self._PackageTypeName = params.get("PackageTypeName")
        self._StatusName = params.get("StatusName")
        self._SubjectAltName = params.get("SubjectAltName")
        self._IsVip = params.get("IsVip")
        self._IsWildcard = params.get("IsWildcard")
        self._IsDv = params.get("IsDv")
        self._IsVulnerability = params.get("IsVulnerability")
        self._RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self._SubmittedData = SubmittedData()
            self._SubmittedData._deserialize(params.get("SubmittedData"))
        self._Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self._Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self._Tags.append(obj)
        self._CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self._CACommonNames = params.get("CACommonNames")
        self._CAEndTimes = params.get("CAEndTimes")
        if params.get("DvRevokeAuthDetail") is not None:
            self._DvRevokeAuthDetail = []
            for item in params.get("DvRevokeAuthDetail"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvRevokeAuthDetail.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认20。最大1000
        :type Limit: int
        :param _SearchKey: 搜索关键词，可搜索证书 ID、备注名称、域名。例如： a8xHcaIs。
        :type SearchKey: str
        :param _CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _ExpirationSort: 按到期时间排序：DESC = 降序， ASC = 升序。
        :type ExpirationSort: str
        :param _CertificateStatus: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :type CertificateStatus: list of int non-negative
        :param _Deployable: 是否可部署，可选值：1 = 可部署，0 =  不可部署。
        :type Deployable: int
        :param _Upload: 是否筛选上传托管的 1筛选，0不筛选
        :type Upload: int
        :param _Renew: 是否筛选可续期证书 1筛选 0不筛选
        :type Renew: int
        :param _FilterSource: 筛选来源， upload：上传证书， buy：腾讯云证书， 不传默认全部
        :type FilterSource: str
        :param _IsSM: 是否筛选国密证书。1:筛选  0:不筛选
        :type IsSM: int
        :param _FilterExpiring: 筛选证书是否即将过期，传1是筛选，0不筛选
        :type FilterExpiring: int
        """
        self._Offset = None
        self._Limit = None
        self._SearchKey = None
        self._CertificateType = None
        self._ProjectId = None
        self._ExpirationSort = None
        self._CertificateStatus = None
        self._Deployable = None
        self._Upload = None
        self._Renew = None
        self._FilterSource = None
        self._IsSM = None
        self._FilterExpiring = None

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
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ExpirationSort(self):
        return self._ExpirationSort

    @ExpirationSort.setter
    def ExpirationSort(self, ExpirationSort):
        self._ExpirationSort = ExpirationSort

    @property
    def CertificateStatus(self):
        return self._CertificateStatus

    @CertificateStatus.setter
    def CertificateStatus(self, CertificateStatus):
        self._CertificateStatus = CertificateStatus

    @property
    def Deployable(self):
        return self._Deployable

    @Deployable.setter
    def Deployable(self, Deployable):
        self._Deployable = Deployable

    @property
    def Upload(self):
        return self._Upload

    @Upload.setter
    def Upload(self, Upload):
        self._Upload = Upload

    @property
    def Renew(self):
        return self._Renew

    @Renew.setter
    def Renew(self, Renew):
        self._Renew = Renew

    @property
    def FilterSource(self):
        return self._FilterSource

    @FilterSource.setter
    def FilterSource(self, FilterSource):
        self._FilterSource = FilterSource

    @property
    def IsSM(self):
        return self._IsSM

    @IsSM.setter
    def IsSM(self, IsSM):
        self._IsSM = IsSM

    @property
    def FilterExpiring(self):
        return self._FilterExpiring

    @FilterExpiring.setter
    def FilterExpiring(self, FilterExpiring):
        self._FilterExpiring = FilterExpiring


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SearchKey = params.get("SearchKey")
        self._CertificateType = params.get("CertificateType")
        self._ProjectId = params.get("ProjectId")
        self._ExpirationSort = params.get("ExpirationSort")
        self._CertificateStatus = params.get("CertificateStatus")
        self._Deployable = params.get("Deployable")
        self._Upload = params.get("Upload")
        self._Renew = params.get("Renew")
        self._FilterSource = params.get("FilterSource")
        self._IsSM = params.get("IsSM")
        self._FilterExpiring = params.get("FilterExpiring")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _Certificates: 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificates: list of Certificates
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Certificates = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Certificates(self):
        return self._Certificates

    @Certificates.setter
    def Certificates(self, Certificates):
        self._Certificates = Certificates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self._Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self._Certificates.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCompaniesRequest(AbstractModel):
    """DescribeCompanies请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页每页限制数
        :type Limit: int
        :param _CompanyId: 公司ID
        :type CompanyId: int
        """
        self._Offset = None
        self._Limit = None
        self._CompanyId = None

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
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CompanyId = params.get("CompanyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompaniesResponse(AbstractModel):
    """DescribeCompanies返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Companies: 公司列表
        :type Companies: list of CompanyInfo
        :param _TotalCount: 公司总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Companies = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Companies(self):
        return self._Companies

    @Companies.setter
    def Companies(self, Companies):
        self._Companies = Companies

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Companies") is not None:
            self._Companies = []
            for item in params.get("Companies"):
                obj = CompanyInfo()
                obj._deserialize(item)
                self._Companies.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDeployedResourcesRequest(AbstractModel):
    """DescribeDeployedResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID
        :type CertificateIds: list of str
        :param _ResourceType: 资源类型:clb,cdn,live,waf,antiddos
        :type ResourceType: str
        """
        self._CertificateIds = None
        self._ResourceType = None

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployedResourcesResponse(AbstractModel):
    """DescribeDeployedResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployedResources: 资源详情
        :type DeployedResources: list of DeployedResources
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployedResources = None
        self._RequestId = None

    @property
    def DeployedResources(self):
        return self._DeployedResources

    @DeployedResources.setter
    def DeployedResources(self, DeployedResources):
        self._DeployedResources = DeployedResources

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DeployedResources") is not None:
            self._DeployedResources = []
            for item in params.get("DeployedResources"):
                obj = DeployedResources()
                obj._deserialize(item)
                self._DeployedResources.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostApiGatewayInstanceListRequest(AbstractModel):
    """DescribeHostApiGatewayInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostApiGatewayInstanceListResponse(AbstractModel):
    """DescribeHostApiGatewayInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: apiGateway实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of ApiGatewayInstanceDetail
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ApiGatewayInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostCdnInstanceListRequest(AbstractModel):
    """DescribeHostCdnInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        :param _Offset: 分页偏移量，从0开始。	
        :type Offset: int
        :param _Limit: 每页数量，默认10。	
        :type Limit: int
        :param _AsyncCache: 是否异步
        :type AsyncCache: int
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None
        self._Offset = None
        self._Limit = None
        self._AsyncCache = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

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
    def AsyncCache(self):
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._AsyncCache = params.get("AsyncCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostCdnInstanceListResponse(AbstractModel):
    """DescribeHostCdnInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: CDN实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of CdnInstanceDetail
        :param _TotalCount: CDN域名总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _AsyncTotalNum: 异步刷新总数	
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数	
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AsyncTotalNum(self):
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CdnInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostClbInstanceListRequest(AbstractModel):
    """DescribeHostClbInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _AsyncCache: 是否异步缓存
        :type AsyncCache: int
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._Offset = None
        self._Limit = None
        self._IsCache = None
        self._Filters = None
        self._AsyncCache = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AsyncCache(self):
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AsyncCache = params.get("AsyncCache")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostClbInstanceListResponse(AbstractModel):
    """DescribeHostClbInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _InstanceList: CLB实例监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of ClbInstanceDetail
        :param _AsyncTotalNum: 异步刷新总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间	
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def AsyncTotalNum(self):
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = ClbInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostCosInstanceListRequest(AbstractModel):
    """DescribeHostCosInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型 cos
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表
        :type Filters: list of Filter
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
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
        


class DescribeHostCosInstanceListResponse(AbstractModel):
    """DescribeHostCosInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: COS实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of CosInstanceDetail
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _AsyncTotalNum: 异步刷新总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def AsyncTotalNum(self):
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = CosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostDdosInstanceListRequest(AbstractModel):
    """DescribeHostDdosInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDdosInstanceListResponse(AbstractModel):
    """DescribeHostDdosInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: DDOS实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of DdosInstanceDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = DdosInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostDeployRecordDetailRequest(AbstractModel):
    """DescribeHostDeployRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待部署的证书ID
        :type DeployRecordId: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        """
        self._DeployRecordId = None
        self._Offset = None
        self._Limit = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

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
        self._DeployRecordId = params.get("DeployRecordId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDeployRecordDetailResponse(AbstractModel):
    """DescribeHostDeployRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _DeployRecordDetailList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordDetailList: list of DeployRecordDetail
        :param _SuccessTotalCount: 成功总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotalCount: int
        :param _FailedTotalCount: 失败总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedTotalCount: int
        :param _RunningTotalCount: 部署中总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningTotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordDetailList = None
        self._SuccessTotalCount = None
        self._FailedTotalCount = None
        self._RunningTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordDetailList(self):
        return self._DeployRecordDetailList

    @DeployRecordDetailList.setter
    def DeployRecordDetailList(self, DeployRecordDetailList):
        self._DeployRecordDetailList = DeployRecordDetailList

    @property
    def SuccessTotalCount(self):
        return self._SuccessTotalCount

    @SuccessTotalCount.setter
    def SuccessTotalCount(self, SuccessTotalCount):
        self._SuccessTotalCount = SuccessTotalCount

    @property
    def FailedTotalCount(self):
        return self._FailedTotalCount

    @FailedTotalCount.setter
    def FailedTotalCount(self, FailedTotalCount):
        self._FailedTotalCount = FailedTotalCount

    @property
    def RunningTotalCount(self):
        return self._RunningTotalCount

    @RunningTotalCount.setter
    def RunningTotalCount(self, RunningTotalCount):
        self._RunningTotalCount = RunningTotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordDetailList") is not None:
            self._DeployRecordDetailList = []
            for item in params.get("DeployRecordDetailList"):
                obj = DeployRecordDetail()
                obj._deserialize(item)
                self._DeployRecordDetailList.append(obj)
        self._SuccessTotalCount = params.get("SuccessTotalCount")
        self._FailedTotalCount = params.get("FailedTotalCount")
        self._RunningTotalCount = params.get("RunningTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostDeployRecordRequest(AbstractModel):
    """DescribeHostDeployRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _ResourceType: 资源类型
        :type ResourceType: str
        """
        self._CertificateId = None
        self._Offset = None
        self._Limit = None
        self._ResourceType = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDeployRecordResponse(AbstractModel):
    """DescribeHostDeployRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _DeployRecordList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordList: list of DeployRecordInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordList(self):
        return self._DeployRecordList

    @DeployRecordList.setter
    def DeployRecordList(self, DeployRecordList):
        self._DeployRecordList = DeployRecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self._DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = DeployRecordInfo()
                obj._deserialize(item)
                self._DeployRecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostLighthouseInstanceListRequest(AbstractModel):
    """DescribeHostLighthouseInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型 lighthouse
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表
        :type Filters: list of Filter
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
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
        


class DescribeHostLighthouseInstanceListResponse(AbstractModel):
    """DescribeHostLighthouseInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: Lighthouse实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LighthouseInstanceDetail
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LighthouseInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostLiveInstanceListRequest(AbstractModel):
    """DescribeHostLiveInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostLiveInstanceListResponse(AbstractModel):
    """DescribeHostLiveInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: live实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LiveInstanceDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostTeoInstanceListRequest(AbstractModel):
    """DescribeHostTeoInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTeoInstanceListResponse(AbstractModel):
    """DescribeHostTeoInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: teo实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TeoInstanceDetail
        :param _TotalCount: 总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostTkeInstanceListRequest(AbstractModel):
    """DescribeHostTkeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _AsyncCache: 是否异步缓存
        :type AsyncCache: int
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._Offset = None
        self._Limit = None
        self._IsCache = None
        self._Filters = None
        self._AsyncCache = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

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
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def AsyncCache(self):
        return self._AsyncCache

    @AsyncCache.setter
    def AsyncCache(self, AsyncCache):
        self._AsyncCache = AsyncCache

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._AsyncCache = params.get("AsyncCache")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTkeInstanceListResponse(AbstractModel):
    """DescribeHostTkeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _InstanceList: CLB实例监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TkeInstanceDetail
        :param _AsyncTotalNum: 异步刷新总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param _AsyncOffset: 异步刷新当前执行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param _AsyncCacheTime: 当前缓存读取时间	
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncCacheTime: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._InstanceList = None
        self._AsyncTotalNum = None
        self._AsyncOffset = None
        self._AsyncCacheTime = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def AsyncTotalNum(self):
        return self._AsyncTotalNum

    @AsyncTotalNum.setter
    def AsyncTotalNum(self, AsyncTotalNum):
        self._AsyncTotalNum = AsyncTotalNum

    @property
    def AsyncOffset(self):
        return self._AsyncOffset

    @AsyncOffset.setter
    def AsyncOffset(self, AsyncOffset):
        self._AsyncOffset = AsyncOffset

    @property
    def AsyncCacheTime(self):
        return self._AsyncCacheTime

    @AsyncCacheTime.setter
    def AsyncCacheTime(self, AsyncCacheTime):
        self._AsyncCacheTime = AsyncCacheTime

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = TkeInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._AsyncTotalNum = params.get("AsyncTotalNum")
        self._AsyncOffset = params.get("AsyncOffset")
        self._AsyncCacheTime = params.get("AsyncCacheTime")
        self._RequestId = params.get("RequestId")


class DescribeHostUpdateRecordDetailRequest(AbstractModel):
    """DescribeHostUpdateRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待部署的证书ID
        :type DeployRecordId: str
        :param _Limit: 每页数量，默认10。
        :type Limit: str
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: str
        """
        self._DeployRecordId = None
        self._Limit = None
        self._Offset = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordDetailResponse(AbstractModel):
    """DescribeHostUpdateRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RecordDetailList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordDetailList: list of UpdateRecordDetails
        :param _SuccessTotalCount: 成功总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotalCount: int
        :param _FailedTotalCount: 失败总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedTotalCount: int
        :param _RunningTotalCount: 部署中总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningTotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._RecordDetailList = None
        self._SuccessTotalCount = None
        self._FailedTotalCount = None
        self._RunningTotalCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RecordDetailList(self):
        return self._RecordDetailList

    @RecordDetailList.setter
    def RecordDetailList(self, RecordDetailList):
        self._RecordDetailList = RecordDetailList

    @property
    def SuccessTotalCount(self):
        return self._SuccessTotalCount

    @SuccessTotalCount.setter
    def SuccessTotalCount(self, SuccessTotalCount):
        self._SuccessTotalCount = SuccessTotalCount

    @property
    def FailedTotalCount(self):
        return self._FailedTotalCount

    @FailedTotalCount.setter
    def FailedTotalCount(self, FailedTotalCount):
        self._FailedTotalCount = FailedTotalCount

    @property
    def RunningTotalCount(self):
        return self._RunningTotalCount

    @RunningTotalCount.setter
    def RunningTotalCount(self, RunningTotalCount):
        self._RunningTotalCount = RunningTotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("RecordDetailList") is not None:
            self._RecordDetailList = []
            for item in params.get("RecordDetailList"):
                obj = UpdateRecordDetails()
                obj._deserialize(item)
                self._RecordDetailList.append(obj)
        self._SuccessTotalCount = params.get("SuccessTotalCount")
        self._FailedTotalCount = params.get("FailedTotalCount")
        self._RunningTotalCount = params.get("RunningTotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostUpdateRecordRequest(AbstractModel):
    """DescribeHostUpdateRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param _Limit: 每页数量，默认10。
        :type Limit: int
        :param _CertificateId: 新证书ID
        :type CertificateId: str
        :param _OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self._Offset = None
        self._Limit = None
        self._CertificateId = None
        self._OldCertificateId = None

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
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._CertificateId = params.get("CertificateId")
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordResponse(AbstractModel):
    """DescribeHostUpdateRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _DeployRecordList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordList: list of UpdateRecordInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._DeployRecordList = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def DeployRecordList(self):
        return self._DeployRecordList

    @DeployRecordList.setter
    def DeployRecordList(self, DeployRecordList):
        self._DeployRecordList = DeployRecordList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self._DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = UpdateRecordInfo()
                obj._deserialize(item)
                self._DeployRecordList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHostVodInstanceListRequest(AbstractModel):
    """DescribeHostVodInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型 vod
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostVodInstanceListResponse(AbstractModel):
    """DescribeHostVodInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: Vod实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of VodInstanceDetail
        :param _TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = VodInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeHostWafInstanceListRequest(AbstractModel):
    """DescribeHostWafInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param _Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param _OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self._CertificateId = None
        self._ResourceType = None
        self._IsCache = None
        self._Filters = None
        self._OldCertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def IsCache(self):
        return self._IsCache

    @IsCache.setter
    def IsCache(self, IsCache):
        self._IsCache = IsCache

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        self._IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostWafInstanceListResponse(AbstractModel):
    """DescribeHostWafInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param _InstanceList: WAF实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LiveInstanceDetail
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._InstanceList = None
        self._RequestId = None

    @property
    def InstanceList(self):
        return self._InstanceList

    @InstanceList.setter
    def InstanceList(self, InstanceList):
        self._InstanceList = InstanceList

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self._InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self._InstanceList.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeManagerDetailRequest(AbstractModel):
    """DescribeManagerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _Limit: 分页每页数量
        :type Limit: int
        :param _Offset: 分页偏移量
        :type Offset: int
        """
        self._ManagerId = None
        self._Limit = None
        self._Offset = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def Limit(self):
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagerDetailResponse(AbstractModel):
    """DescribeManagerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :type Status: str
        :param _ManagerFirstName: 管理人姓名
        :type ManagerFirstName: str
        :param _ManagerMail: 管理人邮箱
        :type ManagerMail: str
        :param _ContactFirstName: 联系人姓名
        :type ContactFirstName: str
        :param _ManagerLastName: 管理人姓名
        :type ManagerLastName: str
        :param _ContactPosition: 联系人职位
        :type ContactPosition: str
        :param _ManagerPosition: 管理人职位
        :type ManagerPosition: str
        :param _VerifyTime: 核验通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTime: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _ExpireTime: 核验过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _ContactLastName: 联系人姓名
        :type ContactLastName: str
        :param _ManagerPhone: 管理人电话
        :type ManagerPhone: str
        :param _ContactPhone: 联系人电话
        :type ContactPhone: str
        :param _ContactMail: 联系人邮箱
        :type ContactMail: str
        :param _ManagerDepartment: 管理人所属部门
        :type ManagerDepartment: str
        :param _CompanyInfo: 管理人所属公司信息
        :type CompanyInfo: :class:`tencentcloud.ssl.v20191205.models.CompanyInfo`
        :param _CompanyId: 管理人公司ID
        :type CompanyId: int
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _StatusInfo: 审核状态详细信息
        :type StatusInfo: list of ManagerStatusInfo
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Status = None
        self._ManagerFirstName = None
        self._ManagerMail = None
        self._ContactFirstName = None
        self._ManagerLastName = None
        self._ContactPosition = None
        self._ManagerPosition = None
        self._VerifyTime = None
        self._CreateTime = None
        self._ExpireTime = None
        self._ContactLastName = None
        self._ManagerPhone = None
        self._ContactPhone = None
        self._ContactMail = None
        self._ManagerDepartment = None
        self._CompanyInfo = None
        self._CompanyId = None
        self._ManagerId = None
        self._StatusInfo = None
        self._RequestId = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ManagerFirstName(self):
        return self._ManagerFirstName

    @ManagerFirstName.setter
    def ManagerFirstName(self, ManagerFirstName):
        self._ManagerFirstName = ManagerFirstName

    @property
    def ManagerMail(self):
        return self._ManagerMail

    @ManagerMail.setter
    def ManagerMail(self, ManagerMail):
        self._ManagerMail = ManagerMail

    @property
    def ContactFirstName(self):
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ManagerLastName(self):
        return self._ManagerLastName

    @ManagerLastName.setter
    def ManagerLastName(self, ManagerLastName):
        self._ManagerLastName = ManagerLastName

    @property
    def ContactPosition(self):
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def ManagerPosition(self):
        return self._ManagerPosition

    @ManagerPosition.setter
    def ManagerPosition(self, ManagerPosition):
        self._ManagerPosition = ManagerPosition

    @property
    def VerifyTime(self):
        return self._VerifyTime

    @VerifyTime.setter
    def VerifyTime(self, VerifyTime):
        self._VerifyTime = VerifyTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ContactLastName(self):
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ManagerPhone(self):
        return self._ManagerPhone

    @ManagerPhone.setter
    def ManagerPhone(self, ManagerPhone):
        self._ManagerPhone = ManagerPhone

    @property
    def ContactPhone(self):
        return self._ContactPhone

    @ContactPhone.setter
    def ContactPhone(self, ContactPhone):
        self._ContactPhone = ContactPhone

    @property
    def ContactMail(self):
        return self._ContactMail

    @ContactMail.setter
    def ContactMail(self, ContactMail):
        self._ContactMail = ContactMail

    @property
    def ManagerDepartment(self):
        return self._ManagerDepartment

    @ManagerDepartment.setter
    def ManagerDepartment(self, ManagerDepartment):
        self._ManagerDepartment = ManagerDepartment

    @property
    def CompanyInfo(self):
        return self._CompanyInfo

    @CompanyInfo.setter
    def CompanyInfo(self, CompanyInfo):
        self._CompanyInfo = CompanyInfo

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def StatusInfo(self):
        return self._StatusInfo

    @StatusInfo.setter
    def StatusInfo(self, StatusInfo):
        self._StatusInfo = StatusInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ManagerFirstName = params.get("ManagerFirstName")
        self._ManagerMail = params.get("ManagerMail")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ManagerLastName = params.get("ManagerLastName")
        self._ContactPosition = params.get("ContactPosition")
        self._ManagerPosition = params.get("ManagerPosition")
        self._VerifyTime = params.get("VerifyTime")
        self._CreateTime = params.get("CreateTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ContactLastName = params.get("ContactLastName")
        self._ManagerPhone = params.get("ManagerPhone")
        self._ContactPhone = params.get("ContactPhone")
        self._ContactMail = params.get("ContactMail")
        self._ManagerDepartment = params.get("ManagerDepartment")
        if params.get("CompanyInfo") is not None:
            self._CompanyInfo = CompanyInfo()
            self._CompanyInfo._deserialize(params.get("CompanyInfo"))
        self._CompanyId = params.get("CompanyId")
        self._ManagerId = params.get("ManagerId")
        if params.get("StatusInfo") is not None:
            self._StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = ManagerStatusInfo()
                obj._deserialize(item)
                self._StatusInfo.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeManagersRequest(AbstractModel):
    """DescribeManagers请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CompanyId: 公司ID
        :type CompanyId: int
        :param _Offset: 分页偏移量
        :type Offset: int
        :param _Limit: 分页每页数量
        :type Limit: int
        :param _ManagerName: 管理人姓名（将废弃），请使用SearchKey
        :type ManagerName: str
        :param _ManagerMail: 模糊查询管理人邮箱（将废弃），请使用SearchKey
        :type ManagerMail: str
        :param _Status: 根据管理人状态进行筛选，取值有
'none' 未提交审核
'audit', 亚信审核中
'CAaudit' CA审核中
'ok' 已审核
'invalid'  审核失败
'expiring'  即将过期
'expired' 已过期
        :type Status: str
        :param _SearchKey: 管理人姓/管理人名/邮箱/部门精准匹配
        :type SearchKey: str
        """
        self._CompanyId = None
        self._Offset = None
        self._Limit = None
        self._ManagerName = None
        self._ManagerMail = None
        self._Status = None
        self._SearchKey = None

    @property
    def CompanyId(self):
        return self._CompanyId

    @CompanyId.setter
    def CompanyId(self, CompanyId):
        self._CompanyId = CompanyId

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
    def ManagerName(self):
        return self._ManagerName

    @ManagerName.setter
    def ManagerName(self, ManagerName):
        self._ManagerName = ManagerName

    @property
    def ManagerMail(self):
        return self._ManagerMail

    @ManagerMail.setter
    def ManagerMail(self, ManagerMail):
        self._ManagerMail = ManagerMail

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SearchKey(self):
        return self._SearchKey

    @SearchKey.setter
    def SearchKey(self, SearchKey):
        self._SearchKey = SearchKey


    def _deserialize(self, params):
        self._CompanyId = params.get("CompanyId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._ManagerName = params.get("ManagerName")
        self._ManagerMail = params.get("ManagerMail")
        self._Status = params.get("Status")
        self._SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagersResponse(AbstractModel):
    """DescribeManagers返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Managers: 公司管理人列表
        :type Managers: list of ManagerInfo
        :param _TotalCount: 公司管理人总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Managers = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Managers(self):
        return self._Managers

    @Managers.setter
    def Managers(self, Managers):
        self._Managers = Managers

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Managers") is not None:
            self._Managers = []
            for item in params.get("Managers"):
                obj = ManagerInfo()
                obj._deserialize(item)
                self._Managers.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePackagesRequest(AbstractModel):
    """DescribePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 限制数目，默认20。
        :type Limit: int
        :param _Status: 按状态筛选。
        :type Status: str
        :param _ExpireTime: 按过期时间升序或降序排列。
        :type ExpireTime: str
        :param _PackageId: 按权益包ID搜索。
        :type PackageId: str
        :param _Type: 按权益包类型搜索。
        :type Type: str
        :param _Pid: 子产品编号
        :type Pid: int
        """
        self._Offset = None
        self._Limit = None
        self._Status = None
        self._ExpireTime = None
        self._PackageId = None
        self._Type = None
        self._Pid = None

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
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Pid(self):
        return self._Pid

    @Pid.setter
    def Pid(self, Pid):
        self._Pid = Pid


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._PackageId = params.get("PackageId")
        self._Type = params.get("Type")
        self._Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackagesResponse(AbstractModel):
    """DescribePackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Packages: 权益包列表。
        :type Packages: list of PackageInfo
        :param _TotalCount: 总条数。
        :type TotalCount: int
        :param _TotalBalance: 权益点总余额。
        :type TotalBalance: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Packages = None
        self._TotalCount = None
        self._TotalBalance = None
        self._RequestId = None

    @property
    def Packages(self):
        return self._Packages

    @Packages.setter
    def Packages(self, Packages):
        self._Packages = Packages

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TotalBalance(self):
        return self._TotalBalance

    @TotalBalance.setter
    def TotalBalance(self, TotalBalance):
        self._TotalBalance = TotalBalance

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Packages") is not None:
            self._Packages = []
            for item in params.get("Packages"):
                obj = PackageInfo()
                obj._deserialize(item)
                self._Packages.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._TotalBalance = params.get("TotalBalance")
        self._RequestId = params.get("RequestId")


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self._CertificateId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Content: ZIP base64 编码内容，base64 解码后可保存为 ZIP 文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param _ContentType: MIME 类型：application/zip = ZIP 压缩文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Content = None
        self._ContentType = None
        self._RequestId = None

    @property
    def Content(self):
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def ContentType(self):
        return self._ContentType

    @ContentType.setter
    def ContentType(self, ContentType):
        self._ContentType = ContentType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Content = params.get("Content")
        self._ContentType = params.get("ContentType")
        self._RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 DvAuthDetail 的内容。

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param _DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param _DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param _DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param _DvAuthKeySubDomain: DV 认证子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKeySubDomain: str
        :param _DvAuths: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuths: list of DvAuths
        """
        self._DvAuthKey = None
        self._DvAuthValue = None
        self._DvAuthDomain = None
        self._DvAuthPath = None
        self._DvAuthKeySubDomain = None
        self._DvAuths = None

    @property
    def DvAuthKey(self):
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthKeySubDomain(self):
        return self._DvAuthKeySubDomain

    @DvAuthKeySubDomain.setter
    def DvAuthKeySubDomain(self, DvAuthKeySubDomain):
        self._DvAuthKeySubDomain = DvAuthKeySubDomain

    @property
    def DvAuths(self):
        return self._DvAuths

    @DvAuths.setter
    def DvAuths(self, DvAuths):
        self._DvAuths = DvAuths


    def _deserialize(self, params):
        self._DvAuthKey = params.get("DvAuthKey")
        self._DvAuthValue = params.get("DvAuthValue")
        self._DvAuthDomain = params.get("DvAuthDomain")
        self._DvAuthPath = params.get("DvAuthPath")
        self._DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self._DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self._DvAuths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DvAuths(AbstractModel):
    """返回参数键为 DvAuths 的内容。

    """

    def __init__(self):
        r"""
        :param _DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param _DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param _DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param _DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param _DvAuthSubDomain: DV 认证子域名，
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthSubDomain: str
        :param _DvAuthVerifyType: DV 认证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthVerifyType: str
        """
        self._DvAuthKey = None
        self._DvAuthValue = None
        self._DvAuthDomain = None
        self._DvAuthPath = None
        self._DvAuthSubDomain = None
        self._DvAuthVerifyType = None

    @property
    def DvAuthKey(self):
        return self._DvAuthKey

    @DvAuthKey.setter
    def DvAuthKey(self, DvAuthKey):
        self._DvAuthKey = DvAuthKey

    @property
    def DvAuthValue(self):
        return self._DvAuthValue

    @DvAuthValue.setter
    def DvAuthValue(self, DvAuthValue):
        self._DvAuthValue = DvAuthValue

    @property
    def DvAuthDomain(self):
        return self._DvAuthDomain

    @DvAuthDomain.setter
    def DvAuthDomain(self, DvAuthDomain):
        self._DvAuthDomain = DvAuthDomain

    @property
    def DvAuthPath(self):
        return self._DvAuthPath

    @DvAuthPath.setter
    def DvAuthPath(self, DvAuthPath):
        self._DvAuthPath = DvAuthPath

    @property
    def DvAuthSubDomain(self):
        return self._DvAuthSubDomain

    @DvAuthSubDomain.setter
    def DvAuthSubDomain(self, DvAuthSubDomain):
        self._DvAuthSubDomain = DvAuthSubDomain

    @property
    def DvAuthVerifyType(self):
        return self._DvAuthVerifyType

    @DvAuthVerifyType.setter
    def DvAuthVerifyType(self, DvAuthVerifyType):
        self._DvAuthVerifyType = DvAuthVerifyType


    def _deserialize(self, params):
        self._DvAuthKey = params.get("DvAuthKey")
        self._DvAuthValue = params.get("DvAuthValue")
        self._DvAuthDomain = params.get("DvAuthDomain")
        self._DvAuthPath = params.get("DvAuthPath")
        self._DvAuthSubDomain = params.get("DvAuthSubDomain")
        self._DvAuthVerifyType = params.get("DvAuthVerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数列表

    """

    def __init__(self):
        r"""
        :param _FilterKey: 过滤参数key
        :type FilterKey: str
        :param _FilterValue: 过滤参数值
        :type FilterValue: str
        """
        self._FilterKey = None
        self._FilterValue = None

    @property
    def FilterKey(self):
        return self._FilterKey

    @FilterKey.setter
    def FilterKey(self, FilterKey):
        self._FilterKey = FilterKey

    @property
    def FilterValue(self):
        return self._FilterValue

    @FilterValue.setter
    def FilterValue(self, FilterValue):
        self._FilterValue = FilterValue


    def _deserialize(self, params):
        self._FilterKey = params.get("FilterKey")
        self._FilterValue = params.get("FilterValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostCertificateRequest(AbstractModel):
    """HostCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _ResourceType: 资源类型：目前仅限于CLB,CDN
        :type ResourceType: list of str
        """
        self._CertificateId = None
        self._ResourceType = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostCertificateResponse(AbstractModel):
    """HostCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertHostingInfo: 云资源配置详情
        :type CertHostingInfo: :class:`tencentcloud.ssl.v20191205.models.CertHostingInfo`
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertHostingInfo = None
        self._RequestId = None

    @property
    def CertHostingInfo(self):
        return self._CertHostingInfo

    @CertHostingInfo.setter
    def CertHostingInfo(self, CertHostingInfo):
        self._CertHostingInfo = CertHostingInfo

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CertHostingInfo") is not None:
            self._CertHostingInfo = CertHostingInfo()
            self._CertHostingInfo._deserialize(params.get("CertHostingInfo"))
        self._RequestId = params.get("RequestId")


class LighthouseInstanceDetail(AbstractModel):
    """Lighthouse实例

    """

    def __init__(self):
        r"""
        :param _InstanceId: 实例ID
        :type InstanceId: str
        :param _InstanceName: 实例名称
        :type InstanceName: str
        :param _IP: IP地址
        :type IP: list of str
        :param _Domain: 可选择域名
        :type Domain: list of str
        """
        self._InstanceId = None
        self._InstanceName = None
        self._IP = None
        self._Domain = None

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def IP(self):
        return self._IP

    @IP.setter
    def IP(self, IP):
        self._IP = IP

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._IP = params.get("IP")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveInstanceDetail(AbstractModel):
    """live实例详情

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 已绑定的证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _Status: -1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :type Status: int
        """
        self._Domain = None
        self._CertId = None
        self._Status = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerInfo(AbstractModel):
    """管理人信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :type Status: str
        :param _ManagerFirstName: 管理人姓名
        :type ManagerFirstName: str
        :param _ManagerLastName: 管理人姓名
        :type ManagerLastName: str
        :param _ManagerPosition: 管理人职位
        :type ManagerPosition: str
        :param _ManagerPhone: 管理人电话
        :type ManagerPhone: str
        :param _ManagerMail: 管理人邮箱
        :type ManagerMail: str
        :param _ManagerDepartment: 管理人所属部门
        :type ManagerDepartment: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _DomainCount: 管理人域名数量
        :type DomainCount: int
        :param _CertCount: 管理人证书数量
        :type CertCount: int
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _ExpireTime: 审核有效到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _SubmitAuditTime: 最近一次提交审核时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitAuditTime: str
        :param _VerifyTime: 审核通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTime: str
        :param _StatusInfo: 具体审核状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInfo: list of ManagerStatusInfo
        """
        self._Status = None
        self._ManagerFirstName = None
        self._ManagerLastName = None
        self._ManagerPosition = None
        self._ManagerPhone = None
        self._ManagerMail = None
        self._ManagerDepartment = None
        self._CreateTime = None
        self._DomainCount = None
        self._CertCount = None
        self._ManagerId = None
        self._ExpireTime = None
        self._SubmitAuditTime = None
        self._VerifyTime = None
        self._StatusInfo = None

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ManagerFirstName(self):
        return self._ManagerFirstName

    @ManagerFirstName.setter
    def ManagerFirstName(self, ManagerFirstName):
        self._ManagerFirstName = ManagerFirstName

    @property
    def ManagerLastName(self):
        return self._ManagerLastName

    @ManagerLastName.setter
    def ManagerLastName(self, ManagerLastName):
        self._ManagerLastName = ManagerLastName

    @property
    def ManagerPosition(self):
        return self._ManagerPosition

    @ManagerPosition.setter
    def ManagerPosition(self, ManagerPosition):
        self._ManagerPosition = ManagerPosition

    @property
    def ManagerPhone(self):
        return self._ManagerPhone

    @ManagerPhone.setter
    def ManagerPhone(self, ManagerPhone):
        self._ManagerPhone = ManagerPhone

    @property
    def ManagerMail(self):
        return self._ManagerMail

    @ManagerMail.setter
    def ManagerMail(self, ManagerMail):
        self._ManagerMail = ManagerMail

    @property
    def ManagerDepartment(self):
        return self._ManagerDepartment

    @ManagerDepartment.setter
    def ManagerDepartment(self, ManagerDepartment):
        self._ManagerDepartment = ManagerDepartment

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DomainCount(self):
        return self._DomainCount

    @DomainCount.setter
    def DomainCount(self, DomainCount):
        self._DomainCount = DomainCount

    @property
    def CertCount(self):
        return self._CertCount

    @CertCount.setter
    def CertCount(self, CertCount):
        self._CertCount = CertCount

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def SubmitAuditTime(self):
        return self._SubmitAuditTime

    @SubmitAuditTime.setter
    def SubmitAuditTime(self, SubmitAuditTime):
        self._SubmitAuditTime = SubmitAuditTime

    @property
    def VerifyTime(self):
        return self._VerifyTime

    @VerifyTime.setter
    def VerifyTime(self, VerifyTime):
        self._VerifyTime = VerifyTime

    @property
    def StatusInfo(self):
        return self._StatusInfo

    @StatusInfo.setter
    def StatusInfo(self, StatusInfo):
        self._StatusInfo = StatusInfo


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._ManagerFirstName = params.get("ManagerFirstName")
        self._ManagerLastName = params.get("ManagerLastName")
        self._ManagerPosition = params.get("ManagerPosition")
        self._ManagerPhone = params.get("ManagerPhone")
        self._ManagerMail = params.get("ManagerMail")
        self._ManagerDepartment = params.get("ManagerDepartment")
        self._CreateTime = params.get("CreateTime")
        self._DomainCount = params.get("DomainCount")
        self._CertCount = params.get("CertCount")
        self._ManagerId = params.get("ManagerId")
        self._ExpireTime = params.get("ExpireTime")
        self._SubmitAuditTime = params.get("SubmitAuditTime")
        self._VerifyTime = params.get("VerifyTime")
        if params.get("StatusInfo") is not None:
            self._StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = ManagerStatusInfo()
                obj._deserialize(item)
                self._StatusInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerStatusInfo(AbstractModel):
    """管理人的四种审核状态

    """


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _Alias: 备注名称。
        :type Alias: str
        """
        self._CertificateId = None
        self._Alias = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 修改成功的证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIdList: 需要修改所属项目的证书 ID 集合，最多100个证书。
        :type CertificateIdList: list of str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        """
        self._CertificateIdList = None
        self._ProjectId = None

    @property
    def CertificateIdList(self):
        return self._CertificateIdList

    @CertificateIdList.setter
    def CertificateIdList(self, CertificateIdList):
        self._CertificateIdList = CertificateIdList

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._CertificateIdList = params.get("CertificateIdList")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessCertificates: 修改所属项目成功的证书集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCertificates: list of str
        :param _FailCertificates: 修改所属项目失败的证书集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCertificates: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessCertificates = None
        self._FailCertificates = None
        self._RequestId = None

    @property
    def SuccessCertificates(self):
        return self._SuccessCertificates

    @SuccessCertificates.setter
    def SuccessCertificates(self, SuccessCertificates):
        self._SuccessCertificates = SuccessCertificates

    @property
    def FailCertificates(self):
        return self._FailCertificates

    @FailCertificates.setter
    def FailCertificates(self, FailCertificates):
        self._FailCertificates = FailCertificates

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessCertificates = params.get("SuccessCertificates")
        self._FailCertificates = params.get("FailCertificates")
        self._RequestId = params.get("RequestId")


class ModifyCertificatesExpiringNotificationSwitchRequest(AbstractModel):
    """ModifyCertificatesExpiringNotificationSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表。最多50个
        :type CertificateIds: list of str
        :param _SwitchStatus: 0:不忽略通知。1:忽略通知
        :type SwitchStatus: int
        """
        self._CertificateIds = None
        self._SwitchStatus = None

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def SwitchStatus(self):
        return self._SwitchStatus

    @SwitchStatus.setter
    def SwitchStatus(self, SwitchStatus):
        self._SwitchStatus = SwitchStatus


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._SwitchStatus = params.get("SwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificatesExpiringNotificationSwitchResponse(AbstractModel):
    """ModifyCertificatesExpiringNotificationSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateIds: 证书ID列表
        :type CertificateIds: list of str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateIds = None
        self._RequestId = None

    @property
    def CertificateIds(self):
        return self._CertificateIds

    @CertificateIds.setter
    def CertificateIds(self, CertificateIds):
        self._CertificateIds = CertificateIds

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateIds = params.get("CertificateIds")
        self._RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """证书操作日志。

    """

    def __init__(self):
        r"""
        :param _Action: 操作证书动作。
        :type Action: str
        :param _CreatedOn: 操作时间。
        :type CreatedOn: str
        """
        self._Action = None
        self._CreatedOn = None

    @property
    def Action(self):
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def CreatedOn(self):
        return self._CreatedOn

    @CreatedOn.setter
    def CreatedOn(self, CreatedOn):
        self._CreatedOn = CreatedOn


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageInfo(AbstractModel):
    """权益包基本信息

    """

    def __init__(self):
        r"""
        :param _PackageId: 权益包ID。
        :type PackageId: str
        :param _Total: 权益包内权益点总量。
        :type Total: int
        :param _Balance: 权益包内权益点余量。
        :type Balance: int
        :param _Type: 权益包名称。
        :type Type: str
        :param _SourceUin: 权益点是转入时，来源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceUin: int
        :param _Status: 权益点状态。
        :type Status: str
        :param _ExpireTime: 过期时间。
        :type ExpireTime: str
        :param _UpdateTime: 更新时间。
        :type UpdateTime: str
        :param _CreateTime: 生成时间。
        :type CreateTime: str
        :param _SourceType: 来源类型。
        :type SourceType: str
        :param _TransferOutInfos: 转移信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferOutInfos: list of PackageTransferOutInfo
        """
        self._PackageId = None
        self._Total = None
        self._Balance = None
        self._Type = None
        self._SourceUin = None
        self._Status = None
        self._ExpireTime = None
        self._UpdateTime = None
        self._CreateTime = None
        self._SourceType = None
        self._TransferOutInfos = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Balance(self):
        return self._Balance

    @Balance.setter
    def Balance(self, Balance):
        self._Balance = Balance

    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def SourceUin(self):
        return self._SourceUin

    @SourceUin.setter
    def SourceUin(self, SourceUin):
        self._SourceUin = SourceUin

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def SourceType(self):
        return self._SourceType

    @SourceType.setter
    def SourceType(self, SourceType):
        self._SourceType = SourceType

    @property
    def TransferOutInfos(self):
        return self._TransferOutInfos

    @TransferOutInfos.setter
    def TransferOutInfos(self, TransferOutInfos):
        self._TransferOutInfos = TransferOutInfos


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._Total = params.get("Total")
        self._Balance = params.get("Balance")
        self._Type = params.get("Type")
        self._SourceUin = params.get("SourceUin")
        self._Status = params.get("Status")
        self._ExpireTime = params.get("ExpireTime")
        self._UpdateTime = params.get("UpdateTime")
        self._CreateTime = params.get("CreateTime")
        self._SourceType = params.get("SourceType")
        if params.get("TransferOutInfos") is not None:
            self._TransferOutInfos = []
            for item in params.get("TransferOutInfos"):
                obj = PackageTransferOutInfo()
                obj._deserialize(item)
                self._TransferOutInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageTransferOutInfo(AbstractModel):
    """权益包转出详情

    """

    def __init__(self):
        r"""
        :param _PackageId: 权益包ID。
        :type PackageId: str
        :param _TransferCode: 转移码。
        :type TransferCode: str
        :param _TransferCount: 本次转移点数。
        :type TransferCount: int
        :param _ReceivePackageId: 转入的PackageID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceivePackageId: str
        :param _ExpireTime: 本次转移过期时间。
        :type ExpireTime: str
        :param _CreateTime: 本次转移生成时间。
        :type CreateTime: str
        :param _UpdateTime: 本次转移更新时间。
        :type UpdateTime: str
        :param _TransferStatus: 转移状态。
        :type TransferStatus: str
        :param _ReceiverUin: 接收者uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverUin: int
        :param _ReceiveTime: 接收时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiveTime: str
        """
        self._PackageId = None
        self._TransferCode = None
        self._TransferCount = None
        self._ReceivePackageId = None
        self._ExpireTime = None
        self._CreateTime = None
        self._UpdateTime = None
        self._TransferStatus = None
        self._ReceiverUin = None
        self._ReceiveTime = None

    @property
    def PackageId(self):
        return self._PackageId

    @PackageId.setter
    def PackageId(self, PackageId):
        self._PackageId = PackageId

    @property
    def TransferCode(self):
        return self._TransferCode

    @TransferCode.setter
    def TransferCode(self, TransferCode):
        self._TransferCode = TransferCode

    @property
    def TransferCount(self):
        return self._TransferCount

    @TransferCount.setter
    def TransferCount(self, TransferCount):
        self._TransferCount = TransferCount

    @property
    def ReceivePackageId(self):
        return self._ReceivePackageId

    @ReceivePackageId.setter
    def ReceivePackageId(self, ReceivePackageId):
        self._ReceivePackageId = ReceivePackageId

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def TransferStatus(self):
        return self._TransferStatus

    @TransferStatus.setter
    def TransferStatus(self, TransferStatus):
        self._TransferStatus = TransferStatus

    @property
    def ReceiverUin(self):
        return self._ReceiverUin

    @ReceiverUin.setter
    def ReceiverUin(self, ReceiverUin):
        self._ReceiverUin = ReceiverUin

    @property
    def ReceiveTime(self):
        return self._ReceiveTime

    @ReceiveTime.setter
    def ReceiveTime(self, ReceiveTime):
        self._ReceiveTime = ReceiveTime


    def _deserialize(self, params):
        self._PackageId = params.get("PackageId")
        self._TransferCode = params.get("TransferCode")
        self._TransferCount = params.get("TransferCount")
        self._ReceivePackageId = params.get("ReceivePackageId")
        self._ExpireTime = params.get("ExpireTime")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._TransferStatus = params.get("TransferStatus")
        self._ReceiverUin = params.get("ReceiverUin")
        self._ReceiveTime = params.get("ReceiveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreAuditInfo(AbstractModel):
    """预审核信息列表

    """

    def __init__(self):
        r"""
        :param _TotalPeriod: 证书总年限
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPeriod: int
        :param _NowPeriod: 证书当前年限
注意：此字段可能返回 null，表示取不到有效值。
        :type NowPeriod: int
        :param _ManagerId: 证书预审核管理人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagerId: str
        """
        self._TotalPeriod = None
        self._NowPeriod = None
        self._ManagerId = None

    @property
    def TotalPeriod(self):
        return self._TotalPeriod

    @TotalPeriod.setter
    def TotalPeriod(self, TotalPeriod):
        self._TotalPeriod = TotalPeriod

    @property
    def NowPeriod(self):
        return self._NowPeriod

    @NowPeriod.setter
    def NowPeriod(self, NowPeriod):
        self._NowPeriod = NowPeriod

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._TotalPeriod = params.get("TotalPeriod")
        self._NowPeriod = params.get("NowPeriod")
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 下，key为 ProjectInfo 的内容。

    """

    def __init__(self):
        r"""
        :param _ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param _ProjectCreatorUin: 项目创建用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectCreatorUin: int
        :param _ProjectCreateTime: 项目创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectCreateTime: str
        :param _ProjectResume: 项目信息简述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectResume: str
        :param _OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: int
        :param _ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        """
        self._ProjectName = None
        self._ProjectCreatorUin = None
        self._ProjectCreateTime = None
        self._ProjectResume = None
        self._OwnerUin = None
        self._ProjectId = None

    @property
    def ProjectName(self):
        return self._ProjectName

    @ProjectName.setter
    def ProjectName(self, ProjectName):
        self._ProjectName = ProjectName

    @property
    def ProjectCreatorUin(self):
        return self._ProjectCreatorUin

    @ProjectCreatorUin.setter
    def ProjectCreatorUin(self, ProjectCreatorUin):
        self._ProjectCreatorUin = ProjectCreatorUin

    @property
    def ProjectCreateTime(self):
        return self._ProjectCreateTime

    @ProjectCreateTime.setter
    def ProjectCreateTime(self, ProjectCreateTime):
        self._ProjectCreateTime = ProjectCreateTime

    @property
    def ProjectResume(self):
        return self._ProjectResume

    @ProjectResume.setter
    def ProjectResume(self, ProjectResume):
        self._ProjectResume = ProjectResume

    @property
    def OwnerUin(self):
        return self._OwnerUin

    @OwnerUin.setter
    def OwnerUin(self, OwnerUin):
        self._OwnerUin = OwnerUin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId


    def _deserialize(self, params):
        self._ProjectName = params.get("ProjectName")
        self._ProjectCreatorUin = params.get("ProjectCreatorUin")
        self._ProjectCreateTime = params.get("ProjectCreateTime")
        self._ProjectResume = params.get("ProjectResume")
        self._OwnerUin = params.get("OwnerUin")
        self._ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _ValidType: 验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :type ValidType: str
        :param _CsrType: 类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。
        :type CsrType: str
        :param _CsrContent: CSR 内容。
        :type CsrContent: str
        :param _CsrkeyPassword: KEY 密码。
        :type CsrkeyPassword: str
        :param _Reason: 重颁发原因。
        :type Reason: str
        """
        self._CertificateId = None
        self._ValidType = None
        self._CsrType = None
        self._CsrContent = None
        self._CsrkeyPassword = None
        self._Reason = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ValidType(self):
        return self._ValidType

    @ValidType.setter
    def ValidType(self, ValidType):
        self._ValidType = ValidType

    @property
    def CsrType(self):
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CsrkeyPassword(self):
        return self._CsrkeyPassword

    @CsrkeyPassword.setter
    def CsrkeyPassword(self, CsrkeyPassword):
        self._CsrkeyPassword = CsrkeyPassword

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ValidType = params.get("ValidType")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CsrkeyPassword = params.get("CsrkeyPassword")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class ResourceTypeRegions(AbstractModel):
    """云资源地域列表

    """

    def __init__(self):
        r"""
        :param _ResourceType: 云资源类型
        :type ResourceType: str
        :param _Regions: 地域列表
        :type Regions: list of str
        """
        self._ResourceType = None
        self._Regions = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        self._Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeCertificateRequest(AbstractModel):
    """RevokeCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _Reason: 吊销证书原因。
        :type Reason: str
        """
        self._CertificateId = None
        self._Reason = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def Reason(self):
        return self._Reason

    @Reason.setter
    def Reason(self, Reason):
        self._Reason = Reason


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeCertificateResponse(AbstractModel):
    """RevokeCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RevokeDomainValidateAuths: 吊销证书域名验证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RevokeDomainValidateAuths: list of RevokeDomainValidateAuths
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RevokeDomainValidateAuths = None
        self._RequestId = None

    @property
    def RevokeDomainValidateAuths(self):
        return self._RevokeDomainValidateAuths

    @RevokeDomainValidateAuths.setter
    def RevokeDomainValidateAuths(self, RevokeDomainValidateAuths):
        self._RevokeDomainValidateAuths = RevokeDomainValidateAuths

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("RevokeDomainValidateAuths") is not None:
            self._RevokeDomainValidateAuths = []
            for item in params.get("RevokeDomainValidateAuths"):
                obj = RevokeDomainValidateAuths()
                obj._deserialize(item)
                self._RevokeDomainValidateAuths.append(obj)
        self._RequestId = params.get("RequestId")


class RevokeDomainValidateAuths(AbstractModel):
    """返回参数键为 RevokeDomainValidateAuths 的内容。

    """

    def __init__(self):
        r"""
        :param _DomainValidateAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthPath: str
        :param _DomainValidateAuthKey: DV 认证 KEY。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthKey: str
        :param _DomainValidateAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthValue: str
        :param _DomainValidateAuthDomain: DV 认证域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthDomain: str
        """
        self._DomainValidateAuthPath = None
        self._DomainValidateAuthKey = None
        self._DomainValidateAuthValue = None
        self._DomainValidateAuthDomain = None

    @property
    def DomainValidateAuthPath(self):
        return self._DomainValidateAuthPath

    @DomainValidateAuthPath.setter
    def DomainValidateAuthPath(self, DomainValidateAuthPath):
        self._DomainValidateAuthPath = DomainValidateAuthPath

    @property
    def DomainValidateAuthKey(self):
        return self._DomainValidateAuthKey

    @DomainValidateAuthKey.setter
    def DomainValidateAuthKey(self, DomainValidateAuthKey):
        self._DomainValidateAuthKey = DomainValidateAuthKey

    @property
    def DomainValidateAuthValue(self):
        return self._DomainValidateAuthValue

    @DomainValidateAuthValue.setter
    def DomainValidateAuthValue(self, DomainValidateAuthValue):
        self._DomainValidateAuthValue = DomainValidateAuthValue

    @property
    def DomainValidateAuthDomain(self):
        return self._DomainValidateAuthDomain

    @DomainValidateAuthDomain.setter
    def DomainValidateAuthDomain(self, DomainValidateAuthDomain):
        self._DomainValidateAuthDomain = DomainValidateAuthDomain


    def _deserialize(self, params):
        self._DomainValidateAuthPath = params.get("DomainValidateAuthPath")
        self._DomainValidateAuthKey = params.get("DomainValidateAuthKey")
        self._DomainValidateAuthValue = params.get("DomainValidateAuthValue")
        self._DomainValidateAuthDomain = params.get("DomainValidateAuthDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RootCertificates(AbstractModel):
    """根证书

    """

    def __init__(self):
        r"""
        :param _Sign: 国密签名证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Sign: str
        :param _Encrypt: 国密加密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: str
        :param _Standard: 标准证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        """
        self._Sign = None
        self._Encrypt = None
        self._Standard = None

    @property
    def Sign(self):
        return self._Sign

    @Sign.setter
    def Sign(self, Sign):
        self._Sign = Sign

    @property
    def Encrypt(self):
        return self._Encrypt

    @Encrypt.setter
    def Encrypt(self, Encrypt):
        self._Encrypt = Encrypt

    @property
    def Standard(self):
        return self._Standard

    @Standard.setter
    def Standard(self, Standard):
        self._Standard = Standard


    def _deserialize(self, params):
        self._Sign = params.get("Sign")
        self._Encrypt = params.get("Encrypt")
        self._Standard = params.get("Standard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAuditManagerRequest(AbstractModel):
    """SubmitAuditManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        """
        self._ManagerId = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAuditManagerResponse(AbstractModel):
    """SubmitAuditManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ManagerId = None
        self._RequestId = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _CsrType: CSR 生成方式：online = 在线生成, parse = 手动上传。
        :type CsrType: str
        :param _CsrContent: 上传的 CSR 内容。
        :type CsrContent: str
        :param _CertificateDomain: 绑定证书的域名。
        :type CertificateDomain: str
        :param _DomainList: 上传的域名数组（多域名证书可以上传）。
        :type DomainList: list of str
        :param _KeyPassword: 私钥密码（非必填）。
        :type KeyPassword: str
        :param _OrganizationName: 公司名称。
        :type OrganizationName: str
        :param _OrganizationDivision: 部门名称。
        :type OrganizationDivision: str
        :param _OrganizationAddress: 公司详细地址。
        :type OrganizationAddress: str
        :param _OrganizationCountry: 国家名称，如中国：CN 。
        :type OrganizationCountry: str
        :param _OrganizationCity: 公司所在城市。
        :type OrganizationCity: str
        :param _OrganizationRegion: 公司所在省份。
        :type OrganizationRegion: str
        :param _PostalCode: 公司邮编。
        :type PostalCode: str
        :param _PhoneAreaCode: 公司座机区号。
        :type PhoneAreaCode: str
        :param _PhoneNumber: 公司座机号码。
        :type PhoneNumber: str
        :param _VerifyType: 证书验证方式。验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :type VerifyType: str
        :param _AdminFirstName: 管理人名。
        :type AdminFirstName: str
        :param _AdminLastName: 管理人姓。
        :type AdminLastName: str
        :param _AdminPhoneNum: 管理人手机号码。
        :type AdminPhoneNum: str
        :param _AdminEmail: 管理人邮箱地址。
        :type AdminEmail: str
        :param _AdminPosition: 管理人职位。
        :type AdminPosition: str
        :param _ContactFirstName: 联系人名。
        :type ContactFirstName: str
        :param _ContactLastName: 联系人姓。
        :type ContactLastName: str
        :param _ContactEmail: 联系人邮箱地址。
        :type ContactEmail: str
        :param _ContactNumber: 联系人手机号码。
        :type ContactNumber: str
        :param _ContactPosition: 联系人职位。
        :type ContactPosition: str
        """
        self._CertificateId = None
        self._CsrType = None
        self._CsrContent = None
        self._CertificateDomain = None
        self._DomainList = None
        self._KeyPassword = None
        self._OrganizationName = None
        self._OrganizationDivision = None
        self._OrganizationAddress = None
        self._OrganizationCountry = None
        self._OrganizationCity = None
        self._OrganizationRegion = None
        self._PostalCode = None
        self._PhoneAreaCode = None
        self._PhoneNumber = None
        self._VerifyType = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhoneNum = None
        self._AdminEmail = None
        self._AdminPosition = None
        self._ContactFirstName = None
        self._ContactLastName = None
        self._ContactEmail = None
        self._ContactNumber = None
        self._ContactPosition = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def CsrType(self):
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType

    @property
    def AdminFirstName(self):
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactEmail(self):
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactPosition(self):
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CertificateDomain = params.get("CertificateDomain")
        self._DomainList = params.get("DomainList")
        self._KeyPassword = params.get("KeyPassword")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationDivision = params.get("OrganizationDivision")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._OrganizationCountry = params.get("OrganizationCountry")
        self._OrganizationCity = params.get("OrganizationCity")
        self._OrganizationRegion = params.get("OrganizationRegion")
        self._PostalCode = params.get("PostalCode")
        self._PhoneAreaCode = params.get("PhoneAreaCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._VerifyType = params.get("VerifyType")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhoneNum = params.get("AdminPhoneNum")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminPosition = params.get("AdminPosition")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ContactLastName = params.get("ContactLastName")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactNumber = params.get("ContactNumber")
        self._ContactPosition = params.get("ContactPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 SubmittedData 的内容。

    """

    def __init__(self):
        r"""
        :param _CsrType: CSR 类型，（online = 在线生成CSR，parse = 粘贴 CSR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrType: str
        :param _CsrContent: CSR 内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrContent: str
        :param _CertificateDomain: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateDomain: str
        :param _DomainList: DNS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        :param _KeyPassword: 私钥密码。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyPassword: str
        :param _OrganizationName: 企业或单位名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param _OrganizationDivision: 部门。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationDivision: str
        :param _OrganizationAddress: 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationAddress: str
        :param _OrganizationCountry: 国家。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCountry: str
        :param _OrganizationCity: 市。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCity: str
        :param _OrganizationRegion: 省。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationRegion: str
        :param _PostalCode: 邮政编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param _PhoneAreaCode: 座机区号。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneAreaCode: str
        :param _PhoneNumber: 座机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param _AdminFirstName: 管理员名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminFirstName: str
        :param _AdminLastName: 管理员姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminLastName: str
        :param _AdminPhoneNum: 管理员电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPhoneNum: str
        :param _AdminEmail: 管理员邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminEmail: str
        :param _AdminPosition: 管理员职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPosition: str
        :param _ContactFirstName: 联系人名。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactFirstName: str
        :param _ContactLastName: 联系人姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactLastName: str
        :param _ContactNumber: 联系人电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactNumber: str
        :param _ContactEmail: 联系人邮箱地址，
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactEmail: str
        :param _ContactPosition: 联系人职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactPosition: str
        :param _VerifyType: 验证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        """
        self._CsrType = None
        self._CsrContent = None
        self._CertificateDomain = None
        self._DomainList = None
        self._KeyPassword = None
        self._OrganizationName = None
        self._OrganizationDivision = None
        self._OrganizationAddress = None
        self._OrganizationCountry = None
        self._OrganizationCity = None
        self._OrganizationRegion = None
        self._PostalCode = None
        self._PhoneAreaCode = None
        self._PhoneNumber = None
        self._AdminFirstName = None
        self._AdminLastName = None
        self._AdminPhoneNum = None
        self._AdminEmail = None
        self._AdminPosition = None
        self._ContactFirstName = None
        self._ContactLastName = None
        self._ContactNumber = None
        self._ContactEmail = None
        self._ContactPosition = None
        self._VerifyType = None

    @property
    def CsrType(self):
        return self._CsrType

    @CsrType.setter
    def CsrType(self, CsrType):
        self._CsrType = CsrType

    @property
    def CsrContent(self):
        return self._CsrContent

    @CsrContent.setter
    def CsrContent(self, CsrContent):
        self._CsrContent = CsrContent

    @property
    def CertificateDomain(self):
        return self._CertificateDomain

    @CertificateDomain.setter
    def CertificateDomain(self, CertificateDomain):
        self._CertificateDomain = CertificateDomain

    @property
    def DomainList(self):
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def KeyPassword(self):
        return self._KeyPassword

    @KeyPassword.setter
    def KeyPassword(self, KeyPassword):
        self._KeyPassword = KeyPassword

    @property
    def OrganizationName(self):
        return self._OrganizationName

    @OrganizationName.setter
    def OrganizationName(self, OrganizationName):
        self._OrganizationName = OrganizationName

    @property
    def OrganizationDivision(self):
        return self._OrganizationDivision

    @OrganizationDivision.setter
    def OrganizationDivision(self, OrganizationDivision):
        self._OrganizationDivision = OrganizationDivision

    @property
    def OrganizationAddress(self):
        return self._OrganizationAddress

    @OrganizationAddress.setter
    def OrganizationAddress(self, OrganizationAddress):
        self._OrganizationAddress = OrganizationAddress

    @property
    def OrganizationCountry(self):
        return self._OrganizationCountry

    @OrganizationCountry.setter
    def OrganizationCountry(self, OrganizationCountry):
        self._OrganizationCountry = OrganizationCountry

    @property
    def OrganizationCity(self):
        return self._OrganizationCity

    @OrganizationCity.setter
    def OrganizationCity(self, OrganizationCity):
        self._OrganizationCity = OrganizationCity

    @property
    def OrganizationRegion(self):
        return self._OrganizationRegion

    @OrganizationRegion.setter
    def OrganizationRegion(self, OrganizationRegion):
        self._OrganizationRegion = OrganizationRegion

    @property
    def PostalCode(self):
        return self._PostalCode

    @PostalCode.setter
    def PostalCode(self, PostalCode):
        self._PostalCode = PostalCode

    @property
    def PhoneAreaCode(self):
        return self._PhoneAreaCode

    @PhoneAreaCode.setter
    def PhoneAreaCode(self, PhoneAreaCode):
        self._PhoneAreaCode = PhoneAreaCode

    @property
    def PhoneNumber(self):
        return self._PhoneNumber

    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber):
        self._PhoneNumber = PhoneNumber

    @property
    def AdminFirstName(self):
        return self._AdminFirstName

    @AdminFirstName.setter
    def AdminFirstName(self, AdminFirstName):
        self._AdminFirstName = AdminFirstName

    @property
    def AdminLastName(self):
        return self._AdminLastName

    @AdminLastName.setter
    def AdminLastName(self, AdminLastName):
        self._AdminLastName = AdminLastName

    @property
    def AdminPhoneNum(self):
        return self._AdminPhoneNum

    @AdminPhoneNum.setter
    def AdminPhoneNum(self, AdminPhoneNum):
        self._AdminPhoneNum = AdminPhoneNum

    @property
    def AdminEmail(self):
        return self._AdminEmail

    @AdminEmail.setter
    def AdminEmail(self, AdminEmail):
        self._AdminEmail = AdminEmail

    @property
    def AdminPosition(self):
        return self._AdminPosition

    @AdminPosition.setter
    def AdminPosition(self, AdminPosition):
        self._AdminPosition = AdminPosition

    @property
    def ContactFirstName(self):
        return self._ContactFirstName

    @ContactFirstName.setter
    def ContactFirstName(self, ContactFirstName):
        self._ContactFirstName = ContactFirstName

    @property
    def ContactLastName(self):
        return self._ContactLastName

    @ContactLastName.setter
    def ContactLastName(self, ContactLastName):
        self._ContactLastName = ContactLastName

    @property
    def ContactNumber(self):
        return self._ContactNumber

    @ContactNumber.setter
    def ContactNumber(self, ContactNumber):
        self._ContactNumber = ContactNumber

    @property
    def ContactEmail(self):
        return self._ContactEmail

    @ContactEmail.setter
    def ContactEmail(self, ContactEmail):
        self._ContactEmail = ContactEmail

    @property
    def ContactPosition(self):
        return self._ContactPosition

    @ContactPosition.setter
    def ContactPosition(self, ContactPosition):
        self._ContactPosition = ContactPosition

    @property
    def VerifyType(self):
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._CsrType = params.get("CsrType")
        self._CsrContent = params.get("CsrContent")
        self._CertificateDomain = params.get("CertificateDomain")
        self._DomainList = params.get("DomainList")
        self._KeyPassword = params.get("KeyPassword")
        self._OrganizationName = params.get("OrganizationName")
        self._OrganizationDivision = params.get("OrganizationDivision")
        self._OrganizationAddress = params.get("OrganizationAddress")
        self._OrganizationCountry = params.get("OrganizationCountry")
        self._OrganizationCity = params.get("OrganizationCity")
        self._OrganizationRegion = params.get("OrganizationRegion")
        self._PostalCode = params.get("PostalCode")
        self._PhoneAreaCode = params.get("PhoneAreaCode")
        self._PhoneNumber = params.get("PhoneNumber")
        self._AdminFirstName = params.get("AdminFirstName")
        self._AdminLastName = params.get("AdminLastName")
        self._AdminPhoneNum = params.get("AdminPhoneNum")
        self._AdminEmail = params.get("AdminEmail")
        self._AdminPosition = params.get("AdminPosition")
        self._ContactFirstName = params.get("ContactFirstName")
        self._ContactLastName = params.get("ContactLastName")
        self._ContactNumber = params.get("ContactNumber")
        self._ContactEmail = params.get("ContactEmail")
        self._ContactPosition = params.get("ContactPosition")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
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
        


class TeoInstanceDetail(AbstractModel):
    """teo实例详情

    """

    def __init__(self):
        r"""
        :param _Host: 域名
        :type Host: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _ZoneId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param _Status: 域名状态
        :type Status: str
        """
        self._Host = None
        self._CertId = None
        self._ZoneId = None
        self._Status = None

    @property
    def Host(self):
        return self._Host

    @Host.setter
    def Host(self, Host):
        self._Host = Host

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def ZoneId(self):
        return self._ZoneId

    @ZoneId.setter
    def ZoneId(self, ZoneId):
        self._ZoneId = ZoneId

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._Host = params.get("Host")
        self._CertId = params.get("CertId")
        self._ZoneId = params.get("ZoneId")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeIngressDetail(AbstractModel):
    """tke ingress实例详情

    """

    def __init__(self):
        r"""
        :param _IngressName: ingress名称
        :type IngressName: str
        :param _TlsDomains: tls域名列表
        :type TlsDomains: list of str
        :param _Domains: ingress域名列表
        :type Domains: list of str
        """
        self._IngressName = None
        self._TlsDomains = None
        self._Domains = None

    @property
    def IngressName(self):
        return self._IngressName

    @IngressName.setter
    def IngressName(self, IngressName):
        self._IngressName = IngressName

    @property
    def TlsDomains(self):
        return self._TlsDomains

    @TlsDomains.setter
    def TlsDomains(self, TlsDomains):
        self._TlsDomains = TlsDomains

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._IngressName = params.get("IngressName")
        self._TlsDomains = params.get("TlsDomains")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeInstanceDetail(AbstractModel):
    """tke实例详情

    """

    def __init__(self):
        r"""
        :param _ClusterId: 集群ID
        :type ClusterId: str
        :param _ClusterName: 集群名称
        :type ClusterName: str
        :param _NamespaceList: 集群命名空间列表
        :type NamespaceList: list of TkeNameSpaceDetail
        """
        self._ClusterId = None
        self._ClusterName = None
        self._NamespaceList = None

    @property
    def ClusterId(self):
        return self._ClusterId

    @ClusterId.setter
    def ClusterId(self, ClusterId):
        self._ClusterId = ClusterId

    @property
    def ClusterName(self):
        return self._ClusterName

    @ClusterName.setter
    def ClusterName(self, ClusterName):
        self._ClusterName = ClusterName

    @property
    def NamespaceList(self):
        return self._NamespaceList

    @NamespaceList.setter
    def NamespaceList(self, NamespaceList):
        self._NamespaceList = NamespaceList


    def _deserialize(self, params):
        self._ClusterId = params.get("ClusterId")
        self._ClusterName = params.get("ClusterName")
        if params.get("NamespaceList") is not None:
            self._NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TkeNameSpaceDetail()
                obj._deserialize(item)
                self._NamespaceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeNameSpaceDetail(AbstractModel):
    """tke namespace详情

    """

    def __init__(self):
        r"""
        :param _Name: namespace名称
        :type Name: str
        :param _SecretList: secret列表
        :type SecretList: list of TkeSecretDetail
        """
        self._Name = None
        self._SecretList = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def SecretList(self):
        return self._SecretList

    @SecretList.setter
    def SecretList(self, SecretList):
        self._SecretList = SecretList


    def _deserialize(self, params):
        self._Name = params.get("Name")
        if params.get("SecretList") is not None:
            self._SecretList = []
            for item in params.get("SecretList"):
                obj = TkeSecretDetail()
                obj._deserialize(item)
                self._SecretList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeSecretDetail(AbstractModel):
    """tke secret详情

    """

    def __init__(self):
        r"""
        :param _Name: secret名称
        :type Name: str
        :param _CertId: 证书ID
        :type CertId: str
        :param _IngressList: ingress列表
        :type IngressList: list of TkeIngressDetail
        :param _NoMatchDomains: 和新证书不匹配的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self._Name = None
        self._CertId = None
        self._IngressList = None
        self._NoMatchDomains = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def IngressList(self):
        return self._IngressList

    @IngressList.setter
    def IngressList(self, IngressList):
        self._IngressList = IngressList

    @property
    def NoMatchDomains(self):
        return self._NoMatchDomains

    @NoMatchDomains.setter
    def NoMatchDomains(self, NoMatchDomains):
        self._NoMatchDomains = NoMatchDomains


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._CertId = params.get("CertId")
        if params.get("IngressList") is not None:
            self._IngressList = []
            for item in params.get("IngressList"):
                obj = TkeIngressDetail()
                obj._deserialize(item)
                self._IngressList.append(obj)
        self._NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceRequest(AbstractModel):
    """UpdateCertificateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 一键更新新证书ID
        :type CertificateId: str
        :param _OldCertificateId: 一键更新原证书ID
        :type OldCertificateId: str
        :param _ResourceTypes: 需要部署的资源类型
        :type ResourceTypes: list of str
        :param _Regions: 需要部署的地域列表（废弃）
        :type Regions: list of str
        :param _ResourceTypesRegions: 云资源需要部署的地域列表
        :type ResourceTypesRegions: list of ResourceTypeRegions
        """
        self._CertificateId = None
        self._OldCertificateId = None
        self._ResourceTypes = None
        self._Regions = None
        self._ResourceTypesRegions = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def OldCertificateId(self):
        return self._OldCertificateId

    @OldCertificateId.setter
    def OldCertificateId(self, OldCertificateId):
        self._OldCertificateId = OldCertificateId

    @property
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def ResourceTypesRegions(self):
        return self._ResourceTypesRegions

    @ResourceTypesRegions.setter
    def ResourceTypesRegions(self, ResourceTypesRegions):
        self._ResourceTypesRegions = ResourceTypesRegions


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._OldCertificateId = params.get("OldCertificateId")
        self._ResourceTypes = params.get("ResourceTypes")
        self._Regions = params.get("Regions")
        if params.get("ResourceTypesRegions") is not None:
            self._ResourceTypesRegions = []
            for item in params.get("ResourceTypesRegions"):
                obj = ResourceTypeRegions()
                obj._deserialize(item)
                self._ResourceTypesRegions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceResponse(AbstractModel):
    """UpdateCertificateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 云资源部署任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordId: int
        :param _DeployStatus: 部署状态，1表示部署成功，0表示部署失败
        :type DeployStatus: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._DeployStatus = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployStatus(self):
        return self._DeployStatus

    @DeployStatus.setter
    def DeployStatus(self, DeployStatus):
        self._DeployStatus = DeployStatus

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployStatus = params.get("DeployStatus")
        self._RequestId = params.get("RequestId")


class UpdateCertificateRecordRetryRequest(AbstractModel):
    """UpdateCertificateRecordRetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        :param _DeployRecordDetailId: 待重试部署记录详情ID
        :type DeployRecordDetailId: int
        """
        self._DeployRecordId = None
        self._DeployRecordDetailId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def DeployRecordDetailId(self):
        return self._DeployRecordDetailId

    @DeployRecordDetailId.setter
    def DeployRecordDetailId(self, DeployRecordDetailId):
        self._DeployRecordDetailId = DeployRecordDetailId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRetryResponse(AbstractModel):
    """UpdateCertificateRecordRetry返回参数结构体

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


class UpdateCertificateRecordRollbackRequest(AbstractModel):
    """UpdateCertificateRecordRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        """
        self._DeployRecordId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRollbackResponse(AbstractModel):
    """UpdateCertificateRecordRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DeployRecordId: 回滚部署记录ID
        :type DeployRecordId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DeployRecordId = None
        self._RequestId = None

    @property
    def DeployRecordId(self):
        return self._DeployRecordId

    @DeployRecordId.setter
    def DeployRecordId(self, DeployRecordId):
        self._DeployRecordId = DeployRecordId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DeployRecordId = params.get("DeployRecordId")
        self._RequestId = params.get("RequestId")


class UpdateRecordDetail(AbstractModel):
    """更新记录详情

    """

    def __init__(self):
        r"""
        :param _Id: 详情记录id
        :type Id: int
        :param _CertId: 新证书ID
        :type CertId: str
        :param _OldCertId: 旧证书ID
        :type OldCertId: str
        :param _Domains: 部署域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _Region: 部署地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Status: 部署状态
        :type Status: int
        :param _ErrorMsg: 部署错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param _CreateTime: 部署时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次更新时间
        :type UpdateTime: str
        :param _InstanceId: 部署实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param _InstanceName: 部署实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param _ListenerId: 部署监听器ID（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param _ListenerName: 部署监听器名称（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param _Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param _SniSwitch: 是否开启SNI（CLB专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param _Bucket: bucket名称（COS专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param _Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        :param _Namespace: 命名空间（TKE专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param _SecretName: secret名称（TKE专用）
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._Domains = None
        self._ResourceType = None
        self._Region = None
        self._Status = None
        self._ErrorMsg = None
        self._CreateTime = None
        self._UpdateTime = None
        self._InstanceId = None
        self._InstanceName = None
        self._ListenerId = None
        self._ListenerName = None
        self._Protocol = None
        self._SniSwitch = None
        self._Bucket = None
        self._Port = None
        self._Namespace = None
        self._SecretName = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def Region(self):
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorMsg(self):
        return self._ErrorMsg

    @ErrorMsg.setter
    def ErrorMsg(self, ErrorMsg):
        self._ErrorMsg = ErrorMsg

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def InstanceId(self):
        return self._InstanceId

    @InstanceId.setter
    def InstanceId(self, InstanceId):
        self._InstanceId = InstanceId

    @property
    def InstanceName(self):
        return self._InstanceName

    @InstanceName.setter
    def InstanceName(self, InstanceName):
        self._InstanceName = InstanceName

    @property
    def ListenerId(self):
        return self._ListenerId

    @ListenerId.setter
    def ListenerId(self, ListenerId):
        self._ListenerId = ListenerId

    @property
    def ListenerName(self):
        return self._ListenerName

    @ListenerName.setter
    def ListenerName(self, ListenerName):
        self._ListenerName = ListenerName

    @property
    def Protocol(self):
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def SniSwitch(self):
        return self._SniSwitch

    @SniSwitch.setter
    def SniSwitch(self, SniSwitch):
        self._SniSwitch = SniSwitch

    @property
    def Bucket(self):
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket

    @property
    def Port(self):
        return self._Port

    @Port.setter
    def Port(self, Port):
        self._Port = Port

    @property
    def Namespace(self):
        return self._Namespace

    @Namespace.setter
    def Namespace(self, Namespace):
        self._Namespace = Namespace

    @property
    def SecretName(self):
        return self._SecretName

    @SecretName.setter
    def SecretName(self, SecretName):
        self._SecretName = SecretName


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._Domains = params.get("Domains")
        self._ResourceType = params.get("ResourceType")
        self._Region = params.get("Region")
        self._Status = params.get("Status")
        self._ErrorMsg = params.get("ErrorMsg")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        self._InstanceId = params.get("InstanceId")
        self._InstanceName = params.get("InstanceName")
        self._ListenerId = params.get("ListenerId")
        self._ListenerName = params.get("ListenerName")
        self._Protocol = params.get("Protocol")
        self._SniSwitch = params.get("SniSwitch")
        self._Bucket = params.get("Bucket")
        self._Port = params.get("Port")
        self._Namespace = params.get("Namespace")
        self._SecretName = params.get("SecretName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordDetails(AbstractModel):
    """更新记录详情列表

    """

    def __init__(self):
        r"""
        :param _ResourceType: 部署资源类型
        :type ResourceType: str
        :param _List: 部署资源详情列表
        :type List: list of UpdateRecordDetail
        :param _TotalCount: 该部署资源总数
        :type TotalCount: int
        """
        self._ResourceType = None
        self._List = None
        self._TotalCount = None

    @property
    def ResourceType(self):
        return self._ResourceType

    @ResourceType.setter
    def ResourceType(self, ResourceType):
        self._ResourceType = ResourceType

    @property
    def List(self):
        return self._List

    @List.setter
    def List(self, List):
        self._List = List

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount


    def _deserialize(self, params):
        self._ResourceType = params.get("ResourceType")
        if params.get("List") is not None:
            self._List = []
            for item in params.get("List"):
                obj = UpdateRecordDetail()
                obj._deserialize(item)
                self._List.append(obj)
        self._TotalCount = params.get("TotalCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordInfo(AbstractModel):
    """部署记录信息

    """

    def __init__(self):
        r"""
        :param _Id: 记录ID
        :type Id: int
        :param _CertId: 新证书ID
        :type CertId: str
        :param _OldCertId: 原证书ID
        :type OldCertId: str
        :param _ResourceTypes: 部署资源类型列表
        :type ResourceTypes: list of str
        :param _Regions: 部署地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of str
        :param _Status: 部署状态
        :type Status: int
        :param _CreateTime: 部署时间
        :type CreateTime: str
        :param _UpdateTime: 最后一次更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._CertId = None
        self._OldCertId = None
        self._ResourceTypes = None
        self._Regions = None
        self._Status = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def OldCertId(self):
        return self._OldCertId

    @OldCertId.setter
    def OldCertId(self, OldCertId):
        self._OldCertId = OldCertId

    @property
    def ResourceTypes(self):
        return self._ResourceTypes

    @ResourceTypes.setter
    def ResourceTypes(self, ResourceTypes):
        self._ResourceTypes = ResourceTypes

    @property
    def Regions(self):
        return self._Regions

    @Regions.setter
    def Regions(self, Regions):
        self._Regions = Regions

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._CertId = params.get("CertId")
        self._OldCertId = params.get("OldCertId")
        self._ResourceTypes = params.get("ResourceTypes")
        self._Regions = params.get("Regions")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificatePublicKey: 证书内容。
        :type CertificatePublicKey: str
        :param _CertificatePrivateKey: 私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。
        :type CertificatePrivateKey: str
        :param _CertificateType: 证书类型，默认 SVR。CA = CA证书，SVR = 服务器证书。
        :type CertificateType: str
        :param _Alias: 备注名称。
        :type Alias: str
        :param _ProjectId: 项目 ID。
        :type ProjectId: int
        :param _CertificateUse: 证书用途/证书来源。“CLB，CDN，WAF，LIVE，DDOS”
        :type CertificateUse: str
        :param _Repeatable: 相同的证书是否允许重复上传
        :type Repeatable: bool
        """
        self._CertificatePublicKey = None
        self._CertificatePrivateKey = None
        self._CertificateType = None
        self._Alias = None
        self._ProjectId = None
        self._CertificateUse = None
        self._Repeatable = None

    @property
    def CertificatePublicKey(self):
        return self._CertificatePublicKey

    @CertificatePublicKey.setter
    def CertificatePublicKey(self, CertificatePublicKey):
        self._CertificatePublicKey = CertificatePublicKey

    @property
    def CertificatePrivateKey(self):
        return self._CertificatePrivateKey

    @CertificatePrivateKey.setter
    def CertificatePrivateKey(self, CertificatePrivateKey):
        self._CertificatePrivateKey = CertificatePrivateKey

    @property
    def CertificateType(self):
        return self._CertificateType

    @CertificateType.setter
    def CertificateType(self, CertificateType):
        self._CertificateType = CertificateType

    @property
    def Alias(self):
        return self._Alias

    @Alias.setter
    def Alias(self, Alias):
        self._Alias = Alias

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CertificateUse(self):
        return self._CertificateUse

    @CertificateUse.setter
    def CertificateUse(self, CertificateUse):
        self._CertificateUse = CertificateUse

    @property
    def Repeatable(self):
        return self._Repeatable

    @Repeatable.setter
    def Repeatable(self, Repeatable):
        self._Repeatable = Repeatable


    def _deserialize(self, params):
        self._CertificatePublicKey = params.get("CertificatePublicKey")
        self._CertificatePrivateKey = params.get("CertificatePrivateKey")
        self._CertificateType = params.get("CertificateType")
        self._Alias = params.get("Alias")
        self._ProjectId = params.get("ProjectId")
        self._CertificateUse = params.get("CertificateUse")
        self._Repeatable = params.get("Repeatable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RepeatCertId: 重复证书的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RepeatCertId: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._RepeatCertId = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RepeatCertId(self):
        return self._RepeatCertId

    @RepeatCertId.setter
    def RepeatCertId(self, RepeatCertId):
        self._RepeatCertId = RepeatCertId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RepeatCertId = params.get("RepeatCertId")
        self._RequestId = params.get("RequestId")


class UploadConfirmLetterRequest(AbstractModel):
    """UploadConfirmLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _ConfirmLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :type ConfirmLetter: str
        """
        self._CertificateId = None
        self._ConfirmLetter = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def ConfirmLetter(self):
        return self._ConfirmLetter

    @ConfirmLetter.setter
    def ConfirmLetter(self, ConfirmLetter):
        self._ConfirmLetter = ConfirmLetter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._ConfirmLetter = params.get("ConfirmLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadConfirmLetterResponse(AbstractModel):
    """UploadConfirmLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书ID
        :type CertificateId: str
        :param _IsSuccess: 是否成功
        :type IsSuccess: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class UploadRevokeLetterRequest(AbstractModel):
    """UploadRevokeLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _RevokeLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :type RevokeLetter: str
        """
        self._CertificateId = None
        self._RevokeLetter = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def RevokeLetter(self):
        return self._RevokeLetter

    @RevokeLetter.setter
    def RevokeLetter(self, RevokeLetter):
        self._RevokeLetter = RevokeLetter


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._RevokeLetter = params.get("RevokeLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadRevokeLetterResponse(AbstractModel):
    """UploadRevokeLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CertificateId: 证书 ID。
        :type CertificateId: str
        :param _IsSuccess: 是否成功。
        :type IsSuccess: bool
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CertificateId = None
        self._IsSuccess = None
        self._RequestId = None

    @property
    def CertificateId(self):
        return self._CertificateId

    @CertificateId.setter
    def CertificateId(self, CertificateId):
        self._CertificateId = CertificateId

    @property
    def IsSuccess(self):
        return self._IsSuccess

    @IsSuccess.setter
    def IsSuccess(self, IsSuccess):
        self._IsSuccess = IsSuccess

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._CertificateId = params.get("CertificateId")
        self._IsSuccess = params.get("IsSuccess")
        self._RequestId = params.get("RequestId")


class VerifyManagerRequest(AbstractModel):
    """VerifyManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        """
        self._ManagerId = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyManagerResponse(AbstractModel):
    """VerifyManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ManagerId: 管理人ID
        :type ManagerId: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ManagerId = None
        self._RequestId = None

    @property
    def ManagerId(self):
        return self._ManagerId

    @ManagerId.setter
    def ManagerId(self, ManagerId):
        self._ManagerId = ManagerId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ManagerId = params.get("ManagerId")
        self._RequestId = params.get("RequestId")


class VodInstanceDetail(AbstractModel):
    """Vod实例

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _CertId: 证书ID
        :type CertId: str
        """
        self._Domain = None
        self._CertId = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        