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


class BatchStatus(AbstractModel):
    """批量任务状态

    """

    def __init__(self):
        """
        :param LogId: 批量任务id
        :type LogId: int
        :param Status: 批量任务状态  doing：进行中  success：成功  failed：失败  partial_success：部分成功
        :type Status: str
        :param BatchAction: 批量任务类型
        :type BatchAction: str
        """
        self.LogId = None
        self.Status = None
        self.BatchAction = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.Status = params.get("Status")
        self.BatchAction = params.get("BatchAction")


class CertificateInfo(AbstractModel):
    """认证资料信息

    """

    def __init__(self):
        """
        :param CertificateCode: 证件号码。
        :type CertificateCode: str
        :param CertificateType: 证件类型。
        :type CertificateType: str
        :param ImgUrl: 证件照片地址。
        :type ImgUrl: str
        """
        self.CertificateCode = None
        self.CertificateType = None
        self.ImgUrl = None


    def _deserialize(self, params):
        self.CertificateCode = params.get("CertificateCode")
        self.CertificateType = params.get("CertificateType")
        self.ImgUrl = params.get("ImgUrl")


class CheckBatchStatusRequest(AbstractModel):
    """CheckBatchStatus请求参数结构体

    """

    def __init__(self):
        """
        :param LogIds: 批量任务id数组，最多 200 个
        :type LogIds: list of int non-negative
        """
        self.LogIds = None


    def _deserialize(self, params):
        self.LogIds = params.get("LogIds")


class CheckBatchStatusResponse(AbstractModel):
    """CheckBatchStatus返回参数结构体

    """

    def __init__(self):
        """
        :param StatusSet: 批量任务状态集
        :type StatusSet: list of BatchStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatusSet") is not None:
            self.StatusSet = []
            for item in params.get("StatusSet"):
                obj = BatchStatus()
                obj._deserialize(item)
                self.StatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class CheckDomainRequest(AbstractModel):
    """CheckDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 所查询域名名称
        :type DomainName: str
        :param Period: 年限
        :type Period: str
        """
        self.DomainName = None
        self.Period = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Period = params.get("Period")


class CheckDomainResponse(AbstractModel):
    """CheckDomain返回参数结构体

    """

    def __init__(self):
        """
        :param DomainName: 所查询域名名称
        :type DomainName: str
        :param Available: 是否能够注册
        :type Available: bool
        :param Reason: 不能注册原因
        :type Reason: str
        :param Premium: 是否是溢价词
        :type Premium: bool
        :param Price: 域名价格
        :type Price: int
        :param BlackWord: 是否是敏感词
        :type BlackWord: bool
        :param Describe: 溢价词描述
注意：此字段可能返回 null，表示取不到有效值。
        :type Describe: str
        :param FeeRenew: 溢价词的续费价格
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeRenew: int
        :param RealPrice: 域名真实价格
注意：此字段可能返回 null，表示取不到有效值。
        :type RealPrice: int
        :param FeeTransfer: 溢价词的转入价格
注意：此字段可能返回 null，表示取不到有效值。
        :type FeeTransfer: int
        :param FeeRestore: 溢价词的赎回价格
        :type FeeRestore: int
        :param Period: 检测年限
        :type Period: int
        :param RecordSupport: 是否支持北京备案  true 支持  false 不支持
        :type RecordSupport: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainName = None
        self.Available = None
        self.Reason = None
        self.Premium = None
        self.Price = None
        self.BlackWord = None
        self.Describe = None
        self.FeeRenew = None
        self.RealPrice = None
        self.FeeTransfer = None
        self.FeeRestore = None
        self.Period = None
        self.RecordSupport = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Available = params.get("Available")
        self.Reason = params.get("Reason")
        self.Premium = params.get("Premium")
        self.Price = params.get("Price")
        self.BlackWord = params.get("BlackWord")
        self.Describe = params.get("Describe")
        self.FeeRenew = params.get("FeeRenew")
        self.RealPrice = params.get("RealPrice")
        self.FeeTransfer = params.get("FeeTransfer")
        self.FeeRestore = params.get("FeeRestore")
        self.Period = params.get("Period")
        self.RecordSupport = params.get("RecordSupport")
        self.RequestId = params.get("RequestId")


