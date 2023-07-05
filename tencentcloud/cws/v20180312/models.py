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


class CreateMonitorsRequest(AbstractModel):
    """CreateMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 站点的url列表
        :type Urls: list of str
        :param _Name: 任务名称
        :type Name: str
        :param _ScannerType: 扫描模式，normal-正常扫描；deep-深度扫描
        :type ScannerType: str
        :param _Crontab: 扫描周期，单位小时，每X小时执行一次
        :type Crontab: int
        :param _RateLimit: 扫描速率限制，每秒发送X个HTTP请求
        :type RateLimit: int
        :param _FirstScanStartTime: 首次扫描开始时间
        :type FirstScanStartTime: str
        """
        self._Urls = None
        self._Name = None
        self._ScannerType = None
        self._Crontab = None
        self._RateLimit = None
        self._FirstScanStartTime = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ScannerType(self):
        return self._ScannerType

    @ScannerType.setter
    def ScannerType(self, ScannerType):
        self._ScannerType = ScannerType

    @property
    def Crontab(self):
        return self._Crontab

    @Crontab.setter
    def Crontab(self, Crontab):
        self._Crontab = Crontab

    @property
    def RateLimit(self):
        return self._RateLimit

    @RateLimit.setter
    def RateLimit(self, RateLimit):
        self._RateLimit = RateLimit

    @property
    def FirstScanStartTime(self):
        return self._FirstScanStartTime

    @FirstScanStartTime.setter
    def FirstScanStartTime(self, FirstScanStartTime):
        self._FirstScanStartTime = FirstScanStartTime


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._Name = params.get("Name")
        self._ScannerType = params.get("ScannerType")
        self._Crontab = params.get("Crontab")
        self._RateLimit = params.get("RateLimit")
        self._FirstScanStartTime = params.get("FirstScanStartTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateMonitorsResponse(AbstractModel):
    """CreateMonitors返回参数结构体

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


class CreateSitesRequest(AbstractModel):
    """CreateSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 站点的url列表
        :type Urls: list of str
        :param _UserAgent: 访问网站的客户端标识
        :type UserAgent: str
        """
        self._Urls = None
        self._UserAgent = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._UserAgent = params.get("UserAgent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSitesResponse(AbstractModel):
    """CreateSites返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Number: 新增站点数。
        :type Number: int
        :param _Sites: 站点数组
        :type Sites: list of MiniSite
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Number = None
        self._Sites = None
        self._RequestId = None

    @property
    def Number(self):
        return self._Number

    @Number.setter
    def Number(self, Number):
        self._Number = Number

    @property
    def Sites(self):
        return self._Sites

    @Sites.setter
    def Sites(self, Sites):
        self._Sites = Sites

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Number = params.get("Number")
        if params.get("Sites") is not None:
            self._Sites = []
            for item in params.get("Sites"):
                obj = MiniSite()
                obj._deserialize(item)
                self._Sites.append(obj)
        self._RequestId = params.get("RequestId")


class CreateSitesScansRequest(AbstractModel):
    """CreateSitesScans请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteIds: 站点的ID列表
        :type SiteIds: list of int non-negative
        :param _ScannerType: 扫描模式，normal-正常扫描；deep-深度扫描
        :type ScannerType: str
        :param _RateLimit: 扫描速率限制，每秒发送X个HTTP请求
        :type RateLimit: int
        """
        self._SiteIds = None
        self._ScannerType = None
        self._RateLimit = None

    @property
    def SiteIds(self):
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def ScannerType(self):
        return self._ScannerType

    @ScannerType.setter
    def ScannerType(self, ScannerType):
        self._ScannerType = ScannerType

    @property
    def RateLimit(self):
        return self._RateLimit

    @RateLimit.setter
    def RateLimit(self, RateLimit):
        self._RateLimit = RateLimit


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        self._ScannerType = params.get("ScannerType")
        self._RateLimit = params.get("RateLimit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSitesScansResponse(AbstractModel):
    """CreateSitesScans返回参数结构体

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


class CreateVulsMisinformationRequest(AbstractModel):
    """CreateVulsMisinformation请求参数结构体

    """

    def __init__(self):
        r"""
        :param _VulIds: 漏洞ID列表
        :type VulIds: list of int non-negative
        """
        self._VulIds = None

    @property
    def VulIds(self):
        return self._VulIds

    @VulIds.setter
    def VulIds(self, VulIds):
        self._VulIds = VulIds


    def _deserialize(self, params):
        self._VulIds = params.get("VulIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVulsMisinformationResponse(AbstractModel):
    """CreateVulsMisinformation返回参数结构体

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


class CreateVulsReportRequest(AbstractModel):
    """CreateVulsReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 站点ID
        :type SiteId: int
        :param _MonitorId: 监控任务ID
        :type MonitorId: int
        """
        self._SiteId = None
        self._MonitorId = None

    @property
    def SiteId(self):
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._MonitorId = params.get("MonitorId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVulsReportResponse(AbstractModel):
    """CreateVulsReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportFileUrl: 报告下载地址
        :type ReportFileUrl: str
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ReportFileUrl = None
        self._RequestId = None

    @property
    def ReportFileUrl(self):
        return self._ReportFileUrl

    @ReportFileUrl.setter
    def ReportFileUrl(self, ReportFileUrl):
        self._ReportFileUrl = ReportFileUrl

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ReportFileUrl = params.get("ReportFileUrl")
        self._RequestId = params.get("RequestId")


class DeleteMonitorsRequest(AbstractModel):
    """DeleteMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorIds: 监控任务ID列表
        :type MonitorIds: list of int non-negative
        """
        self._MonitorIds = None

    @property
    def MonitorIds(self):
        return self._MonitorIds

    @MonitorIds.setter
    def MonitorIds(self, MonitorIds):
        self._MonitorIds = MonitorIds


    def _deserialize(self, params):
        self._MonitorIds = params.get("MonitorIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteMonitorsResponse(AbstractModel):
    """DeleteMonitors返回参数结构体

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


class DeleteSitesRequest(AbstractModel):
    """DeleteSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteIds: 站点ID列表
        :type SiteIds: list of int non-negative
        """
        self._SiteIds = None

    @property
    def SiteIds(self):
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds


    def _deserialize(self, params):
        self._SiteIds = params.get("SiteIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSitesResponse(AbstractModel):
    """DeleteSites返回参数结构体

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


class DescribeConfigRequest(AbstractModel):
    """DescribeConfig请求参数结构体

    """


class DescribeConfigResponse(AbstractModel):
    """DescribeConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeLevel: 漏洞告警通知等级，4位分别代表：高危、中危、低危、提示。
        :type NoticeLevel: str
        :param _Id: 配置ID。
        :type Id: int
        :param _CreatedAt: 记录创建时间。
        :type CreatedAt: str
        :param _UpdatedAt: 记录更新新建。
        :type UpdatedAt: str
        :param _Appid: 云用户appid。
        :type Appid: int
        :param _ContentLevel: 内容检测通知等级-1:通知,0-不通知
        :type ContentLevel: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._NoticeLevel = None
        self._Id = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Appid = None
        self._ContentLevel = None
        self._RequestId = None

    @property
    def NoticeLevel(self):
        return self._NoticeLevel

    @NoticeLevel.setter
    def NoticeLevel(self, NoticeLevel):
        self._NoticeLevel = NoticeLevel

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def ContentLevel(self):
        return self._ContentLevel

    @ContentLevel.setter
    def ContentLevel(self, ContentLevel):
        self._ContentLevel = ContentLevel

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._NoticeLevel = params.get("NoticeLevel")
        self._Id = params.get("Id")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Appid = params.get("Appid")
        self._ContentLevel = params.get("ContentLevel")
        self._RequestId = params.get("RequestId")


class DescribeMonitorsRequest(AbstractModel):
    """DescribeMonitors请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorIds: 监控任务ID列表
        :type MonitorIds: list of int non-negative
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为10，最大值为100
        :type Limit: int
        """
        self._MonitorIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def MonitorIds(self):
        return self._MonitorIds

    @MonitorIds.setter
    def MonitorIds(self, MonitorIds):
        self._MonitorIds = MonitorIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._MonitorIds = params.get("MonitorIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMonitorsResponse(AbstractModel):
    """DescribeMonitors返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Monitors: 监控任务列表。
        :type Monitors: list of MonitorsDetail
        :param _TotalCount: 监控任务数量。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Monitors = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Monitors(self):
        return self._Monitors

    @Monitors.setter
    def Monitors(self, Monitors):
        self._Monitors = Monitors

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
        if params.get("Monitors") is not None:
            self._Monitors = []
            for item in params.get("Monitors"):
                obj = MonitorsDetail()
                obj._deserialize(item)
                self._Monitors.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeSiteQuotaRequest(AbstractModel):
    """DescribeSiteQuota请求参数结构体

    """


class DescribeSiteQuotaResponse(AbstractModel):
    """DescribeSiteQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Total: 已购买的扫描次数。
        :type Total: int
        :param _Used: 已使用的扫描次数。
        :type Used: int
        :param _Available: 剩余可用的扫描次数。
        :type Available: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Total = None
        self._Used = None
        self._Available = None
        self._RequestId = None

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Used(self):
        return self._Used

    @Used.setter
    def Used(self, Used):
        self._Used = Used

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Total = params.get("Total")
        self._Used = params.get("Used")
        self._Available = params.get("Available")
        self._RequestId = params.get("RequestId")


class DescribeSitesRequest(AbstractModel):
    """DescribeSites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteIds: 站点ID列表
        :type SiteIds: list of int non-negative
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为10，最大值为100
        :type Limit: int
        """
        self._SiteIds = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SiteIds(self):
        return self._SiteIds

    @SiteIds.setter
    def SiteIds(self, SiteIds):
        self._SiteIds = SiteIds

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._SiteIds = params.get("SiteIds")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesResponse(AbstractModel):
    """DescribeSites返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 站点数量。
        :type TotalCount: int
        :param _Sites: 站点信息列表。
        :type Sites: list of Site
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Sites = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Sites(self):
        return self._Sites

    @Sites.setter
    def Sites(self, Sites):
        self._Sites = Sites

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Sites") is not None:
            self._Sites = []
            for item in params.get("Sites"):
                obj = Site()
                obj._deserialize(item)
                self._Sites.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeSitesVerificationRequest(AbstractModel):
    """DescribeSitesVerification请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 站点的url列表
        :type Urls: list of str
        """
        self._Urls = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSitesVerificationResponse(AbstractModel):
    """DescribeSitesVerification返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 验证信息数量。
        :type TotalCount: int
        :param _SitesVerification: 验证信息列表。
        :type SitesVerification: list of SitesVerification
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._SitesVerification = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def SitesVerification(self):
        return self._SitesVerification

    @SitesVerification.setter
    def SitesVerification(self, SitesVerification):
        self._SitesVerification = SitesVerification

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("SitesVerification") is not None:
            self._SitesVerification = []
            for item in params.get("SitesVerification"):
                obj = SitesVerification()
                obj._deserialize(item)
                self._SitesVerification.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulsNumberRequest(AbstractModel):
    """DescribeVulsNumber请求参数结构体

    """


class DescribeVulsNumberResponse(AbstractModel):
    """DescribeVulsNumber返回参数结构体

    """

    def __init__(self):
        r"""
        :param _ImpactSiteNumber: 受影响的网站总数。
        :type ImpactSiteNumber: int
        :param _SiteNumber: 已验证的网站总数。
        :type SiteNumber: int
        :param _VulsHighNumber: 高风险漏洞总数。
        :type VulsHighNumber: int
        :param _VulsMiddleNumber: 中风险漏洞总数。
        :type VulsMiddleNumber: int
        :param _VulsLowNumber: 低高风险漏洞总数。
        :type VulsLowNumber: int
        :param _VulsNoticeNumber: 风险提示总数。
        :type VulsNoticeNumber: int
        :param _PageCount: 扫描页面总数。
        :type PageCount: int
        :param _Sites: 已验证的网站列表。
        :type Sites: list of MonitorMiniSite
        :param _ImpactSites: 受影响的网站列表。
        :type ImpactSites: list of MonitorMiniSite
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._ImpactSiteNumber = None
        self._SiteNumber = None
        self._VulsHighNumber = None
        self._VulsMiddleNumber = None
        self._VulsLowNumber = None
        self._VulsNoticeNumber = None
        self._PageCount = None
        self._Sites = None
        self._ImpactSites = None
        self._RequestId = None

    @property
    def ImpactSiteNumber(self):
        return self._ImpactSiteNumber

    @ImpactSiteNumber.setter
    def ImpactSiteNumber(self, ImpactSiteNumber):
        self._ImpactSiteNumber = ImpactSiteNumber

    @property
    def SiteNumber(self):
        return self._SiteNumber

    @SiteNumber.setter
    def SiteNumber(self, SiteNumber):
        self._SiteNumber = SiteNumber

    @property
    def VulsHighNumber(self):
        return self._VulsHighNumber

    @VulsHighNumber.setter
    def VulsHighNumber(self, VulsHighNumber):
        self._VulsHighNumber = VulsHighNumber

    @property
    def VulsMiddleNumber(self):
        return self._VulsMiddleNumber

    @VulsMiddleNumber.setter
    def VulsMiddleNumber(self, VulsMiddleNumber):
        self._VulsMiddleNumber = VulsMiddleNumber

    @property
    def VulsLowNumber(self):
        return self._VulsLowNumber

    @VulsLowNumber.setter
    def VulsLowNumber(self, VulsLowNumber):
        self._VulsLowNumber = VulsLowNumber

    @property
    def VulsNoticeNumber(self):
        return self._VulsNoticeNumber

    @VulsNoticeNumber.setter
    def VulsNoticeNumber(self, VulsNoticeNumber):
        self._VulsNoticeNumber = VulsNoticeNumber

    @property
    def PageCount(self):
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def Sites(self):
        return self._Sites

    @Sites.setter
    def Sites(self, Sites):
        self._Sites = Sites

    @property
    def ImpactSites(self):
        return self._ImpactSites

    @ImpactSites.setter
    def ImpactSites(self, ImpactSites):
        self._ImpactSites = ImpactSites

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._ImpactSiteNumber = params.get("ImpactSiteNumber")
        self._SiteNumber = params.get("SiteNumber")
        self._VulsHighNumber = params.get("VulsHighNumber")
        self._VulsMiddleNumber = params.get("VulsMiddleNumber")
        self._VulsLowNumber = params.get("VulsLowNumber")
        self._VulsNoticeNumber = params.get("VulsNoticeNumber")
        self._PageCount = params.get("PageCount")
        if params.get("Sites") is not None:
            self._Sites = []
            for item in params.get("Sites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self._Sites.append(obj)
        if params.get("ImpactSites") is not None:
            self._ImpactSites = []
            for item in params.get("ImpactSites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self._ImpactSites.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulsNumberTimelineRequest(AbstractModel):
    """DescribeVulsNumberTimeline请求参数结构体

    """


class DescribeVulsNumberTimelineResponse(AbstractModel):
    """DescribeVulsNumberTimeline返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 统计数据记录数量。
        :type TotalCount: int
        :param _VulsTimeline: 用户漏洞数随时间变化统计数据。
        :type VulsTimeline: list of VulsTimeline
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._VulsTimeline = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def VulsTimeline(self):
        return self._VulsTimeline

    @VulsTimeline.setter
    def VulsTimeline(self, VulsTimeline):
        self._VulsTimeline = VulsTimeline

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("VulsTimeline") is not None:
            self._VulsTimeline = []
            for item in params.get("VulsTimeline"):
                obj = VulsTimeline()
                obj._deserialize(item)
                self._VulsTimeline.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeVulsRequest(AbstractModel):
    """DescribeVuls请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 站点ID
        :type SiteId: int
        :param _MonitorId: 监控任务ID
        :type MonitorId: int
        :param _Filters: 过滤条件
        :type Filters: list of Filter
        :param _Offset: 偏移量，默认为0
        :type Offset: int
        :param _Limit: 返回数量，默认为10，最大值为100
        :type Limit: int
        """
        self._SiteId = None
        self._MonitorId = None
        self._Filters = None
        self._Offset = None
        self._Limit = None

    @property
    def SiteId(self):
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

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
        self._SiteId = params.get("SiteId")
        self._MonitorId = params.get("MonitorId")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeVulsResponse(AbstractModel):
    """DescribeVuls返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 漏洞数量。
        :type TotalCount: int
        :param _Vuls: 漏洞信息列表。
        :type Vuls: list of Vul
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._Vuls = None
        self._RequestId = None

    @property
    def TotalCount(self):
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def Vuls(self):
        return self._Vuls

    @Vuls.setter
    def Vuls(self, Vuls):
        self._Vuls = Vuls

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("Vuls") is not None:
            self._Vuls = []
            for item in params.get("Vuls"):
                obj = Vul()
                obj._deserialize(item)
                self._Vuls.append(obj)
        self._RequestId = params.get("RequestId")


class Filter(AbstractModel):
    """描述键值对过滤器，用于条件过滤查询。例如过滤ID、名称、状态等

    若存在多个Filter时，Filter间的关系为逻辑与（AND）关系。
    若同一个Filter存在多个Values，同一Filter下Values间的关系为逻辑或（OR）关系。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤键的名称。
        :type Name: str
        :param _Values: 一个或者多个过滤值。
        :type Values: list of str
        """
        self._Name = None
        self._Values = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MiniSite(AbstractModel):
    """站点信息。

    """

    def __init__(self):
        r"""
        :param _SiteId: 站点ID。
        :type SiteId: int
        :param _Url: 站点Url。
        :type Url: str
        """
        self._SiteId = None
        self._Url = None

    @property
    def SiteId(self):
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigAttributeRequest(AbstractModel):
    """ModifyConfigAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _NoticeLevel: 漏洞告警通知等级，4位分别代表：高危、中危、低危、提示
        :type NoticeLevel: str
        """
        self._NoticeLevel = None

    @property
    def NoticeLevel(self):
        return self._NoticeLevel

    @NoticeLevel.setter
    def NoticeLevel(self, NoticeLevel):
        self._NoticeLevel = NoticeLevel


    def _deserialize(self, params):
        self._NoticeLevel = params.get("NoticeLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyConfigAttributeResponse(AbstractModel):
    """ModifyConfigAttribute返回参数结构体

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


class ModifyMonitorAttributeRequest(AbstractModel):
    """ModifyMonitorAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _MonitorId: 监测任务ID
        :type MonitorId: int
        :param _Urls: 站点的url列表
        :type Urls: list of str
        :param _Name: 任务名称
        :type Name: str
        :param _ScannerType: 扫描模式，normal-正常扫描；deep-深度扫描
        :type ScannerType: str
        :param _Crontab: 扫描周期，单位小时，每X小时执行一次
        :type Crontab: int
        :param _RateLimit: 扫描速率限制，每秒发送X个HTTP请求
        :type RateLimit: int
        :param _FirstScanStartTime: 首次扫描开始时间
        :type FirstScanStartTime: str
        :param _MonitorStatus: 监测状态：1-监测中；2-暂停监测
        :type MonitorStatus: int
        """
        self._MonitorId = None
        self._Urls = None
        self._Name = None
        self._ScannerType = None
        self._Crontab = None
        self._RateLimit = None
        self._FirstScanStartTime = None
        self._MonitorStatus = None

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def ScannerType(self):
        return self._ScannerType

    @ScannerType.setter
    def ScannerType(self, ScannerType):
        self._ScannerType = ScannerType

    @property
    def Crontab(self):
        return self._Crontab

    @Crontab.setter
    def Crontab(self, Crontab):
        self._Crontab = Crontab

    @property
    def RateLimit(self):
        return self._RateLimit

    @RateLimit.setter
    def RateLimit(self, RateLimit):
        self._RateLimit = RateLimit

    @property
    def FirstScanStartTime(self):
        return self._FirstScanStartTime

    @FirstScanStartTime.setter
    def FirstScanStartTime(self, FirstScanStartTime):
        self._FirstScanStartTime = FirstScanStartTime

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus


    def _deserialize(self, params):
        self._MonitorId = params.get("MonitorId")
        self._Urls = params.get("Urls")
        self._Name = params.get("Name")
        self._ScannerType = params.get("ScannerType")
        self._Crontab = params.get("Crontab")
        self._RateLimit = params.get("RateLimit")
        self._FirstScanStartTime = params.get("FirstScanStartTime")
        self._MonitorStatus = params.get("MonitorStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyMonitorAttributeResponse(AbstractModel):
    """ModifyMonitorAttribute返回参数结构体

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


class ModifySiteAttributeRequest(AbstractModel):
    """ModifySiteAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param _SiteId: 站点ID
        :type SiteId: int
        :param _Name: 站点名称
        :type Name: str
        :param _NeedLogin: 网站是否需要登录扫描：0-未知；-1-不需要；1-需要
        :type NeedLogin: int
        :param _LoginCookie: 登录后的cookie
        :type LoginCookie: str
        :param _LoginCheckUrl: 用于测试cookie是否有效的URL
        :type LoginCheckUrl: str
        :param _LoginCheckKw: 用于测试cookie是否有效的关键字
        :type LoginCheckKw: str
        :param _ScanDisallow: 禁止扫描器扫描的目录关键字
        :type ScanDisallow: str
        """
        self._SiteId = None
        self._Name = None
        self._NeedLogin = None
        self._LoginCookie = None
        self._LoginCheckUrl = None
        self._LoginCheckKw = None
        self._ScanDisallow = None

    @property
    def SiteId(self):
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def NeedLogin(self):
        return self._NeedLogin

    @NeedLogin.setter
    def NeedLogin(self, NeedLogin):
        self._NeedLogin = NeedLogin

    @property
    def LoginCookie(self):
        return self._LoginCookie

    @LoginCookie.setter
    def LoginCookie(self, LoginCookie):
        self._LoginCookie = LoginCookie

    @property
    def LoginCheckUrl(self):
        return self._LoginCheckUrl

    @LoginCheckUrl.setter
    def LoginCheckUrl(self, LoginCheckUrl):
        self._LoginCheckUrl = LoginCheckUrl

    @property
    def LoginCheckKw(self):
        return self._LoginCheckKw

    @LoginCheckKw.setter
    def LoginCheckKw(self, LoginCheckKw):
        self._LoginCheckKw = LoginCheckKw

    @property
    def ScanDisallow(self):
        return self._ScanDisallow

    @ScanDisallow.setter
    def ScanDisallow(self, ScanDisallow):
        self._ScanDisallow = ScanDisallow


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Name = params.get("Name")
        self._NeedLogin = params.get("NeedLogin")
        self._LoginCookie = params.get("LoginCookie")
        self._LoginCheckUrl = params.get("LoginCheckUrl")
        self._LoginCheckKw = params.get("LoginCheckKw")
        self._ScanDisallow = params.get("ScanDisallow")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySiteAttributeResponse(AbstractModel):
    """ModifySiteAttribute返回参数结构体

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


class Monitor(AbstractModel):
    """监控任务基础数据

    """

    def __init__(self):
        r"""
        :param _Id: 监控任务ID。
        :type Id: int
        :param _Name: 监控名称。
        :type Name: str
        :param _MonitorStatus: 监测状态：1-监测中；2-暂停监测。
        :type MonitorStatus: int
        :param _ScannerType: 监测模式，normal-正常扫描；deep-深度扫描。
        :type ScannerType: str
        :param _Crontab: 扫描周期，单位小时，每X小时执行一次。
        :type Crontab: int
        :param _IncludedVulsTypes: 指定扫描类型，3位数每位依次表示：扫描Web漏洞、扫描系统漏洞、扫描系统端口。
        :type IncludedVulsTypes: str
        :param _RateLimit: 速率限制，每秒发送X个HTTP请求。
        :type RateLimit: int
        :param _FirstScanStartTime: 首次扫描开始时间。
        :type FirstScanStartTime: str
        :param _ScanStatus: 扫描状态：0-待扫描（无任何扫描结果）；1-扫描中（正在进行扫描）；2-已扫描（有扫描结果且不正在扫描）；3-扫描完成待同步结果。
        :type ScanStatus: int
        :param _LastScanFinishTime: 上一次扫描完成时间。
        :type LastScanFinishTime: str
        :param _CurrentScanStartTime: 当前扫描开始时间，如扫描完成则为上一次扫描的开始时间。
        :type CurrentScanStartTime: str
        :param _CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param _UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        :param _Appid: 云用户appid。
        :type Appid: int
        :param _ContentScanStatus: 扫描状态：0-待检测；1-检测完成
        :type ContentScanStatus: int
        """
        self._Id = None
        self._Name = None
        self._MonitorStatus = None
        self._ScannerType = None
        self._Crontab = None
        self._IncludedVulsTypes = None
        self._RateLimit = None
        self._FirstScanStartTime = None
        self._ScanStatus = None
        self._LastScanFinishTime = None
        self._CurrentScanStartTime = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Appid = None
        self._ContentScanStatus = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def ScannerType(self):
        return self._ScannerType

    @ScannerType.setter
    def ScannerType(self, ScannerType):
        self._ScannerType = ScannerType

    @property
    def Crontab(self):
        return self._Crontab

    @Crontab.setter
    def Crontab(self, Crontab):
        self._Crontab = Crontab

    @property
    def IncludedVulsTypes(self):
        return self._IncludedVulsTypes

    @IncludedVulsTypes.setter
    def IncludedVulsTypes(self, IncludedVulsTypes):
        self._IncludedVulsTypes = IncludedVulsTypes

    @property
    def RateLimit(self):
        return self._RateLimit

    @RateLimit.setter
    def RateLimit(self, RateLimit):
        self._RateLimit = RateLimit

    @property
    def FirstScanStartTime(self):
        return self._FirstScanStartTime

    @FirstScanStartTime.setter
    def FirstScanStartTime(self, FirstScanStartTime):
        self._FirstScanStartTime = FirstScanStartTime

    @property
    def ScanStatus(self):
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def LastScanFinishTime(self):
        return self._LastScanFinishTime

    @LastScanFinishTime.setter
    def LastScanFinishTime(self, LastScanFinishTime):
        self._LastScanFinishTime = LastScanFinishTime

    @property
    def CurrentScanStartTime(self):
        return self._CurrentScanStartTime

    @CurrentScanStartTime.setter
    def CurrentScanStartTime(self, CurrentScanStartTime):
        self._CurrentScanStartTime = CurrentScanStartTime

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def ContentScanStatus(self):
        return self._ContentScanStatus

    @ContentScanStatus.setter
    def ContentScanStatus(self, ContentScanStatus):
        self._ContentScanStatus = ContentScanStatus


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        self._MonitorStatus = params.get("MonitorStatus")
        self._ScannerType = params.get("ScannerType")
        self._Crontab = params.get("Crontab")
        self._IncludedVulsTypes = params.get("IncludedVulsTypes")
        self._RateLimit = params.get("RateLimit")
        self._FirstScanStartTime = params.get("FirstScanStartTime")
        self._ScanStatus = params.get("ScanStatus")
        self._LastScanFinishTime = params.get("LastScanFinishTime")
        self._CurrentScanStartTime = params.get("CurrentScanStartTime")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Appid = params.get("Appid")
        self._ContentScanStatus = params.get("ContentScanStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorMiniSite(AbstractModel):
    """监控任务中的站点信息。

    """

    def __init__(self):
        r"""
        :param _SiteId: 站点ID。
        :type SiteId: int
        :param _Url: 站点Url。
        :type Url: str
        """
        self._SiteId = None
        self._Url = None

    @property
    def SiteId(self):
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url


    def _deserialize(self, params):
        self._SiteId = params.get("SiteId")
        self._Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MonitorsDetail(AbstractModel):
    """监控任务详细数据

    """

    def __init__(self):
        r"""
        :param _Basic: 监控任务基础信息。
        :type Basic: :class:`tencentcloud.cws.v20180312.models.Monitor`
        :param _Sites: 监控任务包含的站点列表。
        :type Sites: list of MonitorMiniSite
        :param _SiteNumber: 监控任务包含的站点列表数量。
        :type SiteNumber: int
        :param _ImpactSites: 监控任务包含的受漏洞威胁的站点列表。
        :type ImpactSites: list of MonitorMiniSite
        :param _ImpactSiteNumber: 监控任务包含的受漏洞威胁的站点列表数量。
        :type ImpactSiteNumber: int
        :param _VulsHighNumber: 高风险漏洞数量。
        :type VulsHighNumber: int
        :param _VulsMiddleNumber: 中风险漏洞数量。
        :type VulsMiddleNumber: int
        :param _VulsLowNumber: 低风险漏洞数量。
        :type VulsLowNumber: int
        :param _VulsNoticeNumber: 提示数量。
        :type VulsNoticeNumber: int
        :param _Progress: 监控任务包含的站点列表的平均扫描进度。
        :type Progress: int
        :param _PageCount: 扫描页面总数。
        :type PageCount: int
        :param _ContentNumber: 内容检测数量。
        :type ContentNumber: int
        """
        self._Basic = None
        self._Sites = None
        self._SiteNumber = None
        self._ImpactSites = None
        self._ImpactSiteNumber = None
        self._VulsHighNumber = None
        self._VulsMiddleNumber = None
        self._VulsLowNumber = None
        self._VulsNoticeNumber = None
        self._Progress = None
        self._PageCount = None
        self._ContentNumber = None

    @property
    def Basic(self):
        return self._Basic

    @Basic.setter
    def Basic(self, Basic):
        self._Basic = Basic

    @property
    def Sites(self):
        return self._Sites

    @Sites.setter
    def Sites(self, Sites):
        self._Sites = Sites

    @property
    def SiteNumber(self):
        return self._SiteNumber

    @SiteNumber.setter
    def SiteNumber(self, SiteNumber):
        self._SiteNumber = SiteNumber

    @property
    def ImpactSites(self):
        return self._ImpactSites

    @ImpactSites.setter
    def ImpactSites(self, ImpactSites):
        self._ImpactSites = ImpactSites

    @property
    def ImpactSiteNumber(self):
        return self._ImpactSiteNumber

    @ImpactSiteNumber.setter
    def ImpactSiteNumber(self, ImpactSiteNumber):
        self._ImpactSiteNumber = ImpactSiteNumber

    @property
    def VulsHighNumber(self):
        return self._VulsHighNumber

    @VulsHighNumber.setter
    def VulsHighNumber(self, VulsHighNumber):
        self._VulsHighNumber = VulsHighNumber

    @property
    def VulsMiddleNumber(self):
        return self._VulsMiddleNumber

    @VulsMiddleNumber.setter
    def VulsMiddleNumber(self, VulsMiddleNumber):
        self._VulsMiddleNumber = VulsMiddleNumber

    @property
    def VulsLowNumber(self):
        return self._VulsLowNumber

    @VulsLowNumber.setter
    def VulsLowNumber(self, VulsLowNumber):
        self._VulsLowNumber = VulsLowNumber

    @property
    def VulsNoticeNumber(self):
        return self._VulsNoticeNumber

    @VulsNoticeNumber.setter
    def VulsNoticeNumber(self, VulsNoticeNumber):
        self._VulsNoticeNumber = VulsNoticeNumber

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def PageCount(self):
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def ContentNumber(self):
        return self._ContentNumber

    @ContentNumber.setter
    def ContentNumber(self, ContentNumber):
        self._ContentNumber = ContentNumber


    def _deserialize(self, params):
        if params.get("Basic") is not None:
            self._Basic = Monitor()
            self._Basic._deserialize(params.get("Basic"))
        if params.get("Sites") is not None:
            self._Sites = []
            for item in params.get("Sites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self._Sites.append(obj)
        self._SiteNumber = params.get("SiteNumber")
        if params.get("ImpactSites") is not None:
            self._ImpactSites = []
            for item in params.get("ImpactSites"):
                obj = MonitorMiniSite()
                obj._deserialize(item)
                self._ImpactSites.append(obj)
        self._ImpactSiteNumber = params.get("ImpactSiteNumber")
        self._VulsHighNumber = params.get("VulsHighNumber")
        self._VulsMiddleNumber = params.get("VulsMiddleNumber")
        self._VulsLowNumber = params.get("VulsLowNumber")
        self._VulsNoticeNumber = params.get("VulsNoticeNumber")
        self._Progress = params.get("Progress")
        self._PageCount = params.get("PageCount")
        self._ContentNumber = params.get("ContentNumber")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Site(AbstractModel):
    """站点数据

    """

    def __init__(self):
        r"""
        :param _Id: 站点ID。
        :type Id: int
        :param _MonitorId: 监控任务ID，为0时表示未加入监控任务。
        :type MonitorId: int
        :param _Url: 站点url。
        :type Url: str
        :param _Name: 站点名称。
        :type Name: str
        :param _VerifyStatus: 验证状态：0-未验证；1-已验证；2-验证失效，待重新验证。
        :type VerifyStatus: int
        :param _MonitorStatus: 监测状态：0-未监测；1-监测中；2-暂停监测。
        :type MonitorStatus: int
        :param _ScanStatus: 扫描状态：0-待扫描（无任何扫描结果）；1-扫描中（正在进行扫描）；2-已扫描（有扫描结果且不正在扫描）；3-扫描完成待同步结果。
        :type ScanStatus: int
        :param _LastScanTaskId: 最近一次的AIScanner的扫描任务id，注意取消的情况。
        :type LastScanTaskId: int
        :param _LastScanStartTime: 最近一次扫描开始时间。
        :type LastScanStartTime: str
        :param _LastScanFinishTime: 最近一次扫描完成时间。
        :type LastScanFinishTime: str
        :param _LastScanCancelTime: 最近一次取消时间，取消即使用上一次扫描结果。
        :type LastScanCancelTime: str
        :param _LastScanPageCount: 最近一次扫描扫描的页面数。
        :type LastScanPageCount: int
        :param _LastScanScannerType: normal-正常扫描；deep-深度扫描。
        :type LastScanScannerType: str
        :param _LastScanVulsHighNum: 最近一次扫描高风险漏洞数量。
        :type LastScanVulsHighNum: int
        :param _LastScanVulsMiddleNum: 最近一次扫描中风险漏洞数量。
        :type LastScanVulsMiddleNum: int
        :param _LastScanVulsLowNum: 最近一次扫描低风险漏洞数量。
        :type LastScanVulsLowNum: int
        :param _LastScanVulsNoticeNum: 最近一次扫描提示信息数量。
        :type LastScanVulsNoticeNum: int
        :param _CreatedAt: 记录添加时间。
        :type CreatedAt: str
        :param _UpdatedAt: 记录最近修改时间。
        :type UpdatedAt: str
        :param _LastScanRateLimit: 速率限制，每秒发送X个HTTP请求。
        :type LastScanRateLimit: int
        :param _LastScanVulsNum: 最近一次扫描漏洞总数量。
        :type LastScanVulsNum: int
        :param _LastScanNoticeNum: 最近一次扫描提示总数量
        :type LastScanNoticeNum: int
        :param _Progress: 扫描进度，百分比整数
        :type Progress: int
        :param _Appid: 云用户appid。
        :type Appid: int
        :param _Uin: 云用户标识。
        :type Uin: str
        :param _NeedLogin: 网站是否需要登录扫描：0-未知；-1-不需要；1-需要。
        :type NeedLogin: int
        :param _LoginCookie: 登录后的cookie。
        :type LoginCookie: str
        :param _LoginCookieValid: 登录后的cookie是否有效：0-无效；1-有效。
        :type LoginCookieValid: int
        :param _LoginCheckUrl: 用于测试cookie是否有效的URL。
        :type LoginCheckUrl: str
        :param _LoginCheckKw: 用于测试cookie是否有效的关键字。
        :type LoginCheckKw: str
        :param _ScanDisallow: 禁止扫描器扫描的目录关键字。
        :type ScanDisallow: str
        :param _UserAgent: 访问网站的客户端标识。
        :type UserAgent: str
        :param _ContentStatus: 内容检测状态：0-未检测；1-已检测；
        :type ContentStatus: int
        :param _LastScanContentNum: 最近一次扫描内容检测数量
        :type LastScanContentNum: int
        """
        self._Id = None
        self._MonitorId = None
        self._Url = None
        self._Name = None
        self._VerifyStatus = None
        self._MonitorStatus = None
        self._ScanStatus = None
        self._LastScanTaskId = None
        self._LastScanStartTime = None
        self._LastScanFinishTime = None
        self._LastScanCancelTime = None
        self._LastScanPageCount = None
        self._LastScanScannerType = None
        self._LastScanVulsHighNum = None
        self._LastScanVulsMiddleNum = None
        self._LastScanVulsLowNum = None
        self._LastScanVulsNoticeNum = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._LastScanRateLimit = None
        self._LastScanVulsNum = None
        self._LastScanNoticeNum = None
        self._Progress = None
        self._Appid = None
        self._Uin = None
        self._NeedLogin = None
        self._LoginCookie = None
        self._LoginCookieValid = None
        self._LoginCheckUrl = None
        self._LoginCheckKw = None
        self._ScanDisallow = None
        self._UserAgent = None
        self._ContentStatus = None
        self._LastScanContentNum = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def MonitorId(self):
        return self._MonitorId

    @MonitorId.setter
    def MonitorId(self, MonitorId):
        self._MonitorId = MonitorId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def MonitorStatus(self):
        return self._MonitorStatus

    @MonitorStatus.setter
    def MonitorStatus(self, MonitorStatus):
        self._MonitorStatus = MonitorStatus

    @property
    def ScanStatus(self):
        return self._ScanStatus

    @ScanStatus.setter
    def ScanStatus(self, ScanStatus):
        self._ScanStatus = ScanStatus

    @property
    def LastScanTaskId(self):
        return self._LastScanTaskId

    @LastScanTaskId.setter
    def LastScanTaskId(self, LastScanTaskId):
        self._LastScanTaskId = LastScanTaskId

    @property
    def LastScanStartTime(self):
        return self._LastScanStartTime

    @LastScanStartTime.setter
    def LastScanStartTime(self, LastScanStartTime):
        self._LastScanStartTime = LastScanStartTime

    @property
    def LastScanFinishTime(self):
        return self._LastScanFinishTime

    @LastScanFinishTime.setter
    def LastScanFinishTime(self, LastScanFinishTime):
        self._LastScanFinishTime = LastScanFinishTime

    @property
    def LastScanCancelTime(self):
        return self._LastScanCancelTime

    @LastScanCancelTime.setter
    def LastScanCancelTime(self, LastScanCancelTime):
        self._LastScanCancelTime = LastScanCancelTime

    @property
    def LastScanPageCount(self):
        return self._LastScanPageCount

    @LastScanPageCount.setter
    def LastScanPageCount(self, LastScanPageCount):
        self._LastScanPageCount = LastScanPageCount

    @property
    def LastScanScannerType(self):
        return self._LastScanScannerType

    @LastScanScannerType.setter
    def LastScanScannerType(self, LastScanScannerType):
        self._LastScanScannerType = LastScanScannerType

    @property
    def LastScanVulsHighNum(self):
        return self._LastScanVulsHighNum

    @LastScanVulsHighNum.setter
    def LastScanVulsHighNum(self, LastScanVulsHighNum):
        self._LastScanVulsHighNum = LastScanVulsHighNum

    @property
    def LastScanVulsMiddleNum(self):
        return self._LastScanVulsMiddleNum

    @LastScanVulsMiddleNum.setter
    def LastScanVulsMiddleNum(self, LastScanVulsMiddleNum):
        self._LastScanVulsMiddleNum = LastScanVulsMiddleNum

    @property
    def LastScanVulsLowNum(self):
        return self._LastScanVulsLowNum

    @LastScanVulsLowNum.setter
    def LastScanVulsLowNum(self, LastScanVulsLowNum):
        self._LastScanVulsLowNum = LastScanVulsLowNum

    @property
    def LastScanVulsNoticeNum(self):
        return self._LastScanVulsNoticeNum

    @LastScanVulsNoticeNum.setter
    def LastScanVulsNoticeNum(self, LastScanVulsNoticeNum):
        self._LastScanVulsNoticeNum = LastScanVulsNoticeNum

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def LastScanRateLimit(self):
        return self._LastScanRateLimit

    @LastScanRateLimit.setter
    def LastScanRateLimit(self, LastScanRateLimit):
        self._LastScanRateLimit = LastScanRateLimit

    @property
    def LastScanVulsNum(self):
        return self._LastScanVulsNum

    @LastScanVulsNum.setter
    def LastScanVulsNum(self, LastScanVulsNum):
        self._LastScanVulsNum = LastScanVulsNum

    @property
    def LastScanNoticeNum(self):
        return self._LastScanNoticeNum

    @LastScanNoticeNum.setter
    def LastScanNoticeNum(self, LastScanNoticeNum):
        self._LastScanNoticeNum = LastScanNoticeNum

    @property
    def Progress(self):
        return self._Progress

    @Progress.setter
    def Progress(self, Progress):
        self._Progress = Progress

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin

    @property
    def NeedLogin(self):
        return self._NeedLogin

    @NeedLogin.setter
    def NeedLogin(self, NeedLogin):
        self._NeedLogin = NeedLogin

    @property
    def LoginCookie(self):
        return self._LoginCookie

    @LoginCookie.setter
    def LoginCookie(self, LoginCookie):
        self._LoginCookie = LoginCookie

    @property
    def LoginCookieValid(self):
        return self._LoginCookieValid

    @LoginCookieValid.setter
    def LoginCookieValid(self, LoginCookieValid):
        self._LoginCookieValid = LoginCookieValid

    @property
    def LoginCheckUrl(self):
        return self._LoginCheckUrl

    @LoginCheckUrl.setter
    def LoginCheckUrl(self, LoginCheckUrl):
        self._LoginCheckUrl = LoginCheckUrl

    @property
    def LoginCheckKw(self):
        return self._LoginCheckKw

    @LoginCheckKw.setter
    def LoginCheckKw(self, LoginCheckKw):
        self._LoginCheckKw = LoginCheckKw

    @property
    def ScanDisallow(self):
        return self._ScanDisallow

    @ScanDisallow.setter
    def ScanDisallow(self, ScanDisallow):
        self._ScanDisallow = ScanDisallow

    @property
    def UserAgent(self):
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def ContentStatus(self):
        return self._ContentStatus

    @ContentStatus.setter
    def ContentStatus(self, ContentStatus):
        self._ContentStatus = ContentStatus

    @property
    def LastScanContentNum(self):
        return self._LastScanContentNum

    @LastScanContentNum.setter
    def LastScanContentNum(self, LastScanContentNum):
        self._LastScanContentNum = LastScanContentNum


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._MonitorId = params.get("MonitorId")
        self._Url = params.get("Url")
        self._Name = params.get("Name")
        self._VerifyStatus = params.get("VerifyStatus")
        self._MonitorStatus = params.get("MonitorStatus")
        self._ScanStatus = params.get("ScanStatus")
        self._LastScanTaskId = params.get("LastScanTaskId")
        self._LastScanStartTime = params.get("LastScanStartTime")
        self._LastScanFinishTime = params.get("LastScanFinishTime")
        self._LastScanCancelTime = params.get("LastScanCancelTime")
        self._LastScanPageCount = params.get("LastScanPageCount")
        self._LastScanScannerType = params.get("LastScanScannerType")
        self._LastScanVulsHighNum = params.get("LastScanVulsHighNum")
        self._LastScanVulsMiddleNum = params.get("LastScanVulsMiddleNum")
        self._LastScanVulsLowNum = params.get("LastScanVulsLowNum")
        self._LastScanVulsNoticeNum = params.get("LastScanVulsNoticeNum")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._LastScanRateLimit = params.get("LastScanRateLimit")
        self._LastScanVulsNum = params.get("LastScanVulsNum")
        self._LastScanNoticeNum = params.get("LastScanNoticeNum")
        self._Progress = params.get("Progress")
        self._Appid = params.get("Appid")
        self._Uin = params.get("Uin")
        self._NeedLogin = params.get("NeedLogin")
        self._LoginCookie = params.get("LoginCookie")
        self._LoginCookieValid = params.get("LoginCookieValid")
        self._LoginCheckUrl = params.get("LoginCheckUrl")
        self._LoginCheckKw = params.get("LoginCheckKw")
        self._ScanDisallow = params.get("ScanDisallow")
        self._UserAgent = params.get("UserAgent")
        self._ContentStatus = params.get("ContentStatus")
        self._LastScanContentNum = params.get("LastScanContentNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SitesVerification(AbstractModel):
    """站点验证数据

    """

    def __init__(self):
        r"""
        :param _Domain: 根域名。
        :type Domain: str
        :param _TxtName: txt解析域名验证的name。
        :type TxtName: str
        :param _TxtText: txt解析域名验证的text。
        :type TxtText: str
        :param _ValidTo: 验证有效期，在此之前有效。
        :type ValidTo: str
        :param _VerifyStatus: 验证状态：0-未验证；1-已验证；2-验证失效，待重新验证。
        :type VerifyStatus: int
        :param _CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param _UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        :param _Id: ID。
        :type Id: int
        :param _Appid: 云用户appid
        :type Appid: int
        :param _VerifyUrl: 用于验证站点的url，即访问该url获取验证数据。
        :type VerifyUrl: str
        :param _VerifyFileUrl: 获取验证验证文件的url。
        :type VerifyFileUrl: str
        """
        self._Domain = None
        self._TxtName = None
        self._TxtText = None
        self._ValidTo = None
        self._VerifyStatus = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._Id = None
        self._Appid = None
        self._VerifyUrl = None
        self._VerifyFileUrl = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def TxtName(self):
        return self._TxtName

    @TxtName.setter
    def TxtName(self, TxtName):
        self._TxtName = TxtName

    @property
    def TxtText(self):
        return self._TxtText

    @TxtText.setter
    def TxtText(self, TxtText):
        self._TxtText = TxtText

    @property
    def ValidTo(self):
        return self._ValidTo

    @ValidTo.setter
    def ValidTo(self, ValidTo):
        self._ValidTo = ValidTo

    @property
    def VerifyStatus(self):
        return self._VerifyStatus

    @VerifyStatus.setter
    def VerifyStatus(self, VerifyStatus):
        self._VerifyStatus = VerifyStatus

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def VerifyUrl(self):
        return self._VerifyUrl

    @VerifyUrl.setter
    def VerifyUrl(self, VerifyUrl):
        self._VerifyUrl = VerifyUrl

    @property
    def VerifyFileUrl(self):
        return self._VerifyFileUrl

    @VerifyFileUrl.setter
    def VerifyFileUrl(self, VerifyFileUrl):
        self._VerifyFileUrl = VerifyFileUrl


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._TxtName = params.get("TxtName")
        self._TxtText = params.get("TxtText")
        self._ValidTo = params.get("ValidTo")
        self._VerifyStatus = params.get("VerifyStatus")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._Id = params.get("Id")
        self._Appid = params.get("Appid")
        self._VerifyUrl = params.get("VerifyUrl")
        self._VerifyFileUrl = params.get("VerifyFileUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySitesRequest(AbstractModel):
    """VerifySites请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 站点的url列表
        :type Urls: list of str
        """
        self._Urls = None

    @property
    def Urls(self):
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifySitesResponse(AbstractModel):
    """VerifySites返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SuccessNumber: 验证成功的根域名数量。
        :type SuccessNumber: int
        :param _FailNumber: 验证失败的根域名数量。
        :type FailNumber: int
        :param _RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SuccessNumber = None
        self._FailNumber = None
        self._RequestId = None

    @property
    def SuccessNumber(self):
        return self._SuccessNumber

    @SuccessNumber.setter
    def SuccessNumber(self, SuccessNumber):
        self._SuccessNumber = SuccessNumber

    @property
    def FailNumber(self):
        return self._FailNumber

    @FailNumber.setter
    def FailNumber(self, FailNumber):
        self._FailNumber = FailNumber

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SuccessNumber = params.get("SuccessNumber")
        self._FailNumber = params.get("FailNumber")
        self._RequestId = params.get("RequestId")


class Vul(AbstractModel):
    """漏洞数据

    """

    def __init__(self):
        r"""
        :param _Id: 漏洞ID。
        :type Id: int
        :param _SiteId: 站点ID。
        :type SiteId: int
        :param _TaskId: 扫描引擎的扫描任务ID。
        :type TaskId: int
        :param _Level: 漏洞级别：high、middle、low、notice。
        :type Level: str
        :param _Name: 漏洞名称。
        :type Name: str
        :param _Url: 出现漏洞的url。
        :type Url: str
        :param _Html: 网址/细节。
        :type Html: str
        :param _Nickname: 漏洞类型。
        :type Nickname: str
        :param _Harm: 危害说明。
        :type Harm: str
        :param _Describe: 漏洞描述。
        :type Describe: str
        :param _Solution: 解决方案。
        :type Solution: str
        :param _From: 漏洞参考。
        :type From: str
        :param _Parameter: 漏洞通过该参数攻击。
        :type Parameter: str
        :param _CreatedAt: CreatedAt。
        :type CreatedAt: str
        :param _UpdatedAt: UpdatedAt。
        :type UpdatedAt: str
        :param _IsReported: 是否已经添加误报，0-否，1-是。
        :type IsReported: int
        :param _Appid: 云用户appid。
        :type Appid: int
        :param _Uin: 云用户标识。
        :type Uin: str
        """
        self._Id = None
        self._SiteId = None
        self._TaskId = None
        self._Level = None
        self._Name = None
        self._Url = None
        self._Html = None
        self._Nickname = None
        self._Harm = None
        self._Describe = None
        self._Solution = None
        self._From = None
        self._Parameter = None
        self._CreatedAt = None
        self._UpdatedAt = None
        self._IsReported = None
        self._Appid = None
        self._Uin = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def SiteId(self):
        return self._SiteId

    @SiteId.setter
    def SiteId(self, SiteId):
        self._SiteId = SiteId

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Level(self):
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Html(self):
        return self._Html

    @Html.setter
    def Html(self, Html):
        self._Html = Html

    @property
    def Nickname(self):
        return self._Nickname

    @Nickname.setter
    def Nickname(self, Nickname):
        self._Nickname = Nickname

    @property
    def Harm(self):
        return self._Harm

    @Harm.setter
    def Harm(self, Harm):
        self._Harm = Harm

    @property
    def Describe(self):
        return self._Describe

    @Describe.setter
    def Describe(self, Describe):
        self._Describe = Describe

    @property
    def Solution(self):
        return self._Solution

    @Solution.setter
    def Solution(self, Solution):
        self._Solution = Solution

    @property
    def From(self):
        return self._From

    @From.setter
    def From(self, From):
        self._From = From

    @property
    def Parameter(self):
        return self._Parameter

    @Parameter.setter
    def Parameter(self, Parameter):
        self._Parameter = Parameter

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt

    @property
    def IsReported(self):
        return self._IsReported

    @IsReported.setter
    def IsReported(self, IsReported):
        self._IsReported = IsReported

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Uin(self):
        return self._Uin

    @Uin.setter
    def Uin(self, Uin):
        self._Uin = Uin


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._SiteId = params.get("SiteId")
        self._TaskId = params.get("TaskId")
        self._Level = params.get("Level")
        self._Name = params.get("Name")
        self._Url = params.get("Url")
        self._Html = params.get("Html")
        self._Nickname = params.get("Nickname")
        self._Harm = params.get("Harm")
        self._Describe = params.get("Describe")
        self._Solution = params.get("Solution")
        self._From = params.get("From")
        self._Parameter = params.get("Parameter")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        self._IsReported = params.get("IsReported")
        self._Appid = params.get("Appid")
        self._Uin = params.get("Uin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VulsTimeline(AbstractModel):
    """用户漏洞数随时间变化统计数据

    """

    def __init__(self):
        r"""
        :param _Id: ID。
        :type Id: int
        :param _Appid: 云用户appid。
        :type Appid: int
        :param _Date: 日期。
        :type Date: str
        :param _PageCount: 扫描页面总数量。
        :type PageCount: int
        :param _SiteNum: 已验证网站总数量。
        :type SiteNum: int
        :param _ImpactSiteNum: 受影响的网站总数量。
        :type ImpactSiteNum: int
        :param _VulsHighNum: 高危漏洞总数量。
        :type VulsHighNum: int
        :param _VulsMiddleNum: 中危漏洞总数量。
        :type VulsMiddleNum: int
        :param _VulsLowNum: 低危漏洞总数量。
        :type VulsLowNum: int
        :param _VulsNoticeNum: 风险提示总数量
        :type VulsNoticeNum: int
        :param _CreatedAt: 记录添加时间。
        :type CreatedAt: str
        :param _UpdatedAt: 记录最近修改时间。
        :type UpdatedAt: str
        """
        self._Id = None
        self._Appid = None
        self._Date = None
        self._PageCount = None
        self._SiteNum = None
        self._ImpactSiteNum = None
        self._VulsHighNum = None
        self._VulsMiddleNum = None
        self._VulsLowNum = None
        self._VulsNoticeNum = None
        self._CreatedAt = None
        self._UpdatedAt = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Appid(self):
        return self._Appid

    @Appid.setter
    def Appid(self, Appid):
        self._Appid = Appid

    @property
    def Date(self):
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date

    @property
    def PageCount(self):
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def SiteNum(self):
        return self._SiteNum

    @SiteNum.setter
    def SiteNum(self, SiteNum):
        self._SiteNum = SiteNum

    @property
    def ImpactSiteNum(self):
        return self._ImpactSiteNum

    @ImpactSiteNum.setter
    def ImpactSiteNum(self, ImpactSiteNum):
        self._ImpactSiteNum = ImpactSiteNum

    @property
    def VulsHighNum(self):
        return self._VulsHighNum

    @VulsHighNum.setter
    def VulsHighNum(self, VulsHighNum):
        self._VulsHighNum = VulsHighNum

    @property
    def VulsMiddleNum(self):
        return self._VulsMiddleNum

    @VulsMiddleNum.setter
    def VulsMiddleNum(self, VulsMiddleNum):
        self._VulsMiddleNum = VulsMiddleNum

    @property
    def VulsLowNum(self):
        return self._VulsLowNum

    @VulsLowNum.setter
    def VulsLowNum(self, VulsLowNum):
        self._VulsLowNum = VulsLowNum

    @property
    def VulsNoticeNum(self):
        return self._VulsNoticeNum

    @VulsNoticeNum.setter
    def VulsNoticeNum(self, VulsNoticeNum):
        self._VulsNoticeNum = VulsNoticeNum

    @property
    def CreatedAt(self):
        return self._CreatedAt

    @CreatedAt.setter
    def CreatedAt(self, CreatedAt):
        self._CreatedAt = CreatedAt

    @property
    def UpdatedAt(self):
        return self._UpdatedAt

    @UpdatedAt.setter
    def UpdatedAt(self, UpdatedAt):
        self._UpdatedAt = UpdatedAt


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Appid = params.get("Appid")
        self._Date = params.get("Date")
        self._PageCount = params.get("PageCount")
        self._SiteNum = params.get("SiteNum")
        self._ImpactSiteNum = params.get("ImpactSiteNum")
        self._VulsHighNum = params.get("VulsHighNum")
        self._VulsMiddleNum = params.get("VulsMiddleNum")
        self._VulsLowNum = params.get("VulsLowNum")
        self._VulsNoticeNum = params.get("VulsNoticeNum")
        self._CreatedAt = params.get("CreatedAt")
        self._UpdatedAt = params.get("UpdatedAt")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        