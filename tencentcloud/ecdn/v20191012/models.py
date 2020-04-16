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


class AddEcdnDomainRequest(AbstractModel):
    """AddEcdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名。
        :type Domain: str
        :param Origin: 源站配置。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param Area: 域名加速区域，mainland，overseas或global，分别表示中国境内加速，海外加速或全球加速。
        :type Area: str
        :param ProjectId: 项目id，默认0。
        :type ProjectId: int
        :param IpFilter: IP黑白名单配置。
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP限频配置。
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: 源站响应头部配置。
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: 节点缓存配置。
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: 缓存规则配置。
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param Https: Https配置。
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param ForceRedirect: 访问协议强制跳转配置。
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        """
        self.Domain = None
        self.Origin = None
        self.Area = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.ForceRedirect = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Area = params.get("Area")
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))


class AddEcdnDomainResponse(AbstractModel):
    """AddEcdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Cache(AbstractModel):
    """缓存配置简单版本，该版本不支持设置源站未返回max-age情况下的缓存规则。

    """

    def __init__(self):
        """
        :param CacheRules: 缓存配置规则数组。
        :type CacheRules: list of CacheRule
        :param FollowOrigin: 遵循源站 Cache-Control: max-age 配置
on：开启
off：关闭
开启后，未能匹配 CacheRules 规则的资源将根据源站返回的 max-age 值进行节点缓存；匹配了 CacheRules 规则的资源将按照 CacheRules 中设置的缓存过期时间在节点进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self.CacheRules = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = CacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")


class CacheKey(AbstractModel):
    """缓存相关配置。

    """

    def __init__(self):
        """
        :param FullUrlCache: 是否开启全路径缓存，on或off。
        :type FullUrlCache: str
        """
        self.FullUrlCache = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")


