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

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class AccessControl(AbstractModel):
    """请求头部及请求url访问控制

    """

    def __init__(self):
        """
        :param Switch: on | off 是否启用请求头部及请求url访问控制
        :type Switch: str
        :param AccessControlRules: 请求头部及请求url访问规则
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessControlRules: list of AccessControlRule
        :param ReturnCode: 返回状态码
注意：此字段可能返回 null，表示取不到有效值。
        :type ReturnCode: int
        """
        self.Switch = None
        self.AccessControlRules = None
        self.ReturnCode = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("AccessControlRules") is not None:
            self.AccessControlRules = []
            for item in params.get("AccessControlRules"):
                obj = AccessControlRule()
                obj._deserialize(item)
                self.AccessControlRules.append(obj)
        self.ReturnCode = params.get("ReturnCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AccessControlRule(AbstractModel):
    """访问控制规则

    """

    def __init__(self):
        """
        :param RuleType: requestHeader ：对请求头部进行访问控制
url ： 对访问url进行访问控制
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RuleContent: 封禁内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleContent: str
        :param Regex: on ：正则匹配
off ：字面匹配
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: str
        :param RuleHeader: RuleType为requestHeader时必填，否则不需要填
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleHeader: str
        """
        self.RuleType = None
        self.RuleContent = None
        self.Regex = None
        self.RuleHeader = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RuleContent = params.get("RuleContent")
        self.Regex = params.get("Regex")
        self.RuleHeader = params.get("RuleHeader")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param ServiceType: 加速域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :type ServiceType: str
        :param Origin: 源站配置
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param ProjectId: 项目 ID，默认为 0，代表【默认项目】
        :type ProjectId: int
        :param IpFilter: IP 黑白名单配置
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP 限频配置
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: 状态码缓存配置
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: 智能压缩配置
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: 带宽封顶配置
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range 回源配置
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 回源跟随配置。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: 错误码重定向配置（功能灰度中，尚未全量）
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: 请求头部配置
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 响应头部配置
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: 下载速度配置
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: 节点缓存键配置
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: 头部缓存配置
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: 视频拖拽配置
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: 缓存过期时间配置
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: 跨国链路优化配置
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https 加速配置
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: 时间戳防盗链配置
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO 优化配置
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: 访问协议强制跳转配置
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer 防盗链配置
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: 浏览器缓存配置（功能灰度中，尚未全量）
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: Ipv6 配置（功能灰度中，尚未全量）
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param SpecificConfig: 地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: 域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
使用中国境外加速、全球加速时，需要先开通中国境外加速服务
        :type Area: str
        :param OriginPullTimeout: 回源超时配置
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param Tag: 标签配置
        :type Tag: list of Tag
        :param Ipv6Access: Ipv6 访问配置
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param OfflineCache: 离线缓存
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param Quic: QUIC正在内测中，请先提交内测申请，详情请前往QUIC产品文档。
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        """
        self.Domain = None
        self.ServiceType = None
        self.Origin = None
        self.ProjectId = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.SpecificConfig = None
        self.Area = None
        self.OriginPullTimeout = None
        self.Tag = None
        self.Ipv6Access = None
        self.OfflineCache = None
        self.Quic = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ServiceType = params.get("ServiceType")
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
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        if params.get("Ipv6Access") is not None:
            self.Ipv6Access = Ipv6Access()
            self.Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvanceCacheRule(AbstractModel):
    """缓存配置高级版本规则

    """

    def __init__(self):
        """
        :param CacheType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
default：源站未返回 max-age 情况下的缓存规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheType: str
        :param CacheContents: 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
default 时填充 "no max-age"
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheContents: list of str
        :param CacheTime: 缓存过期时间
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvanceConfig(AbstractModel):
    """高级配置集合

    """

    def __init__(self):
        """
        :param Name: 高级配置名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param Value: 是否支持高级配置，
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthentication(AbstractModel):
    """时间戳防盗链高级版配置，白名单功能

    """

    def __init__(self):
        """
        :param Switch: 防盗链配置开关，on或off，开启时必须且只能配置一种模式，其余模式为null。
        :type Switch: str
        :param TypeA: 时间戳防盗链高级版模式A配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeA`
        :param TypeB: 时间戳防盗链高级版模式B配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeB`
        :param TypeC: 时间戳防盗链高级版模式C配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeC`
        :param TypeD: 时间戳防盗链高级版模式D配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeD`
        :param TypeE: 时间戳防盗链高级版模式E配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeE: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeE`
        :param TypeF: 时间戳防盗链高级版模式F配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeF: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeF`
        """
        self.Switch = None
        self.TypeA = None
        self.TypeB = None
        self.TypeC = None
        self.TypeD = None
        self.TypeE = None
        self.TypeF = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = AdvancedAuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self.TypeB = AdvancedAuthenticationTypeB()
            self.TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self.TypeC = AdvancedAuthenticationTypeC()
            self.TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self.TypeD = AdvancedAuthenticationTypeD()
            self.TypeD._deserialize(params.get("TypeD"))
        if params.get("TypeE") is not None:
            self.TypeE = AdvancedAuthenticationTypeE()
            self.TypeE._deserialize(params.get("TypeE"))
        if params.get("TypeF") is not None:
            self.TypeF = AdvancedAuthenticationTypeF()
            self.TypeF._deserialize(params.get("TypeF"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthenticationTypeA(AbstractModel):
    """时间戳防盗链高级版模式A配置。

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
        :type SecretKey: str
        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type SignParam: str
        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type TimeParam: str
        :param ExpireTime: 过期时间，单位秒。
        :type ExpireTime: int
        :param ExpireTimeRequired: 是否必须提供过期时间参数。
        :type ExpireTimeRequired: bool
        :param Format: Url组成格式，如：${private_key}${schema}${host}${full_uri。
        :type Format: str
        :param TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。
        :type TimeFormat: str
        :param FailCode: 鉴权失败时返回的状态码。
        :type FailCode: int
        :param ExpireCode: 链接过期时返回的状态码。
        :type ExpireCode: int
        :param RulePaths: 需要鉴权的url路径列表。
        :type RulePaths: list of str
        :param Transformation: 保留字段。
        :type Transformation: int
        """
        self.SecretKey = None
        self.SignParam = None
        self.TimeParam = None
        self.ExpireTime = None
        self.ExpireTimeRequired = None
        self.Format = None
        self.TimeFormat = None
        self.FailCode = None
        self.ExpireCode = None
        self.RulePaths = None
        self.Transformation = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.ExpireTime = params.get("ExpireTime")
        self.ExpireTimeRequired = params.get("ExpireTimeRequired")
        self.Format = params.get("Format")
        self.TimeFormat = params.get("TimeFormat")
        self.FailCode = params.get("FailCode")
        self.ExpireCode = params.get("ExpireCode")
        self.RulePaths = params.get("RulePaths")
        self.Transformation = params.get("Transformation")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthenticationTypeB(AbstractModel):
    """时间戳防盗链高级版模式B配置。

    """

    def __init__(self):
        """
        :param KeyAlpha: alpha键名。
        :type KeyAlpha: str
        :param KeyBeta: beta键名。
        :type KeyBeta: str
        :param KeyGamma: gamma键名。
        :type KeyGamma: str
        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type SignParam: str
        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type TimeParam: str
        :param ExpireTime: 过期时间，单位秒。
        :type ExpireTime: int
        :param TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。
        :type TimeFormat: str
        :param FailCode: 鉴权失败时返回的状态码。
        :type FailCode: int
        :param ExpireCode: 链接过期时返回的状态码。
        :type ExpireCode: int
        :param RulePaths: 需要鉴权的url路径列表。
        :type RulePaths: list of str
        """
        self.KeyAlpha = None
        self.KeyBeta = None
        self.KeyGamma = None
        self.SignParam = None
        self.TimeParam = None
        self.ExpireTime = None
        self.TimeFormat = None
        self.FailCode = None
        self.ExpireCode = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.KeyAlpha = params.get("KeyAlpha")
        self.KeyBeta = params.get("KeyBeta")
        self.KeyGamma = params.get("KeyGamma")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.ExpireTime = params.get("ExpireTime")
        self.TimeFormat = params.get("TimeFormat")
        self.FailCode = params.get("FailCode")
        self.ExpireCode = params.get("ExpireCode")
        self.RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthenticationTypeC(AbstractModel):
    """时间戳防盗链高级版模式C配置。

    """

    def __init__(self):
        """
        :param AccessKey: 访问密钥。
        :type AccessKey: str
        :param SecretKey: 鉴权密钥。
        :type SecretKey: str
        """
        self.AccessKey = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthenticationTypeD(AbstractModel):
    """时间戳防盗链高级版模式D配置。

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
        :type SecretKey: str
        :param BackupSecretKey: 备份密钥，当使用SecretKey鉴权失败时会使用该密钥重新鉴权。
        :type BackupSecretKey: str
        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type SignParam: str
        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
        :type TimeParam: str
        :param ExpireTime: 过期时间，单位秒。
        :type ExpireTime: int
        :param TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.BackupSecretKey = None
        self.SignParam = None
        self.TimeParam = None
        self.ExpireTime = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.BackupSecretKey = params.get("BackupSecretKey")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.ExpireTime = params.get("ExpireTime")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthenticationTypeE(AbstractModel):
    """时间戳防盗链高级版模式E配置。

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignParam: str
        :param AclSignParam: uri串中Acl签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type AclSignParam: str
        :param StartTimeParam: uri串中开始时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type StartTimeParam: str
        :param ExpireTimeParam: uri串中过期时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTimeParam: str
        :param TimeFormat: 时间格式，dec
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.SignParam = None
        self.AclSignParam = None
        self.StartTimeParam = None
        self.ExpireTimeParam = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.AclSignParam = params.get("AclSignParam")
        self.StartTimeParam = params.get("StartTimeParam")
        self.ExpireTimeParam = params.get("ExpireTimeParam")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedAuthenticationTypeF(AbstractModel):
    """时间戳防盗链高级鉴权模式TypeF配置

    """

    def __init__(self):
        """
        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type SignParam: str
        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeParam: str
        :param TransactionParam: uri串中Transaction字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。
        :type TransactionParam: str
        :param SecretKey: 用于计算签名的主密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param BackupSecretKey: 用于计算签名的备选密钥，主密钥校验失败后再次尝试备选密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupSecretKey: str
        """
        self.SignParam = None
        self.TimeParam = None
        self.TransactionParam = None
        self.SecretKey = None
        self.BackupSecretKey = None


    def _deserialize(self, params):
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.TransactionParam = params.get("TransactionParam")
        self.SecretKey = params.get("SecretKey")
        self.BackupSecretKey = params.get("BackupSecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AdvancedCache(AbstractModel):
    """缓存过期配置高级版（功能灰度中，尚未全量）
    注意：该版本不支持设置首页缓存规则

    """

    def __init__(self):
        """
        :param CacheRules: 缓存过期规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheRules: list of AdvanceCacheRule
        :param IgnoreCacheControl: 强制缓存配置
on：开启
off：关闭
开启时，源站返回 no-cache、no-store 头部时，仍按照缓存过期规则进行节点缓存
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: 当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        """
        self.CacheRules = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = AdvanceCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Authentication(AbstractModel):
    """时间戳防盗链配置

    """

    def __init__(self):
        """
        :param Switch: 防盗链配置开关
on：开启
off：关闭
开启时必须且只配置一种模式，其余模式需要设置为 null
        :type Switch: str
        :param TypeA: 时间戳防盗链模式 A 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`
        :param TypeB: 时间戳防盗链模式 B 配置（模式 B 后台升级中，暂时不支持配置）
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`
        :param TypeC: 时间戳防盗链模式 C 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`
        :param TypeD: 时间戳防盗链模式 D 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`
        """
        self.Switch = None
        self.TypeA = None
        self.TypeB = None
        self.TypeC = None
        self.TypeD = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = AuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        if params.get("TypeB") is not None:
            self.TypeB = AuthenticationTypeB()
            self.TypeB._deserialize(params.get("TypeB"))
        if params.get("TypeC") is not None:
            self.TypeC = AuthenticationTypeC()
            self.TypeC._deserialize(params.get("TypeC"))
        if params.get("TypeD") is not None:
            self.TypeD = AuthenticationTypeD()
            self.TypeD._deserialize(params.get("TypeD"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AuthenticationTypeA(AbstractModel):
    """时间戳防盗链模式 A 配置
    时间戳防盗链模式 A 的访问 URL 格式为：http://DomainName/Filename?sign=timestamp-rand-uid-md5hash
    其中 timestamp 为十进制 UNIX 时间戳；
    rand 为随机字符串，0 ~ 100 位大小写字母与数字组成；
    uid 为 0；
    md5hash：MD5（文件路径-timestamp-rand-uid-自定义密钥）

    """

    def __init__(self):
        """
        :param SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param SignParam: 签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :type SignParam: str
        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        """
        self.SecretKey = None
        self.SignParam = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.SignParam = params.get("SignParam")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AuthenticationTypeB(AbstractModel):
    """时间戳防盗链模式 B 配置（B 模式正在进行平台升级，暂不支持配置）

    """

    def __init__(self):
        """
        :param SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AuthenticationTypeC(AbstractModel):
    """时间戳防盗链模式 C 配置
    时间戳防盗链模式 C 的访问 URL 格式为：http://DomainName/md5hash/timestamp/FileName
    其中 timestamp 为十六进制 UNIX 时间戳；
    md5hash：MD5（自定义密钥 + 文件路径 + timestamp）

    """

    def __init__(self):
        """
        :param SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        :param TimeFormat: 时间戳进制设置
dec：十进制
hex：十六进制
注意：此字段可能返回 null，表示取不到有效值。
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AuthenticationTypeD(AbstractModel):
    """时间戳防盗链模式 D 配置
    时间戳防盗链模式 D 的访问 URL 格式为：http://DomainName/FileName?sign=md5hash&t=timestamp
    其中 timestamp 为十进制或十六进制 UNIX 时间戳；
    md5hash：MD5（自定义密钥 + 文件路径 + timestamp）

    """

    def __init__(self):
        """
        :param SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000
        :type ExpireTime: int
        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件
        :type FileExtensions: list of str
        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权
        :type FilterType: str
        :param SignParam: 签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :type SignParam: str
        :param TimeParam: 时间戳参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头
        :type TimeParam: str
        :param TimeFormat: 时间戳进制设置
dec：十进制
hex：十六进制
        :type TimeFormat: str
        """
        self.SecretKey = None
        self.ExpireTime = None
        self.FileExtensions = None
        self.FilterType = None
        self.SignParam = None
        self.TimeParam = None
        self.TimeFormat = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        self.ExpireTime = params.get("ExpireTime")
        self.FileExtensions = params.get("FileExtensions")
        self.FilterType = params.get("FilterType")
        self.SignParam = params.get("SignParam")
        self.TimeParam = params.get("TimeParam")
        self.TimeFormat = params.get("TimeFormat")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class AwsPrivateAccess(AbstractModel):
    """s3源站回源鉴权。

    """

    def __init__(self):
        """
        :param Switch: 开关，on/off。
        :type Switch: str
        :param AccessKey: 访问ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessKey: str
        :param SecretKey: 密钥。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        """
        self.Switch = None
        self.AccessKey = None
        self.SecretKey = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.AccessKey = params.get("AccessKey")
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BandwidthAlert(AbstractModel):
    """带宽封顶配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 带宽封顶配置开关
on：开启
off：关闭
        :type Switch: str
        :param BpsThreshold: 带宽封顶阈值，单位为bps
注意：此字段可能返回 null，表示取不到有效值。
        :type BpsThreshold: int
        :param CounterMeasure: 达到阈值后的操作
RESOLVE_DNS_TO_ORIGIN：直接回源，仅自有源站域名支持
RETURN_404：全部请求返回 404
注意：此字段可能返回 null，表示取不到有效值。
        :type CounterMeasure: str
        :param LastTriggerTime: 上次触发带宽封顶阈值的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type LastTriggerTime: str
        """
        self.Switch = None
        self.BpsThreshold = None
        self.CounterMeasure = None
        self.LastTriggerTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.BpsThreshold = params.get("BpsThreshold")
        self.CounterMeasure = params.get("CounterMeasure")
        self.LastTriggerTime = params.get("LastTriggerTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BotCookie(AbstractModel):
    """Bot cookie策略

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        :param RuleType: 规则类型，当前只有all
        :type RuleType: str
        :param RuleValue: 规则值，['*']
        :type RuleValue: list of str
        :param Action: 执行动作，monitor|intercept|redirect|captcha
        :type Action: str
        :param RedirectUrl: 重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Switch = None
        self.RuleType = None
        self.RuleValue = None
        self.Action = None
        self.RedirectUrl = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleType = params.get("RuleType")
        self.RuleValue = params.get("RuleValue")
        self.Action = params.get("Action")
        self.RedirectUrl = params.get("RedirectUrl")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BotJavaScript(AbstractModel):
    """Bot js策略

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        :param RuleType: 规则类型，当前只有file
        :type RuleType: str
        :param RuleValue: 规则值，['html', 'htm']
        :type RuleValue: list of str
        :param Action: 执行动作，monitor|intercept|redirect|captcha
        :type Action: str
        :param RedirectUrl: 重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Switch = None
        self.RuleType = None
        self.RuleValue = None
        self.Action = None
        self.RedirectUrl = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RuleType = params.get("RuleType")
        self.RuleValue = params.get("RuleValue")
        self.Action = params.get("Action")
        self.RedirectUrl = params.get("RedirectUrl")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class BriefDomain(AbstractModel):
    """域名基础配置信息，含 CNAME、状态、业务类型、加速区域、创建时间、更新时间、源站配置等。

    """

    def __init__(self):
        """
        :param ResourceId: 域名 ID
        :type ResourceId: str
        :param AppId: 腾讯云账号 ID
        :type AppId: int
        :param Domain: 加速域名
        :type Domain: str
        :param Cname: 域名对应的 CNAME 地址
        :type Cname: str
        :param Status: 加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
online：已启动
offline：已关闭
        :type Status: str
        :param ProjectId: 项目 ID，可前往腾讯云项目管理页面查看
        :type ProjectId: int
        :param ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :type ServiceType: str
        :param CreateTime: 域名创建时间
        :type CreateTime: str
        :param UpdateTime: 域名更新时间
        :type UpdateTime: str
        :param Origin: 源站配置详情
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param Disable: 域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定
        :type Disable: str
        :param Area: 加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
        :type Area: str
        :param Readonly: 域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
        :type Readonly: str
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
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
        self.ServiceType = params.get("ServiceType")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        self.Disable = params.get("Disable")
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Cache(AbstractModel):
    """节点缓存过期时间配置，分为以下两种：
    + 基础版缓存过期规则配置
    + 高级版缓存过期规则配置

    """

    def __init__(self):
        """
        :param SimpleCache: 基础缓存过期时间配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SimpleCache: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`
        :param AdvancedCache: 高级缓存过期时间配置（功能灰度中，尚未全量）
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedCache: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`
        :param RuleCache: 高级路径缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleCache: list of RuleCache
        """
        self.SimpleCache = None
        self.AdvancedCache = None
        self.RuleCache = None


    def _deserialize(self, params):
        if params.get("SimpleCache") is not None:
            self.SimpleCache = SimpleCache()
            self.SimpleCache._deserialize(params.get("SimpleCache"))
        if params.get("AdvancedCache") is not None:
            self.AdvancedCache = AdvancedCache()
            self.AdvancedCache._deserialize(params.get("AdvancedCache"))
        if params.get("RuleCache") is not None:
            self.RuleCache = []
            for item in params.get("RuleCache"):
                obj = RuleCache()
                obj._deserialize(item)
                self.RuleCache.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheConfigCache(AbstractModel):
    """路径缓存缓存配置

    """

    def __init__(self):
        """
        :param Switch: 缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTime: int
        :param CompareMaxAge: 高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareMaxAge: str
        :param IgnoreCacheControl: 强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: 当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        """
        self.Switch = None
        self.CacheTime = None
        self.CompareMaxAge = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.CacheTime = params.get("CacheTime")
        self.CompareMaxAge = params.get("CompareMaxAge")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheConfigFollowOrigin(AbstractModel):
    """路径缓存遵循源站配置

    """

    def __init__(self):
        """
        :param Switch: 遵循源站配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheConfigNoCache(AbstractModel):
    """路径缓存不缓存配置

    """

    def __init__(self):
        """
        :param Switch: 不缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Revalidate: 总是回源站校验
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Revalidate: str
        """
        self.Switch = None
        self.Revalidate = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Revalidate = params.get("Revalidate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheKey(AbstractModel):
    """缓存键配置（过滤参数配置）

    """

    def __init__(self):
        """
        :param FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数过滤）
off：关闭全路径缓存（即开启参数过滤）
        :type FullUrlCache: str
        :param IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.QueryStringKey`
        :param Cookie: CacheKey中包含Cookie
注意：此字段可能返回 null，表示取不到有效值。
        :type Cookie: :class:`tencentcloud.cdn.v20180606.models.CookieKey`
        :param Header: CacheKey中包含请求头部
注意：此字段可能返回 null，表示取不到有效值。
        :type Header: :class:`tencentcloud.cdn.v20180606.models.HeaderKey`
        :param CacheTag: CacheKey中包含自定义字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheTag: :class:`tencentcloud.cdn.v20180606.models.CacheTagKey`
        :param Scheme: CacheKey中包含请求协议
注意：此字段可能返回 null，表示取不到有效值。
        :type Scheme: :class:`tencentcloud.cdn.v20180606.models.SchemeKey`
        :param KeyRules: 分路径缓存键配置
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyRules: list of KeyRule
        """
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None
        self.Cookie = None
        self.Header = None
        self.CacheTag = None
        self.Scheme = None
        self.KeyRules = None


    def _deserialize(self, params):
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = QueryStringKey()
            self.QueryString._deserialize(params.get("QueryString"))
        if params.get("Cookie") is not None:
            self.Cookie = CookieKey()
            self.Cookie._deserialize(params.get("Cookie"))
        if params.get("Header") is not None:
            self.Header = HeaderKey()
            self.Header._deserialize(params.get("Header"))
        if params.get("CacheTag") is not None:
            self.CacheTag = CacheTagKey()
            self.CacheTag._deserialize(params.get("CacheTag"))
        if params.get("Scheme") is not None:
            self.Scheme = SchemeKey()
            self.Scheme._deserialize(params.get("Scheme"))
        if params.get("KeyRules") is not None:
            self.KeyRules = []
            for item in params.get("KeyRules"):
                obj = KeyRule()
                obj._deserialize(item)
                self.KeyRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheOptResult(AbstractModel):
    """违规资源封禁/解封返回类型

    """

    def __init__(self):
        """
        :param SuccessUrls: 成功的url列表
注意：此字段可能返回 null，表示取不到有效值。
        :type SuccessUrls: list of str
        :param FailUrls: 失败的url列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FailUrls: list of str
        """
        self.SuccessUrls = None
        self.FailUrls = None


    def _deserialize(self, params):
        self.SuccessUrls = params.get("SuccessUrls")
        self.FailUrls = params.get("FailUrls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CacheTagKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: 是否使用CacheTag作为CacheKey的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Value: 自定义CacheTag的值
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Switch = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CappingRule(AbstractModel):
    """下行限速配置规则，最多可配置 100 条

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
        :type RuleType: str
        :param RulePaths: RuleType 对应类型下的匹配内容： 
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
        :type RulePaths: list of str
        :param KBpsThreshold: 下行速度值设置，单位为 KB/s
        :type KBpsThreshold: int
        """
        self.RuleType = None
        self.RulePaths = None
        self.KBpsThreshold = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.KBpsThreshold = params.get("KBpsThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CdnData(AbstractModel):
    """访问明细数据类型

    """

    def __init__(self):
        """
        :param Metric: 查询指定的指标名称：
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
        :param DetailData: 明细数据组合
        :type DetailData: list of TimestampData
        :param SummarizedData: 汇总数据组合
        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`
        """
        self.Metric = None
        self.DetailData = None
        self.SummarizedData = None


    def _deserialize(self, params):
        self.Metric = params.get("Metric")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        if params.get("SummarizedData") is not None:
            self.SummarizedData = SummarizedData()
            self.SummarizedData._deserialize(params.get("SummarizedData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CdnIp(AbstractModel):
    """IP 属性信息

    """

    def __init__(self):
        """
        :param Ip: 指定查询的 IP
        :type Ip: str
        :param Platform: IP 归属：
yes：节点归属于腾讯云 CDN
no：节点不属于腾讯云 CDN
        :type Platform: str
        :param Location: 节点所处的省份/国家
unknown 表示节点位置未知
        :type Location: str
        :param History: 节点上下线历史记录
        :type History: list of CdnIpHistory
        :param Area: 节点的所在区域
mainland：中国境内加速节点
overseas：中国境外加速节点
unknown：服务地域无法获取
        :type Area: str
        :param City: 节点的所在城市
注意：此字段可能返回 null，表示取不到有效值。
        :type City: str
        """
        self.Ip = None
        self.Platform = None
        self.Location = None
        self.History = None
        self.Area = None
        self.City = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.Platform = params.get("Platform")
        self.Location = params.get("Location")
        if params.get("History") is not None:
            self.History = []
            for item in params.get("History"):
                obj = CdnIpHistory()
                obj._deserialize(item)
                self.History.append(obj)
        self.Area = params.get("Area")
        self.City = params.get("City")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CdnIpHistory(AbstractModel):
    """CDN 节点上下线历史记录

    """

    def __init__(self):
        """
        :param Status: 操作类型
online：节点上线
offline：节点下线
        :type Status: str
        :param Datetime: 操作类型对应的操作时间
当该值为 null 时表示无历史状态变更记录
注意：此字段可能返回 null，表示取不到有效值。
        :type Datetime: str
        """
        self.Status = None
        self.Datetime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Datetime = params.get("Datetime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClientCert(AbstractModel):
    """https 客户端证书配置

    """

    def __init__(self):
        """
        :param Certificate: 客户端证书
PEM 格式，需要进行 Base 64 编码
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param CertName: 客户端证书名称
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param ExpireTime: 证书过期时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书颁发时间
作为入参时无需填充
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClientInfo(AbstractModel):
    """客户端信息

    """

    def __init__(self):
        """
        :param ProvName: 省份。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProvName: str
        :param Country: 国家。
注意：此字段可能返回 null，表示取不到有效值。
        :type Country: str
        :param IspName: 运营商。
注意：此字段可能返回 null，表示取不到有效值。
        :type IspName: str
        :param Ip: 客户端IP
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        """
        self.ProvName = None
        self.Country = None
        self.IspName = None
        self.Ip = None


    def _deserialize(self, params):
        self.ProvName = params.get("ProvName")
        self.Country = params.get("Country")
        self.IspName = params.get("IspName")
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClsLogObject(AbstractModel):
    """CLS日志搜索对象

    """

    def __init__(self):
        """
        :param TopicId: 主题ID
        :type TopicId: str
        :param TopicName: 主题名字
        :type TopicName: str
        :param Timestamp: 日志时间
        :type Timestamp: str
        :param Content: 日志内容
        :type Content: str
        :param Filename: 采集路径
        :type Filename: str
        :param Source: 日志来源设备
        :type Source: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Timestamp = None
        self.Content = None
        self.Filename = None
        self.Source = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Timestamp = params.get("Timestamp")
        self.Content = params.get("Content")
        self.Filename = params.get("Filename")
        self.Source = params.get("Source")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ClsSearchLogs(AbstractModel):
    """Cls日志搜索结果

    """

    def __init__(self):
        """
        :param Context: 获取更多检索结果的游标
        :type Context: str
        :param Listover: 搜索结果是否已经全部返回
        :type Listover: bool
        :param Results: 日志内容信息
        :type Results: list of ClsLogObject
        """
        self.Context = None
        self.Listover = None
        self.Results = None


    def _deserialize(self, params):
        self.Context = params.get("Context")
        self.Listover = params.get("Listover")
        if params.get("Results") is not None:
            self.Results = []
            for item in params.get("Results"):
                obj = ClsLogObject()
                obj._deserialize(item)
                self.Results.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Compatibility(AbstractModel):
    """是否兼容旧版配置

    """

    def __init__(self):
        """
        :param Code: 兼容标志状态码。
注意：此字段可能返回 null，表示取不到有效值。
        :type Code: int
        """
        self.Code = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Compression(AbstractModel):
    """智能压缩配置，默认对 js、html、css、xml、json、shtml、htm 后缀且大小为 256 ~ 2097152 字节的文件进行 GZIP 压缩

    """

    def __init__(self):
        """
        :param Switch: 智能压缩配置开关
on：开启
off：关闭
        :type Switch: str
        :param CompressionRules: 压缩规则数组
注意：此字段可能返回 null，表示取不到有效值。
        :type CompressionRules: list of CompressionRule
        """
        self.Switch = None
        self.CompressionRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CompressionRules") is not None:
            self.CompressionRules = []
            for item in params.get("CompressionRules"):
                obj = CompressionRule()
                obj._deserialize(item)
                self.CompressionRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CompressionRule(AbstractModel):
    """压缩规则配置，最多可设置 100 条

    """

    def __init__(self):
        """
        :param Compress: true：需要设置为 ture，启用压缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Compress: bool
        :param FileExtensions: 根据文件后缀类型压缩
例如 jpg、txt
注意：此字段可能返回 null，表示取不到有效值。
        :type FileExtensions: list of str
        :param MinLength: 触发压缩的文件长度最小值，单位为字节数
注意：此字段可能返回 null，表示取不到有效值。
        :type MinLength: int
        :param MaxLength: 触发压缩的文件长度最大值，单位为字节数
最大可设置为 30MB
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxLength: int
        :param Algorithms: 文件压缩算法
gzip：指定 GZIP 压缩
brotli：指定Brotli压缩
注意：此字段可能返回 null，表示取不到有效值。
        :type Algorithms: list of str
        """
        self.Compress = None
        self.FileExtensions = None
        self.MinLength = None
        self.MaxLength = None
        self.Algorithms = None


    def _deserialize(self, params):
        self.Compress = params.get("Compress")
        self.FileExtensions = params.get("FileExtensions")
        self.MinLength = params.get("MinLength")
        self.MaxLength = params.get("MaxLength")
        self.Algorithms = params.get("Algorithms")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CookieKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: on | off 是否使用Cookie作为Cache的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Value: 使用的cookie，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Switch = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClsLogTopicRequest(AbstractModel):
    """CreateClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        :param DomainAreaConfigs: 域名区域信息
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self.TopicName = None
        self.LogsetId = None
        self.Channel = None
        self.DomainAreaConfigs = None


    def _deserialize(self, params):
        self.TopicName = params.get("TopicName")
        self.LogsetId = params.get("LogsetId")
        self.Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateClsLogTopicResponse(AbstractModel):
    """CreateClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 主题ID
注意：此字段可能返回 null，表示取不到有效值。
        :type TopicId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDiagnoseUrlRequest(AbstractModel):
    """CreateDiagnoseUrl请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 需诊断的url，形如：http://www.test.com/test.txt。
        :type Url: str
        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateDiagnoseUrlResponse(AbstractModel):
    """CreateDiagnoseUrl返回参数结构体

    """

    def __init__(self):
        """
        :param DiagnoseLink: 系统生成的诊断链接，一个诊断链接最多可访问10次，有效期为24h。
        :type DiagnoseLink: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DiagnoseLink = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiagnoseLink = params.get("DiagnoseLink")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateEdgePackTaskRequest(AbstractModel):
    """CreateEdgePackTask请求参数结构体

    """

    def __init__(self):
        """
        :param CosBucket: apk 所在的 cos 存储桶, 如 edgepack-xxxxxxxx
        :type CosBucket: str
        :param CosUriFrom: apk 源文件的存储路径, 如 /apk/xxxx.apk
        :type CosUriFrom: str
        :param BlockID: BlockID 的值, WALLE为1903654775(0x71777777)，VasDolly为2282837503(0x881155ff),传0或不传时默认为 WALLE 方案
        :type BlockID: int
        :param CosUriTo: 拓展之后的 apk 目标存储路径,如 /out/xxxx.apk
        :type CosUriTo: str
        """
        self.CosBucket = None
        self.CosUriFrom = None
        self.BlockID = None
        self.CosUriTo = None


    def _deserialize(self, params):
        self.CosBucket = params.get("CosBucket")
        self.CosUriFrom = params.get("CosUriFrom")
        self.BlockID = params.get("BlockID")
        self.CosUriTo = params.get("CosUriTo")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateEdgePackTaskResponse(AbstractModel):
    """CreateEdgePackTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateScdnFailedLogTaskRequest(AbstractModel):
    """CreateScdnFailedLogTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 重试失败任务的taskID
        :type TaskId: str
        :param Area: 地域：mainland或overseas
        :type Area: str
        """
        self.TaskId = None
        self.Area = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateScdnFailedLogTaskResponse(AbstractModel):
    """CreateScdnFailedLogTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果, 
"0" -> 创建成功
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateScdnLogTaskRequest(AbstractModel):
    """CreateScdnLogTask请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 防护类型
Mode 映射如下：
  waf = "Web攻击"
  cc = "CC攻击"
  bot = "Bot攻击"
        :type Mode: str
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param Domain: 指定域名查询, 不填默认查询全部域名
        :type Domain: str
        :param AttackType: 指定攻击类型, 不填默认查询全部攻击类型
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
        :param DefenceMode: 指定执行动作, 不填默认查询全部执行动作
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
  captcha = "验证码"
  redirect = "重定向"
        :type DefenceMode: str
        :param Ip: 不填为全部ip
        :type Ip: str
        :param Domains: 指定域名查询, 与 Domain 参数同时有值时使用 Domains 参数，不填默认查询全部域名，指定域名查询时最多支持同时选择 5 个域名查询
        :type Domains: list of str
        :param AttackTypes: 指定攻击类型查询, 与 AttackType 参数同时有值时使用 AttackTypes 参数，不填默认查询全部攻击类型
        :type AttackTypes: list of str
        :param Conditions: 查询条件
        :type Conditions: list of ScdnEventLogConditions
        :param Source: 来源产品 cdn ecdn
        :type Source: str
        :param Area: 地域：mainland 或 overseas
        :type Area: str
        """
        self.Mode = None
        self.StartTime = None
        self.EndTime = None
        self.Domain = None
        self.AttackType = None
        self.DefenceMode = None
        self.Ip = None
        self.Domains = None
        self.AttackTypes = None
        self.Conditions = None
        self.Source = None
        self.Area = None


    def _deserialize(self, params):
        self.Mode = params.get("Mode")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domain = params.get("Domain")
        self.AttackType = params.get("AttackType")
        self.DefenceMode = params.get("DefenceMode")
        self.Ip = params.get("Ip")
        self.Domains = params.get("Domains")
        self.AttackTypes = params.get("AttackTypes")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ScdnEventLogConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Source = params.get("Source")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateScdnLogTaskResponse(AbstractModel):
    """CreateScdnLogTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果, 
"0" -> 创建成功
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVerifyRecordRequest(AbstractModel):
    """CreateVerifyRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 要取回的域名
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class CreateVerifyRecordResponse(AbstractModel):
    """CreateVerifyRecord返回参数结构体

    """

    def __init__(self):
        """
        :param SubDomain: 子解析
        :type SubDomain: str
        :param Record: 解析值
        :type Record: str
        :param RecordType: 解析类型
        :type RecordType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SubDomain = None
        self.Record = None
        self.RecordType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.Record = params.get("Record")
        self.RecordType = params.get("RecordType")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
域名状态需要为【已停用】
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClsLogTopicRequest(AbstractModel):
    """DeleteClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        """
        self.TopicId = None
        self.LogsetId = None
        self.Channel = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.LogsetId = params.get("LogsetId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteClsLogTopicResponse(AbstractModel):
    """DeleteClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteScdnDomainRequest(AbstractModel):
    """DeleteScdnDomain请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DeleteScdnDomainResponse(AbstractModel):
    """DeleteScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果，Success表示成功
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定起始时间为 2018-09-04 10:40:00 按小时粒度查询，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定结束时间为  2018-09-04 10:40:00 按小时粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type EndTime: str
        :param Interval: 时间粒度，支持模式如下：
min：1 分钟粒度，查询区间需要小于等于 24 小时
5min：5 分钟粒度，查询区间需要小于等于 31 天
hour：1 小时粒度，查询区间需要小于等于 31 天内
day：天粒度，查询区间需要大于 31 天

Area 字段为 overseas 时暂不支持1分钟粒度数据查询
        :type Interval: str
        :param Domain: 指定域名查询计费数据
        :type Domain: str
        :param Project: 指定项目 ID 查询，[前往查看项目 ID](https://console.cloud.tencent.com/project)
若 Domain 参数填充了具体域名信息，则返回该域名的计费数据，而非指定项目计费数据
        :type Project: int
        :param Area: 指定加速区域查询计费数据：
mainland：中国境内
overseas：中国境外
不填充时，默认为 mainland
        :type Area: str
        :param District: Area 为 overseas 时，指定国家/地区查询
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
不填充时，查询所有国家/地区
        :type District: int
        :param Metric: 计费统计类型
flux：计费流量
bandwidth：计费带宽
默认为 bandwidth
        :type Metric: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.Domain = None
        self.Project = None
        self.Area = None
        self.District = None
        self.Metric = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.Domain = params.get("Domain")
        self.Project = params.get("Project")
        self.Area = params.get("Area")
        self.District = params.get("District")
        self.Metric = params.get("Metric")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 时间粒度，根据查询时传递参数指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :type Interval: str
        :param Data: 数据明细
        :type Data: list of ResourceBillingData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceBillingData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type EndTime: str
        :param Metric: 指定查询指标，支持的类型有：
flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
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
        :param Domains: 指定查询域名列表
最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :type Interval: str
        :param Detail: 多域名查询时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）
        :type Detail: bool
        :param Isp: 查询中国境内CDN数据时，指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定运营商查询时，不可同时指定省份、IP协议查询
        :type Isp: int
        :param District: 查询中国境内CDN数据时，指定省份查询，不填充表示查询所有省份
查询中国境外CDN数据时，指定国家/地区查询，不填充表示查询所有国家/地区
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定（中国境内）省份查询时，不可同时指定运营商、IP协议查询
        :type District: int
        :param Protocol: 指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标
        :type Protocol: str
        :param DataSource: 指定数据源查询，白名单功能
        :type DataSource: str
        :param IpProtocol: 指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
注意：非IPv6白名单用户不可指定ipv4、ipv6进行查询
        :type IpProtocol: str
        :param Area: 指定服务地域查询，不填充表示查询中国境内CDN数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :type Area: str
        :param AreaType: 查询中国境外CDN数据时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据
        :type AreaType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Isp = None
        self.District = None
        self.Protocol = None
        self.DataSource = None
        self.IpProtocol = None
        self.Area = None
        self.AreaType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Isp = params.get("Isp")
        self.District = params.get("District")
        self.Protocol = params.get("Protocol")
        self.DataSource = params.get("DataSource")
        self.IpProtocol = params.get("IpProtocol")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 返回数据的时间粒度，查询时指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度
        :type Interval: str
        :param Data: 指定条件查询得到的数据明细
        :type Data: list of ResourceData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 指定域名查询
        :type Domain: str
        :param StartTime: 开始时间，如 2019-09-04 00:00:00
        :type StartTime: str
        :param EndTime: 结束时间，如 2019-09-04 12:00:00
        :type EndTime: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大为 1000
        :type Limit: int
        :param Area: 指定区域下载日志
mainland：获取境内加速日志包下载链接
overseas：获取境外加速日志包下载链接
global：同时获取境内、境外加速日志包下载链接（分开打包）
不指定时默认为 mainland
        :type Area: str
        :param LogType: 指定下载日志的类型。
access：获取访问日志
        :type LogType: str
        """
        self.Domain = None
        self.StartTime = None
        self.EndTime = None
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.LogType = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.LogType = params.get("LogType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs返回参数结构体

    """

    def __init__(self):
        """
        :param DomainLogs: 日志包下载链接
        :type DomainLogs: list of DomainLog
        :param TotalCount: 查询到的总条数
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
                obj = DomainLog()
                obj._deserialize(item)
                self.DomainLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp请求参数结构体

    """

    def __init__(self):
        """
        :param Ips: 需要查询的 IP 列表
        :type Ips: list of str
        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp返回参数结构体

    """

    def __init__(self):
        """
        :param Ips: 查询的节点归属详情。
        :type Ips: list of CdnIp
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ips = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = CdnIp()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCdnOriginIpRequest(AbstractModel):
    """DescribeCdnOriginIp请求参数结构体

    """


class DescribeCdnOriginIpResponse(AbstractModel):
    """DescribeCdnOriginIp返回参数结构体

    """

    def __init__(self):
        """
        :param Ips: 回源节点IP详情。
        :type Ips: list of OriginIp
        :param TotalCount: 回源节点IP总个数。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ips = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = OriginIp()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCertDomainsRequest(AbstractModel):
    """DescribeCertDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Cert: PEM格式证书Base64编码后的字符串
        :type Cert: str
        """
        self.Cert = None


    def _deserialize(self, params):
        self.Cert = params.get("Cert")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeCertDomainsResponse(AbstractModel):
    """DescribeCertDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 已接入CDN的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Domains: list of str
        :param CertifiedDomains: 已配置证书的CDN域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CertifiedDomains: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.CertifiedDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.CertifiedDomains = params.get("CertifiedDomains")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDiagnoseReportRequest(AbstractModel):
    """DescribeDiagnoseReport请求参数结构体

    """

    def __init__(self):
        """
        :param ReportId: 报告ID
        :type ReportId: str
        """
        self.ReportId = None


    def _deserialize(self, params):
        self.ReportId = params.get("ReportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDiagnoseReportResponse(AbstractModel):
    """DescribeDiagnoseReport返回参数结构体

    """

    def __init__(self):
        """
        :param BaskInfo: 诊断报告基础信息
        :type BaskInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param CnameInfo: CNAME检测信息
        :type CnameInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param ClientInfo: 客户端检测信息
        :type ClientInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param DnsInfo: DNS检测信息
        :type DnsInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param NetworkInfo: 网络检测信息
        :type NetworkInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param OcNodeInfo: 边缘节点检测信息
        :type OcNodeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param MidNodeInfo: 中间源节点检测信息
        :type MidNodeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param OriginInfo: 源站检测信息
        :type OriginInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BaskInfo = None
        self.CnameInfo = None
        self.ClientInfo = None
        self.DnsInfo = None
        self.NetworkInfo = None
        self.OcNodeInfo = None
        self.MidNodeInfo = None
        self.OriginInfo = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("BaskInfo") is not None:
            self.BaskInfo = DiagnoseData()
            self.BaskInfo._deserialize(params.get("BaskInfo"))
        if params.get("CnameInfo") is not None:
            self.CnameInfo = DiagnoseData()
            self.CnameInfo._deserialize(params.get("CnameInfo"))
        if params.get("ClientInfo") is not None:
            self.ClientInfo = DiagnoseData()
            self.ClientInfo._deserialize(params.get("ClientInfo"))
        if params.get("DnsInfo") is not None:
            self.DnsInfo = DiagnoseData()
            self.DnsInfo._deserialize(params.get("DnsInfo"))
        if params.get("NetworkInfo") is not None:
            self.NetworkInfo = DiagnoseData()
            self.NetworkInfo._deserialize(params.get("NetworkInfo"))
        if params.get("OcNodeInfo") is not None:
            self.OcNodeInfo = DiagnoseData()
            self.OcNodeInfo._deserialize(params.get("OcNodeInfo"))
        if params.get("MidNodeInfo") is not None:
            self.MidNodeInfo = DiagnoseData()
            self.MidNodeInfo._deserialize(params.get("MidNodeInfo"))
        if params.get("OriginInfo") is not None:
            self.OriginInfo = DiagnoseData()
            self.OriginInfo._deserialize(params.get("OriginInfo"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDistrictIspDataRequest(AbstractModel):
    """DescribeDistrictIspData请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表，最多支持20个域名
        :type Domains: list of str
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
支持近 60 天内的数据查询，每次查询时间区间为 3 小时
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
结束时间与起始时间区间最大为 3 小时
        :type EndTime: str
        :param Metric: 指定查询指标，支持:
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
        :type Metric: str
        :param Districts: 指定省份查询，不填充表示查询所有省份
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
        :type Districts: list of int
        :param Isps: 指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
        :type Isps: list of int
        :param Protocol: 指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标
        :type Protocol: str
        :param IpProtocol: 指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
        :type IpProtocol: str
        :param Interval: 时间粒度，支持以下几种模式（默认5min）：
min：1 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过10分钟，可返回 1 分钟粒度明细数据
5min：5 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过3 小时，可返回 5 分钟粒度明细数据
        :type Interval: str
        """
        self.Domains = None
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Districts = None
        self.Isps = None
        self.Protocol = None
        self.IpProtocol = None
        self.Interval = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Districts = params.get("Districts")
        self.Isps = params.get("Isps")
        self.Protocol = params.get("Protocol")
        self.IpProtocol = params.get("IpProtocol")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDistrictIspDataResponse(AbstractModel):
    """DescribeDistrictIspData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 地区运营商数据明细
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DistrictIspInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DistrictIspInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Filters: 查询条件过滤器，复杂类型
        :type Filters: list of DomainFilter
        :param Sort: 排序规则
        :type Sort: :class:`tencentcloud.cdn.v20180606.models.Sort`
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表
        :type Domains: list of DetailDomain
        :param TotalNumber: 符合查询条件的域名总数
用于分页查询
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = DetailDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000
        :type Limit: int
        :param Filters: 查询条件过滤器，复杂类型
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表
        :type Domains: list of BriefDomain
        :param TotalNumber: 符合查询条件的域名总数
用于分页查询
        :type TotalNumber: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Domains = None
        self.TotalNumber = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Domains") is not None:
            self.Domains = []
            for item in params.get("Domains"):
                obj = BriefDomain()
                obj._deserialize(item)
                self.Domains.append(obj)
        self.TotalNumber = params.get("TotalNumber")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageConfigRequest(AbstractModel):
    """DescribeImageConfig请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeImageConfigResponse(AbstractModel):
    """DescribeImageConfig返回参数结构体

    """

    def __init__(self):
        """
        :param WebpAdapter: WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 加速域名
        :type Domain: str
        :param Layer: 节点类型：
edge：表示边缘节点
last：表示回源层节点
不填充情况下，默认返回边缘节点信息
        :type Layer: str
        :param Area: 查询区域：
mainland: 国内节点
overseas: 海外节点
global: 全球节点
        :type Area: str
        """
        self.Domain = None
        self.Layer = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Layer = params.get("Layer")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Ips: 节点列表
        :type Ips: list of IpStatus
        :param TotalCount: 节点总个数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Ips = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Ips") is not None:
            self.Ips = []
            for item in params.get("Ips"):
                obj = IpStatus()
                obj._deserialize(item)
                self.Ips.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:10，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:40:00
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:10，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:40:00
        :type EndTime: str
        :param Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param Interval: 时间粒度，支持以下几种模式：
5min：5 分钟粒度，查询时间区间 24 小时内，默认返回 5 分钟粒度活跃用户数
day：天粒度，查询时间区间大于 1 天时，默认返回天粒度活跃用户数
        :type Interval: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Domains = None
        self.Project = None
        self.Interval = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 数据统计的时间粒度，支持5min,  day，分别表示5分钟，1天的时间粒度。
        :type Interval: str
        :param Data: 各个资源的回源数据详情。
        :type Data: list of ResourceData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 映射查询类别：
isp：运营商映射查询
district：省份（中国境内）、国家/地区（中国境外）映射查询
        :type Name: str
        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MapInfoList: 映射关系数组。
        :type MapInfoList: list of MapInfo
        :param ServerRegionRelation: 服务端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerRegionRelation: list of RegionMapRelation
        :param ClientRegionRelation: 客户端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientRegionRelation: list of RegionMapRelation
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.MapInfoList = None
        self.ServerRegionRelation = None
        self.ClientRegionRelation = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("MapInfoList") is not None:
            self.MapInfoList = []
            for item in params.get("MapInfoList"):
                obj = MapInfo()
                obj._deserialize(item)
                self.MapInfoList.append(obj)
        if params.get("ServerRegionRelation") is not None:
            self.ServerRegionRelation = []
            for item in params.get("ServerRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ServerRegionRelation.append(obj)
        if params.get("ClientRegionRelation") is not None:
            self.ClientRegionRelation = []
            for item in params.get("ClientRegionRelation"):
                obj = RegionMapRelation()
                obj._deserialize(item)
                self.ClientRegionRelation.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天
        :type EndTime: str
        :param Metric: 指定查询指标，支持的类型有：
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
        :param Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，最多可一次性查询 30 个加速域名明细
若填充了具体域名信息，以域名为主
        :type Project: int
        :param Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据
        :type Interval: str
        :param Detail: Domains 传入多个时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）
        :type Detail: bool
        :param Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据
        :type Area: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Domains = None
        self.Project = None
        self.Interval = None
        self.Detail = None
        self.Area = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Interval = params.get("Interval")
        self.Detail = params.get("Detail")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 数据统计的时间粒度，支持min, 5min, hour, day，分别表示1分钟，5分钟，1小时和1天的时间粒度。
        :type Interval: str
        :param Data: 各个资源的回源数据详情。
        :type Data: list of ResourceOriginData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Interval = None
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Interval = params.get("Interval")
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = ResourceOriginData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType请求参数结构体

    """

    def __init__(self):
        """
        :param Area: 指定服务地域查询
mainland：境内计费方式查询
overseas：境外计费方式查询
未填充时默认为 mainland
        :type Area: str
        """
        self.Area = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType返回参数结构体

    """

    def __init__(self):
        """
        :param PayType: 计费类型：
flux：流量计费
bandwidth：带宽计费
日结计费方式切换时，若当日产生消耗，则此字段表示第二天即将生效的计费方式，若未产生消耗，则表示已经生效的计费方式。
        :type PayType: str
        :param BillingCycle: 计费周期：
day：日结计费
month：月结计费
        :type BillingCycle: str
        :param StatType: 计费方式：
monthMax：日峰值月平均计费，月结模式
day95：日 95 带宽计费，月结模式
month95：月95带宽计费，月结模式
sum：总流量计费，日结与月结均有流量计费模式
max：峰值带宽计费，日结模式
        :type StatType: str
        :param RegionType: 境外计费类型：
all：全地区统一计费
multiple：分地区计费
        :type RegionType: str
        :param CurrentPayType: 当前生效计费类型：
flux：流量计费
bandwidth：带宽计费
        :type CurrentPayType: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PayType = None
        self.BillingCycle = None
        self.StatType = None
        self.RegionType = None
        self.CurrentPayType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PayType = params.get("PayType")
        self.BillingCycle = params.get("BillingCycle")
        self.StatType = params.get("StatType")
        self.RegionType = params.get("RegionType")
        self.CurrentPayType = params.get("CurrentPayType")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota请求参数结构体

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param UrlPurge: URL刷新用量及配额。
        :type UrlPurge: list of Quota
        :param PathPurge: 目录刷新用量及配额。
        :type PathPurge: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UrlPurge = None
        self.PathPurge = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self.UrlPurge = []
            for item in params.get("UrlPurge"):
                obj = Quota()
                obj._deserialize(item)
                self.UrlPurge.append(obj)
        if params.get("PathPurge") is not None:
            self.PathPurge = []
            for item in params.get("PathPurge"):
                obj = Quota()
                obj._deserialize(item)
                self.PathPurge.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param PurgeType: 指定刷新类型查询
url：url 刷新记录
path：目录刷新记录
        :type PurgeType: str
        :param StartTime: 根据时间区间查询时，填充开始时间，如 2018-08-08 00:00:00
        :type StartTime: str
        :param EndTime: 根据时间区间查询时，填充结束时间，如 2018-08-08 23:59:59
        :type EndTime: str
        :param TaskId: 根据任务 ID 查询时，填充任务 ID
查询时任务 ID 与起始时间必须填充一项
        :type TaskId: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 20
        :type Limit: int
        :param Keyword: 支持域名过滤，或 http(s):// 开头完整 URL 过滤
        :type Keyword: str
        :param Status: 指定任务状态查询
fail：刷新失败
done：刷新成功
process：刷新中
        :type Status: str
        :param Area: 指定刷新地域查询
mainland：境内
overseas：境外
global：全球
        :type Area: str
        """
        self.PurgeType = None
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Offset = None
        self.Limit = None
        self.Keyword = None
        self.Status = None
        self.Area = None


    def _deserialize(self, params):
        self.PurgeType = params.get("PurgeType")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Keyword = params.get("Keyword")
        self.Status = params.get("Status")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param PurgeLogs: 详细刷新记录
注意：此字段可能返回 null，表示取不到有效值。
        :type PurgeLogs: list of PurgeTask
        :param TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePushQuotaRequest(AbstractModel):
    """DescribePushQuota请求参数结构体

    """


class DescribePushQuotaResponse(AbstractModel):
    """DescribePushQuota返回参数结构体

    """

    def __init__(self):
        """
        :param UrlPush: Url预热用量及配额。
        :type UrlPush: list of Quota
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UrlPush = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlPush") is not None:
            self.UrlPush = []
            for item in params.get("UrlPush"):
                obj = Quota()
                obj._deserialize(item)
                self.UrlPush.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，如2018-08-08 00:00:00。
        :type StartTime: str
        :param EndTime: 结束时间，如2018-08-08 23:59:59。
        :type EndTime: str
        :param TaskId: 指定任务 ID 查询
TaskId 和起始时间必须指定一项
        :type TaskId: str
        :param Keyword: 查询关键字，请输入域名或 http(s):// 开头完整 URL
        :type Keyword: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 20
        :type Limit: int
        :param Area: 指定地区查询预热纪录
mainland：境内
overseas：境外
global：全球
        :type Area: str
        :param Status: 指定任务状态查询
fail：预热失败
done：预热成功
process：预热中
        :type Status: str
        """
        self.StartTime = None
        self.EndTime = None
        self.TaskId = None
        self.Keyword = None
        self.Offset = None
        self.Limit = None
        self.Area = None
        self.Status = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.TaskId = params.get("TaskId")
        self.Keyword = params.get("Keyword")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Area = params.get("Area")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks返回参数结构体

    """

    def __init__(self):
        """
        :param PushLogs: 预热历史记录
注意：此字段可能返回 null，表示取不到有效值。
        :type PushLogs: list of PushTask
        :param TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PushLogs = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("PushLogs") is not None:
            self.PushLogs = []
            for item in params.get("PushLogs"):
                obj = PushTask()
                obj._deserialize(item)
                self.PushLogs.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReportDataRequest(AbstractModel):
    """DescribeReportData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天
        :type StartTime: str
        :param EndTime: 查询结束时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天
        :type EndTime: str
        :param ReportType: 报表类型
daily：日报表
weekly：周报表（周一至周日）
monthly：月报表（自然月）
        :type ReportType: str
        :param Area: 域名加速区域
mainland：中国境内
overseas：中国境外
        :type Area: str
        :param Offset: 偏移量，默认0。
        :type Offset: int
        :param Limit: 数据个数，默认1000。
        :type Limit: int
        :param Project: 按项目ID筛选
        :type Project: int
        """
        self.StartTime = None
        self.EndTime = None
        self.ReportType = None
        self.Area = None
        self.Offset = None
        self.Limit = None
        self.Project = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.ReportType = params.get("ReportType")
        self.Area = params.get("Area")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Project = params.get("Project")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeReportDataResponse(AbstractModel):
    """DescribeReportData返回参数结构体

    """

    def __init__(self):
        """
        :param DomainReport: 域名维度数据详情
        :type DomainReport: list of ReportData
        :param ProjectReport: 项目维度数据详情
        :type ProjectReport: list of ReportData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainReport = None
        self.ProjectReport = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainReport") is not None:
            self.DomainReport = []
            for item in params.get("DomainReport"):
                obj = ReportData()
                obj._deserialize(item)
                self.DomainReport.append(obj)
        if params.get("ProjectReport") is not None:
            self.ProjectReport = []
            for item in params.get("ProjectReport"):
                obj = ReportData()
                obj._deserialize(item)
                self.ProjectReport.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeScdnConfigRequest(AbstractModel):
    """DescribeScdnConfig请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeScdnConfigResponse(AbstractModel):
    """DescribeScdnConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Acl: 自定义防护策略配置
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param Waf: Web 攻击防护（WAF）配置
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param CC: CC 防护配置
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param Ddos: DDOS 防护配置
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param Bot: BOT 防护配置
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        :param Status: 当前状态，取值online | offline
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Acl = None
        self.Waf = None
        self.CC = None
        self.Ddos = None
        self.Bot = None
        self.Status = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Acl") is not None:
            self.Acl = ScdnAclConfig()
            self.Acl._deserialize(params.get("Acl"))
        if params.get("Waf") is not None:
            self.Waf = ScdnWafConfig()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("CC") is not None:
            self.CC = ScdnConfig()
            self.CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self.Ddos = ScdnDdosConfig()
            self.Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self.Bot = ScdnBotConfig()
            self.Bot._deserialize(params.get("Bot"))
        self.Status = params.get("Status")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeScdnTopDataRequest(AbstractModel):
    """DescribeScdnTopData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
        :type StartTime: str
        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
        :type EndTime: str
        :param Mode: 查询的SCDN TOP攻击数据类型：
waf：Web 攻击防护TOP数据
        :type Mode: str
        :param Metric: 排序对象，支持以下几种形式：
url：攻击目标 url 排序
ip：攻击源 IP 排序
attackType：攻击类型排序
        :type Metric: str
        :param Filter: 排序使用的指标名称：
request：请求次数
        :type Filter: str
        :param Domain: 指定域名查询
        :type Domain: str
        :param AttackType: 指定攻击类型, 仅 Mode=waf 时有效
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
        :param DefenceMode: 指定防御模式,仅 Mode=waf 时有效
不填则查询所有防御模式的数据总和
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
        :type DefenceMode: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Mode = None
        self.Metric = None
        self.Filter = None
        self.Domain = None
        self.AttackType = None
        self.DefenceMode = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Mode = params.get("Mode")
        self.Metric = params.get("Metric")
        self.Filter = params.get("Filter")
        self.Domain = params.get("Domain")
        self.AttackType = params.get("AttackType")
        self.DefenceMode = params.get("DefenceMode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeScdnTopDataResponse(AbstractModel):
    """DescribeScdnTopData返回参数结构体

    """

    def __init__(self):
        """
        :param TopTypeData: WAF 攻击类型统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TopTypeData: list of ScdnTypeData
        :param TopIpData: TOP 攻击源 IP 统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TopIpData: list of ScdnTopData
        :param Mode: 查询的SCDN类型，当前仅支持 waf
        :type Mode: str
        :param TopUrlData: TOP URL 统计
注意：此字段可能返回 null，表示取不到有效值。
        :type TopUrlData: list of ScdnTopUrlData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TopTypeData = None
        self.TopIpData = None
        self.Mode = None
        self.TopUrlData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TopTypeData") is not None:
            self.TopTypeData = []
            for item in params.get("TopTypeData"):
                obj = ScdnTypeData()
                obj._deserialize(item)
                self.TopTypeData.append(obj)
        if params.get("TopIpData") is not None:
            self.TopIpData = []
            for item in params.get("TopIpData"):
                obj = ScdnTopData()
                obj._deserialize(item)
                self.TopIpData.append(obj)
        self.Mode = params.get("Mode")
        if params.get("TopUrlData") is not None:
            self.TopUrlData = []
            for item in params.get("TopUrlData"):
                obj = ScdnTopUrlData()
                obj._deserialize(item)
                self.TopUrlData.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTrafficPackagesRequest(AbstractModel):
    """DescribeTrafficPackages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询起始地址，默认 0
        :type Offset: int
        :param Limit: 分页查询记录个数，默认100，最大1000
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeTrafficPackagesResponse(AbstractModel):
    """DescribeTrafficPackages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 流量包总个数
        :type TotalCount: int
        :param TrafficPackages: 流量包详情
        :type TrafficPackages: list of TrafficPackage
        :param ExpiringCount: 即将过期的流量包个数（7天内）
        :type ExpiringCount: int
        :param EnabledCount: 有效流量包个数
        :type EnabledCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.TrafficPackages = None
        self.ExpiringCount = None
        self.EnabledCount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("TrafficPackages") is not None:
            self.TrafficPackages = []
            for item in params.get("TrafficPackages"):
                obj = TrafficPackage()
                obj._deserialize(item)
                self.TrafficPackages.append(obj)
        self.ExpiringCount = params.get("ExpiringCount")
        self.EnabledCount = params.get("EnabledCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为 100
        :type Limit: int
        :param Domains: 指定的域名查询
        :type Domains: list of str
        """
        self.Offset = None
        self.Limit = None
        self.Domains = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domains = params.get("Domains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations返回参数结构体

    """

    def __init__(self):
        """
        :param UrlRecordList: 违规 URL 详情
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of ViolationUrl
        :param TotalCount: 记录总数，用于分页
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = ViolationUrl()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DetailDomain(AbstractModel):
    """加速域名全量配置信息

    """

    def __init__(self):
        """
        :param ResourceId: 域名 ID
        :type ResourceId: str
        :param AppId: 腾讯云账号ID
        :type AppId: int
        :param Domain: 加速域名
        :type Domain: str
        :param Cname: 域名对应的 CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param Status: 加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
online：已启动
offline：已关闭
        :type Status: str
        :param ProjectId: 项目 ID，可前往腾讯云项目管理页面查看
        :type ProjectId: int
        :param ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :type ServiceType: str
        :param CreateTime: 域名创建时间
        :type CreateTime: str
        :param UpdateTime: 域名更新时间
        :type UpdateTime: str
        :param Origin: 源站配置
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP 黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP 访问限频配置
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: 状态码缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: 智能压缩配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: 带宽封顶配置
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range 回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 回源自动跟随配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: 自定义错误页面配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: 自定义请求头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 自定义响应头部配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: 单链接下行限速配置
注意：此字段可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: 带参/不带参缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: 源站头部缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: 视频拖拽配置
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: 节点缓存过期规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: 跨国链路优化配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https 加速相关配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: 时间戳防盗链配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO 优化配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param Disable: 域名封禁状态
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
        :param ForceRedirect: 访问协议强制跳转配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer 防盗链配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: 浏览器缓存过期规则配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Ipv6: Ipv6 回源配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`
        :param Compatibility: 是否兼容旧版本配置（内部兼容性字段）
注意：此字段可能返回 null，表示取不到有效值。
        :type Compatibility: :class:`tencentcloud.cdn.v20180606.models.Compatibility`
        :param SpecificConfig: 区域特殊配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: 加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param Readonly: 域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
注意：此字段可能返回 null，表示取不到有效值。
        :type Readonly: str
        :param OriginPullTimeout: 回源超时配置
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param AwsPrivateAccess: 回源S3鉴权配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param SecurityConfig: Scdn配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SecurityConfig: :class:`tencentcloud.cdn.v20180606.models.SecurityConfig`
        :param ImageOptimization: ImageOptimization配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ImageOptimization: :class:`tencentcloud.cdn.v20180606.models.ImageOptimization`
        :param UserAgentFilter: UA黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param AccessControl: 访问控制
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param Advance: 是否支持高级配置项
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。
        :type Advance: str
        :param UrlRedirect: URL重定向配置
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param AccessPort: 访问端口配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessPort: list of int
        :param Tag: 标签配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param AdvancedAuthentication: 时间戳防盗链高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param OriginAuthentication: 回源鉴权高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param Ipv6Access: Ipv6访问配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param AdvanceSet: 高级配置集合。
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceSet: list of AdvanceConfig
        :param OfflineCache: 离线缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param OriginCombine: 合并回源
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param PostMaxSize: POST上传配置项
注意：此字段可能返回 null，表示取不到有效值。
        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`
        :param Quic: Quic配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        """
        self.ResourceId = None
        self.AppId = None
        self.Domain = None
        self.Cname = None
        self.Status = None
        self.ProjectId = None
        self.ServiceType = None
        self.CreateTime = None
        self.UpdateTime = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.Disable = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.Ipv6 = None
        self.Compatibility = None
        self.SpecificConfig = None
        self.Area = None
        self.Readonly = None
        self.OriginPullTimeout = None
        self.AwsPrivateAccess = None
        self.SecurityConfig = None
        self.ImageOptimization = None
        self.UserAgentFilter = None
        self.AccessControl = None
        self.Advance = None
        self.UrlRedirect = None
        self.AccessPort = None
        self.Tag = None
        self.AdvancedAuthentication = None
        self.OriginAuthentication = None
        self.Ipv6Access = None
        self.AdvanceSet = None
        self.OfflineCache = None
        self.OriginCombine = None
        self.PostMaxSize = None
        self.Quic = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.AppId = params.get("AppId")
        self.Domain = params.get("Domain")
        self.Cname = params.get("Cname")
        self.Status = params.get("Status")
        self.ProjectId = params.get("ProjectId")
        self.ServiceType = params.get("ServiceType")
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
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Ipv6") is not None:
            self.Ipv6 = Ipv6()
            self.Ipv6._deserialize(params.get("Ipv6"))
        if params.get("Compatibility") is not None:
            self.Compatibility = Compatibility()
            self.Compatibility._deserialize(params.get("Compatibility"))
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        self.Readonly = params.get("Readonly")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("SecurityConfig") is not None:
            self.SecurityConfig = SecurityConfig()
            self.SecurityConfig._deserialize(params.get("SecurityConfig"))
        if params.get("ImageOptimization") is not None:
            self.ImageOptimization = ImageOptimization()
            self.ImageOptimization._deserialize(params.get("ImageOptimization"))
        if params.get("UserAgentFilter") is not None:
            self.UserAgentFilter = UserAgentFilter()
            self.UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self.AccessControl = AccessControl()
            self.AccessControl._deserialize(params.get("AccessControl"))
        self.Advance = params.get("Advance")
        if params.get("UrlRedirect") is not None:
            self.UrlRedirect = UrlRedirect()
            self.UrlRedirect._deserialize(params.get("UrlRedirect"))
        self.AccessPort = params.get("AccessPort")
        if params.get("Tag") is not None:
            self.Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self.Tag.append(obj)
        if params.get("AdvancedAuthentication") is not None:
            self.AdvancedAuthentication = AdvancedAuthentication()
            self.AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self.OriginAuthentication = OriginAuthentication()
            self.OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self.Ipv6Access = Ipv6Access()
            self.Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("AdvanceSet") is not None:
            self.AdvanceSet = []
            for item in params.get("AdvanceSet"):
                obj = AdvanceConfig()
                obj._deserialize(item)
                self.AdvanceSet.append(obj)
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self.OriginCombine = OriginCombine()
            self.OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("PostMaxSize") is not None:
            self.PostMaxSize = PostSize()
            self.PostMaxSize._deserialize(params.get("PostMaxSize"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DiagnoseData(AbstractModel):
    """诊断报告内容数据

    """

    def __init__(self):
        """
        :param Data: 诊断报告内容
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: list of DiagnoseUnit
        :param Status: 当前诊断项是否正常。
"ok"：正常
"error"：异常
"warning"："警告"
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        """
        self.Data = None
        self.Status = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DiagnoseUnit()
                obj._deserialize(item)
                self.Data.append(obj)
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DiagnoseInfo(AbstractModel):
    """诊断信息

    """

    def __init__(self):
        """
        :param DiagnoseUrl: 待诊断的URL。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseUrl: str
        :param DiagnoseLink: 由系统生成的诊断链接。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseLink: str
        :param CreateTime: 诊断创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param ExpireDate: 诊断链接过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireDate: str
        :param VisitCount: 诊断链接当前访问次数，一个诊断链接最多可访问10次。
注意：此字段可能返回 null，表示取不到有效值。
        :type VisitCount: int
        :param ClientList: 访问诊断链接的客户端简易信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientList: list of DiagnoseList
        :param Area: 域名加速区域
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
        self.DiagnoseUrl = None
        self.DiagnoseLink = None
        self.CreateTime = None
        self.ExpireDate = None
        self.VisitCount = None
        self.ClientList = None
        self.Area = None


    def _deserialize(self, params):
        self.DiagnoseUrl = params.get("DiagnoseUrl")
        self.DiagnoseLink = params.get("DiagnoseLink")
        self.CreateTime = params.get("CreateTime")
        self.ExpireDate = params.get("ExpireDate")
        self.VisitCount = params.get("VisitCount")
        if params.get("ClientList") is not None:
            self.ClientList = []
            for item in params.get("ClientList"):
                obj = DiagnoseList()
                obj._deserialize(item)
                self.ClientList.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DiagnoseList(AbstractModel):
    """客户端访问诊断URL信息列表

    """

    def __init__(self):
        """
        :param DiagnoseTag: 诊断任务标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type DiagnoseTag: str
        :param ReportId: 报告ID，用于获取详细诊断报告。
注意：此字段可能返回 null，表示取不到有效值。
        :type ReportId: str
        :param ClientInfo: 客户端信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientInfo: list of ClientInfo
        :param FinalDiagnose: 最终诊断结果。
-1：已提交
0  ：检测中
1  ：检测正常
2  ： 检测异常
3  ： 诊断页面异常关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type FinalDiagnose: int
        :param CreateTime: 诊断任务创建时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.DiagnoseTag = None
        self.ReportId = None
        self.ClientInfo = None
        self.FinalDiagnose = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.DiagnoseTag = params.get("DiagnoseTag")
        self.ReportId = params.get("ReportId")
        if params.get("ClientInfo") is not None:
            self.ClientInfo = []
            for item in params.get("ClientInfo"):
                obj = ClientInfo()
                obj._deserialize(item)
                self.ClientInfo.append(obj)
        self.FinalDiagnose = params.get("FinalDiagnose")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DiagnoseUnit(AbstractModel):
    """诊断报告单元信息

    """

    def __init__(self):
        """
        :param Key: 内容单元英文名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type Key: str
        :param KeyText: 内容单元中文名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type KeyText: str
        :param Value: 报告内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        :param ValueText: 报告内容。
注意：此字段可能返回 null，表示取不到有效值。
        :type ValueText: str
        """
        self.Key = None
        self.KeyText = None
        self.Value = None
        self.ValueText = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.KeyText = params.get("KeyText")
        self.Value = params.get("Value")
        self.ValueText = params.get("ValueText")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisableCachesRequest(AbstractModel):
    """DisableCaches请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 禁用的 URL 列表（分协议生效，必须包含http://或https://）
每次最多可提交 100 条，每日最多可提交 3000 条
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisableCachesResponse(AbstractModel):
    """DisableCaches返回参数结构体

    """

    def __init__(self):
        """
        :param CacheOptResult: 提交结果
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisableClsLogTopicRequest(AbstractModel):
    """DisableClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DisableClsLogTopicResponse(AbstractModel):
    """DisableClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DistrictIspInfo(AbstractModel):
    """地区运营商明细数据

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param Protocol: 协议类型
        :type Protocol: str
        :param IpProtocol: IP协议类型
        :type IpProtocol: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param Interval: 时间间隔，单位为分钟
        :type Interval: int
        :param Metric: 指标名称
        :type Metric: str
        :param District: 地区ID
        :type District: int
        :param Isp: 运营商ID
        :type Isp: int
        :param DataPoints: 指标数据点
        :type DataPoints: list of int non-negative
        :param DistrictName: 地区名称
        :type DistrictName: str
        :param IspName: 运营商名称
        :type IspName: str
        """
        self.Domain = None
        self.Protocol = None
        self.IpProtocol = None
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.Metric = None
        self.District = None
        self.Isp = None
        self.DataPoints = None
        self.DistrictName = None
        self.IspName = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Protocol = params.get("Protocol")
        self.IpProtocol = params.get("IpProtocol")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.Metric = params.get("Metric")
        self.District = params.get("District")
        self.Isp = params.get("Isp")
        self.DataPoints = params.get("DataPoints")
        self.DistrictName = params.get("DistrictName")
        self.IspName = params.get("IspName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainAreaConfig(AbstractModel):
    """域名地区配置

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param Area: 地区列表，其中元素可为mainland/overseas
        :type Area: list of str
        """
        self.Domain = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainFilter(AbstractModel):
    """域名查询时过滤条件。

    """

    def __init__(self):
        """
        :param Name: 过滤字段名，支持的列表如下：
- origin：主源站。
- domain：域名。
- resourceId：域名id。
- status：域名状态，online，offline或processing。
- serviceType：业务类型，web，download或media。
- projectId：项目ID。
- domainType：主源站类型，cname表示自有源，cos表示cos接入。
- fullUrlCache：全路径缓存，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源协议类型，支持http，follow或https。
- tagKey：标签键。
        :type Name: str
        :param Value: 过滤字段值。
        :type Value: list of str
        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为origin，domain。
模糊查询时，Value长度最大为1，否则Value长度最大为5。
        :type Fuzzy: bool
        """
        self.Name = None
        self.Value = None
        self.Fuzzy = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        self.Fuzzy = params.get("Fuzzy")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DomainLog(AbstractModel):
    """日志包下载链接详情

    """

    def __init__(self):
        """
        :param StartTime: 日志包起始时间
        :type StartTime: str
        :param EndTime: 日志包结束时间
        :type EndTime: str
        :param LogPath: 日志包下载链接
        :type LogPath: str
        :param Area: 日志包对应加速区域
mainland：境内
overseas：境外
        :type Area: str
        :param LogName: 日志包文件名
        :type LogName: str
        """
        self.StartTime = None
        self.EndTime = None
        self.LogPath = None
        self.Area = None
        self.LogName = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.LogPath = params.get("LogPath")
        self.Area = params.get("Area")
        self.LogName = params.get("LogName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DownstreamCapping(AbstractModel):
    """单链接下行限速配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 下行速度配置开关
on：开启
off：关闭
        :type Switch: str
        :param CappingRules: 下行限速规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CappingRules: list of CappingRule
        """
        self.Switch = None
        self.CappingRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CappingRules") is not None:
            self.CappingRules = []
            for item in params.get("CappingRules"):
                obj = CappingRule()
                obj._deserialize(item)
                self.CappingRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DuplicateDomainConfigRequest(AbstractModel):
    """DuplicateDomainConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 新增域名
        :type Domain: str
        :param ReferenceDomain: 被拷贝配置的域名
        :type ReferenceDomain: str
        """
        self.Domain = None
        self.ReferenceDomain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ReferenceDomain = params.get("ReferenceDomain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class DuplicateDomainConfigResponse(AbstractModel):
    """DuplicateDomainConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableCachesRequest(AbstractModel):
    """EnableCaches请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 解封 URL 列表
        :type Urls: list of str
        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableCachesResponse(AbstractModel):
    """EnableCaches返回参数结构体

    """

    def __init__(self):
        """
        :param CacheOptResult: 结果列表
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableClsLogTopicRequest(AbstractModel):
    """EnableClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class EnableClsLogTopicResponse(AbstractModel):
    """EnableClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ErrorPage(AbstractModel):
    """状态码重定向配置，默认为关闭状态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 状态码重定向配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param PageRules: 状态码重定向规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PageRules: list of ErrorPageRule
        """
        self.Switch = None
        self.PageRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PageRules") is not None:
            self.PageRules = []
            for item in params.get("PageRules"):
                obj = ErrorPageRule()
                obj._deserialize(item)
                self.PageRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ErrorPageRule(AbstractModel):
    """状态码重定向规则配置

    """

    def __init__(self):
        """
        :param StatusCode: 状态码
支持 400、403、404、500
        :type StatusCode: int
        :param RedirectCode: 重定向状态码设置
支持 301 或 302
        :type RedirectCode: int
        :param RedirectUrl: 重定向 URL
需要为完整跳转路径，如 https://www.test.com/error.html
        :type RedirectUrl: str
        """
        self.StatusCode = None
        self.RedirectCode = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.RedirectCode = params.get("RedirectCode")
        self.RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class FollowRedirect(AbstractModel):
    """回源 301/302 状态码自动跟随配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 回源跟随开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ForceRedirect(AbstractModel):
    """访问协议强制跳转配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 访问强制跳转配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param RedirectType: 访问强制跳转类型
http：强制 http 跳转
https：强制 https 跳转
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectType: str
        :param RedirectStatusCode: 强制跳转时返回状态码 
支持 301、302
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        :param CarryHeaders: 强制跳转时是否返回增加的头部。
注意：此字段可能返回 null，表示取不到有效值。
        :type CarryHeaders: str
        """
        self.Switch = None
        self.RedirectType = None
        self.RedirectStatusCode = None
        self.CarryHeaders = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.RedirectType = params.get("RedirectType")
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        self.CarryHeaders = params.get("CarryHeaders")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，如：2018-12-12 10:24:00。
        :type StartTime: str
        :param EndTime: 结束时间，如：2018-12-14 10:24:00。
        :type EndTime: str
        :param Url: 指定 URL 查询
        :type Url: str
        :param Status: URL 当前状态
disable：当前仍为禁用状态，访问返回 403
enable：当前为可用状态，已解禁，可正常访问
        :type Status: str
        :param Offset: 分页查询偏移量，默认为 0
        :type Offset: int
        :param Limit: 分页查询限制数目，默认为20。
        :type Limit: int
        """
        self.StartTime = None
        self.EndTime = None
        self.Url = None
        self.Status = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords返回参数结构体

    """

    def __init__(self):
        """
        :param UrlRecordList: 封禁历史记录
注意：此字段可能返回 null，表示取不到有效值。
        :type UrlRecordList: list of UrlRecord
        :param TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.UrlRecordList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("UrlRecordList") is not None:
            self.UrlRecordList = []
            for item in params.get("UrlRecordList"):
                obj = UrlRecord()
                obj._deserialize(item)
                self.UrlRecordList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class GuetzliAdapter(AbstractModel):
    """图片优化-GuetzliAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 开关，"on/off"
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HeaderKey(AbstractModel):
    """组成CacheKey

    """

    def __init__(self):
        """
        :param Switch: 是否组成Cachekey
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Value: 组成CacheKey的header数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Switch = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Hsts(AbstractModel):
    """HSTS 配置。

    """

    def __init__(self):
        """
        :param Switch: 是否开启，on或off。
        :type Switch: str
        :param MaxAge: MaxAge数值。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: int
        :param IncludeSubDomains: 是否包含子域名，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type IncludeSubDomains: str
        """
        self.Switch = None
        self.MaxAge = None
        self.IncludeSubDomains = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxAge = params.get("MaxAge")
        self.IncludeSubDomains = params.get("IncludeSubDomains")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpHeaderPathRule(AbstractModel):
    """Http 头部设置规则，最多可设置 100 条

    """

    def __init__(self):
        """
        :param HeaderMode: http 头部设置方式
set：设置。变更指定头部参数的取值为设置后的值；若设置的头部不存在，则会增加该头部；若存在多个重复的头部参数，则会全部变更，同时合并为一个头部。
del：删除。删除指定的头部参数
add：增加。增加指定的头部参数，默认允许重复添加，即重复添加相同的头部（注：重复添加可能会影响浏览器响应，请优先使用set操作）
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderMode: str
        :param HeaderName: http 头部名称，最多可设置 100 个字符
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        :param HeaderValue: http 头部值，最多可设置 1000 个字符
Mode 为 del 时非必填
Mode 为 add/set 时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderValue: str
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class HttpHeaderRule(AbstractModel):
    """http头部设置规则。

    """

    def __init__(self):
        """
        :param HeaderMode: http头部设置方式，支持add，set或del，分别表示新增，设置或删除头部。
        :type HeaderMode: str
        :param HeaderName: http头部名称。
        :type HeaderName: str
        :param HeaderValue: http头部值。
        :type HeaderValue: str
        """
        self.HeaderMode = None
        self.HeaderName = None
        self.HeaderValue = None


    def _deserialize(self, params):
        self.HeaderMode = params.get("HeaderMode")
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Https(AbstractModel):
    """域名 https 加速配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: https 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Http2: http2 配置开关
on：开启
off：关闭
初次启用 https 加速会默认开启 http2 配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param OcspStapling: OCSP 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param VerifyClient: 客户端证书校验功能
on：开启
off：关闭
默认为关闭状态，开启时需要上传客户端证书信息，该配置项目前在灰度中，尚未全量
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyClient: str
        :param CertInfo: 服务端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`
        :param ClientCertInfo: 客户端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`
        :param Spdy: Spdy 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type Spdy: str
        :param SslStatus: https 证书部署状态
closed：已关闭
deploying：部署中
deployed：部署成功
failed：部署失败
注意：此字段可能返回 null，表示取不到有效值。
        :type SslStatus: str
        :param Hsts: Hsts配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.cdn.v20180606.models.Hsts`
        :param TlsVersion: Tls版本设置，仅支持部分Advance域名，支持设置 TLSv1, TLSV1.1, TLSV1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。
        :type TlsVersion: list of str
        """
        self.Switch = None
        self.Http2 = None
        self.OcspStapling = None
        self.VerifyClient = None
        self.CertInfo = None
        self.ClientCertInfo = None
        self.Spdy = None
        self.SslStatus = None
        self.Hsts = None
        self.TlsVersion = None


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
        if params.get("Hsts") is not None:
            self.Hsts = Hsts()
            self.Hsts._deserialize(params.get("Hsts"))
        self.TlsVersion = params.get("TlsVersion")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ImageOptimization(AbstractModel):
    """ImageOptimization配置

    """

    def __init__(self):
        """
        :param WebpAdapter: WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None


    def _deserialize(self, params):
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpFilter(AbstractModel):
    """IP 黑白名单配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: IP 黑白名单配置开关
on：开启
off：关闭
        :type Switch: str
        :param FilterType: IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param Filters: IP 黑白名单列表
支持 X.X.X.X 形式 IP，或 /8、 /16、/24 形式网段
最多可填充 50 个白名单或 50 个黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of str
        :param FilterRules: IP 黑白名单分路径配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of IpFilterPathRule
        """
        self.Switch = None
        self.FilterType = None
        self.Filters = None
        self.FilterRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = IpFilterPathRule()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpFilterPathRule(AbstractModel):
    """IP黑白名单分路径配置

    """

    def __init__(self):
        """
        :param FilterType: IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param Filters: IP 黑白名单列表
支持 X.X.X.X 形式 IP，或 /8、 /16、/24 形式网段
最多可填充 50 个白名单或 50 个黑名单
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of str
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        """
        self.FilterType = None
        self.Filters = None
        self.RuleType = None
        self.RulePaths = None


    def _deserialize(self, params):
        self.FilterType = params.get("FilterType")
        self.Filters = params.get("Filters")
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpFreqLimit(AbstractModel):
    """单节点单 IP 访问限频配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: IP 限频配置开关
on：开启
off：关闭
        :type Switch: str
        :param Qps: 设置每秒请求数限制
超出限制的请求会直接返回 514
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        """
        self.Switch = None
        self.Qps = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Qps = params.get("Qps")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class IpStatus(AbstractModel):
    """节点 IP 信息

    """

    def __init__(self):
        """
        :param Ip: 节点 IP
        :type Ip: str
        :param District: 节点所属区域
        :type District: str
        :param Isp: 节点所属运营商
        :type Isp: str
        :param City: 节点所在城市
        :type City: str
        :param Status: 节点状态
online：上线状态，正常调度服务中
offline：下线状态
        :type Status: str
        """
        self.Ip = None
        self.District = None
        self.Isp = None
        self.City = None
        self.Status = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        self.District = params.get("District")
        self.Isp = params.get("Isp")
        self.City = params.get("City")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Ipv6(AbstractModel):
    """Ipv6启用配置，不可更改

    """

    def __init__(self):
        """
        :param Switch: 域名是否开启ipv6功能，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Ipv6Access(AbstractModel):
    """Ipv6访问配置

    """

    def __init__(self):
        """
        :param Switch: 域名是否开启ipv6访问功能，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class KeyRule(AbstractModel):
    """缓存键分路径配置

    """

    def __init__(self):
        """
        :param RulePaths: CacheType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        :param RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数过滤）
off：关闭全路径缓存（即开启参数过滤）
注意：此字段可能返回 null，表示取不到有效值。
        :type FullUrlCache: str
        :param IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCase: str
        :param QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。
        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.RuleQueryString`
        :param RuleTag: 路径缓存键标签，传 user
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleTag: str
        """
        self.RulePaths = None
        self.RuleType = None
        self.FullUrlCache = None
        self.IgnoreCase = None
        self.QueryString = None
        self.RuleTag = None


    def _deserialize(self, params):
        self.RulePaths = params.get("RulePaths")
        self.RuleType = params.get("RuleType")
        self.FullUrlCache = params.get("FullUrlCache")
        self.IgnoreCase = params.get("IgnoreCase")
        if params.get("QueryString") is not None:
            self.QueryString = RuleQueryString()
            self.QueryString._deserialize(params.get("QueryString"))
        self.RuleTag = params.get("RuleTag")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListClsLogTopicsRequest(AbstractModel):
    """ListClsLogTopics请求参数结构体

    """

    def __init__(self):
        """
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        """
        self.Channel = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListClsLogTopicsResponse(AbstractModel):
    """ListClsLogTopics返回参数结构体

    """

    def __init__(self):
        """
        :param Logset: 日志集信息
        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`
        :param Topics: 日志主题信息列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Topics: list of TopicInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Logset = None
        self.Topics = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logset") is not None:
            self.Logset = LogSetInfo()
            self.Logset._deserialize(params.get("Logset"))
        if params.get("Topics") is not None:
            self.Topics = []
            for item in params.get("Topics"):
                obj = TopicInfo()
                obj._deserialize(item)
                self.Topics.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListClsTopicDomainsRequest(AbstractModel):
    """ListClsTopicDomains请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListClsTopicDomainsResponse(AbstractModel):
    """ListClsTopicDomains返回参数结构体

    """

    def __init__(self):
        """
        :param AppId: 开发者ID
        :type AppId: int
        :param Channel: 渠道
        :type Channel: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param DomainAreaConfigs: 域名区域配置，其中可能含有已删除的域名，如果要再传回ManageClsTopicDomains接口，需要结合ListCdnDomains接口排除掉已删除的域名
        :type DomainAreaConfigs: list of DomainAreaConfig
        :param TopicName: 日志主题名称
        :type TopicName: str
        :param UpdateTime: 日志主题最近更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AppId = None
        self.Channel = None
        self.LogsetId = None
        self.TopicId = None
        self.DomainAreaConfigs = None
        self.TopicName = None
        self.UpdateTime = None
        self.RequestId = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Channel = params.get("Channel")
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        self.TopicName = params.get("TopicName")
        self.UpdateTime = params.get("UpdateTime")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListDiagnoseReportRequest(AbstractModel):
    """ListDiagnoseReport请求参数结构体

    """

    def __init__(self):
        """
        :param KeyWords: 用于搜索诊断URL的关键字，不填时返回用户所有的诊断任务。
        :type KeyWords: str
        :param DiagnoseLink: 用于搜索诊断系统返回的诊断链接，形如：http://cdn.cloud.tencent.com/self_diagnose/xxxxx
        :type DiagnoseLink: str
        """
        self.KeyWords = None
        self.DiagnoseLink = None


    def _deserialize(self, params):
        self.KeyWords = params.get("KeyWords")
        self.DiagnoseLink = params.get("DiagnoseLink")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListDiagnoseReportResponse(AbstractModel):
    """ListDiagnoseReport返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 诊断信息。
        :type Data: list of DiagnoseInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = DiagnoseInfo()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListScdnDomainsRequest(AbstractModel):
    """ListScdnDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页起始地址
        :type Offset: int
        :param Limit: 列表分页记录条数，最大1000
        :type Limit: int
        :param Domain: 域名信息
        :type Domain: str
        """
        self.Offset = None
        self.Limit = None
        self.Domain = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListScdnDomainsResponse(AbstractModel):
    """ListScdnDomains返回参数结构体

    """

    def __init__(self):
        """
        :param DomainList: 域名列表信息
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainList: list of ScdnDomain
        :param TotalCount: 域名的总条数。
注意：此字段可能返回 null，表示取不到有效值。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainList") is not None:
            self.DomainList = []
            for item in params.get("DomainList"):
                obj = ScdnDomain()
                obj._deserialize(item)
                self.DomainList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListScdnLogTasksRequest(AbstractModel):
    """ListScdnLogTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Source: 产品来源 cdn/ecdn
        :type Source: str
        :param Area: 地域：mainland 或 overseas 为空表示查询所有地域
        :type Area: str
        """
        self.Source = None
        self.Area = None


    def _deserialize(self, params):
        self.Source = params.get("Source")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListScdnLogTasksResponse(AbstractModel):
    """ListScdnLogTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskList: 日志下载任务详情
        :type TaskList: list of ScdnLogTaskDetail
        :param TotalCount: 查询到的下载任务的总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskList = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("TaskList") is not None:
            self.TaskList = []
            for item in params.get("TaskList"):
                obj = ScdnLogTaskDetail()
                obj._deserialize(item)
                self.TaskList.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListTopDataRequest(AbstractModel):
    """ListTopData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为起始日期
返回大于等于起始日期当天 00:00:00 点产生的数据
仅支持 90 天内数据查询
        :type StartTime: str
        :param EndTime: 查询结束日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为结束日期
返回小于等于结束日期当天 23:59:59 产生的数据
EndTime 需要大于等于 StartTime
        :type EndTime: str
        :param Metric: 排序对象，支持以下几种形式：
url：访问 URL 排序（无参数的URL），支持的 Filter 为 flux、request
district：省份、国家/地区排序，支持的 Filter 为 flux、request
isp：运营商排序，支持的 Filter 为 flux、request
host：域名访问数据排序，支持的 Filter 为：flux、request、bandwidth、fluxHitRate、2XX、3XX、4XX、5XX、statusCode
originHost：域名回源数据排序，支持的 Filter 为 flux、request、bandwidth、origin_2XX、origin_3XX、origin_4XX、origin_5XX、OriginStatusCode
        :type Metric: str
        :param Filter: 排序使用的指标名称：
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
        :param Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细
        :type Domains: list of str
        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Project: int
        :param Detail: 多域名查询时，默认（false)返回所有域名汇总排序结果
Metric 为 url、path、district、isp，Filter 为 flux、request 时，可设置为 true，返回每一个 Domain 的排序数据
        :type Detail: bool
        :param Code: Filter 为 statusCode、OriginStatusCode 时，填充指定状态码查询排序结果
        :type Code: str
        :param Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据，支持的 Metric 为 url、district、host、originHost，当 Metric 为 originHost 时仅支持 flux、request、bandwidth Filter
        :type Area: str
        :param AreaType: 查询中国境外CDN数据，且仅当 Metric 为 district 或 host 时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas，且 Metric 是 district 或 host 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据，当 Metric 为 host 时仅支持 flux、request、bandwidth Filter
        :type AreaType: str
        """
        self.StartTime = None
        self.EndTime = None
        self.Metric = None
        self.Filter = None
        self.Domains = None
        self.Project = None
        self.Detail = None
        self.Code = None
        self.Area = None
        self.AreaType = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Metric = params.get("Metric")
        self.Filter = params.get("Filter")
        self.Domains = params.get("Domains")
        self.Project = params.get("Project")
        self.Detail = params.get("Detail")
        self.Code = params.get("Code")
        self.Area = params.get("Area")
        self.AreaType = params.get("AreaType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ListTopDataResponse(AbstractModel):
    """ListTopData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 各个资源的Top 访问数据详情。
        :type Data: list of TopData
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Data = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self.Data = []
            for item in params.get("Data"):
                obj = TopData()
                obj._deserialize(item)
                self.Data.append(obj)
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class LogSetInfo(AbstractModel):
    """日志集信息

    """

    def __init__(self):
        """
        :param AppId: 开发者ID
        :type AppId: int
        :param Channel: 渠道
注意：此字段可能返回 null，表示取不到有效值。
        :type Channel: str
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param LogsetName: 日志集名字
        :type LogsetName: str
        :param IsDefault: 是否默认日志集
        :type IsDefault: int
        :param LogsetSavePeriod: 日志保存时间，单位为天
        :type LogsetSavePeriod: int
        :param CreateTime: 创建日期
        :type CreateTime: str
        :param Region: 区域
        :type Region: str
        """
        self.AppId = None
        self.Channel = None
        self.LogsetId = None
        self.LogsetName = None
        self.IsDefault = None
        self.LogsetSavePeriod = None
        self.CreateTime = None
        self.Region = None


    def _deserialize(self, params):
        self.AppId = params.get("AppId")
        self.Channel = params.get("Channel")
        self.LogsetId = params.get("LogsetId")
        self.LogsetName = params.get("LogsetName")
        self.IsDefault = params.get("IsDefault")
        self.LogsetSavePeriod = params.get("LogsetSavePeriod")
        self.CreateTime = params.get("CreateTime")
        self.Region = params.get("Region")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MainlandConfig(AbstractModel):
    """域名国内地区特殊配置。分地区特殊配置。UpdateDomainConfig接口只支持修改部分分地区配置，为了兼容旧版本配置，本类型会列出旧版本所有可能存在差异的配置列表，支持修改的配置列表如下：
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        """
        :param Authentication: 时间戳防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: 带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param CacheKey: 缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: 下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: 错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: 浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: 跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: 防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: 回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: 遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ServiceType: 域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param StatusCodeCache: 状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: 视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ManageClsTopicDomainsRequest(AbstractModel):
    """ManageClsTopicDomains请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID
        :type LogsetId: str
        :param TopicId: 日志主题ID
        :type TopicId: str
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        :param DomainAreaConfigs: 域名区域配置，注意：如果此字段为空，则表示解绑对应主题下的所有域名
        :type DomainAreaConfigs: list of DomainAreaConfig
        """
        self.LogsetId = None
        self.TopicId = None
        self.Channel = None
        self.DomainAreaConfigs = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicId = params.get("TopicId")
        self.Channel = params.get("Channel")
        if params.get("DomainAreaConfigs") is not None:
            self.DomainAreaConfigs = []
            for item in params.get("DomainAreaConfigs"):
                obj = DomainAreaConfig()
                obj._deserialize(item)
                self.DomainAreaConfigs.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ManageClsTopicDomainsResponse(AbstractModel):
    """ManageClsTopicDomains返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MapInfo(AbstractModel):
    """名称与ID映射关系

    """

    def __init__(self):
        """
        :param Id: 对象 Id
        :type Id: int
        :param Name: 对象名称
        :type Name: str
        """
        self.Id = None
        self.Name = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MaxAge(AbstractModel):
    """浏览器缓存规则配置，用于设置 MaxAge 默认值，默认为关闭状态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 浏览器缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param MaxAgeRules: MaxAge 规则
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAgeRules: list of MaxAgeRule
        """
        self.Switch = None
        self.MaxAgeRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("MaxAgeRules") is not None:
            self.MaxAgeRules = []
            for item in params.get("MaxAgeRules"):
                obj = MaxAgeRule()
                obj._deserialize(item)
                self.MaxAgeRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class MaxAgeRule(AbstractModel):
    """MagAge 规则配置

    """

    def __init__(self):
        """
        :param MaxAgeType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效
        :type MaxAgeType: str
        :param MaxAgeContents: MaxAgeType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：all规则不可删除，默认遵循源站，可修改。
        :type MaxAgeContents: list of str
        :param MaxAgeTime: MaxAge 时间设置，单位秒
注意：时间为0，即不缓存。
        :type MaxAgeTime: int
        :param FollowOrigin: 是否遵循源站，on或off，开启时忽略时间设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self.MaxAgeType = None
        self.MaxAgeContents = None
        self.MaxAgeTime = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        self.MaxAgeType = params.get("MaxAgeType")
        self.MaxAgeContents = params.get("MaxAgeContents")
        self.MaxAgeTime = params.get("MaxAgeTime")
        self.FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OfflineCache(AbstractModel):
    """离线缓存是否开启

    """

    def __init__(self):
        """
        :param Switch: on | off, 离线缓存是否开启
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Origin(AbstractModel):
    """源站配置复杂类型，支持以下配置：
    + 源站指定为单个域名
    + 源站指定为多个 IP，可配置端口（1~65535），可配置权重（1~100），格式为 IP:端口:权重
    + 回源域名配置
    + 对象存储（COS）作为源站
    + 热备源站指定为单个域名
    + 热备源站指定为多个 IP，可配置端口（1~65535），暂不支持权重配置
    + 热备源站回源域名配置

    """

    def __init__(self):
        """
        :param Origins: 主源站列表
修改源站时，需要同时填充对应的 OriginType
注意：此字段可能返回 null，表示取不到有效值。
        :type Origins: list of str
        :param OriginType: 主源站类型
入参支持以下几种类型：
domain：域名类型
cos：对象存储源站
ip：IP 列表作为源站
ipv6：源站列表为一个单独的 IPv6 地址
ip_ipv6：源站列表为多个 IPv4 地址和一个 IPv6 地址
出参增加以下几种类型：
image：数据万象源站
ftp：历史 FTP 托管源源站，现已不维护
修改 Origins 时需要同时填充对应的 OriginType
IPv6 功能目前尚未全量，需要先申请试用
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param ServerName: 回主源站时 Host 头部，不填充则默认为加速域名
若接入的是泛域名，则回源 Host 默认为访问时的子域名
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param CosPrivateAccess: OriginType 为对象存储（COS）时，可以指定是否允许访问私有 bucket
注意：需要先授权 CDN 访问该私有 Bucket 的权限后，才可开启此配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CosPrivateAccess: str
        :param OriginPullProtocol: 回源协议配置
http：强制 http 回源
follow：协议跟随回源
https：强制 https 回源，https 回源时仅支持源站 443 端口
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param BackupOrigins: 备源站列表
修改备源站时，需要同时填充对应的 BackupOriginType
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOrigins: list of str
        :param BackupOriginType: 备源站类型，支持以下类型：
domain：域名类型
ip：IP 列表作为源站
修改 BackupOrigins 时需要同时填充对应的 BackupOriginType
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOriginType: str
        :param BackupServerName: 回备源站时 Host 头部，不填充则默认为主源站的 ServerName
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupServerName: str
        :param BasePath: 回源路径
注意：此字段可能返回 null，表示取不到有效值。
        :type BasePath: str
        :param PathRules: 回源路径重写规则配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PathRules: list of PathRule
        :param PathBasedOrigin: 分路径回源配置
注意：此字段可能返回 null，表示取不到有效值。
        :type PathBasedOrigin: list of PathBasedOriginRule
        """
        self.Origins = None
        self.OriginType = None
        self.ServerName = None
        self.CosPrivateAccess = None
        self.OriginPullProtocol = None
        self.BackupOrigins = None
        self.BackupOriginType = None
        self.BackupServerName = None
        self.BasePath = None
        self.PathRules = None
        self.PathBasedOrigin = None


    def _deserialize(self, params):
        self.Origins = params.get("Origins")
        self.OriginType = params.get("OriginType")
        self.ServerName = params.get("ServerName")
        self.CosPrivateAccess = params.get("CosPrivateAccess")
        self.OriginPullProtocol = params.get("OriginPullProtocol")
        self.BackupOrigins = params.get("BackupOrigins")
        self.BackupOriginType = params.get("BackupOriginType")
        self.BackupServerName = params.get("BackupServerName")
        self.BasePath = params.get("BasePath")
        if params.get("PathRules") is not None:
            self.PathRules = []
            for item in params.get("PathRules"):
                obj = PathRule()
                obj._deserialize(item)
                self.PathRules.append(obj)
        if params.get("PathBasedOrigin") is not None:
            self.PathBasedOrigin = []
            for item in params.get("PathBasedOrigin"):
                obj = PathBasedOriginRule()
                obj._deserialize(item)
                self.PathBasedOrigin.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OriginAuthentication(AbstractModel):
    """回源鉴权高级配置

    """

    def __init__(self):
        """
        :param Switch: 鉴权开关，on或off
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param TypeA: 鉴权类型A配置
注意：此字段可能返回 null，表示取不到有效值。
        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.OriginAuthenticationTypeA`
        """
        self.Switch = None
        self.TypeA = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("TypeA") is not None:
            self.TypeA = OriginAuthenticationTypeA()
            self.TypeA._deserialize(params.get("TypeA"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OriginAuthenticationTypeA(AbstractModel):
    """回源鉴权高级配置TypeA

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。
        :type SecretKey: str
        """
        self.SecretKey = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OriginCombine(AbstractModel):
    """合并回源配置项

    """

    def __init__(self):
        """
        :param Switch: on|off 是否开启合并回源
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OriginIp(AbstractModel):
    """CDN回源节点IP信息

    """

    def __init__(self):
        """
        :param Ip: 回源IP段/回源IP，默认返回IP段信息。
        :type Ip: str
        """
        self.Ip = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OriginPullOptimization(AbstractModel):
    """跨国回源优化配置，默认为关闭状态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 跨国回源优化配置开关
on：开启
off：关闭
        :type Switch: str
        :param OptimizationType: 跨国类型
OVToCN：境外回源境内
CNToOV：境内回源境外
注意：此字段可能返回 null，表示取不到有效值。
        :type OptimizationType: str
        """
        self.Switch = None
        self.OptimizationType = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.OptimizationType = params.get("OptimizationType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OriginPullTimeout(AbstractModel):
    """回源超时配置

    """

    def __init__(self):
        """
        :param ConnectTimeout: 回源建连超时时间，单位为秒，要求5~60之间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnectTimeout: int
        :param ReceiveTimeout: 回源接收超时时间，单位为秒，要求10 ~ 60之间
注意：此字段可能返回 null，表示取不到有效值。
        :type ReceiveTimeout: int
        """
        self.ConnectTimeout = None
        self.ReceiveTimeout = None


    def _deserialize(self, params):
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.ReceiveTimeout = params.get("ReceiveTimeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class OverseaConfig(AbstractModel):
    """域名海外地区特殊配置。UpdateDomainConfig接口只支持修改部分分地区配置，为了兼容旧版本配置，本类型会列出旧版本所有可能存在差异的配置列表，支持修改的配置列表如下：
    + Authentication
    + BandwidthAlert
    + ErrorPage
    + IpFilter
    + Origin
    + Referer

    """

    def __init__(self):
        """
        :param Authentication: 时间戳防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param BandwidthAlert: 带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param CacheKey: 缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param DownstreamCapping: 下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param ErrorPage: 错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param FollowRedirect: 301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param MaxAge: 浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param OriginPullOptimization: 跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param RangeOriginPull: Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param Referer: 防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param RequestHeader: 回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param ResponseHeaderCache: 遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param Seo: seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ServiceType: 域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServiceType: str
        :param StatusCodeCache: 状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param VideoSeek: 视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        """
        self.Authentication = None
        self.BandwidthAlert = None
        self.Cache = None
        self.CacheKey = None
        self.Compression = None
        self.DownstreamCapping = None
        self.ErrorPage = None
        self.FollowRedirect = None
        self.ForceRedirect = None
        self.Https = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.MaxAge = None
        self.Origin = None
        self.OriginPullOptimization = None
        self.RangeOriginPull = None
        self.Referer = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.ResponseHeaderCache = None
        self.Seo = None
        self.ServiceType = None
        self.StatusCodeCache = None
        self.VideoSeek = None


    def _deserialize(self, params):
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        self.ServiceType = params.get("ServiceType")
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PathBasedOriginRule(AbstractModel):
    """分路径回源规则

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效
        :type RuleType: str
        :param RulePaths: RuleType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
        :type RulePaths: list of str
        :param Origin: 源站列表，支持域名或ipv4地址
        :type Origin: list of str
        """
        self.RuleType = None
        self.RulePaths = None
        self.Origin = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.Origin = params.get("Origin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PathRule(AbstractModel):
    """分路径回源配置规则。

    """

    def __init__(self):
        """
        :param Regex: 是否开启通配符“*”匹配：
false：关闭
true：开启
注意：此字段可能返回 null，表示取不到有效值。
        :type Regex: bool
        :param Path: 匹配的URL路径，仅支持Url路径，不支持参数。默认完全匹配，开启通配符“*”匹配后，最多支持5个通配符，最大长度为1024个字符。
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        :param Origin: 路径匹配时的回源源站。暂不支持开了私有读写的COS源。不填写时沿用默认源站。
注意：此字段可能返回 null，表示取不到有效值。
        :type Origin: str
        :param ServerName: 路径匹配时回源的Host头部。不填写时沿用默认ServerName。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param OriginArea: 源站所属区域，支持CN，OV：
CN：中国境内
OV：中国境外
默认为CN。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginArea: str
        :param ForwardUri: 路径匹配时回源的URI路径，必须以“/”开头，不包含参数部分。最大长度为1024个字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号“*”，最多支持10个捕获值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardUri: str
        :param RequestHeaders: 路径匹配时回源的头部设置。
注意：此字段可能返回 null，表示取不到有效值。
        :type RequestHeaders: list of HttpHeaderRule
        """
        self.Regex = None
        self.Path = None
        self.Origin = None
        self.ServerName = None
        self.OriginArea = None
        self.ForwardUri = None
        self.RequestHeaders = None


    def _deserialize(self, params):
        self.Regex = params.get("Regex")
        self.Path = params.get("Path")
        self.Origin = params.get("Origin")
        self.ServerName = params.get("ServerName")
        self.OriginArea = params.get("OriginArea")
        self.ForwardUri = params.get("ForwardUri")
        if params.get("RequestHeaders") is not None:
            self.RequestHeaders = []
            for item in params.get("RequestHeaders"):
                obj = HttpHeaderRule()
                obj._deserialize(item)
                self.RequestHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PostSize(AbstractModel):
    """POST请求上传文件流式传输最大限制

    """

    def __init__(self):
        """
        :param Switch: 是调整POST请求限制，平台默认为32MB。
关闭：off，
开启：on。
        :type Switch: str
        :param MaxSize: 最大限制，取值在1MB和200MB之间。
        :type MaxSize: int
        """
        self.Switch = None
        self.MaxSize = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.MaxSize = params.get("MaxSize")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache请求参数结构体

    """

    def __init__(self):
        """
        :param Paths: 目录列表，需要包含协议头部 http:// 或 https://
        :type Paths: list of str
        :param FlushType: 刷新类型
flush：刷新产生更新的资源
delete：刷新全部资源
        :type FlushType: str
        :param UrlEncode: 是否对中文字符进行编码后刷新
        :type UrlEncode: bool
        """
        self.Paths = None
        self.FlushType = None
        self.UrlEncode = None


    def _deserialize(self, params):
        self.Paths = params.get("Paths")
        self.FlushType = params.get("FlushType")
        self.UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务 ID，同一批次提交的目录共用一个任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgeTask(AbstractModel):
    """刷新任务详情

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务 ID
        :type TaskId: str
        :param Url: 刷新 URL
        :type Url: str
        :param Status: 刷新任务状态
fail：刷新失败
done：刷新成功
process：刷新中
        :type Status: str
        :param PurgeType: 刷新类型
url：URL 刷新
path：目录刷新
        :type PurgeType: str
        :param FlushType: 刷新方式
flush：刷新更新资源（仅目录刷新时有此类型）
delete：刷新全部资源
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: URL 列表，需要包含协议头部 http:// 或 https://
        :type Urls: list of str
        :param Area: 刷新区域
无此参数时，默认刷新加速域名所在加速区域
填充 mainland 时，仅刷新中国境内加速节点上缓存内容
填充 overseas 时，仅刷新中国境外加速节点上缓存内容
指定刷新区域时，需要与域名加速区域匹配
        :type Area: str
        :param UrlEncode: 是否对中文字符进行编码后刷新
        :type UrlEncode: bool
        """
        self.Urls = None
        self.Area = None
        self.UrlEncode = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.Area = params.get("Area")
        self.UrlEncode = params.get("UrlEncode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务 ID，同一批次提交的 URL 共用一个任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushTask(AbstractModel):
    """预热任务详情

    """

    def __init__(self):
        """
        :param TaskId: 预热任务 ID
        :type TaskId: str
        :param Url: 预热 URL
        :type Url: str
        :param Status: 预热任务状态
fail：预热失败
done：预热成功
process：预热中
        :type Status: str
        :param Percent: 预热进度百分比
        :type Percent: int
        :param CreateTime: 预热任务提交时间
        :type CreateTime: str
        :param Area: 预热区域
mainland：境内
overseas：境外
global：全球
        :type Area: str
        :param UpdateTime: 预热任务更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.TaskId = None
        self.Url = None
        self.Status = None
        self.Percent = None
        self.CreateTime = None
        self.Area = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.Url = params.get("Url")
        self.Status = params.get("Status")
        self.Percent = params.get("Percent")
        self.CreateTime = params.get("CreateTime")
        self.Area = params.get("Area")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: URL 列表，需要包含协议头部 http:// 或 https://
        :type Urls: list of str
        :param UserAgent: 指定预热请求回源时 HTTP 请求的 User-Agent 头部
默认为 TencentCdn
        :type UserAgent: str
        :param Area: 预热生效区域
mainland：预热至境内节点
overseas：预热至境外节点
global：预热全球节点
不填充情况下，默认为 mainland， URL 中域名必须在对应区域启用了加速服务才能提交对应区域的预热任务
        :type Area: str
        :param Layer: 填写"middle"或不填充时预热至中间层节点
        :type Layer: str
        :param ParseM3U8: 是否递归解析m3u8文件中的ts分片预热
注意事项：
1. 该功能要求m3u8索引文件能直接请求获取
2. 当前只支持递归解析一级索引和子索引中的ts分片，递归深度不超过3层
3. 解析获取的ts分片会正常累加每日预热用量，当用量超出配额时，会静默处理，不再执行预热
        :type ParseM3U8: bool
        """
        self.Urls = None
        self.UserAgent = None
        self.Area = None
        self.Layer = None
        self.ParseM3U8 = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.UserAgent = params.get("UserAgent")
        self.Area = params.get("Area")
        self.Layer = params.get("Layer")
        self.ParseM3U8 = params.get("ParseM3U8")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 此批提交的任务 ID
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class QueryStringKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: on | off CacheKey是否由QueryString组成
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Reorder: 是否重新排序
注意：此字段可能返回 null，表示取不到有效值。
        :type Reorder: str
        :param Action: includeAll | excludeAll | includeCustom | excludeAll 使用/排除部分url参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param Value: 使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Switch = None
        self.Reorder = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Reorder = params.get("Reorder")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Quic(AbstractModel):
    """Quic配置项

    """

    def __init__(self):
        """
        :param Switch: 是否启动Quic配置
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Quota(AbstractModel):
    """刷新/预热 可用量及配额

    """

    def __init__(self):
        """
        :param Batch: 单次批量提交配额上限。
        :type Batch: int
        :param Total: 每日提交配额上限。
        :type Total: int
        :param Available: 每日剩余的可提交配额。
        :type Available: int
        :param Area: 配额的区域。
        :type Area: str
        """
        self.Batch = None
        self.Total = None
        self.Available = None
        self.Area = None


    def _deserialize(self, params):
        self.Batch = params.get("Batch")
        self.Total = params.get("Total")
        self.Available = params.get("Available")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RangeOriginPull(AbstractModel):
    """分片回源配置，默认为开启状态

    """

    def __init__(self):
        """
        :param Switch: 分片回源配置开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Referer(AbstractModel):
    """Referer 黑白名单配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: referer 黑白名单配置开关
on：开启
off：关闭
        :type Switch: str
        :param RefererRules: referer 黑白名单配置规则
注意：此字段可能返回 null，表示取不到有效值。
        :type RefererRules: list of RefererRule
        """
        self.Switch = None
        self.RefererRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("RefererRules") is not None:
            self.RefererRules = []
            for item in params.get("RefererRules"):
                obj = RefererRule()
                obj._deserialize(item)
                self.RefererRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RefererRule(AbstractModel):
    """Referer 黑白名单配置规则，针对特定资源生效

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
        :type RuleType: str
        :param RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
        :type RulePaths: list of str
        :param RefererType: referer 配置类型
whitelist：白名单
blacklist：黑名单
        :type RefererType: str
        :param Referers: referer 内容列表列表
        :type Referers: list of str
        :param AllowEmpty: 是否允许空 referer
true：允许空 referer
false：不允许空 referer
        :type AllowEmpty: bool
        """
        self.RuleType = None
        self.RulePaths = None
        self.RefererType = None
        self.Referers = None
        self.AllowEmpty = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.RefererType = params.get("RefererType")
        self.Referers = params.get("Referers")
        self.AllowEmpty = params.get("AllowEmpty")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RegionMapRelation(AbstractModel):
    """区域映射id和子区域id的关联信息。

    """

    def __init__(self):
        """
        :param RegionId: 区域ID。
        :type RegionId: int
        :param SubRegionIdList: 子区域ID列表
        :type SubRegionIdList: list of int
        """
        self.RegionId = None
        self.SubRegionIdList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.SubRegionIdList = params.get("SubRegionIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ReportData(AbstractModel):
    """CDN报表数据

    """

    def __init__(self):
        """
        :param ResourceId: 项目ID/域名ID。
        :type ResourceId: str
        :param Resource: 项目名称/域名。
        :type Resource: str
        :param Value: 流量总和/带宽最大值，单位分别为bytes，bps。
        :type Value: int
        :param Percentage: 单个资源占总体百分比。
        :type Percentage: float
        :param BillingValue: 计费流量总和/计费带宽最大值，单位分别为bytes，bps。
        :type BillingValue: int
        :param BillingPercentage: 计费数值占总体百分比。
        :type BillingPercentage: float
        """
        self.ResourceId = None
        self.Resource = None
        self.Value = None
        self.Percentage = None
        self.BillingValue = None
        self.BillingPercentage = None


    def _deserialize(self, params):
        self.ResourceId = params.get("ResourceId")
        self.Resource = params.get("Resource")
        self.Value = params.get("Value")
        self.Percentage = params.get("Percentage")
        self.BillingValue = params.get("BillingValue")
        self.BillingPercentage = params.get("BillingPercentage")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RequestHeader(AbstractModel):
    """自定义请求头配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 自定义请求头配置开关
on：开启
off：关闭
        :type Switch: str
        :param HeaderRules: 自定义请求头配置规则
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceBillingData(AbstractModel):
    """计费数据明细

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
某一个具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
某一个项目 ID：指定项目查询时，显示为项目 ID
all：账号维度数据明细
        :type Resource: str
        :param BillingData: 计费数据详情
        :type BillingData: list of CdnData
        """
        self.Resource = None
        self.BillingData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("BillingData") is not None:
            self.BillingData = []
            for item in params.get("BillingData"):
                obj = CdnData()
                obj._deserialize(item)
                self.BillingData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        :param CdnData: 资源对应的数据明细
        :type CdnData: list of CdnData
        """
        self.Resource = None
        self.CdnData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("CdnData") is not None:
            self.CdnData = []
            for item in params.get("CdnData"):
                obj = CdnData()
                obj._deserialize(item)
                self.CdnData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResourceOriginData(AbstractModel):
    """查询对象及其对应的回源明细数据

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :type Resource: str
        :param OriginData: 回源数据详情
        :type OriginData: list of CdnData
        """
        self.Resource = None
        self.OriginData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("OriginData") is not None:
            self.OriginData = []
            for item in params.get("OriginData"):
                obj = CdnData()
                obj._deserialize(item)
                self.OriginData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResponseHeader(AbstractModel):
    """自定义响应头配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 自定义响应头开关
on：开启
off：关闭
        :type Switch: str
        :param HeaderRules: 自定义响应头规则
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ResponseHeaderCache(AbstractModel):
    """源站头部缓存配置，默认为开启状态，缓存所有头部信息

    """

    def __init__(self):
        """
        :param Switch: 源站头部缓存开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Revalidate(AbstractModel):
    """是否回源站校验

    """

    def __init__(self):
        """
        :param Switch: on | off 是否总是回源校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Path: 只在特定请求路径回源站校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Path: str
        """
        self.Switch = None
        self.Path = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Path = params.get("Path")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleCache(AbstractModel):
    """缓存配置分路径版本。
    默认情况下所有文件缓存过期时间为 30 天
    默认情况下静态加速类型的域名 .php;.jsp;.asp;.aspx 不缓存

    """

    def __init__(self):
        """
        :param RulePaths: CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param CacheConfig: 缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.RuleCacheConfig`
        """
        self.RulePaths = None
        self.RuleType = None
        self.CacheConfig = None


    def _deserialize(self, params):
        self.RulePaths = params.get("RulePaths")
        self.RuleType = params.get("RuleType")
        if params.get("CacheConfig") is not None:
            self.CacheConfig = RuleCacheConfig()
            self.CacheConfig._deserialize(params.get("CacheConfig"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleCacheConfig(AbstractModel):
    """路径缓存缓存配置（三种缓存模式中选取一种）

    """

    def __init__(self):
        """
        :param Cache: 缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigCache`
        :param NoCache: 不缓存配置
注意：此字段可能返回 null，表示取不到有效值。
        :type NoCache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigNoCache`
        :param FollowOrigin: 遵循源站配置
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: :class:`tencentcloud.cdn.v20180606.models.CacheConfigFollowOrigin`
        """
        self.Cache = None
        self.NoCache = None
        self.FollowOrigin = None


    def _deserialize(self, params):
        if params.get("Cache") is not None:
            self.Cache = CacheConfigCache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("NoCache") is not None:
            self.NoCache = CacheConfigNoCache()
            self.NoCache._deserialize(params.get("NoCache"))
        if params.get("FollowOrigin") is not None:
            self.FollowOrigin = CacheConfigFollowOrigin()
            self.FollowOrigin._deserialize(params.get("FollowOrigin"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class RuleQueryString(AbstractModel):
    """路径保留参数配置

    """

    def __init__(self):
        """
        :param Switch: on | off CacheKey是否由QueryString组成
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param Action: includeCustom 包含部分url参数
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param Value: 使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。
        :type Value: str
        """
        self.Switch = None
        self.Action = None
        self.Value = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Action = params.get("Action")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnAclConfig(AbstractModel):
    """SCDN访问控制

    """

    def __init__(self):
        """
        :param Switch: 是否开启，on | off
        :type Switch: str
        :param ScriptData: Acl规则组，switch为on时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type ScriptData: list of ScdnAclGroup
        :param ErrorPage: 错误页面配置
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        """
        self.Switch = None
        self.ScriptData = None
        self.ErrorPage = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("ScriptData") is not None:
            self.ScriptData = []
            for item in params.get("ScriptData"):
                obj = ScdnAclGroup()
                obj._deserialize(item)
                self.ScriptData.append(obj)
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ScdnErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnAclGroup(AbstractModel):
    """SCDN精准访问控制配置

    """

    def __init__(self):
        """
        :param RuleName: 规则名称
        :type RuleName: str
        :param Configure: 具体配置
        :type Configure: list of ScdnAclRule
        :param Result: 规则行为，一般为refuse
        :type Result: str
        :param Status: 规则是否生效中active|inactive
        :type Status: str
        """
        self.RuleName = None
        self.Configure = None
        self.Result = None
        self.Status = None


    def _deserialize(self, params):
        self.RuleName = params.get("RuleName")
        if params.get("Configure") is not None:
            self.Configure = []
            for item in params.get("Configure"):
                obj = ScdnAclRule()
                obj._deserialize(item)
                self.Configure.append(obj)
        self.Result = params.get("Result")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnAclRule(AbstractModel):
    """精准访问控制匹配规则

    """

    def __init__(self):
        """
        :param MatchKey: 匹配关键字, params | url | ip | referer | user-agent
        :type MatchKey: str
        :param LogiOperator: 逻辑操作符，取值 exclude, include, notequal, equal, len-less, len-equal, len-more
        :type LogiOperator: str
        :param MatchValue: 匹配值
        :type MatchValue: str
        """
        self.MatchKey = None
        self.LogiOperator = None
        self.MatchValue = None


    def _deserialize(self, params):
        self.MatchKey = params.get("MatchKey")
        self.LogiOperator = params.get("LogiOperator")
        self.MatchValue = params.get("MatchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnBotConfig(AbstractModel):
    """bot配置类型

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        :param BotCookie: Bot cookie策略
注意：此字段可能返回 null，表示取不到有效值。
        :type BotCookie: list of BotCookie
        :param BotJavaScript: Bot Js策略
注意：此字段可能返回 null，表示取不到有效值。
        :type BotJavaScript: list of BotJavaScript
        """
        self.Switch = None
        self.BotCookie = None
        self.BotJavaScript = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("BotCookie") is not None:
            self.BotCookie = []
            for item in params.get("BotCookie"):
                obj = BotCookie()
                obj._deserialize(item)
                self.BotCookie.append(obj)
        if params.get("BotJavaScript") is not None:
            self.BotJavaScript = []
            for item in params.get("BotJavaScript"):
                obj = BotJavaScript()
                obj._deserialize(item)
                self.BotJavaScript.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnCCRules(AbstractModel):
    """scdn 的自定义 cc 规则

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
        :type RuleType: str
        :param RuleValue: 规则值
        :type RuleValue: list of str
        :param Qps: 规则限频
        :type Qps: int
        :param DetectionTime: 探测时长
注意：此字段可能返回 null，表示取不到有效值。
        :type DetectionTime: int
        :param FrequencyLimit: 限频阈值
注意：此字段可能返回 null，表示取不到有效值。
        :type FrequencyLimit: int
        :param PunishmentSwitch: IP 惩罚开关，可选on|off
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishmentSwitch: str
        :param PunishmentTime: IP 惩罚时长
注意：此字段可能返回 null，表示取不到有效值。
        :type PunishmentTime: int
        :param Action: 执行动作，intercept|redirect
注意：此字段可能返回 null，表示取不到有效值。
        :type Action: str
        :param RedirectUrl: 动作为 redirect 时，重定向的url
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectUrl: str
        """
        self.RuleType = None
        self.RuleValue = None
        self.Qps = None
        self.DetectionTime = None
        self.FrequencyLimit = None
        self.PunishmentSwitch = None
        self.PunishmentTime = None
        self.Action = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RuleValue = params.get("RuleValue")
        self.Qps = params.get("Qps")
        self.DetectionTime = params.get("DetectionTime")
        self.FrequencyLimit = params.get("FrequencyLimit")
        self.PunishmentSwitch = params.get("PunishmentSwitch")
        self.PunishmentTime = params.get("PunishmentTime")
        self.Action = params.get("Action")
        self.RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnConfig(AbstractModel):
    """cc的配置类型

    """

    def __init__(self):
        """
        :param Switch: on | off
        :type Switch: str
        :param Rules: 自定义 cc 防护规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ScdnCCRules
        """
        self.Switch = None
        self.Rules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ScdnCCRules()
                obj._deserialize(item)
                self.Rules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnDdosConfig(AbstractModel):
    """ddos配置类型

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnDomain(AbstractModel):
    """聚合了SCDN域名的基本信息

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param Status: 当前状态，取值online | offline | process
        :type Status: str
        :param Waf: Waf 状态默认为‘/’，取值 close | intercept | observe
        :type Waf: str
        :param Acl: Acl 状态默认为‘/’，取值 close | open
        :type Acl: str
        :param CC: CC 状态默认为‘/’，取值 close | open
        :type CC: str
        :param Ddos: Ddos 状态默认为‘/’，取值 close | open
        :type Ddos: str
        :param ProjectId: 项目ID
        :type ProjectId: str
        :param AclRuleNumbers: Acl 规则数
        :type AclRuleNumbers: int
        :param Bot: Bot 状态默认为‘/’，取值 close | open
        :type Bot: str
        :param Area: 域名加速区域，取值global | mainland |  overseas
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
        self.Domain = None
        self.Status = None
        self.Waf = None
        self.Acl = None
        self.CC = None
        self.Ddos = None
        self.ProjectId = None
        self.AclRuleNumbers = None
        self.Bot = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Status = params.get("Status")
        self.Waf = params.get("Waf")
        self.Acl = params.get("Acl")
        self.CC = params.get("CC")
        self.Ddos = params.get("Ddos")
        self.ProjectId = params.get("ProjectId")
        self.AclRuleNumbers = params.get("AclRuleNumbers")
        self.Bot = params.get("Bot")
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnErrorPage(AbstractModel):
    """acl的错误页面

    """

    def __init__(self):
        """
        :param RedirectCode: 状态码
        :type RedirectCode: int
        :param RedirectUrl: 重定向url
        :type RedirectUrl: str
        """
        self.RedirectCode = None
        self.RedirectUrl = None


    def _deserialize(self, params):
        self.RedirectCode = params.get("RedirectCode")
        self.RedirectUrl = params.get("RedirectUrl")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnEventLogConditions(AbstractModel):
    """SCDN 事件日志查询条件

    """

    def __init__(self):
        """
        :param Key: 匹配关键字，ip, attack_location
        :type Key: str
        :param Operator: 逻辑操作符，取值 exclude, include
        :type Operator: str
        :param Value: 匹配值，允许使用通配符(*)查询，匹配零个、单个、多个字符，例如 1.2.*
        :type Value: str
        """
        self.Key = None
        self.Operator = None
        self.Value = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Operator = params.get("Operator")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnLogTaskDetail(AbstractModel):
    """SCDN日志事件详细信息

    """

    def __init__(self):
        """
        :param Domain: scdn域名
        :type Domain: str
        :param Mode: 防护类型
        :type Mode: str
        :param StartTime: 查询任务开始时间
        :type StartTime: str
        :param EndTime: 查询任务结束时间
        :type EndTime: str
        :param CreateTime: 任务创建时间
        :type CreateTime: str
        :param DownloadUrl: 日志包下载链接
成功返回下载链接，其他情况返回'-'
注意：此字段可能返回 null，表示取不到有效值。
        :type DownloadUrl: str
        :param Status: 任务状态
created->任务已经创建
processing->任务正在执行
done->任务执行成功
failed->任务执行失败
no-log->没有日志产生
        :type Status: str
        :param TaskID: 日志任务唯一id
        :type TaskID: str
        :param AttackType: 攻击类型, 可以为"all"
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
        :param DefenceMode: 防御模式,可以为"all"
DefenceMode映射如下：
  observe = '观察模式'
  intercept = '防御模式'
        :type DefenceMode: str
        :param Conditions: 查询条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Conditions: list of ScdnEventLogConditions
        :param Area: mainland或overseas
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        """
        self.Domain = None
        self.Mode = None
        self.StartTime = None
        self.EndTime = None
        self.CreateTime = None
        self.DownloadUrl = None
        self.Status = None
        self.TaskID = None
        self.AttackType = None
        self.DefenceMode = None
        self.Conditions = None
        self.Area = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Mode = params.get("Mode")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.CreateTime = params.get("CreateTime")
        self.DownloadUrl = params.get("DownloadUrl")
        self.Status = params.get("Status")
        self.TaskID = params.get("TaskID")
        self.AttackType = params.get("AttackType")
        self.DefenceMode = params.get("DefenceMode")
        if params.get("Conditions") is not None:
            self.Conditions = []
            for item in params.get("Conditions"):
                obj = ScdnEventLogConditions()
                obj._deserialize(item)
                self.Conditions.append(obj)
        self.Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnTopData(AbstractModel):
    """SCDN攻击数据Top展示

    """

    def __init__(self):
        """
        :param Time: 时间
        :type Time: str
        :param Value: 数值
        :type Value: int
        :param Isp: 运营商
        :type Isp: str
        :param Ip: IP地址
        :type Ip: str
        :param District: 区域
        :type District: str
        """
        self.Time = None
        self.Value = None
        self.Isp = None
        self.Ip = None
        self.District = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        self.Isp = params.get("Isp")
        self.Ip = params.get("Ip")
        self.District = params.get("District")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnTopUrlData(AbstractModel):
    """SCDN攻击数据Top URL展示

    """

    def __init__(self):
        """
        :param Url: Top数据的URL
        :type Url: str
        :param Value: 数值
        :type Value: int
        :param Time: 时间
        :type Time: str
        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        """
        self.Url = None
        self.Value = None
        self.Time = None
        self.Domain = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.Value = params.get("Value")
        self.Time = params.get("Time")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnTypeData(AbstractModel):
    """Scdn饼图数据，waf仅有

    """

    def __init__(self):
        """
        :param AttackType: 攻击类型
        :type AttackType: str
        :param Value: 攻击值
        :type Value: int
        """
        self.AttackType = None
        self.Value = None


    def _deserialize(self, params):
        self.AttackType = params.get("AttackType")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnWafConfig(AbstractModel):
    """waf配置类型

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        :param Mode: intercept|observe，默认intercept
注意：此字段可能返回 null，表示取不到有效值。
        :type Mode: str
        :param ErrorPage: 重定向的错误页面
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`
        :param WebShellSwitch: webshell拦截开关，on|off，默认off
注意：此字段可能返回 null，表示取不到有效值。
        :type WebShellSwitch: str
        :param Rules: 类型拦截规则
注意：此字段可能返回 null，表示取不到有效值。
        :type Rules: list of ScdnWafRule
        :param Level: waf规则等级，可取100|200|300
注意：此字段可能返回 null，表示取不到有效值。
        :type Level: int
        :param SubRuleSwitch: waf子规则开关
注意：此字段可能返回 null，表示取不到有效值。
        :type SubRuleSwitch: list of WafSubRuleStatus
        """
        self.Switch = None
        self.Mode = None
        self.ErrorPage = None
        self.WebShellSwitch = None
        self.Rules = None
        self.Level = None
        self.SubRuleSwitch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Mode = params.get("Mode")
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ScdnErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        self.WebShellSwitch = params.get("WebShellSwitch")
        if params.get("Rules") is not None:
            self.Rules = []
            for item in params.get("Rules"):
                obj = ScdnWafRule()
                obj._deserialize(item)
                self.Rules.append(obj)
        self.Level = params.get("Level")
        if params.get("SubRuleSwitch") is not None:
            self.SubRuleSwitch = []
            for item in params.get("SubRuleSwitch"):
                obj = WafSubRuleStatus()
                obj._deserialize(item)
                self.SubRuleSwitch.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ScdnWafRule(AbstractModel):
    """Waf 规则信息

    """

    def __init__(self):
        """
        :param AttackType: 攻击类型
        :type AttackType: str
        :param Operate: 防护措施，observe
        :type Operate: str
        """
        self.AttackType = None
        self.Operate = None


    def _deserialize(self, params):
        self.AttackType = params.get("AttackType")
        self.Operate = params.get("Operate")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SchemeKey(AbstractModel):
    """作为CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: on | off 是否使用scheme作为cache key的一部分
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 需要查询的日志集ID
        :type LogsetId: str
        :param TopicIds: 需要查询的日志主题ID组合，以逗号分隔
        :type TopicIds: str
        :param StartTime: 需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS
        :type StartTime: str
        :param EndTime: 需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS
        :type EndTime: str
        :param Limit: 单次要返回的日志条数，单次返回的最大条数为100
        :type Limit: int
        :param Channel: 接入渠道，默认值为cdn
        :type Channel: str
        :param Query: 需要查询的内容，详情请参考https://cloud.tencent.com/document/product/614/16982
        :type Query: str
        :param Context: 加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围
        :type Context: str
        :param Sort: 按日志时间排序， asc（升序）或者 desc（降序），默认为 desc
        :type Sort: str
        """
        self.LogsetId = None
        self.TopicIds = None
        self.StartTime = None
        self.EndTime = None
        self.Limit = None
        self.Channel = None
        self.Query = None
        self.Context = None
        self.Sort = None


    def _deserialize(self, params):
        self.LogsetId = params.get("LogsetId")
        self.TopicIds = params.get("TopicIds")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Limit = params.get("Limit")
        self.Channel = params.get("Channel")
        self.Query = params.get("Query")
        self.Context = params.get("Context")
        self.Sort = params.get("Sort")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog返回参数结构体

    """

    def __init__(self):
        """
        :param Logs: 查询结果
        :type Logs: :class:`tencentcloud.cdn.v20180606.models.ClsSearchLogs`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logs") is not None:
            self.Logs = ClsSearchLogs()
            self.Logs._deserialize(params.get("Logs"))
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SecurityConfig(AbstractModel):
    """scdn相关的配置

    """

    def __init__(self):
        """
        :param Switch: on|off
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Seo(AbstractModel):
    """SEO 搜索引擎优化配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: SEO 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ServerCert(AbstractModel):
    """https 加速服务端证书配置：
    + 支持使用托管至 SSL 证书管理的证书进行部署
    + 支持上传 PEM 格式的证书进行部署
    注意：上传 PEM 证书时，需要进行 Base 64 编码

    """

    def __init__(self):
        """
        :param CertId: 服务器证书 ID
在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param CertName: 服务器证书名称
在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param Certificate: 服务器证书信息
上传自有证书时必填，需要包含完整的证书链
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param PrivateKey: 服务器密钥信息
上传自有证书时必填
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param ExpireTime: 证书过期时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param DeployTime: 证书颁发时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param Message: 证书备注信息
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SimpleCache(AbstractModel):
    """缓存配置基础版本
    默认情况下所有文件缓存过期时间为 30 天
    默认情况下静态加速类型的域名 .php;.jsp;.asp;.aspx 不缓存
    注意：该版本不支持设置源站未返回 max-age 情况下的缓存过期规则设置

    """

    def __init__(self):
        """
        :param CacheRules: 缓存过期时间规则
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheRules: list of SimpleCacheRule
        :param FollowOrigin: 遵循源站 Cache-Control: max-age 配置
on：开启
off：关闭
开启后，未能匹配 CacheRules 规则的资源将根据源站返回的 max-age 值进行节点缓存；匹配了 CacheRules 规则的资源将按照 CacheRules 中设置的缓存过期时间在节点进行缓存
与 CompareMaxAge 冲突，不能同时开启
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        :param IgnoreCacheControl: 强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreCacheControl: str
        :param IgnoreSetCookie: 忽略源站的Set-Cookie头部
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type IgnoreSetCookie: str
        :param CompareMaxAge: 高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。
        :type CompareMaxAge: str
        :param Revalidate: 总是回源站校验
注意：此字段可能返回 null，表示取不到有效值。
        :type Revalidate: :class:`tencentcloud.cdn.v20180606.models.Revalidate`
        """
        self.CacheRules = None
        self.FollowOrigin = None
        self.IgnoreCacheControl = None
        self.IgnoreSetCookie = None
        self.CompareMaxAge = None
        self.Revalidate = None


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = SimpleCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        self.FollowOrigin = params.get("FollowOrigin")
        self.IgnoreCacheControl = params.get("IgnoreCacheControl")
        self.IgnoreSetCookie = params.get("IgnoreSetCookie")
        self.CompareMaxAge = params.get("CompareMaxAge")
        if params.get("Revalidate") is not None:
            self.Revalidate = Revalidate()
            self.Revalidate._deserialize(params.get("Revalidate"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SimpleCacheRule(AbstractModel):
    """缓存过期规则配置

    """

    def __init__(self):
        """
        :param CacheType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
        :type CacheType: str
        :param CacheContents: CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
        :type CacheContents: list of str
        :param CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
        :type CacheTime: int
        """
        self.CacheType = None
        self.CacheContents = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.CacheType = params.get("CacheType")
        self.CacheContents = params.get("CacheContents")
        self.CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Sort(AbstractModel):
    """查询结果排序条件

    """

    def __init__(self):
        """
        :param Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
默认createTime。
        :type Key: str
        :param Sequence: asc/desc，默认desc。
        :type Sequence: str
        """
        self.Key = None
        self.Sequence = None


    def _deserialize(self, params):
        self.Key = params.get("Key")
        self.Sequence = params.get("Sequence")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SpecificConfig(AbstractModel):
    """域名国内海外分地区特殊配置。

    """

    def __init__(self):
        """
        :param Mainland: 国内特殊配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Mainland: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`
        :param Overseas: 海外特殊配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Overseas: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`
        """
        self.Mainland = None
        self.Overseas = None


    def _deserialize(self, params):
        if params.get("Mainland") is not None:
            self.Mainland = MainlandConfig()
            self.Mainland._deserialize(params.get("Mainland"))
        if params.get("Overseas") is not None:
            self.Overseas = OverseaConfig()
            self.Overseas._deserialize(params.get("Overseas"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
域名状态需要为【已停用】
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartScdnDomainRequest(AbstractModel):
    """StartScdnDomain请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StartScdnDomainResponse(AbstractModel):
    """StartScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 开启结果，Success表示成功
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StatusCodeCache(AbstractModel):
    """状态码缓存过期配置，默认情况下会对 404 状态码缓存 10 秒

    """

    def __init__(self):
        """
        :param Switch: 状态码缓存过期配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param CacheRules: 状态码缓存过期规则明细
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheRules: list of StatusCodeCacheRule
        """
        self.Switch = None
        self.CacheRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("CacheRules") is not None:
            self.CacheRules = []
            for item in params.get("CacheRules"):
                obj = StatusCodeCacheRule()
                obj._deserialize(item)
                self.CacheRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StatusCodeCacheRule(AbstractModel):
    """状态码缓存过期时间规则配置

    """

    def __init__(self):
        """
        :param StatusCode: http 状态码
支持 403、404 状态码
        :type StatusCode: str
        :param CacheTime: 状态码缓存过期时间，单位秒
        :type CacheTime: int
        """
        self.StatusCode = None
        self.CacheTime = None


    def _deserialize(self, params):
        self.StatusCode = params.get("StatusCode")
        self.CacheTime = params.get("CacheTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
域名需要为【已启动】状态
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopScdnDomainRequest(AbstractModel):
    """StopScdnDomain请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class StopScdnDomainResponse(AbstractModel):
    """StopScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 关闭结果，Success表示成功
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class SummarizedData(AbstractModel):
    """明细数据的汇总值，各指标根据其特性不同拥有不同汇总方式

    """

    def __init__(self):
        """
        :param Name: 汇总方式，存在以下几种：
sum：累加求和
max：最大值，带宽模式下，采用 5 分钟粒度汇总数据，计算峰值带宽
avg：平均值
        :type Name: str
        :param Value: 汇总后的数据值
        :type Value: float
        """
        self.Name = None
        self.Value = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class Tag(AbstractModel):
    """域名标签配置

    """

    def __init__(self):
        """
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。
        :type TagKey: str
        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TimestampData(AbstractModel):
    """时间戳与其对应的数值

    """

    def __init__(self):
        """
        :param Time: 数据统计时间点，采用向前汇总模式
以 5 分钟粒度为例，13:35:00 时间点代表的统计数据区间为 13:35:00 至 13:39:59
        :type Time: str
        :param Value: 数据值
        :type Value: float
        """
        self.Time = None
        self.Value = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Value = params.get("Value")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TopData(AbstractModel):
    """排序类型数据结构

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :type Resource: str
        :param DetailData: 排序结果详情
        :type DetailData: list of TopDetailData
        """
        self.Resource = None
        self.DetailData = None


    def _deserialize(self, params):
        self.Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self.DetailData = []
            for item in params.get("DetailData"):
                obj = TopDetailData()
                obj._deserialize(item)
                self.DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TopDetailData(AbstractModel):
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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TopicInfo(AbstractModel):
    """CLS主题信息

    """

    def __init__(self):
        """
        :param TopicId: 主题ID
        :type TopicId: str
        :param TopicName: 主题名字
        :type TopicName: str
        :param Enabled: 是否启用投递
        :type Enabled: int
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        """
        self.TopicId = None
        self.TopicName = None
        self.Enabled = None
        self.CreateTime = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Enabled = params.get("Enabled")
        self.CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TpgAdapter(AbstractModel):
    """图片优化-TpgAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 开关，"on/off"
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class TrafficPackage(AbstractModel):
    """CDN加速流量包。

    """

    def __init__(self):
        """
        :param Id: 流量包 Id
        :type Id: int
        :param Type: 流量包类型
        :type Type: str
        :param Bytes: 流量包大小（单位为 Byte）
        :type Bytes: int
        :param BytesUsed: 已消耗流量（单位为 Byte）
        :type BytesUsed: int
        :param Status: 流量包状态
enabled：已启用
expired：已过期
disabled：未启用
        :type Status: str
        :param CreateTime: 流量包发放时间
        :type CreateTime: str
        :param EnableTime: 流量包生效时间
        :type EnableTime: str
        :param ExpireTime: 流量包过期时间
        :type ExpireTime: str
        :param ContractExtension: 流量包是否续订
        :type ContractExtension: bool
        :param AutoExtension: 流量包是否自动续订
        :type AutoExtension: bool
        :param Channel: 流量包来源
        :type Channel: str
        :param Area: 流量包生效区域，目前仅支持mainland
        :type Area: str
        :param LifeTimeMonth: 流量包生命周期月数
        :type LifeTimeMonth: int
        :param ExtensionAvailable: 流量包是否支持续订
        :type ExtensionAvailable: bool
        :param RefundAvailable: 流量包是否支持退费
        :type RefundAvailable: bool
        """
        self.Id = None
        self.Type = None
        self.Bytes = None
        self.BytesUsed = None
        self.Status = None
        self.CreateTime = None
        self.EnableTime = None
        self.ExpireTime = None
        self.ContractExtension = None
        self.AutoExtension = None
        self.Channel = None
        self.Area = None
        self.LifeTimeMonth = None
        self.ExtensionAvailable = None
        self.RefundAvailable = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.Type = params.get("Type")
        self.Bytes = params.get("Bytes")
        self.BytesUsed = params.get("BytesUsed")
        self.Status = params.get("Status")
        self.CreateTime = params.get("CreateTime")
        self.EnableTime = params.get("EnableTime")
        self.ExpireTime = params.get("ExpireTime")
        self.ContractExtension = params.get("ContractExtension")
        self.AutoExtension = params.get("AutoExtension")
        self.Channel = params.get("Channel")
        self.Area = params.get("Area")
        self.LifeTimeMonth = params.get("LifeTimeMonth")
        self.ExtensionAvailable = params.get("ExtensionAvailable")
        self.RefundAvailable = params.get("RefundAvailable")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param ProjectId: 项目 ID
        :type ProjectId: int
        :param Origin: 源站配置
        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`
        :param IpFilter: IP 黑白名单配置
        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`
        :param IpFreqLimit: IP 限频配置
        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`
        :param StatusCodeCache: 状态码缓存配置
        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`
        :param Compression: 智能压缩配置
        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`
        :param BandwidthAlert: 带宽封顶配置
        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`
        :param RangeOriginPull: Range 回源配置
        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`
        :param FollowRedirect: 301/302 回源跟随配置
        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`
        :param ErrorPage: 错误码重定向配置（功能灰度中，尚未全量）
        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`
        :param RequestHeader: 请求头部配置
        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`
        :param ResponseHeader: 响应头部配置
        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`
        :param DownstreamCapping: 下载速度配置
        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`
        :param CacheKey: 节点缓存键配置
        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`
        :param ResponseHeaderCache: 头部缓存配置
        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`
        :param VideoSeek: 视频拖拽配置
        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`
        :param Cache: 缓存过期时间配置
        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`
        :param OriginPullOptimization: 跨国链路优化配置
        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`
        :param Https: Https 加速配置
        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`
        :param Authentication: 时间戳防盗链配置
        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`
        :param Seo: SEO 优化配置
        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`
        :param ForceRedirect: 访问协议强制跳转配置
        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`
        :param Referer: Referer 防盗链配置
        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`
        :param MaxAge: 浏览器缓存配置（功能灰度中，尚未全量）
        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`
        :param ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速
        :type ServiceType: str
        :param SpecificConfig: 地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景
        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`
        :param Area: 域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
        :type Area: str
        :param OriginPullTimeout: 回源超时配置
        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`
        :param AwsPrivateAccess: 回源S3私有鉴权
        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`
        :param UserAgentFilter: UA黑白名单配置
        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`
        :param AccessControl: 访问控制
        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`
        :param UrlRedirect: URL重定向配置
        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`
        :param AccessPort: 访问端口配置
        :type AccessPort: list of int
        :param AdvancedAuthentication: 时间戳防盗链高级版配置，白名单功能
        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`
        :param OriginAuthentication: 回源鉴权高级版配置，白名单功能
        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`
        :param Ipv6Access: Ipv6 访问配置
        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`
        :param OfflineCache: 离线缓存
        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`
        :param OriginCombine: 合并回源
        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`
        :param Quic: QUIC正在内测中，请先提交内测申请，详情请前往QUIC产品文档。
        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`
        """
        self.Domain = None
        self.ProjectId = None
        self.Origin = None
        self.IpFilter = None
        self.IpFreqLimit = None
        self.StatusCodeCache = None
        self.Compression = None
        self.BandwidthAlert = None
        self.RangeOriginPull = None
        self.FollowRedirect = None
        self.ErrorPage = None
        self.RequestHeader = None
        self.ResponseHeader = None
        self.DownstreamCapping = None
        self.CacheKey = None
        self.ResponseHeaderCache = None
        self.VideoSeek = None
        self.Cache = None
        self.OriginPullOptimization = None
        self.Https = None
        self.Authentication = None
        self.Seo = None
        self.ForceRedirect = None
        self.Referer = None
        self.MaxAge = None
        self.ServiceType = None
        self.SpecificConfig = None
        self.Area = None
        self.OriginPullTimeout = None
        self.AwsPrivateAccess = None
        self.UserAgentFilter = None
        self.AccessControl = None
        self.UrlRedirect = None
        self.AccessPort = None
        self.AdvancedAuthentication = None
        self.OriginAuthentication = None
        self.Ipv6Access = None
        self.OfflineCache = None
        self.OriginCombine = None
        self.Quic = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.ProjectId = params.get("ProjectId")
        if params.get("Origin") is not None:
            self.Origin = Origin()
            self.Origin._deserialize(params.get("Origin"))
        if params.get("IpFilter") is not None:
            self.IpFilter = IpFilter()
            self.IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self.IpFreqLimit = IpFreqLimit()
            self.IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("StatusCodeCache") is not None:
            self.StatusCodeCache = StatusCodeCache()
            self.StatusCodeCache._deserialize(params.get("StatusCodeCache"))
        if params.get("Compression") is not None:
            self.Compression = Compression()
            self.Compression._deserialize(params.get("Compression"))
        if params.get("BandwidthAlert") is not None:
            self.BandwidthAlert = BandwidthAlert()
            self.BandwidthAlert._deserialize(params.get("BandwidthAlert"))
        if params.get("RangeOriginPull") is not None:
            self.RangeOriginPull = RangeOriginPull()
            self.RangeOriginPull._deserialize(params.get("RangeOriginPull"))
        if params.get("FollowRedirect") is not None:
            self.FollowRedirect = FollowRedirect()
            self.FollowRedirect._deserialize(params.get("FollowRedirect"))
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        if params.get("RequestHeader") is not None:
            self.RequestHeader = RequestHeader()
            self.RequestHeader._deserialize(params.get("RequestHeader"))
        if params.get("ResponseHeader") is not None:
            self.ResponseHeader = ResponseHeader()
            self.ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("DownstreamCapping") is not None:
            self.DownstreamCapping = DownstreamCapping()
            self.DownstreamCapping._deserialize(params.get("DownstreamCapping"))
        if params.get("CacheKey") is not None:
            self.CacheKey = CacheKey()
            self.CacheKey._deserialize(params.get("CacheKey"))
        if params.get("ResponseHeaderCache") is not None:
            self.ResponseHeaderCache = ResponseHeaderCache()
            self.ResponseHeaderCache._deserialize(params.get("ResponseHeaderCache"))
        if params.get("VideoSeek") is not None:
            self.VideoSeek = VideoSeek()
            self.VideoSeek._deserialize(params.get("VideoSeek"))
        if params.get("Cache") is not None:
            self.Cache = Cache()
            self.Cache._deserialize(params.get("Cache"))
        if params.get("OriginPullOptimization") is not None:
            self.OriginPullOptimization = OriginPullOptimization()
            self.OriginPullOptimization._deserialize(params.get("OriginPullOptimization"))
        if params.get("Https") is not None:
            self.Https = Https()
            self.Https._deserialize(params.get("Https"))
        if params.get("Authentication") is not None:
            self.Authentication = Authentication()
            self.Authentication._deserialize(params.get("Authentication"))
        if params.get("Seo") is not None:
            self.Seo = Seo()
            self.Seo._deserialize(params.get("Seo"))
        if params.get("ForceRedirect") is not None:
            self.ForceRedirect = ForceRedirect()
            self.ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Referer") is not None:
            self.Referer = Referer()
            self.Referer._deserialize(params.get("Referer"))
        if params.get("MaxAge") is not None:
            self.MaxAge = MaxAge()
            self.MaxAge._deserialize(params.get("MaxAge"))
        self.ServiceType = params.get("ServiceType")
        if params.get("SpecificConfig") is not None:
            self.SpecificConfig = SpecificConfig()
            self.SpecificConfig._deserialize(params.get("SpecificConfig"))
        self.Area = params.get("Area")
        if params.get("OriginPullTimeout") is not None:
            self.OriginPullTimeout = OriginPullTimeout()
            self.OriginPullTimeout._deserialize(params.get("OriginPullTimeout"))
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("UserAgentFilter") is not None:
            self.UserAgentFilter = UserAgentFilter()
            self.UserAgentFilter._deserialize(params.get("UserAgentFilter"))
        if params.get("AccessControl") is not None:
            self.AccessControl = AccessControl()
            self.AccessControl._deserialize(params.get("AccessControl"))
        if params.get("UrlRedirect") is not None:
            self.UrlRedirect = UrlRedirect()
            self.UrlRedirect._deserialize(params.get("UrlRedirect"))
        self.AccessPort = params.get("AccessPort")
        if params.get("AdvancedAuthentication") is not None:
            self.AdvancedAuthentication = AdvancedAuthentication()
            self.AdvancedAuthentication._deserialize(params.get("AdvancedAuthentication"))
        if params.get("OriginAuthentication") is not None:
            self.OriginAuthentication = OriginAuthentication()
            self.OriginAuthentication._deserialize(params.get("OriginAuthentication"))
        if params.get("Ipv6Access") is not None:
            self.Ipv6Access = Ipv6Access()
            self.Ipv6Access._deserialize(params.get("Ipv6Access"))
        if params.get("OfflineCache") is not None:
            self.OfflineCache = OfflineCache()
            self.OfflineCache._deserialize(params.get("OfflineCache"))
        if params.get("OriginCombine") is not None:
            self.OriginCombine = OriginCombine()
            self.OriginCombine._deserialize(params.get("OriginCombine"))
        if params.get("Quic") is not None:
            self.Quic = Quic()
            self.Quic._deserialize(params.get("Quic"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateImageConfigRequest(AbstractModel):
    """UpdateImageConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param WebpAdapter: WebpAdapter配置项
        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`
        :param TpgAdapter: TpgAdapter配置项
        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`
        :param GuetzliAdapter: GuetzliAdapter配置项
        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`
        """
        self.Domain = None
        self.WebpAdapter = None
        self.TpgAdapter = None
        self.GuetzliAdapter = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("WebpAdapter") is not None:
            self.WebpAdapter = WebpAdapter()
            self.WebpAdapter._deserialize(params.get("WebpAdapter"))
        if params.get("TpgAdapter") is not None:
            self.TpgAdapter = TpgAdapter()
            self.TpgAdapter._deserialize(params.get("TpgAdapter"))
        if params.get("GuetzliAdapter") is not None:
            self.GuetzliAdapter = GuetzliAdapter()
            self.GuetzliAdapter._deserialize(params.get("GuetzliAdapter"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateImageConfigResponse(AbstractModel):
    """UpdateImageConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType请求参数结构体

    """

    def __init__(self):
        """
        :param Area: 计费区域，mainland或overseas。
        :type Area: str
        :param PayType: 计费类型，flux或bandwidth。
        :type PayType: str
        """
        self.Area = None
        self.PayType = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.PayType = params.get("PayType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateScdnDomainRequest(AbstractModel):
    """UpdateScdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
        :type Domain: str
        :param Waf: Web 攻击防护（WAF）配置
        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`
        :param Acl: 自定义防护策略配置
        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`
        :param CC: CC 防护配置，目前 CC 防护默认开启
        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`
        :param Ddos: DDOS 防护配置，目前 DDoS 防护默认开启
        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`
        :param Bot: BOT 防护配置
        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`
        """
        self.Domain = None
        self.Waf = None
        self.Acl = None
        self.CC = None
        self.Ddos = None
        self.Bot = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("Waf") is not None:
            self.Waf = ScdnWafConfig()
            self.Waf._deserialize(params.get("Waf"))
        if params.get("Acl") is not None:
            self.Acl = ScdnAclConfig()
            self.Acl._deserialize(params.get("Acl"))
        if params.get("CC") is not None:
            self.CC = ScdnConfig()
            self.CC._deserialize(params.get("CC"))
        if params.get("Ddos") is not None:
            self.Ddos = ScdnDdosConfig()
            self.Ddos._deserialize(params.get("Ddos"))
        if params.get("Bot") is not None:
            self.Bot = ScdnBotConfig()
            self.Bot._deserialize(params.get("Bot"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UpdateScdnDomainResponse(AbstractModel):
    """UpdateScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 提交结果，Success表示成功
        :type Result: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UrlRecord(AbstractModel):
    """封禁url的详细信息

    """

    def __init__(self):
        """
        :param Status: 状态(disable表示封禁，enable表示解封)
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: str
        :param RealUrl: 对应的url
注意：此字段可能返回 null，表示取不到有效值。
        :type RealUrl: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: str
        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。
        :type UpdateTime: str
        """
        self.Status = None
        self.RealUrl = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.RealUrl = params.get("RealUrl")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UrlRedirect(AbstractModel):
    """URL重定向配置

    """

    def __init__(self):
        """
        :param Switch: URL重定向配置开关
on：开启
off：关闭
        :type Switch: str
        :param PathRules: URL重定向规则，当Switch为on时必填，规则数量最大为10个。
注意：此字段可能返回 null，表示取不到有效值。
        :type PathRules: list of UrlRedirectRule
        """
        self.Switch = None
        self.PathRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("PathRules") is not None:
            self.PathRules = []
            for item in params.get("PathRules"):
                obj = UrlRedirectRule()
                obj._deserialize(item)
                self.PathRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UrlRedirectRule(AbstractModel):
    """Url重定向规则配置

    """

    def __init__(self):
        """
        :param RedirectStatusCode: 重定向状态码，301 | 302
        :type RedirectStatusCode: int
        :param Pattern: 待匹配的Url，仅支持Url路径，不支持参数。默认完全匹配，支持通配符 *，最多支持5个通配符，最大长度1024字符。
        :type Pattern: str
        :param RedirectUrl: 目标URL，必须以“/”开头，不包含参数部分。最大长度1024字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号，最多支持10个捕获值。
        :type RedirectUrl: str
        :param RedirectHost: 目标host，必须以http://或https://开头，并填写标准格式域名，如果不填写，默认为http:// + 当前域名
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectHost: str
        """
        self.RedirectStatusCode = None
        self.Pattern = None
        self.RedirectUrl = None
        self.RedirectHost = None


    def _deserialize(self, params):
        self.RedirectStatusCode = params.get("RedirectStatusCode")
        self.Pattern = params.get("Pattern")
        self.RedirectUrl = params.get("RedirectUrl")
        self.RedirectHost = params.get("RedirectHost")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UserAgentFilter(AbstractModel):
    """UserAgent黑白名单配置

    """

    def __init__(self):
        """
        :param Switch: 开关，on或off
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param FilterRules: UA黑白名单生效规则列表
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterRules: list of UserAgentFilterRule
        """
        self.Switch = None
        self.FilterRules = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        if params.get("FilterRules") is not None:
            self.FilterRules = []
            for item in params.get("FilterRules"):
                obj = UserAgentFilterRule()
                obj._deserialize(item)
                self.FilterRules.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class UserAgentFilterRule(AbstractModel):
    """UserAgent黑白名单规则配置

    """

    def __init__(self):
        """
        :param RuleType: 访问路径生效类型
all: 所有访问路径生效
file: 根据文件后缀类型生效
directory: 根据目录生效
path: 根据完整访问路径生效
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param RulePaths: 访问路径生效内容
注意：此字段可能返回 null，表示取不到有效值。
        :type RulePaths: list of str
        :param UserAgents: UserAgent列表
注意：此字段可能返回 null，表示取不到有效值。
        :type UserAgents: list of str
        :param FilterType: 黑名单或白名单，blacklist或whitelist
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        """
        self.RuleType = None
        self.RulePaths = None
        self.UserAgents = None
        self.FilterType = None


    def _deserialize(self, params):
        self.RuleType = params.get("RuleType")
        self.RulePaths = params.get("RulePaths")
        self.UserAgents = params.get("UserAgents")
        self.FilterType = params.get("FilterType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VerifyDomainRecordRequest(AbstractModel):
    """VerifyDomainRecord请求参数结构体

    """

    def __init__(self):
        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VerifyDomainRecordResponse(AbstractModel):
    """VerifyDomainRecord返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否验证成功
        :type Result: bool
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class VideoSeek(AbstractModel):
    """视频拖拽配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 视频拖拽开关
on：开启
off：关闭
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class ViolationUrl(AbstractModel):
    """违规 URL 详情

    """

    def __init__(self):
        """
        :param Id: ID
        :type Id: int
        :param RealUrl: 违规资源原始访问 URL
        :type RealUrl: str
        :param DownloadUrl: 快照路径，用于控制台展示违规内容快照
        :type DownloadUrl: str
        :param UrlStatus: 违规资源当前状态
forbid：已封禁
release：已解封
delay ： 延迟处理
reject ：申诉驳回，状态仍为封禁态
complain：申诉进行中
        :type UrlStatus: str
        :param CreateTime: 创建时间
        :type CreateTime: str
        :param UpdateTime: 更新时间
        :type UpdateTime: str
        """
        self.Id = None
        self.RealUrl = None
        self.DownloadUrl = None
        self.UrlStatus = None
        self.CreateTime = None
        self.UpdateTime = None


    def _deserialize(self, params):
        self.Id = params.get("Id")
        self.RealUrl = params.get("RealUrl")
        self.DownloadUrl = params.get("DownloadUrl")
        self.UrlStatus = params.get("UrlStatus")
        self.CreateTime = params.get("CreateTime")
        self.UpdateTime = params.get("UpdateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WafSubRuleStatus(AbstractModel):
    """Waf子规则开关状态

    """

    def __init__(self):
        """
        :param Switch: 子规则状态，on|off
        :type Switch: str
        :param SubIds: 规则id列表
        :type SubIds: list of int
        """
        self.Switch = None
        self.SubIds = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.SubIds = params.get("SubIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        


class WebpAdapter(AbstractModel):
    """图片优化-WebpAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 开关，"on/off"
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set), Warning)
        