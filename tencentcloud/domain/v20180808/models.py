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


class BatchModifyDomainInfoRequest(AbstractModel):
    """BatchModifyDomainInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domains: 批量修改的域名。
        :type Domains: list of str
        :param TemplateId: 模板ID。
        :type TemplateId: str
        :param LockTransfer: true： 开启60天内禁止转移注册商锁定
false：关闭60天内禁止转移注册商锁定
默认 true
        :type LockTransfer: bool
        """
        self.Domains = None
        self.TemplateId = None
        self.LockTransfer = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.TemplateId = params.get("TemplateId")
        self.LockTransfer = params.get("LockTransfer")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BatchModifyDomainInfoResponse(AbstractModel):
    """BatchModifyDomainInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class BatchStatus(AbstractModel):
    """批量任务状态

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateInfo(AbstractModel):
    """认证资料信息

    """

    def __init__(self):
        r"""
        :param CertificateCode: 证件号码。
        :type CertificateCode: str
        :param CertificateType: 证件类型。
SFZ: 身份证。
HZ: 护照。
TXZ: 中国港澳居民来往内地通行证。
TWSFZ: 中国台湾居民来往大陆通行证。
GWSFZ: 外国人永久居留身份证。
ORG: 组织机构代码证
YYZZ: 工商营业执照。
TYDMZ: 统一社会信用代码证书。
BDDH: 部队代号
JDXKZ: 军队单位对外有偿服务许可证。
SYZS: 事业单位法定代表人证书。
GWCZDJZ: 外国企业常驻代表机构登记证。
STDJZ: 社会团体法定代表人登记证书。
ZJDJZ: 宗教活动场所登记证。
MBDJZ: 民办非企业单位登记证书。
JJDJZ: 基金会法定代表人登记证书。
LSXKZ: 律师事务所执业许可证。
GWZHDJZ: 外国在华文化中心登记证。
GWLYDJZ: 外国政府旅游部门常驻代表机构批准登记证。
SFXKZ: 司法鉴定许可证
GWJGZJ: 外国机构证件。
SHFWJGZ: 社会服务机构登记证书。
MBXXXKZ: 民办学校办学许可证。
YLJGXKZ: 医疗机构执业许可证。
GAJZZ: 中国港澳居住证。
TWJZZ: 中国台湾居住证。
QTTYDM: 其他-统一社会信用代码证书。
GZJGZY: 公证机构执业证。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBatchStatusRequest(AbstractModel):
    """CheckBatchStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogIds: 操作日志 ID数组，最多 200 个
        :type LogIds: list of int non-negative
        """
        self.LogIds = None


    def _deserialize(self, params):
        self.LogIds = params.get("LogIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckBatchStatusResponse(AbstractModel):
    """CheckBatchStatus返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
        :param DomainName: 所查询域名名称
        :type DomainName: str
        :param Period: 年限。该参数为空时无法查询溢价词域名
        :type Period: str
        """
        self.DomainName = None
        self.Period = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        self.Period = params.get("Period")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckDomainResponse(AbstractModel):
    """CheckDomain返回参数结构体

    """

    def __init__(self):
        r"""
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
        :param RealPrice: 域名真实价格, 溢价词时价格跟年限有关，非溢价词时价格为1年的价格
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchRequest(AbstractModel):
    """CreateDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID。详情请查看：[获取模板列表](https://cloud.tencent.com/document/product/242/48940)
        :type TemplateId: str
        :param Period: 购买域名的年限，可选值：[1-10]
        :type Period: int
        :param Domains: 批量购买的域名,最多为4000个
        :type Domains: list of str
        :param PayMode: 付费模式 0手动在线付费，1使用余额付费，2使用特惠包
        :type PayMode: int
        :param AutoRenewFlag: 自动续费开关。有两个可选值：
0 表示关闭，不自动续费（默认值）
1 表示开启，将自动续费
        :type AutoRenewFlag: int
        :param PackageResourceId: 使用的特惠包ID，PayMode为2时必填
        :type PackageResourceId: str
        :param UpdateProhibition: 是否开启更新锁：0=默认不开启，1=开启
        :type UpdateProhibition: int
        :param TransferProhibition: 是否开启转移锁：0=默认不开启，1=开启
        :type TransferProhibition: int
        """
        self.TemplateId = None
        self.Period = None
        self.Domains = None
        self.PayMode = None
        self.AutoRenewFlag = None
        self.PackageResourceId = None
        self.UpdateProhibition = None
        self.TransferProhibition = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Period = params.get("Period")
        self.Domains = params.get("Domains")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PackageResourceId = params.get("PackageResourceId")
        self.UpdateProhibition = params.get("UpdateProhibition")
        self.TransferProhibition = params.get("TransferProhibition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainBatchResponse(AbstractModel):
    """CreateDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
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


class CreatePhoneEmailRequest(AbstractModel):
    """CreatePhoneEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Code: 手机号或者邮箱
        :type Code: str
        :param Type: 1：手机   2：邮箱
        :type Type: int
        :param VerifyCode: 验证码
        :type VerifyCode: str
        """
        self.Code = None
        self.Type = None
        self.VerifyCode = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.VerifyCode = params.get("VerifyCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreatePhoneEmailResponse(AbstractModel):
    """CreatePhoneEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateTemplateRequest(AbstractModel):
    """CreateTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ContactInfo: 联系人信息
        :type ContactInfo: :class:`tencentcloud.domain.v20180808.models.ContactInfo`
        :param CertificateInfo: 证件信息
        :type CertificateInfo: :class:`tencentcloud.domain.v20180808.models.CertificateInfo`
        """
        self.ContactInfo = None
        self.CertificateInfo = None


    def _deserialize(self, params):
        if params.get("ContactInfo") is not None:
            self.ContactInfo = ContactInfo()
            self.ContactInfo._deserialize(params.get("ContactInfo"))
        if params.get("CertificateInfo") is not None:
            self.CertificateInfo = CertificateInfo()
            self.CertificateInfo._deserialize(params.get("CertificateInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTemplateResponse(AbstractModel):
    """CreateTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Template: 模板信息
        :type Template: :class:`tencentcloud.domain.v20180808.models.TemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DeletePhoneEmailRequest(AbstractModel):
    """DeletePhoneEmail请求参数结构体

    """

    def __init__(self):
        r"""
        :param Code: 手机或者邮箱
        :type Code: str
        :param Type: 1：手机  2：邮箱
        :type Type: int
        """
        self.Code = None
        self.Type = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeletePhoneEmailResponse(AbstractModel):
    """DeletePhoneEmail返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteTemplateRequest(AbstractModel):
    """DeleteTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteTemplateResponse(AbstractModel):
    """DeleteTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBatchOperationLogDetailsRequest(AbstractModel):
    """DescribeBatchOperationLogDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID。
        :type LogId: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为200。
        :type Limit: int
        """
        self.LogId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchOperationLogDetailsResponse(AbstractModel):
    """DescribeBatchOperationLogDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量。
        :type TotalCount: int
        :param DomainBatchDetailSet: 日志详情列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainBatchDetailSet: list of DomainBatchDetailSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DomainBatchDetailSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainBatchDetailSet") is not None:
            self.DomainBatchDetailSet = []
            for item in params.get("DomainBatchDetailSet"):
                obj = DomainBatchDetailSet()
                obj._deserialize(item)
                self.DomainBatchDetailSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBatchOperationLogsRequest(AbstractModel):
    """DescribeBatchOperationLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为200。
        :type Limit: int
        """
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBatchOperationLogsResponse(AbstractModel):
    """DescribeBatchOperationLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 总数量
        :type TotalCount: int
        :param DomainBatchLogSet: 日志列表
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainBatchLogSet: list of DomainBatchLogSet
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DomainBatchLogSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DomainBatchLogSet") is not None:
            self.DomainBatchLogSet = []
            for item in params.get("DomainBatchLogSet"):
                obj = DomainBatchLogSet()
                obj._deserialize(item)
                self.DomainBatchLogSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainBaseInfoRequest(AbstractModel):
    """DescribeDomainBaseInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domain: 域名
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainBaseInfoResponse(AbstractModel):
    """DescribeDomainBaseInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.domain.v20180808.models.DomainBaseInfo`
        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。
        :type Uin: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainBaseInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class DescribeDomainNameListRequest(AbstractModel):
    """DescribeDomainNameList请求参数结构体

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainNameListResponse(AbstractModel):
    """DescribeDomainNameList返回参数结构体

    """

    def __init__(self):
        r"""
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
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainPriceListResponse(AbstractModel):
    """DescribeDomainPriceList返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeDomainSimpleInfoRequest(AbstractModel):
    """DescribeDomainSimpleInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainName: 域名
        :type DomainName: str
        """
        self.DomainName = None


    def _deserialize(self, params):
        self.DomainName = params.get("DomainName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainSimpleInfoResponse(AbstractModel):
    """DescribeDomainSimpleInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainInfo: 域名信息
        :type DomainInfo: :class:`tencentcloud.domain.v20180808.models.DomainSimpleInfo`
        :param Uin: 账号ID
        :type Uin: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainInfo = None
        self.Uin = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainInfo") is not None:
            self.DomainInfo = DomainSimpleInfo()
            self.DomainInfo._deserialize(params.get("DomainInfo"))
        self.Uin = params.get("Uin")
        self.RequestId = params.get("RequestId")


class DescribePhoneEmailListRequest(AbstractModel):
    """DescribePhoneEmailList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Type: 0：所有类型  1：手机  2：邮箱，默认0
        :type Type: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为20，取值范围[1,200]
        :type Limit: int
        :param Code: 手机或者邮箱精确搜索
        :type Code: str
        """
        self.Type = None
        self.Offset = None
        self.Limit = None
        self.Code = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePhoneEmailListResponse(AbstractModel):
    """DescribePhoneEmailList返回参数结构体

    """

    def __init__(self):
        r"""
        :param PhoneEmailList: 手机或者邮箱列表
        :type PhoneEmailList: list of PhoneEmailData
        :param TotalCount: 总数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PhoneEmailList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PhoneEmailList") is not None:
            self.PhoneEmailList = []
            for item in params.get("PhoneEmailList"):
                obj = PhoneEmailData()
                obj._deserialize(item)
                self.PhoneEmailList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeTemplateListRequest(AbstractModel):
    """DescribeTemplateList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Type: 用户注册类型，默认:all , 个人：I ,企业: E
        :type Type: str
        :param Status: 认证状态：未实名审核:NotUpload, 实名审核中:InAudit，已实名审核:Approved，实名审核失败:Reject，更新手机邮箱:NotVerified。
        :type Status: str
        :param Keyword: 域名所有者筛选
        :type Keyword: str
        """
        self.Offset = None
        self.Limit = None
        self.Type = None
        self.Status = None
        self.Keyword = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Type = params.get("Type")
        self.Status = params.get("Status")
        self.Keyword = params.get("Keyword")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateListResponse(AbstractModel):
    """DescribeTemplateList返回参数结构体

    """

    def __init__(self):
        r"""
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


class DescribeTemplateRequest(AbstractModel):
    """DescribeTemplate请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        """
        self.TemplateId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTemplateResponse(AbstractModel):
    """DescribeTemplate返回参数结构体

    """

    def __init__(self):
        r"""
        :param Template: 模板信息
        :type Template: :class:`tencentcloud.domain.v20180808.models.TemplateInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DomainBaseInfo(AbstractModel):
    """获取域名基础信息

    """

    def __init__(self):
        r"""
        :param DomainId: 域名资源ID。
        :type DomainId: str
        :param DomainName: 域名名称。
        :type DomainName: str
        :param RealNameAuditStatus: 域名实名认证状态。
NotUpload：未实名认证
InAudit：实名审核中
Approved：实名审核通过
Reject：实名审核失败
NoAudit: 无需实名认证
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
        :param RegistrarType: 注册商类型
epp: DNSPod, Inc.（烟台帝思普网络科技有限公司）
qcloud: Tencent Cloud Computing (Beijing) Limited Liability Company（腾讯云计算（北京）有限责任公司）
yunxun: Guangzhou Yunxun Information Technology Co., Ltd.（广州云讯信息科技有限公司）
xinnet: Xin Net Technology Corporation（北京新网数码信息技术有限公司）
        :type RegistrarType: str
        :param NameServer: 域名绑定的ns
        :type NameServer: list of str
        :param LockTransfer: true：开启锁定
false：关闭锁定
        :type LockTransfer: bool
        :param LockEndTime: 锁定结束时间
        :type LockEndTime: str
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
        self.NameServer = None
        self.LockTransfer = None
        self.LockEndTime = None


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
        self.NameServer = params.get("NameServer")
        self.LockTransfer = params.get("LockTransfer")
        self.LockEndTime = params.get("LockEndTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainBatchDetailSet(AbstractModel):
    """批量操作日志详情

    """

    def __init__(self):
        r"""
        :param Id: 详情ID
        :type Id: int
        :param Domain: 域名
        :type Domain: str
        :param Status: 执行状态：
doing 执行中。
failed 操作失败。
success  操作成功。
        :type Status: str
        :param Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。
        :type Reason: str
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param UpdatedOn: 更新时间
        :type UpdatedOn: str
        """
        self.Id = None
        self.Domain = None
        self.Status = None
        self.Reason = None
        self.CreatedOn = None
        self.UpdatedOn = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Status = params.get("Status")
        self.Reason = params.get("Reason")
        self.CreatedOn = params.get("CreatedOn")
        self.UpdatedOn = params.get("UpdatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainBatchLogSet(AbstractModel):
    """批量操作记录

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID
        :type LogId: int
        :param Number: 数量
        :type Number: int
        :param Status: 执行状态：
doing 执行中。
done 执行完成。
        :type Status: str
        :param CreatedOn: 提交时间
        :type CreatedOn: str
        """
        self.LogId = None
        self.Number = None
        self.Status = None
        self.CreatedOn = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.Number = params.get("Number")
        self.Status = params.get("Status")
        self.CreatedOn = params.get("CreatedOn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainList(AbstractModel):
    """域名列表

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainSimpleInfo(AbstractModel):
    """获取域名基础模板信息

    """

    def __init__(self):
        r"""
        :param DomainId: 域名资源ID。
        :type DomainId: str
        :param DomainName: 域名名称。
        :type DomainName: str
        :param RealNameAuditStatus: 域名实名认证状态。
NotUpload：未实名认证
InAudit：实名审核中
Approved：实名审核通过
Reject：实名审核失败
NoAudit: 无需实名认证
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
        :param RegistrarType: 注册商类型
epp: DNSPod, Inc.（烟台帝思普网络科技有限公司）
qcloud: Tencent Cloud Computing (Beijing) Limited Liability Company（腾讯云计算（北京）有限责任公司）
yunxun: Guangzhou Yunxun Information Technology Co., Ltd.（广州云讯信息科技有限公司）
xinnet: Xin Net Technology Corporation（北京新网数码信息技术有限公司）
        :type RegistrarType: str
        :param NameServer: 域名绑定的ns
        :type NameServer: list of str
        :param LockTransfer: true：开启锁定
false：关闭锁定
        :type LockTransfer: bool
        :param LockEndTime: 锁定结束时间
        :type LockEndTime: str
        :param RegistrantType: 认证类型：I=个人，E=企业
        :type RegistrantType: str
        :param OrganizationNameCN: 域名所有者，中文
        :type OrganizationNameCN: str
        :param OrganizationName: 域名所有者，英文
        :type OrganizationName: str
        :param RegistrantNameCN: 域名联系人，中文
        :type RegistrantNameCN: str
        :param RegistrantName: 域名联系人，英文
        :type RegistrantName: str
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
        self.NameServer = None
        self.LockTransfer = None
        self.LockEndTime = None
        self.RegistrantType = None
        self.OrganizationNameCN = None
        self.OrganizationName = None
        self.RegistrantNameCN = None
        self.RegistrantName = None


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
        self.NameServer = params.get("NameServer")
        self.LockTransfer = params.get("LockTransfer")
        self.LockEndTime = params.get("LockEndTime")
        self.RegistrantType = params.get("RegistrantType")
        self.OrganizationNameCN = params.get("OrganizationNameCN")
        self.OrganizationName = params.get("OrganizationName")
        self.RegistrantNameCN = params.get("RegistrantNameCN")
        self.RegistrantName = params.get("RegistrantName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainDNSBatchRequest(AbstractModel):
    """ModifyDomainDNSBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domains: 批量操作的域名。
        :type Domains: list of str
        :param Dns: 域名DNS 数组。
        :type Dns: list of str
        """
        self.Domains = None
        self.Dns = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Dns = params.get("Dns")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainDNSBatchResponse(AbstractModel):
    """ModifyDomainDNSBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID。
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class ModifyDomainOwnerBatchRequest(AbstractModel):
    """ModifyDomainOwnerBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domains: 要过户的域名。
        :type Domains: list of str
        :param NewOwnerUin: 转入账户的uin。
        :type NewOwnerUin: str
        :param TransferDns: 是否同时转移对应的 DNS 解析域名，默认false
        :type TransferDns: bool
        :param NewOwnerAppId: 转入账户的appid。
        :type NewOwnerAppId: str
        """
        self.Domains = None
        self.NewOwnerUin = None
        self.TransferDns = None
        self.NewOwnerAppId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.NewOwnerUin = params.get("NewOwnerUin")
        self.TransferDns = params.get("TransferDns")
        self.NewOwnerAppId = params.get("NewOwnerAppId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainOwnerBatchResponse(AbstractModel):
    """ModifyDomainOwnerBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志id
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class PhoneEmailData(AbstractModel):
    """手机号邮箱列表

    """

    def __init__(self):
        r"""
        :param Code: 手机号或者邮箱
        :type Code: str
        :param Type: 1：手机  2：邮箱
        :type Type: int
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param CheckStatus: 1=控制台校验，2=第三方校验
        :type CheckStatus: int
        """
        self.Code = None
        self.Type = None
        self.CreatedOn = None
        self.CheckStatus = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        self.CreatedOn = params.get("CreatedOn")
        self.CheckStatus = params.get("CheckStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PriceInfo(AbstractModel):
    """域名价格信息

    """

    def __init__(self):
        r"""
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDomainBatchRequest(AbstractModel):
    """RenewDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param Period: 域名续费的年限。
        :type Period: int
        :param Domains: 批量续费的域名。
        :type Domains: list of str
        :param PayMode: 付费模式 0手动在线付费，1使用余额付费。
        :type PayMode: int
        :param AutoRenewFlag: 自动续费开关。有三个可选值：
0 表示关闭，不自动续费
1 表示开启，将自动续费
2 表示不处理，保留域名原有状态（默认值）
        :type AutoRenewFlag: int
        """
        self.Period = None
        self.Domains = None
        self.PayMode = None
        self.AutoRenewFlag = None


    def _deserialize(self, params):
        self.Period = params.get("Period")
        self.Domains = params.get("Domains")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RenewDomainBatchResponse(AbstractModel):
    """RenewDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 操作日志ID。
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class SendPhoneEmailCodeRequest(AbstractModel):
    """SendPhoneEmailCode请求参数结构体

    """

    def __init__(self):
        r"""
        :param Code: 手机或者邮箱号。
        :type Code: str
        :param Type: 1：手机  2：邮箱。
        :type Type: int
        """
        self.Code = None
        self.Type = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        self.Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SendPhoneEmailCodeResponse(AbstractModel):
    """SendPhoneEmailCode返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SetDomainAutoRenewRequest(AbstractModel):
    """SetDomainAutoRenew请求参数结构体

    """

    def __init__(self):
        r"""
        :param DomainId: 域名ID。
        :type DomainId: str
        :param AutoRenew: AutoRenew 有三个可选值：
 0：不设置自动续费
1：设置自动续费
2：设置到期后不续费
        :type AutoRenew: int
        """
        self.DomainId = None
        self.AutoRenew = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")
        self.AutoRenew = params.get("AutoRenew")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetDomainAutoRenewResponse(AbstractModel):
    """SetDomainAutoRenew返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TemplateInfo(AbstractModel):
    """Template数据

    """

    def __init__(self):
        r"""
        :param TemplateId: 模板ID
        :type TemplateId: str
        :param AuditStatus: 认证状态：未实名认证:NotUpload, 实名审核中:InAudit，已实名认证:Approved，实名审核失败:Reject
        :type AuditStatus: str
        :param CreatedOn: 创建时间
        :type CreatedOn: str
        :param UpdatedOn: 更新时间
        :type UpdatedOn: str
        :param UserUin: 用户UIN
        :type UserUin: str
        :param IsDefault: 是否是默认模板: 是:yes，否:no
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferInDomainBatchRequest(AbstractModel):
    """TransferInDomainBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domains: 转入的域名名称数组。
        :type Domains: list of str
        :param PassWords: 域名转移码数组。
        :type PassWords: list of str
        :param TemplateId: 模板ID。
        :type TemplateId: str
        :param PayMode: 付费模式 0手动在线付费，1使用余额付费。
        :type PayMode: int
        :param AutoRenewFlag: 自动续费开关。有两个可选值：
0 表示关闭，不自动续费（默认值）
1 表示开启，将自动续费
        :type AutoRenewFlag: int
        :param LockTransfer: true： 开启60天内禁止转移注册商锁定
false：关闭60天内禁止转移注册商锁定
默认 true
        :type LockTransfer: bool
        :param UpdateProhibition: 是否开启更新锁：0=默认不开启，1=开启
        :type UpdateProhibition: int
        :param TransferProhibition: 是否开启转移锁：0=默认不开启，1=开启
        :type TransferProhibition: int
        """
        self.Domains = None
        self.PassWords = None
        self.TemplateId = None
        self.PayMode = None
        self.AutoRenewFlag = None
        self.LockTransfer = None
        self.UpdateProhibition = None
        self.TransferProhibition = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.PassWords = params.get("PassWords")
        self.TemplateId = params.get("TemplateId")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.LockTransfer = params.get("LockTransfer")
        self.UpdateProhibition = params.get("UpdateProhibition")
        self.TransferProhibition = params.get("TransferProhibition")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferInDomainBatchResponse(AbstractModel):
    """TransferInDomainBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class TransferProhibitionBatchRequest(AbstractModel):
    """TransferProhibitionBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domains: 批量操作的域名。
        :type Domains: list of str
        :param Status: 是否开启禁止域名转移。
True: 开启禁止域名转移状态。
False：关闭禁止域名转移状态。
        :type Status: bool
        """
        self.Domains = None
        self.Status = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TransferProhibitionBatchResponse(AbstractModel):
    """TransferProhibitionBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class UpdateProhibitionBatchRequest(AbstractModel):
    """UpdateProhibitionBatch请求参数结构体

    """

    def __init__(self):
        r"""
        :param Domains: 批量操作的域名。
        :type Domains: list of str
        :param Status: 是否开启禁止域名更新。
True:开启禁止域名更新状态。
False：关闭禁止域名更新状态。
        :type Status: bool
        """
        self.Domains = None
        self.Status = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateProhibitionBatchResponse(AbstractModel):
    """UpdateProhibitionBatch返回参数结构体

    """

    def __init__(self):
        r"""
        :param LogId: 日志ID
        :type LogId: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class UploadImageRequest(AbstractModel):
    """UploadImage请求参数结构体

    """

    def __init__(self):
        r"""
        :param ImageFile: 资质照片，照片的base64编码。
        :type ImageFile: str
        """
        self.ImageFile = None


    def _deserialize(self, params):
        self.ImageFile = params.get("ImageFile")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UploadImageResponse(AbstractModel):
    """UploadImage返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessUrl: 资质照片地址。
        :type AccessUrl: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessUrl = params.get("AccessUrl")
        self.RequestId = params.get("RequestId")