class CacheRule(AbstractModel):
    """缓存配置规则。

    """

    def __init__(self):
        """
        :param CacheType: 缓存类型，支持all，file，directory，path，index，分别表示全部文件，后缀类型，目录，完整路径，首页。
        :type CacheType: str
        :param CacheContents: 缓存内容列表。
        :type CacheContents: list of str
        :param CacheTime: 缓存时间，单位秒。
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")


class ClientCert(AbstractModel):
    """https客户端证书配置。

    """

    def __init__(self):
        """
        :param Certificate: 客户端证书，pem格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param CertName: 客户端证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书颁发时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        """
        self.Certificate = None
        self.CertName = None
        self.ExpireTime = None
        self.DeployTime = None


    def _deserialize(self, params):
        self.Certificate = params.get("Certificate")
        self.CertName = params.get("CertName")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")


class DeleteEcdnDomainRequest(AbstractModel):
    """DeleteEcdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 待删除域名。
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class DeleteEcdnDomainResponse(AbstractModel):
    """DeleteEcdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询的偏移地址，默认0。
        :type Offset: int
        :param Limit: 分页查询的域名个数，默认100。
        :type Limit: int
        :param Filters: 查询条件过滤器。
        :type Filters: list of DomainFilter
        :param Sort: 查询结果排序规则。
        :type Sort: :class:`tencentcloud.ecdn.v20191012.models.Sort`
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.Sort = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("Sort") is not None:
            self.Sort = Sort()
            self.Sort._deserialize(params.get("Sort"))


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表。
        :type Domains: list of DomainDetailInfo
        :param TotalCount: 符合查询条件的域名总数，用于分页查询。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询的偏移地址，默认0。
        :type Offset: int
        :param Limit: 分页查询的域名个数，默认100，最大支持1000。
        :type Limit: int
        :param Filters: 查询条件过滤器。
        :type Filters: list of DomainFilter
        """
        self.Offset = None
        self.Limit = None
        self.Filters = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self.Filters.append(obj)


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名信息列表。
        :type Domains: list of DomainBriefInfo
        :param TotalCount: 域名总个数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DomainBriefInfo()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEcdnDomainLogsRequest(AbstractModel):
    """DescribeEcdnDomainLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 待查询域名。
        :type Domain: str
        :param StartTime: 日志起始时间。如：2019-10-01 00:00:00
        :type StartTime: str
        :param EndTime: 日志结束时间，只支持最近30天内日志查询。2019-10-02 00:00:00
        :type EndTime: str
        :param Offset: 日志链接列表分页起始地址，默认0。
        :type Offset: int
        :param Limit: 日志链接列表分页记录条数，默认100，最大1000。
        :type Limit: int
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeEcdnDomainLogsResponse(AbstractModel):
    """DescribeEcdnDomainLogs返回参数结构体

    """

    def __init__(self):
        """
        :param DomainLogs: 日志链接列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainLogs: list of DomainLogs
        :param TotalCount: 日志链接总条数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self.DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLogs()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEcdnDomainStatisticsRequest(AbstractModel):
    """DescribeEcdnDomainStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2019-12-13 00:00:00。
起止时间不超过90天。
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2019-12-13 23:59:59。
起止时间不超过90天。
        :type EndTime: str
        :param Metrics: 统计指标名称。flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
delay：响应时间，单位为ms
static_request ： 静态请求数，单位为 次
static_flux：静态流量，单位为 byte
static_bandwidth ： 静态带宽，单位为 bps
dynamic_request：动态请求数，单位为 次
dynamic_flux：动态流量，单位为 byte
dynamic_bandwidth：动态带宽，单位为 bps
        :type Metrics: list of str
        :param Domains: 指定查询域名列表
        :type Domains: list of str
        :param Projects: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Projects: list of int
        :param Offset: 列表分页起始地址，默认0。
        :type Offset: int
        :param Limit: 列表分页记录条数，默认1000，最大3000。
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Metrics = None
        self.Domains = None
        self.Projects = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metrics = params.get("Metrics")
        self.Domains = params.get("Domains")
        self.Projects = params.get("Projects")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")


class DescribeEcdnDomainStatisticsResponse(AbstractModel):
    """DescribeEcdnDomainStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 域名数据
        :type Data: list of DomainData
        :param TotalCount: 数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DomainData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeEcdnStatisticsRequest(AbstractModel):
    """DescribeEcdnStatistics请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2019-12-13 00:00:00
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2019-12-13 23:59:59
        :type EndTime: str
        :param Metrics: 指定查询指标，支持的类型有：
flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
delay：响应时间，单位为ms
2xx：返回 2xx 状态码汇总或者 2 开头状态码数据，单位为 个
3xx：返回 3xx 状态码汇总或者 3 开头状态码数据，单位为 个
4xx：返回 4xx 状态码汇总或者 4 开头状态码数据，单位为 个
5xx：返回 5xx 状态码汇总或者 5 开头状态码数据，单位为 个
static_request ： 静态请求数，单位为 次
static_flux：静态流量，单位为 byte
static_bandwidth ： 静态带宽，单位为 bps
dynamic_request：动态请求数，单位为 次
dynamic_flux：动态流量，单位为 byte
dynamic_bandwidth：动态带宽，单位为 bps
        :type Metrics: list of str
        :param Interval: 时间粒度，支持以下几种模式：
1 天	 1，5，15，30，60，120，240，1440 
2 ~ 3 天	15，30，60，120，240，1440
4 ~ 7 天	30，60，120，240，1440
8 ~ 90 天	 60，120，240，1440
        :type Interval: int
        :param Domains: 指定查询域名列表

最多可一次性查询30个加速域名。
        :type Domains: list of str
        :param Projects: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Projects: list of int
        """
        self.StartTime = None
        self.EndTime = None
        self.Metrics = None
        self.Interval = None
        self.Domains = None
        self.Projects = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metrics = params.get("Metrics")
        self.Interval = params.get("Interval")
        self.Domains = params.get("Domains")
        self.Projects = params.get("Projects")


