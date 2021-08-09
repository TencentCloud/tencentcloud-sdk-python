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


class ApplyCertificateRequest(AbstractModel):
    """ApplyCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param DvAuthMethod: 验证方式：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证。\n        :type DvAuthMethod: str\n        :param DomainName: 域名。\n        :type DomainName: str\n        :param ProjectId: 项目 ID。\n        :type ProjectId: int\n        :param PackageType: 证书类型，目前仅支持类型2。2 = TrustAsia TLS RSA CA。\n        :type PackageType: str\n        :param ContactEmail: 邮箱。\n        :type ContactEmail: str\n        :param ContactPhone: 手机。\n        :type ContactPhone: str\n        :param ValidityPeriod: 有效期，默认12个月，目前仅支持12个月。\n        :type ValidityPeriod: str\n        :param CsrEncryptAlgo: 加密算法，仅支持 RSA。\n        :type CsrEncryptAlgo: str\n        :param CsrKeyParameter: 密钥对参数，仅支持2048。\n        :type CsrKeyParameter: str\n        :param CsrKeyPassword: CSR 的加密密码。\n        :type CsrKeyPassword: str\n        :param Alias: 备注名称。\n        :type Alias: str\n        :param OldCertificateId: 原证书 ID，用于重新申请。\n        :type OldCertificateId: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CancelCertificateOrderRequest(AbstractModel):
    """CancelCertificateOrder请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        """
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
        """
        :param CertificateId: 取消订单成功的证书 ID。\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CertificateExtra(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 数组下，key为CertificateExtra 的内容。

    """

    def __init__(self):
        """
        :param DomainNumber: 证书可配置域名数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainNumber: str\n        :param OriginCertificateId: 原始证书 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginCertificateId: str\n        :param ReplacedBy: 重颁发证书原始 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReplacedBy: str\n        :param ReplacedFor: 重颁发证书新 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReplacedFor: str\n        :param RenewOrder: 新订单证书 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewOrder: str\n        """
        self.DomainNumber = None
        self.OriginCertificateId = None
        self.ReplacedBy = None
        self.ReplacedFor = None
        self.RenewOrder = None


    def _deserialize(self, params):
        self.DomainNumber = params.get("DomainNumber")
        self.OriginCertificateId = params.get("OriginCertificateId")
        self.ReplacedBy = params.get("ReplacedBy")
        self.ReplacedFor = params.get("ReplacedFor")
        self.RenewOrder = params.get("RenewOrder")
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
        """
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: str\n        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: str\n        :param From: 证书来源。
注意：此字段可能返回 null，表示取不到有效值。\n        :type From: str\n        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageType: str\n        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateType: str\n        :param ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductZhName: str\n        :param Domain: 主域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        :param Status: 状态值 0：审核中，1：已通过，2：审核失败，3：已过期，4：已添加 DNS 解析记录，5：OV/EV 证书，待提交资料，6：订单取消中，7：已取消，8：已提交资料， 待上传确认函。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`\n        :param VulnerabilityStatus: 漏洞扫描状态：INACTIVE = 未开启，ACTIVE = 已开启
注意：此字段可能返回 null，表示取不到有效值。\n        :type VulnerabilityStatus: str\n        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusMsg: str\n        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyType: str\n        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertBeginTime: str\n        :param CertEndTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertEndTime: str\n        :param ValidityPeriod: 证书有效期，单位（月）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValidityPeriod: str\n        :param InsertTime: 创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InsertTime: str\n        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateId: str\n        :param SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubjectAltName: list of str\n        :param PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageTypeName: str\n        :param StatusName: 状态名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusName: str\n        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVip: bool\n        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDv: bool\n        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsWildcard: bool\n        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVulnerability: bool\n        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewAble: bool\n        :param ProjectInfo: 项目信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectInfo: :class:`tencentcloud.ssl.v20191205.models.ProjectInfo`\n        :param BoundResource: 关联的云资源，暂不可用
注意：此字段可能返回 null，表示取不到有效值。\n        :type BoundResource: list of str\n        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Deployable: bool\n        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tags\n        """
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
        """
        :param CertificateChain: 待检查的证书链\n        :type CertificateChain: str\n        """
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
        """
        :param IsValid: true为通过检查，false为未通过检查。\n        :type IsValid: bool\n        :param IsTrustedCA: true为可信CA，false为不可信CA。\n        :type IsTrustedCA: bool\n        :param Chains: 包含证书链中每一段证书的通用名称。\n        :type Chains: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.IsValid = None
        self.IsTrustedCA = None
        self.Chains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.IsValid = params.get("IsValid")
        self.IsTrustedCA = params.get("IsTrustedCA")
        self.Chains = params.get("Chains")
        self.RequestId = params.get("RequestId")


class CommitCertificateInformationRequest(AbstractModel):
    """CommitCertificateInformation请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
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
        """
        :param OrderId: CA机构侧订单号。\n        :type OrderId: str\n        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。\n        :type Status: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CompanyName: 公司名称\n        :type CompanyName: str\n        :param CompanyId: 公司ID\n        :type CompanyId: int\n        :param CompanyCountry: 公司所在国家\n        :type CompanyCountry: str\n        :param CompanyProvince: 公司所在省份\n        :type CompanyProvince: str\n        :param CompanyCity: 公司所在城市\n        :type CompanyCity: str\n        :param CompanyAddress: 公司所在详细地址\n        :type CompanyAddress: str\n        :param CompanyPhone: 公司电话\n        :type CompanyPhone: str\n        """
        self.CompanyName = None
        self.CompanyId = None
        self.CompanyCountry = None
        self.CompanyProvince = None
        self.CompanyCity = None
        self.CompanyAddress = None
        self.CompanyPhone = None


    def _deserialize(self, params):
        self.CompanyName = params.get("CompanyName")
        self.CompanyId = params.get("CompanyId")
        self.CompanyCountry = params.get("CompanyCountry")
        self.CompanyProvince = params.get("CompanyProvince")
        self.CompanyCity = params.get("CompanyCity")
        self.CompanyAddress = params.get("CompanyAddress")
        self.CompanyPhone = params.get("CompanyPhone")
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
        """
        :param CertificateId: 证书ID\n        :type CertificateId: str\n        """
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
        """
        :param CertificateId: 证书ID\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param ProductId: 证书商品ID，3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书，25 = Wotrus 域名型证书，26 = Wotrus 域名型多域名证书，27 = Wotrus 域名型通配符证书，28 = Wotrus 企业型证书，29 = Wotrus 企业型多域名证书，30 = Wotrus 企业型通配符证书，31 = Wotrus 增强型证书，32 = Wotrus 增强型多域名证书，33 = DNSPod 国密域名型证书，34 = DNSPod 国密域名型多域名证书，35 = DNSPod 国密域名型通配符证书，37 = DNSPod 国密企业型证书，38 = DNSPod 国密企业型多域名证书，39 = DNSPod 国密企业型通配符证书，40 = DNSPod 国密增强型证书，41 = DNSPod 国密增强型多域名证书，42 = TrustAsia 域名型通配符多域名证书。\n        :type ProductId: int\n        :param DomainNum: 证书包含的域名数量\n        :type DomainNum: int\n        :param TimeSpan: 证书年限，当前只支持 1 年证书的购买\n        :type TimeSpan: int\n        """
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
        """
        :param CertificateIds: 证书ID列表\n        :type CertificateIds: list of str\n        :param DealIds: 订单号列表\n        :type DealIds: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateIds = None
        self.DealIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateIds = params.get("CertificateIds")
        self.DealIds = params.get("DealIds")
        self.RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        """
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
        """
        :param DeleteResult: 删除结果（true：删除成功，false：删除失败）\n        :type DeleteResult: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DeleteResult = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DeleteResult = params.get("DeleteResult")
        self.RequestId = params.get("RequestId")


class DeleteManagerRequest(AbstractModel):
    """DeleteManager请求参数结构体

    """

    def __init__(self):
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        """
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
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ManagerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        """
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
        """
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: str\n        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: str\n        :param From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。\n        :type From: str\n        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateType: str\n        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书，25 = Wotrus 域名型证书，26 = Wotrus 域名型多域名证书，27 = Wotrus 域名型通配符证书，28 = Wotrus 企业型证书，29 = Wotrus 企业型多域名证书，30 = Wotrus 企业型通配符证书，31 = Wotrus 增强型证书，32 = Wotrus 增强型多域名证书，33 = DNSPod 国密域名型证书，34 = DNSPod 国密域名型多域名证书，35 = DNSPod 国密域名型通配符证书，37 = DNSPod 国密企业型证书，38 = DNSPod 国密企业型多域名证书，39 = DNSPod 国密企业型通配符证书，40 = DNSPod 国密增强型证书，41 = DNSPod 国密增强型多域名证书，42 = TrustAsia 域名型通配符多域名证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageType: str\n        :param ProductZhName: 颁发者。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductZhName: str\n        :param Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函，13 = 免费证书待提交资料。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusMsg: str\n        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyType: str\n        :param VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VulnerabilityStatus: str\n        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertBeginTime: str\n        :param CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertEndTime: str\n        :param ValidityPeriod: 证书有效期：单位（月）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValidityPeriod: str\n        :param InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InsertTime: str\n        :param OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrderId: str\n        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`\n        :param CertificatePrivateKey: 证书私钥
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificatePrivateKey: str\n        :param CertificatePublicKey: 证书公钥（即证书内容）
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificatePublicKey: str\n        :param DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`\n        :param VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VulnerabilityReport: str\n        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateId: str\n        :param TypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeName: str\n        :param StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusName: str\n        :param SubjectAltName: 证书包含的多个域名（包含主域名）
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubjectAltName: list of str\n        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVip: bool\n        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsWildcard: bool\n        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDv: bool\n        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVulnerability: bool\n        :param SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`\n        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewAble: bool\n        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Deployable: bool\n        :param Tags: 关联标签列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tags\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DescribeCertificateOperateLogsRequest(AbstractModel):
    """DescribeCertificateOperateLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 请求日志数量，默认为20。\n        :type Limit: int\n        :param StartTime: 开始时间，默认15天前。\n        :type StartTime: str\n        :param EndTime: 结束时间，默认现在时间。\n        :type EndTime: str\n        """
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
        """
        :param AllTotal: 当前查询条件日志总数。\n        :type AllTotal: int\n        :param TotalCount: 本次请求返回的日志数量。\n        :type TotalCount: int\n        :param OperateLogs: 证书操作日志列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OperateLogs: list of OperationLog\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        """
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
        """
        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: str\n        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: str\n        :param From: 证书来源：trustasia = 亚洲诚信，upload = 用户上传。
注意：此字段可能返回 null，表示取不到有效值。\n        :type From: str\n        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateType: str\n        :param PackageType: 证书套餐类型：1 = GeoTrust DV SSL CA - G3， 2 = TrustAsia TLS RSA CA， 3 = SecureSite 增强型企业版（EV Pro）， 4 = SecureSite 增强型（EV）， 5 = SecureSite 企业型专业版（OV Pro）， 6 = SecureSite 企业型（OV）， 7 = SecureSite 企业型（OV）通配符， 8 = Geotrust 增强型（EV）， 9 = Geotrust 企业型（OV）， 10 = Geotrust 企业型（OV）通配符， 11 = TrustAsia 域名型多域名 SSL 证书， 12 = TrustAsia 域名型（DV）通配符， 13 = TrustAsia 企业型通配符（OV）SSL 证书（D3）， 14 = TrustAsia 企业型（OV）SSL 证书（D3）， 15 = TrustAsia 企业型多域名 （OV）SSL 证书（D3）， 16 = TrustAsia 增强型 （EV）SSL 证书（D3）， 17 = TrustAsia 增强型多域名（EV）SSL 证书（D3）， 18 = GlobalSign 企业型（OV）SSL 证书， 19 = GlobalSign 企业型通配符 （OV）SSL 证书， 20 = GlobalSign 增强型 （EV）SSL 证书， 21 = TrustAsia 企业型通配符多域名（OV）SSL 证书（D3）， 22 = GlobalSign 企业型多域名（OV）SSL 证书， 23 = GlobalSign 企业型通配符多域名（OV）SSL 证书， 24 = GlobalSign 增强型多域名（EV）SSL 证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageType: str\n        :param ProductZhName: 证书颁发者名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProductZhName: str\n        :param Domain: 域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        :param Alias: 备注名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Alias: str\n        :param Status: 证书状态：0 = 审核中，1 = 已通过，2 = 审核失败，3 = 已过期，4 = 已添加DNS记录，5 = 企业证书，待提交，6 = 订单取消中，7 = 已取消，8 = 已提交资料， 待上传确认函，9 = 证书吊销中，10 = 已吊销，11 = 重颁发中，12 = 待上传吊销确认函。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: int\n        :param StatusMsg: 状态信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusMsg: str\n        :param VerifyType: 验证类型：DNS_AUTO = 自动DNS验证，DNS = 手动DNS验证，FILE = 文件验证，EMAIL = 邮件验证。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyType: str\n        :param VulnerabilityStatus: 漏洞扫描状态。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VulnerabilityStatus: str\n        :param CertBeginTime: 证书生效时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertBeginTime: str\n        :param CertEndTime: 证书失效时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertEndTime: str\n        :param ValidityPeriod: 证书有效期：单位(月)。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValidityPeriod: str\n        :param InsertTime: 申请时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type InsertTime: str\n        :param OrderId: 订单 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrderId: str\n        :param CertificateExtra: 证书扩展信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateExtra: :class:`tencentcloud.ssl.v20191205.models.CertificateExtra`\n        :param DvAuthDetail: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthDetail: :class:`tencentcloud.ssl.v20191205.models.DvAuthDetail`\n        :param VulnerabilityReport: 漏洞扫描评估报告。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VulnerabilityReport: str\n        :param CertificateId: 证书 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateId: str\n        :param PackageTypeName: 证书类型名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PackageTypeName: str\n        :param StatusName: 状态描述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusName: str\n        :param SubjectAltName: 证书包含的多个域名（包含主域名）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubjectAltName: list of str\n        :param IsVip: 是否为 VIP 客户。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVip: bool\n        :param IsWildcard: 是否为泛域名证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsWildcard: bool\n        :param IsDv: 是否为 DV 版证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsDv: bool\n        :param IsVulnerability: 是否启用了漏洞扫描功能。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IsVulnerability: bool\n        :param RenewAble: 是否可重颁发证书。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RenewAble: bool\n        :param SubmittedData: 提交的资料信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubmittedData: :class:`tencentcloud.ssl.v20191205.models.SubmittedData`\n        :param Deployable: 是否可部署。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Deployable: bool\n        :param Tags: 标签列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tags: list of Tags\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页偏移量，从0开始。\n        :type Offset: int\n        :param Limit: 每页数量，默认20。\n        :type Limit: int\n        :param SearchKey: 搜索关键词，可搜索证书 ID、备注名称、域名。例如： a8xHcaIs。\n        :type SearchKey: str\n        :param CertificateType: 证书类型：CA = 客户端证书，SVR = 服务器证书。\n        :type CertificateType: str\n        :param ProjectId: 项目 ID。\n        :type ProjectId: int\n        :param ExpirationSort: 按到期时间排序：DESC = 降序， ASC = 升序。\n        :type ExpirationSort: str\n        :param CertificateStatus: 证书状态。\n        :type CertificateStatus: list of int non-negative\n        :param Deployable: 是否可部署，可选值：1 = 可部署，0 =  不可部署。\n        :type Deployable: int\n        :param Upload: 是否筛选上传托管的 1筛选，0不筛选\n        :type Upload: int\n        :param Renew: 是否筛选可续期证书 1筛选 0不筛选\n        :type Renew: int\n        """
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
        """
        :param TotalCount: 总数量。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param Certificates: 列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Certificates: list of Certificates\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeManagerDetailRequest(AbstractModel):
    """DescribeManagerDetail请求参数结构体

    """

    def __init__(self):
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        :param Limit: 分页每页数量\n        :type Limit: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        """
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
        """
        :param Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期\n        :type Status: str\n        :param ManagerFirstName: 管理人姓名\n        :type ManagerFirstName: str\n        :param ManagerMail: 管理人邮箱\n        :type ManagerMail: str\n        :param ContactFirstName: 联系人姓名\n        :type ContactFirstName: str\n        :param ManagerLastName: 管理人姓名\n        :type ManagerLastName: str\n        :param ContactPosition: 联系人职位\n        :type ContactPosition: str\n        :param ManagerPosition: 管理人职位\n        :type ManagerPosition: str\n        :param VerifyTime: 核验通过时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyTime: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param ExpireTime: 核验过期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param ContactLastName: 联系人姓名\n        :type ContactLastName: str\n        :param ManagerPhone: 管理人电话\n        :type ManagerPhone: str\n        :param ContactPhone: 联系人电话\n        :type ContactPhone: str\n        :param ContactMail: 联系人邮箱\n        :type ContactMail: str\n        :param ManagerDepartment: 管理人所属部门\n        :type ManagerDepartment: str\n        :param CompanyInfo: 管理人所属公司信息\n        :type CompanyInfo: :class:`tencentcloud.ssl.v20191205.models.CompanyInfo`\n        :param CompanyId: 管理人公司ID\n        :type CompanyId: int\n        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        self.RequestId = params.get("RequestId")


class DescribeManagersRequest(AbstractModel):
    """DescribeManagers请求参数结构体

    """

    def __init__(self):
        """
        :param CompanyId: 公司ID\n        :type CompanyId: int\n        :param Offset: 分页偏移量\n        :type Offset: int\n        :param Limit: 分页每页数量\n        :type Limit: int\n        :param ManagerName: 管理人姓名\n        :type ManagerName: str\n        :param ManagerMail: 模糊查询管理人邮箱\n        :type ManagerMail: str\n        :param Status: 根据管理人状态进行筛选，取值有
'none' 未提交审核
'audit', 亚信审核中
'CAaudit' CA审核中
'ok' 已审核
'invalid'  审核失败
'expiring'  即将过期
'expired' 已过期\n        :type Status: str\n        """
        self.CompanyId = None
        self.Offset = None
        self.Limit = None
        self.ManagerName = None
        self.ManagerMail = None
        self.Status = None


    def _deserialize(self, params):
        self.CompanyId = params.get("CompanyId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ManagerName = params.get("ManagerName")
        self.ManagerMail = params.get("ManagerMail")
        self.Status = params.get("Status")
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
        """
        :param Managers: 公司管理人列表\n        :type Managers: list of ManagerInfo\n        :param TotalCount: 公司管理人总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DownloadCertificateRequest(AbstractModel):
    """DownloadCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        """
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
        """
        :param Content: ZIP base64 编码内容，base64 解码后可保存为 ZIP 文件。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Content: str\n        :param ContentType: MIME 类型：application/zip = ZIP 压缩文件。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContentType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthKey: str\n        :param DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthValue: str\n        :param DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthDomain: str\n        :param DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthPath: str\n        :param DvAuthKeySubDomain: DV 认证子域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthKeySubDomain: str\n        :param DvAuths: DV 认证信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuths: list of DvAuths\n        """
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
        """
        :param DvAuthKey: DV 认证密钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthKey: str\n        :param DvAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthValue: str\n        :param DvAuthDomain: DV 认证值域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthDomain: str\n        :param DvAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthPath: str\n        :param DvAuthSubDomain: DV 认证子域名，
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthSubDomain: str\n        :param DvAuthVerifyType: DV 认证类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DvAuthVerifyType: str\n        """
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
        


class ManagerInfo(AbstractModel):
    """管理人信息

    """

    def __init__(self):
        """
        :param Status: 状态: audit: 审核中 ok: 审核通过 invalid: 失效 expiring: 即将过期 expired: 已过期\n        :type Status: str\n        :param ManagerFirstName: 管理人姓名\n        :type ManagerFirstName: str\n        :param ManagerLastName: 管理人姓名\n        :type ManagerLastName: str\n        :param ManagerPosition: 管理人职位\n        :type ManagerPosition: str\n        :param ManagerPhone: 管理人电话\n        :type ManagerPhone: str\n        :param ManagerMail: 管理人邮箱\n        :type ManagerMail: str\n        :param ManagerDepartment: 管理人所属部门\n        :type ManagerDepartment: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param DomainCount: 管理人域名数量\n        :type DomainCount: int\n        :param CertCount: 管理人证书数量\n        :type CertCount: int\n        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        :param ExpireTime: 审核有效到期时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param SubmitAuditTime: 最近一次提交审核时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubmitAuditTime: str\n        :param VerifyTime: 审核通过时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyTime: str\n        """
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAliasRequest(AbstractModel):
    """ModifyCertificateAlias请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param Alias: 备注名称。\n        :type Alias: str\n        """
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
        """
        :param CertificateId: 修改成功的证书 ID。\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class ModifyCertificateProjectRequest(AbstractModel):
    """ModifyCertificateProject请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateIdList: 需要修改所属项目的证书 ID 集合，最多100个证书。\n        :type CertificateIdList: list of str\n        :param ProjectId: 项目 ID。\n        :type ProjectId: int\n        """
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
        """
        :param SuccessCertificates: 修改所属项目成功的证书集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessCertificates: list of str\n        :param FailCertificates: 修改所属项目失败的证书集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailCertificates: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SuccessCertificates = None
        self.FailCertificates = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessCertificates = params.get("SuccessCertificates")
        self.FailCertificates = params.get("FailCertificates")
        self.RequestId = params.get("RequestId")


class OperationLog(AbstractModel):
    """证书操作日志。

    """

    def __init__(self):
        """
        :param Action: 操作证书动作。\n        :type Action: str\n        :param CreatedOn: 操作时间。\n        :type CreatedOn: str\n        """
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
        


class ProjectInfo(AbstractModel):
    """获取证书列表（DescribeCertificates）返回参数键为 Certificates 下，key为 ProjectInfo 的内容。

    """

    def __init__(self):
        """
        :param ProjectName: 项目名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectName: str\n        :param ProjectCreatorUin: 项目创建用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectCreatorUin: int\n        :param ProjectCreateTime: 项目创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectCreateTime: str\n        :param ProjectResume: 项目信息简述。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectResume: str\n        :param OwnerUin: 用户 UIN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OwnerUin: int\n        :param ProjectId: 项目 ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProjectId: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param ValidType: 验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。\n        :type ValidType: str\n        :param CsrType: 类型，默认 Original。可选项：Original = 原证书 CSR，Upload = 手动上传，Online = 在线生成。\n        :type CsrType: str\n        :param CsrContent: CSR 内容。\n        :type CsrContent: str\n        :param CsrkeyPassword: KEY 密码。\n        :type CsrkeyPassword: str\n        :param Reason: 重颁发原因。\n        :type Reason: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class RevokeCertificateRequest(AbstractModel):
    """RevokeCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param Reason: 吊销证书原因。\n        :type Reason: str\n        """
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
        """
        :param RevokeDomainValidateAuths: 吊销证书域名验证信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RevokeDomainValidateAuths: list of RevokeDomainValidateAuths\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param DomainValidateAuthPath: DV 认证值路径。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainValidateAuthPath: str\n        :param DomainValidateAuthKey: DV 认证 KEY。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainValidateAuthKey: str\n        :param DomainValidateAuthValue: DV 认证值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainValidateAuthValue: str\n        :param DomainValidateAuthDomain: DV 认证域名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainValidateAuthDomain: str\n        """
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
        


class SubmitAuditManagerRequest(AbstractModel):
    """SubmitAuditManager请求参数结构体

    """

    def __init__(self):
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        """
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
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ManagerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.RequestId = params.get("RequestId")


class SubmitCertificateInformationRequest(AbstractModel):
    """SubmitCertificateInformation请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param CsrType: CSR 生成方式：online = 在线生成, parse = 手动上传。\n        :type CsrType: str\n        :param CsrContent: 上传的 CSR 内容。\n        :type CsrContent: str\n        :param CertificateDomain: 绑定证书的域名。\n        :type CertificateDomain: str\n        :param DomainList: 上传的域名数组（多域名证书可以上传）。\n        :type DomainList: list of str\n        :param KeyPassword: 私钥密码（非必填）。\n        :type KeyPassword: str\n        :param OrganizationName: 公司名称。\n        :type OrganizationName: str\n        :param OrganizationDivision: 部门名称。\n        :type OrganizationDivision: str\n        :param OrganizationAddress: 公司详细地址。\n        :type OrganizationAddress: str\n        :param OrganizationCountry: 国家名称，如中国：CN 。\n        :type OrganizationCountry: str\n        :param OrganizationCity: 公司所在城市。\n        :type OrganizationCity: str\n        :param OrganizationRegion: 公司所在省份。\n        :type OrganizationRegion: str\n        :param PostalCode: 公司邮编。\n        :type PostalCode: str\n        :param PhoneAreaCode: 公司座机区号。\n        :type PhoneAreaCode: str\n        :param PhoneNumber: 公司座机号码。\n        :type PhoneNumber: str\n        :param VerifyType: 证书验证方式。验证类型：DNS_AUTO = 自动DNS验证（仅支持在腾讯云解析且解析状态正常的域名使用该验证类型），DNS = 手动DNS验证，FILE = 文件验证。\n        :type VerifyType: str\n        :param AdminFirstName: 管理人名。\n        :type AdminFirstName: str\n        :param AdminLastName: 管理人姓。\n        :type AdminLastName: str\n        :param AdminPhoneNum: 管理人手机号码。\n        :type AdminPhoneNum: str\n        :param AdminEmail: 管理人邮箱地址。\n        :type AdminEmail: str\n        :param AdminPosition: 管理人职位。\n        :type AdminPosition: str\n        :param ContactFirstName: 联系人名。\n        :type ContactFirstName: str\n        :param ContactLastName: 联系人姓。\n        :type ContactLastName: str\n        :param ContactEmail: 联系人邮箱地址。\n        :type ContactEmail: str\n        :param ContactNumber: 联系人手机号码。\n        :type ContactNumber: str\n        :param ContactPosition: 联系人职位。\n        :type ContactPosition: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class SubmittedData(AbstractModel):
    """获取证书列表（DescribeCertificate）返回参数键为 SubmittedData 的内容。

    """

    def __init__(self):
        """
        :param CsrType: CSR 类型，（online = 在线生成CSR，parse = 粘贴 CSR）。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CsrType: str\n        :param CsrContent: CSR 内容。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CsrContent: str\n        :param CertificateDomain: 域名信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertificateDomain: str\n        :param DomainList: DNS 信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainList: list of str\n        :param KeyPassword: 私钥密码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyPassword: str\n        :param OrganizationName: 企业或单位名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationName: str\n        :param OrganizationDivision: 部门。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationDivision: str\n        :param OrganizationAddress: 地址。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationAddress: str\n        :param OrganizationCountry: 国家。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationCountry: str\n        :param OrganizationCity: 市。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationCity: str\n        :param OrganizationRegion: 省。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OrganizationRegion: str\n        :param PostalCode: 邮政编码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostalCode: str\n        :param PhoneAreaCode: 座机区号。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneAreaCode: str\n        :param PhoneNumber: 座机号码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PhoneNumber: str\n        :param AdminFirstName: 管理员名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdminFirstName: str\n        :param AdminLastName: 管理员姓。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdminLastName: str\n        :param AdminPhoneNum: 管理员电话号码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdminPhoneNum: str\n        :param AdminEmail: 管理员邮箱地址。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdminEmail: str\n        :param AdminPosition: 管理员职位。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdminPosition: str\n        :param ContactFirstName: 联系人名。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContactFirstName: str\n        :param ContactLastName: 联系人姓。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContactLastName: str\n        :param ContactNumber: 联系人电话号码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContactNumber: str\n        :param ContactEmail: 联系人邮箱地址，
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContactEmail: str\n        :param ContactPosition: 联系人职位。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ContactPosition: str\n        :param VerifyType: 验证类型。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyType: str\n        """
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
        """
        :param TagKey: 标签键\n        :type TagKey: str\n        :param TagValue: 标签值\n        :type TagValue: str\n        """
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
        


class UploadCertificateRequest(AbstractModel):
    """UploadCertificate请求参数结构体

    """

    def __init__(self):
        """
        :param CertificatePublicKey: 证书内容。\n        :type CertificatePublicKey: str\n        :param CertificatePrivateKey: 私钥内容，证书类型为 SVR 时必填，为 CA 时可不填。\n        :type CertificatePrivateKey: str\n        :param CertificateType: 证书类型，默认 SVR。CA = 客户端证书，SVR = 服务器证书。\n        :type CertificateType: str\n        :param Alias: 备注名称。\n        :type Alias: str\n        :param ProjectId: 项目 ID。\n        :type ProjectId: int\n        :param CertificateUse: 证书用途/证书来源。“CLB，CDN，WAF，LIVE，DDOS”\n        :type CertificateUse: str\n        """
        self.CertificatePublicKey = None
        self.CertificatePrivateKey = None
        self.CertificateType = None
        self.Alias = None
        self.ProjectId = None
        self.CertificateUse = None


    def _deserialize(self, params):
        self.CertificatePublicKey = params.get("CertificatePublicKey")
        self.CertificatePrivateKey = params.get("CertificatePrivateKey")
        self.CertificateType = params.get("CertificateType")
        self.Alias = params.get("Alias")
        self.ProjectId = params.get("ProjectId")
        self.CertificateUse = params.get("CertificateUse")
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class UploadConfirmLetterRequest(AbstractModel):
    """UploadConfirmLetter请求参数结构体

    """

    def __init__(self):
        """
        :param CertificateId: 证书ID\n        :type CertificateId: str\n        :param ConfirmLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。\n        :type ConfirmLetter: str\n        """
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
        """
        :param CertificateId: 证书ID\n        :type CertificateId: str\n        :param IsSuccess: 是否成功\n        :type IsSuccess: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param RevokeLetter: base64编码后的证书确认函文件，格式应为jpg、jpeg、png、pdf，大小应在1kb与1.4M之间。\n        :type RevokeLetter: str\n        """
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
        """
        :param CertificateId: 证书 ID。\n        :type CertificateId: str\n        :param IsSuccess: 是否成功。\n        :type IsSuccess: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        """
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
        """
        :param ManagerId: 管理人ID\n        :type ManagerId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.ManagerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ManagerId = params.get("ManagerId")
        self.RequestId = params.get("RequestId")