class ContactInfo(AbstractModel):
    """域名联系人信息

    """

    def __init__(self):
        """
        :param OrganizationNameCN: 注册人（中文）
        :type OrganizationNameCN: str
        :param OrganizationName: 注册人（英文）
        :type OrganizationName: str
        :param RegistrantNameCN: 联系人（中文）
        :type RegistrantNameCN: str
        :param RegistrantName: 联系人（英文）
        :type RegistrantName: str
        :param ProvinceCN: 省份（中文）
        :type ProvinceCN: str
        :param CityCN: 城市（中文）
        :type CityCN: str
        :param StreetCN: 街道（中文）
        :type StreetCN: str
        :param Street: 街道（英文）
        :type Street: str
        :param CountryCN: 国家（中文）
        :type CountryCN: str
        :param Telephone: 联系人手机号
        :type Telephone: str
        :param Email: 联系人邮箱
        :type Email: str
        :param ZipCode: 邮编
        :type ZipCode: str
        :param RegistrantType: 用户类型 E:组织， I:个人
        :type RegistrantType: str
        :param Province: 省份（英文）。作为入参时可以不填
        :type Province: str
        :param City: 城市（英文）。作为入参时可以不填
        :type City: str
        :param Country: 国家（英文）。作为入参时可以不填
        :type Country: str
        """
        self.OrganizationNameCN = None
        self.OrganizationName = None
        self.RegistrantNameCN = None
        self.RegistrantName = None
        self.ProvinceCN = None
        self.CityCN = None
        self.StreetCN = None
        self.Street = None
        self.CountryCN = None
        self.Telephone = None
        self.Email = None
        self.ZipCode = None
        self.RegistrantType = None
        self.Province = None
        self.City = None
        self.Country = None


    def _deserialize(self, params):
        self.OrganizationNameCN = params.get("OrganizationNameCN")
        self.OrganizationName = params.get("OrganizationName")
        self.RegistrantNameCN = params.get("RegistrantNameCN")
        self.RegistrantName = params.get("RegistrantName")
        self.ProvinceCN = params.get("ProvinceCN")
        self.CityCN = params.get("CityCN")
        self.StreetCN = params.get("StreetCN")
        self.Street = params.get("Street")
        self.CountryCN = params.get("CountryCN")
        self.Telephone = params.get("Telephone")
        self.Email = params.get("Email")
        self.ZipCode = params.get("ZipCode")
        self.RegistrantType = params.get("RegistrantType")
        self.Province = params.get("Province")
        self.City = params.get("City")
        self.Country = params.get("Country")


class CreateDomainBatchRequest(AbstractModel):
    """CreateDomainBatch请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param Period: 购买域名的年限，可选值：[1-10]
        :type Period: int
        :param Domains: 批量购买的域名,最多为4000个
        :type Domains: list of str
        :param PayMode: 付费模式 0手动在线付费，1使用余额付费
        :type PayMode: int
        """
        self.TemplateId = None
        self.Period = None
        self.Domains = None
        self.PayMode = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Period = params.get("Period")
        self.Domains = params.get("Domains")
        self.PayMode = params.get("PayMode")


class CreateDomainBatchResponse(AbstractModel):
    """CreateDomainBatch返回参数结构体

    """

    def __init__(self):
        """
        :param LogId: 批量日志ID
注意：此字段可能返回 null，表示取不到有效值。
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class DescribeDomainBaseInfoRequest(AbstractModel):
    """DescribeDomainBaseInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class DescribeDomainBaseInfoResponse(AbstractModel):
    """DescribeDomainBaseInfo返回参数结构体

    """

    def __init__(self):
        """
        :param DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.domain.v20180808.models.DomainBaseInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainBaseInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.RequestId = params.get("RequestId")


class DescribeDomainNameListRequest(AbstractModel):
    """DescribeDomainNameList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，取值范围[1,100]
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeDomainNameListResponse(AbstractModel):
    """DescribeDomainNameList返回参数结构体

    """

    def __init__(self):
        """
        :param DomainSet: 域名信息集合
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainSet: list of DomainList
        :param TotalCount: 域名总数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainSet") is not None:
            self.DomainSet = []
            for item in params.get("DomainSet"):
                obj = DomainList()
                obj._deserialize(item)
                self.DomainSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDomainPriceListRequest(AbstractModel):
    """DescribeDomainPriceList请求参数结构体

    """

    def __init__(self):
        """
        :param TldList: 查询价格的后缀列表。默认则为全部后缀
        :type TldList: list of str
        :param Year: 查询购买的年份，默认会列出所有年份的价格
        :type Year: list of int
        :param Operation: 域名的购买类型：new  新购，renew 续费，redem 赎回，tran 转入
        :type Operation: list of str
        """
        self.TldList = None
        self.Year = None
        self.Operation = None


    def _deserialize(self, params):
        self.TldList = params.get("TldList")
        self.Year = params.get("Year")
        self.Operation = params.get("Operation")


class DescribeDomainPriceListResponse(AbstractModel):
    """DescribeDomainPriceList返回参数结构体

    """

    def __init__(self):
        """
        :param PriceList: 域名价格列表
        :type PriceList: list of PriceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PriceList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PriceList") is not None:
            self.PriceList = []
            for item in params.get("PriceList"):
                obj = PriceInfo()
                obj._deserialize(item)
                self.PriceList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTemplateListRequest(AbstractModel):
    """DescribeTemplateList请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Type: 用户注册类型，默认:all , 个人：I ,企业: E
        :type Type: str
        :param Status: 认证状态：未实名认证:NotUpload, 实名审核中:InAudit，已实名认证:Approved，实名审核失败:Reject
        :type Status: str
        """
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.Status = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.Status = params.get("Status")