class DescribeEcdnStatisticsResponse(AbstractModel):
    """DescribeEcdnStatistics返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 指定条件查询得到的数据明细
        :type Data: list of ResourceData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota请求参数结构体

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param UrlPurge: Url刷新用量及配额。
        :type UrlPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param PathPurge: 目录刷新用量及配额。
        :type PathPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UrlPurge = None
        self.PathPurge = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self.UrlPurge = Quota()
            self.UrlPurge._deserialize(params.get("UrlPurge"))
        if params.get("PathPurge") is not None:
            self.PathPurge = Quota()
            self.PathPurge._deserialize(params.get("PathPurge"))
        self.RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param PurgeType: 查询刷新类型。url：查询 url 刷新记录；path：查询目录刷新记录。
        :type PurgeType: str
        :param StartTime: 开始时间，如2018-08-08 00:00:00。
        :type StartTime: str
        :param EndTime: 结束时间，如2018-08-08 23:59:59。
        :type EndTime: str
        :param TaskId: 提交时返回的任务 Id，查询时 TaskId 和起始时间必须指定一项。
        :type TaskId: str
        :param Offset: 分页查询偏移量，默认为0（从第0条开始）。
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为20。
        :type Limit: int
        :param Keyword: 查询关键字，请输入域名或 http(s):// 开头完整 URL。
        :type Keyword: str
        :param Status: 查询指定任务状态，fail表示失败，done表示成功，process表示刷新中。
        :type Status: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param PurgeLogs: 刷新历史记录。
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: 任务总数，用于分页。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PurgeLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PurgeLogs") is not None:
            self.PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self.PurgeLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DetailData(AbstractModel):
    """排序类型的数据结构

    """

    def __init__(self):
        """
        :param Name: 数据类型的名称
        :type Name: str
        :param Value: 数据值
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")


class DomainBriefInfo(AbstractModel):
    """CDN域名简要信息。

    """

    def __init__(self):
        """
        :param ResourceId: 域名ID。
        :type ResourceId: str
        :param AppId: 腾讯云账号ID。
        :type AppId: int
        :param Domain: CDN加速域名。
        :type Domain: str
        :param Cname: 域名CName。
        :type Cname: str
        :param Status: 域名状态，pending，rejected，processing， online，offline，deleted分别表示审核中，审核未通过，审核通过部署中，已开启，已关闭，已删除。
        :type Status: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param CreateTime: 域名创建时间。
        :type CreateTime: str
        :param UpdateTime: 域名更新时间。
        :type UpdateTime: str
        :param Origin: 源站配置详情。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param Disable: 域名封禁状态，normal，overdue，quota，malicious，ddos，idle，unlicensed，capping，readonly分别表示 正常，欠费停服，试用客户流量包耗尽，恶意用户，ddos攻击，无流量域名，未备案，带宽封顶，只读
        :type Disable: str
        :param Area: 加速区域，mainland，oversea或global。
        :type Area: str
        :param Readonly: 域名锁定状态，normal、global，分别表示未被锁定、全球锁定。
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.Disable = None
        self.Area = None
        self.Readonly = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")


class DomainData(AbstractModel):
    """排序类型数据结构

    """

    def __init__(self):
        """
        :param Resource: 域名
        :type Resource: str
        :param DetailData: 结果详情
        :type DetailData: list of DetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = DetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)


