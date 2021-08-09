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
        """
        :param Switch: on | off 是否启用请求头部及请求url访问控制\n        :type Switch: str\n        :param AccessControlRules: 请求头部及请求url访问规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessControlRules: list of AccessControlRule\n        :param ReturnCode: 返回状态码
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReturnCode: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessControlRule(AbstractModel):
    """访问控制规则

    """

    def __init__(self):
        """
        :param RuleType: requestHeader ：对请求头部进行访问控制
url ： 对访问url进行访问控制
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleType: str\n        :param RuleContent: 封禁内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleContent: str\n        :param Regex: on ：正则匹配
off ：字面匹配
注意：此字段可能返回 null，表示取不到有效值。\n        :type Regex: str\n        :param RuleHeader: RuleType为requestHeader时必填，否则不需要填
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleHeader: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCdnDomainRequest(AbstractModel):
    """AddCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param ServiceType: 加速域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速\n        :type ServiceType: str\n        :param Origin: 源站配置\n        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`\n        :param ProjectId: 项目 ID，默认为 0，代表【默认项目】\n        :type ProjectId: int\n        :param IpFilter: IP 黑白名单配置\n        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`\n        :param IpFreqLimit: IP 限频配置\n        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`\n        :param StatusCodeCache: 状态码缓存配置\n        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`\n        :param Compression: 智能压缩配置\n        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`\n        :param BandwidthAlert: 带宽封顶配置\n        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`\n        :param RangeOriginPull: Range 回源配置\n        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`\n        :param FollowRedirect: 301/302 回源跟随配置。\n        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`\n        :param ErrorPage: 错误码重定向配置（功能灰度中，尚未全量）\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`\n        :param RequestHeader: 请求头部配置\n        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`\n        :param ResponseHeader: 响应头部配置\n        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`\n        :param DownstreamCapping: 下载速度配置\n        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`\n        :param CacheKey: 节点缓存键配置\n        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`\n        :param ResponseHeaderCache: 头部缓存配置\n        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`\n        :param VideoSeek: 视频拖拽配置\n        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`\n        :param Cache: 缓存过期时间配置\n        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`\n        :param OriginPullOptimization: 跨国链路优化配置\n        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`\n        :param Https: Https 加速配置\n        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`\n        :param Authentication: 时间戳防盗链配置\n        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`\n        :param Seo: SEO 优化配置\n        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`\n        :param ForceRedirect: 访问协议强制跳转配置\n        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`\n        :param Referer: Referer 防盗链配置\n        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`\n        :param MaxAge: 浏览器缓存配置（功能灰度中，尚未全量）\n        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`\n        :param Ipv6: Ipv6 配置（功能灰度中，尚未全量）\n        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`\n        :param SpecificConfig: 地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景\n        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`\n        :param Area: 域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
使用中国境外加速、全球加速时，需要先开通中国境外加速服务\n        :type Area: str\n        :param OriginPullTimeout: 回源超时配置\n        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`\n        :param Tag: 标签配置\n        :type Tag: list of Tag\n        :param Ipv6Access: Ipv6 访问配置\n        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`\n        :param OfflineCache: 离线缓存\n        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`\n        :param Quic: QUIC正在内测中，请先提交内测申请，详情请前往QUIC产品文档。\n        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`\n        :param AwsPrivateAccess: 回源S3私有鉴权\n        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`\n        :param OssPrivateAccess: 回源OSS私有鉴权\n        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`\n        """
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
        self.AwsPrivateAccess = None
        self.OssPrivateAccess = None


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
        if params.get("AwsPrivateAccess") is not None:
            self.AwsPrivateAccess = AwsPrivateAccess()
            self.AwsPrivateAccess._deserialize(params.get("AwsPrivateAccess"))
        if params.get("OssPrivateAccess") is not None:
            self.OssPrivateAccess = OssPrivateAccess()
            self.OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddCdnDomainResponse(AbstractModel):
    """AddCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheType: str\n        :param CacheContents: 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
default 时填充 "no max-age"
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheContents: list of str\n        :param CacheTime: 缓存过期时间
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheTime: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvanceConfig(AbstractModel):
    """高级配置集合

    """

    def __init__(self):
        """
        :param Name: 高级配置名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Name: str\n        :param Value: 是否支持高级配置，
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthentication(AbstractModel):
    """时间戳防盗链高级版配置，白名单功能

    """

    def __init__(self):
        """
        :param Switch: 防盗链配置开关，on或off，开启时必须且只能配置一种模式，其余模式为null。\n        :type Switch: str\n        :param TypeA: 时间戳防盗链高级版模式A配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeA`\n        :param TypeB: 时间戳防盗链高级版模式B配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeB`\n        :param TypeC: 时间戳防盗链高级版模式C配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeC`\n        :param TypeD: 时间戳防盗链高级版模式D配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeD`\n        :param TypeE: 时间戳防盗链高级版模式E配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeE: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeE`\n        :param TypeF: 时间戳防盗链高级版模式F配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeF: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthenticationTypeF`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeA(AbstractModel):
    """时间戳防盗链高级版模式A配置。

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。\n        :type SecretKey: str\n        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。\n        :type SignParam: str\n        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。\n        :type TimeParam: str\n        :param ExpireTime: 过期时间，单位秒。\n        :type ExpireTime: int\n        :param ExpireTimeRequired: 是否必须提供过期时间参数。\n        :type ExpireTimeRequired: bool\n        :param Format: Url组成格式，如：${private_key}${schema}${host}${full_uri。\n        :type Format: str\n        :param TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。\n        :type TimeFormat: str\n        :param FailCode: 鉴权失败时返回的状态码。\n        :type FailCode: int\n        :param ExpireCode: 链接过期时返回的状态码。\n        :type ExpireCode: int\n        :param RulePaths: 需要鉴权的url路径列表。\n        :type RulePaths: list of str\n        :param Transformation: 保留字段。\n        :type Transformation: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeB(AbstractModel):
    """时间戳防盗链高级版模式B配置。

    """

    def __init__(self):
        """
        :param KeyAlpha: alpha键名。\n        :type KeyAlpha: str\n        :param KeyBeta: beta键名。\n        :type KeyBeta: str\n        :param KeyGamma: gamma键名。\n        :type KeyGamma: str\n        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。\n        :type SignParam: str\n        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。\n        :type TimeParam: str\n        :param ExpireTime: 过期时间，单位秒。\n        :type ExpireTime: int\n        :param TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。\n        :type TimeFormat: str\n        :param FailCode: 鉴权失败时返回的状态码。\n        :type FailCode: int\n        :param ExpireCode: 链接过期时返回的状态码。\n        :type ExpireCode: int\n        :param RulePaths: 需要鉴权的url路径列表。\n        :type RulePaths: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeC(AbstractModel):
    """时间戳防盗链高级版模式C配置。

    """

    def __init__(self):
        """
        :param AccessKey: 访问密钥。\n        :type AccessKey: str\n        :param SecretKey: 鉴权密钥。\n        :type SecretKey: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeD(AbstractModel):
    """时间戳防盗链高级版模式D配置。

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。\n        :type SecretKey: str\n        :param BackupSecretKey: 备份密钥，当使用SecretKey鉴权失败时会使用该密钥重新鉴权。\n        :type BackupSecretKey: str\n        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。\n        :type SignParam: str\n        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。\n        :type TimeParam: str\n        :param ExpireTime: 过期时间，单位秒。\n        :type ExpireTime: int\n        :param TimeFormat: 时间格式，dec，hex分别表示十进制，十六进制。\n        :type TimeFormat: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeE(AbstractModel):
    """时间戳防盗链高级版模式E配置。

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SignParam: str\n        :param AclSignParam: uri串中Acl签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AclSignParam: str\n        :param StartTimeParam: uri串中开始时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StartTimeParam: str\n        :param ExpireTimeParam: uri串中过期时间字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTimeParam: str\n        :param TimeFormat: 时间格式，dec
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeFormat: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedAuthenticationTypeF(AbstractModel):
    """时间戳防盗链高级鉴权模式TypeF配置

    """

    def __init__(self):
        """
        :param SignParam: uri串中签名的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SignParam: str\n        :param TimeParam: uri串中时间的字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeParam: str\n        :param TransactionParam: uri串中Transaction字段名，字母，数字或下划线构成，同时必须以字母开头。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TransactionParam: str\n        :param SecretKey: 用于计算签名的主密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        :param BackupSecretKey: 用于计算签名的备选密钥，主密钥校验失败后再次尝试备选密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupSecretKey: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AdvancedCache(AbstractModel):
    """缓存过期配置高级版（功能灰度中，尚未全量）
    注意：该版本不支持设置首页缓存规则

    """

    def __init__(self):
        """
        :param CacheRules: 缓存过期规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheRules: list of AdvanceCacheRule\n        :param IgnoreCacheControl: 强制缓存配置
on：开启
off：关闭
开启时，源站返回 no-cache、no-store 头部时，仍按照缓存过期规则进行节点缓存
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreCacheControl: str\n        :param IgnoreSetCookie: 当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreSetCookie: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Authentication(AbstractModel):
    """时间戳防盗链配置

    """

    def __init__(self):
        """
        :param Switch: 防盗链配置开关
on：开启
off：关闭
开启时必须且只配置一种模式，其余模式需要设置为 null\n        :type Switch: str\n        :param TypeA: 时间戳防盗链模式 A 配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeA`\n        :param TypeB: 时间戳防盗链模式 B 配置（模式 B 后台升级中，暂时不支持配置）
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeB: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeB`\n        :param TypeC: 时间戳防盗链模式 C 配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeC: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeC`\n        :param TypeD: 时间戳防盗链模式 D 配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeD: :class:`tencentcloud.cdn.v20180606.models.AuthenticationTypeD`\n        """
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
        """
        :param SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        :param SignParam: 签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头\n        :type SignParam: str\n        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000\n        :type ExpireTime: int\n        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件\n        :type FileExtensions: list of str\n        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权\n        :type FilterType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AuthenticationTypeB(AbstractModel):
    """时间戳防盗链模式 B 配置（B 模式正在进行平台升级，暂不支持配置）

    """

    def __init__(self):
        """
        :param SecretKey: 计算签名的密钥
仅允许大小写字母与数字，长度 6~32 位
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000\n        :type ExpireTime: int\n        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件\n        :type FileExtensions: list of str\n        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权\n        :type FilterType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000\n        :type ExpireTime: int\n        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件\n        :type FileExtensions: list of str\n        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权\n        :type FilterType: str\n        :param TimeFormat: 时间戳进制设置
dec：十进制
hex：十六进制
注意：此字段可能返回 null，表示取不到有效值。\n        :type TimeFormat: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        :param ExpireTime: 签名过期时间设置
单位为秒，最大可设置为 630720000\n        :type ExpireTime: int\n        :param FileExtensions: 鉴权/不做鉴权的文件扩展名列表设置
如果包含字符 *  则表示所有文件\n        :type FileExtensions: list of str\n        :param FilterType: whitelist：白名单，表示对除了 FileExtensions 列表之外的所有类型进行鉴权
blacklist：黑名单，表示仅对 FileExtensions 中的类型进行鉴权\n        :type FilterType: str\n        :param SignParam: 签名参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头\n        :type SignParam: str\n        :param TimeParam: 时间戳参数名设置
仅允许大小写字母、数字或下划线，长度 1~100 位，不能以数字开头\n        :type TimeParam: str\n        :param TimeFormat: 时间戳进制设置
dec：十进制
hex：十六进制\n        :type TimeFormat: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AwsPrivateAccess(AbstractModel):
    """s3源站回源鉴权。

    """

    def __init__(self):
        """
        :param Switch: 开关，on/off。\n        :type Switch: str\n        :param AccessKey: 访问ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessKey: str\n        :param SecretKey: 密钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BandwidthAlert(AbstractModel):
    """带宽封顶配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 带宽封顶配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param BpsThreshold: 带宽封顶阈值，单位为bps
注意：此字段可能返回 null，表示取不到有效值。\n        :type BpsThreshold: int\n        :param CounterMeasure: 达到阈值后的操作
RESOLVE_DNS_TO_ORIGIN：直接回源，仅自有源站域名支持
RETURN_404：全部请求返回 404
注意：此字段可能返回 null，表示取不到有效值。\n        :type CounterMeasure: str\n        :param LastTriggerTime: 上次触发带宽封顶阈值的时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type LastTriggerTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotCookie(AbstractModel):
    """Bot cookie策略

    """

    def __init__(self):
        """
        :param Switch: on|off\n        :type Switch: str\n        :param RuleType: 规则类型，当前只有all\n        :type RuleType: str\n        :param RuleValue: 规则值，['*']\n        :type RuleValue: list of str\n        :param Action: 执行动作，monitor|intercept|redirect|captcha\n        :type Action: str\n        :param RedirectUrl: 重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。\n        :type RedirectUrl: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BotJavaScript(AbstractModel):
    """Bot js策略

    """

    def __init__(self):
        """
        :param Switch: on|off\n        :type Switch: str\n        :param RuleType: 规则类型，当前只有file\n        :type RuleType: str\n        :param RuleValue: 规则值，['html', 'htm']\n        :type RuleValue: list of str\n        :param Action: 执行动作，monitor|intercept|redirect|captcha\n        :type Action: str\n        :param RedirectUrl: 重定向时设置的重定向页面
注意：此字段可能返回 null，表示取不到有效值。\n        :type RedirectUrl: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BriefDomain(AbstractModel):
    """域名基础配置信息，含 CNAME、状态、业务类型、加速区域、创建时间、更新时间、源站配置等。

    """

    def __init__(self):
        """
        :param ResourceId: 域名 ID\n        :type ResourceId: str\n        :param AppId: 腾讯云账号 ID\n        :type AppId: int\n        :param Domain: 加速域名\n        :type Domain: str\n        :param Cname: 域名对应的 CNAME 地址\n        :type Cname: str\n        :param Status: 加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
online：已启动
offline：已关闭\n        :type Status: str\n        :param ProjectId: 项目 ID，可前往腾讯云项目管理页面查看\n        :type ProjectId: int\n        :param ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速\n        :type ServiceType: str\n        :param CreateTime: 域名创建时间\n        :type CreateTime: str\n        :param UpdateTime: 域名更新时间\n        :type UpdateTime: str\n        :param Origin: 源站配置详情\n        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`\n        :param Disable: 域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定\n        :type Disable: str\n        :param Area: 加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速\n        :type Area: str\n        :param Readonly: 域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定\n        :type Readonly: str\n        :param Product: 域名所属产品，cdn/ecdn\n        :type Product: str\n        """
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
        self.Product = None


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
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Cache(AbstractModel):
    """节点缓存过期时间配置，分为以下两种：
    + 基础版缓存过期规则配置
    + 高级版缓存过期规则配置

    """

    def __init__(self):
        """
        :param SimpleCache: 基础缓存过期时间配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type SimpleCache: :class:`tencentcloud.cdn.v20180606.models.SimpleCache`\n        :param AdvancedCache: 高级缓存过期时间配置（功能灰度中，尚未全量）
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdvancedCache: :class:`tencentcloud.cdn.v20180606.models.AdvancedCache`\n        :param RuleCache: 高级路径缓存配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleCache: list of RuleCache\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigCache(AbstractModel):
    """路径缓存缓存配置

    """

    def __init__(self):
        """
        :param Switch: 缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheTime: int\n        :param CompareMaxAge: 高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type CompareMaxAge: str\n        :param IgnoreCacheControl: 强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreCacheControl: str\n        :param IgnoreSetCookie: 当源站返回Set-Cookie头部时，节点是否缓存该头部及body
on：开启，不缓存该头部及body
off：关闭，遵循用户自定义的节点缓存规则
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreSetCookie: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigFollowOrigin(AbstractModel):
    """路径缓存遵循源站配置

    """

    def __init__(self):
        """
        :param Switch: 遵循源站配置开关
on：开启
off：关闭\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheConfigNoCache(AbstractModel):
    """路径缓存不缓存配置

    """

    def __init__(self):
        """
        :param Switch: 不缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Revalidate: 总是回源站校验
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Revalidate: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存键配置（过滤参数配置）

    """

    def __init__(self):
        """
        :param FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数过滤）
off：关闭全路径缓存（即开启参数过滤）\n        :type FullUrlCache: str\n        :param IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreCase: str\n        :param QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.QueryStringKey`\n        :param Cookie: CacheKey中包含Cookie
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cookie: :class:`tencentcloud.cdn.v20180606.models.CookieKey`\n        :param Header: CacheKey中包含请求头部
注意：此字段可能返回 null，表示取不到有效值。\n        :type Header: :class:`tencentcloud.cdn.v20180606.models.HeaderKey`\n        :param CacheTag: CacheKey中包含自定义字符串
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheTag: :class:`tencentcloud.cdn.v20180606.models.CacheTagKey`\n        :param Scheme: CacheKey中包含请求协议
注意：此字段可能返回 null，表示取不到有效值。\n        :type Scheme: :class:`tencentcloud.cdn.v20180606.models.SchemeKey`\n        :param KeyRules: 分路径缓存键配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyRules: list of KeyRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheOptResult(AbstractModel):
    """违规资源封禁/解封返回类型

    """

    def __init__(self):
        """
        :param SuccessUrls: 成功的url列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type SuccessUrls: list of str\n        :param FailUrls: 失败的url列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type FailUrls: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheTagKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: 是否使用CacheTag作为CacheKey的一部分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Value: 自定义CacheTag的值
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CappingRule(AbstractModel):
    """下行限速配置规则，最多可配置 100 条

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效\n        :type RuleType: str\n        :param RulePaths: RuleType 对应类型下的匹配内容： 
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html\n        :type RulePaths: list of str\n        :param KBpsThreshold: 下行速度值设置，单位为 KB/s\n        :type KBpsThreshold: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
或指定查询的某一具体状态码\n        :type Metric: str\n        :param DetailData: 明细数据组合\n        :type DetailData: list of TimestampData\n        :param SummarizedData: 汇总数据组合\n        :type SummarizedData: :class:`tencentcloud.cdn.v20180606.models.SummarizedData`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIp(AbstractModel):
    """IP 属性信息

    """

    def __init__(self):
        """
        :param Ip: 指定查询的 IP\n        :type Ip: str\n        :param Platform: IP 归属：
yes：节点归属于腾讯云 CDN
no：节点不属于腾讯云 CDN\n        :type Platform: str\n        :param Location: 节点所处的省份/国家
unknown 表示节点位置未知\n        :type Location: str\n        :param History: 节点上下线历史记录\n        :type History: list of CdnIpHistory\n        :param Area: 节点的所在区域
mainland：中国境内加速节点
overseas：中国境外加速节点
unknown：服务地域无法获取\n        :type Area: str\n        :param City: 节点的所在城市
注意：此字段可能返回 null，表示取不到有效值。\n        :type City: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CdnIpHistory(AbstractModel):
    """CDN 节点上下线历史记录

    """

    def __init__(self):
        """
        :param Status: 操作类型
online：节点上线
offline：节点下线\n        :type Status: str\n        :param Datetime: 操作类型对应的操作时间
当该值为 null 时表示无历史状态变更记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type Datetime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientCert(AbstractModel):
    """https 客户端证书配置

    """

    def __init__(self):
        """
        :param Certificate: 客户端证书
PEM 格式，需要进行 Base 64 编码
注意：此字段可能返回 null，表示取不到有效值。\n        :type Certificate: str\n        :param CertName: 客户端证书名称
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertName: str\n        :param ExpireTime: 证书过期时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param DeployTime: 证书颁发时间
作为入参时无需填充
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClientInfo(AbstractModel):
    """客户端信息

    """

    def __init__(self):
        """
        :param ProvName: 省份。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ProvName: str\n        :param Country: 国家。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Country: str\n        :param IspName: 运营商。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IspName: str\n        :param Ip: 客户端IP
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ip: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsLogObject(AbstractModel):
    """CLS日志搜索对象

    """

    def __init__(self):
        """
        :param TopicId: 主题ID\n        :type TopicId: str\n        :param TopicName: 主题名字\n        :type TopicName: str\n        :param Timestamp: 日志时间\n        :type Timestamp: str\n        :param Content: 日志内容\n        :type Content: str\n        :param Filename: 采集路径\n        :type Filename: str\n        :param Source: 日志来源设备\n        :type Source: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ClsSearchLogs(AbstractModel):
    """Cls日志搜索结果

    """

    def __init__(self):
        """
        :param Context: 获取更多检索结果的游标\n        :type Context: str\n        :param Listover: 搜索结果是否已经全部返回\n        :type Listover: bool\n        :param Results: 日志内容信息\n        :type Results: list of ClsLogObject\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compatibility(AbstractModel):
    """是否兼容旧版配置

    """

    def __init__(self):
        """
        :param Code: 兼容标志状态码。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Code: int\n        """
        self.Code = None


    def _deserialize(self, params):
        self.Code = params.get("Code")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Compression(AbstractModel):
    """智能压缩配置，默认对 js、html、css、xml、json、shtml、htm 后缀且大小为 256 ~ 2097152 字节的文件进行 GZIP 压缩

    """

    def __init__(self):
        """
        :param Switch: 智能压缩配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param CompressionRules: 压缩规则数组
注意：此字段可能返回 null，表示取不到有效值。\n        :type CompressionRules: list of CompressionRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CompressionRule(AbstractModel):
    """压缩规则配置，最多可设置 100 条

    """

    def __init__(self):
        """
        :param Compress: true：需要设置为 ture，启用压缩
注意：此字段可能返回 null，表示取不到有效值。\n        :type Compress: bool\n        :param FileExtensions: 根据文件后缀类型压缩
例如 jpg、txt
注意：此字段可能返回 null，表示取不到有效值。\n        :type FileExtensions: list of str\n        :param MinLength: 触发压缩的文件长度最小值，单位为字节数
注意：此字段可能返回 null，表示取不到有效值。\n        :type MinLength: int\n        :param MaxLength: 触发压缩的文件长度最大值，单位为字节数
最大可设置为 30MB
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxLength: int\n        :param Algorithms: 文件压缩算法
gzip：指定 GZIP 压缩
brotli：指定Brotli压缩
注意：此字段可能返回 null，表示取不到有效值。\n        :type Algorithms: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CookieKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: on | off 是否使用Cookie作为Cache的一部分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Value: 使用的cookie，';' 分割
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicRequest(AbstractModel):
    """CreateClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicName: 日志主题名称\n        :type TopicName: str\n        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        :param DomainAreaConfigs: 域名区域信息\n        :type DomainAreaConfigs: list of DomainAreaConfig\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateClsLogTopicResponse(AbstractModel):
    """CreateClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 主题ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopicId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TopicId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.RequestId = params.get("RequestId")


class CreateDiagnoseUrlRequest(AbstractModel):
    """CreateDiagnoseUrl请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 需诊断的url，形如：http://www.test.com/test.txt。\n        :type Url: str\n        """
        self.Url = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDiagnoseUrlResponse(AbstractModel):
    """CreateDiagnoseUrl返回参数结构体

    """

    def __init__(self):
        """
        :param DiagnoseLink: 系统生成的诊断链接，一个诊断链接最多可访问10次，有效期为24h。\n        :type DiagnoseLink: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.DiagnoseLink = None
        self.RequestId = None


    def _deserialize(self, params):
        self.DiagnoseLink = params.get("DiagnoseLink")
        self.RequestId = params.get("RequestId")


class CreateEdgePackTaskRequest(AbstractModel):
    """CreateEdgePackTask请求参数结构体

    """

    def __init__(self):
        """
        :param CosBucket: apk 所在的 cos 存储桶, 如 edgepack-xxxxxxxx\n        :type CosBucket: str\n        :param CosUriFrom: apk 源文件的存储路径, 如 /apk/xxxx.apk\n        :type CosUriFrom: str\n        :param BlockID: BlockID 的值, WALLE为1903654775(0x71777777)，VasDolly为2282837503(0x881155ff),传0或不传时默认为 WALLE 方案\n        :type BlockID: int\n        :param CosUriTo: 拓展之后的 apk 目标存储路径,如 /out/xxxx.apk\n        :type CosUriTo: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateEdgePackTaskResponse(AbstractModel):
    """CreateEdgePackTask返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateScdnDomainRequest(AbstractModel):
    """CreateScdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Waf: Web 攻击防护（WAF）配置\n        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`\n        :param Acl: 自定义防护策略配置\n        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`\n        :param CC: CC 防护配置，目前 CC 防护默认开启\n        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`\n        :param Ddos: DDOS 防护配置，目前 DDoS 防护默认开启\n        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`\n        :param Bot: BOT 防护配置\n        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnDomainResponse(AbstractModel):
    """CreateScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果，Success表示成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateScdnFailedLogTaskRequest(AbstractModel):
    """CreateScdnFailedLogTask请求参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 重试失败任务的taskID\n        :type TaskId: str\n        :param Area: 地域：mainland或overseas\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnFailedLogTaskResponse(AbstractModel):
    """CreateScdnFailedLogTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果, 
"0" -> 创建成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateScdnLogTaskRequest(AbstractModel):
    """CreateScdnLogTask请求参数结构体

    """

    def __init__(self):
        """
        :param Mode: 防护类型
Mode 映射如下：
  waf = "Web攻击"
  cc = "CC攻击"
  bot = "Bot攻击"\n        :type Mode: str\n        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间\n        :type EndTime: str\n        :param Domain: 指定域名查询, 不填默认查询全部域名\n        :type Domain: str\n        :param AttackType: 指定攻击类型, 不填默认查询全部攻击类型
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
  cookie = "Cookie指纹"\n        :type AttackType: str\n        :param DefenceMode: 指定执行动作, 不填默认查询全部执行动作
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'
  captcha = "验证码"
  redirect = "重定向"\n        :type DefenceMode: str\n        :param Ip: 不填为全部ip\n        :type Ip: str\n        :param Domains: 指定域名查询, 与 Domain 参数同时有值时使用 Domains 参数，不填默认查询全部域名，指定域名查询时最多支持同时选择 5 个域名查询\n        :type Domains: list of str\n        :param AttackTypes: 指定攻击类型查询, 与 AttackType 参数同时有值时使用 AttackTypes 参数，不填默认查询全部攻击类型\n        :type AttackTypes: list of str\n        :param Conditions: 查询条件\n        :type Conditions: list of ScdnEventLogConditions\n        :param Source: 来源产品 cdn ecdn\n        :type Source: str\n        :param Area: 地域：mainland 或 overseas\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateScdnLogTaskResponse(AbstractModel):
    """CreateScdnLogTask返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果, 
"0" -> 创建成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class CreateVerifyRecordRequest(AbstractModel):
    """CreateVerifyRecord请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 要取回的域名\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateVerifyRecordResponse(AbstractModel):
    """CreateVerifyRecord返回参数结构体

    """

    def __init__(self):
        """
        :param SubDomain: 子解析\n        :type SubDomain: str\n        :param Record: 解析值\n        :type Record: str\n        :param RecordType: 解析类型\n        :type RecordType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.SubDomain = None
        self.Record = None
        self.RecordType = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SubDomain = params.get("SubDomain")
        self.Record = params.get("Record")
        self.RecordType = params.get("RecordType")
        self.RequestId = params.get("RequestId")


class DeleteCdnDomainRequest(AbstractModel):
    """DeleteCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
域名状态需要为【已停用】\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCdnDomainResponse(AbstractModel):
    """DeleteCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteClsLogTopicRequest(AbstractModel):
    """DeleteClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param TopicId: 日志主题ID\n        :type TopicId: str\n        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteClsLogTopicResponse(AbstractModel):
    """DeleteClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteScdnDomainRequest(AbstractModel):
    """DeleteScdnDomain请求参数结构体

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
        


class DeleteScdnDomainResponse(AbstractModel):
    """DeleteScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 创建结果，Success表示成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class DescribeBillingDataRequest(AbstractModel):
    """DescribeBillingData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定起始时间为 2018-09-04 10:40:00 按小时粒度查询，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度参数不同，会进行向前取整，如指定结束时间为  2018-09-04 10:40:00 按小时粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天\n        :type EndTime: str\n        :param Interval: 时间粒度，支持模式如下：
min：1 分钟粒度，查询区间需要小于等于 24 小时
5min：5 分钟粒度，查询区间需要小于等于 31 天
hour：1 小时粒度，查询区间需要小于等于 31 天内
day：天粒度，查询区间需要大于 31 天

Area 字段为 overseas 时暂不支持1分钟粒度数据查询\n        :type Interval: str\n        :param Domain: 指定域名查询计费数据\n        :type Domain: str\n        :param Project: 指定项目 ID 查询，[前往查看项目 ID](https://console.cloud.tencent.com/project)
若 Domain 参数填充了具体域名信息，则返回该域名的计费数据，而非指定项目计费数据\n        :type Project: int\n        :param Area: 指定加速区域查询计费数据：
mainland：中国境内
overseas：中国境外
不填充时，默认为 mainland\n        :type Area: str\n        :param District: Area 为 overseas 时，指定国家/地区查询
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E7.9C.81.E4.BB.BD.E6.98.A0.E5.B0.84)
不填充时，查询所有国家/地区\n        :type District: int\n        :param Metric: 计费统计类型
flux：计费流量
bandwidth：计费带宽
默认为 bandwidth\n        :type Metric: str\n        :param Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn\n        :type Product: str\n        """
        self.StartTime = None
        self.EndTime = None
        self.Interval = None
        self.Domain = None
        self.Project = None
        self.Area = None
        self.District = None
        self.Metric = None
        self.Product = None


    def _deserialize(self, params):
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Interval = params.get("Interval")
        self.Domain = params.get("Domain")
        self.Project = params.get("Project")
        self.Area = params.get("Area")
        self.District = params.get("District")
        self.Metric = params.get("Metric")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeBillingDataResponse(AbstractModel):
    """DescribeBillingData返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 时间粒度，根据查询时传递参数指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度\n        :type Interval: str\n        :param Data: 数据明细\n        :type Data: list of ResourceBillingData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCdnDataRequest(AbstractModel):
    """DescribeCdnData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天\n        :type EndTime: str\n        :param Metric: 指定查询指标，支持的类型有：
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
支持指定具体状态码查询，若未产生过，则返回为空\n        :type Metric: str\n        :param Domains: 指定查询域名列表
最多可一次性查询 30 个加速域名明细\n        :type Domains: list of str\n        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主\n        :type Project: int\n        :param Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据\n        :type Interval: str\n        :param Detail: 多域名查询时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）\n        :type Detail: bool\n        :param Isp: 查询中国境内CDN数据时，指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定运营商查询时，不可同时指定省份、IP协议查询\n        :type Isp: int\n        :param District: 查询中国境内CDN数据时，指定省份查询，不填充表示查询所有省份
查询中国境外CDN数据时，指定国家/地区查询，不填充表示查询所有国家/地区
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)
指定（中国境内）省份查询时，不可同时指定运营商、IP协议查询\n        :type District: int\n        :param Protocol: 指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标\n        :type Protocol: str\n        :param DataSource: 指定数据源查询，白名单功能\n        :type DataSource: str\n        :param IpProtocol: 指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询
注意：非IPv6白名单用户不可指定ipv4、ipv6进行查询\n        :type IpProtocol: str\n        :param Area: 指定服务地域查询，不填充表示查询中国境内CDN数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据\n        :type Area: str\n        :param AreaType: 查询中国境外CDN数据时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据\n        :type AreaType: str\n        :param Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn\n        :type Product: str\n        """
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
        self.Product = None


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
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDataResponse(AbstractModel):
    """DescribeCdnData返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 返回数据的时间粒度，查询时指定：
min：1 分钟粒度
5min：5 分钟粒度
hour：1 小时粒度
day：天粒度\n        :type Interval: str\n        :param Data: 指定条件查询得到的数据明细\n        :type Data: list of ResourceData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCdnDomainLogsRequest(AbstractModel):
    """DescribeCdnDomainLogs请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 指定域名查询\n        :type Domain: str\n        :param StartTime: 开始时间，如 2019-09-04 00:00:00\n        :type StartTime: str\n        :param EndTime: 结束时间，如 2019-09-04 12:00:00\n        :type EndTime: str\n        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为 100，最大为 1000\n        :type Limit: int\n        :param Area: 指定区域下载日志
mainland：获取境内加速日志包下载链接
overseas：获取境外加速日志包下载链接
global：同时获取境内、境外加速日志包下载链接（分开打包）
不指定时默认为 mainland\n        :type Area: str\n        :param LogType: 指定下载日志的类型。
access：获取访问日志\n        :type LogType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnDomainLogsResponse(AbstractModel):
    """DescribeCdnDomainLogs返回参数结构体

    """

    def __init__(self):
        """
        :param DomainLogs: 日志包下载链接\n        :type DomainLogs: list of DomainLog\n        :param TotalCount: 查询到的总条数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCdnIpRequest(AbstractModel):
    """DescribeCdnIp请求参数结构体

    """

    def __init__(self):
        """
        :param Ips: 需要查询的 IP 列表\n        :type Ips: list of str\n        """
        self.Ips = None


    def _deserialize(self, params):
        self.Ips = params.get("Ips")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCdnIpResponse(AbstractModel):
    """DescribeCdnIp返回参数结构体

    """

    def __init__(self):
        """
        :param Ips: 查询的节点归属详情。\n        :type Ips: list of CdnIp\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCdnOriginIpRequest(AbstractModel):
    """DescribeCdnOriginIp请求参数结构体

    """


class DescribeCdnOriginIpResponse(AbstractModel):
    """DescribeCdnOriginIp返回参数结构体

    """

    def __init__(self):
        """
        :param Ips: 回源节点IP详情。\n        :type Ips: list of OriginIp\n        :param TotalCount: 回源节点IP总个数。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeCertDomainsRequest(AbstractModel):
    """DescribeCertDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Cert: PEM格式证书Base64编码后的字符串\n        :type Cert: str\n        :param CertId: 托管证书ID，Cert和CertId不能均未空，都填写时以CerId为准。\n        :type CertId: str\n        :param Product: 域名所属产品，cdn或ecdn，默认cdn。\n        :type Product: str\n        """
        self.Cert = None
        self.CertId = None
        self.Product = None


    def _deserialize(self, params):
        self.Cert = params.get("Cert")
        self.CertId = params.get("CertId")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertDomainsResponse(AbstractModel):
    """DescribeCertDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 已接入CDN的域名列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domains: list of str\n        :param CertifiedDomains: 已配置证书的CDN域名列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertifiedDomains: list of str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Domains = None
        self.CertifiedDomains = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Domains = params.get("Domains")
        self.CertifiedDomains = params.get("CertifiedDomains")
        self.RequestId = params.get("RequestId")


class DescribeDiagnoseReportRequest(AbstractModel):
    """DescribeDiagnoseReport请求参数结构体

    """

    def __init__(self):
        """
        :param ReportId: 报告ID\n        :type ReportId: str\n        """
        self.ReportId = None


    def _deserialize(self, params):
        self.ReportId = params.get("ReportId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDiagnoseReportResponse(AbstractModel):
    """DescribeDiagnoseReport返回参数结构体

    """

    def __init__(self):
        """
        :param BaskInfo: 诊断报告基础信息\n        :type BaskInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param CnameInfo: CNAME检测信息\n        :type CnameInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param ClientInfo: 客户端检测信息\n        :type ClientInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param DnsInfo: DNS检测信息\n        :type DnsInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param NetworkInfo: 网络检测信息\n        :type NetworkInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param OcNodeInfo: 边缘节点检测信息\n        :type OcNodeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param MidNodeInfo: 中间源节点检测信息\n        :type MidNodeInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param OriginInfo: 源站检测信息\n        :type OriginInfo: :class:`tencentcloud.cdn.v20180606.models.DiagnoseData`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDistrictIspDataRequest(AbstractModel):
    """DescribeDistrictIspData请求参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表，最多支持20个域名\n        :type Domains: list of str\n        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
支持近 60 天内的数据查询，每次查询时间区间为 3 小时\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
结束时间与起始时间区间最大为 3 小时\n        :type EndTime: str\n        :param Metric: 指定查询指标，支持:
bandwidth：带宽，单位为 bps
request：请求数，单位为 次\n        :type Metric: str\n        :param Districts: 指定省份查询，不填充表示查询所有省份
省份、国家/地区编码可以查看 [省份编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\n        :type Districts: list of int\n        :param Isps: 指定运营商查询，不填充表示查询所有运营商
运营商编码可以查看 [运营商编码映射](https://cloud.tencent.com/document/product/228/6316#.E5.8C.BA.E5.9F.9F-.2F-.E8.BF.90.E8.90.A5.E5.95.86.E6.98.A0.E5.B0.84.E8.A1.A8)\n        :type Isps: list of int\n        :param Protocol: 指定协议查询，不填充表示查询所有协议
all：所有协议
http：指定查询 HTTP 对应指标
https：指定查询 HTTPS 对应指标\n        :type Protocol: str\n        :param IpProtocol: 指定IP协议查询，不填充表示查询所有协议
all：所有协议
ipv4：指定查询 ipv4 对应指标
ipv6：指定查询 ipv6 对应指标
指定IP协议查询时，不可同时指定省份、运营商查询\n        :type IpProtocol: str\n        :param Interval: 时间粒度，支持以下几种模式（默认5min）：
min：1 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过10分钟，可返回 1 分钟粒度明细数据
5min：5 分钟粒度，支持近 60 天内的数据查询，每次查询时间区间不超过3 小时，可返回 5 分钟粒度明细数据\n        :type Interval: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDistrictIspDataResponse(AbstractModel):
    """DescribeDistrictIspData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 地区运营商数据明细
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of DistrictIspInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000\n        :type Limit: int\n        :param Filters: 查询条件过滤器，复杂类型\n        :type Filters: list of DomainFilter\n        :param Sort: 排序规则\n        :type Sort: :class:`tencentcloud.cdn.v20180606.models.Sort`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsConfigResponse(AbstractModel):
    """DescribeDomainsConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表\n        :type Domains: list of DetailDomain\n        :param TotalNumber: 符合查询条件的域名总数
用于分页查询\n        :type TotalNumber: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为 100，最大可设置为 1000\n        :type Limit: int\n        :param Filters: 查询条件过滤器，复杂类型\n        :type Filters: list of DomainFilter\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainsResponse(AbstractModel):
    """DescribeDomains返回参数结构体

    """

    def __init__(self):
        """
        :param Domains: 域名列表\n        :type Domains: list of BriefDomain\n        :param TotalNumber: 符合查询条件的域名总数
用于分页查询\n        :type TotalNumber: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeImageConfigRequest(AbstractModel):
    """DescribeImageConfig请求参数结构体

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
        


class DescribeImageConfigResponse(AbstractModel):
    """DescribeImageConfig返回参数结构体

    """

    def __init__(self):
        """
        :param WebpAdapter: WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`\n        :param TpgAdapter: TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`\n        :param GuetzliAdapter: GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 加速域名\n        :type Domain: str\n        :param Layer: 节点类型：
edge：表示边缘节点
last：表示回源层节点
不填充情况下，默认返回边缘节点信息\n        :type Layer: str\n        :param Area: 查询区域：
mainland: 国内节点
overseas: 海外节点
global: 全球节点\n        :type Area: str\n        :param Segment: 是否以IP段的格式返回。\n        :type Segment: bool\n        """
        self.Domain = None
        self.Layer = None
        self.Area = None
        self.Segment = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        self.Layer = params.get("Layer")
        self.Area = params.get("Area")
        self.Segment = params.get("Segment")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpStatusResponse(AbstractModel):
    """DescribeIpStatus返回参数结构体

    """

    def __init__(self):
        """
        :param Ips: 节点列表\n        :type Ips: list of IpStatus\n        :param TotalCount: 节点总个数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeIpVisitRequest(AbstractModel):
    """DescribeIpVisit请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:10，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:40:00\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:10，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:10 在按 5 分钟的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:40:00\n        :type EndTime: str\n        :param Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细\n        :type Domains: list of str\n        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主\n        :type Project: int\n        :param Interval: 时间粒度，支持以下几种模式：
5min：5 分钟粒度，查询时间区间 24 小时内，默认返回 5 分钟粒度活跃用户数
day：天粒度，查询时间区间大于 1 天时，默认返回天粒度活跃用户数\n        :type Interval: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeIpVisitResponse(AbstractModel):
    """DescribeIpVisit返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 数据统计的时间粒度，支持5min,  day，分别表示5分钟，1天的时间粒度。\n        :type Interval: str\n        :param Data: 各个资源的回源数据详情。\n        :type Data: list of ResourceData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeMapInfoRequest(AbstractModel):
    """DescribeMapInfo请求参数结构体

    """

    def __init__(self):
        """
        :param Name: 映射查询类别：
isp：运营商映射查询
district：省份（中国境内）、国家/地区（中国境外）映射查询\n        :type Name: str\n        """
        self.Name = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeMapInfoResponse(AbstractModel):
    """DescribeMapInfo返回参数结构体

    """

    def __init__(self):
        """
        :param MapInfoList: 映射关系数组。\n        :type MapInfoList: list of MapInfo\n        :param ServerRegionRelation: 服务端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerRegionRelation: list of RegionMapRelation\n        :param ClientRegionRelation: 客户端区域id和子区域id的映射关系。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientRegionRelation: list of RegionMapRelation\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeOriginDataRequest(AbstractModel):
    """DescribeOriginData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的第一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间
根据指定时间粒度不同，会进行向前归整，如 2018-09-04 10:40:00 在按 1 小时的时间粒度查询时，返回的最后一个数据对应时间点为 2018-09-04 10:00:00
起始时间与结束时间间隔小于等于 90 天\n        :type EndTime: str\n        :param Metric: 指定查询指标，支持的类型有：
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
支持指定具体状态码查询，若未产生过，则返回为空\n        :type Metric: str\n        :param Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细\n        :type Domains: list of str\n        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，最多可一次性查询 30 个加速域名明细
若填充了具体域名信息，以域名为主\n        :type Project: int\n        :param Interval: 时间粒度，支持以下几种模式：
min：1 分钟粒度，指定查询区间 24 小时内（含 24 小时），可返回 1 分钟粒度明细数据（指定查询服务地域为中国境外时不支持 1 分钟粒度）
5min：5 分钟粒度，指定查询区间 31 天内（含 31 天），可返回 5 分钟粒度明细数据
hour：1 小时粒度，指定查询区间 31 天内（含 31 天），可返回 1 小时粒度明细数据
day：天粒度，指定查询区间大于 31 天，可返回天粒度明细数据\n        :type Interval: str\n        :param Detail: Domains 传入多个时，默认（false)返回多个域名的汇总数据
可按需指定为 true，返回每一个 Domain 的明细数据（statusCode 指标暂不支持）\n        :type Detail: bool\n        :param Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeOriginDataResponse(AbstractModel):
    """DescribeOriginData返回参数结构体

    """

    def __init__(self):
        """
        :param Interval: 数据统计的时间粒度，支持min, 5min, hour, day，分别表示1分钟，5分钟，1小时和1天的时间粒度。\n        :type Interval: str\n        :param Data: 各个资源的回源数据详情。\n        :type Data: list of ResourceOriginData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePayTypeRequest(AbstractModel):
    """DescribePayType请求参数结构体

    """

    def __init__(self):
        """
        :param Area: 指定服务地域查询
mainland：境内计费方式查询
overseas：境外计费方式查询
未填充时默认为 mainland\n        :type Area: str\n        :param Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn\n        :type Product: str\n        """
        self.Area = None
        self.Product = None


    def _deserialize(self, params):
        self.Area = params.get("Area")
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePayTypeResponse(AbstractModel):
    """DescribePayType返回参数结构体

    """

    def __init__(self):
        """
        :param PayType: 计费类型：
flux：流量计费
bandwidth：带宽计费
request：请求数计费
日结计费方式切换时，若当日产生消耗，则此字段表示第二天即将生效的计费方式，若未产生消耗，则表示已经生效的计费方式。\n        :type PayType: str\n        :param BillingCycle: 计费周期：
day：日结计费
month：月结计费\n        :type BillingCycle: str\n        :param StatType: monthMax：日峰值月平均，月结模式
day95：日 95 带宽，月结模式
month95：月95带宽，月结模式
sum：总流量/总请求数，日结或月结模式
max：峰值带宽，日结模式\n        :type StatType: str\n        :param RegionType: 境外计费类型：
all：全地区统一计费
multiple：分地区计费\n        :type RegionType: str\n        :param CurrentPayType: 当前生效计费类型：
flux：流量计费
bandwidth：带宽计费
request：请求数计费\n        :type CurrentPayType: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota请求参数结构体

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回参数结构体

    """

    def __init__(self):
        """
        :param UrlPurge: URL刷新用量及配额。\n        :type UrlPurge: list of Quota\n        :param PathPurge: 目录刷新用量及配额。\n        :type PathPurge: list of Quota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        """
        :param PurgeType: 指定刷新类型查询
url：url 刷新记录
path：目录刷新记录\n        :type PurgeType: str\n        :param StartTime: 根据时间区间查询时，填充开始时间，如 2018-08-08 00:00:00\n        :type StartTime: str\n        :param EndTime: 根据时间区间查询时，填充结束时间，如 2018-08-08 23:59:59\n        :type EndTime: str\n        :param TaskId: 根据任务 ID 查询时，填充任务 ID
查询时任务 ID 与起始时间必须填充一项\n        :type TaskId: str\n        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为 20\n        :type Limit: int\n        :param Keyword: 支持域名过滤，或 http(s):// 开头完整 URL 过滤\n        :type Keyword: str\n        :param Status: 指定任务状态查询
fail：刷新失败
done：刷新成功
process：刷新中\n        :type Status: str\n        :param Area: 指定刷新地域查询
mainland：境内
overseas：境外
global：全球\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePurgeTasksResponse(AbstractModel):
    """DescribePurgeTasks返回参数结构体

    """

    def __init__(self):
        """
        :param PurgeLogs: 详细刷新记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type PurgeLogs: list of PurgeTask\n        :param TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePushQuotaRequest(AbstractModel):
    """DescribePushQuota请求参数结构体

    """


class DescribePushQuotaResponse(AbstractModel):
    """DescribePushQuota返回参数结构体

    """

    def __init__(self):
        """
        :param UrlPush: Url预热用量及配额。\n        :type UrlPush: list of Quota\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribePushTasksRequest(AbstractModel):
    """DescribePushTasks请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 开始时间，如2018-08-08 00:00:00。\n        :type StartTime: str\n        :param EndTime: 结束时间，如2018-08-08 23:59:59。\n        :type EndTime: str\n        :param TaskId: 指定任务 ID 查询
TaskId 和起始时间必须指定一项\n        :type TaskId: str\n        :param Keyword: 查询关键字，请输入域名或 http(s):// 开头完整 URL\n        :type Keyword: str\n        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为 20\n        :type Limit: int\n        :param Area: 指定地区查询预热纪录
mainland：境内
overseas：境外
global：全球\n        :type Area: str\n        :param Status: 指定任务状态查询
fail：预热失败
done：预热成功
process：预热中
invalid: 预热无效(源站返回4xx或5xx状态码)\n        :type Status: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribePushTasksResponse(AbstractModel):
    """DescribePushTasks返回参数结构体

    """

    def __init__(self):
        """
        :param PushLogs: 预热历史记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type PushLogs: list of PushTask\n        :param TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeReportDataRequest(AbstractModel):
    """DescribeReportData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天\n        :type StartTime: str\n        :param EndTime: 查询结束时间：yyyy-MM-dd
当报表类型为daily，起始时间和结束时间必须为同一天
当报表类型为weekly，起始时间须为周一，结束时间须为同一周的周日
当报表类型为monthly，起始时间须为自然月第一天，即1号，结束时间须为该自然月最后一天\n        :type EndTime: str\n        :param ReportType: 报表类型
daily：日报表
weekly：周报表（周一至周日）
monthly：月报表（自然月）\n        :type ReportType: str\n        :param Area: 域名加速区域
mainland：中国境内
overseas：中国境外\n        :type Area: str\n        :param Offset: 偏移量，默认0。\n        :type Offset: int\n        :param Limit: 数据个数，默认1000。\n        :type Limit: int\n        :param Project: 按项目ID筛选\n        :type Project: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeReportDataResponse(AbstractModel):
    """DescribeReportData返回参数结构体

    """

    def __init__(self):
        """
        :param DomainReport: 域名维度数据详情\n        :type DomainReport: list of ReportData\n        :param ProjectReport: 项目维度数据详情\n        :type ProjectReport: list of ReportData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeScdnConfigRequest(AbstractModel):
    """DescribeScdnConfig请求参数结构体

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
        


class DescribeScdnConfigResponse(AbstractModel):
    """DescribeScdnConfig返回参数结构体

    """

    def __init__(self):
        """
        :param Acl: 自定义防护策略配置\n        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`\n        :param Waf: Web 攻击防护（WAF）配置\n        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`\n        :param CC: CC 防护配置\n        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`\n        :param Ddos: DDOS 防护配置\n        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`\n        :param Bot: BOT 防护配置\n        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`\n        :param Status: 当前状态，取值online | offline
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeScdnTopDataRequest(AbstractModel):
    """DescribeScdnTopData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始时间，如：2018-09-04 10:40:00，返回结果大于等于指定时间\n        :type StartTime: str\n        :param EndTime: 查询结束时间，如：2018-09-04 10:40:00，返回结果小于等于指定时间\n        :type EndTime: str\n        :param Mode: 查询的SCDN TOP攻击数据类型：
waf：Web 攻击防护TOP数据\n        :type Mode: str\n        :param Metric: 排序对象，支持以下几种形式：
url：攻击目标 url 排序
ip：攻击源 IP 排序
attackType：攻击类型排序\n        :type Metric: str\n        :param Filter: 排序使用的指标名称：
request：请求次数\n        :type Filter: str\n        :param Domain: 指定域名查询\n        :type Domain: str\n        :param AttackType: 指定攻击类型, 仅 Mode=waf 时有效
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
  malicious_file_upload= '恶意文件上传'\n        :type AttackType: str\n        :param DefenceMode: 指定防御模式,仅 Mode=waf 时有效
不填则查询所有防御模式的数据总和
DefenceMode 映射如下：
  observe = '观察模式'
  intercept = '拦截模式'\n        :type DefenceMode: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeScdnTopDataResponse(AbstractModel):
    """DescribeScdnTopData返回参数结构体

    """

    def __init__(self):
        """
        :param TopTypeData: WAF 攻击类型统计
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopTypeData: list of ScdnTypeData\n        :param TopIpData: TOP 攻击源 IP 统计
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopIpData: list of ScdnTopData\n        :param Mode: 查询的SCDN类型，当前仅支持 waf\n        :type Mode: str\n        :param TopUrlData: TOP URL 统计
注意：此字段可能返回 null，表示取不到有效值。\n        :type TopUrlData: list of ScdnTopUrlData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeTrafficPackagesRequest(AbstractModel):
    """DescribeTrafficPackages请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询起始地址，默认 0\n        :type Offset: int\n        :param Limit: 分页查询记录个数，默认100，最大1000\n        :type Limit: int\n        """
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
        


class DescribeTrafficPackagesResponse(AbstractModel):
    """DescribeTrafficPackages返回参数结构体

    """

    def __init__(self):
        """
        :param TotalCount: 流量包总个数\n        :type TotalCount: int\n        :param TrafficPackages: 流量包详情\n        :type TrafficPackages: list of TrafficPackage\n        :param ExpiringCount: 即将过期的流量包个数（7天内）\n        :type ExpiringCount: int\n        :param EnabledCount: 有效流量包个数\n        :type EnabledCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DescribeUrlViolationsRequest(AbstractModel):
    """DescribeUrlViolations请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为 100\n        :type Limit: int\n        :param Domains: 指定的域名查询\n        :type Domains: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUrlViolationsResponse(AbstractModel):
    """DescribeUrlViolations返回参数结构体

    """

    def __init__(self):
        """
        :param UrlRecordList: 违规 URL 详情
注意：此字段可能返回 null，表示取不到有效值。\n        :type UrlRecordList: list of ViolationUrl\n        :param TotalCount: 记录总数，用于分页\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class DetailDomain(AbstractModel):
    """加速域名全量配置信息

    """

    def __init__(self):
        """
        :param ResourceId: 域名 ID\n        :type ResourceId: str\n        :param AppId: 腾讯云账号ID\n        :type AppId: int\n        :param Domain: 加速域名\n        :type Domain: str\n        :param Cname: 域名对应的 CNAME 地址
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cname: str\n        :param Status: 加速服务状态
rejected：域名审核未通过，域名备案过期/被注销导致
processing：部署中
online：已启动
offline：已关闭\n        :type Status: str\n        :param ProjectId: 项目 ID，可前往腾讯云项目管理页面查看\n        :type ProjectId: int\n        :param ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速\n        :type ServiceType: str\n        :param CreateTime: 域名创建时间\n        :type CreateTime: str\n        :param UpdateTime: 域名更新时间\n        :type UpdateTime: str\n        :param Origin: 源站配置\n        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`\n        :param IpFilter: IP 黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`\n        :param IpFreqLimit: IP 访问限频配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`\n        :param StatusCodeCache: 状态码缓存配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`\n        :param Compression: 智能压缩配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`\n        :param BandwidthAlert: 带宽封顶配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`\n        :param RangeOriginPull: Range 回源配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`\n        :param FollowRedirect: 301/302 回源自动跟随配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`\n        :param ErrorPage: 自定义错误页面配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`\n        :param RequestHeader: 自定义请求头部配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`\n        :param ResponseHeader: 自定义响应头部配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`\n        :param DownstreamCapping: 单链接下行限速配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`\n        :param CacheKey: 带参/不带参缓存配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`\n        :param ResponseHeaderCache: 源站头部缓存配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`\n        :param VideoSeek: 视频拖拽配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`\n        :param Cache: 节点缓存过期规则配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`\n        :param OriginPullOptimization: 跨国链路优化配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`\n        :param Https: Https 加速相关配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`\n        :param Authentication: 时间戳防盗链配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`\n        :param Seo: SEO 优化配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`\n        :param Disable: 域名封禁状态
normal：正常状态
overdue：账号欠费导致域名关闭，充值完成后可自行启动加速服务
malicious：域名出现恶意行为，强制关闭加速服务
ddos：域名被大规模 DDoS 攻击，关闭加速服务
idle：域名超过 90 天内无任何操作、数据产生，判定为不活跃域名自动关闭加速服务，可自行启动加速服务
unlicensed：域名未备案/备案注销，自动关闭加速服务，备案完成后可自行启动加速服务
capping：触发配置的带宽阈值上限
readonly：域名存在特殊配置，被锁定
注意：此字段可能返回 null，表示取不到有效值。\n        :type Disable: str\n        :param ForceRedirect: 访问协议强制跳转配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`\n        :param Referer: Referer 防盗链配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`\n        :param MaxAge: 浏览器缓存过期规则配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`\n        :param Ipv6: Ipv6 回源配置（功能灰度中，敬请期待）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6: :class:`tencentcloud.cdn.v20180606.models.Ipv6`\n        :param Compatibility: 是否兼容旧版本配置（内部兼容性字段）
注意：此字段可能返回 null，表示取不到有效值。\n        :type Compatibility: :class:`tencentcloud.cdn.v20180606.models.Compatibility`\n        :param SpecificConfig: 区域特殊配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`\n        :param Area: 加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速
注意：此字段可能返回 null，表示取不到有效值。\n        :type Area: str\n        :param Readonly: 域名锁定状态
normal：未锁定
mainland：中国境内锁定
overseas：中国境外锁定
global：全球锁定
注意：此字段可能返回 null，表示取不到有效值。\n        :type Readonly: str\n        :param OriginPullTimeout: 回源超时配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`\n        :param AwsPrivateAccess: 回源S3鉴权配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`\n        :param SecurityConfig: Scdn配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecurityConfig: :class:`tencentcloud.cdn.v20180606.models.SecurityConfig`\n        :param ImageOptimization: ImageOptimization配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ImageOptimization: :class:`tencentcloud.cdn.v20180606.models.ImageOptimization`\n        :param UserAgentFilter: UA黑白名单配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`\n        :param AccessControl: 访问控制
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`\n        :param Advance: 是否支持高级配置项
on：支持
off：不支持
注意：此字段可能返回 null，表示取不到有效值。\n        :type Advance: str\n        :param UrlRedirect: URL重定向配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`\n        :param AccessPort: 访问端口配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessPort: list of int\n        :param Tag: 标签配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Tag: list of Tag\n        :param AdvancedAuthentication: 时间戳防盗链高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`\n        :param OriginAuthentication: 回源鉴权高级配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`\n        :param Ipv6Access: Ipv6访问配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`\n        :param AdvanceSet: 高级配置集合。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AdvanceSet: list of AdvanceConfig\n        :param OfflineCache: 离线缓存
注意：此字段可能返回 null，表示取不到有效值。\n        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`\n        :param OriginCombine: 合并回源
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`\n        :param PostMaxSize: POST上传配置项
注意：此字段可能返回 null，表示取不到有效值。\n        :type PostMaxSize: :class:`tencentcloud.cdn.v20180606.models.PostSize`\n        :param Quic: Quic配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`\n        :param OssPrivateAccess: 回源OSS私有鉴权
注意：此字段可能返回 null，表示取不到有效值。\n        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`\n        :param WebSocket: WebSocket配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`\n        """
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
        self.OssPrivateAccess = None
        self.WebSocket = None


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
        if params.get("OssPrivateAccess") is not None:
            self.OssPrivateAccess = OssPrivateAccess()
            self.OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseData(AbstractModel):
    """诊断报告内容数据

    """

    def __init__(self):
        """
        :param Data: 诊断报告内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type Data: list of DiagnoseUnit\n        :param Status: 当前诊断项是否正常。
"ok"：正常
"error"：异常
"warning"："警告"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseInfo(AbstractModel):
    """诊断信息

    """

    def __init__(self):
        """
        :param DiagnoseUrl: 待诊断的URL。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnoseUrl: str\n        :param DiagnoseLink: 由系统生成的诊断链接。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnoseLink: str\n        :param CreateTime: 诊断创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param ExpireDate: 诊断链接过期时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireDate: str\n        :param VisitCount: 诊断链接当前访问次数，一个诊断链接最多可访问10次。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VisitCount: int\n        :param ClientList: 访问诊断链接的客户端简易信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientList: list of DiagnoseList\n        :param Area: 域名加速区域
注意：此字段可能返回 null，表示取不到有效值。\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseList(AbstractModel):
    """客户端访问诊断URL信息列表

    """

    def __init__(self):
        """
        :param DiagnoseTag: 诊断任务标签。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DiagnoseTag: str\n        :param ReportId: 报告ID，用于获取详细诊断报告。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReportId: str\n        :param ClientInfo: 客户端信息。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientInfo: list of ClientInfo\n        :param FinalDiagnose: 最终诊断结果。
-1：已提交
0  ：检测中
1  ：检测正常
2  ： 检测异常
3  ： 诊断页面异常关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type FinalDiagnose: int\n        :param CreateTime: 诊断任务创建时间。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DiagnoseUnit(AbstractModel):
    """诊断报告单元信息

    """

    def __init__(self):
        """
        :param Key: 内容单元英文名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Key: str\n        :param KeyText: 内容单元中文名称。
注意：此字段可能返回 null，表示取不到有效值。\n        :type KeyText: str\n        :param Value: 报告内容。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        :param ValueText: 报告内容。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ValueText: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesRequest(AbstractModel):
    """DisableCaches请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 禁用的 URL 列表（分协议生效，必须包含http://或https://）
每次最多可提交 100 条，每日最多可提交 3000 条\n        :type Urls: list of str\n        """
        self.Urls = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableCachesResponse(AbstractModel):
    """DisableCaches返回参数结构体

    """

    def __init__(self):
        """
        :param CacheOptResult: 提交结果
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`\n        :param TaskId: 任务ID
注意：此字段可能返回 null，表示取不到有效值。\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CacheOptResult = None
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class DisableClsLogTopicRequest(AbstractModel):
    """DisableClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param TopicId: 日志主题ID\n        :type TopicId: str\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DisableClsLogTopicResponse(AbstractModel):
    """DisableClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DistrictIspInfo(AbstractModel):
    """地区运营商明细数据

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Protocol: 协议类型\n        :type Protocol: str\n        :param IpProtocol: IP协议类型\n        :type IpProtocol: str\n        :param StartTime: 起始时间\n        :type StartTime: str\n        :param EndTime: 结束时间\n        :type EndTime: str\n        :param Interval: 时间间隔，单位为分钟\n        :type Interval: int\n        :param Metric: 指标名称\n        :type Metric: str\n        :param District: 地区ID\n        :type District: int\n        :param Isp: 运营商ID\n        :type Isp: int\n        :param DataPoints: 指标数据点\n        :type DataPoints: list of int non-negative\n        :param DistrictName: 地区名称\n        :type DistrictName: str\n        :param IspName: 运营商名称\n        :type IspName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAreaConfig(AbstractModel):
    """域名地区配置

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Area: 地区列表，其中元素可为mainland/overseas\n        :type Area: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
- domainType：主源站类型，cname表示自有源，cos表示cos接入，third_party表示第三方对象存储。
- fullUrlCache：全路径缓存，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源协议类型，支持http，follow或https。
- tagKey：标签键。\n        :type Name: str\n        :param Value: 过滤字段值。\n        :type Value: list of str\n        :param Fuzzy: 是否启用模糊查询，仅支持过滤字段名为origin，domain。
模糊查询时，Value长度最大为1，否则Value长度最大为5。\n        :type Fuzzy: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainLog(AbstractModel):
    """日志包下载链接详情

    """

    def __init__(self):
        """
        :param StartTime: 日志包起始时间\n        :type StartTime: str\n        :param EndTime: 日志包结束时间\n        :type EndTime: str\n        :param LogPath: 日志包下载链接\n        :type LogPath: str\n        :param Area: 日志包对应加速区域
mainland：境内
overseas：境外\n        :type Area: str\n        :param LogName: 日志包文件名\n        :type LogName: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DownstreamCapping(AbstractModel):
    """单链接下行限速配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 下行速度配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param CappingRules: 下行限速规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type CappingRules: list of CappingRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateDomainConfigRequest(AbstractModel):
    """DuplicateDomainConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 新增域名\n        :type Domain: str\n        :param ReferenceDomain: 被拷贝配置的域名\n        :type ReferenceDomain: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DuplicateDomainConfigResponse(AbstractModel):
    """DuplicateDomainConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class EnableCachesRequest(AbstractModel):
    """EnableCaches请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: 解封 URL 列表\n        :type Urls: list of str\n        :param Date: URL封禁日期\n        :type Date: str\n        """
        self.Urls = None
        self.Date = None


    def _deserialize(self, params):
        self.Urls = params.get("Urls")
        self.Date = params.get("Date")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableCachesResponse(AbstractModel):
    """EnableCaches返回参数结构体

    """

    def __init__(self):
        """
        :param CacheOptResult: 结果列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheOptResult: :class:`tencentcloud.cdn.v20180606.models.CacheOptResult`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.CacheOptResult = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CacheOptResult") is not None:
            self.CacheOptResult = CacheOptResult()
            self.CacheOptResult._deserialize(params.get("CacheOptResult"))
        self.RequestId = params.get("RequestId")


class EnableClsLogTopicRequest(AbstractModel):
    """EnableClsLogTopic请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param TopicId: 日志主题ID\n        :type TopicId: str\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EnableClsLogTopicResponse(AbstractModel):
    """EnableClsLogTopic返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ErrorPage(AbstractModel):
    """状态码重定向配置，默认为关闭状态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 状态码重定向配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param PageRules: 状态码重定向规则配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type PageRules: list of ErrorPageRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ErrorPageRule(AbstractModel):
    """状态码重定向规则配置

    """

    def __init__(self):
        """
        :param StatusCode: 状态码
支持 400、403、404、500\n        :type StatusCode: int\n        :param RedirectCode: 重定向状态码设置
支持 301 或 302\n        :type RedirectCode: int\n        :param RedirectUrl: 重定向 URL
需要为完整跳转路径，如 https://www.test.com/error.html\n        :type RedirectUrl: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FollowRedirect(AbstractModel):
    """回源 301/302 状态码自动跟随配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 回源跟随开关
on：开启
off：关闭\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """访问协议强制跳转配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 访问强制跳转配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param RedirectType: 访问强制跳转类型
http：强制 http 跳转
https：强制 https 跳转
注意：此字段可能返回 null，表示取不到有效值。\n        :type RedirectType: str\n        :param RedirectStatusCode: 强制跳转时返回状态码 
支持 301、302
注意：此字段可能返回 null，表示取不到有效值。\n        :type RedirectStatusCode: int\n        :param CarryHeaders: 强制跳转时是否返回增加的头部。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CarryHeaders: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsRequest(AbstractModel):
    """GetDisableRecords请求参数结构体

    """

    def __init__(self):
        """
        :param Url: 指定 URL 查询\n        :type Url: str\n        :param StartTime: 开始时间，如：2018-12-12 10:24:00。\n        :type StartTime: str\n        :param EndTime: 结束时间，如：2018-12-14 10:24:00。\n        :type EndTime: str\n        :param Status: URL 当前状态
disable：当前仍为禁用状态，访问返回 403
enable：当前为可用状态，已解禁，可正常访问\n        :type Status: str\n        :param Offset: 分页查询偏移量，默认为 0\n        :type Offset: int\n        :param Limit: 分页查询限制数目，默认为20。\n        :type Limit: int\n        :param TaskId: 任务ID，任务ID和起始时间需要至少填写一项。\n        :type TaskId: str\n        """
        self.Url = None
        self.StartTime = None
        self.EndTime = None
        self.Status = None
        self.Offset = None
        self.Limit = None
        self.TaskId = None


    def _deserialize(self, params):
        self.Url = params.get("Url")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Status = params.get("Status")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.TaskId = params.get("TaskId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GetDisableRecordsResponse(AbstractModel):
    """GetDisableRecords返回参数结构体

    """

    def __init__(self):
        """
        :param UrlRecordList: 封禁历史记录
注意：此字段可能返回 null，表示取不到有效值。\n        :type UrlRecordList: list of UrlRecord\n        :param TotalCount: 任务总数，用于分页
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class GuetzliAdapter(AbstractModel):
    """图片优化-GuetzliAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 开关，"on/off"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HeaderKey(AbstractModel):
    """组成CacheKey

    """

    def __init__(self):
        """
        :param Switch: 是否组成Cachekey
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Value: 组成CacheKey的header数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Hsts(AbstractModel):
    """HSTS 配置。

    """

    def __init__(self):
        """
        :param Switch: 是否开启，on或off。\n        :type Switch: str\n        :param MaxAge: MaxAge数值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxAge: int\n        :param IncludeSubDomains: 是否包含子域名，on或off。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IncludeSubDomains: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderPathRule(AbstractModel):
    """Http 头部设置规则，最多可设置 100 条

    """

    def __init__(self):
        """
        :param HeaderMode: http 头部设置方式
set：设置。变更指定头部参数的取值为设置后的值；若设置的头部不存在，则会增加该头部；若存在多个重复的头部参数，则会全部变更，同时合并为一个头部。
del：删除。删除指定的头部参数
add：增加。增加指定的头部参数，默认允许重复添加，即重复添加相同的头部（注：重复添加可能会影响浏览器响应，请优先使用set操作）
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeaderMode: str\n        :param HeaderName: http 头部名称，最多可设置 100 个字符
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeaderName: str\n        :param HeaderValue: http 头部值，最多可设置 1000 个字符
Mode 为 del 时非必填
Mode 为 add/set 时必填
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeaderValue: str\n        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleType: str\n        :param RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。\n        :type RulePaths: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderRule(AbstractModel):
    """http头部设置规则。

    """

    def __init__(self):
        """
        :param HeaderMode: http头部设置方式，支持add，set或del，分别表示新增，设置或删除头部。\n        :type HeaderMode: str\n        :param HeaderName: http头部名称。\n        :type HeaderName: str\n        :param HeaderValue: http头部值。\n        :type HeaderValue: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Https(AbstractModel):
    """域名 https 加速配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: https 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Http2: http2 配置开关
on：开启
off：关闭
初次启用 https 加速会默认开启 http2 配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Http2: str\n        :param OcspStapling: OCSP 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type OcspStapling: str\n        :param VerifyClient: 客户端证书校验功能
on：开启
off：关闭
默认为关闭状态，开启时需要上传客户端证书信息，该配置项目前在灰度中，尚未全量
注意：此字段可能返回 null，表示取不到有效值。\n        :type VerifyClient: str\n        :param CertInfo: 服务端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertInfo: :class:`tencentcloud.cdn.v20180606.models.ServerCert`\n        :param ClientCertInfo: 客户端证书配置信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type ClientCertInfo: :class:`tencentcloud.cdn.v20180606.models.ClientCert`\n        :param Spdy: Spdy 配置开关
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type Spdy: str\n        :param SslStatus: https 证书部署状态
closed：已关闭
deploying：部署中
deployed：部署成功
failed：部署失败
注意：此字段可能返回 null，表示取不到有效值。\n        :type SslStatus: str\n        :param Hsts: Hsts配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Hsts: :class:`tencentcloud.cdn.v20180606.models.Hsts`\n        :param TlsVersion: Tls版本设置，仅支持部分Advance域名，支持设置 TLSv1, TLSV1.1, TLSV1.2, TLSv1.3，修改时必须开启连续的版本
注意：此字段可能返回 null，表示取不到有效值。\n        :type TlsVersion: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ImageOptimization(AbstractModel):
    """ImageOptimization配置

    """

    def __init__(self):
        """
        :param WebpAdapter: WebpAdapter配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`\n        :param TpgAdapter: TpgAdapter配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`\n        :param GuetzliAdapter: GuetzliAdapter配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP 黑白名单配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: IP 黑白名单配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param FilterType: IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterType: str\n        :param Filters: IP 黑白名单列表
支持 X.X.X.X 形式 IP，或 /8、 /16、/24 形式网段
最多可填充 50 个白名单或 50 个黑名单
注意：此字段可能返回 null，表示取不到有效值。\n        :type Filters: list of str\n        :param FilterRules: IP 黑白名单分路径配置，白名单功能
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterRules: list of IpFilterPathRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilterPathRule(AbstractModel):
    """IP黑白名单分路径配置

    """

    def __init__(self):
        """
        :param FilterType: IP 黑白名单类型
whitelist：白名单
blacklist：黑名单
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterType: str\n        :param Filters: IP 黑白名单列表
支持 X.X.X.X 形式 IP，或 /8、 /16、/24 形式网段
最多可填充 50 个白名单或 50 个黑名单
注意：此字段可能返回 null，表示取不到有效值。\n        :type Filters: list of str\n        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleType: str\n        :param RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
注意：此字段可能返回 null，表示取不到有效值。\n        :type RulePaths: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """单节点单 IP 访问限频配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: IP 限频配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param Qps: 设置每秒请求数限制
超出限制的请求会直接返回 514
注意：此字段可能返回 null，表示取不到有效值。\n        :type Qps: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpStatus(AbstractModel):
    """节点 IP 信息

    """

    def __init__(self):
        """
        :param Ip: 节点 IP\n        :type Ip: str\n        :param District: 节点所属区域\n        :type District: str\n        :param Isp: 节点所属运营商\n        :type Isp: str\n        :param City: 节点所在城市\n        :type City: str\n        :param Status: 节点状态
online：上线状态，正常调度服务中
offline：下线状态\n        :type Status: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6(AbstractModel):
    """Ipv6启用配置，不可更改

    """

    def __init__(self):
        """
        :param Switch: 域名是否开启ipv6功能，on或off。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Ipv6Access(AbstractModel):
    """Ipv6访问配置

    """

    def __init__(self):
        """
        :param Switch: 域名是否开启ipv6访问功能，on或off。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type RulePaths: list of str\n        :param RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleType: str\n        :param FullUrlCache: 是否开启全路径缓存
on：开启全路径缓存（即关闭参数过滤）
off：关闭全路径缓存（即开启参数过滤）
注意：此字段可能返回 null，表示取不到有效值。\n        :type FullUrlCache: str\n        :param IgnoreCase: 是否忽略大小写缓存
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreCase: str\n        :param QueryString: CacheKey中包含请求参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type QueryString: :class:`tencentcloud.cdn.v20180606.models.RuleQueryString`\n        :param RuleTag: 路径缓存键标签，传 user
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleTag: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsRequest(AbstractModel):
    """ListClsLogTopics请求参数结构体

    """

    def __init__(self):
        """
        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        """
        self.Channel = None


    def _deserialize(self, params):
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsLogTopicsResponse(AbstractModel):
    """ListClsLogTopics返回参数结构体

    """

    def __init__(self):
        """
        :param Logset: 日志集信息\n        :type Logset: :class:`tencentcloud.cdn.v20180606.models.LogSetInfo`\n        :param Topics: 日志主题信息列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type Topics: list of TopicInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ListClsTopicDomainsRequest(AbstractModel):
    """ListClsTopicDomains请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param TopicId: 日志主题ID\n        :type TopicId: str\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListClsTopicDomainsResponse(AbstractModel):
    """ListClsTopicDomains返回参数结构体

    """

    def __init__(self):
        """
        :param AppId: 开发者ID\n        :type AppId: int\n        :param Channel: 渠道\n        :type Channel: str\n        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param TopicId: 日志主题ID\n        :type TopicId: str\n        :param DomainAreaConfigs: 域名区域配置，其中可能含有已删除的域名，如果要再传回ManageClsTopicDomains接口，需要结合ListCdnDomains接口排除掉已删除的域名\n        :type DomainAreaConfigs: list of DomainAreaConfig\n        :param TopicName: 日志主题名称\n        :type TopicName: str\n        :param UpdateTime: 日志主题最近更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ListDiagnoseReportRequest(AbstractModel):
    """ListDiagnoseReport请求参数结构体

    """

    def __init__(self):
        """
        :param KeyWords: 用于搜索诊断URL的关键字，不填时返回用户所有的诊断任务。\n        :type KeyWords: str\n        :param DiagnoseLink: 用于搜索诊断系统返回的诊断链接，形如：http://cdn.cloud.tencent.com/self_diagnose/xxxxx\n        :type DiagnoseLink: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListDiagnoseReportResponse(AbstractModel):
    """ListDiagnoseReport返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 诊断信息。\n        :type Data: list of DiagnoseInfo\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ListScdnDomainsRequest(AbstractModel):
    """ListScdnDomains请求参数结构体

    """

    def __init__(self):
        """
        :param Offset: 分页起始地址\n        :type Offset: int\n        :param Limit: 列表分页记录条数，最大1000\n        :type Limit: int\n        :param Domain: 域名信息\n        :type Domain: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListScdnDomainsResponse(AbstractModel):
    """ListScdnDomains返回参数结构体

    """

    def __init__(self):
        """
        :param DomainList: 域名列表信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type DomainList: list of ScdnDomain\n        :param TotalCount: 域名的总条数。
注意：此字段可能返回 null，表示取不到有效值。\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ListScdnLogTasksRequest(AbstractModel):
    """ListScdnLogTasks请求参数结构体

    """

    def __init__(self):
        """
        :param Source: 产品来源 cdn/ecdn\n        :type Source: str\n        :param Area: 地域：mainland 或 overseas 为空表示查询所有地域\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListScdnLogTasksResponse(AbstractModel):
    """ListScdnLogTasks返回参数结构体

    """

    def __init__(self):
        """
        :param TaskList: 日志下载任务详情\n        :type TaskList: list of ScdnLogTaskDetail\n        :param TotalCount: 查询到的下载任务的总数\n        :type TotalCount: int\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class ListTopDataRequest(AbstractModel):
    """ListTopData请求参数结构体

    """

    def __init__(self):
        """
        :param StartTime: 查询起始日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为起始日期
返回大于等于起始日期当天 00:00:00 点产生的数据
仅支持 90 天内数据查询\n        :type StartTime: str\n        :param EndTime: 查询结束日期：yyyy-MM-dd HH:mm:ss
仅支持按天粒度的数据查询，取入参中的天信息作为结束日期
返回小于等于结束日期当天 23:59:59 产生的数据
EndTime 需要大于等于 StartTime\n        :type EndTime: str\n        :param Metric: 排序对象，支持以下几种形式：
url：访问 URL 排序（无参数的URL），支持的 Filter 为 flux、request
district：省份、国家/地区排序，支持的 Filter 为 flux、request
isp：运营商排序，支持的 Filter 为 flux、request
host：域名访问数据排序，支持的 Filter 为：flux、request、bandwidth、fluxHitRate、2XX、3XX、4XX、5XX、statusCode
originHost：域名回源数据排序，支持的 Filter 为 flux、request、bandwidth、origin_2XX、origin_3XX、origin_4XX、origin_5XX、OriginStatusCode\n        :type Metric: str\n        :param Filter: 排序使用的指标名称：
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
OriginStatusCode：指定回源状态码统计，在 Code 参数中填充指定状态码\n        :type Filter: str\n        :param Domains: 指定查询域名列表，最多可一次性查询 30 个加速域名明细\n        :type Domains: list of str\n        :param Project: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主\n        :type Project: int\n        :param Detail: 多域名查询时，默认（false)返回所有域名汇总排序结果
Metric 为 url、path、district、isp，Filter 为 flux、request 时，可设置为 true，返回每一个 Domain 的排序数据\n        :type Detail: bool\n        :param Code: Filter 为 statusCode、OriginStatusCode 时，填充指定状态码查询排序结果\n        :type Code: str\n        :param Area: 指定服务地域查询，不填充表示查询中国境内 CDN 数据
mainland：指定查询中国境内 CDN 数据
overseas：指定查询中国境外 CDN 数据，支持的 Metric 为 url、district、host、originHost，当 Metric 为 originHost 时仅支持 flux、request、bandwidth Filter\n        :type Area: str\n        :param AreaType: 查询中国境外CDN数据，且仅当 Metric 为 district 或 host 时，可指定地区类型查询，不填充表示查询服务地区数据（仅在 Area 为 overseas，且 Metric 是 district 或 host 时可用）
server：指定查询服务地区（腾讯云 CDN 节点服务器所在地区）数据
client：指定查询客户端地区（用户请求终端所在地区）数据，当 Metric 为 host 时仅支持 flux、request、bandwidth Filter\n        :type AreaType: str\n        :param Product: 指定查询的产品数据，可选为cdn或者ecdn，默认为cdn\n        :type Product: str\n        """
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
        self.Product = None


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
        self.Product = params.get("Product")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ListTopDataResponse(AbstractModel):
    """ListTopData返回参数结构体

    """

    def __init__(self):
        """
        :param Data: 各个资源的Top 访问数据详情。\n        :type Data: list of TopData\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
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


