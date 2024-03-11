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


class AddEcdnDomainRequest(AbstractModel):
    """AddEcdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名。
        :type Domain: str
        :param _Origin: 源站配置。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _Area: 域名加速区域，mainland，overseas或global，分别表示中国境内加速，海外加速或全球加速。
        :type Area: str
        :param _ProjectId: 项目id，默认0。
        :type ProjectId: int
        :param _IpFilter: IP黑白名单配置。
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param _IpFreqLimit: IP限频配置。
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param _ResponseHeader: 源站响应头部配置。
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param _CacheKey: 节点缓存配置。
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param _Cache: 缓存规则配置。
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param _Https: Https配置。
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param _ForceRedirect: 访问协议强制跳转配置。
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param _Tag: 域名绑定的标签
        :type Tag: list of Tag
        :param _WebSocket: WebSocket配置
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self._Domain = None
        self._Origin = None
        self._Area = None
        self._ProjectId = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._ResponseHeader = None
        self._CacheKey = None
        self._Cache = None
        self._Https = None
        self._ForceRedirect = None
        self._Tag = None
        self._WebSocket = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._Area = params.get("Area")
        self._ProjectId = params.get("ProjectId")
        if params.get("IpFilter") is not None:
            self._IpFilter = IpFilter()
            self._IpFilter._deserialize(params.get("IpFilter"))
        if params.get("IpFreqLimit") is not None:
            self._IpFreqLimit = IpFreqLimit()
            self._IpFreqLimit._deserialize(params.get("IpFreqLimit"))
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddEcdnDomainResponse(AbstractModel):
    """AddEcdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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
        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        :param _OriginCertInfo: 源站证书配置信息
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        """
        self._CustomTlsStatus = None
        self._TlsVersion = None
        self._Cipher = None
        self._VerifyOriginType = None
        self._CertInfo = None
        self._OriginCertInfo = None

    @property
    def CustomTlsStatus(self):
        return self._CustomTlsStatus

    @CustomTlsStatus.setter
    def CustomTlsStatus(self, CustomTlsStatus):
        self._CustomTlsStatus = CustomTlsStatus

    @property
    def TlsVersion(self):
        return self._TlsVersion

    @TlsVersion.setter
    def TlsVersion(self, TlsVersion):
        self._TlsVersion = TlsVersion

    @property
    def Cipher(self):
        return self._Cipher

    @Cipher.setter
    def Cipher(self, Cipher):
        self._Cipher = Cipher

    @property
    def VerifyOriginType(self):
        return self._VerifyOriginType

    @VerifyOriginType.setter
    def VerifyOriginType(self, VerifyOriginType):
        self._VerifyOriginType = VerifyOriginType

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def OriginCertInfo(self):
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
        


class Cache(AbstractModel):
    """缓存配置简单版本，该版本不支持设置源站未返回max-age情况下的缓存规则。

    """

    def __init__(self):
        r"""
        :param _CacheRules: 缓存配置规则数组。
        :type CacheRules: list of CacheRule
        :param _FollowOrigin: 遵循源站 Cache-Control: max-age 配置，白名单功能。
on：开启
off：关闭
开启后，未能匹配 CacheRules 规则的资源将根据源站返回的 max-age 值进行节点缓存；匹配了 CacheRules 规则的资源将按照 CacheRules 中设置的缓存过期时间在节点进行缓存
注意：此字段可能返回 null，表示取不到有效值。
        :type FollowOrigin: str
        """
        self._CacheRules = None
        self._FollowOrigin = None

    @property
    def CacheRules(self):
        return self._CacheRules

    @CacheRules.setter
    def CacheRules(self, CacheRules):
        self._CacheRules = CacheRules

    @property
    def FollowOrigin(self):
        return self._FollowOrigin

    @FollowOrigin.setter
    def FollowOrigin(self, FollowOrigin):
        self._FollowOrigin = FollowOrigin


    def _deserialize(self, params):
        if params.get("CacheRules") is not None:
            self._CacheRules = []
            for item in params.get("CacheRules"):
                obj = CacheRule()
                obj._deserialize(item)
                self._CacheRules.append(obj)
        self._FollowOrigin = params.get("FollowOrigin")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheKey(AbstractModel):
    """缓存相关配置。

    """

    def __init__(self):
        r"""
        :param _FullUrlCache: 是否开启全路径缓存，on或off。
        :type FullUrlCache: str
        """
        self._FullUrlCache = None

    @property
    def FullUrlCache(self):
        return self._FullUrlCache

    @FullUrlCache.setter
    def FullUrlCache(self, FullUrlCache):
        self._FullUrlCache = FullUrlCache


    def _deserialize(self, params):
        self._FullUrlCache = params.get("FullUrlCache")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CacheRule(AbstractModel):
    """缓存配置规则。

    """

    def __init__(self):
        r"""
        :param _CacheType: 缓存类型，支持all，file，directory，path，index，分别表示全部文件，后缀类型，目录，完整路径，首页。
        :type CacheType: str
        :param _CacheContents: 缓存内容列表。
        :type CacheContents: list of str
        :param _CacheTime: 缓存时间，单位秒。
        :type CacheTime: int
        """
        self._CacheType = None
        self._CacheContents = None
        self._CacheTime = None

    @property
    def CacheType(self):
        return self._CacheType

    @CacheType.setter
    def CacheType(self, CacheType):
        self._CacheType = CacheType

    @property
    def CacheContents(self):
        return self._CacheContents

    @CacheContents.setter
    def CacheContents(self, CacheContents):
        self._CacheContents = CacheContents

    @property
    def CacheTime(self):
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
        


class ClientCert(AbstractModel):
    """https客户端证书配置。

    """

    def __init__(self):
        r"""
        :param _Certificate: 客户端证书，pem格式。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param _CertName: 客户端证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param _ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DeployTime: 证书颁发时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        """
        self._Certificate = None
        self._CertName = None
        self._ExpireTime = None
        self._DeployTime = None

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
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
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._SubDomain = None
        self._Record = None
        self._RecordType = None
        self._RequestId = None

    @property
    def SubDomain(self):
        return self._SubDomain

    @SubDomain.setter
    def SubDomain(self, SubDomain):
        self._SubDomain = SubDomain

    @property
    def Record(self):
        return self._Record

    @Record.setter
    def Record(self, Record):
        self._Record = Record

    @property
    def RecordType(self):
        return self._RecordType

    @RecordType.setter
    def RecordType(self, RecordType):
        self._RecordType = RecordType

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._SubDomain = params.get("SubDomain")
        self._Record = params.get("Record")
        self._RecordType = params.get("RecordType")
        self._RequestId = params.get("RequestId")


class DeleteEcdnDomainRequest(AbstractModel):
    """DeleteEcdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 待删除域名。
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
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
        