class DomainDetailInfo(AbstractModel):
    """ECDN域名详细配置信息。

    """

    def __init__(self):
        """
        :param ResourceId: 域名ID。
        :type ResourceId: str
        :param AppId: 腾讯云账号ID。
        :type AppId: int
        :param Domain: 加速域名。
        :type Domain: str
        :param Cname: 域名CName。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Status: 域名状态，pending，rejected，processing， online，offline，deleted分别表示审核中，审核未通过，审核通过部署中，已开启，已关闭，已删除。
        :type Status: str
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param CreateTime: 域名创建时间。
        :type CreateTime: str
        :param UpdateTime: 域名更新时间。
        :type UpdateTime: str
        :param Origin: 源站配置。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: 节点缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param Disable: 域名封禁状态，normal，overdue，quota，malicious，ddos，idle，unlicensed，capping，readonly分别表示 正常，欠费停服，试用客户流量包耗尽，恶意用户，ddos攻击，无流量域名，未备案，带宽封顶，只读。
注意：此字段可能返回 null，表示取不到有效值。
        :type Disable: str
        :param ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param Area: 加速区域，mainland，overseas或global。
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param Readonly: 域名锁定状态，normal、global 分别表示未被锁定，全球锁定。
注意：此字段可能返回 null，表示取不到有效值。
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.Disable = None
        self.ForceRedirect = None
        self.Area = None
        self.Readonly = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")


class DomainFilter(AbstractModel):
    """域名查询时过滤条件。

    """

    def __init__(self):
        """
        :param Name: 过滤字段名，支持的列表如下：
- origin：主源站。
- domain：域名。
- resourceId：域名id。
- status：域名状态，online，offline，processing。
- disable：域名封禁状态，normal，unlicensed。
- projectId：项目ID。
- fullUrlCache：全路径缓存，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源协议类型，支持http，follow或https。
- area：加速区域，支持mainland，overseas或global。
        :type Name: str
        :param Value: 过滤字段值。
        :type Value: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为origin，domain。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Value = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Fuzzy = params.get("Fuzzy")


class DomainLogs(AbstractModel):
    """域名日志信息

    """

    def __init__(self):
        """
        :param StartTime: 日志起始时间。
        :type StartTime: str
        :param EndTime: 日志结束时间。
        :type EndTime: str
        :param LogPath: 日志下载路径。
        :type LogPath: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")


class EcdnData(AbstractModel):
    """访问明细数据类型

    """

    def __init__(self):
        """
        :param Metrics: 查询指定的指标名称：Bandwidth，Flux，Request，Delay，状态码，LogBandwidth，LogFlux，LogRequest
        :type Metrics: list of str
        :param DetailData: 明细数据组合
        :type DetailData: list of TimestampData
        """
        self.Metrics = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Metrics = params.get("Metrics")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)


class ForceRedirect(AbstractModel):
    """访问协议强制跳转配置。

    """

    def __init__(self):
        """
        :param Switch: 访问协议强制跳转配置开关，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param RedirectType: 强制跳转访问协议类型，支持http，https，分别表示请求强制跳转http协议，请求强制跳转https协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectType: str
        :param RedirectStatusCode: 强制跳转开启时返回的http状态码，支持301或302。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self.Switch = None
        self.RedirectType = None
        self.RedirectStatusCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectType = params.get("RedirectType")
        self.RedirectStatusCode = params.get("RedirectStatusCode")


