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
        """
        :param Domains: 批量修改的域名。\n        :type Domains: list of str\n        :param TemplateId: 模板ID。\n        :type TemplateId: str\n        :param LockTransfer: true： 开启60天内禁止转移注册商锁定
false：关闭60天内禁止转移注册商锁定
默认 true\n        :type LockTransfer: bool\n        """
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
        """
        :param LogId: 日志ID\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class BatchStatus(AbstractModel):
    """批量任务状态

    """

    def __init__(self):
        """
        :param LogId: 批量任务id\n        :type LogId: int\n        :param Status: 批量任务状态  doing：进行中  success：成功  failed：失败  partial_success：部分成功\n        :type Status: str\n        :param BatchAction: 批量任务类型\n        :type BatchAction: str\n        """
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
        """
        :param CertificateCode: 证件号码。\n        :type CertificateCode: str\n        :param CertificateType: 证件类型。
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
GZJGZY: 公证机构执业证。\n        :type CertificateType: str\n        :param ImgUrl: 证件照片地址。\n        :type ImgUrl: str\n        """
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
        """
        :param LogIds: 操作日志 ID数组，最多 200 个\n        :type LogIds: list of int non-negative\n        """
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
        """
        :param StatusSet: 批量任务状态集\n        :type StatusSet: list of BatchStatus\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param DomainName: 所查询域名名称\n        :type DomainName: str\n        :param Period: 年限。该参数为空时无法查询溢价词域名\n        :type Period: str\n        """
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
        """
        :param DomainName: 所查询域名名称\n        :type DomainName: str\n        :param Available: 是否能够注册\n        :type Available: bool\n        :param Reason: 不能注册原因\n        :type Reason: str\n        :param Premium: 是否是溢价词\n        :type Premium: bool\n        :param Price: 域名价格\n        :type Price: int\n        :param BlackWord: 是否是敏感词\n        :type BlackWord: bool\n        :param Describe: 溢价词描述