class LogSetInfo(AbstractModel):
    """日志集信息

    """

    def __init__(self):
        """
        :param AppId: 开发者ID\n        :type AppId: int\n        :param Channel: 渠道
注意：此字段可能返回 null，表示取不到有效值。\n        :type Channel: str\n        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param LogsetName: 日志集名字\n        :type LogsetName: str\n        :param IsDefault: 是否默认日志集\n        :type IsDefault: int\n        :param LogsetSavePeriod: 日志保存时间，单位为天\n        :type LogsetSavePeriod: int\n        :param CreateTime: 创建日期\n        :type CreateTime: str\n        :param Region: 区域\n        :type Region: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`\n        :param BandwidthAlert: 带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`\n        :param Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`\n        :param CacheKey: 缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`\n        :param Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`\n        :param DownstreamCapping: 下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`\n        :param ErrorPage: 错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`\n        :param FollowRedirect: 301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`\n        :param ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`\n        :param Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`\n        :param IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`\n        :param IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`\n        :param MaxAge: 浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`\n        :param Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`\n        :param OriginPullOptimization: 跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`\n        :param RangeOriginPull: Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`\n        :param Referer: 防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`\n        :param RequestHeader: 回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`\n        :param ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`\n        :param ResponseHeaderCache: 遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`\n        :param Seo: seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`\n        :param ServiceType: 域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceType: str\n        :param StatusCodeCache: 状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`\n        :param VideoSeek: 视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsRequest(AbstractModel):
    """ManageClsTopicDomains请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 日志集ID\n        :type LogsetId: str\n        :param TopicId: 日志主题ID\n        :type TopicId: str\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        :param DomainAreaConfigs: 域名区域配置，注意：如果此字段为空，则表示解绑对应主题下的所有域名\n        :type DomainAreaConfigs: list of DomainAreaConfig\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ManageClsTopicDomainsResponse(AbstractModel):
    """ManageClsTopicDomains返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class MapInfo(AbstractModel):
    """名称与ID映射关系

    """

    def __init__(self):
        """
        :param Id: 对象 Id\n        :type Id: int\n        :param Name: 对象名称\n        :type Name: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MaxAge(AbstractModel):
    """浏览器缓存规则配置，用于设置 MaxAge 默认值，默认为关闭状态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 浏览器缓存配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param MaxAgeRules: MaxAge 规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxAgeRules: list of MaxAgeRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
index: 指定主页生效\n        :type MaxAgeType: str\n        :param MaxAgeContents: MaxAgeType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /
注意：all规则不可删除，默认遵循源站，可修改。\n        :type MaxAgeContents: list of str\n        :param MaxAgeTime: MaxAge 时间设置，单位秒
注意：时间为0，即不缓存。\n        :type MaxAgeTime: int\n        :param FollowOrigin: 是否遵循源站，on或off，开启时忽略时间设置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowOrigin: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPurgeFetchTaskStatusRequest(AbstractModel):
    """ModifyPurgeFetchTaskStatus请求参数结构体

    """

    def __init__(self):
        """
        :param ExecutionTime: 执行时间\n        :type ExecutionTime: str\n        :param ExecutionStatus: 执行状态
