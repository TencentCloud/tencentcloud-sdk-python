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


class CreateMonitorsRequest(AbstractModel):
    """CreateMonitors请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 站点的url列表
        :type Urls: list of str
        :param Name: 任务名称
        :type Name: str
        :param ScannerType: 扫描模式，normal-正常扫描；deep-深度扫描
        :type ScannerType: str
        :param Crontab: 扫描周期，单位小时，每X小时执行一次
        :type Crontab: int
        :param RateLimit: 扫描速率限制，每秒发送X个HTTP请求
        :type RateLimit: int
        :param FirstScanStartTime: 首次扫描开始时间
        :type FirstScanStartTime: str
        """
        self.Urls = None
        self.Name = None
        self.ScannerType = None
        self.Crontab = None
        self.RateLimit = None
        self.FirstScanStartTime = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.Name = params.get("Name")
        self.ScannerType = params.get("ScannerType")
        self.Crontab = params.get("Crontab")
        self.RateLimit = params.get("RateLimit")
        self.FirstScanStartTime = params.get("FirstScanStartTime")


class CreateMonitorsResponse(AbstractModel):
    """CreateMonitors返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateSitesRequest(AbstractModel):
    """CreateSites请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 站点的url列表
        :type Urls: list of str
        :param UserAgent: 访问网站的客户端标识
        :type UserAgent: str
        """
        self.Urls = None
        self.UserAgent = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")


class CreateSitesResponse(AbstractModel):
    """CreateSites返回参数结构体

    """

    def __init__(self):
        """
        :param Number: 新增站点数。
        :type Number: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Number = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Number = params.get("Number")
        self.RequestId = params.get("RequestId")


class CreateSitesScansRequest(AbstractModel):
    """CreateSitesScans请求参数结构体

    """

    def __init__(self):
        """
        :param SiteIds: 站点的ID列表
        :type SiteIds: list of int non-negative
        :param ScannerType: 扫描模式，normal-正常扫描；deep-深度扫描
        :type ScannerType: str
        :param RateLimit: 扫描速率限制，每秒发送X个HTTP请求
        :type RateLimit: int
        """
        self.SiteIds = None
        self.ScannerType = None
        self.RateLimit = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        self.ScannerType = params.get("ScannerType")
        self.RateLimit = params.get("RateLimit")


class CreateSitesScansResponse(AbstractModel):
    """CreateSitesScans返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVulsMisinformationRequest(AbstractModel):
    """CreateVulsMisinformation请求参数结构体

    """

    def __init__(self):
        """
        :param VulIds: 漏洞ID列表
        :type VulIds: list of int non-negative
        """
        self.VulIds = None


    def _deserialize(self, params):
        self.VulIds = params.get("VulIds")


class CreateVulsMisinformationResponse(AbstractModel):
    """CreateVulsMisinformation返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateVulsReportRequest(AbstractModel):
    """CreateVulsReport请求参数结构体

    """

    def __init__(self):
        """
        :param SiteId: 站点ID
        :type SiteId: int
        :param MonitorId: 监控任务ID
        :type MonitorId: int
        """
        self.SiteId = None
        self.MonitorId = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.MonitorId = params.get("MonitorId")


class CreateVulsReportResponse(AbstractModel):
    """CreateVulsReport返回参数结构体

    """

    def __init__(self):
        """
        :param ReportFileUrl: 报告下载地址
        :type ReportFileUrl: str
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ReportFileUrl = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ReportFileUrl = params.get("ReportFileUrl")
        self.RequestId = params.get("RequestId")


class DeleteMonitorsRequest(AbstractModel):
    """DeleteMonitors请求参数结构体

    """

    def __init__(self):
        """
        :param MonitorIds: 监控任务ID列表
        :type MonitorIds: list of int non-negative
        """
        self.MonitorIds = None


    def _deserialize(self, params):
        self.MonitorIds = params.get("MonitorIds")


class DeleteMonitorsResponse(AbstractModel):
    """DeleteMonitors返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSitesRequest(AbstractModel):
    """DeleteSites请求参数结构体

    """

    def __init__(self):
        """
        :param SiteIds: 站点ID列表
        :type SiteIds: list of int non-negative
        """
        self.SiteIds = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")


