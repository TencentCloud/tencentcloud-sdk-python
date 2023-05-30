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
        :param ServiceId: 实例ID
        :type ServiceId: str
        :param ServiceName: 实例名称
        :type ServiceName: str
        :param Domain: 域名
        :type Domain: str
        :param CertId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Protocol: 使用协议
        :type Protocol: str
        """
        self.ServiceId = None
        self.ServiceName = None
        self.Domain = None
        self.CertId = None
        self.Protocol = None


    def _deserialize(self, params):
        self.ServiceId = params.get("ServiceId")
        self.ServiceName = params.get("ServiceName")
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param DvAuthMethod: 验证方式：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。
        :type DvAuthMethod: str
        :param DomainName: 域名。
        :type DomainName: str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        :param PackageType: 证书类型，目前仅支持类型2。2 = TrustAsia TLS RSA CA。
        :type PackageType: str
        :param ContactEmail: 邮箱。
        :type ContactEmail: str
        :param ContactPhone: 手机。
        :type ContactPhone: str
        :param ValidityPeriod: 有效期，默认12个月，目前仅支持12个月。
        :type ValidityPeriod: str
        :param CsrEncryptAlgo: 加密算法，仅支持 RSA。
        :type CsrEncryptAlgo: str
        :param CsrKeyParameter: 密钥对参数，仅支持2048。
        :type CsrKeyParameter: str
        :param CsrKeyPassword: CSR 的加密密码。
        :type CsrKeyPassword: str
        :param Alias: 备注名称。
        :type Alias: str
        :param OldCertificateId: 原证书 ID，用于重新申请。
        :type OldCertificateId: str
        :param PackageId: 权益包ID，用于免费证书扩容包使用
        :type PackageId: str
        :param DeleteDnsAutoRecord: 签发后是否删除自动域名验证记录， 默认为否；仅域名为DNS_AUTO验证类型支持传参
        :type DeleteDnsAutoRecord: bool
        """
        self.DvAuthMethod = None
        self.DomainName = None
        self.ProjectId = None
        self.PackageType = None
        self.ContactEmail = None
        self.ContactPhone = None
        self.ValidityPeriod = None
        self.CsrEncryptAlgo = None
        self.CsrKeyParameter = None
        self.CsrKeyPassword = None
        self.Alias = None
        self.OldCertificateId = None
        self.PackageId = None
        self.DeleteDnsAutoRecord = None


    def _deserialize(self, params):
        self.DvAuthMethod = params.get("DvAuthMethod")
        self.DomainName = params.get("DomainName")
        self.ProjectId = params.get("ProjectId")
        self.PackageType = params.get("PackageType")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPhone = params.get("ContactPhone")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.CsrEncryptAlgo = params.get("CsrEncryptAlgo")
        self.CsrKeyParameter = params.get("CsrKeyParameter")
        self.CsrKeyPassword = params.get("CsrKeyPassword")
        self.Alias = params.get("Alias")
        self.OldCertificateId = params.get("OldCertificateId")
        self.PackageId = params.get("PackageId")
        self.DeleteDnsAutoRecord = params.get("DeleteDnsAutoRecord")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ApplyCertificateResponse(AbstractModel):
    """ApplyCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CancelCertificateOrderResponse(AbstractModel):
    """CancelCertificateOrder返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 取消订单成功的证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CdnInstanceDetail(AbstractModel):
    """CDN实例详情

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param CertId: 已部署证书ID
        :type CertId: str
        :param Status: 域名状态
        :type Status: str
        """
        self.Domain = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertHostingInfo(AbstractModel):
    """云资源配置详情

    """

    def __init__(self):
        r"""
        :param CertId: 证书ID
        :type CertId: str
        :param RenewCertId: 已替换的新证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewCertId: str
        :param ResourceType: 云资源托管 ，CDN或CLB：部分开启，CDN,CLB：已开启，null：未开启托管
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceType: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.CertId = None
        self.RenewCertId = None
        self.ResourceType = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.RenewCertId = params.get("RenewCertId")
        self.ResourceType = params.get("ResourceType")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificate(AbstractModel):
    """CLB证书详情

    """

    def __init__(self):
        r"""
        :param CertId: 证书ID
        :type CertId: str
        :param DnsNames: 证书绑定的域名
        :type DnsNames: list of str
        """
        self.CertId = None
        self.DnsNames = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.DnsNames = params.get("DnsNames")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateExtra(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 数组下，key为CertificateExtra 的内容。

    """

    def __init__(self):
        r"""
        :param DomainNumber: 证书可配置域名数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNumber: str
        :param OriginCertificateId: 原始证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCertificateId: str
        :param ReplacedBy: 重颁发证书原始 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedBy: str
        :param ReplacedFor: 重颁发证书新 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReplacedFor: str
        :param RenewOrder: 新订单证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewOrder: str
        :param SMCert: 是否是国密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type SMCert: int
        """
        self.DomainNumber = None
        self.OriginCertificateId = None
        self.ReplacedBy = None
        self.ReplacedFor = None
        self.RenewOrder = None
        self.SMCert = None


    def _deserialize(self, params):
        self.DomainNumber = params.get("DomainNumber")
        self.OriginCertificateId = params.get("OriginCertificateId")
        self.ReplacedBy = params.get("ReplacedBy")
        self.ReplacedFor = params.get("ReplacedFor")
        self.RenewOrder = params.get("RenewOrder")
        self.SMCert = params.get("SMCert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificates(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 的内容。

    """

    def __init__(self):
        r"""
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 证书来源。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param PackageType: 证书套餐类型：
null = 用户上传证书（没有套餐类型），
1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 主域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 状态。0：审核中，1：已通过，2：审核失败，3：已过期，4：验证方式为 DNS_AUTO 类型的证书， 已添加DNS记录，5：企业证书，待提交，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函，9：证书吊销中，10：已吊销，11：重颁发中，12：待上传吊销确认函，13：免费证书待提交资料状态，14：已退款，
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 证书有效期，单位（月）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param StatusName: 状态名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param ProjectInfo: 项目信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`
        :param BoundResource: 关联的云资源，暂不可用
注意：此字段可能返回 null，表示取不到有效值。
        :type BoundResource: list of str
        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param IsIgnore: 是否已忽略到期通知
注意：此字段可能返回 null，表示取不到有效值。
        :type IsIgnore: bool
        :param IsSM: 是否国密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type IsSM: bool
        :param EncryptAlgorithm: 证书算法
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptAlgorithm: str
        :param CAEncryptAlgorithms: 上传CA证书的加密算法
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEncryptAlgorithms: list of str
        :param CAEndTimes: 上传CA证书的过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEndTimes: list of str
        :param CACommonNames: 上传CA证书的通用名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CACommonNames: list of str
        :param PreAuditInfo: 证书预审核信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PreAuditInfo: :class:`tencentcloud.ssl.v20191205.models.PreAuditInfo`
        :param AutoRenewFlag: 是否自动续费
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoRenewFlag: int
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.PackageType = None
        self.CertificateType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.CertificateExtra = None
        self.VulnerabilityStatus = None
        self.StatusMsg = None
        self.VerifyType = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.CertificateId = None
        self.SubjectAltName = None
        self.PackageTypeName = None
        self.StatusName = None
        self.IsVip = None
        self.IsDv = None
        self.IsWildcard = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.ProjectInfo = None
        self.BoundResource = None
        self.Deployable = None
        self.Tags = None
        self.IsIgnore = None
        self.IsSM = None
        self.EncryptAlgorithm = None
        self.CAEncryptAlgorithms = None
        self.CAEndTimes = None
        self.CACommonNames = None
        self.PreAuditInfo = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.PackageType = params.get("PackageType")
        self.CertificateType = params.get("CertificateType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.CertificateId = params.get("CertificateId")
        self.SubjectAltName = params.get("SubjectAltName")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.IsVip = params.get("IsVip")
        self.IsDv = params.get("IsDv")
        self.IsWildcard = params.get("IsWildcard")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("ProjectInfo") is not None:
            self.ProjectInfo = ProjectInfo()
            self.ProjectInfo._deserialize(params.get("ProjectInfo"))
        self.BoundResource = params.get("BoundResource")
        self.Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.IsIgnore = params.get("IsIgnore")
        self.IsSM = params.get("IsSM")
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self.CAEndTimes = params.get("CAEndTimes")
        self.CACommonNames = params.get("CACommonNames")
        if params.get("PreAuditInfo") is not None:
            self.PreAuditInfo = PreAuditInfo()
            self.PreAuditInfo._deserialize(params.get("PreAuditInfo"))
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateChainRequest(AbstractModel):
    """CheckCertificateChain请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateChain: 待检查的证书链
        :type CertificateChain: str
        """
        self.CertificateChain = None


    def _deserialize(self, params):
        self.CertificateChain = params.get("CertificateChain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckCertificateChainResponse(AbstractModel):
    """CheckCertificateChain返回参数结构体

    """

    def __init__(self):
        r"""
        :param IsValid: true为通过检查，false为未通过检查。
        :type IsValid: bool
        :param IsTrustedCA: true为可信CA，false为不可信CA。
        :type IsTrustedCA: bool
        :param Chains: 包含证书链中每一段证书的通用名称。
        :type Chains: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.IsValid = None
        self.IsTrustedCA = None
        self.Chains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValid = params.get("IsValid")
        self.IsTrustedCA = params.get("IsTrustedCA")
        self.Chains = params.get("Chains")
        self.RequestId = params.get("RequestId")


class ClbInstanceDetail(AbstractModel):
    """clb实例详情

    """

    def __init__(self):
        r"""
        :param LoadBalancerId: CLB实例ID
        :type LoadBalancerId: str
        :param LoadBalancerName: CLB实例名称
        :type LoadBalancerName: str
        :param Listeners: CLB监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Listeners: list of ClbListener
        """
        self.LoadBalancerId = None
        self.LoadBalancerName = None
        self.Listeners = None


    def _deserialize(self, params):
        self.LoadBalancerId = params.get("LoadBalancerId")
        self.LoadBalancerName = params.get("LoadBalancerName")
        if params.get("Listeners") is not None:
            self.Listeners = []
            for item in params.get("Listeners"):
                obj = ClbListener()
                obj._deserialize(item)
                self.Listeners.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListener(AbstractModel):
    """CLB实例监听器

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param SniSwitch: 是否开启SNI，1为开启，0为关闭
        :type SniSwitch: int
        :param Protocol: 监听器协议类型， HTTPS|TCP_SSL
        :type Protocol: str
        :param Certificate: 监听器绑定的证书数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param Rules: 监听器规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ClbListenerRule
        :param NoMatchDomains: 不匹配域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.SniSwitch = None
        self.Protocol = None
        self.Certificate = None
        self.Rules = None
        self.NoMatchDomains = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.SniSwitch = params.get("SniSwitch")
        self.Protocol = params.get("Protocol")
        if params.get("Certificate") is not None:
            self.Certificate = Certificate()
            self.Certificate._deserialize(params.get("Certificate"))
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ClbListenerRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClbListenerRule(AbstractModel):
    """CLB监听器规则

    """

    def __init__(self):
        r"""
        :param LocationId: 规则ID
        :type LocationId: str
        :param Domain: 规则绑定的域名
        :type Domain: str
        :param IsMatch: 规则是否匹配待绑定证书的域名
        :type IsMatch: bool
        :param Certificate: 规则已绑定的证书数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: :class:`tencentcloud.ssl.v20191205.models.Certificate`
        :param NoMatchDomains: 不匹配域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self.LocationId = None
        self.Domain = None
        self.IsMatch = None
        self.Certificate = None
        self.NoMatchDomains = None


    def _deserialize(self, params):
        self.LocationId = params.get("LocationId")
        self.Domain = params.get("Domain")
        self.IsMatch = params.get("IsMatch")
        if params.get("Certificate") is not None:
            self.Certificate = Certificate()
            self.Certificate._deserialize(params.get("Certificate"))
        self.NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param VerifyType: 域名验证方式
        :type VerifyType: str
        """
        self.CertificateId = None
        self.VerifyType = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CommitCertificateInformationResponse(AbstractModel):
    """CommitCertificateInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param OrderId: CA机构侧订单号。
        :type OrderId: str
        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :type Status: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OrderId = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OrderId = params.get("OrderId")
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")


class CompanyInfo(AbstractModel):
    """公司信息

    """

    def __init__(self):
        r"""
        :param CompanyName: 公司名称
        :type CompanyName: str
        :param CompanyId: 公司ID
        :type CompanyId: int
        :param CompanyCountry: 公司所在国家
        :type CompanyCountry: str
        :param CompanyProvince: 公司所在省份
        :type CompanyProvince: str
        :param CompanyCity: 公司所在城市
        :type CompanyCity: str
        :param CompanyAddress: 公司所在详细地址
        :type CompanyAddress: str
        :param CompanyPhone: 公司电话
        :type CompanyPhone: str
        :param IdType: 类型
注意：此字段可能返回 null，表示取不到有效值。
        :type IdType: str
        :param IdNumber: ID号
注意：此字段可能返回 null，表示取不到有效值。
        :type IdNumber: str
        """
        self.CompanyName = None
        self.CompanyId = None
        self.CompanyCountry = None
        self.CompanyProvince = None
        self.CompanyCity = None
        self.CompanyAddress = None
        self.CompanyPhone = None
        self.IdType = None
        self.IdNumber = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.CompanyId = params.get("CompanyId")
        self.CompanyCountry = params.get("CompanyCountry")
        self.CompanyProvince = params.get("CompanyProvince")
        self.CompanyCity = params.get("CompanyCity")
        self.CompanyAddress = params.get("CompanyAddress")
        self.CompanyPhone = params.get("CompanyPhone")
        self.IdType = params.get("IdType")
        self.IdNumber = params.get("IdNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteCertificateRequest(AbstractModel):
    """CompleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompleteCertificateResponse(AbstractModel):
    """CompleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CosInstanceDetail(AbstractModel):
    """COS实例详情

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param CertId: 已绑定的证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Status: ENABLED: 域名上线状态
DISABLED:域名下线状态
        :type Status: str
        :param Bucket: 存储桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Region: 存储桶地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        """
        self.Domain = None
        self.CertId = None
        self.Status = None
        self.Bucket = None
        self.Region = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        self.Bucket = params.get("Bucket")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProductId: 证书商品ID，3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书，25 = Wotrus 域名型证书，26 = Wotrus 域名型多域名证书，27 = Wotrus 域名型通配符证书，28 = Wotrus 企业型证书，29 = Wotrus 企业型多域名证书，30 = Wotrus 企业型通配符证书，31 = Wotrus 增强型证书，32 = Wotrus 增强型多域名证书，33 = DNSPod 国密域名型证书，34 = DNSPod 国密域名型多域名证书，35 = DNSPod 国密域名型通配符证书，37 = DNSPod 国密企业型证书，38 = DNSPod 国密企业型多域名证书，39 = DNSPod 国密企业型通配符证书，40 = DNSPod 国密增强型证书，41 = DNSPod 国密增强型多域名证书，42 = TrustAsia 域名型通配符多域名证书。
        :type ProductId: int
        :param DomainNum: 证书包含的域名数量
        :type DomainNum: int
        :param TimeSpan: 证书年限，当前只支持 1 年证书的购买
        :type TimeSpan: int
        """
        self.ProductId = None
        self.DomainNum = None
        self.TimeSpan = None


    def _deserialize(self, params):
        self.ProductId = params.get("ProductId")
        self.DomainNum = params.get("DomainNum")
        self.TimeSpan = params.get("TimeSpan")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateIds: 证书ID列表
        :type CertificateIds: list of str
        :param DealIds: 订单号列表
        :type DealIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateIds = None
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateIds = params.get("CertificateIds")
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")


class DdosInstanceDetail(AbstractModel):
    """ddos复杂类型

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param Protocol: 协议类型
        :type Protocol: str
        :param CertId: 证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param VirtualPort: 转发端口
        :type VirtualPort: str
        """
        self.Domain = None
        self.InstanceId = None
        self.Protocol = None
        self.CertId = None
        self.VirtualPort = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.InstanceId = params.get("InstanceId")
        self.Protocol = params.get("Protocol")
        self.CertId = params.get("CertId")
        self.VirtualPort = params.get("VirtualPort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeleteResult: 删除结果（true：删除成功，false：删除失败）
        :type DeleteResult: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeleteResult = params.get("DeleteResult")
        self.RequestId = params.get("RequestId")


class DeleteManagerRequest(AbstractModel):
    """DeleteManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        """
        self.ManagerId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteManagerResponse(AbstractModel):
    """DeleteManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ManagerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.RequestId = params.get("RequestId")


class DeployCertificateInstanceRequest(AbstractModel):
    """DeployCertificateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param InstanceIdList: 需要部署实例列表
        :type InstanceIdList: list of str
        :param ResourceType: 部署的云资源类型
        :type ResourceType: str
        :param Status: 部署云资源状态：
云直播：
-1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :type Status: int
        """
        self.CertificateId = None
        self.InstanceIdList = None
        self.ResourceType = None
        self.Status = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.InstanceIdList = params.get("InstanceIdList")
        self.ResourceType = params.get("ResourceType")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateInstanceResponse(AbstractModel):
    """DeployCertificateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 云资源部署任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordId: int
        :param DeployStatus: 部署状态，1表示部署成功，0表示部署失败
        :type DeployStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeployRecordId = None
        self.DeployStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.DeployStatus = params.get("DeployStatus")
        self.RequestId = params.get("RequestId")


class DeployCertificateRecordRetryRequest(AbstractModel):
    """DeployCertificateRecordRetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        :param DeployRecordDetailId: 待重试部署记录详情ID
        :type DeployRecordDetailId: int
        """
        self.DeployRecordId = None
        self.DeployRecordDetailId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateRecordRetryResponse(AbstractModel):
    """DeployCertificateRecordRetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeployCertificateRecordRollbackRequest(AbstractModel):
    """DeployCertificateRecordRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        """
        self.DeployRecordId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployCertificateRecordRollbackResponse(AbstractModel):
    """DeployCertificateRecordRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 回滚部署记录ID
        :type DeployRecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeployRecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.RequestId = params.get("RequestId")


class DeployRecordDetail(AbstractModel):
    """部署记录详情

    """

    def __init__(self):
        r"""
        :param Id: 部署记录详情ID
        :type Id: int
        :param CertId: 部署证书ID
        :type CertId: str
        :param OldCertId: 原绑定证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type OldCertId: str
        :param InstanceId: 部署实例ID
        :type InstanceId: str
        :param InstanceName: 部署实例名称
        :type InstanceName: str
        :param ListenerId: 部署监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param Domains: 部署域名列表
        :type Domains: list of str
        :param Protocol: 部署监听器协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param Status: 部署状态
        :type Status: int
        :param ErrorMsg: 部署错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param CreateTime: 部署记录详情创建时间
        :type CreateTime: str
        :param UpdateTime: 部署记录详情最后一次更新时间
        :type UpdateTime: str
        :param ListenerName: 部署监听器名称
        :type ListenerName: str
        :param SniSwitch: 是否开启SNI
        :type SniSwitch: int
        :param Bucket: COS存储桶名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        :param Namespace: 命名空间名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Namespace: str
        :param SecretName: secret名称
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretName: str
        :param Port: 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type Port: int
        """
        self.Id = None
        self.CertId = None
        self.OldCertId = None
        self.InstanceId = None
        self.InstanceName = None
        self.ListenerId = None
        self.Domains = None
        self.Protocol = None
        self.Status = None
        self.ErrorMsg = None
        self.CreateTime = None
        self.UpdateTime = None
        self.ListenerName = None
        self.SniSwitch = None
        self.Bucket = None
        self.Namespace = None
        self.SecretName = None
        self.Port = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CertId = params.get("CertId")
        self.OldCertId = params.get("OldCertId")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ListenerId = params.get("ListenerId")
        self.Domains = params.get("Domains")
        self.Protocol = params.get("Protocol")
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.ListenerName = params.get("ListenerName")
        self.SniSwitch = params.get("SniSwitch")
        self.Bucket = params.get("Bucket")
        self.Namespace = params.get("Namespace")
        self.SecretName = params.get("SecretName")
        self.Port = params.get("Port")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployRecordInfo(AbstractModel):
    """部署记录信息

    """

    def __init__(self):
        r"""
        :param Id: 部署记录ID
        :type Id: int
        :param CertId: 部署证书ID
        :type CertId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param Region: 部署地域
        :type Region: str
        :param Status: 部署状态
        :type Status: int
        :param CreateTime: 部署时间
        :type CreateTime: str
        :param UpdateTime: 最近一次更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.CertId = None
        self.ResourceType = None
        self.Region = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CertId = params.get("CertId")
        self.ResourceType = params.get("ResourceType")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeployedResources(AbstractModel):
    """资源详情

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param Count: 数量
        :type Count: int
        :param Type: 资源标识:clb,cdn,live,waf,antiddos
        :type Type: str
        :param ResourceIds: 不建议使用。字段返回和Resources相同。本字段后续只返回null
注意：此字段可能返回 null，表示取不到有效值。
        :type ResourceIds: list of str
        :param Resources: 关联资源ID或关联域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Resources: list of str
        """
        self.CertificateId = None
        self.Count = None
        self.Type = None
        self.ResourceIds = None
        self.Resources = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Count = params.get("Count")
        self.Type = params.get("Type")
        self.ResourceIds = params.get("ResourceIds")
        self.Resources = params.get("Resources")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param PackageType: 证书套餐类型：null = 用户上传证书（没有套餐类型），1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书，25 = Wotrus 域名型证书，26 = Wotrus 域名型多域名证书，27 = Wotrus 域名型通配符证书，28 = Wotrus 企业型证书，29 = Wotrus 企业型多域名证书，30 = Wotrus 企业型通配符证书，31 = Wotrus 增强型证书，32 = Wotrus 增强型多域名证书，33 = DNSPod 国密域名型证书，34 = DNSPod 国密域名型多域名证书，35 = DNSPod 国密域名型通配符证书，37 = DNSPod 国密企业型证书，38 = DNSPod 国密企业型多域名证书，39 = DNSPod 国密企业型通配符证书，40 = DNSPod 国密增强型证书，41 = DNSPod 国密增强型多域名证书，42 = TrustAsia 域名型通配符多域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 证书有效期：单位（月）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param CertificatePrivateKey: 证书私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePrivateKey: str
        :param CertificatePublicKey: 证书公钥（即证书内容）
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificatePublicKey: str
        :param DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param TypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeName: str
        :param StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param SubjectAltName: 证书包含的多个域名（不包含主域名，主域名使用Domain字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param IsVip: 是否为付费证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param RenewAble: 是否可续费。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param Tags: 关联标签列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param RootCert: 根证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RootCert: :class:`tencentcloud.ssl.v20191205.models.RootCertificates`
        :param EncryptCert: 国密加密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptCert: str
        :param EncryptPrivateKey: 国密加密私钥
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptPrivateKey: str
        :param CertFingerprint: 签名证书 SHA1指纹
注意：此字段可能返回 null，表示取不到有效值。
        :type CertFingerprint: str
        :param EncryptCertFingerprint: 加密证书 SHA1指纹 （国密证书特有）
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptCertFingerprint: str
        :param EncryptAlgorithm: 证书算法
注意：此字段可能返回 null，表示取不到有效值。
        :type EncryptAlgorithm: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.CertificatePrivateKey = None
        self.CertificatePublicKey = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.TypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.SubmittedData = None
        self.RenewAble = None
        self.Deployable = None
        self.Tags = None
        self.RootCert = None
        self.EncryptCert = None
        self.EncryptPrivateKey = None
        self.CertFingerprint = None
        self.EncryptCertFingerprint = None
        self.EncryptAlgorithm = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.TypeName = params.get("TypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.RenewAble = params.get("RenewAble")
        self.Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        if params.get("RootCert") is not None:
            self.RootCert = RootCertificates()
            self.RootCert._deserialize(params.get("RootCert"))
        self.EncryptCert = params.get("EncryptCert")
        self.EncryptPrivateKey = params.get("EncryptPrivateKey")
        self.CertFingerprint = params.get("CertFingerprint")
        self.EncryptCertFingerprint = params.get("EncryptCertFingerprint")
        self.EncryptAlgorithm = params.get("EncryptAlgorithm")
        self.RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 请求日志数量，默认为20。
        :type Limit: int
        :param StartTime: 开始时间，默认15天前。
        :type StartTime: str
        :param EndTime: 结束时间，默认现在时间。
        :type EndTime: str
        """
        self.Offset = None
        self.Limit = None
        self.StartTime = None
        self.EndTime = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateOperateLogsResponse(AbstractModel):
    """DescribeCertificateOperateLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param AllTotal: 当前查询条件日志总数。
        :type AllTotal: int
        :param TotalCount: 本次请求返回的日志数量。
        :type TotalCount: int
        :param OperateLogs: 证书操作日志列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type OperateLogs: list of OperationLog
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AllTotal = None
        self.TotalCount = None
        self.OperateLogs = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AllTotal = params.get("AllTotal")
        self.TotalCount = params.get("TotalCount")
        if params.get("OperateLogs") is not None:
            self.OperateLogs = []
            for item in params.get("OperateLogs"):
                obj = OperationLog()
                obj._deserialize(item)
                self.OperateLogs.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCertificateRequest(AbstractModel):
    """DescribeCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateResponse(AbstractModel):
    """DescribeCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: str
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        :param From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateType: str
        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param ProductZhName: 证书颁发者名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProductZhName: str
        :param Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Alias: str
        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusMsg: str
        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        :param VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityStatus: str
        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertBeginTime: str
        :param CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertEndTime: str
        :param ValidityPeriod: 证书有效期：单位(月)。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValidityPeriod: str
        :param InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type InsertTime: str
        :param OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrderId: str
        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`
        :param DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`
        :param VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type VulnerabilityReport: str
        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageTypeName: str
        :param StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusName: str
        :param SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectAltName: list of str
        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVip: bool
        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsWildcard: bool
        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsDv: bool
        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。
        :type IsVulnerability: bool
        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。
        :type RenewAble: bool
        :param SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`
        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。
        :type Deployable: bool
        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of Tags
        :param CAEncryptAlgorithms: CA证书的所有加密方式	
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEncryptAlgorithms: list of str
        :param CACommonNames: CA证书的所有通用名称	
注意：此字段可能返回 null，表示取不到有效值。
        :type CACommonNames: list of str
        :param CAEndTimes: CA证书所有的到期时间	
注意：此字段可能返回 null，表示取不到有效值。
        :type CAEndTimes: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OwnerUin = None
        self.ProjectId = None
        self.From = None
        self.CertificateType = None
        self.PackageType = None
        self.ProductZhName = None
        self.Domain = None
        self.Alias = None
        self.Status = None
        self.StatusMsg = None
        self.VerifyType = None
        self.VulnerabilityStatus = None
        self.CertBeginTime = None
        self.CertEndTime = None
        self.ValidityPeriod = None
        self.InsertTime = None
        self.OrderId = None
        self.CertificateExtra = None
        self.DvAuthDetail = None
        self.VulnerabilityReport = None
        self.CertificateId = None
        self.PackageTypeName = None
        self.StatusName = None
        self.SubjectAltName = None
        self.IsVip = None
        self.IsWildcard = None
        self.IsDv = None
        self.IsVulnerability = None
        self.RenewAble = None
        self.SubmittedData = None
        self.Deployable = None
        self.Tags = None
        self.CAEncryptAlgorithms = None
        self.CACommonNames = None
        self.CAEndTimes = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        self.From = params.get("From")
        self.CertificateType = params.get("CertificateType")
        self.PackageType = params.get("PackageType")
        self.ProductZhName = params.get("ProductZhName")
        self.Domain = params.get("Domain")
        self.Alias = params.get("Alias")
        self.Status = params.get("Status")
        self.StatusMsg = params.get("StatusMsg")
        self.VerifyType = params.get("VerifyType")
        self.VulnerabilityStatus = params.get("VulnerabilityStatus")
        self.CertBeginTime = params.get("CertBeginTime")
        self.CertEndTime = params.get("CertEndTime")
        self.ValidityPeriod = params.get("ValidityPeriod")
        self.InsertTime = params.get("InsertTime")
        self.OrderId = params.get("OrderId")
        if params.get("CertificateExtra") is not None:
            self.CertificateExtra = CertificateExtra()
            self.CertificateExtra._deserialize(params.get("CertificateExtra"))
        if params.get("DvAuthDetail") is not None:
            self.DvAuthDetail = DvAuthDetail()
            self.DvAuthDetail._deserialize(params.get("DvAuthDetail"))
        self.VulnerabilityReport = params.get("VulnerabilityReport")
        self.CertificateId = params.get("CertificateId")
        self.PackageTypeName = params.get("PackageTypeName")
        self.StatusName = params.get("StatusName")
        self.SubjectAltName = params.get("SubjectAltName")
        self.IsVip = params.get("IsVip")
        self.IsWildcard = params.get("IsWildcard")
        self.IsDv = params.get("IsDv")
        self.IsVulnerability = params.get("IsVulnerability")
        self.RenewAble = params.get("RenewAble")
        if params.get("SubmittedData") is not None:
            self.SubmittedData = SubmittedData()
            self.SubmittedData._deserialize(params.get("SubmittedData"))
        self.Deployable = params.get("Deployable")
        if params.get("Tags") is not None:
            self.Tags = []
            for item in params.get("Tags"):
                obj = Tags()
                obj._deserialize(item)
                self.Tags.append(obj)
        self.CAEncryptAlgorithms = params.get("CAEncryptAlgorithms")
        self.CACommonNames = params.get("CACommonNames")
        self.CAEndTimes = params.get("CAEndTimes")
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认20。最大1000
        :type Limit: int
        :param SearchKey: 搜索关键词，可搜索证书 ID、备注名称、域名。例如： a8xHcaIs。
        :type SearchKey: str
        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
        :type CertificateType: str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        :param ExpirationSort: 按到期时间排序：DESC = 降序， ASC = 升序。
        :type ExpirationSort: str
        :param CertificateStatus: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
        :type CertificateStatus: list of int non-negative
        :param Deployable: 是否可部署，可选值：1 = 可部署，0 =  不可部署。
        :type Deployable: int
        :param Upload: 是否筛选上传托管的 1筛选，0不筛选
        :type Upload: int
        :param Renew: 是否筛选可续期证书 1筛选 0不筛选
        :type Renew: int
        :param FilterSource: 筛选来源， upload：上传证书， buy：腾讯云证书， 不传默认全部
        :type FilterSource: str
        :param IsSM: 是否筛选国密证书。1:筛选  0:不筛选
        :type IsSM: int
        :param FilterExpiring: 筛选证书是否即将过期，传1是筛选，0不筛选
        :type FilterExpiring: int
        """
        self.Offset = None
        self.Limit = None
        self.SearchKey = None
        self.CertificateType = None
        self.ProjectId = None
        self.ExpirationSort = None
        self.CertificateStatus = None
        self.Deployable = None
        self.Upload = None
        self.Renew = None
        self.FilterSource = None
        self.IsSM = None
        self.FilterExpiring = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchKey = params.get("SearchKey")
        self.CertificateType = params.get("CertificateType")
        self.ProjectId = params.get("ProjectId")
        self.ExpirationSort = params.get("ExpirationSort")
        self.CertificateStatus = params.get("CertificateStatus")
        self.Deployable = params.get("Deployable")
        self.Upload = params.get("Upload")
        self.Renew = params.get("Renew")
        self.FilterSource = params.get("FilterSource")
        self.IsSM = params.get("IsSM")
        self.FilterExpiring = params.get("FilterExpiring")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param Certificates: 列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificates: list of Certificates
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Certificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Certificates") is not None:
            self.Certificates = []
            for item in params.get("Certificates"):
                obj = Certificates()
                obj._deserialize(item)
                self.Certificates.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCompaniesRequest(AbstractModel):
    """DescribeCompanies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页偏移量
        :type Offset: int
        :param Limit: 分页每页限制数
        :type Limit: int
        :param CompanyId: 公司ID
        :type CompanyId: int
        """
        self.Offset = None
        self.Limit = None
        self.CompanyId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CompanyId = params.get("CompanyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCompaniesResponse(AbstractModel):
    """DescribeCompanies返回参数结构体

    """

    def __init__(self):
        r"""
        :param Companies: 公司列表
        :type Companies: list of CompanyInfo
        :param TotalCount: 公司总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Companies = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Companies") is not None:
            self.Companies = []
            for item in params.get("Companies"):
                obj = CompanyInfo()
                obj._deserialize(item)
                self.Companies.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDeployedResourcesRequest(AbstractModel):
    """DescribeDeployedResources请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateIds: 证书ID
        :type CertificateIds: list of str
        :param ResourceType: 资源类型:clb,cdn,live,waf,antiddos
        :type ResourceType: str
        """
        self.CertificateIds = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.CertificateIds = params.get("CertificateIds")
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDeployedResourcesResponse(AbstractModel):
    """DescribeDeployedResources返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeployedResources: 资源详情
        :type DeployedResources: list of DeployedResources
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeployedResources = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DeployedResources") is not None:
            self.DeployedResources = []
            for item in params.get("DeployedResources"):
                obj = DeployedResources()
                obj._deserialize(item)
                self.DeployedResources.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostApiGatewayInstanceListRequest(AbstractModel):
    """DescribeHostApiGatewayInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostApiGatewayInstanceListResponse(AbstractModel):
    """DescribeHostApiGatewayInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: apiGateway实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of ApiGatewayInstanceDetail
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = ApiGatewayInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostCdnInstanceListRequest(AbstractModel):
    """DescribeHostCdnInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param OldCertificateId: 原证书ID
        :type OldCertificateId: str
        :param Offset: 分页偏移量，从0开始。	
        :type Offset: int
        :param Limit: 每页数量，默认10。	
        :type Limit: int
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostCdnInstanceListResponse(AbstractModel):
    """DescribeHostCdnInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: CDN实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of CdnInstanceDetail
        :param TotalCount: CDN域名总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = CdnInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostClbInstanceListRequest(AbstractModel):
    """DescribeHostClbInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认10。
        :type Limit: int
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param AsyncCache: 是否异步缓存
        :type AsyncCache: int
        :param OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.Offset = None
        self.Limit = None
        self.IsCache = None
        self.Filters = None
        self.AsyncCache = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AsyncCache = params.get("AsyncCache")
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostClbInstanceListResponse(AbstractModel):
    """DescribeHostClbInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param InstanceList: CLB实例监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of ClbInstanceDetail
        :param AsyncTotalNum: 异步刷新总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param AsyncOffset: 异步刷新当前执行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.AsyncTotalNum = None
        self.AsyncOffset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = ClbInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.AsyncTotalNum = params.get("AsyncTotalNum")
        self.AsyncOffset = params.get("AsyncOffset")
        self.RequestId = params.get("RequestId")


class DescribeHostCosInstanceListRequest(AbstractModel):
    """DescribeHostCosInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型 cos
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表
        :type Filters: list of Filter
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
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
        


class DescribeHostCosInstanceListResponse(AbstractModel):
    """DescribeHostCosInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: COS实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of CosInstanceDetail
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param AsyncTotalNum: 异步刷新总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param AsyncOffset: 异步刷新当前执行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalCount = None
        self.AsyncTotalNum = None
        self.AsyncOffset = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = CosInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.AsyncTotalNum = params.get("AsyncTotalNum")
        self.AsyncOffset = params.get("AsyncOffset")
        self.RequestId = params.get("RequestId")


class DescribeHostDdosInstanceListRequest(AbstractModel):
    """DescribeHostDdosInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDdosInstanceListResponse(AbstractModel):
    """DescribeHostDdosInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: DDOS实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of DdosInstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = DdosInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostDeployRecordDetailRequest(AbstractModel):
    """DescribeHostDeployRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 待部署的证书ID
        :type DeployRecordId: str
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认10。
        :type Limit: int
        """
        self.DeployRecordId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDeployRecordDetailResponse(AbstractModel):
    """DescribeHostDeployRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param DeployRecordDetailList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordDetailList: list of DeployRecordDetail
        :param SuccessTotalCount: 成功总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotalCount: int
        :param FailedTotalCount: 失败总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedTotalCount: int
        :param RunningTotalCount: 部署中总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningTotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeployRecordDetailList = None
        self.SuccessTotalCount = None
        self.FailedTotalCount = None
        self.RunningTotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeployRecordDetailList") is not None:
            self.DeployRecordDetailList = []
            for item in params.get("DeployRecordDetailList"):
                obj = DeployRecordDetail()
                obj._deserialize(item)
                self.DeployRecordDetailList.append(obj)
        self.SuccessTotalCount = params.get("SuccessTotalCount")
        self.FailedTotalCount = params.get("FailedTotalCount")
        self.RunningTotalCount = params.get("RunningTotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostDeployRecordRequest(AbstractModel):
    """DescribeHostDeployRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认10。
        :type Limit: int
        :param ResourceType: 资源类型
        :type ResourceType: str
        """
        self.CertificateId = None
        self.Offset = None
        self.Limit = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostDeployRecordResponse(AbstractModel):
    """DescribeHostDeployRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param DeployRecordList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordList: list of DeployRecordInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeployRecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self.DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = DeployRecordInfo()
                obj._deserialize(item)
                self.DeployRecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostLighthouseInstanceListRequest(AbstractModel):
    """DescribeHostLighthouseInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型 lighthouse
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表
        :type Filters: list of Filter
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
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
        


class DescribeHostLighthouseInstanceListResponse(AbstractModel):
    """DescribeHostLighthouseInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: Lighthouse实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LighthouseInstanceDetail
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = LighthouseInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostLiveInstanceListRequest(AbstractModel):
    """DescribeHostLiveInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostLiveInstanceListResponse(AbstractModel):
    """DescribeHostLiveInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: live实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LiveInstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostTeoInstanceListRequest(AbstractModel):
    """DescribeHostTeoInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTeoInstanceListResponse(AbstractModel):
    """DescribeHostTeoInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: teo实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TeoInstanceDetail
        :param TotalCount: 总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = TeoInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostTkeInstanceListRequest(AbstractModel):
    """DescribeHostTkeInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认10。
        :type Limit: int
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param AsyncCache: 是否异步缓存
        :type AsyncCache: int
        :param OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.Offset = None
        self.Limit = None
        self.IsCache = None
        self.Filters = None
        self.AsyncCache = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.AsyncCache = params.get("AsyncCache")
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostTkeInstanceListResponse(AbstractModel):
    """DescribeHostTkeInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param InstanceList: CLB实例监听器列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of TkeInstanceDetail
        :param AsyncTotalNum: 异步刷新总数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncTotalNum: int
        :param AsyncOffset: 异步刷新当前执行数
注意：此字段可能返回 null，表示取不到有效值。
        :type AsyncOffset: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceList = None
        self.AsyncTotalNum = None
        self.AsyncOffset = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = TkeInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.AsyncTotalNum = params.get("AsyncTotalNum")
        self.AsyncOffset = params.get("AsyncOffset")
        self.RequestId = params.get("RequestId")


class DescribeHostUpdateRecordDetailRequest(AbstractModel):
    """DescribeHostUpdateRecordDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 待部署的证书ID
        :type DeployRecordId: str
        """
        self.DeployRecordId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordDetailResponse(AbstractModel):
    """DescribeHostUpdateRecordDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RecordDetailList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RecordDetailList: list of UpdateRecordDetails
        :param SuccessTotalCount: 成功总数
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessTotalCount: int
        :param FailedTotalCount: 失败总数
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedTotalCount: int
        :param RunningTotalCount: 部署中总数
注意：此字段可能返回 null，表示取不到有效值。
        :type RunningTotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RecordDetailList = None
        self.SuccessTotalCount = None
        self.FailedTotalCount = None
        self.RunningTotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RecordDetailList") is not None:
            self.RecordDetailList = []
            for item in params.get("RecordDetailList"):
                obj = UpdateRecordDetails()
                obj._deserialize(item)
                self.RecordDetailList.append(obj)
        self.SuccessTotalCount = params.get("SuccessTotalCount")
        self.FailedTotalCount = params.get("FailedTotalCount")
        self.RunningTotalCount = params.get("RunningTotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostUpdateRecordRequest(AbstractModel):
    """DescribeHostUpdateRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 分页偏移量，从0开始。
        :type Offset: int
        :param Limit: 每页数量，默认10。
        :type Limit: int
        :param CertificateId: 新证书ID
        :type CertificateId: str
        :param OldCertificateId: 原证书ID
        :type OldCertificateId: str
        """
        self.Offset = None
        self.Limit = None
        self.CertificateId = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.CertificateId = params.get("CertificateId")
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostUpdateRecordResponse(AbstractModel):
    """DescribeHostUpdateRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param DeployRecordList: 证书部署记录列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordList: list of UpdateRecordInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DeployRecordList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DeployRecordList") is not None:
            self.DeployRecordList = []
            for item in params.get("DeployRecordList"):
                obj = UpdateRecordInfo()
                obj._deserialize(item)
                self.DeployRecordList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHostVodInstanceListRequest(AbstractModel):
    """DescribeHostVodInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型 vod
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表
        :type Filters: list of Filter
        :param OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostVodInstanceListResponse(AbstractModel):
    """DescribeHostVodInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: Vod实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of VodInstanceDetail
        :param TotalCount: 总数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = VodInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeHostWafInstanceListRequest(AbstractModel):
    """DescribeHostWafInstanceList请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 待部署的证书ID
        :type CertificateId: str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param IsCache: 是否查询缓存，1：是； 0：否， 默认为查询缓存，缓存半小时
        :type IsCache: int
        :param Filters: 过滤参数列表； FilterKey：domainMatch（查询域名是否匹配的实例列表） FilterValue：1，表示查询匹配； 0，表示查询不匹配； 默认查询匹配
        :type Filters: list of Filter
        :param OldCertificateId: 已部署的证书ID
        :type OldCertificateId: str
        """
        self.CertificateId = None
        self.ResourceType = None
        self.IsCache = None
        self.Filters = None
        self.OldCertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        self.IsCache = params.get("IsCache")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.OldCertificateId = params.get("OldCertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHostWafInstanceListResponse(AbstractModel):
    """DescribeHostWafInstanceList返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceList: WAF实例列表
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceList: list of LiveInstanceDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceList") is not None:
            self.InstanceList = []
            for item in params.get("InstanceList"):
                obj = LiveInstanceDetail()
                obj._deserialize(item)
                self.InstanceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeManagerDetailRequest(AbstractModel):
    """DescribeManagerDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        :param Limit: 分页每页数量
        :type Limit: int
        :param Offset: 分页偏移量
        :type Offset: int
        """
        self.ManagerId = None
        self.Limit = None
        self.Offset = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.Limit = params.get("Limit")
        self.Offset = params.get("Offset")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagerDetailResponse(AbstractModel):
    """DescribeManagerDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :type Status: str
        :param ManagerFirstName: 管理人姓名
        :type ManagerFirstName: str
        :param ManagerMail: 管理人邮箱
        :type ManagerMail: str
        :param ContactFirstName: 联系人姓名
        :type ContactFirstName: str
        :param ManagerLastName: 管理人姓名
        :type ManagerLastName: str
        :param ContactPosition: 联系人职位
        :type ContactPosition: str
        :param ManagerPosition: 管理人职位
        :type ManagerPosition: str
        :param VerifyTime: 核验通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTime: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param ExpireTime: 核验过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param ContactLastName: 联系人姓名
        :type ContactLastName: str
        :param ManagerPhone: 管理人电话
        :type ManagerPhone: str
        :param ContactPhone: 联系人电话
        :type ContactPhone: str
        :param ContactMail: 联系人邮箱
        :type ContactMail: str
        :param ManagerDepartment: 管理人所属部门
        :type ManagerDepartment: str
        :param CompanyInfo: 管理人所属公司信息
        :type CompanyInfo: :class:`tencentcloud.ssl.v20191205.models.CompanyInfo`
        :param CompanyId: 管理人公司ID
        :type CompanyId: int
        :param ManagerId: 管理人ID
        :type ManagerId: int
        :param StatusInfo: 审核状态详细信息
        :type StatusInfo: list of ManagerStatusInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.ManagerFirstName = None
        self.ManagerMail = None
        self.ContactFirstName = None
        self.ManagerLastName = None
        self.ContactPosition = None
        self.ManagerPosition = None
        self.VerifyTime = None
        self.CreateTime = None
        self.ExpireTime = None
        self.ContactLastName = None
        self.ManagerPhone = None
        self.ContactPhone = None
        self.ContactMail = None
        self.ManagerDepartment = None
        self.CompanyInfo = None
        self.CompanyId = None
        self.ManagerId = None
        self.StatusInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ManagerFirstName = params.get("ManagerFirstName")
        self.ManagerMail = params.get("ManagerMail")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ManagerLastName = params.get("ManagerLastName")
        self.ContactPosition = params.get("ContactPosition")
        self.ManagerPosition = params.get("ManagerPosition")
        self.VerifyTime = params.get("VerifyTime")
        self.CreateTime = params.get("CreateTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ContactLastName = params.get("ContactLastName")
        self.ManagerPhone = params.get("ManagerPhone")
        self.ContactPhone = params.get("ContactPhone")
        self.ContactMail = params.get("ContactMail")
        self.ManagerDepartment = params.get("ManagerDepartment")
        if params.get("CompanyInfo") is not None:
            self.CompanyInfo = CompanyInfo()
            self.CompanyInfo._deserialize(params.get("CompanyInfo"))
        self.CompanyId = params.get("CompanyId")
        self.ManagerId = params.get("ManagerId")
        if params.get("StatusInfo") is not None:
            self.StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = ManagerStatusInfo()
                obj._deserialize(item)
                self.StatusInfo.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeManagersRequest(AbstractModel):
    """DescribeManagers请求参数结构体

    """

    def __init__(self):
        r"""
        :param CompanyId: 公司ID
        :type CompanyId: int
        :param Offset: 分页偏移量
        :type Offset: int
        :param Limit: 分页每页数量
        :type Limit: int
        :param ManagerName: 管理人姓名（将废弃），请使用SearchKey
        :type ManagerName: str
        :param ManagerMail: 模糊查询管理人邮箱（将废弃），请使用SearchKey
        :type ManagerMail: str
        :param Status: 根据管理人状态进行筛选，取值有
'none' 未提交审核
'audit', 亚信审核中
'CAaudit' CA审核中
'ok' 已审核
'invalid'  审核失败
'expiring'  即将过期
'expired' 已过期
        :type Status: str
        :param SearchKey: 管理人姓/管理人名/邮箱/部门精准匹配
        :type SearchKey: str
        """
        self.CompanyId = None
        self.Offset = None
        self.Limit = None
        self.ManagerName = None
        self.ManagerMail = None
        self.Status = None
        self.SearchKey = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ManagerName = params.get("ManagerName")
        self.ManagerMail = params.get("ManagerMail")
        self.Status = params.get("Status")
        self.SearchKey = params.get("SearchKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeManagersResponse(AbstractModel):
    """DescribeManagers返回参数结构体

    """

    def __init__(self):
        r"""
        :param Managers: 公司管理人列表
        :type Managers: list of ManagerInfo
        :param TotalCount: 公司管理人总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Managers = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Managers") is not None:
            self.Managers = []
            for item in params.get("Managers"):
                obj = ManagerInfo()
                obj._deserialize(item)
                self.Managers.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribePackagesRequest(AbstractModel):
    """DescribePackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认0。
        :type Offset: int
        :param Limit: 限制数目，默认20。
        :type Limit: int
        :param Status: 按状态筛选。
        :type Status: str
        :param ExpireTime: 按过期时间升序或降序排列。
        :type ExpireTime: str
        :param PackageId: 按权益包ID搜索。
        :type PackageId: str
        :param Type: 按权益包类型搜索。
        :type Type: str
        :param Pid: 子产品编号
        :type Pid: int
        """
        self.Offset = None
        self.Limit = None
        self.Status = None
        self.ExpireTime = None
        self.PackageId = None
        self.Type = None
        self.Pid = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Status = params.get("Status")
        self.ExpireTime = params.get("ExpireTime")
        self.PackageId = params.get("PackageId")
        self.Type = params.get("Type")
        self.Pid = params.get("Pid")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePackagesResponse(AbstractModel):
    """DescribePackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param Packages: 权益包列表。
        :type Packages: list of PackageInfo
        :param TotalCount: 总条数。
        :type TotalCount: int
        :param TotalBalance: 权益点总余额。
        :type TotalBalance: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Packages = None
        self.TotalCount = None
        self.TotalBalance = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Packages") is not None:
            self.Packages = []
            for item in params.get("Packages"):
                obj = PackageInfo()
                obj._deserialize(item)
                self.Packages.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.TotalBalance = params.get("TotalBalance")
        self.RequestId = params.get("RequestId")


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownloadCertificateResponse(AbstractModel):
    """DownloadCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Content: ZIP base64 编码内容，base64 解码后可保存为 ZIP 文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        :param ContentType: MIME 类型：application/zip = ZIP 压缩文件。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContentType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Content = None
        self.ContentType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Content = params.get("Content")
        self.ContentType = params.get("ContentType")
        self.RequestId = params.get("RequestId")


class DvAuthDetail(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 DvAuthDetail 的内容。

    """

    def __init__(self):
        r"""
        :param DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param DvAuthKeySubDomain: DV 认证子域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKeySubDomain: str
        :param DvAuths: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuths: list of DvAuths
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthKeySubDomain = None
        self.DvAuths = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthKeySubDomain = params.get("DvAuthKeySubDomain")
        if params.get("DvAuths") is not None:
            self.DvAuths = []
            for item in params.get("DvAuths"):
                obj = DvAuths()
                obj._deserialize(item)
                self.DvAuths.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DvAuths(AbstractModel):
    """返回参数键为 DvAuths 的内容。

    """

    def __init__(self):
        r"""
        :param DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthKey: str
        :param DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthValue: str
        :param DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthDomain: str
        :param DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthPath: str
        :param DvAuthSubDomain: DV 认证子域名，
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthSubDomain: str
        :param DvAuthVerifyType: DV 认证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type DvAuthVerifyType: str
        """
        self.DvAuthKey = None
        self.DvAuthValue = None
        self.DvAuthDomain = None
        self.DvAuthPath = None
        self.DvAuthSubDomain = None
        self.DvAuthVerifyType = None


    def _deserialize(self, params):
        self.DvAuthKey = params.get("DvAuthKey")
        self.DvAuthValue = params.get("DvAuthValue")
        self.DvAuthDomain = params.get("DvAuthDomain")
        self.DvAuthPath = params.get("DvAuthPath")
        self.DvAuthSubDomain = params.get("DvAuthSubDomain")
        self.DvAuthVerifyType = params.get("DvAuthVerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤参数列表

    """

    def __init__(self):
        r"""
        :param FilterKey: 过滤参数key
        :type FilterKey: str
        :param FilterValue: 过滤参数值
        :type FilterValue: str
        """
        self.FilterKey = None
        self.FilterValue = None


    def _deserialize(self, params):
        self.FilterKey = params.get("FilterKey")
        self.FilterValue = params.get("FilterValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostCertificateRequest(AbstractModel):
    """HostCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param ResourceType: 资源类型：目前仅限于CLB,CDN
        :type ResourceType: list of str
        """
        self.CertificateId = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HostCertificateResponse(AbstractModel):
    """HostCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertHostingInfo: 云资源配置详情
        :type CertHostingInfo: :class:`tencentcloud.ssl.v20191205.models.CertHostingInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertHostingInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertHostingInfo") is not None:
            self.CertHostingInfo = CertHostingInfo()
            self.CertHostingInfo._deserialize(params.get("CertHostingInfo"))
        self.RequestId = params.get("RequestId")


class LighthouseInstanceDetail(AbstractModel):
    """Lighthouse实例

    """

    def __init__(self):
        r"""
        :param InstanceId: 实例ID
        :type InstanceId: str
        :param InstanceName: 实例名称
        :type InstanceName: str
        :param IP: IP地址
        :type IP: list of str
        :param Domain: 可选择域名
        :type Domain: list of str
        """
        self.InstanceId = None
        self.InstanceName = None
        self.IP = None
        self.Domain = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.IP = params.get("IP")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class LiveInstanceDetail(AbstractModel):
    """live实例详情

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param CertId: 已绑定的证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param Status: -1：域名未关联证书。
1： 域名https已开启。
0： 域名https已关闭。
        :type Status: int
        """
        self.Domain = None
        self.CertId = None
        self.Status = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManagerInfo(AbstractModel):
    """管理人信息

    """

    def __init__(self):
        r"""
        :param Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期
        :type Status: str
        :param ManagerFirstName: 管理人姓名
        :type ManagerFirstName: str
        :param ManagerLastName: 管理人姓名
        :type ManagerLastName: str
        :param ManagerPosition: 管理人职位
        :type ManagerPosition: str
        :param ManagerPhone: 管理人电话
        :type ManagerPhone: str
        :param ManagerMail: 管理人邮箱
        :type ManagerMail: str
        :param ManagerDepartment: 管理人所属部门
        :type ManagerDepartment: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param DomainCount: 管理人域名数量
        :type DomainCount: int
        :param CertCount: 管理人证书数量
        :type CertCount: int
        :param ManagerId: 管理人ID
        :type ManagerId: int
        :param ExpireTime: 审核有效到期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param SubmitAuditTime: 最近一次提交审核时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SubmitAuditTime: str
        :param VerifyTime: 审核通过时间
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyTime: str
        :param StatusInfo: 具体审核状态信息
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusInfo: list of ManagerStatusInfo
        """
        self.Status = None
        self.ManagerFirstName = None
        self.ManagerLastName = None
        self.ManagerPosition = None
        self.ManagerPhone = None
        self.ManagerMail = None
        self.ManagerDepartment = None
        self.CreateTime = None
        self.DomainCount = None
        self.CertCount = None
        self.ManagerId = None
        self.ExpireTime = None
        self.SubmitAuditTime = None
        self.VerifyTime = None
        self.StatusInfo = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.ManagerFirstName = params.get("ManagerFirstName")
        self.ManagerLastName = params.get("ManagerLastName")
        self.ManagerPosition = params.get("ManagerPosition")
        self.ManagerPhone = params.get("ManagerPhone")
        self.ManagerMail = params.get("ManagerMail")
        self.ManagerDepartment = params.get("ManagerDepartment")
        self.CreateTime = params.get("CreateTime")
        self.DomainCount = params.get("DomainCount")
        self.CertCount = params.get("CertCount")
        self.ManagerId = params.get("ManagerId")
        self.ExpireTime = params.get("ExpireTime")
        self.SubmitAuditTime = params.get("SubmitAuditTime")
        self.VerifyTime = params.get("VerifyTime")
        if params.get("StatusInfo") is not None:
            self.StatusInfo = []
            for item in params.get("StatusInfo"):
                obj = ManagerStatusInfo()
                obj._deserialize(item)
                self.StatusInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
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
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param Alias: 备注名称。
        :type Alias: str
        """
        self.CertificateId = None
        self.Alias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Alias = params.get("Alias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasResponse(AbstractModel):
    """ModifyCertificateAlias返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 修改成功的证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateIdList: 需要修改所属项目的证书 ID 集合，最多100个证书。
        :type CertificateIdList: list of str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        """
        self.CertificateIdList = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.CertificateIdList = params.get("CertificateIdList")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateProjectResponse(AbstractModel):
    """ModifyCertificateProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param SuccessCertificates: 修改所属项目成功的证书集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessCertificates: list of str
        :param FailCertificates: 修改所属项目失败的证书集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type FailCertificates: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SuccessCertificates = None
        self.FailCertificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCertificates = params.get("SuccessCertificates")
        self.FailCertificates = params.get("FailCertificates")
        self.RequestId = params.get("RequestId")


class ModifyCertificatesExpiringNotificationSwitchRequest(AbstractModel):
    """ModifyCertificatesExpiringNotificationSwitch请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateIds: 证书ID列表。最多50个
        :type CertificateIds: list of str
        :param SwitchStatus: 0:不忽略通知。1:忽略通知
        :type SwitchStatus: int
        """
        self.CertificateIds = None
        self.SwitchStatus = None


    def _deserialize(self, params):
        self.CertificateIds = params.get("CertificateIds")
        self.SwitchStatus = params.get("SwitchStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificatesExpiringNotificationSwitchResponse(AbstractModel):
    """ModifyCertificatesExpiringNotificationSwitch返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateIds: 证书ID列表
        :type CertificateIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateIds = params.get("CertificateIds")
        self.RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """证书操作日志。

    """

    def __init__(self):
        r"""
        :param Action: 操作证书动作。
        :type Action: str
        :param CreatedOn: 操作时间。
        :type CreatedOn: str
        """
        self.Action = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageInfo(AbstractModel):
    """权益包基本信息

    """

    def __init__(self):
        r"""
        :param PackageId: 权益包ID。
        :type PackageId: str
        :param Total: 权益包内权益点总量。
        :type Total: int
        :param Balance: 权益包内权益点余量。
        :type Balance: int
        :param Type: 权益包名称。
        :type Type: str
        :param SourceUin: 权益点是转入时，来源信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type SourceUin: int
        :param Status: 权益点状态。
        :type Status: str
        :param ExpireTime: 过期时间。
        :type ExpireTime: str
        :param UpdateTime: 更新时间。
        :type UpdateTime: str
        :param CreateTime: 生成时间。
        :type CreateTime: str
        :param SourceType: 来源类型。
        :type SourceType: str
        :param TransferOutInfos: 转移信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransferOutInfos: list of PackageTransferOutInfo
        """
        self.PackageId = None
        self.Total = None
        self.Balance = None
        self.Type = None
        self.SourceUin = None
        self.Status = None
        self.ExpireTime = None
        self.UpdateTime = None
        self.CreateTime = None
        self.SourceType = None
        self.TransferOutInfos = None


    def _deserialize(self, params):
        self.PackageId = params.get("PackageId")
        self.Total = params.get("Total")
        self.Balance = params.get("Balance")
        self.Type = params.get("Type")
        self.SourceUin = params.get("SourceUin")
        self.Status = params.get("Status")
        self.ExpireTime = params.get("ExpireTime")
        self.UpdateTime = params.get("UpdateTime")
        self.CreateTime = params.get("CreateTime")
        self.SourceType = params.get("SourceType")
        if params.get("TransferOutInfos") is not None:
            self.TransferOutInfos = []
            for item in params.get("TransferOutInfos"):
                obj = PackageTransferOutInfo()
                obj._deserialize(item)
                self.TransferOutInfos.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PackageTransferOutInfo(AbstractModel):
    """权益包转出详情

    """

    def __init__(self):
        r"""
        :param PackageId: 权益包ID。
        :type PackageId: str
        :param TransferCode: 转移码。
        :type TransferCode: str
        :param TransferCount: 本次转移点数。
        :type TransferCount: int
        :param ReceivePackageId: 转入的PackageID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceivePackageId: str
        :param ExpireTime: 本次转移过期时间。
        :type ExpireTime: str
        :param CreateTime: 本次转移生成时间。
        :type CreateTime: str
        :param UpdateTime: 本次转移更新时间。
        :type UpdateTime: str
        :param TransferStatus: 转移状态。
        :type TransferStatus: str
        :param ReceiverUin: 接收者uin。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiverUin: int
        :param ReceiveTime: 接收时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiveTime: str
        """
        self.PackageId = None
        self.TransferCode = None
        self.TransferCount = None
        self.ReceivePackageId = None
        self.ExpireTime = None
        self.CreateTime = None
        self.UpdateTime = None
        self.TransferStatus = None
        self.ReceiverUin = None
        self.ReceiveTime = None


    def _deserialize(self, params):
        self.PackageId = params.get("PackageId")
        self.TransferCode = params.get("TransferCode")
        self.TransferCount = params.get("TransferCount")
        self.ReceivePackageId = params.get("ReceivePackageId")
        self.ExpireTime = params.get("ExpireTime")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.TransferStatus = params.get("TransferStatus")
        self.ReceiverUin = params.get("ReceiverUin")
        self.ReceiveTime = params.get("ReceiveTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PreAuditInfo(AbstractModel):
    """预审核信息列表

    """

    def __init__(self):
        r"""
        :param TotalPeriod: 证书总年限
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalPeriod: int
        :param NowPeriod: 证书当前年限
注意：此字段可能返回 null，表示取不到有效值。
        :type NowPeriod: int
        :param ManagerId: 证书预审核管理人ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ManagerId: str
        """
        self.TotalPeriod = None
        self.NowPeriod = None
        self.ManagerId = None


    def _deserialize(self, params):
        self.TotalPeriod = params.get("TotalPeriod")
        self.NowPeriod = params.get("NowPeriod")
        self.ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProjectInfo(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 下，key为 ProjectInfo 的内容。

    """

    def __init__(self):
        r"""
        :param ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectName: str
        :param ProjectCreatorUin: 项目创建用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectCreatorUin: int
        :param ProjectCreateTime: 项目创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectCreateTime: str
        :param ProjectResume: 项目信息简述。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectResume: str
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OwnerUin: int
        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProjectId: str
        """
        self.ProjectName = None
        self.ProjectCreatorUin = None
        self.ProjectCreateTime = None
        self.ProjectResume = None
        self.OwnerUin = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectName = params.get("ProjectName")
        self.ProjectCreatorUin = params.get("ProjectCreatorUin")
        self.ProjectCreateTime = params.get("ProjectCreateTime")
        self.ProjectResume = params.get("ProjectResume")
        self.OwnerUin = params.get("OwnerUin")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateRequest(AbstractModel):
    """ReplaceCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param ValidType: 验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :type ValidType: str
        :param CsrType: 类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。
        :type CsrType: str
        :param CsrContent: CSR 内容。
        :type CsrContent: str
        :param CsrkeyPassword: KEY 密码。
        :type CsrkeyPassword: str
        :param Reason: 重颁发原因。
        :type Reason: str
        """
        self.CertificateId = None
        self.ValidType = None
        self.CsrType = None
        self.CsrContent = None
        self.CsrkeyPassword = None
        self.Reason = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ValidType = params.get("ValidType")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CsrkeyPassword = params.get("CsrkeyPassword")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReplaceCertificateResponse(AbstractModel):
    """ReplaceCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ResourceTypeRegions(AbstractModel):
    """云资源地域列表

    """

    def __init__(self):
        r"""
        :param ResourceType: 云资源类型
        :type ResourceType: str
        :param Regions: 地域列表
        :type Regions: list of str
        """
        self.ResourceType = None
        self.Regions = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.Regions = params.get("Regions")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeCertificateRequest(AbstractModel):
    """RevokeCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param Reason: 吊销证书原因。
        :type Reason: str
        """
        self.CertificateId = None
        self.Reason = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.Reason = params.get("Reason")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RevokeCertificateResponse(AbstractModel):
    """RevokeCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RevokeDomainValidateAuths: 吊销证书域名验证信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type RevokeDomainValidateAuths: list of RevokeDomainValidateAuths
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RevokeDomainValidateAuths = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RevokeDomainValidateAuths") is not None:
            self.RevokeDomainValidateAuths = []
            for item in params.get("RevokeDomainValidateAuths"):
                obj = RevokeDomainValidateAuths()
                obj._deserialize(item)
                self.RevokeDomainValidateAuths.append(obj)
        self.RequestId = params.get("RequestId")


class RevokeDomainValidateAuths(AbstractModel):
    """返回参数键为 RevokeDomainValidateAuths 的内容。

    """

    def __init__(self):
        r"""
        :param DomainValidateAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthPath: str
        :param DomainValidateAuthKey: DV 认证 KEY。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthKey: str
        :param DomainValidateAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthValue: str
        :param DomainValidateAuthDomain: DV 认证域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainValidateAuthDomain: str
        """
        self.DomainValidateAuthPath = None
        self.DomainValidateAuthKey = None
        self.DomainValidateAuthValue = None
        self.DomainValidateAuthDomain = None


    def _deserialize(self, params):
        self.DomainValidateAuthPath = params.get("DomainValidateAuthPath")
        self.DomainValidateAuthKey = params.get("DomainValidateAuthKey")
        self.DomainValidateAuthValue = params.get("DomainValidateAuthValue")
        self.DomainValidateAuthDomain = params.get("DomainValidateAuthDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RootCertificates(AbstractModel):
    """根证书

    """

    def __init__(self):
        r"""
        :param Sign: 国密签名证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Sign: str
        :param Encrypt: 国密加密证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Encrypt: str
        :param Standard: 标准证书
注意：此字段可能返回 null，表示取不到有效值。
        :type Standard: str
        """
        self.Sign = None
        self.Encrypt = None
        self.Standard = None


    def _deserialize(self, params):
        self.Sign = params.get("Sign")
        self.Encrypt = params.get("Encrypt")
        self.Standard = params.get("Standard")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAuditManagerRequest(AbstractModel):
    """SubmitAuditManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        """
        self.ManagerId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitAuditManagerResponse(AbstractModel):
    """SubmitAuditManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ManagerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param CsrType: CSR 生成方式：online = 在线生成, parse = 手动上传。
        :type CsrType: str
        :param CsrContent: 上传的 CSR 内容。
        :type CsrContent: str
        :param CertificateDomain: 绑定证书的域名。
        :type CertificateDomain: str
        :param DomainList: 上传的域名数组（多域名证书可以上传）。
        :type DomainList: list of str
        :param KeyPassword: 私钥密码（非必填）。
        :type KeyPassword: str
        :param OrganizationName: 公司名称。
        :type OrganizationName: str
        :param OrganizationDivision: 部门名称。
        :type OrganizationDivision: str
        :param OrganizationAddress: 公司详细地址。
        :type OrganizationAddress: str
        :param OrganizationCountry: 国家名称，如中国：CN 。
        :type OrganizationCountry: str
        :param OrganizationCity: 公司所在城市。
        :type OrganizationCity: str
        :param OrganizationRegion: 公司所在省份。
        :type OrganizationRegion: str
        :param PostalCode: 公司邮编。
        :type PostalCode: str
        :param PhoneAreaCode: 公司座机区号。
        :type PhoneAreaCode: str
        :param PhoneNumber: 公司座机号码。
        :type PhoneNumber: str
        :param VerifyType: 证书验证方式。验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。
        :type VerifyType: str
        :param AdminFirstName: 管理人名。
        :type AdminFirstName: str
        :param AdminLastName: 管理人姓。
        :type AdminLastName: str
        :param AdminPhoneNum: 管理人手机号码。
        :type AdminPhoneNum: str
        :param AdminEmail: 管理人邮箱地址。
        :type AdminEmail: str
        :param AdminPosition: 管理人职位。
        :type AdminPosition: str
        :param ContactFirstName: 联系人名。
        :type ContactFirstName: str
        :param ContactLastName: 联系人姓。
        :type ContactLastName: str
        :param ContactEmail: 联系人邮箱地址。
        :type ContactEmail: str
        :param ContactNumber: 联系人手机号码。
        :type ContactNumber: str
        :param ContactPosition: 联系人职位。
        :type ContactPosition: str
        """
        self.CertificateId = None
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.VerifyType = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactEmail = None
        self.ContactNumber = None
        self.ContactPosition = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.VerifyType = params.get("VerifyType")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactPosition = params.get("ContactPosition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SubmitCertificateInformationResponse(AbstractModel):
    """SubmitCertificateInformation返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 SubmittedData 的内容。

    """

    def __init__(self):
        r"""
        :param CsrType: CSR 类型，（online = 在线生成CSR，parse = 粘贴 CSR）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrType: str
        :param CsrContent: CSR 内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type CsrContent: str
        :param CertificateDomain: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateDomain: str
        :param DomainList: DNS 信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of str
        :param KeyPassword: 私钥密码。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyPassword: str
        :param OrganizationName: 企业或单位名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationName: str
        :param OrganizationDivision: 部门。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationDivision: str
        :param OrganizationAddress: 地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationAddress: str
        :param OrganizationCountry: 国家。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCountry: str
        :param OrganizationCity: 市。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationCity: str
        :param OrganizationRegion: 省。
注意：此字段可能返回 null，表示取不到有效值。
        :type OrganizationRegion: str
        :param PostalCode: 邮政编码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PostalCode: str
        :param PhoneAreaCode: 座机区号。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneAreaCode: str
        :param PhoneNumber: 座机号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type PhoneNumber: str
        :param AdminFirstName: 管理员名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminFirstName: str
        :param AdminLastName: 管理员姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminLastName: str
        :param AdminPhoneNum: 管理员电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPhoneNum: str
        :param AdminEmail: 管理员邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminEmail: str
        :param AdminPosition: 管理员职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdminPosition: str
        :param ContactFirstName: 联系人名。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactFirstName: str
        :param ContactLastName: 联系人姓。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactLastName: str
        :param ContactNumber: 联系人电话号码。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactNumber: str
        :param ContactEmail: 联系人邮箱地址，
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactEmail: str
        :param ContactPosition: 联系人职位。
注意：此字段可能返回 null，表示取不到有效值。
        :type ContactPosition: str
        :param VerifyType: 验证类型。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyType: str
        """
        self.CsrType = None
        self.CsrContent = None
        self.CertificateDomain = None
        self.DomainList = None
        self.KeyPassword = None
        self.OrganizationName = None
        self.OrganizationDivision = None
        self.OrganizationAddress = None
        self.OrganizationCountry = None
        self.OrganizationCity = None
        self.OrganizationRegion = None
        self.PostalCode = None
        self.PhoneAreaCode = None
        self.PhoneNumber = None
        self.AdminFirstName = None
        self.AdminLastName = None
        self.AdminPhoneNum = None
        self.AdminEmail = None
        self.AdminPosition = None
        self.ContactFirstName = None
        self.ContactLastName = None
        self.ContactNumber = None
        self.ContactEmail = None
        self.ContactPosition = None
        self.VerifyType = None


    def _deserialize(self, params):
        self.CsrType = params.get("CsrType")
        self.CsrContent = params.get("CsrContent")
        self.CertificateDomain = params.get("CertificateDomain")
        self.DomainList = params.get("DomainList")
        self.KeyPassword = params.get("KeyPassword")
        self.OrganizationName = params.get("OrganizationName")
        self.OrganizationDivision = params.get("OrganizationDivision")
        self.OrganizationAddress = params.get("OrganizationAddress")
        self.OrganizationCountry = params.get("OrganizationCountry")
        self.OrganizationCity = params.get("OrganizationCity")
        self.OrganizationRegion = params.get("OrganizationRegion")
        self.PostalCode = params.get("PostalCode")
        self.PhoneAreaCode = params.get("PhoneAreaCode")
        self.PhoneNumber = params.get("PhoneNumber")
        self.AdminFirstName = params.get("AdminFirstName")
        self.AdminLastName = params.get("AdminLastName")
        self.AdminPhoneNum = params.get("AdminPhoneNum")
        self.AdminEmail = params.get("AdminEmail")
        self.AdminPosition = params.get("AdminPosition")
        self.ContactFirstName = params.get("ContactFirstName")
        self.ContactLastName = params.get("ContactLastName")
        self.ContactNumber = params.get("ContactNumber")
        self.ContactEmail = params.get("ContactEmail")
        self.ContactPosition = params.get("ContactPosition")
        self.VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tags(AbstractModel):
    """标签

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
        


class TeoInstanceDetail(AbstractModel):
    """teo实例详情

    """

    def __init__(self):
        r"""
        :param Host: 域名
        :type Host: str
        :param CertId: 证书ID
        :type CertId: str
        :param ZoneId: 区域ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ZoneId: str
        :param Status: 域名状态
        :type Status: str
        """
        self.Host = None
        self.CertId = None
        self.ZoneId = None
        self.Status = None


    def _deserialize(self, params):
        self.Host = params.get("Host")
        self.CertId = params.get("CertId")
        self.ZoneId = params.get("ZoneId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeIngressDetail(AbstractModel):
    """tke ingress实例详情

    """

    def __init__(self):
        r"""
        :param IngressName: ingress名称
        :type IngressName: str
        :param TlsDomains: tls域名列表
        :type TlsDomains: list of str
        :param Domains: ingress域名列表
        :type Domains: list of str
        """
        self.IngressName = None
        self.TlsDomains = None
        self.Domains = None


    def _deserialize(self, params):
        self.IngressName = params.get("IngressName")
        self.TlsDomains = params.get("TlsDomains")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeInstanceDetail(AbstractModel):
    """tke实例详情

    """

    def __init__(self):
        r"""
        :param ClusterId: 集群ID
        :type ClusterId: str
        :param ClusterName: 集群名称
        :type ClusterName: str
        :param NamespaceList: 集群命名空间列表
        :type NamespaceList: list of TkeNameSpaceDetail
        """
        self.ClusterId = None
        self.ClusterName = None
        self.NamespaceList = None


    def _deserialize(self, params):
        self.ClusterId = params.get("ClusterId")
        self.ClusterName = params.get("ClusterName")
        if params.get("NamespaceList") is not None:
            self.NamespaceList = []
            for item in params.get("NamespaceList"):
                obj = TkeNameSpaceDetail()
                obj._deserialize(item)
                self.NamespaceList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeNameSpaceDetail(AbstractModel):
    """tke namespace详情

    """

    def __init__(self):
        r"""
        :param Name: namespace名称
        :type Name: str
        :param SecretList: secret列表
        :type SecretList: list of TkeSecretDetail
        """
        self.Name = None
        self.SecretList = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("SecretList") is not None:
            self.SecretList = []
            for item in params.get("SecretList"):
                obj = TkeSecretDetail()
                obj._deserialize(item)
                self.SecretList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TkeSecretDetail(AbstractModel):
    """tke secret详情

    """

    def __init__(self):
        r"""
        :param Name: secret名称
        :type Name: str
        :param CertId: 证书ID
        :type CertId: str
        :param IngressList: ingress列表
        :type IngressList: list of TkeIngressDetail
        :param NoMatchDomains: 和新证书不匹配的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type NoMatchDomains: list of str
        """
        self.Name = None
        self.CertId = None
        self.IngressList = None
        self.NoMatchDomains = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.CertId = params.get("CertId")
        if params.get("IngressList") is not None:
            self.IngressList = []
            for item in params.get("IngressList"):
                obj = TkeIngressDetail()
                obj._deserialize(item)
                self.IngressList.append(obj)
        self.NoMatchDomains = params.get("NoMatchDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceRequest(AbstractModel):
    """UpdateCertificateInstance请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 一键更新新证书ID
        :type CertificateId: str
        :param OldCertificateId: 一键更新原证书ID
        :type OldCertificateId: str
        :param ResourceTypes: 需要部署的资源类型
        :type ResourceTypes: list of str
        :param Regions: 需要部署的地域列表（废弃）
        :type Regions: list of str
        :param ResourceTypesRegions: 云资源需要部署的地域列表
        :type ResourceTypesRegions: list of ResourceTypeRegions
        """
        self.CertificateId = None
        self.OldCertificateId = None
        self.ResourceTypes = None
        self.Regions = None
        self.ResourceTypesRegions = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.OldCertificateId = params.get("OldCertificateId")
        self.ResourceTypes = params.get("ResourceTypes")
        self.Regions = params.get("Regions")
        if params.get("ResourceTypesRegions") is not None:
            self.ResourceTypesRegions = []
            for item in params.get("ResourceTypesRegions"):
                obj = ResourceTypeRegions()
                obj._deserialize(item)
                self.ResourceTypesRegions.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateInstanceResponse(AbstractModel):
    """UpdateCertificateInstance返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 云资源部署任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployRecordId: int
        :param DeployStatus: 部署状态，1表示部署成功，0表示部署失败
        :type DeployStatus: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeployRecordId = None
        self.DeployStatus = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.DeployStatus = params.get("DeployStatus")
        self.RequestId = params.get("RequestId")


class UpdateCertificateRecordRetryRequest(AbstractModel):
    """UpdateCertificateRecordRetry请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        :param DeployRecordDetailId: 待重试部署记录详情ID
        :type DeployRecordDetailId: int
        """
        self.DeployRecordId = None
        self.DeployRecordDetailId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.DeployRecordDetailId = params.get("DeployRecordDetailId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRetryResponse(AbstractModel):
    """UpdateCertificateRecordRetry返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateCertificateRecordRollbackRequest(AbstractModel):
    """UpdateCertificateRecordRollback请求参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 待重试部署记录ID
        :type DeployRecordId: int
        """
        self.DeployRecordId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateCertificateRecordRollbackResponse(AbstractModel):
    """UpdateCertificateRecordRollback返回参数结构体

    """

    def __init__(self):
        r"""
        :param DeployRecordId: 回滚部署记录ID
        :type DeployRecordId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DeployRecordId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeployRecordId = params.get("DeployRecordId")
        self.RequestId = params.get("RequestId")


class UpdateRecordDetail(AbstractModel):
    """更新记录详情

    """

    def __init__(self):
        r"""
        :param Id: 详情记录id
        :type Id: int
        :param CertId: 新证书ID
        :type CertId: str
        :param OldCertId: 旧证书ID
        :type OldCertId: str
        :param Domains: 部署域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param Region: 部署地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param Status: 部署状态
        :type Status: int
        :param ErrorMsg: 部署错误信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorMsg: str
        :param CreateTime: 部署时间
        :type CreateTime: str
        :param UpdateTime: 最后一次更新时间
        :type UpdateTime: str
        :param InstanceId: 部署实例ID
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param InstanceName: 部署实例名称
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceName: str
        :param ListenerId: 部署监听器ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerId: str
        :param ListenerName: 部署监听器名称
注意：此字段可能返回 null，表示取不到有效值。
        :type ListenerName: str
        :param Protocol: 协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param SniSwitch: 是否开启SNI
注意：此字段可能返回 null，表示取不到有效值。
        :type SniSwitch: int
        :param Bucket: bucket名称
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self.Id = None
        self.CertId = None
        self.OldCertId = None
        self.Domains = None
        self.ResourceType = None
        self.Region = None
        self.Status = None
        self.ErrorMsg = None
        self.CreateTime = None
        self.UpdateTime = None
        self.InstanceId = None
        self.InstanceName = None
        self.ListenerId = None
        self.ListenerName = None
        self.Protocol = None
        self.SniSwitch = None
        self.Bucket = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CertId = params.get("CertId")
        self.OldCertId = params.get("OldCertId")
        self.Domains = params.get("Domains")
        self.ResourceType = params.get("ResourceType")
        self.Region = params.get("Region")
        self.Status = params.get("Status")
        self.ErrorMsg = params.get("ErrorMsg")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        self.InstanceId = params.get("InstanceId")
        self.InstanceName = params.get("InstanceName")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Protocol = params.get("Protocol")
        self.SniSwitch = params.get("SniSwitch")
        self.Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordDetails(AbstractModel):
    """更新记录详情列表

    """

    def __init__(self):
        r"""
        :param ResourceType: 部署资源类型
        :type ResourceType: str
        :param List: 部署资源详情列表
        :type List: list of UpdateRecordDetail
        """
        self.ResourceType = None
        self.List = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        if params.get("List") is not None:
            self.List = []
            for item in params.get("List"):
                obj = UpdateRecordDetail()
                obj._deserialize(item)
                self.List.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateRecordInfo(AbstractModel):
    """部署记录信息

    """

    def __init__(self):
        r"""
        :param Id: 记录ID
        :type Id: int
        :param CertId: 新证书ID
        :type CertId: str
        :param OldCertId: 原证书ID
        :type OldCertId: str
        :param ResourceTypes: 部署资源类型列表
        :type ResourceTypes: list of str
        :param Regions: 部署地域列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Regions: list of str
        :param Status: 部署状态
        :type Status: int
        :param CreateTime: 部署时间
        :type CreateTime: str
        :param UpdateTime: 最后一次更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.CertId = None
        self.OldCertId = None
        self.ResourceTypes = None
        self.Regions = None
        self.Status = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.CertId = params.get("CertId")
        self.OldCertId = params.get("OldCertId")
        self.ResourceTypes = params.get("ResourceTypes")
        self.Regions = params.get("Regions")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificatePublicKey: 证书内容。
        :type CertificatePublicKey: str
        :param CertificatePrivateKey: 私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。
        :type CertificatePrivateKey: str
        :param CertificateType: 证书类型，默认 SVR。CA = CA证书，SVR = 服务器证书。
        :type CertificateType: str
        :param Alias: 备注名称。
        :type Alias: str
        :param ProjectId: 项目 ID。
        :type ProjectId: int
        :param CertificateUse: 证书用途/证书来源。“CLB，CDN，WAF，LIVE，DDOS”
        :type CertificateUse: str
        :param Repeatable: 相同的证书是否允许重复上传
        :type Repeatable: bool
        """
        self.CertificatePublicKey = None
        self.CertificatePrivateKey = None
        self.CertificateType = None
        self.Alias = None
        self.ProjectId = None
        self.CertificateUse = None
        self.Repeatable = None


    def _deserialize(self, params):
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificateType = params.get("CertificateType")
        self.Alias = params.get("Alias")
        self.ProjectId = params.get("ProjectId")
        self.CertificateUse = params.get("CertificateUse")
        self.Repeatable = params.get("Repeatable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadCertificateResponse(AbstractModel):
    """UploadCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RepeatCertId: 重复证书的ID
注意：此字段可能返回 null，表示取不到有效值。
        :type RepeatCertId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RepeatCertId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RepeatCertId = params.get("RepeatCertId")
        self.RequestId = params.get("RequestId")


class UploadConfirmLetterRequest(AbstractModel):
    """UploadConfirmLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param ConfirmLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :type ConfirmLetter: str
        """
        self.CertificateId = None
        self.ConfirmLetter = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.ConfirmLetter = params.get("ConfirmLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadConfirmLetterResponse(AbstractModel):
    """UploadConfirmLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param IsSuccess: 是否成功
        :type IsSuccess: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class UploadRevokeLetterRequest(AbstractModel):
    """UploadRevokeLetter请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param RevokeLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。
        :type RevokeLetter: str
        """
        self.CertificateId = None
        self.RevokeLetter = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RevokeLetter = params.get("RevokeLetter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadRevokeLetterResponse(AbstractModel):
    """UploadRevokeLetter返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书 ID。
        :type CertificateId: str
        :param IsSuccess: 是否成功。
        :type IsSuccess: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.IsSuccess = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.IsSuccess = params.get("IsSuccess")
        self.RequestId = params.get("RequestId")


class VerifyManagerRequest(AbstractModel):
    """VerifyManager请求参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        """
        self.ManagerId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyManagerResponse(AbstractModel):
    """VerifyManager返回参数结构体

    """

    def __init__(self):
        r"""
        :param ManagerId: 管理人ID
        :type ManagerId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ManagerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.RequestId = params.get("RequestId")


class VodInstanceDetail(AbstractModel):
    """Vod实例

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        :param CertId: 证书ID
        :type CertId: str
        """
        self.Domain = None
        self.CertId = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.CertId = params.get("CertId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        