success: 成功
failed: 失败\n        :type ExecutionStatus: str\n        :param Id: 任务 ID\n        :type Id: str\n        :param ExecutionStatusDesc: 执行状态详情\n        :type ExecutionStatusDesc: str\n        """
        self.ExecutionTime = None
        self.ExecutionStatus = None
        self.Id = None
        self.ExecutionStatusDesc = None


    def _deserialize(self, params):
        self.ExecutionTime = params.get("ExecutionTime")
        self.ExecutionStatus = params.get("ExecutionStatus")
        self.Id = params.get("Id")
        self.ExecutionStatusDesc = params.get("ExecutionStatusDesc")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyPurgeFetchTaskStatusResponse(AbstractModel):
    """ModifyPurgeFetchTaskStatus返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class OfflineCache(AbstractModel):
    """离线缓存是否开启

    """

    def __init__(self):
        """
        :param Switch: on | off, 离线缓存是否开启\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Origins: list of str\n        :param OriginType: 主源站类型
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
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginType: str\n        :param ServerName: 回主源站时 Host 头部，不填充则默认为加速域名
若接入的是泛域名，则回源 Host 默认为访问时的子域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerName: str\n        :param CosPrivateAccess: OriginType 为对象存储（COS）时，可以指定是否允许访问私有 bucket
注意：需要先授权 CDN 访问该私有 Bucket 的权限后，才可开启此配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CosPrivateAccess: str\n        :param OriginPullProtocol: 回源协议配置
http：强制 http 回源
follow：协议跟随回源
https：强制 https 回源，https 回源时仅支持源站 443 端口
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginPullProtocol: str\n        :param BackupOrigins: 备源站列表
修改备源站时，需要同时填充对应的 BackupOriginType
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupOrigins: list of str\n        :param BackupOriginType: 备源站类型，支持以下类型：
domain：域名类型
ip：IP 列表作为源站
修改 BackupOrigins 时需要同时填充对应的 BackupOriginType
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupOriginType: str\n        :param BackupServerName: 回备源站时 Host 头部，不填充则默认为主源站的 ServerName
注意：此字段可能返回 null，表示取不到有效值。\n        :type BackupServerName: str\n        :param BasePath: 回源路径
注意：此字段可能返回 null，表示取不到有效值。\n        :type BasePath: str\n        :param PathRules: 回源路径重写规则配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathRules: list of PathRule\n        :param PathBasedOrigin: 分路径回源配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathBasedOrigin: list of PathBasedOriginRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthentication(AbstractModel):
    """回源鉴权高级配置

    """

    def __init__(self):
        """
        :param Switch: 鉴权开关，on或off
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param TypeA: 鉴权类型A配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type TypeA: :class:`tencentcloud.cdn.v20180606.models.OriginAuthenticationTypeA`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginAuthenticationTypeA(AbstractModel):
    """回源鉴权高级配置TypeA

    """

    def __init__(self):
        """
        :param SecretKey: 用于计算签名的密钥，只允许字母和数字，长度6-32字节。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        """
        self.SecretKey = None


    def _deserialize(self, params):
        self.SecretKey = params.get("SecretKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginCombine(AbstractModel):
    """合并回源配置项

    """

    def __init__(self):
        """
        :param Switch: on|off 是否开启合并回源\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginIp(AbstractModel):
    """CDN回源节点IP信息

    """

    def __init__(self):
        """
        :param Ip: 回源IP段/回源IP，默认返回IP段信息。\n        :type Ip: str\n        """
        self.Ip = None


    def _deserialize(self, params):
        self.Ip = params.get("Ip")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullOptimization(AbstractModel):
    """跨国回源优化配置，默认为关闭状态（功能灰度中，尚未全量）

    """

    def __init__(self):
        """
        :param Switch: 跨国回源优化配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param OptimizationType: 跨国类型
OVToCN：境外回源境内
CNToOV：境内回源境外
注意：此字段可能返回 null，表示取不到有效值。\n        :type OptimizationType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OriginPullTimeout(AbstractModel):
    """回源超时配置

    """

    def __init__(self):
        """
        :param ConnectTimeout: 回源建连超时时间，单位为秒，要求5~60之间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ConnectTimeout: int\n        :param ReceiveTimeout: 回源接收超时时间，单位为秒，要求10 ~ 60之间
注意：此字段可能返回 null，表示取不到有效值。\n        :type ReceiveTimeout: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OssPrivateAccess(AbstractModel):
    """oss回源鉴权

    """

    def __init__(self):
        """
        :param Switch: 开关， on/off。\n        :type Switch: str\n        :param AccessKey: 访问ID。
注意：此字段可能返回 null，表示取不到有效值。\n        :type AccessKey: str\n        :param SecretKey: 密钥。
注意：此字段可能返回 null，表示取不到有效值。\n        :type SecretKey: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`\n        :param BandwidthAlert: 带宽封顶配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`\n        :param Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`\n        :param CacheKey: 缓存相关配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`\n        :param Compression: 智能压缩配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`\n        :param DownstreamCapping: 下载限速配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`\n        :param ErrorPage: 错误码重定向配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`\n        :param FollowRedirect: 301和302自动回源跟随配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`\n        :param ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`\n        :param Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`\n        :param IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`\n        :param IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`\n        :param MaxAge: 浏览器缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`\n        :param Origin: 源站配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`\n        :param OriginPullOptimization: 跨国优化配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`\n        :param RangeOriginPull: Range回源配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`\n        :param Referer: 防盗链配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`\n        :param RequestHeader: 回源请求头部配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`\n        :param ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`\n        :param ResponseHeaderCache: 遵循源站缓存头部配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`\n        :param Seo: seo优化配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`\n        :param ServiceType: 域名业务类型，web，download，media分别表示静态加速，下载加速和流媒体加速。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServiceType: str\n        :param StatusCodeCache: 状态码缓存配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`\n        :param VideoSeek: 视频拖拽配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathBasedOriginRule(AbstractModel):
    """分路径回源规则

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index: 指定主页生效\n        :type RuleType: str\n        :param RulePaths: RuleType 对应类型下的匹配内容：
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /\n        :type RulePaths: list of str\n        :param Origin: 源站列表，支持域名或ipv4地址\n        :type Origin: list of str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PathRule(AbstractModel):
    """分路径回源配置规则。

    """

    def __init__(self):
        """
        :param Regex: 是否开启通配符“*”匹配：
false：关闭
true：开启
注意：此字段可能返回 null，表示取不到有效值。\n        :type Regex: bool\n        :param Path: 匹配的URL路径，仅支持Url路径，不支持参数。默认完全匹配，开启通配符“*”匹配后，最多支持5个通配符，最大长度为1024个字符。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        :param Origin: 路径匹配时的回源源站。暂不支持开了私有读写的COS源。不填写时沿用默认源站。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Origin: str\n        :param ServerName: 路径匹配时回源的Host头部。不填写时沿用默认ServerName。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ServerName: str\n        :param OriginArea: 源站所属区域，支持CN，OV：
CN：中国境内
OV：中国境外
默认为CN。
注意：此字段可能返回 null，表示取不到有效值。\n        :type OriginArea: str\n        :param ForwardUri: 路径匹配时回源的URI路径，必须以“/”开头，不包含参数部分。最大长度为1024个字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号“*”，最多支持10个捕获值。
注意：此字段可能返回 null，表示取不到有效值。\n        :type ForwardUri: str\n        :param RequestHeaders: 路径匹配时回源的头部设置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type RequestHeaders: list of HttpHeaderRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PostSize(AbstractModel):
    """POST请求上传文件流式传输最大限制

    """

    def __init__(self):
        """
        :param Switch: 是调整POST请求限制，平台默认为32MB。
关闭：off，
开启：on。\n        :type Switch: str\n        :param MaxSize: 最大限制，取值在1MB和200MB之间。\n        :type MaxSize: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheRequest(AbstractModel):
    """PurgePathCache请求参数结构体

    """

    def __init__(self):
        """
        :param Paths: 目录列表，需要包含协议头部 http:// 或 https://\n        :type Paths: list of str\n        :param FlushType: 刷新类型
flush：刷新产生更新的资源
delete：刷新全部资源\n        :type FlushType: str\n        :param UrlEncode: 是否对中文字符进行编码后刷新\n        :type UrlEncode: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgePathCacheResponse(AbstractModel):
    """PurgePathCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务 ID，同一批次提交的目录共用一个任务 ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """刷新任务详情

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务 ID\n        :type TaskId: str\n        :param Url: 刷新 URL\n        :type Url: str\n        :param Status: 刷新任务状态
fail：刷新失败
done：刷新成功
process：刷新中\n        :type Status: str\n        :param PurgeType: 刷新类型
url：URL 刷新
path：目录刷新\n        :type PurgeType: str\n        :param FlushType: 刷新方式
flush：刷新更新资源（仅目录刷新时有此类型）
delete：刷新全部资源\n        :type FlushType: str\n        :param CreateTime: 刷新任务提交时间\n        :type CreateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheRequest(AbstractModel):
    """PurgeUrlsCache请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: URL 列表，需要包含协议头部 http:// 或 https://\n        :type Urls: list of str\n        :param Area: 刷新区域
无此参数时，默认刷新加速域名所在加速区域
填充 mainland 时，仅刷新中国境内加速节点上缓存内容
填充 overseas 时，仅刷新中国境外加速节点上缓存内容
指定刷新区域时，需要与域名加速区域匹配\n        :type Area: str\n        :param UrlEncode: 是否对中文字符进行编码后刷新\n        :type UrlEncode: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 刷新任务 ID，同一批次提交的 URL 共用一个任务 ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class PushTask(AbstractModel):
    """预热任务详情

    """

    def __init__(self):
        """
        :param TaskId: 预热任务 ID\n        :type TaskId: str\n        :param Url: 预热 URL\n        :type Url: str\n        :param Status: 预热任务状态
fail：预热失败
done：预热成功
process：预热中
invalid：预热无效(源站返回4xx或5xx状态码)\n        :type Status: str\n        :param Percent: 预热进度百分比\n        :type Percent: int\n        :param CreateTime: 预热任务提交时间\n        :type CreateTime: str\n        :param Area: 预热区域
mainland：境内
overseas：境外
global：全球\n        :type Area: str\n        :param UpdateTime: 预热任务更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheRequest(AbstractModel):
    """PushUrlsCache请求参数结构体

    """

    def __init__(self):
        """
        :param Urls: URL 列表，需要包含协议头部 http:// 或 https://\n        :type Urls: list of str\n        :param UserAgent: 指定预热请求回源时 HTTP 请求的 User-Agent 头部
默认为 TencentCdn\n        :type UserAgent: str\n        :param Area: 预热生效区域
mainland：预热至境内节点
overseas：预热至境外节点
global：预热全球节点
不填充情况下，默认为 mainland， URL 中域名必须在对应区域启用了加速服务才能提交对应区域的预热任务\n        :type Area: str\n        :param Layer: 填写"middle"或不填充时预热至中间层节点\n        :type Layer: str\n        :param ParseM3U8: 是否递归解析m3u8文件中的ts分片预热
注意事项：
1. 该功能要求m3u8索引文件能直接请求获取
2. 当前只支持递归解析一级索引和子索引中的ts分片，递归深度不超过3层
3. 解析获取的ts分片会正常累加每日预热用量，当用量超出配额时，会静默处理，不再执行预热\n        :type ParseM3U8: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class PushUrlsCacheResponse(AbstractModel):
    """PushUrlsCache返回参数结构体

    """

    def __init__(self):
        """
        :param TaskId: 此批提交的任务 ID\n        :type TaskId: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class QueryStringKey(AbstractModel):
    """组成CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: on | off CacheKey是否由QueryString组成
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Reorder: 是否重新排序
注意：此字段可能返回 null，表示取不到有效值。\n        :type Reorder: str\n        :param Action: includeAll | excludeAll | includeCustom | excludeAll 使用/排除部分url参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Action: str\n        :param Value: 使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quic(AbstractModel):
    """Quic配置项

    """

    def __init__(self):
        """
        :param Switch: 是否启动Quic配置\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Quota(AbstractModel):
    """刷新/预热 可用量及配额

    """

    def __init__(self):
        """
        :param Batch: 单次批量提交配额上限。\n        :type Batch: int\n        :param Total: 每日提交配额上限。\n        :type Total: int\n        :param Available: 每日剩余的可提交配额。\n        :type Available: int\n        :param Area: 配额的区域。\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RangeOriginPull(AbstractModel):
    """分片回源配置，默认为开启状态

    """

    def __init__(self):
        """
        :param Switch: 分片回源配置开关
on：开启
off：关闭\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Referer(AbstractModel):
    """Referer 黑白名单配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: referer 黑白名单配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param RefererRules: referer 黑白名单配置规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type RefererRules: list of RefererRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RefererRule(AbstractModel):
    """Referer 黑白名单配置规则，针对特定资源生效

    """

    def __init__(self):
        """
        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效\n        :type RuleType: str\n        :param RulePaths: RuleType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test/
path 时填充绝对路径，如 /xxx/test.html\n        :type RulePaths: list of str\n        :param RefererType: referer 配置类型
whitelist：白名单
blacklist：黑名单\n        :type RefererType: str\n        :param Referers: referer 内容列表列表\n        :type Referers: list of str\n        :param AllowEmpty: 是否允许空 referer
true：允许空 referer
false：不允许空 referer\n        :type AllowEmpty: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionMapRelation(AbstractModel):
    """区域映射id和子区域id的关联信息。

    """

    def __init__(self):
        """
        :param RegionId: 区域ID。\n        :type RegionId: int\n        :param SubRegionIdList: 子区域ID列表\n        :type SubRegionIdList: list of int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ReportData(AbstractModel):
    """CDN报表数据

    """

    def __init__(self):
        """
        :param ResourceId: 项目ID/域名ID。\n        :type ResourceId: str\n        :param Resource: 项目名称/域名。\n        :type Resource: str\n        :param Value: 流量总和/带宽最大值，单位分别为bytes，bps。\n        :type Value: int\n        :param Percentage: 单个资源占总体百分比。\n        :type Percentage: float\n        :param BillingValue: 计费流量总和/计费带宽最大值，单位分别为bytes，bps。\n        :type BillingValue: int\n        :param BillingPercentage: 计费数值占总体百分比。\n        :type BillingPercentage: float\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RequestHeader(AbstractModel):
    """自定义请求头配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 自定义请求头配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param HeaderRules: 自定义请求头配置规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeaderRules: list of HttpHeaderPathRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceBillingData(AbstractModel):
    """计费数据明细

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
某一个具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
某一个项目 ID：指定项目查询时，显示为项目 ID
all：账号维度数据明细\n        :type Resource: str\n        :param BillingData: 计费数据详情\n        :type BillingData: list of CdnData\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceData(AbstractModel):
    """查询对象及其对应的访问明细数据

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据\n        :type Resource: str\n        :param CdnData: 资源对应的数据明细\n        :type CdnData: list of CdnData\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResourceOriginData(AbstractModel):
    """查询对象及其对应的回源明细数据

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据\n        :type Resource: str\n        :param OriginData: 回源数据详情\n        :type OriginData: list of CdnData\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """自定义响应头配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 自定义响应头开关
on：开启
off：关闭\n        :type Switch: str\n        :param HeaderRules: 自定义响应头规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type HeaderRules: list of HttpHeaderPathRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeaderCache(AbstractModel):
    """源站头部缓存配置，默认为开启状态，缓存所有头部信息

    """

    def __init__(self):
        """
        :param Switch: 源站头部缓存开关
on：开启
off：关闭\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Revalidate(AbstractModel):
    """是否回源站校验

    """

    def __init__(self):
        """
        :param Switch: on | off 是否总是回源校验
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Path: 只在特定请求路径回源站校验
注意：此字段可能返回 null，表示取不到有效值。\n        :type Path: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type RulePaths: list of str\n        :param RuleType: 规则类型：
all：所有文件生效
file：指定文件后缀生效
directory：指定路径生效
path：指定绝对路径生效
index：首页
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleType: str\n        :param CacheConfig: 缓存配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheConfig: :class:`tencentcloud.cdn.v20180606.models.RuleCacheConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleCacheConfig(AbstractModel):
    """路径缓存缓存配置（三种缓存模式中选取一种）

    """

    def __init__(self):
        """
        :param Cache: 缓存配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type Cache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigCache`\n        :param NoCache: 不缓存配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type NoCache: :class:`tencentcloud.cdn.v20180606.models.CacheConfigNoCache`\n        :param FollowOrigin: 遵循源站配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowOrigin: :class:`tencentcloud.cdn.v20180606.models.CacheConfigFollowOrigin`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleQueryString(AbstractModel):
    """路径保留参数配置

    """

    def __init__(self):
        """
        :param Switch: on | off CacheKey是否由QueryString组成
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param Action: includeCustom 包含部分url参数
注意：此字段可能返回 null，表示取不到有效值。\n        :type Action: str\n        :param Value: 使用/排除的url参数数组，';' 分割
注意：此字段可能返回 null，表示取不到有效值。\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclConfig(AbstractModel):
    """SCDN访问控制

    """

    def __init__(self):
        """
        :param Switch: 是否开启，on | off\n        :type Switch: str\n        :param ScriptData: Acl规则组，switch为on时必填
注意：此字段可能返回 null，表示取不到有效值。\n        :type ScriptData: list of ScdnAclGroup\n        :param ErrorPage: 错误页面配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclGroup(AbstractModel):
    """SCDN精准访问控制配置

    """

    def __init__(self):
        """
        :param RuleName: 规则名称\n        :type RuleName: str\n        :param Configure: 具体配置\n        :type Configure: list of ScdnAclRule\n        :param Result: 规则行为，一般为refuse，重定向redirect\n        :type Result: str\n        :param Status: 规则是否生效中active|inactive\n        :type Status: str\n        :param ErrorPage: 错误页面配置
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`\n        """
        self.RuleName = None
        self.Configure = None
        self.Result = None
        self.Status = None
        self.ErrorPage = None


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
        if params.get("ErrorPage") is not None:
            self.ErrorPage = ScdnErrorPage()
            self.ErrorPage._deserialize(params.get("ErrorPage"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnAclRule(AbstractModel):
    """精准访问控制匹配规则

    """

    def __init__(self):
        """
        :param MatchKey: 匹配关键字, params | url | ip | referer | user-agent\n        :type MatchKey: str\n        :param LogiOperator: 逻辑操作符，取值 exclude, include, notequal, equal, len-less, len-equal, len-more\n        :type LogiOperator: str\n        :param MatchValue: 匹配值\n        :type MatchValue: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnBotConfig(AbstractModel):
    """bot配置类型

    """

    def __init__(self):
        """
        :param Switch: on|off\n        :type Switch: str\n        :param BotCookie: Bot cookie策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type BotCookie: list of BotCookie\n        :param BotJavaScript: Bot Js策略
注意：此字段可能返回 null，表示取不到有效值。\n        :type BotJavaScript: list of BotJavaScript\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
index：首页\n        :type RuleType: str\n        :param RuleValue: 规则值\n        :type RuleValue: list of str\n        :param Qps: 规则限频\n        :type Qps: int\n        :param DetectionTime: 探测时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type DetectionTime: int\n        :param FrequencyLimit: 限频阈值
注意：此字段可能返回 null，表示取不到有效值。\n        :type FrequencyLimit: int\n        :param PunishmentSwitch: IP 惩罚开关，可选on|off
注意：此字段可能返回 null，表示取不到有效值。\n        :type PunishmentSwitch: str\n        :param PunishmentTime: IP 惩罚时长
注意：此字段可能返回 null，表示取不到有效值。\n        :type PunishmentTime: int\n        :param Action: 执行动作，intercept|redirect
注意：此字段可能返回 null，表示取不到有效值。\n        :type Action: str\n        :param RedirectUrl: 动作为 redirect 时，重定向的url
注意：此字段可能返回 null，表示取不到有效值。\n        :type RedirectUrl: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnConfig(AbstractModel):
    """cc的配置类型

    """

    def __init__(self):
        """
        :param Switch: on | off\n        :type Switch: str\n        :param Rules: 自定义 cc 防护规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rules: list of ScdnCCRules\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnDdosConfig(AbstractModel):
    """ddos配置类型

    """

    def __init__(self):
        """
        :param Switch: on|off\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnDomain(AbstractModel):
    """聚合了SCDN域名的基本信息

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Status: 当前状态，取值online | offline | process\n        :type Status: str\n        :param Waf: Waf 状态默认为‘/’，取值 close | intercept | observe\n        :type Waf: str\n        :param Acl: Acl 状态默认为‘/’，取值 close | open\n        :type Acl: str\n        :param CC: CC 状态默认为‘/’，取值 close | open\n        :type CC: str\n        :param Ddos: Ddos 状态默认为‘/’，取值 close | open\n        :type Ddos: str\n        :param ProjectId: 项目ID\n        :type ProjectId: str\n        :param AclRuleNumbers: Acl 规则数\n        :type AclRuleNumbers: int\n        :param Bot: Bot 状态默认为‘/’，取值 close | open\n        :type Bot: str\n        :param Area: 域名加速区域，取值global | mainland |  overseas
注意：此字段可能返回 null，表示取不到有效值。\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnErrorPage(AbstractModel):
    """acl的错误页面

    """

    def __init__(self):
        """
        :param RedirectCode: 状态码\n        :type RedirectCode: int\n        :param RedirectUrl: 重定向url\n        :type RedirectUrl: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnEventLogConditions(AbstractModel):
    """SCDN 事件日志查询条件

    """

    def __init__(self):
        """
        :param Key: 匹配关键字，ip, attack_location\n        :type Key: str\n        :param Operator: 逻辑操作符，取值 exclude, include\n        :type Operator: str\n        :param Value: 匹配值，允许使用通配符(*)查询，匹配零个、单个、多个字符，例如 1.2.*\n        :type Value: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnLogTaskDetail(AbstractModel):
    """SCDN日志事件详细信息

    """

    def __init__(self):
        """
        :param Domain: scdn域名\n        :type Domain: str\n        :param Mode: 防护类型\n        :type Mode: str\n        :param StartTime: 查询任务开始时间\n        :type StartTime: str\n        :param EndTime: 查询任务结束时间\n        :type EndTime: str\n        :param CreateTime: 任务创建时间\n        :type CreateTime: str\n        :param DownloadUrl: 日志包下载链接
成功返回下载链接，其他情况返回'-'
注意：此字段可能返回 null，表示取不到有效值。\n        :type DownloadUrl: str\n        :param Status: 任务状态
created->任务已经创建
processing->任务正在执行
done->任务执行成功
failed->任务执行失败
no-log->没有日志产生\n        :type Status: str\n        :param TaskID: 日志任务唯一id\n        :type TaskID: str\n        :param AttackType: 攻击类型, 可以为"all"
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
  malicious_file_upload= '恶意文件上传'\n        :type AttackType: str\n        :param DefenceMode: 防御模式,可以为"all"
DefenceMode映射如下：
  observe = '观察模式'
  intercept = '防御模式'\n        :type DefenceMode: str\n        :param Conditions: 查询条件
注意：此字段可能返回 null，表示取不到有效值。\n        :type Conditions: list of ScdnEventLogConditions\n        :param Area: mainland或overseas
注意：此字段可能返回 null，表示取不到有效值。\n        :type Area: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTopData(AbstractModel):
    """SCDN攻击数据Top展示

    """

    def __init__(self):
        """
        :param Time: 时间\n        :type Time: str\n        :param Value: 数值\n        :type Value: int\n        :param Isp: 运营商\n        :type Isp: str\n        :param Ip: IP地址\n        :type Ip: str\n        :param District: 区域\n        :type District: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTopUrlData(AbstractModel):
    """SCDN攻击数据Top URL展示

    """

    def __init__(self):
        """
        :param Url: Top数据的URL\n        :type Url: str\n        :param Value: 数值\n        :type Value: int\n        :param Time: 时间\n        :type Time: str\n        :param Domain: 域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type Domain: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnTypeData(AbstractModel):
    """Scdn饼图数据，waf仅有

    """

    def __init__(self):
        """
        :param AttackType: 攻击类型\n        :type AttackType: str\n        :param Value: 攻击值\n        :type Value: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafConfig(AbstractModel):
    """waf配置类型

    """

    def __init__(self):
        """
        :param Switch: on|off\n        :type Switch: str\n        :param Mode: intercept|observe，默认intercept
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mode: str\n        :param ErrorPage: 重定向的错误页面
注意：此字段可能返回 null，表示取不到有效值。\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ScdnErrorPage`\n        :param WebShellSwitch: webshell拦截开关，on|off，默认off
注意：此字段可能返回 null，表示取不到有效值。\n        :type WebShellSwitch: str\n        :param Rules: 类型拦截规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type Rules: list of ScdnWafRule\n        :param Level: waf规则等级，可取100|200|300
注意：此字段可能返回 null，表示取不到有效值。\n        :type Level: int\n        :param SubRuleSwitch: waf子规则开关
注意：此字段可能返回 null，表示取不到有效值。\n        :type SubRuleSwitch: list of WafSubRuleStatus\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ScdnWafRule(AbstractModel):
    """Waf 规则信息

    """

    def __init__(self):
        """
        :param AttackType: 攻击类型\n        :type AttackType: str\n        :param Operate: 防护措施，observe\n        :type Operate: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SchemeKey(AbstractModel):
    """作为CacheKey的一部分

    """

    def __init__(self):
        """
        :param Switch: on | off 是否使用scheme作为cache key的一部分
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogRequest(AbstractModel):
    """SearchClsLog请求参数结构体

    """

    def __init__(self):
        """
        :param LogsetId: 需要查询的日志集ID\n        :type LogsetId: str\n        :param TopicIds: 需要查询的日志主题ID组合，以逗号分隔\n        :type TopicIds: str\n        :param StartTime: 需要查询的日志的起始时间，格式 YYYY-mm-dd HH:MM:SS\n        :type StartTime: str\n        :param EndTime: 需要查询的日志的结束时间，格式 YYYY-mm-dd HH:MM:SS\n        :type EndTime: str\n        :param Limit: 单次要返回的日志条数，单次返回的最大条数为100\n        :type Limit: int\n        :param Channel: 接入渠道，默认值为cdn\n        :type Channel: str\n        :param Query: 需要查询的内容，详情请参考https://cloud.tencent.com/document/product/614/16982\n        :type Query: str\n        :param Context: 加载更多使用，透传上次返回的 context 值，获取后续的日志内容，通过游标最多可获取10000条，请尽可能缩小时间范围\n        :type Context: str\n        :param Sort: 按日志时间排序， asc（升序）或者 desc（降序），默认为 desc\n        :type Sort: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SearchClsLogResponse(AbstractModel):
    """SearchClsLog返回参数结构体

    """

    def __init__(self):
        """
        :param Logs: 查询结果\n        :type Logs: :class:`tencentcloud.cdn.v20180606.models.ClsSearchLogs`\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Logs = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("Logs") is not None:
            self.Logs = ClsSearchLogs()
            self.Logs._deserialize(params.get("Logs"))
        self.RequestId = params.get("RequestId")


class SecurityConfig(AbstractModel):
    """scdn相关的配置

    """

    def __init__(self):
        """
        :param Switch: on|off\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Seo(AbstractModel):
    """SEO 搜索引擎优化配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: SEO 配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertId: str\n        :param CertName: 服务器证书名称
在 SSL 证书管理进行证书托管时自动生成
注意：此字段可能返回 null，表示取不到有效值。\n        :type CertName: str\n        :param Certificate: 服务器证书信息
上传自有证书时必填，需要包含完整的证书链
注意：此字段可能返回 null，表示取不到有效值。\n        :type Certificate: str\n        :param PrivateKey: 服务器密钥信息
上传自有证书时必填
注意：此字段可能返回 null，表示取不到有效值。\n        :type PrivateKey: str\n        :param ExpireTime: 证书过期时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。\n        :type ExpireTime: str\n        :param DeployTime: 证书颁发时间
作为入参配置时无需填充
注意：此字段可能返回 null，表示取不到有效值。\n        :type DeployTime: str\n        :param Message: 证书备注信息
注意：此字段可能返回 null，表示取不到有效值。\n        :type Message: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SimpleCache(AbstractModel):
    """缓存配置基础版本
    默认情况下所有文件缓存过期时间为 30 天
    默认情况下静态加速类型的域名 .php;.jsp;.asp;.aspx 不缓存
    注意：该版本不支持设置源站未返回 max-age 情况下的缓存过期规则设置

    """

    def __init__(self):
        """
        :param CacheRules: 缓存过期时间规则
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheRules: list of SimpleCacheRule\n        :param FollowOrigin: 遵循源站 Cache-Control: max-age 配置
on：开启
off：关闭
开启后，未能匹配 CacheRules 规则的资源将根据源站返回的 max-age 值进行节点缓存；匹配了 CacheRules 规则的资源将按照 CacheRules 中设置的缓存过期时间在节点进行缓存
与 CompareMaxAge 冲突，不能同时开启
注意：此字段可能返回 null，表示取不到有效值。\n        :type FollowOrigin: str\n        :param IgnoreCacheControl: 强制缓存
on：开启
off：关闭
默认为关闭状态，开启后，源站返回的 no-store、no-cache 资源，也将按照 CacheRules 规则进行缓存
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreCacheControl: str\n        :param IgnoreSetCookie: 忽略源站的Set-Cookie头部
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type IgnoreSetCookie: str\n        :param CompareMaxAge: 高级缓存过期配置，开启时会对比源站返回的 max-age 值与 CacheRules 中设置的缓存过期时间，取最小值在节点进行缓存
on：开启
off：关闭
默认为关闭状态
注意：此字段可能返回 null，表示取不到有效值。\n        :type CompareMaxAge: str\n        :param Revalidate: 总是回源站校验
注意：此字段可能返回 null，表示取不到有效值。\n        :type Revalidate: :class:`tencentcloud.cdn.v20180606.models.Revalidate`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
index：首页\n        :type CacheType: str\n        :param CacheContents: CacheType 对应类型下的匹配内容：
all 时填充 *
file 时填充后缀名，如 jpg、txt
directory 时填充路径，如 /xxx/test
path 时填充绝对路径，如 /xxx/test.html
index 时填充 /\n        :type CacheContents: list of str\n        :param CacheTime: 缓存过期时间设置
单位为秒，最大可设置为 365 天\n        :type CacheTime: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """查询结果排序条件

    """

    def __init__(self):
        """
        :param Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
默认createTime。\n        :type Key: str\n        :param Sequence: asc/desc，默认desc。\n        :type Sequence: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SpecificConfig(AbstractModel):
    """域名国内海外分地区特殊配置。

    """

    def __init__(self):
        """
        :param Mainland: 国内特殊配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Mainland: :class:`tencentcloud.cdn.v20180606.models.MainlandConfig`\n        :param Overseas: 海外特殊配置。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Overseas: :class:`tencentcloud.cdn.v20180606.models.OverseaConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainRequest(AbstractModel):
    """StartCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
域名状态需要为【已停用】\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StartCdnDomainResponse(AbstractModel):
    """StartCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StartScdnDomainRequest(AbstractModel):
    """StartScdnDomain请求参数结构体

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
        


class StartScdnDomainResponse(AbstractModel):
    """StartScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 开启结果，Success表示成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class StatusCodeCache(AbstractModel):
    """状态码缓存过期配置，默认情况下会对 404 状态码缓存 10 秒

    """

    def __init__(self):
        """
        :param Switch: 状态码缓存过期配置开关
on：开启
off：关闭
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param CacheRules: 状态码缓存过期规则明细
注意：此字段可能返回 null，表示取不到有效值。\n        :type CacheRules: list of StatusCodeCacheRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatusCodeCacheRule(AbstractModel):
    """状态码缓存过期时间规则配置

    """

    def __init__(self):
        """
        :param StatusCode: http 状态码
支持 403、404 状态码\n        :type StatusCode: str\n        :param CacheTime: 状态码缓存过期时间，单位秒\n        :type CacheTime: int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainRequest(AbstractModel):
    """StopCdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名
域名需要为【已启动】状态\n        :type Domain: str\n        """
        self.Domain = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StopCdnDomainResponse(AbstractModel):
    """StopCdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class StopScdnDomainRequest(AbstractModel):
    """StopScdnDomain请求参数结构体

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
        


class StopScdnDomainResponse(AbstractModel):
    """StopScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 关闭结果，Success表示成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class SummarizedData(AbstractModel):
    """明细数据的汇总值，各指标根据其特性不同拥有不同汇总方式

    """

    def __init__(self):
        """
        :param Name: 汇总方式，存在以下几种：
sum：累加求和
max：最大值，带宽模式下，采用 5 分钟粒度汇总数据，计算峰值带宽
avg：平均值\n        :type Name: str\n        :param Value: 汇总后的数据值\n        :type Value: float\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Tag(AbstractModel):
    """域名标签配置

    """

    def __init__(self):
        """
        :param TagKey: 标签键
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagKey: str\n        :param TagValue: 标签值
注意：此字段可能返回 null，表示取不到有效值。\n        :type TagValue: str\n        """
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
        


class TimestampData(AbstractModel):
    """时间戳与其对应的数值

    """

    def __init__(self):
        """
        :param Time: 数据统计时间点，采用向前汇总模式
以 5 分钟粒度为例，13:35:00 时间点代表的统计数据区间为 13:35:00 至 13:39:59\n        :type Time: str\n        :param Value: 数据值\n        :type Value: float\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopData(AbstractModel):
    """排序类型数据结构

    """

    def __init__(self):
        """
        :param Resource: 资源名称，根据查询条件不同分为以下几类：
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据\n        :type Resource: str\n        :param DetailData: 排序结果详情\n        :type DetailData: list of TopDetailData\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopDetailData(AbstractModel):
    """排序类型的数据结构

    """

    def __init__(self):
        """
        :param Name: 数据类型的名称\n        :type Name: str\n        :param Value: 数据值\n        :type Value: float\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TopicInfo(AbstractModel):
    """CLS主题信息

    """

    def __init__(self):
        """
        :param TopicId: 主题ID\n        :type TopicId: str\n        :param TopicName: 主题名字\n        :type TopicName: str\n        :param Enabled: 是否启用投递\n        :type Enabled: int\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param Channel: 归属于cdn或ecdn
注意：此字段可能返回 null，表示取不到有效值。\n        :type Channel: str\n        """
        self.TopicId = None
        self.TopicName = None
        self.Enabled = None
        self.CreateTime = None
        self.Channel = None


    def _deserialize(self, params):
        self.TopicId = params.get("TopicId")
        self.TopicName = params.get("TopicName")
        self.Enabled = params.get("Enabled")
        self.CreateTime = params.get("CreateTime")
        self.Channel = params.get("Channel")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TpgAdapter(AbstractModel):
    """图片优化-TpgAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 开关，"on/off"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TrafficPackage(AbstractModel):
    """CDN加速流量包。

    """

    def __init__(self):
        """
        :param Id: 流量包 Id\n        :type Id: int\n        :param Type: 流量包类型\n        :type Type: str\n        :param Bytes: 流量包大小（单位为 Byte）\n        :type Bytes: int\n        :param BytesUsed: 已消耗流量（单位为 Byte）\n        :type BytesUsed: int\n        :param Status: 流量包状态
enabled：已启用
expired：已过期
disabled：未启用\n        :type Status: str\n        :param CreateTime: 流量包发放时间\n        :type CreateTime: str\n        :param EnableTime: 流量包生效时间\n        :type EnableTime: str\n        :param ExpireTime: 流量包过期时间\n        :type ExpireTime: str\n        :param ContractExtension: 流量包是否续订\n        :type ContractExtension: bool\n        :param AutoExtension: 流量包是否自动续订\n        :type AutoExtension: bool\n        :param Channel: 流量包来源\n        :type Channel: str\n        :param Area: 流量包生效区域，目前仅支持mainland\n        :type Area: str\n        :param LifeTimeMonth: 流量包生命周期月数\n        :type LifeTimeMonth: int\n        :param ExtensionAvailable: 流量包是否支持续订\n        :type ExtensionAvailable: bool\n        :param RefundAvailable: 流量包是否支持退费\n        :type RefundAvailable: bool\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param ProjectId: 项目 ID\n        :type ProjectId: int\n        :param Origin: 源站配置\n        :type Origin: :class:`tencentcloud.cdn.v20180606.models.Origin`\n        :param IpFilter: IP 黑白名单配置\n        :type IpFilter: :class:`tencentcloud.cdn.v20180606.models.IpFilter`\n        :param IpFreqLimit: IP 限频配置\n        :type IpFreqLimit: :class:`tencentcloud.cdn.v20180606.models.IpFreqLimit`\n        :param StatusCodeCache: 状态码缓存配置\n        :type StatusCodeCache: :class:`tencentcloud.cdn.v20180606.models.StatusCodeCache`\n        :param Compression: 智能压缩配置\n        :type Compression: :class:`tencentcloud.cdn.v20180606.models.Compression`\n        :param BandwidthAlert: 带宽封顶配置\n        :type BandwidthAlert: :class:`tencentcloud.cdn.v20180606.models.BandwidthAlert`\n        :param RangeOriginPull: Range 回源配置\n        :type RangeOriginPull: :class:`tencentcloud.cdn.v20180606.models.RangeOriginPull`\n        :param FollowRedirect: 301/302 回源跟随配置\n        :type FollowRedirect: :class:`tencentcloud.cdn.v20180606.models.FollowRedirect`\n        :param ErrorPage: 错误码重定向配置（功能灰度中，尚未全量）\n        :type ErrorPage: :class:`tencentcloud.cdn.v20180606.models.ErrorPage`\n        :param RequestHeader: 请求头部配置\n        :type RequestHeader: :class:`tencentcloud.cdn.v20180606.models.RequestHeader`\n        :param ResponseHeader: 响应头部配置\n        :type ResponseHeader: :class:`tencentcloud.cdn.v20180606.models.ResponseHeader`\n        :param DownstreamCapping: 下载速度配置\n        :type DownstreamCapping: :class:`tencentcloud.cdn.v20180606.models.DownstreamCapping`\n        :param CacheKey: 节点缓存键配置\n        :type CacheKey: :class:`tencentcloud.cdn.v20180606.models.CacheKey`\n        :param ResponseHeaderCache: 头部缓存配置\n        :type ResponseHeaderCache: :class:`tencentcloud.cdn.v20180606.models.ResponseHeaderCache`\n        :param VideoSeek: 视频拖拽配置\n        :type VideoSeek: :class:`tencentcloud.cdn.v20180606.models.VideoSeek`\n        :param Cache: 缓存过期时间配置\n        :type Cache: :class:`tencentcloud.cdn.v20180606.models.Cache`\n        :param OriginPullOptimization: 跨国链路优化配置\n        :type OriginPullOptimization: :class:`tencentcloud.cdn.v20180606.models.OriginPullOptimization`\n        :param Https: Https 加速配置\n        :type Https: :class:`tencentcloud.cdn.v20180606.models.Https`\n        :param Authentication: 时间戳防盗链配置\n        :type Authentication: :class:`tencentcloud.cdn.v20180606.models.Authentication`\n        :param Seo: SEO 优化配置\n        :type Seo: :class:`tencentcloud.cdn.v20180606.models.Seo`\n        :param ForceRedirect: 访问协议强制跳转配置\n        :type ForceRedirect: :class:`tencentcloud.cdn.v20180606.models.ForceRedirect`\n        :param Referer: Referer 防盗链配置\n        :type Referer: :class:`tencentcloud.cdn.v20180606.models.Referer`\n        :param MaxAge: 浏览器缓存配置（功能灰度中，尚未全量）\n        :type MaxAge: :class:`tencentcloud.cdn.v20180606.models.MaxAge`\n        :param ServiceType: 域名业务类型
web：静态加速
download：下载加速
media：流媒体点播加速\n        :type ServiceType: str\n        :param SpecificConfig: 地域属性特殊配置
适用于域名境内加速、境外加速配置不一致场景\n        :type SpecificConfig: :class:`tencentcloud.cdn.v20180606.models.SpecificConfig`\n        :param Area: 域名加速区域
mainland：中国境内加速
overseas：中国境外加速
global：全球加速\n        :type Area: str\n        :param OriginPullTimeout: 回源超时配置\n        :type OriginPullTimeout: :class:`tencentcloud.cdn.v20180606.models.OriginPullTimeout`\n        :param AwsPrivateAccess: 回源S3私有鉴权\n        :type AwsPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.AwsPrivateAccess`\n        :param UserAgentFilter: UA黑白名单配置\n        :type UserAgentFilter: :class:`tencentcloud.cdn.v20180606.models.UserAgentFilter`\n        :param AccessControl: 访问控制\n        :type AccessControl: :class:`tencentcloud.cdn.v20180606.models.AccessControl`\n        :param UrlRedirect: URL重定向配置\n        :type UrlRedirect: :class:`tencentcloud.cdn.v20180606.models.UrlRedirect`\n        :param AccessPort: 访问端口配置\n        :type AccessPort: list of int\n        :param AdvancedAuthentication: 时间戳防盗链高级版配置，白名单功能\n        :type AdvancedAuthentication: :class:`tencentcloud.cdn.v20180606.models.AdvancedAuthentication`\n        :param OriginAuthentication: 回源鉴权高级版配置，白名单功能\n        :type OriginAuthentication: :class:`tencentcloud.cdn.v20180606.models.OriginAuthentication`\n        :param Ipv6Access: Ipv6 访问配置\n        :type Ipv6Access: :class:`tencentcloud.cdn.v20180606.models.Ipv6Access`\n        :param OfflineCache: 离线缓存\n        :type OfflineCache: :class:`tencentcloud.cdn.v20180606.models.OfflineCache`\n        :param OriginCombine: 合并回源\n        :type OriginCombine: :class:`tencentcloud.cdn.v20180606.models.OriginCombine`\n        :param Quic: QUIC正在内测中，请先提交内测申请，详情请前往QUIC产品文档。\n        :type Quic: :class:`tencentcloud.cdn.v20180606.models.Quic`\n        :param OssPrivateAccess: 回源OSS私有鉴权\n        :type OssPrivateAccess: :class:`tencentcloud.cdn.v20180606.models.OssPrivateAccess`\n        :param WebSocket: WebSocket配置\n        :type WebSocket: :class:`tencentcloud.cdn.v20180606.models.WebSocket`\n        """
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
        self.OssPrivateAccess = None
        self.WebSocket = None


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
        if params.get("OssPrivateAccess") is not None:
            self.OssPrivateAccess = OssPrivateAccess()
            self.OssPrivateAccess._deserialize(params.get("OssPrivateAccess"))
        if params.get("WebSocket") is not None:
            self.WebSocket = WebSocket()
            self.WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateDomainConfigResponse(AbstractModel):
    """UpdateDomainConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateImageConfigRequest(AbstractModel):
    """UpdateImageConfig请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param WebpAdapter: WebpAdapter配置项\n        :type WebpAdapter: :class:`tencentcloud.cdn.v20180606.models.WebpAdapter`\n        :param TpgAdapter: TpgAdapter配置项\n        :type TpgAdapter: :class:`tencentcloud.cdn.v20180606.models.TpgAdapter`\n        :param GuetzliAdapter: GuetzliAdapter配置项\n        :type GuetzliAdapter: :class:`tencentcloud.cdn.v20180606.models.GuetzliAdapter`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateImageConfigResponse(AbstractModel):
    """UpdateImageConfig返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdatePayTypeRequest(AbstractModel):
    """UpdatePayType请求参数结构体

    """

    def __init__(self):
        """
        :param Area: 计费区域，mainland或overseas。\n        :type Area: str\n        :param PayType: 计费类型，flux或bandwidth。\n        :type PayType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdatePayTypeResponse(AbstractModel):
    """UpdatePayType返回参数结构体

    """

    def __init__(self):
        """
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class UpdateScdnDomainRequest(AbstractModel):
    """UpdateScdnDomain请求参数结构体

    """

    def __init__(self):
        """
        :param Domain: 域名\n        :type Domain: str\n        :param Waf: Web 攻击防护（WAF）配置\n        :type Waf: :class:`tencentcloud.cdn.v20180606.models.ScdnWafConfig`\n        :param Acl: 自定义防护策略配置\n        :type Acl: :class:`tencentcloud.cdn.v20180606.models.ScdnAclConfig`\n        :param CC: CC 防护配置，目前 CC 防护默认开启\n        :type CC: :class:`tencentcloud.cdn.v20180606.models.ScdnConfig`\n        :param Ddos: DDOS 防护配置，目前 DDoS 防护默认开启\n        :type Ddos: :class:`tencentcloud.cdn.v20180606.models.ScdnDdosConfig`\n        :param Bot: BOT 防护配置\n        :type Bot: :class:`tencentcloud.cdn.v20180606.models.ScdnBotConfig`\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UpdateScdnDomainResponse(AbstractModel):
    """UpdateScdnDomain返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 提交结果，Success表示成功\n        :type Result: str\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class UrlRecord(AbstractModel):
    """封禁url的详细信息

    """

    def __init__(self):
        """
        :param Status: 状态(disable表示封禁，enable表示解封)
注意：此字段可能返回 null，表示取不到有效值。\n        :type Status: str\n        :param RealUrl: 对应的url
注意：此字段可能返回 null，表示取不到有效值。\n        :type RealUrl: str\n        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type CreateTime: str\n        :param UpdateTime: 更新时间
注意：此字段可能返回 null，表示取不到有效值。\n        :type UpdateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirect(AbstractModel):
    """URL重定向配置

    """

    def __init__(self):
        """
        :param Switch: URL重定向配置开关
on：开启
off：关闭\n        :type Switch: str\n        :param PathRules: URL重定向规则，当Switch为on时必填，规则数量最大为10个。
注意：此字段可能返回 null，表示取不到有效值。\n        :type PathRules: list of UrlRedirectRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UrlRedirectRule(AbstractModel):
    """Url重定向规则配置

    """

    def __init__(self):
        """
        :param RedirectStatusCode: 重定向状态码，301 | 302\n        :type RedirectStatusCode: int\n        :param Pattern: 待匹配的Url，仅支持Url路径，不支持参数。默认完全匹配，支持通配符 *，最多支持5个通配符，最大长度1024字符。\n        :type Pattern: str\n        :param RedirectUrl: 目标URL，必须以“/”开头，不包含参数部分。最大长度1024字符。可使用$1, $2, $3, $4, $5分别捕获匹配路径中的通配符号，最多支持10个捕获值。\n        :type RedirectUrl: str\n        :param RedirectHost: 目标host，必须以http://或https://开头，并填写标准格式域名，如果不填写，默认为http:// + 当前域名
注意：此字段可能返回 null，表示取不到有效值。\n        :type RedirectHost: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UserAgentFilter(AbstractModel):
    """UserAgent黑白名单配置

    """

    def __init__(self):
        """
        :param Switch: 开关，on或off
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        :param FilterRules: UA黑白名单生效规则列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterRules: list of UserAgentFilterRule\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


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
注意：此字段可能返回 null，表示取不到有效值。\n        :type RuleType: str\n        :param RulePaths: 访问路径生效内容
注意：此字段可能返回 null，表示取不到有效值。\n        :type RulePaths: list of str\n        :param UserAgents: UserAgent列表
注意：此字段可能返回 null，表示取不到有效值。\n        :type UserAgents: list of str\n        :param FilterType: 黑名单或白名单，blacklist或whitelist
注意：此字段可能返回 null，表示取不到有效值。\n        :type FilterType: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class VerifyDomainRecordRequest(AbstractModel):
    """VerifyDomainRecord请求参数结构体

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
        


class VerifyDomainRecordResponse(AbstractModel):
    """VerifyDomainRecord返回参数结构体

    """

    def __init__(self):
        """
        :param Result: 是否验证成功\n        :type Result: bool\n        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。\n        :type RequestId: str\n        """
        self.Result = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Result = params.get("Result")
        self.RequestId = params.get("RequestId")


class VideoSeek(AbstractModel):
    """视频拖拽配置，默认为关闭状态

    """

    def __init__(self):
        """
        :param Switch: 视频拖拽开关
on：开启
off：关闭\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ViolationUrl(AbstractModel):
    """违规 URL 详情

    """

    def __init__(self):
        """
        :param Id: ID\n        :type Id: int\n        :param RealUrl: 违规资源原始访问 URL\n        :type RealUrl: str\n        :param DownloadUrl: 快照路径，用于控制台展示违规内容快照\n        :type DownloadUrl: str\n        :param UrlStatus: 违规资源当前状态
forbid：已封禁
release：已解封
delay ： 延迟处理
reject ：申诉驳回，状态仍为封禁态
complain：申诉进行中\n        :type UrlStatus: str\n        :param CreateTime: 创建时间\n        :type CreateTime: str\n        :param UpdateTime: 更新时间\n        :type UpdateTime: str\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WafSubRuleStatus(AbstractModel):
    """Waf子规则开关状态

    """

    def __init__(self):
        """
        :param Switch: 子规则状态，on|off\n        :type Switch: str\n        :param SubIds: 规则id列表\n        :type SubIds: list of int\n        """
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebSocket(AbstractModel):
    """WebSocket配置

    """

    def __init__(self):
        """
        :param Switch: WebSocket 超时配置开关, 开关为off时，平台仍支持WebSocket连接，此时超时时间默认为15秒，若需要调整超时时间，将开关置为on.

* WebSocket 为内测功能,如需使用,请联系腾讯云工程师开白.\n        :type Switch: str\n        :param Timeout: 设置超时时间，单位为秒，最大超时时间65秒。
注意：此字段可能返回 null，表示取不到有效值。\n        :type Timeout: int\n        """
        self.Switch = None
        self.Timeout = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        self.Timeout = params.get("Timeout")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class WebpAdapter(AbstractModel):
    """图片优化-WebpAdapter配置

    """

    def __init__(self):
        """
        :param Switch: 开关，"on/off"
注意：此字段可能返回 null，表示取不到有效值。\n        :type Switch: str\n        """
        self.Switch = None


    def _deserialize(self, params):
        self.Switch = params.get("Switch")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        