class DescribeTemplateListResponse(AbstractModel):
    """DescribeTemplateList返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 模板数量。
        :type TotalCount: int
        :param TemplateSet: 模板详细信息列表。
        :type TemplateSet: list of TemplateInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TemplateSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TemplateSet") is not None:
            self.TemplateSet = []
            for item in params.get("TemplateSet"):
                obj = TemplateInfo()
                obj._deserialize(item)
                self.TemplateSet.append(obj)
        self.RequestId = params.get("RequestId")


class DomainBaseInfo(AbstractModel):
    """获取域名基础信息

    """

    def __init__(self):
        """
        :param DomainId: 域名资源ID。
        :type DomainId: str
        :param DomainName: 域名名称。
        :type DomainName: str
        :param RealNameAuditStatus: 域名实名认证状态。
NotUpload：未实名认证
InAudit：实名审核中
Approved：实名审核通过
Reject：实名审核失败
        :type RealNameAuditStatus: str
        :param RealNameAuditUnpassReason: 域名实名认证不通过原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealNameAuditUnpassReason: str
        :param DomainNameAuditStatus: 域名命名审核状态。
NotAudit：命名审核未上传
Pending：命名审核待上传
Auditing：域名命名审核中
Approved：域名命名审核通过
Rejected：域名命名审核拒绝
        :type DomainNameAuditStatus: str
        :param DomainNameAuditUnpassReason: 域名命名审核不通过原因。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainNameAuditUnpassReason: str
        :param CreationDate: 注册时间。
        :type CreationDate: str
        :param ExpirationDate: 到期时间
        :type ExpirationDate: str
        :param DomainStatus: 域名状态。
ok：正常
serverHold：注册局暂停解析 
clientHold：注册商暂停解析
pendingTransfer：转移中
renewingPeriod：续费期
redemptionPeriod：偿还期
pendingDelete：删除期
serverTransferProhibited：注册局禁止转移
serverUpdateProhibited：注册局禁止更新
serverDeleteProhibited：注册局禁止删除
clientTransferProhibited：注册商禁止转移
clientUpdateProhibited：注册商禁止更新
clientDeleteProhibited：注册商禁止删除
        :type DomainStatus: list of str
        :param BuyStatus: 域名购买状态。
ok：正常
RegisterPending：待注册
RegisterDoing：注册中
RegisterFailed：注册失败
AboutToExpire: 即将过期
RenewPending：已进入续费期，需要进行续费
RenewDoing：续费中
RedemptionPending：已进入赎回期，需要进行续费
RedemptionDoing：赎回中
TransferPending：待转入中
TransferTransing：转入中
TransferFailed：转入失败
        :type BuyStatus: str
        :param RegistrarType: 注册类型
epp （腾讯云自有域名）
xinnet (新网域名)
        :type RegistrarType: str
        """
        self.DomainId = None
        self.DomainName = None
        self.RealNameAuditStatus = None
        self.RealNameAuditUnpassReason = None
        self.DomainNameAuditStatus = None
        self.DomainNameAuditUnpassReason = None
        self.CreationDate = None
        self.ExpirationDate = None
        self.DomainStatus = None
        self.BuyStatus = None
        self.RegistrarType = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.DomainName = params.get("DomainName")
        self.RealNameAuditStatus = params.get("RealNameAuditStatus")
        self.RealNameAuditUnpassReason = params.get("RealNameAuditUnpassReason")
        self.DomainNameAuditStatus = params.get("DomainNameAuditStatus")
        self.DomainNameAuditUnpassReason = params.get("DomainNameAuditUnpassReason")
        self.CreationDate = params.get("CreationDate")
        self.ExpirationDate = params.get("ExpirationDate")
        self.DomainStatus = params.get("DomainStatus")
        self.BuyStatus = params.get("BuyStatus")
        self.RegistrarType = params.get("RegistrarType")


class DomainList(AbstractModel):
    """域名列表

    """

    def __init__(self):
        """
        :param IsPremium: 是否是溢价域名：