class DeleteEcdnDomainResponse(AbstractModel):
    """DeleteEcdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class DescribeDomainsConfigRequest(AbstractModel):
    """DescribeDomainsConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询的偏移地址，默认0。
        :type Offset: int
        :param _Limit: 分页查询的域名个数，默认100。
        :type Limit: int
        :param _Filters: 查询条件过滤器。
        :type Filters: list of DomainFilter
        :param _Sort: 查询结果排序规则。
        :type Sort: :class:`tencentcloud.ecdn.v20191012.models.Sort`
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None
        self._Sort = None

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

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
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
        :param _Domains: 域名列表。
        :type Domains: list of DomainDetailInfo
        :param _TotalCount: 符合查询条件的域名总数，用于分页查询。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

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
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DomainDetailInfo()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeDomainsRequest(AbstractModel):
    """DescribeDomains请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Offset: 分页查询的偏移地址，默认0。
        :type Offset: int
        :param _Limit: 分页查询的域名个数，默认100，最大支持1000。
        :type Limit: int
        :param _Filters: 查询条件过滤器。
        :type Filters: list of DomainFilter
        """
        self._Offset = None
        self._Limit = None
        self._Filters = None

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

    @property
    def Filters(self):
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
        :param _Domains: 域名信息列表。
        :type Domains: list of DomainBriefInfo
        :param _TotalCount: 域名总个数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Domains = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

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
        if params.get("Domains") is not None:
            self._Domains = []
            for item in params.get("Domains"):
                obj = DomainBriefInfo()
                obj._deserialize(item)
                self._Domains.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEcdnDomainLogsRequest(AbstractModel):
    """DescribeEcdnDomainLogs请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 待查询域名。
        :type Domain: str
        :param _StartTime: 日志起始时间。如：2019-10-01 00:00:00
        :type StartTime: str
        :param _EndTime: 日志结束时间，只支持最近30天内日志查询。2019-10-02 00:00:00
        :type EndTime: str
        :param _Offset: 日志链接列表分页起始地址，默认0。
        :type Offset: int
        :param _Limit: 日志链接列表分页记录条数，默认100，最大1000。
        :type Limit: int
        """
        self._Domain = None
        self._StartTime = None
        self._EndTime = None
        self._Offset = None
        self._Limit = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

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
        self._Domain = params.get("Domain")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnDomainLogsResponse(AbstractModel):
    """DescribeEcdnDomainLogs返回参数结构体

    """

    def __init__(self):
        r"""
        :param _DomainLogs: 日志链接列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainLogs: list of DomainLogs
        :param _TotalCount: 日志链接总条数。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._DomainLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def DomainLogs(self):
        return self._DomainLogs

    @DomainLogs.setter
    def DomainLogs(self, DomainLogs):
        self._DomainLogs = DomainLogs

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
        if params.get("DomainLogs") is not None:
            self._DomainLogs = []
            for item in params.get("DomainLogs"):
                obj = DomainLogs()
                obj._deserialize(item)
                self._DomainLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEcdnDomainStatisticsRequest(AbstractModel):
    """DescribeEcdnDomainStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2019-12-13 00:00:00。
起止时间不超过90天。
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2019-12-13 23:59:59。
起止时间不超过90天。
        :type EndTime: str
        :param _Metrics: 统计指标名称:
flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
        :type Metrics: list of str
        :param _Domains: 指定查询域名列表
        :type Domains: list of str
        :param _Projects: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Projects: list of int
        :param _Offset: 列表分页起始地址，默认0。
        :type Offset: int
        :param _Limit: 列表分页记录条数，默认1000，最大3000。
        :type Limit: int
        :param _Area: 统计区域:
mainland: 境内
oversea: 境外
global: 全部
默认 global
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metrics = None
        self._Domains = None
        self._Projects = None
        self._Offset = None
        self._Limit = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

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

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metrics = params.get("Metrics")
        self._Domains = params.get("Domains")
        self._Projects = params.get("Projects")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnDomainStatisticsResponse(AbstractModel):
    """DescribeEcdnDomainStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 域名数据
        :type Data: list of DomainData
        :param _TotalCount: 数量
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

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
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = DomainData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribeEcdnStatisticsRequest(AbstractModel):
    """DescribeEcdnStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param _StartTime: 查询起始时间，如：2019-12-13 00:00:00
        :type StartTime: str
        :param _EndTime: 查询结束时间，如：2019-12-13 23:59:59
        :type EndTime: str
        :param _Metrics: 指定查询指标，支持的类型有：
flux：流量，单位为 byte
bandwidth：带宽，单位为 bps
request：请求数，单位为 次
2xx：返回 2xx 状态码汇总或者 2 开头状态码数据，单位为 个
3xx：返回 3xx 状态码汇总或者 3 开头状态码数据，单位为 个
4xx：返回 4xx 状态码汇总或者 4 开头状态码数据，单位为 个
5xx：返回 5xx 状态码汇总或者 5 开头状态码数据，单位为 个
        :type Metrics: list of str
        :param _Interval: 时间粒度，支持以下几种模式：
1 天	 1，5，15，30，60，120，240，1440 
2 ~ 3 天	15，30，60，120，240，1440
4 ~ 7 天	30，60，120，240，1440
8 ~ 31 天	 60，120，240，1440
        :type Interval: int
        :param _Domains: 指定查询域名列表

