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


class CertInfo(AbstractModel):
    """证书信息

    """

    def __init__(self):
        """
        :param Hash: 证书sha1
        :type Hash: str
        :param CN: 证书通用名称
        :type CN: str
        :param SANs: 备用名称
        :type SANs: str
        :param KeyAlgo: 公钥算法
        :type KeyAlgo: str
        :param Issuer: 颁发者
        :type Issuer: str
        :param BeginTime: 有效期开始
        :type BeginTime: str
        :param EndTime: 有效期结束
        :type EndTime: str
        :param Days: 剩余天数
        :type Days: int
        :param Brand: 品牌
        :type Brand: str
        :param TrustStatus: 信任状态
        :type TrustStatus: str
        :param CertType: 证书类型
注意：此字段可能返回 null，表示取不到有效值。
        :type CertType: str
        """
        self.Hash = None
        self.CN = None
        self.SANs = None
        self.KeyAlgo = None
        self.Issuer = None
        self.BeginTime = None
        self.EndTime = None
        self.Days = None
        self.Brand = None
        self.TrustStatus = None
        self.CertType = None


    def _deserialize(self, params):
        self.Hash = params.get("Hash")
        self.CN = params.get("CN")
        self.SANs = params.get("SANs")
        self.KeyAlgo = params.get("KeyAlgo")
        self.Issuer = params.get("Issuer")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.Days = params.get("Days")
        self.Brand = params.get("Brand")
        self.TrustStatus = params.get("TrustStatus")
        self.CertType = params.get("CertType")