ture 是    
false 不是
        :type IsPremium: bool
        :param DomainId: 域名资源ID。
        :type DomainId: str
        :param DomainName: 域名名称。
        :type DomainName: str
        :param AutoRenew: 是否已设置自动续费 。
0：未设置 
1：已设置
        :type AutoRenew: int
        :param CreationDate: 注册时间。
        :type CreationDate: str
        :param ExpirationDate: 到期时间。
        :type ExpirationDate: str
        :param Tld: 域名后缀
        :type Tld: str
        :param CodeTld: 编码后的后缀（中文会进行编码）
        :type CodeTld: str
        :param BuyStatus: 域名购买状态。
ok：正常
AboutToExpire: 即将到期
RegisterPending：注册中
RegisterDoing：注册中
RegisterFailed：注册失败
RenewPending：续费期
RenewDoing：续费中
RedemptionPending：赎回期
RedemptionDoing：赎回中
TransferPending：转入中
TransferTransing：转入中
TransferFailed：转入失败
        :type BuyStatus: str
        """
        self.IsPremium = None
        self.DomainId = None
        self.DomainName = None
        self.AutoRenew = None
        self.CreationDate = None
        self.ExpirationDate = None
        self.Tld = None
        self.CodeTld = None
        self.BuyStatus = None


    def _deserialize(self, params):
        self.IsPremium = params.get("IsPremium")
        self.DomainId = params.get("DomainId")
        self.DomainName = params.get("DomainName")
        self.AutoRenew = params.get("AutoRenew")
        self.CreationDate = params.get("CreationDate")
        self.ExpirationDate = params.get("ExpirationDate")
        self.Tld = params.get("Tld")
        self.CodeTld = params.get("CodeTld")
        self.BuyStatus = params.get("BuyStatus")


class PriceInfo(AbstractModel):
    """域名价格信息

    """

    def __init__(self):
        """
        :param Tld: 域名后缀，例如.com
        :type Tld: str
        :param Year: 购买年限，范围[1-10]
        :type Year: int
        :param Price: 域名原价
        :type Price: int
        :param RealPrice: 域名现价
        :type RealPrice: int
        :param Operation: 商品的购买类型，新购，续费，赎回，转入，续费并转入
        :type Operation: str
        """
        self.Tld = None
        self.Year = None
        self.Price = None
        self.RealPrice = None
        self.Operation = None


    def _deserialize(self, params):
        self.Tld = params.get("Tld")
        self.Year = params.get("Year")
        self.Price = params.get("Price")
        self.RealPrice = params.get("RealPrice")
        self.Operation = params.get("Operation")


class TemplateInfo(AbstractModel):
    """Template数据

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param AuditStatus: 认证状态
        :type AuditStatus: str
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param UpdatedOn: 更新时间
        :type UpdatedOn: str
        :param UserUin: 用户UIN
        :type UserUin: str
        :param IsDefault: 是否是默认模板
        :type IsDefault: str
        :param AuditReason: 认证失败原因
        :type AuditReason: str
        :param CertificateInfo: 认证信息
        :type CertificateInfo: :class:`tencentcloud.domain.v20180808.models.CertificateInfo`
        :param ContactInfo: 联系人信息
        :type ContactInfo: :class:`tencentcloud.domain.v20180808.models.ContactInfo`
        :param IsValidTemplate: 模板是否符合规范， 1是 0 否
        :type IsValidTemplate: int
        :param InvalidReason: 不符合规范原因
        :type InvalidReason: str
        """
        self.TemplateId = None
        self.AuditStatus = None
        self.CreatedOn = None
        self.UpdatedOn = None
        self.UserUin = None
        self.IsDefault = None
        self.AuditReason = None
        self.CertificateInfo = None
        self.ContactInfo = None
        self.IsValidTemplate = None
        self.InvalidReason = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.AuditStatus = params.get("AuditStatus")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        self.UserUin = params.get("UserUin")
        self.IsDefault = params.get("IsDefault")
        self.AuditReason = params.get("AuditReason")
        if params.get("CertificateInfo") is not None:
            self.CertificateInfo = CertificateInfo()
            self.CertificateInfo._deserialize(params.get("CertificateInfo"))
        if params.get("ContactInfo") is not None:
            self.ContactInfo = ContactInfo()
            self.ContactInfo._deserialize(params.get("ContactInfo"))
        self.IsValidTemplate = params.get("IsValidTemplate")
        self.InvalidReason = params.get("InvalidReason")