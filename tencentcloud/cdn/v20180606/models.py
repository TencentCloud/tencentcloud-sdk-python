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


class AccessControl(AbstractModel):
    """请求头部及请求url访问控制

    """

    def __init__(self):
        r"""
        :param _Switch: 启用请求头部及请求url访问控制开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _AccessControlRules: 请求头部及请求url访问规则
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessControlRules: list of AccessControlRule
        :param _ReturnCode: 返回状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        """
        self._Switch = None
        self._AccessControlRules = None
        self._ReturnCode = None

    @property
    def Switch(self):
        """启用请求头部及请求url访问控制开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessControlRules(self):
        """请求头部及请求url访问规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AccessControlRule
        """
        return self._AccessControlRules

    @AccessControlRules.setter
    def AccessControlRules(self, AccessControlRules):
        self._AccessControlRules = AccessControlRules

    @property
    def ReturnCode(self):
        """返回状态码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("AccessControlRules") is not None:
            self._AccessControlRules = []
            for item in params.get("AccessControlRules"):
                obj = AccessControlRule()
                obj._deserialize(item)
                self._AccessControlRules.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlRule(AbstractModel):
    """访问控制规则

    """

    def __init__(self):
        r"""
        :param _RuleType: requestHeader ：对请求头部进行访问控制
url ： 对访问url进行访问控制
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RuleContent: 封禁内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleContent: str
        :param _Regex: on ：正则匹配
off ：字面匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        :param _RuleHeader: RuleType为requestHeader时必填，否则不需要填
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleHeader: str
        """
        self._RuleType = None
        self._RuleContent = None
        self._Regex = None
        self._RuleHeader = None

    @property
    def RuleType(self):
        """requestHeader ：对请求头部进行访问控制
url ： 对访问url进行访问控制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleContent(self):
        """封禁内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleContent

    @RuleContent.setter
    def RuleContent(self, RuleContent):
        self._RuleContent = RuleContent

    @property
    def Regex(self):
        """on ：正则匹配
off ：字面匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def RuleHeader(self):
        """RuleType为requestHeader时必填，否则不需要填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleHeader

    @RuleHeader.setter
    def RuleHeader(self, RuleHeader):
        self._RuleHeader = RuleHeader


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RuleContent = params.get("RuleContent")
        self._Regex = params.get("Regex")
        self._RuleHeader = params.get("RuleHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCLSTopicDomainsRequest(AbstractModel):
    """AddCLSTopicDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _DomainAreaConfigs: 域名区域配置
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._DomainAreaConfigs = None
        self._Channel = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def DomainAreaConfigs(self):
        """域名区域配置
        :rtype: list of DomainAreaConfig
        """
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCLSTopicDomainsResponse(AbstractModel):
    """AddCLSTopicDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _ServiceType: 加速域名业务类型
web：网页小文件
download：下载大文件
media：音视频点播
hybrid:  动静加速
dynamic:  动态加速
        :type ServiceType: str
        :param _Origin: 源站配置
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _ProjectId: 项目 ID，默认为 0，代表【默认项目】
        :type ProjectId: int
        :param _IpFilter: IP 黑白名单配置
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP 限频配置
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _StatusCodeCache: 状态码缓存配置
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _Compression: 智能压缩配置
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _BandwidthAlert: 带宽封顶配置
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _RangeOriginPull: Range 回源配置
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _FollowRedirect: 301/302 回源跟随配置。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ErrorPage: 错误码重定向配置（功能灰度中，尚未全量）
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _RequestHeader: 请求头部配置
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: 响应头部配置
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _DownstreamCapping: 下载速度配置
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _CacheKey: 节点缓存键配置
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _ResponseHeaderCache: 头部缓存配置
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _VideoSeek: 视频拖拽配置
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _Cache: 缓存过期时间配置
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _OriginPullOptimization: 跨国链路优化配置
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _Https: Https 加速配置
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _Authentication: 时间戳防盗链配置
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _Seo: SEO 优化配置
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ForceRedirect: 访问协议强制跳转配置
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Referer: Referer 防盗链配置
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _MaxAge: 浏览器缓存配置（功能灰度中，尚未全量）
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Ipv6: Ipv6 配置（功能灰度中，尚未全量）
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param _SpecificConfig: 地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param _Area: 域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
使用中国境外加速、全球加速时，需要先开通中国境外加速服务
        :type Area: str
        :param _OriginPullTimeout: 回源超时配置
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param _Tag: 标签配置
        :type Tag: list of Tag
        :param _Ipv6Access: Ipv6 访问配置
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param _OfflineCache: 离线缓存
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param _Quic: Quic访问（收费服务，详见计费说明和产品文档）
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param _AwsPrivateAccess: 回源S3私有鉴权
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _OssPrivateAccess: 回源OSS私有鉴权
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _HwPrivateAccess: 华为云对象存储回源鉴权
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: 七牛云对象存储回源鉴权
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        :param _OthersPrivateAccess: 其他厂商对象存储回源鉴权
        :type OthersPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        :param _HttpsBilling: HTTPS服务，默认开启（收费服务，详见计费说明和产品文档）
        :type HttpsBilling: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        """
        self._Domain = None
        self._ServiceType = None
        self._Origin = None
        self._ProjectId = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._StatusCodeCache = None
        self._Compression = None
        self._BandwidthAlert = None
        self._RangeOriginPull = None
        self._FollowRedirect = None
        self._ErrorPage = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._DownstreamCapping = None
        self._CacheKey = None
        self._ResponseHeaderCache = None
        self._VideoSeek = None
        self._Cache = None
        self._OriginPullOptimization = None
        self._Https = None
        self._Authentication = None
        self._Seo = None
        self._ForceRedirect = None
        self._Referer = None
        self._MaxAge = None
        self._Ipv6 = None
        self._SpecificConfig = None
        self._Area = None
        self._OriginPullTimeout = None
        self._Tag = None
        self._Ipv6Access = None
        self._OfflineCache = None
        self._Quic = None
        self._AwsPrivateAccess = None
        self._OssPrivateAccess = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None
        self._OthersPrivateAccess = None
        self._HttpsBilling = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ServiceType(self):
        """加速域名业务类型
web：网页小文件
download：下载大文件
media：音视频点播
hybrid:  动静加速
dynamic:  动态加速
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Origin(self):
        """源站配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ProjectId(self):
        """项目 ID，默认为 0，代表【默认项目】
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IpFilter(self):
        """IP 黑白名单配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP 限频配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def StatusCodeCache(self):
        """状态码缓存配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        """
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def Compression(self):
        """智能压缩配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def BandwidthAlert(self):
        """带宽封顶配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        """
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def RangeOriginPull(self):
        """Range 回源配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        """
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def FollowRedirect(self):
        """301/302 回源跟随配置。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        """
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ErrorPage(self):
        """错误码重定向配置（功能灰度中，尚未全量）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def RequestHeader(self):
        """请求头部配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        """响应头部配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def DownstreamCapping(self):
        """下载速度配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        """
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def CacheKey(self):
        """节点缓存键配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def ResponseHeaderCache(self):
        """头部缓存配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        """
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def VideoSeek(self):
        """视频拖拽配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def Cache(self):
        """缓存过期时间配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def OriginPullOptimization(self):
        """跨国链路优化配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        """
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def Https(self):
        """Https 加速配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Authentication(self):
        """时间戳防盗链配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Seo(self):
        """SEO 优化配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Seo`
        """
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ForceRedirect(self):
        """访问协议强制跳转配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Referer(self):
        """Referer 防盗链配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Referer`
        """
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def MaxAge(self):
        """浏览器缓存配置（功能灰度中，尚未全量）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Ipv6(self):
        """Ipv6 配置（功能灰度中，尚未全量）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def SpecificConfig(self):
        """地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        """
        return self._SpecificConfig

    @SpecificConfig.setter
    def SpecificConfig(self, SpecificConfig):
        self._SpecificConfig = SpecificConfig

    @property
    def Area(self):
        """域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
使用中国境外加速、全球加速时，需要先开通中国境外加速服务
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def OriginPullTimeout(self):
        """回源超时配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        """
        return self._OriginPullTimeout

    @OriginPullTimeout.setter
    def OriginPullTimeout(self, OriginPullTimeout):
        self._OriginPullTimeout = OriginPullTimeout

    @property
    def Tag(self):
        """标签配置
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def Ipv6Access(self):
        """Ipv6 访问配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        """
        return self._Ipv6Access

    @Ipv6Access.setter
    def Ipv6Access(self, Ipv6Access):
        self._Ipv6Access = Ipv6Access

    @property
    def OfflineCache(self):
        """离线缓存
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        """
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def Quic(self):
        """Quic访问（收费服务，详见计费说明和产品文档）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Quic`
        """
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def AwsPrivateAccess(self):
        """回源S3私有鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        """
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def OssPrivateAccess(self):
        """回源OSS私有鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        """
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def HwPrivateAccess(self):
        """华为云对象存储回源鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        """
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        """七牛云对象存储回源鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess

    @property
    def OthersPrivateAccess(self):
        """其他厂商对象存储回源鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        """
        return self._OthersPrivateAccess

    @OthersPrivateAccess.setter
    def OthersPrivateAccess(self, OthersPrivateAccess):
        self._OthersPrivateAccess = OthersPrivateAccess

    @property
    def HttpsBilling(self):
        """HTTPS服务，默认开启（收费服务，详见计费说明和产品文档）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        """
        return self._HttpsBilling

    @HttpsBilling.setter
    def HttpsBilling(self, HttpsBilling):
        self._HttpsBilling = HttpsBilling


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ServiceType = params.get("ServiceType")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("SpecificConfig") is not None:
            self._SpecificConfig = SpecificConfig()
            self._SpecificConfig._deserialize(params.get("SpecificConfig"))
        self._Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self._OriginPullTimeout = OriginPullTimeout()
            self._OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("Ipv6Access") is not None:
            self._Ipv6Access = Ipv6Access()
            self._Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        if params.get("OthersPrivateAccess") is not None:
            self._OthersPrivateAccess = OthersPrivateAccess()
            self._OthersPrivateAccess._deserialize(params.get("OthersPrivateAccess"))
        if params.get("HttpsBilling") is not None:
            self._HttpsBilling = HttpsBilling()
            self._HttpsBilling._deserialize(params.get("HttpsBilling"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class AdvanceCacheRule(AbstractModel):
    """缓存配置高级版本规则

    """

    def __init__(self):
        r"""
        :param _CacheType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
default：源站未返回 max-age 情况下的缓存规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheType: str
        :param _CacheContents: 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
default 时填充 "no max-age"
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheContents: list of str
        :param _CacheTime: 缓存过期时间
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        """
        self._CacheType = None
        self._CacheContents = None
        self._CacheTime = None

    @property
    def CacheType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
default：源站未返回 max-age 情况下的缓存规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CacheType

    @CacheType.setter
    def CacheType(self, CacheType):
        self._CacheType = CacheType

    @property
    def CacheContents(self):
        """对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
default 时填充 "no max-age"
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CacheContents

    @CacheContents.setter
    def CacheContents(self, CacheContents):
        self._CacheContents = CacheContents

    @property
    def CacheTime(self):
        """缓存过期时间
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._CacheType = params.get("CacheType")
        self._CacheContents = params.get("CacheContents")
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvanceConfig(AbstractModel):
    """高级配置集合

    """

    def __init__(self):
        r"""
        :param _Name: 高级配置名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _Value: 是否支持高级配置，
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """高级配置名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """是否支持高级配置，
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvanceHttps(AbstractModel):
    """回源的自定义Https配置

    """

    def __init__(self):
        r"""
        :param _CustomTlsStatus: 自定义Tls数据开关
注意：此字段可能返回 null，表示取不到有效值。
        :type CustomTlsStatus: str
        :param _TlsVersion: Tls版本列表，支持设置 TLSv1, TLSV1.1, TLSV1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        :param _Cipher: 自定义加密套件
注意：此字段可能返回 null，表示取不到有效值。
        :type Cipher: str
        :param _VerifyOriginType: 回源双向校验开启状态
off - 关闭校验
oneWay - 校验源站
twoWay - 双向校验
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyOriginType: str
        :param _CertInfo: 回源层证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param _OriginCertInfo: 源站证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        """
        self._CustomTlsStatus = None
        self._TlsVersion = None
        self._Cipher = None
        self._VerifyOriginType = None
        self._CertInfo = None
        self._OriginCertInfo = None

    @property
    def CustomTlsStatus(self):
        """自定义Tls数据开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CustomTlsStatus

    @CustomTlsStatus.setter
    def CustomTlsStatus(self, CustomTlsStatus):
        self._CustomTlsStatus = CustomTlsStatus

    @property
    def TlsVersion(self):
        """Tls版本列表，支持设置 TLSv1, TLSV1.1, TLSV1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Cipher(self):
        """自定义加密套件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cipher

    @Cipher.setter
    def Cipher(self, Cipher):
        self._Cipher = Cipher

    @property
    def VerifyOriginType(self):
        """回源双向校验开启状态
off - 关闭校验
oneWay - 校验源站
twoWay - 双向校验
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyOriginType

    @VerifyOriginType.setter
    def VerifyOriginType(self, VerifyOriginType):
        self._VerifyOriginType = VerifyOriginType

    @property
    def CertInfo(self):
        """回源层证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def OriginCertInfo(self):
        """源站证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        """
        return self._OriginCertInfo

    @OriginCertInfo.setter
    def OriginCertInfo(self, OriginCertInfo):
        self._OriginCertInfo = OriginCertInfo


    def _deserialize(self, params):
        self._CustomTlsStatus = params.get("CustomTlsStatus")
        self._TlsVersion = params.get("TlsVersion")
        self._Cipher = params.get("Cipher")
        self._VerifyOriginType = params.get("VerifyOriginType")
        if params.get("CertInfo") is not None:
            self._CertInfo = ServerCert()
            self._CertInfo._deserialize(params.get("CertInfo"))
        if params.get("OriginCertInfo") is not None:
            self._OriginCertInfo = ClientCert()
            self._OriginCertInfo._deserialize(params.get("OriginCertInfo"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthentication(AbstractModel):
    """时间戳防盗链高级版配置，白名单功能

    """

    def __init__(self):
        r"""
        :param _Switch: 防盗链配置开关，取值有：
on：开启
off：关闭
开启时必须且只配置一种模式，其余模式需要设置为 null
        :type Switch: str
        :param _TypeA: 时间戳防盗链高级版模式A配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeA`
        :param _TypeB: 时间戳防盗链高级版模式B配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeB`
        :param _TypeC: 时间戳防盗链高级版模式C配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeC`
        :param _TypeD: 时间戳防盗链高级版模式D配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeD`
        :param _TypeE: 时间戳防盗链高级版模式E配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeE: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeE`
        :param _TypeF: 时间戳防盗链高级版模式F配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeF: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeF`
        """
        self._Switch = None
        self._TypeA = None
        self._TypeB = None
        self._TypeC = None
        self._TypeD = None
        self._TypeE = None
        self._TypeF = None

    @property
    def Switch(self):
        """防盗链配置开关，取值有：
on：开启
off：关闭
开启时必须且只配置一种模式，其余模式需要设置为 null
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def TypeA(self):
        """时间戳防盗链高级版模式A配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeA`
        """
        return self._TypeA

    @TypeA.setter
    def TypeA(self, TypeA):
        self._TypeA = TypeA

    @property
    def TypeB(self):
        """时间戳防盗链高级版模式B配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeB`
        """
        return self._TypeB

    @TypeB.setter
    def TypeB(self, TypeB):
        self._TypeB = TypeB

    @property
    def TypeC(self):
        """时间戳防盗链高级版模式C配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeC`
        """
        return self._TypeC

    @TypeC.setter
    def TypeC(self, TypeC):
        self._TypeC = TypeC

    @property
    def TypeD(self):
        """时间戳防盗链高级版模式D配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeD`
        """
        return self._TypeD

    @TypeD.setter
    def TypeD(self, TypeD):
        self._TypeD = TypeD

    @property
    def TypeE(self):
        """时间戳防盗链高级版模式E配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeE`
        """
        return self._TypeE

    @TypeE.setter
    def TypeE(self, TypeE):
        self._TypeE = TypeE

    @property
    def TypeF(self):
        """时间戳防盗链高级版模式F配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeF`
        """
        return self._TypeF

    @TypeF.setter
    def TypeF(self, TypeF):
        self._TypeF = TypeF


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self._TypeA = AdvancedAuthenticationTypeA()
            self._TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self._TypeB = AdvancedAuthenticationTypeB()
            self._TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self._TypeC = AdvancedAuthenticationTypeC()
            self._TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self._TypeD = AdvancedAuthenticationTypeD()
            self._TypeD._deserialize(params.get("TypeD"))
        if params.get("TypeE") is not None:
            self._TypeE = AdvancedAuthenticationTypeE()
            self._TypeE._deserialize(params.get("TypeE"))
        if params.get("TypeF") is not None:
            self._TypeF = AdvancedAuthenticationTypeF()
            self._TypeF._deserialize(params.get("TypeF"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeA(AbstractModel):
    """时间戳防盗链高级版模式A配置。

    """

    def __init__(self):
        r"""
        :param _SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
        :type SecretKey: str
        :param _SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type SignParam: str
        :param _TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type TimeParam: str
        :param _ExpireTime: 过期时间，单位秒。
        :type ExpireTime: int
        :param _ExpireTimeRequired: 是否必须提供过期时间参数。
        :type ExpireTimeRequired: bool
        :param _Format: URL 组成格式，如：${private_key}${schema}${host}${full_uri}。
        :type Format: str
        :param _TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。
        :type TimeFormat: str
        :param _FailCode: 鉴权失败时返回的状态码。
        :type FailCode: int
        :param _ExpireCode: 链接过期时返回的状态码。
        :type ExpireCode: int
        :param _RulePaths: 需要鉴权的url路径列表。
        :type RulePaths: list of str
        :param _Transformation: 保留字段。
        :type Transformation: int
        """
        self._SecretKey = None
        self._SignParam = None
        self._TimeParam = None
        self._ExpireTime = None
        self._ExpireTimeRequired = None
        self._Format = None
        self._TimeFormat = None
        self._FailCode = None
        self._ExpireCode = None
        self._RulePaths = None
        self._Transformation = None

    @property
    def SecretKey(self):
        """用于计算签名的密钥，只允许字母和数字，长度6-32字节。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SignParam(self):
        """uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        """uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :rtype: str
        """
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def ExpireTime(self):
        """过期时间，单位秒。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ExpireTimeRequired(self):
        """是否必须提供过期时间参数。
        :rtype: bool
        """
        return self._ExpireTimeRequired

    @ExpireTimeRequired.setter
    def ExpireTimeRequired(self, ExpireTimeRequired):
        self._ExpireTimeRequired = ExpireTimeRequired

    @property
    def Format(self):
        """URL 组成格式，如：${private_key}${schema}${host}${full_uri}。
        :rtype: str
        """
        return self._Format

    @Format.setter
    def Format(self, Format):
        self._Format = Format

    @property
    def TimeFormat(self):
        """时间格式，dec，hex分别表示十进制，十六进制。
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def FailCode(self):
        """鉴权失败时返回的状态码。
        :rtype: int
        """
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def ExpireCode(self):
        """链接过期时返回的状态码。
        :rtype: int
        """
        return self._ExpireCode

    @ExpireCode.setter
    def ExpireCode(self, ExpireCode):
        self._ExpireCode = ExpireCode

    @property
    def RulePaths(self):
        """需要鉴权的url路径列表。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def Transformation(self):
        """保留字段。
        :rtype: int
        """
        return self._Transformation

    @Transformation.setter
    def Transformation(self, Transformation):
        self._Transformation = Transformation


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._ExpireTime = params.get("ExpireTime")
        self._ExpireTimeRequired = params.get("ExpireTimeRequired")
        self._Format = params.get("Format")
        self._TimeFormat = params.get("TimeFormat")
        self._FailCode = params.get("FailCode")
        self._ExpireCode = params.get("ExpireCode")
        self._RulePaths = params.get("RulePaths")
        self._Transformation = params.get("Transformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeB(AbstractModel):
    """时间戳防盗链高级版模式B配置。

    """

    def __init__(self):
        r"""
        :param _KeyAlpha: alpha键名。
        :type KeyAlpha: str
        :param _KeyBeta: beta键名。
        :type KeyBeta: str
        :param _KeyGamma: gamma键名。
        :type KeyGamma: str
        :param _SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type SignParam: str
        :param _TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type TimeParam: str
        :param _ExpireTime: 过期时间，单位秒。
        :type ExpireTime: int
        :param _TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。
        :type TimeFormat: str
        :param _FailCode: 鉴权失败时返回的状态码。
        :type FailCode: int
        :param _ExpireCode: 链接过期时返回的状态码。
        :type ExpireCode: int
        :param _RulePaths: 需要鉴权的url路径列表。
        :type RulePaths: list of str
        """
        self._KeyAlpha = None
        self._KeyBeta = None
        self._KeyGamma = None
        self._SignParam = None
        self._TimeParam = None
        self._ExpireTime = None
        self._TimeFormat = None
        self._FailCode = None
        self._ExpireCode = None
        self._RulePaths = None

    @property
    def KeyAlpha(self):
        """alpha键名。
        :rtype: str
        """
        return self._KeyAlpha

    @KeyAlpha.setter
    def KeyAlpha(self, KeyAlpha):
        self._KeyAlpha = KeyAlpha

    @property
    def KeyBeta(self):
        """beta键名。
        :rtype: str
        """
        return self._KeyBeta

    @KeyBeta.setter
    def KeyBeta(self, KeyBeta):
        self._KeyBeta = KeyBeta

    @property
    def KeyGamma(self):
        """gamma键名。
        :rtype: str
        """
        return self._KeyGamma

    @KeyGamma.setter
    def KeyGamma(self, KeyGamma):
        self._KeyGamma = KeyGamma

    @property
    def SignParam(self):
        """uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        """uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :rtype: str
        """
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def ExpireTime(self):
        """过期时间，单位秒。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TimeFormat(self):
        """时间格式，dec，hex分别表示十进制，十六进制。
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def FailCode(self):
        """鉴权失败时返回的状态码。
        :rtype: int
        """
        return self._FailCode

    @FailCode.setter
    def FailCode(self, FailCode):
        self._FailCode = FailCode

    @property
    def ExpireCode(self):
        """链接过期时返回的状态码。
        :rtype: int
        """
        return self._ExpireCode

    @ExpireCode.setter
    def ExpireCode(self, ExpireCode):
        self._ExpireCode = ExpireCode

    @property
    def RulePaths(self):
        """需要鉴权的url路径列表。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._KeyAlpha = params.get("KeyAlpha")
        self._KeyBeta = params.get("KeyBeta")
        self._KeyGamma = params.get("KeyGamma")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._ExpireTime = params.get("ExpireTime")
        self._TimeFormat = params.get("TimeFormat")
        self._FailCode = params.get("FailCode")
        self._ExpireCode = params.get("ExpireCode")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeC(AbstractModel):
    """时间戳防盗链高级版模式C配置。

    """

    def __init__(self):
        r"""
        :param _AccessKey: 访问密钥。
        :type AccessKey: str
        :param _SecretKey: 鉴权密钥。
        :type SecretKey: str
        """
        self._AccessKey = None
        self._SecretKey = None

    @property
    def AccessKey(self):
        """访问密钥。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """鉴权密钥。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeD(AbstractModel):
    """时间戳防盗链高级版模式D配置。

    """

    def __init__(self):
        r"""
        :param _SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
        :type SecretKey: str
        :param _BackupSecretKey: 备份密钥，当使用SecretKey鉴权失败时会使用该密钥重新鉴权。
        :type BackupSecretKey: str
        :param _SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type SignParam: str
        :param _TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type TimeParam: str
        :param _ExpireTime: 过期时间，单位秒。
        :type ExpireTime: int
        :param _TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。
        :type TimeFormat: str
        """
        self._SecretKey = None
        self._BackupSecretKey = None
        self._SignParam = None
        self._TimeParam = None
        self._ExpireTime = None
        self._TimeFormat = None

    @property
    def SecretKey(self):
        """用于计算签名的密钥，只允许字母和数字，长度6-32字节。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def BackupSecretKey(self):
        """备份密钥，当使用SecretKey鉴权失败时会使用该密钥重新鉴权。
        :rtype: str
        """
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey

    @property
    def SignParam(self):
        """uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        """uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :rtype: str
        """
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def ExpireTime(self):
        """过期时间，单位秒。
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def TimeFormat(self):
        """时间格式，dec，hex分别表示十进制，十六进制。
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._BackupSecretKey = params.get("BackupSecretKey")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._ExpireTime = params.get("ExpireTime")
        self._TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeE(AbstractModel):
    """时间戳防盗链高级版模式E配置。

    """

    def __init__(self):
        r"""
        :param _SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignParam: str
        :param _AclSignParam: uri串中Acl签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclSignParam: str
        :param _StartTimeParam: uri串中开始时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeParam: str
        :param _ExpireTimeParam: uri串中过期时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTimeParam: str
        :param _TimeFormat: 时间格式，dec
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        """
        self._SecretKey = None
        self._SignParam = None
        self._AclSignParam = None
        self._StartTimeParam = None
        self._ExpireTimeParam = None
        self._TimeFormat = None

    @property
    def SecretKey(self):
        """用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SignParam(self):
        """uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def AclSignParam(self):
        """uri串中Acl签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AclSignParam

    @AclSignParam.setter
    def AclSignParam(self, AclSignParam):
        self._AclSignParam = AclSignParam

    @property
    def StartTimeParam(self):
        """uri串中开始时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._StartTimeParam

    @StartTimeParam.setter
    def StartTimeParam(self, StartTimeParam):
        self._StartTimeParam = StartTimeParam

    @property
    def ExpireTimeParam(self):
        """uri串中过期时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTimeParam

    @ExpireTimeParam.setter
    def ExpireTimeParam(self, ExpireTimeParam):
        self._ExpireTimeParam = ExpireTimeParam

    @property
    def TimeFormat(self):
        """时间格式，dec
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SignParam = params.get("SignParam")
        self._AclSignParam = params.get("AclSignParam")
        self._StartTimeParam = params.get("StartTimeParam")
        self._ExpireTimeParam = params.get("ExpireTimeParam")
        self._TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeF(AbstractModel):
    """时间戳防盗链高级鉴权模式TypeF配置

    """

    def __init__(self):
        r"""
        :param _SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignParam: str
        :param _TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeParam: str
        :param _TransactionParam: uri串中Transaction字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionParam: str
        :param _SecretKey: 用于计算签名的主密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _BackupSecretKey: 用于计算签名的备选密钥，主密钥校验失败后再次尝试备选密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSecretKey: str
        """
        self._SignParam = None
        self._TimeParam = None
        self._TransactionParam = None
        self._SecretKey = None
        self._BackupSecretKey = None

    @property
    def SignParam(self):
        """uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        """uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def TransactionParam(self):
        """uri串中Transaction字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TransactionParam

    @TransactionParam.setter
    def TransactionParam(self, TransactionParam):
        self._TransactionParam = TransactionParam

    @property
    def SecretKey(self):
        """用于计算签名的主密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def BackupSecretKey(self):
        """用于计算签名的备选密钥，主密钥校验失败后再次尝试备选密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._TransactionParam = params.get("TransactionParam")
        self._SecretKey = params.get("SecretKey")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedCCRules(AbstractModel):
    """scdn 的自定义 cc 规则

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _DetectionTime: 探测时长
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionTime: int
        :param _FrequencyLimit: 限频阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyLimit: int
        :param _PunishmentSwitch: IP 惩罚配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishmentSwitch: str
        :param _PunishmentTime: IP 惩罚时长
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishmentTime: int
        :param _Action: 执行动作，intercept|redirect
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _RedirectUrl: 动作为 redirect 时，重定向的url
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param _Configure: 七层限频具体配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Configure: list of ScdnSevenLayerRules
        :param _Switch: 自定义cc规则配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._RuleName = None
        self._DetectionTime = None
        self._FrequencyLimit = None
        self._PunishmentSwitch = None
        self._PunishmentTime = None
        self._Action = None
        self._RedirectUrl = None
        self._Configure = None
        self._Switch = None

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def DetectionTime(self):
        """探测时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DetectionTime

    @DetectionTime.setter
    def DetectionTime(self, DetectionTime):
        self._DetectionTime = DetectionTime

    @property
    def FrequencyLimit(self):
        """限频阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FrequencyLimit

    @FrequencyLimit.setter
    def FrequencyLimit(self, FrequencyLimit):
        self._FrequencyLimit = FrequencyLimit

    @property
    def PunishmentSwitch(self):
        """IP 惩罚配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PunishmentSwitch

    @PunishmentSwitch.setter
    def PunishmentSwitch(self, PunishmentSwitch):
        self._PunishmentSwitch = PunishmentSwitch

    @property
    def PunishmentTime(self):
        """IP 惩罚时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PunishmentTime

    @PunishmentTime.setter
    def PunishmentTime(self, PunishmentTime):
        self._PunishmentTime = PunishmentTime

    @property
    def Action(self):
        """执行动作，intercept|redirect
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        """动作为 redirect 时，重定向的url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def Configure(self):
        """七层限频具体配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnSevenLayerRules
        """
        return self._Configure

    @Configure.setter
    def Configure(self, Configure):
        self._Configure = Configure

    @property
    def Switch(self):
        """自定义cc规则配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        self._DetectionTime = params.get("DetectionTime")
        self._FrequencyLimit = params.get("FrequencyLimit")
        self._PunishmentSwitch = params.get("PunishmentSwitch")
        self._PunishmentTime = params.get("PunishmentTime")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        if params.get("Configure") is not None:
            self._Configure = []
            for item in params.get("Configure"):
                obj = ScdnSevenLayerRules()
                obj._deserialize(item)
                self._Configure.append(obj)
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedCache(AbstractModel):
    """缓存过期配置高级版，注意：此字段已经弃用，请使用RuleCache

    """

    def __init__(self):
        r"""
        :param _CacheRules: 缓存过期规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheRules: list of AdvanceCacheRule
        :param _IgnoreCacheControl: 强制缓存配置
on：开启
off：关闭
开启时，源站返回 no-cache、no-store 头部时，仍按照缓存过期规则进行节点缓存
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param _IgnoreSetCookie: 当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        """
        self._CacheRules = None
        self._IgnoreCacheControl = None
        self._IgnoreSetCookie = None

    @property
    def CacheRules(self):
        """缓存过期规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvanceCacheRule
        """
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules

    @property
    def IgnoreCacheControl(self):
        """强制缓存配置
on：开启
off：关闭
开启时，源站返回 no-cache、no-store 头部时，仍按照缓存过期规则进行节点缓存
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl

    @property
    def IgnoreSetCookie(self):
        """当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreSetCookie

    @IgnoreSetCookie.setter
    def IgnoreSetCookie(self, IgnoreSetCookie):
        self._IgnoreSetCookie = IgnoreSetCookie


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = AdvanceCacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        self._IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedScdnAclGroup(AbstractModel):
    """SCDN精准访问控制配置

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Configure: 具体配置
        :type Configure: list of AdvancedScdnAclRule
        :param _Result: 执行动作，intercept|redirect
        :type Result: str
        :param _Status: 规则是否生效，active|inactive
        :type Status: str
        :param _ErrorPage: 错误页面配置
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self._RuleName = None
        self._Configure = None
        self._Result = None
        self._Status = None
        self._ErrorPage = None

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Configure(self):
        """具体配置
        :rtype: list of AdvancedScdnAclRule
        """
        return self._Configure

    @Configure.setter
    def Configure(self, Configure):
        self._Configure = Configure

    @property
    def Result(self):
        """执行动作，intercept|redirect
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Status(self):
        """规则是否生效，active|inactive
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorPage(self):
        """错误页面配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("Configure") is not None:
            self._Configure = []
            for item in params.get("Configure"):
                obj = AdvancedScdnAclRule()
                obj._deserialize(item)
                self._Configure.append(obj)
        self._Result = params.get("Result")
        self._Status = params.get("Status")
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedScdnAclRule(AbstractModel):
    """精准访问控制匹配规则

    """

    def __init__(self):
        r"""
        :param _MatchKey: 匹配关键字，可取值有：
<li>protocol：HTTP协议</li>
<li>httpVersion：HTTP版本</li>
<li>method：请求方法</li>
<li>ip：请求源IP</li>
<li>ipAsn：请求源IP自治域号</li>
<li>ipCountry：请求源IP所在国家</li>
<li>ipArea：请求源IP所在大区</li>
<li>xForwardFor：请求头X-Forwarded-For</li>
<li>directory：路径</li>
<li>index：首页</li>
<li>path：文件全路径</li>
<li>file：文件扩展名</li>
<li>param：请求参数</li>
<li>referer：请求头Referer</li>
<li>cookie：请求头Cookie</li>
<li>userAgent：请求头User-Agent</li>
<li>head：自定义请求头</li>
        :type MatchKey: str
        :param _LogicOperator: 逻辑操作符，取值如下：
不包含：exclude
包含：include
不等于：notequal
等于：equal
前缀匹配：matching
内容为空或不存在：null
        :type LogicOperator: str
        :param _MatchValue: 匹配值。
当MatchKey为protocol时
取值：HTTP、HTTPS

当MatchKey为httpVersion时
取值：HTTP/1.0、HTTP/1.1、HTTP/1.2、HTTP/2、HTTP/3

当MatchKey为method时
取值：HEAD、GET、POST、PUT、OPTIONS、TRACE、DELETE、PATCH、CONNECT

当MatchKey为ipCountry时，取值为：
其他：OTHER
委内瑞拉：VE
乌拉圭：UY
苏里南：SR
巴拉圭：PY
秘鲁：PE
圭亚那：GY
厄瓜多尔：EC
哥伦比亚：CO
智利：CL
巴西：BR
玻利维亚：BO
阿根廷：AR
新西兰：NZ
萨摩亚：WS
瓦努阿图：VU
图瓦卢：TV
汤加：TO
托克劳：TK
帕劳：PW
纽埃：NU
瑙鲁：NR
基里巴斯：KI
关岛：GU
密克罗尼西亚：FM
澳大利亚：AU
美国：US
波多黎各：PR
多米尼加共和国：DO
哥斯达黎加：CR
东萨摩亚：AS
安提瓜和巴布达：AG
巴拿马：PA
尼加拉瓜：NI
墨西哥：MX
牙买加：JM
海地：HT
洪都拉斯：HN
危地马拉：GT
瓜德罗普岛：GP
格陵兰：GL
格林纳达：GD
古巴：CU
加拿大：CA
伯利兹：BZ
巴哈马：BS
百慕大：BM
巴巴多斯：BB
阿鲁巴：AW
安圭拉：AI
梵蒂冈：VA
斯洛伐克：SK
英国：GB
捷克共和国：CZ
乌克兰：UA
土耳其：TR
斯洛文尼亚：SI
瑞典：SE
塞尔维亚：RS
罗马尼亚：RO
葡萄牙：PT
波兰：PL
挪威：NO
荷兰：NL
马耳他：MT
马其顿：MK
黑山：ME
摩尔多瓦：MD
摩纳哥：MC
拉脱维亚：LV
卢森堡：LU
立陶宛：LT
列支敦士登：LI
哈萨克斯坦：KZ
意大利：IT
冰岛：IS
爱尔兰：IE
匈牙利：HU
克罗地亚：HR
希腊：GR
直布罗陀：GI
根西岛：GG
格鲁吉亚：GE
法国：FR
芬兰：FI
西班牙：ES
爱沙尼亚：EE
丹麦：DK
德国：DE
塞浦路斯：CY
瑞士：CH
白俄罗斯：BY
保加利亚：BG
比利时：BE
阿塞拜疆：AZ
奥地利：AT
亚美尼亚：AM
阿尔巴尼亚：AL
安道尔：AD
东帝汶：TL
叙利亚：SY
沙特阿拉伯：SA
巴勒斯坦：PS
斯里兰卡：LK
斯里兰卡：LK
朝鲜：KP
吉尔吉斯斯坦：KG
中国香港：HK
文莱：BN
孟加拉：BD
阿联酋：AE
也门：YE
越南：VN
乌兹别克斯坦：UZ
中国台湾：TW
土库曼斯坦：TM
塔吉克斯坦：TJ
泰国：TH
新加坡：SG
卡塔尔：QA
巴基斯坦：PK
菲律宾：PH
阿曼：OM
尼泊尔：NP
马来西亚：MY
马尔代夫：MV
中国澳门：MO
蒙古：MN
缅甸：MM
黎巴嫩：LB
科威特：KW
韩国：KR
柬埔寨：KH
日本：JP
约旦：JO
伊朗：IR
伊拉克：IQ
印度：IN
以色列：IL
印度尼西亚：ID
中国：CN
不丹：BT
巴林：BH
阿富汗：AF
利比亚：LY
刚果金：CG
留尼汪岛：RE
斯威士兰：SZ
津巴布韦：ZW
赞比亚：ZM
马约特：YT
乌干达：UG
坦桑尼亚：TZ
突尼斯：TN
多哥：TG
乍得：TD
索马里：SO
塞内加尔：SN
苏丹：SD
塞舌尔：SC
卢旺达：RW
尼日利亚：NG
尼日尔：NE
纳米比亚：NA
莫桑比克：MZ
马拉维：MW
毛里求斯：MU
毛里塔尼亚：MR
马里：ML
马达加斯加：MG
摩洛哥：MA
莱索托：LS
利比里亚：LR
科摩罗：KM
肯尼亚：KE
几内亚：GN
冈比亚：GM
加纳：GH
加蓬：GA
埃塞俄比亚：ET
厄立特里亚：ER
埃及：EG
阿尔及利亚：DZ
吉布提：DJ
喀麦隆：CM
刚果：CG
博茨瓦纳：BW
贝宁：BJ
布隆迪：BI
安哥拉：AO

当MatchKey为ipArea时，取值为：
其他：OTHER
亚洲：AS
欧洲：EU
南极洲：AN
非洲：AF
大洋洲：OC
北美洲：NA
南美洲：SA

当MatchKey为index时
取值为：/;/index.html
        :type MatchValue: list of str
        :param _CaseSensitive: 是否区分大小写 true：区分 false：不区分
        :type CaseSensitive: bool
        :param _MatchKeyParam: 当MatchKey为param时必填：表示请求参数Key 当MatchKey为cookie时必填：表示请求头Cookie中参数的
        :type MatchKeyParam: str
        """
        self._MatchKey = None
        self._LogicOperator = None
        self._MatchValue = None
        self._CaseSensitive = None
        self._MatchKeyParam = None

    @property
    def MatchKey(self):
        """匹配关键字，可取值有：
<li>protocol：HTTP协议</li>
<li>httpVersion：HTTP版本</li>
<li>method：请求方法</li>
<li>ip：请求源IP</li>
<li>ipAsn：请求源IP自治域号</li>
<li>ipCountry：请求源IP所在国家</li>
<li>ipArea：请求源IP所在大区</li>
<li>xForwardFor：请求头X-Forwarded-For</li>
<li>directory：路径</li>
<li>index：首页</li>
<li>path：文件全路径</li>
<li>file：文件扩展名</li>
<li>param：请求参数</li>
<li>referer：请求头Referer</li>
<li>cookie：请求头Cookie</li>
<li>userAgent：请求头User-Agent</li>
<li>head：自定义请求头</li>
        :rtype: str
        """
        return self._MatchKey

    @MatchKey.setter
    def MatchKey(self, MatchKey):
        self._MatchKey = MatchKey

    @property
    def LogicOperator(self):
        """逻辑操作符，取值如下：
不包含：exclude
包含：include
不等于：notequal
等于：equal
前缀匹配：matching
内容为空或不存在：null
        :rtype: str
        """
        return self._LogicOperator

    @LogicOperator.setter
    def LogicOperator(self, LogicOperator):
        self._LogicOperator = LogicOperator

    @property
    def MatchValue(self):
        """匹配值。
当MatchKey为protocol时
取值：HTTP、HTTPS

当MatchKey为httpVersion时
取值：HTTP/1.0、HTTP/1.1、HTTP/1.2、HTTP/2、HTTP/3

当MatchKey为method时
取值：HEAD、GET、POST、PUT、OPTIONS、TRACE、DELETE、PATCH、CONNECT

当MatchKey为ipCountry时，取值为：
其他：OTHER
委内瑞拉：VE
乌拉圭：UY
苏里南：SR
巴拉圭：PY
秘鲁：PE
圭亚那：GY
厄瓜多尔：EC
哥伦比亚：CO
智利：CL
巴西：BR
玻利维亚：BO
阿根廷：AR
新西兰：NZ
萨摩亚：WS
瓦努阿图：VU
图瓦卢：TV
汤加：TO
托克劳：TK
帕劳：PW
纽埃：NU
瑙鲁：NR
基里巴斯：KI
关岛：GU
密克罗尼西亚：FM
澳大利亚：AU
美国：US
波多黎各：PR
多米尼加共和国：DO
哥斯达黎加：CR
东萨摩亚：AS
安提瓜和巴布达：AG
巴拿马：PA
尼加拉瓜：NI
墨西哥：MX
牙买加：JM
海地：HT
洪都拉斯：HN
危地马拉：GT
瓜德罗普岛：GP
格陵兰：GL
格林纳达：GD
古巴：CU
加拿大：CA
伯利兹：BZ
巴哈马：BS
百慕大：BM
巴巴多斯：BB
阿鲁巴：AW
安圭拉：AI
梵蒂冈：VA
斯洛伐克：SK
英国：GB
捷克共和国：CZ
乌克兰：UA
土耳其：TR
斯洛文尼亚：SI
瑞典：SE
塞尔维亚：RS
罗马尼亚：RO
葡萄牙：PT
波兰：PL
挪威：NO
荷兰：NL
马耳他：MT
马其顿：MK
黑山：ME
摩尔多瓦：MD
摩纳哥：MC
拉脱维亚：LV
卢森堡：LU
立陶宛：LT
列支敦士登：LI
哈萨克斯坦：KZ
意大利：IT
冰岛：IS
爱尔兰：IE
匈牙利：HU
克罗地亚：HR
希腊：GR
直布罗陀：GI
根西岛：GG
格鲁吉亚：GE
法国：FR
芬兰：FI
西班牙：ES
爱沙尼亚：EE
丹麦：DK
德国：DE
塞浦路斯：CY
瑞士：CH
白俄罗斯：BY
保加利亚：BG
比利时：BE
阿塞拜疆：AZ
奥地利：AT
亚美尼亚：AM
阿尔巴尼亚：AL
安道尔：AD
东帝汶：TL
叙利亚：SY
沙特阿拉伯：SA
巴勒斯坦：PS
斯里兰卡：LK
斯里兰卡：LK
朝鲜：KP
吉尔吉斯斯坦：KG
中国香港：HK
文莱：BN
孟加拉：BD
阿联酋：AE
也门：YE
越南：VN
乌兹别克斯坦：UZ
中国台湾：TW
土库曼斯坦：TM
塔吉克斯坦：TJ
泰国：TH
新加坡：SG
卡塔尔：QA
巴基斯坦：PK
菲律宾：PH
阿曼：OM
尼泊尔：NP
马来西亚：MY
马尔代夫：MV
中国澳门：MO
蒙古：MN
缅甸：MM
黎巴嫩：LB
科威特：KW
韩国：KR
柬埔寨：KH
日本：JP
约旦：JO
伊朗：IR
伊拉克：IQ
印度：IN
以色列：IL
印度尼西亚：ID
中国：CN
不丹：BT
巴林：BH
阿富汗：AF
利比亚：LY
刚果金：CG
留尼汪岛：RE
斯威士兰：SZ
津巴布韦：ZW
赞比亚：ZM
马约特：YT
乌干达：UG
坦桑尼亚：TZ
突尼斯：TN
多哥：TG
乍得：TD
索马里：SO
塞内加尔：SN
苏丹：SD
塞舌尔：SC
卢旺达：RW
尼日利亚：NG
尼日尔：NE
纳米比亚：NA
莫桑比克：MZ
马拉维：MW
毛里求斯：MU
毛里塔尼亚：MR
马里：ML
马达加斯加：MG
摩洛哥：MA
莱索托：LS
利比里亚：LR
科摩罗：KM
肯尼亚：KE
几内亚：GN
冈比亚：GM
加纳：GH
加蓬：GA
埃塞俄比亚：ET
厄立特里亚：ER
埃及：EG
阿尔及利亚：DZ
吉布提：DJ
喀麦隆：CM
刚果：CG
博茨瓦纳：BW
贝宁：BJ
布隆迪：BI
安哥拉：AO

当MatchKey为ipArea时，取值为：
其他：OTHER
亚洲：AS
欧洲：EU
南极洲：AN
非洲：AF
大洋洲：OC
北美洲：NA
南美洲：SA

当MatchKey为index时
取值为：/;/index.html
        :rtype: list of str
        """
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue

    @property
    def CaseSensitive(self):
        """是否区分大小写 true：区分 false：不区分
        :rtype: bool
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def MatchKeyParam(self):
        """当MatchKey为param时必填：表示请求参数Key 当MatchKey为cookie时必填：表示请求头Cookie中参数的
        :rtype: str
        """
        return self._MatchKeyParam

    @MatchKeyParam.setter
    def MatchKeyParam(self, MatchKeyParam):
        self._MatchKeyParam = MatchKeyParam


    def _deserialize(self, params):
        self._MatchKey = params.get("MatchKey")
        self._LogicOperator = params.get("LogicOperator")
        self._MatchValue = params.get("MatchValue")
        self._CaseSensitive = params.get("CaseSensitive")
        self._MatchKeyParam = params.get("MatchKeyParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Authentication(AbstractModel):
    """时间戳防盗链配置

    """

    def __init__(self):
        r"""
        :param _Switch: 防盗链配置开关，取值有：
on：开启
off：关闭
开启时必须且只配置一种模式，其余模式需要设置为 null
        :type Switch: str
        :param _AuthAlgorithm: 鉴权算法，取值有：
md5：按MD5算法取hash值
sha256：按SHA-256算法取hash值
默认为 md5
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthAlgorithm: str
        :param _TypeA: 时间戳防盗链模式 A 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`
        :param _TypeB: 时间戳防盗链模式 B 配置（模式 B 后台升级中，暂时不支持配置）
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`
        :param _TypeC: 时间戳防盗链模式 C 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`
        :param _TypeD: 时间戳防盗链模式 D 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        self._Switch = None
        self._AuthAlgorithm = None
        self._TypeA = None
        self._TypeB = None
        self._TypeC = None
        self._TypeD = None

    @property
    def Switch(self):
        """防盗链配置开关，取值有：
on：开启
off：关闭
开启时必须且只配置一种模式，其余模式需要设置为 null
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AuthAlgorithm(self):
        """鉴权算法，取值有：
md5：按MD5算法取hash值
sha256：按SHA-256算法取hash值
默认为 md5
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AuthAlgorithm

    @AuthAlgorithm.setter
    def AuthAlgorithm(self, AuthAlgorithm):
        self._AuthAlgorithm = AuthAlgorithm

    @property
    def TypeA(self):
        """时间戳防盗链模式 A 配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`
        """
        return self._TypeA

    @TypeA.setter
    def TypeA(self, TypeA):
        self._TypeA = TypeA

    @property
    def TypeB(self):
        """时间戳防盗链模式 B 配置（模式 B 后台升级中，暂时不支持配置）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`
        """
        return self._TypeB

    @TypeB.setter
    def TypeB(self, TypeB):
        self._TypeB = TypeB

    @property
    def TypeC(self):
        """时间戳防盗链模式 C 配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`
        """
        return self._TypeC

    @TypeC.setter
    def TypeC(self, TypeC):
        self._TypeC = TypeC

    @property
    def TypeD(self):
        """时间戳防盗链模式 D 配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        return self._TypeD

    @TypeD.setter
    def TypeD(self, TypeD):
        self._TypeD = TypeD


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AuthAlgorithm = params.get("AuthAlgorithm")
        if params.get("TypeA") is not None:
            self._TypeA = AuthenticationTypeA()
            self._TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self._TypeB = AuthenticationTypeB()
            self._TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self._TypeC = AuthenticationTypeC()
            self._TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self._TypeD = AuthenticationTypeD()
            self._TypeD._deserialize(params.get("TypeD"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeA(AbstractModel):
    """时间戳防盗链模式 A 配置
    时间戳防盗链模式 A 的访问 URL 格式为：http://DomainName/Filename?sign=timestamp-rand-uid-md5hash
    其中 timestamp 为十进制 UNIX 时间戳；
    rand 为随机字符串，0 ~ 100 位大小写字母与数字组成；
    uid 为 0；
    md5hash：MD5（文件路径-timestamp-rand-uid-自定义密钥）

    """

    def __init__(self):
        r"""
        :param _SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _SignParam: 签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :type SignParam: str
        :param _ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param _FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param _FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        :param _BackupSecretKey: 计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._SignParam = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        """计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def SignParam(self):
        """签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def ExpireTime(self):
        """签名过期时间设置
单位为秒，最大可设置为 630720000
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        """鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :rtype: list of str
        """
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        """whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def BackupSecretKey(self):
        """计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._SignParam = params.get("SignParam")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeB(AbstractModel):
    """时间戳防盗链模式 B 配置（B 模式正在进行平台升级，暂不支持配置）

    """

    def __init__(self):
        r"""
        :param _SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param _FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param _FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        :param _BackupSecretKey: 计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        """计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def ExpireTime(self):
        """签名过期时间设置
单位为秒，最大可设置为 630720000
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        """鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :rtype: list of str
        """
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        """whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def BackupSecretKey(self):
        """计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeC(AbstractModel):
    """时间戳防盗链模式 C 配置
    时间戳防盗链模式 C 的访问 URL 格式为：http://DomainName/md5hash/timestamp/FileName
    其中 timestamp 为十六进制 UNIX 时间戳；
    md5hash：MD5（自定义密钥 + 文件路径 + timestamp）

    """

    def __init__(self):
        r"""
        :param _SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param _FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param _FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        :param _TimeFormat: 时间戳进制设置
dec：十进制
hex：十六进制
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        :param _BackupSecretKey: 计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._TimeFormat = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        """计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def ExpireTime(self):
        """签名过期时间设置
单位为秒，最大可设置为 630720000
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        """鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :rtype: list of str
        """
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        """whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def TimeFormat(self):
        """时间戳进制设置
dec：十进制
hex：十六进制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def BackupSecretKey(self):
        """计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._TimeFormat = params.get("TimeFormat")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeD(AbstractModel):
    """时间戳防盗链模式 D 配置
    时间戳防盗链模式 D 的访问 URL 格式为：http://DomainName/FileName?sign=md5hash&t=timestamp
    其中 timestamp 为十进制或十六进制 UNIX 时间戳；
    md5hash：MD5（自定义密钥 + 文件路径 + timestamp）

    """

    def __init__(self):
        r"""
        :param _SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param _FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param _FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        :param _SignParam: 签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :type SignParam: str
        :param _TimeParam: 时间戳参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :type TimeParam: str
        :param _TimeFormat: 时间戳进制设置
dec：十进制
hex：十六进制
        :type TimeFormat: str
        :param _BackupSecretKey: 计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSecretKey: str
        """
        self._SecretKey = None
        self._ExpireTime = None
        self._FileExtensions = None
        self._FilterType = None
        self._SignParam = None
        self._TimeParam = None
        self._TimeFormat = None
        self._BackupSecretKey = None

    @property
    def SecretKey(self):
        """计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def ExpireTime(self):
        """签名过期时间设置
单位为秒，最大可设置为 630720000
        :rtype: int
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def FileExtensions(self):
        """鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :rtype: list of str
        """
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def FilterType(self):
        """whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def SignParam(self):
        """签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :rtype: str
        """
        return self._SignParam

    @SignParam.setter
    def SignParam(self, SignParam):
        self._SignParam = SignParam

    @property
    def TimeParam(self):
        """时间戳参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :rtype: str
        """
        return self._TimeParam

    @TimeParam.setter
    def TimeParam(self, TimeParam):
        self._TimeParam = TimeParam

    @property
    def TimeFormat(self):
        """时间戳进制设置
dec：十进制
hex：十六进制
        :rtype: str
        """
        return self._TimeFormat

    @TimeFormat.setter
    def TimeFormat(self, TimeFormat):
        self._TimeFormat = TimeFormat

    @property
    def BackupSecretKey(self):
        """计算签名的备用密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupSecretKey

    @BackupSecretKey.setter
    def BackupSecretKey(self, BackupSecretKey):
        self._BackupSecretKey = BackupSecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        self._ExpireTime = params.get("ExpireTime")
        self._FileExtensions = params.get("FileExtensions")
        self._FilterType = params.get("FilterType")
        self._SignParam = params.get("SignParam")
        self._TimeParam = params.get("TimeParam")
        self._TimeFormat = params.get("TimeFormat")
        self._BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AvifAdapter(AbstractModel):
    """图片优化-AvifAdapter配置

    """

    def __init__(self):
        r"""
        :param _Switch: 图片优化AvifAdapter配置项开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _FallbackFormats: 当原图是 avif 且客户端 Accept 头包含 image/avif 时，直接返回原图。
当原图是 avif 且客户端 Accept 头不包含 image/avif 时但包含 image/webp，将 avif 转 webp 格式返回。如果 Accept 头不包含 image/webp, 则转 jpeg 返回。

可用的枚举值： 
- []
- ["webp"]
- ["jpeg"]
- ["webp", "jpeg"]

"webp"：是否开启  avif 转 webp，"jpeg": 是否开启 avif 转 jpeg。如果 webp 和 jpeg 都开启的情况下，webp 必须在 jpeg 前面。
注意：此字段可能返回 null，表示取不到有效值。
        :type FallbackFormats: list of str
        """
        self._Switch = None
        self._FallbackFormats = None

    @property
    def Switch(self):
        """图片优化AvifAdapter配置项开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FallbackFormats(self):
        """当原图是 avif 且客户端 Accept 头包含 image/avif 时，直接返回原图。
当原图是 avif 且客户端 Accept 头不包含 image/avif 时但包含 image/webp，将 avif 转 webp 格式返回。如果 Accept 头不包含 image/webp, 则转 jpeg 返回。

可用的枚举值： 
- []
- ["webp"]
- ["jpeg"]
- ["webp", "jpeg"]

"webp"：是否开启  avif 转 webp，"jpeg": 是否开启 avif 转 jpeg。如果 webp 和 jpeg 都开启的情况下，webp 必须在 jpeg 前面。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FallbackFormats

    @FallbackFormats.setter
    def FallbackFormats(self, FallbackFormats):
        self._FallbackFormats = FallbackFormats


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FallbackFormats = params.get("FallbackFormats")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AwsPrivateAccess(AbstractModel):
    """s3源站回源鉴权。

    """

    def __init__(self):
        r"""
        :param _Switch: s3源站回源鉴权配置项开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _AccessKey: 访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _SecretKey: 密钥，字段为脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Bucket: Bucketname
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Region = None
        self._Bucket = None

    @property
    def Switch(self):
        """s3源站回源鉴权配置项开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        """访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """密钥，字段为脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        """Bucketname
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BandwidthAlert(AbstractModel):
    """带宽封顶配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 用量封顶配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _BpsThreshold: 用量封顶阈值，带宽单位为bps，流量单位byte
注意：此字段可能返回 null，表示取不到有效值。
        :type BpsThreshold: int
        :param _CounterMeasure: 达到阈值后的操作
RETURN_404：全部请求返回 404
注意：此字段可能返回 null，表示取不到有效值。
        :type CounterMeasure: str
        :param _LastTriggerTime: 境内区域上次触发用量封顶阈值的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerTime: str
        :param _AlertSwitch: 用量封顶提醒配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertSwitch: str
        :param _AlertPercentage: 用量封顶阈值提醒百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertPercentage: int
        :param _LastTriggerTimeOverseas: 海外区域上次触发用量封顶阈值的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerTimeOverseas: str
        :param _Metric: 用量阈值触发的维度
带宽：bandwidth
流量：flux
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param _StatisticItems: 累计用量配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StatisticItems: list of StatisticItem
        """
        self._Switch = None
        self._BpsThreshold = None
        self._CounterMeasure = None
        self._LastTriggerTime = None
        self._AlertSwitch = None
        self._AlertPercentage = None
        self._LastTriggerTimeOverseas = None
        self._Metric = None
        self._StatisticItems = None

    @property
    def Switch(self):
        """用量封顶配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BpsThreshold(self):
        """用量封顶阈值，带宽单位为bps，流量单位byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BpsThreshold

    @BpsThreshold.setter
    def BpsThreshold(self, BpsThreshold):
        self._BpsThreshold = BpsThreshold

    @property
    def CounterMeasure(self):
        """达到阈值后的操作
RETURN_404：全部请求返回 404
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CounterMeasure

    @CounterMeasure.setter
    def CounterMeasure(self, CounterMeasure):
        self._CounterMeasure = CounterMeasure

    @property
    def LastTriggerTime(self):
        """境内区域上次触发用量封顶阈值的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastTriggerTime

    @LastTriggerTime.setter
    def LastTriggerTime(self, LastTriggerTime):
        self._LastTriggerTime = LastTriggerTime

    @property
    def AlertSwitch(self):
        """用量封顶提醒配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlertSwitch

    @AlertSwitch.setter
    def AlertSwitch(self, AlertSwitch):
        self._AlertSwitch = AlertSwitch

    @property
    def AlertPercentage(self):
        """用量封顶阈值提醒百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AlertPercentage

    @AlertPercentage.setter
    def AlertPercentage(self, AlertPercentage):
        self._AlertPercentage = AlertPercentage

    @property
    def LastTriggerTimeOverseas(self):
        """海外区域上次触发用量封顶阈值的时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._LastTriggerTimeOverseas

    @LastTriggerTimeOverseas.setter
    def LastTriggerTimeOverseas(self, LastTriggerTimeOverseas):
        self._LastTriggerTimeOverseas = LastTriggerTimeOverseas

    @property
    def Metric(self):
        """用量阈值触发的维度
带宽：bandwidth
流量：flux
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def StatisticItems(self):
        """累计用量配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StatisticItem
        """
        return self._StatisticItems

    @StatisticItems.setter
    def StatisticItems(self, StatisticItems):
        self._StatisticItems = StatisticItems


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._BpsThreshold = params.get("BpsThreshold")
        self._CounterMeasure = params.get("CounterMeasure")
        self._LastTriggerTime = params.get("LastTriggerTime")
        self._AlertSwitch = params.get("AlertSwitch")
        self._AlertPercentage = params.get("AlertPercentage")
        self._LastTriggerTimeOverseas = params.get("LastTriggerTimeOverseas")
        self._Metric = params.get("Metric")
        if params.get("StatisticItems") is not None:
            self._StatisticItems = []
            for item in params.get("StatisticItems"):
                obj = StatisticItem()
                obj._deserialize(item)
                self._StatisticItems.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotCookie(AbstractModel):
    """Bot cookie策略

    """

    def __init__(self):
        r"""
        :param _Switch: Bot cookie策略配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _RuleType: 规则类型，当前只有all
        :type RuleType: str
        :param _RuleValue: 规则值，['*']
        :type RuleValue: list of str
        :param _Action: 执行动作，monitor|intercept|redirect|captcha
        :type Action: str
        :param _RedirectUrl: 重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._Switch = None
        self._RuleType = None
        self._RuleValue = None
        self._Action = None
        self._RedirectUrl = None
        self._UpdateTime = None

    @property
    def Switch(self):
        """Bot cookie策略配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleType(self):
        """规则类型，当前只有all
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        """规则值，['*']
        :rtype: list of str
        """
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Action(self):
        """执行动作，monitor|intercept|redirect|captcha
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        """重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotJavaScript(AbstractModel):
    """Bot js策略

    """

    def __init__(self):
        r"""
        :param _Switch: Bot js策略配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _RuleType: 规则类型，当前只有file
        :type RuleType: str
        :param _RuleValue: 规则值，['html', 'htm']
        :type RuleValue: list of str
        :param _Action: 执行动作，monitor|intercept|redirect|captcha
        :type Action: str
        :param _RedirectUrl: 重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._Switch = None
        self._RuleType = None
        self._RuleValue = None
        self._Action = None
        self._RedirectUrl = None
        self._UpdateTime = None

    @property
    def Switch(self):
        """Bot js策略配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleType(self):
        """规则类型，当前只有file
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        """规则值，['html', 'htm']
        :rtype: list of str
        """
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Action(self):
        """执行动作，monitor|intercept|redirect|captcha
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        """重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotRecord(AbstractModel):
    """BOT记录详细内容

    """

    def __init__(self):
        r"""
        :param _Action: 动作，取值为以为3个类型中的一个："intercept","permit","monitor"，分别表示： 拦截， 放行，监控
        :type Action: str
        :param _Nums: 会话总次数
        :type Nums: int
        :param _RuleName: BotType=UB时，表示预测标签，取值如下：
                "crawler_unregular",
                "crawler_regular",
                "request_repeat",
                "credential_miss_user",
                "credential_without_user",
                "credential_only_action",
                "credential_user_password",
                "credential_cracking",
                "credential_stuffing",
                "brush_sms",
                "brush_captcha",
                "reg_malicious"
BotType=TCB时，表示Bot分类，取值如下：
                "Uncategorised",
                "Search engine bot",
                "Site monitor",
                "Screenshot creator",
                "Link checker",
                "Web scraper",
                "Vulnerability scanner",
                "Virus scanner",
                "Speed tester",
                "Feed Fetcher",
                "Tool",
                "Marketing"
BotType=UCB时，为二期接口，暂时未定义内容
        :type RuleName: str
        :param _SessionDuration: 会话持续时间
        :type SessionDuration: float
        :param _SrcIp: 访问源IP
        :type SrcIp: str
        :param _BotFeature: 异常特征
        :type BotFeature: list of str
        :param _Time: 最新检测时间
        :type Time: str
        :param _Score: BOT得分
        :type Score: int
        :param _AvgSpeed: 平均速率
        :type AvgSpeed: float
        :param _TcbDetail: BotType=TCB，表示TCB名称
注意：此字段可能返回 null，表示取不到有效值。
        :type TcbDetail: str
        :param _Id: BOT记录唯一ID，用于查询访问详情
        :type Id: str
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._Action = None
        self._Nums = None
        self._RuleName = None
        self._SessionDuration = None
        self._SrcIp = None
        self._BotFeature = None
        self._Time = None
        self._Score = None
        self._AvgSpeed = None
        self._TcbDetail = None
        self._Id = None
        self._Domain = None

    @property
    def Action(self):
        """动作，取值为以为3个类型中的一个："intercept","permit","monitor"，分别表示： 拦截， 放行，监控
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Nums(self):
        """会话总次数
        :rtype: int
        """
        return self._Nums

    @Nums.setter
    def Nums(self, Nums):
        self._Nums = Nums

    @property
    def RuleName(self):
        """BotType=UB时，表示预测标签，取值如下：
                "crawler_unregular",
                "crawler_regular",
                "request_repeat",
                "credential_miss_user",
                "credential_without_user",
                "credential_only_action",
                "credential_user_password",
                "credential_cracking",
                "credential_stuffing",
                "brush_sms",
                "brush_captcha",
                "reg_malicious"
BotType=TCB时，表示Bot分类，取值如下：
                "Uncategorised",
                "Search engine bot",
                "Site monitor",
                "Screenshot creator",
                "Link checker",
                "Web scraper",
                "Vulnerability scanner",
                "Virus scanner",
                "Speed tester",
                "Feed Fetcher",
                "Tool",
                "Marketing"
BotType=UCB时，为二期接口，暂时未定义内容
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def SessionDuration(self):
        """会话持续时间
        :rtype: float
        """
        return self._SessionDuration

    @SessionDuration.setter
    def SessionDuration(self, SessionDuration):
        self._SessionDuration = SessionDuration

    @property
    def SrcIp(self):
        """访问源IP
        :rtype: str
        """
        return self._SrcIp

    @SrcIp.setter
    def SrcIp(self, SrcIp):
        self._SrcIp = SrcIp

    @property
    def BotFeature(self):
        """异常特征
        :rtype: list of str
        """
        return self._BotFeature

    @BotFeature.setter
    def BotFeature(self, BotFeature):
        self._BotFeature = BotFeature

    @property
    def Time(self):
        """最新检测时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Score(self):
        """BOT得分
        :rtype: int
        """
        return self._Score

    @Score.setter
    def Score(self, Score):
        self._Score = Score

    @property
    def AvgSpeed(self):
        """平均速率
        :rtype: float
        """
        return self._AvgSpeed

    @AvgSpeed.setter
    def AvgSpeed(self, AvgSpeed):
        self._AvgSpeed = AvgSpeed

    @property
    def TcbDetail(self):
        """BotType=TCB，表示TCB名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TcbDetail

    @TcbDetail.setter
    def TcbDetail(self, TcbDetail):
        self._TcbDetail = TcbDetail

    @property
    def Id(self):
        """BOT记录唯一ID，用于查询访问详情
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Domain(self):
        """域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._Nums = params.get("Nums")
        self._RuleName = params.get("RuleName")
        self._SessionDuration = params.get("SessionDuration")
        self._SrcIp = params.get("SrcIp")
        self._BotFeature = params.get("BotFeature")
        self._Time = params.get("Time")
        self._Score = params.get("Score")
        self._AvgSpeed = params.get("AvgSpeed")
        self._TcbDetail = params.get("TcbDetail")
        self._Id = params.get("Id")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotSortBy(AbstractModel):
    """Bot记录的排序选项

    """

    def __init__(self):
        r"""
        :param _Key: 排序参数名称， 取值为：timestamp， nums， session_duration，score.total，stat.avg_speed分别表示按照：最新检测时间，会话总次数，会话持续时间，BOT得分，平均速率排序
        :type Key: str
        :param _Sequence: asc/desc
        :type Sequence: str
        """
        self._Key = None
        self._Sequence = None

    @property
    def Key(self):
        """排序参数名称， 取值为：timestamp， nums， session_duration，score.total，stat.avg_speed分别表示按照：最新检测时间，会话总次数，会话持续时间，BOT得分，平均速率排序
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Sequence(self):
        """asc/desc
        :rtype: str
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotStatisticsCount(AbstractModel):
    """session/ip维度的bot统计复杂对象

    """

    def __init__(self):
        r"""
        :param _Count: BOT次数
        :type Count: int
        :param _Value: Top指标值,如果是ip维度就是ip如果是session维度就是域名
        :type Value: str
        :param _Country: ip所在国家
        :type Country: str
        :param _Province: ip所在省份
        :type Province: str
        :param _Isp: ip归属的idc
        :type Isp: str
        """
        self._Count = None
        self._Value = None
        self._Country = None
        self._Province = None
        self._Isp = None

    @property
    def Count(self):
        """BOT次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Value(self):
        """Top指标值,如果是ip维度就是ip如果是session维度就是域名
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Country(self):
        """ip所在国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """ip所在省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Isp(self):
        """ip归属的idc
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp


    def _deserialize(self, params):
        self._Count = params.get("Count")
        self._Value = params.get("Value")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._Isp = params.get("Isp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotStats(AbstractModel):
    """BOT统计结果数据

    """

    def __init__(self):
        r"""
        :param _Metric: 指标名称
        :type Metric: str
        :param _DetailData: 指标详细数据
        :type DetailData: list of BotStatsDetailData
        """
        self._Metric = None
        self._DetailData = None

    @property
    def Metric(self):
        """指标名称
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DetailData(self):
        """指标详细数据
        :rtype: list of BotStatsDetailData
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = BotStatsDetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotStatsDetailData(AbstractModel):
    """BOT统计结果数据详细数据

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _Value: 数据值
        :type Value: int
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """数据值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BriefDomain(AbstractModel):
    """域名基础配置信息，含 CNAME、状态、业务类型、加速区域、创建时间、更新时间、源站配置等。

    """

    def __init__(self):
        r"""
        :param _ResourceId: 域名 ID
        :type ResourceId: str
        :param _AppId: 腾讯云账号 ID
        :type AppId: int
        :param _Domain: 加速域名
        :type Domain: str
        :param _Cname: 域名对应的 CNAME 地址
        :type Cname: str
        :param _Status: 加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
closing：关闭中
online：已启动
offline：已关闭
        :type Status: str
        :param _ProjectId: 项目 ID，可前往腾讯云项目管理页面查看
        :type ProjectId: int
        :param _ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :type ServiceType: str
        :param _CreateTime: 域名创建时间
        :type CreateTime: str
        :param _UpdateTime: 域名更新时间
        :type UpdateTime: str
        :param _Origin: 源站配置详情
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _Disable: 域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定
        :type Disable: str
        :param _Area: 加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
        :type Area: str
        :param _Readonly: 域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
        :type Readonly: str
        :param _Product: 域名所属产品，cdn/ecdn
        :type Product: str
        :param _ParentHost: 主域名
        :type ParentHost: str
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._ServiceType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._Disable = None
        self._Area = None
        self._Readonly = None
        self._Product = None
        self._ParentHost = None

    @property
    def ResourceId(self):
        """域名 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        """腾讯云账号 ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        """加速域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        """域名对应的 CNAME 地址
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        """加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
closing：关闭中
online：已启动
offline：已关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        """项目 ID，可前往腾讯云项目管理页面查看
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ServiceType(self):
        """域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def CreateTime(self):
        """域名创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """域名更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        """源站配置详情
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Disable(self):
        """域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定
        :rtype: str
        """
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Area(self):
        """加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        """域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
        :rtype: str
        """
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def Product(self):
        """域名所属产品，cdn/ecdn
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def ParentHost(self):
        """主域名
        :rtype: str
        """
        return self._ParentHost

    @ParentHost.setter
    def ParentHost(self, ParentHost):
        self._ParentHost = ParentHost


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ServiceType = params.get("ServiceType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._Disable = params.get("Disable")
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        self._Product = params.get("Product")
        self._ParentHost = params.get("ParentHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """节点缓存过期时间配置，分为以下两种：
    + 基础版缓存过期规则配置
    + 高级版缓存过期规则配置

    """

    def __init__(self):
        r"""
        :param _SimpleCache: 基础缓存过期时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SimpleCache: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`
        :param _AdvancedCache: 高级缓存过期时间配置（已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedCache: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`
        :param _RuleCache: 高级路径缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCache: list of RuleCache
        """
        self._SimpleCache = None
        self._AdvancedCache = None
        self._RuleCache = None

    @property
    def SimpleCache(self):
        """基础缓存过期时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`
        """
        return self._SimpleCache

    @SimpleCache.setter
    def SimpleCache(self, SimpleCache):
        self._SimpleCache = SimpleCache

    @property
    def AdvancedCache(self):
        """高级缓存过期时间配置（已弃用）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`
        """
        return self._AdvancedCache

    @AdvancedCache.setter
    def AdvancedCache(self, AdvancedCache):
        self._AdvancedCache = AdvancedCache

    @property
    def RuleCache(self):
        """高级路径缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RuleCache
        """
        return self._RuleCache

    @RuleCache.setter
    def RuleCache(self, RuleCache):
        self._RuleCache = RuleCache


    def _deserialize(self, params):
        if params.get("SimpleCache") is not None:
            self._SimpleCache = SimpleCache()
            self._SimpleCache._deserialize(params.get("SimpleCache"))
        if params.get("AdvancedCache") is not None:
            self._AdvancedCache = AdvancedCache()
            self._AdvancedCache._deserialize(params.get("AdvancedCache"))
        if params.get("RuleCache") is not None:
            self._RuleCache = []
            for item in params.get("RuleCache"):
                obj = RuleCache()
                obj._deserialize(item)
                self._RuleCache.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfig(AbstractModel):
    """启发式自定义时间缓存配置

    """

    def __init__(self):
        r"""
        :param _HeuristicCacheTimeSwitch: 启发式自定义时间缓存配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type HeuristicCacheTimeSwitch: str
        :param _HeuristicCacheTime: 单位 秒.
注意：此字段可能返回 null，表示取不到有效值。
        :type HeuristicCacheTime: int
        """
        self._HeuristicCacheTimeSwitch = None
        self._HeuristicCacheTime = None

    @property
    def HeuristicCacheTimeSwitch(self):
        """启发式自定义时间缓存配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HeuristicCacheTimeSwitch

    @HeuristicCacheTimeSwitch.setter
    def HeuristicCacheTimeSwitch(self, HeuristicCacheTimeSwitch):
        self._HeuristicCacheTimeSwitch = HeuristicCacheTimeSwitch

    @property
    def HeuristicCacheTime(self):
        """单位 秒.
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._HeuristicCacheTime

    @HeuristicCacheTime.setter
    def HeuristicCacheTime(self, HeuristicCacheTime):
        self._HeuristicCacheTime = HeuristicCacheTime


    def _deserialize(self, params):
        self._HeuristicCacheTimeSwitch = params.get("HeuristicCacheTimeSwitch")
        self._HeuristicCacheTime = params.get("HeuristicCacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """路径缓存缓存配置

    """

    def __init__(self):
        r"""
        :param _Switch: 路径缓存配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        :param _CompareMaxAge: 高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareMaxAge: str
        :param _IgnoreCacheControl: 强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param _IgnoreSetCookie: 当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        :param _OriginMtimeCheckType: 当缓存过期后，是否开启源站 mtime 校验，配置值为equal、since、none 和 null。默认配置值为equal，会校验源站文件的mtime与长度。2024-09-12 18:00 之前创建的域名默认值 null，行为保持不变。
equal：源站响应mtime必须和缓存mtime一致，若mtime值不一致，清除缓存。
since：若源站响应mtime大于缓存mtime，清除缓存。
none： 缓存过期回源重新获取文件mtime和长度后，不会校验源站响应mtime，若源站响应携带Content-Length头部，只有文件大小改变时才会更新缓存；若源站响应不携带Content-Length头部，会更新缓存。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginMtimeCheckType: str
        """
        self._Switch = None
        self._CacheTime = None
        self._CompareMaxAge = None
        self._IgnoreCacheControl = None
        self._IgnoreSetCookie = None
        self._OriginMtimeCheckType = None

    @property
    def Switch(self):
        """路径缓存配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheTime(self):
        """缓存过期时间设置
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime

    @property
    def CompareMaxAge(self):
        """高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompareMaxAge

    @CompareMaxAge.setter
    def CompareMaxAge(self, CompareMaxAge):
        self._CompareMaxAge = CompareMaxAge

    @property
    def IgnoreCacheControl(self):
        """强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl

    @property
    def IgnoreSetCookie(self):
        """当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreSetCookie

    @IgnoreSetCookie.setter
    def IgnoreSetCookie(self, IgnoreSetCookie):
        self._IgnoreSetCookie = IgnoreSetCookie

    @property
    def OriginMtimeCheckType(self):
        """当缓存过期后，是否开启源站 mtime 校验，配置值为equal、since、none 和 null。默认配置值为equal，会校验源站文件的mtime与长度。2024-09-12 18:00 之前创建的域名默认值 null，行为保持不变。
equal：源站响应mtime必须和缓存mtime一致，若mtime值不一致，清除缓存。
since：若源站响应mtime大于缓存mtime，清除缓存。
none： 缓存过期回源重新获取文件mtime和长度后，不会校验源站响应mtime，若源站响应携带Content-Length头部，只有文件大小改变时才会更新缓存；若源站响应不携带Content-Length头部，会更新缓存。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginMtimeCheckType

    @OriginMtimeCheckType.setter
    def OriginMtimeCheckType(self, OriginMtimeCheckType):
        self._OriginMtimeCheckType = OriginMtimeCheckType


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._CacheTime = params.get("CacheTime")
        self._CompareMaxAge = params.get("CompareMaxAge")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        self._IgnoreSetCookie = params.get("IgnoreSetCookie")
        self._OriginMtimeCheckType = params.get("OriginMtimeCheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """路径缓存遵循源站配置

    """

    def __init__(self):
        r"""
        :param _Switch: 路径缓存遵循源站配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _HeuristicCache: 启发式缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type HeuristicCache: :class:`tencentcloud.cdn.v20180606.models.HeuristicCache`
        :param _OriginMtimeCheckType: 当缓存过期后，是否开启源站 mtime 校验，配置值为equal、since、none 和 null。默认配置值为equal，会校验源站文件的mtime与长度。2024-09-12 18:00 之前创建的域名默认值 null，行为保持不变。
equal：源站响应mtime必须和缓存mtime一致，若mtime值不一致，清除缓存。
since：若源站响应mtime大于缓存mtime，清除缓存。
none： 缓存过期回源重新获取文件mtime和长度后，不会校验源站响应mtime，若源站响应携带Content-Length头部，只有文件大小改变时才会更新缓存；若源站响应不携带Content-Length头部，会更新缓存。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginMtimeCheckType: str
        """
        self._Switch = None
        self._HeuristicCache = None
        self._OriginMtimeCheckType = None

    @property
    def Switch(self):
        """路径缓存遵循源站配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeuristicCache(self):
        """启发式缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HeuristicCache`
        """
        return self._HeuristicCache

    @HeuristicCache.setter
    def HeuristicCache(self, HeuristicCache):
        self._HeuristicCache = HeuristicCache

    @property
    def OriginMtimeCheckType(self):
        """当缓存过期后，是否开启源站 mtime 校验，配置值为equal、since、none 和 null。默认配置值为equal，会校验源站文件的mtime与长度。2024-09-12 18:00 之前创建的域名默认值 null，行为保持不变。
equal：源站响应mtime必须和缓存mtime一致，若mtime值不一致，清除缓存。
since：若源站响应mtime大于缓存mtime，清除缓存。
none： 缓存过期回源重新获取文件mtime和长度后，不会校验源站响应mtime，若源站响应携带Content-Length头部，只有文件大小改变时才会更新缓存；若源站响应不携带Content-Length头部，会更新缓存。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginMtimeCheckType

    @OriginMtimeCheckType.setter
    def OriginMtimeCheckType(self, OriginMtimeCheckType):
        self._OriginMtimeCheckType = OriginMtimeCheckType


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("HeuristicCache") is not None:
            self._HeuristicCache = HeuristicCache()
            self._HeuristicCache._deserialize(params.get("HeuristicCache"))
        self._OriginMtimeCheckType = params.get("OriginMtimeCheckType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """路径缓存不缓存配置

    """

    def __init__(self):
        r"""
        :param _Switch: 路径缓存不缓存配置配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Revalidate: 总是回源站校验
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Revalidate: str
        """
        self._Switch = None
        self._Revalidate = None

    @property
    def Switch(self):
        """路径缓存不缓存配置配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Revalidate(self):
        """总是回源站校验
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Revalidate

    @Revalidate.setter
    def Revalidate(self, Revalidate):
        self._Revalidate = Revalidate


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Revalidate = params.get("Revalidate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存键配置（忽略参数配置）

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数忽略）
off：关闭全路径缓存（即开启参数忽略）
        :type FullUrlCache: str
        :param _IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param _QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.QueryStringKey`
        :param _Cookie: CacheKey中包含Cookie
注意：此字段可能返回 null，表示取不到有效值。
        :type Cookie: :class:`tencentcloud.cdn.v20180606.models.CookieKey`
        :param _Header: CacheKey中包含请求头部
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: :class:`tencentcloud.cdn.v20180606.models.HeaderKey`
        :param _CacheTag: CacheKey中包含自定义字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTag: :class:`tencentcloud.cdn.v20180606.models.CacheTagKey`
        :param _Scheme: CacheKey中包含请求协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: :class:`tencentcloud.cdn.v20180606.models.SchemeKey`
        :param _KeyRules: 分路径缓存键配置
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyRules: list of KeyRule
        """
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None
        self._Cookie = None
        self._Header = None
        self._CacheTag = None
        self._Scheme = None
        self._KeyRules = None

    @property
    def FullUrlCache(self):
        """是否开启全路径缓存
on：开启全路径缓存（即关闭参数忽略）
off：关闭全路径缓存（即开启参数忽略）
        :rtype: str
        """
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        """是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        """CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.QueryStringKey`
        """
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def Cookie(self):
        """CacheKey中包含Cookie
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CookieKey`
        """
        return self._Cookie

    @Cookie.setter
    def Cookie(self, Cookie):
        self._Cookie = Cookie

    @property
    def Header(self):
        """CacheKey中包含请求头部
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HeaderKey`
        """
        return self._Header

    @Header.setter
    def Header(self, Header):
        self._Header = Header

    @property
    def CacheTag(self):
        """CacheKey中包含自定义字符串
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheTagKey`
        """
        return self._CacheTag

    @CacheTag.setter
    def CacheTag(self, CacheTag):
        self._CacheTag = CacheTag

    @property
    def Scheme(self):
        """CacheKey中包含请求协议
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SchemeKey`
        """
        return self._Scheme

    @Scheme.setter
    def Scheme(self, Scheme):
        self._Scheme = Scheme

    @property
    def KeyRules(self):
        """分路径缓存键配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of KeyRule
        """
        return self._KeyRules

    @KeyRules.setter
    def KeyRules(self, KeyRules):
        self._KeyRules = KeyRules


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = QueryStringKey()
            self._QueryString._deserialize(params.get("QueryString"))
        if params.get("Cookie") is not None:
            self._Cookie = CookieKey()
            self._Cookie._deserialize(params.get("Cookie"))
        if params.get("Header") is not None:
            self._Header = HeaderKey()
            self._Header._deserialize(params.get("Header"))
        if params.get("CacheTag") is not None:
            self._CacheTag = CacheTagKey()
            self._CacheTag._deserialize(params.get("CacheTag"))
        if params.get("Scheme") is not None:
            self._Scheme = SchemeKey()
            self._Scheme._deserialize(params.get("Scheme"))
        if params.get("KeyRules") is not None:
            self._KeyRules = []
            for item in params.get("KeyRules"):
                obj = KeyRule()
                obj._deserialize(item)
                self._KeyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheOptResult(AbstractModel):
    """违规资源封禁/解封返回类型

    """

    def __init__(self):
        r"""
        :param _SuccessUrls: 成功的url列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessUrls: list of str
        :param _FailUrls: 失败的url列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailUrls: list of str
        """
        self._SuccessUrls = None
        self._FailUrls = None

    @property
    def SuccessUrls(self):
        """成功的url列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._SuccessUrls

    @SuccessUrls.setter
    def SuccessUrls(self, SuccessUrls):
        self._SuccessUrls = SuccessUrls

    @property
    def FailUrls(self):
        """失败的url列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FailUrls

    @FailUrls.setter
    def FailUrls(self, FailUrls):
        self._FailUrls = FailUrls


    def _deserialize(self, params):
        self._SuccessUrls = params.get("SuccessUrls")
        self._FailUrls = params.get("FailUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheTagKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        r"""
        :param _Switch: 使用CacheTag作为CacheKey的一部分配置开关，取值有
on：开启，使用CacheTag作为CacheKey的一部分
off：关闭，不使用CacheTag作为CacheKey的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Value: 自定义CacheTag的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Switch = None
        self._Value = None

    @property
    def Switch(self):
        """使用CacheTag作为CacheKey的一部分配置开关，取值有
on：开启，使用CacheTag作为CacheKey的一部分
off：关闭，不使用CacheTag作为CacheKey的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Value(self):
        """自定义CacheTag的值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CappingRule(AbstractModel):
    """下行限速配置规则，最多可配置 100 条

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
        :type RuleType: str
        :param _RulePaths: RuleType 对应类型下的匹配内容： 
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
        :type RulePaths: list of str
        :param _KBpsThreshold: 下行速度值设置，单位为 KB/s
        :type KBpsThreshold: int
        """
        self._RuleType = None
        self._RulePaths = None
        self._KBpsThreshold = None

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """RuleType 对应类型下的匹配内容： 
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def KBpsThreshold(self):
        """下行速度值设置，单位为 KB/s
        :rtype: int
        """
        return self._KBpsThreshold

    @KBpsThreshold.setter
    def KBpsThreshold(self, KBpsThreshold):
        self._KBpsThreshold = KBpsThreshold


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._KBpsThreshold = params.get("KBpsThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CcTopData(AbstractModel):
    """CC攻击Top数据

    """

    def __init__(self):
        r"""
        :param _Ip: 客户端Ip
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _Url: 访问URL
注意：此字段可能返回 null，表示取不到有效值。
        :type Url: str
        :param _UserAgent: 客户端UserAgent
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAgent: str
        :param _Value: 请求数
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: int
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._Ip = None
        self._Url = None
        self._UserAgent = None
        self._Value = None
        self._Domain = None

    @property
    def Ip(self):
        """客户端Ip
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Url(self):
        """访问URL
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def UserAgent(self):
        """客户端UserAgent
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Value(self):
        """请求数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Domain(self):
        """域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Url = params.get("Url")
        self._UserAgent = params.get("UserAgent")
        self._Value = params.get("Value")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnData(AbstractModel):
    """访问明细数据类型

    """

    def __init__(self):
        r"""
        :param _Metric: 查询指定的指标名称：
flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
fluxHitRate：流量命中率，单位为 %
statusCode：状态码，返回 2XX、3XX、4XX、5XX 汇总数据，单位为 个
2XX：返回 2XX 状态码汇总及各 2 开头状态码数据，单位为 个
3XX：返回 3XX 状态码汇总及各 3 开头状态码数据，单位为 个
4XX：返回 4XX 状态码汇总及各 4 开头状态码数据，单位为 个
5XX：返回 5XX 状态码汇总及各 5 开头状态码数据，单位为 个
或指定查询的某一具体状态码
        :type Metric: str
        :param _DetailData: 明细数据组合
        :type DetailData: list of TimestampData
        :param _SummarizedData: 汇总数据组合
        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        self._Metric = None
        self._DetailData = None
        self._SummarizedData = None

    @property
    def Metric(self):
        """查询指定的指标名称：
flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
fluxHitRate：流量命中率，单位为 %
statusCode：状态码，返回 2XX、3XX、4XX、5XX 汇总数据，单位为 个
2XX：返回 2XX 状态码汇总及各 2 开头状态码数据，单位为 个
3XX：返回 3XX 状态码汇总及各 3 开头状态码数据，单位为 个
4XX：返回 4XX 状态码汇总及各 4 开头状态码数据，单位为 个
5XX：返回 5XX 状态码汇总及各 5 开头状态码数据，单位为 个
或指定查询的某一具体状态码
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def DetailData(self):
        """明细数据组合
        :rtype: list of TimestampData
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData

    @property
    def SummarizedData(self):
        """汇总数据组合
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        return self._SummarizedData

    @SummarizedData.setter
    def SummarizedData(self, SummarizedData):
        self._SummarizedData = SummarizedData


    def _deserialize(self, params):
        self._Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        if params.get("SummarizedData") is not None:
            self._SummarizedData = SummarizedData()
            self._SummarizedData._deserialize(params.get("SummarizedData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIp(AbstractModel):
    """IP 属性信息

    """

    def __init__(self):
        r"""
        :param _Ip: 指定查询的 IP
        :type Ip: str
        :param _Platform: IP 归属：
yes：节点归属于腾讯云 CDN
no：节点不属于腾讯云 CDN
        :type Platform: str
        :param _Location: 节点所处的省份/国家
unknown 表示节点位置未知
        :type Location: str
        :param _History: 节点上下线历史记录
        :type History: list of CdnIpHistory
        :param _Area: 节点的所在区域
mainland：中国境内加速节点
overseas：中国境外加速节点
unknown：服务地域无法获取
        :type Area: str
        :param _City: 节点的所在城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        """
        self._Ip = None
        self._Platform = None
        self._Location = None
        self._History = None
        self._Area = None
        self._City = None

    @property
    def Ip(self):
        """指定查询的 IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Platform(self):
        """IP 归属：
yes：节点归属于腾讯云 CDN
no：节点不属于腾讯云 CDN
        :rtype: str
        """
        return self._Platform

    @Platform.setter
    def Platform(self, Platform):
        self._Platform = Platform

    @property
    def Location(self):
        """节点所处的省份/国家
unknown 表示节点位置未知
        :rtype: str
        """
        return self._Location

    @Location.setter
    def Location(self, Location):
        self._Location = Location

    @property
    def History(self):
        """节点上下线历史记录
        :rtype: list of CdnIpHistory
        """
        return self._History

    @History.setter
    def History(self, History):
        self._History = History

    @property
    def Area(self):
        """节点的所在区域
mainland：中国境内加速节点
overseas：中国境外加速节点
unknown：服务地域无法获取
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def City(self):
        """节点的所在城市
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._Platform = params.get("Platform")
        self._Location = params.get("Location")
        if params.get("History") is not None:
            self._History = []
            for item in params.get("History"):
                obj = CdnIpHistory()
                obj._deserialize(item)
                self._History.append(obj)
        self._Area = params.get("Area")
        self._City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIpHistory(AbstractModel):
    """CDN 节点上下线历史记录

    """

    def __init__(self):
        r"""
        :param _Status: 操作类型
online：节点上线
offline：节点下线
        :type Status: str
        :param _Datetime: 操作类型对应的操作时间
当该值为 null 时表示无历史状态变更记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Datetime: str
        """
        self._Status = None
        self._Datetime = None

    @property
    def Status(self):
        """操作类型
online：节点上线
offline：节点下线
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Datetime(self):
        """操作类型对应的操作时间
当该值为 null 时表示无历史状态变更记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Datetime

    @Datetime.setter
    def Datetime(self, Datetime):
        self._Datetime = Datetime


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._Datetime = params.get("Datetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientCert(AbstractModel):
    """https 客户端证书配置

    """

    def __init__(self):
        r"""
        :param _Certificate: 客户端证书
PEM 格式，需要进行 Base 64 编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param _CertName: 客户端证书名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param _ExpireTime: 证书过期时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DeployTime: 证书颁发时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        """
        self._Certificate = None
        self._CertName = None
        self._ExpireTime = None
        self._DeployTime = None

    @property
    def Certificate(self):
        """客户端证书
PEM 格式，需要进行 Base 64 编码
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def CertName(self):
        """客户端证书名称
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def ExpireTime(self):
        """证书过期时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        """证书颁发时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime


    def _deserialize(self, params):
        self._Certificate = params.get("Certificate")
        self._CertName = params.get("CertName")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientInfo(AbstractModel):
    """客户端信息

    """

    def __init__(self):
        r"""
        :param _ProvName: 省份。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProvName: str
        :param _Country: 国家。
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param _IspName: 运营商。
注意：此字段可能返回 null，表示取不到有效值。
        :type IspName: str
        :param _Ip: 客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        """
        self._ProvName = None
        self._Country = None
        self._IspName = None
        self._Ip = None

    @property
    def ProvName(self):
        """省份。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ProvName

    @ProvName.setter
    def ProvName(self, ProvName):
        self._ProvName = ProvName

    @property
    def Country(self):
        """国家。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def IspName(self):
        """运营商。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IspName

    @IspName.setter
    def IspName(self, IspName):
        self._IspName = IspName

    @property
    def Ip(self):
        """客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._ProvName = params.get("ProvName")
        self._Country = params.get("Country")
        self._IspName = params.get("IspName")
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogIpData(AbstractModel):
    """通过Cls日志，计算出来的IP每秒访问数量

    """

    def __init__(self):
        r"""
        :param _ClientIp: IP
        :type ClientIp: str
        :param _Request: 在给定的时间段中，1秒内的最大请求量
        :type Request: int
        :param _Count: 在获取的Top信息中，IP出现的次数
        :type Count: int
        :param _Time: 在给定的时间段中，1秒内的最大请求量对应的时间
        :type Time: str
        """
        self._ClientIp = None
        self._Request = None
        self._Count = None
        self._Time = None

    @property
    def ClientIp(self):
        """IP
        :rtype: str
        """
        return self._ClientIp

    @ClientIp.setter
    def ClientIp(self, ClientIp):
        self._ClientIp = ClientIp

    @property
    def Request(self):
        """在给定的时间段中，1秒内的最大请求量
        :rtype: int
        """
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request

    @property
    def Count(self):
        """在获取的Top信息中，IP出现的次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Time(self):
        """在给定的时间段中，1秒内的最大请求量对应的时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._ClientIp = params.get("ClientIp")
        self._Request = params.get("Request")
        self._Count = params.get("Count")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogObject(AbstractModel):
    """CLS日志搜索对象

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题ID
        :type TopicId: str
        :param _TopicName: 主题名字
        :type TopicName: str
        :param _Timestamp: 日志时间
        :type Timestamp: str
        :param _Content: 日志内容
        :type Content: str
        :param _Filename: 采集路径
        :type Filename: str
        :param _Source: 日志来源设备
        :type Source: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Timestamp = None
        self._Content = None
        self._Filename = None
        self._Source = None

    @property
    def TopicId(self):
        """主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名字
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Timestamp(self):
        """日志时间
        :rtype: str
        """
        return self._Timestamp

    @Timestamp.setter
    def Timestamp(self, Timestamp):
        self._Timestamp = Timestamp

    @property
    def Content(self):
        """日志内容
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content

    @property
    def Filename(self):
        """采集路径
        :rtype: str
        """
        return self._Filename

    @Filename.setter
    def Filename(self, Filename):
        self._Filename = Filename

    @property
    def Source(self):
        """日志来源设备
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Timestamp = params.get("Timestamp")
        self._Content = params.get("Content")
        self._Filename = params.get("Filename")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsSearchLogs(AbstractModel):
    """Cls日志搜索结果

    """

    def __init__(self):
        r"""
        :param _Context: 获取更多检索结果的游标
        :type Context: str
        :param _Listover: 搜索结果是否已经全部返回
        :type Listover: bool
        :param _Results: 日志内容信息
        :type Results: list of ClsLogObject
        """
        self._Context = None
        self._Listover = None
        self._Results = None

    @property
    def Context(self):
        """获取更多检索结果的游标
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Listover(self):
        """搜索结果是否已经全部返回
        :rtype: bool
        """
        return self._Listover

    @Listover.setter
    def Listover(self, Listover):
        self._Listover = Listover

    @property
    def Results(self):
        """日志内容信息
        :rtype: list of ClsLogObject
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results


    def _deserialize(self, params):
        self._Context = params.get("Context")
        self._Listover = params.get("Listover")
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = ClsLogObject()
                obj._deserialize(item)
                self._Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compatibility(AbstractModel):
    """是否兼容旧版配置

    """

    def __init__(self):
        r"""
        :param _Code: 兼容标志状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        """
        self._Code = None

    @property
    def Code(self):
        """兼容标志状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code


    def _deserialize(self, params):
        self._Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """智能压缩配置，默认对 js、html、css、xml、json、shtml、htm 后缀且大小为 256 ~ 2097152 字节的文件进行 GZIP 压缩

    """

    def __init__(self):
        r"""
        :param _Switch: 智能压缩配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _CompressionRules: 压缩规则数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CompressionRules: list of CompressionRule
        """
        self._Switch = None
        self._CompressionRules = None

    @property
    def Switch(self):
        """智能压缩配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CompressionRules(self):
        """压缩规则数组
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CompressionRule
        """
        return self._CompressionRules

    @CompressionRules.setter
    def CompressionRules(self, CompressionRules):
        self._CompressionRules = CompressionRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CompressionRules") is not None:
            self._CompressionRules = []
            for item in params.get("CompressionRules"):
                obj = CompressionRule()
                obj._deserialize(item)
                self._CompressionRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressionRule(AbstractModel):
    """智能压缩规则配置

    """

    def __init__(self):
        r"""
        :param _Compress: true：需要设置为 ture，启用压缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Compress: bool
        :param _MinLength: 触发压缩的文件长度最小值，单位为字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinLength: int
        :param _MaxLength: 触发压缩的文件长度最大值，单位为字节数
最大可设置为 30MB
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxLength: int
        :param _Algorithms: 文件压缩算法
gzip：指定 GZIP 压缩
brotli：指定Brotli压缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Algorithms: list of str
        :param _FileExtensions: 根据文件后缀类型压缩
例如 jpg、txt
注意：此字段可能返回 null，表示取不到有效值。
        :type FileExtensions: list of str
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
contentType：指定Content-Type头为特定值时生效
当指定了此字段时，FileExtensions字段不生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RulePaths: CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
contentType 时填充 text/html
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self._Compress = None
        self._MinLength = None
        self._MaxLength = None
        self._Algorithms = None
        self._FileExtensions = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def Compress(self):
        """true：需要设置为 ture，启用压缩
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Compress

    @Compress.setter
    def Compress(self, Compress):
        self._Compress = Compress

    @property
    def MinLength(self):
        """触发压缩的文件长度最小值，单位为字节数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MinLength

    @MinLength.setter
    def MinLength(self, MinLength):
        self._MinLength = MinLength

    @property
    def MaxLength(self):
        """触发压缩的文件长度最大值，单位为字节数
最大可设置为 30MB
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxLength

    @MaxLength.setter
    def MaxLength(self, MaxLength):
        self._MaxLength = MaxLength

    @property
    def Algorithms(self):
        """文件压缩算法
gzip：指定 GZIP 压缩
brotli：指定Brotli压缩
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Algorithms

    @Algorithms.setter
    def Algorithms(self, Algorithms):
        self._Algorithms = Algorithms

    @property
    def FileExtensions(self):
        """根据文件后缀类型压缩
例如 jpg、txt
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FileExtensions

    @FileExtensions.setter
    def FileExtensions(self, FileExtensions):
        self._FileExtensions = FileExtensions

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
contentType：指定Content-Type头为特定值时生效
当指定了此字段时，FileExtensions字段不生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
contentType 时填充 text/html
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._Compress = params.get("Compress")
        self._MinLength = params.get("MinLength")
        self._MaxLength = params.get("MaxLength")
        self._Algorithms = params.get("Algorithms")
        self._FileExtensions = params.get("FileExtensions")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CookieKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        r"""
        :param _Switch: 使用Cookie作为Cache的一部分配置开关，取值有：
on：开启，使用Cookie作为Cache的一部分
off：关闭，不使用Cookie作为Cache的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Value: 使用的cookie，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Switch = None
        self._Value = None

    @property
    def Switch(self):
        """使用Cookie作为Cache的一部分配置开关，取值有：
on：开启，使用Cookie作为Cache的一部分
off：关闭，不使用Cookie作为Cache的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Value(self):
        """使用的cookie，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicRequest(AbstractModel):
    """CreateClsLogTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        :param _DomainAreaConfigs: 域名区域信息
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self._TopicName = None
        self._LogsetId = None
        self._Channel = None
        self._DomainAreaConfigs = None

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def DomainAreaConfigs(self):
        """域名区域信息
        :rtype: list of DomainAreaConfig
        """
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs


    def _deserialize(self, params):
        self._TopicName = params.get("TopicName")
        self._LogsetId = params.get("LogsetId")
        self._Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicResponse(AbstractModel):
    """CreateClsLogTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopicId = None
        self._RequestId = None

    @property
    def TopicId(self):
        """主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._RequestId = params.get("RequestId")


class CreateDiagnoseUrlRequest(AbstractModel):
    """CreateDiagnoseUrl请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 需诊断的url，形如：http://www.test.com/test.txt。
        :type Url: str
        :param _Origin: 请求源带协议头，形如：https://console.cloud.tencent.com
        :type Origin: str
        """
        self._Url = None
        self._Origin = None

    @property
    def Url(self):
        """需诊断的url，形如：http://www.test.com/test.txt。
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Origin(self):
        """请求源带协议头，形如：https://console.cloud.tencent.com
        :rtype: str
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Origin = params.get("Origin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDiagnoseUrlResponse(AbstractModel):
    """CreateDiagnoseUrl返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DiagnoseLink: 系统生成的诊断链接，一个诊断链接最多可访问10次，有效期为24h。
        :type DiagnoseLink: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DiagnoseLink = None
        self._RequestId = None

    @property
    def DiagnoseLink(self):
        """系统生成的诊断链接，一个诊断链接最多可访问10次，有效期为24h。
        :rtype: str
        """
        return self._DiagnoseLink

    @DiagnoseLink.setter
    def DiagnoseLink(self, DiagnoseLink):
        self._DiagnoseLink = DiagnoseLink

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._DiagnoseLink = params.get("DiagnoseLink")
        self._RequestId = params.get("RequestId")


class CreateEdgePackTaskRequest(AbstractModel):
    """CreateEdgePackTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _CosBucket: apk 所在的 cos 存储桶, 如 edgepack-xxxxxxxx
        :type CosBucket: str
        :param _CosUriFrom: apk 源文件的存储路径, 如 /apk/xxxx.apk
        :type CosUriFrom: str
        :param _BlockID: BlockID 的值, WALLE为1903654775(0x71777777)，VasDolly为2282837503(0x881155ff),传0或不传时默认为 WALLE 方案
        :type BlockID: int
        :param _CosUriTo: 拓展之后的 apk 目标存储路径,如 /out/xxxx.apk
        :type CosUriTo: str
        """
        self._CosBucket = None
        self._CosUriFrom = None
        self._BlockID = None
        self._CosUriTo = None

    @property
    def CosBucket(self):
        """apk 所在的 cos 存储桶, 如 edgepack-xxxxxxxx
        :rtype: str
        """
        return self._CosBucket

    @CosBucket.setter
    def CosBucket(self, CosBucket):
        self._CosBucket = CosBucket

    @property
    def CosUriFrom(self):
        """apk 源文件的存储路径, 如 /apk/xxxx.apk
        :rtype: str
        """
        return self._CosUriFrom

    @CosUriFrom.setter
    def CosUriFrom(self, CosUriFrom):
        self._CosUriFrom = CosUriFrom

    @property
    def BlockID(self):
        """BlockID 的值, WALLE为1903654775(0x71777777)，VasDolly为2282837503(0x881155ff),传0或不传时默认为 WALLE 方案
        :rtype: int
        """
        return self._BlockID

    @BlockID.setter
    def BlockID(self, BlockID):
        self._BlockID = BlockID

    @property
    def CosUriTo(self):
        """拓展之后的 apk 目标存储路径,如 /out/xxxx.apk
        :rtype: str
        """
        return self._CosUriTo

    @CosUriTo.setter
    def CosUriTo(self, CosUriTo):
        self._CosUriTo = CosUriTo


    def _deserialize(self, params):
        self._CosBucket = params.get("CosBucket")
        self._CosUriFrom = params.get("CosUriFrom")
        self._BlockID = params.get("BlockID")
        self._CosUriTo = params.get("CosUriTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgePackTaskResponse(AbstractModel):
    """CreateEdgePackTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class CreateScdnDomainRequest(AbstractModel):
    """CreateScdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Waf: Web 攻击防护（WAF）配置
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param _Acl: 自定义防护策略配置
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param _CC: CC 防护配置，目前 CC 防护默认开启
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param _Ddos: DDOS 防护配置，目前 DDoS 防护默认开启
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param _Bot: BOT 防护配置
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        self._Domain = None
        self._Waf = None
        self._Acl = None
        self._CC = None
        self._Ddos = None
        self._Bot = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Waf(self):
        """Web 攻击防护（WAF）配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        """
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def Acl(self):
        """自定义防护策略配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        """
        return self._Acl

    @Acl.setter
    def Acl(self, Acl):
        self._Acl = Acl

    @property
    def CC(self):
        """CC 防护配置，目前 CC 防护默认开启
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        """
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def Ddos(self):
        """DDOS 防护配置，目前 DDoS 防护默认开启
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        """
        return self._Ddos

    @Ddos.setter
    def Ddos(self, Ddos):
        self._Ddos = Ddos

    @property
    def Bot(self):
        """BOT 防护配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        return self._Bot

    @Bot.setter
    def Bot(self, Bot):
        self._Bot = Bot


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("Waf") is not None:
            self._Waf = ScdnWafConfig()
            self._Waf._deserialize(params.get("Waf"))
        if params.get("Acl") is not None:
            self._Acl = ScdnAclConfig()
            self._Acl._deserialize(params.get("Acl"))
        if params.get("CC") is not None:
            self._CC = ScdnConfig()
            self._CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self._Ddos = ScdnDdosConfig()
            self._Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self._Bot = ScdnBotConfig()
            self._Bot._deserialize(params.get("Bot"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnDomainResponse(AbstractModel):
    """CreateScdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建结果，Success表示成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """创建结果，Success表示成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateScdnFailedLogTaskRequest(AbstractModel):
    """CreateScdnFailedLogTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 重试失败任务的taskID
        :type TaskId: str
        :param _Area: 地域：mainland或overseas
        :type Area: str
        """
        self._TaskId = None
        self._Area = None

    @property
    def TaskId(self):
        """重试失败任务的taskID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Area(self):
        """地域：mainland或overseas
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnFailedLogTaskResponse(AbstractModel):
    """CreateScdnFailedLogTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建结果, 
"0" -> 创建成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """创建结果, 
"0" -> 创建成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateScdnLogTaskRequest(AbstractModel):
    """CreateScdnLogTask请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 防护类型
Mode 映射如下：
  waf = "Web攻击"
  cc = "CC攻击"
  bot = "Bot攻击"
        :type Mode: str
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param _Domain: 指定域名查询, 不填默认查询全部域名
        :type Domain: str
        :param _AttackType: 指定攻击类型, 不填默认查询全部攻击类型
AttackType 映射如下:
  other = '未知类型'
  malicious_scan = "恶意扫描"
  sql_inject = "SQL注入攻击"
  xss = "XSS攻击"
  cmd_inject = "命令注入攻击"
  ldap_inject = "LDAP注入攻击"
  ssi_inject = "SSI注入攻击"
  xml_inject = "XML注入攻击"
  web_service = "WEB服务漏洞攻击"
  web_app = "WEB应用漏洞攻击"
  path_traversal = "路径跨越攻击"
  illegal_access_core_file = "核心文件非法访问"
  trojan_horse = "木马后门攻击"
  csrf = "CSRF攻击"
  malicious_file_upload= '恶意文件上传'
  js = "JS主动探测"
  cookie = "Cookie指纹"
        :type AttackType: str
        :param _DefenceMode: 指定执行动作, 不填默认查询全部执行动作
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
  captcha = "验证码"
  redirect = "重定向"
        :type DefenceMode: str
        :param _Ip: 不填为全部ip
        :type Ip: str
        :param _Domains: 指定域名查询, 与 Domain 参数同时有值时使用 Domains 参数，不填默认查询全部域名，指定域名查询时最多支持同时选择 5 个域名查询
        :type Domains: list of str
        :param _AttackTypes: 指定攻击类型查询, 与 AttackType 参数同时有值时使用 AttackTypes 参数，不填默认查询全部攻击类型
        :type AttackTypes: list of str
        :param _Conditions: 查询条件
        :type Conditions: list of ScdnEventLogConditions
        :param _Source: 来源产品 cdn ecdn
        :type Source: str
        :param _Area: 地域：mainland 或 overseas
        :type Area: str
        """
        self._Mode = None
        self._StartTime = None
        self._EndTime = None
        self._Domain = None
        self._AttackType = None
        self._DefenceMode = None
        self._Ip = None
        self._Domains = None
        self._AttackTypes = None
        self._Conditions = None
        self._Source = None
        self._Area = None

    @property
    def Mode(self):
        """防护类型
Mode 映射如下：
  waf = "Web攻击"
  cc = "CC攻击"
  bot = "Bot攻击"
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domain(self):
        """指定域名查询, 不填默认查询全部域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AttackType(self):
        """指定攻击类型, 不填默认查询全部攻击类型
AttackType 映射如下:
  other = '未知类型'
  malicious_scan = "恶意扫描"
  sql_inject = "SQL注入攻击"
  xss = "XSS攻击"
  cmd_inject = "命令注入攻击"
  ldap_inject = "LDAP注入攻击"
  ssi_inject = "SSI注入攻击"
  xml_inject = "XML注入攻击"
  web_service = "WEB服务漏洞攻击"
  web_app = "WEB应用漏洞攻击"
  path_traversal = "路径跨越攻击"
  illegal_access_core_file = "核心文件非法访问"
  trojan_horse = "木马后门攻击"
  csrf = "CSRF攻击"
  malicious_file_upload= '恶意文件上传'
  js = "JS主动探测"
  cookie = "Cookie指纹"
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def DefenceMode(self):
        """指定执行动作, 不填默认查询全部执行动作
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
  captcha = "验证码"
  redirect = "重定向"
        :rtype: str
        """
        return self._DefenceMode

    @DefenceMode.setter
    def DefenceMode(self, DefenceMode):
        self._DefenceMode = DefenceMode

    @property
    def Ip(self):
        """不填为全部ip
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def Domains(self):
        """指定域名查询, 与 Domain 参数同时有值时使用 Domains 参数，不填默认查询全部域名，指定域名查询时最多支持同时选择 5 个域名查询
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def AttackTypes(self):
        """指定攻击类型查询, 与 AttackType 参数同时有值时使用 AttackTypes 参数，不填默认查询全部攻击类型
        :rtype: list of str
        """
        return self._AttackTypes

    @AttackTypes.setter
    def AttackTypes(self, AttackTypes):
        self._AttackTypes = AttackTypes

    @property
    def Conditions(self):
        """查询条件
        :rtype: list of ScdnEventLogConditions
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Source(self):
        """来源产品 cdn ecdn
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Area(self):
        """地域：mainland 或 overseas
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domain = params.get("Domain")
        self._AttackType = params.get("AttackType")
        self._DefenceMode = params.get("DefenceMode")
        self._Ip = params.get("Ip")
        self._Domains = params.get("Domains")
        self._AttackTypes = params.get("AttackTypes")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ScdnEventLogConditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Source = params.get("Source")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnLogTaskResponse(AbstractModel):
    """CreateScdnLogTask返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建结果, 
"0" -> 创建成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """创建结果, 
"0" -> 创建成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class CreateVerifyRecordRequest(AbstractModel):
    """CreateVerifyRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 要取回的域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """要取回的域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVerifyRecordResponse(AbstractModel):
    """CreateVerifyRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _SubDomain: 子解析
        :type SubDomain: str
        :param _Record: 解析值
        :type Record: str
        :param _RecordType: 解析类型
        :type RecordType: str
        :param _FileVerifyUrl: 文件验证 URL 指引
注意：此字段可能返回 null，表示取不到有效值。
        :type FileVerifyUrl: str
        :param _FileVerifyDomains: 文件校验域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FileVerifyDomains: list of str
        :param _FileVerifyName: 文件校验文件名
注意：此字段可能返回 null，表示取不到有效值。
        :type FileVerifyName: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubDomain = None
        self._Record = None
        self._RecordType = None
        self._FileVerifyUrl = None
        self._FileVerifyDomains = None
        self._FileVerifyName = None
        self._RequestId = None

    @property
    def SubDomain(self):
        """子解析
        :rtype: str
        """
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Record(self):
        """解析值
        :rtype: str
        """
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def RecordType(self):
        """解析类型
        :rtype: str
        """
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def FileVerifyUrl(self):
        """文件验证 URL 指引
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileVerifyUrl

    @FileVerifyUrl.setter
    def FileVerifyUrl(self, FileVerifyUrl):
        self._FileVerifyUrl = FileVerifyUrl

    @property
    def FileVerifyDomains(self):
        """文件校验域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._FileVerifyDomains

    @FileVerifyDomains.setter
    def FileVerifyDomains(self, FileVerifyDomains):
        self._FileVerifyDomains = FileVerifyDomains

    @property
    def FileVerifyName(self):
        """文件校验文件名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FileVerifyName

    @FileVerifyName.setter
    def FileVerifyName(self, FileVerifyName):
        self._FileVerifyName = FileVerifyName

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._Record = params.get("Record")
        self._RecordType = params.get("RecordType")
        self._FileVerifyUrl = params.get("FileVerifyUrl")
        self._FileVerifyDomains = params.get("FileVerifyDomains")
        self._FileVerifyName = params.get("FileVerifyName")
        self._RequestId = params.get("RequestId")


class DDoSAttackBandwidthData(AbstractModel):
    """ddos攻击带宽峰值数据

    """

    def __init__(self):
        r"""
        :param _AttackType: ddos攻击类型，当值为all的时候表示所有的攻击类型的总带宽峰值
        :type AttackType: str
        :param _Value: ddos攻击带宽大小
        :type Value: float
        :param _Time: 攻击时间点
        :type Time: str
        """
        self._AttackType = None
        self._Value = None
        self._Time = None

    @property
    def AttackType(self):
        """ddos攻击类型，当值为all的时候表示所有的攻击类型的总带宽峰值
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Value(self):
        """ddos攻击带宽大小
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Time(self):
        """攻击时间点
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time


    def _deserialize(self, params):
        self._AttackType = params.get("AttackType")
        self._Value = params.get("Value")
        self._Time = params.get("Time")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSAttackIPTopData(AbstractModel):
    """攻击ip数据详细数据

    """

    def __init__(self):
        r"""
        :param _AttackIP: 攻击ip
        :type AttackIP: str
        :param _Province: 攻击ip所在省份
        :type Province: str
        :param _Country: 攻击ip所在国家
        :type Country: str
        :param _Isp: 红果电信
        :type Isp: str
        :param _AttackCount: 攻击次数
        :type AttackCount: float
        """
        self._AttackIP = None
        self._Province = None
        self._Country = None
        self._Isp = None
        self._AttackCount = None

    @property
    def AttackIP(self):
        """攻击ip
        :rtype: str
        """
        return self._AttackIP

    @AttackIP.setter
    def AttackIP(self, AttackIP):
        self._AttackIP = AttackIP

    @property
    def Province(self):
        """攻击ip所在省份
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Country(self):
        """攻击ip所在国家
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Isp(self):
        """红果电信
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def AttackCount(self):
        """攻击次数
        :rtype: float
        """
        return self._AttackCount

    @AttackCount.setter
    def AttackCount(self, AttackCount):
        self._AttackCount = AttackCount


    def _deserialize(self, params):
        self._AttackIP = params.get("AttackIP")
        self._Province = params.get("Province")
        self._Country = params.get("Country")
        self._Isp = params.get("Isp")
        self._AttackCount = params.get("AttackCount")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSStatsData(AbstractModel):
    """DDoS统计数据

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _Value: 带宽数值，单位bps
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """带宽数值，单位bps
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DDoSTopData(AbstractModel):
    """DDoS攻击Top数据

    """

    def __init__(self):
        r"""
        :param _AttackType: 攻击类型
        :type AttackType: str
        :param _Value: 攻击带宽，单位：bps
        :type Value: int
        """
        self._AttackType = None
        self._Value = None

    @property
    def AttackType(self):
        """攻击类型
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Value(self):
        """攻击带宽，单位：bps
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._AttackType = params.get("AttackType")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
域名状态需要为【已停用】
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
域名状态需要为【已停用】
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteClsLogTopicRequest(AbstractModel):
    """DeleteClsLogTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        """
        self._TopicId = None
        self._LogsetId = None
        self._Channel = None

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._LogsetId = params.get("LogsetId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClsLogTopicResponse(AbstractModel):
    """DeleteClsLogTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DeleteScdnDomainRequest(AbstractModel):
    """DeleteScdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteScdnDomainResponse(AbstractModel):
    """DeleteScdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 创建结果，Success表示成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """创建结果，Success表示成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定起始时间为 2018-09-04 10:40:00 按小时粒度查询，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定结束时间为  2018-09-04 10:40:00 按小时粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type EndTime: str
        :param _Interval: 时间粒度，支持模式如下：
min：1 分钟粒度，查询区间需要小于等于 24 小时
5min：5 分钟粒度，查询区间需要小于等于 31 天(计费数据粒度)
hour：1 小时粒度，查询区间需要小于等于 31 天内
day：天粒度，查询区间需要大于 31 天

Area 字段为 overseas 时暂不支持1分钟粒度数据查询
        :type Interval: str
        :param _Domain: 指定域名查询计费数据
        :type Domain: str
        :param _Project: 指定项目 ID 查询，[前往查看项目 ID](https://console.cloud.tencent.com/project)
若 Domain 参数填充了具体域名信息，则返回该域名的计费数据，而非指定项目计费数据
        :type Project: int
        :param _Area: 指定加速区域查询计费数据：
mainland：中国境内
overseas：中国境外
不填充时，默认为 mainland
        :type Area: str
        :param _District: Area 为 overseas 时，指定国家/地区查询
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
不填充时，查询所有国家/地区
        :type District: int
        :param _Metric: 计费统计类型
flux：计费流量
bandwidth：计费带宽
默认为 bandwidth
        :type Metric: str
        :param _Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :type Product: str
        :param _TimeZone: 指定查询时间的时区，默认UTC+08:00
        :type TimeZone: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Interval = None
        self._Domain = None
        self._Project = None
        self._Area = None
        self._District = None
        self._Metric = None
        self._Product = None
        self._TimeZone = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定起始时间为 2018-09-04 10:40:00 按小时粒度查询，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定结束时间为  2018-09-04 10:40:00 按小时粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Interval(self):
        """时间粒度，支持模式如下：
min：1 分钟粒度，查询区间需要小于等于 24 小时
5min：5 分钟粒度，查询区间需要小于等于 31 天(计费数据粒度)
hour：1 小时粒度，查询区间需要小于等于 31 天内
day：天粒度，查询区间需要大于 31 天

Area 字段为 overseas 时暂不支持1分钟粒度数据查询
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domain(self):
        """指定域名查询计费数据
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Project(self):
        """指定项目 ID 查询，[前往查看项目 ID](https://console.cloud.tencent.com/project)
若 Domain 参数填充了具体域名信息，则返回该域名的计费数据，而非指定项目计费数据
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Area(self):
        """指定加速区域查询计费数据：
mainland：中国境内
overseas：中国境外
不填充时，默认为 mainland
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def District(self):
        """Area 为 overseas 时，指定国家/地区查询
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
不填充时，查询所有国家/地区
        :rtype: int
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Metric(self):
        """计费统计类型
flux：计费流量
bandwidth：计费带宽
默认为 bandwidth
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Product(self):
        """指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def TimeZone(self):
        """指定查询时间的时区，默认UTC+08:00
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        self._Domain = params.get("Domain")
        self._Project = params.get("Project")
        self._Area = params.get("Area")
        self._District = params.get("District")
        self._Metric = params.get("Metric")
        self._Product = params.get("Product")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 时间粒度，根据查询时传递参数指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :type Interval: str
        :param _Data: 数据明细
        :type Data: list of ResourceBillingData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        """时间粒度，根据查询时传递参数指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        """数据明细
        :rtype: list of ResourceBillingData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceBillingData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCcDataRequest(AbstractModel):
    """DescribeCcData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param _Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :type Interval: str
        :param _Domain: 指定域名查询，为空时，表示查询账号级别数据
        :type Domain: str
        :param _ActionName: 执行动作，取值为：intercept/redirect/observe
分别表示：拦截/重定向/观察
为空时，表示所有执行动作
        :type ActionName: str
        :param _Domains: 指定域名列表查询，为空时，表示查询账号级别数据
        :type Domains: list of str
        :param _Source: cdn表示CDN数据，默认值
ecdn表示ECDN数据
        :type Source: str
        :param _Area: 地域：mainland或overseas，表示国内或海外，不填写默认表示国内
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Interval = None
        self._Domain = None
        self._ActionName = None
        self._Domains = None
        self._Source = None
        self._Area = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domain(self):
        """指定域名查询，为空时，表示查询账号级别数据
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ActionName(self):
        """执行动作，取值为：intercept/redirect/observe
分别表示：拦截/重定向/观察
为空时，表示所有执行动作
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Domains(self):
        """指定域名列表查询，为空时，表示查询账号级别数据
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Source(self):
        """cdn表示CDN数据，默认值
ecdn表示ECDN数据
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Area(self):
        """地域：mainland或overseas，表示国内或海外，不填写默认表示国内
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        self._Domain = params.get("Domain")
        self._ActionName = params.get("ActionName")
        self._Domains = params.get("Domains")
        self._Source = params.get("Source")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCcDataResponse(AbstractModel):
    """DescribeCcData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 指定执行动作的请求数数据，如果指定类型为空，表示所有类型的请求总数
        :type Data: list of TimestampData
        :param _Interval: 粒度
        :type Interval: str
        :param _InterceptQpsData: 执行动作为拦截类型QPS统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type InterceptQpsData: list of TimestampData
        :param _RedirectQpsData: 执行动作为重定向类型QPS统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectQpsData: list of TimestampData
        :param _ObserveQpsData: 执行动作为观察类型QPS统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :type ObserveQpsData: list of TimestampData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._InterceptQpsData = None
        self._RedirectQpsData = None
        self._ObserveQpsData = None
        self._RequestId = None

    @property
    def Data(self):
        """指定执行动作的请求数数据，如果指定类型为空，表示所有类型的请求总数
        :rtype: list of TimestampData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        """粒度
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def InterceptQpsData(self):
        """执行动作为拦截类型QPS统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TimestampData
        """
        return self._InterceptQpsData

    @InterceptQpsData.setter
    def InterceptQpsData(self, InterceptQpsData):
        self._InterceptQpsData = InterceptQpsData

    @property
    def RedirectQpsData(self):
        """执行动作为重定向类型QPS统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TimestampData
        """
        return self._RedirectQpsData

    @RedirectQpsData.setter
    def RedirectQpsData(self, RedirectQpsData):
        self._RedirectQpsData = RedirectQpsData

    @property
    def ObserveQpsData(self):
        """执行动作为观察类型QPS统计数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TimestampData
        """
        return self._ObserveQpsData

    @ObserveQpsData.setter
    def ObserveQpsData(self, ObserveQpsData):
        self._ObserveQpsData = ObserveQpsData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimestampData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        if params.get("InterceptQpsData") is not None:
            self._InterceptQpsData = []
            for item in params.get("InterceptQpsData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._InterceptQpsData.append(obj)
        if params.get("RedirectQpsData") is not None:
            self._RedirectQpsData = []
            for item in params.get("RedirectQpsData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._RedirectQpsData.append(obj)
        if params.get("ObserveQpsData") is not None:
            self._ObserveQpsData = []
            for item in params.get("ObserveQpsData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._ObserveQpsData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type EndTime: str
        :param _Metric: 指定查询指标，支持的类型有：
flux：流量，单位为 byte
fluxIn：上行流量，单位为 byte，该指标仅ecdn支持查询
fluxOut：下行流量，单位为 byte，该指标仅ecdn支持查询
bandwidth：带宽，单位为 bps
bandwidthIn：上行带宽，单位为 bps，该指标仅ecdn支持查询
bandwidthOut：下行带宽，单位为 bps，该指标仅ecdn支持查询
request：请求数，单位为 次
hitRequest：命中请求数，单位为 次
requestHitRate：请求命中率，单位为 %，保留小数点后两位
hitFlux：命中流量，单位为byte
fluxHitRate：流量命中率，单位为 %，保留小数点后两位
statusCode：状态码，返回 2xx、3xx、4xx、5xx 汇总数据，单位为 个
2xx：返回 2xx 状态码汇总及各 2 开头状态码数据，单位为 个
3xx：返回 3xx 状态码汇总及各 3 开头状态码数据，单位为 个
4xx：返回 4xx 状态码汇总及各 4 开头状态码数据，单位为 个
5xx：返回 5xx 状态码汇总及各 5 开头状态码数据，单位为 个
支持指定具体状态码查询，若未产生过，则返回为空
        :type Metric: str
        :param _Domains: 指定查询域名列表
查询单域名：指定单个域名
查询多个域名：指定多个域名，最多可一次性查询 30 个
查询账号下所有域名：不传参，默认查询账号维度
        :type Domains: list of str
        :param _Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param _Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :type Interval: str
        :param _Detail: 多域名查询时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode、2xx、3xx、4xx、5xx 指标暂不支持）
        :type Detail: bool
        :param _Isp: 查询中国境内CDN数据时，指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定运营商查询时，不可同时指定省份、IP协议查询
        :type Isp: int
        :param _District: 查询中国境内CDN数据时，指定省份查询，不填充表示查询所有省份
查询中国境外CDN数据时，指定国家/地区查询，不填充表示查询所有国家/地区
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定（中国境内）省份查询时，不可同时指定运营商、IP协议查询
        :type District: int
        :param _Protocol: 指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标
        :type Protocol: str
        :param _DataSource: 指定数据源查询，白名单功能
        :type DataSource: str
        :param _IpProtocol: 指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
注意：非IPv6白名单用户不可指定ipv4、ipv6进行查询
        :type IpProtocol: str
        :param _Area: 指定服务地域查询，不填充表示查询中国境内CDN数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :type Area: str
        :param _AreaType: 查询中国境外CDN数据时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据
        :type AreaType: str
        :param _Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :type Product: str
        :param _TimeZone: 指定查询时间的时区，默认UTC+08:00
        :type TimeZone: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Domains = None
        self._Project = None
        self._Interval = None
        self._Detail = None
        self._Isp = None
        self._District = None
        self._Protocol = None
        self._DataSource = None
        self._IpProtocol = None
        self._Area = None
        self._AreaType = None
        self._Product = None
        self._TimeZone = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """指定查询指标，支持的类型有：
flux：流量，单位为 byte
fluxIn：上行流量，单位为 byte，该指标仅ecdn支持查询
fluxOut：下行流量，单位为 byte，该指标仅ecdn支持查询
bandwidth：带宽，单位为 bps
bandwidthIn：上行带宽，单位为 bps，该指标仅ecdn支持查询
bandwidthOut：下行带宽，单位为 bps，该指标仅ecdn支持查询
request：请求数，单位为 次
hitRequest：命中请求数，单位为 次
requestHitRate：请求命中率，单位为 %，保留小数点后两位
hitFlux：命中流量，单位为byte
fluxHitRate：流量命中率，单位为 %，保留小数点后两位
statusCode：状态码，返回 2xx、3xx、4xx、5xx 汇总数据，单位为 个
2xx：返回 2xx 状态码汇总及各 2 开头状态码数据，单位为 个
3xx：返回 3xx 状态码汇总及各 3 开头状态码数据，单位为 个
4xx：返回 4xx 状态码汇总及各 4 开头状态码数据，单位为 个
5xx：返回 5xx 状态码汇总及各 5 开头状态码数据，单位为 个
支持指定具体状态码查询，若未产生过，则返回为空
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Domains(self):
        """指定查询域名列表
查询单域名：指定单个域名
查询多个域名：指定多个域名，最多可一次性查询 30 个
查询账号下所有域名：不传参，默认查询账号维度
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        """指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Detail(self):
        """多域名查询时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode、2xx、3xx、4xx、5xx 指标暂不支持）
        :rtype: bool
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Isp(self):
        """查询中国境内CDN数据时，指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定运营商查询时，不可同时指定省份、IP协议查询
        :rtype: int
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def District(self):
        """查询中国境内CDN数据时，指定省份查询，不填充表示查询所有省份
查询中国境外CDN数据时，指定国家/地区查询，不填充表示查询所有国家/地区
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定（中国境内）省份查询时，不可同时指定运营商、IP协议查询
        :rtype: int
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Protocol(self):
        """指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def DataSource(self):
        """指定数据源查询，白名单功能
        :rtype: str
        """
        return self._DataSource

    @DataSource.setter
    def DataSource(self, DataSource):
        self._DataSource = DataSource

    @property
    def IpProtocol(self):
        """指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
注意：非IPv6白名单用户不可指定ipv4、ipv6进行查询
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Area(self):
        """指定服务地域查询，不填充表示查询中国境内CDN数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AreaType(self):
        """查询中国境外CDN数据时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据
        :rtype: str
        """
        return self._AreaType

    @AreaType.setter
    def AreaType(self, AreaType):
        self._AreaType = AreaType

    @property
    def Product(self):
        """指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def TimeZone(self):
        """指定查询时间的时区，默认UTC+08:00
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Interval = params.get("Interval")
        self._Detail = params.get("Detail")
        self._Isp = params.get("Isp")
        self._District = params.get("District")
        self._Protocol = params.get("Protocol")
        self._DataSource = params.get("DataSource")
        self._IpProtocol = params.get("IpProtocol")
        self._Area = params.get("Area")
        self._AreaType = params.get("AreaType")
        self._Product = params.get("Product")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 返回数据的时间粒度，查询时指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :type Interval: str
        :param _Data: 指定条件查询得到的数据明细
        :type Data: list of ResourceData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        """返回数据的时间粒度，查询时指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        """指定条件查询得到的数据明细
        :rtype: list of ResourceData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 指定域名查询
        :type Domain: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为 100，最大为 1000
        :type Limit: int
        :param _Area: 指定区域下载日志，默认为 mainland，可取值有：
<li>mainland：获取境内加速日志包下载链接</li>
<li>overseas：获取境外加速日志包下载链接</li>
<li>global：同时获取境内、境外加速日志包下载链接（分开打包）</li>
        :type Area: str
        :param _LogType: 指定下载日志的类型，可取值有：
<li>access：访问日志</li>
        :type LogType: str
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._LogType = None

    @property
    def Domain(self):
        """指定域名查询
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为 100，最大为 1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        """指定区域下载日志，默认为 mainland，可取值有：
<li>mainland：获取境内加速日志包下载链接</li>
<li>overseas：获取境外加速日志包下载链接</li>
<li>global：同时获取境内、境外加速日志包下载链接（分开打包）</li>
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogType(self):
        """指定下载日志的类型，可取值有：
<li>access：访问日志</li>
        :rtype: str
        """
        return self._LogType

    @LogType.setter
    def LogType(self, LogType):
        self._LogType = LogType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        self._LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainLogs: 日志包下载链接。
下载内容是gz后缀的压缩包，解压后是无扩展名的文本文件。链接有效期1天。
        :type DomainLogs: list of DomainLog
        :param _TotalCount: 查询到的总条数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainLogs(self):
        """日志包下载链接。
下载内容是gz后缀的压缩包，解压后是无扩展名的文本文件。链接有效期1天。
        :rtype: list of DomainLog
        """
        return self._DomainLogs

    @DomainLogs.setter
    def DomainLogs(self, DomainLogs):
        self._DomainLogs = DomainLogs

    @property
    def TotalCount(self):
        """查询到的总条数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainLogs") is not None:
            self._DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLog()
                obj._deserialize(item)
                self._DomainLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Ips: 需要查询的 IP 列表，单次可支持1-20个IP查询。
        :type Ips: list of str
        """
        self._Ips = None

    @property
    def Ips(self):
        """需要查询的 IP 列表，单次可支持1-20个IP查询。
        :rtype: list of str
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips


    def _deserialize(self, params):
        self._Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ips: 查询的节点归属详情。
        :type Ips: list of CdnIp
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ips = None
        self._RequestId = None

    @property
    def Ips(self):
        """查询的节点归属详情。
        :rtype: list of CdnIp
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = CdnIp()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeCdnOriginIpRequest(AbstractModel):
    """DescribeCdnOriginIp请求参数结构体

    """


class DescribeCdnOriginIpResponse(AbstractModel):
    """DescribeCdnOriginIp返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ips: 回源节点IP详情。
        :type Ips: list of OriginIp
        :param _TotalCount: 回源节点IP总个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ips = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Ips(self):
        """回源节点IP详情。
        :rtype: list of OriginIp
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def TotalCount(self):
        """回源节点IP总个数。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = OriginIp()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeCertDomainsRequest(AbstractModel):
    """DescribeCertDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Cert: PEM格式证书Base64编码后的字符串
        :type Cert: str
        :param _CertId: 托管证书ID，Cert和CertId不能均未空，都填写时以CerId为准。
        :type CertId: str
        :param _Product: 域名所属产品，cdn或ecdn，默认cdn。
        :type Product: str
        """
        self._Cert = None
        self._CertId = None
        self._Product = None

    @property
    def Cert(self):
        """PEM格式证书Base64编码后的字符串
        :rtype: str
        """
        return self._Cert

    @Cert.setter
    def Cert(self, Cert):
        self._Cert = Cert

    @property
    def CertId(self):
        """托管证书ID，Cert和CertId不能均未空，都填写时以CerId为准。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def Product(self):
        """域名所属产品，cdn或ecdn，默认cdn。
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._Cert = params.get("Cert")
        self._CertId = params.get("CertId")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertDomainsResponse(AbstractModel):
    """DescribeCertDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 已接入CDN的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param _CertifiedDomains: 已配置证书的CDN域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CertifiedDomains: list of str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._CertifiedDomains = None
        self._RequestId = None

    @property
    def Domains(self):
        """已接入CDN的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def CertifiedDomains(self):
        """已配置证书的CDN域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._CertifiedDomains

    @CertifiedDomains.setter
    def CertifiedDomains(self, CertifiedDomains):
        self._CertifiedDomains = CertifiedDomains

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._CertifiedDomains = params.get("CertifiedDomains")
        self._RequestId = params.get("RequestId")


class DescribeDDoSDataRequest(AbstractModel):
    """DescribeDDoSData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param _Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Interval = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDDoSDataResponse(AbstractModel):
    """DescribeDDoSData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: DDoS统计数据数组
        :type Data: list of DDoSStatsData
        :param _Interval: 时间粒度：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :type Interval: str
        :param _AttackBandwidthData: DDoS统计攻击带宽峰值数组
        :type AttackBandwidthData: list of DDoSAttackBandwidthData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._AttackBandwidthData = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS统计数据数组
        :rtype: list of DDoSStatsData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        """时间粒度：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def AttackBandwidthData(self):
        """DDoS统计攻击带宽峰值数组
        :rtype: list of DDoSAttackBandwidthData
        """
        return self._AttackBandwidthData

    @AttackBandwidthData.setter
    def AttackBandwidthData(self, AttackBandwidthData):
        self._AttackBandwidthData = AttackBandwidthData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSStatsData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        if params.get("AttackBandwidthData") is not None:
            self._AttackBandwidthData = []
            for item in params.get("AttackBandwidthData"):
                obj = DDoSAttackBandwidthData()
                obj._deserialize(item)
                self._AttackBandwidthData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDiagnoseReportRequest(AbstractModel):
    """DescribeDiagnoseReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ReportId: 报告ID
        :type ReportId: str
        """
        self._ReportId = None

    @property
    def ReportId(self):
        """报告ID
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId


    def _deserialize(self, params):
        self._ReportId = params.get("ReportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagnoseReportResponse(AbstractModel):
    """DescribeDiagnoseReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _BaskInfo: 诊断报告基础信息
        :type BaskInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _CnameInfo: CNAME检测信息
        :type CnameInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _ClientInfo: 客户端检测信息
        :type ClientInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _DnsInfo: DNS检测信息
        :type DnsInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _NetworkInfo: 网络检测信息
        :type NetworkInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _OcNodeInfo: 边缘节点检测信息
        :type OcNodeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _MidNodeInfo: 中间源节点检测信息
        :type MidNodeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _OriginInfo: 源站检测信息
        :type OriginInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _PurgeInfo: 刷新检测信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PurgeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._BaskInfo = None
        self._CnameInfo = None
        self._ClientInfo = None
        self._DnsInfo = None
        self._NetworkInfo = None
        self._OcNodeInfo = None
        self._MidNodeInfo = None
        self._OriginInfo = None
        self._PurgeInfo = None
        self._RequestId = None

    @property
    def BaskInfo(self):
        """诊断报告基础信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._BaskInfo

    @BaskInfo.setter
    def BaskInfo(self, BaskInfo):
        self._BaskInfo = BaskInfo

    @property
    def CnameInfo(self):
        """CNAME检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._CnameInfo

    @CnameInfo.setter
    def CnameInfo(self, CnameInfo):
        self._CnameInfo = CnameInfo

    @property
    def ClientInfo(self):
        """客户端检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._ClientInfo

    @ClientInfo.setter
    def ClientInfo(self, ClientInfo):
        self._ClientInfo = ClientInfo

    @property
    def DnsInfo(self):
        """DNS检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._DnsInfo

    @DnsInfo.setter
    def DnsInfo(self, DnsInfo):
        self._DnsInfo = DnsInfo

    @property
    def NetworkInfo(self):
        """网络检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._NetworkInfo

    @NetworkInfo.setter
    def NetworkInfo(self, NetworkInfo):
        self._NetworkInfo = NetworkInfo

    @property
    def OcNodeInfo(self):
        """边缘节点检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._OcNodeInfo

    @OcNodeInfo.setter
    def OcNodeInfo(self, OcNodeInfo):
        self._OcNodeInfo = OcNodeInfo

    @property
    def MidNodeInfo(self):
        """中间源节点检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._MidNodeInfo

    @MidNodeInfo.setter
    def MidNodeInfo(self, MidNodeInfo):
        self._MidNodeInfo = MidNodeInfo

    @property
    def OriginInfo(self):
        """源站检测信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._OriginInfo

    @OriginInfo.setter
    def OriginInfo(self, OriginInfo):
        self._OriginInfo = OriginInfo

    @property
    def PurgeInfo(self):
        """刷新检测信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        """
        return self._PurgeInfo

    @PurgeInfo.setter
    def PurgeInfo(self, PurgeInfo):
        self._PurgeInfo = PurgeInfo

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("BaskInfo") is not None:
            self._BaskInfo = DiagnoseData()
            self._BaskInfo._deserialize(params.get("BaskInfo"))
        if params.get("CnameInfo") is not None:
            self._CnameInfo = DiagnoseData()
            self._CnameInfo._deserialize(params.get("CnameInfo"))
        if params.get("ClientInfo") is not None:
            self._ClientInfo = DiagnoseData()
            self._ClientInfo._deserialize(params.get("ClientInfo"))
        if params.get("DnsInfo") is not None:
            self._DnsInfo = DiagnoseData()
            self._DnsInfo._deserialize(params.get("DnsInfo"))
        if params.get("NetworkInfo") is not None:
            self._NetworkInfo = DiagnoseData()
            self._NetworkInfo._deserialize(params.get("NetworkInfo"))
        if params.get("OcNodeInfo") is not None:
            self._OcNodeInfo = DiagnoseData()
            self._OcNodeInfo._deserialize(params.get("OcNodeInfo"))
        if params.get("MidNodeInfo") is not None:
            self._MidNodeInfo = DiagnoseData()
            self._MidNodeInfo._deserialize(params.get("MidNodeInfo"))
        if params.get("OriginInfo") is not None:
            self._OriginInfo = DiagnoseData()
            self._OriginInfo._deserialize(params.get("OriginInfo"))
        if params.get("PurgeInfo") is not None:
            self._PurgeInfo = DiagnoseData()
            self._PurgeInfo._deserialize(params.get("PurgeInfo"))
        self._RequestId = params.get("RequestId")


class DescribeDistrictIspDataRequest(AbstractModel):
    """DescribeDistrictIspData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 域名列表，最多支持20个域名
        :type Domains: list of str
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
支持近 60 天内的数据查询，每次查询时间区间为 3 小时
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
结束时间与起始时间区间最大为 3 小时
        :type EndTime: str
        :param _Metric: 指定查询指标，支持:
bandwidth：带宽，单位为 bps
flux：流量，单位为 byte
request：请求数，单位为 次
statusCode：状态码，返回 0、2xx、3xx、4xx、5xx 汇总数据，单位为 次
2xx：返回 2xx 状态码汇总及各 2 开头状态码数据，单位为 次
3xx：返回 3xx 状态码汇总及各 3 开头状态码数据，单位为 次
4xx：返回 4xx 状态码汇总及各 4 开头状态码数据，单位为 次
5xx：返回 5xx 状态码汇总及各 5 开头状态码数据，单位为 次
支持指定具体状态码查询，若未产生过，则返回为空
        :type Metric: str
        :param _Districts: 指定省份查询，不填充表示查询所有省份
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
        :type Districts: list of int
        :param _Isps: 指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
        :type Isps: list of int
        :param _Protocol: 指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标
        :type Protocol: str
        :param _IpProtocol: 指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
        :type IpProtocol: str
        :param _Interval: 时间粒度，支持以下几种模式（默认5min）：
min：1 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过10分钟，可返回 1 分钟粒度明细数据
5min：5 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过3 小时，可返回 5 分钟粒度明细数据
        :type Interval: str
        """
        self._Domains = None
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Districts = None
        self._Isps = None
        self._Protocol = None
        self._IpProtocol = None
        self._Interval = None

    @property
    def Domains(self):
        """域名列表，最多支持20个域名
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
支持近 60 天内的数据查询，每次查询时间区间为 3 小时
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
结束时间与起始时间区间最大为 3 小时
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """指定查询指标，支持:
bandwidth：带宽，单位为 bps
flux：流量，单位为 byte
request：请求数，单位为 次
statusCode：状态码，返回 0、2xx、3xx、4xx、5xx 汇总数据，单位为 次
2xx：返回 2xx 状态码汇总及各 2 开头状态码数据，单位为 次
3xx：返回 3xx 状态码汇总及各 3 开头状态码数据，单位为 次
4xx：返回 4xx 状态码汇总及各 4 开头状态码数据，单位为 次
5xx：返回 5xx 状态码汇总及各 5 开头状态码数据，单位为 次
支持指定具体状态码查询，若未产生过，则返回为空
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Districts(self):
        """指定省份查询，不填充表示查询所有省份
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
        :rtype: list of int
        """
        return self._Districts

    @Districts.setter
    def Districts(self, Districts):
        self._Districts = Districts

    @property
    def Isps(self):
        """指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
        :rtype: list of int
        """
        return self._Isps

    @Isps.setter
    def Isps(self, Isps):
        self._Isps = Isps

    @property
    def Protocol(self):
        """指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IpProtocol(self):
        """指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式（默认5min）：
min：1 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过10分钟，可返回 1 分钟粒度明细数据
5min：5 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过3 小时，可返回 5 分钟粒度明细数据
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._Domains = params.get("Domains")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Districts = params.get("Districts")
        self._Isps = params.get("Isps")
        self._Protocol = params.get("Protocol")
        self._IpProtocol = params.get("IpProtocol")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDistrictIspDataResponse(AbstractModel):
    """DescribeDistrictIspData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 地区运营商数据明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DistrictIspInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """地区运营商数据明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DistrictIspInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DistrictIspInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param _Filters: 查询条件过滤器，复杂类型
        :type Filters: list of DomainFilter
        :param _Sort: 排序规则
        :type Sort: :class:`tencentcloud.cdn.v20180606.models.Sort`
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sort = None

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为 100，最大可设置为 1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """查询条件过滤器，复杂类型
        :rtype: list of DomainFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        """排序规则
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Sort`
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 域名列表
        :type Domains: list of DetailDomain
        :param _TotalNumber: 符合查询条件的域名总数
用于分页查询
        :type TotalNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def Domains(self):
        """域名列表
        :rtype: list of DetailDomain
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalNumber(self):
        """符合查询条件的域名总数
用于分页查询
        :rtype: int
        """
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DetailDomain()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param _Filters: 查询条件过滤器，复杂类型
        :type Filters: list of DomainFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为 100，最大可设置为 1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """查询条件过滤器，复杂类型
        :rtype: list of DomainFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = DomainFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Domains: 域名列表
        :type Domains: list of BriefDomain
        :param _TotalNumber: 符合查询条件的域名总数
用于分页查询
        :type TotalNumber: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._TotalNumber = None
        self._RequestId = None

    @property
    def Domains(self):
        """域名列表
        :rtype: list of BriefDomain
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def TotalNumber(self):
        """符合查询条件的域名总数
用于分页查询
        :rtype: int
        """
        return self._TotalNumber

    @TotalNumber.setter
    def TotalNumber(self, TotalNumber):
        self._TotalNumber = TotalNumber

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = BriefDomain()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalNumber = params.get("TotalNumber")
        self._RequestId = params.get("RequestId")


class DescribeEdgePackTaskStatusRequest(AbstractModel):
    """DescribeEdgePackTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Filters: 查询条件过滤器
        :type Filters: list of EdgePackTaskFilter
        """
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Offset = None
        self._Filters = None

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """分页查询限制数目，默认为 100，最大可设置为 1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Filters(self):
        """查询条件过滤器
        :rtype: list of EdgePackTaskFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Offset = params.get("Offset")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = EdgePackTaskFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEdgePackTaskStatusResponse(AbstractModel):
    """DescribeEdgePackTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _EdgePackTaskStatusSet: 动态打包任务状态列表
        :type EdgePackTaskStatusSet: list of EdgePackTaskStatus
        :param _TotalCount: 总数，用于分页查询
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._EdgePackTaskStatusSet = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def EdgePackTaskStatusSet(self):
        """动态打包任务状态列表
        :rtype: list of EdgePackTaskStatus
        """
        return self._EdgePackTaskStatusSet

    @EdgePackTaskStatusSet.setter
    def EdgePackTaskStatusSet(self, EdgePackTaskStatusSet):
        self._EdgePackTaskStatusSet = EdgePackTaskStatusSet

    @property
    def TotalCount(self):
        """总数，用于分页查询
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("EdgePackTaskStatusSet") is not None:
            self._EdgePackTaskStatusSet = []
            for item in params.get("EdgePackTaskStatusSet"):
                obj = EdgePackTaskStatus()
                obj._deserialize(item)
                self._EdgePackTaskStatusSet.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEventLogDataRequest(AbstractModel):
    """DescribeEventLogData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Mode: 防护类型，映射如下：
  waf = "Web攻击"
  cc = "CC攻击"
        :type Mode: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间，最长跨度为30分钟
        :type EndTime: str
        :param _Domain: 域名
        :type Domain: str
        :param _ActionName: 执行动作，取值为：intercept/redirect/observe
分别表示：拦截/重定向/观察
参数放空，表示查询全部动作数据
        :type ActionName: str
        :param _Url: 请求URL，支持URL开头和结尾使用\*表示通配
如：
/files/* 表示所有以/files/开头的请求
*.jpg 表示所有以.jpg结尾的请求
        :type Url: str
        :param _Area: 地域 mainland 或者 overseas，为空时默认 mainland
        :type Area: str
        :param _Source: 来源产品，cdn 或者 ecdn，为空时默认 cdn
        :type Source: str
        """
        self._Mode = None
        self._StartTime = None
        self._EndTime = None
        self._Domain = None
        self._ActionName = None
        self._Url = None
        self._Area = None
        self._Source = None

    @property
    def Mode(self):
        """防护类型，映射如下：
  waf = "Web攻击"
  cc = "CC攻击"
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，最长跨度为30分钟
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ActionName(self):
        """执行动作，取值为：intercept/redirect/observe
分别表示：拦截/重定向/观察
参数放空，表示查询全部动作数据
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Url(self):
        """请求URL，支持URL开头和结尾使用\*表示通配
如：
/files/* 表示所有以/files/开头的请求
*.jpg 表示所有以.jpg结尾的请求
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Area(self):
        """地域 mainland 或者 overseas，为空时默认 mainland
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Source(self):
        """来源产品，cdn 或者 ecdn，为空时默认 cdn
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source


    def _deserialize(self, params):
        self._Mode = params.get("Mode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domain = params.get("Domain")
        self._ActionName = params.get("ActionName")
        self._Url = params.get("Url")
        self._Area = params.get("Area")
        self._Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEventLogDataResponse(AbstractModel):
    """DescribeEventLogData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Results: 统计曲线结果
        :type Results: list of EventLogStatsData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Results = None
        self._RequestId = None

    @property
    def Results(self):
        """统计曲线结果
        :rtype: list of EventLogStatsData
        """
        return self._Results

    @Results.setter
    def Results(self, Results):
        self._Results = Results

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Results") is not None:
            self._Results = []
            for item in params.get("Results"):
                obj = EventLogStatsData()
                obj._deserialize(item)
                self._Results.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeHttpsPackagesRequest(AbstractModel):
    """DescribeHttpsPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询起始地址，默认 0
        :type Offset: int
        :param _Limit: 分页查询记录个数，默认100，最大1000
        :type Limit: int
        """
        self._Offset = None
        self._Limit = None

    @property
    def Offset(self):
        """分页查询起始地址，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询记录个数，默认100，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHttpsPackagesResponse(AbstractModel):
    """DescribeHttpsPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: HTTPS请求包总个数
        :type TotalCount: int
        :param _HttpsPackages: HTTPS请求包详情
        :type HttpsPackages: list of HttpsPackage
        :param _ExpiringCount: 即将过期的HTTPS请求包个数（7天内）
        :type ExpiringCount: int
        :param _EnabledCount: 有效HTTPS请求包个数
        :type EnabledCount: int
        :param _PaidCount: 付费HTTPS请求包个数
        :type PaidCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._HttpsPackages = None
        self._ExpiringCount = None
        self._EnabledCount = None
        self._PaidCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """HTTPS请求包总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def HttpsPackages(self):
        """HTTPS请求包详情
        :rtype: list of HttpsPackage
        """
        return self._HttpsPackages

    @HttpsPackages.setter
    def HttpsPackages(self, HttpsPackages):
        self._HttpsPackages = HttpsPackages

    @property
    def ExpiringCount(self):
        """即将过期的HTTPS请求包个数（7天内）
        :rtype: int
        """
        return self._ExpiringCount

    @ExpiringCount.setter
    def ExpiringCount(self, ExpiringCount):
        self._ExpiringCount = ExpiringCount

    @property
    def EnabledCount(self):
        """有效HTTPS请求包个数
        :rtype: int
        """
        return self._EnabledCount

    @EnabledCount.setter
    def EnabledCount(self, EnabledCount):
        self._EnabledCount = EnabledCount

    @property
    def PaidCount(self):
        """付费HTTPS请求包个数
        :rtype: int
        """
        return self._PaidCount

    @PaidCount.setter
    def PaidCount(self, PaidCount):
        self._PaidCount = PaidCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("HttpsPackages") is not None:
            self._HttpsPackages = []
            for item in params.get("HttpsPackages"):
                obj = HttpsPackage()
                obj._deserialize(item)
                self._HttpsPackages.append(obj)
        self._ExpiringCount = params.get("ExpiringCount")
        self._EnabledCount = params.get("EnabledCount")
        self._PaidCount = params.get("PaidCount")
        self._RequestId = params.get("RequestId")


class DescribeImageConfigRequest(AbstractModel):
    """DescribeImageConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeImageConfigResponse(AbstractModel):
    """DescribeImageConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _WebpAdapter: WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param _TpgAdapter: TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param _GuetzliAdapter: GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        :param _AvifAdapter: AvifAdapter配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type AvifAdapter: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._WebpAdapter = None
        self._TpgAdapter = None
        self._GuetzliAdapter = None
        self._AvifAdapter = None
        self._RequestId = None

    @property
    def WebpAdapter(self):
        """WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        """
        return self._WebpAdapter

    @WebpAdapter.setter
    def WebpAdapter(self, WebpAdapter):
        self._WebpAdapter = WebpAdapter

    @property
    def TpgAdapter(self):
        """TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        """
        return self._TpgAdapter

    @TpgAdapter.setter
    def TpgAdapter(self, TpgAdapter):
        self._TpgAdapter = TpgAdapter

    @property
    def GuetzliAdapter(self):
        """GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        return self._GuetzliAdapter

    @GuetzliAdapter.setter
    def GuetzliAdapter(self, GuetzliAdapter):
        self._GuetzliAdapter = GuetzliAdapter

    @property
    def AvifAdapter(self):
        """AvifAdapter配置项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        """
        return self._AvifAdapter

    @AvifAdapter.setter
    def AvifAdapter(self, AvifAdapter):
        self._AvifAdapter = AvifAdapter

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self._WebpAdapter = WebpAdapter()
            self._WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self._TpgAdapter = TpgAdapter()
            self._TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self._GuetzliAdapter = GuetzliAdapter()
            self._GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        if params.get("AvifAdapter") is not None:
            self._AvifAdapter = AvifAdapter()
            self._AvifAdapter._deserialize(params.get("AvifAdapter"))
        self._RequestId = params.get("RequestId")


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 加速域名
        :type Domain: str
        :param _Layer: 节点类型：
edge：表示边缘节点
last：表示回源层节点
不填充情况下，默认返回边缘节点信息
        :type Layer: str
        :param _Area: 查询区域：
mainland: 国内节点
overseas: 海外节点
global: 全球节点
        :type Area: str
        :param _Segment: 是否以IP段的格式返回。
        :type Segment: bool
        :param _ShowIpv6: 是否查询节点 IPV6 信息。
        :type ShowIpv6: bool
        :param _AbbreviationIpv6: 是否对IPV6进行缩写。
        :type AbbreviationIpv6: bool
        """
        self._Domain = None
        self._Layer = None
        self._Area = None
        self._Segment = None
        self._ShowIpv6 = None
        self._AbbreviationIpv6 = None

    @property
    def Domain(self):
        """加速域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Layer(self):
        """节点类型：
edge：表示边缘节点
last：表示回源层节点
不填充情况下，默认返回边缘节点信息
        :rtype: str
        """
        return self._Layer

    @Layer.setter
    def Layer(self, Layer):
        self._Layer = Layer

    @property
    def Area(self):
        """查询区域：
mainland: 国内节点
overseas: 海外节点
global: 全球节点
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Segment(self):
        """是否以IP段的格式返回。
        :rtype: bool
        """
        return self._Segment

    @Segment.setter
    def Segment(self, Segment):
        self._Segment = Segment

    @property
    def ShowIpv6(self):
        """是否查询节点 IPV6 信息。
        :rtype: bool
        """
        return self._ShowIpv6

    @ShowIpv6.setter
    def ShowIpv6(self, ShowIpv6):
        self._ShowIpv6 = ShowIpv6

    @property
    def AbbreviationIpv6(self):
        """是否对IPV6进行缩写。
        :rtype: bool
        """
        return self._AbbreviationIpv6

    @AbbreviationIpv6.setter
    def AbbreviationIpv6(self, AbbreviationIpv6):
        self._AbbreviationIpv6 = AbbreviationIpv6


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Layer = params.get("Layer")
        self._Area = params.get("Area")
        self._Segment = params.get("Segment")
        self._ShowIpv6 = params.get("ShowIpv6")
        self._AbbreviationIpv6 = params.get("AbbreviationIpv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Ips: 节点列表
        :type Ips: list of IpStatus
        :param _TotalCount: 节点总个数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Ips = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Ips(self):
        """节点列表
        :rtype: list of IpStatus
        """
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

    @property
    def TotalCount(self):
        """节点总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = IpStatus()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:10，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:40:00
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:10，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:40:00
        :type EndTime: str
        :param _Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param _Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param _Interval: 时间粒度，支持以下几种模式：
5min：5 分钟粒度，查询时间区间 24 小时内，默认返回 5 分钟粒度活跃用户数
day：天粒度，查询时间区间大于 1 天时，默认返回天粒度活跃用户数
        :type Interval: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Domains = None
        self._Project = None
        self._Interval = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:10，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:40:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:10，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:40:00
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domains(self):
        """指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        """指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式：
5min：5 分钟粒度，查询时间区间 24 小时内，默认返回 5 分钟粒度活跃用户数
day：天粒度，查询时间区间大于 1 天时，默认返回天粒度活跃用户数
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 数据统计的时间粒度，支持5min,  day，分别表示5分钟，1天的时间粒度。
        :type Interval: str
        :param _Data: 各个资源的回源数据详情。
        :type Data: list of ResourceData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        """数据统计的时间粒度，支持5min,  day，分别表示5分钟，1天的时间粒度。
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        """各个资源的回源数据详情。
        :rtype: list of ResourceData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Name: 映射查询类别：
isp：运营商映射查询
district：省份（中国境内）、国家/地区（中国境外）映射查询
        :type Name: str
        """
        self._Name = None

    @property
    def Name(self):
        """映射查询类别：
isp：运营商映射查询
district：省份（中国境内）、国家/地区（中国境外）映射查询
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param _MapInfoList: 映射关系数组。
        :type MapInfoList: list of MapInfo
        :param _ServerRegionRelation: 服务端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerRegionRelation: list of RegionMapRelation
        :param _ClientRegionRelation: 客户端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientRegionRelation: list of RegionMapRelation
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._MapInfoList = None
        self._ServerRegionRelation = None
        self._ClientRegionRelation = None
        self._RequestId = None

    @property
    def MapInfoList(self):
        """映射关系数组。
        :rtype: list of MapInfo
        """
        return self._MapInfoList

    @MapInfoList.setter
    def MapInfoList(self, MapInfoList):
        self._MapInfoList = MapInfoList

    @property
    def ServerRegionRelation(self):
        """服务端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RegionMapRelation
        """
        return self._ServerRegionRelation

    @ServerRegionRelation.setter
    def ServerRegionRelation(self, ServerRegionRelation):
        self._ServerRegionRelation = ServerRegionRelation

    @property
    def ClientRegionRelation(self):
        """客户端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RegionMapRelation
        """
        return self._ClientRegionRelation

    @ClientRegionRelation.setter
    def ClientRegionRelation(self, ClientRegionRelation):
        self._ClientRegionRelation = ClientRegionRelation

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self._MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self._MapInfoList.append(obj)
        if params.get("ServerRegionRelation") is not None:
            self._ServerRegionRelation = []
            for item in params.get("ServerRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self._ServerRegionRelation.append(obj)
        if params.get("ClientRegionRelation") is not None:
            self._ClientRegionRelation = []
            for item in params.get("ClientRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self._ClientRegionRelation.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type EndTime: str
        :param _Metric: 指定查询指标，支持的类型有：
flux：回源流量，单位为 byte
bandwidth：回源带宽，单位为 bps
request：回源请求数，单位为 次
failRequest：回源失败请求数，单位为 次
failRate：回源失败率，单位为 %
statusCode：回源状态码，返回 2xx、3xx、4xx、5xx 汇总数据，单位为 个
2xx：返回 2xx 回源状态码汇总及各 2 开头回源状态码数据，单位为 个
3xx：返回 3xx 回源状态码汇总及各 3 开头回源状态码数据，单位为 个
4xx：返回 4xx 回源状态码汇总及各 4 开头回源状态码数据，单位为 个
5xx：返回 5xx 回源状态码汇总及各 5 开头回源状态码数据，单位为 个
支持指定具体状态码查询，若未产生过，则返回为空
        :type Metric: str
        :param _Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param _Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，最多可一次性查询 30 个加速域名明细
若填充了具体域名信息，以域名为主
        :type Project: int
        :param _Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :type Interval: str
        :param _Detail: Domains 传入多个时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode、2xx、3xx、4xx、5xx 指标暂不支持）
        :type Detail: bool
        :param _Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :type Area: str
        :param _TimeZone: 指定查询时间的时区，默认UTC+08:00
        :type TimeZone: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Domains = None
        self._Project = None
        self._Interval = None
        self._Detail = None
        self._Area = None
        self._TimeZone = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """指定查询指标，支持的类型有：
flux：回源流量，单位为 byte
bandwidth：回源带宽，单位为 bps
request：回源请求数，单位为 次
failRequest：回源失败请求数，单位为 次
failRate：回源失败率，单位为 %
statusCode：回源状态码，返回 2xx、3xx、4xx、5xx 汇总数据，单位为 个
2xx：返回 2xx 回源状态码汇总及各 2 开头回源状态码数据，单位为 个
3xx：返回 3xx 回源状态码汇总及各 3 开头回源状态码数据，单位为 个
4xx：返回 4xx 回源状态码汇总及各 4 开头回源状态码数据，单位为 个
5xx：返回 5xx 回源状态码汇总及各 5 开头回源状态码数据，单位为 个
支持指定具体状态码查询，若未产生过，则返回为空
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Domains(self):
        """指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        """指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，最多可一次性查询 30 个加速域名明细
若填充了具体域名信息，以域名为主
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Detail(self):
        """Domains 传入多个时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode、2xx、3xx、4xx、5xx 指标暂不支持）
        :rtype: bool
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Area(self):
        """指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def TimeZone(self):
        """指定查询时间的时区，默认UTC+08:00
        :rtype: str
        """
        return self._TimeZone

    @TimeZone.setter
    def TimeZone(self, TimeZone):
        self._TimeZone = TimeZone


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Interval = params.get("Interval")
        self._Detail = params.get("Detail")
        self._Area = params.get("Area")
        self._TimeZone = params.get("TimeZone")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Interval: 数据统计的时间粒度，支持min, 5min, hour, day，分别表示1分钟，5分钟，1小时和1天的时间粒度。
        :type Interval: str
        :param _Data: 各个资源的回源数据详情。
        :type Data: list of ResourceOriginData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Interval = None
        self._Data = None
        self._RequestId = None

    @property
    def Interval(self):
        """数据统计的时间粒度，支持min, 5min, hour, day，分别表示1分钟，5分钟，1小时和1天的时间粒度。
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Data(self):
        """各个资源的回源数据详情。
        :rtype: list of ResourceOriginData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Interval = params.get("Interval")
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceOriginData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Area: 指定服务地域查询
mainland：境内计费方式查询
overseas：境外计费方式查询
global：全球计费方式查询
未填充时，默认为 mainland
        :type Area: str
        :param _Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :type Product: str
        :param _Type: 指定资源包查询
flux：流量包
https：HTTPS请求包
未填充时，默认为 flux
        :type Type: str
        """
        self._Area = None
        self._Product = None
        self._Type = None

    @property
    def Area(self):
        """指定服务地域查询
mainland：境内计费方式查询
overseas：境外计费方式查询
global：全球计费方式查询
未填充时，默认为 mainland
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Product(self):
        """指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Type(self):
        """指定资源包查询
flux：流量包
https：HTTPS请求包
未填充时，默认为 flux
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type


    def _deserialize(self, params):
        self._Area = params.get("Area")
        self._Product = params.get("Product")
        self._Type = params.get("Type")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PayType: 计费类型
flux：流量计费
bandwidth：带宽计费
request：请求数计费
flux_sep：动静分离流量计费
bandwidth_sep：动静分离带宽计费
日结计费方式切换时，若当日产生消耗，则此字段表示第二天即将生效的计费方式，若未产生消耗，则表示已经生效的计费方式。
        :type PayType: str
        :param _BillingCycle: 计费周期
day：日结计费
month：月结计费
hour：小时结计费
        :type BillingCycle: str
        :param _StatType: 统计类型
monthMax：日峰值月平均，月结模式
day95：日 95 带宽，月结模式
month95：月95带宽，月结模式
sum：总流量/总请求数，日结或月结模式
max：峰值带宽，日结模式
        :type StatType: str
        :param _RegionType: 计费区域
all：全地区统一计费
multiple：分地区计费
        :type RegionType: str
        :param _CurrentPayType: 当前生效计费类型
flux：流量计费
bandwidth：带宽计费
request：请求数计费
flux_sep：动静分离流量计费
bandwidth_sep：动静分离带宽计费
        :type CurrentPayType: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PayType = None
        self._BillingCycle = None
        self._StatType = None
        self._RegionType = None
        self._CurrentPayType = None
        self._RequestId = None

    @property
    def PayType(self):
        """计费类型
flux：流量计费
bandwidth：带宽计费
request：请求数计费
flux_sep：动静分离流量计费
bandwidth_sep：动静分离带宽计费
日结计费方式切换时，若当日产生消耗，则此字段表示第二天即将生效的计费方式，若未产生消耗，则表示已经生效的计费方式。
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType

    @property
    def BillingCycle(self):
        """计费周期
day：日结计费
month：月结计费
hour：小时结计费
        :rtype: str
        """
        return self._BillingCycle

    @BillingCycle.setter
    def BillingCycle(self, BillingCycle):
        self._BillingCycle = BillingCycle

    @property
    def StatType(self):
        """统计类型
monthMax：日峰值月平均，月结模式
day95：日 95 带宽，月结模式
month95：月95带宽，月结模式
sum：总流量/总请求数，日结或月结模式
max：峰值带宽，日结模式
        :rtype: str
        """
        return self._StatType

    @StatType.setter
    def StatType(self, StatType):
        self._StatType = StatType

    @property
    def RegionType(self):
        """计费区域
all：全地区统一计费
multiple：分地区计费
        :rtype: str
        """
        return self._RegionType

    @RegionType.setter
    def RegionType(self, RegionType):
        self._RegionType = RegionType

    @property
    def CurrentPayType(self):
        """当前生效计费类型
flux：流量计费
bandwidth：带宽计费
request：请求数计费
flux_sep：动静分离流量计费
bandwidth_sep：动静分离带宽计费
        :rtype: str
        """
        return self._CurrentPayType

    @CurrentPayType.setter
    def CurrentPayType(self, CurrentPayType):
        self._CurrentPayType = CurrentPayType

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._PayType = params.get("PayType")
        self._BillingCycle = params.get("BillingCycle")
        self._StatType = params.get("StatType")
        self._RegionType = params.get("RegionType")
        self._CurrentPayType = params.get("CurrentPayType")
        self._RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota请求参数结构体

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UrlPurge: URL刷新用量及配额。
        :type UrlPurge: list of Quota
        :param _PathPurge: 目录刷新用量及配额。
        :type PathPurge: list of Quota
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UrlPurge = None
        self._PathPurge = None
        self._RequestId = None

    @property
    def UrlPurge(self):
        """URL刷新用量及配额。
        :rtype: list of Quota
        """
        return self._UrlPurge

    @UrlPurge.setter
    def UrlPurge(self, UrlPurge):
        self._UrlPurge = UrlPurge

    @property
    def PathPurge(self):
        """目录刷新用量及配额。
        :rtype: list of Quota
        """
        return self._PathPurge

    @PathPurge.setter
    def PathPurge(self, PathPurge):
        self._PathPurge = PathPurge

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self._UrlPurge = []
            for item in params.get("UrlPurge"):
                obj = Quota()
                obj._deserialize(item)
                self._UrlPurge.append(obj)
        if params.get("PathPurge") is not None:
            self._PathPurge = []
            for item in params.get("PathPurge"):
                obj = Quota()
                obj._deserialize(item)
                self._PathPurge.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PurgeType: 指定刷新类型查询
url：url 刷新记录
path：目录刷新记录
        :type PurgeType: str
        :param _StartTime: 根据时间区间查询时，填充开始时间，如 2018-08-08 00:00:00
        :type StartTime: str
        :param _EndTime: 根据时间区间查询时，填充结束时间，如 2018-08-08 23:59:59
        :type EndTime: str
        :param _TaskId: 根据任务 ID 查询时，填充任务 ID
查询时任务 ID 与起始时间必须填充一项
        :type TaskId: str
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为 20
        :type Limit: int
        :param _Keyword: 支持域名过滤，或 http(s):// 开头完整 URL 过滤
        :type Keyword: str
        :param _Status: 指定任务状态查询
fail：刷新失败
done：刷新成功
process：刷新中
        :type Status: str
        :param _Area: 指定刷新地域查询
mainland：境内
overseas：境外
global：全球
        :type Area: str
        """
        self._PurgeType = None
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Status = None
        self._Area = None

    @property
    def PurgeType(self):
        """指定刷新类型查询
url：url 刷新记录
path：目录刷新记录
        :rtype: str
        """
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def StartTime(self):
        """根据时间区间查询时，填充开始时间，如 2018-08-08 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """根据时间区间查询时，填充结束时间，如 2018-08-08 23:59:59
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskId(self):
        """根据任务 ID 查询时，填充任务 ID
查询时任务 ID 与起始时间必须填充一项
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Keyword(self):
        """支持域名过滤，或 http(s):// 开头完整 URL 过滤
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Status(self):
        """指定任务状态查询
fail：刷新失败
done：刷新成功
process：刷新中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Area(self):
        """指定刷新地域查询
mainland：境内
overseas：境外
global：全球
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._PurgeType = params.get("PurgeType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Status = params.get("Status")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PurgeLogs: 详细刷新记录
注意：此字段可能返回 null，表示取不到有效值。
        :type PurgeLogs: list of PurgeTask
        :param _TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PurgeLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PurgeLogs(self):
        """详细刷新记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PurgeTask
        """
        return self._PurgeLogs

    @PurgeLogs.setter
    def PurgeLogs(self, PurgeLogs):
        self._PurgeLogs = PurgeLogs

    @property
    def TotalCount(self):
        """任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PurgeLogs") is not None:
            self._PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self._PurgeLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePushQuotaRequest(AbstractModel):
    """DescribePushQuota请求参数结构体

    """


class DescribePushQuotaResponse(AbstractModel):
    """DescribePushQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UrlPush: Url预热用量及配额。
        :type UrlPush: list of Quota
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UrlPush = None
        self._RequestId = None

    @property
    def UrlPush(self):
        """Url预热用量及配额。
        :rtype: list of Quota
        """
        return self._UrlPush

    @UrlPush.setter
    def UrlPush(self, UrlPush):
        self._UrlPush = UrlPush

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlPush") is not None:
            self._UrlPush = []
            for item in params.get("UrlPush"):
                obj = Quota()
                obj._deserialize(item)
                self._UrlPush.append(obj)
        self._RequestId = params.get("RequestId")


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间，如2018-08-08 00:00:00。
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-08-08 23:59:59。
        :type EndTime: str
        :param _TaskId: 指定任务 ID 查询
TaskId 和起始时间必须指定一项
        :type TaskId: str
        :param _Keyword: 查询关键字，请输入域名或 http(s):// 开头完整 URL
        :type Keyword: str
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为 20
        :type Limit: int
        :param _Area: 指定地区查询预热记录
mainland：境内
overseas：境外
global：全球
        :type Area: str
        :param _Status: 指定任务状态查询
fail：预热失败
done：预热成功
process：预热中
invalid: 预热无效(源站返回4xx或5xx状态码)
        :type Status: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Keyword = None
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._Status = None

    @property
    def StartTime(self):
        """开始时间，如2018-08-08 00:00:00。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如2018-08-08 23:59:59。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskId(self):
        """指定任务 ID 查询
TaskId 和起始时间必须指定一项
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Keyword(self):
        """查询关键字，请输入域名或 http(s):// 开头完整 URL
        :rtype: str
        """
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为 20
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        """指定地区查询预热记录
mainland：境内
overseas：境外
global：全球
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Status(self):
        """指定任务状态查询
fail：预热失败
done：预热成功
process：预热中
invalid: 预热无效(源站返回4xx或5xx状态码)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Keyword = params.get("Keyword")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _PushLogs: 预热历史记录
注意：此字段可能返回 null，表示取不到有效值。
        :type PushLogs: list of PushTask
        :param _TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PushLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PushLogs(self):
        """预热历史记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PushTask
        """
        return self._PushLogs

    @PushLogs.setter
    def PushLogs(self, PushLogs):
        self._PushLogs = PushLogs

    @property
    def TotalCount(self):
        """任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("PushLogs") is not None:
            self._PushLogs = []
            for item in params.get("PushLogs"):
                obj = PushTask()
                obj._deserialize(item)
                self._PushLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeReportDataRequest(AbstractModel):
    """DescribeReportData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天
        :type StartTime: str
        :param _EndTime: 查询结束时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天
        :type EndTime: str
        :param _ReportType: 报表类型
daily：日报表
weekly：周报表（周一至周日）
monthly：月报表（自然月）
        :type ReportType: str
        :param _Area: 域名加速区域
mainland：中国境内
overseas：中国境外
        :type Area: str
        :param _Offset: 偏移量，默认0。
        :type Offset: int
        :param _Limit: 数据个数，默认1000。
        :type Limit: int
        :param _Project: 按项目ID筛选
        :type Project: int
        """
        self._StartTime = None
        self._EndTime = None
        self._ReportType = None
        self._Area = None
        self._Offset = None
        self._Limit = None
        self._Project = None

    @property
    def StartTime(self):
        """查询起始时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def ReportType(self):
        """报表类型
daily：日报表
weekly：周报表（周一至周日）
monthly：月报表（自然月）
        :rtype: str
        """
        return self._ReportType

    @ReportType.setter
    def ReportType(self, ReportType):
        self._ReportType = ReportType

    @property
    def Area(self):
        """域名加速区域
mainland：中国境内
overseas：中国境外
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Offset(self):
        """偏移量，默认0。
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """数据个数，默认1000。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Project(self):
        """按项目ID筛选
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._ReportType = params.get("ReportType")
        self._Area = params.get("Area")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Project = params.get("Project")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportDataResponse(AbstractModel):
    """DescribeReportData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainReport: 域名维度数据详情
        :type DomainReport: list of ReportData
        :param _ProjectReport: 项目维度数据详情
        :type ProjectReport: list of ReportData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainReport = None
        self._ProjectReport = None
        self._RequestId = None

    @property
    def DomainReport(self):
        """域名维度数据详情
        :rtype: list of ReportData
        """
        return self._DomainReport

    @DomainReport.setter
    def DomainReport(self, DomainReport):
        self._DomainReport = DomainReport

    @property
    def ProjectReport(self):
        """项目维度数据详情
        :rtype: list of ReportData
        """
        return self._ProjectReport

    @ProjectReport.setter
    def ProjectReport(self, ProjectReport):
        self._ProjectReport = ProjectReport

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainReport") is not None:
            self._DomainReport = []
            for item in params.get("DomainReport"):
                obj = ReportData()
                obj._deserialize(item)
                self._DomainReport.append(obj)
        if params.get("ProjectReport") is not None:
            self._ProjectReport = []
            for item in params.get("ProjectReport"):
                obj = ReportData()
                obj._deserialize(item)
                self._ProjectReport.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeScdnBotDataRequest(AbstractModel):
    """DescribeScdnBotData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Area: mainland 大陆地区 overseas境外地区
        :type Area: str
        :param _Interval: 取值："2min"或者"hour"，表示查询2分钟或者1小时粒度的数据，如果查询时间范围>1天，则强制返回1小时粒度数据
        :type Interval: str
        :param _Domains: 域名数组，多选域名时，使用此参数,不填写表示查询所有域名的数据（AppID维度数据）
        :type Domains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._Area = None
        self._Interval = None
        self._Domains = None

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Area(self):
        """mainland 大陆地区 overseas境外地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Interval(self):
        """取值："2min"或者"hour"，表示查询2分钟或者1小时粒度的数据，如果查询时间范围>1天，则强制返回1小时粒度数据
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domains(self):
        """域名数组，多选域名时，使用此参数,不填写表示查询所有域名的数据（AppID维度数据）
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Area = params.get("Area")
        self._Interval = params.get("Interval")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScdnBotDataResponse(AbstractModel):
    """DescribeScdnBotData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 统计信息详细数据
        :type Data: list of BotStats
        :param _Interval: 当前返回数据的粒度，取值："2min"或者"hour"，分别表示2分钟或者1小时粒度
        :type Interval: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """统计信息详细数据
        :rtype: list of BotStats
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        """当前返回数据的粒度，取值："2min"或者"hour"，分别表示2分钟或者1小时粒度
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BotStats()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DescribeScdnBotRecordsRequest(AbstractModel):
    """DescribeScdnBotRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _BotType: BOT类型，取值为"UB","UCB","TCB"，分别表示：未知类型，自定义类型，公开类型
        :type BotType: str
        :param _Domain: 域名
        :type Domain: str
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Offset: 分页参数
        :type Offset: int
        :param _Limit: 分页参数
        :type Limit: int
        :param _Area: mainland 大陆地区 overseas境外地区
        :type Area: str
        :param _SortBy: 排序参数
        :type SortBy: list of BotSortBy
        :param _FilterName: BotType=UB时，表示需要过滤的预测标签，取值如下：
                "crawler_unregular",
                "crawler_regular",
                "request_repeat",
                "credential_miss_user",
                "credential_without_user",
                "credential_only_action",
                "credential_user_password",
                "credential_cracking",
                "credential_stuffing",
                "brush_sms",
                "brush_captcha",
                "reg_malicious"
BotType=TCB时，表示需要过滤的Bot分类，取值如下：
                "Uncategorised",
                "Search engine bot",
                "Site monitor",
                "Screenshot creator",
                "Link checker",
                "Web scraper",
                "Vulnerability scanner",
                "Virus scanner",
                "Speed tester",
                "Feed Fetcher",
                "Tool",
                "Marketing"
BotType=UCB时，取值如下：
User-Agent为空或不存在
User-Agent类型为BOT
User-Agent类型为HTTP Library
User-Agent类型为Framework
User-Agent类型为Tools
User-Agent类型为Unkonwn BOT
User-Agent类型为Scanner
Referer空或不存在
Referer滥用(多个UA使用相同Referer)
Cookie滥用(多个UA使用相同Cookie)
Cookie空或不存在
Connection空或不存在
Accept空或不存在
Accept-Language空或不存在
Accept-Enconding空或不存在
使用HTTP HEAD方法
HTTP协议为1.0或者更低
IDC-IP 腾讯云
IDC-IP 阿里云
IDC-IP 华为云
IDC-IP 金山云
IDC-IP UCloud
IDC-IP 百度云
IDC-IP 京东云
IDC-IP 青云
IDC-IP Aws
IDC-IP Azure
IDC-IP Google

以上所有类型，FilterName为空时，表示不过滤，获取所有内容
        :type FilterName: str
        :param _FilterAction: 目前支持的Action
"intercept" 拦截
"monitor"，监控
"permit" 放行
"redirect" 重定向

尚未支持的Action
"captcha" 验证码
        :type FilterAction: str
        :param _FilterIp: 过滤的IP
        :type FilterIp: str
        :param _Domains: 域名列表，为空表示查询AppID维度数据
        :type Domains: list of str
        """
        self._BotType = None
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None
        self._Area = None
        self._SortBy = None
        self._FilterName = None
        self._FilterAction = None
        self._FilterIp = None
        self._Domains = None

    @property
    def BotType(self):
        """BOT类型，取值为"UB","UCB","TCB"，分别表示：未知类型，自定义类型，公开类型
        :rtype: str
        """
        return self._BotType

    @BotType.setter
    def BotType(self, BotType):
        self._BotType = BotType

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Offset(self):
        """分页参数
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页参数
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Area(self):
        """mainland 大陆地区 overseas境外地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def SortBy(self):
        """排序参数
        :rtype: list of BotSortBy
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy

    @property
    def FilterName(self):
        """BotType=UB时，表示需要过滤的预测标签，取值如下：
                "crawler_unregular",
                "crawler_regular",
                "request_repeat",
                "credential_miss_user",
                "credential_without_user",
                "credential_only_action",
                "credential_user_password",
                "credential_cracking",
                "credential_stuffing",
                "brush_sms",
                "brush_captcha",
                "reg_malicious"
BotType=TCB时，表示需要过滤的Bot分类，取值如下：
                "Uncategorised",
                "Search engine bot",
                "Site monitor",
                "Screenshot creator",
                "Link checker",
                "Web scraper",
                "Vulnerability scanner",
                "Virus scanner",
                "Speed tester",
                "Feed Fetcher",
                "Tool",
                "Marketing"
BotType=UCB时，取值如下：
User-Agent为空或不存在
User-Agent类型为BOT
User-Agent类型为HTTP Library
User-Agent类型为Framework
User-Agent类型为Tools
User-Agent类型为Unkonwn BOT
User-Agent类型为Scanner
Referer空或不存在
Referer滥用(多个UA使用相同Referer)
Cookie滥用(多个UA使用相同Cookie)
Cookie空或不存在
Connection空或不存在
Accept空或不存在
Accept-Language空或不存在
Accept-Enconding空或不存在
使用HTTP HEAD方法
HTTP协议为1.0或者更低
IDC-IP 腾讯云
IDC-IP 阿里云
IDC-IP 华为云
IDC-IP 金山云
IDC-IP UCloud
IDC-IP 百度云
IDC-IP 京东云
IDC-IP 青云
IDC-IP Aws
IDC-IP Azure
IDC-IP Google

以上所有类型，FilterName为空时，表示不过滤，获取所有内容
        :rtype: str
        """
        return self._FilterName

    @FilterName.setter
    def FilterName(self, FilterName):
        self._FilterName = FilterName

    @property
    def FilterAction(self):
        """目前支持的Action
"intercept" 拦截
"monitor"，监控
"permit" 放行
"redirect" 重定向

尚未支持的Action
"captcha" 验证码
        :rtype: str
        """
        return self._FilterAction

    @FilterAction.setter
    def FilterAction(self, FilterAction):
        self._FilterAction = FilterAction

    @property
    def FilterIp(self):
        """过滤的IP
        :rtype: str
        """
        return self._FilterIp

    @FilterIp.setter
    def FilterIp(self, FilterIp):
        self._FilterIp = FilterIp

    @property
    def Domains(self):
        """域名列表，为空表示查询AppID维度数据
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._BotType = params.get("BotType")
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        if params.get("SortBy") is not None:
            self._SortBy = []
            for item in params.get("SortBy"):
                obj = BotSortBy()
                obj._deserialize(item)
                self._SortBy.append(obj)
        self._FilterName = params.get("FilterName")
        self._FilterAction = params.get("FilterAction")
        self._FilterIp = params.get("FilterIp")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScdnBotRecordsResponse(AbstractModel):
    """DescribeScdnBotRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: BOT拦截结果数组
        :type Data: list of BotRecord
        :param _TotalCount: 记录数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        """BOT拦截结果数组
        :rtype: list of BotRecord
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """记录数量
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BotRecord()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeScdnConfigRequest(AbstractModel):
    """DescribeScdnConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScdnConfigResponse(AbstractModel):
    """DescribeScdnConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Acl: 自定义防护策略配置
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param _Waf: Web 攻击防护（WAF）配置
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param _CC: CC 防护配置
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param _Ddos: DDOS 防护配置
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param _Bot: BOT 防护配置
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        :param _Status: 当前状态，取值online | offline
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Acl = None
        self._Waf = None
        self._CC = None
        self._Ddos = None
        self._Bot = None
        self._Status = None
        self._RequestId = None

    @property
    def Acl(self):
        """自定义防护策略配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        """
        return self._Acl

    @Acl.setter
    def Acl(self, Acl):
        self._Acl = Acl

    @property
    def Waf(self):
        """Web 攻击防护（WAF）配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        """
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def CC(self):
        """CC 防护配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        """
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def Ddos(self):
        """DDOS 防护配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        """
        return self._Ddos

    @Ddos.setter
    def Ddos(self, Ddos):
        self._Ddos = Ddos

    @property
    def Bot(self):
        """BOT 防护配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        return self._Bot

    @Bot.setter
    def Bot(self, Bot):
        self._Bot = Bot

    @property
    def Status(self):
        """当前状态，取值online | offline
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Acl") is not None:
            self._Acl = ScdnAclConfig()
            self._Acl._deserialize(params.get("Acl"))
        if params.get("Waf") is not None:
            self._Waf = ScdnWafConfig()
            self._Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self._CC = ScdnConfig()
            self._CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self._Ddos = ScdnDdosConfig()
            self._Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self._Bot = ScdnBotConfig()
            self._Bot._deserialize(params.get("Bot"))
        self._Status = params.get("Status")
        self._RequestId = params.get("RequestId")


class DescribeScdnIpStrategyRequest(AbstractModel):
    """DescribeScdnIpStrategy请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页起始地址
        :type Offset: int
        :param _Limit: 列表分页记录条数，最大1000
        :type Limit: int
        :param _Filters: 查询条件过滤器
        :type Filters: list of ScdnIpStrategyFilter
        :param _Order: 指定查询返回结果的排序字段，支持domain，update_time
        :type Order: str
        :param _Sequence: 排序方式，支持asc，desc
        :type Sequence: str
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Order = None
        self._Sequence = None

    @property
    def Offset(self):
        """分页起始地址
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """列表分页记录条数，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Filters(self):
        """查询条件过滤器
        :rtype: list of ScdnIpStrategyFilter
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Order(self):
        """指定查询返回结果的排序字段，支持domain，update_time
        :rtype: str
        """
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order

    @property
    def Sequence(self):
        """排序方式，支持asc，desc
        :rtype: str
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = ScdnIpStrategyFilter()
                obj._deserialize(item)
                self._Filters.append(obj)
        self._Order = params.get("Order")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScdnIpStrategyResponse(AbstractModel):
    """DescribeScdnIpStrategy返回参数结构体

    """

    def __init__(self):
        r"""
        :param _IpStrategyList: IP策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IpStrategyList: list of ScdnIpStrategy
        :param _TotalCount: 配置的策略条数
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._IpStrategyList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def IpStrategyList(self):
        """IP策略列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnIpStrategy
        """
        return self._IpStrategyList

    @IpStrategyList.setter
    def IpStrategyList(self, IpStrategyList):
        self._IpStrategyList = IpStrategyList

    @property
    def TotalCount(self):
        """配置的策略条数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("IpStrategyList") is not None:
            self._IpStrategyList = []
            for item in params.get("IpStrategyList"):
                obj = ScdnIpStrategy()
                obj._deserialize(item)
                self._IpStrategyList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeScdnTopDataRequest(AbstractModel):
    """DescribeScdnTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param _Mode: 查询的SCDN TOP攻击数据类型：
waf：Web 攻击防护TOP数据
        :type Mode: str
        :param _Metric: 排序对象，支持以下几种形式：
url：攻击目标 url 排序
ip：攻击源 IP 排序
attackType：攻击类型排序
        :type Metric: str
        :param _Filter: 排序使用的指标名称：
request：请求次数
        :type Filter: str
        :param _Domain: 指定域名查询
        :type Domain: str
        :param _AttackType: 指定攻击类型, 仅 Mode=waf 时有效
不填则查询所有攻击类型的数据总和
AttackType 映射如下:
  other = '未知类型'
  malicious_scan = "恶意扫描"
  sql_inject = "SQL注入攻击"
  xss = "XSS攻击"
  cmd_inject = "命令注入攻击"
  ldap_inject = "LDAP注入攻击"
  ssi_inject = "SSI注入攻击"
  xml_inject = "XML注入攻击"
  web_service = "WEB服务漏洞攻击"
  web_app = "WEB应用漏洞攻击"
  path_traversal = "路径跨越攻击"
  illegal_access_core_file = "核心文件非法访问"
  trojan_horse = "木马后门攻击"
  csrf = "CSRF攻击"
  malicious_file_upload= '恶意文件上传'
        :type AttackType: str
        :param _DefenceMode: 指定防御模式,仅 Mode=waf 时有效
不填则查询所有防御模式的数据总和
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :type DefenceMode: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Mode = None
        self._Metric = None
        self._Filter = None
        self._Domain = None
        self._AttackType = None
        self._DefenceMode = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Mode(self):
        """查询的SCDN TOP攻击数据类型：
waf：Web 攻击防护TOP数据
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def Metric(self):
        """排序对象，支持以下几种形式：
url：攻击目标 url 排序
ip：攻击源 IP 排序
attackType：攻击类型排序
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Filter(self):
        """排序使用的指标名称：
request：请求次数
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Domain(self):
        """指定域名查询
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AttackType(self):
        """指定攻击类型, 仅 Mode=waf 时有效
不填则查询所有攻击类型的数据总和
AttackType 映射如下:
  other = '未知类型'
  malicious_scan = "恶意扫描"
  sql_inject = "SQL注入攻击"
  xss = "XSS攻击"
  cmd_inject = "命令注入攻击"
  ldap_inject = "LDAP注入攻击"
  ssi_inject = "SSI注入攻击"
  xml_inject = "XML注入攻击"
  web_service = "WEB服务漏洞攻击"
  web_app = "WEB应用漏洞攻击"
  path_traversal = "路径跨越攻击"
  illegal_access_core_file = "核心文件非法访问"
  trojan_horse = "木马后门攻击"
  csrf = "CSRF攻击"
  malicious_file_upload= '恶意文件上传'
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def DefenceMode(self):
        """指定防御模式,仅 Mode=waf 时有效
不填则查询所有防御模式的数据总和
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :rtype: str
        """
        return self._DefenceMode

    @DefenceMode.setter
    def DefenceMode(self, DefenceMode):
        self._DefenceMode = DefenceMode


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Mode = params.get("Mode")
        self._Metric = params.get("Metric")
        self._Filter = params.get("Filter")
        self._Domain = params.get("Domain")
        self._AttackType = params.get("AttackType")
        self._DefenceMode = params.get("DefenceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScdnTopDataResponse(AbstractModel):
    """DescribeScdnTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopTypeData: WAF 攻击类型统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TopTypeData: list of ScdnTypeData
        :param _TopIpData: TOP 攻击源 IP 统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TopIpData: list of ScdnTopData
        :param _Mode: 查询的SCDN类型，当前仅支持 waf
        :type Mode: str
        :param _TopUrlData: TOP URL 统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TopUrlData: list of ScdnTopUrlData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopTypeData = None
        self._TopIpData = None
        self._Mode = None
        self._TopUrlData = None
        self._RequestId = None

    @property
    def TopTypeData(self):
        """WAF 攻击类型统计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnTypeData
        """
        return self._TopTypeData

    @TopTypeData.setter
    def TopTypeData(self, TopTypeData):
        self._TopTypeData = TopTypeData

    @property
    def TopIpData(self):
        """TOP 攻击源 IP 统计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnTopData
        """
        return self._TopIpData

    @TopIpData.setter
    def TopIpData(self, TopIpData):
        self._TopIpData = TopIpData

    @property
    def Mode(self):
        """查询的SCDN类型，当前仅支持 waf
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def TopUrlData(self):
        """TOP URL 统计
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnTopUrlData
        """
        return self._TopUrlData

    @TopUrlData.setter
    def TopUrlData(self, TopUrlData):
        self._TopUrlData = TopUrlData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopTypeData") is not None:
            self._TopTypeData = []
            for item in params.get("TopTypeData"):
                obj = ScdnTypeData()
                obj._deserialize(item)
                self._TopTypeData.append(obj)
        if params.get("TopIpData") is not None:
            self._TopIpData = []
            for item in params.get("TopIpData"):
                obj = ScdnTopData()
                obj._deserialize(item)
                self._TopIpData.append(obj)
        self._Mode = params.get("Mode")
        if params.get("TopUrlData") is not None:
            self._TopUrlData = []
            for item in params.get("TopUrlData"):
                obj = ScdnTopUrlData()
                obj._deserialize(item)
                self._TopUrlData.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTopDataRequest(AbstractModel):
    """DescribeTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为起始日期
返回大于等于起始日期当天 00:00:00 点产生的数据，如 StartTime为2018-09-04 10:40:00，返回数据的起始时间为2018-09-04 00:00:00
仅支持 90 天内数据查询
        :type StartTime: str
        :param _EndTime: 查询结束日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为结束日期
返回小于等于结束日期当天 23:59:59 产生的数据，如EndTime为2018-09-05 22:40:00，返回数据的结束时间为2018-09-05 23:59:59
EndTime 需要大于等于 StartTime
        :type EndTime: str
        :param _Metric: 排序对象，支持以下几种形式：
ip、ua_device、ua_browser、ua_os、referer
        :type Metric: str
        :param _Filter: 排序使用的指标名称：
flux：Metric 为 host 时指代访问流量
request：Metric 为 host 时指代访问请求数
        :type Filter: str
        :param _Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param _Project: 未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param _Detail: 是否详细显示每个域名的的具体数值
        :type Detail: bool
        :param _Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :type Area: str
        :param _Product: 指定查询的产品数据，目前仅可使用cdn
        :type Product: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Filter = None
        self._Domains = None
        self._Project = None
        self._Detail = None
        self._Area = None
        self._Product = None

    @property
    def StartTime(self):
        """查询起始日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为起始日期
返回大于等于起始日期当天 00:00:00 点产生的数据，如 StartTime为2018-09-04 10:40:00，返回数据的起始时间为2018-09-04 00:00:00
仅支持 90 天内数据查询
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为结束日期
返回小于等于结束日期当天 23:59:59 产生的数据，如EndTime为2018-09-05 22:40:00，返回数据的结束时间为2018-09-05 23:59:59
EndTime 需要大于等于 StartTime
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """排序对象，支持以下几种形式：
ip、ua_device、ua_browser、ua_os、referer
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Filter(self):
        """排序使用的指标名称：
flux：Metric 为 host 时指代访问流量
request：Metric 为 host 时指代访问请求数
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Domains(self):
        """指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        """未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Detail(self):
        """是否详细显示每个域名的的具体数值
        :rtype: bool
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Area(self):
        """指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Product(self):
        """指定查询的产品数据，目前仅可使用cdn
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Filter = params.get("Filter")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Detail = params.get("Detail")
        self._Area = params.get("Area")
        self._Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTopDataResponse(AbstractModel):
    """DescribeTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 各个资源的Top 访问数据详情。
        :type Data: list of TopDataMore
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """各个资源的Top 访问数据详情。
        :rtype: list of TopDataMore
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopDataMore()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeTrafficPackagesRequest(AbstractModel):
    """DescribeTrafficPackages请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询起始地址，默认 0
        :type Offset: int
        :param _Limit: 分页查询记录个数，默认100，最大1000
        :type Limit: int
        :param _SortBy: 流量包排序方式，支持以下值：
expireTimeDesc：默认值，按过期时间倒序
expireTimeAsc：按过期时间正序
createTimeDesc：按创建时间倒序
createTimeAsc：按创建时间正序
status：按状态排序，正常抵扣>未生效>已用尽>已过期
channel：按来源排序，主动购买>自动续订>CDN赠送
        :type SortBy: str
        """
        self._Offset = None
        self._Limit = None
        self._SortBy = None

    @property
    def Offset(self):
        """分页查询起始地址，默认 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询记录个数，默认100，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def SortBy(self):
        """流量包排序方式，支持以下值：
expireTimeDesc：默认值，按过期时间倒序
expireTimeAsc：按过期时间正序
createTimeDesc：按创建时间倒序
createTimeAsc：按创建时间正序
status：按状态排序，正常抵扣>未生效>已用尽>已过期
channel：按来源排序，主动购买>自动续订>CDN赠送
        :rtype: str
        """
        return self._SortBy

    @SortBy.setter
    def SortBy(self, SortBy):
        self._SortBy = SortBy


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._SortBy = params.get("SortBy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTrafficPackagesResponse(AbstractModel):
    """DescribeTrafficPackages返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TotalCount: 流量包总个数
        :type TotalCount: int
        :param _TrafficPackages: 流量包详情
        :type TrafficPackages: list of TrafficPackage
        :param _ExpiringCount: 即将过期的流量包个数（7天内）
        :type ExpiringCount: int
        :param _EnabledCount: 有效流量包个数
        :type EnabledCount: int
        :param _PaidCount: 付费流量包个数
        :type PaidCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TotalCount = None
        self._TrafficPackages = None
        self._ExpiringCount = None
        self._EnabledCount = None
        self._PaidCount = None
        self._RequestId = None

    @property
    def TotalCount(self):
        """流量包总个数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def TrafficPackages(self):
        """流量包详情
        :rtype: list of TrafficPackage
        """
        return self._TrafficPackages

    @TrafficPackages.setter
    def TrafficPackages(self, TrafficPackages):
        self._TrafficPackages = TrafficPackages

    @property
    def ExpiringCount(self):
        """即将过期的流量包个数（7天内）
        :rtype: int
        """
        return self._ExpiringCount

    @ExpiringCount.setter
    def ExpiringCount(self, ExpiringCount):
        self._ExpiringCount = ExpiringCount

    @property
    def EnabledCount(self):
        """有效流量包个数
        :rtype: int
        """
        return self._EnabledCount

    @EnabledCount.setter
    def EnabledCount(self, EnabledCount):
        self._EnabledCount = EnabledCount

    @property
    def PaidCount(self):
        """付费流量包个数
        :rtype: int
        """
        return self._PaidCount

    @PaidCount.setter
    def PaidCount(self, PaidCount):
        self._PaidCount = PaidCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TotalCount = params.get("TotalCount")
        if params.get("TrafficPackages") is not None:
            self._TrafficPackages = []
            for item in params.get("TrafficPackages"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self._TrafficPackages.append(obj)
        self._ExpiringCount = params.get("ExpiringCount")
        self._EnabledCount = params.get("EnabledCount")
        self._PaidCount = params.get("PaidCount")
        self._RequestId = params.get("RequestId")


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为 100
        :type Limit: int
        :param _Domains: 指定的域名查询
        :type Domains: list of str
        """
        self._Offset = None
        self._Limit = None
        self._Domains = None

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为 100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Domains(self):
        """指定的域名查询
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UrlRecordList: 违规 URL 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of ViolationUrl
        :param _TotalCount: 记录总数，用于分页
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UrlRecordList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UrlRecordList(self):
        """违规 URL 详情
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ViolationUrl
        """
        return self._UrlRecordList

    @UrlRecordList.setter
    def UrlRecordList(self, UrlRecordList):
        self._UrlRecordList = UrlRecordList

    @property
    def TotalCount(self):
        """记录总数，用于分页
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self._UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = ViolationUrl()
                obj._deserialize(item)
                self._UrlRecordList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeWafDataRequest(AbstractModel):
    """DescribeWafData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param _Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据

仅支持30天内数据查询，且查询时间范围在 7 到 30 天最小粒度是 hour。
        :type Interval: str
        :param _Domain: 指定域名查询
        :type Domain: str
        :param _AttackType: 指定攻击类型
不填则查询所有攻击类型的数据分布
AttackType 映射如下:
"webshell" : Webshell检测防护
"oa" : 常见OA漏洞防护
"xss" : XSS跨站脚本攻击防护
"xxe" : XXE攻击防护
"webscan" : 扫描器攻击漏洞防护
"cms" : 常见CMS漏洞防护
"upload" : 恶意文件上传攻击防护
"sql" : SQL注入攻击防护
"cmd_inject": 命令/代码注入攻击防护
"osc" : 开源组件漏洞防护
"file_read" : 任意文件读取
"ldap" : LDAP注入攻击防护
"other" : 其它漏洞防护
        :type AttackType: str
        :param _DefenceMode: 指定防御模式
不填则查询所有防御模式的数据总和
DefenceMode映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :type DefenceMode: str
        :param _Area: 地域：mainland 或 overseas
        :type Area: str
        :param _AttackTypes: 指定多个攻击类型，取值参考AttackType
        :type AttackTypes: list of str
        :param _Domains: 指定域名列表查询
        :type Domains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._Interval = None
        self._Domain = None
        self._AttackType = None
        self._DefenceMode = None
        self._Area = None
        self._AttackTypes = None
        self._Domains = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Interval(self):
        """时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据

仅支持30天内数据查询，且查询时间范围在 7 到 30 天最小粒度是 hour。
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domain(self):
        """指定域名查询
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AttackType(self):
        """指定攻击类型
不填则查询所有攻击类型的数据分布
AttackType 映射如下:
"webshell" : Webshell检测防护
"oa" : 常见OA漏洞防护
"xss" : XSS跨站脚本攻击防护
"xxe" : XXE攻击防护
"webscan" : 扫描器攻击漏洞防护
"cms" : 常见CMS漏洞防护
"upload" : 恶意文件上传攻击防护
"sql" : SQL注入攻击防护
"cmd_inject": 命令/代码注入攻击防护
"osc" : 开源组件漏洞防护
"file_read" : 任意文件读取
"ldap" : LDAP注入攻击防护
"other" : 其它漏洞防护
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def DefenceMode(self):
        """指定防御模式
不填则查询所有防御模式的数据总和
DefenceMode映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :rtype: str
        """
        return self._DefenceMode

    @DefenceMode.setter
    def DefenceMode(self, DefenceMode):
        self._DefenceMode = DefenceMode

    @property
    def Area(self):
        """地域：mainland 或 overseas
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AttackTypes(self):
        """指定多个攻击类型，取值参考AttackType
        :rtype: list of str
        """
        return self._AttackTypes

    @AttackTypes.setter
    def AttackTypes(self, AttackTypes):
        self._AttackTypes = AttackTypes

    @property
    def Domains(self):
        """指定域名列表查询
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        self._Domain = params.get("Domain")
        self._AttackType = params.get("AttackType")
        self._DefenceMode = params.get("DefenceMode")
        self._Area = params.get("Area")
        self._AttackTypes = params.get("AttackTypes")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeWafDataResponse(AbstractModel):
    """DescribeWafData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 粒度数据
        :type Data: list of TimestampData
        :param _Interval: 粒度
        :type Interval: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._Interval = None
        self._RequestId = None

    @property
    def Data(self):
        """粒度数据
        :rtype: list of TimestampData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Interval(self):
        """粒度
        :rtype: str
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TimestampData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Interval = params.get("Interval")
        self._RequestId = params.get("RequestId")


class DetailDomain(AbstractModel):
    """加速域名全量配置信息

    """

    def __init__(self):
        r"""
        :param _ResourceId: 域名 ID
        :type ResourceId: str
        :param _AppId: 腾讯云账号ID
        :type AppId: int
        :param _Domain: 加速域名
        :type Domain: str
        :param _Cname: 域名对应的 CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param _Status: 加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
closing：关闭中
online：已启动
offline：已关闭
        :type Status: str
        :param _ProjectId: 项目 ID，可前往腾讯云项目管理页面查看
        :type ProjectId: int
        :param _ServiceType: 加速域名业务类型
web：网页小文件
download：下载大文件
media：音视频点播
hybrid:  动静加速
dynamic:  动态加速
        :type ServiceType: str
        :param _CreateTime: 域名创建时间
        :type CreateTime: str
        :param _UpdateTime: 域名更新时间
        :type UpdateTime: str
        :param _Origin: 源站配置
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _IpFilter: IP 黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP 访问限频配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _StatusCodeCache: 状态码缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _Compression: 智能压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _BandwidthAlert: 带宽封顶配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _RangeOriginPull: Range 回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _FollowRedirect: 301/302 回源自动跟随配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ErrorPage: 自定义错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _RequestHeader: 自定义请求头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: 自定义响应头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _DownstreamCapping: 单链接下行限速配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _CacheKey: 带参/不带参缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _ResponseHeaderCache: 源站头部缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _VideoSeek: 视频拖拽配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _Cache: 节点缓存过期规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _OriginPullOptimization: 跨国链路优化配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _Https: Https 加速相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _Authentication: 时间戳防盗链配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _Seo: SEO 优化配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _Disable: 域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定
注意：此字段可能返回 null，表示取不到有效值。
        :type Disable: str
        :param _ForceRedirect: 访问协议强制跳转配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Referer: Referer 防盗链配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _MaxAge: 浏览器缓存过期规则配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Ipv6: Ipv6 回源配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param _Compatibility: 是否兼容旧版本配置（内部兼容性字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type Compatibility: :class:`tencentcloud.cdn.v20180606.models.Compatibility`
        :param _SpecificConfig: 区域特殊配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param _Area: 加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param _Readonly: 域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
注意：此字段可能返回 null，表示取不到有效值。
        :type Readonly: str
        :param _OriginPullTimeout: 回源超时配置
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param _AwsPrivateAccess: 回源S3鉴权配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _SecurityConfig: Scdn配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityConfig: :class:`tencentcloud.cdn.v20180606.models.SecurityConfig`
        :param _ImageOptimization: ImageOptimization配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageOptimization: :class:`tencentcloud.cdn.v20180606.models.ImageOptimization`
        :param _UserAgentFilter: UA黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param _AccessControl: 访问控制
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param _Advance: 是否支持高级配置项
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Advance: str
        :param _UrlRedirect: URL重定向配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param _AccessPort: 访问端口配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessPort: list of int
        :param _Tag: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _AdvancedAuthentication: 时间戳防盗链高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param _OriginAuthentication: 回源鉴权高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param _Ipv6Access: Ipv6访问配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param _AdvanceSet: 高级配置集合
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceSet: list of AdvanceConfig
        :param _OfflineCache: 离线缓存（功能灰度中，尚未全量，请等待后续全量发布）
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param _OriginCombine: 合并回源（白名单功能）
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param _PostMaxSize: POST上传配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        :param _Quic: Quic配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param _OssPrivateAccess: 回源OSS私有鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _WebSocket: WebSocket配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        :param _RemoteAuthentication: 远程鉴权配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoteAuthentication: :class:`tencentcloud.cdn.v20180606.models.RemoteAuthentication`
        :param _ShareCname: 共享CNAME配置（白名单功能）
注意：此字段可能返回 null，表示取不到有效值。
        :type ShareCname: :class:`tencentcloud.cdn.v20180606.models.ShareCname`
        :param _RuleEngine: 规则引擎
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleEngine: :class:`tencentcloud.cdn.v20180606.models.RuleEngine`
        :param _ParentHost: 主域名
注意：此字段可能返回 null，表示取不到有效值。
        :type ParentHost: str
        :param _HwPrivateAccess: 华为云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: 七牛云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        :param _HttpsBilling: HTTPS服务，缺省时默认开启
注意：此字段可能返回 null，表示取不到有效值。
        :type HttpsBilling: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        :param _OthersPrivateAccess: 其他厂商对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type OthersPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        :param _ParamFilter: 参数黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type ParamFilter: :class:`tencentcloud.cdn.v20180606.models.ParamFilter`
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._ServiceType = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._StatusCodeCache = None
        self._Compression = None
        self._BandwidthAlert = None
        self._RangeOriginPull = None
        self._FollowRedirect = None
        self._ErrorPage = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._DownstreamCapping = None
        self._CacheKey = None
        self._ResponseHeaderCache = None
        self._VideoSeek = None
        self._Cache = None
        self._OriginPullOptimization = None
        self._Https = None
        self._Authentication = None
        self._Seo = None
        self._Disable = None
        self._ForceRedirect = None
        self._Referer = None
        self._MaxAge = None
        self._Ipv6 = None
        self._Compatibility = None
        self._SpecificConfig = None
        self._Area = None
        self._Readonly = None
        self._OriginPullTimeout = None
        self._AwsPrivateAccess = None
        self._SecurityConfig = None
        self._ImageOptimization = None
        self._UserAgentFilter = None
        self._AccessControl = None
        self._Advance = None
        self._UrlRedirect = None
        self._AccessPort = None
        self._Tag = None
        self._AdvancedAuthentication = None
        self._OriginAuthentication = None
        self._Ipv6Access = None
        self._AdvanceSet = None
        self._OfflineCache = None
        self._OriginCombine = None
        self._PostMaxSize = None
        self._Quic = None
        self._OssPrivateAccess = None
        self._WebSocket = None
        self._RemoteAuthentication = None
        self._ShareCname = None
        self._RuleEngine = None
        self._ParentHost = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None
        self._HttpsBilling = None
        self._OthersPrivateAccess = None
        self._ParamFilter = None

    @property
    def ResourceId(self):
        """域名 ID
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        """腾讯云账号ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        """加速域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        """域名对应的 CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        """加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
closing：关闭中
online：已启动
offline：已关闭
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        """项目 ID，可前往腾讯云项目管理页面查看
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def ServiceType(self):
        """加速域名业务类型
web：网页小文件
download：下载大文件
media：音视频点播
hybrid:  动静加速
dynamic:  动态加速
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def CreateTime(self):
        """域名创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """域名更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        """源站配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def IpFilter(self):
        """IP 黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP 访问限频配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def StatusCodeCache(self):
        """状态码缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        """
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def Compression(self):
        """智能压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def BandwidthAlert(self):
        """带宽封顶配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        """
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def RangeOriginPull(self):
        """Range 回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        """
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def FollowRedirect(self):
        """301/302 回源自动跟随配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        """
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ErrorPage(self):
        """自定义错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def RequestHeader(self):
        """自定义请求头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        """自定义响应头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def DownstreamCapping(self):
        """单链接下行限速配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        """
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def CacheKey(self):
        """带参/不带参缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def ResponseHeaderCache(self):
        """源站头部缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        """
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def VideoSeek(self):
        """视频拖拽配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def Cache(self):
        """节点缓存过期规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def OriginPullOptimization(self):
        """跨国链路优化配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        """
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def Https(self):
        """Https 加速相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Authentication(self):
        """时间戳防盗链配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Seo(self):
        """SEO 优化配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Seo`
        """
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def Disable(self):
        """域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ForceRedirect(self):
        """访问协议强制跳转配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Referer(self):
        """Referer 防盗链配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Referer`
        """
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def MaxAge(self):
        """浏览器缓存过期规则配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Ipv6(self):
        """Ipv6 回源配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6

    @property
    def Compatibility(self):
        """是否兼容旧版本配置（内部兼容性字段）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Compatibility`
        """
        return self._Compatibility

    @Compatibility.setter
    def Compatibility(self, Compatibility):
        self._Compatibility = Compatibility

    @property
    def SpecificConfig(self):
        """区域特殊配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        """
        return self._SpecificConfig

    @SpecificConfig.setter
    def SpecificConfig(self, SpecificConfig):
        self._SpecificConfig = SpecificConfig

    @property
    def Area(self):
        """加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        """域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def OriginPullTimeout(self):
        """回源超时配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        """
        return self._OriginPullTimeout

    @OriginPullTimeout.setter
    def OriginPullTimeout(self, OriginPullTimeout):
        self._OriginPullTimeout = OriginPullTimeout

    @property
    def AwsPrivateAccess(self):
        """回源S3鉴权配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        """
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def SecurityConfig(self):
        """Scdn配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SecurityConfig`
        """
        return self._SecurityConfig

    @SecurityConfig.setter
    def SecurityConfig(self, SecurityConfig):
        self._SecurityConfig = SecurityConfig

    @property
    def ImageOptimization(self):
        """ImageOptimization配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ImageOptimization`
        """
        return self._ImageOptimization

    @ImageOptimization.setter
    def ImageOptimization(self, ImageOptimization):
        self._ImageOptimization = ImageOptimization

    @property
    def UserAgentFilter(self):
        """UA黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        """
        return self._UserAgentFilter

    @UserAgentFilter.setter
    def UserAgentFilter(self, UserAgentFilter):
        self._UserAgentFilter = UserAgentFilter

    @property
    def AccessControl(self):
        """访问控制
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        """
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def Advance(self):
        """是否支持高级配置项
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Advance

    @Advance.setter
    def Advance(self, Advance):
        self._Advance = Advance

    @property
    def UrlRedirect(self):
        """URL重定向配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        """
        return self._UrlRedirect

    @UrlRedirect.setter
    def UrlRedirect(self, UrlRedirect):
        self._UrlRedirect = UrlRedirect

    @property
    def AccessPort(self):
        """访问端口配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of int
        """
        return self._AccessPort

    @AccessPort.setter
    def AccessPort(self, AccessPort):
        self._AccessPort = AccessPort

    @property
    def Tag(self):
        """标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of Tag
        """
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def AdvancedAuthentication(self):
        """时间戳防盗链高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        """
        return self._AdvancedAuthentication

    @AdvancedAuthentication.setter
    def AdvancedAuthentication(self, AdvancedAuthentication):
        self._AdvancedAuthentication = AdvancedAuthentication

    @property
    def OriginAuthentication(self):
        """回源鉴权高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        """
        return self._OriginAuthentication

    @OriginAuthentication.setter
    def OriginAuthentication(self, OriginAuthentication):
        self._OriginAuthentication = OriginAuthentication

    @property
    def Ipv6Access(self):
        """Ipv6访问配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        """
        return self._Ipv6Access

    @Ipv6Access.setter
    def Ipv6Access(self, Ipv6Access):
        self._Ipv6Access = Ipv6Access

    @property
    def AdvanceSet(self):
        """高级配置集合
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvanceConfig
        """
        return self._AdvanceSet

    @AdvanceSet.setter
    def AdvanceSet(self, AdvanceSet):
        self._AdvanceSet = AdvanceSet

    @property
    def OfflineCache(self):
        """离线缓存（功能灰度中，尚未全量，请等待后续全量发布）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        """
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def OriginCombine(self):
        """合并回源（白名单功能）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        """
        return self._OriginCombine

    @OriginCombine.setter
    def OriginCombine(self, OriginCombine):
        self._OriginCombine = OriginCombine

    @property
    def PostMaxSize(self):
        """POST上传配置项
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        """
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Quic(self):
        """Quic配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Quic`
        """
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def OssPrivateAccess(self):
        """回源OSS私有鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        """
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def WebSocket(self):
        """WebSocket配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def RemoteAuthentication(self):
        """远程鉴权配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RemoteAuthentication`
        """
        return self._RemoteAuthentication

    @RemoteAuthentication.setter
    def RemoteAuthentication(self, RemoteAuthentication):
        self._RemoteAuthentication = RemoteAuthentication

    @property
    def ShareCname(self):
        """共享CNAME配置（白名单功能）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ShareCname`
        """
        return self._ShareCname

    @ShareCname.setter
    def ShareCname(self, ShareCname):
        self._ShareCname = ShareCname

    @property
    def RuleEngine(self):
        """规则引擎
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RuleEngine`
        """
        return self._RuleEngine

    @RuleEngine.setter
    def RuleEngine(self, RuleEngine):
        self._RuleEngine = RuleEngine

    @property
    def ParentHost(self):
        """主域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ParentHost

    @ParentHost.setter
    def ParentHost(self, ParentHost):
        self._ParentHost = ParentHost

    @property
    def HwPrivateAccess(self):
        """华为云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        """
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        """七牛云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess

    @property
    def HttpsBilling(self):
        """HTTPS服务，缺省时默认开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        """
        return self._HttpsBilling

    @HttpsBilling.setter
    def HttpsBilling(self, HttpsBilling):
        self._HttpsBilling = HttpsBilling

    @property
    def OthersPrivateAccess(self):
        """其他厂商对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        """
        return self._OthersPrivateAccess

    @OthersPrivateAccess.setter
    def OthersPrivateAccess(self, OthersPrivateAccess):
        self._OthersPrivateAccess = OthersPrivateAccess

    @property
    def ParamFilter(self):
        """参数黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ParamFilter`
        """
        return self._ParamFilter

    @ParamFilter.setter
    def ParamFilter(self, ParamFilter):
        self._ParamFilter = ParamFilter


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._ServiceType = params.get("ServiceType")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        self._Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self._Ipv6 = Ipv6()
            self._Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Compatibility") is not None:
            self._Compatibility = Compatibility()
            self._Compatibility._deserialize(params.get("Compatibility"))
        if params.get("SpecificConfig") is not None:
            self._SpecificConfig = SpecificConfig()
            self._SpecificConfig._deserialize(params.get("SpecificConfig"))
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        if params.get("OriginPullTimeout") is not None:
            self._OriginPullTimeout = OriginPullTimeout()
            self._OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("SecurityConfig") is not None:
            self._SecurityConfig = SecurityConfig()
            self._SecurityConfig._deserialize(params.get("SecurityConfig"))
        if params.get("ImageOptimization") is not None:
            self._ImageOptimization = ImageOptimization()
            self._ImageOptimization._deserialize(params.get("ImageOptimization"))
        if params.get("UserAgentFilter") is not None:
            self._UserAgentFilter = UserAgentFilter()
            self._UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self._AccessControl = AccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        self._Advance = params.get("Advance")
        if params.get("UrlRedirect") is not None:
            self._UrlRedirect = UrlRedirect()
            self._UrlRedirect._deserialize(params.get("UrlRedirect"))
        self._AccessPort = params.get("AccessPort")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("AdvancedAuthentication") is not None:
            self._AdvancedAuthentication = AdvancedAuthentication()
            self._AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self._OriginAuthentication = OriginAuthentication()
            self._OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self._Ipv6Access = Ipv6Access()
            self._Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("AdvanceSet") is not None:
            self._AdvanceSet = []
            for item in params.get("AdvanceSet"):
                obj = AdvanceConfig()
                obj._deserialize(item)
                self._AdvanceSet.append(obj)
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self._OriginCombine = OriginCombine()
            self._OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("RemoteAuthentication") is not None:
            self._RemoteAuthentication = RemoteAuthentication()
            self._RemoteAuthentication._deserialize(params.get("RemoteAuthentication"))
        if params.get("ShareCname") is not None:
            self._ShareCname = ShareCname()
            self._ShareCname._deserialize(params.get("ShareCname"))
        if params.get("RuleEngine") is not None:
            self._RuleEngine = RuleEngine()
            self._RuleEngine._deserialize(params.get("RuleEngine"))
        self._ParentHost = params.get("ParentHost")
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        if params.get("HttpsBilling") is not None:
            self._HttpsBilling = HttpsBilling()
            self._HttpsBilling._deserialize(params.get("HttpsBilling"))
        if params.get("OthersPrivateAccess") is not None:
            self._OthersPrivateAccess = OthersPrivateAccess()
            self._OthersPrivateAccess._deserialize(params.get("OthersPrivateAccess"))
        if params.get("ParamFilter") is not None:
            self._ParamFilter = ParamFilter()
            self._ParamFilter._deserialize(params.get("ParamFilter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseData(AbstractModel):
    """诊断报告内容数据

    """

    def __init__(self):
        r"""
        :param _Data: 诊断报告内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DiagnoseUnit
        :param _Status: 当前诊断项是否正常。
"ok"：正常
"error"：异常
"warning"："警告"
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self._Data = None
        self._Status = None

    @property
    def Data(self):
        """诊断报告内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DiagnoseUnit
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def Status(self):
        """当前诊断项是否正常。
"ok"：正常
"error"：异常
"warning"："警告"
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DiagnoseUnit()
                obj._deserialize(item)
                self._Data.append(obj)
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseInfo(AbstractModel):
    """诊断信息

    """

    def __init__(self):
        r"""
        :param _DiagnoseUrl: 待诊断的URL。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseUrl: str
        :param _DiagnoseLink: 由系统生成的诊断链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseLink: str
        :param _CreateTime: 诊断创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _ExpireDate: 诊断链接过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireDate: str
        :param _VisitCount: 诊断链接当前访问次数，一个诊断链接最多可访问10次。
注意：此字段可能返回 null，表示取不到有效值。
        :type VisitCount: int
        :param _ClientList: 访问诊断链接的客户端简易信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientList: list of DiagnoseList
        :param _Area: 域名加速区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
        self._DiagnoseUrl = None
        self._DiagnoseLink = None
        self._CreateTime = None
        self._ExpireDate = None
        self._VisitCount = None
        self._ClientList = None
        self._Area = None

    @property
    def DiagnoseUrl(self):
        """待诊断的URL。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiagnoseUrl

    @DiagnoseUrl.setter
    def DiagnoseUrl(self, DiagnoseUrl):
        self._DiagnoseUrl = DiagnoseUrl

    @property
    def DiagnoseLink(self):
        """由系统生成的诊断链接。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiagnoseLink

    @DiagnoseLink.setter
    def DiagnoseLink(self, DiagnoseLink):
        self._DiagnoseLink = DiagnoseLink

    @property
    def CreateTime(self):
        """诊断创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def ExpireDate(self):
        """诊断链接过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireDate

    @ExpireDate.setter
    def ExpireDate(self, ExpireDate):
        self._ExpireDate = ExpireDate

    @property
    def VisitCount(self):
        """诊断链接当前访问次数，一个诊断链接最多可访问10次。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._VisitCount

    @VisitCount.setter
    def VisitCount(self, VisitCount):
        self._VisitCount = VisitCount

    @property
    def ClientList(self):
        """访问诊断链接的客户端简易信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of DiagnoseList
        """
        return self._ClientList

    @ClientList.setter
    def ClientList(self, ClientList):
        self._ClientList = ClientList

    @property
    def Area(self):
        """域名加速区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._DiagnoseUrl = params.get("DiagnoseUrl")
        self._DiagnoseLink = params.get("DiagnoseLink")
        self._CreateTime = params.get("CreateTime")
        self._ExpireDate = params.get("ExpireDate")
        self._VisitCount = params.get("VisitCount")
        if params.get("ClientList") is not None:
            self._ClientList = []
            for item in params.get("ClientList"):
                obj = DiagnoseList()
                obj._deserialize(item)
                self._ClientList.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseList(AbstractModel):
    """客户端访问诊断URL信息列表

    """

    def __init__(self):
        r"""
        :param _DiagnoseTag: 诊断任务标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseTag: str
        :param _ReportId: 报告ID，用于获取详细诊断报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param _ClientInfo: 客户端信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientInfo: list of ClientInfo
        :param _FinalDiagnose: 最终诊断结果。
-1：已提交
0  ：检测中
1  ：检测正常
2  ： 检测异常
3  ： 诊断页面异常关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalDiagnose: int
        :param _CreateTime: 诊断任务创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self._DiagnoseTag = None
        self._ReportId = None
        self._ClientInfo = None
        self._FinalDiagnose = None
        self._CreateTime = None

    @property
    def DiagnoseTag(self):
        """诊断任务标签。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DiagnoseTag

    @DiagnoseTag.setter
    def DiagnoseTag(self, DiagnoseTag):
        self._DiagnoseTag = DiagnoseTag

    @property
    def ReportId(self):
        """报告ID，用于获取详细诊断报告。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReportId

    @ReportId.setter
    def ReportId(self, ReportId):
        self._ReportId = ReportId

    @property
    def ClientInfo(self):
        """客户端信息。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ClientInfo
        """
        return self._ClientInfo

    @ClientInfo.setter
    def ClientInfo(self, ClientInfo):
        self._ClientInfo = ClientInfo

    @property
    def FinalDiagnose(self):
        """最终诊断结果。
-1：已提交
0  ：检测中
1  ：检测正常
2  ： 检测异常
3  ： 诊断页面异常关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FinalDiagnose

    @FinalDiagnose.setter
    def FinalDiagnose(self, FinalDiagnose):
        self._FinalDiagnose = FinalDiagnose

    @property
    def CreateTime(self):
        """诊断任务创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._DiagnoseTag = params.get("DiagnoseTag")
        self._ReportId = params.get("ReportId")
        if params.get("ClientInfo") is not None:
            self._ClientInfo = []
            for item in params.get("ClientInfo"):
                obj = ClientInfo()
                obj._deserialize(item)
                self._ClientInfo.append(obj)
        self._FinalDiagnose = params.get("FinalDiagnose")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseUnit(AbstractModel):
    """诊断报告单元信息

    """

    def __init__(self):
        r"""
        :param _Key: 内容单元英文名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _KeyText: 内容单元中文名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyText: str
        :param _Value: 报告内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _ValueText: 报告内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueText: str
        """
        self._Key = None
        self._KeyText = None
        self._Value = None
        self._ValueText = None

    @property
    def Key(self):
        """内容单元英文名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def KeyText(self):
        """内容单元中文名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._KeyText

    @KeyText.setter
    def KeyText(self, KeyText):
        self._KeyText = KeyText

    @property
    def Value(self):
        """报告内容。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def ValueText(self):
        """报告内容。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ValueText

    @ValueText.setter
    def ValueText(self, ValueText):
        self._ValueText = ValueText


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._KeyText = params.get("KeyText")
        self._Value = params.get("Value")
        self._ValueText = params.get("ValueText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesRequest(AbstractModel):
    """DisableCaches请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 禁用的 URL 列表（分协议生效，必须包含http://或https://）
每次最多可提交 100 条，每日最多可提交 3000 条
        :type Urls: list of str
        """
        self._Urls = None

    @property
    def Urls(self):
        """禁用的 URL 列表（分协议生效，必须包含http://或https://）
每次最多可提交 100 条，每日最多可提交 3000 条
        :rtype: list of str
        """
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
        


class DisableCachesResponse(AbstractModel):
    """DisableCaches返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CacheOptResult: 提交结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CacheOptResult = None
        self._TaskId = None
        self._RequestId = None

    @property
    def CacheOptResult(self):
        """提交结果
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        """
        return self._CacheOptResult

    @CacheOptResult.setter
    def CacheOptResult(self, CacheOptResult):
        self._CacheOptResult = CacheOptResult

    @property
    def TaskId(self):
        """任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self._CacheOptResult = CacheOptResult()
            self._CacheOptResult._deserialize(params.get("CacheOptResult"))
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class DisableClsLogTopicRequest(AbstractModel):
    """DisableClsLogTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableClsLogTopicResponse(AbstractModel):
    """DisableClsLogTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class DistrictIspInfo(AbstractModel):
    """地区运营商明细数据

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Protocol: 协议类型
        :type Protocol: str
        :param _IpProtocol: IP协议类型
        :type IpProtocol: str
        :param _StartTime: 起始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Interval: 时间间隔，单位为分钟
        :type Interval: int
        :param _Metric: 指标名称
        :type Metric: str
        :param _District: 地区ID
        :type District: int
        :param _Isp: 运营商ID
        :type Isp: int
        :param _DataPoints: 指标数据点
        :type DataPoints: list of int non-negative
        :param _DistrictName: 地区名称
        :type DistrictName: str
        :param _IspName: 运营商名称
        :type IspName: str
        """
        self._Domain = None
        self._Protocol = None
        self._IpProtocol = None
        self._StartTime = None
        self._EndTime = None
        self._Interval = None
        self._Metric = None
        self._District = None
        self._Isp = None
        self._DataPoints = None
        self._DistrictName = None
        self._IspName = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Protocol(self):
        """协议类型
        :rtype: str
        """
        return self._Protocol

    @Protocol.setter
    def Protocol(self, Protocol):
        self._Protocol = Protocol

    @property
    def IpProtocol(self):
        """IP协议类型
        :rtype: str
        """
        return self._IpProtocol

    @IpProtocol.setter
    def IpProtocol(self, IpProtocol):
        self._IpProtocol = IpProtocol

    @property
    def StartTime(self):
        """起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Interval(self):
        """时间间隔，单位为分钟
        :rtype: int
        """
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Metric(self):
        """指标名称
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def District(self):
        """地区ID
        :rtype: int
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Isp(self):
        """运营商ID
        :rtype: int
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def DataPoints(self):
        """指标数据点
        :rtype: list of int non-negative
        """
        return self._DataPoints

    @DataPoints.setter
    def DataPoints(self, DataPoints):
        self._DataPoints = DataPoints

    @property
    def DistrictName(self):
        """地区名称
        :rtype: str
        """
        return self._DistrictName

    @DistrictName.setter
    def DistrictName(self, DistrictName):
        self._DistrictName = DistrictName

    @property
    def IspName(self):
        """运营商名称
        :rtype: str
        """
        return self._IspName

    @IspName.setter
    def IspName(self, IspName):
        self._IspName = IspName


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Protocol = params.get("Protocol")
        self._IpProtocol = params.get("IpProtocol")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Interval = params.get("Interval")
        self._Metric = params.get("Metric")
        self._District = params.get("District")
        self._Isp = params.get("Isp")
        self._DataPoints = params.get("DataPoints")
        self._DistrictName = params.get("DistrictName")
        self._IspName = params.get("IspName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAreaConfig(AbstractModel):
    """域名地区配置

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Area: 地区列表，其中元素可为mainland/overseas
        :type Area: list of str
        """
        self._Domain = None
        self._Area = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Area(self):
        """地区列表，其中元素可为mainland/overseas
        :rtype: list of str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainBotCount(AbstractModel):
    """域名及其他指标Bot次数

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Count: BOT次数
        :type Count: int
        :param _Value: Top指标值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param _Country: 国家/地区
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param _Province: 省份
注意：此字段可能返回 null，表示取不到有效值。
        :type Province: str
        :param _Isp: 运营商
注意：此字段可能返回 null，表示取不到有效值。
        :type Isp: str
        """
        self._Domain = None
        self._Count = None
        self._Value = None
        self._Country = None
        self._Province = None
        self._Isp = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Count(self):
        """BOT次数
        :rtype: int
        """
        return self._Count

    @Count.setter
    def Count(self, Count):
        self._Count = Count

    @property
    def Value(self):
        """Top指标值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Country(self):
        """国家/地区
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Country

    @Country.setter
    def Country(self, Country):
        self._Country = Country

    @property
    def Province(self):
        """省份
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Province

    @Province.setter
    def Province(self, Province):
        self._Province = Province

    @property
    def Isp(self):
        """运营商
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Count = params.get("Count")
        self._Value = params.get("Value")
        self._Country = params.get("Country")
        self._Province = params.get("Province")
        self._Isp = params.get("Isp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainFilter(AbstractModel):
    """域名查询时过滤条件。

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名，支持的列表如下：
- origin：主源站。
- domain：域名。
- resourceId：域名id。
- status：域名状态，online，offline或processing，deleted。
- serviceType：业务类型，web，download，media，hybrid或dynamic。
- projectId：项目ID。
- domainType：主源站类型，cname表示自有源，cos表示cos接入，third_party表示第三方对象存储，igtm表示IGTM多活源。
- fullUrlCache：全路径缓存，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源协议类型，支持http，follow或https。
- tagKey：标签键。
        :type Name: str
        :param _Value: 过滤字段值，默认最多传 5 个。当 Name 是 origin/domain 且 Fuzzy 传 true，最多传 1 个。
        :type Value: list of str
        :param _Fuzzy: 是否启用模糊查询，仅支持过滤字段名为origin，domain。
模糊查询时，Value长度最大为1，否则Value长度最大为5。
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        """过滤字段名，支持的列表如下：
- origin：主源站。
- domain：域名。
- resourceId：域名id。
- status：域名状态，online，offline或processing，deleted。
- serviceType：业务类型，web，download，media，hybrid或dynamic。
- projectId：项目ID。
- domainType：主源站类型，cname表示自有源，cos表示cos接入，third_party表示第三方对象存储，igtm表示IGTM多活源。
- fullUrlCache：全路径缓存，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源协议类型，支持http，follow或https。
- tagKey：标签键。
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """过滤字段值，默认最多传 5 个。当 Name 是 origin/domain 且 Fuzzy 传 true，最多传 1 个。
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
        """是否启用模糊查询，仅支持过滤字段名为origin，domain。
模糊查询时，Value长度最大为1，否则Value长度最大为5。
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainLog(AbstractModel):
    """日志包下载链接详情

    """

    def __init__(self):
        r"""
        :param _StartTime: 日志包起始时间
        :type StartTime: str
        :param _EndTime: 日志包结束时间
        :type EndTime: str
        :param _LogPath: 日志包下载链接
        :type LogPath: str
        :param _Area: 日志包对应加速区域
mainland：境内
overseas：境外
        :type Area: str
        :param _LogName: 日志包文件名
        :type LogName: str
        :param _FileSize: 文件大小，单位: Byte
注意：此字段可能返回 null，表示取不到有效值。
        :type FileSize: int
        """
        self._StartTime = None
        self._EndTime = None
        self._LogPath = None
        self._Area = None
        self._LogName = None
        self._FileSize = None

    @property
    def StartTime(self):
        """日志包起始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """日志包结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LogPath(self):
        """日志包下载链接
        :rtype: str
        """
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath

    @property
    def Area(self):
        """日志包对应加速区域
mainland：境内
overseas：境外
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LogName(self):
        """日志包文件名
        :rtype: str
        """
        return self._LogName

    @LogName.setter
    def LogName(self, LogName):
        self._LogName = LogName

    @property
    def FileSize(self):
        """文件大小，单位: Byte
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FileSize

    @FileSize.setter
    def FileSize(self, FileSize):
        self._FileSize = FileSize


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._LogPath = params.get("LogPath")
        self._Area = params.get("Area")
        self._LogName = params.get("LogName")
        self._FileSize = params.get("FileSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownstreamCapping(AbstractModel):
    """单链接下行限速配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 下行速度配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _CappingRules: 下行限速规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CappingRules: list of CappingRule
        """
        self._Switch = None
        self._CappingRules = None

    @property
    def Switch(self):
        """下行速度配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CappingRules(self):
        """下行限速规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CappingRule
        """
        return self._CappingRules

    @CappingRules.setter
    def CappingRules(self, CappingRules):
        self._CappingRules = CappingRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CappingRules") is not None:
            self._CappingRules = []
            for item in params.get("CappingRules"):
                obj = CappingRule()
                obj._deserialize(item)
                self._CappingRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateDomainConfigRequest(AbstractModel):
    """DuplicateDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 新增域名
        :type Domain: str
        :param _ReferenceDomain: 被拷贝配置的域名
        :type ReferenceDomain: str
        """
        self._Domain = None
        self._ReferenceDomain = None

    @property
    def Domain(self):
        """新增域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ReferenceDomain(self):
        """被拷贝配置的域名
        :rtype: str
        """
        return self._ReferenceDomain

    @ReferenceDomain.setter
    def ReferenceDomain(self, ReferenceDomain):
        self._ReferenceDomain = ReferenceDomain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ReferenceDomain = params.get("ReferenceDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateDomainConfigResponse(AbstractModel):
    """DuplicateDomainConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class EdgePackTaskFilter(AbstractModel):
    """动态打包任务过滤器

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名
apk: apk名称
status: 母包处理进度 done, failed, processing
        :type Name: str
        :param _Value: 过滤字段值
        :type Value: list of str
        :param _Fuzzy: 是否启用模糊查询，仅支持过滤字段名为 apk。
模糊查询时，Value长度最大为1。
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        """过滤字段名
apk: apk名称
status: 母包处理进度 done, failed, processing
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """过滤字段值
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
        """是否启用模糊查询，仅支持过滤字段名为 apk。
模糊查询时，Value长度最大为1。
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EdgePackTaskStatus(AbstractModel):
    """动态打包任务状态

    """

    def __init__(self):
        r"""
        :param _Apk: APK 名称
        :type Apk: str
        :param _DstDir: 输出目录
        :type DstDir: str
        :param _UploadTime: 上传时间
        :type UploadTime: str
        :param _Status: 任务状态
created: 创建成功
processing: 处理中
done: 处理完成
failed: 处理失败
        :type Status: str
        :param _SrcDir: 上传目录
        :type SrcDir: list of str
        :param _StatusDesc: 失败任务状态详情
        :type StatusDesc: str
        """
        self._Apk = None
        self._DstDir = None
        self._UploadTime = None
        self._Status = None
        self._SrcDir = None
        self._StatusDesc = None

    @property
    def Apk(self):
        """APK 名称
        :rtype: str
        """
        return self._Apk

    @Apk.setter
    def Apk(self, Apk):
        self._Apk = Apk

    @property
    def DstDir(self):
        """输出目录
        :rtype: str
        """
        return self._DstDir

    @DstDir.setter
    def DstDir(self, DstDir):
        self._DstDir = DstDir

    @property
    def UploadTime(self):
        """上传时间
        :rtype: str
        """
        return self._UploadTime

    @UploadTime.setter
    def UploadTime(self, UploadTime):
        self._UploadTime = UploadTime

    @property
    def Status(self):
        """任务状态
created: 创建成功
processing: 处理中
done: 处理完成
failed: 处理失败
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def SrcDir(self):
        """上传目录
        :rtype: list of str
        """
        return self._SrcDir

    @SrcDir.setter
    def SrcDir(self, SrcDir):
        self._SrcDir = SrcDir

    @property
    def StatusDesc(self):
        """失败任务状态详情
        :rtype: str
        """
        return self._StatusDesc

    @StatusDesc.setter
    def StatusDesc(self, StatusDesc):
        self._StatusDesc = StatusDesc


    def _deserialize(self, params):
        self._Apk = params.get("Apk")
        self._DstDir = params.get("DstDir")
        self._UploadTime = params.get("UploadTime")
        self._Status = params.get("Status")
        self._SrcDir = params.get("SrcDir")
        self._StatusDesc = params.get("StatusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesRequest(AbstractModel):
    """EnableCaches请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: 解封 URL 列表
        :type Urls: list of str
        :param _Date: URL封禁日期
        :type Date: str
        """
        self._Urls = None
        self._Date = None

    @property
    def Urls(self):
        """解封 URL 列表
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Date(self):
        """URL封禁日期
        :rtype: str
        """
        return self._Date

    @Date.setter
    def Date(self, Date):
        self._Date = Date


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesResponse(AbstractModel):
    """EnableCaches返回参数结构体

    """

    def __init__(self):
        r"""
        :param _CacheOptResult: 结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param _TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._CacheOptResult = None
        self._TaskId = None
        self._RequestId = None

    @property
    def CacheOptResult(self):
        """结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        """
        return self._CacheOptResult

    @CacheOptResult.setter
    def CacheOptResult(self, CacheOptResult):
        self._CacheOptResult = CacheOptResult

    @property
    def TaskId(self):
        """任务ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self._CacheOptResult = CacheOptResult()
            self._CacheOptResult._deserialize(params.get("CacheOptResult"))
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class EnableClsLogTopicRequest(AbstractModel):
    """EnableClsLogTopic请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClsLogTopicResponse(AbstractModel):
    """EnableClsLogTopic返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ErrorPage(AbstractModel):
    """状态码重定向配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 状态码重定向配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _PageRules: 状态码重定向规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PageRules: list of ErrorPageRule
        """
        self._Switch = None
        self._PageRules = None

    @property
    def Switch(self):
        """状态码重定向配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PageRules(self):
        """状态码重定向规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ErrorPageRule
        """
        return self._PageRules

    @PageRules.setter
    def PageRules(self, PageRules):
        self._PageRules = PageRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("PageRules") is not None:
            self._PageRules = []
            for item in params.get("PageRules"):
                obj = ErrorPageRule()
                obj._deserialize(item)
                self._PageRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorPageRule(AbstractModel):
    """状态码重定向规则配置

    """

    def __init__(self):
        r"""
        :param _StatusCode: 状态码
支持 400、403、404、500
        :type StatusCode: int
        :param _RedirectCode: 重定向状态码设置
支持 301 或 302
        :type RedirectCode: int
        :param _RedirectUrl: 重定向 URL
需要为完整跳转路径，如 https://www.test.com/error.html
        :type RedirectUrl: str
        """
        self._StatusCode = None
        self._RedirectCode = None
        self._RedirectUrl = None

    @property
    def StatusCode(self):
        """状态码
支持 400、403、404、500
        :rtype: int
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def RedirectCode(self):
        """重定向状态码设置
支持 301 或 302
        :rtype: int
        """
        return self._RedirectCode

    @RedirectCode.setter
    def RedirectCode(self, RedirectCode):
        self._RedirectCode = RedirectCode

    @property
    def RedirectUrl(self):
        """重定向 URL
需要为完整跳转路径，如 https://www.test.com/error.html
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._StatusCode = params.get("StatusCode")
        self._RedirectCode = params.get("RedirectCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EventLogStatsData(AbstractModel):
    """事件日志统计数据结果

    """

    def __init__(self):
        r"""
        :param _Datetime: 时间
        :type Datetime: str
        :param _Request: 请求数
        :type Request: int
        """
        self._Datetime = None
        self._Request = None

    @property
    def Datetime(self):
        """时间
        :rtype: str
        """
        return self._Datetime

    @Datetime.setter
    def Datetime(self, Datetime):
        self._Datetime = Datetime

    @property
    def Request(self):
        """请求数
        :rtype: int
        """
        return self._Request

    @Request.setter
    def Request(self, Request):
        self._Request = Request


    def _deserialize(self, params):
        self._Datetime = params.get("Datetime")
        self._Request = params.get("Request")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ExtraLogset(AbstractModel):
    """除上海外其他区域日志集和日志主题信息

    """

    def __init__(self):
        r"""
        :param _Logset: 日志集信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        :param _Topics: 日志主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: list of TopicInfo
        """
        self._Logset = None
        self._Topics = None

    @property
    def Logset(self):
        """日志集信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        """
        return self._Logset

    @Logset.setter
    def Logset(self, Logset):
        self._Logset = Logset

    @property
    def Topics(self):
        """日志主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TopicInfo
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self._Logset = LogSetInfo()
            self._Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowRedirect(AbstractModel):
    """回源 301/302 状态码自动跟随配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 回源跟随配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _RedirectConfig: 自定义回源302 follow请求host配置，该功能为白名单功能，需要开启请联系腾讯云工程师。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectConfig: :class:`tencentcloud.cdn.v20180606.models.RedirectConfig`
        """
        self._Switch = None
        self._RedirectConfig = None

    @property
    def Switch(self):
        """回源跟随配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectConfig(self):
        """自定义回源302 follow请求host配置，该功能为白名单功能，需要开启请联系腾讯云工程师。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RedirectConfig`
        """
        return self._RedirectConfig

    @RedirectConfig.setter
    def RedirectConfig(self, RedirectConfig):
        self._RedirectConfig = RedirectConfig


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RedirectConfig") is not None:
            self._RedirectConfig = RedirectConfig()
            self._RedirectConfig._deserialize(params.get("RedirectConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """访问协议强制跳转配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 访问强制跳转配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _RedirectType: 访问强制跳转类型
http：强制 http 跳转
https：强制 https 跳转
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectType: str
        :param _RedirectStatusCode: 强制跳转时返回状态码 
支持 301、302、307、308
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        :param _CarryHeaders: 强制跳转时是否返回增加的头部。
注意：此字段可能返回 null，表示取不到有效值。
        :type CarryHeaders: str
        """
        self._Switch = None
        self._RedirectType = None
        self._RedirectStatusCode = None
        self._CarryHeaders = None

    @property
    def Switch(self):
        """访问强制跳转配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectType(self):
        """访问强制跳转类型
http：强制 http 跳转
https：强制 https 跳转
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RedirectType

    @RedirectType.setter
    def RedirectType(self, RedirectType):
        self._RedirectType = RedirectType

    @property
    def RedirectStatusCode(self):
        """强制跳转时返回状态码 
支持 301、302、307、308
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode

    @property
    def CarryHeaders(self):
        """强制跳转时是否返回增加的头部。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CarryHeaders

    @CarryHeaders.setter
    def CarryHeaders(self, CarryHeaders):
        self._CarryHeaders = CarryHeaders


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectType = params.get("RedirectType")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        self._CarryHeaders = params.get("CarryHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Url: 指定 URL 查询
        :type Url: str
        :param _StartTime: 开始时间，如：2018-12-12 10:24:00。
        :type StartTime: str
        :param _EndTime: 结束时间，如：2018-12-14 10:24:00。
        :type EndTime: str
        :param _Status: URL 当前状态
disable：当前仍为禁用状态，访问返回 403
enable：当前为可用状态，已解禁，可正常访问
        :type Status: str
        :param _Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为20。
        :type Limit: int
        :param _TaskId: 任务ID，任务ID和起始时间需要至少填写一项。
        :type TaskId: str
        """
        self._Url = None
        self._StartTime = None
        self._EndTime = None
        self._Status = None
        self._Offset = None
        self._Limit = None
        self._TaskId = None

    @property
    def Url(self):
        """指定 URL 查询
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def StartTime(self):
        """开始时间，如：2018-12-12 10:24:00。
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间，如：2018-12-14 10:24:00。
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Status(self):
        """URL 当前状态
disable：当前仍为禁用状态，访问返回 403
enable：当前为可用状态，已解禁，可正常访问
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Offset(self):
        """分页查询偏移量，默认为 0
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """分页查询限制数目，默认为20。
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def TaskId(self):
        """任务ID，任务ID和起始时间需要至少填写一项。
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Status = params.get("Status")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UrlRecordList: 封禁历史记录
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of UrlRecord
        :param _TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UrlRecordList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def UrlRecordList(self):
        """封禁历史记录
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UrlRecord
        """
        return self._UrlRecordList

    @UrlRecordList.setter
    def UrlRecordList(self, UrlRecordList):
        self._UrlRecordList = UrlRecordList

    @property
    def TotalCount(self):
        """任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self._UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self._UrlRecordList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class GuetzliAdapter(AbstractModel):
    """图片优化-GuetzliAdapter配置

    """

    def __init__(self):
        r"""
        :param _Switch: 图片优化-GuetzliAdapter配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """图片优化-GuetzliAdapter配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPHeader(AbstractModel):
    """HTTP 请求头

    """

    def __init__(self):
        r"""
        :param _Name: 请求头名称
        :type Name: str
        :param _Value: 请求头值
        :type Value: str
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """请求头名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """请求头值
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeaderKey(AbstractModel):
    """组成CacheKey

    """

    def __init__(self):
        r"""
        :param _Switch: 组成Cachekey配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Value: 组成CacheKey的header数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Switch = None
        self._Value = None

    @property
    def Switch(self):
        """组成Cachekey配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Value(self):
        """组成CacheKey的header数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeuristicCache(AbstractModel):
    """启发式缓存配置

    """

    def __init__(self):
        r"""
        :param _Switch: 启发式缓存配置开关，取值有：
on：开启
off：关闭（默认）
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _CacheConfig: 自定义启发式缓存时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.CacheConfig`
        """
        self._Switch = None
        self._CacheConfig = None

    @property
    def Switch(self):
        """启发式缓存配置开关，取值有：
on：开启
off：关闭（默认）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheConfig(self):
        """自定义启发式缓存时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheConfig`
        """
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CacheConfig") is not None:
            self._CacheConfig = CacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS 配置。

    """

    def __init__(self):
        r"""
        :param _Switch: HSTS 配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _MaxAge: MaxAge数值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param _IncludeSubDomains: 是否包含子域名，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        """
        self._Switch = None
        self._MaxAge = None
        self._IncludeSubDomains = None

    @property
    def Switch(self):
        """HSTS 配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        """MaxAge数值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
        """是否包含子域名，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IncludeSubDomains

    @IncludeSubDomains.setter
    def IncludeSubDomains(self, IncludeSubDomains):
        self._IncludeSubDomains = IncludeSubDomains


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxAge = params.get("MaxAge")
        self._IncludeSubDomains = params.get("IncludeSubDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderPathRule(AbstractModel):
    """Http 头部设置规则，最多可设置 100 条

    """

    def __init__(self):
        r"""
        :param _HeaderMode: http 头部设置方式
set：设置。变更指定头部参数的取值为设置后的值；若设置的头部不存在，则会增加该头部；若存在多个重复的头部参数，则会全部变更，同时合并为一个头部。
del：删除。删除指定的头部参数
add：增加。增加指定的头部参数，默认允许重复添加，即重复添加相同的头部（注：重复添加可能会影响浏览器响应，请优先使用set操作）
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderMode: str
        :param _HeaderName: http 头部名称，最多可设置 100 个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        :param _HeaderValue: http 头部值，最多可设置 1000 个字符
Mode 为 del 时非必填
Mode 为 add/set 时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderValue: str
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self._HeaderMode = None
        self._HeaderName = None
        self._HeaderValue = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def HeaderMode(self):
        """http 头部设置方式
set：设置。变更指定头部参数的取值为设置后的值；若设置的头部不存在，则会增加该头部；若存在多个重复的头部参数，则会全部变更，同时合并为一个头部。
del：删除。删除指定的头部参数
add：增加。增加指定的头部参数，默认允许重复添加，即重复添加相同的头部（注：重复添加可能会影响浏览器响应，请优先使用set操作）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HeaderMode

    @HeaderMode.setter
    def HeaderMode(self, HeaderMode):
        self._HeaderMode = HeaderMode

    @property
    def HeaderName(self):
        """http 头部名称，最多可设置 100 个字符
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        """http 头部值，最多可设置 1000 个字符
Mode 为 del 时非必填
Mode 为 add/set 时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._HeaderMode = params.get("HeaderMode")
        self._HeaderName = params.get("HeaderName")
        self._HeaderValue = params.get("HeaderValue")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderRule(AbstractModel):
    """http头部设置规则。

    """

    def __init__(self):
        r"""
        :param _HeaderMode: http头部设置方式，支持add，set或del，分别表示新增，设置或删除头部。
        :type HeaderMode: str
        :param _HeaderName: http头部名称。
        :type HeaderName: str
        :param _HeaderValue: http头部值。
        :type HeaderValue: str
        """
        self._HeaderMode = None
        self._HeaderName = None
        self._HeaderValue = None

    @property
    def HeaderMode(self):
        """http头部设置方式，支持add，set或del，分别表示新增，设置或删除头部。
        :rtype: str
        """
        return self._HeaderMode

    @HeaderMode.setter
    def HeaderMode(self, HeaderMode):
        self._HeaderMode = HeaderMode

    @property
    def HeaderName(self):
        """http头部名称。
        :rtype: str
        """
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        """http头部值。
        :rtype: str
        """
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue


    def _deserialize(self, params):
        self._HeaderMode = params.get("HeaderMode")
        self._HeaderName = params.get("HeaderName")
        self._HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """域名 https 加速配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: https 配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Http2: http2 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param _OcspStapling: OCSP 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param _VerifyClient: 客户端证书校验功能
on：开启
off：关闭
默认为关闭状态，开启时需要上传客户端证书信息，该配置项目前在灰度中，尚未全量
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyClient: str
        :param _CertInfo: 服务端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param _ClientCertInfo: 客户端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        :param _Spdy: Spdy 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Spdy: str
        :param _SslStatus: https 证书部署状态
closed：已关闭
deploying：部署中
deployed：部署成功
failed：部署失败
注意：此字段可能返回 null，表示取不到有效值。
        :type SslStatus: str
        :param _Hsts: Hsts配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.cdn.v20180606.models.Hsts`
        :param _TlsVersion: Tls版本设置，仅支持部分Advance域名，支持设置 TLSv1, TLSv1.1, TLSv1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        """
        self._Switch = None
        self._Http2 = None
        self._OcspStapling = None
        self._VerifyClient = None
        self._CertInfo = None
        self._ClientCertInfo = None
        self._Spdy = None
        self._SslStatus = None
        self._Hsts = None
        self._TlsVersion = None

    @property
    def Switch(self):
        """https 配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Http2(self):
        """http2 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        """OCSP 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def VerifyClient(self):
        """客户端证书校验功能
on：开启
off：关闭
默认为关闭状态，开启时需要上传客户端证书信息，该配置项目前在灰度中，尚未全量
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._VerifyClient

    @VerifyClient.setter
    def VerifyClient(self, VerifyClient):
        self._VerifyClient = VerifyClient

    @property
    def CertInfo(self):
        """服务端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        """
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def ClientCertInfo(self):
        """客户端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        """
        return self._ClientCertInfo

    @ClientCertInfo.setter
    def ClientCertInfo(self, ClientCertInfo):
        self._ClientCertInfo = ClientCertInfo

    @property
    def Spdy(self):
        """Spdy 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Spdy

    @Spdy.setter
    def Spdy(self, Spdy):
        self._Spdy = Spdy

    @property
    def SslStatus(self):
        """https 证书部署状态
closed：已关闭
deploying：部署中
deployed：部署成功
failed：部署失败
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SslStatus

    @SslStatus.setter
    def SslStatus(self, SslStatus):
        self._SslStatus = SslStatus

    @property
    def Hsts(self):
        """Hsts配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Hsts`
        """
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts

    @property
    def TlsVersion(self):
        """Tls版本设置，仅支持部分Advance域名，支持设置 TLSv1, TLSv1.1, TLSv1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Http2 = params.get("Http2")
        self._OcspStapling = params.get("OcspStapling")
        self._VerifyClient = params.get("VerifyClient")
        if params.get("CertInfo") is not None:
            self._CertInfo = ServerCert()
            self._CertInfo._deserialize(params.get("CertInfo"))
        if params.get("ClientCertInfo") is not None:
            self._ClientCertInfo = ClientCert()
            self._ClientCertInfo._deserialize(params.get("ClientCertInfo"))
        self._Spdy = params.get("Spdy")
        self._SslStatus = params.get("SslStatus")
        if params.get("Hsts") is not None:
            self._Hsts = Hsts()
            self._Hsts._deserialize(params.get("Hsts"))
        self._TlsVersion = params.get("TlsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpsBilling(AbstractModel):
    """HTTPS服务，若关闭，下发配置拦截https请求，开启时会产生计费

    """

    def __init__(self):
        r"""
        :param _Switch: HTTPS服务配置开关，取值有：
on：开启，缺省时默认开启，会产生计费
off：关闭，拦截https请求

        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """HTTPS服务配置开关，取值有：
on：开启，缺省时默认开启，会产生计费
off：关闭，拦截https请求

        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpsPackage(AbstractModel):
    """CDN HTTPS请求包。

    """

    def __init__(self):
        r"""
        :param _Id: HTTPS请求包 Id
        :type Id: int
        :param _Type: HTTPS请求包类型
        :type Type: str
        :param _Size: HTTPS请求包大小（单位为：次）
        :type Size: int
        :param _SizeUsed: 已消耗HTTPS请求包（单位为：次）
        :type SizeUsed: int
        :param _Status: HTTPS请求包状态
enabled：已启用
expired：已过期
disabled：未启用
        :type Status: str
        :param _CreateTime: HTTPS请求包发放时间
        :type CreateTime: str
        :param _EnableTime: HTTPS请求包生效时间
        :type EnableTime: str
        :param _ExpireTime: HTTPS请求包过期时间
        :type ExpireTime: str
        :param _Channel: HTTPS请求包来源
        :type Channel: str
        :param _LifeTimeMonth: HTTPS请求包生命周期月数
        :type LifeTimeMonth: int
        :param _RefundAvailable: HTTPS请求包是否支持退费
        :type RefundAvailable: bool
        :param _ConfigId: HTTPS请求包类型id
        :type ConfigId: int
        :param _TrueEnableTime: HTTPS请求包实际生效时间
        :type TrueEnableTime: str
        :param _TrueExpireTime: HTTPS请求包实际过期时间
        :type TrueExpireTime: str
        :param _Area: HTTPS请求包生效区域 
global：全球
        :type Area: str
        :param _ContractExtension: HTTPS请求包是否续订
        :type ContractExtension: bool
        :param _ExtensionAvailable: HTTPS请求包是否支持续订
        :type ExtensionAvailable: bool
        :param _ExtensionMode: HTTPS请求包当前续订模式
0：未续订
1：到期续订
2：用完续订
3：到期或用完续订
        :type ExtensionMode: int
        :param _AutoExtension: HTTPS请求包是否自动续订
注意：此字段可能返回 null，表示取不到有效值。
        :type AutoExtension: bool
        """
        self._Id = None
        self._Type = None
        self._Size = None
        self._SizeUsed = None
        self._Status = None
        self._CreateTime = None
        self._EnableTime = None
        self._ExpireTime = None
        self._Channel = None
        self._LifeTimeMonth = None
        self._RefundAvailable = None
        self._ConfigId = None
        self._TrueEnableTime = None
        self._TrueExpireTime = None
        self._Area = None
        self._ContractExtension = None
        self._ExtensionAvailable = None
        self._ExtensionMode = None
        self._AutoExtension = None

    @property
    def Id(self):
        """HTTPS请求包 Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """HTTPS请求包类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Size(self):
        """HTTPS请求包大小（单位为：次）
        :rtype: int
        """
        return self._Size

    @Size.setter
    def Size(self, Size):
        self._Size = Size

    @property
    def SizeUsed(self):
        """已消耗HTTPS请求包（单位为：次）
        :rtype: int
        """
        return self._SizeUsed

    @SizeUsed.setter
    def SizeUsed(self, SizeUsed):
        self._SizeUsed = SizeUsed

    @property
    def Status(self):
        """HTTPS请求包状态
enabled：已启用
expired：已过期
disabled：未启用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """HTTPS请求包发放时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableTime(self):
        """HTTPS请求包生效时间
        :rtype: str
        """
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime

    @property
    def ExpireTime(self):
        """HTTPS请求包过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def Channel(self):
        """HTTPS请求包来源
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def LifeTimeMonth(self):
        """HTTPS请求包生命周期月数
        :rtype: int
        """
        return self._LifeTimeMonth

    @LifeTimeMonth.setter
    def LifeTimeMonth(self, LifeTimeMonth):
        self._LifeTimeMonth = LifeTimeMonth

    @property
    def RefundAvailable(self):
        """HTTPS请求包是否支持退费
        :rtype: bool
        """
        return self._RefundAvailable

    @RefundAvailable.setter
    def RefundAvailable(self, RefundAvailable):
        self._RefundAvailable = RefundAvailable

    @property
    def ConfigId(self):
        """HTTPS请求包类型id
        :rtype: int
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def TrueEnableTime(self):
        """HTTPS请求包实际生效时间
        :rtype: str
        """
        return self._TrueEnableTime

    @TrueEnableTime.setter
    def TrueEnableTime(self, TrueEnableTime):
        self._TrueEnableTime = TrueEnableTime

    @property
    def TrueExpireTime(self):
        """HTTPS请求包实际过期时间
        :rtype: str
        """
        return self._TrueExpireTime

    @TrueExpireTime.setter
    def TrueExpireTime(self, TrueExpireTime):
        self._TrueExpireTime = TrueExpireTime

    @property
    def Area(self):
        """HTTPS请求包生效区域 
global：全球
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ContractExtension(self):
        """HTTPS请求包是否续订
        :rtype: bool
        """
        return self._ContractExtension

    @ContractExtension.setter
    def ContractExtension(self, ContractExtension):
        self._ContractExtension = ContractExtension

    @property
    def ExtensionAvailable(self):
        """HTTPS请求包是否支持续订
        :rtype: bool
        """
        return self._ExtensionAvailable

    @ExtensionAvailable.setter
    def ExtensionAvailable(self, ExtensionAvailable):
        self._ExtensionAvailable = ExtensionAvailable

    @property
    def ExtensionMode(self):
        """HTTPS请求包当前续订模式
0：未续订
1：到期续订
2：用完续订
3：到期或用完续订
        :rtype: int
        """
        return self._ExtensionMode

    @ExtensionMode.setter
    def ExtensionMode(self, ExtensionMode):
        self._ExtensionMode = ExtensionMode

    @property
    def AutoExtension(self):
        """HTTPS请求包是否自动续订
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._AutoExtension

    @AutoExtension.setter
    def AutoExtension(self, AutoExtension):
        self._AutoExtension = AutoExtension


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Size = params.get("Size")
        self._SizeUsed = params.get("SizeUsed")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._EnableTime = params.get("EnableTime")
        self._ExpireTime = params.get("ExpireTime")
        self._Channel = params.get("Channel")
        self._LifeTimeMonth = params.get("LifeTimeMonth")
        self._RefundAvailable = params.get("RefundAvailable")
        self._ConfigId = params.get("ConfigId")
        self._TrueEnableTime = params.get("TrueEnableTime")
        self._TrueExpireTime = params.get("TrueExpireTime")
        self._Area = params.get("Area")
        self._ContractExtension = params.get("ContractExtension")
        self._ExtensionAvailable = params.get("ExtensionAvailable")
        self._ExtensionMode = params.get("ExtensionMode")
        self._AutoExtension = params.get("AutoExtension")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HwPrivateAccess(AbstractModel):
    """华为云对象存储回源鉴权

    """

    def __init__(self):
        r"""
        :param _Switch:  华为云对象存储回源鉴权配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _AccessKey: 访问 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _SecretKey: 密钥，字段为脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Bucket: bucketname
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Bucket = None

    @property
    def Switch(self):
        """ 华为云对象存储回源鉴权配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        """访问 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """密钥，字段为脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Bucket(self):
        """bucketname
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOptimization(AbstractModel):
    """ImageOptimization配置

    """

    def __init__(self):
        r"""
        :param _WebpAdapter: WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param _TpgAdapter: TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param _GuetzliAdapter: GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        :param _AvifAdapter: AvifAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AvifAdapter: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        """
        self._WebpAdapter = None
        self._TpgAdapter = None
        self._GuetzliAdapter = None
        self._AvifAdapter = None

    @property
    def WebpAdapter(self):
        """WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        """
        return self._WebpAdapter

    @WebpAdapter.setter
    def WebpAdapter(self, WebpAdapter):
        self._WebpAdapter = WebpAdapter

    @property
    def TpgAdapter(self):
        """TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        """
        return self._TpgAdapter

    @TpgAdapter.setter
    def TpgAdapter(self, TpgAdapter):
        self._TpgAdapter = TpgAdapter

    @property
    def GuetzliAdapter(self):
        """GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        return self._GuetzliAdapter

    @GuetzliAdapter.setter
    def GuetzliAdapter(self, GuetzliAdapter):
        self._GuetzliAdapter = GuetzliAdapter

    @property
    def AvifAdapter(self):
        """AvifAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        """
        return self._AvifAdapter

    @AvifAdapter.setter
    def AvifAdapter(self, AvifAdapter):
        self._AvifAdapter = AvifAdapter


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self._WebpAdapter = WebpAdapter()
            self._WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self._TpgAdapter = TpgAdapter()
            self._TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self._GuetzliAdapter = GuetzliAdapter()
            self._GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        if params.get("AvifAdapter") is not None:
            self._AvifAdapter = AvifAdapter()
            self._AvifAdapter._deserialize(params.get("AvifAdapter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP 黑白名单配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: IP 黑白名单配置开关，取值有
on：开启
off：关闭
        :type Switch: str
        :param _FilterType: IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param _Filters: IP 黑白名单列表
支持 X.X.X.X 格式IPV4地址 或X:X:X:X:X:X:X:X 格式IPV6地址， 或网段格式/X（IPV4:1≤X≤32；IPV6:1≤X≤128）
最多可填充 200 个白名单或 200 个黑名单；
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of str
        :param _FilterRules: IP 黑白名单分路径配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of IpFilterPathRule
        :param _ReturnCode: IP 黑白名单验证失败时返回的 code <br><font color=red>已下线，参数失效，不支持自定义状态码，固定返回514</font>
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        """
        self._Switch = None
        self._FilterType = None
        self._Filters = None
        self._FilterRules = None
        self._ReturnCode = None

    @property
    def Switch(self):
        """IP 黑白名单配置开关，取值有
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterType(self):
        """IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filters(self):
        """IP 黑白名单列表
支持 X.X.X.X 格式IPV4地址 或X:X:X:X:X:X:X:X 格式IPV6地址， 或网段格式/X（IPV4:1≤X≤32；IPV6:1≤X≤128）
最多可填充 200 个白名单或 200 个黑名单；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FilterRules(self):
        """IP 黑白名单分路径配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of IpFilterPathRule
        """
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules

    @property
    def ReturnCode(self):
        """IP 黑白名单验证失败时返回的 code <br><font color=red>已下线，参数失效，不支持自定义状态码，固定返回514</font>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FilterType = params.get("FilterType")
        self._Filters = params.get("Filters")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = IpFilterPathRule()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        self._ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilterPathRule(AbstractModel):
    """IP黑白名单分路径配置

    """

    def __init__(self):
        r"""
        :param _FilterType: IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param _Filters: IP 黑白名单列表
支持 X.X.X.X 格式IPV4地址 或X:X:X:X:X:X:X:X 格式IPV6地址， 或网段格式/X（IPV4:1≤X≤32；IPV6:1≤X≤128）
最多可填充 200 个白名单或 500 个黑名单；
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of str
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self._FilterType = None
        self._Filters = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def FilterType(self):
        """IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filters(self):
        """IP 黑白名单列表
支持 X.X.X.X 格式IPV4地址 或X:X:X:X:X:X:X:X 格式IPV6地址， 或网段格式/X（IPV4:1≤X≤32；IPV6:1≤X≤128）
最多可填充 200 个白名单或 500 个黑名单；
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._FilterType = params.get("FilterType")
        self._Filters = params.get("Filters")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """单节点单 IP 访问限频配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: IP 限频配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _Qps: 设置每秒请求数限制
超出限制的请求会直接返回 514
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        """
        self._Switch = None
        self._Qps = None

    @property
    def Switch(self):
        """IP 限频配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Qps(self):
        """设置每秒请求数限制
超出限制的请求会直接返回 514
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Qps = params.get("Qps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatus(AbstractModel):
    """节点 IP 信息

    """

    def __init__(self):
        r"""
        :param _Ip: 节点 IP
        :type Ip: str
        :param _District: 节点所属区域
        :type District: str
        :param _Isp: 节点所属运营商
        :type Isp: str
        :param _City: 节点所在城市
        :type City: str
        :param _Status: 节点状态
online：上线状态，正常调度服务中
offline：下线状态
        :type Status: str
        :param _Ipv6: 节点 IPV6
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: str
        """
        self._Ip = None
        self._District = None
        self._Isp = None
        self._City = None
        self._Status = None
        self._Ipv6 = None

    @property
    def Ip(self):
        """节点 IP
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def District(self):
        """节点所属区域
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Isp(self):
        """节点所属运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def City(self):
        """节点所在城市
        :rtype: str
        """
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Status(self):
        """节点状态
online：上线状态，正常调度服务中
offline：下线状态
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Ipv6(self):
        """节点 IPV6
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Ipv6

    @Ipv6.setter
    def Ipv6(self, Ipv6):
        self._Ipv6 = Ipv6


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._District = params.get("District")
        self._Isp = params.get("Isp")
        self._City = params.get("City")
        self._Status = params.get("Status")
        self._Ipv6 = params.get("Ipv6")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """Ipv6源站启用配置，不可更改

    """

    def __init__(self):
        r"""
        :param _Switch: 域名开启源站ipv6配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """域名开启源站ipv6配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Access(AbstractModel):
    """Ipv6访问配置

    """

    def __init__(self):
        r"""
        :param _Switch: 域名开启ipv6访问配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """域名开启ipv6访问配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class KeyRule(AbstractModel):
    """缓存键分路径配置

    """

    def __init__(self):
        r"""
        :param _RulePaths: CacheType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        :param _RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数忽略）
off：关闭全路径缓存（即开启参数忽略）
注意：此字段可能返回 null，表示取不到有效值。
        :type FullUrlCache: str
        :param _IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param _QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.RuleQueryString`
        :param _RuleTag: 路径缓存键标签，传 user
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTag: str
        """
        self._RulePaths = None
        self._RuleType = None
        self._FullUrlCache = None
        self._IgnoreCase = None
        self._QueryString = None
        self._RuleTag = None

    @property
    def RulePaths(self):
        """CacheType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def RuleType(self):
        """规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def FullUrlCache(self):
        """是否开启全路径缓存
on：开启全路径缓存（即关闭参数忽略）
off：关闭全路径缓存（即开启参数忽略）
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache

    @property
    def IgnoreCase(self):
        """是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreCase

    @IgnoreCase.setter
    def IgnoreCase(self, IgnoreCase):
        self._IgnoreCase = IgnoreCase

    @property
    def QueryString(self):
        """CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RuleQueryString`
        """
        return self._QueryString

    @QueryString.setter
    def QueryString(self, QueryString):
        self._QueryString = QueryString

    @property
    def RuleTag(self):
        """路径缓存键标签，传 user
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleTag

    @RuleTag.setter
    def RuleTag(self, RuleTag):
        self._RuleTag = RuleTag


    def _deserialize(self, params):
        self._RulePaths = params.get("RulePaths")
        self._RuleType = params.get("RuleType")
        self._FullUrlCache = params.get("FullUrlCache")
        self._IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self._QueryString = RuleQueryString()
            self._QueryString._deserialize(params.get("QueryString"))
        self._RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsRequest(AbstractModel):
    """ListClsLogTopics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        """
        self._Channel = None

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsResponse(AbstractModel):
    """ListClsLogTopics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Logset: 上海区域日志集信息
        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        :param _Topics: 上海区域日志主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: list of TopicInfo
        :param _ExtraLogset: 其他区域日志集信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtraLogset: list of ExtraLogset
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Logset = None
        self._Topics = None
        self._ExtraLogset = None
        self._RequestId = None

    @property
    def Logset(self):
        """上海区域日志集信息
        :rtype: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        """
        return self._Logset

    @Logset.setter
    def Logset(self, Logset):
        self._Logset = Logset

    @property
    def Topics(self):
        """上海区域日志主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of TopicInfo
        """
        return self._Topics

    @Topics.setter
    def Topics(self, Topics):
        self._Topics = Topics

    @property
    def ExtraLogset(self):
        """其他区域日志集信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ExtraLogset
        """
        return self._ExtraLogset

    @ExtraLogset.setter
    def ExtraLogset(self, ExtraLogset):
        self._ExtraLogset = ExtraLogset

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self._Logset = LogSetInfo()
            self._Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self._Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self._Topics.append(obj)
        if params.get("ExtraLogset") is not None:
            self._ExtraLogset = []
            for item in params.get("ExtraLogset"):
                obj = ExtraLogset()
                obj._deserialize(item)
                self._ExtraLogset.append(obj)
        self._RequestId = params.get("RequestId")


class ListClsTopicDomainsRequest(AbstractModel):
    """ListClsTopicDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsTopicDomainsResponse(AbstractModel):
    """ListClsTopicDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _AppId: 开发者ID
        :type AppId: int
        :param _Channel: 渠道
        :type Channel: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _DomainAreaConfigs: 域名区域配置，其中可能含有已删除的域名，如果要再传回ManageClsTopicDomains接口，需要结合ListCdnDomains接口排除掉已删除的域名
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param _TopicName: 日志主题名称
        :type TopicName: str
        :param _UpdateTime: 日志主题最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._AppId = None
        self._Channel = None
        self._LogsetId = None
        self._TopicId = None
        self._DomainAreaConfigs = None
        self._TopicName = None
        self._UpdateTime = None
        self._RequestId = None

    @property
    def AppId(self):
        """开发者ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Channel(self):
        """渠道
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def DomainAreaConfigs(self):
        """域名区域配置，其中可能含有已删除的域名，如果要再传回ManageClsTopicDomains接口，需要结合ListCdnDomains接口排除掉已删除的域名
        :rtype: list of DomainAreaConfig
        """
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs

    @property
    def TopicName(self):
        """日志主题名称
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def UpdateTime(self):
        """日志主题最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Channel = params.get("Channel")
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        self._TopicName = params.get("TopicName")
        self._UpdateTime = params.get("UpdateTime")
        self._RequestId = params.get("RequestId")


class ListDiagnoseReportRequest(AbstractModel):
    """ListDiagnoseReport请求参数结构体

    """

    def __init__(self):
        r"""
        :param _KeyWords: 用于搜索诊断URL的关键字，不填时返回用户所有的诊断任务。
        :type KeyWords: str
        :param _DiagnoseLink: 用于搜索诊断系统返回的诊断链接，形如：http://cdn.cloud.tencent.com/self_diagnose/xxxxx
        :type DiagnoseLink: str
        :param _Origin: 请求源带协议头，形如：https://console.cloud.tencent.com
        :type Origin: str
        """
        self._KeyWords = None
        self._DiagnoseLink = None
        self._Origin = None

    @property
    def KeyWords(self):
        """用于搜索诊断URL的关键字，不填时返回用户所有的诊断任务。
        :rtype: str
        """
        return self._KeyWords

    @KeyWords.setter
    def KeyWords(self, KeyWords):
        self._KeyWords = KeyWords

    @property
    def DiagnoseLink(self):
        """用于搜索诊断系统返回的诊断链接，形如：http://cdn.cloud.tencent.com/self_diagnose/xxxxx
        :rtype: str
        """
        return self._DiagnoseLink

    @DiagnoseLink.setter
    def DiagnoseLink(self, DiagnoseLink):
        self._DiagnoseLink = DiagnoseLink

    @property
    def Origin(self):
        """请求源带协议头，形如：https://console.cloud.tencent.com
        :rtype: str
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin


    def _deserialize(self, params):
        self._KeyWords = params.get("KeyWords")
        self._DiagnoseLink = params.get("DiagnoseLink")
        self._Origin = params.get("Origin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDiagnoseReportResponse(AbstractModel):
    """ListDiagnoseReport返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 诊断信息。
        :type Data: list of DiagnoseInfo
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """诊断信息。
        :rtype: list of DiagnoseInfo
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DiagnoseInfo()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListScdnDomainsRequest(AbstractModel):
    """ListScdnDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页起始地址
        :type Offset: int
        :param _Limit: 列表分页记录条数，最大1000
        :type Limit: int
        :param _Domain: 域名信息
        :type Domain: str
        """
        self._Offset = None
        self._Limit = None
        self._Domain = None

    @property
    def Offset(self):
        """分页起始地址
        :rtype: int
        """
        return self._Offset

    @Offset.setter
    def Offset(self, Offset):
        self._Offset = Offset

    @property
    def Limit(self):
        """列表分页记录条数，最大1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Domain(self):
        """域名信息
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListScdnDomainsResponse(AbstractModel):
    """ListScdnDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainList: 域名列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of ScdnDomain
        :param _TotalCount: 域名的总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainList(self):
        """域名列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnDomain
        """
        return self._DomainList

    @DomainList.setter
    def DomainList(self, DomainList):
        self._DomainList = DomainList

    @property
    def TotalCount(self):
        """域名的总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("DomainList") is not None:
            self._DomainList = []
            for item in params.get("DomainList"):
                obj = ScdnDomain()
                obj._deserialize(item)
                self._DomainList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListScdnLogTasksRequest(AbstractModel):
    """ListScdnLogTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Source: 产品来源 cdn/ecdn
        :type Source: str
        :param _Area: 地域：mainland 或 overseas 为空表示查询所有地域
        :type Area: str
        """
        self._Source = None
        self._Area = None

    @property
    def Source(self):
        """产品来源 cdn/ecdn
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Area(self):
        """地域：mainland 或 overseas 为空表示查询所有地域
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Source = params.get("Source")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListScdnLogTasksResponse(AbstractModel):
    """ListScdnLogTasks返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskList: 日志下载任务详情
        :type TaskList: list of ScdnLogTaskDetail
        :param _TotalCount: 查询到的下载任务的总数
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskList = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def TaskList(self):
        """日志下载任务详情
        :rtype: list of ScdnLogTaskDetail
        """
        return self._TaskList

    @TaskList.setter
    def TaskList(self, TaskList):
        self._TaskList = TaskList

    @property
    def TotalCount(self):
        """查询到的下载任务的总数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self._TaskList = []
            for item in params.get("TaskList"):
                obj = ScdnLogTaskDetail()
                obj._deserialize(item)
                self._TaskList.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class ListScdnTopBotDataRequest(AbstractModel):
    """ListScdnTopBotData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopCount: 获取Top量，取值范围[1-10]
        :type TopCount: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Area: mainland 大陆地区 overseas境外地区
        :type Area: str
        :param _Metric: session表示查询BOT会话的Top信息
ip表示查询BOT客户端IP的Top信息

不填代表获取会话信息
        :type Metric: str
        :param _Domains: 域名，仅当Metric=ip，并且Domain为空时有效，不填写表示获取AppID信息
        :type Domains: list of str
        """
        self._TopCount = None
        self._StartTime = None
        self._EndTime = None
        self._Area = None
        self._Metric = None
        self._Domains = None

    @property
    def TopCount(self):
        """获取Top量，取值范围[1-10]
        :rtype: int
        """
        return self._TopCount

    @TopCount.setter
    def TopCount(self, TopCount):
        self._TopCount = TopCount

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Area(self):
        """mainland 大陆地区 overseas境外地区
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Metric(self):
        """session表示查询BOT会话的Top信息
ip表示查询BOT客户端IP的Top信息

不填代表获取会话信息
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Domains(self):
        """域名，仅当Metric=ip，并且Domain为空时有效，不填写表示获取AppID信息
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._TopCount = params.get("TopCount")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Area = params.get("Area")
        self._Metric = params.get("Metric")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListScdnTopBotDataResponse(AbstractModel):
    """ListScdnTopBotData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 域名BOT次数列表
        :type Data: list of BotStatisticsCount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """域名BOT次数列表
        :rtype: list of BotStatisticsCount
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = BotStatisticsCount()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopBotDataRequest(AbstractModel):
    """ListTopBotData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _TopCount: 获取Top量，取值范围[1-10]
        :type TopCount: int
        :param _StartTime: 开始时间
        :type StartTime: str
        :param _EndTime: 结束时间
        :type EndTime: str
        :param _Metric: session表示查询BOT会话的Top信息
ip表示查询BOT客户端IP的Top信息

不填代表获取会话信息
        :type Metric: str
        :param _Domain: 域名，仅当Metric=ip时有效，不填写表示使用Domains参数
        :type Domain: str
        :param _Domains: 域名，仅当Metric=ip，并且Domain为空时有效，不填写表示获取AppID信息
        :type Domains: list of str
        """
        self._TopCount = None
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Domain = None
        self._Domains = None

    @property
    def TopCount(self):
        """获取Top量，取值范围[1-10]
        :rtype: int
        """
        return self._TopCount

    @TopCount.setter
    def TopCount(self, TopCount):
        self._TopCount = TopCount

    @property
    def StartTime(self):
        """开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """session表示查询BOT会话的Top信息
ip表示查询BOT客户端IP的Top信息

不填代表获取会话信息
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Domain(self):
        """域名，仅当Metric=ip时有效，不填写表示使用Domains参数
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Domains(self):
        """域名，仅当Metric=ip，并且Domain为空时有效，不填写表示获取AppID信息
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._TopCount = params.get("TopCount")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Domain = params.get("Domain")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopBotDataResponse(AbstractModel):
    """ListTopBotData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 域名BOT次数列表
        :type Data: list of DomainBotCount
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """域名BOT次数列表
        :rtype: list of DomainBotCount
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainBotCount()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopCcDataRequest(AbstractModel):
    """ListTopCcData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询Top数据的开始时间，格式为：2020-01-01 00:00:00
        :type StartTime: str
        :param _EndTime: 查询Top数据的结束时间，格式为：2020-01-01 23:59:59
支持 90 天内数据查询，不传此参数，表示查当天数据
时间跨度要小于等于7天
        :type EndTime: str
        :param _Domain: 域名，不传此参数，表示查询账号级别数据
        :type Domain: str
        :param _Metric: 统计指标：
ip_url : Top IP+URL 默认值
ua :  Top UA
        :type Metric: str
        :param _Source: cdn表示CDN数据，默认值
ecdn表示ECDN数据
        :type Source: str
        :param _Domains: 域名列表，不传此参数，表示查询账号级别数据
        :type Domains: list of str
        :param _ActionName: 执行动作，取值为：intercept/redirect/observe
分别表示：拦截/重定向/观察
为空表示查询所有执行动作数据
        :type ActionName: str
        :param _Area: 地域：mainland或overseas，表示国内或海外，不填写默认表示国内
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Domain = None
        self._Metric = None
        self._Source = None
        self._Domains = None
        self._ActionName = None
        self._Area = None

    @property
    def StartTime(self):
        """查询Top数据的开始时间，格式为：2020-01-01 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询Top数据的结束时间，格式为：2020-01-01 23:59:59
支持 90 天内数据查询，不传此参数，表示查当天数据
时间跨度要小于等于7天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domain(self):
        """域名，不传此参数，表示查询账号级别数据
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Metric(self):
        """统计指标：
ip_url : Top IP+URL 默认值
ua :  Top UA
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Source(self):
        """cdn表示CDN数据，默认值
ecdn表示ECDN数据
        :rtype: str
        """
        return self._Source

    @Source.setter
    def Source(self, Source):
        self._Source = Source

    @property
    def Domains(self):
        """域名列表，不传此参数，表示查询账号级别数据
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def ActionName(self):
        """执行动作，取值为：intercept/redirect/observe
分别表示：拦截/重定向/观察
为空表示查询所有执行动作数据
        :rtype: str
        """
        return self._ActionName

    @ActionName.setter
    def ActionName(self, ActionName):
        self._ActionName = ActionName

    @property
    def Area(self):
        """地域：mainland或overseas，表示国内或海外，不填写默认表示国内
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domain = params.get("Domain")
        self._Metric = params.get("Metric")
        self._Source = params.get("Source")
        self._Domains = params.get("Domains")
        self._ActionName = params.get("ActionName")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopCcDataResponse(AbstractModel):
    """ListTopCcData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: Top数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of CcTopData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """Top数据
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of CcTopData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = CcTopData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopClsLogDataRequest(AbstractModel):
    """ListTopClsLogData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 需要查询的日志集ID
        :type LogsetId: str
        :param _TopicIds: 需要查询的日志主题ID组合，多个以逗号分隔
        :type TopicIds: str
        :param _StartTime: 需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS
        :type StartTime: str
        :param _EndTime: 需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS，时间跨度应小于10分钟
        :type EndTime: str
        :param _Domain: 指定域名查询
        :type Domain: str
        :param _Url: 指定访问的URL查询，支持URL开头和结尾使用\*表示通配
如：
/files/* 表示所有以/files/开头的请求
*.jpg 表示所有以.jpg结尾的请求
        :type Url: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        :param _Limit: 要查询的Top条数，最大值为100，默认为10
        :type Limit: int
        :param _Sort: 按请求量排序， asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        """
        self._LogsetId = None
        self._TopicIds = None
        self._StartTime = None
        self._EndTime = None
        self._Domain = None
        self._Url = None
        self._Channel = None
        self._Limit = None
        self._Sort = None

    @property
    def LogsetId(self):
        """需要查询的日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicIds(self):
        """需要查询的日志主题ID组合，多个以逗号分隔
        :rtype: str
        """
        return self._TopicIds

    @TopicIds.setter
    def TopicIds(self, TopicIds):
        self._TopicIds = TopicIds

    @property
    def StartTime(self):
        """需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS，时间跨度应小于10分钟
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domain(self):
        """指定域名查询
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Url(self):
        """指定访问的URL查询，支持URL开头和结尾使用\*表示通配
如：
/files/* 表示所有以/files/开头的请求
*.jpg 表示所有以.jpg结尾的请求
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Limit(self):
        """要查询的Top条数，最大值为100，默认为10
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Sort(self):
        """按请求量排序， asc（升序）或者 desc（降序），默认为 desc
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicIds = params.get("TopicIds")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domain = params.get("Domain")
        self._Url = params.get("Url")
        self._Channel = params.get("Channel")
        self._Limit = params.get("Limit")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopClsLogDataResponse(AbstractModel):
    """ListTopClsLogData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 数据列表
        :type Data: list of ClsLogIpData
        :param _TotalCount: 获取到Top总记录数
        :type TotalCount: int
        :param _IpCount: 获取到的不重复IP条数
        :type IpCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._IpCount = None
        self._RequestId = None

    @property
    def Data(self):
        """数据列表
        :rtype: list of ClsLogIpData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def TotalCount(self):
        """获取到Top总记录数
        :rtype: int
        """
        return self._TotalCount

    @TotalCount.setter
    def TotalCount(self, TotalCount):
        self._TotalCount = TotalCount

    @property
    def IpCount(self):
        """获取到的不重复IP条数
        :rtype: int
        """
        return self._IpCount

    @IpCount.setter
    def IpCount(self, IpCount):
        self._IpCount = IpCount

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ClsLogIpData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._IpCount = params.get("IpCount")
        self._RequestId = params.get("RequestId")


class ListTopDDoSDataRequest(AbstractModel):
    """ListTopDDoSData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询Top数据的开始时间，格式为：2020-01-01 00:00:00
        :type StartTime: str
        :param _EndTime: 查询Top数据的结束时间，格式为：2020-01-01 23:59:59
支持 90 天内数据查询，时间跨度要小于等于7天
        :type EndTime: str
        :param _TopCount: 查询Top的数量，不填默认值为10
        :type TopCount: int
        :param _Metric: AttackIP表示查询攻击ip的top排行，AttackType表示攻击类型的top排行，为空默认为AttackType
        :type Metric: str
        """
        self._StartTime = None
        self._EndTime = None
        self._TopCount = None
        self._Metric = None

    @property
    def StartTime(self):
        """查询Top数据的开始时间，格式为：2020-01-01 00:00:00
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询Top数据的结束时间，格式为：2020-01-01 23:59:59
支持 90 天内数据查询，时间跨度要小于等于7天
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TopCount(self):
        """查询Top的数量，不填默认值为10
        :rtype: int
        """
        return self._TopCount

    @TopCount.setter
    def TopCount(self, TopCount):
        self._TopCount = TopCount

    @property
    def Metric(self):
        """AttackIP表示查询攻击ip的top排行，AttackType表示攻击类型的top排行，为空默认为AttackType
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TopCount = params.get("TopCount")
        self._Metric = params.get("Metric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopDDoSDataResponse(AbstractModel):
    """ListTopDDoSData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: DDoS 攻击类型的top数据，当Metric=AttackType的时候返回攻击类型的统计数据，IPData为空
        :type Data: list of DDoSTopData
        :param _IPData: ddos攻击ip的top数据，Metric=AttackIP的时候返回IPData，Data为空
        :type IPData: list of DDoSAttackIPTopData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._IPData = None
        self._RequestId = None

    @property
    def Data(self):
        """DDoS 攻击类型的top数据，当Metric=AttackType的时候返回攻击类型的统计数据，IPData为空
        :rtype: list of DDoSTopData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def IPData(self):
        """ddos攻击ip的top数据，Metric=AttackIP的时候返回IPData，Data为空
        :rtype: list of DDoSAttackIPTopData
        """
        return self._IPData

    @IPData.setter
    def IPData(self, IPData):
        self._IPData = IPData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DDoSTopData()
                obj._deserialize(item)
                self._Data.append(obj)
        if params.get("IPData") is not None:
            self._IPData = []
            for item in params.get("IPData"):
                obj = DDoSAttackIPTopData()
                obj._deserialize(item)
                self._IPData.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopDataRequest(AbstractModel):
    """ListTopData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间：yyyy-MM-dd HH:mm:ss
仅支持按分钟粒度的数据查询，按入参抹去秒位作为起始时间，如 StartTime为2018-09-04 10:40:23，返回数据的起始时间为2018-09-04 10:40:00
仅支持 90 天内数据查询
        :type StartTime: str
        :param _EndTime: 查询结束时间：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为结束日期 返回小于等于结束日期当天 23:59:59 产生的数据，如EndTime为2018-09-05 22:40:00，返回数据的结束时间为2018-09-05 23:59:59
EndTime 需要大于等于 StartTime
        :type EndTime: str
        :param _Metric: 排序对象，支持以下几种形式：
url：访问 URL 排序（无参数的URL），支持的 Filter 为 flux、request
district：省份、国家/地区排序，支持的 Filter 为 flux、request
isp：运营商排序，支持的 Filter 为 flux、request
host：域名访问数据排序，支持的 Filter 为：flux、request、bandwidth、fluxHitRate、2XX、3XX、4XX、5XX、statusCode
originHost：域名回源数据排序，支持的 Filter 为 flux、request、bandwidth、origin_2XX、origin_3XX、origin_4XX、origin_5XX、OriginStatusCode
        :type Metric: str
        :param _Filter: 排序使用的指标名称：
flux：Metric 为 host 时指代访问流量，originHost 时指代回源流量
bandwidth：Metric 为 host 时指代访问带宽，originHost 时指代回源带宽
request：Metric 为 host 时指代访问请求数，originHost 时指代回源请求数
fluxHitRate：平均流量命中率
2XX：访问 2XX 状态码
3XX：访问 3XX 状态码
4XX：访问 4XX 状态码
5XX：访问 5XX 状态码
origin_2XX：回源 2XX 状态码
origin_3XX：回源 3XX 状态码
origin_4XX：回源 4XX 状态码
origin_5XX：回源 5XX 状态码
statusCode：指定访问状态码统计，在 Code 参数中填充指定状态码
OriginStatusCode：指定回源状态码统计，在 Code 参数中填充指定状态码
        :type Filter: str
        :param _Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param _Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param _Detail: 多域名查询时，默认（false)返回所有域名汇总排序结果
Metric 为 url、path、district、isp，Filter 为 flux、request 时，可设置为 true，返回每一个 Domain 的排序数据
        :type Detail: bool
        :param _Code: Filter 为 statusCode、OriginStatusCode 时，填充指定状态码查询排序结果
        :type Code: str
        :param _Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据，支持的 Metric 为 url、district、host、originHost，当 Metric 为 originHost 时仅支持 flux、request、bandwidth Filter
        :type Area: str
        :param _AreaType: 查询中国境外CDN数据，且仅当 Metric 为 district 或 host 时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas，且 Metric 是 district 或 host 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据，当 Metric 为 host 时仅支持 flux、request、bandwidth Filter
        :type AreaType: str
        :param _Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :type Product: str
        :param _Limit: 只返回前N条数据，默认为最大值100，metric=url时默认为最大值1000
        :type Limit: int
        """
        self._StartTime = None
        self._EndTime = None
        self._Metric = None
        self._Filter = None
        self._Domains = None
        self._Project = None
        self._Detail = None
        self._Code = None
        self._Area = None
        self._AreaType = None
        self._Product = None
        self._Limit = None

    @property
    def StartTime(self):
        """查询起始时间：yyyy-MM-dd HH:mm:ss
仅支持按分钟粒度的数据查询，按入参抹去秒位作为起始时间，如 StartTime为2018-09-04 10:40:23，返回数据的起始时间为2018-09-04 10:40:00
仅支持 90 天内数据查询
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为结束日期 返回小于等于结束日期当天 23:59:59 产生的数据，如EndTime为2018-09-05 22:40:00，返回数据的结束时间为2018-09-05 23:59:59
EndTime 需要大于等于 StartTime
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metric(self):
        """排序对象，支持以下几种形式：
url：访问 URL 排序（无参数的URL），支持的 Filter 为 flux、request
district：省份、国家/地区排序，支持的 Filter 为 flux、request
isp：运营商排序，支持的 Filter 为 flux、request
host：域名访问数据排序，支持的 Filter 为：flux、request、bandwidth、fluxHitRate、2XX、3XX、4XX、5XX、statusCode
originHost：域名回源数据排序，支持的 Filter 为 flux、request、bandwidth、origin_2XX、origin_3XX、origin_4XX、origin_5XX、OriginStatusCode
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Filter(self):
        """排序使用的指标名称：
flux：Metric 为 host 时指代访问流量，originHost 时指代回源流量
bandwidth：Metric 为 host 时指代访问带宽，originHost 时指代回源带宽
request：Metric 为 host 时指代访问请求数，originHost 时指代回源请求数
fluxHitRate：平均流量命中率
2XX：访问 2XX 状态码
3XX：访问 3XX 状态码
4XX：访问 4XX 状态码
5XX：访问 5XX 状态码
origin_2XX：回源 2XX 状态码
origin_3XX：回源 3XX 状态码
origin_4XX：回源 4XX 状态码
origin_5XX：回源 5XX 状态码
statusCode：指定访问状态码统计，在 Code 参数中填充指定状态码
OriginStatusCode：指定回源状态码统计，在 Code 参数中填充指定状态码
        :rtype: str
        """
        return self._Filter

    @Filter.setter
    def Filter(self, Filter):
        self._Filter = Filter

    @property
    def Domains(self):
        """指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Project(self):
        """指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :rtype: int
        """
        return self._Project

    @Project.setter
    def Project(self, Project):
        self._Project = Project

    @property
    def Detail(self):
        """多域名查询时，默认（false)返回所有域名汇总排序结果
Metric 为 url、path、district、isp，Filter 为 flux、request 时，可设置为 true，返回每一个 Domain 的排序数据
        :rtype: bool
        """
        return self._Detail

    @Detail.setter
    def Detail(self, Detail):
        self._Detail = Detail

    @property
    def Code(self):
        """Filter 为 statusCode、OriginStatusCode 时，填充指定状态码查询排序结果
        :rtype: str
        """
        return self._Code

    @Code.setter
    def Code(self, Code):
        self._Code = Code

    @property
    def Area(self):
        """指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据，支持的 Metric 为 url、district、host、originHost，当 Metric 为 originHost 时仅支持 flux、request、bandwidth Filter
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AreaType(self):
        """查询中国境外CDN数据，且仅当 Metric 为 district 或 host 时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas，且 Metric 是 district 或 host 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据，当 Metric 为 host 时仅支持 flux、request、bandwidth Filter
        :rtype: str
        """
        return self._AreaType

    @AreaType.setter
    def AreaType(self, AreaType):
        self._AreaType = AreaType

    @property
    def Product(self):
        """指定查询的产品数据，可选为cdn或者ecdn，默认为cdn
        :rtype: str
        """
        return self._Product

    @Product.setter
    def Product(self, Product):
        self._Product = Product

    @property
    def Limit(self):
        """只返回前N条数据，默认为最大值100，metric=url时默认为最大值1000
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metric = params.get("Metric")
        self._Filter = params.get("Filter")
        self._Domains = params.get("Domains")
        self._Project = params.get("Project")
        self._Detail = params.get("Detail")
        self._Code = params.get("Code")
        self._Area = params.get("Area")
        self._AreaType = params.get("AreaType")
        self._Product = params.get("Product")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopDataResponse(AbstractModel):
    """ListTopData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 各个资源的Top 访问数据详情。
        :type Data: list of TopData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        """各个资源的Top 访问数据详情。
        :rtype: list of TopData
        """
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = TopData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class ListTopWafDataRequest(AbstractModel):
    """ListTopWafData请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param _Domain: 指定域名查询，不填写查询整个AppID下数据
        :type Domain: str
        :param _AttackType: 指定攻击类型
不填则查询所有攻击类型的数据总和
AttackType 映射如下:
"webshell" : Webshell检测防护
"oa" : 常见OA漏洞防护
"xss" : XSS跨站脚本攻击防护
"xxe" : XXE攻击防护
"webscan" : 扫描器攻击漏洞防护
"cms" : 常见CMS漏洞防护
"upload" : 恶意文件上传攻击防护
"sql" : SQL注入攻击防护
"cmd_inject": 命令/代码注入攻击防护
"osc" : 开源组件漏洞防护
"file_read" : 任意文件读取
"ldap" : LDAP注入攻击防护
"other" : 其它漏洞防护
        :type AttackType: str
        :param _DefenceMode: 指定防御模式
不填则查询所有防御模式的数据总和
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :type DefenceMode: str
        :param _Metric: 排序对象，支持以下几种形式：
url：攻击目标 url 排序
ip：攻击源 IP 排序
attackType：攻击类型排序
domain：当查询整个AppID下数据时，按照域名请求量排序
        :type Metric: str
        :param _Area: 地域：mainland 或 overseas
        :type Area: str
        :param _AttackTypes: 指定攻击类型列表，取值参考AttackType
        :type AttackTypes: list of str
        :param _Domains: 指定域名列表查询，不填写查询整个AppID下数据
        :type Domains: list of str
        """
        self._StartTime = None
        self._EndTime = None
        self._Domain = None
        self._AttackType = None
        self._DefenceMode = None
        self._Metric = None
        self._Area = None
        self._AttackTypes = None
        self._Domains = None

    @property
    def StartTime(self):
        """查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Domain(self):
        """指定域名查询，不填写查询整个AppID下数据
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def AttackType(self):
        """指定攻击类型
不填则查询所有攻击类型的数据总和
AttackType 映射如下:
"webshell" : Webshell检测防护
"oa" : 常见OA漏洞防护
"xss" : XSS跨站脚本攻击防护
"xxe" : XXE攻击防护
"webscan" : 扫描器攻击漏洞防护
"cms" : 常见CMS漏洞防护
"upload" : 恶意文件上传攻击防护
"sql" : SQL注入攻击防护
"cmd_inject": 命令/代码注入攻击防护
"osc" : 开源组件漏洞防护
"file_read" : 任意文件读取
"ldap" : LDAP注入攻击防护
"other" : 其它漏洞防护
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def DefenceMode(self):
        """指定防御模式
不填则查询所有防御模式的数据总和
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :rtype: str
        """
        return self._DefenceMode

    @DefenceMode.setter
    def DefenceMode(self, DefenceMode):
        self._DefenceMode = DefenceMode

    @property
    def Metric(self):
        """排序对象，支持以下几种形式：
url：攻击目标 url 排序
ip：攻击源 IP 排序
attackType：攻击类型排序
domain：当查询整个AppID下数据时，按照域名请求量排序
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Area(self):
        """地域：mainland 或 overseas
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def AttackTypes(self):
        """指定攻击类型列表，取值参考AttackType
        :rtype: list of str
        """
        return self._AttackTypes

    @AttackTypes.setter
    def AttackTypes(self, AttackTypes):
        self._AttackTypes = AttackTypes

    @property
    def Domains(self):
        """指定域名列表查询，不填写查询整个AppID下数据
        :rtype: list of str
        """
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Domain = params.get("Domain")
        self._AttackType = params.get("AttackType")
        self._DefenceMode = params.get("DefenceMode")
        self._Metric = params.get("Metric")
        self._Area = params.get("Area")
        self._AttackTypes = params.get("AttackTypes")
        self._Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopWafDataResponse(AbstractModel):
    """ListTopWafData返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TopTypeData: 攻击类型统计
        :type TopTypeData: list of ScdnTypeData
        :param _TopIpData: IP统计
        :type TopIpData: list of ScdnTopData
        :param _TopUrlData: URL统计
        :type TopUrlData: list of ScdnTopUrlData
        :param _TopDomainData: 域名统计
        :type TopDomainData: list of ScdnTopDomainData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TopTypeData = None
        self._TopIpData = None
        self._TopUrlData = None
        self._TopDomainData = None
        self._RequestId = None

    @property
    def TopTypeData(self):
        """攻击类型统计
        :rtype: list of ScdnTypeData
        """
        return self._TopTypeData

    @TopTypeData.setter
    def TopTypeData(self, TopTypeData):
        self._TopTypeData = TopTypeData

    @property
    def TopIpData(self):
        """IP统计
        :rtype: list of ScdnTopData
        """
        return self._TopIpData

    @TopIpData.setter
    def TopIpData(self, TopIpData):
        self._TopIpData = TopIpData

    @property
    def TopUrlData(self):
        """URL统计
        :rtype: list of ScdnTopUrlData
        """
        return self._TopUrlData

    @TopUrlData.setter
    def TopUrlData(self, TopUrlData):
        self._TopUrlData = TopUrlData

    @property
    def TopDomainData(self):
        """域名统计
        :rtype: list of ScdnTopDomainData
        """
        return self._TopDomainData

    @TopDomainData.setter
    def TopDomainData(self, TopDomainData):
        self._TopDomainData = TopDomainData

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("TopTypeData") is not None:
            self._TopTypeData = []
            for item in params.get("TopTypeData"):
                obj = ScdnTypeData()
                obj._deserialize(item)
                self._TopTypeData.append(obj)
        if params.get("TopIpData") is not None:
            self._TopIpData = []
            for item in params.get("TopIpData"):
                obj = ScdnTopData()
                obj._deserialize(item)
                self._TopIpData.append(obj)
        if params.get("TopUrlData") is not None:
            self._TopUrlData = []
            for item in params.get("TopUrlData"):
                obj = ScdnTopUrlData()
                obj._deserialize(item)
                self._TopUrlData.append(obj)
        if params.get("TopDomainData") is not None:
            self._TopDomainData = []
            for item in params.get("TopDomainData"):
                obj = ScdnTopDomainData()
                obj._deserialize(item)
                self._TopDomainData.append(obj)
        self._RequestId = params.get("RequestId")


class LogSetInfo(AbstractModel):
    """日志集信息

    """

    def __init__(self):
        r"""
        :param _AppId: 开发者ID
        :type AppId: int
        :param _Channel: 渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: str
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _LogsetName: 日志集名字
        :type LogsetName: str
        :param _IsDefault: 是否默认日志集
        :type IsDefault: int
        :param _LogsetSavePeriod: 日志保存时间，单位为天
        :type LogsetSavePeriod: int
        :param _CreateTime: 创建日期
        :type CreateTime: str
        :param _Region: 区域
        :type Region: str
        :param _Deleted: cls侧是否已经被删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Deleted: str
        :param _RegionEn: 英文区域
注意：此字段可能返回 null，表示取不到有效值。
        :type RegionEn: str
        """
        self._AppId = None
        self._Channel = None
        self._LogsetId = None
        self._LogsetName = None
        self._IsDefault = None
        self._LogsetSavePeriod = None
        self._CreateTime = None
        self._Region = None
        self._Deleted = None
        self._RegionEn = None

    @property
    def AppId(self):
        """开发者ID
        :rtype: int
        """
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Channel(self):
        """渠道
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def LogsetName(self):
        """日志集名字
        :rtype: str
        """
        return self._LogsetName

    @LogsetName.setter
    def LogsetName(self, LogsetName):
        self._LogsetName = LogsetName

    @property
    def IsDefault(self):
        """是否默认日志集
        :rtype: int
        """
        return self._IsDefault

    @IsDefault.setter
    def IsDefault(self, IsDefault):
        self._IsDefault = IsDefault

    @property
    def LogsetSavePeriod(self):
        """日志保存时间，单位为天
        :rtype: int
        """
        return self._LogsetSavePeriod

    @LogsetSavePeriod.setter
    def LogsetSavePeriod(self, LogsetSavePeriod):
        self._LogsetSavePeriod = LogsetSavePeriod

    @property
    def CreateTime(self):
        """创建日期
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Region(self):
        """区域
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Deleted(self):
        """cls侧是否已经被删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted

    @property
    def RegionEn(self):
        """英文区域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RegionEn

    @RegionEn.setter
    def RegionEn(self, RegionEn):
        self._RegionEn = RegionEn


    def _deserialize(self, params):
        self._AppId = params.get("AppId")
        self._Channel = params.get("Channel")
        self._LogsetId = params.get("LogsetId")
        self._LogsetName = params.get("LogsetName")
        self._IsDefault = params.get("IsDefault")
        self._LogsetSavePeriod = params.get("LogsetSavePeriod")
        self._CreateTime = params.get("CreateTime")
        self._Region = params.get("Region")
        self._Deleted = params.get("Deleted")
        self._RegionEn = params.get("RegionEn")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MainlandConfig(AbstractModel):
    """域名国内地区特殊配置。分地区特殊配置。UpdateDomainConfig接口只支持修改部分地区配置，为了兼容旧版本配置，本类型会列出旧版本所有可能存在差异的配置列表，支持修改的配置列表如下：
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        r"""
        :param _Authentication: 时间戳防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _BandwidthAlert: 带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _CacheKey: 缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _DownstreamCapping: 下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _ErrorPage: 错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _FollowRedirect: 301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _MaxAge: 浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _OriginPullOptimization: 跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _RangeOriginPull: Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _Referer: 防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _RequestHeader: 回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _ResponseHeaderCache: 遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _Seo: seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ServiceType: 域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _StatusCodeCache: 状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _VideoSeek: 视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _AwsPrivateAccess: 回源S3私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _OssPrivateAccess: 回源OSS私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _HwPrivateAccess: 华为云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: 七牛云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        self._Authentication = None
        self._BandwidthAlert = None
        self._Cache = None
        self._CacheKey = None
        self._Compression = None
        self._DownstreamCapping = None
        self._ErrorPage = None
        self._FollowRedirect = None
        self._ForceRedirect = None
        self._Https = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._MaxAge = None
        self._Origin = None
        self._OriginPullOptimization = None
        self._RangeOriginPull = None
        self._Referer = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._ResponseHeaderCache = None
        self._Seo = None
        self._ServiceType = None
        self._StatusCodeCache = None
        self._VideoSeek = None
        self._AwsPrivateAccess = None
        self._OssPrivateAccess = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None

    @property
    def Authentication(self):
        """时间戳防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def BandwidthAlert(self):
        """带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        """
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def Cache(self):
        """缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def CacheKey(self):
        """缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Compression(self):
        """智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def DownstreamCapping(self):
        """下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        """
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def ErrorPage(self):
        """错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def FollowRedirect(self):
        """301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        """
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ForceRedirect(self):
        """访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        """Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def IpFilter(self):
        """IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def MaxAge(self):
        """浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Origin(self):
        """源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def OriginPullOptimization(self):
        """跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        """
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def RangeOriginPull(self):
        """Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        """
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def Referer(self):
        """防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Referer`
        """
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def RequestHeader(self):
        """回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        """源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def ResponseHeaderCache(self):
        """遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        """
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def Seo(self):
        """seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Seo`
        """
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ServiceType(self):
        """域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StatusCodeCache(self):
        """状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        """
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def VideoSeek(self):
        """视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def AwsPrivateAccess(self):
        """回源S3私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        """
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def OssPrivateAccess(self):
        """回源OSS私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        """
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def HwPrivateAccess(self):
        """华为云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        """
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        """七牛云对象存储回源鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        self._ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsRequest(AbstractModel):
    """ManageClsTopicDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 日志集ID
        :type LogsetId: str
        :param _TopicId: 日志主题ID
        :type TopicId: str
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        :param _DomainAreaConfigs: 域名区域配置，注意：如果此字段为空，则表示解绑对应主题下的所有域名
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self._LogsetId = None
        self._TopicId = None
        self._Channel = None
        self._DomainAreaConfigs = None

    @property
    def LogsetId(self):
        """日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicId(self):
        """日志主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def DomainAreaConfigs(self):
        """域名区域配置，注意：如果此字段为空，则表示解绑对应主题下的所有域名
        :rtype: list of DomainAreaConfig
        """
        return self._DomainAreaConfigs

    @DomainAreaConfigs.setter
    def DomainAreaConfigs(self, DomainAreaConfigs):
        self._DomainAreaConfigs = DomainAreaConfigs


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicId = params.get("TopicId")
        self._Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self._DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self._DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsResponse(AbstractModel):
    """ManageClsTopicDomains返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class MapInfo(AbstractModel):
    """名称与ID映射关系

    """

    def __init__(self):
        r"""
        :param _Id: 对象 Id
        :type Id: int
        :param _Name: 对象名称
        :type Name: str
        """
        self._Id = None
        self._Name = None

    @property
    def Id(self):
        """对象 Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Name(self):
        """对象名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """浏览器缓存规则配置，用于设置 MaxAge 默认值，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 浏览器缓存配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _MaxAgeRules: MaxAge 规则
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAgeRules: list of MaxAgeRule
        :param _MaxAgeCodeRule: MaxAge 状态码相关规则
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAgeCodeRule: :class:`tencentcloud.cdn.v20180606.models.MaxAgeCodeRule`
        """
        self._Switch = None
        self._MaxAgeRules = None
        self._MaxAgeCodeRule = None

    @property
    def Switch(self):
        """浏览器缓存配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAgeRules(self):
        """MaxAge 规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of MaxAgeRule
        """
        return self._MaxAgeRules

    @MaxAgeRules.setter
    def MaxAgeRules(self, MaxAgeRules):
        self._MaxAgeRules = MaxAgeRules

    @property
    def MaxAgeCodeRule(self):
        """MaxAge 状态码相关规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MaxAgeCodeRule`
        """
        return self._MaxAgeCodeRule

    @MaxAgeCodeRule.setter
    def MaxAgeCodeRule(self, MaxAgeCodeRule):
        self._MaxAgeCodeRule = MaxAgeCodeRule


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("MaxAgeRules") is not None:
            self._MaxAgeRules = []
            for item in params.get("MaxAgeRules"):
                obj = MaxAgeRule()
                obj._deserialize(item)
                self._MaxAgeRules.append(obj)
        if params.get("MaxAgeCodeRule") is not None:
            self._MaxAgeCodeRule = MaxAgeCodeRule()
            self._MaxAgeCodeRule._deserialize(params.get("MaxAgeCodeRule"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAgeCodeRule(AbstractModel):
    """MaxAge 状态码相关规则配置

    """

    def __init__(self):
        r"""
        :param _Action: 处理动作
clear：清除 cache-control 头部
        :type Action: str
        :param _StatusCodes: 指定HTTP状态码生效，当前仅支持填写"400-599"
        :type StatusCodes: list of str
        """
        self._Action = None
        self._StatusCodes = None

    @property
    def Action(self):
        """处理动作
clear：清除 cache-control 头部
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def StatusCodes(self):
        """指定HTTP状态码生效，当前仅支持填写"400-599"
        :rtype: list of str
        """
        return self._StatusCodes

    @StatusCodes.setter
    def StatusCodes(self, StatusCodes):
        self._StatusCodes = StatusCodes


    def _deserialize(self, params):
        self._Action = params.get("Action")
        self._StatusCodes = params.get("StatusCodes")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAgeRule(AbstractModel):
    """MagAge 规则配置

    """

    def __init__(self):
        r"""
        :param _MaxAgeType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效
        :type MaxAgeType: str
        :param _MaxAgeContents: MaxAgeType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：all规则不可删除，默认遵循源站，可修改。
        :type MaxAgeContents: list of str
        :param _MaxAgeTime: MaxAge 时间设置，单位秒
注意：时间为0，即不缓存。
        :type MaxAgeTime: int
        :param _FollowOrigin: 是否遵循源站，on或off，开启时忽略时间设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self._MaxAgeType = None
        self._MaxAgeContents = None
        self._MaxAgeTime = None
        self._FollowOrigin = None

    @property
    def MaxAgeType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效
        :rtype: str
        """
        return self._MaxAgeType

    @MaxAgeType.setter
    def MaxAgeType(self, MaxAgeType):
        self._MaxAgeType = MaxAgeType

    @property
    def MaxAgeContents(self):
        """MaxAgeType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：all规则不可删除，默认遵循源站，可修改。
        :rtype: list of str
        """
        return self._MaxAgeContents

    @MaxAgeContents.setter
    def MaxAgeContents(self, MaxAgeContents):
        self._MaxAgeContents = MaxAgeContents

    @property
    def MaxAgeTime(self):
        """MaxAge 时间设置，单位秒
注意：时间为0，即不缓存。
        :rtype: int
        """
        return self._MaxAgeTime

    @MaxAgeTime.setter
    def MaxAgeTime(self, MaxAgeTime):
        self._MaxAgeTime = MaxAgeTime

    @property
    def FollowOrigin(self):
        """是否遵循源站，on或off，开启时忽略时间设置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        self._MaxAgeType = params.get("MaxAgeType")
        self._MaxAgeContents = params.get("MaxAgeContents")
        self._MaxAgeTime = params.get("MaxAgeTime")
        self._FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainConfigRequest(AbstractModel):
    """ModifyDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Route: 配置路径
        :type Route: str
        :param _Value: 配置路径值，使用 json 进行序列化，其中固定 update 作为 key
        :type Value: str
        """
        self._Domain = None
        self._Route = None
        self._Value = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Route(self):
        """配置路径
        :rtype: str
        """
        return self._Route

    @Route.setter
    def Route(self, Route):
        self._Route = Route

    @property
    def Value(self):
        """配置路径值，使用 json 进行序列化，其中固定 update 作为 key
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Route = params.get("Route")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainConfigResponse(AbstractModel):
    """ModifyDomainConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class ModifyPurgeFetchTaskStatusRequest(AbstractModel):
    """ModifyPurgeFetchTaskStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _ExecutionTime: 执行时间
        :type ExecutionTime: str
        :param _ExecutionStatus: 执行状态
success: 成功
failed: 失败
        :type ExecutionStatus: str
        :param _Id: 任务 ID
        :type Id: str
        :param _ExecutionStatusDesc: 执行状态详情
        :type ExecutionStatusDesc: str
        """
        self._ExecutionTime = None
        self._ExecutionStatus = None
        self._Id = None
        self._ExecutionStatusDesc = None

    @property
    def ExecutionTime(self):
        """执行时间
        :rtype: str
        """
        return self._ExecutionTime

    @ExecutionTime.setter
    def ExecutionTime(self, ExecutionTime):
        self._ExecutionTime = ExecutionTime

    @property
    def ExecutionStatus(self):
        """执行状态
success: 成功
failed: 失败
        :rtype: str
        """
        return self._ExecutionStatus

    @ExecutionStatus.setter
    def ExecutionStatus(self, ExecutionStatus):
        self._ExecutionStatus = ExecutionStatus

    @property
    def Id(self):
        """任务 ID
        :rtype: str
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def ExecutionStatusDesc(self):
        """执行状态详情
        :rtype: str
        """
        return self._ExecutionStatusDesc

    @ExecutionStatusDesc.setter
    def ExecutionStatusDesc(self, ExecutionStatusDesc):
        self._ExecutionStatusDesc = ExecutionStatusDesc


    def _deserialize(self, params):
        self._ExecutionTime = params.get("ExecutionTime")
        self._ExecutionStatus = params.get("ExecutionStatus")
        self._Id = params.get("Id")
        self._ExecutionStatusDesc = params.get("ExecutionStatusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPurgeFetchTaskStatusResponse(AbstractModel):
    """ModifyPurgeFetchTaskStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """离线缓存是否开启

    """

    def __init__(self):
        r"""
        :param _Switch: 离线缓存配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """离线缓存配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """源站配置复杂类型，支持以下配置：
    + 源站指定为单个域名
    + 源站指定为多个 IP，可配置端口（1\~65535），可配置权重（1\~100），格式为 IP:端口:权重
    + 回源域名配置
    + 对象存储（COS）作为源站
    + 热备源站指定为单个域名
    + 热备源站指定为多个 IP，可配置端口（1\~65535），暂不支持权重配置
    + 热备源站回源域名配置

    """

    def __init__(self):
        r"""
        :param _Origins: 主源站列表
<font color=red>修改源站时，需要同时填充对应的 OriginType</font>
注意：此字段可能返回 null，表示取不到有效值。
        :type Origins: list of str
        :param _OriginType: 主源站类型
<font color=red>当源站列表 Origins 不为空时必填</font>
入参支持以下几种类型：
domain：域名类型
domainv6：域名解析V6类型
cos：对象存储源站
third_party: 第三方存储源站
igtm: IGTM多活源
ip：IP 列表作为源站
ipv6：源站列表为一个单独的 IPv6 地址
ip_ipv6：源站列表为多个 IPv4 地址和IPv6 地址
ip_domain: 支持IP和域名形式源站混填（白名单功能）
ip_domainv6：源站列表为多个 IPv4 地址以及域名解析v6地址
ipv6_domain: 源站列表为多个 IPv6 地址以及域名
ipv6_domainv6：源站列表为多个 IPv6 地址以及域名解析v6地址
domain_domainv6：源站列表为多个域名解析v4 地址以及域名解析v6地址
ip_ipv6_domain：源站列表为多个 IPv4 地址IPv6 地址以及域名
ip_ipv6_domainv6：源站列表为多个 IPv4 地址IPv6 地址以及域名解析v6地址
ip_domain_domainv6：源站列表为多个 IPv4 地址域名解析v4 地址以及域名解析v6地址
ipv6_domain_domainv6：源站列表为多个 域名解析v4 地址IPv6 地址以及域名解析v6地址
ip_ipv6_domain_domainv6：源站列表为多个 IPv4 地址IPv6 地址 域名解析v4 地址以及域名解析v6地址
出参增加以下几种类型：
image：数据万象源站
ftp：历史 FTP 托管源源站，现已不维护
修改 Origins 时需要同时填充对应的 OriginType
IPv6 功能目前尚未全量，需要先申请试用
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param _ServerName: 回主源站时 Host 头部
<font color=red>当源站类型为cos或者第三方存储加速时,ServerName字段必填</font>
不填充则默认为加速域名
若接入的是泛域名，则回源 Host 默认为访问时的子域名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _CosPrivateAccess: OriginType 为对象存储（COS）时，可以指定是否允许访问私有 bucket
注意：需要先授权 CDN 访问该私有 Bucket 的权限后，才可开启此配置。取值范围: on/off
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPrivateAccess: str
        :param _OriginPullProtocol: 回源协议配置
http：强制 http 回源
follow：协议跟随回源
https：强制 https 回源
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param _BackupOrigins: 备源站列表
<font color=red>修改备源站时，需要同时填充对应的 BackupOriginType</font>
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOrigins: list of str
        :param _BackupOriginType: 备源站类型
<font color=red>备源站列表BackupOrigins 不为空时必填</font>
支持以下类型：
domain：域名类型
ip：IP 列表作为源站
以下备源源站类型尚未全量支持，需要申请试用：
ipv6_domain: 源站列表为多个 IPv6 地址以及域名
ip_ipv6：源站列表为多个 IPv4 地址和IPv6 地址
ipv6_domain: 源站列表为多个 IPv6 地址以及域名
ip_ipv6_domain：源站列表为多个 IPv4 地址IPv6 地址以及域名
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOriginType: str
        :param _BackupServerName: 回备源站时 Host 头部，不填充则默认为主源站的 ServerName
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupServerName: str
        :param _BasePath: 回源路径
注意：此字段可能返回 null，表示取不到有效值。
        :type BasePath: str
        :param _PathRules: 回源路径重写规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PathRules: list of PathRule
        :param _PathBasedOrigin: 分路径回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PathBasedOrigin: list of PathBasedOriginRule
        :param _Sni: HTTPS回源SNI配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Sni: :class:`tencentcloud.cdn.v20180606.models.OriginSni`
        :param _AdvanceHttps: HTTPS回源高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceHttps: :class:`tencentcloud.cdn.v20180606.models.AdvanceHttps`
        :param _OriginCompany: 对象存储回源厂商
<font color=red>当源站类型为第三方存储源站(third_party)时必填</font>
可选值包括以下:
aws_s3: AWS S3
ali_oss: 阿里云 OSS
hw_obs: 华为 OBS
qiniu_kodo: 七牛云 kodo
others: 其它厂商对象存储,仅支持兼容以AWS签名算法的对象存储，如腾讯云金融专区COS
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCompany: str
        """
        self._Origins = None
        self._OriginType = None
        self._ServerName = None
        self._CosPrivateAccess = None
        self._OriginPullProtocol = None
        self._BackupOrigins = None
        self._BackupOriginType = None
        self._BackupServerName = None
        self._BasePath = None
        self._PathRules = None
        self._PathBasedOrigin = None
        self._Sni = None
        self._AdvanceHttps = None
        self._OriginCompany = None

    @property
    def Origins(self):
        """主源站列表
<font color=red>修改源站时，需要同时填充对应的 OriginType</font>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def OriginType(self):
        """主源站类型
<font color=red>当源站列表 Origins 不为空时必填</font>
入参支持以下几种类型：
domain：域名类型
domainv6：域名解析V6类型
cos：对象存储源站
third_party: 第三方存储源站
igtm: IGTM多活源
ip：IP 列表作为源站
ipv6：源站列表为一个单独的 IPv6 地址
ip_ipv6：源站列表为多个 IPv4 地址和IPv6 地址
ip_domain: 支持IP和域名形式源站混填（白名单功能）
ip_domainv6：源站列表为多个 IPv4 地址以及域名解析v6地址
ipv6_domain: 源站列表为多个 IPv6 地址以及域名
ipv6_domainv6：源站列表为多个 IPv6 地址以及域名解析v6地址
domain_domainv6：源站列表为多个域名解析v4 地址以及域名解析v6地址
ip_ipv6_domain：源站列表为多个 IPv4 地址IPv6 地址以及域名
ip_ipv6_domainv6：源站列表为多个 IPv4 地址IPv6 地址以及域名解析v6地址
ip_domain_domainv6：源站列表为多个 IPv4 地址域名解析v4 地址以及域名解析v6地址
ipv6_domain_domainv6：源站列表为多个 域名解析v4 地址IPv6 地址以及域名解析v6地址
ip_ipv6_domain_domainv6：源站列表为多个 IPv4 地址IPv6 地址 域名解析v4 地址以及域名解析v6地址
出参增加以下几种类型：
image：数据万象源站
ftp：历史 FTP 托管源源站，现已不维护
修改 Origins 时需要同时填充对应的 OriginType
IPv6 功能目前尚未全量，需要先申请试用
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def ServerName(self):
        """回主源站时 Host 头部
<font color=red>当源站类型为cos或者第三方存储加速时,ServerName字段必填</font>
不填充则默认为加速域名
若接入的是泛域名，则回源 Host 默认为访问时的子域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def CosPrivateAccess(self):
        """OriginType 为对象存储（COS）时，可以指定是否允许访问私有 bucket
注意：需要先授权 CDN 访问该私有 Bucket 的权限后，才可开启此配置。取值范围: on/off
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CosPrivateAccess

    @CosPrivateAccess.setter
    def CosPrivateAccess(self, CosPrivateAccess):
        self._CosPrivateAccess = CosPrivateAccess

    @property
    def OriginPullProtocol(self):
        """回源协议配置
http：强制 http 回源
follow：协议跟随回源
https：强制 https 回源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol

    @property
    def BackupOrigins(self):
        """备源站列表
<font color=red>修改备源站时，需要同时填充对应的 BackupOriginType</font>
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._BackupOrigins

    @BackupOrigins.setter
    def BackupOrigins(self, BackupOrigins):
        self._BackupOrigins = BackupOrigins

    @property
    def BackupOriginType(self):
        """备源站类型
<font color=red>备源站列表BackupOrigins 不为空时必填</font>
支持以下类型：
domain：域名类型
ip：IP 列表作为源站
以下备源源站类型尚未全量支持，需要申请试用：
ipv6_domain: 源站列表为多个 IPv6 地址以及域名
ip_ipv6：源站列表为多个 IPv4 地址和IPv6 地址
ipv6_domain: 源站列表为多个 IPv6 地址以及域名
ip_ipv6_domain：源站列表为多个 IPv4 地址IPv6 地址以及域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupOriginType

    @BackupOriginType.setter
    def BackupOriginType(self, BackupOriginType):
        self._BackupOriginType = BackupOriginType

    @property
    def BackupServerName(self):
        """回备源站时 Host 头部，不填充则默认为主源站的 ServerName
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BackupServerName

    @BackupServerName.setter
    def BackupServerName(self, BackupServerName):
        self._BackupServerName = BackupServerName

    @property
    def BasePath(self):
        """回源路径
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._BasePath

    @BasePath.setter
    def BasePath(self, BasePath):
        self._BasePath = BasePath

    @property
    def PathRules(self):
        """回源路径重写规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PathRule
        """
        return self._PathRules

    @PathRules.setter
    def PathRules(self, PathRules):
        self._PathRules = PathRules

    @property
    def PathBasedOrigin(self):
        """分路径回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of PathBasedOriginRule
        """
        return self._PathBasedOrigin

    @PathBasedOrigin.setter
    def PathBasedOrigin(self, PathBasedOrigin):
        self._PathBasedOrigin = PathBasedOrigin

    @property
    def Sni(self):
        """HTTPS回源SNI配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginSni`
        """
        return self._Sni

    @Sni.setter
    def Sni(self, Sni):
        self._Sni = Sni

    @property
    def AdvanceHttps(self):
        """HTTPS回源高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvanceHttps`
        """
        return self._AdvanceHttps

    @AdvanceHttps.setter
    def AdvanceHttps(self, AdvanceHttps):
        self._AdvanceHttps = AdvanceHttps

    @property
    def OriginCompany(self):
        """对象存储回源厂商
<font color=red>当源站类型为第三方存储源站(third_party)时必填</font>
可选值包括以下:
aws_s3: AWS S3
ali_oss: 阿里云 OSS
hw_obs: 华为 OBS
qiniu_kodo: 七牛云 kodo
others: 其它厂商对象存储,仅支持兼容以AWS签名算法的对象存储，如腾讯云金融专区COS
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginCompany

    @OriginCompany.setter
    def OriginCompany(self, OriginCompany):
        self._OriginCompany = OriginCompany


    def _deserialize(self, params):
        self._Origins = params.get("Origins")
        self._OriginType = params.get("OriginType")
        self._ServerName = params.get("ServerName")
        self._CosPrivateAccess = params.get("CosPrivateAccess")
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        self._BackupOrigins = params.get("BackupOrigins")
        self._BackupOriginType = params.get("BackupOriginType")
        self._BackupServerName = params.get("BackupServerName")
        self._BasePath = params.get("BasePath")
        if params.get("PathRules") is not None:
            self._PathRules = []
            for item in params.get("PathRules"):
                obj = PathRule()
                obj._deserialize(item)
                self._PathRules.append(obj)
        if params.get("PathBasedOrigin") is not None:
            self._PathBasedOrigin = []
            for item in params.get("PathBasedOrigin"):
                obj = PathBasedOriginRule()
                obj._deserialize(item)
                self._PathBasedOrigin.append(obj)
        if params.get("Sni") is not None:
            self._Sni = OriginSni()
            self._Sni._deserialize(params.get("Sni"))
        if params.get("AdvanceHttps") is not None:
            self._AdvanceHttps = AdvanceHttps()
            self._AdvanceHttps._deserialize(params.get("AdvanceHttps"))
        self._OriginCompany = params.get("OriginCompany")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthentication(AbstractModel):
    """回源鉴权高级配置

    """

    def __init__(self):
        r"""
        :param _Switch: 回源鉴权高级配置开关，取值有：
on：开启
off：关闭

注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _TypeA: 鉴权类型A配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.OriginAuthenticationTypeA`
        """
        self._Switch = None
        self._TypeA = None

    @property
    def Switch(self):
        """回源鉴权高级配置开关，取值有：
on：开启
off：关闭

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def TypeA(self):
        """鉴权类型A配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginAuthenticationTypeA`
        """
        return self._TypeA

    @TypeA.setter
    def TypeA(self, TypeA):
        self._TypeA = TypeA


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self._TypeA = OriginAuthenticationTypeA()
            self._TypeA._deserialize(params.get("TypeA"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthenticationTypeA(AbstractModel):
    """回源鉴权高级配置TypeA

    """

    def __init__(self):
        r"""
        :param _SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        """
        self._SecretKey = None

    @property
    def SecretKey(self):
        """用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCombine(AbstractModel):
    """合并回源配置项

    """

    def __init__(self):
        r"""
        :param _Switch: 合并回源配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """合并回源配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginIp(AbstractModel):
    """CDN回源节点IP信息

    """

    def __init__(self):
        r"""
        :param _Ip: 回源IP段/回源IP，默认返回IP段信息。
        :type Ip: str
        """
        self._Ip = None

    @property
    def Ip(self):
        """回源IP段/回源IP，默认返回IP段信息。
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullOptimization(AbstractModel):
    """跨国回源优化配置，默认为关闭状态 (已下线)

    """

    def __init__(self):
        r"""
        :param _Switch: 跨国回源优化配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _OptimizationType: 跨国类型
OVToCN：境外回源境内
CNToOV：境内回源境外
注意：此字段可能返回 null，表示取不到有效值。
        :type OptimizationType: str
        """
        self._Switch = None
        self._OptimizationType = None

    @property
    def Switch(self):
        """跨国回源优化配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def OptimizationType(self):
        """跨国类型
OVToCN：境外回源境内
CNToOV：境内回源境外
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OptimizationType

    @OptimizationType.setter
    def OptimizationType(self, OptimizationType):
        self._OptimizationType = OptimizationType


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._OptimizationType = params.get("OptimizationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullTimeout(AbstractModel):
    """回源超时配置

    """

    def __init__(self):
        r"""
        :param _ConnectTimeout: 回源建连超时时间，单位为秒，要求5~60之间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectTimeout: int
        :param _ReceiveTimeout: 回源接收超时时间，单位为秒，要求10 ~ 300之间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiveTimeout: int
        """
        self._ConnectTimeout = None
        self._ReceiveTimeout = None

    @property
    def ConnectTimeout(self):
        """回源建连超时时间，单位为秒，要求5~60之间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConnectTimeout

    @ConnectTimeout.setter
    def ConnectTimeout(self, ConnectTimeout):
        self._ConnectTimeout = ConnectTimeout

    @property
    def ReceiveTimeout(self):
        """回源接收超时时间，单位为秒，要求10 ~ 300之间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ReceiveTimeout

    @ReceiveTimeout.setter
    def ReceiveTimeout(self, ReceiveTimeout):
        self._ReceiveTimeout = ReceiveTimeout


    def _deserialize(self, params):
        self._ConnectTimeout = params.get("ConnectTimeout")
        self._ReceiveTimeout = params.get("ReceiveTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginSni(AbstractModel):
    """HTTPS回源SNI

    """

    def __init__(self):
        r"""
        :param _Switch: 是否开启HTTPS回源SNI。
开启：on，
关闭：off
        :type Switch: str
        :param _ServerName: 回源域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        """
        self._Switch = None
        self._ServerName = None

    @property
    def Switch(self):
        """是否开启HTTPS回源SNI。
开启：on，
关闭：off
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ServerName(self):
        """回源域名。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._ServerName = params.get("ServerName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OssPrivateAccess(AbstractModel):
    """oss回源鉴权

    """

    def __init__(self):
        r"""
        :param _Switch: oss回源鉴权配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _AccessKey: 访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _SecretKey: 密钥，字段为脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Region: 地域
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Bucket: Bucketname
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Region = None
        self._Bucket = None

    @property
    def Switch(self):
        """oss回源鉴权配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        """访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """密钥，字段为脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Region(self):
        """地域
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        """Bucketname
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OthersPrivateAccess(AbstractModel):
    """其他厂商对象存储回源鉴权

    """

    def __init__(self):
        r"""
        :param _Switch: 其他厂商对象存储回源鉴权配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _AccessKey: 访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _SecretKey: 密钥，字段位脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param _Region: 地域。
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: str
        :param _Bucket: 存储桶名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Bucket: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None
        self._Region = None
        self._Bucket = None

    @property
    def Switch(self):
        """其他厂商对象存储回源鉴权配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        """访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """密钥，字段位脱敏返回。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey

    @property
    def Region(self):
        """地域。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def Bucket(self):
        """存储桶名称。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Bucket

    @Bucket.setter
    def Bucket(self, Bucket):
        self._Bucket = Bucket


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        self._Region = params.get("Region")
        self._Bucket = params.get("Bucket")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OverseaConfig(AbstractModel):
    """域名海外地区特殊配置。UpdateDomainConfig接口只支持修改部分地区配置，为了兼容旧版本配置，本类型会列出旧版本所有可能存在差异的配置列表，支持修改的配置列表如下：
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        r"""
        :param _Authentication: 时间戳防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _BandwidthAlert: 带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _CacheKey: 缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _DownstreamCapping: 下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _ErrorPage: 错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _FollowRedirect: 301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _MaxAge: 浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _OriginPullOptimization: 跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _RangeOriginPull: Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _Referer: 防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _RequestHeader: 回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _ResponseHeaderCache: 遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _Seo: seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ServiceType: 域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param _StatusCodeCache: 状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _VideoSeek: 视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _AwsPrivateAccess: 回源S3私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _OssPrivateAccess: 回源OSS私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _HwPrivateAccess: 华为云对象存储鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: 七牛云对象存储鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        self._Authentication = None
        self._BandwidthAlert = None
        self._Cache = None
        self._CacheKey = None
        self._Compression = None
        self._DownstreamCapping = None
        self._ErrorPage = None
        self._FollowRedirect = None
        self._ForceRedirect = None
        self._Https = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._MaxAge = None
        self._Origin = None
        self._OriginPullOptimization = None
        self._RangeOriginPull = None
        self._Referer = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._ResponseHeaderCache = None
        self._Seo = None
        self._ServiceType = None
        self._StatusCodeCache = None
        self._VideoSeek = None
        self._AwsPrivateAccess = None
        self._OssPrivateAccess = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None

    @property
    def Authentication(self):
        """时间戳防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def BandwidthAlert(self):
        """带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        """
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def Cache(self):
        """缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def CacheKey(self):
        """缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Compression(self):
        """智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def DownstreamCapping(self):
        """下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        """
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def ErrorPage(self):
        """错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def FollowRedirect(self):
        """301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        """
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ForceRedirect(self):
        """访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Https(self):
        """Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def IpFilter(self):
        """IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def MaxAge(self):
        """浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def Origin(self):
        """源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def OriginPullOptimization(self):
        """跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        """
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def RangeOriginPull(self):
        """Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        """
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def Referer(self):
        """防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Referer`
        """
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def RequestHeader(self):
        """回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        """源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def ResponseHeaderCache(self):
        """遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        """
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def Seo(self):
        """seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Seo`
        """
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ServiceType(self):
        """域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def StatusCodeCache(self):
        """状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        """
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def VideoSeek(self):
        """视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def AwsPrivateAccess(self):
        """回源S3私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        """
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def OssPrivateAccess(self):
        """回源OSS私有鉴权。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        """
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def HwPrivateAccess(self):
        """华为云对象存储鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        """
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        """七牛云对象存储鉴权
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        self._ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamFilter(AbstractModel):
    """参数黑名单

    """

    def __init__(self):
        r"""
        :param _Switch:  参数黑名单开关
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _FilterRules: 参数黑名单规则
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of ParamFilterRule
        """
        self._Switch = None
        self._FilterRules = None

    @property
    def Switch(self):
        """ 参数黑名单开关
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterRules(self):
        """参数黑名单规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ParamFilterRule
        """
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = ParamFilterRule()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ParamFilterRule(AbstractModel):
    """参数黑名单规则

    """

    def __init__(self):
        r"""
        :param _Key: 参数名
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param _Values: 参数值数组, 小于10个
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        :param _ReturnCode: http 返回码 ( 暂仅支持403)
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: str
        """
        self._Key = None
        self._Values = None
        self._ReturnCode = None

    @property
    def Key(self):
        """参数名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Values(self):
        """参数值数组, 小于10个
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values

    @property
    def ReturnCode(self):
        """http 返回码 ( 暂仅支持403)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ReturnCode

    @ReturnCode.setter
    def ReturnCode(self, ReturnCode):
        self._ReturnCode = ReturnCode


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Values = params.get("Values")
        self._ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathBasedOriginRule(AbstractModel):
    """分路径回源规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效
        :type RuleType: str
        :param _RulePaths: RuleType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
        :type RulePaths: list of str
        :param _Origin: 源站列表，支持域名或ipv4地址
        :type Origin: list of str
        """
        self._RuleType = None
        self._RulePaths = None
        self._Origin = None

    @property
    def RuleType(self):
        """规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """RuleType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def Origin(self):
        """源站列表，支持域名或ipv4地址
        :rtype: list of str
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._Origin = params.get("Origin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRule(AbstractModel):
    """分路径回源配置规则。

    """

    def __init__(self):
        r"""
        :param _Regex: 是否开启通配符“*”匹配：
false：关闭
true：开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: bool
        :param _Path: 匹配的URL路径，仅支持Url路径，不支持参数。默认完全匹配，开启通配符“*”匹配后，最多支持5个通配符，最大长度为1024个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param _Origin: 路径匹配时的回源源站。暂不支持开了私有读写的COS源。不填写时沿用默认源站。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: str
        :param _ServerName: 路径匹配时回源的Host头部。不填写时沿用默认ServerName。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _OriginArea: 源站所属区域，支持CN，OV：
CN：中国境内
OV：中国境外
默认为CN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginArea: str
        :param _ForwardUri: 路径匹配时回源的URI路径，必须以“/”开头，不包含参数部分。最大长度为1024个字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号“*”，最多支持10个捕获值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardUri: str
        :param _RequestHeaders: 路径匹配时回源的头部设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeaders: list of HttpHeaderRule
        :param _FullMatch: 当Regex为false时，Path是否开启完全匹配。
false：关闭
true：开启
注意：此字段可能返回 null，表示取不到有效值。
        :type FullMatch: bool
        """
        self._Regex = None
        self._Path = None
        self._Origin = None
        self._ServerName = None
        self._OriginArea = None
        self._ForwardUri = None
        self._RequestHeaders = None
        self._FullMatch = None

    @property
    def Regex(self):
        """是否开启通配符“*”匹配：
false：关闭
true：开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._Regex

    @Regex.setter
    def Regex(self, Regex):
        self._Regex = Regex

    @property
    def Path(self):
        """匹配的URL路径，仅支持Url路径，不支持参数。默认完全匹配，开启通配符“*”匹配后，最多支持5个通配符，最大长度为1024个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path

    @property
    def Origin(self):
        """路径匹配时的回源源站。暂不支持开了私有读写的COS源。不填写时沿用默认源站。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ServerName(self):
        """路径匹配时回源的Host头部。不填写时沿用默认ServerName。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OriginArea(self):
        """源站所属区域，支持CN，OV：
CN：中国境内
OV：中国境外
默认为CN。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._OriginArea

    @OriginArea.setter
    def OriginArea(self, OriginArea):
        self._OriginArea = OriginArea

    @property
    def ForwardUri(self):
        """路径匹配时回源的URI路径，必须以“/”开头，不包含参数部分。最大长度为1024个字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号“*”，最多支持10个捕获值。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ForwardUri

    @ForwardUri.setter
    def ForwardUri(self, ForwardUri):
        self._ForwardUri = ForwardUri

    @property
    def RequestHeaders(self):
        """路径匹配时回源的头部设置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HttpHeaderRule
        """
        return self._RequestHeaders

    @RequestHeaders.setter
    def RequestHeaders(self, RequestHeaders):
        self._RequestHeaders = RequestHeaders

    @property
    def FullMatch(self):
        """当Regex为false时，Path是否开启完全匹配。
false：关闭
true：开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._FullMatch

    @FullMatch.setter
    def FullMatch(self, FullMatch):
        self._FullMatch = FullMatch


    def _deserialize(self, params):
        self._Regex = params.get("Regex")
        self._Path = params.get("Path")
        self._Origin = params.get("Origin")
        self._ServerName = params.get("ServerName")
        self._OriginArea = params.get("OriginArea")
        self._ForwardUri = params.get("ForwardUri")
        if params.get("RequestHeaders") is not None:
            self._RequestHeaders = []
            for item in params.get("RequestHeaders"):
                obj = HttpHeaderRule()
                obj._deserialize(item)
                self._RequestHeaders.append(obj)
        self._FullMatch = params.get("FullMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostSize(AbstractModel):
    """POST请求上传文件流式传输最大限制

    """

    def __init__(self):
        r"""
        :param _Switch: POST请求上传文件流式传输最大限制配置开关，取值有：
on：开启，平台默认为32MB
off：关闭

        :type Switch: str
        :param _MaxSize: 最大限制，取值在1MB和200MB之间。
        :type MaxSize: int
        """
        self._Switch = None
        self._MaxSize = None

    @property
    def Switch(self):
        """POST请求上传文件流式传输最大限制配置开关，取值有：
on：开启，平台默认为32MB
off：关闭

        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxSize(self):
        """最大限制，取值在1MB和200MB之间。
        :rtype: int
        """
        return self._MaxSize

    @MaxSize.setter
    def MaxSize(self, MaxSize):
        self._MaxSize = MaxSize


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Paths: 目录列表，需要包含协议头部 http:// 或 https://
        :type Paths: list of str
        :param _FlushType: 刷新类型
flush：刷新产生更新的资源
delete：刷新全部资源
        :type FlushType: str
        :param _UrlEncode: 是否对中文字符进行编码后刷新
        :type UrlEncode: bool
        :param _Area: 刷新区域
无此参数时，默认刷新加速域名所在加速区域
填充 mainland 时，仅刷新中国境内加速节点上缓存内容
填充 overseas 时，仅刷新中国境外加速节点上缓存内容
指定刷新区域时，需要与域名加速区域匹配
        :type Area: str
        """
        self._Paths = None
        self._FlushType = None
        self._UrlEncode = None
        self._Area = None

    @property
    def Paths(self):
        """目录列表，需要包含协议头部 http:// 或 https://
        :rtype: list of str
        """
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def FlushType(self):
        """刷新类型
flush：刷新产生更新的资源
delete：刷新全部资源
        :rtype: str
        """
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType

    @property
    def UrlEncode(self):
        """是否对中文字符进行编码后刷新
        :rtype: bool
        """
        return self._UrlEncode

    @UrlEncode.setter
    def UrlEncode(self, UrlEncode):
        self._UrlEncode = UrlEncode

    @property
    def Area(self):
        """刷新区域
无此参数时，默认刷新加速域名所在加速区域
填充 mainland 时，仅刷新中国境内加速节点上缓存内容
填充 overseas 时，仅刷新中国境外加速节点上缓存内容
指定刷新区域时，需要与域名加速区域匹配
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Paths = params.get("Paths")
        self._FlushType = params.get("FlushType")
        self._UrlEncode = params.get("UrlEncode")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 刷新任务 ID，同一批次提交的目录共用一个任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """刷新任务 ID，同一批次提交的目录共用一个任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """刷新任务详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 刷新任务 ID
        :type TaskId: str
        :param _Url: 刷新 URL
        :type Url: str
        :param _Status: 刷新任务状态
fail：刷新失败
done：刷新成功
process：刷新中
        :type Status: str
        :param _PurgeType: 刷新类型
url：URL 刷新
path：目录刷新
        :type PurgeType: str
        :param _FlushType: 刷新方式
flush：刷新更新资源（仅目录刷新时有此类型）
delete：刷新全部资源
        :type FlushType: str
        :param _CreateTime: 刷新任务提交时间
        :type CreateTime: str
        """
        self._TaskId = None
        self._Url = None
        self._Status = None
        self._PurgeType = None
        self._FlushType = None
        self._CreateTime = None

    @property
    def TaskId(self):
        """刷新任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        """刷新 URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """刷新任务状态
fail：刷新失败
done：刷新成功
process：刷新中
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PurgeType(self):
        """刷新类型
url：URL 刷新
path：目录刷新
        :rtype: str
        """
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def FlushType(self):
        """刷新方式
flush：刷新更新资源（仅目录刷新时有此类型）
delete：刷新全部资源
        :rtype: str
        """
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType

    @property
    def CreateTime(self):
        """刷新任务提交时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._PurgeType = params.get("PurgeType")
        self._FlushType = params.get("FlushType")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: URL 列表，需要包含协议头部 http:// 或 https://
        :type Urls: list of str
        :param _Area: 刷新区域
无此参数时，默认刷新加速域名所在加速区域
填充 mainland 时，仅刷新中国境内加速节点上缓存内容
填充 overseas 时，仅刷新中国境外加速节点上缓存内容
指定刷新区域时，需要与域名加速区域匹配
        :type Area: str
        :param _UrlEncode: 是否对中文字符进行编码后刷新
        :type UrlEncode: bool
        """
        self._Urls = None
        self._Area = None
        self._UrlEncode = None

    @property
    def Urls(self):
        """URL 列表，需要包含协议头部 http:// 或 https://
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def Area(self):
        """刷新区域
无此参数时，默认刷新加速域名所在加速区域
填充 mainland 时，仅刷新中国境内加速节点上缓存内容
填充 overseas 时，仅刷新中国境外加速节点上缓存内容
指定刷新区域时，需要与域名加速区域匹配
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def UrlEncode(self):
        """是否对中文字符进行编码后刷新
        :rtype: bool
        """
        return self._UrlEncode

    @UrlEncode.setter
    def UrlEncode(self, UrlEncode):
        self._UrlEncode = UrlEncode


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._Area = params.get("Area")
        self._UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 刷新任务 ID，同一批次提交的 URL 共用一个任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """刷新任务 ID，同一批次提交的 URL 共用一个任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PushTask(AbstractModel):
    """预热任务详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 预热任务 ID
        :type TaskId: str
        :param _Url: 预热 URL
        :type Url: str
        :param _Status: 预热任务状态
fail：预热失败
done：预热成功
process：预热中
invalid：预热无效(源站返回4xx或5xx状态码)
        :type Status: str
        :param _Percent: 预热进度百分比
        :type Percent: int
        :param _CreateTime: 预热任务提交时间
        :type CreateTime: str
        :param _Area: 预热区域
mainland：境内
overseas：境外
global：全球
        :type Area: str
        :param _UpdateTime: 预热任务更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._TaskId = None
        self._Url = None
        self._Status = None
        self._Percent = None
        self._CreateTime = None
        self._Area = None
        self._UpdateTime = None

    @property
    def TaskId(self):
        """预热任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        """预热 URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        """预热任务状态
fail：预热失败
done：预热成功
process：预热中
invalid：预热无效(源站返回4xx或5xx状态码)
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Percent(self):
        """预热进度百分比
        :rtype: int
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent

    @property
    def CreateTime(self):
        """预热任务提交时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Area(self):
        """预热区域
mainland：境内
overseas：境外
global：全球
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def UpdateTime(self):
        """预热任务更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._Url = params.get("Url")
        self._Status = params.get("Status")
        self._Percent = params.get("Percent")
        self._CreateTime = params.get("CreateTime")
        self._Area = params.get("Area")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Urls: URL 列表，需要包含协议头部 http:// 或 https://
        :type Urls: list of str
        :param _UserAgent: 指定预热请求回源时 HTTP 请求的 User-Agent 头部
默认为 TencentCdn
        :type UserAgent: str
        :param _Area: 预热生效区域
mainland：预热至境内节点
overseas：预热至境外节点
global：预热全球节点
不填充情况下，默认为 mainland， URL 中域名必须在对应区域启用了加速服务才能提交对应区域的预热任务
        :type Area: str
        :param _Layer: 中国境内区域默认预热至中间层节点，中国境外区域默认预热至边缘节点。预热至边缘产生的边缘层流量会计入计费流量。
填写"middle"或不填充时，可指定预热至中间层节点。
        :type Layer: str
        :param _ParseM3U8: 是否递归解析m3u8文件中的ts分片预热
注意事项：
1. 该功能要求m3u8索引文件能直接请求获取
2. 当前只支持递归解析一级索引和子索引中的ts分片，递归深度不超过3层
3. 解析获取的ts分片会正常累加每日预热用量，当用量超出配额时，会静默处理，不再执行预热
        :type ParseM3U8: bool
        :param _DisableRange: 是否关闭Range回源
注意事项：
此功能灰度发布中，敬请期待
        :type DisableRange: bool
        :param _Headers: 自定义 HTTP 请求头。最多定义 20 个，Name 长度不超过 128 字节，Value 长度不超过 1024 字节
        :type Headers: list of HTTPHeader
        :param _UrlEncode: 是否对URL进行编码
        :type UrlEncode: bool
        """
        self._Urls = None
        self._UserAgent = None
        self._Area = None
        self._Layer = None
        self._ParseM3U8 = None
        self._DisableRange = None
        self._Headers = None
        self._UrlEncode = None

    @property
    def Urls(self):
        """URL 列表，需要包含协议头部 http:// 或 https://
        :rtype: list of str
        """
        return self._Urls

    @Urls.setter
    def Urls(self, Urls):
        self._Urls = Urls

    @property
    def UserAgent(self):
        """指定预热请求回源时 HTTP 请求的 User-Agent 头部
默认为 TencentCdn
        :rtype: str
        """
        return self._UserAgent

    @UserAgent.setter
    def UserAgent(self, UserAgent):
        self._UserAgent = UserAgent

    @property
    def Area(self):
        """预热生效区域
mainland：预热至境内节点
overseas：预热至境外节点
global：预热全球节点
不填充情况下，默认为 mainland， URL 中域名必须在对应区域启用了加速服务才能提交对应区域的预热任务
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Layer(self):
        """中国境内区域默认预热至中间层节点，中国境外区域默认预热至边缘节点。预热至边缘产生的边缘层流量会计入计费流量。
填写"middle"或不填充时，可指定预热至中间层节点。
        :rtype: str
        """
        return self._Layer

    @Layer.setter
    def Layer(self, Layer):
        self._Layer = Layer

    @property
    def ParseM3U8(self):
        """是否递归解析m3u8文件中的ts分片预热
注意事项：
1. 该功能要求m3u8索引文件能直接请求获取
2. 当前只支持递归解析一级索引和子索引中的ts分片，递归深度不超过3层
3. 解析获取的ts分片会正常累加每日预热用量，当用量超出配额时，会静默处理，不再执行预热
        :rtype: bool
        """
        return self._ParseM3U8

    @ParseM3U8.setter
    def ParseM3U8(self, ParseM3U8):
        self._ParseM3U8 = ParseM3U8

    @property
    def DisableRange(self):
        """是否关闭Range回源
注意事项：
此功能灰度发布中，敬请期待
        :rtype: bool
        """
        return self._DisableRange

    @DisableRange.setter
    def DisableRange(self, DisableRange):
        self._DisableRange = DisableRange

    @property
    def Headers(self):
        """自定义 HTTP 请求头。最多定义 20 个，Name 长度不超过 128 字节，Value 长度不超过 1024 字节
        :rtype: list of HTTPHeader
        """
        return self._Headers

    @Headers.setter
    def Headers(self, Headers):
        self._Headers = Headers

    @property
    def UrlEncode(self):
        """是否对URL进行编码
        :rtype: bool
        """
        return self._UrlEncode

    @UrlEncode.setter
    def UrlEncode(self, UrlEncode):
        self._UrlEncode = UrlEncode


    def _deserialize(self, params):
        self._Urls = params.get("Urls")
        self._UserAgent = params.get("UserAgent")
        self._Area = params.get("Area")
        self._Layer = params.get("Layer")
        self._ParseM3U8 = params.get("ParseM3U8")
        self._DisableRange = params.get("DisableRange")
        if params.get("Headers") is not None:
            self._Headers = []
            for item in params.get("Headers"):
                obj = HTTPHeader()
                obj._deserialize(item)
                self._Headers.append(obj)
        self._UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 此批提交的任务 ID
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        """此批提交的任务 ID
        :rtype: str
        """
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class QnPrivateAccess(AbstractModel):
    """七牛元对象存储回源鉴权配置

    """

    def __init__(self):
        r"""
        :param _Switch: 七牛元对象存储回源鉴权配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _AccessKey: 访问 ID
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param _SecretKey: 密钥，字段为脱敏返回。
        :type SecretKey: str
        """
        self._Switch = None
        self._AccessKey = None
        self._SecretKey = None

    @property
    def Switch(self):
        """七牛元对象存储回源鉴权配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def AccessKey(self):
        """访问 ID
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AccessKey

    @AccessKey.setter
    def AccessKey(self, AccessKey):
        self._AccessKey = AccessKey

    @property
    def SecretKey(self):
        """密钥，字段为脱敏返回。
        :rtype: str
        """
        return self._SecretKey

    @SecretKey.setter
    def SecretKey(self, SecretKey):
        self._SecretKey = SecretKey


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._AccessKey = params.get("AccessKey")
        self._SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class QueryStringKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        r"""
        :param _Switch: CacheKey是否由QueryString组成配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Reorder: 是否重新排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Reorder: str
        :param _Action: 使用/排除部分url参数，取值有：
includeAll：包含所有
excludeAll：排除所有
includeCustom：自定义包含
excludeCustom：自定义排除
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _Value: 使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Switch = None
        self._Reorder = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        """CacheKey是否由QueryString组成配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Reorder(self):
        """是否重新排序
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Reorder

    @Reorder.setter
    def Reorder(self, Reorder):
        self._Reorder = Reorder

    @property
    def Action(self):
        """使用/排除部分url参数，取值有：
includeAll：包含所有
excludeAll：排除所有
includeCustom：自定义包含
excludeCustom：自定义排除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        """使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Reorder = params.get("Reorder")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """Quic配置项

    """

    def __init__(self):
        r"""
        :param _Switch: Quic功能配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Quic功能配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """刷新/预热 可用量及配额

    """

    def __init__(self):
        r"""
        :param _Batch: 单次批量提交配额上限。
        :type Batch: int
        :param _Total: 每日提交配额上限。
        :type Total: int
        :param _Available: 每日剩余的可提交配额。
        :type Available: int
        :param _Area: 配额的区域。
        :type Area: str
        """
        self._Batch = None
        self._Total = None
        self._Available = None
        self._Area = None

    @property
    def Batch(self):
        """单次批量提交配额上限。
        :rtype: int
        """
        return self._Batch

    @Batch.setter
    def Batch(self, Batch):
        self._Batch = Batch

    @property
    def Total(self):
        """每日提交配额上限。
        :rtype: int
        """
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Available(self):
        """每日剩余的可提交配额。
        :rtype: int
        """
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available

    @property
    def Area(self):
        """配额的区域。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Batch = params.get("Batch")
        self._Total = params.get("Total")
        self._Available = params.get("Available")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RangeOriginPull(AbstractModel):
    """分片回源配置，默认为开启状态

    """

    def __init__(self):
        r"""
        :param _Switch: 分片回源配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _RangeRules: 分路径分片回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeRules: list of RangeOriginPullRule
        """
        self._Switch = None
        self._RangeRules = None

    @property
    def Switch(self):
        """分片回源配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RangeRules(self):
        """分路径分片回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RangeOriginPullRule
        """
        return self._RangeRules

    @RangeRules.setter
    def RangeRules(self, RangeRules):
        self._RangeRules = RangeRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RangeRules") is not None:
            self._RangeRules = []
            for item in params.get("RangeRules"):
                obj = RangeOriginPullRule()
                obj._deserialize(item)
                self._RangeRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RangeOriginPullRule(AbstractModel):
    """分路径分片回源配置

    """

    def __init__(self):
        r"""
        :param _Switch: 分片回源配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RulePaths: RuleType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self._Switch = None
        self._RuleType = None
        self._RulePaths = None

    @property
    def Switch(self):
        """分片回源配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RuleType(self):
        """规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """RuleType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RedirectConfig(AbstractModel):
    """自定义回源302 follow请求host配置

    """

    def __init__(self):
        r"""
        :param _Switch: 自定义回源302 follow请求host配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _FollowRedirectHost: 主源站follow302请求时带的自定义的host头部
        :type FollowRedirectHost: str
        :param _FollowRedirectBackupHost: 备份源站follow302请求时带的自定义的host头部
        :type FollowRedirectBackupHost: str
        """
        self._Switch = None
        self._FollowRedirectHost = None
        self._FollowRedirectBackupHost = None

    @property
    def Switch(self):
        """自定义回源302 follow请求host配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FollowRedirectHost(self):
        """主源站follow302请求时带的自定义的host头部
        :rtype: str
        """
        return self._FollowRedirectHost

    @FollowRedirectHost.setter
    def FollowRedirectHost(self, FollowRedirectHost):
        self._FollowRedirectHost = FollowRedirectHost

    @property
    def FollowRedirectBackupHost(self):
        """备份源站follow302请求时带的自定义的host头部
        :rtype: str
        """
        return self._FollowRedirectBackupHost

    @FollowRedirectBackupHost.setter
    def FollowRedirectBackupHost(self, FollowRedirectBackupHost):
        self._FollowRedirectBackupHost = FollowRedirectBackupHost


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FollowRedirectHost = params.get("FollowRedirectHost")
        self._FollowRedirectBackupHost = params.get("FollowRedirectBackupHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Referer(AbstractModel):
    """Referer 黑白名单配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: referer 黑白名单配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _RefererRules: referer 黑白名单配置规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RefererRules: list of RefererRule
        """
        self._Switch = None
        self._RefererRules = None

    @property
    def Switch(self):
        """referer 黑白名单配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RefererRules(self):
        """referer 黑白名单配置规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RefererRule
        """
        return self._RefererRules

    @RefererRules.setter
    def RefererRules(self, RefererRules):
        self._RefererRules = RefererRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RefererRules") is not None:
            self._RefererRules = []
            for item in params.get("RefererRules"):
                obj = RefererRule()
                obj._deserialize(item)
                self._RefererRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefererRule(AbstractModel):
    """Referer 黑白名单配置规则，针对特定资源生效

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
        :type RuleType: str
        :param _RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
        :type RulePaths: list of str
        :param _RefererType: referer 配置类型
whitelist：白名单
blacklist：黑名单
        :type RefererType: str
        :param _Referers: referer 内容列表
        :type Referers: list of str
        :param _AllowEmpty: 是否允许空 referer
防盗链类型为白名单时，true表示允许空 referer，false表示不允许空 referer；
防盗链类型为黑名单时，true表示拒绝空referer，false表示不拒绝空referer；
        :type AllowEmpty: bool
        """
        self._RuleType = None
        self._RulePaths = None
        self._RefererType = None
        self._Referers = None
        self._AllowEmpty = None

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def RefererType(self):
        """referer 配置类型
whitelist：白名单
blacklist：黑名单
        :rtype: str
        """
        return self._RefererType

    @RefererType.setter
    def RefererType(self, RefererType):
        self._RefererType = RefererType

    @property
    def Referers(self):
        """referer 内容列表
        :rtype: list of str
        """
        return self._Referers

    @Referers.setter
    def Referers(self, Referers):
        self._Referers = Referers

    @property
    def AllowEmpty(self):
        """是否允许空 referer
防盗链类型为白名单时，true表示允许空 referer，false表示不允许空 referer；
防盗链类型为黑名单时，true表示拒绝空referer，false表示不拒绝空referer；
        :rtype: bool
        """
        return self._AllowEmpty

    @AllowEmpty.setter
    def AllowEmpty(self, AllowEmpty):
        self._AllowEmpty = AllowEmpty


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._RefererType = params.get("RefererType")
        self._Referers = params.get("Referers")
        self._AllowEmpty = params.get("AllowEmpty")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionMapRelation(AbstractModel):
    """区域映射id和子区域id的关联信息。

    """

    def __init__(self):
        r"""
        :param _RegionId: 区域ID。
        :type RegionId: int
        :param _SubRegionIdList: 子区域ID列表
        :type SubRegionIdList: list of int
        """
        self._RegionId = None
        self._SubRegionIdList = None

    @property
    def RegionId(self):
        """区域ID。
        :rtype: int
        """
        return self._RegionId

    @RegionId.setter
    def RegionId(self, RegionId):
        self._RegionId = RegionId

    @property
    def SubRegionIdList(self):
        """子区域ID列表
        :rtype: list of int
        """
        return self._SubRegionIdList

    @SubRegionIdList.setter
    def SubRegionIdList(self, SubRegionIdList):
        self._SubRegionIdList = SubRegionIdList


    def _deserialize(self, params):
        self._RegionId = params.get("RegionId")
        self._SubRegionIdList = params.get("SubRegionIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoteAuthentication(AbstractModel):
    """远程鉴权规则配置，可以包含多种规则配置。
    RemoteAuthenticationRules和Server 互斥，只需要配置其中一个。
    若只配置Server ，RemoteAuthenticationRules中详细规则参数将采用默认参数；默认参数值见各个配置项中说明；

    """

    def __init__(self):
        r"""
        :param _Switch: 远程鉴权配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _RemoteAuthenticationRules: 远程鉴权规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RemoteAuthenticationRules: list of RemoteAuthenticationRule
        :param _Server: 远程鉴权Server
注意：此字段可能返回 null，表示取不到有效值。
        :type Server: str
        """
        self._Switch = None
        self._RemoteAuthenticationRules = None
        self._Server = None

    @property
    def Switch(self):
        """远程鉴权配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RemoteAuthenticationRules(self):
        """远程鉴权规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of RemoteAuthenticationRule
        """
        return self._RemoteAuthenticationRules

    @RemoteAuthenticationRules.setter
    def RemoteAuthenticationRules(self, RemoteAuthenticationRules):
        self._RemoteAuthenticationRules = RemoteAuthenticationRules

    @property
    def Server(self):
        """远程鉴权Server
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("RemoteAuthenticationRules") is not None:
            self._RemoteAuthenticationRules = []
            for item in params.get("RemoteAuthenticationRules"):
                obj = RemoteAuthenticationRule()
                obj._deserialize(item)
                self._RemoteAuthenticationRules.append(obj)
        self._Server = params.get("Server")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoteAuthenticationRule(AbstractModel):
    """远程鉴权规则。

    """

    def __init__(self):
        r"""
        :param _Server: 远程鉴权Server。
默认值:和上层配置的"Server"一致；
        :type Server: str
        :param _AuthMethod: 请求远程鉴权服务器的http方法；取值范围[get,post,head,all]; 
all: 表示"遵循终端用户请求方法"
默认值: all
        :type AuthMethod: str
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定目录生效
path：指定文件绝对路径生效
默认值:all
        :type RuleType: str
        :param _RulePaths: 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
默认值:*
        :type RulePaths: list of str
        :param _AuthTimeout: 请求远程鉴权服务器超时时间，单位毫秒；
取值范围：[1,30 000]
默认值:20000
        :type AuthTimeout: int
        :param _AuthTimeoutAction: 请求远程鉴权服务器超时后执行拦截或者放行；
RETURN_200: 超时后放行；
RETURN_403:超时拦截；
默认值:RETURN_200
        :type AuthTimeoutAction: str
        """
        self._Server = None
        self._AuthMethod = None
        self._RuleType = None
        self._RulePaths = None
        self._AuthTimeout = None
        self._AuthTimeoutAction = None

    @property
    def Server(self):
        """远程鉴权Server。
默认值:和上层配置的"Server"一致；
        :rtype: str
        """
        return self._Server

    @Server.setter
    def Server(self, Server):
        self._Server = Server

    @property
    def AuthMethod(self):
        """请求远程鉴权服务器的http方法；取值范围[get,post,head,all]; 
all: 表示"遵循终端用户请求方法"
默认值: all
        :rtype: str
        """
        return self._AuthMethod

    @AuthMethod.setter
    def AuthMethod(self, AuthMethod):
        self._AuthMethod = AuthMethod

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定目录生效
path：指定文件绝对路径生效
默认值:all
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
默认值:*
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def AuthTimeout(self):
        """请求远程鉴权服务器超时时间，单位毫秒；
取值范围：[1,30 000]
默认值:20000
        :rtype: int
        """
        return self._AuthTimeout

    @AuthTimeout.setter
    def AuthTimeout(self, AuthTimeout):
        self._AuthTimeout = AuthTimeout

    @property
    def AuthTimeoutAction(self):
        """请求远程鉴权服务器超时后执行拦截或者放行；
RETURN_200: 超时后放行；
RETURN_403:超时拦截；
默认值:RETURN_200
        :rtype: str
        """
        return self._AuthTimeoutAction

    @AuthTimeoutAction.setter
    def AuthTimeoutAction(self, AuthTimeoutAction):
        self._AuthTimeoutAction = AuthTimeoutAction


    def _deserialize(self, params):
        self._Server = params.get("Server")
        self._AuthMethod = params.get("AuthMethod")
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._AuthTimeout = params.get("AuthTimeout")
        self._AuthTimeoutAction = params.get("AuthTimeoutAction")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportData(AbstractModel):
    """CDN报表数据

    """

    def __init__(self):
        r"""
        :param _ResourceId: 项目ID/域名ID。
        :type ResourceId: str
        :param _Resource: 项目名称/域名。
        :type Resource: str
        :param _Value: 流量总和/带宽最大值，单位分别为bytes，bps。
        :type Value: int
        :param _Percentage: 单个资源占总体百分比。
        :type Percentage: float
        :param _BillingValue: 计费流量总和/计费带宽最大值，单位分别为bytes，bps。
        :type BillingValue: int
        :param _BillingPercentage: 计费数值占总体百分比。
        :type BillingPercentage: float
        """
        self._ResourceId = None
        self._Resource = None
        self._Value = None
        self._Percentage = None
        self._BillingValue = None
        self._BillingPercentage = None

    @property
    def ResourceId(self):
        """项目ID/域名ID。
        :rtype: str
        """
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def Resource(self):
        """项目名称/域名。
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def Value(self):
        """流量总和/带宽最大值，单位分别为bytes，bps。
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Percentage(self):
        """单个资源占总体百分比。
        :rtype: float
        """
        return self._Percentage

    @Percentage.setter
    def Percentage(self, Percentage):
        self._Percentage = Percentage

    @property
    def BillingValue(self):
        """计费流量总和/计费带宽最大值，单位分别为bytes，bps。
        :rtype: int
        """
        return self._BillingValue

    @BillingValue.setter
    def BillingValue(self, BillingValue):
        self._BillingValue = BillingValue

    @property
    def BillingPercentage(self):
        """计费数值占总体百分比。
        :rtype: float
        """
        return self._BillingPercentage

    @BillingPercentage.setter
    def BillingPercentage(self, BillingPercentage):
        self._BillingPercentage = BillingPercentage


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._Resource = params.get("Resource")
        self._Value = params.get("Value")
        self._Percentage = params.get("Percentage")
        self._BillingValue = params.get("BillingValue")
        self._BillingPercentage = params.get("BillingPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestHeader(AbstractModel):
    """自定义请求头配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 自定义请求头配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _HeaderRules: 自定义请求头配置规则
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self._Switch = None
        self._HeaderRules = None

    @property
    def Switch(self):
        """自定义请求头配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderRules(self):
        """自定义请求头配置规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HttpHeaderPathRule
        """
        return self._HeaderRules

    @HeaderRules.setter
    def HeaderRules(self, HeaderRules):
        self._HeaderRules = HeaderRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self._HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self._HeaderRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceBillingData(AbstractModel):
    """计费数据明细

    """

    def __init__(self):
        r"""
        :param _Resource: 资源名称，根据查询条件不同分为以下几类：
某一个具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
某一个项目 ID：指定项目查询时，显示为项目 ID
all：账号维度数据明细
        :type Resource: str
        :param _BillingData: 计费数据详情
        :type BillingData: list of CdnData
        """
        self._Resource = None
        self._BillingData = None

    @property
    def Resource(self):
        """资源名称，根据查询条件不同分为以下几类：
某一个具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
某一个项目 ID：指定项目查询时，显示为项目 ID
all：账号维度数据明细
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def BillingData(self):
        """计费数据详情
        :rtype: list of CdnData
        """
        return self._BillingData

    @BillingData.setter
    def BillingData(self, BillingData):
        self._BillingData = BillingData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("BillingData") is not None:
            self._BillingData = []
            for item in params.get("BillingData"):
                obj = CdnData()
                obj._deserialize(item)
                self._BillingData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceData(AbstractModel):
    """查询对象及其对应的访问明细数据

    """

    def __init__(self):
        r"""
        :param _Resource: 资源名称，根据查询条件不同分为以下几类：
单域名：指定单域名查询，表示该域名明细数据，当传入参数 detail 指定为 true 时，显示该域名（ detail 参数默认为 false ）
多域名：指定多个域名查询，表示多域名汇总明细数据，显示 multiDomains
项目 ID：指定项目查询时，表示该项目下的域名汇总明细数据，显示该项目 ID
all：账号维度明细数据，即账号下所有域名的汇总明细数据
        :type Resource: str
        :param _CdnData: 资源对应的数据明细
        :type CdnData: list of CdnData
        """
        self._Resource = None
        self._CdnData = None

    @property
    def Resource(self):
        """资源名称，根据查询条件不同分为以下几类：
单域名：指定单域名查询，表示该域名明细数据，当传入参数 detail 指定为 true 时，显示该域名（ detail 参数默认为 false ）
多域名：指定多个域名查询，表示多域名汇总明细数据，显示 multiDomains
项目 ID：指定项目查询时，表示该项目下的域名汇总明细数据，显示该项目 ID
all：账号维度明细数据，即账号下所有域名的汇总明细数据
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def CdnData(self):
        """资源对应的数据明细
        :rtype: list of CdnData
        """
        return self._CdnData

    @CdnData.setter
    def CdnData(self, CdnData):
        self._CdnData = CdnData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("CdnData") is not None:
            self._CdnData = []
            for item in params.get("CdnData"):
                obj = CdnData()
                obj._deserialize(item)
                self._CdnData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceOriginData(AbstractModel):
    """查询对象及其对应的回源明细数据

    """

    def __init__(self):
        r"""
        :param _Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :type Resource: str
        :param _OriginData: 回源数据详情
        :type OriginData: list of CdnData
        """
        self._Resource = None
        self._OriginData = None

    @property
    def Resource(self):
        """资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def OriginData(self):
        """回源数据详情
        :rtype: list of CdnData
        """
        return self._OriginData

    @OriginData.setter
    def OriginData(self, OriginData):
        self._OriginData = OriginData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("OriginData") is not None:
            self._OriginData = []
            for item in params.get("OriginData"):
                obj = CdnData()
                obj._deserialize(item)
                self._OriginData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """自定义响应头配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 自定义响应头配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _HeaderRules: 自定义响应头规则
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self._Switch = None
        self._HeaderRules = None

    @property
    def Switch(self):
        """自定义响应头配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderRules(self):
        """自定义响应头规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of HttpHeaderPathRule
        """
        return self._HeaderRules

    @HeaderRules.setter
    def HeaderRules(self, HeaderRules):
        self._HeaderRules = HeaderRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("HeaderRules") is not None:
            self._HeaderRules = []
            for item in params.get("HeaderRules"):
                obj = HttpHeaderPathRule()
                obj._deserialize(item)
                self._HeaderRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeaderCache(AbstractModel):
    """源站头部缓存配置，默认为开启状态，缓存所有头部信息

    """

    def __init__(self):
        r"""
        :param _Switch: 源站头部缓存配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """源站头部缓存配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Revalidate(AbstractModel):
    """是否回源站校验

    """

    def __init__(self):
        r"""
        :param _Switch: 总是回源校验配置开关，取值有：
on：开启
off：关闭

注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Path: 只在特定请求路径回源站校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self._Switch = None
        self._Path = None

    @property
    def Switch(self):
        """总是回源校验配置开关，取值有：
on：开启
off：关闭

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Path(self):
        """只在特定请求路径回源站校验
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Path

    @Path.setter
    def Path(self, Path):
        self._Path = Path


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCache(AbstractModel):
    """缓存配置分路径版本。
    默认情况下所有文件缓存过期时间为 30 天
    默认情况下静态加速类型的域名 .php;.jsp;.asp;.aspx 不缓存

    """

    def __init__(self):
        r"""
        :param _RulePaths: CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _CacheConfig: 缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.RuleCacheConfig`
        """
        self._RulePaths = None
        self._RuleType = None
        self._CacheConfig = None

    @property
    def RulePaths(self):
        """CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def CacheConfig(self):
        """缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RuleCacheConfig`
        """
        return self._CacheConfig

    @CacheConfig.setter
    def CacheConfig(self, CacheConfig):
        self._CacheConfig = CacheConfig


    def _deserialize(self, params):
        self._RulePaths = params.get("RulePaths")
        self._RuleType = params.get("RuleType")
        if params.get("CacheConfig") is not None:
            self._CacheConfig = RuleCacheConfig()
            self._CacheConfig._deserialize(params.get("CacheConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCacheConfig(AbstractModel):
    """路径缓存缓存配置（三种缓存模式中选取一种）

    """

    def __init__(self):
        r"""
        :param _Cache: 缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigCache`
        :param _NoCache: 不缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigNoCache`
        :param _FollowOrigin: 遵循源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: :class:`tencentcloud.cdn.v20180606.models.CacheConfigFollowOrigin`
        """
        self._Cache = None
        self._NoCache = None
        self._FollowOrigin = None

    @property
    def Cache(self):
        """缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheConfigCache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def NoCache(self):
        """不缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheConfigNoCache`
        """
        return self._NoCache

    @NoCache.setter
    def NoCache(self, NoCache):
        self._NoCache = NoCache

    @property
    def FollowOrigin(self):
        """遵循源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheConfigFollowOrigin`
        """
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self._Cache = CacheConfigCache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self._NoCache = CacheConfigNoCache()
            self._NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self._FollowOrigin = CacheConfigFollowOrigin()
            self._FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleEngine(AbstractModel):
    """规则引擎配置

    """

    def __init__(self):
        r"""
        :param _Switch: 规则引擎配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _Content: 规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Content: str
        """
        self._Switch = None
        self._Content = None

    @property
    def Switch(self):
        """规则引擎配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Content(self):
        """规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Content

    @Content.setter
    def Content(self, Content):
        self._Content = Content


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Content = params.get("Content")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleQueryString(AbstractModel):
    """路径保留参数配置

    """

    def __init__(self):
        r"""
        :param _Switch: 路径保留参数配置开关，取值有：
on：开启，CacheKey由QueryString组成
off：关闭，CacheKey不由QueryString组成

注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Action: includeCustom 包含部分url参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _Value: 使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self._Switch = None
        self._Action = None
        self._Value = None

    @property
    def Switch(self):
        """路径保留参数配置开关，取值有：
on：开启，CacheKey由QueryString组成
off：关闭，CacheKey不由QueryString组成

注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Action(self):
        """includeCustom 包含部分url参数
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def Value(self):
        """使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Action = params.get("Action")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclConfig(AbstractModel):
    """SCDN访问控制

    """

    def __init__(self):
        r"""
        :param _Switch: SCDN访问控制配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _ScriptData: 新版本请使用AdvancedScriptData
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptData: list of ScdnAclGroup
        :param _ErrorPage: 错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        :param _AdvancedScriptData: Acl规则组，switch为on时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedScriptData: list of AdvancedScdnAclGroup
        """
        self._Switch = None
        self._ScriptData = None
        self._ErrorPage = None
        self._AdvancedScriptData = None

    @property
    def Switch(self):
        """SCDN访问控制配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def ScriptData(self):
        """新版本请使用AdvancedScriptData
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnAclGroup
        """
        return self._ScriptData

    @ScriptData.setter
    def ScriptData(self, ScriptData):
        self._ScriptData = ScriptData

    @property
    def ErrorPage(self):
        """错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def AdvancedScriptData(self):
        """Acl规则组，switch为on时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvancedScdnAclGroup
        """
        return self._AdvancedScriptData

    @AdvancedScriptData.setter
    def AdvancedScriptData(self, AdvancedScriptData):
        self._AdvancedScriptData = AdvancedScriptData


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("ScriptData") is not None:
            self._ScriptData = []
            for item in params.get("ScriptData"):
                obj = ScdnAclGroup()
                obj._deserialize(item)
                self._ScriptData.append(obj)
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("AdvancedScriptData") is not None:
            self._AdvancedScriptData = []
            for item in params.get("AdvancedScriptData"):
                obj = AdvancedScdnAclGroup()
                obj._deserialize(item)
                self._AdvancedScriptData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclGroup(AbstractModel):
    """SCDN精准访问控制配置

    """

    def __init__(self):
        r"""
        :param _RuleName: 规则名称
        :type RuleName: str
        :param _Configure: 具体配置
        :type Configure: list of ScdnAclRule
        :param _Result: 执行动作，intercept|redirect
        :type Result: str
        :param _Status: 规则是否生效，active|inactive
        :type Status: str
        :param _ErrorPage: 错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self._RuleName = None
        self._Configure = None
        self._Result = None
        self._Status = None
        self._ErrorPage = None

    @property
    def RuleName(self):
        """规则名称
        :rtype: str
        """
        return self._RuleName

    @RuleName.setter
    def RuleName(self, RuleName):
        self._RuleName = RuleName

    @property
    def Configure(self):
        """具体配置
        :rtype: list of ScdnAclRule
        """
        return self._Configure

    @Configure.setter
    def Configure(self, Configure):
        self._Configure = Configure

    @property
    def Result(self):
        """执行动作，intercept|redirect
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def Status(self):
        """规则是否生效，active|inactive
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ErrorPage(self):
        """错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage


    def _deserialize(self, params):
        self._RuleName = params.get("RuleName")
        if params.get("Configure") is not None:
            self._Configure = []
            for item in params.get("Configure"):
                obj = ScdnAclRule()
                obj._deserialize(item)
                self._Configure.append(obj)
        self._Result = params.get("Result")
        self._Status = params.get("Status")
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclRule(AbstractModel):
    """精准访问控制匹配规则

    """

    def __init__(self):
        r"""
        :param _MatchKey: 匹配关键字
        :type MatchKey: str
        :param _LogiOperator: 逻辑操作符，取值如下
        :type LogiOperator: str
        :param _MatchValue: 匹配值。
        :type MatchValue: str
        """
        self._MatchKey = None
        self._LogiOperator = None
        self._MatchValue = None

    @property
    def MatchKey(self):
        """匹配关键字
        :rtype: str
        """
        return self._MatchKey

    @MatchKey.setter
    def MatchKey(self, MatchKey):
        self._MatchKey = MatchKey

    @property
    def LogiOperator(self):
        """逻辑操作符，取值如下
        :rtype: str
        """
        return self._LogiOperator

    @LogiOperator.setter
    def LogiOperator(self, LogiOperator):
        self._LogiOperator = LogiOperator

    @property
    def MatchValue(self):
        """匹配值。
        :rtype: str
        """
        return self._MatchValue

    @MatchValue.setter
    def MatchValue(self, MatchValue):
        self._MatchValue = MatchValue


    def _deserialize(self, params):
        self._MatchKey = params.get("MatchKey")
        self._LogiOperator = params.get("LogiOperator")
        self._MatchValue = params.get("MatchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnBotConfig(AbstractModel):
    """bot配置类型

    """

    def __init__(self):
        r"""
        :param _Switch: Scdn bot配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _BotCookie: Bot cookie策略
注意：此字段可能返回 null，表示取不到有效值。
        :type BotCookie: list of BotCookie
        :param _BotJavaScript: Bot Js策略
注意：此字段可能返回 null，表示取不到有效值。
        :type BotJavaScript: list of BotJavaScript
        """
        self._Switch = None
        self._BotCookie = None
        self._BotJavaScript = None

    @property
    def Switch(self):
        """Scdn bot配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def BotCookie(self):
        """Bot cookie策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BotCookie
        """
        return self._BotCookie

    @BotCookie.setter
    def BotCookie(self, BotCookie):
        self._BotCookie = BotCookie

    @property
    def BotJavaScript(self):
        """Bot Js策略
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of BotJavaScript
        """
        return self._BotJavaScript

    @BotJavaScript.setter
    def BotJavaScript(self, BotJavaScript):
        self._BotJavaScript = BotJavaScript


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("BotCookie") is not None:
            self._BotCookie = []
            for item in params.get("BotCookie"):
                obj = BotCookie()
                obj._deserialize(item)
                self._BotCookie.append(obj)
        if params.get("BotJavaScript") is not None:
            self._BotJavaScript = []
            for item in params.get("BotJavaScript"):
                obj = BotJavaScript()
                obj._deserialize(item)
                self._BotJavaScript.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnCCRules(AbstractModel):
    """scdn 的自定义 cc 规则

    """

    def __init__(self):
        r"""
        :param _RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
        :type RuleType: str
        :param _RuleValue: 规则值
        :type RuleValue: list of str
        :param _Qps: 规则限频
        :type Qps: int
        :param _DetectionTime: 探测时长
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionTime: int
        :param _FrequencyLimit: 限频阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyLimit: int
        :param _PunishmentSwitch: IP 惩罚配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishmentSwitch: str
        :param _PunishmentTime: IP 惩罚时长
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishmentTime: int
        :param _Action: 执行动作，intercept|redirect
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param _RedirectUrl: 动作为 redirect 时，重定向的url
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        """
        self._RuleType = None
        self._RuleValue = None
        self._Qps = None
        self._DetectionTime = None
        self._FrequencyLimit = None
        self._PunishmentSwitch = None
        self._PunishmentTime = None
        self._Action = None
        self._RedirectUrl = None

    @property
    def RuleType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        """规则值
        :rtype: list of str
        """
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def Qps(self):
        """规则限频
        :rtype: int
        """
        return self._Qps

    @Qps.setter
    def Qps(self, Qps):
        self._Qps = Qps

    @property
    def DetectionTime(self):
        """探测时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._DetectionTime

    @DetectionTime.setter
    def DetectionTime(self, DetectionTime):
        self._DetectionTime = DetectionTime

    @property
    def FrequencyLimit(self):
        """限频阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._FrequencyLimit

    @FrequencyLimit.setter
    def FrequencyLimit(self, FrequencyLimit):
        self._FrequencyLimit = FrequencyLimit

    @property
    def PunishmentSwitch(self):
        """IP 惩罚配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PunishmentSwitch

    @PunishmentSwitch.setter
    def PunishmentSwitch(self, PunishmentSwitch):
        self._PunishmentSwitch = PunishmentSwitch

    @property
    def PunishmentTime(self):
        """IP 惩罚时长
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._PunishmentTime

    @PunishmentTime.setter
    def PunishmentTime(self, PunishmentTime):
        self._PunishmentTime = PunishmentTime

    @property
    def Action(self):
        """执行动作，intercept|redirect
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Action

    @Action.setter
    def Action(self, Action):
        self._Action = Action

    @property
    def RedirectUrl(self):
        """动作为 redirect 时，重定向的url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        self._Qps = params.get("Qps")
        self._DetectionTime = params.get("DetectionTime")
        self._FrequencyLimit = params.get("FrequencyLimit")
        self._PunishmentSwitch = params.get("PunishmentSwitch")
        self._PunishmentTime = params.get("PunishmentTime")
        self._Action = params.get("Action")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnConfig(AbstractModel):
    """cc的配置类型

    """

    def __init__(self):
        r"""
        :param _Switch: scdn cc配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _Rules: 自定义 cc 防护规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ScdnCCRules
        :param _AdvancedRules: 增强自定义 cc 防护规则
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedRules: list of AdvancedCCRules
        :param _GlobalAdvancedRules: 增强自定义 cc 防护规则， 全局
注意：此字段可能返回 null，表示取不到有效值。
        :type GlobalAdvancedRules: list of AdvancedCCRules
        """
        self._Switch = None
        self._Rules = None
        self._AdvancedRules = None
        self._GlobalAdvancedRules = None

    @property
    def Switch(self):
        """scdn cc配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Rules(self):
        """自定义 cc 防护规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnCCRules
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def AdvancedRules(self):
        """增强自定义 cc 防护规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvancedCCRules
        """
        return self._AdvancedRules

    @AdvancedRules.setter
    def AdvancedRules(self, AdvancedRules):
        self._AdvancedRules = AdvancedRules

    @property
    def GlobalAdvancedRules(self):
        """增强自定义 cc 防护规则， 全局
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of AdvancedCCRules
        """
        return self._GlobalAdvancedRules

    @GlobalAdvancedRules.setter
    def GlobalAdvancedRules(self, GlobalAdvancedRules):
        self._GlobalAdvancedRules = GlobalAdvancedRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ScdnCCRules()
                obj._deserialize(item)
                self._Rules.append(obj)
        if params.get("AdvancedRules") is not None:
            self._AdvancedRules = []
            for item in params.get("AdvancedRules"):
                obj = AdvancedCCRules()
                obj._deserialize(item)
                self._AdvancedRules.append(obj)
        if params.get("GlobalAdvancedRules") is not None:
            self._GlobalAdvancedRules = []
            for item in params.get("GlobalAdvancedRules"):
                obj = AdvancedCCRules()
                obj._deserialize(item)
                self._GlobalAdvancedRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnDdosConfig(AbstractModel):
    """ddos配置类型

    """

    def __init__(self):
        r"""
        :param _Switch: Scdn ddos配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """Scdn ddos配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnDomain(AbstractModel):
    """聚合了SCDN域名的基本信息

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Status: 当前状态，取值online | offline | process
        :type Status: str
        :param _Waf: Waf 状态默认为‘/’，取值 close | intercept | observe
        :type Waf: str
        :param _Acl: Acl 状态默认为‘/’，取值 close | open
        :type Acl: str
        :param _CC: CC 状态默认为‘/’，取值 close | open
        :type CC: str
        :param _Ddos: Ddos 状态默认为‘/’，取值 close | open
        :type Ddos: str
        :param _ProjectId: 项目ID
        :type ProjectId: str
        :param _AclRuleNumbers: Acl 规则数
        :type AclRuleNumbers: int
        :param _Bot: Bot 状态默认为‘/’，取值 close | open
        :type Bot: str
        :param _Area: 域名加速区域，取值global | mainland |  overseas
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param _WafLevel: waf规则等级，可取100|200|300
注意：此字段可能返回 null，表示取不到有效值。
        :type WafLevel: int
        """
        self._Domain = None
        self._Status = None
        self._Waf = None
        self._Acl = None
        self._CC = None
        self._Ddos = None
        self._ProjectId = None
        self._AclRuleNumbers = None
        self._Bot = None
        self._Area = None
        self._WafLevel = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Status(self):
        """当前状态，取值online | offline | process
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def Waf(self):
        """Waf 状态默认为‘/’，取值 close | intercept | observe
        :rtype: str
        """
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def Acl(self):
        """Acl 状态默认为‘/’，取值 close | open
        :rtype: str
        """
        return self._Acl

    @Acl.setter
    def Acl(self, Acl):
        self._Acl = Acl

    @property
    def CC(self):
        """CC 状态默认为‘/’，取值 close | open
        :rtype: str
        """
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def Ddos(self):
        """Ddos 状态默认为‘/’，取值 close | open
        :rtype: str
        """
        return self._Ddos

    @Ddos.setter
    def Ddos(self, Ddos):
        self._Ddos = Ddos

    @property
    def ProjectId(self):
        """项目ID
        :rtype: str
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def AclRuleNumbers(self):
        """Acl 规则数
        :rtype: int
        """
        return self._AclRuleNumbers

    @AclRuleNumbers.setter
    def AclRuleNumbers(self, AclRuleNumbers):
        self._AclRuleNumbers = AclRuleNumbers

    @property
    def Bot(self):
        """Bot 状态默认为‘/’，取值 close | open
        :rtype: str
        """
        return self._Bot

    @Bot.setter
    def Bot(self, Bot):
        self._Bot = Bot

    @property
    def Area(self):
        """域名加速区域，取值global | mainland |  overseas
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def WafLevel(self):
        """waf规则等级，可取100|200|300
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._WafLevel

    @WafLevel.setter
    def WafLevel(self, WafLevel):
        self._WafLevel = WafLevel


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Status = params.get("Status")
        self._Waf = params.get("Waf")
        self._Acl = params.get("Acl")
        self._CC = params.get("CC")
        self._Ddos = params.get("Ddos")
        self._ProjectId = params.get("ProjectId")
        self._AclRuleNumbers = params.get("AclRuleNumbers")
        self._Bot = params.get("Bot")
        self._Area = params.get("Area")
        self._WafLevel = params.get("WafLevel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnErrorPage(AbstractModel):
    """acl的错误页面

    """

    def __init__(self):
        r"""
        :param _RedirectCode: 状态码
执行动作为：intercept 默认传值 403
执行动作为：redirect 默认传值 301
        :type RedirectCode: int
        :param _RedirectUrl: 重定向url
        :type RedirectUrl: str
        """
        self._RedirectCode = None
        self._RedirectUrl = None

    @property
    def RedirectCode(self):
        """状态码
执行动作为：intercept 默认传值 403
执行动作为：redirect 默认传值 301
        :rtype: int
        """
        return self._RedirectCode

    @RedirectCode.setter
    def RedirectCode(self, RedirectCode):
        self._RedirectCode = RedirectCode

    @property
    def RedirectUrl(self):
        """重定向url
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl


    def _deserialize(self, params):
        self._RedirectCode = params.get("RedirectCode")
        self._RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnEventLogConditions(AbstractModel):
    """SCDN 事件日志查询条件

    """

    def __init__(self):
        r"""
        :param _Key: 匹配关键字，ip, attack_location
        :type Key: str
        :param _Operator: 逻辑操作符，取值 exclude, include
        :type Operator: str
        :param _Value: 匹配值，允许使用通配符(*)查询，匹配零个、单个、多个字符，例如 1.2.*
        :type Value: str
        """
        self._Key = None
        self._Operator = None
        self._Value = None

    @property
    def Key(self):
        """匹配关键字，ip, attack_location
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Operator(self):
        """逻辑操作符，取值 exclude, include
        :rtype: str
        """
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Value(self):
        """匹配值，允许使用通配符(*)查询，匹配零个、单个、多个字符，例如 1.2.*
        :rtype: str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Operator = params.get("Operator")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnIpStrategy(AbstractModel):
    """scdn的IP白名单策略

    """

    def __init__(self):
        r"""
        :param _Domain: 域名|global表示全部域名
        :type Domain: str
        :param _StrategyId: 策略ID
        :type StrategyId: str
        :param _IpList: IP白名单列表
        :type IpList: list of str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        :param _Remark: 备注
        :type Remark: str
        :param _RuleType: 规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RuleValue: 规则值
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleValue: list of str
        """
        self._Domain = None
        self._StrategyId = None
        self._IpList = None
        self._UpdateTime = None
        self._Remark = None
        self._RuleType = None
        self._RuleValue = None

    @property
    def Domain(self):
        """域名|global表示全部域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StrategyId(self):
        """策略ID
        :rtype: str
        """
        return self._StrategyId

    @StrategyId.setter
    def StrategyId(self, StrategyId):
        self._StrategyId = StrategyId

    @property
    def IpList(self):
        """IP白名单列表
        :rtype: list of str
        """
        return self._IpList

    @IpList.setter
    def IpList(self, IpList):
        self._IpList = IpList

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Remark(self):
        """备注
        :rtype: str
        """
        return self._Remark

    @Remark.setter
    def Remark(self, Remark):
        self._Remark = Remark

    @property
    def RuleType(self):
        """规则类型
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RuleValue(self):
        """规则值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._StrategyId = params.get("StrategyId")
        self._IpList = params.get("IpList")
        self._UpdateTime = params.get("UpdateTime")
        self._Remark = params.get("Remark")
        self._RuleType = params.get("RuleType")
        self._RuleValue = params.get("RuleValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnIpStrategyFilter(AbstractModel):
    """IP策略查询过滤参数

    """

    def __init__(self):
        r"""
        :param _Name: 过滤字段名，支持domain, ip
        :type Name: str
        :param _Value: 过滤字段值
        :type Value: list of str
        :param _Fuzzy: 是否启用模糊查询，仅支持过滤字段名为domain。
模糊查询时，Value长度最大为1
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        """过滤字段名，支持domain, ip
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """过滤字段值
        :rtype: list of str
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
        """是否启用模糊查询，仅支持过滤字段名为domain。
模糊查询时，Value长度最大为1
        :rtype: bool
        """
        return self._Fuzzy

    @Fuzzy.setter
    def Fuzzy(self, Fuzzy):
        self._Fuzzy = Fuzzy


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnLogTaskDetail(AbstractModel):
    """SCDN日志事件详细信息

    """

    def __init__(self):
        r"""
        :param _Domain: scdn域名
        :type Domain: str
        :param _Mode: 防护类型
        :type Mode: str
        :param _StartTime: 查询任务开始时间
        :type StartTime: str
        :param _EndTime: 查询任务结束时间
        :type EndTime: str
        :param _CreateTime: 任务创建时间
        :type CreateTime: str
        :param _DownloadUrl: 日志包下载链接
成功返回下载链接，其他情况返回'-'
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param _Status: 任务状态
created->任务已经创建
processing->任务正在执行
done->任务执行成功
failed->任务执行失败
no-log->没有日志产生
        :type Status: str
        :param _TaskID: 日志任务唯一id
        :type TaskID: str
        :param _AttackType: 攻击类型, 可以为"all"
AttackType映射如下:
  other = '未知类型'
  malicious_scan = "恶意扫描"
  sql_inject = "SQL注入攻击"
  xss = "XSS攻击"
  cmd_inject = "命令注入攻击"
  ldap_inject = "LDAP注入攻击"
  ssi_inject = "SSI注入攻击"
  xml_inject = "XML注入攻击"
  web_service = "WEB服务漏洞攻击"
  web_app = "WEB应用漏洞攻击"
  path_traversal = "路径跨越攻击"
  illegal_access_core_file = "核心文件非法访问"
  file_upload = "文件上传攻击"
  trojan_horse = "木马后门攻击"
  csrf = "CSRF攻击"
  custom_policy = "自定义策略"
  ai_engine= 'AI引擎检出'
  malicious_file_upload= '恶意文件上传'
        :type AttackType: str
        :param _DefenceMode: 防御模式,可以为"all"
DefenceMode映射如下：
  observe = '观察模式'
  intercept = '防御模式'
        :type DefenceMode: str
        :param _Conditions: 查询条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of ScdnEventLogConditions
        :param _Area: mainland或overseas
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
        self._Domain = None
        self._Mode = None
        self._StartTime = None
        self._EndTime = None
        self._CreateTime = None
        self._DownloadUrl = None
        self._Status = None
        self._TaskID = None
        self._AttackType = None
        self._DefenceMode = None
        self._Conditions = None
        self._Area = None

    @property
    def Domain(self):
        """scdn域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Mode(self):
        """防护类型
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def StartTime(self):
        """查询任务开始时间
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """查询任务结束时间
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def CreateTime(self):
        """任务创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def DownloadUrl(self):
        """日志包下载链接
成功返回下载链接，其他情况返回'-'
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def Status(self):
        """任务状态
created->任务已经创建
processing->任务正在执行
done->任务执行成功
failed->任务执行失败
no-log->没有日志产生
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def TaskID(self):
        """日志任务唯一id
        :rtype: str
        """
        return self._TaskID

    @TaskID.setter
    def TaskID(self, TaskID):
        self._TaskID = TaskID

    @property
    def AttackType(self):
        """攻击类型, 可以为"all"
AttackType映射如下:
  other = '未知类型'
  malicious_scan = "恶意扫描"
  sql_inject = "SQL注入攻击"
  xss = "XSS攻击"
  cmd_inject = "命令注入攻击"
  ldap_inject = "LDAP注入攻击"
  ssi_inject = "SSI注入攻击"
  xml_inject = "XML注入攻击"
  web_service = "WEB服务漏洞攻击"
  web_app = "WEB应用漏洞攻击"
  path_traversal = "路径跨越攻击"
  illegal_access_core_file = "核心文件非法访问"
  file_upload = "文件上传攻击"
  trojan_horse = "木马后门攻击"
  csrf = "CSRF攻击"
  custom_policy = "自定义策略"
  ai_engine= 'AI引擎检出'
  malicious_file_upload= '恶意文件上传'
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def DefenceMode(self):
        """防御模式,可以为"all"
DefenceMode映射如下：
  observe = '观察模式'
  intercept = '防御模式'
        :rtype: str
        """
        return self._DefenceMode

    @DefenceMode.setter
    def DefenceMode(self, DefenceMode):
        self._DefenceMode = DefenceMode

    @property
    def Conditions(self):
        """查询条件
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnEventLogConditions
        """
        return self._Conditions

    @Conditions.setter
    def Conditions(self, Conditions):
        self._Conditions = Conditions

    @property
    def Area(self):
        """mainland或overseas
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Mode = params.get("Mode")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._CreateTime = params.get("CreateTime")
        self._DownloadUrl = params.get("DownloadUrl")
        self._Status = params.get("Status")
        self._TaskID = params.get("TaskID")
        self._AttackType = params.get("AttackType")
        self._DefenceMode = params.get("DefenceMode")
        if params.get("Conditions") is not None:
            self._Conditions = []
            for item in params.get("Conditions"):
                obj = ScdnEventLogConditions()
                obj._deserialize(item)
                self._Conditions.append(obj)
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnSevenLayerRules(AbstractModel):
    """Scdn的七层限频配置

    """

    def __init__(self):
        r"""
        :param _CaseSensitive: 区分大小写
        :type CaseSensitive: bool
        :param _RuleType: 规则类型：
protocol：协议，填写 HTTP/HTTPS
method：请求方法，支持 HEAD、GET、POST、PUT、OPTIONS、TRACE、DELETE、PATCH、CONNECT
all：域名 匹配内容固定为"*",不可编辑修改
ip：IP 填写 CIDR 表达式
directory：路径，以/开头，支持目录和具体路径，128字符以内
index：首页 默认固定值：/;/index.html,不可编辑修改
path：文件全路径，资源地址，如/acb/test.png，支持通配符，如/abc/*.jpg
file：文件扩展名，填写具体扩展名，如 jpg;png;css
param：请求参数，填写具体 value 值，512字符以内
referer：Referer，填写具体 value 值，512字符以内
cookie：Cookie，填写具体 value 值，512字符以内
user-agent：User-Agent，填写具体 value 值，512字符以内
head：自定义请求头，填写具体value值，512字符以内；内容为空或者不存在时，无匹配内容输入框，填写匹配参数即可
        :type RuleType: str
        :param _LogicOperator: 逻辑操作符，取值 ：
不包含：exclude, 
包含：include, 
不等于：notequal, 
等于：equal, 
前缀匹配：matching
内容为空或不存在：null
        :type LogicOperator: str
        :param _RuleValue: 规则值
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleValue: list of str
        :param _RuleParam: 匹配参数，只有请求参数、Cookie、自定义请求头 有值
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleParam: str
        """
        self._CaseSensitive = None
        self._RuleType = None
        self._LogicOperator = None
        self._RuleValue = None
        self._RuleParam = None

    @property
    def CaseSensitive(self):
        """区分大小写
        :rtype: bool
        """
        return self._CaseSensitive

    @CaseSensitive.setter
    def CaseSensitive(self, CaseSensitive):
        self._CaseSensitive = CaseSensitive

    @property
    def RuleType(self):
        """规则类型：
protocol：协议，填写 HTTP/HTTPS
method：请求方法，支持 HEAD、GET、POST、PUT、OPTIONS、TRACE、DELETE、PATCH、CONNECT
all：域名 匹配内容固定为"*",不可编辑修改
ip：IP 填写 CIDR 表达式
directory：路径，以/开头，支持目录和具体路径，128字符以内
index：首页 默认固定值：/;/index.html,不可编辑修改
path：文件全路径，资源地址，如/acb/test.png，支持通配符，如/abc/*.jpg
file：文件扩展名，填写具体扩展名，如 jpg;png;css
param：请求参数，填写具体 value 值，512字符以内
referer：Referer，填写具体 value 值，512字符以内
cookie：Cookie，填写具体 value 值，512字符以内
user-agent：User-Agent，填写具体 value 值，512字符以内
head：自定义请求头，填写具体value值，512字符以内；内容为空或者不存在时，无匹配内容输入框，填写匹配参数即可
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def LogicOperator(self):
        """逻辑操作符，取值 ：
不包含：exclude, 
包含：include, 
不等于：notequal, 
等于：equal, 
前缀匹配：matching
内容为空或不存在：null
        :rtype: str
        """
        return self._LogicOperator

    @LogicOperator.setter
    def LogicOperator(self, LogicOperator):
        self._LogicOperator = LogicOperator

    @property
    def RuleValue(self):
        """规则值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RuleValue

    @RuleValue.setter
    def RuleValue(self, RuleValue):
        self._RuleValue = RuleValue

    @property
    def RuleParam(self):
        """匹配参数，只有请求参数、Cookie、自定义请求头 有值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleParam

    @RuleParam.setter
    def RuleParam(self, RuleParam):
        self._RuleParam = RuleParam


    def _deserialize(self, params):
        self._CaseSensitive = params.get("CaseSensitive")
        self._RuleType = params.get("RuleType")
        self._LogicOperator = params.get("LogicOperator")
        self._RuleValue = params.get("RuleValue")
        self._RuleParam = params.get("RuleParam")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTopData(AbstractModel):
    """SCDN攻击数据Top展示

    """

    def __init__(self):
        r"""
        :param _Time: 时间
        :type Time: str
        :param _Value: 数值
        :type Value: int
        :param _Isp: 运营商
        :type Isp: str
        :param _Ip: IP地址
        :type Ip: str
        :param _District: 区域
        :type District: str
        """
        self._Time = None
        self._Value = None
        self._Isp = None
        self._Ip = None
        self._District = None

    @property
    def Time(self):
        """时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """数值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Isp(self):
        """运营商
        :rtype: str
        """
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def Ip(self):
        """IP地址
        :rtype: str
        """
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def District(self):
        """区域
        :rtype: str
        """
        return self._District

    @District.setter
    def District(self, District):
        self._District = District


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        self._Isp = params.get("Isp")
        self._Ip = params.get("Ip")
        self._District = params.get("District")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTopDomainData(AbstractModel):
    """SCDN攻击数据Top展示

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Value: 请求量
        :type Value: int
        :param _Percent: 百分比
        :type Percent: float
        """
        self._Domain = None
        self._Value = None
        self._Percent = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Value(self):
        """请求量
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Percent(self):
        """百分比
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._Value = params.get("Value")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTopUrlData(AbstractModel):
    """SCDN攻击数据Top URL展示

    """

    def __init__(self):
        r"""
        :param _Url: Top数据的URL
        :type Url: str
        :param _Value: 数值
        :type Value: int
        :param _Time: 时间
        :type Time: str
        :param _Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self._Url = None
        self._Value = None
        self._Time = None
        self._Domain = None

    @property
    def Url(self):
        """Top数据的URL
        :rtype: str
        """
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Value(self):
        """数值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Time(self):
        """时间
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Domain(self):
        """域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Url = params.get("Url")
        self._Value = params.get("Value")
        self._Time = params.get("Time")
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTypeData(AbstractModel):
    """Scdn饼图数据，waf仅有

    """

    def __init__(self):
        r"""
        :param _AttackType: 攻击类型
        :type AttackType: str
        :param _Value: 攻击值
        :type Value: int
        """
        self._AttackType = None
        self._Value = None

    @property
    def AttackType(self):
        """攻击类型
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Value(self):
        """攻击值
        :rtype: int
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._AttackType = params.get("AttackType")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafConfig(AbstractModel):
    """waf配置类型

    """

    def __init__(self):
        r"""
        :param _Switch: Scdn waf配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _Mode: intercept|observe，默认intercept
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param _ErrorPage: 重定向的错误页面
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        :param _WebShellSwitch: webshell拦截配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type WebShellSwitch: str
        :param _Rules: 类型拦截规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ScdnWafRule
        :param _Level: waf规则等级，可取100|200|300
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param _SubRuleSwitch: waf子规则配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type SubRuleSwitch: list of WafSubRuleStatus
        """
        self._Switch = None
        self._Mode = None
        self._ErrorPage = None
        self._WebShellSwitch = None
        self._Rules = None
        self._Level = None
        self._SubRuleSwitch = None

    @property
    def Switch(self):
        """Scdn waf配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Mode(self):
        """intercept|observe，默认intercept
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Mode

    @Mode.setter
    def Mode(self, Mode):
        self._Mode = Mode

    @property
    def ErrorPage(self):
        """重定向的错误页面
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def WebShellSwitch(self):
        """webshell拦截配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._WebShellSwitch

    @WebShellSwitch.setter
    def WebShellSwitch(self, WebShellSwitch):
        self._WebShellSwitch = WebShellSwitch

    @property
    def Rules(self):
        """类型拦截规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of ScdnWafRule
        """
        return self._Rules

    @Rules.setter
    def Rules(self, Rules):
        self._Rules = Rules

    @property
    def Level(self):
        """waf规则等级，可取100|200|300
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Level

    @Level.setter
    def Level(self, Level):
        self._Level = Level

    @property
    def SubRuleSwitch(self):
        """waf子规则配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of WafSubRuleStatus
        """
        return self._SubRuleSwitch

    @SubRuleSwitch.setter
    def SubRuleSwitch(self, SubRuleSwitch):
        self._SubRuleSwitch = SubRuleSwitch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Mode = params.get("Mode")
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ScdnErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        self._WebShellSwitch = params.get("WebShellSwitch")
        if params.get("Rules") is not None:
            self._Rules = []
            for item in params.get("Rules"):
                obj = ScdnWafRule()
                obj._deserialize(item)
                self._Rules.append(obj)
        self._Level = params.get("Level")
        if params.get("SubRuleSwitch") is not None:
            self._SubRuleSwitch = []
            for item in params.get("SubRuleSwitch"):
                obj = WafSubRuleStatus()
                obj._deserialize(item)
                self._SubRuleSwitch.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafRule(AbstractModel):
    """Waf 规则信息

    """

    def __init__(self):
        r"""
        :param _AttackType: 攻击类型
        :type AttackType: str
        :param _Operate: 防护措施，observe
        :type Operate: str
        """
        self._AttackType = None
        self._Operate = None

    @property
    def AttackType(self):
        """攻击类型
        :rtype: str
        """
        return self._AttackType

    @AttackType.setter
    def AttackType(self, AttackType):
        self._AttackType = AttackType

    @property
    def Operate(self):
        """防护措施，observe
        :rtype: str
        """
        return self._Operate

    @Operate.setter
    def Operate(self, Operate):
        self._Operate = Operate


    def _deserialize(self, params):
        self._AttackType = params.get("AttackType")
        self._Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemeKey(AbstractModel):
    """作为CacheKey的一部分

    """

    def __init__(self):
        r"""
        :param _Switch: scheme作为cache key配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """scheme作为cache key配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog请求参数结构体

    """

    def __init__(self):
        r"""
        :param _LogsetId: 需要查询的日志集ID
        :type LogsetId: str
        :param _TopicIds: 需要查询的日志主题ID组合，以逗号分隔
        :type TopicIds: str
        :param _StartTime: 需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS
        :type StartTime: str
        :param _EndTime: 需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS
        :type EndTime: str
        :param _Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param _Channel: 接入渠道，cdn或者ecdn，默认值为cdn
        :type Channel: str
        :param _Query: 需要查询的内容，详情请参考https://cloud.tencent.com/document/product/614/16982
        :type Query: str
        :param _Context: 加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :type Context: str
        :param _Sort: 按日志时间排序， asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        """
        self._LogsetId = None
        self._TopicIds = None
        self._StartTime = None
        self._EndTime = None
        self._Limit = None
        self._Channel = None
        self._Query = None
        self._Context = None
        self._Sort = None

    @property
    def LogsetId(self):
        """需要查询的日志集ID
        :rtype: str
        """
        return self._LogsetId

    @LogsetId.setter
    def LogsetId(self, LogsetId):
        self._LogsetId = LogsetId

    @property
    def TopicIds(self):
        """需要查询的日志主题ID组合，以逗号分隔
        :rtype: str
        """
        return self._TopicIds

    @TopicIds.setter
    def TopicIds(self, TopicIds):
        self._TopicIds = TopicIds

    @property
    def StartTime(self):
        """需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS
        :rtype: str
        """
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        """需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS
        :rtype: str
        """
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Limit(self):
        """单次要返回的日志条数，单次返回的最大条数为100
        :rtype: int
        """
        return self._Limit

    @Limit.setter
    def Limit(self, Limit):
        self._Limit = Limit

    @property
    def Channel(self):
        """接入渠道，cdn或者ecdn，默认值为cdn
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Query(self):
        """需要查询的内容，详情请参考https://cloud.tencent.com/document/product/614/16982
        :rtype: str
        """
        return self._Query

    @Query.setter
    def Query(self, Query):
        self._Query = Query

    @property
    def Context(self):
        """加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :rtype: str
        """
        return self._Context

    @Context.setter
    def Context(self, Context):
        self._Context = Context

    @property
    def Sort(self):
        """按日志时间排序， asc（升序）或者 desc（降序），默认为 desc
        :rtype: str
        """
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort


    def _deserialize(self, params):
        self._LogsetId = params.get("LogsetId")
        self._TopicIds = params.get("TopicIds")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Limit = params.get("Limit")
        self._Channel = params.get("Channel")
        self._Query = params.get("Query")
        self._Context = params.get("Context")
        self._Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Logs: 查询结果
        :type Logs: :class:`tencentcloud.cdn.v20180606.models.ClsSearchLogs`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Logs = None
        self._RequestId = None

    @property
    def Logs(self):
        """查询结果
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ClsSearchLogs`
        """
        return self._Logs

    @Logs.setter
    def Logs(self, Logs):
        self._Logs = Logs

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Logs") is not None:
            self._Logs = ClsSearchLogs()
            self._Logs._deserialize(params.get("Logs"))
        self._RequestId = params.get("RequestId")


class SecurityConfig(AbstractModel):
    """scdn相关的配置

    """

    def __init__(self):
        r"""
        :param _Switch: scdn 安全配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """scdn 安全配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Seo(AbstractModel):
    """SEO 搜索引擎优化配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: SEO 搜索引擎优化配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """SEO 搜索引擎优化配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ServerCert(AbstractModel):
    """https 加速服务端证书配置：
    + 支持使用托管至 SSL 证书管理的证书进行部署
    + 支持上传 PEM 格式的证书进行部署

    """

    def __init__(self):
        r"""
        :param _CertId: 服务器证书 ID 在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _CertName: 服务器证书名称
在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param _Certificate: 服务器证书信息
上传自有证书时必填，需要包含完整的证书链
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param _PrivateKey: 服务器密钥信息
上传自有证书时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param _ExpireTime: 证书过期时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DeployTime: 证书颁发时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param _Message: 证书备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        :param _From: 证书来源
注意：此字段可能返回 null，表示取不到有效值。
        :type From: str
        """
        self._CertId = None
        self._CertName = None
        self._Certificate = None
        self._PrivateKey = None
        self._ExpireTime = None
        self._DeployTime = None
        self._Message = None
        self._From = None

    @property
    def CertId(self):
        """服务器证书 ID 在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        """服务器证书名称
在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Certificate(self):
        """服务器证书信息
上传自有证书时必填，需要包含完整的证书链
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def PrivateKey(self):
        """服务器密钥信息
上传自有证书时必填
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def ExpireTime(self):
        """证书过期时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        """证书颁发时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Message(self):
        """证书备注信息
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message

    @property
    def From(self):
        """证书来源
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._From

    @From.setter
    def From(self, From):
        self._From = From


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._Certificate = params.get("Certificate")
        self._PrivateKey = params.get("PrivateKey")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._Message = params.get("Message")
        self._From = params.get("From")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ShareCname(AbstractModel):
    """ShareCname配置
    ShareCname 为内测功能,如需使用,请联系腾讯云工程师开白.

    """

    def __init__(self):
        r"""
        :param _Switch: ShareCname 配置开关, 取值有：
on：开启，使用共享CNAME
off：关闭，使用默认CNAME

        :type Switch: str
        :param _Cname: 设置共享CNAME.
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        """
        self._Switch = None
        self._Cname = None

    @property
    def Switch(self):
        """ShareCname 配置开关, 取值有：
on：开启，使用共享CNAME
off：关闭，使用默认CNAME

        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Cname(self):
        """设置共享CNAME.
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Cname = params.get("Cname")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleCache(AbstractModel):
    """缓存配置基础版本
    默认情况下所有文件缓存过期时间为 30 天
    默认情况下静态加速类型的域名 .php;.jsp;.asp;.aspx 不缓存
    注意：该版本不支持设置源站未返回 max-age 情况下的缓存过期规则设置

    """

    def __init__(self):
        r"""
        :param _CacheRules: 缓存过期时间规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheRules: list of SimpleCacheRule
        :param _FollowOrigin: 遵循源站 Cache-Control: max-age 配置
on：开启
off：关闭
开启后，未能匹配 CacheRules 规则的资源将根据源站返回的 max-age 值进行节点缓存；匹配了 CacheRules 规则的资源将按照 CacheRules 中设置的缓存过期时间在节点进行缓存
与 CompareMaxAge 冲突，不能同时开启
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        :param _IgnoreCacheControl: 强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param _IgnoreSetCookie: 忽略源站的Set-Cookie头部
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        :param _CompareMaxAge: 高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareMaxAge: str
        :param _Revalidate: 总是回源站校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Revalidate: :class:`tencentcloud.cdn.v20180606.models.Revalidate`
        """
        self._CacheRules = None
        self._FollowOrigin = None
        self._IgnoreCacheControl = None
        self._IgnoreSetCookie = None
        self._CompareMaxAge = None
        self._Revalidate = None

    @property
    def CacheRules(self):
        """缓存过期时间规则
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of SimpleCacheRule
        """
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules

    @property
    def FollowOrigin(self):
        """遵循源站 Cache-Control: max-age 配置
on：开启
off：关闭
开启后，未能匹配 CacheRules 规则的资源将根据源站返回的 max-age 值进行节点缓存；匹配了 CacheRules 规则的资源将按照 CacheRules 中设置的缓存过期时间在节点进行缓存
与 CompareMaxAge 冲突，不能同时开启
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin

    @property
    def IgnoreCacheControl(self):
        """强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreCacheControl

    @IgnoreCacheControl.setter
    def IgnoreCacheControl(self, IgnoreCacheControl):
        self._IgnoreCacheControl = IgnoreCacheControl

    @property
    def IgnoreSetCookie(self):
        """忽略源站的Set-Cookie头部
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._IgnoreSetCookie

    @IgnoreSetCookie.setter
    def IgnoreSetCookie(self, IgnoreSetCookie):
        self._IgnoreSetCookie = IgnoreSetCookie

    @property
    def CompareMaxAge(self):
        """高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CompareMaxAge

    @CompareMaxAge.setter
    def CompareMaxAge(self, CompareMaxAge):
        self._CompareMaxAge = CompareMaxAge

    @property
    def Revalidate(self):
        """总是回源站校验
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Revalidate`
        """
        return self._Revalidate

    @Revalidate.setter
    def Revalidate(self, Revalidate):
        self._Revalidate = Revalidate


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = SimpleCacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        self._FollowOrigin = params.get("FollowOrigin")
        self._IgnoreCacheControl = params.get("IgnoreCacheControl")
        self._IgnoreSetCookie = params.get("IgnoreSetCookie")
        self._CompareMaxAge = params.get("CompareMaxAge")
        if params.get("Revalidate") is not None:
            self._Revalidate = Revalidate()
            self._Revalidate._deserialize(params.get("Revalidate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleCacheRule(AbstractModel):
    """缓存过期规则配置

    """

    def __init__(self):
        r"""
        :param _CacheType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
        :type CacheType: str
        :param _CacheContents: CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
        :type CacheContents: list of str
        :param _CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
        :type CacheTime: int
        """
        self._CacheType = None
        self._CacheContents = None
        self._CacheTime = None

    @property
    def CacheType(self):
        """规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
        :rtype: str
        """
        return self._CacheType

    @CacheType.setter
    def CacheType(self, CacheType):
        self._CacheType = CacheType

    @property
    def CacheContents(self):
        """CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
        :rtype: list of str
        """
        return self._CacheContents

    @CacheContents.setter
    def CacheContents(self, CacheContents):
        self._CacheContents = CacheContents

    @property
    def CacheTime(self):
        """缓存过期时间设置
单位为秒，最大可设置为 365 天
        :rtype: int
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._CacheType = params.get("CacheType")
        self._CacheContents = params.get("CacheContents")
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """查询结果排序条件

    """

    def __init__(self):
        r"""
        :param _Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
默认createTime。
        :type Key: str
        :param _Sequence: asc/desc，默认desc。
        :type Sequence: str
        """
        self._Key = None
        self._Sequence = None

    @property
    def Key(self):
        """排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
默认createTime。
        :rtype: str
        """
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Sequence(self):
        """asc/desc，默认desc。
        :rtype: str
        """
        return self._Sequence

    @Sequence.setter
    def Sequence(self, Sequence):
        self._Sequence = Sequence


    def _deserialize(self, params):
        self._Key = params.get("Key")
        self._Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificConfig(AbstractModel):
    """域名国内海外分地区特殊配置。

    """

    def __init__(self):
        r"""
        :param _Mainland: 国内特殊配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mainland: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`
        :param _Overseas: 海外特殊配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Overseas: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`
        """
        self._Mainland = None
        self._Overseas = None

    @property
    def Mainland(self):
        """国内特殊配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`
        """
        return self._Mainland

    @Mainland.setter
    def Mainland(self, Mainland):
        self._Mainland = Mainland

    @property
    def Overseas(self):
        """海外特殊配置。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`
        """
        return self._Overseas

    @Overseas.setter
    def Overseas(self, Overseas):
        self._Overseas = Overseas


    def _deserialize(self, params):
        if params.get("Mainland") is not None:
            self._Mainland = MainlandConfig()
            self._Mainland._deserialize(params.get("Mainland"))
        if params.get("Overseas") is not None:
            self._Overseas = OverseaConfig()
            self._Overseas._deserialize(params.get("Overseas"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
域名状态需要为【已停用】
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
域名状态需要为【已停用】
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StartScdnDomainRequest(AbstractModel):
    """StartScdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartScdnDomainResponse(AbstractModel):
    """StartScdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 开启结果，Success表示成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """开启结果，Success表示成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class StatisticItem(AbstractModel):
    """累计用量封顶的配置

    """

    def __init__(self):
        r"""
        :param _Type: 封顶类型，累计用量total，瞬时用量moment
注意：此字段可能返回 null，表示取不到有效值。
        :type Type: str
        :param _UnBlockTime: 自动解封时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UnBlockTime: int
        :param _BpsThreshold: 带宽、流量阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type BpsThreshold: int
        :param _CounterMeasure: 关闭方式 返回404:RETURN_404
注意：此字段可能返回 null，表示取不到有效值。
        :type CounterMeasure: str
        :param _AlertPercentage: 触发提醒阈值百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertPercentage: int
        :param _AlertSwitch: 累计用量封顶告警配置，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type AlertSwitch: str
        :param _Metric: 指标类型，流量flux或带宽bandwidth
注意：此字段可能返回 null，表示取不到有效值。
        :type Metric: str
        :param _Cycle: 检测周期，单位分钟，60或1440
注意：此字段可能返回 null，表示取不到有效值。
        :type Cycle: int
        :param _Switch: 累计用量封顶配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Type = None
        self._UnBlockTime = None
        self._BpsThreshold = None
        self._CounterMeasure = None
        self._AlertPercentage = None
        self._AlertSwitch = None
        self._Metric = None
        self._Cycle = None
        self._Switch = None

    @property
    def Type(self):
        """封顶类型，累计用量total，瞬时用量moment
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def UnBlockTime(self):
        """自动解封时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._UnBlockTime

    @UnBlockTime.setter
    def UnBlockTime(self, UnBlockTime):
        self._UnBlockTime = UnBlockTime

    @property
    def BpsThreshold(self):
        """带宽、流量阈值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._BpsThreshold

    @BpsThreshold.setter
    def BpsThreshold(self, BpsThreshold):
        self._BpsThreshold = BpsThreshold

    @property
    def CounterMeasure(self):
        """关闭方式 返回404:RETURN_404
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CounterMeasure

    @CounterMeasure.setter
    def CounterMeasure(self, CounterMeasure):
        self._CounterMeasure = CounterMeasure

    @property
    def AlertPercentage(self):
        """触发提醒阈值百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._AlertPercentage

    @AlertPercentage.setter
    def AlertPercentage(self, AlertPercentage):
        self._AlertPercentage = AlertPercentage

    @property
    def AlertSwitch(self):
        """累计用量封顶告警配置，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._AlertSwitch

    @AlertSwitch.setter
    def AlertSwitch(self, AlertSwitch):
        self._AlertSwitch = AlertSwitch

    @property
    def Metric(self):
        """指标类型，流量flux或带宽bandwidth
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Metric

    @Metric.setter
    def Metric(self, Metric):
        self._Metric = Metric

    @property
    def Cycle(self):
        """检测周期，单位分钟，60或1440
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Cycle

    @Cycle.setter
    def Cycle(self, Cycle):
        self._Cycle = Cycle

    @property
    def Switch(self):
        """累计用量封顶配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Type = params.get("Type")
        self._UnBlockTime = params.get("UnBlockTime")
        self._BpsThreshold = params.get("BpsThreshold")
        self._CounterMeasure = params.get("CounterMeasure")
        self._AlertPercentage = params.get("AlertPercentage")
        self._AlertSwitch = params.get("AlertSwitch")
        self._Metric = params.get("Metric")
        self._Cycle = params.get("Cycle")
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusCodeCache(AbstractModel):
    """状态码缓存过期配置，默认情况下会对 404 状态码缓存 10 秒

    """

    def __init__(self):
        r"""
        :param _Switch: 状态码缓存过期配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _CacheRules: 状态码缓存过期规则明细
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheRules: list of StatusCodeCacheRule
        """
        self._Switch = None
        self._CacheRules = None

    @property
    def Switch(self):
        """状态码缓存过期配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def CacheRules(self):
        """状态码缓存过期规则明细
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of StatusCodeCacheRule
        """
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = StatusCodeCacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusCodeCacheRule(AbstractModel):
    """状态码缓存过期时间规则配置

    """

    def __init__(self):
        r"""
        :param _StatusCode: http 状态码
支持 403、404 状态码
        :type StatusCode: str
        :param _CacheTime: 状态码缓存过期时间，单位秒
        :type CacheTime: int
        """
        self._StatusCode = None
        self._CacheTime = None

    @property
    def StatusCode(self):
        """http 状态码
支持 403、404 状态码
        :rtype: str
        """
        return self._StatusCode

    @StatusCode.setter
    def StatusCode(self, StatusCode):
        self._StatusCode = StatusCode

    @property
    def CacheTime(self):
        """状态码缓存过期时间，单位秒
        :rtype: int
        """
        return self._CacheTime

    @CacheTime.setter
    def CacheTime(self, CacheTime):
        self._CacheTime = CacheTime


    def _deserialize(self, params):
        self._StatusCode = params.get("StatusCode")
        self._CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
域名需要为【已启动】状态
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
域名需要为【已启动】状态
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class StopScdnDomainRequest(AbstractModel):
    """StopScdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopScdnDomainResponse(AbstractModel):
    """StopScdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 关闭结果，Success表示成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """关闭结果，Success表示成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class SummarizedData(AbstractModel):
    """明细数据的汇总值，各指标根据其特性不同拥有不同汇总方式

    """

    def __init__(self):
        r"""
        :param _Name: 汇总方式，存在以下几种：
sum：累加求和
max：最大值，带宽模式下，采用 5 分钟粒度汇总数据，计算峰值带宽
avg：平均值
        :type Name: str
        :param _Value: 汇总后的数据值
        :type Value: float
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """汇总方式，存在以下几种：
sum：累加求和
max：最大值，带宽模式下，采用 5 分钟粒度汇总数据，计算峰值带宽
avg：平均值
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """汇总后的数据值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """域名标签配置

    """

    def __init__(self):
        r"""
        :param _TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param _TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
        :type TagValue: str
        """
        self._TagKey = None
        self._TagValue = None

    @property
    def TagKey(self):
        """标签键
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
        """标签值
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
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
        


class TimestampData(AbstractModel):
    """时间戳与其对应的数值

    """

    def __init__(self):
        r"""
        :param _Time: 数据统计时间点，采用向前汇总模式
以 5 分钟粒度为例，13:35:00 时间点代表的统计数据区间为 13:35:00 至 13:39:59
        :type Time: str
        :param _Value: 数据值
        :type Value: float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        """数据统计时间点，采用向前汇总模式
以 5 分钟粒度为例，13:35:00 时间点代表的统计数据区间为 13:35:00 至 13:39:59
        :rtype: str
        """
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
        """数据值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Time = params.get("Time")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopData(AbstractModel):
    """排序类型数据结构

    """

    def __init__(self):
        r"""
        :param _Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :type Resource: str
        :param _DetailData: 排序结果详情
        :type DetailData: list of TopDetailData
        """
        self._Resource = None
        self._DetailData = None

    @property
    def Resource(self):
        """资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DetailData(self):
        """排序结果详情
        :rtype: list of TopDetailData
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDataMore(AbstractModel):
    """排序类型数据结构

    """

    def __init__(self):
        r"""
        :param _Resource: 资源名称，根据查询条件不同分为以下几类：
        :type Resource: str
        :param _DetailData: 排序结果详情
        :type DetailData: list of TopDetailDataMore
        """
        self._Resource = None
        self._DetailData = None

    @property
    def Resource(self):
        """资源名称，根据查询条件不同分为以下几类：
        :rtype: str
        """
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DetailData(self):
        """排序结果详情
        :rtype: list of TopDetailDataMore
        """
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailDataMore()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """排序类型的数据结构

    """

    def __init__(self):
        r"""
        :param _Name: 数据类型的名称
        :type Name: str
        :param _Value: 数据值
        :type Value: float
        """
        self._Name = None
        self._Value = None

    @property
    def Name(self):
        """数据类型的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """数据值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailDataMore(AbstractModel):
    """排序类型的数据结构，同时附带上该项的在总值的占比

    """

    def __init__(self):
        r"""
        :param _Name: 数据类型的名称
        :type Name: str
        :param _Value: 数据值
        :type Value: float
        :param _Percent: 数据值在总值中的百分比
注意：此字段可能返回 null，表示取不到有效值。
        :type Percent: float
        """
        self._Name = None
        self._Value = None
        self._Percent = None

    @property
    def Name(self):
        """数据类型的名称
        :rtype: str
        """
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        """数据值
        :rtype: float
        """
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Percent(self):
        """数据值在总值中的百分比
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: float
        """
        return self._Percent

    @Percent.setter
    def Percent(self, Percent):
        self._Percent = Percent


    def _deserialize(self, params):
        self._Name = params.get("Name")
        self._Value = params.get("Value")
        self._Percent = params.get("Percent")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInfo(AbstractModel):
    """CLS主题信息

    """

    def __init__(self):
        r"""
        :param _TopicId: 主题ID
        :type TopicId: str
        :param _TopicName: 主题名字
        :type TopicName: str
        :param _Enabled: 是否启用投递
        :type Enabled: int
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _Channel: 归属于cdn或ecdn
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: str
        :param _Deleted: cls侧是否已经被删除
注意：此字段可能返回 null，表示取不到有效值。
        :type Deleted: str
        """
        self._TopicId = None
        self._TopicName = None
        self._Enabled = None
        self._CreateTime = None
        self._Channel = None
        self._Deleted = None

    @property
    def TopicId(self):
        """主题ID
        :rtype: str
        """
        return self._TopicId

    @TopicId.setter
    def TopicId(self, TopicId):
        self._TopicId = TopicId

    @property
    def TopicName(self):
        """主题名字
        :rtype: str
        """
        return self._TopicName

    @TopicName.setter
    def TopicName(self, TopicName):
        self._TopicName = TopicName

    @property
    def Enabled(self):
        """是否启用投递
        :rtype: int
        """
        return self._Enabled

    @Enabled.setter
    def Enabled(self, Enabled):
        self._Enabled = Enabled

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def Channel(self):
        """归属于cdn或ecdn
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Deleted(self):
        """cls侧是否已经被删除
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Deleted

    @Deleted.setter
    def Deleted(self, Deleted):
        self._Deleted = Deleted


    def _deserialize(self, params):
        self._TopicId = params.get("TopicId")
        self._TopicName = params.get("TopicName")
        self._Enabled = params.get("Enabled")
        self._CreateTime = params.get("CreateTime")
        self._Channel = params.get("Channel")
        self._Deleted = params.get("Deleted")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TpgAdapter(AbstractModel):
    """图片优化-TpgAdapter配置

    """

    def __init__(self):
        r"""
        :param _Switch: 图片优化-TpgAdapter配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """图片优化-TpgAdapter配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficPackage(AbstractModel):
    """CDN加速流量包。

    """

    def __init__(self):
        r"""
        :param _Id: 流量包 Id
        :type Id: int
        :param _Type: 流量包类型
        :type Type: str
        :param _Bytes: 流量包大小（单位为 Byte）
        :type Bytes: int
        :param _BytesUsed: 已消耗流量（单位为 Byte）
        :type BytesUsed: int
        :param _Status: 流量包状态
enabled：已启用
expired：已过期
disabled：未启用
        :type Status: str
        :param _CreateTime: 流量包发放时间
        :type CreateTime: str
        :param _EnableTime: 流量包生效时间
        :type EnableTime: str
        :param _ExpireTime: 流量包过期时间
        :type ExpireTime: str
        :param _ContractExtension: 流量包是否续订
        :type ContractExtension: bool
        :param _AutoExtension: 流量包是否自动续订
        :type AutoExtension: bool
        :param _Channel: 流量包来源
        :type Channel: str
        :param _Area: 流量包生效区域，mainland或overseas
        :type Area: str
        :param _LifeTimeMonth: 流量包生命周期月数
        :type LifeTimeMonth: int
        :param _ExtensionAvailable: 流量包是否支持续订
        :type ExtensionAvailable: bool
        :param _RefundAvailable: 流量包是否支持退费
        :type RefundAvailable: bool
        :param _Region: 流量包生效区域
0：中国大陆
1：亚太一区
2：亚太二区
3：亚太三区
4：中东
5：北美
6：欧洲
7：南美
8：非洲
注意：此字段可能返回 null，表示取不到有效值。
        :type Region: int
        :param _ConfigId: 流量包类型id
注意：此字段可能返回 null，表示取不到有效值。
        :type ConfigId: int
        :param _ExtensionMode: 流量包当前续订模式，0 未续订、1到期续订、2用完续订、3到期或用完续订
注意：此字段可能返回 null，表示取不到有效值。
        :type ExtensionMode: int
        :param _TrueEnableTime: 流量包实际生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrueEnableTime: str
        :param _TrueExpireTime: 流量包实际过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :type TrueExpireTime: str
        """
        self._Id = None
        self._Type = None
        self._Bytes = None
        self._BytesUsed = None
        self._Status = None
        self._CreateTime = None
        self._EnableTime = None
        self._ExpireTime = None
        self._ContractExtension = None
        self._AutoExtension = None
        self._Channel = None
        self._Area = None
        self._LifeTimeMonth = None
        self._ExtensionAvailable = None
        self._RefundAvailable = None
        self._Region = None
        self._ConfigId = None
        self._ExtensionMode = None
        self._TrueEnableTime = None
        self._TrueExpireTime = None

    @property
    def Id(self):
        """流量包 Id
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Type(self):
        """流量包类型
        :rtype: str
        """
        return self._Type

    @Type.setter
    def Type(self, Type):
        self._Type = Type

    @property
    def Bytes(self):
        """流量包大小（单位为 Byte）
        :rtype: int
        """
        return self._Bytes

    @Bytes.setter
    def Bytes(self, Bytes):
        self._Bytes = Bytes

    @property
    def BytesUsed(self):
        """已消耗流量（单位为 Byte）
        :rtype: int
        """
        return self._BytesUsed

    @BytesUsed.setter
    def BytesUsed(self, BytesUsed):
        self._BytesUsed = BytesUsed

    @property
    def Status(self):
        """流量包状态
enabled：已启用
expired：已过期
disabled：未启用
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        """流量包发放时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def EnableTime(self):
        """流量包生效时间
        :rtype: str
        """
        return self._EnableTime

    @EnableTime.setter
    def EnableTime(self, EnableTime):
        self._EnableTime = EnableTime

    @property
    def ExpireTime(self):
        """流量包过期时间
        :rtype: str
        """
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def ContractExtension(self):
        """流量包是否续订
        :rtype: bool
        """
        return self._ContractExtension

    @ContractExtension.setter
    def ContractExtension(self, ContractExtension):
        self._ContractExtension = ContractExtension

    @property
    def AutoExtension(self):
        """流量包是否自动续订
        :rtype: bool
        """
        return self._AutoExtension

    @AutoExtension.setter
    def AutoExtension(self, AutoExtension):
        self._AutoExtension = AutoExtension

    @property
    def Channel(self):
        """流量包来源
        :rtype: str
        """
        return self._Channel

    @Channel.setter
    def Channel(self, Channel):
        self._Channel = Channel

    @property
    def Area(self):
        """流量包生效区域，mainland或overseas
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def LifeTimeMonth(self):
        """流量包生命周期月数
        :rtype: int
        """
        return self._LifeTimeMonth

    @LifeTimeMonth.setter
    def LifeTimeMonth(self, LifeTimeMonth):
        self._LifeTimeMonth = LifeTimeMonth

    @property
    def ExtensionAvailable(self):
        """流量包是否支持续订
        :rtype: bool
        """
        return self._ExtensionAvailable

    @ExtensionAvailable.setter
    def ExtensionAvailable(self, ExtensionAvailable):
        self._ExtensionAvailable = ExtensionAvailable

    @property
    def RefundAvailable(self):
        """流量包是否支持退费
        :rtype: bool
        """
        return self._RefundAvailable

    @RefundAvailable.setter
    def RefundAvailable(self, RefundAvailable):
        self._RefundAvailable = RefundAvailable

    @property
    def Region(self):
        """流量包生效区域
0：中国大陆
1：亚太一区
2：亚太二区
3：亚太三区
4：中东
5：北美
6：欧洲
7：南美
8：非洲
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Region

    @Region.setter
    def Region(self, Region):
        self._Region = Region

    @property
    def ConfigId(self):
        """流量包类型id
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ConfigId

    @ConfigId.setter
    def ConfigId(self, ConfigId):
        self._ConfigId = ConfigId

    @property
    def ExtensionMode(self):
        """流量包当前续订模式，0 未续订、1到期续订、2用完续订、3到期或用完续订
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._ExtensionMode

    @ExtensionMode.setter
    def ExtensionMode(self, ExtensionMode):
        self._ExtensionMode = ExtensionMode

    @property
    def TrueEnableTime(self):
        """流量包实际生效时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TrueEnableTime

    @TrueEnableTime.setter
    def TrueEnableTime(self, TrueEnableTime):
        self._TrueEnableTime = TrueEnableTime

    @property
    def TrueExpireTime(self):
        """流量包实际过期时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._TrueExpireTime

    @TrueExpireTime.setter
    def TrueExpireTime(self, TrueExpireTime):
        self._TrueExpireTime = TrueExpireTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Type = params.get("Type")
        self._Bytes = params.get("Bytes")
        self._BytesUsed = params.get("BytesUsed")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        self._EnableTime = params.get("EnableTime")
        self._ExpireTime = params.get("ExpireTime")
        self._ContractExtension = params.get("ContractExtension")
        self._AutoExtension = params.get("AutoExtension")
        self._Channel = params.get("Channel")
        self._Area = params.get("Area")
        self._LifeTimeMonth = params.get("LifeTimeMonth")
        self._ExtensionAvailable = params.get("ExtensionAvailable")
        self._RefundAvailable = params.get("RefundAvailable")
        self._Region = params.get("Region")
        self._ConfigId = params.get("ConfigId")
        self._ExtensionMode = params.get("ExtensionMode")
        self._TrueEnableTime = params.get("TrueEnableTime")
        self._TrueExpireTime = params.get("TrueExpireTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _ProjectId: 项目 ID
        :type ProjectId: int
        :param _Origin: 源站配置
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param _IpFilter: IP 黑白名单配置
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param _IpFreqLimit: IP 限频配置
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param _StatusCodeCache: 状态码缓存配置
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param _Compression: 智能压缩配置
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param _BandwidthAlert: 带宽封顶配置
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param _RangeOriginPull: Range 回源配置
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param _FollowRedirect: 301/302 回源跟随配置
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param _ErrorPage: 错误码重定向配置（功能灰度中，尚未全量）
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param _RequestHeader: 回源请求头部配置
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param _ResponseHeader: 响应头部配置
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param _DownstreamCapping: 下载速度配置
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param _CacheKey: 节点缓存键配置
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param _ResponseHeaderCache: 头部缓存配置
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param _VideoSeek: 视频拖拽配置
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param _Cache: 缓存过期时间配置
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param _OriginPullOptimization: 跨国链路优化配置（已下线）
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param _Https: Https 加速配置
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param _Authentication: 时间戳防盗链配置
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param _Seo: SEO 优化配置
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param _ForceRedirect: 访问协议强制跳转配置
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param _Referer: Referer 防盗链配置
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param _MaxAge: 浏览器缓存配置（功能灰度中，尚未全量）
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param _SpecificConfig: 地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param _ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :type ServiceType: str
        :param _Area: 域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
从mainland/overseas修改至global时，域名的配置将被同步至overseas/mainland。若域名含有后端特殊配置，此类配置的同步过程有一定延时，请耐心等待
        :type Area: str
        :param _OriginPullTimeout: 回源超时配置
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param _AwsPrivateAccess: 回源S3私有鉴权
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param _UserAgentFilter: UA黑白名单配置
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param _AccessControl: 访问控制
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param _UrlRedirect: 访问URL重写配置
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param _AccessPort: 访问端口配置
        :type AccessPort: list of int
        :param _AdvancedAuthentication: 时间戳防盗链高级版配置，白名单功能
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param _OriginAuthentication: 回源鉴权高级版配置，白名单功能
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param _Ipv6Access: Ipv6 访问配置
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param _OfflineCache: 离线缓存
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param _OriginCombine: 合并回源
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param _PostMaxSize: POST请求传输配置
        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        :param _Quic: Quic访问（收费服务，详见计费说明和产品文档）
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        :param _OssPrivateAccess: 回源OSS私有鉴权
        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        :param _WebSocket: WebSocket配置
        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        :param _RemoteAuthentication: 远程鉴权配置
        :type RemoteAuthentication: :class:`tencentcloud.cdn.v20180606.models.RemoteAuthentication`
        :param _ShareCname: 共享CNAME配置，白名单功能
        :type ShareCname: :class:`tencentcloud.cdn.v20180606.models.ShareCname`
        :param _HwPrivateAccess: 华为云对象存储回源鉴权
        :type HwPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        :param _QnPrivateAccess: 七牛云对象存储回源鉴权
        :type QnPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        :param _OthersPrivateAccess: 其他厂商对象存储回源鉴权
        :type OthersPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        :param _HttpsBilling: HTTPS服务（收费服务，详见计费说明和产品文档）
        :type HttpsBilling: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        :param _ParamFilter: 参数黑名单
        :type ParamFilter: :class:`tencentcloud.cdn.v20180606.models.ParamFilter`
        """
        self._Domain = None
        self._ProjectId = None
        self._Origin = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._StatusCodeCache = None
        self._Compression = None
        self._BandwidthAlert = None
        self._RangeOriginPull = None
        self._FollowRedirect = None
        self._ErrorPage = None
        self._RequestHeader = None
        self._ResponseHeader = None
        self._DownstreamCapping = None
        self._CacheKey = None
        self._ResponseHeaderCache = None
        self._VideoSeek = None
        self._Cache = None
        self._OriginPullOptimization = None
        self._Https = None
        self._Authentication = None
        self._Seo = None
        self._ForceRedirect = None
        self._Referer = None
        self._MaxAge = None
        self._SpecificConfig = None
        self._ServiceType = None
        self._Area = None
        self._OriginPullTimeout = None
        self._AwsPrivateAccess = None
        self._UserAgentFilter = None
        self._AccessControl = None
        self._UrlRedirect = None
        self._AccessPort = None
        self._AdvancedAuthentication = None
        self._OriginAuthentication = None
        self._Ipv6Access = None
        self._OfflineCache = None
        self._OriginCombine = None
        self._PostMaxSize = None
        self._Quic = None
        self._OssPrivateAccess = None
        self._WebSocket = None
        self._RemoteAuthentication = None
        self._ShareCname = None
        self._HwPrivateAccess = None
        self._QnPrivateAccess = None
        self._OthersPrivateAccess = None
        self._HttpsBilling = None
        self._ParamFilter = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def ProjectId(self):
        """项目 ID
        :rtype: int
        """
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def Origin(self):
        """源站配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Origin`
        """
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def IpFilter(self):
        """IP 黑白名单配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        """
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        """IP 限频配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        """
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def StatusCodeCache(self):
        """状态码缓存配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        """
        return self._StatusCodeCache

    @StatusCodeCache.setter
    def StatusCodeCache(self, StatusCodeCache):
        self._StatusCodeCache = StatusCodeCache

    @property
    def Compression(self):
        """智能压缩配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Compression`
        """
        return self._Compression

    @Compression.setter
    def Compression(self, Compression):
        self._Compression = Compression

    @property
    def BandwidthAlert(self):
        """带宽封顶配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        """
        return self._BandwidthAlert

    @BandwidthAlert.setter
    def BandwidthAlert(self, BandwidthAlert):
        self._BandwidthAlert = BandwidthAlert

    @property
    def RangeOriginPull(self):
        """Range 回源配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        """
        return self._RangeOriginPull

    @RangeOriginPull.setter
    def RangeOriginPull(self, RangeOriginPull):
        self._RangeOriginPull = RangeOriginPull

    @property
    def FollowRedirect(self):
        """301/302 回源跟随配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        """
        return self._FollowRedirect

    @FollowRedirect.setter
    def FollowRedirect(self, FollowRedirect):
        self._FollowRedirect = FollowRedirect

    @property
    def ErrorPage(self):
        """错误码重定向配置（功能灰度中，尚未全量）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        """
        return self._ErrorPage

    @ErrorPage.setter
    def ErrorPage(self, ErrorPage):
        self._ErrorPage = ErrorPage

    @property
    def RequestHeader(self):
        """回源请求头部配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        """
        return self._RequestHeader

    @RequestHeader.setter
    def RequestHeader(self, RequestHeader):
        self._RequestHeader = RequestHeader

    @property
    def ResponseHeader(self):
        """响应头部配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        """
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def DownstreamCapping(self):
        """下载速度配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        """
        return self._DownstreamCapping

    @DownstreamCapping.setter
    def DownstreamCapping(self, DownstreamCapping):
        self._DownstreamCapping = DownstreamCapping

    @property
    def CacheKey(self):
        """节点缓存键配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        """
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def ResponseHeaderCache(self):
        """头部缓存配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        """
        return self._ResponseHeaderCache

    @ResponseHeaderCache.setter
    def ResponseHeaderCache(self, ResponseHeaderCache):
        self._ResponseHeaderCache = ResponseHeaderCache

    @property
    def VideoSeek(self):
        """视频拖拽配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        return self._VideoSeek

    @VideoSeek.setter
    def VideoSeek(self, VideoSeek):
        self._VideoSeek = VideoSeek

    @property
    def Cache(self):
        """缓存过期时间配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Cache`
        """
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def OriginPullOptimization(self):
        """跨国链路优化配置（已下线）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        """
        return self._OriginPullOptimization

    @OriginPullOptimization.setter
    def OriginPullOptimization(self, OriginPullOptimization):
        self._OriginPullOptimization = OriginPullOptimization

    @property
    def Https(self):
        """Https 加速配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Https`
        """
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Authentication(self):
        """时间戳防盗链配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        """
        return self._Authentication

    @Authentication.setter
    def Authentication(self, Authentication):
        self._Authentication = Authentication

    @property
    def Seo(self):
        """SEO 优化配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Seo`
        """
        return self._Seo

    @Seo.setter
    def Seo(self, Seo):
        self._Seo = Seo

    @property
    def ForceRedirect(self):
        """访问协议强制跳转配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        """
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Referer(self):
        """Referer 防盗链配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Referer`
        """
        return self._Referer

    @Referer.setter
    def Referer(self, Referer):
        self._Referer = Referer

    @property
    def MaxAge(self):
        """浏览器缓存配置（功能灰度中，尚未全量）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        """
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def SpecificConfig(self):
        """地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景
        :rtype: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        """
        return self._SpecificConfig

    @SpecificConfig.setter
    def SpecificConfig(self, SpecificConfig):
        self._SpecificConfig = SpecificConfig

    @property
    def ServiceType(self):
        """域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :rtype: str
        """
        return self._ServiceType

    @ServiceType.setter
    def ServiceType(self, ServiceType):
        self._ServiceType = ServiceType

    @property
    def Area(self):
        """域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
从mainland/overseas修改至global时，域名的配置将被同步至overseas/mainland。若域名含有后端特殊配置，此类配置的同步过程有一定延时，请耐心等待
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def OriginPullTimeout(self):
        """回源超时配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        """
        return self._OriginPullTimeout

    @OriginPullTimeout.setter
    def OriginPullTimeout(self, OriginPullTimeout):
        self._OriginPullTimeout = OriginPullTimeout

    @property
    def AwsPrivateAccess(self):
        """回源S3私有鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        """
        return self._AwsPrivateAccess

    @AwsPrivateAccess.setter
    def AwsPrivateAccess(self, AwsPrivateAccess):
        self._AwsPrivateAccess = AwsPrivateAccess

    @property
    def UserAgentFilter(self):
        """UA黑白名单配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        """
        return self._UserAgentFilter

    @UserAgentFilter.setter
    def UserAgentFilter(self, UserAgentFilter):
        self._UserAgentFilter = UserAgentFilter

    @property
    def AccessControl(self):
        """访问控制
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        """
        return self._AccessControl

    @AccessControl.setter
    def AccessControl(self, AccessControl):
        self._AccessControl = AccessControl

    @property
    def UrlRedirect(self):
        """访问URL重写配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        """
        return self._UrlRedirect

    @UrlRedirect.setter
    def UrlRedirect(self, UrlRedirect):
        self._UrlRedirect = UrlRedirect

    @property
    def AccessPort(self):
        """访问端口配置
        :rtype: list of int
        """
        return self._AccessPort

    @AccessPort.setter
    def AccessPort(self, AccessPort):
        self._AccessPort = AccessPort

    @property
    def AdvancedAuthentication(self):
        """时间戳防盗链高级版配置，白名单功能
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        """
        return self._AdvancedAuthentication

    @AdvancedAuthentication.setter
    def AdvancedAuthentication(self, AdvancedAuthentication):
        self._AdvancedAuthentication = AdvancedAuthentication

    @property
    def OriginAuthentication(self):
        """回源鉴权高级版配置，白名单功能
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        """
        return self._OriginAuthentication

    @OriginAuthentication.setter
    def OriginAuthentication(self, OriginAuthentication):
        self._OriginAuthentication = OriginAuthentication

    @property
    def Ipv6Access(self):
        """Ipv6 访问配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        """
        return self._Ipv6Access

    @Ipv6Access.setter
    def Ipv6Access(self, Ipv6Access):
        self._Ipv6Access = Ipv6Access

    @property
    def OfflineCache(self):
        """离线缓存
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        """
        return self._OfflineCache

    @OfflineCache.setter
    def OfflineCache(self, OfflineCache):
        self._OfflineCache = OfflineCache

    @property
    def OriginCombine(self):
        """合并回源
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        """
        return self._OriginCombine

    @OriginCombine.setter
    def OriginCombine(self, OriginCombine):
        self._OriginCombine = OriginCombine

    @property
    def PostMaxSize(self):
        """POST请求传输配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        """
        return self._PostMaxSize

    @PostMaxSize.setter
    def PostMaxSize(self, PostMaxSize):
        self._PostMaxSize = PostMaxSize

    @property
    def Quic(self):
        """Quic访问（收费服务，详见计费说明和产品文档）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.Quic`
        """
        return self._Quic

    @Quic.setter
    def Quic(self, Quic):
        self._Quic = Quic

    @property
    def OssPrivateAccess(self):
        """回源OSS私有鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`
        """
        return self._OssPrivateAccess

    @OssPrivateAccess.setter
    def OssPrivateAccess(self, OssPrivateAccess):
        self._OssPrivateAccess = OssPrivateAccess

    @property
    def WebSocket(self):
        """WebSocket配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.WebSocket`
        """
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket

    @property
    def RemoteAuthentication(self):
        """远程鉴权配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.RemoteAuthentication`
        """
        return self._RemoteAuthentication

    @RemoteAuthentication.setter
    def RemoteAuthentication(self, RemoteAuthentication):
        self._RemoteAuthentication = RemoteAuthentication

    @property
    def ShareCname(self):
        """共享CNAME配置，白名单功能
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ShareCname`
        """
        return self._ShareCname

    @ShareCname.setter
    def ShareCname(self, ShareCname):
        self._ShareCname = ShareCname

    @property
    def HwPrivateAccess(self):
        """华为云对象存储回源鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HwPrivateAccess`
        """
        return self._HwPrivateAccess

    @HwPrivateAccess.setter
    def HwPrivateAccess(self, HwPrivateAccess):
        self._HwPrivateAccess = HwPrivateAccess

    @property
    def QnPrivateAccess(self):
        """七牛云对象存储回源鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.QnPrivateAccess`
        """
        return self._QnPrivateAccess

    @QnPrivateAccess.setter
    def QnPrivateAccess(self, QnPrivateAccess):
        self._QnPrivateAccess = QnPrivateAccess

    @property
    def OthersPrivateAccess(self):
        """其他厂商对象存储回源鉴权
        :rtype: :class:`tencentcloud.cdn.v20180606.models.OthersPrivateAccess`
        """
        return self._OthersPrivateAccess

    @OthersPrivateAccess.setter
    def OthersPrivateAccess(self, OthersPrivateAccess):
        self._OthersPrivateAccess = OthersPrivateAccess

    @property
    def HttpsBilling(self):
        """HTTPS服务（收费服务，详见计费说明和产品文档）
        :rtype: :class:`tencentcloud.cdn.v20180606.models.HttpsBilling`
        """
        return self._HttpsBilling

    @HttpsBilling.setter
    def HttpsBilling(self, HttpsBilling):
        self._HttpsBilling = HttpsBilling

    @property
    def ParamFilter(self):
        """参数黑名单
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ParamFilter`
        """
        return self._ParamFilter

    @ParamFilter.setter
    def ParamFilter(self, ParamFilter):
        self._ParamFilter = ParamFilter


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._ProjectId = params.get("ProjectId")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self._StatusCodeCache = StatusCodeCache()
            self._StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self._Compression = Compression()
            self._Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self._BandwidthAlert = BandwidthAlert()
            self._BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self._RangeOriginPull = RangeOriginPull()
            self._RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self._FollowRedirect = FollowRedirect()
            self._FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self._ErrorPage = ErrorPage()
            self._ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self._RequestHeader = RequestHeader()
            self._RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self._DownstreamCapping = DownstreamCapping()
            self._DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self._ResponseHeaderCache = ResponseHeaderCache()
            self._ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self._VideoSeek = VideoSeek()
            self._VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self._OriginPullOptimization = OriginPullOptimization()
            self._OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self._Authentication = Authentication()
            self._Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self._Seo = Seo()
            self._Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self._Referer = Referer()
            self._Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self._MaxAge = MaxAge()
            self._MaxAge._deserialize(params.get("MaxAge"))
        if params.get("SpecificConfig") is not None:
            self._SpecificConfig = SpecificConfig()
            self._SpecificConfig._deserialize(params.get("SpecificConfig"))
        self._ServiceType = params.get("ServiceType")
        self._Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self._OriginPullTimeout = OriginPullTimeout()
            self._OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self._AwsPrivateAccess = AwsPrivateAccess()
            self._AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("UserAgentFilter") is not None:
            self._UserAgentFilter = UserAgentFilter()
            self._UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self._AccessControl = AccessControl()
            self._AccessControl._deserialize(params.get("AccessControl"))
        if params.get("UrlRedirect") is not None:
            self._UrlRedirect = UrlRedirect()
            self._UrlRedirect._deserialize(params.get("UrlRedirect"))
        self._AccessPort = params.get("AccessPort")
        if params.get("AdvancedAuthentication") is not None:
            self._AdvancedAuthentication = AdvancedAuthentication()
            self._AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self._OriginAuthentication = OriginAuthentication()
            self._OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self._Ipv6Access = Ipv6Access()
            self._Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self._OfflineCache = OfflineCache()
            self._OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self._OriginCombine = OriginCombine()
            self._OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("PostMaxSize") is not None:
            self._PostMaxSize = PostSize()
            self._PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Quic") is not None:
            self._Quic = Quic()
            self._Quic._deserialize(params.get("Quic"))
        if params.get("OssPrivateAccess") is not None:
            self._OssPrivateAccess = OssPrivateAccess()
            self._OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        if params.get("RemoteAuthentication") is not None:
            self._RemoteAuthentication = RemoteAuthentication()
            self._RemoteAuthentication._deserialize(params.get("RemoteAuthentication"))
        if params.get("ShareCname") is not None:
            self._ShareCname = ShareCname()
            self._ShareCname._deserialize(params.get("ShareCname"))
        if params.get("HwPrivateAccess") is not None:
            self._HwPrivateAccess = HwPrivateAccess()
            self._HwPrivateAccess._deserialize(params.get("HwPrivateAccess"))
        if params.get("QnPrivateAccess") is not None:
            self._QnPrivateAccess = QnPrivateAccess()
            self._QnPrivateAccess._deserialize(params.get("QnPrivateAccess"))
        if params.get("OthersPrivateAccess") is not None:
            self._OthersPrivateAccess = OthersPrivateAccess()
            self._OthersPrivateAccess._deserialize(params.get("OthersPrivateAccess"))
        if params.get("HttpsBilling") is not None:
            self._HttpsBilling = HttpsBilling()
            self._HttpsBilling._deserialize(params.get("HttpsBilling"))
        if params.get("ParamFilter") is not None:
            self._ParamFilter = ParamFilter()
            self._ParamFilter._deserialize(params.get("ParamFilter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateImageConfigRequest(AbstractModel):
    """UpdateImageConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _WebpAdapter: WebpAdapter配置项
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param _TpgAdapter: TpgAdapter配置项
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param _GuetzliAdapter: GuetzliAdapter配置项
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        :param _AvifAdapter: AvifAdapter配置项
        :type AvifAdapter: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        """
        self._Domain = None
        self._WebpAdapter = None
        self._TpgAdapter = None
        self._GuetzliAdapter = None
        self._AvifAdapter = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def WebpAdapter(self):
        """WebpAdapter配置项
        :rtype: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        """
        return self._WebpAdapter

    @WebpAdapter.setter
    def WebpAdapter(self, WebpAdapter):
        self._WebpAdapter = WebpAdapter

    @property
    def TpgAdapter(self):
        """TpgAdapter配置项
        :rtype: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        """
        return self._TpgAdapter

    @TpgAdapter.setter
    def TpgAdapter(self, TpgAdapter):
        self._TpgAdapter = TpgAdapter

    @property
    def GuetzliAdapter(self):
        """GuetzliAdapter配置项
        :rtype: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        return self._GuetzliAdapter

    @GuetzliAdapter.setter
    def GuetzliAdapter(self, GuetzliAdapter):
        self._GuetzliAdapter = GuetzliAdapter

    @property
    def AvifAdapter(self):
        """AvifAdapter配置项
        :rtype: :class:`tencentcloud.cdn.v20180606.models.AvifAdapter`
        """
        return self._AvifAdapter

    @AvifAdapter.setter
    def AvifAdapter(self, AvifAdapter):
        self._AvifAdapter = AvifAdapter


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("WebpAdapter") is not None:
            self._WebpAdapter = WebpAdapter()
            self._WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self._TpgAdapter = TpgAdapter()
            self._TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self._GuetzliAdapter = GuetzliAdapter()
            self._GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        if params.get("AvifAdapter") is not None:
            self._AvifAdapter = AvifAdapter()
            self._AvifAdapter._deserialize(params.get("AvifAdapter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateImageConfigResponse(AbstractModel):
    """UpdateImageConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Area: 计费区域，mainland或overseas。
        :type Area: str
        :param _PayType: 计费类型，flux或bandwidth。
        :type PayType: str
        """
        self._Area = None
        self._PayType = None

    @property
    def Area(self):
        """计费区域，mainland或overseas。
        :rtype: str
        """
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def PayType(self):
        """计费类型，flux或bandwidth。
        :rtype: str
        """
        return self._PayType

    @PayType.setter
    def PayType(self, PayType):
        self._PayType = PayType


    def _deserialize(self, params):
        self._Area = params.get("Area")
        self._PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._RequestId = None

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class UpdateScdnDomainRequest(AbstractModel):
    """UpdateScdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _Waf: Web 攻击防护（WAF）配置
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param _Acl: 自定义防护策略配置
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param _CC: CC 防护配置，目前 CC 防护默认开启
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param _Ddos: DDOS 防护配置，目前 DDoS 防护默认开启
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param _Bot: BOT 防护配置
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        self._Domain = None
        self._Waf = None
        self._Acl = None
        self._CC = None
        self._Ddos = None
        self._Bot = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Waf(self):
        """Web 攻击防护（WAF）配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        """
        return self._Waf

    @Waf.setter
    def Waf(self, Waf):
        self._Waf = Waf

    @property
    def Acl(self):
        """自定义防护策略配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        """
        return self._Acl

    @Acl.setter
    def Acl(self, Acl):
        self._Acl = Acl

    @property
    def CC(self):
        """CC 防护配置，目前 CC 防护默认开启
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        """
        return self._CC

    @CC.setter
    def CC(self, CC):
        self._CC = CC

    @property
    def Ddos(self):
        """DDOS 防护配置，目前 DDoS 防护默认开启
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        """
        return self._Ddos

    @Ddos.setter
    def Ddos(self, Ddos):
        self._Ddos = Ddos

    @property
    def Bot(self):
        """BOT 防护配置
        :rtype: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        return self._Bot

    @Bot.setter
    def Bot(self, Bot):
        self._Bot = Bot


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("Waf") is not None:
            self._Waf = ScdnWafConfig()
            self._Waf._deserialize(params.get("Waf"))
        if params.get("Acl") is not None:
            self._Acl = ScdnAclConfig()
            self._Acl._deserialize(params.get("Acl"))
        if params.get("CC") is not None:
            self._CC = ScdnConfig()
            self._CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self._Ddos = ScdnDdosConfig()
            self._Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self._Bot = ScdnBotConfig()
            self._Bot._deserialize(params.get("Bot"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScdnDomainResponse(AbstractModel):
    """UpdateScdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 提交结果，Success表示成功
        :type Result: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """提交结果，Success表示成功
        :rtype: str
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class UrlRecord(AbstractModel):
    """封禁url的详细信息

    """

    def __init__(self):
        r"""
        :param _Status: 状态(disable表示封禁，enable表示解封)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param _RealUrl: 对应的url
注意：此字段可能返回 null，表示取不到有效值。
        :type RealUrl: str
        :param _CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param _UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self._Status = None
        self._RealUrl = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Status(self):
        """状态(disable表示封禁，enable表示解封)
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def RealUrl(self):
        """对应的url
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RealUrl

    @RealUrl.setter
    def RealUrl(self, RealUrl):
        self._RealUrl = RealUrl

    @property
    def CreateTime(self):
        """创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Status = params.get("Status")
        self._RealUrl = params.get("RealUrl")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirect(AbstractModel):
    """访问URL重写配置

    """

    def __init__(self):
        r"""
        :param _Switch: 访问URL重写配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _PathRules: 访问URL重写规则，当Switch为on时必填，规则数量最大为10个。
注意：此字段可能返回 null，表示取不到有效值。
        :type PathRules: list of UrlRedirectRule
        """
        self._Switch = None
        self._PathRules = None

    @property
    def Switch(self):
        """访问URL重写配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def PathRules(self):
        """访问URL重写规则，当Switch为on时必填，规则数量最大为10个。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UrlRedirectRule
        """
        return self._PathRules

    @PathRules.setter
    def PathRules(self, PathRules):
        self._PathRules = PathRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("PathRules") is not None:
            self._PathRules = []
            for item in params.get("PathRules"):
                obj = UrlRedirectRule()
                obj._deserialize(item)
                self._PathRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirectRule(AbstractModel):
    """Url重定向规则配置

    """

    def __init__(self):
        r"""
        :param _RedirectStatusCode: 重定向状态码，301 | 302
        :type RedirectStatusCode: int
        :param _Pattern: 待匹配的Url，仅支持Url路径，不支持参数。默认完全匹配，支持通配符 *，最多支持5个通配符，最大长度1024字符。
        :type Pattern: str
        :param _RedirectUrl: 目标URL，必须以“/”开头，不包含参数部分。最大长度1024字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号，最多支持10个捕获值。
        :type RedirectUrl: str
        :param _RedirectHost: 目标host，必须以http://或https://开头，并填写标准格式域名，如果不填写，默认为http:// + 当前域名
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectHost: str
        :param _FullMatch: 指定是全路径配置还是任意匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type FullMatch: bool
        """
        self._RedirectStatusCode = None
        self._Pattern = None
        self._RedirectUrl = None
        self._RedirectHost = None
        self._FullMatch = None

    @property
    def RedirectStatusCode(self):
        """重定向状态码，301 | 302
        :rtype: int
        """
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode

    @property
    def Pattern(self):
        """待匹配的Url，仅支持Url路径，不支持参数。默认完全匹配，支持通配符 *，最多支持5个通配符，最大长度1024字符。
        :rtype: str
        """
        return self._Pattern

    @Pattern.setter
    def Pattern(self, Pattern):
        self._Pattern = Pattern

    @property
    def RedirectUrl(self):
        """目标URL，必须以“/”开头，不包含参数部分。最大长度1024字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号，最多支持10个捕获值。
        :rtype: str
        """
        return self._RedirectUrl

    @RedirectUrl.setter
    def RedirectUrl(self, RedirectUrl):
        self._RedirectUrl = RedirectUrl

    @property
    def RedirectHost(self):
        """目标host，必须以http://或https://开头，并填写标准格式域名，如果不填写，默认为http:// + 当前域名
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RedirectHost

    @RedirectHost.setter
    def RedirectHost(self, RedirectHost):
        self._RedirectHost = RedirectHost

    @property
    def FullMatch(self):
        """指定是全路径配置还是任意匹配
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: bool
        """
        return self._FullMatch

    @FullMatch.setter
    def FullMatch(self, FullMatch):
        self._FullMatch = FullMatch


    def _deserialize(self, params):
        self._RedirectStatusCode = params.get("RedirectStatusCode")
        self._Pattern = params.get("Pattern")
        self._RedirectUrl = params.get("RedirectUrl")
        self._RedirectHost = params.get("RedirectHost")
        self._FullMatch = params.get("FullMatch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilter(AbstractModel):
    """UserAgent黑白名单配置

    """

    def __init__(self):
        r"""
        :param _Switch: UserAgent黑白名单配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _FilterRules: UA黑白名单生效规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of UserAgentFilterRule
        """
        self._Switch = None
        self._FilterRules = None

    @property
    def Switch(self):
        """UserAgent黑白名单配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterRules(self):
        """UA黑白名单生效规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of UserAgentFilterRule
        """
        return self._FilterRules

    @FilterRules.setter
    def FilterRules(self, FilterRules):
        self._FilterRules = FilterRules


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        if params.get("FilterRules") is not None:
            self._FilterRules = []
            for item in params.get("FilterRules"):
                obj = UserAgentFilterRule()
                obj._deserialize(item)
                self._FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilterRule(AbstractModel):
    """UserAgent黑白名单规则配置

    """

    def __init__(self):
        r"""
        :param _RuleType: 访问路径生效类型
all: 所有访问路径生效
file: 根据文件后缀类型生效
directory: 根据目录生效
path: 根据完整访问路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RulePaths: 访问路径生效内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        :param _UserAgents: UserAgent列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAgents: list of str
        :param _FilterType: 黑名单或白名单，blacklist或whitelist
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        """
        self._RuleType = None
        self._RulePaths = None
        self._UserAgents = None
        self._FilterType = None

    @property
    def RuleType(self):
        """访问路径生效类型
all: 所有访问路径生效
file: 根据文件后缀类型生效
directory: 根据目录生效
path: 根据完整访问路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
        """访问路径生效内容
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._RulePaths

    @RulePaths.setter
    def RulePaths(self, RulePaths):
        self._RulePaths = RulePaths

    @property
    def UserAgents(self):
        """UserAgent列表
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: list of str
        """
        return self._UserAgents

    @UserAgents.setter
    def UserAgents(self, UserAgents):
        self._UserAgents = UserAgents

    @property
    def FilterType(self):
        """黑名单或白名单，blacklist或whitelist
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType


    def _deserialize(self, params):
        self._RuleType = params.get("RuleType")
        self._RulePaths = params.get("RulePaths")
        self._UserAgents = params.get("UserAgents")
        self._FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyDomainRecordRequest(AbstractModel):
    """VerifyDomainRecord请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名
        :type Domain: str
        :param _VerifyType: 验证方式
dns: DNS 解析验证（默认值）
file: 文件验证
        :type VerifyType: str
        """
        self._Domain = None
        self._VerifyType = None

    @property
    def Domain(self):
        """域名
        :rtype: str
        """
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def VerifyType(self):
        """验证方式
dns: DNS 解析验证（默认值）
file: 文件验证
        :rtype: str
        """
        return self._VerifyType

    @VerifyType.setter
    def VerifyType(self, VerifyType):
        self._VerifyType = VerifyType


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        self._VerifyType = params.get("VerifyType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyDomainRecordResponse(AbstractModel):
    """VerifyDomainRecord返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Result: 是否验证成功
        :type Result: bool
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Result = None
        self._RequestId = None

    @property
    def Result(self):
        """是否验证成功
        :rtype: bool
        """
        return self._Result

    @Result.setter
    def Result(self, Result):
        self._Result = Result

    @property
    def RequestId(self):
        """唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :rtype: str
        """
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._Result = params.get("Result")
        self._RequestId = params.get("RequestId")


class VideoSeek(AbstractModel):
    """视频拖拽配置，默认为关闭状态

    """

    def __init__(self):
        r"""
        :param _Switch: 视频拖拽配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """视频拖拽配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViolationUrl(AbstractModel):
    """违规 URL 详情

    """

    def __init__(self):
        r"""
        :param _Id: ID
        :type Id: int
        :param _RealUrl: 违规资源原始访问 URL
        :type RealUrl: str
        :param _DownloadUrl: 快照路径，用于控制台展示违规内容快照
        :type DownloadUrl: str
        :param _UrlStatus: 违规资源当前状态
forbid：已封禁
release：已解封
delay ： 延迟处理
reject ：申诉驳回，状态仍为封禁状态
complain：申诉进行中
        :type UrlStatus: str
        :param _CreateTime: 创建时间
        :type CreateTime: str
        :param _UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self._Id = None
        self._RealUrl = None
        self._DownloadUrl = None
        self._UrlStatus = None
        self._CreateTime = None
        self._UpdateTime = None

    @property
    def Id(self):
        """ID
        :rtype: int
        """
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def RealUrl(self):
        """违规资源原始访问 URL
        :rtype: str
        """
        return self._RealUrl

    @RealUrl.setter
    def RealUrl(self, RealUrl):
        self._RealUrl = RealUrl

    @property
    def DownloadUrl(self):
        """快照路径，用于控制台展示违规内容快照
        :rtype: str
        """
        return self._DownloadUrl

    @DownloadUrl.setter
    def DownloadUrl(self, DownloadUrl):
        self._DownloadUrl = DownloadUrl

    @property
    def UrlStatus(self):
        """违规资源当前状态
forbid：已封禁
release：已解封
delay ： 延迟处理
reject ：申诉驳回，状态仍为封禁状态
complain：申诉进行中
        :rtype: str
        """
        return self._UrlStatus

    @UrlStatus.setter
    def UrlStatus(self, UrlStatus):
        self._UrlStatus = UrlStatus

    @property
    def CreateTime(self):
        """创建时间
        :rtype: str
        """
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        """更新时间
        :rtype: str
        """
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._RealUrl = params.get("RealUrl")
        self._DownloadUrl = params.get("DownloadUrl")
        self._UrlStatus = params.get("UrlStatus")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafSubRuleStatus(AbstractModel):
    """Waf子规则开关状态

    """

    def __init__(self):
        r"""
        :param _Switch: Waf子规则开关状态配置开关，取值有：
on：开启
off：关闭
        :type Switch: str
        :param _SubIds: 规则id列表
        :type SubIds: list of int
        """
        self._Switch = None
        self._SubIds = None

    @property
    def Switch(self):
        """Waf子规则开关状态配置开关，取值有：
on：开启
off：关闭
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def SubIds(self):
        """规则id列表
        :rtype: list of int
        """
        return self._SubIds

    @SubIds.setter
    def SubIds(self, SubIds):
        self._SubIds = SubIds


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._SubIds = params.get("SubIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket配置
    WebSocket 为ECDN产品功能，如需使用请通过ECDN域名配置.

    """

    def __init__(self):
        r"""
        :param _Switch: WebSocket 超时配置开关，取值有：
on：开启，可以调整超时时间
off：关闭，平台仍支持WebSocket连接，此时超时时间默认为15秒

        :type Switch: str
        :param _Timeout: 设置超时时间，单位为秒，最大超时时间300秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        """WebSocket 超时配置开关，取值有：
on：开启，可以调整超时时间
off：关闭，平台仍支持WebSocket连接，此时超时时间默认为15秒

        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
        """设置超时时间，单位为秒，最大超时时间300秒。
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: int
        """
        return self._Timeout

    @Timeout.setter
    def Timeout(self, Timeout):
        self._Timeout = Timeout


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebpAdapter(AbstractModel):
    """图片优化-WebpAdapter配置

    """

    def __init__(self):
        r"""
        :param _Switch: 图片优化-WebpAdapter配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self._Switch = None

    @property
    def Switch(self):
        """图片优化-WebpAdapter配置开关，取值有：
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :rtype: str
        """
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        