class HttpHeaderPathRule(AbstractModel):
    """分路径的http头部设置规则。

    """

    def __init__(self):
        """
        :param HeaderMode: http头部设置方式，支持add，set或del，分别表示新增，设置或删除头部。
请求头部暂不支持set。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderMode: str
        :param HeaderName: http头部名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        :param HeaderValue: http头部值。del时可不填写该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderValue: str
        :param RuleType: 生效的url路径规则类型，支持all，file，directory或path，分别表示全部路径，文件后缀类型，目录或绝对路径生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RulePaths: url路径或文件类型列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self.HeaderMode = None
        self.HeaderName = None
        self.HeaderValue = None
        self.RuleType = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.HeaderMode = params.get("HeaderMode")
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")


class Https(AbstractModel):
    """域名https配置。

    """

    def __init__(self):
        """
        :param Switch: https配置开关，on或off。开启https配置的域名在部署中状态，开关保持off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Http2: 是否开启http2，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: 是否开启OCSP功能，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param VerifyClient: 是否开启客户端证书校验功能，on或off，开启时必选上传客户端证书信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyClient: str
        :param CertInfo: 服务器证书配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        :param ClientCertInfo: 客户端证书配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        :param Spdy: 是否开启Spdy，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Spdy: str
        :param SslStatus: https证书部署状态，closed，deploying，deployed，failed分别表示已关闭，部署中，部署成功，部署失败。不可作为入参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type SslStatus: str
        """
        self.Switch = None
        self.Http2 = None
        self.OcspStapling = None
        self.VerifyClient = None
        self.CertInfo = None
        self.ClientCertInfo = None
        self.Spdy = None
        self.SslStatus = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Http2 = params.get("Http2")
        self.OcspStapling = params.get("OcspStapling")
        self.VerifyClient = params.get("VerifyClient")
        if params.get("CertInfo") is not None:
            self.CertInfo = ServerCert()
            self.CertInfo._deserialize(params.get("CertInfo"))
        if params.get("ClientCertInfo") is not None:
            self.ClientCertInfo = ClientCert()
            self.ClientCertInfo._deserialize(params.get("ClientCertInfo"))
        self.Spdy = params.get("Spdy")
        self.SslStatus = params.get("SslStatus")


class IpFilter(AbstractModel):
    """IP黑白名单。

    """

    def __init__(self):
        """
        :param Switch: IP黑白名单开关，on或off。
        :type Switch: str
        :param FilterType: IP黑白名单类型，whitelist或blacklist。
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param Filters: IP黑白名单列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of str
        """
        self.Switch = None
        self.FilterType = None
        self.Filters = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")


class IpFreqLimit(AbstractModel):
    """IP限频配置。

    """

    def __init__(self):
        """
        :param Switch: IP限频配置开关，on或off。
        :type Switch: str
        :param Qps: 每秒请求数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        """
        self.Switch = None
        self.Qps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Qps = params.get("Qps")


class Origin(AbstractModel):
    """源站配置。

    """

    def __init__(self):
        """
        :param Origins: 主源站列表，默认格式为 ["ip1:port1", "ip2:port2"]。
支持在源站列表中配置权重，配置IP源站权重格式为 ["ip1:port1:weight1", "ip2:port2:weight2"]。
        :type Origins: list of str
        :param OriginType: 主源站类型，支持domain，ip，分别表示域名源站，ip源站。
设置Origins时必须填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ServerName: 回源时Host头部值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param OriginPullProtocol: 回源协议类型，支持http，follow，https，分别表示强制http回源，协议跟随回源，https回源。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param BackupOrigins: 备份源站列表。
        :type BackupOrigins: list of str
        :param BackupOriginType: 备份源站类型，同OriginType。
设置BackupOrigins时必须填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOriginType: str
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache请求参数结构体

    """

    def __init__(self):
        """
        :param Paths: 要刷新的目录列表，必须包含协议头部。
        :type Paths: list of str
        :param FlushType: 刷新类型，flush 代表刷新有更新的资源，delete 表示刷新全部资源。
        :type FlushType: str
        """
        self.Paths = None
        self.FlushType = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务Id，前十位为提交任务时的UTC时间。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """刷新任务日志详情

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务ID。
        :type TaskId: str
        :param Url: 刷新Url。
        :type Url: str
        :param Status: 刷新任务状态，fail表示失败，done表示成功，process表示刷新中。
        :type Status: str
        :param PurgeType: 刷新类型，url表示url刷新，path表示目录刷新。
        :type PurgeType: str
        :param FlushType: 刷新资源方式，flush代表刷新更新资源，delete代表刷新全部资源。
        :type FlushType: str
        :param CreateTime: 刷新任务提交时间
        :type CreateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.PurgeType = None
        self.FlushType = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.PurgeType = params.get("PurgeType")
        self.FlushType = params.get("FlushType")
        self.CreateTime = params.get("CreateTime")


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 要刷新的Url列表，必须包含协议头部。
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务Id，前十位为提交任务时的UTC时间。
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """刷新用量及刷新配额

    """

    def __init__(self):
        """
        :param Batch: 单次批量提交配额上限。
        :type Batch: int
        :param Total: 每日提交配额上限。
        :type Total: int
        :param Available: 每日剩余的可提交配额。
        :type Available: int
        """
        self.Batch = None
        self.Total = None
        self.Available = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Total = params.get("Total")
        self.Available = params.get("Available")


