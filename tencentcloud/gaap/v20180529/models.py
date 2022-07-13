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


class AccessConfiguration(AbstractModel):
    """通道组加速地域列表，包括加速地域，以及该加速地域对应的带宽和并发配置。

    """

    def __init__(self):
        r"""
        :param AccessRegion: 加速地域。
        :type AccessRegion: str
        :param Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param NetworkType: 网络类型，可取值：normal、cn2，默认值为normal
        :type NetworkType: str
        """
        self.AccessRegion = None
        self.Bandwidth = None
        self.Concurrent = None
        self.NetworkType = None


    def _deserialize(self, params):
        self.AccessRegion = params.get("AccessRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.NetworkType = params.get("NetworkType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRegionDetial(AbstractModel):
    """根据源站查询的可用加速区域信息及对应的可选带宽和并发量。

    """

    def __init__(self):
        r"""
        :param RegionId: 区域ID
        :type RegionId: str
        :param RegionName: 区域的中文或英文名称
        :type RegionName: str
        :param ConcurrentList: 可选的并发量取值数组
        :type ConcurrentList: list of int
        :param BandwidthList: 可选的带宽取值数组
        :type BandwidthList: list of int
        :param RegionArea: 机房所属大区
        :type RegionArea: str
        :param RegionAreaName: 机房所属大区名
        :type RegionAreaName: str
        :param IDCType: 机房类型, dc表示DataCenter数据中心, ec表示EdgeComputing边缘节点
        :type IDCType: str
        :param FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
0，表示不支持该特性；
1，表示支持该特性。
特性位图含义如下（从右往左）：
第1个bit，支持4层加速；
第2个bit，支持7层加速；
第3个bit，支持Http3接入；
第4个bit，支持IPv6；
第5个bit，支持精品BGP接入；
第6个bit，支持三网接入；
第7个bit，支持接入段Qos加速。
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureBitmap: int
        """
        self.RegionId = None
        self.RegionName = None
        self.ConcurrentList = None
        self.BandwidthList = None
        self.RegionArea = None
        self.RegionAreaName = None
        self.IDCType = None
        self.FeatureBitmap = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.ConcurrentList = params.get("ConcurrentList")
        self.BandwidthList = params.get("BandwidthList")
        self.RegionArea = params.get("RegionArea")
        self.RegionAreaName = params.get("RegionAreaName")
        self.IDCType = params.get("IDCType")
        self.FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AccessRegionDomainConf(AbstractModel):
    """域名就近接入配置

    """

    def __init__(self):
        r"""
        :param RegionId: 地域ID。
        :type RegionId: str
        :param NationCountryInnerList: 就近接入区域国家内部编码，编码列表可通过DescribeCountryAreaMapping接口获取。
        :type NationCountryInnerList: list of str
        """
        self.RegionId = None
        self.NationCountryInnerList = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.NationCountryInnerList = params.get("NationCountryInnerList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRealServersRequest(AbstractModel):
    """AddRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 源站对应的项目ID
        :type ProjectId: int
        :param RealServerIP: 源站对应的IP或域名
        :type RealServerIP: list of str
        :param RealServerName: 源站名称
        :type RealServerName: str
        :param TagSet: 标签列表
        :type TagSet: list of TagPair
        """
        self.ProjectId = None
        self.RealServerIP = None
        self.RealServerName = None
        self.TagSet = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerName = params.get("RealServerName")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class AddRealServersResponse(AbstractModel):
    """AddRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RealServerSet: 源站信息列表
        :type RealServerSet: list of NewRealServer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RealServerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = NewRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.RequestId = params.get("RequestId")


class BanAndRecoverProxyRequest(AbstractModel):
    """BanAndRecoverProxy请求参数结构体

    """


class BanAndRecoverProxyResponse(AbstractModel):
    """BanAndRecoverProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BandwidthPriceGradient(AbstractModel):
    """带宽梯度价格

    """

    def __init__(self):
        r"""
        :param BandwidthRange: 带宽范围。
        :type BandwidthRange: list of int
        :param BandwidthUnitPrice: 在对应带宽范围内的单宽单价，单位：元/Mbps/天。
        :type BandwidthUnitPrice: float
        :param DiscountBandwidthUnitPrice: 带宽折扣价，单位：元/Mbps/天。
        :type DiscountBandwidthUnitPrice: float
        """
        self.BandwidthRange = None
        self.BandwidthUnitPrice = None
        self.DiscountBandwidthUnitPrice = None


    def _deserialize(self, params):
        self.BandwidthRange = params.get("BandwidthRange")
        self.BandwidthUnitPrice = params.get("BandwidthUnitPrice")
        self.DiscountBandwidthUnitPrice = params.get("DiscountBandwidthUnitPrice")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindListenerRealServersRequest(AbstractModel):
    """BindListenerRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param RealServerBindSet: 待绑定源站列表。如果该监听器的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self.ListenerId = None
        self.RealServerBindSet = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        if params.get("RealServerBindSet") is not None:
            self.RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self.RealServerBindSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindListenerRealServersResponse(AbstractModel):
    """BindListenerRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class BindRealServer(AbstractModel):
    """已绑定的源站信息

    """

    def __init__(self):
        r"""
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerIP: 源站IP或者域名
        :type RealServerIP: str
        :param RealServerWeight: 该源站所占权重
        :type RealServerWeight: int
        :param RealServerStatus: 源站健康检查状态，其中：
0表示正常；
1表示异常。
未开启健康检查状态时，该状态始终为正常。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerStatus: int
        :param RealServerPort: 源站的端口号
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param DownIPList: 当源站为域名时，域名被解析成一个或者多个IP，该字段表示其中异常的IP列表。状态异常，但该字段为空时，表示域名解析异常。
        :type DownIPList: list of str
        """
        self.RealServerId = None
        self.RealServerIP = None
        self.RealServerWeight = None
        self.RealServerStatus = None
        self.RealServerPort = None
        self.DownIPList = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerWeight = params.get("RealServerWeight")
        self.RealServerStatus = params.get("RealServerStatus")
        self.RealServerPort = params.get("RealServerPort")
        self.DownIPList = params.get("DownIPList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRealServerInfo(AbstractModel):
    """添加源站的源站信息返回值

    """

    def __init__(self):
        r"""
        :param RealServerIP: 源站的IP或域名
        :type RealServerIP: str
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerName: 源站名称
        :type RealServerName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param TagSet: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of TagPair
        """
        self.RealServerIP = None
        self.RealServerId = None
        self.RealServerName = None
        self.ProjectId = None
        self.TagSet = None


    def _deserialize(self, params):
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerId = params.get("RealServerId")
        self.RealServerName = params.get("RealServerName")
        self.ProjectId = params.get("ProjectId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRuleRealServersRequest(AbstractModel):
    """BindRuleRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 转发规则ID
        :type RuleId: str
        :param RealServerBindSet: 需要绑定的源站信息列表。
如果已经存在绑定的源站，则会覆盖更新成这个源站列表。
当不带该字段时，表示解绑该规则上的所有源站。
如果该规则的源站调度策略是加权轮询，需要填写源站权重 RealServerWeight, 不填或者其他调度类型默认源站权重为1。
        :type RealServerBindSet: list of RealServerBindSetReq
        """
        self.RuleId = None
        self.RealServerBindSet = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        if params.get("RealServerBindSet") is not None:
            self.RealServerBindSet = []
            for item in params.get("RealServerBindSet"):
                obj = RealServerBindSetReq()
                obj._deserialize(item)
                self.RealServerBindSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class BindRuleRealServersResponse(AbstractModel):
    """BindRuleRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class Capacity(AbstractModel):
    """接口扩展参数

    """

    def __init__(self):
        r"""
        :param CTCCToken: 电信鉴权的Token
        :type CTCCToken: str
        :param Province: 终端所处在的省份，建议不填写由服务端自动获取，若需填写请填写带有省、市、自治区、特别行政区等后缀的省份中文全称
        :type Province: str
        """
        self.CTCCToken = None
        self.Province = None


    def _deserialize(self, params):
        self.CTCCToken = params.get("CTCCToken")
        self.Province = params.get("Province")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Certificate(AbstractModel):
    """服务器证书

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param CertificateName: 证书名称（旧参数，请使用CertificateAlias）。
        :type CertificateName: str
        :param CertificateType: 证书类型。
        :type CertificateType: int
        :param CertificateAlias: 证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param CreateTime: 证书创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type CreateTime: int
        :param BeginTime: 证书生效起始时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param EndTime: 证书过期时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param IssuerCN: 证书签发者通用名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IssuerCN: str
        :param SubjectCN: 证书主题通用名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectCN: str
        """
        self.CertificateId = None
        self.CertificateName = None
        self.CertificateType = None
        self.CertificateAlias = None
        self.CreateTime = None
        self.BeginTime = None
        self.EndTime = None
        self.IssuerCN = None
        self.SubjectCN = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateName = params.get("CertificateName")
        self.CertificateType = params.get("CertificateType")
        self.CertificateAlias = params.get("CertificateAlias")
        self.CreateTime = params.get("CreateTime")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.IssuerCN = params.get("IssuerCN")
        self.SubjectCN = params.get("SubjectCN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateAliasInfo(AbstractModel):
    """证书别名信息

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param CertificateAlias: 证书别名
        :type CertificateAlias: str
        """
        self.CertificateId = None
        self.CertificateAlias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CertificateDetail(AbstractModel):
    """证书详情，包括证书ID， 证书名字，证书类型，证书内容以及密钥内容。

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID。
        :type CertificateId: str
        :param CertificateType: 证书类型。
        :type CertificateType: int
        :param CertificateAlias: 证书名字。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param CertificateContent: 证书内容。
        :type CertificateContent: str
        :param CertificateKey: 密钥内容。仅当证书类型为SSL证书时，返回该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateKey: str
        :param CreateTime: 创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param BeginTime: 证书生效起始时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
注意：此字段可能返回 null，表示取不到有效值。
        :type BeginTime: int
        :param EndTime: 证书过期时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
注意：此字段可能返回 null，表示取不到有效值。
        :type EndTime: int
        :param IssuerCN: 证书签发者通用名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type IssuerCN: str
        :param SubjectCN: 证书主题通用名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type SubjectCN: str
        """
        self.CertificateId = None
        self.CertificateType = None
        self.CertificateAlias = None
        self.CertificateContent = None
        self.CertificateKey = None
        self.CreateTime = None
        self.BeginTime = None
        self.EndTime = None
        self.IssuerCN = None
        self.SubjectCN = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateType = params.get("CertificateType")
        self.CertificateAlias = params.get("CertificateAlias")
        self.CertificateContent = params.get("CertificateContent")
        self.CertificateKey = params.get("CertificateKey")
        self.CreateTime = params.get("CreateTime")
        self.BeginTime = params.get("BeginTime")
        self.EndTime = params.get("EndTime")
        self.IssuerCN = params.get("IssuerCN")
        self.SubjectCN = params.get("SubjectCN")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckProxyCreateRequest(AbstractModel):
    """CheckProxyCreate请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRegion: 通道的接入(加速)区域。取值可通过接口DescribeAccessRegionsByDestRegion获取到
        :type AccessRegion: str
        :param RealServerRegion: 通道的源站区域。取值可通过接口DescribeDestRegions获取到
        :type RealServerRegion: str
        :param Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param GroupId: 如果在通道组下创建通道，需要填写通道组的ID
        :type GroupId: str
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param NetworkType: 网络类型，可取值：normal、cn2，默认值normal
        :type NetworkType: str
        :param PackageType: 通道套餐类型。Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        :param Http3Supported: 支持Http3的开关，其中：0，表示不需要支持Http3接入；1，表示需要支持Http3接入。注意：如果开启了Http3的功能，那么该通道就不再支持TCP/UDP接入的功能。该功能的启停无法在通道创建完毕后再修改。
        :type Http3Supported: int
        """
        self.AccessRegion = None
        self.RealServerRegion = None
        self.Bandwidth = None
        self.Concurrent = None
        self.GroupId = None
        self.IPAddressVersion = None
        self.NetworkType = None
        self.PackageType = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.AccessRegion = params.get("AccessRegion")
        self.RealServerRegion = params.get("RealServerRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.GroupId = params.get("GroupId")
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.NetworkType = params.get("NetworkType")
        self.PackageType = params.get("PackageType")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CheckProxyCreateResponse(AbstractModel):
    """CheckProxyCreate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CheckFlag: 查询能否创建给定配置的通道，1可以创建，0不可创建。
        :type CheckFlag: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CheckFlag = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CheckFlag = params.get("CheckFlag")
        self.RequestId = params.get("RequestId")


class CloseProxiesRequest(AbstractModel):
    """CloseProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: （旧参数，请切换到ProxyIds）通道的实例ID。
        :type InstanceIds: list of str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param ProxyIds: （新参数）通道的实例ID。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxiesResponse(AbstractModel):
    """CloseProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvalidStatusInstanceSet: 非运行状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class CloseProxyGroupRequest(AbstractModel):
    """CloseProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组的实例 ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseProxyGroupResponse(AbstractModel):
    """CloseProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvalidStatusInstanceSet: 非运行状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class CloseSecurityPolicyRequest(AbstractModel):
    """CloseSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param PolicyId: 安全组策略ID
        :type PolicyId: str
        """
        self.ProxyId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CloseSecurityPolicyResponse(AbstractModel):
    """CloseSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 异步流程ID，可以通过DescribeAsyncTaskStatus 查询流程执行进展和状态
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class CountryAreaMap(AbstractModel):
    """国家地区映射关系（名称和编码）

    """

    def __init__(self):
        r"""
        :param NationCountryName: 国家名称。
        :type NationCountryName: str
        :param NationCountryInnerCode: 国家编码。
        :type NationCountryInnerCode: str
        :param GeographicalZoneName: 地区名称。
        :type GeographicalZoneName: str
        :param GeographicalZoneInnerCode: 地区编码。
        :type GeographicalZoneInnerCode: str
        :param ContinentName: 大洲名称。
        :type ContinentName: str
        :param ContinentInnerCode: 大洲编码。
        :type ContinentInnerCode: str
        :param Remark: 标注信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Remark: str
        """
        self.NationCountryName = None
        self.NationCountryInnerCode = None
        self.GeographicalZoneName = None
        self.GeographicalZoneInnerCode = None
        self.ContinentName = None
        self.ContinentInnerCode = None
        self.Remark = None


    def _deserialize(self, params):
        self.NationCountryName = params.get("NationCountryName")
        self.NationCountryInnerCode = params.get("NationCountryInnerCode")
        self.GeographicalZoneName = params.get("GeographicalZoneName")
        self.GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self.ContinentName = params.get("ContinentName")
        self.ContinentInnerCode = params.get("ContinentInnerCode")
        self.Remark = params.get("Remark")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateRequest(AbstractModel):
    """CreateCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateType: 证书类型。其中：
0，表示基础认证配置；
1，表示客户端CA证书；
2，服务器SSL证书；
3，表示源站CA证书；
4，表示通道SSL证书。
        :type CertificateType: int
        :param CertificateContent: 证书内容。采用url编码。其中：
当证书类型为基础认证配置时，该参数填写用户名/密码对。格式：“用户名：密码”，例如：root:FSGdT。其中密码使用htpasswd或者openssl，例如：openssl passwd -crypt 123456。
当证书类型为CA/SSL证书时，该参数填写证书内容，格式为pem。
        :type CertificateContent: str
        :param CertificateAlias: 证书名称
        :type CertificateAlias: str
        :param CertificateKey: 密钥内容。采用url编码。仅当证书类型为SSL证书时，需要填写该参数。格式为pem。
        :type CertificateKey: str
        """
        self.CertificateType = None
        self.CertificateContent = None
        self.CertificateAlias = None
        self.CertificateKey = None


    def _deserialize(self, params):
        self.CertificateType = params.get("CertificateType")
        self.CertificateContent = params.get("CertificateContent")
        self.CertificateAlias = params.get("CertificateAlias")
        self.CertificateKey = params.get("CertificateKey")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCertificateResponse(AbstractModel):
    """CreateCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID
        :type CertificateId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.RequestId = params.get("RequestId")


class CreateCustomHeaderRequest(AbstractModel):
    """CreateCustomHeader请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则id
        :type RuleId: str
        :param Headers: 新增的header名称和内容列表， ‘’$remote_addr‘’会被解析替换成客户端ip，其他值原样透传到源站。
        :type Headers: list of HttpHeaderParam
        """
        self.RuleId = None
        self.Headers = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self.Headers.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateCustomHeaderResponse(AbstractModel):
    """CreateCustomHeader返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateDomainErrorPageInfoRequest(AbstractModel):
    """CreateDomainErrorPageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param Domain: 域名
        :type Domain: str
        :param ErrorNos: 原始错误码
        :type ErrorNos: list of int
        :param Body: 新的响应包体
        :type Body: str
        :param NewErrorNo: 新错误码
        :type NewErrorNo: int
        :param ClearHeaders: 需要删除的响应头
        :type ClearHeaders: list of str
        :param SetHeaders: 需要设置的响应头
        :type SetHeaders: list of HttpHeaderParam
        """
        self.ListenerId = None
        self.Domain = None
        self.ErrorNos = None
        self.Body = None
        self.NewErrorNo = None
        self.ClearHeaders = None
        self.SetHeaders = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.ErrorNos = params.get("ErrorNos")
        self.Body = params.get("Body")
        self.NewErrorNo = params.get("NewErrorNo")
        self.ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self.SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self.SetHeaders.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainErrorPageInfoResponse(AbstractModel):
    """CreateDomainErrorPageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorPageId: 错误定制响应的配置ID
        :type ErrorPageId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorPageId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ErrorPageId = params.get("ErrorPageId")
        self.RequestId = params.get("RequestId")


class CreateDomainRequest(AbstractModel):
    """CreateDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID。
        :type ListenerId: str
        :param Domain: 需要创建的域名，一个监听器下最大支持100个域名。
        :type Domain: str
        :param CertificateId: 服务器证书，用于客户端与GAAP的HTTPS的交互。
        :type CertificateId: str
        :param ClientCertificateId: 客户端CA证书，用于客户端与GAAP的HTTPS的交互。
仅当采用双向认证的方式时，需要设置该字段或PolyClientCertificateIds字段。
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 客户端CA证书，用于客户端与GAAP的HTTPS的交互。
仅当采用双向认证的方式时，需要设置该字段或ClientCertificateId字段。
        :type PolyClientCertificateIds: list of str
        :param Http3Supported: 是否开启Http3特性的标识，其中：
0，表示不开启Http3；
1，表示开启Http3。
默认不开启Http3。可以通过SetDomainHttp3开启。
        :type Http3Supported: int
        """
        self.ListenerId = None
        self.Domain = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateDomainResponse(AbstractModel):
    """CreateDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class CreateFirstLinkSessionRequest(AbstractModel):
    """CreateFirstLinkSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param TemplateId: 模版ID
        :type TemplateId: str
        :param SrcAddressInfo: 终端网络信息
        :type SrcAddressInfo: :class:`tencentcloud.gaap.v20180529.models.SrcAddressInfo`
        :param DestAddressInfo: 加速目标网络信息
        :type DestAddressInfo: :class:`tencentcloud.gaap.v20180529.models.DestAddressInfo`
        :param DeviceInfo: 终端设备信息
        :type DeviceInfo: :class:`tencentcloud.gaap.v20180529.models.DeviceInfo`
        :param Capacity: 接口扩展参数，如果是电信用户，需要填充CTCC Token字段
        :type Capacity: :class:`tencentcloud.gaap.v20180529.models.Capacity`
        """
        self.TemplateId = None
        self.SrcAddressInfo = None
        self.DestAddressInfo = None
        self.DeviceInfo = None
        self.Capacity = None


    def _deserialize(self, params):
        self.TemplateId = params.get("TemplateId")
        if params.get("SrcAddressInfo") is not None:
            self.SrcAddressInfo = SrcAddressInfo()
            self.SrcAddressInfo._deserialize(params.get("SrcAddressInfo"))
        if params.get("DestAddressInfo") is not None:
            self.DestAddressInfo = DestAddressInfo()
            self.DestAddressInfo._deserialize(params.get("DestAddressInfo"))
        if params.get("DeviceInfo") is not None:
            self.DeviceInfo = DeviceInfo()
            self.DeviceInfo._deserialize(params.get("DeviceInfo"))
        if params.get("Capacity") is not None:
            self.Capacity = Capacity()
            self.Capacity._deserialize(params.get("Capacity"))
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateFirstLinkSessionResponse(AbstractModel):
    """CreateFirstLinkSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 加速成功时返回，单次加速唯一会话Id。。
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionId: str
        :param Duration: 剩余的加速时间，单位秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.SessionId = None
        self.Duration = None
        self.RequestId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        self.Duration = params.get("Duration")
        self.RequestId = params.get("RequestId")


class CreateHTTPListenerRequest(AbstractModel):
    """CreateHTTPListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复
        :type Port: int
        :param ProxyId: 通道ID，与GroupId不能同时设置，对应为通道创建监听器
        :type ProxyId: str
        :param GroupId: 通道组ID，与ProxyId不能同时设置，对应为通道组创建监听器
        :type GroupId: str
        """
        self.ListenerName = None
        self.Port = None
        self.ProxyId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHTTPListenerResponse(AbstractModel):
    """CreateHTTPListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 创建的监听器ID
        :type ListenerId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RequestId = params.get("RequestId")


class CreateHTTPSListenerRequest(AbstractModel):
    """CreateHTTPSListener请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器端口，基于同种传输层协议（TCP 或 UDP）的监听器，端口不可重复
        :type Port: int
        :param CertificateId: 服务器证书ID
        :type CertificateId: str
        :param ForwardProtocol: 加速通道转发到源站的协议类型：HTTP | HTTPS
        :type ForwardProtocol: str
        :param ProxyId: 通道ID，与GroupId之间只能设置一个。表示创建通道的监听器。
        :type ProxyId: str
        :param AuthType: 认证类型，其中：
0，单向认证；
1，双向认证。
默认使用单向认证。
        :type AuthType: int
        :param ClientCertificateId: 客户端CA单证书ID，仅当双向认证时设置该参数或PolyClientCertificateIds参数
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 新的客户端多CA证书ID，仅当双向认证时设置该参数或设置ClientCertificateId参数
        :type PolyClientCertificateIds: list of str
        :param GroupId: 通道组ID，与ProxyId之间只能设置一个。表示创建通道组的监听器。
        :type GroupId: str
        :param Http3Supported: 支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
该功能的启停无法在监听器创建完毕后再修改。
        :type Http3Supported: int
        """
        self.ListenerName = None
        self.Port = None
        self.CertificateId = None
        self.ForwardProtocol = None
        self.ProxyId = None
        self.AuthType = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None
        self.GroupId = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.CertificateId = params.get("CertificateId")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.ProxyId = params.get("ProxyId")
        self.AuthType = params.get("AuthType")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        self.GroupId = params.get("GroupId")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateHTTPSListenerResponse(AbstractModel):
    """CreateHTTPSListener返回参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 创建的监听器ID
        :type ListenerId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RequestId = params.get("RequestId")


class CreateProxyGroupDomainRequest(AbstractModel):
    """CreateProxyGroupDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 需要开启域名的通道组ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyGroupDomainResponse(AbstractModel):
    """CreateProxyGroupDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID。
        :type GroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateProxyGroupRequest(AbstractModel):
    """CreateProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 通道组所属项目ID
        :type ProjectId: int
        :param GroupName: 通道组别名
        :type GroupName: str
        :param RealServerRegion: 源站地域，参考接口DescribeDestRegions 返回参数RegionDetail中的RegionId
        :type RealServerRegion: str
        :param TagSet: 标签列表
        :type TagSet: list of TagPair
        :param AccessRegionSet: 加速地域列表，包括加速地域名，及该地域对应的带宽和并发配置。
        :type AccessRegionSet: list of AccessConfiguration
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param PackageType: 通道组套餐类型，可取值：Thunder、Accelerator，默认值Thunder
        :type PackageType: str
        :param Http3Supported: 支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果开启了Http3的功能，那么该通道组就不再支持TCP/UDP接入的功能。
该功能的启停无法在通道组创建完毕后再修改。
        :type Http3Supported: int
        """
        self.ProjectId = None
        self.GroupName = None
        self.RealServerRegion = None
        self.TagSet = None
        self.AccessRegionSet = None
        self.IPAddressVersion = None
        self.PackageType = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.GroupName = params.get("GroupName")
        self.RealServerRegion = params.get("RealServerRegion")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("AccessRegionSet") is not None:
            self.AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessConfiguration()
                obj._deserialize(item)
                self.AccessRegionSet.append(obj)
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.PackageType = params.get("PackageType")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyGroupResponse(AbstractModel):
    """CreateProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID
        :type GroupId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.RequestId = params.get("RequestId")


class CreateProxyRequest(AbstractModel):
    """CreateProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 通道的项目ID。
        :type ProjectId: int
        :param ProxyName: 通道名称。
        :type ProxyName: str
        :param AccessRegion: 接入地域。
        :type AccessRegion: str
        :param Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param RealServerRegion: 源站地域。当GroupId存在时，源站地域为通道组的源站地域,此时可不填该字段。当GroupId不存在时，需要填写该字段
        :type RealServerRegion: str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param GroupId: 通道所在的通道组ID，当在通道组中创建通道时必带，否则忽略该字段。
        :type GroupId: str
        :param TagSet: 通道需要添加的标签列表。
        :type TagSet: list of TagPair
        :param ClonedProxyId: 被复制的通道ID。只有处于运行中状态的通道可以被复制。
当设置该参数时，表示复制该通道。
        :type ClonedProxyId: str
        :param BillingType: 计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）
        :type BillingType: int
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param NetworkType: 网络类型，normal表示常规BGP，cn2表示精品BGP，triple表示三网
        :type NetworkType: str
        :param PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        :param Http3Supported: 支持Http3的开关，其中：0，表示不需要支持Http3接入；1，表示需要支持Http3接入。注意：如果开启了Http3的功能，那么该通道就不再支持TCP/UDP接入的功能。该功能的启停无法在通道创建完毕后再修改。
        :type Http3Supported: int
        """
        self.ProjectId = None
        self.ProxyName = None
        self.AccessRegion = None
        self.Bandwidth = None
        self.Concurrent = None
        self.RealServerRegion = None
        self.ClientToken = None
        self.GroupId = None
        self.TagSet = None
        self.ClonedProxyId = None
        self.BillingType = None
        self.IPAddressVersion = None
        self.NetworkType = None
        self.PackageType = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.ProxyName = params.get("ProxyName")
        self.AccessRegion = params.get("AccessRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.RealServerRegion = params.get("RealServerRegion")
        self.ClientToken = params.get("ClientToken")
        self.GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.ClonedProxyId = params.get("ClonedProxyId")
        self.BillingType = params.get("BillingType")
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.NetworkType = params.get("NetworkType")
        self.PackageType = params.get("PackageType")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateProxyResponse(AbstractModel):
    """CreateProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: 通道的实例ID。
        :type InstanceId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.RequestId = params.get("RequestId")


class CreateRuleRequest(AbstractModel):
    """CreateRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 7层监听器ID
        :type ListenerId: str
        :param Domain: 转发规则的域名
        :type Domain: str
        :param Path: 转发规则的路径
        :type Path: str
        :param RealServerType: 转发规则对应源站的类型，支持IP和DOMAIN类型。
        :type RealServerType: str
        :param Scheduler: 规则转发源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）。
        :type Scheduler: str
        :param HealthCheck: 规则是否开启健康检查，1开启，0关闭。
        :type HealthCheck: int
        :param CheckParams: 源站健康检查相关参数
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param ForwardProtocol: 加速通道转发到源站的协议类型：支持HTTP或HTTPS。
不传递该字段时表示使用对应监听器的ForwardProtocol。
        :type ForwardProtocol: str
        :param ForwardHost: 回源Host。加速通道转发到源站的host，不设置该参数时，使用默认的host设置，即客户端发起的http请求的host。
        :type ForwardHost: str
        :param ServerNameIndicationSwitch: 服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
        :type ServerNameIndicationSwitch: str
        :param ServerNameIndication: 服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
        :type ServerNameIndication: str
        :param ForcedRedirect: HTTP强制跳转HTTPS。输入当前规则对应的域名与地址。
        :type ForcedRedirect: str
        """
        self.ListenerId = None
        self.Domain = None
        self.Path = None
        self.RealServerType = None
        self.Scheduler = None
        self.HealthCheck = None
        self.CheckParams = None
        self.ForwardProtocol = None
        self.ForwardHost = None
        self.ServerNameIndicationSwitch = None
        self.ServerNameIndication = None
        self.ForcedRedirect = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.Path = params.get("Path")
        self.RealServerType = params.get("RealServerType")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self.CheckParams = RuleCheckParams()
            self.CheckParams._deserialize(params.get("CheckParams"))
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.ForwardHost = params.get("ForwardHost")
        self.ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self.ServerNameIndication = params.get("ServerNameIndication")
        self.ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateRuleResponse(AbstractModel):
    """CreateRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 创建转发规则成功返回规则ID
        :type RuleId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.RequestId = params.get("RequestId")


class CreateSecurityPolicyRequest(AbstractModel):
    """CreateSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param DefaultAction: 默认策略：ACCEPT或DROP
        :type DefaultAction: str
        :param ProxyId: 加速通道ID
        :type ProxyId: str
        :param GroupId: 通道组ID
        :type GroupId: str
        """
        self.DefaultAction = None
        self.ProxyId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.DefaultAction = params.get("DefaultAction")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityPolicyResponse(AbstractModel):
    """CreateSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.PolicyId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RequestId = params.get("RequestId")


class CreateSecurityRulesRequest(AbstractModel):
    """CreateSecurityRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RuleList: 访问规则列表
        :type RuleList: list of SecurityPolicyRuleIn
        """
        self.PolicyId = None
        self.RuleList = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleIn()
                obj._deserialize(item)
                self.RuleList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateSecurityRulesResponse(AbstractModel):
    """CreateSecurityRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIdList: 规则ID列表
        :type RuleIdList: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleIdList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleIdList = params.get("RuleIdList")
        self.RequestId = params.get("RequestId")


class CreateTCPListenersRequest(AbstractModel):
    """CreateTCPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerName: 监听器名称。
        :type ListenerName: str
        :param Ports: 监听器端口列表。
        :type Ports: list of int non-negative
        :param Scheduler: 监听器源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）。
        :type Scheduler: str
        :param HealthCheck: 源站是否开启健康检查：1开启，0关闭，UDP监听器不支持健康检查
        :type HealthCheck: int
        :param RealServerType: 监听器对应源站类型，支持IP或者DOMAIN类型。DOMAIN源站类型不支持wrr的源站调度策略。
        :type RealServerType: str
        :param ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param RealServerPorts: 源站端口列表，该参数仅支持v1版本监听器和通道组监听器。
        :type RealServerPorts: list of int non-negative
        :param ClientIPMethod: 监听器获取客户端 IP 的方式，0表示 TOA, 1表示Proxy Protocol
        :type ClientIPMethod: int
        :param FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        """
        self.ListenerName = None
        self.Ports = None
        self.Scheduler = None
        self.HealthCheck = None
        self.RealServerType = None
        self.ProxyId = None
        self.GroupId = None
        self.DelayLoop = None
        self.ConnectTimeout = None
        self.RealServerPorts = None
        self.ClientIPMethod = None
        self.FailoverSwitch = None
        self.HealthyThreshold = None
        self.UnhealthyThreshold = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Ports = params.get("Ports")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        self.RealServerType = params.get("RealServerType")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        self.DelayLoop = params.get("DelayLoop")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.RealServerPorts = params.get("RealServerPorts")
        self.ClientIPMethod = params.get("ClientIPMethod")
        self.FailoverSwitch = params.get("FailoverSwitch")
        self.HealthyThreshold = params.get("HealthyThreshold")
        self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateTCPListenersResponse(AbstractModel):
    """CreateTCPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerIds: 返回监听器ID
        :type ListenerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class CreateUDPListenersRequest(AbstractModel):
    """CreateUDPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Ports: 监听器端口列表
        :type Ports: list of int non-negative
        :param Scheduler: 监听器源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）
        :type Scheduler: str
        :param RealServerType: 监听器对应源站类型，支持IP或者DOMAIN类型
        :type RealServerType: str
        :param ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param RealServerPorts: 源站端口列表，该参数仅支持v1版本监听器和通道组监听器
        :type RealServerPorts: list of int non-negative
        """
        self.ListenerName = None
        self.Ports = None
        self.Scheduler = None
        self.RealServerType = None
        self.ProxyId = None
        self.GroupId = None
        self.RealServerPorts = None


    def _deserialize(self, params):
        self.ListenerName = params.get("ListenerName")
        self.Ports = params.get("Ports")
        self.Scheduler = params.get("Scheduler")
        self.RealServerType = params.get("RealServerType")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        self.RealServerPorts = params.get("RealServerPorts")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class CreateUDPListenersResponse(AbstractModel):
    """CreateUDPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerIds: 返回监听器ID
        :type ListenerIds: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ListenerIds = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.RequestId = params.get("RequestId")


class DeleteCertificateRequest(AbstractModel):
    """DeleteCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 需要删除的证书ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteCertificateResponse(AbstractModel):
    """DeleteCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainErrorPageInfoRequest(AbstractModel):
    """DeleteDomainErrorPageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorPageId: 定制错误响应页的唯一ID，请参考CreateDomainErrorPageInfo的响应
        :type ErrorPageId: str
        """
        self.ErrorPageId = None


    def _deserialize(self, params):
        self.ErrorPageId = params.get("ErrorPageId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainErrorPageInfoResponse(AbstractModel):
    """DeleteDomainErrorPageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteDomainRequest(AbstractModel):
    """DeleteDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param Domain: 需要删除的域名
        :type Domain: str
        :param Force: 是否强制删除已绑定源站的转发规则，0非强制，1强制。
当采用非强制删除时，如果域名下已有规则绑定了源站，则无法删除。
        :type Force: int
        """
        self.ListenerId = None
        self.Domain = None
        self.Force = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteDomainResponse(AbstractModel):
    """DeleteDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteFirstLinkSessionRequest(AbstractModel):
    """DeleteFirstLinkSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 单次加速唯一会话Id
        :type SessionId: str
        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteFirstLinkSessionResponse(AbstractModel):
    """DeleteFirstLinkSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteListenersRequest(AbstractModel):
    """DeleteListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerIds: 待删除的监听器ID列表
        :type ListenerIds: list of str
        :param Force: 已绑定源站的监听器是否允许强制删除，1：允许， 0：不允许
        :type Force: int
        :param GroupId: 通道组ID，该参数和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param ProxyId: 通道ID，该参数和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        """
        self.ListenerIds = None
        self.Force = None
        self.GroupId = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ListenerIds = params.get("ListenerIds")
        self.Force = params.get("Force")
        self.GroupId = params.get("GroupId")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteListenersResponse(AbstractModel):
    """DeleteListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param OperationFailedListenerSet: 删除操作失败的监听器ID列表
        :type OperationFailedListenerSet: list of str
        :param OperationSucceedListenerSet: 删除操作成功的监听器ID列表
        :type OperationSucceedListenerSet: list of str
        :param InvalidStatusListenerSet: 无效的监听器ID列表，如：监听器不存在，监听器对应实例不匹配
        :type InvalidStatusListenerSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.OperationFailedListenerSet = None
        self.OperationSucceedListenerSet = None
        self.InvalidStatusListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.OperationFailedListenerSet = params.get("OperationFailedListenerSet")
        self.OperationSucceedListenerSet = params.get("OperationSucceedListenerSet")
        self.InvalidStatusListenerSet = params.get("InvalidStatusListenerSet")
        self.RequestId = params.get("RequestId")


class DeleteProxyGroupRequest(AbstractModel):
    """DeleteProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 需要删除的通道组ID。
        :type GroupId: str
        :param Force: 强制删除标识。其中：
0，不强制删除，
1，强制删除。
默认为0，当通道组中存在通道或通道组中存在监听器/规则绑定了源站时，且Force为0时，该操作会返回失败。
        :type Force: int
        """
        self.GroupId = None
        self.Force = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteProxyGroupResponse(AbstractModel):
    """DeleteProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteRuleRequest(AbstractModel):
    """DeleteRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 7层监听器ID
        :type ListenerId: str
        :param RuleId: 转发规则ID
        :type RuleId: str
        :param Force: 是否可以强制删除已绑定源站的转发规则，0非强制，1强制
        :type Force: int
        """
        self.ListenerId = None
        self.RuleId = None
        self.Force = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RuleId = params.get("RuleId")
        self.Force = params.get("Force")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteRuleResponse(AbstractModel):
    """DeleteRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityPolicyRequest(AbstractModel):
    """DeleteSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 策略ID
        :type PolicyId: str
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityPolicyResponse(AbstractModel):
    """DeleteSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DeleteSecurityRulesRequest(AbstractModel):
    """DeleteSecurityRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RuleIdList: 访问规则ID列表
        :type RuleIdList: list of str
        """
        self.PolicyId = None
        self.RuleIdList = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        self.RuleIdList = params.get("RuleIdList")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DeleteSecurityRulesResponse(AbstractModel):
    """DeleteSecurityRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeAccessRegionsByDestRegionRequest(AbstractModel):
    """DescribeAccessRegionsByDestRegion请求参数结构体

    """

    def __init__(self):
        r"""
        :param DestRegion: 源站区域：接口DescribeDestRegions返回DestRegionSet中的RegionId字段值
        :type DestRegion: str
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        """
        self.DestRegion = None
        self.IPAddressVersion = None
        self.PackageType = None


    def _deserialize(self, params):
        self.DestRegion = params.get("DestRegion")
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeAccessRegionsByDestRegionResponse(AbstractModel):
    """DescribeAccessRegionsByDestRegion返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 可用加速区域数量
        :type TotalCount: int
        :param AccessRegionSet: 可用加速区域信息列表
        :type AccessRegionSet: list of AccessRegionDetial
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccessRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccessRegionSet") is not None:
            self.AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = AccessRegionDetial()
                obj._deserialize(item)
                self.AccessRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeAccessRegionsRequest(AbstractModel):
    """DescribeAccessRegions请求参数结构体

    """


class DescribeAccessRegionsResponse(AbstractModel):
    """DescribeAccessRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 加速区域总数
        :type TotalCount: int
        :param AccessRegionSet: 加速区域详情列表
        :type AccessRegionSet: list of RegionDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.AccessRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("AccessRegionSet") is not None:
            self.AccessRegionSet = []
            for item in params.get("AccessRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.AccessRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeBlackHeaderRequest(AbstractModel):
    """DescribeBlackHeader请求参数结构体

    """


class DescribeBlackHeaderResponse(AbstractModel):
    """DescribeBlackHeader返回参数结构体

    """

    def __init__(self):
        r"""
        :param BlackHeaders: 禁用的自定义header列表
注意：此字段可能返回 null，表示取不到有效值。
        :type BlackHeaders: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.BlackHeaders = None
        self.RequestId = None


    def _deserialize(self, params):
        self.BlackHeaders = params.get("BlackHeaders")
        self.RequestId = params.get("RequestId")


class DescribeCertificateDetailRequest(AbstractModel):
    """DescribeCertificateDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID。
        :type CertificateId: str
        """
        self.CertificateId = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificateDetailResponse(AbstractModel):
    """DescribeCertificateDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateDetail: 证书详情。
        :type CertificateDetail: :class:`tencentcloud.gaap.v20180529.models.CertificateDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertificateDetail") is not None:
            self.CertificateDetail = CertificateDetail()
            self.CertificateDetail._deserialize(params.get("CertificateDetail"))
        self.RequestId = params.get("RequestId")


class DescribeCertificatesRequest(AbstractModel):
    """DescribeCertificates请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateType: 证书类型。其中：
0，表示基础认证配置；
1，表示客户端CA证书；
2，表示服务器SSL证书；
3，表示源站CA证书；
4，表示通道SSL证书。
-1，所有类型。
默认为-1。
        :type CertificateType: int
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 限制数量，默认为20。
        :type Limit: int
        """
        self.CertificateType = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.CertificateType = params.get("CertificateType")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeCertificatesResponse(AbstractModel):
    """DescribeCertificates返回参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateSet: 服务器证书列表，包括证书ID 和证书名称。
        :type CertificateSet: list of Certificate
        :param TotalCount: 满足查询条件的服务器证书总数量。
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CertificateSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CertificateSet") is not None:
            self.CertificateSet = []
            for item in params.get("CertificateSet"):
                obj = Certificate()
                obj._deserialize(item)
                self.CertificateSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeCountryAreaMappingRequest(AbstractModel):
    """DescribeCountryAreaMapping请求参数结构体

    """


class DescribeCountryAreaMappingResponse(AbstractModel):
    """DescribeCountryAreaMapping返回参数结构体

    """

    def __init__(self):
        r"""
        :param CountryAreaMappingList: 国家地区编码映射表。
        :type CountryAreaMappingList: list of CountryAreaMap
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.CountryAreaMappingList = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("CountryAreaMappingList") is not None:
            self.CountryAreaMappingList = []
            for item in params.get("CountryAreaMappingList"):
                obj = CountryAreaMap()
                obj._deserialize(item)
                self.CountryAreaMappingList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeCrossBorderProxiesRequest(AbstractModel):
    """DescribeCrossBorderProxies请求参数结构体

    """


class DescribeCrossBorderProxiesResponse(AbstractModel):
    """DescribeCrossBorderProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class DescribeCustomHeaderRequest(AbstractModel):
    """DescribeCustomHeader请求参数结构体

    """


class DescribeCustomHeaderResponse(AbstractModel):
    """DescribeCustomHeader返回参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则id
注意：此字段可能返回 null，表示取不到有效值。
        :type RuleId: str
        :param Headers: 自定义header列表
注意：此字段可能返回 null，表示取不到有效值。
        :type Headers: list of HttpHeaderParam
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RuleId = None
        self.Headers = None
        self.RequestId = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        if params.get("Headers") is not None:
            self.Headers = []
            for item in params.get("Headers"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self.Headers.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDestRegionsRequest(AbstractModel):
    """DescribeDestRegions请求参数结构体

    """


class DescribeDestRegionsResponse(AbstractModel):
    """DescribeDestRegions返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 源站区域总数
        :type TotalCount: int
        :param DestRegionSet: 源站区域详情列表
        :type DestRegionSet: list of RegionDetail
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DestRegionSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DestRegionSet") is not None:
            self.DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.DestRegionSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoByIdsRequest(AbstractModel):
    """DescribeDomainErrorPageInfoByIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorPageIds: 定制错误ID列表,最多支持10个
        :type ErrorPageIds: list of str
        """
        self.ErrorPageIds = None


    def _deserialize(self, params):
        self.ErrorPageIds = params.get("ErrorPageIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainErrorPageInfoByIdsResponse(AbstractModel):
    """DescribeDomainErrorPageInfoByIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorPageSet: 定制错误响应配置集
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorPageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrorPageSet") is not None:
            self.ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self.ErrorPageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeDomainErrorPageInfoRequest(AbstractModel):
    """DescribeDomainErrorPageInfo请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param Domain: 域名
        :type Domain: str
        """
        self.ListenerId = None
        self.Domain = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDomainErrorPageInfoResponse(AbstractModel):
    """DescribeDomainErrorPageInfo返回参数结构体

    """

    def __init__(self):
        r"""
        :param ErrorPageSet: 定制错误响应配置集
注意：此字段可能返回 null，表示取不到有效值。
        :type ErrorPageSet: list of DomainErrorPageInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ErrorPageSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ErrorPageSet") is not None:
            self.ErrorPageSet = []
            for item in params.get("ErrorPageSet"):
                obj = DomainErrorPageInfo()
                obj._deserialize(item)
                self.ErrorPageSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeFirstLinkSessionRequest(AbstractModel):
    """DescribeFirstLinkSession请求参数结构体

    """

    def __init__(self):
        r"""
        :param SessionId: 单次加速唯一会话Id
        :type SessionId: str
        """
        self.SessionId = None


    def _deserialize(self, params):
        self.SessionId = params.get("SessionId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeFirstLinkSessionResponse(AbstractModel):
    """DescribeFirstLinkSession返回参数结构体

    """

    def __init__(self):
        r"""
        :param Status: 会话状态，具体如下：
1： 加速中；
0： 非加速中。
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        :param Duration: 剩余加速时间，单位秒。
注意：此字段可能返回 null，表示取不到有效值。
        :type Duration: int
        :param SuiteType: 加速套餐类型。
套餐说明如下：
T100K：上/下行保障100kbps；
BD4M：下行带宽保障4Mbps；
BU4M：上行带宽保障4Mbps。
注意：此字段可能返回 null，表示取不到有效值。
        :type SuiteType: str
        :param SrcPublicIpv4: 加速终端的公网ip
注意：此字段可能返回 null，表示取不到有效值。
        :type SrcPublicIpv4: str
        :param DestIpv4: 加速目标ip
注意：此字段可能返回 null，表示取不到有效值。
        :type DestIpv4: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.Status = None
        self.Duration = None
        self.SuiteType = None
        self.SrcPublicIpv4 = None
        self.DestIpv4 = None
        self.RequestId = None


    def _deserialize(self, params):
        self.Status = params.get("Status")
        self.Duration = params.get("Duration")
        self.SuiteType = params.get("SuiteType")
        self.SrcPublicIpv4 = params.get("SrcPublicIpv4")
        self.DestIpv4 = params.get("DestIpv4")
        self.RequestId = params.get("RequestId")


class DescribeGroupAndStatisticsProxyRequest(AbstractModel):
    """DescribeGroupAndStatisticsProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupAndStatisticsProxyResponse(AbstractModel):
    """DescribeGroupAndStatisticsProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param GroupSet: 可以统计的通道组信息
        :type GroupSet: list of GroupStatisticsInfo
        :param TotalCount: 通道组数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.GroupSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("GroupSet") is not None:
            self.GroupSet = []
            for item in params.get("GroupSet"):
                obj = GroupStatisticsInfo()
                obj._deserialize(item)
                self.GroupSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeGroupDomainConfigRequest(AbstractModel):
    """DescribeGroupDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeGroupDomainConfigResponse(AbstractModel):
    """DescribeGroupDomainConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRegionList: 域名解析就近接入配置列表。
        :type AccessRegionList: list of DomainAccessRegionDict
        :param DefaultDnsIp: 默认访问Ip。
        :type DefaultDnsIp: str
        :param GroupId: 通道组ID。
        :type GroupId: str
        :param AccessRegionCount: 接入地域的配置的总数。
        :type AccessRegionCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.AccessRegionList = None
        self.DefaultDnsIp = None
        self.GroupId = None
        self.AccessRegionCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("AccessRegionList") is not None:
            self.AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = DomainAccessRegionDict()
                obj._deserialize(item)
                self.AccessRegionList.append(obj)
        self.DefaultDnsIp = params.get("DefaultDnsIp")
        self.GroupId = params.get("GroupId")
        self.AccessRegionCount = params.get("AccessRegionCount")
        self.RequestId = params.get("RequestId")


class DescribeHTTPListenersRequest(AbstractModel):
    """DescribeHTTPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param ListenerId: 过滤条件，按照监听器ID进行精确查询
        :type ListenerId: str
        :param ListenerName: 过滤条件，按照监听器名称进行精确查询
        :type ListenerName: str
        :param Port: 过滤条件，按照监听器端口进行精确查询
        :type Port: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 限制数量，默认为20个
        :type Limit: int
        :param SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :type SearchValue: str
        :param GroupId: 通道组ID
        :type GroupId: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.SearchValue = None
        self.GroupId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchValue = params.get("SearchValue")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHTTPListenersResponse(AbstractModel):
    """DescribeHTTPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 监听器数量
        :type TotalCount: int
        :param ListenerSet: HTTP监听器列表
        :type ListenerSet: list of HTTPListener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeHTTPSListenersRequest(AbstractModel):
    """DescribeHTTPSListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 过滤条件，通道ID
        :type ProxyId: str
        :param ListenerId: 过滤条件，根据监听器ID进行精确查询。
        :type ListenerId: str
        :param ListenerName: 过滤条件，根据监听器名称进行精确查询。
        :type ListenerName: str
        :param Port: 过滤条件，根据监听器端口进行精确查询。
        :type Port: int
        :param Offset: 偏移量， 默认为0
        :type Offset: int
        :param Limit: 限制数量，默认为20
        :type Limit: int
        :param SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询
        :type SearchValue: str
        :param GroupId: 过滤条件，通道组ID
        :type GroupId: str
        :param Http3Supported: 支持Http3的开关，其中：
0，表示不需要支持Http3接入；
1，表示需要支持Http3接入。
注意：如果支持了Http3的功能，那么该监听器会占用对应的UDP接入端口，不可再创建相同端口的UDP监听器。
该功能的启停无法在监听器创建完毕后再修改。
        :type Http3Supported: int
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.SearchValue = None
        self.GroupId = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.SearchValue = params.get("SearchValue")
        self.GroupId = params.get("GroupId")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeHTTPSListenersResponse(AbstractModel):
    """DescribeHTTPSListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 监听器数量
        :type TotalCount: int
        :param ListenerSet: HTTPS监听器列表
        :type ListenerSet: list of HTTPSListener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = HTTPSListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenerRealServersRequest(AbstractModel):
    """DescribeListenerRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        """
        self.ListenerId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerRealServersResponse(AbstractModel):
    """DescribeListenerRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 可绑定源站的个数
        :type TotalCount: int
        :param RealServerSet: 源站信息列表
        :type RealServerSet: list of RealServer
        :param BindRealServerTotalCount: 已绑定源站的个数
        :type BindRealServerTotalCount: int
        :param BindRealServerSet: 已绑定源站信息列表
        :type BindRealServerSet: list of BindRealServer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RealServerSet = None
        self.BindRealServerTotalCount = None
        self.BindRealServerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self.BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.BindRealServerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeListenerStatisticsRequest(AbstractModel):
    """DescribeListenerStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricNames: 统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets。
        :type MetricNames: list of str
        :param Granularity: 监控粒度，目前支持300，3600，86400，单位：秒。
查询时间范围不超过1天，支持最小粒度300秒；
查询间范围不超过7天，支持最小粒度3600秒；
查询间范围超过7天，支持最小粒度86400秒。
        :type Granularity: int
        """
        self.ListenerId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Granularity = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeListenerStatisticsResponse(AbstractModel):
    """DescribeListenerStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsData: 通道组统计数据
        :type StatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxiesRequest(AbstractModel):
    """DescribeProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: （旧参数，请切换到ProxyIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :type InstanceIds: list of str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为100。
        :type Limit: int
        :param Filters: 过滤条件。   
每次请求的Filters的上限为10，Filter.Values的上限为5。参数不支持同时指定InstanceIds和Filters。 
ProjectId - String - 是否必填：否 -（过滤条件）按照项目ID过滤。   
AccessRegion - String - 是否必填：否 - （过滤条件）按照接入地域过滤。    
RealServerRegion - String - 是否必填：否 - （过滤条件）按照源站地域过滤。
GroupId - String - 是否必填：否 - （过滤条件）按照通道组ID过滤。
IPAddressVersion - String - 是否必填：否 - （过滤条件）按照IP版本过滤。
PackageType - String - 是否必填：否 - （过滤条件）按照通道套餐类型过滤。
        :type Filters: list of Filter
        :param ProxyIds: （新参数，替代InstanceIds）按照一个或者多个实例ID查询。每次请求的实例的上限为100。参数不支持同时指定InstanceIds和Filters。
        :type ProxyIds: list of str
        :param TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，通道会被拉取出来。
        :type TagSet: list of TagPair
        :param Independent: 当该字段为1时，仅拉取非通道组的通道，
当该字段为0时，仅拉取通道组的通道，
不存在该字段时，拉取所有通道，包括独立通道和通道组通道。
        :type Independent: int
        :param Order: 输出通道列表的排列顺序。取值范围：
asc：升序排列；
desc：降序排列。
默认为降序。
        :type Order: str
        :param OrderField: 通道列表排序的依据字段。取值范围：
create_time：依据通道的创建时间排序；
proxy_id：依据通道的ID排序；
bandwidth：依据通道带宽上限排序；
concurrent_connections：依据通道并发排序；
默认按通道创建时间排序。
        :type OrderField: str
        """
        self.InstanceIds = None
        self.Offset = None
        self.Limit = None
        self.Filters = None
        self.ProxyIds = None
        self.TagSet = None
        self.Independent = None
        self.Order = None
        self.OrderField = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        self.ProxyIds = params.get("ProxyIds")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.Independent = params.get("Independent")
        self.Order = params.get("Order")
        self.OrderField = params.get("OrderField")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesResponse(AbstractModel):
    """DescribeProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 通道个数。
        :type TotalCount: int
        :param InstanceSet: （旧参数，请切换到ProxySet）通道实例信息列表。
        :type InstanceSet: list of ProxyInfo
        :param ProxySet: （新参数）通道实例信息列表。
        :type ProxySet: list of ProxyInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.InstanceSet = None
        self.ProxySet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("InstanceSet") is not None:
            self.InstanceSet = []
            for item in params.get("InstanceSet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self.InstanceSet.append(obj)
        if params.get("ProxySet") is not None:
            self.ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxyInfo()
                obj._deserialize(item)
                self.ProxySet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxiesStatusRequest(AbstractModel):
    """DescribeProxiesStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: （旧参数，请切换到ProxyIds）通道ID列表。
        :type InstanceIds: list of str
        :param ProxyIds: （新参数）通道ID列表。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxiesStatusResponse(AbstractModel):
    """DescribeProxiesStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceStatusSet: 通道状态列表。
        :type InstanceStatusSet: list of ProxyStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InstanceStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("InstanceStatusSet") is not None:
            self.InstanceStatusSet = []
            for item in params.get("InstanceStatusSet"):
                obj = ProxyStatus()
                obj._deserialize(item)
                self.InstanceStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxyAndStatisticsListenersRequest(AbstractModel):
    """DescribeProxyAndStatisticsListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 项目ID
        :type ProjectId: int
        """
        self.ProjectId = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyAndStatisticsListenersResponse(AbstractModel):
    """DescribeProxyAndStatisticsListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxySet: 可以统计的通道信息
        :type ProxySet: list of ProxySimpleInfo
        :param TotalCount: 通道数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxySet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProxySet") is not None:
            self.ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self.ProxySet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeProxyDetailRequest(AbstractModel):
    """DescribeProxyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 需查询的通道ID。
        :type ProxyId: str
        """
        self.ProxyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyDetailResponse(AbstractModel):
    """DescribeProxyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyDetail: 通道详情信息。
        :type ProxyDetail: :class:`tencentcloud.gaap.v20180529.models.ProxyInfo`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProxyDetail") is not None:
            self.ProxyDetail = ProxyInfo()
            self.ProxyDetail._deserialize(params.get("ProxyDetail"))
        self.RequestId = params.get("RequestId")


class DescribeProxyGroupDetailsRequest(AbstractModel):
    """DescribeProxyGroupDetails请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID。
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupDetailsResponse(AbstractModel):
    """DescribeProxyGroupDetails返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyGroupDetail: 通道组详细信息。
        :type ProxyGroupDetail: :class:`tencentcloud.gaap.v20180529.models.ProxyGroupDetail`
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyGroupDetail = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("ProxyGroupDetail") is not None:
            self.ProxyGroupDetail = ProxyGroupDetail()
            self.ProxyGroupDetail._deserialize(params.get("ProxyGroupDetail"))
        self.RequestId = params.get("RequestId")


class DescribeProxyGroupListRequest(AbstractModel):
    """DescribeProxyGroupList请求参数结构体

    """

    def __init__(self):
        r"""
        :param Offset: 偏移量，默认值为0。
        :type Offset: int
        :param Limit: 返回数量，默认值为20，最大值为100。
        :type Limit: int
        :param ProjectId: 项目ID。取值范围：
-1，该用户下所有项目
0，默认项目
其他值，指定的项目
        :type ProjectId: int
        :param Filters: 过滤条件。   
每次请求的Filter.Values的上限为5。
RealServerRegion - String - 是否必填：否 -（过滤条件）按照源站地域过滤，可参考DescribeDestRegions接口返回结果中的RegionId。
PackageType - String - 是否必填：否 - （过滤条件）通道组类型，Thunder表示标准通道组，Accelerator表示银牌加速通道组。
        :type Filters: list of Filter
        :param TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，该通道组会被拉取出来。
        :type TagSet: list of TagPair
        """
        self.Offset = None
        self.Limit = None
        self.ProjectId = None
        self.Filters = None
        self.TagSet = None


    def _deserialize(self, params):
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.ProjectId = params.get("ProjectId")
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupListResponse(AbstractModel):
    """DescribeProxyGroupList返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 通道组总数。
        :type TotalCount: int
        :param ProxyGroupList: 通道组列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyGroupList: list of ProxyGroupInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ProxyGroupList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ProxyGroupList") is not None:
            self.ProxyGroupList = []
            for item in params.get("ProxyGroupList"):
                obj = ProxyGroupInfo()
                obj._deserialize(item)
                self.ProxyGroupList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxyGroupStatisticsRequest(AbstractModel):
    """DescribeProxyGroupStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID
        :type GroupId: str
        :param StartTime: 起始时间
        :type StartTime: str
        :param EndTime: 结束时间
        :type EndTime: str
        :param MetricNames: 统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets
        :type MetricNames: list of str
        :param Granularity: 监控粒度，目前支持60，300，3600，86400，单位：秒。
当时间范围不超过1天，支持最小粒度60秒；
当时间范围不超过7天，支持最小粒度3600秒；
当时间范围不超过30天，支持最小粒度86400秒。
        :type Granularity: int
        """
        self.GroupId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Granularity = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyGroupStatisticsResponse(AbstractModel):
    """DescribeProxyGroupStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsData: 通道组统计数据
        :type StatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeProxyStatisticsRequest(AbstractModel):
    """DescribeProxyStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param StartTime: 起始时间(2019-03-25 12:00:00)
        :type StartTime: str
        :param EndTime: 结束时间(2019-03-25 12:00:00)
        :type EndTime: str
        :param MetricNames: 统计指标名称列表，支持: 入带宽:InBandwidth, 出带宽:OutBandwidth, 并发:Concurrent, 入包量:InPackets, 出包量:OutPackets, 丢包率:PacketLoss, 延迟:Latency，http请求量：HttpQPS, Https请求量：HttpsQPS
        :type MetricNames: list of str
        :param Granularity: 监控粒度，目前支持60，300，3600，86400，单位：秒。
当时间范围不超过3天，支持最小粒度60秒；
当时间范围不超过7天，支持最小粒度300秒；
当时间范围不超过30天，支持最小粒度3600秒。
        :type Granularity: int
        :param Isp: 运营商（通道为三网通道时有效），支持CMCC，CUCC，CTCC，传空值或不传则合并三个运营商数据
        :type Isp: str
        """
        self.ProxyId = None
        self.StartTime = None
        self.EndTime = None
        self.MetricNames = None
        self.Granularity = None
        self.Isp = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.MetricNames = params.get("MetricNames")
        self.Granularity = params.get("Granularity")
        self.Isp = params.get("Isp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeProxyStatisticsResponse(AbstractModel):
    """DescribeProxyStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsData: 通道统计数据
        :type StatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealServerStatisticsRequest(AbstractModel):
    """DescribeRealServerStatistics请求参数结构体

    """

    def __init__(self):
        r"""
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param RuleId: L7层规则ID
        :type RuleId: str
        :param WithinTime: 统计时长，单位：小时。仅支持最近1,3,6,12,24小时的统计查询
        :type WithinTime: int
        :param StartTime: 统计开始时间(2020-08-19 00:00:00)
        :type StartTime: str
        :param EndTime: 统计结束时间(2020-08-19 23:59:59)
        :type EndTime: str
        :param Granularity: 统计的数据粒度，单位：秒，仅支持1分钟-60和5分钟-300粒度
        :type Granularity: int
        """
        self.RealServerId = None
        self.ListenerId = None
        self.RuleId = None
        self.WithinTime = None
        self.StartTime = None
        self.EndTime = None
        self.Granularity = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.ListenerId = params.get("ListenerId")
        self.RuleId = params.get("RuleId")
        self.WithinTime = params.get("WithinTime")
        self.StartTime = params.get("StartTime")
        self.EndTime = params.get("EndTime")
        self.Granularity = params.get("Granularity")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServerStatisticsResponse(AbstractModel):
    """DescribeRealServerStatistics返回参数结构体

    """

    def __init__(self):
        r"""
        :param StatisticsData: 指定监听器的源站状态统计数据
        :type StatisticsData: list of StatisticsDataInfo
        :param RsStatisticsData: 多个源站状态统计数据
        :type RsStatisticsData: list of MetricStatisticsInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.StatisticsData = None
        self.RsStatisticsData = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("StatisticsData") is not None:
            self.StatisticsData = []
            for item in params.get("StatisticsData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self.StatisticsData.append(obj)
        if params.get("RsStatisticsData") is not None:
            self.RsStatisticsData = []
            for item in params.get("RsStatisticsData"):
                obj = MetricStatisticsInfo()
                obj._deserialize(item)
                self.RsStatisticsData.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRealServersRequest(AbstractModel):
    """DescribeRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 查询源站的所属项目ID，-1表示所有项目
        :type ProjectId: int
        :param SearchValue: 需要查询的源站IP或域名，支持模糊匹配
        :type SearchValue: str
        :param Offset: 偏移量，默认值是0
        :type Offset: int
        :param Limit: 返回数量，默认为20个，最大值为50个
        :type Limit: int
        :param TagSet: 标签列表，当存在该字段时，拉取对应标签下的资源列表。
最多支持5个标签，当存在两个或两个以上的标签时，满足其中任意一个标签时，源站会被拉取出来。
        :type TagSet: list of TagPair
        :param Filters: 过滤条件。filter的name取值(RealServerName,RealServerIP)
        :type Filters: list of Filter
        """
        self.ProjectId = None
        self.SearchValue = None
        self.Offset = None
        self.Limit = None
        self.TagSet = None
        self.Filters = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.SearchValue = params.get("SearchValue")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        if params.get("Filters") is not None:
            self.Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self.Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServersResponse(AbstractModel):
    """DescribeRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RealServerSet: 源站信息列表
        :type RealServerSet: list of BindRealServerInfo
        :param TotalCount: 查询得到的源站数量
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RealServerSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServerInfo()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeRealServersStatusRequest(AbstractModel):
    """DescribeRealServersStatus请求参数结构体

    """

    def __init__(self):
        r"""
        :param RealServerIds: 源站ID列表
        :type RealServerIds: list of str
        """
        self.RealServerIds = None


    def _deserialize(self, params):
        self.RealServerIds = params.get("RealServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRealServersStatusResponse(AbstractModel):
    """DescribeRealServersStatus返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回源站查询结果的个数
        :type TotalCount: int
        :param RealServerStatusSet: 源站被绑定状态列表
        :type RealServerStatusSet: list of RealServerStatus
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RealServerStatusSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RealServerStatusSet") is not None:
            self.RealServerStatusSet = []
            for item in params.get("RealServerStatusSet"):
                obj = RealServerStatus()
                obj._deserialize(item)
                self.RealServerStatusSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRegionAndPriceRequest(AbstractModel):
    """DescribeRegionAndPrice请求参数结构体

    """

    def __init__(self):
        r"""
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        """
        self.IPAddressVersion = None
        self.PackageType = None


    def _deserialize(self, params):
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.PackageType = params.get("PackageType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRegionAndPriceResponse(AbstractModel):
    """DescribeRegionAndPrice返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 源站区域总数
        :type TotalCount: int
        :param DestRegionSet: 源站区域详情列表
        :type DestRegionSet: list of RegionDetail
        :param BandwidthUnitPrice: 通道带宽费用梯度价格
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param Currency: 带宽价格货币类型：
CNY 人民币
USD 美元
        :type Currency: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.DestRegionSet = None
        self.BandwidthUnitPrice = None
        self.Currency = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("DestRegionSet") is not None:
            self.DestRegionSet = []
            for item in params.get("DestRegionSet"):
                obj = RegionDetail()
                obj._deserialize(item)
                self.DestRegionSet.append(obj)
        if params.get("BandwidthUnitPrice") is not None:
            self.BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self.BandwidthUnitPrice.append(obj)
        self.Currency = params.get("Currency")
        self.RequestId = params.get("RequestId")


class DescribeResourcesByTagRequest(AbstractModel):
    """DescribeResourcesByTag请求参数结构体

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键。
        :type TagKey: str
        :param TagValue: 标签值。
        :type TagValue: str
        :param ResourceType: 资源类型，其中：
Proxy表示通道；
ProxyGroup表示通道组；
RealServer表示源站。
不指定该字段则查询该标签下所有资源。
        :type ResourceType: str
        """
        self.TagKey = None
        self.TagValue = None
        self.ResourceType = None


    def _deserialize(self, params):
        self.TagKey = params.get("TagKey")
        self.TagValue = params.get("TagValue")
        self.ResourceType = params.get("ResourceType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeResourcesByTagResponse(AbstractModel):
    """DescribeResourcesByTag返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 资源总数
        :type TotalCount: int
        :param ResourceSet: 标签对应的资源列表
        :type ResourceSet: list of TagResourceInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ResourceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ResourceSet") is not None:
            self.ResourceSet = []
            for item in params.get("ResourceSet"):
                obj = TagResourceInfo()
                obj._deserialize(item)
                self.ResourceSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRuleRealServersRequest(AbstractModel):
    """DescribeRuleRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 转发规则ID
        :type RuleId: str
        :param Offset: 偏移量，默认为0。
        :type Offset: int
        :param Limit: 返回数量，默认为20，最大值为1000。
        :type Limit: int
        """
        self.RuleId = None
        self.Offset = None
        self.Limit = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRuleRealServersResponse(AbstractModel):
    """DescribeRuleRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 可绑定的源站个数
        :type TotalCount: int
        :param RealServerSet: 可绑定的源站信息列表
        :type RealServerSet: list of RealServer
        :param BindRealServerTotalCount: 已绑定的源站个数
        :type BindRealServerTotalCount: int
        :param BindRealServerSet: 已绑定的源站信息列表
        :type BindRealServerSet: list of BindRealServer
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RealServerSet = None
        self.BindRealServerTotalCount = None
        self.BindRealServerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = RealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.BindRealServerTotalCount = params.get("BindRealServerTotalCount")
        if params.get("BindRealServerSet") is not None:
            self.BindRealServerSet = []
            for item in params.get("BindRealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.BindRealServerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesByRuleIdsRequest(AbstractModel):
    """DescribeRulesByRuleIds请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleIds: 规则ID列表。最多支持10个规则。
        :type RuleIds: list of str
        """
        self.RuleIds = None


    def _deserialize(self, params):
        self.RuleIds = params.get("RuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesByRuleIdsResponse(AbstractModel):
    """DescribeRulesByRuleIds返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的规则总个数。
        :type TotalCount: int
        :param RuleSet: 返回的规则列表。
        :type RuleSet: list of RuleInfo
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.RuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeRulesRequest(AbstractModel):
    """DescribeRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 7层监听器Id。
        :type ListenerId: str
        """
        self.ListenerId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeRulesResponse(AbstractModel):
    """DescribeRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param DomainRuleSet: 按照域名分类的规则信息列表
        :type DomainRuleSet: list of DomainRuleSet
        :param TotalCount: 该监听器下的域名总数
        :type TotalCount: int
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.DomainRuleSet = None
        self.TotalCount = None
        self.RequestId = None


    def _deserialize(self, params):
        if params.get("DomainRuleSet") is not None:
            self.DomainRuleSet = []
            for item in params.get("DomainRuleSet"):
                obj = DomainRuleSet()
                obj._deserialize(item)
                self.DomainRuleSet.append(obj)
        self.TotalCount = params.get("TotalCount")
        self.RequestId = params.get("RequestId")


class DescribeSecurityPolicyDetailRequest(AbstractModel):
    """DescribeSecurityPolicyDetail请求参数结构体

    """

    def __init__(self):
        r"""
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self.PolicyId = None


    def _deserialize(self, params):
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityPolicyDetailResponse(AbstractModel):
    """DescribeSecurityPolicyDetail返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 通道ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param Status: 安全策略状态：
BOUND，已开启安全策略
UNBIND，已关闭安全策略
BINDING，安全策略开启中
UNBINDING，安全策略关闭中。
        :type Status: str
        :param DefaultAction: 默认策略：ACCEPT或DROP。
        :type DefaultAction: str
        :param PolicyId: 策略ID
        :type PolicyId: str
        :param RuleList: 规则列表
        :type RuleList: list of SecurityPolicyRuleOut
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyId = None
        self.Status = None
        self.DefaultAction = None
        self.PolicyId = None
        self.RuleList = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.Status = params.get("Status")
        self.DefaultAction = params.get("DefaultAction")
        self.PolicyId = params.get("PolicyId")
        if params.get("RuleList") is not None:
            self.RuleList = []
            for item in params.get("RuleList"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self.RuleList.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeSecurityRulesRequest(AbstractModel):
    """DescribeSecurityRules请求参数结构体

    """

    def __init__(self):
        r"""
        :param SecurityRuleIds: 安全规则ID列表。总数不能超过20个。
        :type SecurityRuleIds: list of str
        """
        self.SecurityRuleIds = None


    def _deserialize(self, params):
        self.SecurityRuleIds = params.get("SecurityRuleIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeSecurityRulesResponse(AbstractModel):
    """DescribeSecurityRules返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 返回的安全规则详情总数。
        :type TotalCount: int
        :param SecurityRuleSet: 返回的安全规则详情列表。
        :type SecurityRuleSet: list of SecurityPolicyRuleOut
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.SecurityRuleSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("SecurityRuleSet") is not None:
            self.SecurityRuleSet = []
            for item in params.get("SecurityRuleSet"):
                obj = SecurityPolicyRuleOut()
                obj._deserialize(item)
                self.SecurityRuleSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeTCPListenersRequest(AbstractModel):
    """DescribeTCPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type ProxyId: str
        :param ListenerId: 过滤条件，根据监听器ID精确查询。
当设置了ProxyId时，会检查该监听器是否归属于该通道。
当设置了GroupId时，会检查该监听器是否归属于该通道组。
        :type ListenerId: str
        :param ListenerName: 过滤条件，根据监听器名称精确查询
        :type ListenerName: str
        :param Port: 过滤条件，根据监听器端口精确查询
        :type Port: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 限制数量，默认为20
        :type Limit: int
        :param GroupId: 过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type GroupId: str
        :param SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :type SearchValue: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeTCPListenersResponse(AbstractModel):
    """DescribeTCPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 满足条件的监听器总个数
        :type TotalCount: int
        :param ListenerSet: TCP监听器列表
        :type ListenerSet: list of TCPListener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = TCPListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DescribeUDPListenersRequest(AbstractModel):
    """DescribeUDPListeners请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 过滤条件，根据通道ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type ProxyId: str
        :param ListenerId: 过滤条件，根据监听器ID精确查询。
当设置了ProxyId时，会检查该监听器是否归属于该通道。
当设置了GroupId时，会检查该监听器是否归属于该通道组。
        :type ListenerId: str
        :param ListenerName: 过滤条件，根据监听器名称精确查询
        :type ListenerName: str
        :param Port: 过滤条件，根据监听器端口精确查询
        :type Port: int
        :param Offset: 偏移量，默认为0
        :type Offset: int
        :param Limit: 限制数量，默认为20
        :type Limit: int
        :param GroupId: 过滤条件，根据通道组ID进行拉取，ProxyId/GroupId/ListenerId必须设置一个，但ProxyId和GroupId不能同时设置。
        :type GroupId: str
        :param SearchValue: 过滤条件，支持按照端口或监听器名称进行模糊查询，该参数不能与ListenerName和Port同时使用
        :type SearchValue: str
        """
        self.ProxyId = None
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Offset = None
        self.Limit = None
        self.GroupId = None
        self.SearchValue = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Offset = params.get("Offset")
        self.Limit = params.get("Limit")
        self.GroupId = params.get("GroupId")
        self.SearchValue = params.get("SearchValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeUDPListenersResponse(AbstractModel):
    """DescribeUDPListeners返回参数结构体

    """

    def __init__(self):
        r"""
        :param TotalCount: 监听器个数
        :type TotalCount: int
        :param ListenerSet: UDP监听器列表
        :type ListenerSet: list of UDPListener
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TotalCount = None
        self.ListenerSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TotalCount = params.get("TotalCount")
        if params.get("ListenerSet") is not None:
            self.ListenerSet = []
            for item in params.get("ListenerSet"):
                obj = UDPListener()
                obj._deserialize(item)
                self.ListenerSet.append(obj)
        self.RequestId = params.get("RequestId")


class DestAddressInfo(AbstractModel):
    """网络加速的目标地址信息

    """

    def __init__(self):
        r"""
        :param DestIp: 加速的目标IP，可多ip一起加速
        :type DestIp: list of str
        """
        self.DestIp = None


    def _deserialize(self, params):
        self.DestIp = params.get("DestIp")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyProxiesRequest(AbstractModel):
    """DestroyProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param Force: 强制删除标识。
1，强制删除该通道列表，无论是否已经绑定了源站；
0，如果已绑定了源站，则无法删除。
删除多通道时，如果该标识为0，只有所有的通道都没有绑定源站，才允许删除。
        :type Force: int
        :param InstanceIds: （旧参数，请切换到ProxyIds）通道实例ID列表。
        :type InstanceIds: list of str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param ProxyIds: （新参数）通道实例ID列表。
        :type ProxyIds: list of str
        """
        self.Force = None
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.Force = params.get("Force")
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DestroyProxiesResponse(AbstractModel):
    """DestroyProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvalidStatusInstanceSet: 处于不可销毁状态下的通道实例ID列表。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 销毁操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class DeviceInfo(AbstractModel):
    """终端设备信息

    """

    def __init__(self):
        r"""
        :param Vendor: 设备数据卡所属的运营商
1：移动
2：电信
3：联通
4：广电
99：其他
        :type Vendor: int
        :param OS: 设备操作系统
1：Android
2： IOS
99：其他
        :type OS: int
        :param DeviceId: 设备唯一标识
IOS 填写 IDFV
Android 填写 IMEI
        :type DeviceId: str
        :param PhoneNum: 用户手机号码
        :type PhoneNum: str
        :param Wireless: 无线信息
1：4G
2：5G
3：WIFI
99：其他
        :type Wireless: int
        """
        self.Vendor = None
        self.OS = None
        self.DeviceId = None
        self.PhoneNum = None
        self.Wireless = None


    def _deserialize(self, params):
        self.Vendor = params.get("Vendor")
        self.OS = params.get("OS")
        self.DeviceId = params.get("DeviceId")
        self.PhoneNum = params.get("PhoneNum")
        self.Wireless = params.get("Wireless")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainAccessRegionDict(AbstractModel):
    """域名解析就近访问配置详情

    """

    def __init__(self):
        r"""
        :param NationCountryInnerList: 就近接入区域
        :type NationCountryInnerList: list of NationCountryInnerInfo
        :param ProxyList: 加速区域通道列表
        :type ProxyList: list of ProxyIdDict
        :param RegionId: 加速区域ID
        :type RegionId: str
        :param GeographicalZoneInnerCode: 加速区域内部编码
        :type GeographicalZoneInnerCode: str
        :param ContinentInnerCode: 加速区域所属大洲内部编码
        :type ContinentInnerCode: str
        :param RegionName: 加速区域别名
        :type RegionName: str
        """
        self.NationCountryInnerList = None
        self.ProxyList = None
        self.RegionId = None
        self.GeographicalZoneInnerCode = None
        self.ContinentInnerCode = None
        self.RegionName = None


    def _deserialize(self, params):
        if params.get("NationCountryInnerList") is not None:
            self.NationCountryInnerList = []
            for item in params.get("NationCountryInnerList"):
                obj = NationCountryInnerInfo()
                obj._deserialize(item)
                self.NationCountryInnerList.append(obj)
        if params.get("ProxyList") is not None:
            self.ProxyList = []
            for item in params.get("ProxyList"):
                obj = ProxyIdDict()
                obj._deserialize(item)
                self.ProxyList.append(obj)
        self.RegionId = params.get("RegionId")
        self.GeographicalZoneInnerCode = params.get("GeographicalZoneInnerCode")
        self.ContinentInnerCode = params.get("ContinentInnerCode")
        self.RegionName = params.get("RegionName")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainErrorPageInfo(AbstractModel):
    """域名的定制错误响应配置

    """

    def __init__(self):
        r"""
        :param ErrorPageId: 错误定制响应的配置ID
        :type ErrorPageId: str
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param Domain: 域名
        :type Domain: str
        :param ErrorNos: 原始错误码
        :type ErrorNos: list of int
        :param NewErrorNo: 新的错误码
注意：此字段可能返回 null，表示取不到有效值。
        :type NewErrorNo: int
        :param ClearHeaders: 需要清理的响应头
注意：此字段可能返回 null，表示取不到有效值。
        :type ClearHeaders: list of str
        :param SetHeaders: 需要设置的响应头
注意：此字段可能返回 null，表示取不到有效值。
        :type SetHeaders: list of HttpHeaderParam
        :param Body: 设置的响应体(不包括 HTTP头)
注意：此字段可能返回 null，表示取不到有效值。
        :type Body: str
        :param Status: 规则状态,0为成功
注意：此字段可能返回 null，表示取不到有效值。
        :type Status: int
        """
        self.ErrorPageId = None
        self.ListenerId = None
        self.Domain = None
        self.ErrorNos = None
        self.NewErrorNo = None
        self.ClearHeaders = None
        self.SetHeaders = None
        self.Body = None
        self.Status = None


    def _deserialize(self, params):
        self.ErrorPageId = params.get("ErrorPageId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.ErrorNos = params.get("ErrorNos")
        self.NewErrorNo = params.get("NewErrorNo")
        self.ClearHeaders = params.get("ClearHeaders")
        if params.get("SetHeaders") is not None:
            self.SetHeaders = []
            for item in params.get("SetHeaders"):
                obj = HttpHeaderParam()
                obj._deserialize(item)
                self.SetHeaders.append(obj)
        self.Body = params.get("Body")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DomainRuleSet(AbstractModel):
    """按照域名分类的7层监听器转发规则信息

    """

    def __init__(self):
        r"""
        :param Domain: 转发规则域名。
        :type Domain: str
        :param RuleSet: 该域名对应的转发规则列表。
        :type RuleSet: list of RuleInfo
        :param CertificateId: 该域名对应的服务器证书ID，值为default时，表示使用默认证书（监听器配置的证书）。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateId: str
        :param CertificateAlias: 该域名对应服务器证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param ClientCertificateId: 该域名对应的客户端证书ID，值为default时，表示使用默认证书（监听器配置的证书）。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertificateId: str
        :param ClientCertificateAlias: 该域名对应客户端证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertificateAlias: str
        :param BasicAuthConfId: 该域名对应基础认证配置ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicAuthConfId: str
        :param BasicAuth: 基础认证开关，其中：
0，表示未开启；
1，表示已开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicAuth: int
        :param BasicAuthConfAlias: 该域名对应基础认证配置名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type BasicAuthConfAlias: str
        :param RealServerCertificateId: 该域名对应源站认证证书ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerCertificateId: str
        :param RealServerAuth: 源站认证开关，其中：
0，表示未开启；
1，表示已开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerAuth: int
        :param RealServerCertificateAlias: 该域名对应源站认证证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerCertificateAlias: str
        :param GaapCertificateId: 该域名对应通道认证证书ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type GaapCertificateId: str
        :param GaapAuth: 通道认证开关，其中：
0，表示未开启；
1，表示已开启。
注意：此字段可能返回 null，表示取不到有效值。
        :type GaapAuth: int
        :param GaapCertificateAlias: 该域名对应通道认证证书名称。
注意：此字段可能返回 null，表示取不到有效值。
        :type GaapCertificateAlias: str
        :param RealServerCertificateDomain: 源站认证域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerCertificateDomain: str
        :param PolyClientCertificateAliasInfo: 多客户端证书时，返回多个证书的id和别名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        :param PolyRealServerCertificateAliasInfo: 多源站证书时，返回多个证书的id和别名
注意：此字段可能返回 null，表示取不到有效值。
        :type PolyRealServerCertificateAliasInfo: list of CertificateAliasInfo
        :param DomainStatus: 域名的状态。
0表示运行中，
1表示变更中，
2表示删除中。
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainStatus: int
        :param BanStatus: 封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type BanStatus: str
        :param Http3Supported: Http3特性标识，其中：
0表示关闭；
1表示启用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Http3Supported: int
        """
        self.Domain = None
        self.RuleSet = None
        self.CertificateId = None
        self.CertificateAlias = None
        self.ClientCertificateId = None
        self.ClientCertificateAlias = None
        self.BasicAuthConfId = None
        self.BasicAuth = None
        self.BasicAuthConfAlias = None
        self.RealServerCertificateId = None
        self.RealServerAuth = None
        self.RealServerCertificateAlias = None
        self.GaapCertificateId = None
        self.GaapAuth = None
        self.GaapCertificateAlias = None
        self.RealServerCertificateDomain = None
        self.PolyClientCertificateAliasInfo = None
        self.PolyRealServerCertificateAliasInfo = None
        self.DomainStatus = None
        self.BanStatus = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.Domain = params.get("Domain")
        if params.get("RuleSet") is not None:
            self.RuleSet = []
            for item in params.get("RuleSet"):
                obj = RuleInfo()
                obj._deserialize(item)
                self.RuleSet.append(obj)
        self.CertificateId = params.get("CertificateId")
        self.CertificateAlias = params.get("CertificateAlias")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.ClientCertificateAlias = params.get("ClientCertificateAlias")
        self.BasicAuthConfId = params.get("BasicAuthConfId")
        self.BasicAuth = params.get("BasicAuth")
        self.BasicAuthConfAlias = params.get("BasicAuthConfAlias")
        self.RealServerCertificateId = params.get("RealServerCertificateId")
        self.RealServerAuth = params.get("RealServerAuth")
        self.RealServerCertificateAlias = params.get("RealServerCertificateAlias")
        self.GaapCertificateId = params.get("GaapCertificateId")
        self.GaapAuth = params.get("GaapAuth")
        self.GaapCertificateAlias = params.get("GaapCertificateAlias")
        self.RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self.PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self.PolyClientCertificateAliasInfo.append(obj)
        if params.get("PolyRealServerCertificateAliasInfo") is not None:
            self.PolyRealServerCertificateAliasInfo = []
            for item in params.get("PolyRealServerCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self.PolyRealServerCertificateAliasInfo.append(obj)
        self.DomainStatus = params.get("DomainStatus")
        self.BanStatus = params.get("BanStatus")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """过滤条件

    """

    def __init__(self):
        r"""
        :param Name: 过滤条件
        :type Name: str
        :param Values: 过滤值
        :type Values: list of str
        """
        self.Name = None
        self.Values = None


    def _deserialize(self, params):
        self.Name = params.get("Name")
        self.Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class GroupStatisticsInfo(AbstractModel):
    """可以显示统计数据的通道组和对应通道信息

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID
        :type GroupId: str
        :param GroupName: 通道组名称
        :type GroupName: str
        :param ProxySet: 通道组下通道列表
        :type ProxySet: list of ProxySimpleInfo
        """
        self.GroupId = None
        self.GroupName = None
        self.ProxySet = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        if params.get("ProxySet") is not None:
            self.ProxySet = []
            for item in params.get("ProxySet"):
                obj = ProxySimpleInfo()
                obj._deserialize(item)
                self.ProxySet.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPListener(AbstractModel):
    """HTTP类型监听器信息

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器端口
        :type Port: int
        :param CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param Protocol: 监听器协议， HTTP表示HTTP，HTTPS表示HTTPS，此结构取值HTTP
        :type Protocol: str
        :param ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.CreateTime = None
        self.Protocol = None
        self.ListenerStatus = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.CreateTime = params.get("CreateTime")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HTTPSListener(AbstractModel):
    """HTTPS类型监听器信息

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器端口
        :type Port: int
        :param Protocol: 监听器协议， HTTP表示HTTP，HTTPS表示HTTPS，此结构取值HTTPS
        :type Protocol: str
        :param ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param CertificateId: 监听器服务器SSL证书ID
        :type CertificateId: str
        :param ForwardProtocol: 监听器后端转发源站协议
        :type ForwardProtocol: str
        :param CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param CertificateAlias: 服务器SSL证书的别名
注意：此字段可能返回 null，表示取不到有效值。
        :type CertificateAlias: str
        :param ClientCertificateId: 监听器客户端CA证书ID
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertificateId: str
        :param AuthType: 监听器认证方式。其中，
0表示单向认证；
1表示双向认证。
注意：此字段可能返回 null，表示取不到有效值。
        :type AuthType: int
        :param ClientCertificateAlias: 客户端CA证书别名
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientCertificateAlias: str
        :param PolyClientCertificateAliasInfo: 多客户端CA证书别名信息
注意：此字段可能返回 null，表示取不到有效值。
        :type PolyClientCertificateAliasInfo: list of CertificateAliasInfo
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Protocol = None
        self.ListenerStatus = None
        self.CertificateId = None
        self.ForwardProtocol = None
        self.CreateTime = None
        self.CertificateAlias = None
        self.ClientCertificateId = None
        self.AuthType = None
        self.ClientCertificateAlias = None
        self.PolyClientCertificateAliasInfo = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        self.CertificateId = params.get("CertificateId")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.CreateTime = params.get("CreateTime")
        self.CertificateAlias = params.get("CertificateAlias")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.AuthType = params.get("AuthType")
        self.ClientCertificateAlias = params.get("ClientCertificateAlias")
        if params.get("PolyClientCertificateAliasInfo") is not None:
            self.PolyClientCertificateAliasInfo = []
            for item in params.get("PolyClientCertificateAliasInfo"):
                obj = CertificateAliasInfo()
                obj._deserialize(item)
                self.PolyClientCertificateAliasInfo.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class HttpHeaderParam(AbstractModel):
    """描述HTTP的包头参数

    """

    def __init__(self):
        r"""
        :param HeaderName: HTTP头名
        :type HeaderName: str
        :param HeaderValue: HTTP头值
        :type HeaderValue: str
        """
        self.HeaderName = None
        self.HeaderValue = None


    def _deserialize(self, params):
        self.HeaderName = params.get("HeaderName")
        self.HeaderValue = params.get("HeaderValue")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class IPDetail(AbstractModel):
    """ip信息详情

    """

    def __init__(self):
        r"""
        :param IP: IP字符串
        :type IP: str
        :param Provider: 供应商，BGP表示默认，CMCC表示中国移动，CUCC表示中国联通，CTCC表示中国电信
        :type Provider: str
        :param Bandwidth: 带宽
        :type Bandwidth: int
        """
        self.IP = None
        self.Provider = None
        self.Bandwidth = None


    def _deserialize(self, params):
        self.IP = params.get("IP")
        self.Provider = params.get("Provider")
        self.Bandwidth = params.get("Bandwidth")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateProxyRequest(AbstractModel):
    """InquiryPriceCreateProxy请求参数结构体

    """

    def __init__(self):
        r"""
        :param AccessRegion: 加速区域名称。
        :type AccessRegion: str
        :param Bandwidth: 通道带宽上限，单位：Mbps。
        :type Bandwidth: int
        :param DestRegion: （旧参数，请切换到RealServerRegion）源站区域名称。
        :type DestRegion: str
        :param Concurrency: （旧参数，请切换到Concurrent）通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrency: int
        :param RealServerRegion: （新参数）源站区域名称。
        :type RealServerRegion: str
        :param Concurrent: （新参数）通道并发量上限，表示同时在线的连接数，单位：万。
        :type Concurrent: int
        :param BillingType: 计费方式，0表示按带宽计费，1表示按流量计费。默认按带宽计费
        :type BillingType: int
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
        :type IPAddressVersion: str
        :param NetworkType: 网络类型，可取值：normal、cn2，默认值normal
        :type NetworkType: str
        :param PackageType: 通道套餐类型，Thunder表示标准通道组，Accelerator表示游戏加速器通道，CrossBorder表示跨境通道。
        :type PackageType: str
        :param Http3Supported: 支持Http3的开关，其中：0，表示不需要支持Http3接入；1，表示需要支持Http3接入。注意：如果开启了Http3的功能，那么该通道就不再支持TCP/UDP接入的功能。该功能的启停无法在通道创建完毕后再修改。
        :type Http3Supported: int
        """
        self.AccessRegion = None
        self.Bandwidth = None
        self.DestRegion = None
        self.Concurrency = None
        self.RealServerRegion = None
        self.Concurrent = None
        self.BillingType = None
        self.IPAddressVersion = None
        self.NetworkType = None
        self.PackageType = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.AccessRegion = params.get("AccessRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.DestRegion = params.get("DestRegion")
        self.Concurrency = params.get("Concurrency")
        self.RealServerRegion = params.get("RealServerRegion")
        self.Concurrent = params.get("Concurrent")
        self.BillingType = params.get("BillingType")
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.NetworkType = params.get("NetworkType")
        self.PackageType = params.get("PackageType")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class InquiryPriceCreateProxyResponse(AbstractModel):
    """InquiryPriceCreateProxy返回参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyDailyPrice: 通道基础费用价格，单位：元/天。
        :type ProxyDailyPrice: float
        :param BandwidthUnitPrice: 通道带宽费用梯度价格。
注意：此字段可能返回 null，表示取不到有效值。
        :type BandwidthUnitPrice: list of BandwidthPriceGradient
        :param DiscountProxyDailyPrice: 通道基础费用折扣价格，单位：元/天。
        :type DiscountProxyDailyPrice: float
        :param Currency: 价格使用的货币，支持人民币，美元等。
        :type Currency: str
        :param FlowUnitPrice: 通道的流量费用价格，单位: 元/GB
注意：此字段可能返回 null，表示取不到有效值。
        :type FlowUnitPrice: float
        :param DiscountFlowUnitPrice: 通道的流量费用折扣价格，单位:元/GB
注意：此字段可能返回 null，表示取不到有效值。
        :type DiscountFlowUnitPrice: float
        :param Cn2BandwidthPrice: 精品BGP的带宽费用价格，单位: 元/Mbps/天
注意：此字段可能返回 null，表示取不到有效值。
        :type Cn2BandwidthPrice: float
        :param Cn2BandwidthPriceWithDiscount: 精品BGP的折后带宽费用价格，单位: 元/Mbps/天
注意：此字段可能返回 null，表示取不到有效值。
        :type Cn2BandwidthPriceWithDiscount: float
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.ProxyDailyPrice = None
        self.BandwidthUnitPrice = None
        self.DiscountProxyDailyPrice = None
        self.Currency = None
        self.FlowUnitPrice = None
        self.DiscountFlowUnitPrice = None
        self.Cn2BandwidthPrice = None
        self.Cn2BandwidthPriceWithDiscount = None
        self.RequestId = None


    def _deserialize(self, params):
        self.ProxyDailyPrice = params.get("ProxyDailyPrice")
        if params.get("BandwidthUnitPrice") is not None:
            self.BandwidthUnitPrice = []
            for item in params.get("BandwidthUnitPrice"):
                obj = BandwidthPriceGradient()
                obj._deserialize(item)
                self.BandwidthUnitPrice.append(obj)
        self.DiscountProxyDailyPrice = params.get("DiscountProxyDailyPrice")
        self.Currency = params.get("Currency")
        self.FlowUnitPrice = params.get("FlowUnitPrice")
        self.DiscountFlowUnitPrice = params.get("DiscountFlowUnitPrice")
        self.Cn2BandwidthPrice = params.get("Cn2BandwidthPrice")
        self.Cn2BandwidthPriceWithDiscount = params.get("Cn2BandwidthPriceWithDiscount")
        self.RequestId = params.get("RequestId")


class ListenerInfo(AbstractModel):
    """内部接口使用，返回可以查询统计数据的监听器信息

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器监听端口
        :type Port: int
        :param Protocol: 监听器协议类型
        :type Protocol: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.Protocol = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.Protocol = params.get("Protocol")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class MetricStatisticsInfo(AbstractModel):
    """单指标的统计数据

    """

    def __init__(self):
        r"""
        :param MetricName: 指标名称
        :type MetricName: str
        :param MetricData: 指标统计数据
        :type MetricData: list of StatisticsDataInfo
        """
        self.MetricName = None
        self.MetricData = None


    def _deserialize(self, params):
        self.MetricName = params.get("MetricName")
        if params.get("MetricData") is not None:
            self.MetricData = []
            for item in params.get("MetricData"):
                obj = StatisticsDataInfo()
                obj._deserialize(item)
                self.MetricData.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAttributesRequest(AbstractModel):
    """ModifyCertificateAttributes请求参数结构体

    """

    def __init__(self):
        r"""
        :param CertificateId: 证书ID。
        :type CertificateId: str
        :param CertificateAlias: 证书名字。长度不超过50个字符。
        :type CertificateAlias: str
        """
        self.CertificateId = None
        self.CertificateAlias = None


    def _deserialize(self, params):
        self.CertificateId = params.get("CertificateId")
        self.CertificateAlias = params.get("CertificateAlias")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateAttributesResponse(AbstractModel):
    """ModifyCertificateAttributes返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyCertificateRequest(AbstractModel):
    """ModifyCertificate请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器实例ID
        :type ListenerId: str
        :param Domain: 需要修改证书的域名
        :type Domain: str
        :param CertificateId: 新的服务器证书ID。其中：
当CertificateId=default时，表示使用监听器的证书。
        :type CertificateId: str
        :param ClientCertificateId: 新的客户端证书ID。其中：
当ClientCertificateId=default时，表示使用监听器的证书。
仅当采用双向认证方式时，需要设置该参数或者PolyClientCertificateIds。
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 新的多客户端证书ID列表。其中：
仅当采用双向认证方式时，需要设置该参数或ClientCertificateId参数。
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.Domain = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyCertificateResponse(AbstractModel):
    """ModifyCertificate返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyDomainRequest(AbstractModel):
    """ModifyDomain请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 7层监听器ID
        :type ListenerId: str
        :param OldDomain: 修改前的域名信息
        :type OldDomain: str
        :param NewDomain: 修改后的域名信息
        :type NewDomain: str
        :param CertificateId: 服务器SSL证书ID，仅适用于version3.0的通道。其中：
不带该字段时，表示使用原证书；
携带该字段时并且CertificateId=default，表示使用监听器证书；
其他情况，使用该CertificateId指定的证书。
        :type CertificateId: str
        :param ClientCertificateId: 客户端CA证书ID，仅适用于version3.0的通道。其中：
不带该字段和PolyClientCertificateIds时，表示使用原证书；
携带该字段时并且ClientCertificateId=default，表示使用监听器证书；
其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 客户端CA证书ID，仅适用于version3.0的通道。其中：
不带该字段和ClientCertificateId时，表示使用原证书；
携带该字段时并且ClientCertificateId=default，表示使用监听器证书；
其他情况，使用该ClientCertificateId或PolyClientCertificateIds指定的证书。
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.OldDomain = None
        self.NewDomain = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.OldDomain = params.get("OldDomain")
        self.NewDomain = params.get("NewDomain")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyDomainResponse(AbstractModel):
    """ModifyDomain返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyGroupDomainConfigRequest(AbstractModel):
    """ModifyGroupDomainConfig请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组ID。
        :type GroupId: str
        :param DefaultDnsIp: 域名解析默认访问IP或域名。
        :type DefaultDnsIp: str
        :param AccessRegionList: 就近接入区域配置。
        :type AccessRegionList: list of AccessRegionDomainConf
        """
        self.GroupId = None
        self.DefaultDnsIp = None
        self.AccessRegionList = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.DefaultDnsIp = params.get("DefaultDnsIp")
        if params.get("AccessRegionList") is not None:
            self.AccessRegionList = []
            for item in params.get("AccessRegionList"):
                obj = AccessRegionDomainConf()
                obj._deserialize(item)
                self.AccessRegionList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyGroupDomainConfigResponse(AbstractModel):
    """ModifyGroupDomainConfig返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHTTPListenerAttributeRequest(AbstractModel):
    """ModifyHTTPListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 需要修改的监听器ID
        :type ListenerId: str
        :param ListenerName: 新的监听器名称
        :type ListenerName: str
        :param ProxyId: 通道ID
        :type ProxyId: str
        """
        self.ListenerId = None
        self.ListenerName = None
        self.ProxyId = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHTTPListenerAttributeResponse(AbstractModel):
    """ModifyHTTPListenerAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyHTTPSListenerAttributeRequest(AbstractModel):
    """ModifyHTTPSListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ProxyId: 通道ID， 若为单通道监听器，此项必须填写
        :type ProxyId: str
        :param ListenerName: 修改后的监听器名称
        :type ListenerName: str
        :param ForwardProtocol: 监听器后端转发与源站之间的协议类型
        :type ForwardProtocol: str
        :param CertificateId: 修改后的监听器服务器证书ID
        :type CertificateId: str
        :param ClientCertificateId: 修改后的监听器客户端证书ID，不支持多客户端证书，多客户端证书新采用PolyClientCertificateIds字段
        :type ClientCertificateId: str
        :param PolyClientCertificateIds: 新字段,修改后的监听器客户端证书ID
        :type PolyClientCertificateIds: list of str
        """
        self.ListenerId = None
        self.ProxyId = None
        self.ListenerName = None
        self.ForwardProtocol = None
        self.CertificateId = None
        self.ClientCertificateId = None
        self.PolyClientCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ProxyId = params.get("ProxyId")
        self.ListenerName = params.get("ListenerName")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.CertificateId = params.get("CertificateId")
        self.ClientCertificateId = params.get("ClientCertificateId")
        self.PolyClientCertificateIds = params.get("PolyClientCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyHTTPSListenerAttributeResponse(AbstractModel):
    """ModifyHTTPSListenerAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxiesAttributeRequest(AbstractModel):
    """ModifyProxiesAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: （旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。
        :type InstanceIds: list of str
        :param ProxyName: 通道名称。可任意命名，但不得超过30个字符。
        :type ProxyName: str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param ProxyIds: （新参数）一个或多个待操作的通道ID。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ProxyName = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ProxyName = params.get("ProxyName")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxiesAttributeResponse(AbstractModel):
    """ModifyProxiesAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxiesProjectRequest(AbstractModel):
    """ModifyProxiesProject请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProjectId: 需要修改到的项目ID。
        :type ProjectId: int
        :param InstanceIds: （旧参数，请切换到ProxyIds）一个或多个待操作的通道ID。
        :type InstanceIds: list of str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param ProxyIds: （新参数）一个或多个待操作的通道ID。
        :type ProxyIds: list of str
        """
        self.ProjectId = None
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.ProjectId = params.get("ProjectId")
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxiesProjectResponse(AbstractModel):
    """ModifyProxiesProject返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxyConfigurationRequest(AbstractModel):
    """ModifyProxyConfiguration请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceId: （旧参数，请切换到ProxyId）通道的实例ID。
        :type InstanceId: str
        :param Bandwidth: 需要调整到的目标带宽，单位：Mbps。
Bandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到
        :type Bandwidth: int
        :param Concurrent: 需要调整到的目标并发值，单位：万。
Bandwidth与Concurrent必须至少设置一个。取值范围根据DescribeAccessRegionsByDestRegion接口获取得到
        :type Concurrent: int
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param ProxyId: （新参数）通道的实例ID。
        :type ProxyId: str
        :param BillingType: 计费方式 (0:按带宽计费，1:按流量计费 默认按带宽计费）
        :type BillingType: int
        """
        self.InstanceId = None
        self.Bandwidth = None
        self.Concurrent = None
        self.ClientToken = None
        self.ProxyId = None
        self.BillingType = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.ClientToken = params.get("ClientToken")
        self.ProxyId = params.get("ProxyId")
        self.BillingType = params.get("BillingType")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyConfigurationResponse(AbstractModel):
    """ModifyProxyConfiguration返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyProxyGroupAttributeRequest(AbstractModel):
    """ModifyProxyGroupAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 需要修改的通道组ID。
        :type GroupId: str
        :param GroupName: 修改后的通道组名称：不超过30个字符，超过部分会被截断。
        :type GroupName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        """
        self.GroupId = None
        self.GroupName = None
        self.ProjectId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyProxyGroupAttributeResponse(AbstractModel):
    """ModifyProxyGroupAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRealServerNameRequest(AbstractModel):
    """ModifyRealServerName请求参数结构体

    """

    def __init__(self):
        r"""
        :param RealServerName: 源站名称
        :type RealServerName: str
        :param RealServerId: 源站ID
        :type RealServerId: str
        """
        self.RealServerName = None
        self.RealServerId = None


    def _deserialize(self, params):
        self.RealServerName = params.get("RealServerName")
        self.RealServerId = params.get("RealServerId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRealServerNameResponse(AbstractModel):
    """ModifyRealServerName返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyRuleAttributeRequest(AbstractModel):
    """ModifyRuleAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param RuleId: 转发规则ID
        :type RuleId: str
        :param Scheduler: 调度策略，其中：
rr，轮询；
wrr，加权轮询；
lc，最小连接数。
        :type Scheduler: str
        :param HealthCheck: 源站健康检查开关，其中：
1，开启；
0，关闭。
        :type HealthCheck: int
        :param CheckParams: 健康检查配置参数
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param Path: 转发规则路径
        :type Path: str
        :param ForwardProtocol: 加速通道转发到源站的协议类型，支持：default, HTTP和HTTPS。
当ForwardProtocol=default时，表示使用对应监听器的ForwardProtocol。
        :type ForwardProtocol: str
        :param ForwardHost: 回源Host。加速通道转发到源站的请求中携带的host。
当ForwardHost=default时，使用规则的域名，其他情况为该字段所设置的值。
        :type ForwardHost: str
        :param ServerNameIndicationSwitch: 服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
        :type ServerNameIndicationSwitch: str
        :param ServerNameIndication: 服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
        :type ServerNameIndication: str
        :param ForcedRedirect: HTTP强制跳转HTTPS。输入当前规则对应的域名与地址。
        :type ForcedRedirect: str
        """
        self.ListenerId = None
        self.RuleId = None
        self.Scheduler = None
        self.HealthCheck = None
        self.CheckParams = None
        self.Path = None
        self.ForwardProtocol = None
        self.ForwardHost = None
        self.ServerNameIndicationSwitch = None
        self.ServerNameIndication = None
        self.ForcedRedirect = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.RuleId = params.get("RuleId")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        if params.get("CheckParams") is not None:
            self.CheckParams = RuleCheckParams()
            self.CheckParams._deserialize(params.get("CheckParams"))
        self.Path = params.get("Path")
        self.ForwardProtocol = params.get("ForwardProtocol")
        self.ForwardHost = params.get("ForwardHost")
        self.ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self.ServerNameIndication = params.get("ServerNameIndication")
        self.ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyRuleAttributeResponse(AbstractModel):
    """ModifyRuleAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifySecurityRuleRequest(AbstractModel):
    """ModifySecurityRule请求参数结构体

    """

    def __init__(self):
        r"""
        :param RuleId: 规则ID
        :type RuleId: str
        :param AliasName: 规则名：不得超过30个字符，超过部分会被截断。
        :type AliasName: str
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        :param RuleAction: 安全规则动作
        :type RuleAction: str
        :param SourceCidr: 规则关联地址，格式需要满足CIDR网络地址规范
        :type SourceCidr: str
        :param Protocol: 协议类型
        :type Protocol: str
        :param DestPortRange: 端口范围，支持以下格式
单个端口: 80
多个端口: 80,443
连续端口: 3306-20000
所有端口: ALL
        :type DestPortRange: str
        """
        self.RuleId = None
        self.AliasName = None
        self.PolicyId = None
        self.RuleAction = None
        self.SourceCidr = None
        self.Protocol = None
        self.DestPortRange = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.AliasName = params.get("AliasName")
        self.PolicyId = params.get("PolicyId")
        self.RuleAction = params.get("RuleAction")
        self.SourceCidr = params.get("SourceCidr")
        self.Protocol = params.get("Protocol")
        self.DestPortRange = params.get("DestPortRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifySecurityRuleResponse(AbstractModel):
    """ModifySecurityRule返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyTCPListenerAttributeRequest(AbstractModel):
    """ModifyTCPListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Scheduler: 监听器源站调度策略，支持轮询（rr），加权轮询（wrr），最小连接数（lc）。
        :type Scheduler: str
        :param DelayLoop: 源站健康检查时间间隔，单位：秒。时间间隔取值在[5，300]之间。
        :type DelayLoop: int
        :param ConnectTimeout: 源站健康检查响应超时时间，单位：秒。超时时间取值在[2，60]之间。超时时间应小于健康检查时间间隔DelayLoop。
        :type ConnectTimeout: int
        :param HealthCheck: 是否开启健康检查，1开启，0关闭。
        :type HealthCheck: int
        :param FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
        :type FailoverSwitch: int
        :param HealthyThreshold: 健康阈值，表示连续检查成功多少次数后认定源站健康。范围为1到10
        :type HealthyThreshold: int
        :param UnhealthyThreshold: 不健康阈值，表示连续检查失败次数后认定源站不健康。范围为1到10
        :type UnhealthyThreshold: int
        """
        self.ListenerId = None
        self.GroupId = None
        self.ProxyId = None
        self.ListenerName = None
        self.Scheduler = None
        self.DelayLoop = None
        self.ConnectTimeout = None
        self.HealthCheck = None
        self.FailoverSwitch = None
        self.HealthyThreshold = None
        self.UnhealthyThreshold = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.GroupId = params.get("GroupId")
        self.ProxyId = params.get("ProxyId")
        self.ListenerName = params.get("ListenerName")
        self.Scheduler = params.get("Scheduler")
        self.DelayLoop = params.get("DelayLoop")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.HealthCheck = params.get("HealthCheck")
        self.FailoverSwitch = params.get("FailoverSwitch")
        self.HealthyThreshold = params.get("HealthyThreshold")
        self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyTCPListenerAttributeResponse(AbstractModel):
    """ModifyTCPListenerAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class ModifyUDPListenerAttributeRequest(AbstractModel):
    """ModifyUDPListenerAttribute请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param GroupId: 通道组ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type GroupId: str
        :param ProxyId: 通道ID，ProxyId和GroupId必须设置一个，但不能同时设置。
        :type ProxyId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Scheduler: 监听器源站调度策略
        :type Scheduler: str
        """
        self.ListenerId = None
        self.GroupId = None
        self.ProxyId = None
        self.ListenerName = None
        self.Scheduler = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.GroupId = params.get("GroupId")
        self.ProxyId = params.get("ProxyId")
        self.ListenerName = params.get("ListenerName")
        self.Scheduler = params.get("Scheduler")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ModifyUDPListenerAttributeResponse(AbstractModel):
    """ModifyUDPListenerAttribute返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class NationCountryInnerInfo(AbstractModel):
    """就近接入的国家地区详情

    """

    def __init__(self):
        r"""
        :param NationCountryName: 国家名
        :type NationCountryName: str
        :param NationCountryInnerCode: 国家内部编码
        :type NationCountryInnerCode: str
        """
        self.NationCountryName = None
        self.NationCountryInnerCode = None


    def _deserialize(self, params):
        self.NationCountryName = params.get("NationCountryName")
        self.NationCountryInnerCode = params.get("NationCountryInnerCode")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class NewRealServer(AbstractModel):
    """新添加源站信息

    """

    def __init__(self):
        r"""
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerIP: 源站ip或域名
        :type RealServerIP: str
        """
        self.RealServerId = None
        self.RealServerIP = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.RealServerIP = params.get("RealServerIP")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxiesRequest(AbstractModel):
    """OpenProxies请求参数结构体

    """

    def __init__(self):
        r"""
        :param InstanceIds: （旧参数，请切换到ProxyIds）通道的实例ID列表。
        :type InstanceIds: list of str
        :param ClientToken: 用于保证请求幂等性的字符串。该字符串由客户生成，需保证不同请求之间唯一，最大值不超过64个ASCII字符。若不指定该参数，则无法保证请求的幂等性。
更多详细信息请参阅：如何保证幂等性。
        :type ClientToken: str
        :param ProxyIds: （新参数）通道的实例ID列表。
        :type ProxyIds: list of str
        """
        self.InstanceIds = None
        self.ClientToken = None
        self.ProxyIds = None


    def _deserialize(self, params):
        self.InstanceIds = params.get("InstanceIds")
        self.ClientToken = params.get("ClientToken")
        self.ProxyIds = params.get("ProxyIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxiesResponse(AbstractModel):
    """OpenProxies返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvalidStatusInstanceSet: 非关闭状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class OpenProxyGroupRequest(AbstractModel):
    """OpenProxyGroup请求参数结构体

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组实例 ID
        :type GroupId: str
        """
        self.GroupId = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenProxyGroupResponse(AbstractModel):
    """OpenProxyGroup返回参数结构体

    """

    def __init__(self):
        r"""
        :param InvalidStatusInstanceSet: 非关闭状态下的通道实例ID列表，不可开启。
        :type InvalidStatusInstanceSet: list of str
        :param OperationFailedInstanceSet: 开启操作失败的通道实例ID列表。
        :type OperationFailedInstanceSet: list of str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.InvalidStatusInstanceSet = None
        self.OperationFailedInstanceSet = None
        self.RequestId = None


    def _deserialize(self, params):
        self.InvalidStatusInstanceSet = params.get("InvalidStatusInstanceSet")
        self.OperationFailedInstanceSet = params.get("OperationFailedInstanceSet")
        self.RequestId = params.get("RequestId")


class OpenSecurityPolicyRequest(AbstractModel):
    """OpenSecurityPolicy请求参数结构体

    """

    def __init__(self):
        r"""
        :param ProxyId: 需开启安全策略的通道ID
        :type ProxyId: str
        :param PolicyId: 安全策略ID
        :type PolicyId: str
        """
        self.ProxyId = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class OpenSecurityPolicyResponse(AbstractModel):
    """OpenSecurityPolicy返回参数结构体

    """

    def __init__(self):
        r"""
        :param TaskId: 异步流程ID，可以通过DescribeAsyncTaskStatus接口查询流程运行状态
        :type TaskId: str
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.TaskId = None
        self.RequestId = None


    def _deserialize(self, params):
        self.TaskId = params.get("TaskId")
        self.RequestId = params.get("RequestId")


class ProxyGroupDetail(AbstractModel):
    """通道组详情信息

    """

    def __init__(self):
        r"""
        :param CreateTime: 创建时间
        :type CreateTime: int
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param ProxyNum: 通道组中通道数量
        :type ProxyNum: int
        :param Status: 通道组状态：
0表示正常运行；
1表示创建中；
4表示销毁中；
11表示迁移中；
12表示部分部署中。
        :type Status: int
        :param OwnerUin: 归属Uin
        :type OwnerUin: str
        :param CreateUin: 创建Uin
        :type CreateUin: str
        :param GroupName: 通道名称
        :type GroupName: str
        :param DnsDefaultIp: 通道组域名解析默认IP
        :type DnsDefaultIp: str
        :param Domain: 通道组域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param RealServerRegionInfo: 目标地域
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param IsOldGroup: 是否老通道组，2018-08-03之前创建的通道组为老通道组
        :type IsOldGroup: bool
        :param GroupId: 通道组ID
        :type GroupId: str
        :param TagSet: 标签列表
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of TagPair
        :param PolicyId: 安全策略ID，当设置了安全策略时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        :param Version: 通道组版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param ClientIPMethod: 通道获取客户端IP的方式，0表示TOA，1表示Proxy Protocol
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIPMethod: list of int
        :param IPAddressVersion: IP版本，可取值：IPv4、IPv6，默认值IPv4
注意：此字段可能返回 null，表示取不到有效值。
        :type IPAddressVersion: str
        :param PackageType: 通道组套餐类型：Thunder表示标准通道组，Accelerator表示银牌加速通道组，CrossBorder表示跨境通道组。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param Http3Supported: 支持Http3特性的标识，其中：
0表示关闭；
1表示启用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Http3Supported: int
        """
        self.CreateTime = None
        self.ProjectId = None
        self.ProxyNum = None
        self.Status = None
        self.OwnerUin = None
        self.CreateUin = None
        self.GroupName = None
        self.DnsDefaultIp = None
        self.Domain = None
        self.RealServerRegionInfo = None
        self.IsOldGroup = None
        self.GroupId = None
        self.TagSet = None
        self.PolicyId = None
        self.Version = None
        self.ClientIPMethod = None
        self.IPAddressVersion = None
        self.PackageType = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.ProxyNum = params.get("ProxyNum")
        self.Status = params.get("Status")
        self.OwnerUin = params.get("OwnerUin")
        self.CreateUin = params.get("CreateUin")
        self.GroupName = params.get("GroupName")
        self.DnsDefaultIp = params.get("DnsDefaultIp")
        self.Domain = params.get("Domain")
        if params.get("RealServerRegionInfo") is not None:
            self.RealServerRegionInfo = RegionDetail()
            self.RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self.IsOldGroup = params.get("IsOldGroup")
        self.GroupId = params.get("GroupId")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.PolicyId = params.get("PolicyId")
        self.Version = params.get("Version")
        self.ClientIPMethod = params.get("ClientIPMethod")
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.PackageType = params.get("PackageType")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyGroupInfo(AbstractModel):
    """通道组详情列表

    """

    def __init__(self):
        r"""
        :param GroupId: 通道组id
        :type GroupId: str
        :param Domain: 通道组域名
注意：此字段可能返回 null，表示取不到有效值。
        :type Domain: str
        :param GroupName: 通道组名称
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param RealServerRegionInfo: 目标地域
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param Status: 通道组状态。
其中，
RUNNING表示运行中；
CREATING表示创建中；
DESTROYING表示销毁中；
MOVING表示通道迁移中；
CHANGING表示部分部署中。
        :type Status: str
        :param TagSet: 标签列表。
        :type TagSet: list of TagPair
        :param Version: 通道组版本
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param CreateTime: 创建时间
注意：此字段可能返回 null，表示取不到有效值。
        :type CreateTime: int
        :param ProxyType: 通道组是否包含微软通道
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyType: int
        :param Http3Supported: 支持Http3特性的标识，其中：
0表示关闭；
1表示启用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Http3Supported: int
        """
        self.GroupId = None
        self.Domain = None
        self.GroupName = None
        self.ProjectId = None
        self.RealServerRegionInfo = None
        self.Status = None
        self.TagSet = None
        self.Version = None
        self.CreateTime = None
        self.ProxyType = None
        self.Http3Supported = None


    def _deserialize(self, params):
        self.GroupId = params.get("GroupId")
        self.Domain = params.get("Domain")
        self.GroupName = params.get("GroupName")
        self.ProjectId = params.get("ProjectId")
        if params.get("RealServerRegionInfo") is not None:
            self.RealServerRegionInfo = RegionDetail()
            self.RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self.Status = params.get("Status")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.Version = params.get("Version")
        self.CreateTime = params.get("CreateTime")
        self.ProxyType = params.get("ProxyType")
        self.Http3Supported = params.get("Http3Supported")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyIdDict(AbstractModel):
    """通道ID

    """

    def __init__(self):
        r"""
        :param ProxyId: 通道ID
        :type ProxyId: str
        """
        self.ProxyId = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyInfo(AbstractModel):
    """通道信息

    """

    def __init__(self):
        r"""
        :param InstanceId: （旧参数，请使用ProxyId）通道实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type InstanceId: str
        :param CreateTime: 创建时间，采用Unix时间戳的方式，表示从1970年1月1日（UTC/GMT的午夜）开始所经过的秒数。
        :type CreateTime: int
        :param ProjectId: 项目ID。
        :type ProjectId: int
        :param ProxyName: 通道名称。
        :type ProxyName: str
        :param AccessRegion: 接入地域。
        :type AccessRegion: str
        :param RealServerRegion: 源站地域。
        :type RealServerRegion: str
        :param Bandwidth: 带宽，单位：Mbps。
        :type Bandwidth: int
        :param Concurrent: 并发，单位：个/秒。
        :type Concurrent: int
        :param Status: 通道状态。其中：
RUNNING表示运行中；
CREATING表示创建中；
DESTROYING表示销毁中；
OPENING表示开启中；
CLOSING表示关闭中；
CLOSED表示已关闭；
ADJUSTING表示配置变更中；
ISOLATING表示隔离中；
ISOLATED表示已隔离；
CLONING表示复制中；
RECOVERING表示通道维护中；
MOVING表示迁移中。
        :type Status: str
        :param Domain: 接入域名。
        :type Domain: str
        :param IP: 接入IP。
        :type IP: str
        :param Version: 通道版本号：1.0，2.0，3.0。
        :type Version: str
        :param ProxyId: （新参数）通道实例ID。
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyId: str
        :param Scalarable: 1，该通道可缩扩容；0，该通道无法缩扩容。
        :type Scalarable: int
        :param SupportProtocols: 支持的协议类型。
        :type SupportProtocols: list of str
        :param GroupId: 通道组ID，当通道归属于某一通道组时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        :param PolicyId: 安全策略ID，当设置了安全策略时，存在该字段。
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        :param AccessRegionInfo: 接入地域详细信息，包括地域ID和地域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type AccessRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param RealServerRegionInfo: 源站地域详细信息，包括地域ID和地域名。
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerRegionInfo: :class:`tencentcloud.gaap.v20180529.models.RegionDetail`
        :param ForwardIP: 通道转发IP
        :type ForwardIP: str
        :param TagSet: 标签列表，不存在标签时，该字段为空列表。
注意：此字段可能返回 null，表示取不到有效值。
        :type TagSet: list of TagPair
        :param SupportSecurity: 是否支持安全组配置
注意：此字段可能返回 null，表示取不到有效值。
        :type SupportSecurity: int
        :param BillingType: 计费类型: 0表示按带宽计费  1表示按流量计费。
注意：此字段可能返回 null，表示取不到有效值。
        :type BillingType: int
        :param RelatedGlobalDomains: 关联了解析的域名列表
注意：此字段可能返回 null，表示取不到有效值。
        :type RelatedGlobalDomains: list of str
        :param ModifyConfigTime: 配置变更时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ModifyConfigTime: int
        :param ProxyType: 通道类型，100表示THUNDER通道，103表示微软合作通道
注意：此字段可能返回 null，表示取不到有效值。
        :type ProxyType: int
        :param ClientIPMethod: 通道获取客户端IP的方式，0表示TOA，1表示Proxy Protocol
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIPMethod: list of int
        :param IPAddressVersion: IP版本：IPv4、IPv6
注意：此字段可能返回 null，表示取不到有效值。
        :type IPAddressVersion: str
        :param NetworkType: 网络类型：normal表示常规BGP，cn2表示精品BGP，triple表示三网，secure_eip表示定制安全EIP
注意：此字段可能返回 null，表示取不到有效值。
        :type NetworkType: str
        :param PackageType: 通道套餐类型：Thunder表示标准通道，Accelerator表示银牌加速通道，
CrossBorder表示跨境通道。
注意：此字段可能返回 null，表示取不到有效值。
        :type PackageType: str
        :param BanStatus: 封禁解封状态：BANNED表示已封禁，RECOVER表示已解封或未封禁，BANNING表示封禁中，RECOVERING表示解封中，BAN_FAILED表示封禁失败，RECOVER_FAILED表示解封失败。
注意：此字段可能返回 null，表示取不到有效值。
        :type BanStatus: str
        :param IPList: IP列表
注意：此字段可能返回 null，表示取不到有效值。
        :type IPList: list of IPDetail
        :param Http3Supported: 支持Http3协议的标识，其中：
0表示关闭；
1表示启用。
注意：此字段可能返回 null，表示取不到有效值。
        :type Http3Supported: int
        :param InBanBlacklist: 是否在封禁黑名单中，其中：0表示不在黑名单中，1表示在黑名单中。
注意：此字段可能返回 null，表示取不到有效值。
        :type InBanBlacklist: int
        """
        self.InstanceId = None
        self.CreateTime = None
        self.ProjectId = None
        self.ProxyName = None
        self.AccessRegion = None
        self.RealServerRegion = None
        self.Bandwidth = None
        self.Concurrent = None
        self.Status = None
        self.Domain = None
        self.IP = None
        self.Version = None
        self.ProxyId = None
        self.Scalarable = None
        self.SupportProtocols = None
        self.GroupId = None
        self.PolicyId = None
        self.AccessRegionInfo = None
        self.RealServerRegionInfo = None
        self.ForwardIP = None
        self.TagSet = None
        self.SupportSecurity = None
        self.BillingType = None
        self.RelatedGlobalDomains = None
        self.ModifyConfigTime = None
        self.ProxyType = None
        self.ClientIPMethod = None
        self.IPAddressVersion = None
        self.NetworkType = None
        self.PackageType = None
        self.BanStatus = None
        self.IPList = None
        self.Http3Supported = None
        self.InBanBlacklist = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.CreateTime = params.get("CreateTime")
        self.ProjectId = params.get("ProjectId")
        self.ProxyName = params.get("ProxyName")
        self.AccessRegion = params.get("AccessRegion")
        self.RealServerRegion = params.get("RealServerRegion")
        self.Bandwidth = params.get("Bandwidth")
        self.Concurrent = params.get("Concurrent")
        self.Status = params.get("Status")
        self.Domain = params.get("Domain")
        self.IP = params.get("IP")
        self.Version = params.get("Version")
        self.ProxyId = params.get("ProxyId")
        self.Scalarable = params.get("Scalarable")
        self.SupportProtocols = params.get("SupportProtocols")
        self.GroupId = params.get("GroupId")
        self.PolicyId = params.get("PolicyId")
        if params.get("AccessRegionInfo") is not None:
            self.AccessRegionInfo = RegionDetail()
            self.AccessRegionInfo._deserialize(params.get("AccessRegionInfo"))
        if params.get("RealServerRegionInfo") is not None:
            self.RealServerRegionInfo = RegionDetail()
            self.RealServerRegionInfo._deserialize(params.get("RealServerRegionInfo"))
        self.ForwardIP = params.get("ForwardIP")
        if params.get("TagSet") is not None:
            self.TagSet = []
            for item in params.get("TagSet"):
                obj = TagPair()
                obj._deserialize(item)
                self.TagSet.append(obj)
        self.SupportSecurity = params.get("SupportSecurity")
        self.BillingType = params.get("BillingType")
        self.RelatedGlobalDomains = params.get("RelatedGlobalDomains")
        self.ModifyConfigTime = params.get("ModifyConfigTime")
        self.ProxyType = params.get("ProxyType")
        self.ClientIPMethod = params.get("ClientIPMethod")
        self.IPAddressVersion = params.get("IPAddressVersion")
        self.NetworkType = params.get("NetworkType")
        self.PackageType = params.get("PackageType")
        self.BanStatus = params.get("BanStatus")
        if params.get("IPList") is not None:
            self.IPList = []
            for item in params.get("IPList"):
                obj = IPDetail()
                obj._deserialize(item)
                self.IPList.append(obj)
        self.Http3Supported = params.get("Http3Supported")
        self.InBanBlacklist = params.get("InBanBlacklist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxySimpleInfo(AbstractModel):
    """内部接口使用，返回可以查询统计数据的通道和对应的监听器信息

    """

    def __init__(self):
        r"""
        :param ProxyId: 通道ID
        :type ProxyId: str
        :param ProxyName: 通道名称
        :type ProxyName: str
        :param ListenerList: 监听器列表
        :type ListenerList: list of ListenerInfo
        """
        self.ProxyId = None
        self.ProxyName = None
        self.ListenerList = None


    def _deserialize(self, params):
        self.ProxyId = params.get("ProxyId")
        self.ProxyName = params.get("ProxyName")
        if params.get("ListenerList") is not None:
            self.ListenerList = []
            for item in params.get("ListenerList"):
                obj = ListenerInfo()
                obj._deserialize(item)
                self.ListenerList.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class ProxyStatus(AbstractModel):
    """通道状态信息

    """

    def __init__(self):
        r"""
        :param InstanceId: 通道实例ID。
        :type InstanceId: str
        :param Status: 通道状态。
其中：
RUNNING表示运行中；
CREATING表示创建中；
DESTROYING表示销毁中；
OPENING表示开启中；
CLOSING表示关闭中；
CLOSED表示已关闭；
ADJUSTING表示配置变更中；
ISOLATING表示隔离中；
ISOLATED表示已隔离；
MOVING表示迁移中。
        :type Status: str
        """
        self.InstanceId = None
        self.Status = None


    def _deserialize(self, params):
        self.InstanceId = params.get("InstanceId")
        self.Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServer(AbstractModel):
    """查询监听器或者规则相关的源站信息，不包括tag信息

    """

    def __init__(self):
        r"""
        :param RealServerIP: 源站的IP或域名
        :type RealServerIP: str
        :param RealServerId: 源站ID
        :type RealServerId: str
        :param RealServerName: 源站名称
        :type RealServerName: str
        :param ProjectId: 项目ID
        :type ProjectId: int
        :param InBanBlacklist: 是否在封禁黑名单中，其中：0表示不在黑名单中，1表示在黑名单中。
        :type InBanBlacklist: int
        """
        self.RealServerIP = None
        self.RealServerId = None
        self.RealServerName = None
        self.ProjectId = None
        self.InBanBlacklist = None


    def _deserialize(self, params):
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerId = params.get("RealServerId")
        self.RealServerName = params.get("RealServerName")
        self.ProjectId = params.get("ProjectId")
        self.InBanBlacklist = params.get("InBanBlacklist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServerBindSetReq(AbstractModel):
    """绑定的源站信息

    """

    def __init__(self):
        r"""
        :param RealServerId: 源站id
        :type RealServerId: str
        :param RealServerPort: 源站端口
        :type RealServerPort: int
        :param RealServerIP: 源站IP
        :type RealServerIP: str
        :param RealServerWeight: 源站权重
        :type RealServerWeight: int
        :param RealServerFailoverRole: 源站主备角色：master主，slave备，该参数必须在监听器打开了源站主备模式，且监听器类型为TCP监听器
        :type RealServerFailoverRole: str
        """
        self.RealServerId = None
        self.RealServerPort = None
        self.RealServerIP = None
        self.RealServerWeight = None
        self.RealServerFailoverRole = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.RealServerPort = params.get("RealServerPort")
        self.RealServerIP = params.get("RealServerIP")
        self.RealServerWeight = params.get("RealServerWeight")
        self.RealServerFailoverRole = params.get("RealServerFailoverRole")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RealServerStatus(AbstractModel):
    """源站绑定信息查询，BindStatus， 0: 未被绑定 1：被规则或者监听器绑定

    """

    def __init__(self):
        r"""
        :param RealServerId: 源站ID。
        :type RealServerId: str
        :param BindStatus: 0表示未被绑定 1表示被规则或者监听器绑定。
        :type BindStatus: int
        :param ProxyId: 绑定此源站的通道ID，没有绑定时为空字符串。
        :type ProxyId: str
        :param GroupId: 绑定此源站的通道组ID，没有绑定时为空字符串。
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: str
        """
        self.RealServerId = None
        self.BindStatus = None
        self.ProxyId = None
        self.GroupId = None


    def _deserialize(self, params):
        self.RealServerId = params.get("RealServerId")
        self.BindStatus = params.get("BindStatus")
        self.ProxyId = params.get("ProxyId")
        self.GroupId = params.get("GroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RegionDetail(AbstractModel):
    """区域信息详情

    """

    def __init__(self):
        r"""
        :param RegionId: 区域ID
        :type RegionId: str
        :param RegionName: 区域英文名或中文名
        :type RegionName: str
        :param RegionArea: 机房所属大区
        :type RegionArea: str
        :param RegionAreaName: 机房所属大区名
        :type RegionAreaName: str
        :param IDCType: 机房类型, dc表示DataCenter数据中心, ec表示EdgeComputing边缘节点
        :type IDCType: str
        :param FeatureBitmap: 特性位图，每个bit位代表一种特性，其中：
0，表示不支持该特性；
1，表示支持该特性。
特性位图含义如下（从右往左）：
第1个bit，支持4层加速；
第2个bit，支持7层加速；
第3个bit，支持Http3接入；
第4个bit，支持IPv6；
第5个bit，支持精品BGP接入；
第6个bit，支持三网接入；
第7个bit，支持接入段Qos加速。
注意：此字段可能返回 null，表示取不到有效值。
        :type FeatureBitmap: int
        """
        self.RegionId = None
        self.RegionName = None
        self.RegionArea = None
        self.RegionAreaName = None
        self.IDCType = None
        self.FeatureBitmap = None


    def _deserialize(self, params):
        self.RegionId = params.get("RegionId")
        self.RegionName = params.get("RegionName")
        self.RegionArea = params.get("RegionArea")
        self.RegionAreaName = params.get("RegionAreaName")
        self.IDCType = params.get("IDCType")
        self.FeatureBitmap = params.get("FeatureBitmap")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRealServersRequest(AbstractModel):
    """RemoveRealServers请求参数结构体

    """

    def __init__(self):
        r"""
        :param RealServerIds: 源站Id列表
        :type RealServerIds: list of str
        """
        self.RealServerIds = None


    def _deserialize(self, params):
        self.RealServerIds = params.get("RealServerIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RemoveRealServersResponse(AbstractModel):
    """RemoveRealServers返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class RuleCheckParams(AbstractModel):
    """7层监听器转发规则健康检查相关参数

    """

    def __init__(self):
        r"""
        :param DelayLoop: 健康检查的时间间隔
        :type DelayLoop: int
        :param ConnectTimeout: 健康检查的响应超时时间
        :type ConnectTimeout: int
        :param Path: 健康检查的检查路径
        :type Path: str
        :param Method: 健康检查的方法，GET/HEAD
        :type Method: str
        :param StatusCode: 确认源站正常的返回码，可选范围[100, 200, 300, 400, 500]
        :type StatusCode: list of int non-negative
        :param Domain: 健康检查的检查域名。
当调用ModifyRuleAttribute时，不支持修改该参数。
        :type Domain: str
        :param FailedCountInter: 源站服务失败统计频率
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedCountInter: int
        :param FailedThreshold: 源站健康性检查阀值，超过该阀值会屏蔽服务
注意：此字段可能返回 null，表示取不到有效值。
        :type FailedThreshold: int
        :param BlockInter: 源站健康性检测超出阀值后，屏蔽的时间
注意：此字段可能返回 null，表示取不到有效值。
        :type BlockInter: int
        """
        self.DelayLoop = None
        self.ConnectTimeout = None
        self.Path = None
        self.Method = None
        self.StatusCode = None
        self.Domain = None
        self.FailedCountInter = None
        self.FailedThreshold = None
        self.BlockInter = None


    def _deserialize(self, params):
        self.DelayLoop = params.get("DelayLoop")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.Path = params.get("Path")
        self.Method = params.get("Method")
        self.StatusCode = params.get("StatusCode")
        self.Domain = params.get("Domain")
        self.FailedCountInter = params.get("FailedCountInter")
        self.FailedThreshold = params.get("FailedThreshold")
        self.BlockInter = params.get("BlockInter")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class RuleInfo(AbstractModel):
    """7层监听器转发规则信息

    """

    def __init__(self):
        r"""
        :param RuleId: 规则信息
        :type RuleId: str
        :param ListenerId: 监听器信息
        :type ListenerId: str
        :param Domain: 规则域名
        :type Domain: str
        :param Path: 规则路径
        :type Path: str
        :param RealServerType: 源站类型
        :type RealServerType: str
        :param Scheduler: 转发源站策略
        :type Scheduler: str
        :param HealthCheck: 是否开启健康检查标志，1表示开启，0表示关闭
        :type HealthCheck: int
        :param RuleStatus: 规则状态，0表示运行中，1表示创建中，2表示销毁中，3表示绑定解绑源站中，4表示配置更新中
        :type RuleStatus: int
        :param CheckParams: 健康检查相关参数
        :type CheckParams: :class:`tencentcloud.gaap.v20180529.models.RuleCheckParams`
        :param RealServerSet: 已绑定的源站相关信息
        :type RealServerSet: list of BindRealServer
        :param BindStatus: 源站的服务状态，0表示异常，1表示正常。
未开启健康检查时，该状态始终未正常。
只要有一个源站健康状态为异常时，该状态为异常，具体源站的状态请查看RealServerSet。
        :type BindStatus: int
        :param ForwardHost: 通道转发到源站的请求所携带的host，其中default表示直接转发接收到的host。
注意：此字段可能返回 null，表示取不到有效值。
        :type ForwardHost: str
        :param ServerNameIndicationSwitch: 服务器名称指示（ServerNameIndication，简称SNI）开关。ON表示开启，OFF表示关闭。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerNameIndicationSwitch: str
        :param ServerNameIndication: 服务器名称指示（ServerNameIndication，简称SNI），当SNI开关打开时，该字段必填。
注意：此字段可能返回 null，表示取不到有效值。
注意：此字段可能返回 null，表示取不到有效值。
        :type ServerNameIndication: str
        :param ForcedRedirect: 强转HTTPS指示，当传递值为https:时表示强转为https
注意：此字段可能返回 null，表示取不到有效值。
        :type ForcedRedirect: str
        """
        self.RuleId = None
        self.ListenerId = None
        self.Domain = None
        self.Path = None
        self.RealServerType = None
        self.Scheduler = None
        self.HealthCheck = None
        self.RuleStatus = None
        self.CheckParams = None
        self.RealServerSet = None
        self.BindStatus = None
        self.ForwardHost = None
        self.ServerNameIndicationSwitch = None
        self.ServerNameIndication = None
        self.ForcedRedirect = None


    def _deserialize(self, params):
        self.RuleId = params.get("RuleId")
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.Path = params.get("Path")
        self.RealServerType = params.get("RealServerType")
        self.Scheduler = params.get("Scheduler")
        self.HealthCheck = params.get("HealthCheck")
        self.RuleStatus = params.get("RuleStatus")
        if params.get("CheckParams") is not None:
            self.CheckParams = RuleCheckParams()
            self.CheckParams._deserialize(params.get("CheckParams"))
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.BindStatus = params.get("BindStatus")
        self.ForwardHost = params.get("ForwardHost")
        self.ServerNameIndicationSwitch = params.get("ServerNameIndicationSwitch")
        self.ServerNameIndication = params.get("ServerNameIndication")
        self.ForcedRedirect = params.get("ForcedRedirect")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRuleIn(AbstractModel):
    """安全策略规则（入参）

    """

    def __init__(self):
        r"""
        :param SourceCidr: 请求来源IP或IP段。
        :type SourceCidr: str
        :param Action: 策略：允许（ACCEPT）或拒绝（DROP）
        :type Action: str
        :param AliasName: 规则别名
        :type AliasName: str
        :param Protocol: 协议：TCP或UDP，ALL表示所有协议
        :type Protocol: str
        :param DestPortRange: 目标端口，填写格式举例：
单个端口: 80
多个端口: 80,443
连续端口: 3306-20000
所有端口: ALL
        :type DestPortRange: str
        """
        self.SourceCidr = None
        self.Action = None
        self.AliasName = None
        self.Protocol = None
        self.DestPortRange = None


    def _deserialize(self, params):
        self.SourceCidr = params.get("SourceCidr")
        self.Action = params.get("Action")
        self.AliasName = params.get("AliasName")
        self.Protocol = params.get("Protocol")
        self.DestPortRange = params.get("DestPortRange")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SecurityPolicyRuleOut(AbstractModel):
    """安全策略规则（出参）

    """

    def __init__(self):
        r"""
        :param Action: 策略：允许（ACCEPT）或拒绝（DROP）
        :type Action: str
        :param SourceCidr: 请求来源Ip或Ip段
        :type SourceCidr: str
        :param AliasName: 规则别名
        :type AliasName: str
        :param DestPortRange: 目标端口范围
注意：此字段可能返回 null，表示取不到有效值。
        :type DestPortRange: str
        :param RuleId: 规则ID
        :type RuleId: str
        :param Protocol: 要匹配的协议类型（TCP/UDP）
注意：此字段可能返回 null，表示取不到有效值。
        :type Protocol: str
        :param PolicyId: 安全策略ID
注意：此字段可能返回 null，表示取不到有效值。
        :type PolicyId: str
        """
        self.Action = None
        self.SourceCidr = None
        self.AliasName = None
        self.DestPortRange = None
        self.RuleId = None
        self.Protocol = None
        self.PolicyId = None


    def _deserialize(self, params):
        self.Action = params.get("Action")
        self.SourceCidr = params.get("SourceCidr")
        self.AliasName = params.get("AliasName")
        self.DestPortRange = params.get("DestPortRange")
        self.RuleId = params.get("RuleId")
        self.Protocol = params.get("Protocol")
        self.PolicyId = params.get("PolicyId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAuthenticationRequest(AbstractModel):
    """SetAuthentication请求参数结构体

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID。
        :type ListenerId: str
        :param Domain: 需要进行高级配置的域名，该域名为监听器下的转发规则的域名。
        :type Domain: str
        :param BasicAuth: 基础认证开关，其中：
0，关闭基础认证；
1，开启基础认证。
默认为0。
        :type BasicAuth: int
        :param GaapAuth: 通道认证开关，用于源站对Gaap的认证，其中：
0，关闭通道认证；
1，开启通道认证。
默认为0。
        :type GaapAuth: int
        :param RealServerAuth: 源站认证开关，用于Gaap对服务器的认证，其中：
0，关闭源站认证；
1，开启源站认证。
默认为0。
        :type RealServerAuth: int
        :param BasicAuthConfId: 基础认证配置ID，从证书管理页获取。
        :type BasicAuthConfId: str
        :param GaapCertificateId: 通道SSL证书ID，从证书管理页获取。
        :type GaapCertificateId: str
        :param RealServerCertificateId: 源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数
        :type RealServerCertificateId: str
        :param RealServerCertificateDomain: 该字段已废弃，请使用创建规则和修改规则中的SNI功能。
        :type RealServerCertificateDomain: str
        :param PolyRealServerCertificateIds: 多源站CA证书ID，从证书管理页获取。源站认证时，填写该参数或RealServerCertificateId参数
        :type PolyRealServerCertificateIds: list of str
        """
        self.ListenerId = None
        self.Domain = None
        self.BasicAuth = None
        self.GaapAuth = None
        self.RealServerAuth = None
        self.BasicAuthConfId = None
        self.GaapCertificateId = None
        self.RealServerCertificateId = None
        self.RealServerCertificateDomain = None
        self.PolyRealServerCertificateIds = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.Domain = params.get("Domain")
        self.BasicAuth = params.get("BasicAuth")
        self.GaapAuth = params.get("GaapAuth")
        self.RealServerAuth = params.get("RealServerAuth")
        self.BasicAuthConfId = params.get("BasicAuthConfId")
        self.GaapCertificateId = params.get("GaapCertificateId")
        self.RealServerCertificateId = params.get("RealServerCertificateId")
        self.RealServerCertificateDomain = params.get("RealServerCertificateDomain")
        self.PolyRealServerCertificateIds = params.get("PolyRealServerCertificateIds")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class SetAuthenticationResponse(AbstractModel):
    """SetAuthentication返回参数结构体

    """

    def __init__(self):
        r"""
        :param RequestId: 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self.RequestId = None


    def _deserialize(self, params):
        self.RequestId = params.get("RequestId")


class SrcAddressInfo(AbstractModel):
    """网络加速的原地址信息

    """

    def __init__(self):
        r"""
        :param SrcIpv4: 内网Ip4地址
        :type SrcIpv4: str
        :param SrcPublicIpv4: 公网Ip4地址
        :type SrcPublicIpv4: str
        """
        self.SrcIpv4 = None
        self.SrcPublicIpv4 = None


    def _deserialize(self, params):
        self.SrcIpv4 = params.get("SrcIpv4")
        self.SrcPublicIpv4 = params.get("SrcPublicIpv4")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class StatisticsDataInfo(AbstractModel):
    """统计数据信息

    """

    def __init__(self):
        r"""
        :param Time: 对应的时间点
        :type Time: int
        :param Data: 统计数据值
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: float
        """
        self.Time = None
        self.Data = None


    def _deserialize(self, params):
        self.Time = params.get("Time")
        self.Data = params.get("Data")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TCPListener(AbstractModel):
    """TCP类型监听器信息

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器端口
        :type Port: int
        :param RealServerPort: 监听器转发源站端口，仅对版本为1.0的通道有效
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param RealServerType: 监听器绑定源站类型
        :type RealServerType: str
        :param Protocol: 监听器协议， TCP
        :type Protocol: str
        :param ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param Scheduler: 监听器源站访问策略，其中：
rr表示轮询；
wrr表示加权轮询；
lc表示最小连接数。
        :type Scheduler: str
        :param ConnectTimeout: 源站健康检查响应超时时间，单位：秒
        :type ConnectTimeout: int
        :param DelayLoop: 源站健康检查时间间隔，单位：秒
        :type DelayLoop: int
        :param HealthCheck: 监听器是否开启健康检查，其中：
0表示关闭；
1表示开启
        :type HealthCheck: int
        :param BindStatus: 监听器绑定的源站状态， 其中：
0表示异常；
1表示正常。
        :type BindStatus: int
        :param RealServerSet: 监听器绑定的源站信息
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerSet: list of BindRealServer
        :param CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param ClientIPMethod: 监听器获取客户端 IP 的方式，0表示TOA, 1表示Proxy Protocol
注意：此字段可能返回 null，表示取不到有效值。
        :type ClientIPMethod: int
        :param HealthyThreshold: 健康阈值，表示连续检查成功多少次后认定源站健康。范围为1到10
注意：此字段可能返回 null，表示取不到有效值。
        :type HealthyThreshold: int
        :param UnhealthyThreshold: 不健康阈值，表示连续检查失败多少次数后认为源站不健康。范围为1到10
注意：此字段可能返回 null，表示取不到有效值。
        :type UnhealthyThreshold: int
        :param FailoverSwitch: 源站是否开启主备模式：1开启，0关闭，DOMAIN类型源站不支持开启
注意：此字段可能返回 null，表示取不到有效值。
        :type FailoverSwitch: int
        :param SessionPersist: 是否开启会话保持选项：0关闭， 非0开启，非0值为会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionPersist: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.RealServerPort = None
        self.RealServerType = None
        self.Protocol = None
        self.ListenerStatus = None
        self.Scheduler = None
        self.ConnectTimeout = None
        self.DelayLoop = None
        self.HealthCheck = None
        self.BindStatus = None
        self.RealServerSet = None
        self.CreateTime = None
        self.ClientIPMethod = None
        self.HealthyThreshold = None
        self.UnhealthyThreshold = None
        self.FailoverSwitch = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.RealServerPort = params.get("RealServerPort")
        self.RealServerType = params.get("RealServerType")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        self.Scheduler = params.get("Scheduler")
        self.ConnectTimeout = params.get("ConnectTimeout")
        self.DelayLoop = params.get("DelayLoop")
        self.HealthCheck = params.get("HealthCheck")
        self.BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.ClientIPMethod = params.get("ClientIPMethod")
        self.HealthyThreshold = params.get("HealthyThreshold")
        self.UnhealthyThreshold = params.get("UnhealthyThreshold")
        self.FailoverSwitch = params.get("FailoverSwitch")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagPair(AbstractModel):
    """标签键值对

    """

    def __init__(self):
        r"""
        :param TagKey: 标签键
        :type TagKey: str
        :param TagValue: 标签值
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
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class TagResourceInfo(AbstractModel):
    """标签对应资源信息

    """

    def __init__(self):
        r"""
        :param ResourceType: 资源类型，其中：
Proxy表示通道，
ProxyGroup表示通道组，
RealServer表示源站
        :type ResourceType: str
        :param ResourceId: 资源ID
        :type ResourceId: str
        """
        self.ResourceType = None
        self.ResourceId = None


    def _deserialize(self, params):
        self.ResourceType = params.get("ResourceType")
        self.ResourceId = params.get("ResourceId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class UDPListener(AbstractModel):
    """UDP类型监听器信息

    """

    def __init__(self):
        r"""
        :param ListenerId: 监听器ID
        :type ListenerId: str
        :param ListenerName: 监听器名称
        :type ListenerName: str
        :param Port: 监听器端口
        :type Port: int
        :param RealServerPort: 监听器转发源站端口，仅V1版本通道或通道组监听器有效
注意：此字段可能返回 null，表示取不到有效值。
        :type RealServerPort: int
        :param RealServerType: 监听器绑定源站类型
        :type RealServerType: str
        :param Protocol: 监听器协议， UDP
        :type Protocol: str
        :param ListenerStatus: 监听器状态，其中：
0表示运行中；
1表示创建中；
2表示销毁中；
3表示源站调整中；
4表示配置变更中。
        :type ListenerStatus: int
        :param Scheduler: 监听器源站访问策略
        :type Scheduler: str
        :param BindStatus: 监听器绑定源站状态， 0表示正常，1表示IP异常，2表示域名解析异常
        :type BindStatus: int
        :param RealServerSet: 监听器绑定的源站信息
        :type RealServerSet: list of BindRealServer
        :param CreateTime: 监听器创建时间，Unix时间戳
        :type CreateTime: int
        :param SessionPersist: 是否开启会话保持选项：0关闭， 非0开启，非0值为会话保持时间
注意：此字段可能返回 null，表示取不到有效值。
        :type SessionPersist: int
        """
        self.ListenerId = None
        self.ListenerName = None
        self.Port = None
        self.RealServerPort = None
        self.RealServerType = None
        self.Protocol = None
        self.ListenerStatus = None
        self.Scheduler = None
        self.BindStatus = None
        self.RealServerSet = None
        self.CreateTime = None
        self.SessionPersist = None


    def _deserialize(self, params):
        self.ListenerId = params.get("ListenerId")
        self.ListenerName = params.get("ListenerName")
        self.Port = params.get("Port")
        self.RealServerPort = params.get("RealServerPort")
        self.RealServerType = params.get("RealServerType")
        self.Protocol = params.get("Protocol")
        self.ListenerStatus = params.get("ListenerStatus")
        self.Scheduler = params.get("Scheduler")
        self.BindStatus = params.get("BindStatus")
        if params.get("RealServerSet") is not None:
            self.RealServerSet = []
            for item in params.get("RealServerSet"):
                obj = BindRealServer()
                obj._deserialize(item)
                self.RealServerSet.append(obj)
        self.CreateTime = params.get("CreateTime")
        self.SessionPersist = params.get("SessionPersist")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            if name in memeber_set:
                memeber_set.remove(name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        