class ChartHistogram(AbstractModel):
    """直方图数据结构

    """

    def __init__(self):
        """
        :param Name: 项目名
        :type Name: str
        :param Children: 项目值
        :type Children: list of ChartNameValue
        """
        self.Name = None
        self.Children = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        if params.get("Children") is not None:
            self.Children = []
            for item in params.get("Children"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self.Children.append(obj)


class ChartNameValue(AbstractModel):
    """通用图表键值对

    """

    def __init__(self):
        """
        :param Name: 图表项名称
        :type Name: str
        :param Value: 图表项值
        :type Value: int
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        """
        :param ServerType: 监控的服务器类型（0：web，1：smtp，2：imap，3：pops）
        :type ServerType: int
        :param Domain: 添加的域名
        :type Domain: str
        :param Port: 添加的端口
        :type Port: str
        :param IP: 指定域名的IP
        :type IP: str
        :param Notice: 是否开启通知告警
        :type Notice: bool
        :param Tags: 给域名添加标签，多个以逗号隔开
        :type Tags: str
        """
        self.ServerType = None
        self.Domain = None
        self.Port = None
        self.IP = None
        self.Notice = None
        self.Tags = None


    def _deserialize(self, params):
        self.ServerType = params.get("ServerType")
        self.Domain = params.get("Domain")
        self.Port = params.get("Port")
        self.IP = params.get("IP")
        self.Notice = params.get("Notice")
        self.Tags = params.get("Tags")


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DashboardResult(AbstractModel):
    """面板数据

    """

    def __init__(self):
        """
        :param SecurityLevelPie: 安全等级图表
        :type SecurityLevelPie: list of ChartNameValue
        :param CertBrandsPie: 证书品牌图表
        :type CertBrandsPie: list of ChartNameValue
        :param CertValidTimePie: 证书有效时间图表
        :type CertValidTimePie: list of ChartNameValue
        :param CertTypePie: 证书类型图表
        :type CertTypePie: list of ChartNameValue
        :param SSLBugsLoopholeHistogram: ssl bugs图表
        :type SSLBugsLoopholeHistogram: list of ChartHistogram
        :param ComplianceHistogram: 合规图表
        :type ComplianceHistogram: list of ChartHistogram
        """
        self.SecurityLevelPie = None
        self.CertBrandsPie = None
        self.CertValidTimePie = None
        self.CertTypePie = None
        self.SSLBugsLoopholeHistogram = None
        self.ComplianceHistogram = None


    def _deserialize(self, params):
        if params.get("SecurityLevelPie") is not None:
            self.SecurityLevelPie = []
            for item in params.get("SecurityLevelPie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self.SecurityLevelPie.append(obj)
        if params.get("CertBrandsPie") is not None:
            self.CertBrandsPie = []
            for item in params.get("CertBrandsPie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self.CertBrandsPie.append(obj)
        if params.get("CertValidTimePie") is not None:
            self.CertValidTimePie = []
            for item in params.get("CertValidTimePie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self.CertValidTimePie.append(obj)
        if params.get("CertTypePie") is not None:
            self.CertTypePie = []
            for item in params.get("CertTypePie"):
                obj = ChartNameValue()
                obj._deserialize(item)
                self.CertTypePie.append(obj)
        if params.get("SSLBugsLoopholeHistogram") is not None:
            self.SSLBugsLoopholeHistogram = []
            for item in params.get("SSLBugsLoopholeHistogram"):
                obj = ChartHistogram()
                obj._deserialize(item)
                self.SSLBugsLoopholeHistogram.append(obj)
        if params.get("ComplianceHistogram") is not None:
            self.ComplianceHistogram = []
            for item in params.get("ComplianceHistogram"):
                obj = ChartHistogram()
                obj._deserialize(item)
                self.ComplianceHistogram.append(obj)


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainId: 域名ID，可通过搜索域名接口获得
        :type DomainId: int
        """
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDashboardRequest(AbstractModel):
    """DescribeDashboard请求参数结构体

    """


class DescribeDashboardResponse(AbstractModel):
    """DescribeDashboard返回参数结构体

    """

    def __init__(self):
        """
        :param Data: dashboard面板数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.sslpod.v20190605.models.DashboardResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DashboardResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeDomainCertsRequest(AbstractModel):
    """DescribeDomainCerts请求参数结构体

    """

    def __init__(self):
        """
        :param DomainId: 域名ID，可通过搜索域名接口获得
        :type DomainId: int
        """
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")


class DescribeDomainCertsResponse(AbstractModel):
    """DescribeDomainCerts返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 证书信息
        :type Data: list of CertInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = CertInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainTagsRequest(AbstractModel):
    """DescribeDomainTags请求参数结构体

    """


class DescribeDomainTagsResponse(AbstractModel):
    """DescribeDomainTags返回参数结构体

    """

    def __init__(self):
        """
        :param Data: Tag数组
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")


class DescribeDomains(AbstractModel):
    """监控域名列表

    """

    def __init__(self):
        """
        :param Result: 列表数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Result: list of DomainSiteInfo
        :param SearchTotal: 搜索出来的数量
        :type SearchTotal: int
        :param Total: 总数
        :type Total: int
        :param AllowMonitoringCount: 允许的监控数量
        :type AllowMonitoringCount: int
        :param CurrentMonitoringCount: 当前监控的数量
        :type CurrentMonitoringCount: int
        :param AllowMaxAddDomain: 允许添加域名总数
        :type AllowMaxAddDomain: int
        """
        self.Result = None
        self.SearchTotal = None
        self.Total = None
        self.AllowMonitoringCount = None
        self.CurrentMonitoringCount = None
        self.AllowMaxAddDomain = None


    def _deserialize(self, params):
        if params.get("Result") is not None:
            self.Result = []
            for item in params.get("Result"):
                obj = DomainSiteInfo()
                obj._deserialize(item)
                self.Result.append(obj)
        self.SearchTotal = params.get("SearchTotal")
        self.Total = params.get("Total")
        self.AllowMonitoringCount = params.get("AllowMonitoringCount")
        self.CurrentMonitoringCount = params.get("CurrentMonitoringCount")
        self.AllowMaxAddDomain = params.get("AllowMaxAddDomain")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 偏移量
        :type Offset: int
        :param Limit: 获取数量
        :type Limit: int
        :param SearchType: 搜索的类型 Enums(none,tags,grade,brand,code,hash,limit)
        :type SearchType: str
        :param Tag: 标签，多个标签用逗号分隔
        :type Tag: str
        :param Grade: 等级
        :type Grade: str
        :param Brand: 品牌
        :type Brand: str
        :param Code: 混合搜索
        :type Code: str
        :param Hash: 证书指纹
        :type Hash: str
        :param Item: 搜索图标类型
        :type Item: str
        :param Status: 搜索图标值
        :type Status: str
        """
        self.Offset = None
        self.Limit = None
        self.SearchType = None
        self.Tag = None
        self.Grade = None
        self.Brand = None
        self.Code = None
        self.Hash = None
        self.Item = None
        self.Status = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchType = params.get("SearchType")
        self.Tag = params.get("Tag")
        self.Grade = params.get("Grade")
        self.Brand = params.get("Brand")
        self.Code = params.get("Code")
        self.Hash = params.get("Hash")
        self.Item = params.get("Item")
        self.Status = params.get("Status")


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 列表数据
        :type Data: :class:`tencentcloud.sslpod.v20190605.models.DescribeDomains`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = DescribeDomains()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DescribeNoticeInfoRequest(AbstractModel):
    """DescribeNoticeInfo请求参数结构体

    """


class DescribeNoticeInfoResponse(AbstractModel):
    """DescribeNoticeInfo返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 通知信息结果
        :type Data: :class:`tencentcloud.sslpod.v20190605.models.NoticeInfoResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = NoticeInfoResult()
            self.Data._deserialize(params.get("Data"))
        self.RequestId = params.get("RequestId")


class DomainSiteInfo(AbstractModel):
    """监控的域名站点信息

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param Domain: 域名
        :type Domain: str
        :param Ip: IP地址
        :type Ip: str
        :param AutoIP: 是否自动获取IP
        :type AutoIP: bool
        :param ServerType: 监控服务类型
        :type ServerType: int
        :param Brand: 证书品牌
        :type Brand: str
        :param Grade: 评级
        :type Grade: str
        :param GradeCode: 评级Code
        :type GradeCode: int
        :param Notice: 是否监控告警
        :type Notice: bool
        :param AccountDomainId: 账号域名关系ID
        :type AccountDomainId: int
        :param Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: list of str
        :param Status: 域名状态
        :type Status: str
        :param Port: 域名端口
        :type Port: str
        """
        self.Id = None
        self.Domain = None
        self.Ip = None
        self.AutoIP = None
        self.ServerType = None
        self.Brand = None
        self.Grade = None
        self.GradeCode = None
        self.Notice = None
        self.AccountDomainId = None
        self.Tags = None
        self.Status = None
        self.Port = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Domain = params.get("Domain")
        self.Ip = params.get("Ip")
        self.AutoIP = params.get("AutoIP")
        self.ServerType = params.get("ServerType")
        self.Brand = params.get("Brand")
        self.Grade = params.get("Grade")
        self.GradeCode = params.get("GradeCode")
        self.Notice = params.get("Notice")
        self.AccountDomainId = params.get("AccountDomainId")
        self.Tags = params.get("Tags")
        self.Status = params.get("Status")
        self.Port = params.get("Port")


class LimitInfo(AbstractModel):
    """通知额度限制信息

    """

    def __init__(self):
        """
        :param Type: 通知类型
        :type Type: str
        :param Total: 总量
        :type Total: int
        :param Sent: 已发送
        :type Sent: int
        """
        self.Type = None
        self.Total = None
        self.Sent = None


    def _deserialize(self, params):
        self.Type = params.get("Type")
        self.Total = params.get("Total")
        self.Sent = params.get("Sent")


class ModifyDomainTagsRequest(AbstractModel):
    """ModifyDomainTags请求参数结构体

    """

    def __init__(self):
        """
        :param AccountDomainId: 账号下域名ID
        :type AccountDomainId: int
        :param Tags: 更新后的tag，多个以逗号隔开
        :type Tags: str
        """
        self.AccountDomainId = None
        self.Tags = None


    def _deserialize(self, params):
        self.AccountDomainId = params.get("AccountDomainId")
        self.Tags = params.get("Tags")


class ModifyDomainTagsResponse(AbstractModel):
    """ModifyDomainTags返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NoticeInfoResult(AbstractModel):
    """通知信息结果

    """

    def __init__(self):
        """
        :param Id: 通知ID
        :type Id: int
        :param NoticeType: 通知开关信息
        :type NoticeType: int
        :param LimitInfos: 额度信息
        :type LimitInfos: list of LimitInfo
        """
        self.Id = None
        self.NoticeType = None
        self.LimitInfos = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.NoticeType = params.get("NoticeType")
        if params.get("LimitInfos") is not None:
            self.LimitInfos = []
            for item in params.get("LimitInfos"):
                obj = LimitInfo()
                obj._deserialize(item)
                self.LimitInfos.append(obj)


class RefreshDomainRequest(AbstractModel):
    """RefreshDomain请求参数结构体

    """

    def __init__(self):
        """
        :param DomainId: 域名列表中的ID，可通过搜索域名接口获得
        :type DomainId: int
        """
        self.DomainId = None


    def _deserialize(self, params):
        self.DomainId = params.get("DomainId")


class RefreshDomainResponse(AbstractModel):
    """RefreshDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ResolveDomainRequest(AbstractModel):
    """ResolveDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class ResolveDomainResponse(AbstractModel):
    """ResolveDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 响应数据
        :type Data: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Data = params.get("Data")
        self.RequestId = params.get("RequestId")