最多可一次性查询30个加速域名。
        :type Domains: list of str
        :param _Projects: 指定要查询的项目 ID，[前往查看项目 ID](https://console.cloud.tencent.com/project)
未填充域名情况下，指定项目查询，若填充了具体域名信息，以域名为主
        :type Projects: list of int
        :param _Area: 统计区域:
mainland: 境内
oversea: 境外
global: 全部
默认 global
        :type Area: str
        """
        self._StartTime = None
        self._EndTime = None
        self._Metrics = None
        self._Interval = None
        self._Domains = None
        self._Projects = None
        self._Area = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def Interval(self):
        return self._Interval

    @Interval.setter
    def Interval(self, Interval):
        self._Interval = Interval

    @property
    def Domains(self):
        return self._Domains

    @Domains.setter
    def Domains(self, Domains):
        self._Domains = Domains

    @property
    def Projects(self):
        return self._Projects

    @Projects.setter
    def Projects(self, Projects):
        self._Projects = Projects

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._Metrics = params.get("Metrics")
        self._Interval = params.get("Interval")
        self._Domains = params.get("Domains")
        self._Projects = params.get("Projects")
        self._Area = params.get("Area")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeEcdnStatisticsResponse(AbstractModel):
    """DescribeEcdnStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 指定条件查询得到的数据明细
        :type Data: list of ResourceData
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = []
            for item in params.get("Data"):
                obj = ResourceData()
                obj._deserialize(item)
                self._Data.append(obj)
        self._RequestId = params.get("RequestId")


class DescribeIpStatusRequest(AbstractModel):
    """DescribeIpStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 加速域名
        :type Domain: str
        :param _Area: 查询区域：
mainland: 国内节点
overseas: 海外节点
global: 全球节点
        :type Area: str
        """
        self._Domain = None
        self._Area = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Area(self):
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
        return self._Ips

    @Ips.setter
    def Ips(self, Ips):
        self._Ips = Ips

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
        if params.get("Ips") is not None:
            self._Ips = []
            for item in params.get("Ips"):
                obj = IpStatus()
                obj._deserialize(item)
                self._Ips.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DescribePurgeQuotaRequest(AbstractModel):
    """DescribePurgeQuota请求参数结构体

    """


class DescribePurgeQuotaResponse(AbstractModel):
    """DescribePurgeQuota返回参数结构体

    """

    def __init__(self):
        r"""
        :param _UrlPurge: Url刷新用量及配额。
        :type UrlPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param _PathPurge: 目录刷新用量及配额。
        :type PathPurge: :class:`tencentcloud.ecdn.v20191012.models.Quota`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._UrlPurge = None
        self._PathPurge = None
        self._RequestId = None

    @property
    def UrlPurge(self):
        return self._UrlPurge

    @UrlPurge.setter
    def UrlPurge(self, UrlPurge):
        self._UrlPurge = UrlPurge

    @property
    def PathPurge(self):
        return self._PathPurge

    @PathPurge.setter
    def PathPurge(self, PathPurge):
        self._PathPurge = PathPurge

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("UrlPurge") is not None:
            self._UrlPurge = Quota()
            self._UrlPurge._deserialize(params.get("UrlPurge"))
        if params.get("PathPurge") is not None:
            self._PathPurge = Quota()
            self._PathPurge._deserialize(params.get("PathPurge"))
        self._RequestId = params.get("RequestId")


class DescribePurgeTasksRequest(AbstractModel):
    """DescribePurgeTasks请求参数结构体

    """

    def __init__(self):
        r"""
        :param _PurgeType: 查询刷新类型。url：查询 url 刷新记录；path：查询目录刷新记录。
        :type PurgeType: str
        :param _StartTime: 开始时间，如2018-08-08 00:00:00。
        :type StartTime: str
        :param _EndTime: 结束时间，如2018-08-08 23:59:59。
        :type EndTime: str
        :param _TaskId: 提交时返回的任务 Id，查询时 TaskId 和起始时间必须指定一项。
        :type TaskId: str
        :param _Offset: 分页查询偏移量，默认为0（从第0条开始）。
        :type Offset: int
        :param _Limit: 分页查询限制数目，默认为20。
        :type Limit: int
        :param _Keyword: 查询关键字，请输入域名或 http(s):// 开头完整 URL。
        :type Keyword: str
        :param _Status: 查询指定任务状态，fail表示失败，done表示成功，process表示刷新中。
        :type Status: str
        """
        self._PurgeType = None
        self._StartTime = None
        self._EndTime = None
        self._TaskId = None
        self._Offset = None
        self._Limit = None
        self._Keyword = None
        self._Status = None

    @property
    def PurgeType(self):
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

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

    @property
    def Keyword(self):
        return self._Keyword

    @Keyword.setter
    def Keyword(self, Keyword):
        self._Keyword = Keyword

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        self._PurgeType = params.get("PurgeType")
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._TaskId = params.get("TaskId")
        self._Offset = params.get("Offset")
        self._Limit = params.get("Limit")
        self._Keyword = params.get("Keyword")
        self._Status = params.get("Status")
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
        :param _PurgeLogs: 刷新历史记录。
        :type PurgeLogs: list of PurgeTask
        :param _TotalCount: 任务总数，用于分页。
        :type TotalCount: int
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._PurgeLogs = None
        self._TotalCount = None
        self._RequestId = None

    @property
    def PurgeLogs(self):
        return self._PurgeLogs

    @PurgeLogs.setter
    def PurgeLogs(self, PurgeLogs):
        self._PurgeLogs = PurgeLogs

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
        if params.get("PurgeLogs") is not None:
            self._PurgeLogs = []
            for item in params.get("PurgeLogs"):
                obj = PurgeTask()
                obj._deserialize(item)
                self._PurgeLogs.append(obj)
        self._TotalCount = params.get("TotalCount")
        self._RequestId = params.get("RequestId")


class DetailData(AbstractModel):
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
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
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
        


class DomainBriefInfo(AbstractModel):
    """CDN域名简要信息。

    """

    def __init__(self):
        r"""
        :param _ResourceId: 域名ID。
        :type ResourceId: str
        :param _AppId: 腾讯云账号ID。
        :type AppId: int
        :param _Domain: CDN加速域名。
        :type Domain: str
        :param _Cname: 域名CName。
        :type Cname: str
        :param _Status: 域名状态，pending，rejected，processing， online，offline，deleted分别表示审核中，审核未通过，审核通过部署中，已开启，已关闭，已删除。
        :type Status: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _CreateTime: 域名创建时间。
        :type CreateTime: str
        :param _UpdateTime: 域名更新时间。
        :type UpdateTime: str
        :param _Origin: 源站配置详情。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _Disable: 域名封禁状态，normal，overdue，quota，malicious，ddos，idle，unlicensed，capping，readonly分别表示 正常，欠费停服，试用客户流量包耗尽，恶意用户，ddos攻击，无流量域名，未备案，带宽封顶，只读
        :type Disable: str
        :param _Area: 加速区域，mainland，oversea或global。
        :type Area: str
        :param _Readonly: 域名锁定状态，normal、global，分别表示未被锁定、全球锁定。
        :type Readonly: str
        :param _Tag: 域名标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._Disable = None
        self._Area = None
        self._Readonly = None
        self._Tag = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
        self._CreateTime = params.get("CreateTime")
        self._UpdateTime = params.get("UpdateTime")
        if params.get("Origin") is not None:
            self._Origin = Origin()
            self._Origin._deserialize(params.get("Origin"))
        self._Disable = params.get("Disable")
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainData(AbstractModel):
    """排序类型数据结构

    """

    def __init__(self):
        r"""
        :param _Resource: 域名
        :type Resource: str
        :param _DetailData: 结果详情
        :type DetailData: list of DetailData
        """
        self._Resource = None
        self._DetailData = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def DetailData(self):
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = DetailData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainDetailInfo(AbstractModel):
    """ECDN域名详细配置信息。

    """

    def __init__(self):
        r"""
        :param _ResourceId: 域名ID。
        :type ResourceId: str
        :param _AppId: 腾讯云账号ID。
        :type AppId: int
        :param _Domain: 加速域名。
        :type Domain: str
        :param _Cname: 域名CName。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cname: str
        :param _Status: 域名状态，pending，rejected，processing， online，offline，deleted分别表示审核中，审核未通过，审核通过部署中，已开启，已关闭，已删除。
        :type Status: str
        :param _ProjectId: 项目ID。
        :type ProjectId: int
        :param _CreateTime: 域名创建时间。
        :type CreateTime: str
        :param _UpdateTime: 域名更新时间。
        :type UpdateTime: str
        :param _Origin: 源站配置。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _IpFilter: IP黑白名单配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param _IpFreqLimit: IP限频配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param _ResponseHeader: 源站响应头部配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param _CacheKey: 节点缓存配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param _Cache: 缓存规则配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param _Https: Https配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param _Disable: 域名封禁状态，normal，overdue，quota，malicious，ddos，idle，unlicensed，capping，readonly分别表示 正常，欠费停服，试用客户流量包耗尽，恶意用户，ddos攻击，无流量域名，未备案，带宽封顶，只读。
注意：此字段可能返回 null，表示取不到有效值。
        :type Disable: str
        :param _ForceRedirect: 访问协议强制跳转配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param _Area: 加速区域，mainland，overseas或global。
注意：此字段可能返回 null，表示取不到有效值。
        :type Area: str
        :param _Readonly: 域名锁定状态，normal、global 分别表示未被锁定，全球锁定。
注意：此字段可能返回 null，表示取不到有效值。
        :type Readonly: str
        :param _Tag: 域名标签。
注意：此字段可能返回 null，表示取不到有效值。
        :type Tag: list of Tag
        :param _WebSocket: WebSocket配置。
注意：此字段可能返回 null，表示取不到有效值。
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self._ResourceId = None
        self._AppId = None
        self._Domain = None
        self._Cname = None
        self._Status = None
        self._ProjectId = None
        self._CreateTime = None
        self._UpdateTime = None
        self._Origin = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._ResponseHeader = None
        self._CacheKey = None
        self._Cache = None
        self._Https = None
        self._Disable = None
        self._ForceRedirect = None
        self._Area = None
        self._Readonly = None
        self._Tag = None
        self._WebSocket = None

    @property
    def ResourceId(self):
        return self._ResourceId

    @ResourceId.setter
    def ResourceId(self, ResourceId):
        self._ResourceId = ResourceId

    @property
    def AppId(self):
        return self._AppId

    @AppId.setter
    def AppId(self, AppId):
        self._AppId = AppId

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Cname(self):
        return self._Cname

    @Cname.setter
    def Cname(self, Cname):
        self._Cname = Cname

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime

    @property
    def UpdateTime(self):
        return self._UpdateTime

    @UpdateTime.setter
    def UpdateTime(self, UpdateTime):
        self._UpdateTime = UpdateTime

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def Disable(self):
        return self._Disable

    @Disable.setter
    def Disable(self, Disable):
        self._Disable = Disable

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def Readonly(self):
        return self._Readonly

    @Readonly.setter
    def Readonly(self, Readonly):
        self._Readonly = Readonly

    @property
    def Tag(self):
        return self._Tag

    @Tag.setter
    def Tag(self, Tag):
        self._Tag = Tag

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket


    def _deserialize(self, params):
        self._ResourceId = params.get("ResourceId")
        self._AppId = params.get("AppId")
        self._Domain = params.get("Domain")
        self._Cname = params.get("Cname")
        self._Status = params.get("Status")
        self._ProjectId = params.get("ProjectId")
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
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        self._Disable = params.get("Disable")
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        self._Area = params.get("Area")
        self._Readonly = params.get("Readonly")
        if params.get("Tag") is not None:
            self._Tag = []
            for item in params.get("Tag"):
                obj = Tag()
                obj._deserialize(item)
                self._Tag.append(obj)
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
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
- status：域名状态，online，offline，processing。
- disable：域名封禁状态，normal，unlicensed。
- projectId：项目ID。
- fullUrlCache：全路径缓存，on或off。
- https：是否配置https，on，off或processing。
- originPullProtocol：回源协议类型，支持http，follow或https。
- area：加速区域，支持mainland，overseas或global。
- tagKey：标签键。
        :type Name: str
        :param _Value: 过滤字段值。
        :type Value: list of str
        :param _Fuzzy: 是否启用模糊查询，仅支持过滤字段名为origin，domain。
        :type Fuzzy: bool
        """
        self._Name = None
        self._Value = None
        self._Fuzzy = None

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def Value(self):
        return self._Value

    @Value.setter
    def Value(self, Value):
        self._Value = Value

    @property
    def Fuzzy(self):
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
        


class DomainLogs(AbstractModel):
    """域名日志信息

    """

    def __init__(self):
        r"""
        :param _StartTime: 日志起始时间。
        :type StartTime: str
        :param _EndTime: 日志结束时间。
        :type EndTime: str
        :param _LogPath: 日志下载路径。
        :type LogPath: str
        """
        self._StartTime = None
        self._EndTime = None
        self._LogPath = None

    @property
    def StartTime(self):
        return self._StartTime

    @StartTime.setter
    def StartTime(self, StartTime):
        self._StartTime = StartTime

    @property
    def EndTime(self):
        return self._EndTime

    @EndTime.setter
    def EndTime(self, EndTime):
        self._EndTime = EndTime

    @property
    def LogPath(self):
        return self._LogPath

    @LogPath.setter
    def LogPath(self, LogPath):
        self._LogPath = LogPath


    def _deserialize(self, params):
        self._StartTime = params.get("StartTime")
        self._EndTime = params.get("EndTime")
        self._LogPath = params.get("LogPath")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class EcdnData(AbstractModel):
    """访问明细数据类型

    """

    def __init__(self):
        r"""
        :param _Metrics: 查询指定的指标名称：Bandwidth，Flux，Request，Delay，状态码，LogBandwidth，LogFlux，LogRequest
        :type Metrics: list of str
        :param _DetailData: 明细数据组合
        :type DetailData: list of TimestampData
        """
        self._Metrics = None
        self._DetailData = None

    @property
    def Metrics(self):
        return self._Metrics

    @Metrics.setter
    def Metrics(self, Metrics):
        self._Metrics = Metrics

    @property
    def DetailData(self):
        return self._DetailData

    @DetailData.setter
    def DetailData(self, DetailData):
        self._DetailData = DetailData


    def _deserialize(self, params):
        self._Metrics = params.get("Metrics")
        if params.get("DetailData") is not None:
            self._DetailData = []
            for item in params.get("DetailData"):
                obj = TimestampData()
                obj._deserialize(item)
                self._DetailData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ForceRedirect(AbstractModel):
    """访问协议强制跳转配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 访问协议强制跳转配置开关，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _RedirectType: 强制跳转访问协议类型，支持http，https，分别表示请求强制跳转http协议，请求强制跳转https协议。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectType: str
        :param _RedirectStatusCode: 强制跳转开启时返回的http状态码，支持301或302。
注意：此字段可能返回 null，表示取不到有效值。
        :type RedirectStatusCode: int
        """
        self._Switch = None
        self._RedirectType = None
        self._RedirectStatusCode = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def RedirectType(self):
        return self._RedirectType

    @RedirectType.setter
    def RedirectType(self, RedirectType):
        self._RedirectType = RedirectType

    @property
    def RedirectStatusCode(self):
        return self._RedirectStatusCode

    @RedirectStatusCode.setter
    def RedirectStatusCode(self, RedirectStatusCode):
        self._RedirectStatusCode = RedirectStatusCode


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._RedirectType = params.get("RedirectType")
        self._RedirectStatusCode = params.get("RedirectStatusCode")
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
        :param _Switch: 是否开启，on或off。
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
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def MaxAge(self):
        return self._MaxAge

    @MaxAge.setter
    def MaxAge(self, MaxAge):
        self._MaxAge = MaxAge

    @property
    def IncludeSubDomains(self):
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
    """分路径的http头部设置规则。

    """

    def __init__(self):
        r"""
        :param _HeaderMode: http头部设置方式，支持add，set或del，分别表示新增，设置或删除头部。
请求头部暂不支持set。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderMode: str
        :param _HeaderName: http头部名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderName: str
        :param _HeaderValue: http头部值。del时可不填写该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderValue: str
        :param _RuleType: 生效的url路径规则类型，支持all，file，directory或path，分别表示全部路径，文件后缀类型，目录或绝对路径生效。
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleType: str
        :param _RulePaths: url路径或文件类型列表。
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
        return self._HeaderMode

    @HeaderMode.setter
    def HeaderMode(self, HeaderMode):
        self._HeaderMode = HeaderMode

    @property
    def HeaderName(self):
        return self._HeaderName

    @HeaderName.setter
    def HeaderName(self, HeaderName):
        self._HeaderName = HeaderName

    @property
    def HeaderValue(self):
        return self._HeaderValue

    @HeaderValue.setter
    def HeaderValue(self, HeaderValue):
        self._HeaderValue = HeaderValue

    @property
    def RuleType(self):
        return self._RuleType

    @RuleType.setter
    def RuleType(self, RuleType):
        self._RuleType = RuleType

    @property
    def RulePaths(self):
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
        


class Https(AbstractModel):
    """域名https配置。

    """

    def __init__(self):
        r"""
        :param _Switch: https配置开关，on或off。开启https配置的域名在部署中状态，开关保持off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Switch: str
        :param _Http2: 是否开启http2，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Http2: str
        :param _OcspStapling: 是否开启OCSP功能，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type OcspStapling: str
        :param _VerifyClient: 是否开启客户端证书校验功能，on或off，开启时必选上传客户端证书信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type VerifyClient: str
        :param _CertInfo: 服务器证书配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertInfo: :class:`tencentcloud.ecdn.v20191012.models.ServerCert`
        :param _ClientCertInfo: 客户端证书配置信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertInfo: :class:`tencentcloud.ecdn.v20191012.models.ClientCert`
        :param _Spdy: 是否开启Spdy，on或off。
注意：此字段可能返回 null，表示取不到有效值。
        :type Spdy: str
        :param _SslStatus: https证书部署状态，closed，deploying，deployed，failed分别表示已关闭，部署中，部署成功，部署失败。不可作为入参使用。
注意：此字段可能返回 null，表示取不到有效值。
        :type SslStatus: str
        :param _Hsts: Hsts配置
注意：此字段可能返回 null，表示取不到有效值。
        :type Hsts: :class:`tencentcloud.ecdn.v20191012.models.Hsts`
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

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Http2(self):
        return self._Http2

    @Http2.setter
    def Http2(self, Http2):
        self._Http2 = Http2

    @property
    def OcspStapling(self):
        return self._OcspStapling

    @OcspStapling.setter
    def OcspStapling(self, OcspStapling):
        self._OcspStapling = OcspStapling

    @property
    def VerifyClient(self):
        return self._VerifyClient

    @VerifyClient.setter
    def VerifyClient(self, VerifyClient):
        self._VerifyClient = VerifyClient

    @property
    def CertInfo(self):
        return self._CertInfo

    @CertInfo.setter
    def CertInfo(self, CertInfo):
        self._CertInfo = CertInfo

    @property
    def ClientCertInfo(self):
        return self._ClientCertInfo

    @ClientCertInfo.setter
    def ClientCertInfo(self, ClientCertInfo):
        self._ClientCertInfo = ClientCertInfo

    @property
    def Spdy(self):
        return self._Spdy

    @Spdy.setter
    def Spdy(self, Spdy):
        self._Spdy = Spdy

    @property
    def SslStatus(self):
        return self._SslStatus

    @SslStatus.setter
    def SslStatus(self, SslStatus):
        self._SslStatus = SslStatus

    @property
    def Hsts(self):
        return self._Hsts

    @Hsts.setter
    def Hsts(self, Hsts):
        self._Hsts = Hsts


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
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFilter(AbstractModel):
    """IP黑白名单。

    """

    def __init__(self):
        r"""
        :param _Switch: IP黑白名单开关，on或off。
        :type Switch: str
        :param _FilterType: IP黑白名单类型，whitelist或blacklist。
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterType: str
        :param _Filters: IP黑白名单列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of str
        """
        self._Switch = None
        self._FilterType = None
        self._Filters = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def FilterType(self):
        return self._FilterType

    @FilterType.setter
    def FilterType(self, FilterType):
        self._FilterType = FilterType

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        self._Switch = params.get("Switch")
        self._FilterType = params.get("FilterType")
        self._Filters = params.get("Filters")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IpFreqLimit(AbstractModel):
    """IP限频配置。

    """

    def __init__(self):
        r"""
        :param _Switch: IP限频配置开关，on或off。
        :type Switch: str
        :param _Qps: 每秒请求数。
注意：此字段可能返回 null，表示取不到有效值。
        :type Qps: int
        """
        self._Switch = None
        self._Qps = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Qps(self):
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
        :param _CreateTime: 节点 IP 添加时间
        :type CreateTime: str
        """
        self._Ip = None
        self._District = None
        self._Isp = None
        self._City = None
        self._Status = None
        self._CreateTime = None

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def District(self):
        return self._District

    @District.setter
    def District(self, District):
        self._District = District

    @property
    def Isp(self):
        return self._Isp

    @Isp.setter
    def Isp(self, Isp):
        self._Isp = Isp

    @property
    def City(self):
        return self._City

    @City.setter
    def City(self, City):
        self._City = City

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def CreateTime(self):
        return self._CreateTime

    @CreateTime.setter
    def CreateTime(self, CreateTime):
        self._CreateTime = CreateTime


    def _deserialize(self, params):
        self._Ip = params.get("Ip")
        self._District = params.get("District")
        self._Isp = params.get("Isp")
        self._City = params.get("City")
        self._Status = params.get("Status")
        self._CreateTime = params.get("CreateTime")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Origin(AbstractModel):
    """源站配置。

    """

    def __init__(self):
        r"""
        :param _Origins: 主源站列表，IP与域名源站不可混填。配置源站端口["origin1:port1", "origin2:port2"]，配置回源权重["origin1::weight1", "origin2::weight2"]，同时配置端口与权重 ["origin1:port1:weight1", "origin2:port2:weight2"]，权重值有效范围为0-100。
        :type Origins: list of str
        :param _OriginType: 主源站类型，支持domain，ip，分别表示域名源站，ip源站。
设置Origins时必须填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginType: str
        :param _ServerName: 回源时Host头部值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerName: str
        :param _OriginPullProtocol: 回源协议类型，支持http，follow，https，分别表示强制http回源，协议跟随回源，https回源。
不传入的情况下默认为http回源.
注意：此字段可能返回 null，表示取不到有效值。
        :type OriginPullProtocol: str
        :param _BackupOrigins: 备份源站列表。
        :type BackupOrigins: list of str
        :param _BackupOriginType: 备份源站类型，同OriginType。
设置BackupOrigins时必须填写。
注意：此字段可能返回 null，表示取不到有效值。
        :type BackupOriginType: str
        :param _AdvanceHttps: HTTPS回源高级配置
注意：此字段可能返回 null，表示取不到有效值。
        :type AdvanceHttps: :class:`tencentcloud.ecdn.v20191012.models.AdvanceHttps`
        """
        self._Origins = None
        self._OriginType = None
        self._ServerName = None
        self._OriginPullProtocol = None
        self._BackupOrigins = None
        self._BackupOriginType = None
        self._AdvanceHttps = None

    @property
    def Origins(self):
        return self._Origins

    @Origins.setter
    def Origins(self, Origins):
        self._Origins = Origins

    @property
    def OriginType(self):
        return self._OriginType

    @OriginType.setter
    def OriginType(self, OriginType):
        self._OriginType = OriginType

    @property
    def ServerName(self):
        return self._ServerName

    @ServerName.setter
    def ServerName(self, ServerName):
        self._ServerName = ServerName

    @property
    def OriginPullProtocol(self):
        return self._OriginPullProtocol

    @OriginPullProtocol.setter
    def OriginPullProtocol(self, OriginPullProtocol):
        self._OriginPullProtocol = OriginPullProtocol

    @property
    def BackupOrigins(self):
        return self._BackupOrigins

    @BackupOrigins.setter
    def BackupOrigins(self, BackupOrigins):
        self._BackupOrigins = BackupOrigins

    @property
    def BackupOriginType(self):
        return self._BackupOriginType

    @BackupOriginType.setter
    def BackupOriginType(self, BackupOriginType):
        self._BackupOriginType = BackupOriginType

    @property
    def AdvanceHttps(self):
        return self._AdvanceHttps

    @AdvanceHttps.setter
    def AdvanceHttps(self, AdvanceHttps):
        self._AdvanceHttps = AdvanceHttps


    def _deserialize(self, params):
        self._Origins = params.get("Origins")
        self._OriginType = params.get("OriginType")
        self._ServerName = params.get("ServerName")
        self._OriginPullProtocol = params.get("OriginPullProtocol")
        self._BackupOrigins = params.get("BackupOrigins")
        self._BackupOriginType = params.get("BackupOriginType")
        if params.get("AdvanceHttps") is not None:
            self._AdvanceHttps = AdvanceHttps()
            self._AdvanceHttps._deserialize(params.get("AdvanceHttps"))
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
        :param _Paths: 要刷新的目录列表，必须包含协议头部。
        :type Paths: list of str
        :param _FlushType: 刷新类型，flush 代表刷新有更新的资源，delete 表示刷新全部资源。
        :type FlushType: str
        """
        self._Paths = None
        self._FlushType = None

    @property
    def Paths(self):
        return self._Paths

    @Paths.setter
    def Paths(self, Paths):
        self._Paths = Paths

    @property
    def FlushType(self):
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType


    def _deserialize(self, params):
        self._Paths = params.get("Paths")
        self._FlushType = params.get("FlushType")
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
        :param _TaskId: 刷新任务Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class PurgeTask(AbstractModel):
    """刷新任务日志详情

    """

    def __init__(self):
        r"""
        :param _TaskId: 刷新任务ID。
        :type TaskId: str
        :param _Url: 刷新Url。
        :type Url: str
        :param _Status: 刷新任务状态，fail表示失败，done表示成功，process表示刷新中。
        :type Status: str
        :param _PurgeType: 刷新类型，url表示url刷新，path表示目录刷新。
        :type PurgeType: str
        :param _FlushType: 刷新资源方式，flush代表刷新更新资源，delete代表刷新全部资源。
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
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def Url(self):
        return self._Url

    @Url.setter
    def Url(self, Url):
        self._Url = Url

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status

    @property
    def PurgeType(self):
        return self._PurgeType

    @PurgeType.setter
    def PurgeType(self, PurgeType):
        self._PurgeType = PurgeType

    @property
    def FlushType(self):
        return self._FlushType

    @FlushType.setter
    def FlushType(self, FlushType):
        self._FlushType = FlushType

    @property
    def CreateTime(self):
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
        :param _Urls: 要刷新的Url列表，必须包含协议头部。
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
        


class PurgeUrlsCacheResponse(AbstractModel):
    """PurgeUrlsCache返回参数结构体

    """

    def __init__(self):
        r"""
        :param _TaskId: 刷新任务Id。
        :type TaskId: str
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._TaskId = None
        self._RequestId = None

    @property
    def TaskId(self):
        return self._TaskId

    @TaskId.setter
    def TaskId(self, TaskId):
        self._TaskId = TaskId

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._TaskId = params.get("TaskId")
        self._RequestId = params.get("RequestId")


class Quota(AbstractModel):
    """刷新用量及刷新配额

    """

    def __init__(self):
        r"""
        :param _Batch: 单次批量提交配额上限。
        :type Batch: int
        :param _Total: 每日提交配额上限。
        :type Total: int
        :param _Available: 每日剩余的可提交配额。
        :type Available: int
        """
        self._Batch = None
        self._Total = None
        self._Available = None

    @property
    def Batch(self):
        return self._Batch

    @Batch.setter
    def Batch(self, Batch):
        self._Batch = Batch

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total

    @property
    def Available(self):
        return self._Available

    @Available.setter
    def Available(self, Available):
        self._Available = Available


    def _deserialize(self, params):
        self._Batch = params.get("Batch")
        self._Total = params.get("Total")
        self._Available = params.get("Available")
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
具体域名：表示该域名明细数据
multiDomains：表示多域名汇总明细数据
项目 ID：指定项目查询时，显示为项目 ID
all：账号维度明细数据
        :type Resource: str
        :param _EcdnData: 资源对应的数据明细
        :type EcdnData: :class:`tencentcloud.ecdn.v20191012.models.EcdnData`
        """
        self._Resource = None
        self._EcdnData = None

    @property
    def Resource(self):
        return self._Resource

    @Resource.setter
    def Resource(self, Resource):
        self._Resource = Resource

    @property
    def EcdnData(self):
        return self._EcdnData

    @EcdnData.setter
    def EcdnData(self, EcdnData):
        self._EcdnData = EcdnData


    def _deserialize(self, params):
        self._Resource = params.get("Resource")
        if params.get("EcdnData") is not None:
            self._EcdnData = EcdnData()
            self._EcdnData._deserialize(params.get("EcdnData"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ResponseHeader(AbstractModel):
    """自定义响应头配置。

    """

    def __init__(self):
        r"""
        :param _Switch: 自定义响应头开关，on或off。
        :type Switch: str
        :param _HeaderRules: 自定义响应头规则数组。
注意：此字段可能返回 null，表示取不到有效值。
        :type HeaderRules: list of HttpHeaderPathRule
        """
        self._Switch = None
        self._HeaderRules = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def HeaderRules(self):
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
        


class ServerCert(AbstractModel):
    """https服务端证书配置。

    """

    def __init__(self):
        r"""
        :param _CertId: 服务器证书id，当证书为腾讯云托管证书时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertId: str
        :param _CertName: 服务器证书名称，当证书为腾讯云托管证书时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertName: str
        :param _Certificate: 服务器证书信息，上传自有证书时必填，必须包含完整的证书链信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Certificate: str
        :param _PrivateKey: 服务器密钥信息，上传自有证书时必填。
注意：此字段可能返回 null，表示取不到有效值。
        :type PrivateKey: str
        :param _ExpireTime: 证书过期时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type ExpireTime: str
        :param _DeployTime: 证书颁发时间。
注意：此字段可能返回 null，表示取不到有效值。
        :type DeployTime: str
        :param _Message: 证书备注信息。
注意：此字段可能返回 null，表示取不到有效值。
        :type Message: str
        """
        self._CertId = None
        self._CertName = None
        self._Certificate = None
        self._PrivateKey = None
        self._ExpireTime = None
        self._DeployTime = None
        self._Message = None

    @property
    def CertId(self):
        return self._CertId

    @CertId.setter
    def CertId(self, CertId):
        self._CertId = CertId

    @property
    def CertName(self):
        return self._CertName

    @CertName.setter
    def CertName(self, CertName):
        self._CertName = CertName

    @property
    def Certificate(self):
        return self._Certificate

    @Certificate.setter
    def Certificate(self, Certificate):
        self._Certificate = Certificate

    @property
    def PrivateKey(self):
        return self._PrivateKey

    @PrivateKey.setter
    def PrivateKey(self, PrivateKey):
        self._PrivateKey = PrivateKey

    @property
    def ExpireTime(self):
        return self._ExpireTime

    @ExpireTime.setter
    def ExpireTime(self, ExpireTime):
        self._ExpireTime = ExpireTime

    @property
    def DeployTime(self):
        return self._DeployTime

    @DeployTime.setter
    def DeployTime(self, DeployTime):
        self._DeployTime = DeployTime

    @property
    def Message(self):
        return self._Message

    @Message.setter
    def Message(self, Message):
        self._Message = Message


    def _deserialize(self, params):
        self._CertId = params.get("CertId")
        self._CertName = params.get("CertName")
        self._Certificate = params.get("Certificate")
        self._PrivateKey = params.get("PrivateKey")
        self._ExpireTime = params.get("ExpireTime")
        self._DeployTime = params.get("DeployTime")
        self._Message = params.get("Message")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """查询结果排序条件。

    """

    def __init__(self):
        r"""
        :param _Key: 排序字段，当前支持：
createTime，域名创建时间
certExpireTime，证书过期时间
        :type Key: str
        :param _Sequence: asc/desc，默认desc。
        :type Sequence: str
        """
        self._Key = None
        self._Sequence = None

    @property
    def Key(self):
        return self._Key

    @Key.setter
    def Key(self, Key):
        self._Key = Key

    @property
    def Sequence(self):
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
        


class StartEcdnDomainRequest(AbstractModel):
    """StartEcdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 待启用域名。
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
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
        


class StartEcdnDomainResponse(AbstractModel):
    """StartEcdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class StopEcdnDomainRequest(AbstractModel):
    """StopEcdnDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 待停用域名。
        :type Domain: str
        """
        self._Domain = None

    @property
    def Domain(self):
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
        


class StopEcdnDomainResponse(AbstractModel):
    """StopEcdnDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
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


class Tag(AbstractModel):
    """标签键和标签值

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
        return self._TagKey

    @TagKey.setter
    def TagKey(self, TagKey):
        self._TagKey = TagKey

    @property
    def TagValue(self):
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
        :type Value: list of float
        """
        self._Time = None
        self._Value = None

    @property
    def Time(self):
        return self._Time

    @Time.setter
    def Time(self, Time):
        self._Time = Time

    @property
    def Value(self):
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
        


class UpdateDomainConfigRequest(AbstractModel):
    """UpdateDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Domain: 域名。
        :type Domain: str
        :param _Origin: 源站配置。
        :type Origin: :class:`tencentcloud.ecdn.v20191012.models.Origin`
        :param _ProjectId: 项目id。
        :type ProjectId: int
        :param _IpFilter: IP黑白名单配置。
        :type IpFilter: :class:`tencentcloud.ecdn.v20191012.models.IpFilter`
        :param _IpFreqLimit: IP限频配置。
        :type IpFreqLimit: :class:`tencentcloud.ecdn.v20191012.models.IpFreqLimit`
        :param _ResponseHeader: 源站响应头部配置。
        :type ResponseHeader: :class:`tencentcloud.ecdn.v20191012.models.ResponseHeader`
        :param _CacheKey: 节点缓存配置。
        :type CacheKey: :class:`tencentcloud.ecdn.v20191012.models.CacheKey`
        :param _Cache: 缓存规则配置。
        :type Cache: :class:`tencentcloud.ecdn.v20191012.models.Cache`
        :param _Https: Https配置。
        :type Https: :class:`tencentcloud.ecdn.v20191012.models.Https`
        :param _ForceRedirect: 访问协议强制跳转配置。
        :type ForceRedirect: :class:`tencentcloud.ecdn.v20191012.models.ForceRedirect`
        :param _Area: 域名加速区域，mainland，overseas或global，分别表示中国境内加速，海外加速或全球加速。
        :type Area: str
        :param _WebSocket: WebSocket配置
        :type WebSocket: :class:`tencentcloud.ecdn.v20191012.models.WebSocket`
        """
        self._Domain = None
        self._Origin = None
        self._ProjectId = None
        self._IpFilter = None
        self._IpFreqLimit = None
        self._ResponseHeader = None
        self._CacheKey = None
        self._Cache = None
        self._Https = None
        self._ForceRedirect = None
        self._Area = None
        self._WebSocket = None

    @property
    def Domain(self):
        return self._Domain

    @Domain.setter
    def Domain(self, Domain):
        self._Domain = Domain

    @property
    def Origin(self):
        return self._Origin

    @Origin.setter
    def Origin(self, Origin):
        self._Origin = Origin

    @property
    def ProjectId(self):
        return self._ProjectId

    @ProjectId.setter
    def ProjectId(self, ProjectId):
        self._ProjectId = ProjectId

    @property
    def IpFilter(self):
        return self._IpFilter

    @IpFilter.setter
    def IpFilter(self, IpFilter):
        self._IpFilter = IpFilter

    @property
    def IpFreqLimit(self):
        return self._IpFreqLimit

    @IpFreqLimit.setter
    def IpFreqLimit(self, IpFreqLimit):
        self._IpFreqLimit = IpFreqLimit

    @property
    def ResponseHeader(self):
        return self._ResponseHeader

    @ResponseHeader.setter
    def ResponseHeader(self, ResponseHeader):
        self._ResponseHeader = ResponseHeader

    @property
    def CacheKey(self):
        return self._CacheKey

    @CacheKey.setter
    def CacheKey(self, CacheKey):
        self._CacheKey = CacheKey

    @property
    def Cache(self):
        return self._Cache

    @Cache.setter
    def Cache(self, Cache):
        self._Cache = Cache

    @property
    def Https(self):
        return self._Https

    @Https.setter
    def Https(self, Https):
        self._Https = Https

    @property
    def ForceRedirect(self):
        return self._ForceRedirect

    @ForceRedirect.setter
    def ForceRedirect(self, ForceRedirect):
        self._ForceRedirect = ForceRedirect

    @property
    def Area(self):
        return self._Area

    @Area.setter
    def Area(self, Area):
        self._Area = Area

    @property
    def WebSocket(self):
        return self._WebSocket

    @WebSocket.setter
    def WebSocket(self, WebSocket):
        self._WebSocket = WebSocket


    def _deserialize(self, params):
        self._Domain = params.get("Domain")
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
        if params.get("ResponseHeader") is not None:
            self._ResponseHeader = ResponseHeader()
            self._ResponseHeader._deserialize(params.get("ResponseHeader"))
        if params.get("CacheKey") is not None:
            self._CacheKey = CacheKey()
            self._CacheKey._deserialize(params.get("CacheKey"))
        if params.get("Cache") is not None:
            self._Cache = Cache()
            self._Cache._deserialize(params.get("Cache"))
        if params.get("Https") is not None:
            self._Https = Https()
            self._Https._deserialize(params.get("Https"))
        if params.get("ForceRedirect") is not None:
            self._ForceRedirect = ForceRedirect()
            self._ForceRedirect._deserialize(params.get("ForceRedirect"))
        self._Area = params.get("Area")
        if params.get("WebSocket") is not None:
            self._WebSocket = WebSocket()
            self._WebSocket._deserialize(params.get("WebSocket"))
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
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        self._RequestId = params.get("RequestId")


class WebSocket(AbstractModel):
    """WebSocket配置。

    """

    def __init__(self):
        r"""
        :param _Switch: WebSocket 超时配置开关, 开关为off时，平台仍支持WebSocket连接，此时超时时间默认为15秒，若需要调整超时时间，将开关置为on.

* WebSocket 为内测功能,如需使用,请联系腾讯云工程师开白.
        :type Switch: str
        :param _Timeout: 设置超时时间，单位为秒，最大超时时间65秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Timeout: int
        """
        self._Switch = None
        self._Timeout = None

    @property
    def Switch(self):
        return self._Switch

    @Switch.setter
    def Switch(self, Switch):
        self._Switch = Switch

    @property
    def Timeout(self):
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
        