class ResourceData(AbstractModel):
    """查询对象及其对应的访问明细数据

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :type Resource: str
        :param EcdnData: 资源对应的数据明细
        :type EcdnData: :class:`tencentcloud.ecdn.v20191012.models.EcdnData`
        """
        self.Resource = None
        self.EcdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("EcdnData") is not None:
            self.EcdnData = EcdnData()
            self.EcdnData._deserialize(params.get("EcdnData"))


class ResponseHeader(AbstractModel):
    """自定义响应头配置。

    """

    def __init__(self):
        """
        :param Switch: 自定义响应头开关，on或off。
        :type Switch: str
        :param HeaderRules: 自定义响应头规则数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self.Switch = None
        self.HeaderRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self.HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self.HeaderRules.append(obj)


class ServerCert(AbstractModel):
    """https服务端证书配置。

    """

    def __init__(self):
        """
        :param CertId: 服务器证书id，当证书为腾讯云托管证书时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param CertName: 服务器证书名称，当证书为腾讯云托管证书时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param Certificate: 服务器证书信息，上传自有证书时必填，必须包含完整的证书链信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param PrivateKey: 服务器密钥信息，上传自有证书时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书颁发时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Message: 证书备注信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self.CertId = None
        self.CertName = None
        self.Certificate = None
        self.PrivateKey = None
        self.ExpireTime = None
        self.DeployTime = None
        self.Message = None


    def _deserialize(self, params):
        self.CertId = params.get("CertId")
        self.CertName = params.get("CertName")
        self.Certificate = params.get("Certificate")
        self.PrivateKey = params.get("PrivateKey")
        self.ExpireTime = params.get("ExpireTime")
        self.DeployTime = params.get("DeployTime")
        self.Message = params.get("Message")


class Sort(AbstractModel):
    """查询结果排序条件。

    """

    def __init__(self):
        """
        :param Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
        :type Key: str
        :param Sequence: asc/desc，默认desc。
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")


class StartEcdnDomainRequest(AbstractModel):
    """StartEcdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 待启用域名。
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StartEcdnDomainResponse(AbstractModel):
    """StartEcdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopEcdnDomainRequest(AbstractModel):
    """StopEcdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 待停用域名。
        :type Domain: str
        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")


class StopEcdnDomainResponse(AbstractModel):
    """StopEcdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class TimestampData(AbstractModel):
    """时间戳与其对应的数值

    """

    def __init__(self):
        """
        :param Time: 数据统计时间点，采用向前汇总模式
以 5 分钟粒度为例，13:35:00 时间点代表的统计数据区间为 13:35:00 至 13:39:59
        :type Time: str
        :param Value: 数据值
        :type Value: list of float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名。
        :type Domain: str
        :param Origin: 源站配置。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param ProjectId: 项目id。
        :type ProjectId: int
        :param IpFilter: IP黑白名单配置。
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param IpFreqLimit: IP限频配置。
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param ResponseHeader: 源站响应头部配置。
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param CacheKey: 节点缓存配置。
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param Cache: 缓存规则配置。
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param Https: Https配置。
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param ForceRedirect: 访问协议强制跳转配置。
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param Area: 域名加速区域，mainland，overseas或global，分别表示中国境内加速，海外加速或全球加速。
        :type Area: str
        """
        self.Domain = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.ResponseHeader = None
        self.CacheKey = None
        self.Cache = None
        self.Https = None
        self.ForceRedirect = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        self.Area = params.get("Area")


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")