class DeleteSitesResponse(AbstractModel):
    """DeleteSites返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        """
        :param NoticeLevel: 漏洞告警通知等级，4位分别代表：高危、中危、低危、提示。
        :type NoticeLevel: str
        :param Id: 配置ID。
        :type Id: int
        :param CreatedAt: 记录创建时间。
        :type CreatedAt: str
        :param UpdatedAt: 记录更新新建。
        :type UpdatedAt: str
        :param Appid: 云用户appid。
        :type Appid: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.NoticeLevel = None
        self.Id = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.Appid = None
        self.RequestId = None


    def _deserialize(self, params):
        self.NoticeLevel = params.get("NoticeLevel")
        self.Id = params.get("Id")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.Appid = params.get("Appid")
        self.RequestId = params.get("RequestId")


class DescribeMonitorsRequest(AbstractModel):
    """DescribeMonitors请求参数结构体

    """

    def __init__(self):
        """
        :param MonitorIds: 监控任务ID列表
        :type MonitorIds: list of int non-negative
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100
        :type Limit: int
        """
        self.MonitorIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.MonitorIds = params.get("MonitorIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeMonitorsResponse(AbstractModel):
    """DescribeMonitors返回参数结构体

    """

    def __init__(self):
        """
        :param Monitors: 监控任务列表。
        :type Monitors: list of MonitorsDetail
        :param TotalCount: 监控任务数量。
        :type TotalCount: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Monitors = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Monitors") is not None:
            self.Monitors = []
            for item in params.get("Monitors"):
                obj = MonitorsDetail()
                obj._deserialize(item)
                self.Monitors.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSiteQuotaRequest(AbstractModel):
    """DescribeSiteQuota请求参数结构体

    """


class DescribeSiteQuotaResponse(AbstractModel):
    """DescribeSiteQuota返回参数结构体

    """

    def __init__(self):
        """
        :param Total: 已购买的扫描次数。
        :type Total: int
        :param Used: 已使用的扫描次数。
        :type Used: int
        :param Available: 剩余可用的扫描次数。
        :type Available: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.Total = None
        self.Used = None
        self.Available = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Total = params.get("Total")
        self.Used = params.get("Used")
        self.Available = params.get("Available")
        self.RequestId = params.get("RequestId")


class DescribeSitesRequest(AbstractModel):
    """DescribeSites请求参数结构体

    """

    def __init__(self):
        """
        :param SiteIds: 站点ID列表
        :type SiteIds: list of int non-negative
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100
        :type Limit: int
        """
        self.SiteIds = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SiteIds = params.get("SiteIds")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeSitesResponse(AbstractModel):
    """DescribeSites返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 站点数量。
        :type TotalCount: int
        :param Sites: 站点信息列表。
        :type Sites: list of Site
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Sites = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = Site()
                obj._deserialize(item)
                self.Sites.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSitesVerificationRequest(AbstractModel):
    """DescribeSitesVerification请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 站点的url列表
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class DescribeSitesVerificationResponse(AbstractModel):
    """DescribeSitesVerification返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 验证信息数量。
        :type TotalCount: int
        :param SitesVerification: 验证信息列表。
        :type SitesVerification: list of SitesVerification
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SitesVerification = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SitesVerification") is not None:
            self.SitesVerification = []
            for item in params.get("SitesVerification"):
                obj = SitesVerification()
                obj._deserialize(item)
                self.SitesVerification.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulsNumberRequest(AbstractModel):
    """DescribeVulsNumber请求参数结构体

    """


class DescribeVulsNumberResponse(AbstractModel):
    """DescribeVulsNumber返回参数结构体

    """

    def __init__(self):
        """
        :param ImpactSiteNumber: 受影响的网站总数。
        :type ImpactSiteNumber: int
        :param SiteNumber: 已验证的网站总数。
        :type SiteNumber: int
        :param VulsHighNumber: 高风险漏洞总数。
        :type VulsHighNumber: int
        :param VulsMiddleNumber: 中风险漏洞总数。
        :type VulsMiddleNumber: int
        :param VulsLowNumber: 低高风险漏洞总数。
        :type VulsLowNumber: int
        :param VulsNoticeNumber: 风险提示总数。
        :type VulsNoticeNumber: int
        :param PageCount: 扫描页面总数。
        :type PageCount: int
        :param Sites: 已验证的网站列表。
        :type Sites: list of MonitorMiniSite
        :param ImpactSites: 受影响的网站列表。
        :type ImpactSites: list of MonitorMiniSite
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.ImpactSiteNumber = None
        self.SiteNumber = None
        self.VulsHighNumber = None
        self.VulsMiddleNumber = None
        self.VulsLowNumber = None
        self.VulsNoticeNumber = None
        self.PageCount = None
        self.Sites = None
        self.ImpactSites = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ImpactSiteNumber = params.get("ImpactSiteNumber")
        self.SiteNumber = params.get("SiteNumber")
        self.VulsHighNumber = params.get("VulsHighNumber")
        self.VulsMiddleNumber = params.get("VulsMiddleNumber")
        self.VulsLowNumber = params.get("VulsLowNumber")
        self.VulsNoticeNumber = params.get("VulsNoticeNumber")
        self.PageCount = params.get("PageCount")
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.Sites.append(obj)
        if params.get("ImpactSites") is not None:
            self.ImpactSites = []
            for item in params.get("ImpactSites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.ImpactSites.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulsNumberTimelineRequest(AbstractModel):
    """DescribeVulsNumberTimeline请求参数结构体

    """


class DescribeVulsNumberTimelineResponse(AbstractModel):
    """DescribeVulsNumberTimeline返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 统计数据记录数量。
        :type TotalCount: int
        :param VulsTimeline: 用户漏洞数随时间变化统计数据。
        :type VulsTimeline: list of VulsTimeline
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.VulsTimeline = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("VulsTimeline") is not None:
            self.VulsTimeline = []
            for item in params.get("VulsTimeline"):
                obj = VulsTimeline()
                obj._deserialize(item)
                self.VulsTimeline.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls请求参数结构体

    """

    def __init__(self):
        """
        :param SiteId: 站点ID
        :type SiteId: int
        :param MonitorId: 监控任务ID
        :type MonitorId: int
        :param Filters: 过滤条件
        :type Filters: list of Filter
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 返回数量，默认为10，最大值为100
        :type Limit: int
        """
        self.SiteId = None
        self.MonitorId = None
        self.Filters = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.MonitorId = params.get("MonitorId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 漏洞数量。
        :type TotalCount: int
        :param Vuls: 漏洞信息列表。
        :type Vuls: list of Vul
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.Vuls = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self.Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self.Vuls.append(obj)
        self.RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        """
        :param Name: 过滤键的名称。
        :type Name: str
        :param Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")


class ModifyConfigAttributeRequest(AbstractModel):
    """ModifyConfigAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param NoticeLevel: 漏洞告警通知等级，4位分别代表：高危、中危、低危、提示
        :type NoticeLevel: str
        """
        self.NoticeLevel = None


    def _deserialize(self, params):
        self.NoticeLevel = params.get("NoticeLevel")


class ModifyConfigAttributeResponse(AbstractModel):
    """ModifyConfigAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyMonitorAttributeRequest(AbstractModel):
    """ModifyMonitorAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param MonitorId: 监测任务ID
        :type MonitorId: int
        :param Urls: 站点的url列表
        :type Urls: list of str
        :param Name: 任务名称
        :type Name: str
        :param ScannerType: 扫描模式，normal-正常扫描；deep-深度扫描
        :type ScannerType: str
        :param Crontab: 扫描周期，单位小时，每X小时执行一次
        :type Crontab: int
        :param RateLimit: 扫描速率限制，每秒发送X个HTTP请求
        :type RateLimit: int
        :param FirstScanStartTime: 首次扫描开始时间
        :type FirstScanStartTime: str
        :param MonitorStatus: 监测状态：1-监测中；2-暂停监测
        :type MonitorStatus: int
        """
        self.MonitorId = None
        self.Urls = None
        self.Name = None
        self.ScannerType = None
        self.Crontab = None
        self.RateLimit = None
        self.FirstScanStartTime = None
        self.MonitorStatus = None


    def _deserialize(self, params):
        self.MonitorId = params.get("MonitorId")
        self.Urls = params.get("Urls")
        self.Name = params.get("Name")
        self.ScannerType = params.get("ScannerType")
        self.Crontab = params.get("Crontab")
        self.RateLimit = params.get("RateLimit")
        self.FirstScanStartTime = params.get("FirstScanStartTime")
        self.MonitorStatus = params.get("MonitorStatus")


class ModifyMonitorAttributeResponse(AbstractModel):
    """ModifyMonitorAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySiteAttributeRequest(AbstractModel):
    """ModifySiteAttribute请求参数结构体

    """

    def __init__(self):
        """
        :param SiteId: 站点ID
        :type SiteId: int
        :param Name: 站点名称
        :type Name: str
        :param NeedLogin: 网站是否需要登录扫描：0-未知；-1-不需要；1-需要
        :type NeedLogin: int
        :param LoginCookie: 登录后的cookie
        :type LoginCookie: str
        :param LoginCheckUrl: 用于测试cookie是否有效的URL
        :type LoginCheckUrl: str
        :param LoginCheckKw: 用于测试cookie是否有效的关键字
        :type LoginCheckKw: str
        :param ScanDisallow: 禁止扫描器扫描的目录关键字
        :type ScanDisallow: str
        """
        self.SiteId = None
        self.Name = None
        self.NeedLogin = None
        self.LoginCookie = None
        self.LoginCheckUrl = None
        self.LoginCheckKw = None
        self.ScanDisallow = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Name = params.get("Name")
        self.NeedLogin = params.get("NeedLogin")
        self.LoginCookie = params.get("LoginCookie")
        self.LoginCheckUrl = params.get("LoginCheckUrl")
        self.LoginCheckKw = params.get("LoginCheckKw")
        self.ScanDisallow = params.get("ScanDisallow")


class ModifySiteAttributeResponse(AbstractModel):
    """ModifySiteAttribute返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Monitor(AbstractModel):
    """监控任务基础数据

    """

    def __init__(self):
        """
        :param Appid: 云用户appid。
        :type Appid: int
        :param Id: 监控任务ID。
        :type Id: int
        :param Name: 监控名称。
        :type Name: str
        :param MonitorStatus: 监测状态：1-监测中；2-暂停监测。
        :type MonitorStatus: int
        :param ScannerType: 监测模式，normal-正常扫描；deep-深度扫描。
        :type ScannerType: str
        :param Crontab: 扫描周期，单位小时，每X小时执行一次。
        :type Crontab: int
        :param IncludedVulsTypes: 指定扫描类型，3位数每位依次表示：扫描Web漏洞、扫描系统漏洞、扫描系统端口。
        :type IncludedVulsTypes: str
        :param RateLimit: 速率限制，每秒发送X个HTTP请求。
        :type RateLimit: int
        :param FirstScanStartTime: 首次扫描开始时间。
        :type FirstScanStartTime: str
        :param ScanStatus: 扫描状态：0-待扫描（无任何扫描结果）；1-扫描中（正在进行扫描）；2-已扫描（有扫描结果且不正在扫描）；3-扫描完成待同步结果。
        :type ScanStatus: int
        :param LastScanFinishTime: 上一次扫描完成时间。
        :type LastScanFinishTime: str
        :param CurrentScanStartTime: 当前扫描开始时间，如扫描完成则为上一次扫描的开始时间。
        :type CurrentScanStartTime: str
        :param CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        """
        self.Appid = None
        self.Id = None
        self.Name = None
        self.MonitorStatus = None
        self.ScannerType = None
        self.Crontab = None
        self.IncludedVulsTypes = None
        self.RateLimit = None
        self.FirstScanStartTime = None
        self.ScanStatus = None
        self.LastScanFinishTime = None
        self.CurrentScanStartTime = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Appid = params.get("Appid")
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        self.MonitorStatus = params.get("MonitorStatus")
        self.ScannerType = params.get("ScannerType")
        self.Crontab = params.get("Crontab")
        self.IncludedVulsTypes = params.get("IncludedVulsTypes")
        self.RateLimit = params.get("RateLimit")
        self.FirstScanStartTime = params.get("FirstScanStartTime")
        self.ScanStatus = params.get("ScanStatus")
        self.LastScanFinishTime = params.get("LastScanFinishTime")
        self.CurrentScanStartTime = params.get("CurrentScanStartTime")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")


class MonitorMiniSite(AbstractModel):
    """监控任务中的站点信息。

    """

    def __init__(self):
        """
        :param SiteId: 站点ID。
        :type SiteId: int
        :param Url: 站点Url。
        :type Url: str
        """
        self.SiteId = None
        self.Url = None


    def _deserialize(self, params):
        self.SiteId = params.get("SiteId")
        self.Url = params.get("Url")


class MonitorsDetail(AbstractModel):
    """监控任务详细数据

    """

    def __init__(self):
        """
        :param Progress: 监控任务包含的站点列表的平均扫描进度。
        :type Progress: int
        :param PageCount: 扫描页面总数。
        :type PageCount: int
        :param Basic: 监控任务基础信息。
        :type Basic: :class:`tencentcloud.cws.v20180312.models.Monitor`
        :param Sites: 监控任务包含的站点列表。
        :type Sites: list of MonitorMiniSite
        :param SiteNumber: 监控任务包含的站点列表数量。
        :type SiteNumber: int
        :param ImpactSites: 监控任务包含的受漏洞威胁的站点列表。
        :type ImpactSites: list of MonitorMiniSite
        :param ImpactSiteNumber: 监控任务包含的受漏洞威胁的站点列表数量。
        :type ImpactSiteNumber: int
        :param VulsHighNumber: 高风险漏洞数量。
        :type VulsHighNumber: int
        :param VulsMiddleNumber: 中风险漏洞数量。
        :type VulsMiddleNumber: int
        :param VulsLowNumber: 低风险漏洞数量。
        :type VulsLowNumber: int
        :param VulsNoticeNumber: 提示数量。
        :type VulsNoticeNumber: int
        """
        self.Progress = None
        self.PageCount = None
        self.Basic = None
        self.Sites = None
        self.SiteNumber = None
        self.ImpactSites = None
        self.ImpactSiteNumber = None
        self.VulsHighNumber = None
        self.VulsMiddleNumber = None
        self.VulsLowNumber = None
        self.VulsNoticeNumber = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.PageCount = params.get("PageCount")
        if params.get("Basic") is not None:
            self.Basic = Monitor()
            self.Basic._deserialize(params.get("Basic"))
        if params.get("Sites") is not None:
            self.Sites = []
            for item in params.get("Sites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.Sites.append(obj)
        self.SiteNumber = params.get("SiteNumber")
        if params.get("ImpactSites") is not None:
            self.ImpactSites = []
            for item in params.get("ImpactSites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self.ImpactSites.append(obj)
        self.ImpactSiteNumber = params.get("ImpactSiteNumber")
        self.VulsHighNumber = params.get("VulsHighNumber")
        self.VulsMiddleNumber = params.get("VulsMiddleNumber")
        self.VulsLowNumber = params.get("VulsLowNumber")
        self.VulsNoticeNumber = params.get("VulsNoticeNumber")


class Site(AbstractModel):
    """站点数据

    """

    def __init__(self):
        """
        :param Progress: 扫描进度，百分比整数
        :type Progress: int
        :param Appid: 云用户appid。
        :type Appid: int
        :param Uin: 云用户标识。
        :type Uin: str
        :param NeedLogin: 网站是否需要登录扫描：0-未知；-1-不需要；1-需要。
        :type NeedLogin: int
        :param LoginCookie: 登录后的cookie。
        :type LoginCookie: str
        :param LoginCookieValid: 登录后的cookie是否有效：0-无效；1-有效。
        :type LoginCookieValid: int
        :param LoginCheckUrl: 用于测试cookie是否有效的URL。
        :type LoginCheckUrl: str
        :param LoginCheckKw: 用于测试cookie是否有效的关键字。
        :type LoginCheckKw: str
        :param ScanDisallow: 禁止扫描器扫描的目录关键字。
        :type ScanDisallow: str
        :param UserAgent: 访问网站的客户端标识。
        :type UserAgent: str
        :param Id: 站点ID。
        :type Id: int
        :param MonitorId: 监控任务ID，为0时表示未加入监控任务。
        :type MonitorId: int
        :param Url: 站点url。
        :type Url: str
        :param Name: 站点名称。
        :type Name: str
        :param VerifyStatus: 验证状态：0-未验证；1-已验证；2-验证失效，待重新验证。
        :type VerifyStatus: int
        :param MonitorStatus: 监测状态：0-未监测；1-监测中；2-暂停监测。
        :type MonitorStatus: int
        :param ScanStatus: 扫描状态：0-待扫描（无任何扫描结果）；1-扫描中（正在进行扫描）；2-已扫描（有扫描结果且不正在扫描）；3-扫描完成待同步结果。
        :type ScanStatus: int
        :param LastScanTaskId: 最近一次的AIScanner的扫描任务id，注意取消的情况。
        :type LastScanTaskId: int
        :param LastScanStartTime: 最近一次扫描开始时间。
        :type LastScanStartTime: str
        :param LastScanFinishTime: 最近一次扫描完成时间。
        :type LastScanFinishTime: str
        :param LastScanCancelTime: 最近一次取消时间，取消即使用上一次扫描结果。
        :type LastScanCancelTime: str
        :param LastScanPageCount: 最近一次扫描扫描的页面数。
        :type LastScanPageCount: int
        :param LastScanScannerType: normal-正常扫描；deep-深度扫描。
        :type LastScanScannerType: str
        :param LastScanVulsHighNum: 最近一次扫描高风险漏洞数量。
        :type LastScanVulsHighNum: int
        :param LastScanVulsMiddleNum: 最近一次扫描中风险漏洞数量。
        :type LastScanVulsMiddleNum: int
        :param LastScanVulsLowNum: 最近一次扫描低风险漏洞数量。
        :type LastScanVulsLowNum: int
        :param LastScanVulsNoticeNum: 最近一次扫描提示信息数量。
        :type LastScanVulsNoticeNum: int
        :param CreatedAt: 记录添加时间。
        :type CreatedAt: str
        :param UpdatedAt: 记录最近修改时间。
        :type UpdatedAt: str
        :param LastScanRateLimit: 速率限制，每秒发送X个HTTP请求。
        :type LastScanRateLimit: int
        :param LastScanVulsNum: 最近一次扫描漏洞总数量。
        :type LastScanVulsNum: int
        :param LastScanNoticeNum: 最近一次扫描提示总数量
        :type LastScanNoticeNum: int
        """
        self.Progress = None
        self.Appid = None
        self.Uin = None
        self.NeedLogin = None
        self.LoginCookie = None
        self.LoginCookieValid = None
        self.LoginCheckUrl = None
        self.LoginCheckKw = None
        self.ScanDisallow = None
        self.UserAgent = None
        self.Id = None
        self.MonitorId = None
        self.Url = None
        self.Name = None
        self.VerifyStatus = None
        self.MonitorStatus = None
        self.ScanStatus = None
        self.LastScanTaskId = None
        self.LastScanStartTime = None
        self.LastScanFinishTime = None
        self.LastScanCancelTime = None
        self.LastScanPageCount = None
        self.LastScanScannerType = None
        self.LastScanVulsHighNum = None
        self.LastScanVulsMiddleNum = None
        self.LastScanVulsLowNum = None
        self.LastScanVulsNoticeNum = None
        self.CreatedAt = None
        self.UpdatedAt = None
        self.LastScanRateLimit = None
        self.LastScanVulsNum = None
        self.LastScanNoticeNum = None


    def _deserialize(self, params):
        self.Progress = params.get("Progress")
        self.Appid = params.get("Appid")
        self.Uin = params.get("Uin")
        self.NeedLogin = params.get("NeedLogin")
        self.LoginCookie = params.get("LoginCookie")
        self.LoginCookieValid = params.get("LoginCookieValid")
        self.LoginCheckUrl = params.get("LoginCheckUrl")
        self.LoginCheckKw = params.get("LoginCheckKw")
        self.ScanDisallow = params.get("ScanDisallow")
        self.UserAgent = params.get("UserAgent")
        self.Id = params.get("Id")
        self.MonitorId = params.get("MonitorId")
        self.Url = params.get("Url")
        self.Name = params.get("Name")
        self.VerifyStatus = params.get("VerifyStatus")
        self.MonitorStatus = params.get("MonitorStatus")
        self.ScanStatus = params.get("ScanStatus")
        self.LastScanTaskId = params.get("LastScanTaskId")
        self.LastScanStartTime = params.get("LastScanStartTime")
        self.LastScanFinishTime = params.get("LastScanFinishTime")
        self.LastScanCancelTime = params.get("LastScanCancelTime")
        self.LastScanPageCount = params.get("LastScanPageCount")
        self.LastScanScannerType = params.get("LastScanScannerType")
        self.LastScanVulsHighNum = params.get("LastScanVulsHighNum")
        self.LastScanVulsMiddleNum = params.get("LastScanVulsMiddleNum")
        self.LastScanVulsLowNum = params.get("LastScanVulsLowNum")
        self.LastScanVulsNoticeNum = params.get("LastScanVulsNoticeNum")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")
        self.LastScanRateLimit = params.get("LastScanRateLimit")
        self.LastScanVulsNum = params.get("LastScanVulsNum")
        self.LastScanNoticeNum = params.get("LastScanNoticeNum")


class SitesVerification(AbstractModel):
    """站点验证数据

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Appid: 云用户appid
        :type Appid: int
        :param VerifyUrl: 用于验证站点的url，即访问该url获取验证数据。
        :type VerifyUrl: str
        :param VerifyFileUrl: 获取验证验证文件的url。
        :type VerifyFileUrl: str
        :param Domain: 根域名。
        :type Domain: str
        :param TxtName: txt解析域名验证的name。
        :type TxtName: str
        :param TxtText: txt解析域名验证的text。
        :type TxtText: str
        :param ValidTo: 验证有效期，在此之前有效。
        :type ValidTo: str
        :param VerifyStatus: 验证状态：0-未验证；1-已验证；2-验证失效，待重新验证。
        :type VerifyStatus: int
        :param CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        """
        self.Id = None
        self.Appid = None
        self.VerifyUrl = None
        self.VerifyFileUrl = None
        self.Domain = None
        self.TxtName = None
        self.TxtText = None
        self.ValidTo = None
        self.VerifyStatus = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Appid = params.get("Appid")
        self.VerifyUrl = params.get("VerifyUrl")
        self.VerifyFileUrl = params.get("VerifyFileUrl")
        self.Domain = params.get("Domain")
        self.TxtName = params.get("TxtName")
        self.TxtText = params.get("TxtText")
        self.ValidTo = params.get("ValidTo")
        self.VerifyStatus = params.get("VerifyStatus")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")


class VerifySitesRequest(AbstractModel):
    """VerifySites请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 站点的url列表
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class VerifySitesResponse(AbstractModel):
    """VerifySites返回参数结构体

    """

    def __init__(self):
        """
        :param SuccessNumber: 验证成功的根域名数量。
        :type SuccessNumber: int
        :param FailNumber: 验证失败的根域名数量。
        :type FailNumber: int
        :param RequestId: 唯一请求ID，每次请求都会返回。定位问题时需要提供该次请求的RequestId。
        :type RequestId: str
        """
        self.SuccessNumber = None
        self.FailNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SuccessNumber = params.get("SuccessNumber")
        self.FailNumber = params.get("FailNumber")
        self.RequestId = params.get("RequestId")


class Vul(AbstractModel):
    """漏洞数据

    """

    def __init__(self):
        """
        :param IsReported: 是否已经添加误报，0-否，1-是。
        :type IsReported: int
        :param Appid: 云用户appid。
        :type Appid: int
        :param Uin: 云用户标识。
        :type Uin: str
        :param Id: 漏洞ID。
        :type Id: int
        :param SiteId: 站点ID。
        :type SiteId: int
        :param TaskId: 扫描引擎的扫描任务ID。
        :type TaskId: int
        :param Level: 漏洞级别：high、middle、low、notice。
        :type Level: str
        :param Name: 漏洞名称。
        :type Name: str
        :param Url: 出现漏洞的url。
        :type Url: str
        :param Html: 网址/细节。
        :type Html: str
        :param Nickname: 漏洞类型。
        :type Nickname: str
        :param Harm: 危害说明。
        :type Harm: str
        :param Describe: 漏洞描述。
        :type Describe: str
        :param Solution: 解决方案。
        :type Solution: str
        :param From: 漏洞参考。
        :type From: str
        :param Parameter: 漏洞通过该参数攻击。
        :type Parameter: str
        :param CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        """
        self.IsReported = None
        self.Appid = None
        self.Uin = None
        self.Id = None
        self.SiteId = None
        self.TaskId = None
        self.Level = None
        self.Name = None
        self.Url = None
        self.Html = None
        self.Nickname = None
        self.Harm = None
        self.Describe = None
        self.Solution = None
        self.From = None
        self.Parameter = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.IsReported = params.get("IsReported")
        self.Appid = params.get("Appid")
        self.Uin = params.get("Uin")
        self.Id = params.get("Id")
        self.SiteId = params.get("SiteId")
        self.TaskId = params.get("TaskId")
        self.Level = params.get("Level")
        self.Name = params.get("Name")
        self.Url = params.get("Url")
        self.Html = params.get("Html")
        self.Nickname = params.get("Nickname")
        self.Harm = params.get("Harm")
        self.Describe = params.get("Describe")
        self.Solution = params.get("Solution")
        self.From = params.get("From")
        self.Parameter = params.get("Parameter")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")


class VulsTimeline(AbstractModel):
    """用户漏洞数随时间变化统计数据

    """

    def __init__(self):
        """
        :param Id: ID。
        :type Id: int
        :param Appid: 云用户appid。
        :type Appid: int
        :param Date: 日期。
        :type Date: str
        :param PageCount: 扫描页面总数量。
        :type PageCount: int
        :param SiteNum: 已验证网站总数量。
        :type SiteNum: int
        :param ImpactSiteNum: 受影响的网站总数量。
        :type ImpactSiteNum: int
        :param VulsHighNum: 高危漏洞总数量。
        :type VulsHighNum: int
        :param VulsMiddleNum: 中危漏洞总数量。
        :type VulsMiddleNum: int
        :param VulsLowNum: 低危漏洞总数量。
        :type VulsLowNum: int
        :param VulsNoticeNum: 风险提示总数量
        :type VulsNoticeNum: int
        :param CreatedAt: 记录添加时间。
        :type CreatedAt: str
        :param UpdatedAt: 记录最近修改时间。
        :type UpdatedAt: str
        """
        self.Id = None
        self.Appid = None
        self.Date = None
        self.PageCount = None
        self.SiteNum = None
        self.ImpactSiteNum = None
        self.VulsHighNum = None
        self.VulsMiddleNum = None
        self.VulsLowNum = None
        self.VulsNoticeNum = None
        self.CreatedAt = None
        self.UpdatedAt = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Appid = params.get("Appid")
        self.Date = params.get("Date")
        self.PageCount = params.get("PageCount")
        self.SiteNum = params.get("SiteNum")
        self.ImpactSiteNum = params.get("ImpactSiteNum")
        self.VulsHighNum = params.get("VulsHighNum")
        self.VulsMiddleNum = params.get("VulsMiddleNum")
        self.VulsLowNum = params.get("VulsLowNum")
        self.VulsNoticeNum = params.get("VulsNoticeNum")
        self.CreatedAt = params.get("CreatedAt")
        self.UpdatedAt = params.get("UpdatedAt")