注意：此字段可能返回 null，表示取不到有效值。\n        :type Describe: str\n        :param FeeRenew: 溢价词的续费价格
注意：此字段可能返回 null，表示取不到有效值。\n        :type FeeRenew: int\n        :param RealPrice: 域名真实价格, 溢价词时价格跟年限有关，非溢价词时价格为1年的价格
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealPrice: int\n        :param FeeTransfer: 溢价词的转入价格
注意：此字段可能返回 null，表示取不到有效值。\n        :type FeeTransfer: int\n        :param FeeRestore: 溢价词的赎回价格\n        :type FeeRestore: int\n        :param Period: 检测年限\n        :type Period: int\n        :param RecordSupport: 是否支持北京备案  true 支持  false 不支持\n        :type RecordSupport: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param OrganizationNameCN: 注册人（中文）\n        :type OrganizationNameCN: str\n        :param OrganizationName: 注册人（英文）\n        :type OrganizationName: str\n        :param RegistrantNameCN: 联系人（中文）\n        :type RegistrantNameCN: str\n        :param RegistrantName: 联系人（英文）\n        :type RegistrantName: str\n        :param ProvinceCN: 省份（中文）\n        :type ProvinceCN: str\n        :param CityCN: 城市（中文）\n        :type CityCN: str\n        :param StreetCN: 街道（中文）\n        :type StreetCN: str\n        :param Street: 街道（英文）\n        :type Street: str\n        :param CountryCN: 国家（中文）\n        :type CountryCN: str\n        :param Telephone: 联系人手机号\n        :type Telephone: str\n        :param Email: 联系人邮箱\n        :type Email: str\n        :param ZipCode: 邮编\n        :type ZipCode: str\n        :param RegistrantType: 用户类型 E:组织， I:个人\n        :type RegistrantType: str\n        :param Province: 省份（英文）。作为入参时可以不填\n        :type Province: str\n        :param City: 城市（英文）。作为入参时可以不填\n        :type City: str\n        :param Country: 国家（英文）。作为入参时可以不填\n        :type Country: str\n        """
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
        """
        :param TemplateId: 模板ID。详情请查看：[获取模板列表](https://cloud.tencent.com/document/product/242/48940)\n        :type TemplateId: str\n        :param Period: 购买域名的年限，可选值：[1-10]\n        :type Period: int\n        :param Domains: 批量购买的域名,最多为4000个\n        :type Domains: list of str\n        :param PayMode: 付费模式 0手动在线付费，1使用余额付费，2使用特惠包\n        :type PayMode: int\n        :param AutoRenewFlag: 自动续费开关。有两个可选值：
0 表示关闭，不自动续费（默认值）
1 表示开启，将自动续费\n        :type AutoRenewFlag: int\n        :param PackageResourceId: 使用的特惠包ID，PayMode为2时必填\n        :type PackageResourceId: str\n        """
        self.TemplateId = None
        self.Period = None
        self.Domains = None
        self.PayMode = None
        self.AutoRenewFlag = None
        self.PackageResourceId = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        self.Period = params.get("Period")
        self.Domains = params.get("Domains")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.PackageResourceId = params.get("PackageResourceId")
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
        """
        :param LogId: 批量日志ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class CreateTemplateRequest(AbstractModel):
    """CreateTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param ContactInfo: 联系人信息\n        :type ContactInfo: :class:`tencentcloud.domain.v20180808.models.ContactInfo`\n        :param CertificateInfo: 证件信息\n        :type CertificateInfo: :class:`tencentcloud.domain.v20180808.models.CertificateInfo`\n        """
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
        """
        :param Template: 模板信息\n        :type Template: :class:`tencentcloud.domain.v20180808.models.TemplateInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Template = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Template") is not None:
            self.Template = TemplateInfo()
            self.Template._deserialize(params.get("Template"))
        self.RequestId = params.get("RequestId")


class DeleteTemplateRequest(AbstractModel):
    """DeleteTemplate请求参数结构体

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID\n        :type TemplateId: str\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeBatchOperationLogDetailsRequest(AbstractModel):
    """DescribeBatchOperationLogDetails请求参数结构体

    """

    def __init__(self):
        """
        :param LogId: 日志ID。\n        :type LogId: int\n        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为200。\n        :type Limit: int\n        """
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
        """
        :param TotalCount: 总数量。\n        :type TotalCount: int\n        :param DomainBatchDetailSet: 日志详情列表。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainBatchDetailSet: list of DomainBatchDetailSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为200。\n        :type Limit: int\n        """
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
        """
        :param TotalCount: 总数量\n        :type TotalCount: int\n        :param DomainBatchLogSet: 日志列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainBatchLogSet: list of DomainBatchLogSet\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Domain: 域名\n        :type Domain: str\n        """
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
        """
        :param DomainInfo: 域名信息\n        :type DomainInfo: :class:`tencentcloud.domain.v20180808.models.DomainBaseInfo`\n        :param Uin: 用户Uin
注意：此字段可能返回 null，表示取不到有效值。\n        :type Uin: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param Offset: 偏移量，默认为0\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，取值范围[1,100]\n        :type Limit: int\n        """
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
        """
        :param DomainSet: 域名信息集合
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainSet: list of DomainList\n        :param TotalCount: 域名总数量\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param TldList: 查询价格的后缀列表。默认则为全部后缀\n        :type TldList: list of str\n        :param Year: 查询购买的年份，默认会列出所有年份的价格\n        :type Year: list of int\n        :param Operation: 域名的购买类型：new  新购，renew 续费，redem 赎回，tran 转入\n        :type Operation: list of str\n        """
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
        """
        :param PriceList: 域名价格列表\n        :type PriceList: list of PriceInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        :param Offset: 偏移量，默认为0。\n        :type Offset: int\n        :param Limit: 返回数量，默认为20，最大值为100。\n        :type Limit: int\n        :param Type: 用户注册类型，默认:all , 个人：I ,企业: E\n        :type Type: str\n        :param Status: 认证状态：未实名认证:NotUpload, 实名审核中:InAudit，已实名认证:Approved，实名审核失败:Reject\n        :type Status: str\n        :param Keyword: 域名所有者筛选\n        :type Keyword: str\n        """
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
        """
        :param TotalCount: 模板数量。\n        :type TotalCount: int\n        :param TemplateSet: 模板详细信息列表。\n        :type TemplateSet: list of TemplateInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param TemplateId: 模板ID\n        :type TemplateId: str\n        """
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
        """
        :param Template: 模板信息\n        :type Template: :class:`tencentcloud.domain.v20180808.models.TemplateInfo`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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
        """
        :param DomainId: 域名资源ID。\n        :type DomainId: str\n        :param DomainName: 域名名称。\n        :type DomainName: str\n        :param RealNameAuditStatus: 域名实名认证状态。
NotUpload：未实名认证
InAudit：实名审核中
Approved：实名审核通过
Reject：实名审核失败
NoAudit: 无需实名认证\n        :type RealNameAuditStatus: str\n        :param RealNameAuditUnpassReason: 域名实名认证不通过原因。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealNameAuditUnpassReason: str\n        :param DomainNameAuditStatus: 域名命名审核状态。
NotAudit：命名审核未上传
Pending：命名审核待上传
Auditing：域名命名审核中
Approved：域名命名审核通过
Rejected：域名命名审核拒绝\n        :type DomainNameAuditStatus: str\n        :param DomainNameAuditUnpassReason: 域名命名审核不通过原因。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainNameAuditUnpassReason: str\n        :param CreationDate: 注册时间。\n        :type CreationDate: str\n        :param ExpirationDate: 到期时间\n        :type ExpirationDate: str\n        :param DomainStatus: 域名状态。
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
clientDeleteProhibited：注册商禁止删除\n        :type DomainStatus: list of str\n        :param BuyStatus: 域名购买状态。
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
TransferFailed：转入失败\n        :type BuyStatus: str\n        :param RegistrarType: 注册商类型
epp: DNSPod, Inc.（烟台帝思普网络科技有限公司）
qcloud: Tencent Cloud Computing (Beijing) Limited Liability Company（腾讯云计算（北京）有限责任公司）
yunxun: Guangzhou Yunxun Information Technology Co., Ltd.（广州云讯信息科技有限公司）
xinnet: Xin Net Technology Corporation（北京新网数码信息技术有限公司）\n        :type RegistrarType: str\n        :param NameServer: 域名绑定的ns\n        :type NameServer: list of str\n        :param LockTransfer: true：开启锁定
false：关闭锁定\n        :type LockTransfer: bool\n        :param LockEndTime: 锁定结束时间\n        :type LockEndTime: str\n        """
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
        """
        :param Id: 详情ID\n        :type Id: int\n        :param Domain: 域名\n        :type Domain: str\n        :param Status: 执行状态：
doing 执行中。
failed 操作失败。
success  操作成功。\n        :type Status: str\n        :param Reason: 失败原因
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reason: str\n        :param CreatedOn: 创建时间\n        :type CreatedOn: str\n        :param UpdatedOn: 更新时间\n        :type UpdatedOn: str\n        """
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
        """
        :param LogId: 日志ID\n        :type LogId: int\n        :param Number: 数量\n        :type Number: int\n        :param Status: 执行状态：
doing 执行中。
done 执行完成。\n        :type Status: str\n        :param CreatedOn: 提交时间\n        :type CreatedOn: str\n        """
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
        """
        :param IsPremium: 是否是溢价域名：
ture 是    
false 不是\n        :type IsPremium: bool\n        :param DomainId: 域名资源ID。\n        :type DomainId: str\n        :param DomainName: 域名名称。\n        :type DomainName: str\n        :param AutoRenew: 是否已设置自动续费 。
0：未设置 
1：已设置\n        :type AutoRenew: int\n        :param CreationDate: 注册时间。\n        :type CreationDate: str\n        :param ExpirationDate: 到期时间。\n        :type ExpirationDate: str\n        :param Tld: 域名后缀\n        :type Tld: str\n        :param CodeTld: 编码后的后缀（中文会进行编码）\n        :type CodeTld: str\n        :param BuyStatus: 域名购买状态。
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
TransferFailed：转入失败\n        :type BuyStatus: str\n        """
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
        


class ModifyDomainDNSBatchRequest(AbstractModel):
    """ModifyDomainDNSBatch请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 批量操作的域名。\n        :type Domains: list of str\n        :param Dns: 域名DNS 数组。\n        :type Dns: list of str\n        """
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
        """
        :param LogId: 日志ID。\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class ModifyDomainOwnerBatchRequest(AbstractModel):
    """ModifyDomainOwnerBatch请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 要过户的域名。\n        :type Domains: list of str\n        :param NewOwnerUin: 转入账户的uin。\n        :type NewOwnerUin: str\n        :param TransferDns: 是否同时转移对应的 DNS 解析域名，默认false\n        :type TransferDns: bool\n        """
        self.Domains = None
        self.NewOwnerUin = None
        self.TransferDns = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.NewOwnerUin = params.get("NewOwnerUin")
        self.TransferDns = params.get("TransferDns")
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
        """
        :param LogId: 日志id\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class PriceInfo(AbstractModel):
    """域名价格信息

    """

    def __init__(self):
        """
        :param Tld: 域名后缀，例如.com\n        :type Tld: str\n        :param Year: 购买年限，范围[1-10]\n        :type Year: int\n        :param Price: 域名原价\n        :type Price: int\n        :param RealPrice: 域名现价\n        :type RealPrice: int\n        :param Operation: 商品的购买类型，新购，续费，赎回，转入，续费并转入\n        :type Operation: str\n        """
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
        """
        :param Period: 域名续费的年限。\n        :type Period: int\n        :param Domains: 批量续费的域名。\n        :type Domains: list of str\n        :param PayMode: 付费模式 0手动在线付费，1使用余额付费。\n        :type PayMode: int\n        :param AutoRenewFlag: 自动续费开关。有三个可选值：
0 表示关闭，不自动续费
1 表示开启，将自动续费
2 表示不处理，保留域名原有状态（默认值）\n        :type AutoRenewFlag: int\n        """
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
        """
        :param LogId: 操作日志ID。\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class SetDomainAutoRenewRequest(AbstractModel):
    """SetDomainAutoRenew请求参数结构体

    """

    def __init__(self):
        """
        :param DomainId: 域名ID。\n        :type DomainId: str\n        :param AutoRenew: AutoRenew 有三个可选值：
 0：不设置自动续费
1：设置自动续费
2：设置到期后不续费\n        :type AutoRenew: int\n        """
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
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TemplateInfo(AbstractModel):
    """Template数据

    """

    def __init__(self):
        """
        :param TemplateId: 模板ID\n        :type TemplateId: str\n        :param AuditStatus: 认证状态：未实名认证:NotUpload, 实名审核中:InAudit，已实名认证:Approved，实名审核失败:Reject\n        :type AuditStatus: str\n        :param CreatedOn: 创建时间\n        :type CreatedOn: str\n        :param UpdatedOn: 更新时间\n        :type UpdatedOn: str\n        :param UserUin: 用户UIN\n        :type UserUin: str\n        :param IsDefault: 是否是默认模板: 是:yes，否:no\n        :type IsDefault: str\n        :param AuditReason: 认证失败原因\n        :type AuditReason: str\n        :param CertificateInfo: 认证信息\n        :type CertificateInfo: :class:`tencentcloud.domain.v20180808.models.CertificateInfo`\n        :param ContactInfo: 联系人信息\n        :type ContactInfo: :class:`tencentcloud.domain.v20180808.models.ContactInfo`\n        :param IsValidTemplate: 模板是否符合规范， 1是 0 否\n        :type IsValidTemplate: int\n        :param InvalidReason: 不符合规范原因\n        :type InvalidReason: str\n        """
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
        """
        :param Domains: 转入的域名名称数组。\n        :type Domains: list of str\n        :param PassWords: 域名转移码数组。\n        :type PassWords: list of str\n        :param TemplateId: 模板ID。\n        :type TemplateId: str\n        :param PayMode: 付费模式 0手动在线付费，1使用余额付费。\n        :type PayMode: int\n        :param AutoRenewFlag: 自动续费开关。有两个可选值：
0 表示关闭，不自动续费（默认值）
1 表示开启，将自动续费\n        :type AutoRenewFlag: int\n        :param LockTransfer: true： 开启60天内禁止转移注册商锁定
false：关闭60天内禁止转移注册商锁定
默认 true\n        :type LockTransfer: bool\n        """
        self.Domains = None
        self.PassWords = None
        self.TemplateId = None
        self.PayMode = None
        self.AutoRenewFlag = None
        self.LockTransfer = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.PassWords = params.get("PassWords")
        self.TemplateId = params.get("TemplateId")
        self.PayMode = params.get("PayMode")
        self.AutoRenewFlag = params.get("AutoRenewFlag")
        self.LockTransfer = params.get("LockTransfer")
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
        """
        :param LogId: 日志ID\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class TransferProhibitionBatchRequest(AbstractModel):
    """TransferProhibitionBatch请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 批量操作的域名。\n        :type Domains: list of str\n        :param Status: 是否开启禁止域名转移。
True: 开启禁止域名转移状态。
False：关闭禁止域名转移状态。\n        :type Status: bool\n        """
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
        """
        :param LogId: 日志ID\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class UpdateProhibitionBatchRequest(AbstractModel):
    """UpdateProhibitionBatch请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 批量操作的域名。\n        :type Domains: list of str\n        :param Status: 是否开启禁止域名更新。
True:开启禁止域名更新状态。
False：关闭禁止域名更新状态。\n        :type Status: bool\n        """
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
        """
        :param LogId: 日志ID\n        :type LogId: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.LogId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.LogId = params.get("LogId")
        self.RequestId = params.get("RequestId")


class UploadImageRequest(AbstractModel):
    """UploadImage请求参数结构体

    """

    def __init__(self):
        """
        :param ImageFile: 资质照片，照片的base64编码。\n        :type ImageFile: str\n        """
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
        """
        :param AccessUrl: 资质照片地址。\n        :type AccessUrl: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.AccessUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AccessUrl = params.get("AccessUrl")
        self.RequestId = params.get("RequestId")